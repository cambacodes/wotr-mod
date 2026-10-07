using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class EritriceRoundThreeTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string P = "eritrice.trickster.";
        const string M = "eritrice.minutes.";
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Snapshot World(params string[] flags)
        {
            var state = new Snapshot { Chapter = 5, Hour = 5000,
                CrusadeResources = new Dictionary<string, int> { ["Favors"] = 10000 } };
            state.Flags.UnionWith(flags);
            state.Flags.UnionWith(new[] { "trickster", "trickster.ever", "chapter_later" });
            Rules.Complete(story, state);
            return state;
        }
        Snapshot Play(string id, Snapshot state, string node, string target)
        {
            var scene = S(id);
            Rules.Complete(story, state);
            int index = scene.Nodes.Single(n => n.Id == node).Choices.FindIndex(c => c.Next == target);
            check(index >= 0, "Missing answer: " + id + "/" + node + "/" + target);
            var results = Program.WalkVia(scene, state, node, index);
            check(results.Count > 0, "No selectable continuation: " + id + "/" + node + "/" + target);
            return results.First();
        }
        var proof = S("eritrice.council.a_proof");
        foreach (bool orange in new[] { false, true })
        {
            var state = World("eritrice.started", M + "point_one", "chadali.closed");
            if (orange) state.Flags.Add("council.orange_called");
            Rules.Complete(story, state);
            check(Rules.Available(story, proof, state), "Chadali closure blocks Cobblehoof's recollection");
            var answers = proof.Nodes.Single(n => n.Id == "start").Choices;
            check(answers.Take(2).All(c => Rules.ChoiceAvailable(c, state)), "Cobblehoof question has no answer after closure");
            check(Program.Walk(proof, state).Any(r => r.Has(proof.Id)), "Cobblehoof recollection cannot finish");
        }
        var petition = Play(P + "council.late_motion", World("council.debrief_motion"), "start", "reply");
        petition = Play(P + "special_sitting", petition, "open", "friendly");
        var arranged = Program.WalkVia(S(P + "fought.tabled"), World("council.fought_nocta_allied", "eritrice.lost_at_council.latched"), "ruling_betrayal", 0).First();
        check(arranged.Has(P + "apology_arranged"), "Apology arrangement was not paid");
        var reconciled = Play(P + "special_sitting", arranged, "open", "apology");
        check(reconciled.Has(P + "cost.apologised"), "Reconciliation was not spoken");
        foreach (var entry in new[] { (state: petition, suffix: "_petition"), (state: reconciled, suffix: "_reconciled") })
        {
            var point = S(M + "point_one.drezen");
            var motion = point.Nodes.Single(n => n.Id == "motion" + entry.suffix);
            var state = Play(point.Id, entry.state, motion.Id, "minutes" + entry.suffix);
            state = Program.Walk(S(M + "the_convening.drezen"), state).First(r => r.Has(M + "the_convening"));
            state = Play(M + "quill.drezen", state, "held", "hand" + entry.suffix);
            check(state.Has(M + "wrote_in_the_minutes") || state.Has(M + "quill"), "Unprimed quill walk cannot finish");
        }
        foreach (string suffix in new[] { "", ".drezen" })
        {
            var state = World("eritrice.started", M + "quill");
            var second = S(P + "council.second_reading" + suffix);
            state = Program.WalkVia(second, state, "refused", 0).First();
            state = Play(P + "council.third_reading" + suffix, state, "start", "aye");
            state.Chapter = 6;
            state.Flags.UnionWith(new[] { "trickster.lastcall.taken", "ending.trickster" });
            Rules.Complete(story, state);
            var page = S("eritrice.lastcall.page");
            check(Rules.Available(story, page, state), "Earned third reading lost Last Call: " + suffix);
            state.Flags.Add("eritrice.closed");
            Rules.Complete(story, state);
            check(!Rules.Available(story, page, state), "Closure reopened Last Call: " + suffix);
        }
        Console.WriteLine("PASS: Eritrice round-three counterexample walks");
    }
}
