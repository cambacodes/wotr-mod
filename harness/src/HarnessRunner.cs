using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using HarmonyLib;
using Kingmaker;
using Kingmaker.Controllers.Dialog;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.GameModes;
using Kingmaker.Settings;
using UnityEngine;
using UnityModManagerNet;

namespace RRT.TestHarness
{
    /// <summary>
    /// Drives the whole test run as a resumable step machine from MonoBehaviour.Update.
    /// Every game API used here is cited in harness/README.md with its decompiled signature.
    /// </summary>
    internal sealed class HarnessRunner : MonoBehaviour
    {
        sealed class Box<T> { public T Value = default!; }
        sealed class Wait { public float Seconds; public Wait(float s) { Seconds = s; } }
        sealed class Guarded { public IEnumerator Body; public Action<Exception> OnError; public Guarded(IEnumerator b, Action<Exception> e) { Body = b; OnError = e; } }
        sealed class Frame { public IEnumerator It = null!; public Action<Exception>? OnError; }

        HarnessReport report = null!;
        string reportPath = "";
        Harmony harmony = null!;
        HarnessPlan plan = null!;
        LogCapture capture = null!;
        RrtBridge? rrt;
        Dictionary<string, RrtBridge.ChoiceInfo> choices = new Dictionary<string, RrtBridge.ChoiceInfo>();
        HashSet<string> persistentFlagKeys = new HashSet<string>(StringComparer.Ordinal);
        readonly Stack<Frame> stack = new Stack<Frame>();
        readonly Stopwatch clock = Stopwatch.StartNew();
        float resumeAt;
        bool finished;
        static readonly FieldInfo? CuePlayScheduled = AccessTools.Field(typeof(DialogController), "m_CuePlayScheduled");

        internal void Configure(HarnessReport r, string path, Harmony h)
        {
            report = r; reportPath = path; harmony = h; plan = r.Plan;
            capture = LogCapture.Instance!;
            capture.Context = "startup";
            stack.Push(new Frame { It = Run() });
            TryWrite();
        }

        // ---- step machine -------------------------------------------------------------------------

        void Update()
        {
            if (finished || stack.Count == 0) return;
            if (clock.Elapsed.TotalSeconds > plan.Timeouts.GlobalSeconds) { Abort("global timeout of " + plan.Timeouts.GlobalSeconds + " s"); return; }
            if (Time.realtimeSinceStartup < resumeAt) return;
            // Run steps until one yields a frame or a wait; bounded to keep the frame responsive.
            for (int guard = 0; guard < 64 && stack.Count > 0; guard++)
            {
                var frame = stack.Peek();
                bool more;
                try { more = frame.It.MoveNext(); }
                catch (Exception ex)
                {
                    capture.Add("harness", "Exception", "Harness step failed: " + ex.GetType().Name + ": " + ex.Message, ex.ToString());
                    // Unwind to the nearest guarded frame.
                    while (stack.Count > 0 && stack.Peek().OnError == null) stack.Pop();
                    if (stack.Count == 0) { Abort("unhandled harness exception: " + ex.Message); return; }
                    var handler = stack.Pop().OnError!;
                    try { handler(ex); } catch (Exception hex) { Abort("error handler failed: " + hex.Message); return; }
                    continue;
                }
                if (!more) { stack.Pop(); if (stack.Count == 0) { Finish(); return; } continue; }
                switch (frame.It.Current)
                {
                    case Guarded g: stack.Push(new Frame { It = g.Body, OnError = g.OnError }); continue;
                    case IEnumerator e: stack.Push(new Frame { It = e }); continue;
                    case Wait w: resumeAt = Time.realtimeSinceStartup + w.Seconds; return;
                    default: return; // null: next frame
                }
            }
        }

        IEnumerator WaitFor(Func<bool> condition, double timeoutSeconds, Box<bool> ok, int stableFrames = 1)
        {
            var sw = Stopwatch.StartNew();
            int stable = 0;
            ok.Value = false;
            while (sw.Elapsed.TotalSeconds < timeoutSeconds)
            {
                bool c;
                try { c = condition(); } catch { c = false; }
                stable = c ? stable + 1 : 0;
                if (stable >= stableFrames) { ok.Value = true; yield break; }
                yield return null;
            }
        }

        // ---- game state ---------------------------------------------------------------------------

        static bool InMainMenu => Game.HasInstance && Game.Instance.UI.MainMenu != null;

