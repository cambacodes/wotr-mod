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
        public HarnessTimeouts Timeouts = new HarnessTimeouts();

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

        public void Normalize()
        {
            Saves = (Saves ?? new List<string>()).Where(s => !string.IsNullOrWhiteSpace(s)).Select(s => s.Trim()).ToList();
            SceneFilter = (SceneFilter ?? new List<string>()).Where(s => !string.IsNullOrWhiteSpace(s)).ToList();
            Timeouts ??= new HarnessTimeouts();
            if (!Dfs && !string.Equals(Mode, "random", StringComparison.OrdinalIgnoreCase))
                throw new FormatException("Plan mode must be \"random\" or \"dfs\", not \"" + Mode + "\".");
            if (WalksPerScene < 1) WalksPerScene = 1;
            if (MaxPathsPerScene < 1) MaxPathsPerScene = 1;
            if (MaxStepsPerWalk < 1) MaxStepsPerWalk = 1;
            if (MaxScenesPerSave < 0) MaxScenesPerSave = 0;
            if (ScreenshotsPerScene < 0) ScreenshotsPerScene = 0;
            if (string.IsNullOrWhiteSpace(ScreenshotDir)) ScreenshotDir = null;
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
