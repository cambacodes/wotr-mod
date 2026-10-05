using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using Newtonsoft.Json;

namespace RRT.TestHarness
{
    // Pure data: no Unity or game types, so the offline self-test can load it.
    public sealed class CapturedLog
    {
        public string Source = "";      // unity | owlcat | umm | finalizer | harness
        public string Severity = "";    // Error | Exception | Assert | Critical
        public string Message = "";
        public string? StackTrace;
        public double AtSeconds;
        public string? Context;         // save / scene / phase active when captured
        /// <summary>True when the entry is attributed to RRT or to the dialog system (counts as a failure).</summary>
        public bool Relevant;
    }

    public sealed class InitState
    {
        public bool RrtModFound;
        public bool RrtModActive;
        public bool RrtModErrorOnLoading;
        public string? RrtAssembly;
        public bool Initialized;
        public bool Enabled;
        public string? Error;
        public List<string> Degraded = new List<string>();
        public List<string> Warnings = new List<string>();
        public List<string> ReflectionProblems = new List<string>();
        /// <summary>E18: one line per Story.NativeGates gate, read off the real loaded blueprints ("MISSING ..." fails the run).</summary>
        public List<string> NativeGates = new List<string>();
        public int SceneCount;
        public int DialogCount;
        public bool BlueprintCacheSeen;
        public double MainMenuAtSeconds;
    }

    public sealed class SnapshotData
    {
        public int Chapter;
        public int Hour;
        public string Area = "";
        public List<string> Flags = new List<string>();
        public List<string> AvailableContacts = new List<string>();
        public Dictionary<string, int> Times = new Dictionary<string, int>();
    }

    public sealed class ChoiceTaken
    {
        public int Step;
        public int Index;
        public int Of;
        public string Answer = "";
        public string? Text;
        /// <summary>Story mapping "scene/node/choice" when the answer is an RRT story choice.</summary>
        public string? StoryChoice;
    }

    public sealed class SceneRun
    {
        public string Scene = "";
        public string Relationship = "";
        public bool AvailableAtStart;
        public bool Forced;
        public string Strategy = "";     // random:<seed> | dfs:<prefix>
        public List<int> Path = new List<int>();
        public List<ChoiceTaken> Choices = new List<ChoiceTaken>();
        /// <summary>completed | not-started | stuck | step-limit | exception | skipped | skipped-native (forced, gated on unforceable native keys)
        /// | skipped-inline (-Inline: the host dialog or its list could not be reached; not a failure) | entry-hidden | entry-not-started
        /// | skipped-delay (forced, but the scene's DelayHours cannot be satisfied by backdating from this save; not a failure)
        /// | skipped-forbidden (the save itself holds one of the scene's Forbids; the page is legitimately closed; not a failure)</summary>
        public string Result = "";
        public string? Detail;
        /// <summary>Forced runs of a DelayHours scene: the keys whose hour.* times were backdated, e.g. "trickster.ever@1203".</summary>
        public List<string> DelayBackdated = new List<string>();
        /// <summary>Set when a forced run could not satisfy the scene's DelayHours (see DelayForcing).</summary>
        public string? DelayUnmet;
        /// <summary>The scene's Forbids keys the save held before the run (the harness never sets them); non-empty makes a hidden page skipped-forbidden.</summary>
        public List<string> ForbiddenHeld = new List<string>();
        public bool CompletedFlagSet;
        public List<string> OracleFailures = new List<string>();
        public List<CapturedLog> Exceptions = new List<CapturedLog>();
        public List<string> FlagsAdded = new List<string>();
        public List<string> FlagsRemoved = new List<string>();
        public double Ms;
        public bool Passed;
        /// <summary>Screenshot PNG paths taken during this walk (plan.Screenshots only).</summary>
        public List<string> Screenshots = new List<string>();
        /// <summary>-Inline runs only: how the scene was reached through its native host.</summary>
        public InlineRun? Inline;
    }

    public sealed class InlineRun
    {
        public string Kind = "";          // dialog | return-cue | return-to-list (inline-hosts.json)
        public string? List;
        public string? Dialog;            // host BlueprintDialog name
        public string? Initiator;         // "unit <name>" (StartDialogWithUnit) | "main character" (StartDialogWithoutTarget)
        public string? EntryAnswer;
        public string? ResolvedPath;      // offline shortest path, for comparison with NavPath
        /// <summary>Each native click: "cue: answer [why]".</summary>
        public List<string> NavPath = new List<string>();
        public bool EntryShown;
        public bool SceneStarted;
    }