        /// <summary>Null when the game is idle enough to open a dialog or save; otherwise the blocker.</summary>
        static string? IdleBlocker()
        {
            if (!Game.HasInstance) return "no Game instance";
            var g = Game.Instance;
            if (g.Player == null) return "no player";
            if (g.IsLoadingSave) return "IsLoadingSave";
            if (g.IsUnloading) return "IsUnloading";
            var lp = LoadingProcess.Instance;
            if (lp.IsLoadingInProcess) return "LoadingProcess.IsLoadingInProcess";
            if (lp.IsLoadingScreenActive) return "LoadingProcess.IsLoadingScreenActive";
            if (g.CurrentlyLoadedArea == null) return "no area loaded";
            if (g.UI.MainMenu != null) return "main menu";
            if (g.DialogController.Dialog != null) return "dialog open: " + g.DialogController.Dialog.name;
            if (g.Player.Dialog.Scheduled != null) return "dialog scheduled";
            if (g.Player.IsInCombat) return "in combat";
            if (g.IsPaused) { g.IsPaused = false; return "paused (unpausing)"; }
            var mode = g.CurrentMode;
            if (mode != GameModeType.Default && mode != GameModeType.GlobalMap) return "game mode " + mode;
            return null;
        }

        static string Mode() { try { return Game.HasInstance ? Game.Instance.CurrentMode.ToString() : "none"; } catch { return "?"; } }

        static SaveInfo? FindSave(string path)
        {
            var sm = Game.Instance.SaveManager;
            sm.UpdateSaveListIfNeeded(true);
            string full = Path.GetFullPath(path);
            var listed = sm.FirstOrDefault(s => s.FolderName != null
                && string.Equals(Path.GetFullPath(s.FolderName), full, StringComparison.OrdinalIgnoreCase));
            return listed ?? sm.LoadZipSave(full);
        }

        IEnumerator LoadSave(string path, Box<string?> error, Box<double> ms, Box<string?> notIdle)
        {
            error.Value = null; notIdle.Value = null;
            var sw = Stopwatch.StartNew();
            SaveInfo? info = null;
            try { info = FindSave(path); } catch (Exception ex) { error.Value = "cannot read save: " + ex.Message; }
            if (error.Value != null) yield break;
            if (info == null) { error.Value = "SaveManager.LoadZipSave returned null (broken or incompatible save)"; yield break; }
            if (!info.CheckDlcAvailable()) { error.Value = "save needs a DLC that is not available"; yield break; }
            capture.ResetRecent();
            if (InMainMenu) Game.Instance.UI.MainMenu.LoadGame(info);   // MainMenu.LoadGame -> EnterGame -> Game.LoadGameFromMainMenu
            else Game.Instance.LoadGame(info);                          // same call CommonUILoadService.Load makes in game
            var ok = new Box<bool>();
            yield return WaitFor(() => Game.Instance.IsLoadingSave || LoadingProcess.Instance.IsLoadingInProcess || LoadingProcess.Instance.IsLoadingScreenActive,
                30, ok);
            if (!ok.Value) { error.Value = "load did not start within 30 s (refused by Game.LoadGame)"; yield break; }
            yield return WaitFor(() => Game.HasInstance && !Game.Instance.IsLoadingSave && !LoadingProcess.Instance.IsLoadingInProcess
                && !LoadingProcess.Instance.IsLoadingScreenActive && Game.Instance.CurrentlyLoadedArea != null && Game.Instance.UI.MainMenu == null,
                plan.Timeouts.LoadSeconds, ok, 30);
            if (!ok.Value) { error.Value = "area not loaded within " + plan.Timeouts.LoadSeconds + " s (" + IdleBlocker() + ")"; yield break; }
            yield return WaitFor(() => IdleBlocker() == null, plan.Timeouts.IdleSeconds, ok, 60);
            if (!ok.Value) notIdle.Value = IdleBlocker() ?? "unstable";
            ms.Value = sw.Elapsed.TotalMilliseconds;
            yield return new Wait(1f);
        }

        // ---- run ---------------------------------------------------------------------------------

