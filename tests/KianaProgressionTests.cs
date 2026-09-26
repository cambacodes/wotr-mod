using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KianaProgressionTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "kiana." + id);
        var route = new Story { Scenes = story.Scenes.Where(s => s.Relationship == "kiana").ToList(), Relationships = story.Relationships };
        var farewell = Find("farewell");
        var catchup = Find("another_page");
        var decision = Find("a_place_afterward");
        var breakup = Find("parting");
        var chainIds = new[] { "guest_table", "market_weather", "lenna_door", "blue_room", "bakery_stairs",
            "last_page", "first_readers", "ink_after", "working_room", "kept_evening" }.AsEnumerable();
        if (story.Scenes.Any(s => s.Id == "kiana.borrowed_name"))
            chainIds = chainIds.Concat(new[] { "borrowed_name", "yard_evening", "unborrowed_evening" });
        var chain = chainIds.Select(Find).ToArray();
        var nativeFlags = story.Etudes.Keys.Concat(story.CompletedQuests.Keys).Concat(story.CompletedEtudes.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Distinct().ToArray();
        var visited = new HashSet<string>();

        Snapshot Play(string id, Snapshot input, Func<Snapshot, bool>? select = null)
        {
            var scene = Find(id);
            var ready = Program.Copy(input);
            ready.Hour += scene.DelayHours;
            check(Rules.Available(story, scene, ready), "Kiana predecessor unavailable: " + id);
            return Program.Walk(scene, ready).First(s => s.Has(scene.Id) && !s.Has("kiana.closed") && (select == null || select(s)));
        }

        string[] Endings(Snapshot state, string owner = "Epilogue") => story.Scenes
            .Where(s => s.Relationship == "kiana" && s.Owner == owner && Rules.Available(story, s, state)).Select(s => s.Id).ToArray();

        void Protected(Snapshot before, Snapshot after)
        {
            foreach (var flag in nativeFlags.Concat(new[] { "seelah.committed", "arueshalae.committed",
                "kiana.separated", "kiana.bereaved", "kiana.waited", "kiana.affair", "kiana.farewell", "kiana.farewell_kept" }))
                check(before.Has(flag) == after.Has(flag), "Kiana progression rewrites prior history: " + flag);
            if (before.Has("kiana.committed")) check(after.Has("kiana.committed"), "Kiana progression clears an existing promise.");
        }

        foreach (var history in new[] { "waited", "affair", "widow" })
        foreach (bool committed in new[] { false, true })
        foreach (bool oldFarewell in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(new[] { "seelah.souls_returned", "kiana.aftermath_seen", "kiana.started",
                "seelah.committed", "arueshalae.committed" });
            if (history == "widow") state.Flags.Add("seelah.elan_dead");
            state = Play("invitation", state);
            state = Play("rehearsal", state);
            state = Play("stagecraft", state);
            if (history == "widow") state = Play("widow", state);
            else
            {
                state = Play("marriage", state, s => s.Has("kiana." + history));
                state = Play("answer", state);
            }
            state = Play("date", state);
            state = Play("morning", state, s => s.Has("kiana.committed") == committed);
            state = Play("seelah", state);
            state.Hour += 10000;
            check(!Rules.Available(story, farewell, state), "Elapsed time alone bypasses Kiana's developed route.");
            check(Endings(state).SequenceEqual(new[] { committed ? "kiana.ending_promised" : "kiana.ending_unfinished" }),
                "Early Kiana history receives a developed ending or no honest fallback.");
            check(breakup.ManualOnly && Rules.Available(story, breakup, state), "Kiana loses manual access to breakup.");

            if (oldFarewell)
            {
                // Historical save, not a new attempt to pass the revised farewell gate.
                state.Flags.UnionWith(new[] { "kiana.farewell", "kiana.farewell_kept" });
                state.Times["kiana.farewell"] = 500;
                check(!Rules.Available(story, chain[0], state), "Old farewell silently opts into catch-up.");
                check(catchup.ManualOnly && Rules.Available(story, catchup, state), "Old save cannot request Kiana's catch-up.");
                check(Rules.NextRemote(route, state) == null, "Manual catch-up or breakup enters Kiana's rest queue.");
                var responses = Program.Walk(catchup, state);
                var deferred = responses.Single(s => !s.Has(catchup.Id));
                check(deferred.Flags.SetEquals(state.Flags), "Deferring catch-up changes relationship history.");
                state = responses.Single(s => s.Has(catchup.Id));
                check(state.Has("kiana.catchup_requested") && state.Has("kiana.farewell") && state.Times["kiana.farewell"] == 500,
                    "Kiana catch-up clears or retimes the old farewell.");
            }
            else check(!Rules.Available(story, catchup, state), "A new Kiana route receives an old-save catch-up offer.");

            foreach (var scene in chain)
            {
                state.Hour += scene.DelayHours;
                check(Rules.NextRemote(route, state)?.Id == scene.Id, "Rest queue skips Kiana's played predecessor: " + scene.Id);
                check(!Rules.Available(story, farewell, state), "Kiana farewell opens midway through the developed chain.");
                var done = Program.Walk(scene, state).Where(s => s.Has(scene.Id)).ToArray();
                // Existing focused suites explore all literary branches; this test exercises real queue delivery.
                var result = history == "affair" ? done.Last() : done.First();
                Protected(state, result);
                state = result;
                var premature = Program.Copy(state);
                premature.Hour += 10000;
                check(!Rules.Available(story, farewell, premature), "Kiana farewell bypasses missing later work after a long wait.");
            }

            check(!Rules.Available(story, decision, state), "Kiana later decision ignores its fresh completion timestamp.");
            state.Hour += decision.DelayHours;
            check(Rules.NextRemote(route, state)?.Id == decision.Id, "Kiana's later relationship decision is not next after the developed chain.");
            foreach (string blocker in new[] { "kiana.closed", "inhuman" })
            {
                var blocked = Program.Copy(state); blocked.Flags.Add(blocker);
                check(!Rules.Available(story, decision, blocked), "Catch-up bypasses Kiana decision restriction: " + blocker);
            }
            var interrupted = Program.Copy(state); interrupted.Flags.Remove("seelah.souls_returned");
            check(!Rules.Available(story, decision, interrupted), "Catch-up bypasses Kiana's native quest prerequisite.");
            foreach (var result in Program.Walk(decision, state, (node, snapshot) => visited.Add(node)))
            {
                Protected(state, result);
                if (!result.Has(decision.Id))
                {
                    check(result.Flags.SetEquals(state.Flags), "Deferring Kiana's later decision records commitment or resolution.");
                    continue;
                }
                check(result.Has("kiana.future_settled"), "Kiana completes later decision without a resolved outcome.");
                check(!(result.Has("kiana.future_open") && result.Has("kiana.committed")), "Kiana downgrades an earlier commitment to an open future.");
                string expected = result.Has("kiana.closed") ? "apart" : result.Has("kiana.committed")
                    ? history == "widow" ? "bereaved" : "together" : "open";
                check(Endings(result).SequenceEqual(new[] { "kiana.ending_" + expected }), "Kiana later decision has overlapping or incorrect normal endings.");
                var ascended = Program.Copy(result); ascended.Flags.Add("ascended");
                expected = result.Has("kiana.closed") ? "apart" : result.Has("kiana.committed") ? "ascended" : "open_ascended";
                check(Endings(ascended).SequenceEqual(new[] { "kiana.ending_" + expected }), "Kiana ascension overrides the actual later relationship decision.");
                if (!result.Has("kiana.closed"))
                    check(Endings(result, "AeonEpilogue").Length == 1, "Kiana's continuing relationship lacks a unique Aeon ending.");
                if (!oldFarewell && !result.Has("kiana.closed"))
                {
                    result.Hour += farewell.DelayHours;
                    check(Rules.NextRemote(route, result)?.Id == farewell.Id, "Earned Kiana farewell does not follow her decision.");
                }
                if (oldFarewell) check(!Rules.Available(story, farewell, result), "Kiana replays an old farewell after catch-up.");
            }

            var transformed = Program.Copy(state);
            transformed.Flags.Add("inhuman");
            transformed.Flags.Remove("kiana.farewell");
            check(!Rules.Available(story, catchup, transformed) && !Rules.Available(story, decision, transformed),
                "Kiana offers unsupported physical catch-up to a transformed Commander.");
            check(Rules.Available(story, farewell, transformed), "Kiana's existing transformed fallback is trapped behind unavailable full-route scenes.");
        }
        // Changed native histories are walked by KianaReconciliationTests.
        check(visited.SetEquals(decision.Nodes.Where(n => !n.Id.EndsWith("_former_grief") && !n.Id.EndsWith("_uncertain")).Select(n => n.Id)), "Kiana later-decision tests miss an authored page.");
    }
}
