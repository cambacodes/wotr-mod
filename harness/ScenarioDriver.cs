using System;
using System.Linq;
using System.Reflection;
using System.Diagnostics;
using Kingmaker;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using UnityEngine;
using Newtonsoft.Json;
using System.Collections;
using System.Collections.Generic;
using Kingmaker.Blueprints.Root;

namespace RRT.TestHarness
{
    internal sealed partial class HarnessRunner
    {
        IEnumerator SystemScenarios(SaveReport save, string prefix)
        {
            var cases = SystemCases.Parse(plan.SystemCasesJson!).Cases.Where(c => (c.SaveChapter ?? c.Chapter) == save.State!.Chapter).ToList();
            using (NativeEpilogueInventoryProbe.PreventSaves())
            {
                foreach (var scenario in cases)
                {
                    var coverage = new SystemCoverage { Scenario = scenario.Id, System = scenario.System,
                        Evidence = plan.Force ? "synthetic chapter/flags; real area/contacts/resources; earning unproved" : "loaded save history" };
                    save.Systems.Add(coverage);
                    capture.Context = prefix + "system:" + scenario.Id;
                    var error = new Box<string?>(); var ms = new Box<double>(); var idle = new Box<string?>();
                    yield return LoadSave(save.ResolvedPath, error, ms, idle);
                    if (error.Value != null || idle.Value != null)
                    { coverage.Result = "load-failed"; coverage.Findings.Add(error.Value ?? idle.Value!); TryWrite(); continue; }
                    if (plan.Force && scenario.FixtureFlags == null)
                    { coverage.Result = "missing-fixture"; coverage.Findings.Add("Integration must supply the scene's fixture contract"); TryWrite(); continue; }
                    using (var probe = new SystemScenarioProbe(rrt!, plan.Force ? scenario.FixtureFlags : null, scenario.Chapter))
                        yield return new Guarded(DriveSystem(scenario, coverage, probe, save), ex => {
                            coverage.Result = "exception"; coverage.Findings.Add(ex.ToString()); TryStopDialog();
                        });
                    coverage.Passed = coverage.Result == "completed" && coverage.Findings.Count == 0;
                    TryStopDialog(); TryWrite();
                }
                // All effects and queued deliveries belong to a disposable load, including on an exception.
                var restore = new Box<string?>(); var restoreMs = new Box<double>(); var restoreIdle = new Box<string?>();
                yield return LoadSave(save.ResolvedPath, restore, restoreMs, restoreIdle);
                if (restore.Value != null || restoreIdle.Value != null)
                    save.Systems.Add(new SystemCoverage { Scenario = "restore", Result = "load-failed",
                        Findings = new List<string> { restore.Value ?? restoreIdle.Value! } });
            }
        }