        IEnumerator Run()
        {
            var ok = new Box<bool>();
            yield return WaitFor(() => InMainMenu && !LoadingProcess.Instance.IsLoadingInProcess && !LoadingProcess.Instance.IsLoadingScreenActive,
                plan.Timeouts.MainMenuSeconds, ok, 30);
            if (!ok.Value) { Abort("main menu not reached within " + plan.Timeouts.MainMenuSeconds + " s"); yield break; }
            report.Init.MainMenuAtSeconds = Math.Round(clock.Elapsed.TotalSeconds, 1);
            // RRT builds its blueprints in a BlueprintsCache.Init postfix; the harness postfix runs after it.
            yield return WaitFor(() => Entry.CacheInitSeen || RrtSettled(), plan.Timeouts.CacheSeconds, ok);
            yield return new Wait(2f);
            RecordInit();
            TryWrite();

            string savedGames = Game.Instance.SaveManager.SavePath;
            for (int i = 0; i < plan.Saves.Count; i++)
            {
                var sr = new SaveReport { Save = plan.Saves[i], ResolvedPath = HarnessPlan.ResolveSave(plan.Saves[i], savedGames) };
                report.Saves.Add(sr);
                string prefix = "save:" + i + ":";
                var sw = Stopwatch.StartNew();
                yield return new Guarded(RunSave(sr, prefix), ex =>
                {
                    sr.LoadError ??= sr.LoadOk ? null : "harness exception: " + ex.Message;
                    sr.Exceptions.Add(new CapturedLog { Source = "harness", Severity = "Exception", Message = ex.Message, StackTrace = ex.ToString(), Relevant = true, Context = prefix });
                    TryStopDialog();
                });
                sr.TotalMs = sw.Elapsed.TotalMilliseconds;
                var all = capture.Since(0);
                sr.Exceptions.AddRange(all.Where(e => e.Context != null && e.Context.StartsWith(prefix, StringComparison.Ordinal)
                    && e.Context.IndexOf(":scene:", StringComparison.Ordinal) < 0));
                capture.Context = "between-saves";
                TryWrite();
            }
        }

        bool RrtSettled()
        {
            var asm = RrtBridge.FindLoaded();
            if (asm == null) return false;
            try
            {
                var main = asm.GetType("Tirabade.Main");
                bool init = (bool)main.GetField("initialized", BindingFlags.Static | BindingFlags.NonPublic).GetValue(null);
                object? err = main.GetField("error", BindingFlags.Static | BindingFlags.NonPublic).GetValue(null);
                return init || err != null;
            }
            catch { return false; }
        }

        void RecordInit()
        {
            var init = report.Init;
            init.BlueprintCacheSeen = Entry.CacheInitSeen;
            var entry = UnityModManager.FindMod(Entry.RrtId);
            init.RrtModFound = entry != null;
            init.RrtModActive = entry?.Active == true;
            init.RrtModErrorOnLoading = entry?.ErrorOnLoading == true;
            var asm = RrtBridge.FindLoaded() ?? entry?.Assembly;
            init.RrtAssembly = asm?.Location;
            if (asm == null) { init.ReflectionProblems.Add("assembly " + RrtBridge.AssemblyName + " is not loaded"); }
            else
            {
                init.ReflectionProblems.AddRange(RrtBridge.Validate(asm));
                if (init.ReflectionProblems.Count == 0)
                {
                    rrt = new RrtBridge(asm);
                    init.Initialized = rrt.Initialized;
                    init.Enabled = rrt.Enabled;
                    init.Error = rrt.Error;
                    init.Degraded = rrt.Degraded;
                    init.Warnings = rrt.Warnings;
                    if (rrt.Story != null)
                    {
                        init.SceneCount = rrt.Scenes.Count;
                        choices = rrt.ChoiceIndex();
                    }
                    init.DialogCount = rrt.Dialogs.Count;
                    persistentFlagKeys = new HashSet<string>(rrt.Flags.Keys.Cast<string>(), StringComparer.Ordinal);
                }
                LogCapture.PatchFinalizer(harmony, asm.GetType("Tirabade.Main+RouteCondition") is Type rc ? AccessTools.Method(rc, "CheckCondition") : null, init.ReflectionProblems, "RouteCondition.CheckCondition");
                LogCapture.PatchFinalizer(harmony, asm.GetType("Tirabade.Main+RouteAction") is Type ra ? AccessTools.Method(ra, "RunAction") : null, init.ReflectionProblems, "RouteAction.RunAction");
            }
            LogCapture.PatchFinalizer(harmony, AccessTools.Method(typeof(DialogController), nameof(DialogController.SelectAnswer)), init.ReflectionProblems, "DialogController.SelectAnswer");
            LogCapture.PatchFinalizer(harmony, AccessTools.Method(typeof(DialogController), nameof(DialogController.Tick)), init.ReflectionProblems, "DialogController.Tick");
            if (CuePlayScheduled == null) init.ReflectionProblems.Add("DialogController.m_CuePlayScheduled not found");
            if (plan.Headless) Game.Instance.DialogController.SetHeadlessMode(true);
        }

