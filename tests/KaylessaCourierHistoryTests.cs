using System;
using System.Linq;
using Tirabade;

// D05: exercise the real dispatch answer, not a pre-seeded receipt.
internal static class KaylessaCourierHistoryTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string W = "kaylessa.wasps.";
        const string N = "kaylessa.clearing.";
        var girls = story.Scenes.Single(s => s.Id == W + "the_girls_face");
        var reply = story.Scenes.Single(s => s.Id == N + "courier_reply");
        var first = story.Scenes.Single(s => s.Id == N + "avennara");
        foreach (bool firstAlreadyRead in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 5, Hour = 5000,
                Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(new[] { "trickster", "trickster.ever", "chapter_later",
                "kaylessa.trickster.returned", "kaylessa.committed",
                "kaylessa.trickster.knife_held", "kaylessa.trickster.cost.amulet_burnt",
                "kaylessa.trickster.after.rules", W + "letter_sent" });
            HouseholdTests.Earn(story, state, "kaylessa.payoff.ordinary");
            if (firstAlreadyRead) state.Flags.Add(first.Id);
            state.AvailableContacts.Add("a1569a0739314d04cb8af1d47dcffbe0");
            Rules.Complete(story, state);
            foreach (string flag in state.Flags) state.Times[flag] = 0;
            check(Rules.Available(story, girls, state), "Courier account discussion is unavailable.");
            var dispatched = Program.WalkVia(girls, state, "courier_followup", 0);
            check(dispatched.Count > 0, "No played supplement dispatch history.");
            foreach (var sent in dispatched)
            {
                check(sent.Has(W + "courier_supplement_sent")
                    && sent.Times[W + "courier_supplement_sent"] == state.Hour,
                    "Dispatch does not start its own clock.");
                var receipt = first.Nodes.Single(n => n.Id == "receipt");
                var choices = receipt.Choices.Where(c => Rules.ChoiceAvailable(c, sent)).ToArray();
                check(choices.Length > 0 && choices.All(c => c.Next == "end"),
                    "A mature original letter acknowledges the new supplement.");
                var waiting = Program.Copy(sent); waiting.Hour += 719; Rules.Complete(story, waiting);
                check(!Rules.Available(story, reply, waiting), "Supplement reply arrives before its round trip.");
                waiting.Hour++; Rules.Complete(story, waiting);
                check(Rules.Available(story, reply, waiting), "Supplement reply is unavailable after thirty days.");
                var opened = Program.Walk(reply, waiting);
                check(opened.Count > 0 && opened.All(s => s.Has(W + "courier_acknowledged")),
                    "Opening the reply does not record acknowledgment.");
                foreach (var read in opened)
                    check(!Rules.Available(story, reply, read), "The acknowledged reply repeats.");
            }
        }
    }
}
