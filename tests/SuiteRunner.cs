using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.Json;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using Tirabade;

internal static partial class Program
{
    private static string StoryArgument(string[] args)
    {
        var positional = new List<string>();
        for (int i = 0; i < args.Length; i++)
            if (args[i] == "--suites" || args[i] == "--routes") i++;
            else if (!args[i].StartsWith("--", StringComparison.Ordinal)) positional.Add(args[i]);
        return positional.Last();
    }
    // Diagnostics go to stderr, including in --bindings mode (stdout is JSON).
    private static readonly List<object> suiteTimings = new();
    private static double accountedSuiteSeconds;
    private static int accountedSuiteChecks;
    private static readonly HashSet<string> completedInWorkers = new();
    private static WorldBuildCache? worldBuilds;
    private static readonly HashSet<string> immutableRouteSuites = new() {
        "ArueshalaeTricksterTests", "ChadaliTricksterTests", "DelamereTricksterTests", "DevarraTricksterTests",
        "DorgelindaTricksterTests", "EritriceTricksterTests", "JannahTricksterTests", "KaylessaTricksterTests",
        "MielarahTricksterTests", "NenioTricksterTests"
    };
    internal static void CompleteWorld(Snapshot state)
    {
        if (worldBuilds == null) Rules.Complete(story, state);
        else worldBuilds.Complete(state);
    }
    internal static void RunSuite(string name, Action run)
    {
        if (completedInWorkers.Remove(name)) return;
        int before = checks;
        var timer = Stopwatch.StartNew();
        var previous = worldBuilds;
        worldBuilds = immutableRouteSuites.Contains(name) ? new WorldBuildCache(story) : null;
        try { run(); }
        finally
        {
            accountedSuiteSeconds += timer.Elapsed.TotalSeconds;
            accountedSuiteChecks += checks - before;
            suiteTimings.Add(new { suite = name, seconds = timer.Elapsed.TotalSeconds, assertions = checks - before,
                world_builds = worldBuilds?.Builds ?? 0, world_hits = worldBuilds?.Hits ?? 0 });
            worldBuilds = previous;
            if (Environment.GetEnvironmentVariable("RRT_TEST_PROFILE") == "1")
                Console.Error.WriteLine($"SUITE {name}: {timer.Elapsed.TotalSeconds:F3}s, {checks - before} assertions");
            string? output = Environment.GetEnvironmentVariable("RRT_TEST_TIMINGS");
            if (!string.IsNullOrEmpty(output))
                File.WriteAllText(output, JsonSerializer.Serialize(suiteTimings));
        }
    }

    private static void RecordInlineTiming(double elapsed)
    {
        suiteTimings.Add(new { suite = "OriginalCampaignAndStructure", seconds = Math.Max(0, elapsed - accountedSuiteSeconds),
            assertions = checks - accountedSuiteChecks, world_builds = 0, world_hits = 0 });
        string? output = Environment.GetEnvironmentVariable("RRT_TEST_TIMINGS");
        if (!string.IsNullOrEmpty(output)) File.WriteAllText(output, JsonSerializer.Serialize(suiteTimings));
    }

    private static void RunIndependentFull(string[] args)
    {
        // Opt in only for the unfiltered expansion preflight. Legacy modes and
        // bindings keep their original ordering and stdout contracts.
        string? setting = Environment.GetEnvironmentVariable("RRT_RULES_JOBS");
        if (args.Length != 1 || string.IsNullOrEmpty(setting) || setting == "1") return;
        if (!int.TryParse(setting, out int jobs) || jobs < 1 || jobs > 4)
            throw new ArgumentException("RRT_RULES_JOBS must be between 1 and 4");
        var candidates = new Dictionary<string, string> {
            ["ArueshalaeTricksterTests"] = "arueshalae.trickster.dead.starving",
            ["ChadaliTricksterTests"] = "chadali.trickster.council.coin",
            ["DelamereTricksterTests"] = "delamere.trickster.crypt.stag",
            ["DevarraTricksterTests"] = "devarra.trickster.dead.woken",
            ["DorgelindaTricksterTests"] = "dorgelinda.trickster.audit.open",
            ["EritriceTricksterTests"] = "eritrice.trickster.council.motion",
            ["JannahTricksterTests"] = "jannah.trickster.cage.terms",
            ["KaylessaTricksterTests"] = "kaylessa.trickster.dead.borrow",
            ["MielarahTricksterTests"] = "mielarah.trickster.tavern.arithmetic",
            ["NenioTricksterTests"] = "nenio.trickster.taken.riddle",
        };
        var ids = story.Scenes.Select(s => s.Id).ToHashSet();
        var selected = candidates.Where(p => ids.Contains(p.Value)).Select(p => p.Key).ToHashSet();
        if (selected.Count == 0) return;
        Rules.Validate(story);
        RunParallel(selected, StoryArgument(args), jobs);
        completedInWorkers.UnionWith(selected);
    }