        IEnumerator RunSave(SaveReport sr, string prefix)
        {
            capture.Context = prefix + "load";
            if (!File.Exists(sr.ResolvedPath)) { sr.LoadError = "file not found: " + sr.ResolvedPath; yield break; }
            var err = new Box<string?>(); var ms = new Box<double>(); var notIdle = new Box<string?>();
            yield return LoadSave(sr.ResolvedPath, err, ms, notIdle);
            sr.LoadError = err.Value; sr.LoadOk = err.Value == null; sr.LoadMs = ms.Value; sr.GameMode = Mode();
            if (!sr.LoadOk) yield break;
            if (notIdle.Value != null) { sr.NotIdle = notIdle.Value; yield break; }
            if (rrt == null || !rrt.Initialized) { sr.StateError = "RRT not initialized; scenes skipped"; yield break; }

            object snapshot;
            try { snapshot = rrt.State(); sr.State = RrtBridge.ToData(snapshot); }
            catch (Exception ex) { sr.StateError = ex.GetType().Name + ": " + ex.Message; capture.Add("harness", "Exception", "State() threw", ex.ToString()); yield break; }

            var dialogs = rrt.Dialogs;
            var targets = new List<(object Scene, string Id, bool Available)>();
            foreach (var scene in rrt.Scenes)
            {
                string id = RrtBridge.SceneId(scene!);
                bool available;
                try { available = rrt.Available(scene!, snapshot); }
                catch (Exception ex) { capture.Add("harness", "Exception", "Rules.Available threw for " + id + " (Tirabade)", ex.ToString()); continue; }
                if (available) { sr.AvailableScenes.Add(id); if (!dialogs.Contains(id)) sr.ScenesWithoutDialog.Add(id); }
                if ((available || plan.Force) && dialogs.Contains(id) && plan.IncludesScene(id)) targets.Add((scene!, id, available));
            }
            if (plan.MaxScenesPerSave > 0) targets = targets.Take(plan.MaxScenesPerSave).ToList();

            bool dirty = false;
            // A forced run sets the scene's Requires, and any completed run records the scene and its choices. Without a
            // reload those flags leak into the next walk: a one-shot page reads as already shown, and a page that Forbids a
            // flag another forced page set (e.g. unpriced vs returned) never opens. So reload after any run that left state.
            bool leaked = false;
            var reloadErr = new Box<string?>(); var reloadMs = new Box<double>(); var reloadIdle = new Box<string?>();
            foreach (var target in targets)
            {
                var frontier = new Stack<List<int>>();
                frontier.Push(new List<int>());
                int paths = plan.Dfs ? plan.MaxPathsPerScene : plan.WalksPerScene;
                for (int k = 0; k < paths && (!plan.Dfs || frontier.Count > 0); k++)
                {
                    // DFS branches always need the pristine state; walks reload unless the plan says otherwise.
                    if (dirty && (plan.ShouldReloadBetweenScenes || plan.Dfs || leaked))
                    {
                        capture.Context = prefix + "reload";
                        yield return LoadSave(sr.ResolvedPath, reloadErr, reloadMs, reloadIdle);
                        if (reloadErr.Value != null || reloadIdle.Value != null)
                        {
                            sr.LoadError = "reload before " + target.Id + " failed: " + (reloadErr.Value ?? reloadIdle.Value);
                            yield break;
                        }
                        dirty = false;
                        leaked = false;
                        // A freshly loaded area keeps building its UI for a moment after the game reports idle.
                        yield return new WaitForSecondsRealtime(2f);
                    }
                    var run = new SceneRun { Scene = target.Id, Relationship = RrtBridge.SceneRelationship(target.Scene) };
                    List<int>? prefixPath = plan.Dfs ? frontier.Pop() : null;
                    System.Random? rng = plan.Dfs ? null : new System.Random(StableSeed(plan.Seed, target.Id, k));
                    run.Strategy = plan.Dfs ? "dfs:[" + string.Join(",", prefixPath!) + "]" : "random:" + plan.Seed + "/" + k;
                    var counts = new List<int>();
                    sr.Runs.Add(run);
                    capture.Context = prefix + "scene:" + target.Id;
                    yield return new Guarded(DriveScene(target.Scene, dialogs[target.Id]!, prefixPath, rng, run, counts), ex =>
                    {
                        run.Result = "exception";
                        run.Detail = "harness: " + ex.Message;
                        run.Exceptions.Add(new CapturedLog { Source = "harness", Severity = "Exception", Message = ex.Message, StackTrace = ex.ToString(), Relevant = true, Context = capture.Context });
                        TryStopDialog();
                    });
                    dirty = true;
                    leaked |= run.Forced || run.FlagsAdded.Count > 0;
                    sr.ScenesDriven += k == 0 ? 1 : 0;
                    sr.ChoicesTaken += run.Choices.Count;
                    if (plan.Dfs)
                    {
                        // Children of this path: every untried sibling at depths beyond the replayed prefix.
                        for (int d = Math.Min(counts.Count, run.Path.Count) - 1; d >= prefixPath!.Count; d--)
                            for (int alt = counts[d] - 1; alt >= 1; alt--)
                                frontier.Push(run.Path.Take(d).Concat(new[] { alt }).ToList());
                    }
                    if (plan.RoundTrip && !sr.RoundTrip.Attempted && sr.RoundTrip.SkipReason == null && run.Result == "completed")
                    {
                        capture.Context = prefix + "roundtrip";
                        yield return new Guarded(RoundTrip(sr.RoundTrip, target.Id), ex =>
                        {
                            sr.RoundTrip.Passed = false;
                            sr.RoundTrip.SkipReason = "harness exception: " + ex.Message;
                        });
                    }
                    TryWrite();
                }
            }
        }