    public sealed class RoundTripResult
    {
        public bool Attempted;
        public string? AfterScene;
        public string? SkipReason;
        public string? SaveFile;
        public bool Saved;
        public bool Reloaded;
        public List<string> MissingAfterReload = new List<string>();
        public List<string> ExtraAfterReload = new List<string>();
        /// <summary>Informational: derived (live-state) flags that differ after reload; not a failure.</summary>
        public List<string> DerivedChanged = new List<string>();
        public bool ChapterMatches;
        public bool Passed;
        public double SaveMs;
        public double LoadMs;
        public bool Deleted;
    }

    public sealed class SaveReport
    {
        public string Save = "";
        public string ResolvedPath = "";
        public bool LoadOk;
        public string? LoadError;
        public double LoadMs;
        public string? GameMode;
        /// <summary>Set when the save loaded but never reached an idle state (cutscene, combat, native dialog).</summary>
        public string? NotIdle;
        public SnapshotData? State;
        public string? StateError;
        public List<string> AvailableScenes = new List<string>();
        public List<string> ScenesWithoutDialog = new List<string>();
        public int ScenesDriven;
        public int ChoicesTaken;
        public List<SceneRun> Runs = new List<SceneRun>();
        // BEGIN eng7-f5
        public List<NativeSlideResult> NativeSlides = new List<NativeSlideResult>();
        // END eng7-f5
        public RoundTripResult RoundTrip = new RoundTripResult();
        /// <summary>-Spike Residence only (omitted otherwise): the P2 residence feasibility spike for this save.</summary>
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)] public ResidenceSpikeResult? Residence;
        /// <summary>-Spike Presence only (omitted otherwise): the quiet-copy check or walkable mesh probe for this save.</summary>
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)] public PresenceSpikeResult? PresenceSpike;
        public List<CapturedLog> Exceptions = new List<CapturedLog>();
        public double TotalMs;
        public bool Passed;
    }

    public sealed class ReportSummary
    {
        public bool Passed;
        public int Saves;
        public int SavesLoaded;
        public int Runs;
        public int RunsPassed;
        public int Choices;
        public int RelevantExceptions;
        public int OracleFailures;
        public int RoundTripsPassed;
        public int RoundTripsFailed;
        public int SkippedInline;
        public List<string> Failures = new List<string>();
        // Saves that could not be exercised for reasons outside RRT (e.g. the save opens inside a native dialog).
        public List<string> Skipped = new List<string>();
    }

    public sealed class HarnessReport
    {
        public string Harness = "RRTTestHarness 0.1.0";
        /// <summary>running | complete | aborted</summary>
        public string Status = "running";
        public string? AbortReason;
        public DateTime StartedUtc = DateTime.UtcNow;
        public DateTime? FinishedUtc;
        public double ElapsedSeconds;
        public string? PlanPath;
        public HarnessPlan Plan = new HarnessPlan();
        public InitState Init = new InitState();
        public List<SaveReport> Saves = new List<SaveReport>();
        /// <summary>Errors captured outside any save (startup, main menu).</summary>
        public List<CapturedLog> GlobalExceptions = new List<CapturedLog>();
        public ReportSummary Summary = new ReportSummary();

        public void ComputeSummary()
        {
            var s = new ReportSummary { Saves = Saves.Count };
            // BEGIN eng7-f5
            if (Plan.NativeEpilogueSpike && Saves.Count == 0) s.Failures.Add("No save was exercised by the native slide probe.");
            // END eng7-f5
            if (!Init.RrtModFound) s.Failures.Add("RRT mod RanRomanceTirabade not found by UMM.");
            if (!Init.Initialized) s.Failures.Add("Tirabade.Main did not initialize" + (Init.Error != null ? ": " + Init.Error : "."));
            if (Init.ReflectionProblems.Count > 0) s.Failures.Add("Reflection lookups failed: " + string.Join("; ", Init.ReflectionProblems));
            foreach (var gate in Init.NativeGates)
                if (gate.StartsWith("MISSING", StringComparison.Ordinal)) s.Failures.Add("Native gate not attached: " + gate);
            foreach (var save in Saves)
            {
                if (save.LoadOk) s.SavesLoaded++;
                else s.Failures.Add(save.Save + ": load failed: " + save.LoadError);
                if (save.StateError != null) s.Failures.Add(save.Save + ": State() failed: " + save.StateError);
                // A save that opens inside a native (non-RRT) dialog or cutscene cannot be driven; that is a save choice, not a defect.
                bool nativeHold = save.NotIdle != null && save.NotIdle.StartsWith("dialog open:", StringComparison.Ordinal)
                    && save.NotIdle.IndexOf("RRT_", StringComparison.Ordinal) < 0;
                if (nativeHold) s.Skipped.Add(save.Save + ": opens inside a native dialog (" + save.NotIdle + "); pick a save made in free roam");
                else if (save.NotIdle != null) s.Failures.Add(save.Save + ": loaded but never idle: " + save.NotIdle);
                foreach (var run in save.Runs)
                {
                    s.Runs++;
                    s.Choices += run.Choices.Count;
                    if (run.Result == "skipped-inline")
                    {
                        s.SkippedInline++;
                        s.Skipped.Add(save.Save + " / " + run.Scene + ": skipped-inline (" + run.Detail + ")");
                    }
                    if (run.Result == "skipped-delay" || run.Result == "skipped-forbidden") s.Skipped.Add(save.Save + " / " + run.Scene + ": " + run.Result + " (" + run.Detail + ")");
                    if (run.Passed) s.RunsPassed++;
                    else s.Failures.Add(save.Save + " / " + run.Scene + " [" + run.Strategy + "]: " + run.Result
                        + (run.Detail != null ? " (" + run.Detail + ")" : "")
                        + (run.OracleFailures.Count > 0 ? " oracle: " + string.Join("; ", run.OracleFailures) : "")
                        + (run.Exceptions.Any(e => e.Relevant) ? " exception: " + run.Exceptions.First(e => e.Relevant).Message : ""));
                    s.OracleFailures += run.OracleFailures.Count;
                    s.RelevantExceptions += run.Exceptions.Count(e => e.Relevant);
                }
                s.RelevantExceptions += save.Exceptions.Count(e => e.Relevant);
                if (save.RoundTrip.Attempted)
                {
                    if (save.RoundTrip.Passed) s.RoundTripsPassed++;
                    else
                    {
                        s.RoundTripsFailed++;
                        s.Failures.Add(save.Save + ": save round-trip failed"
                            + (save.RoundTrip.MissingAfterReload.Count > 0 ? "; missing flags " + string.Join(", ", save.RoundTrip.MissingAfterReload) : "")
                            + (save.RoundTrip.SkipReason != null ? "; " + save.RoundTrip.SkipReason : ""));
                    }
                }
                // -Spike Residence: a failed check is a feasibility finding (P3' fallback), reported like a test failure.
                if (save.Residence != null && !save.Residence.Passed)
                    s.Failures.Add(save.Save + ": residence spike: " + (save.Residence.Findings.Count > 0 ? string.Join("; ", save.Residence.Findings) : "not evaluated"));
                if (save.PresenceSpike != null && !save.PresenceSpike.Passed)
                    s.Failures.Add(save.Save + ": presence spike: " + (save.PresenceSpike.Findings.Count > 0 ? string.Join("; ", save.PresenceSpike.Findings) : "not evaluated"));
                // BEGIN eng7-f5: empty, truncated, stuck and exception probes cannot pass silently.
                if (Plan.NativeEpilogueSpike && save.NativeSlides.Count == 0) s.Failures.Add(save.Save + ": no native slide cases ran");
                if (Plan.NativeEpilogueSpike && save.Exceptions.Any(e => e.Relevant))
                    s.Failures.Add(save.Save + ": relevant exception during native slide probing: " + save.Exceptions.First(e => e.Relevant).Message);
                foreach (var slides in save.NativeSlides.Where(r => !r.Passed))
                    s.Failures.Add(save.Save + " / " + slides.Case + ": " + slides.Result + "; " + string.Join("; ", slides.Findings));
                // END eng7-f5
                save.Passed = save.LoadOk && save.StateError == null && save.NotIdle == null && save.Runs.All(r => r.Passed)
                    && !save.Exceptions.Any(e => e.Relevant) && (!save.RoundTrip.Attempted || save.RoundTrip.Passed)
                    && (save.Residence == null || save.Residence.Passed) && (save.PresenceSpike == null || save.PresenceSpike.Passed);
                // BEGIN eng7-f5
                save.Passed &= save.NativeSlides.All(r => r.Passed);
                // END eng7-f5
            }
            s.RelevantExceptions += GlobalExceptions.Count(e => e.Relevant);
            if (GlobalExceptions.Any(e => e.Relevant)) s.Failures.Add("Relevant errors outside any save: " + GlobalExceptions.First(e => e.Relevant).Message);
            if (Status == "aborted") s.Failures.Add("Harness aborted: " + AbortReason);
            s.Passed = s.Failures.Count == 0 && Status == "complete";
            Summary = s;
        }

        public string ToJson() => JsonConvert.SerializeObject(this, Formatting.Indented, new JsonSerializerSettings
        {
            NullValueHandling = NullValueHandling.Include,
            ReferenceLoopHandling = ReferenceLoopHandling.Ignore,
        });

        /// <summary>Atomic write (temp file + replace) so a reader never sees a half-written report.</summary>
        public void Write(string path)
        {
            string? dir = Path.GetDirectoryName(path);
            if (!string.IsNullOrEmpty(dir)) Directory.CreateDirectory(dir);
            string tmp = path + ".tmp";
            File.WriteAllText(tmp, ToJson(), new UTF8Encoding(false));
            if (File.Exists(path)) File.Delete(path);
            File.Move(tmp, path);
        }
    }
}
