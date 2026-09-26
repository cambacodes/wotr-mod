using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class ArsinoeContinuationTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        string[] ids = { "arsinoe_your_hours", "arsinoe_borrowed_court", "arsinoe_price_of_an_evening",
            "arsinoe_courtyard_company", "arsinoe_another_hour", "arsinoe_the_unprofitable_hour" };
        var scenes = ids.Select(id => story.Scenes.Single(s => s.Id == id)).ToArray();
        var visited = scenes.ToDictionary(s => s.Id, _ => new HashSet<string>());
        string[] paceFlags = { "arsinoe.courting", "arsinoe.slow", "arsinoe.friendship" };
        string[][] exclusive = {
            new[] { "arsinoe.interest_games", "arsinoe.interest_stories" },
            new[] { "arsinoe.game_reconstructed", "arsinoe.game_unresolved", "arsinoe.game_house" },
            new[] { "arsinoe.evening_public", "arsinoe.evening_private" },
            new[] { "arsinoe.company_earlier", "arsinoe.company_quiet" }
        };
        var protectedFlags = new[] { "seelah.committed", "arueshalae.committed", "lann.committed" };
        var allNewFlags = scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).ToHashSet();
        var nativeFlags = story.Etudes.Keys.Concat(story.StartedDialogs.Keys).Concat(story.SeenCues.Keys)
            .Concat(story.SelectedAnswers.Keys).Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys).ToHashSet();
        check(!allNewFlags.Overlaps(nativeFlags), "Arsinoe continuation writes native histories.");
        check(!allNewFlags.Overlaps(paceFlags) && !allNewFlags.Contains("arsinoe.committed"),
            "Arsinoe continuation silently changes pacing or awards full commitment.");

        var roll = scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Single(c => c.Check != null);
        check(roll.Check!.Skill == "SkillKnowledgeWorld" && roll.Check.DC == 24 && roll.Check.CommanderOnly,
            "Arsinoe game reconstruction uses the wrong skill, difficulty or actor.");
        check(roll.Set.Length == 0 && roll.Next == null && roll.Check.Success == "original" && roll.Check.Failure == "uncertain",
            "Arsinoe roll records an outcome before the native result.");

        foreach (int chapter in new[] { 3, 5 })
        foreach (string pace in paceFlags)
        {
            var opening = story.Scenes.Single(s => s.Id == "arsinoe_hours_of_her_own");
            var seed = new Snapshot { Chapter = chapter, Area = opening.Areas.Single(), Hour = 1000 };
            seed.Flags.UnionWith(opening.Requires);
            seed.Flags.UnionWith(protectedFlags);
            seed.Flags.UnionWith(new[] { pace, "arsinoe.next_walk" });
            seed.AvailableContacts.Add(opening.ContactUnit!);
            check(Rules.Available(story, opening, seed), "Opening fixture cannot actually play Arsinoe's final opening scene.");
            var states = Distinct(Program.Walk(opening, seed).Where(s => s.Has("arsinoe.opening_kept")));
            check(states.Count > 0, "Arsinoe opening produces no continuation entry.");

            for (int index = 0; index < scenes.Length; index++)
            {
                var scene = scenes[index];
                var next = new List<Snapshot>();
                foreach (var previous in states)
                {
                    var ready = Program.Copy(previous);
                    check(!Rules.Available(story, scene, ready), "Arsinoe continuation ignores its actual predecessor delay: " + scene.Id);
                    ready.Hour += scene.DelayHours;
                    check(Rules.Available(story, scene, ready), "Played Arsinoe history cannot reach " + scene.Id);
                    check(scene.ContactUnit == "a609ed9b2205d034bb3bb04d2a255681" && !Rules.IsRemote(scene),
                        "Arsinoe continuation bypasses live native contact.");

                    // Every branch outcome is terminal, so all interrupted pages retain the entry history.
                    var results = Program.Walk(scene, ready, (page, partial) =>
                    {
                        visited[scene.Id].Add(page);
                        check(partial.Flags.SetEquals(ready.Flags), "Arsinoe records an unacknowledged outcome on " + scene.Id + "/" + page);
                        check(!partial.Has(scene.Id), "Arsinoe completes a scene before its last response.");
                        if (page == "kiss")
                            check(partial.Has("arsinoe.courting") && !partial.Has("arsinoe.continuation_kiss"),
                                "Arsinoe continuation invents an earlier kiss or admits a non-courting path.");
                        if (page == "slow") check(partial.Has("arsinoe.slow"), "Slow continuation ignores chosen pacing.");
                        if (page == "friend") check(partial.Has("arsinoe.friendship"), "Friendship continuation ignores chosen pacing.");
                    });
                    foreach (var result in results)
                    {
                        check(ready.Flags.IsSubsetOf(result.Flags) && protectedFlags.All(result.Has),
                            "Arsinoe continuation resets prior history or another romance.");
                        check(paceFlags.Count(result.Has) == 1 && result.Has(pace), "Arsinoe continuation changes relationship pace.");
                        check(!result.Has("arsinoe.continuation_kiss") || pace == "arsinoe.courting",
                            "A friendship or slow route receives romantic intimacy.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags) && result.Times.Count == ready.Times.Count,
                                "Deferring Arsinoe's activity records unplayed content.");
                            continue;
                        }
                        for (int group = 0; group < exclusive.Length && group <= index; group++)
                            check(exclusive[group].Count(result.Has) == 1, "Arsinoe records conflicting interests, rules, terms or schedules.");
                        check(!Rules.Available(story, scene, result), "Completed Arsinoe activity reopens.");
                        next.Add(result);
                    }
                }
                states = Distinct(next);
                check(states.Count > 0, "Arsinoe continuation loses all paths at " + scene.Id);

                var guard = Program.Copy(states[0]);
                guard.Flags.Remove(scene.Id); guard.Times.Remove(scene.Id);
                guard.Hour += scene.DelayHours;
                foreach (string required in scene.Requires)
                {
                    var missing = Program.Copy(guard); missing.Flags.Remove(required);
                    check(!Rules.Available(story, scene, missing), "Arsinoe continuation ignores prerequisite " + required);
                }
                foreach (string flag in new[] { "arsinoe.closed", "arsinoe.victims_revived", "swarm", "true_lich" })
                {
                    var blocked = Program.Copy(guard); blocked.Flags.Add(flag);
                    check(!Rules.Available(story, scene, blocked), "Arsinoe continuation ignores native/closure guard " + flag);
                    if (flag != "arsinoe.closed")
                        check(!Rules.ContactAvailable(story, scene, blocked), "Active Arsinoe continuation ignores temporary/native unavailability.");
                    blocked.Flags.Remove(flag);
                    check(Rules.Available(story, scene, blocked), "Removing temporary restriction permanently strands Arsinoe.");
                }
                var away = Program.Copy(guard); away.AvailableContacts.Clear();
                check(!Rules.Available(story, scene, away) && !Rules.ContactAvailable(story, scene, away),
                    "Arsinoe continuation remains playable after native contact is lost.");
                away.AvailableContacts.Add(scene.ContactUnit!);
                check(Rules.Available(story, scene, away), "Interrupted Arsinoe continuation cannot resume after live contact returns.");
                away.Area = "outside_drezen";
                check(!Rules.Available(story, scene, away), "Arsinoe continuation can start outside Drezen.");
                away.Area = scene.Areas.Single(); away.Chapter = 4;
                check(!Rules.Available(story, scene, away), "Arsinoe continuation starts in chapter four.");
            }
            check(states.All(s => s.Has("arsinoe.continuation_kept")), "A completed Arsinoe continuation fails to record the evening.");
            check(states.Any(s => !s.Has("arsinoe.continuation_kiss")), "Arsinoe continuation forces a kiss.");
            if (pace == "arsinoe.courting") check(states.Any(s => s.Has("arsinoe.continuation_kiss")), "Courting Arsinoe cannot choose a kiss.");
        }
        foreach (var scene in scenes)
            check(visited[scene.Id].SetEquals(scene.Nodes.Select(n => n.Id)), "Arsinoe continuation contains an unreachable page: " + scene.Id);

        // Reenter from each actual native result page before acknowledging it, then choose the non-roll approach.
        var game = scenes[1];
        var gameReady = new Snapshot { Chapter = 3, Area = game.Areas.Single(), Hour = 1000 };
        gameReady.Flags.UnionWith(game.Requires); gameReady.AvailableContacts.Add(game.ContactUnit!);
        Program.Walk(game, gameReady, (page, partial) =>
        {
            if (page != "original" && page != "uncertain") return;
            var replay = Program.Copy(partial);
            replay.AvailableContacts.Clear();
            check(!Rules.ContactAvailable(story, game, replay), "Native result page ignores contact loss.");
            replay.AvailableContacts.Add(game.ContactUnit!);
            check(Rules.Available(story, game, replay), "Interrupted game result cannot be replayed.");
            var house = Program.Walk(game, replay).Where(s => s.Has("arsinoe.game_house")).ToArray();
            check(house.Length > 0 && house.All(s => !s.Has("arsinoe.game_reconstructed") && !s.Has("arsinoe.game_unresolved")),
                "An unacknowledged roll result contaminates the non-roll replay.");
        });
    }

    private static List<Snapshot> Distinct(IEnumerable<Snapshot> states) => states
        .GroupBy(s => string.Join("|", s.Flags.OrderBy(f => f, StringComparer.Ordinal)))
        .Select(g => g.First()).ToList();
}
