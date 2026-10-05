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
        public string? ActorId, Report, Error;
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
            yield return WaitFor(() => Wanted() && Actor() is UnitEntityData a && a.IsInGame && !a.State.IsDead,
                plan.Presence!.SettleSeconds, ok, 30);
            probe.Wanted = Wanted();
            probe.Report = string.Join("; ", rrt!.PresenceReport().Where(s => s.StartsWith(probe.Key + " ", StringComparison.Ordinal)));
            var actor = Actor();
            if (!ok.Value || actor == null) { probe.Error = "production actor missing; fixture gates/anchor did not resolve"; yield break; }
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