        static int StableSeed(int seed, string id, int walk)
        {
            unchecked
            {
                uint h = 2166136261;
                foreach (char c in id) h = (h ^ c) * 16777619;
                return (int)(h ^ (uint)seed * 31u ^ (uint)walk * 7919u) & int.MaxValue;
            }
        }

        bool Ending(object scene) => RrtBridge.SceneOwner(scene).EndsWith("Epilogue", StringComparison.Ordinal);

        IEnumerator DriveScene(object scene, object dialogObj, List<int>? prefixPath, System.Random? rng, SceneRun run, List<int> counts)
        {
            var bridge = rrt!;
            var sw = Stopwatch.StartNew();
            int mark = capture.Mark();
            var ok = new Box<bool>();
            var unforceable = new List<string>();
            try
            {
                yield return WaitFor(() => IdleBlocker() == null, plan.Timeouts.IdleSeconds, ok, 5);
                if (!ok.Value) { run.Result = "not-started"; run.Detail = "game not idle: " + IdleBlocker(); yield break; }

                var before = bridge.State();
                var flagsBefore = RrtBridge.FlagSet(before);
                run.AvailableAtStart = bridge.Available(scene, before);
                if (!run.AvailableAtStart)
                {
                    run.Forced = true;
                    if (plan.ForceSetRequires)
                        foreach (var req in RrtBridge.SceneRequires(scene).Where(persistentFlagKeys.Contains)) bridge.Set(req);
                    // Native / derived world keys cannot be forced from a save; note them so a page that stays hidden is a skip.
                    unforceable = RrtBridge.SceneRequires(scene).Where(req => !persistentFlagKeys.Contains(req) && !flagsBefore.Contains(req)).ToList();
                    // RequiresAnyGroups: an unmet group is forced with its first persistent flag; a group with none is unforceable.
                    foreach (var group in RrtBridge.SceneRequiresAnyGroups(scene) ?? new string[0][])
                    {
                        if (group.Any(flagsBefore.Contains)) continue;
                        var pick = group.FirstOrDefault(persistentFlagKeys.Contains);
                        if (pick != null && plan.ForceSetRequires) bridge.Set(pick);
                        else if (pick == null) unforceable.Add("any-of [" + string.Join(", ", group) + "]");
                    }
                    // Nor can the chapter: a page gated on a later chapter cannot open from an earlier save.
                    int chapter = RrtBridge.ToData(before).Chapter;
                    if (chapter < RrtBridge.SceneMinChapter(scene) || chapter > RrtBridge.SceneMaxChapter(scene))
                        unforceable.Add("chapter " + chapter + " outside " + RrtBridge.SceneMinChapter(scene) + ".." + RrtBridge.SceneMaxChapter(scene));
                }
                if (plan.MarkStarted && bridge.StartedFlag(run.Relationship) is string started && persistentFlagKeys.Contains(started)) bridge.Set(started);

                var dc = Game.Instance.DialogController;
                dc.StartDialogWithoutTarget((BlueprintDialog)dialogObj, null);
                yield return WaitFor(() => dc.Dialog != null && dc.CurrentCue != null, 10, ok);
                if (!ok.Value)
                {
                    bool nativeGated = run.Forced && unforceable.Count > 0;
                    run.Result = nativeGated ? "skipped-native" : "not-started";
                    run.Detail = nativeGated ? "forced run cannot hold native/derived requires: " + string.Join(", ", unforceable)
                        : "dialog did not start within 10 s (mode " + Mode() + ", dialog " + (dc.Dialog?.name ?? "null") + ")";
                    yield break;
                }

                bool ending = Ending(scene);
                for (int step = 0; ; step++)
                {
                    yield return WaitFor(() => dc.Dialog == null
                        || (!IsCuePlayScheduled(dc) && dc.CurrentCue != null && dc.Answers.Any()), plan.Timeouts.StepSeconds, ok, 2);
                    if (!ok.Value)
                    {
                        run.Result = "stuck";
                        run.Detail = "no answers after " + plan.Timeouts.StepSeconds + " s at cue " + (dc.CurrentCue?.name ?? "null") + ", mode " + Mode();
                        break;
                    }
                    if (dc.Dialog == null) { run.Result = "completed"; break; }
                    if (step >= plan.MaxStepsPerWalk) { run.Result = "step-limit"; run.Detail = "exceeded " + plan.MaxStepsPerWalk + " selections"; break; }

                    // Let the dialog UI bind the current cue before answering: selecting within the bind frame races
                    // CueVM.GetCueText (NullReferenceException in DialogCueView.BindViewImplementation), a harness artefact.
                    // Poll: the same cue must have been current for 0.25 s real time AND 10 rendered frames (the first
                    // dialog after a save load builds its UI over several slow frames, so a fixed delay is not enough).
                    {
                        var shown = dc.CurrentCue;
                        int frame0 = Time.frameCount;
                        float time0 = Time.realtimeSinceStartup;
                        while (dc.Dialog != null && (Time.frameCount - frame0 < 10 || Time.realtimeSinceStartup - time0 < 0.25f))
                        {
                            yield return null;
                            if (dc.CurrentCue != shown) { shown = dc.CurrentCue; frame0 = Time.frameCount; time0 = Time.realtimeSinceStartup; }
                        }
                    }
                    if (dc.Dialog == null) { run.Result = "completed"; break; }
                    // Screenshots (plan.Screenshots): the cue is bound and on screen, so capture it before answering.
                    // Only a cue of the walked scene is captured: a walk that has continued into a native dialog (an epilogue
                    // handing back to the game, a native return) would otherwise photograph the wrong conversation.
                    if (plan.Screenshots && run.Screenshots.Count < plan.ScreenshotsPerScene)
                    {
                        if (dc.Dialog == (BlueprintDialog)dialogObj && ShotBelongs(dc.CurrentCue?.name, run.Scene)) yield return Screenshot(run, step);
                        else ShotFailed(run, "screenshot skipped at step " + step + ": current cue " + (dc.CurrentCue?.name ?? "null") + " is not a cue of " + run.Scene);
                    }
                    if (dc.Dialog == null) { run.Result = "completed"; break; }
                    var answers = dc.Answers.ToList();
                    counts.Add(answers.Count);
                    int index = prefixPath != null ? (step < prefixPath.Count ? prefixPath[step] : 0) : rng!.Next(answers.Count);
                    if (index >= answers.Count)
                    {
                        run.Result = "path-diverged";
                        run.Detail = "replayed path expects answer " + index + " but only " + answers.Count + " shown at step " + step;
                        break;
                    }
                    var answer = answers[index];
                    run.Path.Add(index);
                    var taken = new ChoiceTaken { Step = step, Index = index, Of = answers.Count, Answer = answer.name };
                    try { taken.Text = answer.DisplayText; } catch { }
                    choices.TryGetValue(answer.name ?? "", out var info);
                    taken.StoryChoice = info?.Label;
                    run.Choices.Add(taken);

                    // Oracle precondition: mirror RouteAction.RunAction's own guards (Main.cs).
                    bool expectEffects = false;
                    if (info != null)
                    {
                        var now = bridge.State();
                        bool continuation = !Ending(info.Scene) && (RrtBridge.SceneContactUnit(info.Scene) != null || bridge.IsRemote(info.Scene));
                        expectEffects = info.Revive == null && bridge.Match(info.Requires, info.Forbids, now)
                            && (!continuation || bridge.ContactAvailable(info.Scene, now));
                    }
                    dc.SelectAnswer(answer);
                    if (info != null && expectEffects)
                    {
                        var flags = RrtBridge.FlagSet(bridge.State());
                        var missing = info.Set.Where(f => !flags.Contains(f)).ToList();
                        if (missing.Count > 0) run.OracleFailures.Add(info.Label + ": Set flags not recorded after selection: " + string.Join(", ", missing));
                        if (info.Terminal && !Ending(info.Scene) && !flags.Contains(info.SceneId))
                            run.OracleFailures.Add(info.Label + ": terminal choice did not record completion flag '" + info.SceneId + "'");
                    }
                    yield return null;
                }

                if (dc.Dialog != null) TryStopDialog();
                yield return WaitFor(() => dc.Dialog == null && Game.Instance.CurrentMode != GameModeType.Dialog, 10, ok);
                var after = RrtBridge.FlagSet(bridge.State());
                run.FlagsAdded = after.Except(flagsBefore).OrderBy(x => x, StringComparer.Ordinal).ToList();
                run.FlagsRemoved = flagsBefore.Except(after).OrderBy(x => x, StringComparer.Ordinal).ToList();
                run.CompletedFlagSet = after.Contains(run.Scene);
                if (ending && run.Result == "completed") run.Detail = "epilogue scene: completion flag not expected";
            }
            finally
            {
                run.Ms = sw.Elapsed.TotalMilliseconds;
                run.Exceptions = capture.Since(mark);
                run.Passed = (run.Result == "completed" || run.Result == "skipped-native") && run.OracleFailures.Count == 0 && !run.Exceptions.Any(e => e.Relevant);
            }
        }

