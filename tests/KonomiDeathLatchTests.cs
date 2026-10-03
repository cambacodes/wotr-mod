using System;
using System.Linq;
using Tirabade;

// Engine-q2 item 4: a committed Konomi who died at her post is remembered dead. konomi.retained_dead is a body check (true
// only while her capital scene is loaded); konomi.dead.latched records it, and konomi.dead.unreturned (the latch, withheld by
// her dead.recalled return) keeps her living endings, her Last Call coda and her call-in dark and plays her loss page.
internal static class KonomiDeathLatchTests
{
    private const string Latched = "konomi.dead.latched", Lost = "konomi.dead.unreturned", Confirmed = "konomi.retained_return_confirmed";
    private const string LossPage = "konomi.ending_lost";

    internal static void Run(Story story, Action<bool, string> check)
    {
        if (!story.Scenes.Any(s => s.Id == LossPage)) return;
        Scene Sc(string id) => story.Scenes.Single(s => s.Id == id);
        Snapshot World(params string[] flags)
        {
            var state = new Snapshot { Chapter = 6, Hour = 30000 };
            state.Flags.UnionWith(flags);
            state.Flags.Add("chapter_later");
            Rules.Complete(story, state);
            return state;
        }
        check(story.Latches.TryGetValue(Latched, out var sources) && sources.SequenceEqual(new[] { "konomi.retained_dead" })
              && story.Derived.TryGetValue(Lost, out var groups) && groups.Length == 1 && groups[0].SequenceEqual(new[] { Latched })
              && story.DerivedForbids.TryGetValue(Lost, out var lift) && lift.SequenceEqual(new[] { Confirmed }),
            "Konomi death latch: the latch or its unreturned key is not bound to the body check and her recall.");

        // The body check latches the first time it is observed, and the latch outlives it.
        var observed = World("konomi.committed", "konomi.retained_dead");
        check(observed.Has(Latched) && observed.Has(Lost), "Konomi death latch: her observed death is not recorded.");

        var living = story.Scenes.Where(s => s.Relationship == "konomi" && s.Owner == "Epilogue"
            && s.Id != LossPage && s.Id != "konomi.ending_missed_interrupted").ToArray();
        check(living.Length >= 15 && living.All(s => s.Forbids.Contains(Lost)), "Konomi death latch: a living ending does not Forbid her unreturned death.");
        var coda = Sc("konomi.lastcall.page");
        check(coda.Forbids.Contains(Lost), "Konomi death latch: her Last Call coda plays for a Konomi who stayed dead.");

        var ending = Sc("konomi.ending_private");
        var loss = Sc(LossPage);
        var dead = World("konomi.committed", Latched);
        var alive = World("konomi.committed");
        var recalled = World("konomi.committed", Latched, Confirmed);
        check(!Rules.Available(story, ending, dead) && Rules.Available(story, loss, dead), "Konomi death latch: a dead Konomi keeps her living ending, or loses her loss page.");
        check(Rules.Available(story, ending, alive) && !Rules.Available(story, loss, alive), "Konomi death latch: a living Konomi gets the loss page.");
        check(Rules.Available(story, ending, recalled) && !Rules.Available(story, loss, recalled), "Konomi death latch: the recall does not lift her death.");
        check(!Rules.Available(story, loss, World("konomi.committed", Latched, "sacrifice"))
              && Rules.Available(story, loss, World("konomi.trickster.late_committed", Latched))
              && !Rules.Available(story, loss, World("konomi.attracted", Latched)),
            "Konomi death latch: the loss page plays beside the Commander's own death, misses her late yes, or plays uncommitted.");
        check(loss.Nodes.Count == 1 && loss.Nodes[0].Text.Contains("died at her post") && loss.Nodes[0].Choices.All(c => c.Set.Length == 0),
            "Konomi death latch: the loss page is not a single effect-free page.");

        // Last Call: the coda and the call-in stay dark for the unreturned dead, and her debt does not strand the joke.
        var lastCall = new[] { "trickster", "trickster.ever", "lastcall.active", "trickster.lastcall.open", "konomi.committed",
                               "konomi.trickster.cost.debt_owed" };
        var callDead = World(lastCall.Concat(new[] { Latched }).ToArray());
        var callBack = World(lastCall.Concat(new[] { Latched, Confirmed }).ToArray());
        check(!Rules.Available(story, coda, callDead) && Rules.Available(story, coda, callBack),
            "Konomi death latch: her Last Call coda ignores her death or her recall.");
        check(!callDead.Has("konomi.lastcall.callable") && callBack.Has("konomi.lastcall.callable")
              && Sc("trickster.lastcall.last_joke").Forbids.Contains("konomi.lastcall.callable"),
            "Konomi death latch: a dead Konomi's call-in is still due (or a recalled one's is not).");
    }
}
