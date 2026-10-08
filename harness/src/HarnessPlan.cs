using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Newtonsoft.Json;

namespace RRT.TestHarness
{
    // Pure data: no Unity or game types, so the offline self-test can load it.
    public sealed class HarnessTimeouts
    {
        public double MainMenuSeconds = 600;
        public double CacheSeconds = 180;
        public double LoadSeconds = 300;
        public double SaveSeconds = 120;
        public double IdleSeconds = 60;
        public double StepSeconds = 15;
        public double GlobalSeconds = 3600;
    }

    public sealed class HarnessPlan
    {
        public const string FileName = "rrt-harness-plan.json";
        public const string ReportFileName = "rrt-harness-report.json";
        public const string EnvVar = "RRT_HARNESS_PLAN";

        /// <summary>Absolute .zks paths, or file names inside the game's "Saved Games" folder.</summary>
        public List<string> Saves = new List<string>();
        /// <summary>Drive every scene that has an RRT dialog, not only the available ones.</summary>
        public bool Force;
        /// <summary>"random" (bounded seeded walk) or "dfs" (answer-index depth-first search, reload per branch).</summary>
        public string Mode = "random";
        public int Seed = 20;
        public int WalksPerScene = 1;
        public int MaxPathsPerScene = 8;
        public int MaxStepsPerWalk = 200;
        /// <summary>0 means unlimited.</summary>
        public int MaxScenesPerSave;
        /// <summary>Scene id or prefix filters; empty means all.</summary>
        public List<string> SceneFilter = new List<string>();
        /// <summary>Harness-only fixture flags, set after each source save load, before spikes or scene enumeration.</summary>
        public List<string> SetFlags = new List<string>();
        /// <summary>Harness-only BlueprintEtude GUIDs. Starts unstarted etudes; never resets completed etudes.</summary>
        public List<string> StartEtudes = new List<string>();
        public List<string> SetPresenceFailures = new List<string>(); // presence keys, harness-only transient observation
        public List<string> HoldEtudes = new List<string>(); // BlueprintEtude GUIDs, synthetic playing observation
        public List<string> SeenCues = new List<string>(); // BlueprintCueBase GUIDs, native dialog history
        public List<string> RemoveCompanions = new List<string>(); // BlueprintUnit GUIDs
        [JsonIgnore] public bool HasFixtureSetup => SetFlags.Count > 0 || StartEtudes.Count > 0
            || SetPresenceFailures.Count > 0 || HoldEtudes.Count > 0 || SeenCues.Count > 0 || RemoveCompanions.Count > 0;
        /// <summary>null: reload between scenes unless Force is set.</summary>
        public bool? ReloadBetweenScenes;
        public bool RoundTrip = true;
        public bool DeleteRoundTripSave = true;
        public bool Headless;
        /// <summary>Force mode only: set the scene's Requires flags before starting it.</summary>
        public bool ForceSetRequires = true;
        /// <summary>Mimic Tirabade.Main.Update: set the relationship's started flag before opening the dialog.</summary>
        public bool MarkStarted = true;
        public bool QuitWhenDone = true;
        public string? ReportPath;
        /// <summary>Capture a screenshot of each shown cue (after the dialog UI has bound it), up to ScreenshotsPerScene per walk.</summary>
        public bool Screenshots;
        public int ScreenshotsPerScene = 3;
        /// <summary>Folder for the PNGs (run-harness.ps1 passes the run's shots folder); null: persistentDataPath/RRTHarnessShots.</summary>
        public string? ScreenshotDir;
        /// <summary>
        /// Drive each scene that has a native entry (Rules.EntryTargets) through its host native dialog: start the host,
        /// click toward the answer list, select the RRT entry, then walk the scene. Scenes without a native entry are not driven.
        /// </summary>
        public bool Inline;
        /// <summary>inline-hosts.json from harness/resolve-inline-hosts.py; null: the file next to the harness DLL.</summary>
        public string? InlineHostsPath;
        /// <summary>Clicks allowed inside the host dialog before the list counts as unreachable (skipped-inline).</summary>
        public int MaxInlineNavSteps = 40;
        /// <summary>
        /// Opt-in feasibility spike, run after each save loads instead of driving scenes. "residence": the P2 harem residence
        /// spike (enter the Council Chamber, record its mechanics, spawn one presence copy there). "presence": the E12d quiet
        /// copy check (spawn companion copies in Drezen, force their barks, watch them), or a mesh query in the saved area.
        /// Null: a normal run.
        /// Omitted from the report when null, so a normal run's report is unchanged.
        /// </summary>
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)] public string? Spike;
        /// <summary>Settings of the residence spike; filled with defaults when Spike is "residence".</summary>
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)] public ResidenceSpikePlan? Residence;
        /// <summary>Settings of the presence quiet-copy spike or mesh probe; filled with defaults when Spike is "presence".</summary>
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)] public PresenceSpikePlan? Presence;
        // BEGIN eng7-f5: embedded fixture data keeps the Windows install self-contained.
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)] public string? NativeEpilogueCasesJson;
        [JsonIgnore] public bool NativeEpilogueSpike => string.Equals(Spike, "nativeepilogue", StringComparison.OrdinalIgnoreCase);
        // END eng7-f5
        public HarnessTimeouts Timeouts = new HarnessTimeouts();
        public string? SystemCasesJson;

        [JsonIgnore] public bool ResidenceSpike => string.Equals(Spike, "residence", StringComparison.OrdinalIgnoreCase);
        [JsonIgnore] public bool PresenceSpike => string.Equals(Spike, "presence", StringComparison.OrdinalIgnoreCase);

        [JsonIgnore] public bool Dfs => string.Equals(Mode, "dfs", StringComparison.OrdinalIgnoreCase);
        [JsonIgnore] public bool ShouldReloadBetweenScenes => ReloadBetweenScenes ?? !Force;

        public static HarnessPlan Parse(string json)
        {
            if (string.IsNullOrWhiteSpace(json)) return new HarnessPlan();
            var plan = JsonConvert.DeserializeObject<HarnessPlan>(json, new JsonSerializerSettings
            {
                MissingMemberHandling = MissingMemberHandling.Error,
                ObjectCreationHandling = ObjectCreationHandling.Replace,
            }) ?? new HarnessPlan();
            plan.Normalize();
            return plan;
        }

        static List<string> FixtureKeys(List<string>? values) => (values ?? new List<string>())
            .SelectMany(s => s.Split(',')).Select(s => s.Trim()).Where(s => s.Length > 0).Distinct(StringComparer.Ordinal).ToList();
        static List<string> FixtureGuids(List<string>? values, string field) => FixtureKeys(values).Select(s =>
        {
            if (!Guid.TryParse(s, out var guid)) throw new FormatException(field + " needs blueprint GUIDs: " + s);
            return guid.ToString("N");
        }).Distinct(StringComparer.Ordinal).ToList();

        public void Normalize()
        {
            Saves = (Saves ?? new List<string>()).Where(s => !string.IsNullOrWhiteSpace(s)).Select(s => s.Trim()).ToList();
            SceneFilter = (SceneFilter ?? new List<string>()).Where(s => !string.IsNullOrWhiteSpace(s)).ToList();
            SetFlags = (SetFlags ?? new List<string>()).SelectMany(s => s.Split(',')).Select(s => s.Trim()).Where(s => s.Length > 0).Distinct(StringComparer.Ordinal).ToList();
            StartEtudes = (StartEtudes ?? new List<string>()).SelectMany(s => s.Split(',')).Select(s => s.Trim()).Where(s => s.Length > 0).Select(s =>
            {
                if (!Guid.TryParse(s, out var guid)) throw new FormatException("startEtudes needs BlueprintEtude GUIDs: " + s);
                return guid.ToString("N");
            }).Distinct(StringComparer.Ordinal).ToList();
            SetPresenceFailures = FixtureKeys(SetPresenceFailures);
            HoldEtudes = FixtureGuids(HoldEtudes, "holdEtudes");
            SeenCues = FixtureGuids(SeenCues, "seenCues");
            RemoveCompanions = FixtureGuids(RemoveCompanions, "removeCompanions");
            Timeouts ??= new HarnessTimeouts();
            if (SystemCasesJson != null)
            {
                SystemCases.Parse(SystemCasesJson);
                if (Saves.Count == 0 || RoundTrip || Inline || Spike != null || HasFixtureSetup || SceneFilter.Count > 0)
                    throw new FormatException("System scenarios need saves, NoRoundTrip, no Inline/spike/filter/global fixture setup.");
            }
            if (!Dfs && !string.Equals(Mode, "random", StringComparison.OrdinalIgnoreCase))
                throw new FormatException("Plan mode must be \"random\" or \"dfs\", not \"" + Mode + "\".");
            if (WalksPerScene < 1) WalksPerScene = 1;
            if (MaxPathsPerScene < 1) MaxPathsPerScene = 1;
            if (MaxStepsPerWalk < 1) MaxStepsPerWalk = 1;
            if (MaxScenesPerSave < 0) MaxScenesPerSave = 0;
            if (ScreenshotsPerScene < 0) ScreenshotsPerScene = 0;
            if (string.IsNullOrWhiteSpace(ScreenshotDir)) ScreenshotDir = null;
            if (string.IsNullOrWhiteSpace(InlineHostsPath)) InlineHostsPath = null;
            if (MaxInlineNavSteps < 1) MaxInlineNavSteps = 1;
            if (string.IsNullOrWhiteSpace(Spike)) Spike = null;
            // BEGIN eng7-f5
            if (Spike != null && !ResidenceSpike && !PresenceSpike && !NativeEpilogueSpike)
                throw new FormatException("Plan spike must be residence, presence or nativeepilogue.");
            if (NativeEpilogueSpike)
            {
                if (Saves.Count == 0) throw new FormatException("Native epilogue probe needs a loadable save.");
                if (string.IsNullOrWhiteSpace(NativeEpilogueCasesJson)) throw new FormatException("Native epilogue probe needs serialized cases.");
                NativeSlideCases.Parse(NativeEpilogueCasesJson!);
                if (Inline || RoundTrip || Headless) throw new FormatException("Native epilogue probe needs NoRoundTrip, visible dialogs and no Inline.");
            }
            else if (NativeEpilogueCasesJson != null) throw new FormatException("Slide cases require nativeepilogue spike.");
            // END eng7-f5
            if (ResidenceSpike) (Residence ??= new ResidenceSpikePlan()).Normalize();
            else if (Residence != null) throw new FormatException("Plan residence settings need spike \"residence\".");
            if (PresenceSpike) (Presence ??= new PresenceSpikePlan()).Normalize();
            else if (Presence != null) throw new FormatException("Plan presence settings need spike \"presence\".");
        }

        public bool IncludesScene(string id) =>
            SceneFilter.Count == 0 || SceneFilter.Any(f => id == f || id.StartsWith(f, StringComparison.Ordinal));

        /// <summary>Resolves a plan save entry to an absolute path (does not check existence).</summary>
        public static string ResolveSave(string entry, string savedGamesFolder)
        {
            if (Path.IsPathRooted(entry)) return Path.GetFullPath(entry);
            string name = entry.EndsWith(".zks", StringComparison.OrdinalIgnoreCase) ? entry : entry + ".zks";
            return Path.GetFullPath(Path.Combine(savedGamesFolder, name));
        }

        /// <summary>
        /// Activation rule: the plan file in the mod folder, or the RRT_HARNESS_PLAN environment variable
        /// (a path to a plan file, or "1" for an init-only run with the default plan).
        /// Returns null when the harness must stay inactive.
        /// </summary>
        public static string? FindActivation(string modFolder, Func<string, string?> env, out bool fromModFolder)
        {
            fromModFolder = false;
            string local = Path.Combine(modFolder, FileName);
            if (File.Exists(local)) { fromModFolder = true; return local; }
            string? value = env(EnvVar);
            if (string.IsNullOrWhiteSpace(value)) return null;
            if (File.Exists(value)) return Path.GetFullPath(value);
            return value!.Trim() == "1" ? "" : null;
        }
    }
}
