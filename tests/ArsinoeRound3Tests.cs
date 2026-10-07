using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Audit regressions run independently of the inherited Konomi return fixture.
internal static class ArsinoeRound3Tests
{
    private static Snapshot World(Story story, params string[] flags)
    {
        var state = new Snapshot { Chapter = 5, Area = "2570015799edf594daf2f076f2f975d8", Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.AvailableContacts.Add("a609ed9b2205d034bb3bb04d2a255681");
        Rules.Complete(story, state);
        return state;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        var collection = story.Scenes.Single(s => s.Id == "arsinoe.trickster.cauldron.collection");
        foreach (string absent in new[] { "konomi.closed", "konomi.retained_dead", "konomi.dismissed" })
        foreach (bool recalled in new[] { false, true })
        {
            var state = World(story, "trickster", "arsinoe.capital", "arsinoe.trickster.primed",
                "arsinoe.trickster.cauldron.lease", absent);
            if (recalled) state.Flags.Add("konomi.trickster.cost.recalled");
            Rules.Complete(story, state);
            check(Rules.Available(story, collection, state), "Historical rider blocks collection: " + absent);
            var seen = new HashSet<string>();
            Program.Walk(collection, state, (page, _) => seen.Add(page));
            check(seen.Contains("rider") == recalled, "Invoice ignores its payment receipt.");
        }

        var pot = story.Scenes.Single(s => s.Id == "arsinoe.trickster.epilogue.pot_returned");
        var estate = World(story, "trickster.ever", "trickster.failed", "arsinoe.trickster.cost.lien",
            "arsinoe.trickster.cost.collateral_word", "arsinoe.trickster.cost.rent_grace", "sacrifice");
        estate.Chapter = 6; Rules.Complete(story, estate);
        check(Rules.Available(story, pot, estate), "Genuine death loses documentary returned-stone page.");
        var paragraphs = Rules.VisibleParagraphs(pot.Nodes[0], estate)
            .Select(p => pot.Nodes[0].Paragraphs.IndexOf(p)).ToHashSet();
        check(new[] { 2, 6, 15 }.All(paragraphs.Contains), "Estate rent, word or grace missing.");
        check(!new[] { 16, 17, 18, 19 }.Any(paragraphs.Contains), "Estate history stages a living invitation.");

        var late = story.Scenes.Single(s => s.Id == "arsinoe.trickster.late.commit");
        foreach (bool returning in new[] { false, true })
        {
            var state = World(story, "trickster", "trickster.ever", "arsinoe.started",
                "arsinoe.trickster.stays_to_collect");
            state = LateAcceptanceInventory2Tests.Earn(story, check, "arsinoe.trickster.late.ask",
                state, "arsinoe.trickster.late_accepted");
            if (returning) state.Flags.Add("arsinoe.unprofitable_night_shared");
            state.Chapter = 6; Rules.Complete(story, state);
            check(Rules.Available(story, late, state), "Earned late appointment unavailable.");
            var seen = new HashSet<string>();
            Program.Walk(late, state, (page, _) => seen.Add(page));
            check(seen.SetEquals(new[] { "offer", returning ? "late_return" : "night",
                "arsinoe.trickster.late.commit.explicit.1", "morning", "deferred_evening",
                "arsinoe.trickster.late.commit.explicit.2", "table" }), "Late history repeats refusal or wrong approach.");
        }
    }
}