        static bool IsCuePlayScheduled(DialogController dc) => CuePlayScheduled != null && (bool)CuePlayScheduled.GetValue(dc);

        static void TryStopDialog()
        {
            try { if (Game.HasInstance && Game.Instance.DialogController.Dialog != null) Game.Instance.DialogController.StopDialog(); }
            catch (Exception ex) { LogCapture.Instance?.Add("harness", "Exception", "StopDialog failed: " + ex.Message, ex.ToString()); }
        }

        // Captures the rendered frame to <ScreenshotDir>/<scene>__<step>.png. ScreenCapture writes at the end of the frame, so
        // the file appears a frame or two later; wait up to 2 s real time for it. A failure is logged, never fails the run.
        // An RRT scene's cues are named RRT_cue.<scene>.<node> (paragraphs add .p<n>).
        internal static bool ShotBelongs(string? cueName, string sceneId) =>
            cueName != null && cueName.StartsWith("RRT_cue." + sceneId + ".", StringComparison.Ordinal);

        IEnumerator Screenshot(SceneRun run, int step)
        {
            // UnityModManager opens its window over the game in a normal-window run; close it so it is not captured.
            bool closed = false;
            try { var ui = UnityModManager.UI.Instance; if (ui != null && ui.Opened) { ui.ToggleWindow(false); closed = true; } }
            catch (Exception ex) { ShotFailed(run, "could not close the UnityModManager window: " + ex.Message); }
            if (closed) { yield return null; yield return null; }
            string? path = null;
            try
            {
                string dir = plan.ScreenshotDir ?? Path.Combine(Application.persistentDataPath, "RRTHarnessShots");
                Directory.CreateDirectory(dir);
                string stem = Safe(run.Scene) + "__" + step;
                path = Path.Combine(dir, stem + ".png");
                for (int n = 2; File.Exists(path); n++) path = Path.Combine(dir, stem + "_" + n + ".png");
                ScreenCapture.CaptureScreenshot(path);
            }
            catch (Exception ex) { ShotFailed(run, "screenshot failed: " + ex.Message); yield break; }
            float t0 = Time.realtimeSinceStartup;
            while (!File.Exists(path) && Time.realtimeSinceStartup - t0 < 2f) yield return null;
            if (File.Exists(path)) run.Screenshots.Add(path);
            else ShotFailed(run, "screenshot not written within 2 s: " + path);
        }

