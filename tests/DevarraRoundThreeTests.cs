using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Continuous witnesses: authored receipts come only from executed choices.
// Native observations below are the actual escape, golem and egg readers.
internal static class DevarraRoundThreeTests
{
    const string P = "devarra.trickster.";
    const string T = "devarra.tower.";

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Snapshot Observe(Snapshot prior, params string[] native)
        {
            var state = Program.Copy(prior);
            foreach (var key in native) { state.Flags.Add(key); state.Times[key] = state.Hour; }
            foreach (var key in Rules.PendingLatches(story, state)) state.Times[key] = state.Hour;
            Rules.Complete(story, state);
            return state;
        }
        Snapshot Wait(Snapshot prior, int hours, int chapter = 3)
        {
            var state = Program.Copy(prior); state.Hour += hours; state.Chapter = chapter;
            state.Flags.Remove("devarra.chapter_three");
            if (chapter == 3) state.Flags.Add("devarra.chapter_three");
            if (chapter == 6) state.Flags.Add("chapter.six");
            if (Rules.ChapterFlag(chapter) is string flag) state.Flags.Add(flag);
            Rules.Complete(story, state); return state;
        }
        Snapshot Play(string id, Snapshot prior, string node, int choice)
        {
            var scene = S(id);
            check(Rules.Available(story, scene, prior), "Continuous Devarra witness cannot enter " + id);
            var results = Program.WalkVia(scene, prior, node, choice);
            check(results.Count > 0, "Continuous Devarra witness cannot choose " + id + "/" + node);
            return results.First();
        }
        string Render(string id, Snapshot state) => string.Join("\n", S(id).Nodes.SelectMany(n =>
            new[] { n.Text }.Concat(n.Paragraphs.Where(p => Rules.Match(p.Requires, p.Forbids, state)
                && p.AnyGroups.All(g => g.Any(state.Has))).Select(p => p.Text))));

        var start = new Snapshot { Chapter = 3, Hour = 100,
            Flags = new HashSet<string> { "trickster", "trickster.ever", "chapter_later", "devarra.chapter_three", "devarra.lair_story_heard" },
            CrusadeResources = new Dictionary<string, int> { ["Materials"] = 1000 } };
        Rules.Complete(story, start);
        var pacted = Play(P + "flight.pact", start, "terms", 0);
        var escaped = Observe(pacted, "devarra.escaped", "devarra.golems_met", "devarra.golems_calling");
        var lied = Play(P + "flight.leash", escaped, "report", 0);
        var deactivated = Observe(lied, "devarra.golems_deactivated");
        var left = Play(P + "flight.clutch_left", deactivated, "left", 0);
        var returned = Play(P + "flight.eggs", Wait(left, 48), "clutch", 7);
        var tested = Play(P + "after.tithe", Wait(returned, 48), "ending_free", 0);
        var late = Wait(tested, 200, 6);
        check(!late.Has(P + "late_committed") && !late.Has("devarra.harem.eligible")
            && !late.Has("devarra.payoff.partner") && !Rules.Available(story, S(P + "epilogue.commit"), late),
            "Tithe-only history received a romantic payoff.");
        check(!Rules.Available(story, S("devarra.lastcall.page"), Observe(late, "lastcall.h1")),
            "Tithe-only history received a Last Call partner page.");
        var proposalWorld = Wait(tested, 200, 5);
        var lateYes = Wait(Play(P + "after.late_proposal", proposalWorld, "offer", 0), 0, 6);
        check(lateYes.Has(P + "late_accepted") && lateYes.Has("devarra.committed")
            && lateYes.Has(P + "late_committed") && lateYes.Has("devarra.harem.eligible"),
            "A played late acceptance failed to establish the partner.");
        var lateNo = Play(P + "after.late_proposal", proposalWorld, "offer", 1);
        var lateWait = Play(P + "after.late_proposal", proposalWorld, "offer", 2);
        check(!lateNo.Has("devarra.harem.eligible") && !lateWait.Has(P + "late_committed"),
            "Refused or postponed late proposal became acceptance.");

        var earlyNo = Play(P + "after.tithe", Wait(returned, 48), "tithe_free", 2);
        check(!Render(P + "epilogue.refused", earlyNo).Contains("marks of the Commander"),
            "Refusal before the first climb invented visits.");
        var climbed = Play(T + "first_climb", Wait(tested, 24), "leave", 1);
        var noAfterClimb = Play(P + "after.lair", Wait(climbed, 48), "terms", 1);
        check(Render(P + "epilogue.refused", noAfterClimb).Contains("marks of the Commander"),
            "Refusal after climbing lost the earned recollection.");