        IEnumerator DriveSystem(SystemScenario scenario, SystemCoverage coverage, SystemScenarioProbe probe, SaveReport save)
        {
            var bridge = rrt!;
            foreach (var step in scenario.Steps)
            {
                var scene = bridge.Scenes.Cast<object>().SingleOrDefault(s => RrtBridge.SceneId(s) == step.Scene);
                if (scene == null) { coverage.Findings.Add("Missing scene: " + step.Scene); break; }
                var state = SystemScenarioProbe.Control(bridge, bridge.State(), step);
                bool available = bridge.Available(scene, state);
                coverage.AvailabilityChecked.Add(step.Scene + ": " + available + "; remove=" + string.Join(",", step.Remove)
                    + "; add=" + string.Join(",", step.Add) + "; spent=" + JsonConvert.SerializeObject(step.RestSpent));
                var table = SystemScenarioProbe.TableEntries(bridge, state);
                if (available != step.Available || step.Table && table.Contains(step.Scene) != step.Available)
                { coverage.Findings.Add("Availability/Table assertion failed: " + step.Scene); break; }
                var ledger = SystemScenarioProbe.LedgerEntries(bridge, state);
                foreach (var entry in step.LedgerEntries)
                    if (!ledger.Contains(entry)) coverage.Findings.Add("Ledger entry hidden: " + entry);
                    else coverage.LedgerTouched.Add(entry);
                foreach (var entry in step.HiddenLedgerEntries)
                    if (ledger.Contains(entry)) coverage.Findings.Add("Ledger entry leaked: " + entry);
                if (!step.Available || step.ProbeOnly) continue; // Controls assert rules on a copy; never fabricate live history.
                if (step.Remove.Count > 0 || step.Add.Count > 0 || step.RestSpent.Count > 0)
                { coverage.Findings.Add("Positive walks cannot use transient control mutations"); break; }
                if (!bridge.Available(scene, bridge.State())) { coverage.Findings.Add("Live step became hidden: " + step.Scene); break; }
                var run = new SceneRun { Scene = step.Scene, Relationship = RrtBridge.SceneRelationship(scene),
                    AvailableAtStart = true, Forced = plan.Force, Strategy = "script:" + scenario.Id };
                save.Runs.Add(run);
                var watch = Stopwatch.StartNew();
                var started = bridge.StartedFlag(run.Relationship);
                if (started != null && !RrtBridge.SceneForbids(scene).Contains(started)) bridge.Set(started);
                var before = RrtBridge.FlagSet(bridge.State());
                var dc = Game.Instance.DialogController;
                var ok = new Box<bool>();
                int mark = capture.Mark();
                if (step.Table)
                {
                    table = SystemScenarioProbe.TableEntries(bridge, bridge.State());
                    int target = table.IndexOf(step.Scene);
                    if (target < 0 || !probe.OpenTable()) { coverage.Findings.Add("Table did not open"); break; }
                    for (int page = 0; page <= target / 6; page++)
                    {
                        yield return WaitFor(() => dc.CurrentCue != null && !IsCuePlayScheduled(dc) && dc.Answers.Any(), plan.Timeouts.StepSeconds, ok);
                        if (!ok.Value) break;
                        yield return WaitBound(dc);
                        string name = page < target / 6 ? "RRT_answer.view.table.more" : "RRT_answer.view.table.slot." + target % 6;
                        var answer = dc.Answers.SingleOrDefault(a => a.name == name);
                        if (answer == null) { coverage.Findings.Add("Table answer hidden: " + name); break; }
                        dc.SelectAnswer(answer); yield return null;
                    }
                }
                else if (bridge.Dialogs[step.Scene] is Kingmaker.DialogSystem.Blueprints.BlueprintDialog dialog)
                    dc.StartDialogWithoutTarget(dialog, null);
                else { coverage.Findings.Add("Scene dialog missing: " + step.Scene); break; }
                yield return WaitFor(() => dc.CurrentCue != null && ShotBelongs(dc.CurrentCue!.name, step.Scene), 10, ok);
                if (!ok.Value) { run.Result = "not-started"; coverage.Findings.Add("Scripted scene did not start: " + step.Scene); break; }
                coverage.ScenesTouched.Add(step.Scene);
                save.ScenesDriven++;
                yield return Walk(dc.Dialog, true, null, null, run, new List<int>(), step.Answers);
                yield return Settle(run, before, Ending(scene));
                run.Exceptions = capture.Since(mark); run.Passed = RunPassed(run);
                run.Ms = watch.Elapsed.TotalMilliseconds;
                save.ChoicesTaken += run.Choices.Count;
                coverage.ChoicesTouched.AddRange(run.Choices.Select(c => c.StoryChoice ?? c.Answer));
                var after = bridge.State();
                foreach (var flag in step.ExpectFlags.Where(f => !RrtBridge.FlagSet(after).Contains(f)))
                    coverage.Findings.Add("Expected effect absent: " + flag);
                var spent = (Dictionary<string, int>)RrtBridge.Get(after, "RestSpent")!;
                foreach (var pair in step.ExpectRestSpent)
                    if (!spent.TryGetValue(pair.Key, out int used) || used != pair.Value)
                        coverage.Findings.Add("Wrong rest allowance: " + pair.Key + "; expected " + pair.Value);
                if (!run.Passed) coverage.Findings.Add("Scripted walk failed: " + run.Result + "; " + run.Detail);
                if (coverage.Findings.Count > 0) break;
            }
            coverage.Result = coverage.Findings.Count == 0 && coverage.AvailabilityChecked.Count == scenario.Steps.Count
                ? "completed" : "incomplete";
        }