        static void ShotFailed(SceneRun run, string message) =>
            run.Exceptions.Add(new CapturedLog { Source = "harness", Severity = "Warning", Message = message, Relevant = false, Context = run.Scene });

        static string Safe(string id) => string.Concat(id.Select(ch => Path.GetInvalidFileNameChars().Contains(ch) ? '_' : ch));

        IEnumerator RoundTrip(RoundTripResult rt, string afterScene)
        {
            var bridge = rrt!;
            var ok = new Box<bool>();
            yield return WaitFor(() => IdleBlocker() == null, plan.Timeouts.IdleSeconds, ok, 10);
            if (!ok.Value) { rt.SkipReason = "not idle after scene: " + IdleBlocker(); yield break; }
            var sm = Game.Instance.SaveManager;
            if ((bool)SettingsRoot.Difficulty.OnlyOneSave) { rt.SkipReason = "ironman save: manual saves are refused"; yield break; }
            if (!sm.IsSaveAllowed(SaveInfo.SaveType.Manual)) { rt.SkipReason = "SaveManager.IsSaveAllowed(Manual) is false here"; yield break; }

            rt.Attempted = true;
            rt.AfterScene = afterScene;
            var before = bridge.State();
            var flagsA = RrtBridge.FlagSet(before);
            var timesA = RrtBridge.ToData(before);

            var sw = Stopwatch.StartNew();
            var info = sm.CreateNewSave("RRTHarness roundtrip");
            bool done = false;
            Game.Instance.SaveGame(info, () => done = true);
            yield return WaitFor(() => done && !LoadingProcess.Instance.IsLoadingInProcess && !sm.CommitInProgress, plan.Timeouts.SaveSeconds, ok, 5);
            rt.SaveMs = sw.Elapsed.TotalMilliseconds;
            rt.SaveFile = info.FolderName;
            rt.Saved = ok.Value && info.IsActuallySaved && File.Exists(info.FolderName);
            if (!rt.Saved) { rt.SkipReason = "Game.SaveGame did not produce a file within " + plan.Timeouts.SaveSeconds + " s"; yield break; }

            var err = new Box<string?>(); var ms = new Box<double>(); var notIdle = new Box<string?>();
            yield return LoadSave(info.FolderName, err, ms, notIdle);
            rt.LoadMs = ms.Value;
            rt.Reloaded = err.Value == null && notIdle.Value == null;
            if (!rt.Reloaded) { rt.SkipReason = "reload failed: " + (err.Value ?? notIdle.Value); yield break; }

            var after = bridge.State();
            var flagsB = RrtBridge.FlagSet(after);
            var timesB = RrtBridge.ToData(after);
            rt.MissingAfterReload = flagsA.Except(flagsB).Where(persistentFlagKeys.Contains).OrderBy(x => x, StringComparer.Ordinal).ToList();
            rt.ExtraAfterReload = flagsB.Except(flagsA).Where(persistentFlagKeys.Contains).OrderBy(x => x, StringComparer.Ordinal).ToList();
            foreach (var t in timesA.Times)
                if (!timesB.Times.TryGetValue(t.Key, out int v) || v != t.Value) rt.MissingAfterReload.Add("hour." + t.Key + "=" + t.Value);
            rt.DerivedChanged = flagsA.Except(flagsB).Concat(flagsB.Except(flagsA)).Where(f => !persistentFlagKeys.Contains(f)).OrderBy(x => x, StringComparer.Ordinal).ToList();
            rt.ChapterMatches = timesA.Chapter == timesB.Chapter;
            rt.Passed = rt.MissingAfterReload.Count == 0 && rt.ExtraAfterReload.Count == 0 && rt.ChapterMatches;

            if (plan.DeleteRoundTripSave)
            {
                try
                {
                    var saved = sm.FirstOrDefault(s => s.FolderName != null && string.Equals(Path.GetFullPath(s.FolderName), Path.GetFullPath(info.FolderName), StringComparison.OrdinalIgnoreCase));
                    if (saved != null) sm.DeleteSave(saved);
                    else if (File.Exists(info.FolderName)) File.Delete(info.FolderName);
                    rt.Deleted = !File.Exists(rt.SaveFile);
                }
                catch (Exception ex) { capture.Add("harness", "Error", "round-trip save cleanup failed: " + ex.Message, ex.ToString()); }
            }
        }

        // ---- finish -------------------------------------------------------------------------------

        void TryWrite()
        {
            try
            {
                report.ElapsedSeconds = Math.Round(clock.Elapsed.TotalSeconds, 1);
                report.ComputeSummary();
                report.Write(reportPath);
            }
            catch (Exception ex) { Entry.Mod.Logger.Log("Report write failed: " + ex.Message); }
        }

        void Abort(string reason)
        {
            if (finished) return;
            report.Status = "aborted";
            report.AbortReason = reason;
            Complete();
        }

        void Finish()
        {
            if (finished) return;
            report.Status = "complete";
            Complete();
        }

        void Complete()
        {
            finished = true;
            stack.Clear();
            TryStopDialog();
            report.FinishedUtc = DateTime.UtcNow;
            report.GlobalExceptions = capture.Since(0).Where(e => e.Context == null || !e.Context.StartsWith("save:", StringComparison.Ordinal)).ToList();
            TryWrite();
            Entry.Mod.Logger.Log("Finished: " + report.Status + (report.AbortReason != null ? " (" + report.AbortReason + ")" : "")
                + "; passed=" + report.Summary.Passed + "; report " + reportPath);
            if (plan.QuitWhenDone) Application.Quit();
        }
    }
}
