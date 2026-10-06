using System;
using System.Linq;
using Tirabade;

internal static class EmberAssembledTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        string[] visits = {
            "drawing", "visitor", "rain", "paper_bird", "missing_cloth", "courtyard_play", "after_applause", "second_ending",
            "something_you_cannot_do", "the_empty_basket", "the_cold_side", "the_missing_covering", "a_question_at_the_yard",
            "what_did_not_mend", "the_person_in_the_title", "the_words_people_keep", "a_letter_with_no_road",
            "an_answer_from_elsewhere", "where_she_is_needed", "the_afternoon_not_promised"
        };
        // Complement the exhaustive contribution tests with actual acquisition through the original eight visits.
        foreach (bool trickster in new[] { false, true })
        foreach (bool lastOutcome in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 3, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(new[] { "ember.present", "seelah.committed", "konomi.committed" });
            state.AvailableContacts.Add("2779754eecffd044fbd4842dba55312c");
            if (trickster) state.Flags.Add("trickster");
            foreach (string id in visits)
            {
                var book = story.Scenes.Single(s => s.Id == "ember." + id);
                if (id == "where_she_is_needed") state.Chapter = 5;
                state.Hour += book.DelayHours;
                check(Program.CurrentAvailable(story, book, state), "Full played Ember history cannot enter " + book.Id);
                var before = Program.Copy(state);
                var completed = Program.Walk(book, state)
                    .Where(result => result.Has(book.Id) && !result.Has("ember.closed")).ToArray();
                check(completed.Length > 0, "Full played Ember history has no continuation at " + book.Id);
                state = lastOutcome ? completed.Last() : completed.First();
                check(before.Flags.IsSubsetOf(state.Flags), "Ember continuation erased earlier played history.");
                check(state.Has("seelah.committed") && state.Has("konomi.committed") && !state.Has("ember.lovers"),
                    "Ember friendship changes another relationship or grants romance.");
                if (id == "second_ending")
                    check(state.Has("ember.puppet_afternoons_kept"), "The actual old conclusion did not earn the new campaign entry.");
            }
            check(visits.All(id => state.Has("ember." + id)) && state.Has("ember.trusted_friend")
                && state.Has("ember.campaign_developed"), "Full played Ember friendship lacks its earned conclusion.");
            var endings = story.Scenes.Where(s => s.Relationship == "ember" && s.Owner == "Epilogue"
                && Program.CurrentAvailable(story, s, state)).ToArray();
            check(endings.Length == 1, "Full played Ember history has missing or overlapping endings.");
            var finished = Program.Walk(endings.Single(), state).ToArray();
            check(finished.Any(result => result.Has(endings[0].Id)), "Ember's earned ending cannot finish.");
        }
    }
}