        // eng7-l11: use the exact runtime observations, never DialogSpeaker.GetEntity.
        ContactInventoryProbe CaptureContact(string guid, object before, bool witnesses)
        {
            var type = AppDomain.CurrentDomain.GetAssemblies().Select(a => a.GetType("Tirabade.NativeContact"))
                .First(t => t != null)!;
            var flags = BindingFlags.Static | BindingFlags.NonPublic;
            var rows = (Array)type.GetMethod("Inventory", flags)!.Invoke(null, new object[] { guid })!;
            var probe = new ContactInventoryProbe { Unit = guid, NativeWitnessesPresent = witnesses,
                NativeAccepted = (bool)type.GetMethod("InventoryAvailable", flags)!.Invoke(null, new object[] { guid })!,
                SnapshotAccepted = RrtBridge.ToData(before).AvailableContacts.Contains(guid) };
            foreach (var row in rows)
            {
                var rowType = row!.GetType();
                probe.Actors.Add(new ContactInventoryActor { State = JsonConvert.SerializeObject(row),
                    Usable = (bool)rowType.GetProperty("Usable")!.GetValue(row)!,
                    Ignorable = (bool)rowType.GetProperty("Ignorable")!.GetValue(row)! });
            }
            // Positions and walkability are evidence only; they never make a contact usable.
            var walkability = rows.Cast<object>().Select(row => SampleWalkable(
                (float[])row.GetType().GetField("Position")!.GetValue(row)!)).ToArray();
            var story = rrt!.Story;
            var presences = Newtonsoft.Json.Linq.JObject.FromObject(story.GetType().GetField("Presences")!.GetValue(story)!);
            var anchors = presences.Children<Newtonsoft.Json.Linq.JProperty>()
                .Where(p => (string?)p.Value["Unit"] == guid)
                .Select(p =>
                {
                    var area = Game.Instance.State.LoadedAreaState;
                    bool current = (string?)p.Value["Area"] == Game.Instance.CurrentlyLoadedArea?.AssetGuid.ToString();
                    var at = p.Value["At"];
                    Vector3? origin = null;
                    int matches = 0;
                    if (current && at?["NearUnit"] is Newtonsoft.Json.Linq.JValue near)
                    {
                        var units = area.AllEntityData.OfType<UnitEntityData>().Where(u =>
                            InlineHosts.Norm(u.Blueprint?.AssetGuid.ToString() ?? "") == InlineHosts.Norm((string)near)
                            && !u.Destroyed && !u.DestroyMark && !u.IsDisposed && u.IsInGame
                            && !u.State.IsDead && !u.State.IsFinallyDead).Take(2).ToArray();
                        matches = units.Length;
                        if (matches == 1) origin = units[0].Position;
                    }
                    else if (current && (string?)at?["Locator"] is string locator)
                    {
                        var entity = EntityService.Instance.GetEntity(locator);
                        if (entity != null && !entity.Destroyed) { matches = 1; origin = entity.Position; }
                    }
                    return new { Key = p.Name, Area = (string?)p.Value["Area"], At = at,
                        CurrentArea = current, Matches = matches, Resolved = origin != null,
                        Walkability = origin is Vector3 point ? SampleWalkable(new[] { point.x, point.y, point.z }) : null };
                }).ToArray();
            probe.AnchorWalkability = JsonConvert.SerializeObject(new { anchors, actorWalkability = walkability });
            return probe;
        }

        static WalkableProbe SampleWalkable(float[] position)
        {
            var query = new WalkableProbe { Position = position, Radius = 3 };
            var graphs = AstarPath.active?.data?.graphs;
            if (graphs == null) query.Error = "no pathfinding graphs in saved area";
            else foreach (var graph in graphs)
                graph?.GetNodes((Action<Pathfinding.GraphNode>)(node =>
                {
                    if (!node.Walkable) return;
                    var origin = new Vector3(position[0], position[1], position[2]);
                    var point = node is Pathfinding.MeshNode mesh ? mesh.ClosestPointOnNode(origin) : (Vector3)node.position;
                    query.Consider(point.x, point.y, point.z);
                }));
            return query;
        }
        // end eng7-l11
        IEnumerator NativeEpilogueInventory(SaveReport save, string prefix)
        {
            using (NativeEpilogueInventoryProbe.PreventSaves())
                yield return NativeEpilogueInventoryBody(save, prefix);
        }

