using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using HarmonyLib;
using Kingmaker;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Area;
using Kingmaker.Blueprints.Quests;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.UnitLogic.Commands;
using UnityEngine;

namespace RRT.TestHarness
{
    // -Spike Residence: the P2 feasibility spike of Writer/handoffs/10-HAREM-RESIDENCE.md (findings: 10b-RESIDENCE-SPIKE.md).
    // Runs only when plan.Spike is "residence"; a normal run never reaches this file. The spike never saves: the harness
    // loads the next save (or quits) afterwards, so the area change, the copy and its presence record are discarded.
    internal sealed partial class HarnessRunner
    {
        // Native etudes and objectives the spike reports (blueprints.zip GUIDs; see 10b-RESIDENCE-SPIKE.md).
        static readonly (string Name, string Guid)[] SpikeEtudes =
        {
            ("Council", "c388d0af029feb347b77886db29a59cd"),
            ("Council5_2", "8daea73ec7440aa4c925c74af388538c"),
            ("TricksterCouncil_Council5_2", "9b0197e878a63bd478aded7661cf9cc2"),
            ("AfterCouncil5_2", "16c7763a682e6294292346e1365ef164"),
            ("TricksterCouncil_NoCouncil", "5b4daf74cafb99b469474ce46fcdd0d5"),
            ("TricksterCouncilDefault", "d3306da844810c74984e37a41d6d6f99"),
            ("TricksterCouncil_CouncilFight", "ce1d29b444c5f624dbe558ab89b78950"),
            ("FightAgainstCouncil", "b80a81e97e26167489c439caf34888f8"),
            ("FightAgainstCouncilNoctaAllied", "f4004d2687004c646bbe3a047d15f78f"),
            ("FightAgaintsNoctaCouncilAllied", "ed5d1dfa2402bed4cb7a59a21c14a1a4"),
            ("SocotGone", "007c4990584473046ac29666a235efb3"),
        };
        const string ObjKillNocta = "530a7178ade8aca419c16f06e8a851f4";     // Obj_6a_KillNocta
        const string ObjKillCouncil = "4ee3bbed15c1c6c4fafe19f70a96d060";   // Obj_6b_KillCouncil
        const string SpikePresenceKey = "harness.spike.residence";

        // Native actions observed while the spike runs (Harmony prefixes, patched on the first spike only).
        static List<string>? spikeNativeActions;
        static bool spikePatched;

        static T? Bp<T>(string guid) where T : SimpleBlueprint => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(guid)) as T;

        static void SpikeActionPrefix(GameAction __instance)
        {
            var log = spikeNativeActions;
            if (log == null) return;
            string caption;
            try { caption = __instance.GetCaption(); } catch { caption = "?"; }
            lock (log) log.Add(__instance.GetType().Name + ": " + caption + " (in " + (Game.Instance.CurrentlyLoadedArea?.name ?? "no area") + ")");
        }

        void PatchSpikeObservers(ResidenceSpikeResult res)
        {
            if (spikePatched) return;
            spikePatched = true;
            var prefix = new HarmonyMethod(typeof(HarnessRunner), nameof(SpikeActionPrefix));
            foreach (var type in new[] { typeof(ShowPartySelection), typeof(StartCombat), typeof(PlayCutscene), typeof(TeleportParty) })
            {
                try { harmony.Patch(AccessTools.Method(type, nameof(GameAction.RunAction)), prefix: prefix); }
                catch (Exception ex) { res.Notes.Add("could not observe " + type.Name + ": " + ex.Message); }
            }
        }

        static Dictionary<string, string> SpikeEtudeStates()
        {
            var map = new Dictionary<string, string>(StringComparer.Ordinal);
            var system = Game.Instance.Player.EtudesSystem;
            foreach (var (name, guid) in SpikeEtudes)
            {
                var bp = Bp<BlueprintEtude>(guid);
                if (bp == null) { map[name] = "missing blueprint"; continue; }
                string state = system.EtudeIsCompleted(bp) ? "completed" : system.EtudeIsStarted(bp) ? "started" : "not started";
                try { var fact = system.Etudes.GetFact(bp); if (fact != null && fact.IsPlaying) state += ", playing"; } catch { }
                map[name] = state;
            }
            return map;
        }

        static string Vec(Vector3 v) => "(" + v.x.ToString("0.00") + ", " + v.y.ToString("0.00") + ", " + v.z.ToString("0.00") + ")";

