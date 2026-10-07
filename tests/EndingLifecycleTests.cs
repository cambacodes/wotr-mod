using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// endings job 2: final consumer gates over production loss/return histories.
internal static class EndingLifecycleTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var report = check;
        var failures = new List<string>();
        check = (condition, message) => { if (condition) report(true, message); else failures.Add(message); };
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Snapshot World(params string[] flags)
        {
            var state = new Snapshot { Chapter = 6, Hour = 10000 };
            state.Flags.UnionWith(new[] { "trickster", "chapter_later" }.Concat(flags));
            ImplicitParticipantInventoryTests.Observe(story, state);
            return state;
        }
        void Observe(Snapshot state) => ImplicitParticipantInventoryTests.Observe(story, state);
        string Render(Scene scene, Snapshot state) => string.Join("\n", scene.Nodes.Select(n =>
            n.Text + "\n" + string.Join("\n", Rules.VisibleParagraphs(n, state).Select(p => p.Text))));
        bool Selected(string cue, Snapshot state, string replacement)
        {
            var variants = Rules.EditVariants(story.NativeEpilogueEdits[cue]);
            int selected = Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), state);
            return selected >= 0 && variants[selected].Replacement == replacement;
        }

        foreach (var pair in new[] {
            ("62f20840e6aa33844b641c5c8e10f814", "horzalah.native.eng7_f6c.guild"),
            ("8ae3220fd0a645809f59f54f8d89985f", "horzalah.native.eng7_f6c.trio") })
        {
            var state = World("horzalah.trickster.primed", "horzalah.trickster.returned");
            check(Selected(pair.Item1, state, pair.Item2), "job2: paid Guild ownership not selected");
            state.Flags.Add("horzalah.trickster.left_free"); Observe(state);
            check(!state.Has("horzalah.present_now") && Selected(pair.Item1, state, pair.Item2),
                "job2: free departure loses Guild ownership");
            foreach (string loss in new[] { "horzalah.killed", "horzalah.returned_actor_lost", "legend" })
            {
                var lost = Program.Copy(state); lost.Flags.Add(loss); Observe(lost);
                check(!Selected(pair.Item1, lost, pair.Item2), "job2: native Guild variant survives " + loss);
            }
            var unpaid = World("horzalah.trickster.primed", "horzalah.trickster.left_free");
            check(!Selected(pair.Item1, unpaid, pair.Item2), "job2: unfinished bargain keeps Guild");
            state.Flags.Add("sacrifice"); Observe(state);
            check(Selected(pair.Item1, state, pair.Item2), "job2: Commander death changes distant Guild ownership");
        }

        var refusal = S("camellia.trickster.epilogue.refused");
        var living = World("camellia.closed");
        check(Rules.Available(story, refusal, living) && Render(refusal, living).Contains("answered the Commander"),
            "job2: living Camellia refusal lost service history");
        foreach (string loss in new[] { "camellia.dead", "camellia.killed", "camellia.kicked_out" })
        {
            var gone = Program.Copy(living); gone.Flags.Add(loss); Observe(gone);
            check(Rules.Available(story, refusal, gone), "job2: closure account unavailable after " + loss);
            string text = Render(refusal, gone);
            check(!text.Contains("answered the Commander") && !text.Contains("After the war she went her own way"),
                "job2: absent Camellia performs living refusal after " + loss);
            check(text.Contains(loss == "camellia.kicked_out" ? "dismissed" : "Her death stood"),
                "job2: wrong Camellia closure disposition " + loss);
        }
        var returned = World("camellia.closed", "camellia.killed", "camellia.trickster.cost.knows_you_tried",
            "camellia.trickster.native_death_observed", "camellia.trickster.returned");
        check(Render(refusal, returned).Contains("After the war she went her own way"), "job2: earned Camellia return lost");
        returned.Flags.Add("camellia.returned_actor_lost"); Observe(returned);
        check(!Render(refusal, returned).Contains("After the war she went her own way"), "job2: past return answers later death");

        var stone = S("arsinoe.trickster.epilogue.pot_returned");
        var estate = World("arsinoe.trickster.cost.lien", "arsinoe.trickster.cost.collateral_word", "sacrifice");
        check(Rules.Available(story, stone, estate), "job2: returned property accounting gated by patron's life");
        check(Render(stone, estate).Contains("estate") && !Render(stone, estate).Contains("Only supper"),
            "job2: estate account manufactures personal invitation");
        estate.Flags.Add("arsinoe.trickster.cost.rent_grace"); Observe(estate);
        check(Render(stone, estate).Contains("three waived renewals"), "job2: sacrifice erases earned rent grace");

        foreach (var pair in new[] { ("unvisited", ""), ("refusal", "gesmerha.trickster.declined"), ("finished", "gesmerha.closed") })
        {
            var state = World("gesmerha.trickster.returned", "sacrifice");
            if (pair.Item2 != "") state.Flags.Add(pair.Item2);
            Observe(state);
            var mourned = S("gesmerha.trickster.epilogue." + pair.Item1 + "_mourned");
            check(Rules.Available(story, mourned, state), "job2: missing commission death disposition " + pair.Item1);
            check(!Rules.Available(story, S("gesmerha.trickster.epilogue." + pair.Item1), state),
                "job2: living commission also fires after sacrifice " + pair.Item1);
            state.Flags.Add("ending.trickster"); Observe(state);
            check(!Rules.Available(story, mourned, state), "job2: returned Commander gets mourning " + pair.Item1);
        }
        var departed = World("elyanka.trickster.left_free", "elyanka.trickster.owned", "elyanka.closed", "sacrifice");
        var deathNews = S("elyanka.trickster.epilogue.left_free_mourned");
        check(Rules.Available(story, deathNews, departed) && Render(deathNews, departed).Contains("Ustalav"),
            "job2: departed Elyanka cannot receive sacrifice news");
        check(!Rules.Available(story, S("elyanka.trickster.epilogue.eaten"), departed),
            "job2: departed Elyanka staged in Drezen");

        var unclaimed = S("wenduag.trickster.epilogue.unclaimed");
        var native = World("wenduag.started", "wenduag.romance_finished");
        check(native.Has("wenduag.trickster.native") && !Rules.Available(story, unclaimed, native),
            "job2: early RRT start overwrites finished native Wenduag romance");

        foreach (string suffix in new[] { "article", "commit", "native_article", "native_commit" })
        {
            var page = S("nenio.trickster.epilogue." + suffix);
            foreach (var paragraph in page.Nodes.SelectMany(n => n.Paragraphs).Where(p => p.Text.Contains("Areelu")))
                check(!paragraph.Requires.Any(k => k.StartsWith("crossroute.areelu")),
                    "job2: completed encyclopedia requires a currently available Areelu on " + suffix);
        }
        check(!S("herrax.lastcall.page").Forbids.Contains("crossroute.chivarro.unavailable"),
            "job2: historical dais loses Herrax's coda when Chivarro leaves");
        var herrax = S("herrax.lastcall.page");
        var house = ImplicitParticipantInventoryTests.World(story, herrax);
        house.Flags.Add("chivarro.dead"); Observe(house);
        check(Rules.Available(story, herrax, house), "job2: Chivarro death erases Herrax's earned Last Call");
        var queenPage = S("galfrey.lastcall.page");
        var queen = World("trickster.lastcall.taken", "ending.trickster", "sacrifice", "galfrey.final");
        string queenText = Render(queenPage, queen);
        check(queenText.Contains("Queen Galfrey waited at Threshold") && !queenText.Contains("She had been buried once"),
            "job2: living Queen moved to Drezen or given Kitrane burial");
        queen.Flags.Add("galfrey.trickster.returned"); Observe(queen);
        check(Render(queenPage, queen).Contains("Kitrane stood on Drezen") && Render(queenPage, queen).Contains("She had been buried once"),
            "job2: returned Kitrane lost Drezen watch or earned burial history");
        var eliandra = S("eliandra.lastcall.page");
        var fords = World();
        check(Render(eliandra, fords).Contains("At the fords") && !Render(eliandra, fords).Contains("tended the wounded in Drezen"),
            "job2: unreturned Eliandra relocated by Last Call");
        fords.Flags.Add("eliandra.lastcall.called"); Observe(fords);
        check(Render(eliandra, fords).Contains("At the fords"), "job2: spoken call relocates Eliandra");
        fords.Flags.Add("eliandra.trickster.returned_from_fords"); Observe(fords);
        check(Render(eliandra, fords).Contains("tended the wounded in Drezen") && !Render(eliandra, fords).Contains("At the fords"),
            "job2: actual Eliandra return not carried");
        var salt = S("nidalynn.trickster.epilogue.salt");
        var eggDebt = World("nidalynn.committed", "devarra.trickster.cost.egg_withheld");
        HouseholdTests.Earn(story, eggDebt, "nidalynn.payoff.ordinary"); Observe(eggDebt);
        check(Render(salt, eggDebt).Contains("windowsill"), "job2: local Devarra account lost");
        eggDebt.Flags.UnionWith(new[] { "devarra.closed", "devarra.trickster.refused" }); Observe(eggDebt);
        check(!Render(salt, eggDebt).Contains("windowsill") && Render(salt, eggDebt).Contains("No scales arrived"),
            "job2: historical egg bill summons departed Devarra");
        check(S("vellexia.lastcall.page").Forbids.Contains("vellexia.trickster.kept_as_mirror"),
            "job2: mirror creditor becomes romantic partner");
        var mirrorCall = S("vellexia.lastcall.call");
        var mirror = ImplicitParticipantInventoryTests.World(story, mirrorCall);
        mirror.Flags.Add("vellexia.trickster.kept_as_mirror"); Observe(mirror);
        check(Rules.Available(story, mirrorCall, mirror) && Render(mirrorCall, mirror).Contains("voice answers"),
            "job2: mirror cannot answer her debt call");
        report(failures.Count == 0, string.Join("\n", failures));
        Console.WriteLine("Job 2: life, departure, earned return, sacrifice and native ownership counterexamples passed.");
    }
}
