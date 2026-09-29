using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.CompilerServices;
using Newtonsoft.Json.Linq;
using RRT.TestHarness;

// Offline self-test: runs outside Unity. It loads the harness assembly and checks plan parsing,
// report writing, and the reflection lookups of RRT's private members against the built RRT DLL.
internal static class Program
{
    static int failures;
    static string gameDir = @"D:\SteamLibrary\steamapps\common\Pathfinder Second Adventure";

    static int Main(string[] args)
    {
        string rrtDll = args.Length > 0 ? args[0]
            : Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, @"..\..\..\..\..\src\bin\Release\net48\RanRomance.Tirabade.dll"));
        if (args.Length > 1) gameDir = args[1];
        string managed = Path.Combine(gameDir, "Wrath_Data", "Managed");
        AppDomain.CurrentDomain.AssemblyResolve += (_, e) =>
        {
            string name = new AssemblyName(e.Name).Name + ".dll";
            foreach (var dir in new[] { managed, Path.Combine(managed, "UnityModManager"), Path.GetDirectoryName(rrtDll)! })
            {
                string p = Path.Combine(dir, name);
                if (File.Exists(p)) return Assembly.LoadFrom(p);
            }
            return null;
        };
        Console.WriteLine("RRT harness self-test");
        Console.WriteLine("  harness: " + typeof(HarnessPlan).Assembly.Location);
        Console.WriteLine("  rrt:     " + rrtDll);
        Run("plan parsing", PlanParsing);
        Run("activation rule", Activation);
        Run("report writing", () => ReportWriting());
        Run("reflection lookups vs built RRT DLL", () => Reflection(rrtDll));
        Run("reflection validator rejects a wrong assembly", NegativeReflection);
        Run("capture and log filters", Filters);
        Console.WriteLine(failures == 0 ? "SELF-TEST PASSED" : "SELF-TEST FAILED: " + failures + " check(s)");
        return failures == 0 ? 0 : 1;
    }

    [MethodImpl(MethodImplOptions.NoInlining)]
    static void Run(string name, Action body)
    {
        int before = failures;
        try { body(); }
        catch (Exception ex) { Fail("unexpected " + ex.GetType().Name + ": " + ex.Message + "\n" + ex.StackTrace); }
        Console.WriteLine((failures == before ? "  PASS " : "  FAIL ") + name);
    }

    static void Check(bool condition, string what) { if (!condition) Fail(what); }
    static void Fail(string what) { failures++; Console.WriteLine("    x " + what); }

    static void PlanParsing()
    {
        var p = HarnessPlan.Parse(@"{ ""saves"": [""C:\\s\\a.zks"", "" b "", """"], ""force"": true, ""mode"": ""DFS"", ""seed"": 7,
            ""maxPathsPerScene"": 0, ""sceneFilter"": [""tirabade.""], ""timeouts"": { ""loadSeconds"": 42 } }");
        Check(p.Saves.SequenceEqual(new[] { @"C:\s\a.zks", "b" }), "saves trimmed and blanks dropped");
        Check(p.Force && p.Dfs && p.Seed == 7, "force/mode/seed");
        Check(p.MaxPathsPerScene == 1, "maxPathsPerScene clamped to 1");
        Check(p.Timeouts.LoadSeconds == 42 && p.Timeouts.StepSeconds == 15, "nested timeouts merge with defaults");
        Check(!p.ShouldReloadBetweenScenes, "force defaults to no reload between scenes");
        Check(p.IncludesScene("tirabade.first") && !p.IncludesScene("konomi.first"), "scene filter by prefix");

        // Exact shape emitted by run-harness.ps1 (ConvertTo-Json of the ordered plan).
        var ps = HarnessPlan.Parse(@"{ ""saves"": [ ""C:\\Saved Games\\Manual_1.zks"" ], ""force"": false, ""mode"": ""random"", ""seed"": 20,
            ""walksPerScene"": 1, ""maxPathsPerScene"": 8, ""maxScenesPerSave"": 0, ""sceneFilter"": [ ], ""roundTrip"": true,
            ""headless"": false, ""quitWhenDone"": true, ""timeouts"": { ""globalSeconds"": 2640 } }");
        Check(ps.Saves.Count == 1 && ps.RoundTrip && ps.QuitWhenDone && ps.Timeouts.GlobalSeconds == 2640 && ps.Timeouts.LoadSeconds == 300,
            "run-harness.ps1 plan shape parses");

        // -Screenshots shape: the switch, the per-scene cap and the run's shots folder (added after RunDir exists).
        var sh = HarnessPlan.Parse(@"{ ""saves"": [], ""headless"": false, ""screenshots"": true, ""screenshotsPerScene"": 4,
            ""screenshotDir"": ""C:\\runs\\x\\shots"" }");
        Check(sh.Screenshots && sh.ScreenshotsPerScene == 4 && sh.ScreenshotDir == @"C:\runs\x\shots", "screenshot plan fields parse");
        var shc = HarnessPlan.Parse(@"{ ""screenshots"": true, ""screenshotsPerScene"": -2, ""screenshotDir"": "" "" }");
        Check(shc.ScreenshotsPerScene == 0 && shc.ScreenshotDir == null, "screenshot cap clamped to 0 and a blank folder means the default");

        var d = HarnessPlan.Parse("");
        Check(d.Saves.Count == 0 && !d.Force && !d.Dfs && d.ShouldReloadBetweenScenes && d.RoundTrip, "empty plan gives defaults");
        Check(!d.Screenshots && d.ScreenshotsPerScene == 3 && d.ScreenshotDir == null, "screenshots are off by default");

        bool threw = false;
        try { HarnessPlan.Parse(@"{ ""savez"": [] }"); } catch (Exception) { threw = true; }
        Check(threw, "unknown key (typo) is rejected");
        threw = false;
        try { HarnessPlan.Parse(@"{ ""mode"": ""bfs"" }"); } catch (FormatException) { threw = true; }
        Check(threw, "bad mode is rejected");

        Check(HarnessPlan.ResolveSave("Manual_3_x", @"C:\Saved Games") == @"C:\Saved Games\Manual_3_x.zks", "relative save name resolves into Saved Games");
        Check(HarnessPlan.ResolveSave(@"D:\x\y.zks", @"C:\Saved Games") == @"D:\x\y.zks", "absolute save path kept");
    }

    // Screenshot scene guard and the AIVO audio-shim filter (internal statics, reached by reflection).
    static void Filters()
    {
        var asm = typeof(HarnessPlan).Assembly;
        var belongs = asm.GetType("RRT.TestHarness.HarnessRunner")!.GetMethod("ShotBelongs", BindingFlags.NonPublic | BindingFlags.Static)!;
        bool Belongs(string? cue, string scene) => (bool)belongs.Invoke(null, new object?[] { cue, scene })!;
        Check(Belongs("RRT_cue.chadali.trickster.epilogue.commit.start", "chadali.trickster.epilogue.commit"), "a cue of the walked scene is captured");
        Check(Belongs("RRT_cue.chadali.x.start.p2", "chadali.x"), "a paragraph cue of the walked scene is captured");
        Check(!Belongs("Cue_0012", "chadali.x") && !Belongs(null, "chadali.x"), "a native cue is not captured");
        Check(!Belongs("RRT_cue.chadali.xy.start", "chadali.x"), "a cue of another scene with a shared prefix is not captured");
        var benign = asm.GetType("RRT.TestHarness.LogCapture")!.GetMethod("BenignReason", BindingFlags.NonPublic | BindingFlags.Static, null, new[] { typeof(string), typeof(string) }, null)!;
        string? Benign(string m, string? st) => (string?)benign.Invoke(null, new object?[] { m, st });
        Check(Benign("[Audio] Failed to play sound evt_Anevia_Cue_0012 on DialogSpeaker", "AiVoiceoverMod.Patches.VoiceoverShim_Patch.TryPlayBankEvent") != null,
            "an AIVO-shim audio failure on a native cue is benign");
        Check(Benign("[Audio] Failed to play sound evt_Anevia_Cue_0012 on DialogSpeaker", "Kingmaker.Sound.SoundEventsManager.PostEvent") == null,
            "an audio failure outside the AIVO shim stays relevant-eligible");
        Check(Benign("NullReferenceException in DialogController", "AiVoiceoverMod.Patches.X") == null, "a non-audio error is never benign");
    }

    static void Activation()
    {
        string dir = Path.Combine(Path.GetTempPath(), "rrt-harness-selftest-" + Guid.NewGuid().ToString("N"));
        Directory.CreateDirectory(dir);
        try
        {
            Check(HarnessPlan.FindActivation(dir, _ => null, out _) == null, "inactive with no file and no env var");
            Check(HarnessPlan.FindActivation(dir, _ => "0", out _) == null, "inactive for a non-path env value");
            Check(HarnessPlan.FindActivation(dir, _ => "1", out var local) == "" && !local, "env var 1 activates the default plan");
            string plan = Path.Combine(dir, HarnessPlan.FileName);
            File.WriteAllText(plan, "{}");
            Check(HarnessPlan.FindActivation(dir, _ => null, out local) == plan && local, "plan file in mod folder activates");
            string other = Path.Combine(dir, "elsewhere.json");
            File.WriteAllText(other, "{}");
            File.Delete(plan);
            Check(HarnessPlan.FindActivation(dir, n => n == HarnessPlan.EnvVar ? other : null, out local) == other && !local, "env var path activates");
        }
        finally { Directory.Delete(dir, true); }
    }

    static void ReportWriting()
    {
        var r = new HarnessReport { PlanPath = "x" };
        r.Init.RrtModFound = true; r.Init.Initialized = true;
        var save = new SaveReport { Save = "a.zks", LoadOk = true, State = new SnapshotData { Chapter = 2, Flags = { "started" } } };
        var good = new SceneRun { Scene = "s1", Result = "completed", Passed = true, Choices = { new ChoiceTaken { Index = 0, Of = 2, Answer = "RRT_answer.s1.n.0" } } };
        var bad = new SceneRun { Scene = "s2", Result = "stuck", Passed = false,
            Exceptions = { new CapturedLog { Source = "unity", Severity = "Exception", Message = "NullReferenceException in Tirabade", StackTrace = "at Tirabade.Main.State()", Relevant = true } } };
        save.Runs.Add(good); save.Runs.Add(bad);
        save.RoundTrip = new RoundTripResult { Attempted = true, Passed = false, MissingAfterReload = { "started" } };
        r.Saves.Add(save);
        r.Status = "complete";
        r.ComputeSummary();
        Check(!r.Summary.Passed && r.Summary.Runs == 2 && r.Summary.RunsPassed == 1 && r.Summary.Choices == 1, "summary counts");
        Check(r.Summary.RelevantExceptions == 1 && r.Summary.RoundTripsFailed == 1, "summary exceptions and round trip");
        Check(r.Summary.Failures.Any(f => f.Contains("s2") && f.Contains("stuck")) && r.Summary.Failures.Any(f => f.Contains("missing flags started")), "failure lines");

        string path = Path.Combine(Path.GetTempPath(), "rrt-harness-selftest-" + Guid.NewGuid().ToString("N"), HarnessPlan.ReportFileName);
        try
        {
            r.Write(path);
            r.Write(path); // overwrite path must also work
            var j = JObject.Parse(File.ReadAllText(path));
            Check((string?)j["Status"] == "complete", "status serialized");
            Check((bool?)j["Summary"]?["Passed"] == false, "summary serialized");
            Check((string?)j["Saves"]?[0]?["Runs"]?[1]?["Exceptions"]?[0]?["StackTrace"] == "at Tirabade.Main.State()", "exception stack serialized");
            Check(j["Plan"]?["Dfs"] == null, "computed plan properties are not serialized");
            Check(!File.Exists(path + ".tmp"), "no temp file left behind");

            var ok = new HarnessReport { Status = "complete" };
            ok.Init.RrtModFound = true; ok.Init.Initialized = true;
            ok.Saves.Add(new SaveReport { Save = "b", LoadOk = true, Runs = { new SceneRun { Scene = "s", Result = "completed", Passed = true } } });
            ok.ComputeSummary();
            Check(ok.Summary.Passed, "all-green report passes");
            var running = new HarnessReport();
            running.Init.RrtModFound = true; running.Init.Initialized = true;
            running.ComputeSummary();
            Check(!running.Summary.Passed, "a running (unfinished) report never passes");
        }
        finally { Directory.Delete(Path.GetDirectoryName(path)!, true); }
    }

    static void Reflection(string rrtDll)
    {
        Check(File.Exists(rrtDll), "built RRT DLL exists at " + rrtDll);
        if (!File.Exists(rrtDll)) return;
        var asm = Assembly.LoadFrom(rrtDll);
        var problems = RrtBridge.Validate(asm);
        foreach (var p in problems) Fail(p);
        Console.WriteLine("    " + RrtBridge.Expectations.Length + " member expectations checked, " + problems.Count + " problem(s)");
        if (problems.Count > 0) return;
        // The runtime accessor constructor resolves every method it invokes.
        var bridge = new RrtBridge(asm);
        Check(bridge.Assembly == asm, "bridge constructed");
        // Info.json dependency sanity: the harness must load after the RRT id it reads.
        string info = File.ReadAllText(Path.Combine(AppContext.BaseDirectory, @"..\..\..\..\Info.json"));
        string rrtInfo = File.ReadAllText(Path.Combine(AppContext.BaseDirectory, @"..\..\..\..\..\package\Info.json"));
        string rrtId = (string)JObject.Parse(rrtInfo)["Id"]!;
        var harnessInfo = JObject.Parse(info);
        Check(harnessInfo["LoadAfter"]!.Values<string>().Contains(rrtId), "harness LoadAfter contains RRT id " + rrtId);
        Check((string?)harnessInfo["Id"] == "RRTTestHarness", "harness Id");
        Check((string?)harnessInfo["EntryMethod"] == "RRT.TestHarness.Entry.Load"
            && typeof(HarnessPlan).Assembly.GetType("RRT.TestHarness.Entry")?.GetMethod("Load") != null, "harness EntryMethod exists");
        Check((string?)JObject.Parse(rrtInfo)["AssemblyName"] == RrtBridge.AssemblyName + ".dll", "RRT AssemblyName matches bridge");
    }

    static void NegativeReflection()
    {
        var problems = RrtBridge.Validate(typeof(HarnessPlan).Assembly);
        Check(problems.Count == RrtBridge.Expectations.Length, "every expectation fails against the harness assembly (" + problems.Count + ")");
    }
}
