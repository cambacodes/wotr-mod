using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KianaConsequencesTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var scenes = new[] { "guest_table", "market_weather", "lenna_door", "blue_room" }
            .Select(id => story.Scenes.Single(s => s.Id == "kiana." + id)).ToArray();
        foreach (string history in new[] { "wait", "affair", "widow" })
        foreach (bool committed in new[] { false, true })
        foreach (bool otherLoss in new[] { false, true })
        {
            var initial = new Snapshot { Chapter = 5, Hour = 1000, Area = scenes[0].Areas.Single() };
            initial.AvailableContacts.Add("180b0eaa5dce387458d2ebf0ee943985");
            initial.Flags.UnionWith(Program.Prerequisites(scenes[0]));
            initial.Flags.Add("seelah.committed");
            if (committed) initial.Flags.Add("kiana.committed");
            if (otherLoss) initial.Flags.Add("loss");
            if (history == "widow") initial.Flags.UnionWith(new[] { "kiana.bereaved", "seelah.elan_dead" });
            else initial.Flags.UnionWith(new[] { "kiana.separated", history == "wait" ? "kiana.waited" : "kiana.affair" });
            var states = new List<Snapshot> { initial };
            foreach (var scene in scenes)
            {
                var continuing = new List<Snapshot>();
                foreach (var input in states)
                {
                    var state = Program.Copy(input); state.Hour += scene.DelayHours;
                    check(Rules.Available(story, scene, state), "Kiana consequences strand a valid marital history: " + history + "/" + scene.Id);
                    foreach (var result in Program.Walk(scene, state))
                    {
                        foreach (string flag in new[] { "kiana.committed", "kiana.separated", "kiana.bereaved", "seelah.elan_dead", "seelah.committed", "loss" })
                            check(result.Has(flag) == initial.Has(flag), "Kiana consequences rewrite history: " + flag);
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(state.Flags), "Kiana postponed meeting writes progress.");
                            continue;
                        }
                        check(!Rules.Available(story, scene, result), "Kiana consequence repeats completed event.");
                        if (scene.Id == "kiana.blue_room")
                        {
                            check(result.Has("kiana.blue_room.ready") && result.Has("kiana.roof_supper.kept") && result.Has("kiana.consequences_ready"), "Getting ready ends the book before the same-evening supper.");
                            check(new[] { "performed", "told", "quiet" }.Count(f => result.Has("kiana.roof_supper." + f)) == 1, "Kiana supper loses its chosen activity.");
                        }
                        continuing.Add(result);
                    }
                }
                check(continuing.Count > 0, "Kiana consequence has no completed path.");
                states = continuing;
            }
        }
        check(!story.Scenes.Any(s => s.Id == "kiana.roof_supper"), "Same-evening supper requires a second rest.");
        foreach (var scene in scenes)
        {
            var ready = new Snapshot { Chapter = 5, Hour = 1000, Area = scene.Areas.Single() };
            ready.AvailableContacts.Add("180b0eaa5dce387458d2ebf0ee943985");
            ready.Flags.UnionWith(Program.Prerequisites(scene));
            foreach (string blocker in new[] { "kiana.closed", "kiana.farewell", "inhuman" })
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                check(!Rules.Available(story, scene, blocked), "Kiana consequence ignores " + blocker);
            }
            foreach (string flag in scene.Requires)
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(flag);
                check(!Rules.Available(story, scene, missing), "Kiana consequence skips " + flag);
            }
            foreach (var group in scene.RequiresAnyGroups)
            {
                var missing = Program.Copy(ready); missing.Flags.ExceptWith(group);
                check(!Rules.Available(story, scene, missing), "Kiana consequence skips " + string.Join("|", group));
            }
            ready.Chapter = 4;
            check(!Rules.Available(story, scene, ready), "Kiana consequence appears before soul aftermath.");
            ready.Chapter = 5; ready.Area = "elsewhere";
            check(!Rules.Available(story, scene, ready), "Kiana consequence ignores Drezen location.");
        }
    }
}
