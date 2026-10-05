using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using Kingmaker;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic.Commands;
using UnityEngine;

namespace RRT.TestHarness
{
    public sealed class ProductionPresenceProbe
    {
        public string Key = "";
        public string? ActorId, Report, Error, Diagnostic;
        public List<string> Trace = new List<string>();
        public float[]? Position, Target;
        public float? WalkableGap, Drift, ApproachDistance;
        public bool Wanted, Clickable;
        public List<string> Crowding = new List<string>();
        public IEnumerable<string> Failures()
        {
            if (Error != null) yield return Error;
            if (!Wanted) yield return "production presence not wanted by route state";
            if (ActorId == null) yield return "production actor absent";
            if (WalkableGap == null || WalkableGap > 1.5f) yield return "production spot not walkable within 1.5 m";
            if (Drift == null || Drift > 1.5f) yield return "production actor drift exceeds 1.5 m";
            if (ApproachDistance == null || ApproachDistance > 2f) yield return "Commander did not approach within 2 m";
            if (Crowding.Count > 0) yield return "production body room blocked: " + string.Join("; ", Crowding);
            if (!Clickable) yield return "production hub click did not open a dialog";
        }
    }

    internal sealed partial class HarnessRunner
    {
        // Inspect the actual runtime presence. No forced Tick, translocation or cloned probe actor.
        IEnumerator InspectProductionPresence(ProductionPresenceProbe probe)
        {
            var ok = new Box<bool>();
            UnitEntityData? Actor() => rrt?.ProductionPresence(probe.Key) is object guest
                ? RrtBridge.PresenceActor(guest) as UnitEntityData : null;
            bool Wanted() => rrt!.PresenceReport().Any(s => s.StartsWith(probe.Key + " [", StringComparison.Ordinal)
                && s.Contains("] wanted;"));
            // Diagnostic trace of the first seconds: report line plus every copy's usability inputs.
            for (int i = 0; i < 40 && Environment.GetEnvironmentVariable("RRT_HARNESS_TRACE") == "1"; i++)
            {
                var g1 = rrt!.ProductionPresence(probe.Key);
                string? bp = g1 == null ? null : RrtBridge.PresenceUnit(g1);
                var m1 = Game.Instance.Player.MainCharacter.Value;
                var us = Game.Instance.State.Units.Where(x => x.Blueprint?.AssetGuid.ToString() == bp || x.OriginalBlueprint?.AssetGuid.ToString() == bp)
                    .Select(u => u.UniqueId.Substring(0, 6) + (u.IsInGame ? " in" : " out") + (u.View != null && u.View.gameObject.activeInHierarchy ? " act" : " inact") + (u.IsEnemy(m1) ? " ENEMY" : "")).ToArray();
                probe.Trace.Add(i + " " + string.Join("; ", rrt.PresenceReport().Where(x => x.StartsWith(probe.Key + " ", StringComparison.Ordinal))) + " || cmd=" + m1.Position + " || " + string.Join(",", us) + " || " + (bp == null ? "" : rrt.ContactInventory(bp)));
                yield return new Wait(0.25f);
            }
            // A copy spawned far from the Commander keeps its view inactive (not a usable contact) until the player is
            // near, so walk the Commander to the placed spot first, as a player would, then wait for the contact.
            yield return WaitFor(() => Wanted() && rrt!.ProductionPresence(probe.Key) is object g0
                && (Vector3)RrtBridge.PresenceTarget(g0)! != Vector3.zero, plan.Presence!.SettleSeconds, ok, 30);
            if (ok.Value && Actor() == null)
            {
                var walker = Game.Instance.Player.MainCharacter.Value;
                var spot = (Vector3)RrtBridge.PresenceTarget(rrt!.ProductionPresence(probe.Key)!)!;
                walker.Commands.Run(new UnitMoveTo(spot));
                yield return WaitFor(() => Actor() != null || Vector3.Distance(walker.Position, spot) <= 2f,
                    plan.Presence.EntrySeconds, ok, 30);
            }
            yield return WaitFor(() => Wanted() && Actor() is UnitEntityData a && a.IsInGame && !a.State.IsDead,
                plan.Presence!.SettleSeconds, ok, 30);
            probe.Wanted = Wanted();
            probe.Report = string.Join("; ", rrt!.PresenceReport().Where(s => s.StartsWith(probe.Key + " ", StringComparison.Ordinal)));
            var actor = Actor();
            if (!ok.Value || actor == null)
            {
                try
                {
                    var g = rrt.ProductionPresence(probe.Key);
                    string? unit = g == null ? null : RrtBridge.PresenceUnit(g);
                    var m = Game.Instance.Player.MainCharacter.Value;
                    var lines = new List<string> { "combat=" + Game.Instance.Player.IsInCombat + " commanderConscious=" + m.State.IsConscious };
                    foreach (var u in Game.Instance.State.Units.Where(x => x.Blueprint?.AssetGuid.ToString() == unit || x.OriginalBlueprint?.AssetGuid.ToString() == unit))
                    {
                        var h = u.HoldingState;
                        lines.Add(u.UniqueId + " pos=" + u.Position + " dead=" + u.State.IsDead + " inGame=" + u.IsInGame + " destroyed=" + u.Destroyed + "/" + u.DestroyMark
                            + " susp=" + u.Suppressed + " conscious=" + u.State.IsConscious + " enemy=" + u.IsEnemy(m) + " view=" + (u.View != null)
                            + " viewActive=" + (u.View != null && u.View.gameObject.activeInHierarchy) + " viewScene=" + (u.View != null && u.View.gameObject.scene.isLoaded)
                            + " holding=" + (h == null ? "none" : h.IsSceneLoaded.ToString()));
                    }
                    probe.Diagnostic = string.Join(" | ", lines);
                }
                catch (Exception ex) { probe.Diagnostic = "diag failed: " + ex.Message; }
                probe.Error = "production actor missing; fixture gates/anchor did not resolve"; yield break; }
            yield return new Wait(2f);
            probe.ActorId = actor.UniqueId;
            var guest = rrt.ProductionPresence(probe.Key)!;
            var target = (Vector3)RrtBridge.PresenceTarget(guest)!;
            probe.Target = new[] { target.x, target.y, target.z };
            probe.Position = new[] { actor.Position.x, actor.Position.y, actor.Position.z };
            var nearest = Kingmaker.View.ObstacleAnalyzer.GetNearestNode(target);
            if (nearest.node != null) probe.WalkableGap = Vector3.Distance(target, nearest.position);
            probe.Drift = Vector3.Distance(actor.Position, target);
            var main = Game.Instance.Player.MainCharacter.Value;
            var direction = (main.Position - actor.Position).normalized;
            if (Vector3.Distance(main.Position, actor.Position) > 2f)
            {
                main.Commands.Run(new UnitMoveTo(actor.Position + direction * 1.8f));
                yield return WaitFor(() => Vector3.Distance(main.Position, actor.Position) <= 2f,
                    plan.Presence.EntrySeconds, ok, 30);
            }
            probe.ApproachDistance = Vector3.Distance(main.Position, actor.Position);
            foreach (var other in Game.Instance.State.Units.Where(u => u.IsInGame && !u.State.IsDead
                && !ReferenceEquals(u, actor) && !ReferenceEquals(u, main)))
            {
                float minimum = actor.Corpulence + other.Corpulence + 1f;
                if (Vector3.Distance(actor.Position, other.Position) < minimum)
                    probe.Crowding.Add(other.Blueprint.name + " at " + other.Position);
            }
            if (probe.ApproachDistance <= 2f && rrt.PresenceClick(probe.Key))
            {
                yield return WaitFor(() => Game.Instance.DialogController.Dialog != null, 10, ok);
                probe.Clickable = ok.Value;
                if (plan.Screenshots)
                    yield return Shot(Safe(probe.Key) + "__production", report.Saves.Last().PresenceSpike!.Screenshots,
                        message => probe.Error = message);
                TryStopDialog();
                yield return WaitFor(() => IdleBlocker() == null, plan.Timeouts.IdleSeconds, ok, 30);
                if (!ok.Value) probe.Error = "presence hub did not close to idle";
            }
        }
    }
}
