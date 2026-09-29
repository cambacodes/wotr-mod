using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Reflection;
using HarmonyLib;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Area;
using Kingmaker.Blueprints.Root;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.Visual.Sound;
using UnityEngine;

namespace RRT.TestHarness
{
    // -Spike Presence (E12d quiet copy): runs only when plan.Spike is "presence"; a normal run never reaches this file. The
    // spike never saves: the harness loads the next save (or quits) afterwards, so the copies and their records are discarded.
    internal sealed partial class HarnessRunner
    {
        const string PresenceSpikeKey = "harness.spike.presence.";

        // Audible barks (voice event or text) by unit, recorded by a Harmony prefix on UnitAsksComponent.Bark.Play while the
        // presence spike watches; patched on the first presence spike only.
        static Dictionary<UnitEntityData, List<string>>? spikeBarks;
        static bool barkPatched;
        static readonly FieldInfo? AsksUnit = AccessTools.Field(typeof(UnitAsksComponent), "m_Unit");

        static void SpikeBarkPrefix(UnitAsksComponent.Bark __instance, UnitAsksComponent.BarkEntry entry)
        {
            var log = spikeBarks;
            if (log == null || entry == null || string.IsNullOrEmpty(entry.AkEvent) && entry.Text == null) return;
            if (!(AsksUnit?.GetValue(__instance.Owner) is UnitEntityData unit) || !log.TryGetValue(unit, out var list)) return;
            string text;
            try { text = entry.Text?.String?.ToString() ?? ""; } catch { text = "?"; }
            list.Add((string.IsNullOrEmpty(entry.AkEvent) ? "(text)" : entry.AkEvent) + (text.Length > 0 ? " \"" + text + "\"" : ""));
        }

        static IEnumerable<UnitAsksComponent.Bark> AllBarks(UnitAsksComponent asks)
        {
            foreach (var field in typeof(UnitAsksComponent).GetFields(BindingFlags.Instance | BindingFlags.Public))
                if (field.GetValue(asks) is UnitAsksComponent.Bark bark) yield return bark;
            foreach (var bark in asks.AnimationBarks ?? new UnitAsksComponent.AnimationBark[0]) yield return bark;
        }

        static bool Silent(UnitAsksComponent? asks) => asks == null
            || AllBarks(asks).All(b => b.Entries == null || b.Entries.All(e => string.IsNullOrEmpty(e.AkEvent) && e.Text == null));

