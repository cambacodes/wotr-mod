using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class TirabadeProgressionTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var future = story.Scenes.Single(s => s.Id == "future");
        var watch = story.Scenes.Single(s => s.Id == "last_watch");
        var state = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
        state.AvailableContacts.UnionWith(new[] { "b5e867e13503c6f41bb1316705efb4a2", "280d4712dceb37f4a88e98f1f4c6e64f" });
        state.Flags.UnionWith(new[] { "power", "a_self", "i_self", "power_terms", "kept_terms", "ordinary",
            "trying", "a_affair", "i_affair", "seelah.committed", "arueshalae.committed" });
        check(Rules.Available(story, future, state), "Tirabade future reproduction setup is unavailable.");
        state = Program.Walk(future, state).First(s => s.Has("future") && s.Has("committed") && !s.Has("closed"));
        state.Hour += 10000;
        check(!Rules.Available(story, watch, state),
            "Original future and elapsed time bypass the entire developed Tirabade campaign.");

        Scene Find(string id) => story.Scenes.Single(s => s.Id == id);
        var decision = Find("three_choose_days");
        var catchup = Find("three_more_days");
        var capstone = Find("three_kept_days");
        var route = new Story { Scenes = story.Scenes.Where(s => s.Relationship == "tirabade").ToList(), Relationships = story.Relationships };
        var chain = new[] { "three_locks", "three_outing", "three_yard", "three_match", "three_beth_score",
            "three_anevia_flour", "three_return_game", "three_small_journeys", "three_stolen_roads",
            "three_lantern_debt", "three_beth_steps", "three_ista_departure", "three_lantern_turn", "three_open_road",
            "three_borrowed_names", "three_back_of_seal", "three_beth_account", "three_counterclaim",
            "three_unposted_notice", "three_rooms_unlocked" }.Select(Find).ToArray();
        var native = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Distinct().ToArray();
        var visited = new HashSet<string>();

        string[] Endings(Snapshot snapshot, string owner = "Epilogue") => route.Scenes
            .Where(s => s.Owner == owner && Rules.Available(story, s, snapshot)).Select(s => s.Id).ToArray();

        Snapshot Ready(Scene scene, Snapshot input)
        {
            var copy = Program.Copy(input);
            int latest = scene.Requires.Where(copy.Times.ContainsKey).Select(f => copy.Times[f]).DefaultIfEmpty(copy.Hour).Max();
            copy.Hour = Math.Max(copy.Hour, latest + scene.DelayHours);
            return copy;
        }

        void Protected(Snapshot before, Snapshot after)
        {
            foreach (string flag in native.Concat(new[] { "committed", "seelah.committed", "arueshalae.committed",
                "a_affair", "i_affair", "kept_terms", "last_watch", "last_words" }))
                check(before.Has(flag) == after.Has(flag), "Tirabade progression rewrites existing history: " + flag);
            if (before.Has("last_watch"))
                check(after.Times["last_watch"] == before.Times["last_watch"], "Catch-up retimes the old final watch.");
        }

        Snapshot OriginalPromise()
        {
            var original = new Snapshot { Chapter = 5, Hour = 1000, Area = state.Area };
            original.AvailableContacts.UnionWith(state.AvailableContacts);
            original.Flags.UnionWith(new[] { "chapter_later", "trickster", "seelah.committed", "arueshalae.committed" });
            foreach (string id in new[] { "a_cup", "i_watch", "a_errand", "i_hands", "a_roof", "i_respite",
                "a_crossing", "i_crossing", "a_morning", "i_morning", "reckoning", "a_truth", "i_truth",
                "table", "ordinary", "a_self", "i_self", "return", "power", "future", "shared_night" })
            {
                var scene = Find(id);
                original = Ready(scene, original);
                check(Rules.Available(story, scene, original), "Original route predecessor is unavailable: " + id);
                original = Program.Walk(scene, original).Where(s => s.Has(id) && !s.Has("closed") && Program.LegacyTirabadeOutcome(s))
                    .OrderByDescending(s => s.Flags.Count).First();
            }
            check(original.Has("committed") && original.Has("kept_terms"), "Original played route did not establish the mutual promise.");
            return original;
        }

        void Guarded(Scene scene, Snapshot ready)
        {
            check(Rules.Available(story, scene, ready), "Developed Tirabade scene is unavailable: " + scene.Id);
            foreach (string flag in new[] { "closed", "loss", "inhuman", "anevia_dead", "irabeth_dead", "anevia_gone", "irabeth_gone",
                "swarm", "true_lich", "irabeth_away", "anevia_away" })
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag);
                check(!Rules.Available(story, scene, blocked), "Tirabade continuation bypasses " + flag + ": " + scene.Id);
            }
            foreach (int chapter in new[] { 2, 4, 6 })
            {
                var blocked = Program.Copy(ready); blocked.Chapter = chapter;
                check(!Rules.Available(story, scene, blocked), "Tirabade continuation ignores chapter: " + scene.Id);
            }
            var elsewhere = Program.Copy(ready); elsewhere.Area = "elsewhere";
            check(!Rules.Available(story, scene, elsewhere), "Tirabade continuation ignores Drezen location: " + scene.Id);
            foreach (string prerequisite in scene.Requires)
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(prerequisite);
                check(!Rules.Available(story, scene, missing), "Tirabade continuation skips prerequisite: " + scene.Id + "/" + prerequisite);
            }
            if (scene.DelayHours > 0)
            {
                var fresh = Program.Copy(ready);
                fresh.Times[scene.Requires.Last()] = fresh.Hour;
                fresh.Hour += scene.DelayHours - 1;
                check(!Rules.Available(story, scene, fresh), "Tirabade continuation ignores its predecessor delay: " + scene.Id);
            }
        }

        Snapshot Select(Scene scene, Snapshot input, int profile)
        {
            var ready = Ready(scene, input);
            Guarded(scene, ready);
            check(Rules.NextRemote(route, ready) == null, "Physical Tirabade continuation enters the automatic rest queue.");
            var outcomes = Program.Walk(scene, ready).Where(s => s.Has(scene.Id)).ToArray();
            string? want = scene.Id switch
            {
                "three_stolen_roads" => profile == 1 ? "three_stolen_roads.followed" : "three_stolen_roads.book_safe",
                "three_open_road" => "three_open_road." + new[] { "company", "evening", "night" }[profile],
                "three_back_of_seal" => "three_back_of_seal." + new[] { "unreadable", "impression", "catalogue" }[profile],
                "three_rooms_unlocked" => "three_rooms_unlocked." + new[] { "walk", "rest", "night" }[profile],
                _ => null
            };
            var result = outcomes.First(s => want == null || s.Has(want));
            Protected(ready, result);
            return result;
        }

        // The original 34-scene saved history is played, not assembled from all new prerequisites.
        var promise = OriginalPromise();
        check(Endings(promise).SequenceEqual(new[] { "ending_promised" }), "Early commitment receives an unearned household ending.");
        var ascendedPromise = Program.Copy(promise); ascendedPromise.Flags.Add("ascended");
        check(Endings(ascendedPromise).SequenceEqual(new[] { "ending_ascend_promised" }), "Early ascent receives an unearned developed ending.");
        var choose = Ready(decision, promise);
        Guarded(decision, choose);
        var decisions = Program.Walk(decision, choose, (node, _) => visited.Add(decision.Id + "/" + node));
        foreach (var deferred in decisions.Where(s => !s.Has(decision.Id)))
            check(deferred.Flags.SetEquals(choose.Flags) && deferred.Times.Count == choose.Times.Count,
                "Continuing courtship or deferring writes a short-route decision.");
        var shortRoute = decisions.Single(s => s.Has("three_progression.short_chosen"));
        check(Rules.Available(story, watch, shortRoute), "Explicit shorter-course choice does not open the final watch.");
        shortRoute = Program.Walk(watch, shortRoute).First(s => s.Has("last_watch"));
        check(Endings(shortRoute).SequenceEqual(new[] { "ending_promised" }), "Short course is credited with unplayed development.");
        check(!Rules.Available(story, chain[0], Ready(chain[0], shortRoute)), "Short final watch silently enters unfinished courtship.");
        check(Rules.Available(story, catchup, shortRoute), "Short course cannot later opt into remaining time together.");

        foreach (bool oldWatch in new[] { false, true })
        foreach (bool bethFirst in new[] { false, true })
        foreach (int profile in new[] { 0, 1, 2 })
        {
            var current = Program.Copy(promise);
            var ordered = chain.ToArray();
            if (bethFirst)
                foreach (int first in new[] { 4, 9, 15 })
                    (ordered[first], ordered[first + 1]) = (ordered[first + 1], ordered[first]);
            int checkpoint = oldWatch ? new[] { 0, 8, 20 }[profile] : -1;
            for (int index = 0; index <= ordered.Length; index++)
            {
                if (index == checkpoint)
                {
                    // Replay the unchanged original final-watch pages as a historical pre-gate save.
                    current = Program.Walk(watch, current).First(s => s.Has("last_watch"));
                    var beforeCatchup = Program.Copy(current);
                    if (index < ordered.Length)
                        check(!Rules.Available(story, ordered[index], Ready(ordered[index], current)),
                            "Old final watch silently opts into remaining courtship.");
                    var invitation = Ready(catchup, current);
                    Guarded(catchup, invitation);
                    var replies = Program.Walk(catchup, invitation, (node, _) => visited.Add(catchup.Id + "/" + node));
                    var deferred = replies.Single(s => !s.Has(catchup.Id));
                    check(deferred.Flags.SetEquals(invitation.Flags) && deferred.Times.Count == invitation.Times.Count,
                        "Deferring old-save catch-up changes history.");
                    current = replies.Single(s => s.Has(catchup.Id));
                    Protected(beforeCatchup, current);
                    check(current.Has("three_progression.catchup_requested"), "Catch-up invitation does not authorize continuation.");
                }
                if (index == ordered.Length) break;
                var late = Program.Copy(current); late.Hour += 10000;
                check(!Rules.Available(story, watch, late), "Elapsed time opens final watch midway through the shared campaign.");
                check(!Rules.Available(story, capstone, late), "Capstone bypasses an unplayed predecessor.");
                current = Select(ordered[index], current, profile);
            }
            var readyCapstone = Ready(capstone, current);
            Guarded(capstone, readyCapstone);
            check(!Rules.Available(story, watch, readyCapstone), "Final watch opens before the developed relationship conversation.");
            foreach (var result in Program.Walk(capstone, readyCapstone, (node, _) => visited.Add(capstone.Id + "/" + node)))
            {
                Protected(readyCapstone, result);
                if (!result.Has(capstone.Id))
                {
                    check(result.Flags.SetEquals(readyCapstone.Flags), "Deferring the capstone awards developed credit.");
                    continue;
                }
                check(result.Has("three_progression.developed"), "Played capstone does not award developed history.");
                check(Endings(result).SequenceEqual(new[] { "ending_together" }), "Developed history lacks one earned normal ending.");
                var ascended = Program.Copy(result); ascended.Flags.Add("ascended");
                check(Endings(ascended).SequenceEqual(new[] { "ending_ascend" }), "Developed ascent lacks one earned ending.");
                check(Endings(result, "AeonEpilogue").SequenceEqual(new[] { "ending_aeon" }), "Progression duplicates the existing Aeon history.");
                check(Rules.Available(story, watch, result) == !oldWatch, "Catch-up repeats an old watch or blocks a newly earned one.");
                if (!oldWatch)
                {
                    var done = Program.Walk(watch, result).First(s => s.Has("last_watch"));
                    check(done.Has("last_words") && done.Has("three_progression.developed"), "Final watch loses developed history.");
                }
            }
        }
        check(visited.SetEquals(new[] { decision, catchup, capstone }.SelectMany(s => s.Nodes.Select(n => s.Id + "/" + n.Id))),
            "Tirabade progression tests miss a new played page.");
    }
}
