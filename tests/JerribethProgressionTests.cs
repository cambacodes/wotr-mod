using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class JerribethProgressionTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "jerribeth." + id);
        var route = new Story { Scenes = story.Scenes.Where(s => s.Relationship == "jerribeth").ToList(), Relationships = story.Relationships };
        var future = Find("future");
        var farewell = Find("farewell");
        var visit = Find("settlement_visit");
        var room = Find("room_measure");
        var catchup = Find("another_evening");
        var reaffirm = Find("promise_revisited");
        var seen = new HashSet<string>();
        var native = story.Etudes.Keys.Concat(story.CompletedQuests.Keys).Concat(story.CompletedEtudes.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Distinct().ToArray();
        var outcomes = new[] { "inspection_visible", "inspection_removed", "inspection_refused",
            "catalogue_play", "catalogue_comedy", "catalogue_declined" };
        var campaign = new[] { "offered_signature", "small_print", "unsold_evening", "purchaser_answer",
            "counterfeit_guest", "counterfeit_hinge", "counterfeit_clerk", "counterfeit_audience",
            "counterfeit_spoil", "counterfeit_after" };

        void Preserve(Snapshot before, Snapshot after)
        {
            foreach (string flag in native.Concat(new[] { "seelah.committed", "kiana.committed", "jerribeth.farewell", "jerribeth.farewell_kept" }))
                check(before.Has(flag) == after.Has(flag), "Jerribeth progression changes preserved history: " + flag);
            if (before.Has("jerribeth.committed")) check(after.Has("jerribeth.committed"), "Jerribeth progression clears an old promise.");
        }

        Snapshot Play(string id, Snapshot input, Func<Snapshot, bool>? select = null, bool queue = false)
        {
            var scene = Find(id);
            var state = Program.Copy(input);
            state.Hour += scene.DelayHours;
            check(Rules.Available(story, scene, state), "Jerribeth actual chain cannot enter " + id);
            if (queue) check(Rules.NextRemote(route, state)?.Id == scene.Id, "Jerribeth rest queue skips played scene " + id);
            var results = Program.Walk(scene, state, (node, _) => seen.Add(scene.Id + "/" + node));
            foreach (var result in results) Preserve(state, result);
            var completed = results.FirstOrDefault(s => s.Has(scene.Id) && !s.Has("jerribeth.closed") && (select == null || select(s)));
            check(completed != null, "Jerribeth actual chain cannot finish " + id);
            return completed!;
        }

        Snapshot Core(int chapter)
        {
            var state = new Snapshot { Chapter = chapter, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(new[] { "jerribeth.met", "seelah.committed", "kiana.committed", "trickster" });
            foreach (string id in new[] { "invitation", "question", "guise", "price", "evening", "commission" })
                state = Play(id, state, queue: true);
            return state;
        }

        string[] EndingIds(Snapshot state) => story.Scenes.Where(s => s.Relationship == "jerribeth"
            && s.Owner == "Epilogue" && Rules.Available(story, s, state)).Select(s => s.Id).ToArray();

        void Endings(Snapshot state, bool developed)
        {
            foreach (bool ascended in new[] { false, true })
            {
                var endingState = Program.Copy(state);
                if (ascended) endingState.Flags.Add("ascended");
                string id = ascended ? "ending_ascended" : "ending_together";
                check(EndingIds(endingState).SequenceEqual(new[] { "jerribeth." + id }), "Jerribeth positive epilogues overlap or disappear.");
                var nodes = new HashSet<string>();
                Program.Walk(Find(id), endingState, (node, _) => nodes.Add(node));
                check(nodes.Contains("earlier") != developed && nodes.Contains("settlement") == developed,
                    "Jerribeth ending mistakes an early promise for played development.");
                if (developed)
                    check(nodes.Contains("account") == state.Has("jerribeth.counter_public_account")
                        && nodes.Contains("catalogue") == state.Has("jerribeth.counter_private_archive"),
                        "Jerribeth ending forgets or reverses the settlement.");
            }
            var closed = Program.Copy(state); closed.Flags.Add("jerribeth.closed");
            check(EndingIds(closed).SequenceEqual(new[] { "jerribeth.ending_apart" }), "Jerribeth closed ending overlaps a promise.");
            var unavailable = Program.Copy(state); unavailable.Flags.Add("jerribeth.unavailable");
            check(EndingIds(unavailable).Length == 0, "Jerribeth unavailable history receives an ordinary relationship ending.");
        }

        var core = Core(5);
        core.Hour += 10000;
        check(!Rules.Available(story, future, core), "Original commission->future shortcut remains available with elapsed time alone.");
        check(!Rules.Available(story, farewell, core), "Farewell bypasses the developed or explicitly short promise.");
        check(Find("parting").ManualOnly && Rules.Available(story, Find("parting"), core), "Manual breakup is unavailable or automatic again.");
        check(Rules.NextRemote(route, core)?.Id == Find("offered_signature").Id, "Future or manual breakup steals the purchaser invitation.");
        var shortOffer = Find("short_invitation");
        check(shortOffer.ManualOnly && Rules.Available(story, shortOffer, core), "Explicit shorter-history offer is missing.");
        foreach (var deferred in Program.Walk(shortOffer, core).Where(s => !s.Has(shortOffer.Id)))
            check(deferred.Flags.SetEquals(core.Flags), "Declining the short route changes history.");
        var shortRoute = Play("short_invitation", core);
        shortRoute = Play("future", shortRoute, queue: true);
        check(shortRoute.Has("jerribeth.short_future_chosen") && !shortRoute.Has("jerribeth.developed_future"), "Short future grants developed history.");
        Endings(shortRoute, false);
        var shortOrdinary = Play("ordinary", shortRoute, queue: true);
        shortOrdinary.Hour += 100;
        check(!Rules.Available(story, farewell, shortOrdinary), "Short promise silently schedules a campaign-cutting farewell.");
        check(Find("farewell_review").ManualOnly, "Farewell review steals unfinished visits from the rest queue.");
        check(Rules.NextRemote(route, shortOrdinary)?.Id == Find("offered_signature").Id, "Short courtship blocks unfinished visits before informed farewell.");
        var shortLeaving = Play("farewell_review", shortOrdinary);
        check(Rules.Available(story, farewell, shortLeaving), "Explicit short-history farewell remains blocked.");
        var farewellResults = Program.Walk(farewell, shortLeaving);
        check(farewellResults.Any(s => s.Has("jerribeth.farewell") && !s.Has("jerribeth.developed_future")), "Short farewell silently upgrades its history.");

        // Historical flags reproduce the completed original three-scene shortcut, without resetting them for migration.
        var legacy = Program.Copy(core);
        legacy.Flags.UnionWith(new[] { "jerribeth.future", "jerribeth.committed", "jerribeth.chosen_future", "jerribeth.ordinary", "jerribeth.at_ease" });
        legacy.Times["jerribeth.future"] = 500;
        legacy.Times["jerribeth.ordinary"] = 550;
        check(!Rules.Available(story, farewell, legacy), "Old ordinary bypasses the informed farewell decision.");
        check(Find("old_promise").ManualOnly && Rules.Available(story, Find("old_promise"), legacy), "Old unreviewed promise has no explicit shorter-history option.");
        var oldKept = Play("old_promise", legacy);
        check(oldKept.Has("jerribeth.future_settled") && !oldKept.Has("jerribeth.developed_future"), "Legacy acknowledgement silently develops the promise.");
        Endings(oldKept, false);

        for (int option = 0; option < outcomes.Length; option++)
        foreach (string history in new[] { "fresh", "old", "farewell", "short" })
        {
            bool publicAccount = option < 3;
            var state = history == "fresh" ? Core(option % 2 == 0 ? 3 : 5)
                : Program.Copy(history == "short" ? shortRoute : legacy);
            if (history == "farewell")
            {
                state.Flags.UnionWith(new[] { "jerribeth.farewell", "jerribeth.farewell_kept" });
                state.Times["jerribeth.farewell"] = 600;
                check(!Rules.Available(story, Find(campaign[0]), state), "Old farewell silently reopens the campaign.");
                check(catchup.ManualOnly && Rules.Available(story, catchup, state), "Old farewell has no manual catch-up.");
                check(Rules.NextRemote(route, state) == null, "Manual old-save offers occupy the rest queue.");
                foreach (var deferred in Program.Walk(catchup, state).Where(s => !s.Has(catchup.Id)))
                    check(deferred.Flags.SetEquals(state.Flags), "Deferring catch-up changes old history.");
                state = Play("another_evening", state);
                check(state.Has("jerribeth.catchup_requested") && state.Times["jerribeth.farewell"] == 600,
                    "Catch-up erases or retimes the old farewell.");
            }
            if (history == "short") state = Play("ordinary", state, queue: true);
            if (state.Chapter == 3)
            {
                // JER-08: the Chapter 3 courtship is eight letters; the campaign waits for Chapter 4-5.
                check(!Rules.Available(story, Find(campaign[0]), state), "JER-08: the campaign opens in Chapter 3.");
                state.Chapter = 5;
            }
            bool automatic = true;
            foreach (string id in campaign)
            {
                Func<Snapshot, bool>? pick = null;
                if (id == "counterfeit_hinge") pick = s => s.Has(option % 3 == 0 ? "jerribeth.counter_cache_broken"
                    : option % 3 == 1 ? "jerribeth.counter_stage_cut" : "jerribeth.counter_cache_intact");
                if (id == "counterfeit_clerk") pick = s => s.Has(option % 2 == 0 ? "jerribeth.counter_return_agreement" : "jerribeth.counter_hold_agreement");
                if (id == "counterfeit_audience") pick = s => s.Has(publicAccount ? "jerribeth.counter_public_account" : "jerribeth.counter_private_archive");
                state = Play(id, state, pick, automatic);
                if (history == "fresh")
                {
                    var late = Program.Copy(state); late.Chapter = 5; late.Hour += 10000;
                    check(!Rules.Available(story, future, late), "Partial purchaser/counteroffer history prematurely unlocks developed future.");
                }
            }
            if (state.Chapter == 3)
                check(!Rules.Available(story, visit, state), "Settlement consequence ignores Act 5 restriction.");
            state.Chapter = 5;
            check(!Rules.Available(story, visit, state), "Settlement visitor ignores the freshly completed predecessor delay.");
            state.Hour += visit.DelayHours;
            check(Rules.Available(story, visit, state), "Played settlement cannot begin after its delay.");
            foreach (string flag in new[] { "jerribeth.closed", "jerribeth.unavailable" })
            {
                var blocked = Program.Copy(state); blocked.Flags.Add(flag);
                check(!Rules.Available(story, visit, blocked), "Catch-up overrides native or authored closure: " + flag);
            }
            var wrongArea = Program.Copy(state); wrongArea.Area = "elsewhere";
            check(!Rules.Available(story, visit, wrongArea), "Settlement ignores remote area restrictions.");
            state = Play("settlement_visit", state, s => s.Has("jerribeth." + outcomes[option]), automatic);
            check(!Rules.Available(story, room, state), "Room follow-through ignores its fresh predecessor timestamp.");
            state = Play("room_measure", state,
                s => s.Has(option % 2 == 0 ? "jerribeth.room_loop" : "jerribeth.room_terrace")
                    && s.Has(option % 2 == 0 ? "jerribeth.room_desire" : "jerribeth.room_quiet"), automatic);
            check(state.Has("jerribeth.settlement_kept"), "Played consequences fail to unlock future consideration.");
            if (history == "fresh")
            {
                state = Play("future", state, s => s.Has("jerribeth.fate_terms"), queue: true);
                check(state.Has("jerribeth.developed_future"), "Fresh completed campaign cannot earn its future.");
                check(!Rules.Available(story, reaffirm, state), "Fresh developed promise needlessly repeats as migration.");
            }
            else
            {
                state.Hour += reaffirm.DelayHours;
                var answers = Program.Walk(reaffirm, state, (node, _) => seen.Add(reaffirm.Id + "/" + node));
                check(answers.Any(s => s.Has("jerribeth.promise_held") && !s.Has("jerribeth.developed_future")), "Old promise cannot remain modest after new visits.");
                var closed = answers.Single(s => s.Has("jerribeth.closed"));
                check(closed.Has("jerribeth.committed") && EndingIds(closed).SequenceEqual(new[] { "jerribeth.ending_apart" }),
                    "Later closure resets old commitment or keeps a positive ending.");
                foreach (var deferred in answers.Where(s => !s.Has(reaffirm.Id)))
                    check(deferred.Flags.SetEquals(state.Flags), "Deferring reaffirmation changes old promises.");
                state = Play("promise_revisited", state, s => s.Has("jerribeth.developed_future"), automatic);
            }
            Endings(state, true);
            check(state.Has("seelah.committed") && state.Has("kiana.committed"), "Jerribeth progression changes unrelated romances.");
        }

        foreach (var scene in new[] { visit, room, reaffirm })
        foreach (var node in scene.Nodes)
            check(seen.Contains(scene.Id + "/" + node.Id), "Jerribeth progression node was not exercised: " + scene.Id + "/" + node.Id);
    }
}