    private static Dictionary<string, MethodInfo> SuiteMethods() => typeof(Program).Assembly.GetTypes()
        .Where(t => t.Name.EndsWith("Tests", StringComparison.Ordinal))
        .Select(t => (type: t, run: t.GetMethod("Run", BindingFlags.NonPublic | BindingFlags.Public | BindingFlags.Static)))
        .Where(p => p.run != null && (p.run.GetParameters().Select(v => v.ParameterType)
            .SequenceEqual(new[] { typeof(Action<bool, string>) }) || p.run.GetParameters().Select(v => v.ParameterType)
            .SequenceEqual(new[] { typeof(Story), typeof(Action<bool, string>) })))
        .ToDictionary(p => p.type.Name, p => p.run!, StringComparer.OrdinalIgnoreCase);

    private static string[] SelectorValues(string[] args, string option)
    {
        var values = new List<string>();
        for (int i = 0; i < args.Length; i++)
            if (args[i] == option)
            {
                if (++i >= args.Length || args[i].StartsWith("--")) throw new ArgumentException(option + " needs a value");
                values.AddRange(args[i].Split(',', StringSplitOptions.RemoveEmptyEntries));
            }
            else if (args[i].StartsWith(option + "=", StringComparison.Ordinal))
                values.AddRange(args[i].Substring(option.Length + 1).Split(',', StringSplitOptions.RemoveEmptyEntries));
        if (values.Count == 0) throw new ArgumentException(option + " cannot be empty");
        return values.ToArray();
    }

    private static bool RunSelected(string[] args)
    {
        bool bySuites = args.Any(a => a == "--suites" || a.StartsWith("--suites="));
        bool byRoutes = args.Any(a => a == "--routes" || a.StartsWith("--routes="));
        if (!bySuites && !byRoutes)
        {
            if (args.Any(a => a.StartsWith("--jobs", StringComparison.Ordinal)))
                throw new ArgumentException("--jobs requires --suites or --routes");
            return false;
        }
        if (bySuites && byRoutes) throw new ArgumentException("Use --suites or --routes, one selector at a time");
        if (args.Any(a => a.StartsWith("--") && a != "--suites" && a != "--routes"
            && !a.StartsWith("--suites=") && !a.StartsWith("--routes=") && !a.StartsWith("--jobs=")))
            throw new ArgumentException("Suite selectors cannot be combined with legacy focus flags");
        Rules.Validate(story);
        var methods = SuiteMethods();
        var selected = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
        if (bySuites) selected.UnionWith(SelectorValues(args, "--suites"));
        else
        {
            // Same conservative catalog as the shell gate, generated from the
            // checked-out test sources so added suites cannot disappear silently.
            var start = new ProcessStartInfo(Environment.GetEnvironmentVariable("RRT_PYTHON")
                ?? (OperatingSystem.IsWindows() ? "python" : "python3"))
                { RedirectStandardOutput = true, UseShellExecute = false };
            start.ArgumentList.Add("tools/test_selection.py"); start.ArgumentList.Add("--catalog");
            using var process = Process.Start(start)!;
            var catalog = JsonSerializer.Deserialize<Dictionary<string, string[]>>(process.StandardOutput.ReadToEnd())!;
            process.WaitForExit();
            if (process.ExitCode != 0) throw new Exception("Suite catalog failed");
            var routes = SelectorValues(args, "--routes");
            var known = catalog.Values.SelectMany(v => v).ToHashSet(StringComparer.OrdinalIgnoreCase);
            foreach (var route in routes) if (!known.Contains(route)) throw new ArgumentException("Unknown route: " + route);
            foreach (var pair in catalog)
                if (pair.Value.Length == 0 || pair.Value.Intersect(routes, StringComparer.OrdinalIgnoreCase).Any()) selected.Add(pair.Key);
        }
        foreach (var name in selected) if (!methods.ContainsKey(name)) throw new ArgumentException("Unknown suite: " + name);
        var jobsOption = args.Where(a => a.StartsWith("--jobs=", StringComparison.Ordinal)).ToArray();
        if (jobsOption.Length > 1) throw new ArgumentException("Specify --jobs once");
        int jobs = jobsOption.Length == 0 ? 1 : int.Parse(jobsOption[0].Substring("--jobs=".Length));
        if (jobs < 1 || jobs > 4) throw new ArgumentException("--jobs must be between 1 and 4");
        if (jobs > 1)
        {
            RunParallel(selected, StoryArgument(args), jobs);
            Console.WriteLine($"PASS: {checks} assertions in {selected.Count} selected suites.");
            return true;
        }
        foreach (var name in selected.OrderBy(v => v, StringComparer.Ordinal))
        {
            var method = methods[name];
            RunSuite(name, () => {
                try { method.Invoke(null, method.GetParameters().Length == 1
                    ? new object[] { (Action<bool, string>)Check } : new object[] { story, (Action<bool, string>)Check }); }
                catch (TargetInvocationException e) { throw e.InnerException ?? e; }
                var storyRun = method.DeclaringType!.GetMethod("RunStory", BindingFlags.NonPublic | BindingFlags.Public | BindingFlags.Static);
                if (storyRun != null)
                    try { storyRun.Invoke(null, new object[] { story, (Action<bool, string>)Check }); }
                    catch (TargetInvocationException e) { throw e.InnerException ?? e; }
            });
        }
        Console.WriteLine($"PASS: {checks} assertions in {selected.Count} selected suites.");
        return true;
    }

