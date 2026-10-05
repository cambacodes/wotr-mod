using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng8-q8f: actual return choices -> placement -> offered hub entry -> completion.
internal static class GameplayEntryInventoryTests
{
    private const string P = "terendelev.trickster.", Returned = P + "returned";
    private const string Hub = "terendelev.presence", Fallback = "terendelev.presence.awning";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";

    internal static void Run(Story story, Action<bool, string> check)
    {
        using var contract = JsonDocument.Parse(File.ReadAllText("tools/gameplay_entry_inventory_contracts.json"));
        var ids = contract.RootElement.GetProperty("entries").EnumerateArray().Select(r => r.GetProperty("scene").GetString()!).ToArray();
        foreach (bool fallback in new[] { false, true })
        {
            var world = new InventoryWorldBuilder(story, 4, "");
            world.Native("trickster");
            world.Advance(24);
            world = world.Earn(P + "wound.weeps", P + "blood_tested");
            world.Travel(5, "");
            world.Native("iz.terendelev_battle");
            world = world.Earn(P + "bones.restitution", Returned);
            check(world.State.Has(P + "cost.wound_open") && world.State.Has(Returned),
                "eng8-q8f: contact content must follow the enacted blood return");
            world.Native("iz.done");
            world.Travel(5, Drezen);
            if (fallback) { world.MissingAnchor(Hub); world.Anchor(Fallback); }
            else world.Anchor(Hub);
            world.TickRoute("terendelev");
            string hub = fallback ? Fallback : Hub;
            string suffix = fallback ? "_awning" : "";
            check(world.Observe(hub).CopyAlive && world.State.AvailableContacts.Contains(story.Presences[hub].Unit),
                "eng8-q8f: entry requires successful actual placement " + hub);
            world.Advance(300);
            var returned = world.Copy();
            var first = world.Earn(P + "after.first_night" + suffix, P + "first_night_seen");
            first.Advance(300);
            var dressed = first.Earn(P + "watch.proof" + suffix, P + "watch.proof_seen");
            dressed.Advance(300);
            var committed = dressed.Earn(P + "commit" + suffix, "terendelev.committed");
            committed.Advance(300);
            var night = committed.Earn(P + "night.watch" + suffix, P + "night.seen");
            night.Advance(300);
            foreach (var original in ids)
            {
                var before = original.EndsWith("watch.road") || original.Contains("react.galfrey") ? returned.Copy()
                    : original.Contains("letter.") ? night.Copy()
                    : original.EndsWith("watch.at_the_gate") ? committed.Copy() : dressed.Copy();
                string id = original + suffix;
                var scene = before.Scene(id);
                check(!scene.ManualOnly && !Rules.IsRemote(scene) && scene.Entry.Length > 0
                    && Rules.PresenceHubAvailable(story, hub, scene, before.State),
                    "eng8-q8f: hub must offer the in-world entry " + id);
                var after = before.Walk(id).First(w => w.State.Has(id));
                check(after.State.RestSpent.OrderBy(k => k.Key).SequenceEqual(before.State.RestSpent.OrderBy(k => k.Key)),
                    "eng8-q8f: contact handovers spend no extra chapter rest " + id);
                check(!after.Available(original + (fallback ? "" : "_awning")),
                    "eng8-q8f: both handovers cannot complete " + id);
                var absent = before.Copy();
                foreach (var actor in absent.Actors.Where(a => a.Presence == hub)) actor.Destroyed = true;
                absent.Refresh();
                check(!absent.Available(id), "eng8-q8f: manual readability cannot replace missing contact " + id);
                var closed = before.Copy(); closed.Checkpoint("explicit route closure", "terendelev.closed");
                check(!closed.Available(id), "eng8-q8f: closure cannot borrow the earned contact " + id);
                var laterChapter = before.Copy(); laterChapter.Travel(6, Drezen);
                check(!laterChapter.Available(id), "eng8-q8f: Chapter 5 contact entry cannot move into Chapter 6 " + id);
                if (original.EndsWith("watch.road"))
                {
                    var beforeIz = before.Copy(); beforeIz.State.Flags.Remove("iz.done"); beforeIz.Refresh();
                    var late = before.Copy(); late.Checkpoint("existing late return exclusion", P + "cost.late");
                    check(!beforeIz.Available(id) && !late.Available(id),
                        "eng8-q8f: road needs completed Iz and excludes the late return " + id);
                }
            }
            var unpaid = new InventoryWorldBuilder(story, 5, Drezen);
            unpaid.Native("trickster"); unpaid.Anchor(hub); unpaid.TickRoute("terendelev");
            check(!unpaid.State.Has(Returned) && ids.All(id => !unpaid.Available(id + suffix)),
                "eng8-q8f: no entry without the earned return " + hub);
        }
        Console.WriteLine("PASS: eng8-q8f earned gameplay entries at primary/fallback contacts");
    }
}
