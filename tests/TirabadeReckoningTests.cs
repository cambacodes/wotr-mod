using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class TirabadeReckoningTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var ids = new[] { "three_stolen_roads", "three_lantern_debt", "three_beth_steps", "three_ista_departure", "three_lantern_turn", "three_open_road" };
        var scenes = ids.Select(id => story.Scenes.Single(s => s.Id == id)).ToArray();
        var nativeKeys = story.Etudes.Keys.Concat(story.CompletedQuests.Keys).Concat(story.CompletedEtudes.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Distinct().ToArray();
        var observed = new HashSet<string>();
        void Callback(Scene scene, string node, Snapshot state, string target)
        {
            var eligible = scene.Nodes.Single(n => n.Id == node).Choices
                .Where(c => !c.Abort && Rules.Match(c.Requires, c.Forbids, state)).ToArray();
            check(eligible.Length == 1 && eligible[0].Next == target,
                "Tirabade callback contradicts played history: " + scene.Id + "/" + node);
        }

        foreach (bool bethFirst in new[] { false, true })
        foreach (int chapter in new[] { 3, 5 })
        foreach (string earlierWish in new[] { "water", "street" })
        {
            var ordered = new[] { scenes[0], scenes[bethFirst ? 2 : 1], scenes[bethFirst ? 1 : 2], scenes[3], scenes[4], scenes[5] };
            var start = new Snapshot { Chapter = chapter, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            start.Flags.UnionWith(new[] { "three_small_journeys.kept", "kept_terms", "committed", "seelah.committed", "trickster",
                "three_small_journeys." + earlierWish });
            start.Times["three_small_journeys.kept"] = start.Hour - ordered[0].DelayHours;
            var states = new List<Snapshot> { start };
            for (int index = 0; index < ordered.Length; index++)
            {
                var scene = ordered[index];
                var continuing = new List<Snapshot>();
                foreach (var input in states)
                {
                    var state = Program.Copy(input);
                    int latest = scene.Requires.Where(state.Times.ContainsKey).Select(f => state.Times[f]).DefaultIfEmpty(0).Max();
                    state.Hour = Math.Max(state.Hour, latest + scene.DelayHours);
                    check(Rules.Available(story, scene, state), "Tirabade reckoning strands a wife order or prior outing: " + scene.Id);
                    if (scene.Id == "three_lantern_debt") Callback(scene, "waiting", state, state.Has("three_stolen_roads.followed") ? "followed" : "secured");
                    if (scene.Id == "three_beth_steps") Callback(scene, "tessa", state, state.Has("three_stolen_roads.followed") ? "followed" : "secured");
                    if (scene.Id == "three_ista_departure") Callback(scene, "arrival", state, state.Has("three_stolen_roads.followed") ? "receipts" : "letters");
                    if (scene.Id == "three_lantern_turn")
                    {
                        Callback(scene, "coat", state, state.Has("three_beth_steps.open_coat") ? "open" : "turn");
                        Callback(scene, "beth", state, state.Has("three_beth_steps.followed") ? "follow" : "lead");
                        Callback(scene, "supper", state, state.Has("three_lantern_debt.shared_sketch") ? "sketch" : "quiet");
                    }
                    if (scene.Id == "three_open_road")
                    {
                        Callback(scene, "start", state, state.Has("three_lantern_turn.home") ? "after_home" : "after_later");
                        Callback(scene, "maps", state, state.Has("three_ista_departure.both_roads") ? "steep" : "river");
                    }
                    foreach (var result in Program.Walk(scene, state))
                    {
                        check(result.Has("committed") && result.Has("seelah.committed") && !result.Has("closed"),
                            "Civilian disagreement or private preference changes a relationship commitment.");
                        check(result.Has("three_small_journeys.water") == (earlierWish == "water")
                            && result.Has("three_small_journeys.street") == (earlierWish == "street"), "New map rewrites the earlier outing preference.");
                        check(nativeKeys.All(f => result.Has(f) == state.Has(f)), "Tirabade incident fabricates a native outcome.");
                        check(result.Flags.Except(state.Flags).All(f => ids.Any(id => f == id || f.StartsWith(id + ".", StringComparison.Ordinal))),
                            "Tirabade incident writes outside its own narrative state.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(state.Flags) && result.Times.Count == state.Times.Count
                                && Rules.Available(story, scene, result), "Postponement consumes an invitation or records unplayed events.");
                            continue;
                        }
                        check(!Rules.Available(story, scene, result), "Completed Tirabade incident can repeat.");
                        check(result.Has("three_stolen_roads.book_safe") != result.Has("three_stolen_roads.followed"),
                            "Recovered book and pursued records become contradictory outcomes.");
                        if (scene.Id != "three_stolen_roads")
                            check(result.Has("three_stolen_roads.book_safe") == state.Has("three_stolen_roads.book_safe")
                                && result.Has("three_stolen_roads.followed") == state.Has("three_stolen_roads.followed"),
                                "Later civilian scene rewrites the recovery's material cost.");
                        if (scene.Id == "three_lantern_debt")
                        {
                            check(result.Has("three_lantern_debt.private_sketch") != result.Has("three_lantern_debt.shared_sketch"), "Portrait preference is lost.");
                            check(result.Has("three_lantern_debt.nerve") != result.Has("three_lantern_debt.cost"), "Anevia's response is lost.");
                        }
                        if (scene.Id == "three_beth_steps")
                        {
                            check(result.Has("three_beth_steps.followed") != result.Has("three_beth_steps.led"), "Dance practice has contradictory roles.");
                            check(result.Has("three_beth_steps.open_coat") != result.Has("three_beth_steps.fastened_coat"), "Coat preference is lost.");
                            check(result.Has("three_beth_steps.kissed") != result.Has("three_beth_steps.held"), "Individual quiet affection becomes a compulsory kiss.");
                        }
                        if (scene.Id == "three_ista_departure")
                            check(result.Has("three_ista_departure.both_roads") != result.Has("three_ista_departure.easy_road"), "New road choice is lost.");
                        if (scene.Id == "three_lantern_turn")
                        {
                            check(result.Has("three_lantern_turn.close") != result.Has("three_lantern_turn.quick"), "Anevia's dance choice is lost.");
                            check(result.Has("three_lantern_turn.home") != result.Has("three_lantern_turn.later"), "Leaving the gathering is confused with visiting that night.");
                        }
                        if (scene.Id == "three_open_road")
                        {
                            check(result.Has("three_open_road.kept"), "Private continuation has no completed endpoint.");
                            check(new[] { "night", "evening", "company" }.Count(f => result.Has("three_open_road." + f)) == 1,
                                "Private visit loses its voluntary nighttime choice.");
                        }
                        observed.UnionWith(result.Flags);
                        continuing.Add(result);
                    }
                }
                check(continuing.Count > 0, "A wife order has no completing path at " + scene.Id);
                // Earlier prose-only choices were already checked; retain only differences read by later scenes.
                var futureKeys = ordered.Skip(index + 1).SelectMany(s => s.Requires.Concat(s.Forbids)
                    .Concat(s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids))))
                    .Concat(new[] { "three_stolen_roads.book_safe", "three_stolen_roads.followed" }).Distinct().OrderBy(f => f).ToArray();
                states = continuing.GroupBy(s => string.Join("\n", futureKeys.Where(s.Has))).Select(g => g.First()).ToList();
            }
        }
        foreach (var flag in new[] { "three_stolen_roads.book_safe", "three_stolen_roads.followed", "three_lantern_debt.private_sketch",
            "three_lantern_debt.shared_sketch", "three_beth_steps.followed", "three_beth_steps.led", "three_beth_steps.kissed", "three_beth_steps.held",
            "three_ista_departure.both_roads", "three_ista_departure.easy_road", "three_lantern_turn.home", "three_lantern_turn.later",
            "three_open_road.night", "three_open_road.evening", "three_open_road.company" })
            check(observed.Contains(flag), "A Tirabade narrative alternative was never reached: " + flag);

        foreach (var scene in scenes)
        {
            check(scene.Optional && !Rules.IsRemote(scene), "Tirabade reckoning loses its optional native-contact delivery.");
            var expectedTargets = scene.Id == "three_lantern_debt" ? new[] { "33960c7f7af40cd43b7f801a76c87a0b" }
                : scene.Id == "three_beth_steps" ? new[] { "871af36f2ab2b1f40b5de77976c54276" }
                : new[] { "33960c7f7af40cd43b7f801a76c87a0b", "871af36f2ab2b1f40b5de77976c54276" };
            check(Rules.EntryTargets(scene).SequenceEqual(expectedTargets), "Tirabade reckoning uses the wrong wife's dialogue attachment.");
            check(scene.DelayHours == (scene.Id == "three_lantern_debt" || scene.Id == "three_beth_steps" || scene.Id == "three_open_road" ? 24 : 48),
                "Tirabade reckoning changes its authored meeting intervals.");
            check(scene.Nodes.Skip(1).SelectMany(n => n.Choices).All(c => !c.Abort), "A late abort permits replay after recording consequences.");
            foreach (int chapter in new[] { 3, 5 })
            {
                var ready = new Snapshot { Chapter = chapter, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
                ready.Flags.UnionWith(scene.Requires);
                check(Rules.Available(story, scene, ready), "Eligible Tirabade incident is unavailable.");
                foreach (var prerequisite in scene.Requires)
                {
                    var missing = Program.Copy(ready); missing.Flags.Remove(prerequisite);
                    check(!Rules.Available(story, scene, missing), "Tirabade incident bypasses prerequisite: " + prerequisite);
                }
                foreach (var blocker in new[] { "closed", "loss", "inhuman", "last_watch", "irabeth_away", "anevia_away",
                    "irabeth_dead", "anevia_dead", "irabeth_gone", "anevia_gone", "swarm", "true_lich" })
                {
                    var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                    check(!Rules.Available(story, scene, blocked), "Tirabade incident ignores missing/dead/closed state: " + blocker);
                }
                ready.Times[scene.Requires.Last()] = ready.Hour;
                ready.Hour += scene.DelayHours - 1;
                check(!Rules.Available(story, scene, ready), "Tirabade incident ignores its delay.");
                ready.Hour++;
                check(Rules.Available(story, scene, ready), "Tirabade incident misses its exact delay boundary.");
                ready.Area = "elsewhere";
                check(!Rules.Available(story, scene, ready), "Tirabade incident appears outside Drezen.");
                ready.Area = "2570015799edf594daf2f076f2f975d8";
                foreach (int unavailableChapter in new[] { 2, 4, 6 })
                {
                    ready.Chapter = unavailableChapter;
                    check(!Rules.Available(story, scene, ready), "Tirabade incident escapes its Chapter 3/5 scope.");
                }
            }
        }
        // Snapshot checks cannot prove that the native speaker is physically present or that prose callbacks are accurate.
    }
}
