using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class EmberAfternoonsTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var scenes = new[] { "drawing", "visitor", "rain", "paper_bird", "missing_cloth", "courtyard_play", "after_applause", "second_ending" }
            .Select(id => story.Scenes.Single(s => s.Id == "ember." + id)).ToArray();
        var start = new Snapshot { Chapter = 3, Hour = 1000, Area = scenes[0].Areas.Single() };
        start.Flags.UnionWith(new[] { "ember.present", "seelah.committed", "konomi.committed" });
        var states = new List<Snapshot> { start };
        foreach (var scene in scenes)
        {
            var continuing = new List<Snapshot>();
            foreach (var input in states)
            {
                var state = Program.Copy(input); state.Hour += scene.DelayHours;
                check(Rules.Available(story, scene, state), "Ember friendship cannot continue: " + scene.Id);
                foreach (var result in Program.Walk(scene, state))
                {
                    check(result.Has("seelah.committed") && result.Has("konomi.committed") && !result.Has("ember.lovers"), "Ember friendship alters unrelated romances or invents a lover state.");
                    if (!result.Has(scene.Id))
                    {
                        check(result.Flags.SetEquals(state.Flags), "Ember postponed visit records unplayed events.");
                        continue;
                    }
                    check(!Rules.Available(story, scene, result), "Ember repeats a finished afternoon.");
                    if (scene.Id == "ember.paper_bird") check(result.Has("ember.player_fox") != result.Has("ember.player_narrates"), "Ember rehearsal loses performer roles.");
                    if (scene.Id == "ember.missing_cloth") check(result.Has("ember.stage_road") != result.Has("ember.stage_waited"), "Ember rehearsal loses schedule choice.");
                    if (scene.Id == "ember.second_ending")
                    {
                        check(result.Has("ember.puppet_afternoons_kept"), "Ember revision has no played conclusion.");
                        check(result.Has("ember.puppet_more") != result.Has("ember.puppet_quiet"), "Ember friendship loses the next-activity preference.");
                    }
                    continuing.Add(result);
                }
            }
            check(continuing.Count > 0, "Ember scene has no completed path.");
            states = continuing;
        }
        foreach (var scene in scenes.Skip(3))
        {
            var ready = Program.Copy(start); ready.Flags.UnionWith(scene.Requires);
            foreach (string blocked in new[] { "ember.closed", "ember_dead", "ember_gone", "ember.absent" })
            {
                var state = Program.Copy(ready); state.Flags.Add(blocked);
                check(!Rules.Available(story, scene, state), "Ember afternoon ignores " + blocked);
            }
            foreach (string required in scene.Requires)
            {
                var state = Program.Copy(ready); state.Flags.Remove(required);
                check(!Rules.Available(story, scene, state), "Ember afternoon skips " + required);
            }
            ready.Times[scene.Requires.Last()] = ready.Hour;
            ready.Hour += scene.DelayHours - 1;
            check(!Rules.Available(story, scene, ready), "Ember afternoon skips delay.");
            ready.Hour++;
            check(Rules.Available(story, scene, ready), "Ember afternoon misses exact delay boundary.");
            ready.Chapter = 5;
            check(!Rules.Available(story, scene, ready), "Ember early friendship ignores later native outcomes.");
            ready.Chapter = 3; ready.Area = "elsewhere";
            check(!Rules.Available(story, scene, ready), "Ember courtyard appears outside Drezen.");
        }
    }
}