        var claimed = Play(P + "after.tithe", Wait(returned, 48), "ending_free", 3);
        check(!Rules.Available(story, S(P + "after.late_proposal"), Wait(claimed, 200, 5)),
            "Pending conqueror judgment reached the late proposal.");
        var rejected = Play(P + "after.lair", Wait(claimed, 48), "verdict", 4);
        check(rejected.Has(P + "judgment_refused") && !rejected.Has("devarra.committed")
            && !Rules.Available(story, S(T + "first_climb"), Wait(rejected, 200)),
            "Devarra's rejected judgment leaked a ridge payoff.");
        foreach (bool remote in new[] { false, true })
        {
            var correctionWorld = Wait(remote ? Observe(rejected, "storyteller.dead_main") : rejected, 48);
            string correction = P + "after.corrected_ending" + (remote ? "_remote" : "");
            var corrected = Play(correction, correctionWorld, "terms", 3);
            check(corrected.Has(P + "judgment_answered") && corrected.Has("devarra.committed"),
                "Corrected ending lost renewed acceptance.");
            var finalNo = Play(correction, correctionWorld, "terms", 1);
            check(finalNo.Has("devarra.closed") && !finalNo.Has("devarra.harem.eligible"),
                "Final refusal reopened a partner.");
            var delayed = Play(correction, correctionWorld, "terms", 2);
            check(delayed.Has(P + "left_hungry") && !delayed.Has("devarra.committed"),
                "Corrected ending's postponement became acceptance.");
        }

        var withheld = Play(P + "flight.eggs", Wait(Observe(deactivated, "eggs.project"), 48), "clutch", 4);
        var testedVault = Play(P + "after.tithe", Wait(withheld, 48), "ending_free", 0);
        var climbedVault = Play(T + "first_climb", Wait(testedVault, 24), "leave", 1);
        var vault = Play(T + "the_clutch", Wait(climbedVault, 100), "withheld_vault", 0);
        check(vault.Has(T + "vault_opened"), "Vault witness did not execute the visit.");
        var acceptedVault = Play(P + "after.lair", Wait(vault, 48), "terms", 3);
        var vaultBook = Play(T + "the_garrison_book", Wait(acceptedVault, 100), "start", 2);
        Play(T + "on_the_roof", Wait(vaultBook, 120), "start", 0);
        var cooked = Play(P + "flight.eggs", Wait(Observe(deactivated, "eggs.omelet"), 48), "clutch", 0);
        var testedCook = Play(P + "after.tithe", Wait(cooked, 48), "ending_free", 0);
        var climbedCook = Play(T + "first_climb", Wait(testedCook, 24), "leave", 1);
        check(climbedCook.Has(P + "cook_given"), "Cook witness did not execute collection.");
        var acceptedCook = Play(P + "after.lair", Wait(climbedCook, 48), "terms", 3);
        var cookBook = Play(T + "the_garrison_book", Wait(acceptedCook, 100), "start", 3);
        Play(T + "on_the_roof", Wait(cookBook, 120), "start", 0);
        var acceptedEarly = Play(P + "after.lair", Wait(climbed, 48), "terms", 3);
        var offer = Play(T + "the_generals", Wait(acceptedEarly, 100), "climb", 1);
        var bargain = Play(T + "the_generals", Wait(acceptedEarly, 100), "climb", 2);
        check(!Render(P + "epilogue.woken", offer).Contains("every death in it")
            && Render(P + "epilogue.woken", bargain).Contains("every death in it"),
            "Voluntary battle and purchased battle share an unaccepted price.");

        foreach (string death in new[] { "devarra.dead_lair", "devarra.dead_sanctum" })
        foreach (string eggs in new[] { "eggs.omelet", "eggs.druids", "eggs.destroyed", "eggs.project" })
        {
            var dead = Wait(Observe(start, death, eggs), 200, 6);
            check(Rules.Available(story, S(P + "epilogue.canon_fate"), dead), "Native closure lacks a canon-fate page.");
            check(!Rules.Available(story, S(P + "epilogue.canon_fate"), lateYes), "Returned Devarra received a native death page.");
        }
        Console.WriteLine("PASS: Devarra round 3 continuous campaign witnesses and negative forks");
    }
}
