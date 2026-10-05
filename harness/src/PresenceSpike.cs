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

        // Fixture (RRT_HARNESS_HIDE): hide anchors before RRT's first tick of the area, so a primary placement fails from the start
        // (as a genuinely missing anchor would) instead of spawning first and losing its anchor afterwards. Test-only.
        static bool hidePatched;
        static void HideAnchorsPrefix()
        {
            try
            {
                string? hide = Environment.GetEnvironmentVariable("RRT_HARNESS_HIDE");
                var game = Game.Instance;
                if (string.IsNullOrWhiteSpace(hide) || game?.State?.LoadedAreaState?.MainState == null || game.IsLoadingSave || game.IsUnloading) return;
                var hidden = hide!.Split(',').Select(g => g.Trim()).Where(g => g.Length > 0).ToArray();
                foreach (var unit in game.State.Units.Where(u => hidden.Contains(u.Blueprint?.AssetGuid.ToString()) && u.IsInGame).ToArray())
                { unit.IsInGame = false; unit.MarkForDestroy(); }
            }
            catch { }
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
            if (!hidePatched && !string.IsNullOrWhiteSpace(Environment.GetEnvironmentVariable("RRT_HARNESS_HIDE")))
            {
                hidePatched = true;
                try
                {
                    var tick = AccessTools.TypeByName("Tirabade.Main") is Type main ? AccessTools.Method(main, "TickPresences") : null;
                    if (tick != null) harmony.Patch(tick, prefix: new HarmonyMethod(typeof(HarnessRunner), nameof(HideAnchorsPrefix)));
                    else res.Notes.Add("fixture: Tirabade.Main.TickPresences not found; anchors hidden after area load only");
                }
                catch (Exception ex) { res.Notes.Add("fixture: could not patch TickPresences: " + ex.Message); }
            }
            try
            {
                // ---- Drezen: stay when already there, else load the enter point ------------------------------------------
                if ((sp.ProbeCoordinates == null || sp.ProbeEnter) && sp.EnterPoint != null && Bp<BlueprintAreaEnterPoint>(sp.EnterPoint)?.Area != game.CurrentlyLoadedArea)
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
                // Fixture (RRT_HARNESS_TELEPORT=x,y,z): put the Commander near a spot before the first production tick (test-only).
                string? tp = Environment.GetEnvironmentVariable("RRT_HARNESS_TELEPORT");
                if (!string.IsNullOrWhiteSpace(tp))
                {
                    var c = tp!.Split(',').Select(v => float.Parse(v, System.Globalization.CultureInfo.InvariantCulture)).ToArray();
                    game.Player.MainCharacter.Value.Translocate(new UnityEngine.Vector3(c[0], c[1], c[2]), (float?)null);
                    res.Notes.Add("fixture moved the Commander to " + tp);
                }
                // Fixture (RRT_HARNESS_HIDE=guid,guid): take native anchor units out of play before the first production tick, so a
                // primary placement fails for real and its earned fallback is exercised. Test-only; the input save is untouched.
                string? hide = Environment.GetEnvironmentVariable("RRT_HARNESS_HIDE");
                if (!string.IsNullOrWhiteSpace(hide))
                {
                    var hidden = hide!.Split(',').Select(g => g.Trim()).Where(g => g.Length > 0).ToArray();
                    foreach (var unit in game.State.Units.Where(u => hidden.Contains(u.Blueprint?.AssetGuid.ToString())).ToArray())
                    { unit.IsInGame = false; unit.MarkForDestroy(); res.Notes.Add("fixture hid " + unit.Blueprint?.name + " " + unit.UniqueId); }
                }
                yield return WaitFor(() => IdleBlocker() == null, sp.SettleSeconds, ok, 30);
                if (!ok.Value) { res.NotIdle = IdleBlocker() ?? "unstable"; yield break; }
                // Fixture (RRT_HARNESS_RAYS=x,z,radius,step): downward ray hits (every collider, top first) on a grid, plus all
                // units in range, so a placement can be chosen off a roof/awning and away from static NPCs. Test-only, read-only.
                string? rays = Environment.GetEnvironmentVariable("RRT_HARNESS_RAYS");
                if (!string.IsNullOrWhiteSpace(rays))
                {
                    foreach (string spec in rays!.Split(';'))
                    {
                        var r = spec.Split(',').Select(v => float.Parse(v, System.Globalization.CultureInfo.InvariantCulture)).ToArray();
                        for (float gx = r[0] - r[2]; gx <= r[0] + r[2] + 0.01f; gx += r[3])
                            for (float gz = r[1] - r[2]; gz <= r[1] + r[2] + 0.01f; gz += r[3])
                            {
                                var hits = Physics.RaycastAll(new Vector3(gx, 90f, gz), Vector3.down, 120f).OrderByDescending(h => h.point.y).Take(4)
                                    .Select(h => h.point.y.ToString("0.0") + ":" + h.collider.name + "/" + LayerMask.LayerToName(h.collider.gameObject.layer)).ToArray();
                                var node = Kingmaker.View.ObstacleAnalyzer.GetNearestNode(new Vector3(gx, r.Length > 4 ? r[4] : 56f, gz));
                                res.Notes.Add("ray " + gx.ToString("0.0") + "," + gz.ToString("0.0") + " node "
                                    + (node.node != null ? node.position.y.ToString("0.0") + " d" + Vector3.Distance(new Vector3(gx, r.Length > 4 ? r[4] : 56f, gz), node.position).ToString("0.0") : "none")
                                    + " hits " + string.Join(" | ", hits));
                            }
                    }
                    foreach (var unit in game.State.Units.Where(u => u.IsInGame && !u.State.IsDead))
                        res.Notes.Add("unit " + unit.Blueprint?.name + " " + ResidenceSpikePlan.Norm(unit.Blueprint?.AssetGuid.ToString() ?? "") + " at "
                            + unit.Position.x.ToString("0.00") + "," + unit.Position.y.ToString("0.00") + "," + unit.Position.z.ToString("0.00") + " or " + unit.Orientation.ToString("0")
                            + " corp " + unit.Corpulence.ToString("0.0"));
                    yield break;
                }
                var area = game.CurrentlyLoadedArea!;
                string areaGuid = ResidenceSpikePlan.Norm(area.AssetGuid.ToString());
                res.Area = area.name + " " + areaGuid;
                if (sp.ProbeCoordinates != null)
                {
                    var query = res.Probe = new WalkableProbe { Position = sp.ProbeCoordinates, Radius = sp.ProbeRadius };
                    foreach (var unit in game.State.LoadedAreaState.AllEntityData.OfType<UnitEntityData>().Where(u => !u.Destroyed && !u.IsDisposed))
                        res.Notes.Add("unit " + unit.Blueprint?.name + " [" + ResidenceSpikePlan.Norm(unit.Blueprint?.AssetGuid.ToString() ?? "") + "] "
                            + unit.CharacterName + " at " + unit.Position.x.ToString("0.00") + "," + unit.Position.y.ToString("0.00") + "," + unit.Position.z.ToString("0.00")
                            + (unit.IsPlayerFaction ? " party" : "") + (unit.State.IsDead ? " dead" : ""));
                    var graphs = AstarPath.active?.data?.graphs;
                    if (graphs == null) { query.Error = "no pathfinding graphs in the saved area"; yield break; }
                    var position = new Vector3(query.Position[0], query.Position[1], query.Position[2]);
                    var bands = new SortedDictionary<int, float[]>();
                    foreach (var graph in graphs)
                        graph?.GetNodes((Action<Pathfinding.GraphNode>)(node =>
                        {
                            if (!node.Walkable) return;
                            var q = (Vector3)node.position;
                            int band = (int)Math.Round(q.y / 2f) * 2;
                            if (!bands.TryGetValue(band, out var b)) bands[band] = b = new[] { 0f, q.x, q.x, q.z, q.z };
                            b[0]++; b[1] = Math.Min(b[1], q.x); b[2] = Math.Max(b[2], q.x); b[3] = Math.Min(b[3], q.z); b[4] = Math.Max(b[4], q.z);
                        }));
                    foreach (var kv in bands)
                        res.Notes.Add("band y~" + kv.Key + " nodes " + kv.Value[0] + " x " + kv.Value[1].ToString("0") + ".." + kv.Value[2].ToString("0") + " z " + kv.Value[3].ToString("0") + ".." + kv.Value[4].ToString("0"));
                    foreach (var graph in graphs)
                        graph?.GetNodes((Action<Pathfinding.GraphNode>)(node =>
                        {
                            if (!node.Walkable) return;
                            var point = node is Pathfinding.MeshNode mesh ? mesh.ClosestPointOnNode(position) : (Vector3)node.position;
                            query.Consider(point.x, point.y, point.z);
                        }));
                    yield break;
                }
                if (sp.Key != null)
                {
                    res.ProductionReloadRequired = plan.RoundTrip;
                    var production = res.Production = new ProductionPresenceProbe { Key = sp.Key };
                    yield return InspectProductionPresence(production);
                    yield break;
                }
                var problems = rrt == null ? new List<string> { "RRT bridge not available" } : RrtBridge.Validate(rrt.Assembly, RrtBridge.PresenceSpikeExpectations);
                if (problems.Count > 0) { res.Error = "spike reflection: " + string.Join("; ", problems); yield break; }
                if (!barkPatched)
                {
                    barkPatched = true;
                    try { harmony.Patch(AccessTools.Method(typeof(UnitAsksComponent.Bark), "Play"), prefix: new HarmonyMethod(typeof(HarnessRunner), nameof(SpikeBarkPrefix))); }
                    catch (Exception ex) { res.Error = "could not observe barks: " + ex.Message; yield break; }
                }
                var main = game.Player.MainCharacter.Value;

                // ---- spawn one copy per candidate through RRT's GuestPresence ----------------------------------------------
                var units = game.State.LoadedAreaState.AllEntityData.OfType<UnitEntityData>().Where(u => !u.Destroyed && !u.IsDisposed).ToList();
                int seat = 0;
                // Locator mode (engine queue 9d): every copy stands on the plan's native locator, as an E12b At.Locator presence.
                Vector3? locatorAt = null;
                res.Locator = sp.Locator;
                res.MaxWalkableGap = sp.MaxWalkableGap;
                if (sp.NearUnit != null)
                {
                    var nearGuid = Kingmaker.Blueprints.BlueprintGuid.Parse(sp.NearUnit);
                    var near = units.Where(u => u.Blueprint?.AssetGuid == nearGuid && !u.Destroyed && !u.DestroyMark && !u.IsDisposed && u.IsInGame && !u.State.IsDead && !u.State.IsFinallyDead).Take(2).ToArray();
                    if (near.Length != 1) { res.LocatorError = "anchor unit " + sp.NearUnit + ": " + near.Length + " live matches in " + area.name; yield break; }
                    double r = near[0].Orientation * Math.PI / 180.0;
                    float fx = (float)Math.Sin(r), fz = (float)Math.Cos(r), rx = fz, rz = -fx, dx, dz;
                    switch (sp.Side) { case "left": dx = -rx; dz = -rz; break; case "right": dx = rx; dz = rz; break; case "behind": dx = -fx; dz = -fz; break; default: dx = fx; dz = fz; break; }
                    locatorAt = near[0].Position + new Vector3(dx * sp.AnchorDistance, 0f, dz * sp.AnchorDistance);
                    res.Notes.Add("anchor " + near[0].Blueprint.name + " at " + near[0].Position + " orientation " + near[0].Orientation + " -> " + sp.Side + " " + sp.AnchorDistance + " m = " + locatorAt.Value);
                    res.Locator = "near:" + sp.NearUnit + ":" + sp.Side + ":" + sp.AnchorDistance;
                }
                else if (sp.Locator != null)
                {
                    var entity = Kingmaker.EntitySystem.EntityService.Instance.GetEntity(sp.Locator);
                    if (entity == null || entity.Destroyed) { res.LocatorError = "not found in " + area.name; yield break; }
                    locatorAt = entity.Position;
                }
                foreach (var guid in sp.Units)
                {
                    var bp = Bp<BlueprintUnit>(guid);
                    if (bp == null) { res.Skipped.Add(guid + ": not a BlueprintUnit"); continue; }
                    if (units.Any(u => (u.OriginalBlueprint == bp || u.Blueprint == bp) && !u.State.IsDead)) { res.Skipped.Add(bp.name + ": a live unit of it is already in the area"); continue; }
                    var probe = new QuietCopyProbe { Unit = guid, UnitName = bp.name, NativeFaction = bp.Faction?.name, NativeAsks = bp.Visual?.Barks?.name };
                    res.Copies.Add(probe);
                    var at = locatorAt ?? main.Position + Quaternion.Euler(0f, 90f * seat, 0f) * Vector3.forward * sp.Distance;
                    seat++;
                    if (locatorAt != null)
                    {
                        probe.Target = new[] { at.x, at.y, at.z };
                        try
                        {
                            var node = Kingmaker.View.ObstacleAnalyzer.GetNearestNode(at);
                            if (node.node != null) probe.WalkableGap = Vector3.Distance(at, node.position);
                        }
                        catch (Exception ex) { res.Notes.Add(bp.name + ": walkable query threw " + ex.Message); }
                    }
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
                var shotAt = new List<(Vector3 Position, string Name)>();
                foreach (var (guest, probe) in guests.Where(g => g.Probe.Spawned))
                {
                    if (!(RrtBridge.PresenceActor(guest) is UnitEntityData copy))
                    {
                        probe.Error = "the engine has no actor for its copy after spawning (" + RrtBridge.PresenceStatus(guest) + ")";
                        continue;
                    }
                    copies.Add((copy, probe));
                    spikeBarks[copy] = probe.Barks;
                    probe.Exists = copy.IsInGame && !copy.Destroyed && !copy.State.IsDead && game.State.LoadedAreaState.AllEntityData.Contains(copy);
                    probe.Faction = copy.Descriptor.Faction?.name;
                    probe.PlayerFaction = copy.Descriptor.Faction == BlueprintRoot.Instance.PlayerFaction;
                    probe.PartyGroup = main != null && ReferenceEquals(copy.Group, main.Group);
                    probe.Passive = copy.Passive;
                    probe.Asks = copy.Descriptor.Asks?.name ?? "(none)";
                    probe.AsksSilent = Silent(copy.View?.Asks);
                    if (locatorAt != null)
                    {
                        probe.Drift = Vector3.Distance(copy.Position, locatorAt.Value);
                        probe.Corpulence = copy.View?.Corpulence;
                        float room = (probe.Corpulence ?? 0f) + 1f;
                        foreach (var other in game.State.LoadedAreaState.AllEntityData.OfType<UnitEntityData>())
                        {
                            if (ReferenceEquals(other, copy) || !other.IsInGame || other.Destroyed || other.State.IsDead || other.View == null) continue;
                            float gap = new Vector2(other.Position.x - copy.Position.x, other.Position.z - copy.Position.z).magnitude;
                            if (gap < room + other.View.Corpulence) probe.Crowding.Add(other.CharacterName + " " + gap.ToString("0.0") + " m");
                        }
                        if (plan.Screenshots) shotAt.Add((copy.Position, "presence__" + probe.UnitName));
                    }
                }
                foreach (var (position, name) in shotAt)
                {
                    try { game.UI.GetCameraRig().ScrollToImmediately(position); } catch (Exception ex) { res.Notes.Add("camera: " + ex.Message); }
                    yield return null;
                    yield return Shot(name, res.Screenshots, res.Notes.Add);
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
