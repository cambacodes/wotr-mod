using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class IrabethIndependentTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string area = "2570015799edf594daf2f076f2f975d8";
        const string beth = "280d4712dceb37f4a88e98f1f4c6e64f";
        const string ann = "b5e867e13503c6f41bb1316705efb4a2";
        Scene Get(string id) => story.Scenes.Single(s => s.Id == "irabeth." + id);
        var reached = new HashSet<string>();
        // The Trickster layer (IrabethTricksterTests) is judged by its own suite: its devices serve irabeth_dead by design.
        var newScenes = story.Scenes.Where(s => s.Relationship == "irabeth" && s.AfterDeparture == null
                                                && !s.Id.StartsWith("irabeth.trickster.", StringComparison.Ordinal)).ToArray();
        var ends = newScenes.Where(s => s.Owner == "Epilogue").ToArray();
        var bindings = story.Etudes.Keys.Concat(story.SeenCues.Keys).Concat(story.CompletedEtudes.Keys)
            .Concat(story.CompletedQuests.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys)
            .Concat(new[] { "closed", "committed", "trying", "anevia.lover", "anevia.committed", "seelah.committed", "i_affair", "a_affair" }).Distinct().ToArray();
        Snapshot Start(int chapter, string morale)
        {
            var state = new Snapshot { Chapter = chapter, Area = area, Hour = 1000 };
            state.AvailableContacts.UnionWith(new[] { beth, ann });
            state.Flags.UnionWith(new[] { "trickster", "seelah.committed" });
            state.Flags.Add("irabeth.chapter_" + (chapter == 3 ? "three" : "five"));
            if (morale != "ordinary") state.Flags.Add(morale);
            return state;
        }
        void Preserve(Snapshot before, Snapshot after)
        {
            check(before.Flags.IsSubsetOf(after.Flags), "Irabeth erases history.");
            foreach (string flag in bindings) check(before.Has(flag) == after.Has(flag), "Irabeth writes protected history: " + flag);
            foreach (var time in before.Times) check(after.Times[time.Key] == time.Value, "Irabeth rewrites a timestamp.");
            check(before.AvailableContacts.SetEquals(after.AvailableContacts), "Irabeth invents a native actor.");
        }
        Snapshot Earn(string id, Snapshot input, Func<Snapshot, bool>? select = null)
        {
            var book = Get(id); var ready = Program.Copy(input); ready.Hour += 1000;
            check(Rules.Available(story, book, ready), "Irabeth earned predecessor cannot enter " + id);
            foreach (var output in Program.Walk(book, ready, (page, at) => {
                reached.Add(book.Id + "/" + page);
                if (book.ContactUnit == null) return;
                check(Rules.ContactAvailable(story, book, at), "Irabeth loses its actual contact mid-page.");
                var absent = Program.Copy(at); absent.AvailableContacts.Remove(book.ContactUnit);
                check(!Rules.ContactAvailable(story, book, absent), "Missing actor can continue Irabeth page.");
                var dead = Program.Copy(at); dead.Flags.Add("irabeth_dead");
                check(!Rules.ContactAvailable(story, book, dead), "Irabeth death does not interrupt physical continuation.");
                var other = Program.Copy(at); other.Area = "elsewhere";
                check(!Rules.ContactAvailable(story, book, other), "Irabeth page continues in an unbound area.");
            }))
            {
                Preserve(ready, output);
                if (output.Has(book.Id)) check(!Rules.Available(story, book, output), "Completed Irabeth visit repeats.");
            }
            var chosen = Program.Walk(book, ready).First(s => s.Has(book.Id) && !s.Has("irabeth.closed") && (select == null || select(s)));
            return chosen;
        }
        Snapshot Old(string id, Snapshot input, Func<Snapshot, bool>? select = null)
        {
            var book = story.Scenes.Single(s => s.Id == id); var ready = Program.Copy(input); ready.Hour += 1000;
            check(Rules.Available(story, book, ready), "Actual legacy predecessor unavailable: " + id);
            return Program.Walk(book, ready).First(s => s.Has(id) && !s.Has("closed") && !new[] { "anevia.closed", "irabeth.closed", "anevia.courtship_requested", "irabeth.courtship_requested", "tirabade.group_closed" }.Any(flag => s.Has(flag) && !ready.Has(flag)) && (select == null || select(s)));
        }
        Snapshot Affair(Snapshot state, bool both)
        {
            foreach (string id in new[] { "i_watch", "i_hands", "i_respite", "i_crossing", "i_morning" })
                state = Old(id, state, s => id != "i_crossing" || s.Has("i_affair"));
            check(state.Has("i_affair") && state.Has("i_will_tell"), "Legacy affair fixture did not play the affair and disclosure promise.");
            if (!both) return state;
            foreach (string id in new[] { "a_cup", "a_errand", "a_roof", "a_crossing", "a_morning" })
                state = Old(id, state, s => id != "a_crossing" || s.Has("a_affair"));
            check(!Rules.Available(story, Get("one_truth_to_tell"), state), "Unresolved dual affairs use a single-affair disclosure.");
            foreach (string id in new[] { "reckoning", "a_truth", "i_truth", "table", "ordinary", "i_self" })
                state = Old(id, state, s => id != "table" || s.Has("trying"));
            return state;
        }
        void Ending(Snapshot state, string expected)
        {
            var actual = ends.Where(e => Rules.Available(story, e, state)).ToArray();
            check(actual.Length == 1 && actual[0].Id == "irabeth.ending_" + expected, "Irabeth overlapping or absent ending: " + expected);
            foreach (var result in Program.Walk(actual.Single(), state, (page, _) => reached.Add(actual[0].Id + "/" + page))) Preserve(state, result);
        }
        void Special(Snapshot state)
        {
            var independent = Program.Copy(state); independent.Flags.Add("tirabade.group_closed");
            foreach (var pair in new[] { ("irabeth_dead", "loss"), ("irabeth_gone", "loss"), ("swarm", "changed"), ("true_lich", "changed"), ("inhuman", "changed"), ("ascended", "ascent"), ("sacrifice", "sacrifice") })
            { var changed = Program.Copy(independent); changed.Flags.Add(pair.Item1); Ending(changed, pair.Item2); }
            var overlap = Program.Copy(independent); overlap.Flags.UnionWith(new[] { "irabeth_dead", "irabeth_gone", "inhuman", "ascended", "sacrifice" }); Ending(overlap, "loss");
            overlap.Flags.Remove("irabeth_dead"); overlap.Flags.Remove("irabeth_gone"); Ending(overlap, "changed");
            overlap.Flags.Remove("inhuman"); Ending(overlap, "ascent");
            var aeon = Get("ending_aeon");
            check(Rules.Available(story, aeon, independent), "Irabeth has no earned Aeon rewrite account.");
            Program.Walk(aeon, independent, (page, _) => reached.Add(aeon.Id + "/" + page));
        }

        foreach (string acquisition in new[] { "fresh", "affair", "shared", "split", "widow" })
        foreach (int chapter in new[] { 3, 5 })
        foreach (int variation in Enumerable.Range(0, 3))
        {
            string morale = new[] { "ordinary", "broken", "encouraged" }[variation];
            var state = Start(chapter, morale);
            // An existing independent Anevia romance can precede Irabeth-only acquisition.
            // It cannot precede the retained dual-affair acquisition guarded by the bridge.
            if (acquisition is not ("shared" or "split"))
            {
                if (variation == 1) state.Flags.UnionWith(new[] { "anevia.lover", "anevia.committed" });
                if (variation == 2) state.Flags.UnionWith(new[] { "anevia.lover", "anevia.closed" });
            }
            if (acquisition is "shared" or "split")
            {
                state = Affair(state, true);
                if (acquisition == "split")
                {
                    if (story.Scenes.Any(s => s.Id == "tirabade.negotiated_table"))
                    {
                        var parting = story.Scenes.Single(s => s.Id == "parting");
                        state.Hour += 1000;
                        check(Rules.Available(story, parting, state), "Played old triad cannot discuss separate relationships.");
                        state = Program.Walk(parting, state).First(s => s.Has(parting.Id)
                            && s.Has("tirabade.irabeth_continuation_invited")
                            && s.Has("tirabade.anevia_continuation_invited") && !s.Has("closed"));
                    }
                    else
                    {
                        // Standalone manuscript fixture only; the combined candidate plays the actual bridge above.
                        state.Flags.UnionWith(new[] { "tirabade.group_closed", "tirabade.irabeth_continuation_invited" });
                    }
                    state = Earn("after_the_shared_answer", state);
                }
                else state = Earn("a_day_of_our_own", state);
                if (variation != 0 && story.Scenes.Any(s => s.Id == "anevia.a_place_of_our_own"))
                {
                    string invitation = acquisition == "shared" ? "anevia.a_place_of_our_own" : "anevia.an_invitation_afterward";
                    var book = story.Scenes.Single(s => s.Id == invitation);
                    state.Hour += 1000;
                    check(Rules.Available(story, book, state), "Played legacy predecessors cannot earn Anevia's individual invitation.");
                    state = Program.Walk(book, state).First(s => s.Has(invitation) && s.Has("anevia.lover") && !s.Has("anevia.closed"));
                }
            }
            else if (acquisition == "affair")
            {
                state = Affair(state, false);
                state = Earn("one_truth_to_tell", state);
                state = Earn("anevias_answer", state);
                state = Earn("the_evening_she_chose", state);
            }
            else
            {
                if (acquisition == "widow") state.Flags.Add("anevia_dead");
                state = Earn("a_name_on_the_list", state);
                state = Earn("the_question_outside_duty", state);
                if (acquisition != "widow")
                { state = Earn("anevias_answer", state); state = Earn("the_evening_she_chose", state); }
            }
            check(state.Has("irabeth.lover") && state.Has("irabeth.personal_ready"), "Played acquisition does not earn personal route.");
            if (acquisition is "fresh" or "widow") check(!state.Has("i_affair") && !state.Has("a_affair") && !state.Has("trying"), "Negotiation invents affairs or shared commitment.");
            Special(state);
            string iron = new[] { "iron_read", "iron_uncertain", "iron_assay" }[variation];
            state = Earn("the_seized_wagon", state, s => s.Has("irabeth." + iron));
            check(new[] { "iron_read", "iron_uncertain", "iron_assay" }.Count(f => state.Has("irabeth." + f)) == 1, "Iron check merges failure, success and nonroll history.");
            state = Earn("the_sealed_account", state, s => s.Has("irabeth.account_" + (variation == 1 ? "open" : "sealed")));
            state = Earn("ten_minutes_in_a_hall", state);
            state = Earn("the_cost_afterward", state, s => s.Has("irabeth.instruction_" + (variation == 2 ? "supported" : "her_name")));
            state = Earn("without_an_account", state);
            if (chapter == 3)
            {
                if (variation != 1)
                {
                    state = Earn("before_the_unmapped_road", state);
                    state.Chapter = 4;
                    check(!Rules.Available(story, Get("the_person_who_returns"), state), "Chapter4 has an invented physical Irabeth return.");
                    state = Earn("an_unposted_line", state);
                }
                state.Chapter = 5;
                state.Flags.Remove("irabeth.chapter_three"); state.Flags.Add("irabeth.chapter_five");
            }
            else check(!Rules.Available(story, Get("an_unposted_line"), state), "Fresh Chapter5 borrows an Abyss letter.");
            state.Flags.UnionWith(new[] { "irabeth.scar_known", "irabeth.queen_loss_known" });
            state = Earn("the_person_who_returns", state);
            state = Earn("when_the_instruction_is_used", state);
            string future = new[] { "lasting", "open", "friends" }[variation];
            state = Earn("a_road_she_would_choose", state, s => s.Has("irabeth.future_" + future));
            Special(state);
            var wifeAbsent = Program.Copy(state); wifeAbsent.Flags.Add("anevia_gone");
            Earn("the_hour_before_battle", wifeAbsent);
            state = Earn("the_hour_before_battle", state);
            check(state.Has("irabeth.campaign_kept"), "Full actual Irabeth chain lacks earned farewell.");
            check(state.Has("broken") == (morale == "broken") && state.Has("encouraged") == (morale == "encouraged"), "Romance cures or overwrites native morale.");
            if (acquisition == "shared" && !state.Has("tirabade.group_closed"))
            {
                check(!ends.Any(e => Rules.Available(story, e, state)), "Active legacy shared route receives competing individual epilogue.");
                state.Flags.Add("tirabade.group_closed");
            }
            Ending(state, future);
            foreach (string wife in new[] { "anevia_dead", "anevia_gone" })
            { var changed = Program.Copy(state); changed.Flags.Add(wife); Ending(changed, future); }
            // Q2 (Sol r5 COX): Anevia came back to the gate on the Trickster path; the absent-wife page is not hers.
            { var back = Program.Copy(state); back.Flags.Add("anevia_gone"); back.Flags.Add("anevia.trickster.returned"); Ending(back, future); }
            Special(state);
            foreach (string refusal in new[] { "closed", "irabeth.closed" })
            { var changed = Program.Copy(state); changed.Flags.Add(refusal); check(!ends.Any(e => Rules.Available(story, e, changed)), "Ending ignores an explicit refusal."); }
        }

        var early = Start(5, "ordinary");
        early = Earn("a_name_on_the_list", early);
        var absentWife = Program.Copy(early); absentWife.Flags.Add("anevia_gone");
        absentWife = Earn("the_question_outside_duty", absentWife);
        check(!absentWife.Has("irabeth.lover") && absentWife.Has("irabeth.absence_wait"), "Missing wife fabricated a marital agreement.");
        var living = Earn("the_question_outside_duty", early);
        var delayed = Earn("a_name_on_the_list", Start(3, "ordinary"));
        delayed = Earn("the_question_outside_duty", delayed);
        delayed.Chapter = 5; delayed.Flags.Remove("irabeth.chapter_three"); delayed.Flags.Add("irabeth.chapter_five");
        delayed = Earn("anevias_answer", delayed); delayed = Earn("the_evening_she_chose", delayed);
        check(delayed.Has("irabeth.began_chapter_five") && !delayed.Has("irabeth.began_chapter_three"), "Pending early proposal is mistaken for an early lover.");
        var lossDuringProposal = Program.Copy(living); lossDuringProposal.Flags.Add("anevia_dead");
        lossDuringProposal = Earn("after_the_answer_was_lost", lossDuringProposal);
        check(lossDuringProposal.Has("irabeth.lover") && !lossDuringProposal.Has("irabeth.marital_terms_agreed"), "Death during negotiation invents marital agreement.");
        var lostAffair = Affair(Start(5, "ordinary"), false); lostAffair.Flags.Add("anevia_dead");
        Earn("after_the_answer_was_lost", lostAffair);
        var unavailable = Program.Copy(living); unavailable.AvailableContacts.Remove(ann);
        check(!Rules.Available(story, Get("anevias_answer"), unavailable), "Marital interview creates absent wife.");
        living = Earn("anevias_answer", living); living = Earn("the_evening_she_chose", living);
        Ending(living, "unfinished");
        var changedMarriage = Program.Copy(living); changedMarriage.Flags.Add("anevia_dead"); changedMarriage.Hour += 1000;
        check(Rules.Available(story, Get("the_seized_wagon"), changedMarriage), "Spouse death globally closes Irabeth's already negotiated individual relationship.");
        foreach (var book in newScenes.Where(s => !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)))
        {
            var fixture = Start(book.MinChapter, "ordinary"); fixture.Flags.UnionWith(book.Requires);
            if (book.RequiresAny.Length > 0) fixture.Flags.Add(book.RequiresAny[0]);
            fixture.Hour = 100000;
            foreach (string blocker in new[] { "closed", "irabeth.closed", "irabeth_dead", "irabeth_gone", "swarm", "true_lich", "inhuman" })
            { var blocked = Program.Copy(fixture); blocked.Flags.Add(blocker); check(!Rules.Available(story, book, blocked), "Irabeth ignores blocker " + blocker + " in " + book.Id); }
            if (book.ContactUnit != null)
            {
                check(book.AdditionalContactUnits.Length == 0, "Individual Irabeth scene claims a paired actor.");
                var wrong = Program.Copy(fixture); wrong.AvailableContacts.Remove(book.ContactUnit);
                check(!Rules.Available(story, book, wrong), "Individual scene enters without bound actor.");
            }
        }
        foreach (var book in newScenes)
        foreach (var page in book.Nodes)
            check(reached.Contains(book.Id + "/" + page.Id), "Unplayed Irabeth page: " + book.Id + "/" + page.Id);
    }
}
