using System;
using System.Linq;
using Tirabade;

internal static class ArsinoeAssembledTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        // Play the entire route; no authored predecessor or relationship flags are seeded.
        foreach (int chapter in new[] { 3, 5 })
        foreach (string pace in new[] { "courting", "slow", "friendship" })
        {
            var state = new Snapshot { Chapter = chapter, Hour = 1000,
                Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(new[] { "arsinoe.capital", "trickster", "lann.committed" });
            state.AvailableContacts.Add("a609ed9b2205d034bb3bb04d2a255681");
            foreach (var book in story.Scenes.Where(s => s.Relationship == "arsinoe" && s.ContactUnit != null
                && !s.Id.StartsWith("arsinoe.trickster.", StringComparison.Ordinal)))
            {
                if (book.Id == "arsinoe_before_the_road" && chapter == 5) continue;
                state.Chapter = Math.Max(state.Chapter, book.MinChapter);
                state.Hour += 1000;
                check(Rules.Available(story, book, state), "Assembled Arsinoe predecessor unavailable: " + book.Id);
                var outcomes = Program.Walk(book, state).Where(s => s.Has(book.Id) && !s.Has("arsinoe.closed"));
                if (book.Id == "arsinoe_roofs") outcomes = outcomes.Where(s => s.Has("arsinoe." + pace));
                if (book.Id == "arsinoe_what_she_asks")
                    outcomes = outcomes.Where(s => s.Has(pace == "courting" ? "arsinoe.committed"
                        : pace == "slow" ? "arsinoe.campaign_slow" : "arsinoe.campaign_friend"));
                state = outcomes.First();
            }
            check(state.Has("arsinoe.last_evening_kept") && state.Has("lann.committed"),
                "Assembled Arsinoe route loses its final visit or another relationship.");
            check(state.Has("arsinoe.departure_kept") == (chapter == 3), "Arsinoe departure history is wrong.");
            var endings = story.Scenes.Where(s => s.Relationship == "arsinoe" && s.Owner == "Epilogue"
                && Rules.Available(story, s, state)).ToArray();
            string ending = pace == "courting" ? "kept" : pace == "slow" ? "slow" : "friend";
            check(endings.Length == 1 && endings[0].Id == "arsinoe_ending_" + ending,
                "Played Arsinoe campaign has the wrong ending for " + pace);
            Program.Walk(endings[0], state);
        }
    }
}
