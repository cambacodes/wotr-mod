using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// NM1 (2026-10-01): the Nocticula acquired correspondence within its Chapter 5 budget (storylines/nm1_nocticula.py).
// The six letters arrive as two deliveries (later letters folded into earlier ones, nm1_fold.py), the commitment is reached
// in the second, a save between two letters still gets the next one standalone, the harbor join and the acquired harbor
// are deferred (retired by gating on the runtime-held chapter_later), and the commitment has its own closing page.
internal static class Nm1BudgetTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string A = "noct.acq.";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 1000, Area = Drezen };
        state.Flags.UnionWith(flags);
        if (flags.Contains("noct.complete")) HouseholdTests.Earn(story, state, "nocticula.payoff.ordinary");
        if (flags.Contains(A + "renewed_agreement")) HouseholdTests.Earn(story, state, "nocticula.acquisition.payoff.ordinary");
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 100;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var first = S(A + "the_missing_line");
        var second = S(A + "the_paid_address");
        var guests = new[] { "her_hand", "borrowed_signature", "the_retained_copy", "an_answer_of_her_own" }.Select(k => S(A + k)).ToArray();
        check(first.Nodes.Any(n => n.Id == "her_hand.arrives") && first.Nodes.Any(n => n.Id == "borrowed_signature.arrives")
              && second.Nodes.Any(n => n.Id == "the_retained_copy.arrives") && second.Nodes.Any(n => n.Id == "an_answer_of_her_own.arrives"),
            "NM1_Nocticula_Folded: the correspondence is not two deliveries.");

        var start = World(story, 5, "trickster", A + "requested", A + "seal_received", A + "council_disclosed", "noct.socoth_plan_exposed", A + "audience_question");
        Rules.Complete(story, start);
        var letters = story.Scenes.Where(s => s.Relationship == "nocticula.acquisition" && Rules.IsMailbagLetter(s)).ToArray();
        string[] Due(Snapshot w) => letters.Where(s => Program.CurrentAvailable(story, s, w)).Select(s => s.Id).ToArray();
        var ready = Later(story, start, first.DelayHours);
        check(Due(ready).SequenceEqual(new[] { first.Id }), "NM1_Nocticula_Folded: the first delivery is not the only letter due: " + string.Join(", ", Due(ready)));
        var afterFirst = Program.Walk(first, ready).Where(r => r.Has(A + "borrowed_signature_done")).ToList();
        check(afterFirst.Count > 0 && afterFirst.All(r => r.Has(A + "her_hand_done") && r.Has(A + "correspondence_trial") && r.Has(A + "undertaking_held")),
            "NM1_Nocticula_Folded: the first delivery does not carry her hand and the borrowed signature.");
        int commits = 0;
        foreach (var carried in afterFirst)
        {
            var next = Later(story, carried, second.DelayHours);
            check(Due(next).SequenceEqual(new[] { second.Id }) && guests.All(g => !Program.CurrentAvailable(story, g, Later(story, carried, 500))),
                "NM1_Nocticula_Folded: a folded letter arrives a second time, or the second delivery is not alone.");
            foreach (var done in Program.Walk(second, next))
            {
                check(Due(Later(story, done, 500)).Length == 0, "NM1_Nocticula_Folded: a third acquisition letter follows the second delivery.");
                if (done.Has(A + "renewed_agreement")) commits++;
            }
        }
        check(commits > 0, "NM1_Nocticula_Folded: the second delivery never reaches the renewed agreement.");
        // A save already between two letters still receives the next one on its own.
        var between = World(story, 5, "trickster", A + "requested", A + "seal_received", A + "council_disclosed", "noct.socoth_plan_exposed",
            A + "question_sent", A + "the_missing_line_done", A + "channel_slow", first.Id);
        check(Program.CurrentAvailable(story, guests[0], Later(story, between, guests[0].DelayHours)),
            "NM1_Nocticula_Folded: a save between the missing line and her hand loses her hand.");

        // Deferred past the beta: the harbor join and the acquired harbor never open while the runtime holds chapter_later.
        var deferred = story.Scenes.Where(s => s.Id.StartsWith("noct.join.", StringComparison.Ordinal)
            || s.Relationship == "nocticula" && s.Id.Contains(".acquired.") && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        check(deferred.Length > 3 && deferred.All(s => s.Forbids.Contains("chapter_later")), "NM1_Nocticula_Deferred: a harbor scene is still deliverable.");
        foreach (var s in deferred)
        {
            var w = World(story, 5, s.Requires.Concat(s.RequiresAnyGroups.Select(g => g[0])).ToArray());
            check(!Program.CurrentAvailable(story, s, Later(story, w, s.DelayHours + 1)), "NM1_Nocticula_Deferred: " + s.Id + " opens.");
        }

        // The correspondence's own closing page.
        var page = S(A + "epilogue.correspondence");
        var ending = World(story, 6, "trickster.ever", A + "renewed_agreement");
        check(page.Owner == "Epilogue" && page.Relationship == "nocticula.acquisition" && Program.CurrentAvailable(story, page, ending)
              && !Program.CurrentAvailable(story, page, World(story, 6, "trickster.ever", A + "renewed_agreement", "noct.complete"))
              && !Program.CurrentAvailable(story, page, World(story, 6, "trickster.ever", A + "renewed_agreement", A + "council_fight"))
              && !Program.CurrentAvailable(story, page, World(story, 6, "trickster.ever"))
              && page.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0 && c.Crusade == null && c.Mythic == null && c.Alignment == null),
            "NM1_Nocticula_Page: the correspondence has no closing page, or it plays for the wrong history.");
        // eng7-l01: Last Call reads completed state, including the derived route guard.
        var coda = S("nocticula.lastcall.page");
        var codaWorld = World(story, 6, "trickster.ever", "noct.complete", "trickster.lastcall.taken", "ending.trickster");
        Rules.Complete(story, codaWorld);
        check(codaWorld.Has("lastcall.active") && codaWorld.Has("nocticula.lastcall.route_open")
              && Program.CurrentAvailable(story, coda, codaWorld), "NM1_Nocticula_Coda: completed Last Call cannot select the coda.");
        var fatalWorld = World(story, 6, "trickster.ever", "noct.complete", "sacrifice");
        Rules.Complete(story, fatalWorld);
        check(!Program.CurrentAvailable(story, coda, fatalWorld), "NM1_Nocticula_Coda: unreturned sacrifice receives the coda.");
        // eng7-l01 end
        Console.WriteLine("PASS: NM1 budget (Nocticula's correspondence in two deliveries, the harbor deferred, its closing page).");
    }
}