        IEnumerator NativeEpilogueInventoryBody(SaveReport save, string prefix)
        {
            var source = NativeSlideCases.Parse(plan.NativeEpilogueCasesJson!);
            var cases = plan.Force ? source.Cases.Where(c => plan.IncludesScene(c.ExpectedCandidate)).ToList()
                : source.Cases.Any(c => c.UseSaveState) ? source.Cases.Where(c => c.UseSaveState).ToList()
                : new List<NativeSlideCase> {
                    new NativeSlideCase { Id = "saved/epilogue", Dialog = NativeEpilogueInventoryProbe.EpilogueDialog },
                    new NativeSlideCase { Id = "saved/afterlogue", Dialog = NativeEpilogueInventoryProbe.AfterlogueDialog } };
            if (cases.Count == 0) throw new InvalidOperationException("No slide cases match SceneFilter");
            if (plan.MaxScenesPerSave > 0 && cases.Count > plan.MaxScenesPerSave)
            {
                // Explicit evidence debt; a bounded subset must never be reported as a complete roster proof.
                save.NativeSlides.Add(new NativeSlideResult { Case = "coverage", Result = "truncated", Findings = new List<string> {
                    (cases.Count - plan.MaxScenesPerSave) + " slide cases not run (-MaxScenesPerSave)" } });
                cases = cases.Take(plan.MaxScenesPerSave).ToList();
            }
            foreach (var scenario in cases)
            {
                var result = new NativeSlideResult { Case = scenario.Id };
                save.NativeSlides.Add(result);
                capture.Context = prefix + "slides:" + scenario.Id;
                var error = new Box<string?>(); var ms = new Box<double>(); var notIdle = new Box<string?>();
                yield return LoadSave(save.ResolvedPath, error, ms, notIdle);
                if (error.Value != null || notIdle.Value != null)
                {
                    result.Result = "load-failed"; result.Findings.Add(error.Value ?? notIdle.Value!); TryWrite(); continue;
                }
                yield return new Guarded(DriveNativeSlides(scenario, result), ex =>
                {
                    result.Result = "exception"; result.Passed = false; result.Findings.Add(ex.ToString()); TryStopDialog();
                });
                TryWrite();
            }
            // Native OnShow/OnStop may change the disposable loaded world. Reload the source before leaving this mode.
            var restoreError = new Box<string?>(); var restoreMs = new Box<double>(); var restoreIdle = new Box<string?>();
            yield return LoadSave(save.ResolvedPath, restoreError, restoreMs, restoreIdle);
            if (restoreError.Value != null || restoreIdle.Value != null)
                save.NativeSlides.Add(new NativeSlideResult { Case = "restore", Result = "load-failed", Findings = new List<string> { restoreError.Value ?? restoreIdle.Value! } });
        }

        IEnumerator DriveNativeSlides(NativeSlideCase scenario, NativeSlideResult result)
        {
            int logMark = capture.Mark();
            using (var probe = new NativeEpilogueInventoryProbe(rrt!, scenario, plan.Force, result))
            {
                var dc = Game.Instance.DialogController;
                try
                {
                    dc.StartDialogWithoutTarget(probe.Dialog, null);
                    var ok = new Box<bool>();
                    yield return WaitFor(() => dc.Dialog != null || result.Observations.Count > 0, 10, ok);
                    if (!ok.Value) result.Result = "not-started";
                    else
                    {
                        int step = 0;
                        int scripted = 0;
                        for (; step < plan.MaxStepsPerWalk && dc.Dialog != null; step++)
                        {
                            yield return WaitFor(() => dc.Dialog == null || (!IsCuePlayScheduled(dc) && dc.Answers.Any()), plan.Timeouts.StepSeconds, ok, 2);
                            if (!ok.Value) { result.Result = "stuck"; result.Findings.Add("No answers at " + dc.CurrentCue?.name); break; }
                            if (dc.Dialog == null) break;
                            yield return WaitBound(dc);
                            if (dc.Dialog == null) break;
                            var answers = dc.Answers.ToList();
                            if (plan.Screenshots && result.Screenshots.Count < plan.ScreenshotsPerScene)
                                yield return Shot(Safe(scenario.Id) + "__slides__" + step, result.Screenshots, message => result.Findings.Add(message));
                            var next = answers.FirstOrDefault(a => IsAnswer(a, r => r.ContinueAnswer) || IsAnswer(a, r => r.InterchapterContinueAnswer)
                                || IsAnswer(a, r => r.ExitAnswer) || IsAnswer(a, r => r.InterchapterExitAnswer));
                            if (next == null && scripted < scenario.AnswerPath.Count)
                            {
                                string answer = scenario.AnswerPath[scripted++];
                                next = answers.SingleOrDefault(a => a.AssetGuid.ToString() == answer || a.name == answer);
                                if (next == null) result.Findings.Add("Scripted answer not selectable: " + answer);
                            }
                            if (next == null)
                            {
                                // Epilogue pages use the engine's continue answer; afterlogue verdict branches need an
                                // explicit coordinator script. Never choose an arbitrary moral/campaign answer.
                                result.Result = "needs-answer-script";
                                result.Findings.Add("Native choices at " + dc.CurrentCue?.name + ": " + string.Join(", ", answers.Select(a => a.AssetGuid + " " + a.name)));
                                break;
                            }
                            dc.SelectAnswer(next);
                            yield return null;
                        }
                        if (result.Result == "running") result.Result = dc.Dialog == null ? "completed" : "step-limit";
                    }
                }
                finally { TryStopDialog(); }
                probe.Evaluate(scenario);
                foreach (var error in capture.Since(logMark).Where(e => e.Relevant))
                    result.Findings.Add(error.Source + " " + error.Severity + ": " + error.Message);
                if (result.Findings.Count > 0) result.Passed = false;
            }
        }
    }
}
// END eng7-f5
