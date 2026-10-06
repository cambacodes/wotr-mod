using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class AivuOpeningTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        string[] ids = { "a_city_with_wings", "the_roof_below", "a_way_for_feet", "someone_elses_turn" };
        var scenes = ids.Select(id => story.Scenes.Single(s => s.Id == "aivu." + id)).ToArray();
        const string unit = "32a037e97c3d5c54b85da8f639616c57";
        var reached = new HashSet<string>();
        var outcomes = new HashSet<string>();
        var initial = new Snapshot { Chapter = 3, Hour = 1000, Area = scenes[0].Areas.Single() };
        initial.Flags.UnionWith(new[] { "azata", "seelah.committed", "committed" });
        initial.AvailableContacts.Add(unit);
        var states = new List<Snapshot> { initial };
        foreach (var scene in scenes)
        {
            var next = new List<Snapshot>();
            foreach (var previous in states)
            {
                var ready = Program.Copy(previous);
                ready.Hour += scene.DelayHours;
                check(Program.CurrentAvailable(story, scene, ready), "Aivu earned predecessor does not unlock " + scene.Id);
                if (scene.DelayHours > 0)
                {
                    var early = Program.Copy(ready); early.Hour--;
                    check(!Program.CurrentAvailable(story, scene, early), "Aivu delay boundary ignored.");
                }
                foreach (var result in Program.Walk(scene, ready, (page, state) =>
                {
                    reached.Add(scene.Id + "/" + page);
                    check(state.Flags.SetEquals(ready.Flags), "Aivu interrupted page commits unplayed consequences.");
                    check(Program.CurrentAvailable(story, scene, state), "Aivu incomplete visit cannot be replayed.");
                    foreach (var unavailable in story.Relationships["aivu"].UnavailableFlags)
                    {
                        var absent = Program.Copy(state); absent.Flags.Add(unavailable);
                        check(!Rules.ContactAvailable(story, scene, absent), "Aivu continues during native absence: " + unavailable);
                    }
                    var lost = Program.Copy(state); lost.AvailableContacts.Clear();
                    check(!Rules.ContactAvailable(story, scene, lost), "Aivu uses absent pet.");
                    if (page == "space") check(state.Has("aivu.jori_space"), "Aivu invents Jori's repair history.");
                    if (page == "talked") check(state.Has("aivu.jori_talked"), "Aivu invents Jori's conversation.");
                    if (page == "open") check(state.Has("aivu.shortcut_open"), "Aivu claims blocked passage repaired.");
                    if (page == "blocked") check(state.Has("aivu.shortcut_marked"), "Aivu forgets opened passage.");
                }))
                {
                    check(initial.Flags.All(result.Has), "Aivu changes native path or existing romances.");
                    if (!result.Has(scene.Id))
                    {
                        check(result.Flags.SetEquals(ready.Flags), "Aivu defer changes outcome flags.");
                        continue;
                    }
                    check(!Program.CurrentAvailable(story, scene, result), "Aivu completed visit replays.");
                    next.Add(result);
                    outcomes.UnionWith(result.Flags);
                }
            }
            states = next.GroupBy(x => string.Join("|", x.Flags.OrderBy(f => f))).Select(g => g.First()).ToList();
            check(states.Count > 0, "Aivu has no completed path.");
        }
        foreach (var state in states)
        {
            check(state.Has("aivu.opening_kept") && state.Has("aivu.trusted"), "Aivu opening lacks earned friendship outcome.");
            check(state.Has("aivu.laundry_copy") != state.Has("aivu.garden_next"), "Aivu final desires collapse.");
            check(state.Has("aivu.shortcut_open") != state.Has("aivu.shortcut_marked"), "Aivu clearance and refusal overlap.");
        }
        foreach (string flag in new[] { "map_both_names", "map_two_sides", "jori_space", "jori_talked", "cart_whole", "cart_dismantled", "shortcut_marked", "laundry_copy", "garden_next" })
            check(outcomes.Contains("aivu." + flag), "Unreachable Aivu consequence: " + flag);
        foreach (var scene in scenes)
        {
            check(scene.ContactUnit == unit && !scene.Remote, "Aivu pet identity replaced.");
            foreach (var page in scene.Nodes)
                check(reached.Contains(scene.Id + "/" + page.Id), "Unreached Aivu page: " + scene.Id + "/" + page.Id);
            var ready = Program.Copy(initial); ready.Flags.UnionWith(scene.Requires);
            check(Program.CurrentAvailable(story, scene, ready), "Aivu gate baseline invalid.");
            foreach (var flag in scene.Requires.Where(requiredKey => !requiredKey.EndsWith(".present_now", StringComparison.Ordinal) && !requiredKey.EndsWith(".reachable_by_letter", StringComparison.Ordinal)))
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(flag);
                check(!Program.CurrentAvailable(story, scene, missing), "Aivu missing prerequisite ignored: " + flag);
            }
            foreach (var flag in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag);
                check(!Program.CurrentAvailable(story, scene, blocked), "Aivu blocker ignored: " + flag);
            }
            foreach (int chapter in new[] { 2, 4, 5, 6 })
            {
                var wrong = Program.Copy(ready); wrong.Chapter = chapter;
                check(!Program.CurrentAvailable(story, scene, wrong), "Aivu opening borrows later captivity history.");
            }
            var trickster = Program.Copy(ready); trickster.Flags.Remove("azata"); trickster.Flags.Add("trickster");
            check(!Program.CurrentAvailable(story, scene, trickster), "Aivu pretends Trickster owns Azata pet.");
            var elsewhere = Program.Copy(ready); elsewhere.Area = "elsewhere";
            check(!Program.CurrentAvailable(story, scene, elsewhere), "Aivu Drezen outing starts elsewhere.");
        }
    }
}