        IEnumerator ResidenceSpike(ResidenceSpikeResult res)
        {
            var sp = plan.Residence!;
            var sw = Stopwatch.StartNew();
            var ok = new Box<bool>();
            var game = Game.Instance;
            try
            {
                // Reflection into RRT's presence engine, checked here so a normal run's checks stay as they were.
                var problems = rrt == null ? new List<string> { "RRT bridge not available" } : RrtBridge.Validate(rrt.Assembly, RrtBridge.SpikeExpectations);
                if (problems.Count > 0) { res.Presence.Error = "spike reflection: " + string.Join("; ", problems); }

                // ---- (a) entry --------------------------------------------------------------------------------------
                var enter = Bp<BlueprintAreaEnterPoint>(sp.EnterPoint);
                res.EnterPoint = enter != null ? enter.name + " " + sp.EnterPoint : sp.EnterPoint;
                res.FromArea = game.CurrentlyLoadedArea?.name;
                res.EntryMethod = "Game.LoadArea(" + (enter?.name ?? sp.EnterPoint) + ", AutoSaveMode.None): the TeleportParty path for another area";
                var o6a = Bp<BlueprintQuestObjective>(ObjKillNocta);
                var o6b = Bp<BlueprintQuestObjective>(ObjKillCouncil);
                var s6a = o6a != null ? game.Player.QuestBook.GetObjectiveState(o6a) : QuestObjectiveState.None;
                var s6b = o6b != null ? game.Player.QuestBook.GetObjectiveState(o6b) : QuestObjectiveState.None;
                res.ClosetLive = s6a != QuestObjectiveState.Completed && s6b != QuestObjectiveState.Completed;
                res.ClosetNote = "Obj_6a_KillNocta " + s6a + ", Obj_6b_KillCouncil " + s6b + ": the native closet "
                    + (res.ClosetLive ? "still teleports (ToCouncil_CheckPassedActions IfFalse)" : "only barks (ToCouncil_CheckPassedActions IfTrue)");
                res.EtudesBefore = SpikeEtudeStates();
                if (enter == null) { res.EntryError = "enter point " + sp.EnterPoint + " is not a BlueprintAreaEnterPoint"; yield break; }

                PatchSpikeObservers(res);
                spikeNativeActions = res.NativeActions;
                var load = Stopwatch.StartNew();
                try { game.LoadArea(enter, AutoSaveMode.None); }
                catch (Exception ex) { res.EntryError = "LoadArea threw " + ex.GetType().Name + ": " + ex.Message; capture.Add("harness", "Exception", "spike LoadArea threw", ex.ToString()); yield break; }
                yield return WaitFor(() => game.IsLoadingSave || LoadingProcess.Instance.IsLoadingInProcess || LoadingProcess.Instance.IsLoadingScreenActive
                    || game.CurrentlyLoadedArea == enter.Area, 30, ok);
                res.EntryStarted = ok.Value;
                if (!ok.Value) { res.EntryError = "the load did not start within 30 s"; yield break; }
                yield return WaitFor(() => !LoadingProcess.Instance.IsLoadingInProcess && !LoadingProcess.Instance.IsLoadingScreenActive
                    && game.CurrentlyLoadedArea == enter.Area && game.State.LoadedAreaState?.MainState != null, sp.EntrySeconds, ok, 30);
                res.LoadMs = load.Elapsed.TotalMilliseconds;
                res.AreaLoaded = ok.Value;
                if (!ok.Value) { res.EntryError = "area " + enter.Area?.name + " not loaded within " + sp.EntrySeconds + " s (now " + (game.CurrentlyLoadedArea?.name ?? "none") + ", " + IdleBlocker() + ")"; yield break; }

                // ---- (b) what loaded -----------------------------------------------------------------------------------
                yield return WaitFor(() => IdleBlocker() == null, sp.SettleSeconds, ok, 60);
                res.NotIdleAfterEntry = ok.Value ? null : IdleBlocker() ?? "unstable";
                res.GameModeAfterEntry = Mode();
                res.InCombatAfterEntry = game.Player.IsInCombat;
                foreach (var m in game.Player.EtudesSystem.GetActiveAdditionalMechanics(enter.Area))
                {
                    res.ActiveMechanicsGuids.Add(ResidenceSpikePlan.Norm(m.AssetGuid.ToString()));
                    bool loaded; try { loaded = m.IsSceneLoadedNow(); } catch { loaded = false; }
                    res.ActiveMechanics.Add(m.name + " " + ResidenceSpikePlan.Norm(m.AssetGuid.ToString()) + (loaded ? " (scene loaded)" : " (scene not loaded)"));
                }
                res.Preset = ResidenceSpikePlan.ClassifyPreset(res.ActiveMechanicsGuids);
                res.EtudesAfter = SpikeEtudeStates();
                var main = game.Player.MainCharacter.Value;
                foreach (var u in game.State.LoadedAreaState.AllEntityData.OfType<UnitEntityData>().Where(u => !u.IsPlayerFaction && !u.Destroyed))
                    res.AreaUnits.Add((u.CharacterName ?? "?") + " [" + (u.Blueprint?.name ?? "?") + "] " + (u.IsInGame ? "in game" : "hidden")
                        + (u.State.IsDead ? ", dead" : "") + (main != null && u.IsEnemy(main) ? ", hostile" : "") + " at " + Vec(u.Position));
                if (plan.Screenshots)
                {
                    try { game.UI.GetCameraRig().ScrollToImmediately(new Vector3(sp.Seat[0], sp.Seat[1], sp.Seat[2])); } catch { }
                    yield return new WaitForSecondsRealtime(1f);
                    yield return Shot("residence__entry", res.Screenshots, res.Notes.Add);
                }

                // ---- (c) one presence copy at a seat -----------------------------------------------------------------
                if (res.Presence.Error != null) yield break;
                // A native entry dialog (a replayed session) would block the talk check: note it and close it, so (c) is
                // measured on its own. (b) has already recorded it.
                if (game.DialogController.Dialog != null)
                {
                    res.Notes.Add("closed native dialog " + game.DialogController.Dialog.name + " (at " + (game.DialogController.CurrentCue?.name ?? "no cue") + ") before (c)");
                    TryStopDialog();
                    yield return WaitFor(() => game.DialogController.Dialog == null, 10, ok);
                }
                yield return SpikePresence(res, sp, enter.Area!);
            }
            finally
            {
                spikeNativeActions = null;
                res.Ms = sw.Elapsed.TotalMilliseconds;
            }
        }

