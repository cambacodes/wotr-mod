using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class TirabadeCampaignTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        foreach (bool bethFirst in new[] { true, false })
        foreach (int chapter in new[] { 3, 5 })
        foreach (bool earlierBread in new[] { false, true })
        {
            var ids = new[] { "three_yard", "three_match", bethFirst ? "three_beth_score" : "three_anevia_flour", bethFirst ? "three_anevia_flour" : "three_beth_score", "three_return_game", "three_small_journeys" };
            var initial = new Snapshot { Chapter = chapter, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            initial.Flags.UnionWith(new[] { "three_outing.kept", "kept_terms", "committed", "seelah.committed" });
            if (earlierBread) initial.Flags.Add("a_errand");
            var breadChoice = story.Scenes.Single(s => s.Id == "three_anevia_flour").Nodes.Single(n => n.Id == "want").Choices.Single(c => c.Next == "old_crust");
            check(Rules.Match(breadChoice.Requires, breadChoice.Forbids, initial) == earlierBread, "Bakery lesson invents an earlier shared loaf.");
            var states = new List<Snapshot> { initial };
            foreach (string id in ids)
            {
                var scene = story.Scenes.Single(s => s.Id == id);
                var continuing = new List<Snapshot>();
                foreach (var input in states)
                {
                    var state = Program.Copy(input);
                    int latest = scene.Requires.Where(state.Times.ContainsKey).Select(f => state.Times[f]).DefaultIfEmpty(0).Max();
                    state.Hour = Math.Max(state.Hour, latest + scene.DelayHours);
                    check(Rules.Available(story, scene, state), "Tirabade campaign stranded in individual-scene order: " + id);
                    foreach (var result in Program.Walk(scene, state))
                    {
                        check(result.Has("committed") && result.Has("seelah.committed") && !result.Has("closed"), "Tirabade leisure changes commitments.");
                        if (!result.Has(id))
                        {
                            check(result.Flags.SetEquals(state.Flags), "Tirabade postponement records unplayed events.");
                            continue;
                        }
                        check(!Rules.Available(story, scene, result), "Tirabade leisure repeats a completed event.");
                        if (result.Has("three_match.finished"))
                        {
                            check(result.Has("three_match.stood") != result.Has("three_match.replayed"), "Tirabade disputed score loses its decision.");
                            check(result.Has("three_match.pennant") == result.Has("three_match.stood"), "Tirabade match rewrites the winning result.");
                        }
                        if (id == "three_small_journeys")
                        {
                            check(result.Has("three_small_journeys.kept"), "Tirabade journey planning lacks completion.");
                            check(new[] { "night", "quiet", "later_promise" }.Count(f => result.Has("three_small_journeys." + f)) == 1, "Tirabade evening loses the chosen conclusion.");
                        }
                        continuing.Add(result);
                    }
                }
                check(continuing.Count > 0, "Tirabade campaign has no continuing path.");
                states = continuing;
            }
        }
        foreach (var scene in story.Scenes.Where(s => new[] { "three_yard", "three_match", "three_beth_score", "three_anevia_flour", "three_return_game", "three_small_journeys" }.Contains(s.Id)))
        {
            var ready = new Snapshot { Chapter = 5, Hour = 1000, Area = scene.Areas.Single() };
            ready.Flags.UnionWith(scene.Requires);
            check(Rules.Available(story, scene, ready), "Tirabade scene readiness fixture invalid.");
            foreach (string required in scene.Requires)
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(required);
                check(!Rules.Available(story, scene, missing), "Tirabade skips prerequisite " + required);
            }
            foreach (string blocker in new[] { "closed", "loss", "inhuman", "irabeth_away", "anevia_away", "last_watch", "anevia_dead", "irabeth_dead", "anevia_gone", "irabeth_gone", "swarm", "true_lich" })
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                check(!Rules.Available(story, scene, blocked), "Tirabade scene ignores " + blocker);
            }
            ready.Times[scene.Requires.Last()] = 1000;
            ready.Hour = 1000 + scene.DelayHours - 1;
            check(!Rules.Available(story, scene, ready), "Tirabade scene opens before its delay.");
            ready.Hour++;
            check(Rules.Available(story, scene, ready), "Tirabade scene misses exact delay boundary.");
            ready.Chapter = 4;
            check(!Rules.Available(story, scene, ready), "Tirabade yard appears in the Abyss.");
            ready.Chapter = 5; ready.Area = "elsewhere";
            check(!Rules.Available(story, scene, ready), "Tirabade yard appears outside Drezen.");
        }
    }
}
