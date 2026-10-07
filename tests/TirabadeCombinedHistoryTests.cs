using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class TirabadeCombinedHistoryTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string anevia = "b5e867e13503c6f41bb1316705efb4a2";
        const string irabeth = "280d4712dceb37f4a88e98f1f4c6e64f";
        Scene Get(string id) => story.Scenes.Single(s => s.Id == id);
        Snapshot Fresh()
        {
            var state = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(new[] { "trickster", "irabeth.chapter_five" });
            state.AvailableContacts.UnionWith(new[] { anevia, irabeth });
            Rules.Complete(story, state);
            return state;
        }
        Snapshot Play(string id, Snapshot input, Func<Snapshot, bool>? choose = null, bool allowClosed = false)
        {
            var state = Program.Copy(input); state.Hour += 1000;
            var book = Get(id);
            Rules.Complete(story, state);
            check(Rules.Available(story, book, state), "Unavailable played predecessor: " + id);
            return Program.Walk(book, state, (_, partial) => {
                if (book.ContactUnit == null) return;
                check(Rules.ContactAvailable(story, book, partial), "Authored partial effects interrupt contact: " + id);
                foreach (string actor in new[] { book.ContactUnit }.Concat(book.AdditionalContactUnits))
                {
                    var lost = Program.Copy(partial); lost.AvailableContacts.Remove(actor);
                    check(!Rules.ContactAvailable(story, book, lost), "Lost participant can continue: " + id);
                    lost.AvailableContacts.Add(actor);
                    check(Rules.ContactAvailable(story, book, lost), "Restored participant cannot continue: " + id);
                }
            }).First(output => output.Has(id) && !output.Has("closed")
                && (allowClosed || (!output.Has("anevia.closed") && !output.Has("irabeth.closed")))
                && (choose == null || choose(output)));
        }
        Snapshot AcquireA(Snapshot state)
        {
            foreach (string id in new[] { "unborrowed_hour", "a_question_at_home", "beths_question", "beths_answer", "her_own_answer" })
                state = Play("anevia." + id, state);
            return state;
        }
        Snapshot AcquireI(Snapshot state)
        {
            foreach (string id in new[] { "a_name_on_the_list", "the_question_outside_duty", "anevias_answer", "the_evening_she_chose" })
                state = Play("irabeth." + id, state);
            return state;
        }
        foreach (bool aFirst in new[] { true, false })
        {
            var state = aFirst ? AcquireI(AcquireA(Fresh())) : AcquireA(AcquireI(Fresh()));
            state.Hour += 1000;
            check(Rules.Available(story, Get("tirabade.negotiated_table"), state), "Both played acquisitions do not reach group proposal");
            var joined = Play("tirabade.negotiated_table", state, s => s.Has("trying"));
            check(!joined.Has("a_affair") && !joined.Has("i_affair") && !joined.Has("reckoning"), "Honest joining fabricates history");
            Play("ordinary", joined);
        }
        var friends = AcquireI(AcquireA(Fresh()));
        foreach (string id in new[] { "the_seized_wagon", "the_sealed_account", "ten_minutes_in_a_hall", "the_cost_afterward", "without_an_account", "the_person_who_returns", "when_the_instruction_is_used" })
            friends = Play("irabeth." + id, friends);
        friends = Play("irabeth.a_road_she_would_choose", friends, state => state.Has("irabeth.future_friends"));
        check(friends.Has("irabeth.future_friends"), "Friendship not earned");
        check(!Rules.Available(story, Get("tirabade.negotiated_table"), friends), "Earned friendship still reopens romantic triad");
        friends = Play("irabeth.the_hour_before_battle", friends);
        check(Rules.Available(story, Get("irabeth.ending_friends"), friends), "Friendship closure blocks her own farewell ending");

        var split = AcquireI(AcquireA(Fresh()));
        split = Play("tirabade.negotiated_table", split, state => state.Has("trying"));
        foreach (string id in new[] { "borrowed_signature", "the_paper_seller", "the_woman_with_the_basket", "the_counting_room", "what_the_warning_cost", "the_evening_without_a_case", "the_life_she_lived" })
            split = Play("anevia." + id, split);
        split = Play("anevia.a_key_that_is_hers", split, state => state.Has("anevia.closed"), true);
        check(split.Has("anevia.closed") && !split.Has("irabeth.closed") && split.Has("tirabade.group_closed"), "Wrong split witness");
        var bridges = story.Scenes.Where(book => book.Relationship == "tirabade" && Rules.Available(story, book, split)).ToArray();
        var ends = story.Scenes.Where(book => book.Relationship == "irabeth" && book.Owner == "Epilogue" && Rules.Available(story, book, split)).ToArray();
        check(bridges.Length == 0 && ends.Length == 1, "Ending one romance strands remaining lover or leaves shared continuation");
        check(split.Has("trying") && split.Has("irabeth.lover") && !split.Has("tirabade.irabeth_continuation_invited"), "Split rewrites earned history or fabricates invitation");

        foreach (bool rejectA in new[] { true, false })
        {
            var local = Fresh();
            string rejected = rejectA ? "anevia" : "irabeth";
            string remaining = rejectA ? "irabeth" : "anevia";
            string opening = rejectA ? "anevia.unborrowed_hour" : "irabeth.a_name_on_the_list";
            local = Play(opening, local, state => state.Has(rejected + ".closed"), true);
            check(local.Has("tirabade.group_closed"), "Independent refusal did not record shared consequence");
            var oldIds = rejectA
                ? new[] { "i_watch", "i_hands", "i_respite", "i_crossing", "i_morning" }
                : new[] { "a_cup", "a_errand", "a_roof", "a_crossing", "a_morning" };
            foreach (string id in oldIds)
                local = Play(id, local, state => !state.Has(remaining + ".closed") && !state.Has(remaining + ".courtship_requested")
                    && (!id.EndsWith("crossing") || state.Has(rejectA ? "i_affair" : "a_affair")), true);
            var disclosures = rejectA
                ? new[] { "irabeth.one_truth_to_tell", "irabeth.anevias_answer", "irabeth.the_evening_she_chose" }
                : new[] { "anevia.one_truth", "anevia.beths_question", "anevia.beths_answer", "anevia.her_own_answer" };
            foreach (string id in disclosures)
                local = Play(id, local, state => !state.Has(remaining + ".closed"), true);
            check(local.Has(remaining + ".lover"), "Early local refusal strands other earned romance");
        }

        var past = AcquireI(Fresh());
        foreach (string id in new[] { "the_seized_wagon", "the_sealed_account", "ten_minutes_in_a_hall", "the_cost_afterward", "without_an_account", "the_person_who_returns", "when_the_instruction_is_used" })
            past = Play("irabeth." + id, past);
        past = Play("irabeth.a_road_she_would_choose", past, state => state.Has("irabeth.future_friends"));
        past = Play("anevia.unborrowed_hour", past);
        foreach (string id in new[] { "anevia.a_question_at_home", "anevia.beths_question" })
        {
            var seen = new HashSet<string>();
            bool interview = id.EndsWith("beths_question");
            if (interview) past = Play("anevia.a_question_at_home", past);
            Program.Walk(Get(id), past, (page, _) => seen.Add(page));
            check(!seen.Contains(interview ? "already_lovers" : "her_marriage")
                && seen.Contains(interview ? "past_lovers" : "past_marriage"), "Friendship does not select truthful past-romance callback");
        }
    }
}
