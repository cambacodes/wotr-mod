using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class TirabadeAfterRoadsTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == id);
        var ids = new[] { "three_borrowed_names", "three_back_of_seal", "three_beth_account", "three_counterclaim", "three_unposted_notice", "three_rooms_unlocked" };
        var observed = new HashSet<string>();
        foreach (int chapter in new[] { 3, 5 })
        foreach (bool followed in new[] { false, true })
        {
            var state = new Snapshot { Chapter = chapter, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(new[] { "three_small_journeys.kept", "kept_terms", "committed", "seelah.committed", "three_small_journeys.water" });
            foreach (string id in new[] { "three_stolen_roads", "three_lantern_debt", "three_beth_steps", "three_ista_departure", "three_lantern_turn", "three_open_road" })
            {
                var prior = Find(id); state.Hour += prior.DelayHours;
                check(Rules.Available(story, prior, state), "After-roads predecessor unavailable: " + id);
                state = Program.Walk(prior, state).First(s => s.Has(id) && s.Has("three_stolen_roads.followed") == followed);
            }
            var states = new List<Snapshot> { state };
            foreach (string id in ids)
            {
                var scene = Find(id);
                var next = new List<Snapshot>();
                foreach (var input in states)
                {
                    var ready = Program.Copy(input); ready.Hour += scene.DelayHours;
                    check(Rules.Available(story, scene, ready), "After-roads played history stranded: " + id);
                    foreach (var result in Program.Walk(scene, ready))
                    {
                        check(result.Has("committed") && result.Has("seelah.committed") && !result.Has("closed"), "After-roads changes an existing relationship.");
                        check(result.Has("three_stolen_roads.followed") == followed, "After-roads rewrites the theft history.");
                        if (!result.Has(id))
                        {
                            check(result.Flags.SetEquals(ready.Flags), "After-roads postponement writes progress.");
                            continue;
                        }
                        observed.UnionWith(result.Flags);
                        next.Add(result);
                    }
                }
                check(next.Count > 0, "After-roads has no complete continuing paths.");
                states = next.GroupBy(s => string.Join("|", s.Flags.OrderBy(f => f))).Select(g => g.First()).ToList();
            }
            check(states.All(s => s.Has("three_rooms_unlocked.kept")), "After-roads loses final completion.");
            check(states.All(s => new[] { "three_rooms_unlocked.night", "three_rooms_unlocked.rest", "three_rooms_unlocked.walk" }.Count(s.Has) == 1), "After-roads loses the chosen intimacy boundary.");
        }
        foreach (string flag in new[] { "three_back_of_seal.impression", "three_back_of_seal.unreadable", "three_back_of_seal.catalogue", "three_counterclaim.refunded", "three_counterclaim.partial", "three_counterclaim.unpaid" })
            check(observed.Contains(flag), "After-roads missed an investigation or settlement outcome: " + flag);
        foreach (string id in ids)
        {
            var scene = Find(id);
            var ready = new Snapshot { Chapter = 3, Area = scene.Areas.Single(), Hour = 1000 };
            ready.Flags.UnionWith(scene.Requires);
            check(Rules.Available(story, scene, ready), "After-roads baseline unavailable.");
            foreach (string blocker in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                check(!Rules.Available(story, scene, blocked), "After-roads ignores blocker: " + blocker);
            }
        }
    }
}