        IEnumerator SpikePresence(ResidenceSpikeResult res, ResidenceSpikePlan sp, BlueprintArea area)
        {
            var p = res.Presence;
            var game = Game.Instance;
            var ok = new Box<bool>();
            p.Seat = sp.Seat;
            var seat = new Vector3(sp.Seat[0], sp.Seat[1], sp.Seat[2]);
            var units = game.State.LoadedAreaState.AllEntityData.OfType<UnitEntityData>().Where(u => !u.Destroyed && !u.IsDisposed).ToList();
            BlueprintUnit? chosen = null;
            foreach (var guid in sp.Units)
            {
                var bp = Bp<BlueprintUnit>(guid);
                if (bp == null) { p.Skipped.Add(guid + ": not a BlueprintUnit"); continue; }
                if (units.Any(u => u.Blueprint == bp && !u.State.IsDead)) { p.Skipped.Add(bp.name + ": a live unit of it is already in the area"); continue; }
                chosen = bp;
                break;
            }
            if (chosen == null) yield break;
            p.Unit = ResidenceSpikePlan.Norm(chosen.AssetGuid.ToString());
            p.UnitName = chosen.name;

            // RRT's own engine: a spawn-copy GuestPresence at a Position, ticked as Main.TickPresences ticks registered ones.
            var guest = rrt!.NewSpawnCopyPresence(SpikePresenceKey, p.Unit, ResidenceSpikePlan.Norm(area.AssetGuid.ToString()),
                sp.Seat[0], sp.Seat[1], sp.Seat[2], sp.Seat[3], chosen);
            RrtBridge.PresenceTick(guest, true);
            p.EngineStatus = RrtBridge.PresenceStatus(guest);
            p.Spawned = p.EngineStatus != null && p.EngineStatus.Contains("-> Spawn");
            var err = RrtBridge.PresenceError(guest);
            if (err != null) { p.Error = "GuestPresence.Tick: " + err.Message; capture.Add("harness", "Exception", "spike presence tick failed", err.ToString()); yield break; }
            if (!p.Spawned) yield break;

            UnitEntityData? actor = null;
            yield return WaitFor(() =>
            {
                RrtBridge.PresenceTick(guest, true);
                actor = RrtBridge.PresenceActor(guest) as UnitEntityData;
                return actor != null && actor.View != null;
            }, 10, ok, 5);
            p.EngineStatus = RrtBridge.PresenceStatus(guest);
            try
            {
                if (actor != null)
                {
                    p.Exists = actor.IsInGame && !actor.Destroyed && !actor.State.IsDead
                        && game.State.LoadedAreaState.AllEntityData.Contains(actor);
                    p.HasView = actor.View != null;
                    p.ViewActive = actor.View != null && actor.View.gameObject.activeInHierarchy;
                    p.Position = new[] { actor.Position.x, actor.Position.y, actor.Position.z };
                    p.SeatErrorMetres = Math.Round(Vector3.Distance(actor.Position, seat), 2);
                }
            }
            catch (Exception ex) { res.Notes.Add("presence checks threw: " + ex.Message); }
            if (actor == null || !p.HasView) { yield return SpikeRemove(res, guest); yield break; }

            try { game.UI.GetCameraRig().ScrollToImmediately(actor.Position); } catch { }
            yield return new WaitForSecondsRealtime(1f);
            try { p.Rendered = actor.View!.GetComponentsInChildren<Renderer>().Any(r => r.enabled && r.isVisible); }
            catch (Exception ex) { res.Notes.Add("renderer check threw: " + ex.Message); }
            if (plan.Screenshots) yield return Shot("residence__presence", res.Screenshots, res.Notes.Add);

            // Path: order a walk to PathTo and measure it.
            var start = actor.Position;
            var target = new Vector3(sp.PathTo[0], sp.PathTo[1], sp.PathTo[2]);
            try { actor.Commands.Run(new UnitMoveTo(target)); }
            catch (Exception ex) { res.Notes.Add("UnitMoveTo threw: " + ex.Message); }
            var moving = Stopwatch.StartNew();
            while (moving.Elapsed.TotalSeconds < sp.PathSeconds && Vector3.Distance(actor.Position, target) > 0.8f) yield return null;
            p.PathMovedMetres = Math.Round(Vector3.Distance(start, actor.Position), 2);
            p.PathRemainingMetres = Math.Round(Vector3.Distance(actor.Position, target), 2);
            p.Pathed = p.PathMovedMetres >= sp.PathMinMetres;

            // Talk: start an RRT presence hub dialog with the copy as the target unit, as the E12c click does.
            yield return WaitFor(() => IdleBlocker() == null, 10, ok, 5);
            var hub = rrt.PresenceHubs.Values.OfType<BlueprintDialog>().FirstOrDefault();
            var dc = game.DialogController;
            if (hub == null) res.Notes.Add("no RRT presence hub dialog is built; dialog check skipped");
            else
            {
                p.Dialog = hub.name;
                try { dc.StartDialogWithUnit(hub, actor, game.Player.MainCharacter.Value); }
                catch (Exception ex) { res.Notes.Add("StartDialogWithUnit threw: " + ex.Message); }
                yield return WaitFor(() => dc.Dialog == hub && dc.CurrentCue != null, 10, ok);
                p.DialogStarted = ok.Value;
                if (ok.Value)
                {
                    p.DialogSpeaker = dc.CurrentSpeaker?.CharacterName ?? dc.FirstSpeaker?.CharacterName ?? "(no speaker unit)";
                    yield return WaitBound(dc);
                    if (plan.Screenshots && dc.Dialog != null) yield return Shot("residence__dialog", res.Screenshots, res.Notes.Add);
                }
                TryStopDialog();
                yield return WaitFor(() => dc.Dialog == null, 10, ok);
            }
            yield return SpikeRemove(res, guest);
        }

        IEnumerator SpikeRemove(ResidenceSpikeResult res, object guest)
        {
            var ok = new Box<bool>();
            var actor = RrtBridge.PresenceActor(guest) as UnitEntityData;
            RrtBridge.PresenceTick(guest, false);
            string key = RrtBridge.PresenceSaveKey(guest);
            yield return WaitFor(() => !Game.Instance.Player.SettingsList.ContainsKey(key) && (actor == null || !actor.IsInGame), 5, ok);
            res.Presence.Removed = ok.Value;
            res.Notes.Add("after removal: " + RrtBridge.PresenceStatus(guest));
        }
    }
}