    private static void RunParallel(HashSet<string> selected, string storyPath, int jobs)
    {
        // Processes isolate Program.story, fixture mutations, evidence lists and
        // suite counters. Results are printed/merged in stable suite-name order.
        string scratch = Path.Combine(Path.GetTempPath(), "rrt-rule-suites-" + Guid.NewGuid().ToString("N"));
        Directory.CreateDirectory(scratch);
        var timer = Stopwatch.StartNew();
        int before = checks;
        try
        {
            var names = selected.OrderBy(v => v, StringComparer.Ordinal).ToArray();
            // A batch shares its parsed world across suites, just as the full
            // runner does; isolation is between workers, rather than a costly
            // new process and JSON parse for every small fixture.
            var batches = Enumerable.Range(0, Math.Min(jobs, names.Length))
                .Select(worker => names.Where((name, i) => i % jobs == worker).ToArray()).ToArray();
            var results = new (string output, string error, int code)[batches.Length];
            Parallel.For(0, batches.Length, new ParallelOptions { MaxDegreeOfParallelism = jobs }, i => {
                var start = new ProcessStartInfo("dotnet") { UseShellExecute = false, RedirectStandardOutput = true,
                    RedirectStandardError = true };
                start.ArgumentList.Add(typeof(Program).Assembly.Location);
                start.ArgumentList.Add("--suites=" + string.Join(",", batches[i]));
                start.ArgumentList.Add(Path.GetFullPath(storyPath));
                start.Environment["RRT_TEST_TIMINGS"] = Path.Combine(scratch, i + ".timings.json");
                start.Environment["RRT_NATIVE_COVERAGE_OUTPUT"] = Path.Combine(scratch, i + ".native.json");
                using var process = Process.Start(start)!;
                var output = process.StandardOutput.ReadToEndAsync(); var error = process.StandardError.ReadToEndAsync();
                process.WaitForExit();
                results[i] = (output.GetAwaiter().GetResult(), error.GetAwaiter().GetResult(), process.ExitCode);
            });
            for (int i = 0; i < batches.Length; i++)
            {
                Console.Write(results[i].output); Console.Error.Write(results[i].error);
                if (results[i].code != 0) throw new Exception("Selected suite batch failed: " + string.Join(",", batches[i]));
                var match = Regex.Match(results[i].output, @"PASS: (\d+) assertions in (\d+) selected suites\.");
                if (!match.Success || int.Parse(match.Groups[2].Value) != batches[i].Length)
                    throw new Exception("Selected batch omitted its assertion receipt");
                checks += int.Parse(match.Groups[1].Value);
                using var timings = JsonDocument.Parse(File.ReadAllText(Path.Combine(scratch, i + ".timings.json")));
                suiteTimings.AddRange(timings.RootElement.EnumerateArray().Select(v => (object)v.Clone()));
            }
            string? outputPath = Environment.GetEnvironmentVariable("RRT_TEST_TIMINGS");
            if (!string.IsNullOrEmpty(outputPath)) File.WriteAllText(outputPath, JsonSerializer.Serialize(suiteTimings));
            string? coveragePath = Environment.GetEnvironmentVariable("RRT_NATIVE_COVERAGE_OUTPUT");
            if (!string.IsNullOrEmpty(coveragePath))
            {
                var evaluations = new List<JsonElement>();
                string? hash = null;
                for (int i = 0; i < batches.Length; i++)
                {
                    string path = Path.Combine(scratch, i + ".native.json");
                    if (!File.Exists(path)) continue;
                    using var doc = JsonDocument.Parse(File.ReadAllText(path));
                    string current = doc.RootElement.GetProperty("StorySha256").GetString()!;
                    if (hash != null && hash != current) throw new Exception("Parallel suites used different exports");
                    hash = current;
                    evaluations.AddRange(doc.RootElement.GetProperty("Evaluations").EnumerateArray().Select(v => v.Clone()));
                }
                if (hash != null) File.WriteAllText(coveragePath, JsonSerializer.Serialize(new { StorySha256 = hash, Evaluations = evaluations }));
            }
        }
        finally
        {
            accountedSuiteSeconds += timer.Elapsed.TotalSeconds;
            accountedSuiteChecks += checks - before;
            Directory.Delete(scratch, recursive: true);
        }
    }
}