        IEnumerator PresenceSpike(PresenceSpikeResult res)
        {
            var sp = plan.Presence!;
            var sw = Stopwatch.StartNew();
            var ok = new Box<bool>();
            var game = Game.Instance;
            var guests = new List<(object Guest, QuietCopyProbe Probe)>();
            try
            {
                var problems = rrt == null ? new List<string> { "RRT bridge not available" } : RrtBridge.Validate(rrt.Assembly, RrtBridge.PresenceSpikeExpectations);
                if (problems.Count > 0) { res.Error = "spike reflection: " + string.Join("; ", problems); yield break; }
                if (!barkPatched)
                {
                    barkPatched = true;
                    try { harmony.Patch(AccessTools.Method(typeof(UnitAsksComponent.Bark), "Play"), prefix: new HarmonyMethod(typeof(HarnessRunner), nameof(SpikeBarkPrefix))); }
                    catch (Exception ex) { res.Error = "could not observe barks: " + ex.Message; yield break; }
                }

                // ---- Drezen: stay when already there, else load the enter point ------------------------------------------
                if (sp.EnterPoint != null && ResidenceSpikePlan.Norm(game.CurrentlyLoadedArea?.AssetGuid.ToString() ?? "") != PresenceSpikePlan.DrezenCapital)
                {
                    var enter = Bp<BlueprintAreaEnterPoint>(sp.EnterPoint);
                    if (enter == null) { res.EntryError = "enter point " + sp.EnterPoint + " is not a BlueprintAreaEnterPoint"; yield break; }
                    try { game.LoadArea(enter, AutoSaveMode.None); }
                    catch (Exception ex) { res.EntryError = "LoadArea threw " + ex.GetType().Name + ": " + ex.Message; yield break; }
                    yield return WaitFor(() => game.IsLoadingSave || LoadingProcess.Instance.IsLoadingInProcess || LoadingProcess.Instance.IsLoadingScreenActive
                        || game.CurrentlyLoadedArea == enter.Area, 30, ok);
                    if (!ok.Value) { res.EntryError = "the load did not start within 30 s"; yield break; }
                    yield return WaitFor(() => !LoadingProcess.Instance.IsLoadingInProcess && !LoadingProcess.Instance.IsLoadingScreenActive
                        && game.CurrentlyLoadedArea == enter.Area && game.State.LoadedAreaState?.MainState != null, sp.EntrySeconds, ok, 30);
                    if (!ok.Value) { res.EntryError = "area " + enter.Area?.name + " not loaded within " + sp.EntrySeconds + " s"; yield break; }
                }
                yield return WaitFor(() => IdleBlocker() == null, sp.SettleSeconds, ok, 30);
                if (!ok.Value) { res.NotIdle = IdleBlocker() ?? "unstable"; yield break; }
                var area = game.CurrentlyLoadedArea!;
                string areaGuid = ResidenceSpikePlan.Norm(area.AssetGuid.ToString());
                res.Area = area.name + " " + areaGuid;
                var main = game.Player.MainCharacter.Value;

                // ---- spawn one copy per candidate through RRT's GuestPresence ----------------------------------------------
                var units = game.State.LoadedAreaState.AllEntityData.OfType<UnitEntityData>().Where(u => !u.Destroyed && !u.IsDisposed).ToList();
                int seat = 0;
                foreach (var guid in sp.Units)
                {
                    var bp = Bp<BlueprintUnit>(guid);
                    if (bp == null) { res.Skipped.Add(guid + ": not a BlueprintUnit"); continue; }
                    if (units.Any(u => u.Blueprint == bp && !u.State.IsDead)) { res.Skipped.Add(bp.name + ": a live unit of it is already in the area"); continue; }
                    var probe = new QuietCopyProbe { Unit = guid, UnitName = bp.name, NativeFaction = bp.Faction?.name, NativeAsks = bp.Visual?.Barks?.name };
                    res.Copies.Add(probe);
                    var at = main.Position + Quaternion.Euler(0f, 90f * seat++, 0f) * Vector3.forward * sp.Distance;
                    try
                    {
                        var guest = rrt!.NewSpawnCopyPresence(PresenceSpikeKey + seat, guid, areaGuid, at.x, at.y, at.z, 0f, bp);
                        guests.Add((guest, probe));
                        RrtBridge.PresenceTick(guest, true);
                        probe.EngineStatus = RrtBridge.PresenceStatus(guest);
                        probe.Spawned = probe.EngineStatus != null && probe.EngineStatus.Contains("-> Spawn");
                        probe.Quiet = RrtBridge.PresenceQuiet(guest);
                        var err = RrtBridge.PresenceError(guest);
                        if (err != null) probe.Error = "GuestPresence.Tick: " + err.Message;
                    }
                    catch (Exception ex) { probe.Error = "spawn: " + ex.Message; }
                }
                if (guests.Count == 0) yield break;
                yield return WaitFor(() =>
                {
                    foreach (var g in guests) RrtBridge.PresenceTick(g.Guest, true);
                    return guests.Where(g => g.Probe.Spawned).All(g => (RrtBridge.PresenceActor(g.Guest) as UnitEntityData)?.View != null);
                }, 10, ok, 5);

                // ---- state, forced bark triggers, then a watch --------------------------------------------------------------
                spikeBarks = new Dictionary<UnitEntityData, List<string>>();
                var copies = new List<(UnitEntityData Unit, QuietCopyProbe Probe)>();
                foreach (var (guest, probe) in guests.Where(g => g.Probe.Spawned))
                {
                    if (!(RrtBridge.PresenceActor(guest) is UnitEntityData copy)) continue;
                    copies.Add((copy, probe));
                    spikeBarks[copy] = probe.Barks;
                    probe.Exists = copy.IsInGame && !copy.Destroyed && !copy.State.IsDead && game.State.LoadedAreaState.AllEntityData.Contains(copy);
                    probe.Faction = copy.Descriptor.Faction?.name;
                    probe.PlayerFaction = copy.Descriptor.Faction == BlueprintRoot.Instance.PlayerFaction;
                    probe.PartyGroup = main != null && ReferenceEquals(copy.Group, main.Group);
                    probe.Passive = copy.Passive;
                    probe.Asks = copy.Descriptor.Asks?.name ?? "(none)";
                    probe.AsksSilent = Silent(copy.View?.Asks);
                }
                // Force the triggers a fight, a click and exploring would fire; a silent copy plays nothing audible.
                foreach (var (copy, probe) in copies)
                {
                    var asks = copy.View?.Asks;
                    if (asks == null) continue;
                    foreach (var bark in new[] { asks.Aggro, asks.Pain, asks.LowHealth, asks.Selected, asks.Discovery, asks.CheckFail })
                    {
                        try { bark.Schedule(); } catch (Exception ex) { res.Notes.Add(probe.UnitName + ": forced bark threw " + ex.Message); }
                        yield return null;
                    }
                }
                var dc = game.DialogController;
                object? lastDialog = dc.Dialog;
                var watch = Stopwatch.StartNew();
                while (watch.Elapsed.TotalSeconds < sp.ObserveSeconds)
                {
                    foreach (var g in guests) RrtBridge.PresenceTick(g.Guest, true);   // as Main.TickPresences would
                    foreach (var (copy, probe) in copies) if (copy.IsInCombat) probe.InCombat = true;
                    if (dc.Dialog != null && !ReferenceEquals(dc.Dialog, lastDialog))
                        res.Dialogs.Add(dc.Dialog.name + " (speaker " + (dc.CurrentSpeaker?.CharacterName ?? "none") + ")");
                    lastDialog = dc.Dialog;
                    yield return null;
                }
                if (dc.Dialog != null) TryStopDialog();
            }
            finally
            {
                spikeBarks = null;
                res.Ms = sw.Elapsed.TotalMilliseconds;
            }
            // ---- remove every copy the spike spawned ------------------------------------------------------------------------
            foreach (var (guest, probe) in guests)
            {
                if (!probe.Spawned) continue;
                var actor = RrtBridge.PresenceActor(guest) as UnitEntityData;
                RrtBridge.PresenceTick(guest, false);
                string key = RrtBridge.PresenceSaveKey(guest);
                yield return WaitFor(() => !Game.Instance.Player.SettingsList.ContainsKey(key) && (actor == null || !actor.IsInGame), 5, ok);
                probe.Removed = ok.Value;
            }
        }
    }
}
