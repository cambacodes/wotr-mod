using System;
using System.Linq;
using System.Reflection;
using Kingmaker;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using UnityEngine;
using Newtonsoft.Json;

namespace RRT.TestHarness
{
    internal sealed partial class HarnessRunner
    {
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
    }
}
