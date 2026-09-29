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
    static string gameDir = @"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure";

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
        Run("inline navigation policy", InlinePolicy);
        Run("inline-hosts.json matches the built RRT's entry lists", () => InlineHostsFresh(rrtDll));
        Run("derived keys force through their leaves", DerivedForcingChecks);
        Run("forced runs satisfy DelayHours by backdating hour.* times", DelayForcingChecks);
        Run("residence spike: plan, verdicts, report shape", ResidenceSpikeChecks);
        Run("residence spike: presence engine reflection vs built RRT DLL", () => ResidenceSpikeReflection(rrtDll));
        Run("presence spike: plan, verdicts, report shape", PresenceSpikeChecks);
        Run("presence spike: quiet-copy reflection vs built RRT DLL", () => PresenceSpikeReflection(rrtDll));
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

        // -Inline shape: the switch, an explicit hosts file and the click budget (clamped to 1).
        var inl = HarnessPlan.Parse(@"{ ""inline"": true, ""inlineHostsPath"": ""C:\\h\\inline-hosts.json"", ""maxInlineNavSteps"": 12, ""screenshots"": true }");
        Check(inl.Inline && inl.InlineHostsPath == @"C:\h\inline-hosts.json" && inl.MaxInlineNavSteps == 12 && inl.Screenshots, "inline plan fields parse");
        var inlc = HarnessPlan.Parse(@"{ ""inline"": true, ""inlineHostsPath"": "" "", ""maxInlineNavSteps"": 0 }");
        Check(inlc.InlineHostsPath == null && inlc.MaxInlineNavSteps == 1, "a blank hosts path means the default and the click budget is clamped to 1");

        var d = HarnessPlan.Parse("");
        Check(d.Saves.Count == 0 && !d.Force && !d.Dfs && d.ShouldReloadBetweenScenes && d.RoundTrip, "empty plan gives defaults");
        Check(!d.Screenshots && d.ScreenshotsPerScene == 3 && d.ScreenshotDir == null, "screenshots are off by default");
        Check(!d.Inline && d.InlineHostsPath == null && d.MaxInlineNavSteps == 40, "inline is off by default");

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

    // InlineHosts.Pick: the navigator's answer choice inside a host dialog.
    static void InlinePolicy()
    {
        var host = new InlineHost { Reachable = true, AnswerDist = { ["aaaa"] = 3, ["bbbb"] = 1, ["cccc"] = 1 } };
        InlineHosts.Shown A(string name, string guid, bool cont = false, bool exit = false, bool cond = false) =>
            new InlineHosts.Shown { Name = name, Guid = guid, IsContinue = cont, IsExit = exit, Conditioned = cond };
        var used = new Dictionary<string, int>();
        string why;
        var list = new List<InlineHosts.Shown> { A("Answer_1", "aaaa"), A("RRT_entry.x.y", "eeee"), A("Answer_2", "bbbb") };
        Check(InlineHosts.Pick(list, "RRT_entry.x.y", host, used, out why) == 1 && why == "entry", "the entry answer wins as soon as it is shown");
        Check(InlineHosts.Pick(list, "RRT_entry.x.z", host, used, out why) == 2, "otherwise the answer with the fewest clicks left");
        list = new List<InlineHosts.Shown> { A("Answer_2", "bbbb"), A("Answer_3", "CC-CC") };
        used["bbbb"] = 2;
        Check(InlineHosts.Pick(list, "e", host, used, out why) == 1, "ties go to the least used answer (guids compared without dashes or case)");
        list = new List<InlineHosts.Shown> { A("Exit", "x1", exit: true), A("Continue", "x2", cont: true) };
        Check(InlineHosts.Pick(list, "e", host, used, out why) == 1 && why == "continue", "Continue when no answer is on the resolved path");
        list = new List<InlineHosts.Shown> { A("Exit", "x1", exit: true), A("RRT_entry.other", "x3"), A("Answer_9", "x4", cond: true), A("Answer_8", "x5") };
        Check(InlineHosts.Pick(list, "e", host, used, out why) == 3, "off path: an unconditioned native answer, never Exit or another RRT answer");
        list = new List<InlineHosts.Shown> { A("Exit", "x1", exit: true), A("RRT_entry.other", "x3") };
        Check(InlineHosts.Pick(list, "e", host, used, out why) == -1, "only Exit or RRT answers: give up (skipped-inline)");
        Check(InlineHosts.EntryName("s.a", "0123abcd", false) == "RRT_entry.s.a" && InlineHosts.EntryName("s.a", "0123abcd", true) == "RRT_entry.s.a.0123abcd",
            "entry answer names (Main.Build / BuildReturnToList)");
        var hosts = InlineHosts.Parse(@"{ ""lists"": { ""l1"": { ""hosts"": [ { ""dialogName"": ""D0"", ""reachable"": false, ""reason"": ""r"" },
            { ""dialog"": ""dd"", ""dialogName"": ""D1"", ""reachable"": true, ""clicks"": 2 } ] }, ""l2"": { ""hosts"": [], ""reason"": ""parent list"" } },
            ""extra"": 1 }");
        var chosen = hosts.Choose(new[] { "l2", "L1", "l3" }, out var reason);
        Check(chosen != null && chosen.Value.List == "L1" && chosen.Value.Host.DialogName == "D1", "Choose takes the first list with a reachable host");
        Check(hosts.Choose(new[] { "l2", "l3" }, out reason) == null && reason!.Contains("parent list") && reason.Contains("stale"), "Choose explains an unresolved scene");
    }

    // The committed inline-hosts.json must list exactly the scenes the built RRT attaches to native lists (Rules.EntryTargets),
    // with the entry answer names the navigator looks for.
    static void InlineHostsFresh(string rrtDll)
    {
        string root = Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, @"..\..\..\..\.."));
        string hostsPath = Path.Combine(root, "harness", InlineHosts.FileName);
        Check(File.Exists(hostsPath), "inline-hosts.json exists at " + hostsPath);
        if (!File.Exists(hostsPath) || !File.Exists(rrtDll)) return;
        var hosts = InlineHosts.Parse(File.ReadAllText(hostsPath));
        var asm = Assembly.LoadFrom(rrtDll);
        if (RrtBridge.Validate(asm).Count > 0) return; // reported by the reflection check
        var bridge = new RrtBridge(asm);
        var storyType = asm.GetType("Tirabade.Story", true)!;
        var deserialize = Assembly.Load("Newtonsoft.Json").GetType("Newtonsoft.Json.JsonConvert", true)!
            .GetMethod("DeserializeObject", new[] { typeof(string), typeof(Type) })!;
        object story = deserialize.Invoke(null, new object[] { File.ReadAllText(Path.Combine(root, "development", "Story.json")), storyType })!;
        var scenes = (System.Collections.IList)storyType.GetField("Scenes")!.GetValue(story)!;
        int withEntry = 0, mismatched = 0;
        foreach (var scene in scenes)
        {
            string id = RrtBridge.SceneId(scene!);
            string[] live;
            try { live = bridge.EntryTargets(scene!); } catch (InvalidOperationException) { live = new string[0]; }
            hosts.Scenes.TryGetValue(id, out var known);
            var offline = known?.Lists ?? new List<string>();
            if (live.Length > 0) withEntry++;
            if (!live.SequenceEqual(offline))
            {
                if (mismatched++ < 5) Fail(id + ": EntryTargets [" + string.Join(",", live) + "] but inline-hosts.json has [" + string.Join(",", offline) + "]");
                continue;
            }
            if (known == null) continue;
            bool rtl = RrtBridge.SceneReturnToList(scene!);
            foreach (var l in known.Lists)
                if (!known.Entry.TryGetValue(l, out var name) || name != InlineHosts.EntryName(id, l, rtl))
                    Fail(id + ": inline-hosts.json entry answer " + name + " differs from " + InlineHosts.EntryName(id, l, rtl));
        }
        Check(mismatched == 0, mismatched + " scene(s) with stale entry lists: rerun python harness/resolve-inline-hosts.py");
        Check(withEntry == hosts.Scenes.Count, "every scene in the hosts file has a live entry list (" + withEntry + " vs " + hosts.Scenes.Count + ")");
        Console.WriteLine("    " + withEntry + " scenes with a native entry; " + hosts.Scenes.Values.Count(s => s.Resolved) + " resolve to a host dialog");
        // Reachability: an inline-only scene has no other door, so its list must be shown by some native cue the navigator can reach.
        var stranded = hosts.Scenes.Where(kv => kv.Value.Kind != "dialog" && !kv.Value.Resolved).Select(kv => kv.Key).ToList();
        Check(stranded.Count == 0, stranded.Count + " inline-only scene(s) with no reachable host: " + string.Join(", ", stranded.Take(5)));
        // Regression: Audience_Areelu shows AnswersList_0030 from cues under CueSequence_0019, whose SequenceExit has no ParentAsset.
        Check(hosts.Scenes.TryGetValue("areelu.trickster.audience.notes", out var notes) && notes.Resolved
              && (string?)notes.Host?["dialogName"] == "Audience_Areelu_c4_dialog",
              "areelu.trickster.audience.notes resolves to Audience_Areelu_c4_dialog (SequenceExit -> CueSequence parent)");
    }

    static void DerivedForcingChecks()
    {
        // Synthetic map: nested keys, persistent-only groups preferred, cycles and unforceable keys rejected.
        var d = new Dictionary<string, string[][]>
        {
            ["any"] = new[] { new[] { "native.x" }, new[] { "a.eligible" }, new[] { "b.eligible" } },
            ["a.eligible"] = new[] { new[] { "native.y", "a.committed" } },
            ["b.eligible"] = new[] { new[] { "b.committed" }, new[] { "b.late" } },
            ["loop"] = new[] { new[] { "loop2" } },
            ["loop2"] = new[] { new[] { "loop" } },
        };
        Func<string, bool> persistent = k => k.EndsWith(".committed") || k.EndsWith(".late");
        var none = new HashSet<string>();
        var leaves = DerivedForcing.Leaves("any", d, persistent, none.Contains);
        Check(leaves != null && leaves.SequenceEqual(new[] { "b.committed" }), "any resolves through b.eligible's first persistent group: " + (leaves == null ? "null" : string.Join(",", leaves)));
        Check(DerivedForcing.Leaves("a.eligible", d, persistent, none.Contains) == null, "a group with a native leaf is not forceable");
        Check(DerivedForcing.Leaves("loop", d, persistent, none.Contains) == null, "a cycle resolves to null, not a stack overflow");
        Check(DerivedForcing.Leaves("any", d, persistent, new HashSet<string> { "any" }.Contains)!.Count == 0, "a held key needs nothing");

        // The built Story.json: household.any_eligible must resolve to authored commit flags.
        string root = Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, @"..\..\..\..\.."));
        string storyPath = Path.Combine(root, "development", "Story.json");
        if (!File.Exists(storyPath)) { Fail("Story.json missing at " + storyPath); return; }
        var story = Newtonsoft.Json.Linq.JObject.Parse(File.ReadAllText(storyPath));
        var derived = new Dictionary<string, string[][]>();
        foreach (var p in (Newtonsoft.Json.Linq.JObject?)story["Derived"] ?? new Newtonsoft.Json.Linq.JObject())
            derived[p.Key] = p.Value!.Select(g => g.Select(x => (string)x!).ToArray()).ToArray();
        var authored = new HashSet<string>(story["Scenes"]!.SelectMany(s => s["Nodes"]!).SelectMany(n => n["Choices"] ?? new Newtonsoft.Json.Linq.JArray())
            .SelectMany(c => c["Set"] ?? new Newtonsoft.Json.Linq.JArray()).Select(x => (string)x!));
        Check(derived.ContainsKey("household.any_eligible"), "household.any_eligible is a Derived key");
        var real = DerivedForcing.Leaves("household.any_eligible", derived, authored.Contains, none.Contains);
        Check(real != null && real.Count > 0 && real.All(authored.Contains), "household.any_eligible resolves to authored flags: " + (real == null ? "null" : string.Join(",", real)));
        if (real != null) Console.WriteLine("    household.any_eligible forces via [" + string.Join(", ", real) + "]");
    }

    // Mirrors Rules.Available's delay test: the latest recorded time of the held keys, untimed keys ignored.
    static bool DelayPasses(int delay, int hour, IDictionary<string, int> times, IEnumerable<string> keys)
    {
        var timed = keys.Where(times.ContainsKey).Select(k => times[k]).ToList();
        return hour - (timed.Count == 0 ? hour - delay : timed.Max()) >= delay;
    }

    static void DelayForcingChecks()
    {
        // Live case (chadali.trickster.council.orange, 24 h): the latch trickster.ever is stamped "now" at load and the
        // forced flag chadali.trickster.primed has no time yet. Both get backdated to hour - 24 - margin.
        int hour = 1500;
        var keys = new[] { "trickster.ever", "chadali.trickster.primed" };
        var times = new Dictionary<string, int> { ["trickster.ever"] = hour };
        Check(!DelayPasses(24, hour, times, keys), "precondition: a latch stamped now blocks a 24 h page");
        var r = DelayForcing.Plan(24, hour, times, keys, _ => true);
        Check(r.Unmet == null && r.TargetHour == hour - 24 - DelayForcing.MarginHours, "target is hour - delay - margin: " + r.TargetHour);
        Check(r.Backdate.SequenceEqual(keys), "both the stamped latch and the untimed forced flag are backdated: " + string.Join(",", r.Backdate));
        foreach (var k in r.Backdate) times[k] = r.TargetHour;
        Check(DelayPasses(24, hour, times, keys), "after backdating, the Rules delay test passes");
        // Later stamping of the untimed key would still be old enough: it now carries the backdated time.
        Check(DelayPasses(24, hour + 1, times, keys), "the margin survives an hour boundary");

        // A key already old enough is left alone; no delay needs nothing.
        var old = new Dictionary<string, int> { ["a"] = hour - 200 };
        Check(DelayForcing.Plan(96, hour, old, new[] { "a" }, _ => true).Backdate.Count == 0, "a time already past delay + margin is not touched");
        Check(DelayForcing.Plan(0, hour, times, keys, _ => true).Backdate.Count == 0, "DelayHours 0 backdates nothing");

        // Cannot be satisfied: the save is younger than the delay, or a blocking time has no hour.* flag.
        var young = DelayForcing.Plan(96, 50, new Dictionary<string, int> { ["x"] = 49 }, new[] { "x" }, _ => true);
        Check(young.Unmet != null && young.Backdate.Count == 0, "a save younger than the delay is unmet (skipped-delay): " + young.Unmet);
        var noFlag = DelayForcing.Plan(48, hour, new Dictionary<string, int> { ["native"] = hour - 1 }, new[] { "native" }, _ => false);
        Check(noFlag.Unmet != null, "a blocking time with no settable hour.* flag is unmet");
        var untimedNoFlag = DelayForcing.Plan(48, hour, new Dictionary<string, int>(), new[] { "native" }, _ => false);
        Check(untimedNoFlag.Unmet == null && untimedNoFlag.Backdate.Count == 0, "an untimed key with no hour.* flag does not block");

        // The built Story.json: the scenes seen live as false entry-hidden carry DelayHours and the latch trickster.ever.
        string root = Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, @"..\..\..\..\.."));
        string storyPath = Path.Combine(root, "development", "Story.json");
        if (!File.Exists(storyPath)) { Fail("Story.json missing at " + storyPath); return; }
        var story = JObject.Parse(File.ReadAllText(storyPath));
        var latches = new HashSet<string>(((JObject?)story["Latches"] ?? new JObject()).Properties().Select(p => p.Name));
        foreach (var id in new[] { "anevia.trickster.gone.gate", "chadali.trickster.council.orange", "delamere.trickster.woods.second_hunt" })
        {
            var s = story["Scenes"]!.FirstOrDefault(x => (string?)x["Id"] == id);
            if (s == null) { Fail(id + " missing from Story.json"); continue; }
            var req = s["Requires"]!.Select(x => (string)x!).ToArray();
            int delay = (int)s["DelayHours"]!;
            Check(delay > 0 && req.Any(latches.Contains), id + " has DelayHours and a latched Requires");
            var t = new Dictionary<string, int>();
            foreach (var k in req.Where(latches.Contains)) t[k] = hour;
            var plan = DelayForcing.Plan(delay, hour, t, req, _ => true);
            foreach (var k in plan.Backdate) t[k] = plan.TargetHour;
            Check(plan.Unmet == null && DelayPasses(delay, hour, t, req), id + " delay is satisfied after backdating");
        }
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

    static void ResidenceSpikeChecks()
    {
        // Opt-in: a plan without "spike" is a normal run and its report carries no spike keys.
        var normal = HarnessPlan.Parse("{\"saves\":[\"a\"]}");
        Check(normal.Spike == null && normal.Residence == null && !normal.ResidenceSpike, "no spike by default");
        var plain = new HarnessReport { Plan = normal, Status = "complete" };
        plain.Saves.Add(new SaveReport { Save = "a", LoadOk = true });
        var pj = JObject.Parse(plain.ToJson());
        Check(pj["Plan"]?["Spike"] == null && pj["Plan"]?["Residence"] == null && pj["Saves"]?[0]?["Residence"] == null,
            "a normal report has no Spike/Residence keys (unchanged shape)");

        var sp = HarnessPlan.Parse("{\"spike\":\"Residence\"}");
        Check(sp.ResidenceSpike && sp.Residence != null && sp.Residence.EnterPoint == ResidenceSpikePlan.EnterNative
            && sp.Residence.Units.Count == 3 && sp.Residence.Seat.Length == 4, "spike residence fills the default settings");
        var custom = HarnessPlan.Parse("{\"spike\":\"residence\",\"residence\":{\"units\":[\"B5E867E1-3503-C6F4-1BB1-316705EFB4A2\"],\"seat\":[1,0,2,90]}}");
        Check(custom.Residence!.Units.Single() == "b5e867e13503c6f41bb1316705efb4a2" && custom.Residence.Seat[3] == 90f, "custom units are normalized and the seat parses");
        bool threw = false;
        try { HarnessPlan.Parse("{\"spike\":\"tavern\"}"); } catch (FormatException) { threw = true; }
        Check(threw, "an unknown spike is rejected");
        threw = false;
        try { HarnessPlan.Parse("{\"residence\":{}}"); } catch (FormatException) { threw = true; }
        Check(threw, "residence settings without spike residence are rejected");
        threw = false;
        try { HarnessPlan.Parse("{\"spike\":\"residence\",\"residence\":{\"seat\":[1,2]}}"); } catch (FormatException) { threw = true; }
        Check(threw, "a seat without four numbers is rejected");

        Check(ResidenceSpikePlan.ClassifyPreset(new string[0]) == "base", "no addon mechanics is the base area");
        Check(ResidenceSpikePlan.ClassifyPreset(new[] { ResidenceSpikePlan.MechanicsNoCouncil }) == "NoCouncil", "NoCouncil preset set");
        Check(ResidenceSpikePlan.ClassifyPreset(new[] { ResidenceSpikePlan.MechanicsNoCouncil, ResidenceSpikePlan.MechanicsCouncil1.ToUpperInvariant() }) == "Default", "Default preset set, case-insensitive");
        Check(ResidenceSpikePlan.ClassifyPreset(new[] { ResidenceSpikePlan.MechanicsCouncil1, ResidenceSpikePlan.MechanicsCouncilFight }) == "other", "a fight set is other");

        ResidenceSpikeResult Green() => new ResidenceSpikeResult
        {
            EntryStarted = true, AreaLoaded = true, Preset = "NoCouncil", ActiveMechanicsGuids = { ResidenceSpikePlan.MechanicsNoCouncil },
            Presence = new PresenceProbe { Spawned = true, Exists = true, HasView = true, ViewActive = true, Rendered = true, Pathed = true, PathMovedMetres = 4.7, DialogStarted = true, Removed = true },
        };
        var g = Green(); g.Evaluate(true, 2f);
        Check(g.Passed && g.EntryOk && g.PresetOk && g.PresenceOk && g.Findings.Count == 0, "an all-green spike passes");
        var fight = Green(); fight.Preset = "other"; fight.ActiveMechanicsGuids.Add(ResidenceSpikePlan.MechanicsCouncilFight);
        fight.NativeActions.Add("ShowPartySelection: Show party selection (in TricksterCouncil)"); fight.Evaluate(true, 2f);
        Check(!fight.Passed && fight.EntryOk && !fight.PresetOk && fight.PresenceOk
            && fight.Findings.Any(f => f.Contains("CouncilFight")) && fight.Findings.Any(f => f.Contains("ShowPartySelection")), "CouncilFight mechanics and a party selection fail (b) only");
        var noEntry = new ResidenceSpikeResult { EntryError = "the load did not start within 30 s" }; noEntry.Evaluate(false, 2f);
        Check(!noEntry.Passed && !noEntry.EntryOk && noEntry.Findings.Single().StartsWith("(a)"), "no entry fails (a) and skips the rest");
        var hidden = Green(); hidden.Presence.Rendered = false; hidden.Evaluate(false, 2f);
        Check(hidden.Passed, "rendering is informational without a rendered window");
        hidden.Evaluate(true, 2f);
        Check(!hidden.Passed && hidden.Findings.Any(f => f.Contains("renderer")), "rendering is required with screenshots");
        var still = Green(); still.Presence.Pathed = false; still.Presence.PathMovedMetres = 0.3; still.Evaluate(true, 2f);
        Check(!still.PresenceOk && still.Findings.Any(f => f.Contains("walked 0.3 m")), "a copy that does not walk fails (c)");

        var r = new HarnessReport { Status = "complete", Plan = sp };
        r.Init.RrtModFound = true; r.Init.Initialized = true;
        r.Saves.Add(new SaveReport { Save = "c6", LoadOk = true, Residence = fight });
        r.ComputeSummary();
        Check(!r.Summary.Passed && r.Summary.Failures.Any(f => f.StartsWith("c6: residence spike: (b)")), "a failed spike is a summary failure");
        var j = JObject.Parse(r.ToJson());
        Check((string?)j["Plan"]?["Spike"] == "Residence" && j["Saves"]?[0]?["Residence"]?["Findings"] != null, "the spike result is in the report");
        r.Saves[0].Residence = g; r.ComputeSummary();
        Check(r.Summary.Passed, "a green spike leaves the summary green");
    }

    static void PresenceSpikeChecks()
    {
        var normal = HarnessPlan.Parse("{\"saves\":[\"a\"]}");
        Check(normal.Presence == null && !normal.PresenceSpike, "no presence spike by default");
        var plain = new HarnessReport { Plan = normal, Status = "complete" };
        plain.Saves.Add(new SaveReport { Save = "a", LoadOk = true });
        var pj = JObject.Parse(plain.ToJson());
        Check(pj["Plan"]?["Presence"] == null && pj["Saves"]?[0]?["PresenceSpike"] == null, "a normal report has no presence spike keys");

        var sp = HarnessPlan.Parse("{\"spike\":\"Presence\"}");
        Check(sp.PresenceSpike && !sp.ResidenceSpike && sp.Residence == null && sp.Presence != null && sp.Presence.Units.Count == 4
            && sp.Presence.Units[0] == "397b090721c41044ea3220445300e1b8" && sp.Presence.EnterPoint == PresenceSpikePlan.EnterFromThroneRoom,
            "spike presence fills the default settings (Camellia's companion blueprint first)");
        var stay = HarnessPlan.Parse("{\"spike\":\"presence\",\"presence\":{\"enterPoint\":\"\",\"units\":[\"397B0907-21C4-1044-EA32-20445300E1B8\",\"397b090721c41044ea3220445300e1b8\"],\"observeSeconds\":0}}");
        Check(stay.Presence!.EnterPoint == null && stay.Presence.Units.Count == 1 && stay.Presence.ObserveSeconds >= 1, "custom presence settings normalize");
        bool threw = false;
        try { HarnessPlan.Parse("{\"presence\":{}}"); } catch (FormatException) { threw = true; }
        Check(threw, "presence settings without spike presence are rejected");
        threw = false;
        try { HarnessPlan.Parse("{\"spike\":\"presence\",\"presence\":{\"units\":[]}}"); } catch (FormatException) { threw = true; }
        Check(threw, "a presence spike without units is rejected");

        QuietCopyProbe Quiet() => new QuietCopyProbe { UnitName = "Camelia_Companion", Spawned = true, Exists = true, Faction = "Neutrals",
            Passive = true, AsksSilent = true, Asks = "PC_None_Barks", Removed = true };
        PresenceSpikeResult Green() => new PresenceSpikeResult { Area = "DrezenCapital", Copies = { Quiet() } };
        var g = Green(); g.Evaluate();
        Check(g.Passed && g.Findings.Count == 0, "an all-quiet presence spike passes");
        var loud = Green(); loud.Copies[0].PlayerFaction = true; loud.Copies[0].PartyGroup = true; loud.Copies[0].Passive = false;
        loud.Copies[0].AsksSilent = false; loud.Copies[0].Barks.Add("Camelia_BattleStart_01"); loud.Copies[0].InCombat = true; loud.Evaluate();
        Check(!loud.Passed && new[] { "Player faction", "party's unit group", "not passive", "voiced", "entered combat", "barked: Camelia_BattleStart_01" }
            .All(w => loud.Findings.Any(f => f.Contains(w))), "a companion copy as spawned natively fails every quiet check");
        var talk = Green(); talk.Dialogs.Add("Camelia_Companion_Dialog (speaker Camellia)"); talk.Evaluate();
        Check(!talk.Passed && talk.Findings.Single().StartsWith("dialogs started"), "a dialog started while watching fails");
        var none = new PresenceSpikeResult { Area = "DrezenCapital", Skipped = { "Seelah_NPC_Level1: a live unit of it is already in the area" } }; none.Evaluate();
        Check(!none.Passed && none.Findings.Single().StartsWith("no copy was spawned"), "a spike that spawned nothing fails");

        var r = new HarnessReport { Status = "complete", Plan = sp };
        r.Init.RrtModFound = true; r.Init.Initialized = true;
        r.Saves.Add(new SaveReport { Save = "c3", LoadOk = true, PresenceSpike = loud });
        r.ComputeSummary();
        Check(!r.Summary.Passed && r.Summary.Failures.Any(f => f.StartsWith("c3: presence spike: ")), "a failed presence spike is a summary failure");
        var j = JObject.Parse(r.ToJson());
        Check((string?)j["Plan"]?["Spike"] == "Presence" && j["Saves"]?[0]?["PresenceSpike"]?["Copies"] != null, "the presence spike result is in the report");
        r.Saves[0].PresenceSpike = g; r.ComputeSummary();
        Check(r.Summary.Passed, "a green presence spike leaves the summary green");
    }

    static void PresenceSpikeReflection(string rrtDll)
    {
        if (!File.Exists(rrtDll)) { Fail("built RRT DLL missing: " + rrtDll); return; }
        var asm = Assembly.LoadFrom(rrtDll);
        var problems = RrtBridge.Validate(asm, RrtBridge.PresenceSpikeExpectations);
        foreach (var p in problems) Fail(p);
        Console.WriteLine("    " + RrtBridge.PresenceSpikeExpectations.Length + " presence spike member expectations checked, " + problems.Count + " problem(s)");
        if (problems.Count > 0) return;
        var guest = new RrtBridge(asm).NewSpawnCopyPresence("harness.spike.presence.1", "397b090721c41044ea3220445300e1b8",
            PresenceSpikePlan.DrezenCapital, 0f, 0f, 0f, 0f, null!);
        Check(RrtBridge.PresenceQuiet(guest) == "None", "a fresh presence has applied no quiet repair");
    }

    static void ResidenceSpikeReflection(string rrtDll)
    {
        if (!File.Exists(rrtDll)) { Fail("built RRT DLL missing: " + rrtDll); return; }
        var asm = Assembly.LoadFrom(rrtDll);
        var problems = RrtBridge.Validate(asm, RrtBridge.SpikeExpectations);
        foreach (var p in problems) Fail(p);
        Console.WriteLine("    " + RrtBridge.SpikeExpectations.Length + " spike member expectations checked, " + problems.Count + " problem(s)");
        Check(RrtBridge.Validate(typeof(HarnessPlan).Assembly, RrtBridge.SpikeExpectations).Count == RrtBridge.SpikeExpectations.Length,
            "every spike expectation fails against the harness assembly");
        if (problems.Count > 0) return;
        // Build the presence through the bridge exactly as the spike does (the blueprint is only stored until the first tick).
        var bridge = new RrtBridge(asm);
        var guest = bridge.NewSpawnCopyPresence("harness.spike.residence", "b5e867e13503c6f41bb1316705efb4a2",
            ResidenceSpikePlan.CouncilArea, 0f, 0f, 3.92f, 180f, null!);
        Check(RrtBridge.PresenceSaveKey(guest) == "RanRomance.Tirabade.Presence.harness.spike.residence", "presence record key");
        Check(RrtBridge.PresenceStatus(guest) == "not observed" && RrtBridge.PresenceActor(guest) == null && RrtBridge.PresenceError(guest) == null,
            "a fresh presence is unobserved");
    }
}
