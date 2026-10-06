using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Minagho and Chivarro, Trickster (Writer/handoffs/trickster/minagho.md, chivarro.md): the brand re-addressed (F17), through
// the wrong wardrobe (F01) and the house always collects (F24). One block per spec rules test (Trk_Minagho_*, Trk_Chivarro_*),
// plus the pair chain, the alone commits, the epilogue pages, the reactions and the registered-route edits (G6).
internal static class MinaghoChivarroTricksterTests
{
    private const string P = "minagho_chivarro.trickster.";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string ChivUnit = "b7e819e2a9bb0804abcbffe8e7d91ba6";
    private const string MinUnit = "565ccab37e2475742b043ec912a750fa";
    private const string Complete = "minachiv.complete";
    private const string Closed = "minachiv.closed";
    private const string Primed = P + "primed", Debt = P + "cost.baphomet_debtor", Terms = P + "cost.baphomet_terms";
    private const string Knelt = P + "cost.baphomet_knelt", LateClaim = P + "cost.late_claim", Delivered = P + "collateral_delivered";
    private const string RetM = P + "returned_minagho", RetC = P + "returned_chivarro", MinIn = P + "minagho_in", ChIn = P + "chivarro_in";
    private const string Reunited = P + "reunited", Waiting = P + "chivarro_waiting", SentBack = P + "chivarro_sent_back";
    private const string DeclM = P + "declined_minagho", DeclC = P + "chivarro_declined", Declined = P + "declined";
    private const string Deposit = P + "chivarro_deposit", Favor = P + "cost.herrax_favor", Late = P + "cost.late";
    private const string Owned = P + "chivarro_owned", Kept = P + "kept_in_service", Chain = P + "committed";
    private const string Met = P + "pursuers_met", Refused = P + "baphomet_refused";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000,
            // eng-final / E-Q8-10: fund these positive histories; the walker enforces every debit.
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        if (chapter > 1) state.Flags.Add("chapter_later");
        state.AvailableContacts.UnionWith(new[] { ChivUnit, MinUnit });
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 1000;
        return state;
    }

    // Later: the next rest, far enough on for any delay in this route (<= 120 h).
    private static Snapshot Later(Story story, Snapshot state, params string[] flags)
    {
        var next = Program.Copy(state);
        foreach (var flag in flags) if (next.Flags.Add(flag)) next.Times[flag] = next.Hour;
        next.Hour += 200;
        Rules.Complete(story, next);
        return next;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        bool Av(Scene s, Snapshot w) => Rules.Available(story, s, w);
        List<Snapshot> Done(Scene s, Snapshot w) => Program.Walk(s, w).Where(r => r.Has(s.Id)).ToList();
        HashSet<string> Pages(Scene s, Snapshot w) { var seen = new HashSet<string>(); Program.Walk(s, w, (page, _) => seen.Add(page)); return seen; }

        var setupC4 = S(P + "minagho_dead.setup_c4");
        var setupC3 = S(P + "minagho_dead.setup_c3");
        var parley = S(P + "react.baphomet");
        var brand = S(P + "minagho_dead.brand");
        var brandLetter = S(P + "minagho_dead.brand_letter");
        var collateral = S(P + "minagho_dead.collateral");
        var spared = S(P + "spared.brand");
        var sparedLetter = S(P + "spared.brand_letter");
        var collectors = S(P + "debt.collectors");
        var collectorsSpared = S(P + "debt.collectors_spared");
        var wardrobe = S(P + "reunion.wardrobe");
        var deposit = S(P + "chivarro_dead.deposit");
        var bought = S(P + "chivarro_dead.bought");
        var offer = S(P + "after.what_the_offer_bought");
        var price = S(P + "after.the_price_of_her_name");
        var priceLetter = S(P + "after.the_price_of_her_name_letter");
        var wonBack = S(P + "after.won_back");
        var house = S(P + "after.who_keeps_the_house");

        // Sol CAN (2026-09-30): the native fight kills a real unit (ChivarroKilled on the death trigger), so the return is prepared
        // before it: the deposit sends Herrax's double (Sael) down in her rings, and only a deposit returns her. No raise, no
        // survival invented after the fact; the double's death is a Ledger secret.
        var boughtText = string.Join(" ", bought.Nodes.Select(n => SurfaceIds.Of(story, n)));
        check(SurfaceIds.Has(boughtText, "[minagho_chivarro.trickster.chivarro_dead.bought/start]") && SurfaceIds.Has(boughtText, "[minagho_chivarro.trickster.chivarro_dead.bought/start]") && bought.Requires.Contains(Deposit),
            "Chivarro's return is not the prepared double, or a raise came back (memory rrt-unique-devices).");
        check(deposit.Nodes.Any(n => n.Text.Contains("the rings, and whatever they are on", StringComparison.Ordinal) && n.Text.Contains("Sael", StringComparison.Ordinal))
              && deposit.Nodes.Single(n => n.Id == "menu").Text.Contains("Sael", StringComparison.Ordinal)
              && deposit.Nodes.Single(n => n.Id == "start").Choices[0].Next == "menu"
              && !deposit.Nodes.Single(n => n.Id == "start").Choices[0].Text.Contains("Sael", StringComparison.Ordinal)
              && !deposit.Nodes.Single(n => n.Id == "ink").Choices[0].Set.Contains("trickster.secret.chivarro_double")
              && bought.Requires.Contains("chivarro.dead_confirmed")
              && bought.Nodes.Single(n => n.Id == "paid").Choices[0].Set.Contains("trickster.secret.chivarro_double"),
            "Herrax must disclose the double before the order, and record its killing only at confirmed settlement.");
        var road = S(P + "after.before_the_last_road");
        var roadLetter = S(P + "after.before_the_last_road_letter");
        var aloneChiv = S(P + "alone.chivarro");
        var aloneMin = S(P + "alone.minagho");
        var aloneMinSpared = S(P + "alone.minagho_spared");
        var epPair = S(P + "epilogue.pair");
        var epChiv = S(P + "epilogue.chivarro");
        var epMin = S(P + "epilogue.minagho");
        var epOwned = S(P + "epilogue.owned");
        var epCommit = S(P + "epilogue.commit");
        var epDeclined = S(P + "epilogue.declined");

        // Hooks and shape.
        check(setupC4.AnswerLists.SequenceEqual(new[] { "82a0c2ad3e6dc41469ec66a7affdc486" }) && setupC4.NativeReturnCue == "0aa00bcf3121a694dbf306bea0f62153"
              && setupC4.Nodes.Single().Choices.Single().NativeNext == "99d65001b1b0cfe45b2f47ad7d7dac7c"
              && setupC3.AnswerLists.SequenceEqual(new[] { "b00190e0e55fd9944b7fc8de5c83cbc0" }) && setupC3.NativeReturnCue == "3c6de45d40c17fa40806e4d931eaf7b5"
              && setupC3.Nodes.Single().Choices.Single().NativeNext == "093724348a359594ebe7f7193e7b86dc"
              && new[] { setupC4, setupC3 }.All(s => s.EntryMythic == "PlayerIsTrickster" && s.Entry.Contains("until I spilled the blood of the one who caused me to fail in Kenabres.") && !s.Entry.Contains("failed him", StringComparison.Ordinal)),
            "The brand primers left Minagho's recital of her terms.");
        check(parley.AnswerLists.SequenceEqual(new[] { "cbd2f289d8173fb41a231772290440ba" }) && parley.NativeReturnCue == "2d1a338243b8ddb429bbad5db08ed7de"
              && deposit.AnswerLists.SequenceEqual(new[] { "43f93812d6216c94db356622859397f1" }) && deposit.NativeReturnCue == "1af69c65d15cc8949a4fe47a45c4f85d",
            "The parley or the deposit left its native hub.");
        var hubs = new Dictionary<Scene, string>
        {
            [brand] = "minagho_chivarro.presence.minagho", [collectors] = "minagho_chivarro.presence.minagho", [aloneMin] = "minagho_chivarro.presence.minagho",
            [spared] = "minagho_chivarro.presence.minagho_spared", [collectorsSpared] = "minagho_chivarro.presence.minagho_spared",
            [aloneMinSpared] = "minagho_chivarro.presence.minagho_spared", [price] = "minagho_chivarro.presence.chivarro",
            [road] = "minagho_chivarro.presence.chivarro", [aloneChiv] = "minagho_chivarro.presence.chivarro",
        };
        foreach (var hub in hubs)
            check(hub.Key.InteractionHub == hub.Value && story.Presences[hub.Value].Dialog == "hub" && hub.Key.Areas.SequenceEqual(new[] { Drezen })
                  && hub.Key.ContactUnit == story.Presences[hub.Value].Unit && hub.Key.Chapters.SequenceEqual(new[] { 5 }),
                "Physical beat is not on its presence hub: " + hub.Key.Id);
        check(Rules.PresencesExclusive(story.Presences["minagho_chivarro.presence.minagho"], story.Presences["minagho_chivarro.presence.minagho_spared"]),
            "Two Minagho copies can stand at once.");
        var rel = story.Relationships["minagho_chivarro"];
        check(rel.UnavailableOverrides["minagho.dead"] == RetM && rel.UnavailableOverrides["chivarro.dead"] == RetC && rel.TricksterAccess.Count == 4
              && rel.TricksterAccess.Values.All(a => a.Detect.Contains("minagho.dead") || a.Detect.Contains("!minagho.dead"))
              && rel.TricksterAccess.Values.All(a => a.Detect.Contains("chivarro.dead") || a.Detect.Contains("!chivarro.dead")),
            "The pair's relationship patch does not detect both deaths.");
        var shove = wardrobe.Nodes.SelectMany(n => n.Choices).Where(c => SurfaceIds.Has(SurfaceIds.Of(story, c), "[minagho_chivarro.trickster.reunion.wardrobe/silk/choice/2][minagho_chivarro.trickster.reunion.wardrobe/silk/choice/3][minagho_chivarro.trickster.reunion.wardrobe/cellar/choice/1][minagho_chivarro.trickster.reunion.wardrobe/cellar/choice/2][minagho_chivarro.trickster.reunion.wardrobe/fought/choice/0][minagho_chivarro.trickster.reunion.wardrobe/fought/choice/1]")).ToList();
        check(shove.Count > 0 && shove.All(c => c.Mythic == "PlayerIsTrickster" && c.Alignment?.Direction == "Chaotic"), "The shove lost its [Trickster] answer or its price.");
        foreach (var commit in new[] { road, aloneChiv, aloneMin, aloneMinSpared })
            check(commit.Nodes.Any(n => n.Id == "threshold") && commit.Nodes.SelectMany(n => n.Choices).Where(c => c.Set.Contains(Complete)).All(c => (c.Next == "threshold" || c.Next == "threshold_clean") && c.Set.Contains(Chain)),
                "A physical commit skips the threshold or the chain marker: " + commit.Id);
        check(story.Scenes.Where(s => s.Relationship == "minagho_chivarro").SelectMany(s => s.Nodes).SelectMany(n => n.Choices)
                  .Where(c => c.Set.Contains(Complete)).All(c => c.Set.Contains(Chain) || !c.Set.Any(f => f.StartsWith(P, StringComparison.Ordinal))),
            "A Trickster commit is missing the chain marker.");

        // Trk_Minagho_SetupC4 (and the C3 twin).
        var c4 = World(story, 4, "trickster", "trickster.ever", "minagho.brand_told_c4");
        check(Av(setupC4, c4) && !Av(setupC3, c4), "Trk_Minagho_SetupC4: availability.");
        var primedC4 = Done(setupC4, c4).Single();
        check(primedC4.Has(Primed) && primedC4.Has(Debt) && !Av(setupC4, primedC4), "Trk_Minagho_SetupC4: flags.");
        check(Av(setupC3, World(story, 3, "trickster", "trickster.ever", "minagho.brand_told_c3")), "The Chapter 3 primer is unavailable.");
        check(!Av(setupC4, World(story, 4, "trickster", "trickster.ever", "minagho.brand_told_c4", "minagho.dead")), "A primer plays after her death.");

        // Trk_Minagho_DeadParleyKneel.
        var cell = World(story, 5, "trickster", "trickster.ever", "minagho.dead", Primed, Debt, "baphomet.parley");
        check(Av(parley, cell) && !Av(brand, cell) && !Av(spared, cell), "Trk_Minagho_DeadParleyKneel: availability.");
        var parleyOut = Done(parley, cell);
        var knelt = parleyOut.Single(r => r.Has(Knelt));
        check(knelt.Has(Terms) && knelt.Has(Delivered), "Trk_Minagho_DeadParleyKneel: flags.");
        var tookWord = parleyOut.Single(r => r.Has(Terms) && !r.Has(Knelt));
        check(tookWord.Has(Delivered) && parleyOut.Any(r => r.Has(Refused)), "The parley lost [Take him at his word] or 'Keep her.'.");
        check(Av(brand, Later(story, knelt)) && !Av(collateral, Later(story, knelt)), "Trk_Minagho_DeadParleyKneel: the return does not follow.");
        check(Pages(parley, World(story, 5, "trickster", "trickster.ever", "minagho.dead", Primed, Debt, "baphomet.parley", "kyado.initiated")).Contains("knelt_initiate"),
            "Kyado's temple is not remembered at the kneeling.");

        // Trk_Minagho_DeadParleyLateSign: the late signer must kneel.
        var unprimedCell = World(story, 5, "trickster", "trickster.ever", "minagho.dead", "baphomet.parley");
        check(Av(parley, unprimedCell), "Trk_Minagho_DeadParleyLateSign: availability.");
        var lateOut = Done(parley, unprimedCell);
        check(lateOut.Where(r => r.Has(Terms)).All(r => r.Has(LateClaim) && r.Has(Knelt) && r.Has(Primed) && r.Has(Debt)) && lateOut.Any(r => r.Has(Terms)),
            "Trk_Minagho_DeadParleyLateSign: a late signer escapes the kneeling.");
        check(Pages(parley, unprimedCell).Contains("terms_late"), "The late terms are not spoken.");

        // Trk_Minagho_DeadReturn.
        var delivered = World(story, 5, "trickster", "trickster.ever", "minagho.dead", Primed, Debt, Terms, Delivered);
        check(Av(brand, delivered) && !Av(collateral, delivered) && !Av(brandLetter, delivered), "Trk_Minagho_DeadReturn: availability.");
        var woken = Done(brand, delivered);
        check(woken.Count == 2 && woken.All(r => r.Has(RetM) && r.Has(P + "cost.palm_scar") && r.Has(MinIn) && r.Has("minachiv.started")),
            "Trk_Minagho_DeadReturn: flags.");
        check(woken.Count(r => r.Has(P + "claimed_debt")) == 1, "The pivotal evil answer is missing.");
        check(Done(brand, World(story, 5, "trickster", "trickster.ever", "minagho.dead", Primed, Debt, Terms, Delivered, ChIn)).Any(r => r.Has(Reunited)),
            "A waiting Chivarro is not reunited at the wake.");
        var wakePages = Pages(brand, World(story, 5, "trickster", "trickster.ever", "minagho.dead", Primed, Debt, Terms, Delivered, Knelt, "minagho.killed_by_staunton"));
        check(wakePages.Contains("wake_knelt") && wakePages.Contains("wake_staunton") && !wakePages.Contains("wake_late"), "The wake variants misfire.");
        check(Av(brandLetter, World(story, 5, "trickster", "trickster.ever", "minagho.dead", Primed, Debt, Terms, Delivered, "minagho_chivarro.presence.minagho.failed")),
            "The brand's letter twin does not open when her presence fails.");

        // Trk_Minagho_DeadNoBargain: collectors bring the corpse; the Goat's own iron.
        var refusedWorld = World(story, 5, "trickster", "trickster.ever", "minagho.dead", Primed, Debt, "baphomet.parley", Refused);
        check(Av(collateral, refusedWorld) && !Av(brand, refusedWorld) && !Av(parley, refusedWorld), "Trk_Minagho_DeadNoBargain: availability.");
        var ironed = Done(collateral, refusedWorld).Where(r => r.Has(RetM)).ToList();
        check(ironed.Count >= 2 && ironed.All(r => r.Has(P + "cost.palm_scar") && r.Has(Met) && r.Has(P + "cost.baphomet_branded")),
            "Trk_Minagho_DeadNoBargain: flags.");
        check(!Av(collectors, Later(story, ironed[0])), "Trk_Minagho_DeadNoBargain: the collectors come twice.");
        check(Pages(collateral, refusedWorld).Contains("gate_refused"), "The refused gift is not delivered anyway.");

        // Trk_Minagho_DeadHanged.
        var passed = World(story, 5, "trickster", "trickster.ever", "minagho.dead", Primed, Debt, "baphomet.parley");
        var hanged = Done(collateral, passed).Single(r => r.Has(DeclM));
        check(!hanged.Has(RetM) && !Av(collateral, Later(story, hanged)) && !Av(brand, Later(story, hanged)), "Trk_Minagho_DeadHanged failed.");

        // Trk_Minagho_PathFailedUnprimed.
        var failed = World(story, 5, "trickster.ever", "trickster.failed", "minagho.dead", "baphomet.parley");
        check(!Av(parley, failed) && !Av(collateral, failed) && !Av(brand, failed) && !Av(spared, failed), "Trk_Minagho_PathFailedUnprimed failed.");
        check(!Av(parley, World(story, 5, "trickster.ever", "trickster.failed", "minagho.dead", "baphomet.parley", Primed, Debt)),
            "A primed return completes after the path failed.");

        // Trk_Minagho_BothDead: the shared-flag blocker is gone.
        var bothDead = World(story, 5, "trickster", "trickster.ever", "minagho.dead", "chivarro.dead", "chivarro.exile_objective_done", Primed, Debt, Terms, Delivered, Deposit, Favor);
        check(Av(brand, bothDead) && Av(bought, bothDead) && !Av(wardrobe, With(bothDead, "closets.known")), "Trk_Minagho_BothDead failed.");

        // Trk_Minagho_SparedPrimed / _FledUnprimed.
        var sparedWorld = World(story, 5, "trickster", "trickster.ever", "minagho.spared_c4", Primed, Debt);
        check(Av(spared, sparedWorld) && !Av(brand, sparedWorld), "Trk_Minagho_SparedPrimed: availability.");
        var sparedOut = Done(spared, sparedWorld);
        check(sparedOut.Count(r => r.Has(MinIn)) == 2 && sparedOut.Count(r => r.Has(DeclM)) == 1, "Trk_Minagho_SparedPrimed: flags.");
        var fled = World(story, 5, "trickster", "trickster.ever", "minagho.fled_fane");
        check(Av(spared, fled), "Trk_Minagho_FledUnprimed: availability.");
        check(Done(spared, fled).Where(r => r.Has(MinIn)).All(r => r.Has(Primed) && r.Has(Debt) && r.Has(LateClaim)), "Trk_Minagho_FledUnprimed: flags.");
        check(!Av(spared, World(story, 5, "trickster.ever", "trickster.failed", "minagho.fled_fane")), "An unprimed spared return is offered after the path ended.");
        check(Pages(spared, With(sparedWorld, "minagho.terrified")).Contains("terrified"), "The terrified variant is missing.");
        check(Av(sparedLetter, With(sparedWorld, "minagho_chivarro.presence.minagho_spared.failed")) && !Av(sparedLetter, sparedWorld),
            "The spared letter twin misfires.");
        // Sol INT/HOW (r1): an unprimed spared Minagho whose presence failed is reached in person from her note, and the transfer is
        // made on the page (no opening claims a dry brand before it).
        var unprimedFailed = World(story, 5, "trickster", "trickster.ever", "minagho.fled_fane", "minagho_chivarro.presence.minagho_spared.failed");
        unprimedFailed.AvailableContacts.Remove(MinUnit);
        check(!Av(spared, unprimedFailed) && Av(sparedLetter, unprimedFailed)
              && Done(sparedLetter, unprimedFailed).Any(r => r.Has(MinIn) && r.Has(Primed) && r.Has(Debt) && r.Has(LateClaim))
              && Pages(sparedLetter, unprimedFailed).Contains("late"),
            "An unprimed spared Minagho has no reachable transfer when her presence fails, or an opening precedes its act.");

        // Sol r2 INT: Baphomet's one parley notices Horzalah's escape as it notices Hepzamirah's (a node variant, no debt).
        check(Pages(parley, With(aliveCell0(), "horzalah.trickster.returned")).Contains("weaker")
              && !Pages(parley, aliveCell0()).Contains("weaker"), "The parley ignores Horzalah's escape.");
        // Sol r2 INT: a soft no keeps its priced second ask, for the pair and for each woman alone.
        var pairNo = World(story, 5, "trickster", "trickster.ever", Reunited, ChIn, MinIn, "minagho.spared_c4", P + "tprev.house", Declined);
        var scars = S(P + "after.when_it_scars");
        var scarOut = Done(scars, pairNo);
        check(Av(scars, pairNo) && scarOut.Any(r => r.Has(Complete) && r.Has("minachiv.future_two") && r.Has(P + "night.pair") && r.Has(P + "cost.morning_after"))
              && scarOut.Any(r => r.Has(Closed)) && !Av(scars, With(pairNo, Complete)), "The pair's soft no has no second ask.");
        var minNo = World(story, 5, "trickster", "trickster.ever", "chivarro.dead", "chivarro.exile_objective_done", MinIn, "minagho.spared_c4", DeclC, Declined);
        check(Done(S(P + "alone.minagho_when_it_scars"), minNo).Any(r => r.Has(Complete) && r.Has("minachiv.future_minagho")),
            "Minagho's soft no has no second ask.");
        var chivNo = World(story, 5, "trickster", "trickster.ever", "minagho.dead", ChIn, Waiting, Declined);
        check(Done(S(P + "alone.chivarro_when_it_scars"), chivNo).Any(r => r.Has(Complete) && r.Has("minachiv.future_chivarro")),
            "Chivarro's soft no has no second ask.");
        // Sol r2 BEL: the red silk earns a meeting; the name is priced at it, with the hand on her table.
        var wonBackOut = Done(wonBack, World(story, 5, "trickster", "trickster.ever", P + "chivarro_walked", ChIn));
        check(Pages(wonBack, World(story, 5, "trickster", "trickster.ever", P + "chivarro_walked", ChIn)).Contains("hand")
              && wonBackOut.Where(r => r.Has(P + "tprev.name")).All(r => r.Has(P + "cost.palm_on_table")), "The red silk buys the name without the hand.");

        // Trk_Minagho_SparedParleyAlive.
        var aliveCell = World(story, 5, "trickster", "trickster.ever", "minagho.spared_c4", Primed);
        check(Av(parley, aliveCell) && Done(parley, aliveCell).Any(r => r.Has(P + "baphomet_heard")), "Trk_Minagho_SparedParleyAlive failed.");

        // Trk_Minagho_Collectors (the spared presence's copy of the beat).
        var inDrezen = World(story, 5, "trickster", "trickster.ever", "minagho.spared_c4", Primed, Debt, MinIn);
        check(Av(collectorsSpared, inDrezen) && !Av(collectors, inDrezen), "Trk_Minagho_Collectors: availability.");
        var stamped = Done(collectorsSpared, inDrezen);
        check(stamped.Any(r => r.Has(Met) && r.Has(P + "cost.receipt_sent")) && stamped.All(r => r.Has(Met)), "Trk_Minagho_Collectors: flags.");
        check(!Av(collectors, Later(story, stamped[0])) && !Av(collectorsSpared, Later(story, stamped[0])), "The collectors come twice.");

        // Trk_Chivarro_ReunionMinaghoSpared.
        var reunion = World(story, 5, "trickster", "trickster.ever", "closets.known", "minagho.spared_c4", MinIn);
        check(Av(wardrobe, reunion) && !Av(bought, reunion), "Trk_Chivarro_ReunionMinaghoSpared: availability.");
        var reunited = Done(wardrobe, reunion).Where(r => r.Has(Reunited)).ToList();
        check(reunited.Count == 1 && reunited[0].Has(ChIn) && reunited[0].Has(P + "cost.socoth_owed"), "Trk_Chivarro_ReunionMinaghoSpared: flags.");
        check(Av(offer, Later(story, reunited[0])), "Trk_Chivarro_ReunionMinaghoSpared: the chain does not open.");

        // Trk_Chivarro_DoorKept / _PathFailed / cellar variant.
        var door = World(story, 5, "trickster", "trickster.ever", "closets.known", "socot.gone");
        check(Done(wardrobe, door).All(r => !r.Has(P + "cost.socoth_owed")) && Done(wardrobe, door).All(r => r.Has(P + "cost.door_marked")),
            "Trk_Chivarro_DoorKept failed.");
        check(!Av(wardrobe, World(story, 5, "trickster.ever", "trickster.failed", "closets.known")), "Trk_Chivarro_PathFailed failed.");
        var cellarPages = Pages(wardrobe, World(story, 5, "trickster", "trickster.ever", "closets.known", "chivarro.exiled", "chivarro.fought_commander"));
        check(cellarPages.Contains("cellar") && cellarPages.Contains("fought") && !cellarPages.Contains("door"), "The wardrobe variants misfire.");

        // Trk_Chivarro_PairChain / _PriceWalked / _Commit / _CommitRefused.
        var pair = World(story, 5, "trickster", "trickster.ever", Reunited, ChIn, MinIn, "minagho.spared_c4");
        check(Av(offer, pair) && !Av(price, pair), "Trk_Chivarro_PairChain: availability.");
        var offered = Done(offer, pair);
        check(offered.Count == 2 && offered.All(r => r.Has(P + "tprev.offer")) && Av(price, Later(story, offered[0])), "Trk_Chivarro_PairChain: the price does not follow.");
        var priceOut = Done(price, Later(story, offered[0]));
        var named = priceOut.Single(r => r.Has(P + "tprev.name"));
        var walked = priceOut.Where(r => r.Has(P + "chivarro_walked")).ToList();
        check(named.Has(P + "cost.palm_on_table") && walked.Count == 2, "Her refusal gate is not on every branch of the price.");
        check(Av(wonBack, Later(story, walked[0])) && !Av(house, Later(story, walked[0])), "Trk_Chivarro_PriceWalked failed.");
        var won = Done(wonBack, Later(story, walked[0]));
        check(won.Where(r => r.Has(P + "tprev.name")).All(r => r.Has(P + "cost.won_back")) && won.Count(r => r.Has(P + "tprev.name")) == 2 && won.Any(r => r.Has(SentBack)), "The priced second ask is missing.");
        check(Av(house, Later(story, named)), "The house does not follow the price.");
        var housed = Done(house, Later(story, named));
        check(housed.Count == 2 && housed.All(r => r.Has(P + "tprev.house")), "Who keeps the house: flags.");
        var ready = Later(story, housed[0]);
        check(Av(road, ready) && !Av(roadLetter, ready) && Av(epCommit, ready), "Trk_Chivarro_Commit: availability.");
        var roadOut = Done(road, ready);
        var yes = roadOut.Where(r => r.Has(Complete)).ToList();
        check(yes.Count == 1 && yes[0].Has("minachiv.future_two") && yes[0].Has(Chain) && Pages(road, ready).Contains("threshold"), "Trk_Chivarro_Commit failed.");
        var no = roadOut.Where(r => r.Has(Declined)).ToList();
        check(no.Count == 2 && no.All(r => !r.Has(Complete)), "Trk_Chivarro_CommitRefused: her refusal is not reachable from every branch.");
        check(!Av(roadLetter, Later(story, no[0], "minagho_chivarro.presence.chivarro.failed")) && !Av(epCommit, no[0]) && Av(epDeclined, no[0]),
            "Trk_Chivarro_CommitRefused: continuations.");
        check(Av(epPair, yes[0]) && !Av(epCommit, yes[0]) && !Av(epDeclined, yes[0]), "The pair's ending page does not follow the commit.");
        check(Av(roadLetter, With(ready, "minagho_chivarro.presence.chivarro.failed")), "The commit's letter twin does not open when her presence fails.");

        // W5: play each offer through the price, house and commitment; render only its chosen payoff.
        foreach (var offerChoice in offered)
        {
            var pricedOffer = Done(price, Later(story, offerChoice)).Single(r => r.Has(P + "tprev.name"));
            var housedOffer = Done(house, Later(story, pricedOffer))[0];
            var finalOffer = Done(road, Later(story, housedOffer)).Single(r => r.Has(Complete));
            var payoffs = Rules.VisibleParagraphs(epPair.Nodes[0], finalOffer)
                .Where(p => p.Requires.Contains(P + "offer_sold_back") || p.Requires.Contains(P + "offer_burned")).ToList();
            check(payoffs.Count == 1 && payoffs[0].Requires.Contains(finalOffer.Has(P + "offer_sold_back")
                    ? P + "offer_sold_back" : P + "offer_burned"),
                "The selected offer renders an unchosen or duplicate epilogue consequence.");
        }

        // Trk_Chivarro_ReunionMinaghoDead: Chivarro first, alone; her own commit.
        var waitingWorld = World(story, 5, "trickster", "trickster.ever", "closets.known", "minagho.dead");
        check(Av(wardrobe, waitingWorld), "Trk_Chivarro_ReunionMinaghoDead: availability.");
        var waiting = Done(wardrobe, waitingWorld).Single(r => r.Has(Waiting));
        check(waiting.Has(ChIn) && Av(aloneChiv, Later(story, waiting)) && Av(epCommit, waiting), "Trk_Chivarro_ReunionMinaghoDead failed.");
        var chivYes = Done(aloneChiv, Later(story, waiting)).Where(r => r.Has(Complete)).ToList();
        check(chivYes.Count == 1 && chivYes[0].Has("minachiv.future_chivarro") && chivYes[0].Has(P + "cost.half_the_pair") && Av(epChiv, chivYes[0]),
            "Chivarro's alone commit failed.");
        // Minagho comes home later: the wake reunites them, and the alone commit closes.
        // Sol PP8 r1 (INT): every accepting arrival with Chivarro already in reunites them (no answer strands the pair).
        var bothOuts = Done(brand, World(story, 5, "trickster", "trickster.ever", "minagho.dead", Primed, Debt, Terms, Delivered, ChIn, Waiting)).Where(r => r.Has(MinIn)).ToList();
        check(bothOuts.Count >= 3 && bothOuts.All(r => r.Has(Reunited)), "Trk_Chivarro_FirstThenMinagho: an accepting wake strands the pair.");
        var bothIn = bothOuts.First();
        foreach (var (arrival, w) in new[] {
            (spared, World(story, 5, "trickster", "trickster.ever", "minagho.spared.latched", Primed, ChIn, Waiting)),
            (spared, World(story, 5, "trickster", "trickster.ever", "minagho.spared.latched", ChIn, Waiting)),
            (sparedLetter, World(story, 5, "trickster", "trickster.ever", "minagho.spared.latched", Primed, ChIn, Waiting, "minagho_chivarro.presence.minagho_spared.failed")),
            (sparedLetter, World(story, 5, "trickster", "trickster.ever", "minagho.spared.latched", ChIn, Waiting, "minagho_chivarro.presence.minagho_spared.failed")),
            (sparedLetter, World(story, 5, "trickster", "trickster.ever", "minagho.spared.latched", Primed, ChIn, Waiting, "longcon.offer_heard", "minagho_chivarro.presence.minagho_spared.failed")) })
        {
            var accepted = Program.Walk(arrival, w).Where(r => r.Has(MinIn)).ToList();
            check(accepted.Count > 0 && accepted.All(r => r.Has(Reunited)), "Trk_Chivarro_FirstThenMinagho: an accepting answer strands the pair on " + arrival.Id);
        }
        check(!Av(aloneChiv, Later(story, bothIn)) && Av(offer, Later(story, bothIn)), "A reunited pair still sees the alone commit.");

        // Trk_Chivarro_BothDead / _Killed / _Deposit / _KilledNoDepositLate / _DepositSurvivesFailure / _KilledNoDepositFailed / _KeptBill.
        var bd = World(story, 5, "trickster", "trickster.ever", "chivarro.dead", "chivarro.exile_objective_done", "minagho.dead", Deposit, Favor);
        check(Av(bought, bd) && Av(parley, With(bd, "baphomet.parley")) && !Av(wardrobe, With(bd, "closets.known")), "Trk_Chivarro_BothDead failed.");
        var killed = World(story, 5, "trickster", "trickster.ever", "chivarro.dead", "chivarro.exile_objective_done", Deposit, Favor);
        var boughtOut = Done(bought, killed);
        check(boughtOut.Any(r => r.Has(RetC) && r.Has(ChIn) && r.Has(P + "bill_burned")) && !Av(wardrobe, With(killed, "closets.known")), "Trk_Chivarro_Killed failed.");
        // Trk_Chivarro_KilledNoDeposit: nothing was prepared, the Commander killed her, and the death stands; Minagho knows.
        var killedBare = World(story, 5, "trickster", "trickster.ever", "chivarro.dead", "chivarro.exile_objective_done");
        check(!Av(bought, killedBare) && boughtOut.Where(r => r.Has(RetC)).All(r => !r.Has(Late)), "Trk_Chivarro_KilledNoDeposit failed: a witnessed death is undone.");
        var killerWorld = World(story, 5, "trickster", "trickster.ever", "chivarro.dead", "chivarro.exile_objective_done", MinIn, "minagho.spared_c4");
        check(Pages(aloneMinSpared, killerWorld).Contains("killer") && !Pages(aloneMinSpared, With(killerWorld, Deposit, DeclC)).Contains("killer"),
            "Minagho does not face the Commander who killed Chivarro.");
        // Starting the native fight alone proves no death, even with an old early DOUBLE receipt.
        var combatOnly = World(story, 5, "trickster", "trickster.ever", "chivarro.dead", Deposit, Favor, "trickster.secret.chivarro_double", MinIn, "minagho.spared_c4");
        check(!Av(bought, combatOnly) && !Av(S(P + "chivarro_dead.unbought"), combatOnly)
              && !Av(aloneMinSpared, combatOnly), "An unfinished fight is being treated as Chivarro's death.");
        var killerLetter = S(P + "alone.minagho_letter");
        var letterHistory = With(killerWorld, "minagho_chivarro.presence.minagho_spared.failed");
        check(Pages(killerLetter, letterHistory).Contains("killer_start") && Pages(killerLetter, letterHistory).Contains("killer_decline")
              && !Pages(killerLetter, With(letterHistory, Deposit)).Contains("killer_start"),
            "Confirmed unprepared killing must be acknowledged on both letter answers, without accusing prepared histories.");
        var scarHistory = With(killerWorld, Declined);
        check(Pages(S(P + "alone.minagho_when_it_scars"), scarHistory).Contains("killer_min")
              && !Pages(S(P + "alone.minagho_when_it_scars"), With(scarHistory, Deposit)).Contains("killer_min"),
            "The existing scar retry cannot skip the killing or accuse a prepared substitution.");
        var herrax = World(story, 4, "trickster", "trickster.ever", "herrax.asked_kill_chivarro");
        check(Av(deposit, herrax) && Done(deposit, herrax).Single().Has(Deposit) && Done(deposit, herrax).Single().Has(Favor), "Trk_Chivarro_Deposit failed.");
        var depositFailed = World(story, 5, "trickster.ever", "trickster.failed", "chivarro.dead", "chivarro.exile_objective_done", Deposit, Favor);
        check(!Av(bought, depositFailed), "Trk_Chivarro_Deposit: a paid deposit completes a return after the path failed.");
        check(!Av(bought, World(story, 5, "trickster.ever", "trickster.failed", "chivarro.dead", "chivarro.exile_objective_done")), "Trk_Chivarro_KilledNoDepositFailed failed.");
        // Polish W3/D1: a paid order cannot narrate Sael's death merely because the fight began.
        var fighting = World(story, 5, "trickster", "trickster.ever", "chivarro.dead", Deposit, Favor);
        check(!Av(bought, fighting), "Combat-start delivered living Chivarro before the confirmed substitution.");
        var prepared = Done(deposit, herrax).Single();
        check(!prepared.Has("trickster.secret.chivarro_double"), "Preparation claims the boy is already dead.");
        prepared.Chapter = 5;
        prepared = Later(story, prepared, "chivarro.dead");
        check(!Av(bought, prepared), "An executed deposit treats the combat-start etude as a death.");
        prepared = Later(story, prepared, "chivarro.exile_objective_done");
        check(Av(bought, prepared), "The native completed objective does not unlock the prepared delivery.");
        var deliveredDouble = Program.WalkVia(bought, prepared, "paid", 0).Where(r => r.Has(RetC)).ToList();
        check(deliveredDouble.Count > 0 && deliveredDouble.All(r => r.Has("trickster.secret.chivarro_double")),
            "Completed delivery lost its witnessed double secret.");
        check(deposit.Nodes.Single(n => n.Id == "start").Choices[0].Next == "menu"
              && deposit.Nodes.Single(n => n.Id == "menu").Choices[0].Next == "ink",
            "The Commander orders the double before learning what Herrax sells.");

        // W2: every paid transfer, including primed refusals and copied Long Con choices, keeps the wound.
        foreach (var arrival in new[] { spared, sparedLetter })
        foreach (bool primed in new[] { false, true })
        foreach (bool terrified in new[] { false, true })
        foreach (bool con in new[] { false, true })
        foreach (bool cellars in new[] { false, true })
        {
            var transfer = World(story, 5, "trickster", "trickster.ever", "minagho.spared_c4",
                "minagho_chivarro.presence.minagho_spared.failed");
            if (primed) transfer = Later(story, transfer, Primed, Debt);
            if (terrified) transfer = Later(story, transfer, "minagho.terrified");
            if (con) transfer = Later(story, transfer, "longcon.offer_heard");
            if (cellars) transfer = Later(story, transfer, "longcon.sting_exposed");
            foreach (var result in Done(arrival, transfer))
            {
                bool paid = primed || result.Has(Debt);
                check(result.Has(P + "cost.palm_scar") == paid,
                    "A paid/refused transfer misreports the palm: " + arrival.Id);
            }
        }
        foreach (var priorAnswer in new[] { DeclC, SentBack })
        {
            var unfinished = World(story, 5, "trickster", "trickster.ever", "chivarro.dead", MinIn, "minagho.spared_c4", priorAnswer);
            check(!Av(S(P + "alone.minagho_spared"), unfinished),
                "An unfinished fight plus an earlier refusal must not admit an answerless solo page.");
        }

        var ownedOut = boughtOut.Single(r => r.Has(Owned));
        check(ownedOut.Has(RetC) && !ownedOut.Has("minachiv.started") && !Av(aloneChiv, Later(story, ownedOut, "minagho.dead", DeclM)),
            "Trk_Chivarro_KeptBill failed: keeping the bill starts the relationship.");
        // The kept bill never buys a romance: nothing of the pair moves until Chivarro's bill scene, where it is burned or kept.
        var bill = S(P + "chivarro_dead.the_bill");
        var billLetter = S(P + "chivarro_dead.the_bill_letter");
        var ownedReady = World(story, 5, "trickster", "trickster.ever", Reunited, ChIn, MinIn, RetC, "chivarro.dead", "chivarro.exile_objective_done", "minagho.spared_c4", Owned, P + "tprev.house");
        check(!Av(road, ownedReady) && !Av(roadLetter, With(ownedReady, "minagho_chivarro.presence.chivarro.failed")) && !Av(epCommit, ownedReady)
              && !Av(offer, With(ownedReady)) && Av(bill, ownedReady) && !Av(billLetter, ownedReady),
            "An owned Chivarro can be courted before the bill is settled.");
        var billOut = Done(bill, ownedReady);
        var burned = billOut.Single(r => r.Has(P + "bill_burned"));
        var service = billOut.Single(r => r.Has(Kept));
        check(burned.Has("minachiv.started") && !service.Has("minachiv.started") && !Av(bill, burned) && !Av(bill, service), "The bill's outcomes.");
        check(Av(road, Later(story, burned)) && Av(epCommit, burned), "A burned bill does not reopen the courtship.");
        check(!Av(road, Later(story, service)) && !Av(epCommit, service) && !Av(epPair, service) && Av(epOwned, service),
            "The kept bill is treated as a romance.");
        check(Av(billLetter, With(ownedReady, "minagho_chivarro.presence.chivarro.failed")), "The bill's letter twin misfires.");
        // Sol r3 INT/HOW: Minagho first, then Chivarro bought, by every burn (at once, after keeping the bill, or by letter): the pair
        // is reunited and its chain opens; nothing seeds the reunion.
        var minFirst = World(story, 5, "trickster", "trickster.ever", "minagho.spared_c4", MinIn, Primed, Debt, "chivarro.dead", "chivarro.exile_objective_done", Deposit, Favor);
        var minFirstOut = Done(bought, minFirst);
        check(minFirstOut.Where(r => r.Has(P + "bill_burned")).All(r => r.Has(Reunited)) && minFirstOut.Any(r => r.Has(P + "bill_burned"))
              && Av(offer, Later(story, minFirstOut.First(r => r.Has(P + "bill_burned")))), "A Chivarro bought after Minagho is not reunited with her.");
        var keptFirst = Later(story, minFirstOut.First(r => r.Has(Owned)));
        var releasedOut = Done(bill, keptFirst);
        var releasedByLetter = Done(billLetter, With(keptFirst, "minagho_chivarro.presence.chivarro.failed"));
        check(releasedOut.Where(r => r.Has(P + "bill_burned")).All(r => r.Has(Reunited)) && releasedOut.Any(r => r.Has(P + "bill_burned"))
              && releasedByLetter.Where(r => r.Has(P + "bill_burned")).All(r => r.Has(Reunited))
              && Av(offer, Later(story, releasedOut.First(r => r.Has(P + "bill_burned")))), "Burning a kept bill strands a pair whose Minagho came first.");
        check(Pages(price, Later(story, With(burned, P + "tprev.offer"))).Contains("owned"), "The owned variant of the price is missing.");

        // Trk_Chivarro_MinaghoAlone (spared presence copy of the beat) and the dead-returned beat.
        var minAlone = World(story, 5, "trickster", "trickster.ever", "chivarro.dead", "chivarro.exile_objective_done", MinIn, "minagho.spared_c4", DeclC);
        check(Av(aloneMinSpared, minAlone) && !Av(aloneMin, minAlone), "Trk_Chivarro_MinaghoAlone: availability.");
        var minYes = Done(aloneMinSpared, minAlone).Where(r => r.Has(Complete)).ToList();
        check(minYes.Count == 1 && minYes[0].Has("minachiv.future_minagho") && Av(epMin, minYes[0]), "Trk_Chivarro_MinaghoAlone: flags.");
        var minReturnedAlone = World(story, 5, "trickster", "trickster.ever", "minagho.dead", "chivarro.dead", "chivarro.exile_objective_done", RetM, MinIn, DeclC, Primed, Debt, Terms, Delivered);
        check(Av(aloneMin, minReturnedAlone) && !Av(aloneMinSpared, minReturnedAlone), "The returned Minagho has no alone commit.");
        // Sol PP8 r2 (INT): reunion, Chivarro's walkout, "Let her stay gone": Minagho's own commit stays open, in her words.
        var walkedOut = World(story, 5, "trickster", "trickster.ever", "minagho.spared_c4", MinIn, ChIn, Reunited, SentBack);
        var walkedPages = new HashSet<string>();
        Program.Walk(aloneMinSpared, walkedOut, (page, _) => walkedPages.Add(page));
        check(Av(aloneMinSpared, walkedOut) && Done(aloneMinSpared, walkedOut).Any(r => r.Has(Complete))
              && aloneMinSpared.Nodes.Single(n => n.Id == "start").Choices.Count(c => Rules.Match(c.Requires, c.Forbids, walkedOut)) == 1,
            "Trk_Chivarro_WalkoutThenMinagho: letting Chivarro go strands Minagho's own commit.");

        // The morning after each physical commit: once, after the night, before the ending pages.
        var pairMorning = S(P + "after.the_morning_after");
        var chivMorning = S(P + "alone.chivarro_morning");
        var minMorning = S(P + "alone.minagho_morning");
        var minSparedMorning = S(P + "alone.minagho_spared_morning");
        check(!Av(pairMorning, yes[0]) && Av(pairMorning, Later(story, yes[0])), "The pair's morning is not the morning after.");
        var pairMorningOut = Done(pairMorning, Later(story, yes[0]));
        check(pairMorningOut.Count == 4 && pairMorningOut.All(r => r.Has(P + "cost.morning_after")) && !Av(pairMorning, Later(story, pairMorningOut[0])),
            "The pair's morning lost a branch or repeats.");
        check(Av(chivMorning, Later(story, chivYes[0])) && Done(chivMorning, Later(story, chivYes[0])).Any(r => r.Has(P + "morning_coin")),
            "Chivarro's morning after is missing.");
        check(Av(minSparedMorning, Later(story, minYes[0])) && !Av(minMorning, Later(story, minYes[0]))
              && Done(minSparedMorning, Later(story, minYes[0])).Any(r => r.Has(P + "morning_bound")), "Minagho's morning after is missing.");
        var minRetYes = Done(aloneMin, minReturnedAlone).Single(r => r.Has(Complete));
        check(Av(minMorning, Later(story, minRetYes)) && !Av(minSparedMorning, Later(story, minRetYes)), "The returned Minagho has no morning after.");
        foreach (var m in new[] { pairMorning, chivMorning, minMorning, minSparedMorning })
            check(!m.Remote && m.InteractionHub != null && m.DelayHours > 0, "A morning after is not a physical beat after the night: " + m.Id);

        // Epilogue page selection. The committed pair's page and the late-commit page never play together.
        check(epPair.Requires.Contains(Complete) && epCommit.Forbids.Contains(Complete), "The pair ending and the late commit can both play.");
        var lateHouse = World(story, 5, "trickster", "trickster.ever", Reunited, ChIn, MinIn, "minagho.spared_c4", P + "tprev.house");
        var lateOutcomes = Program.Walk(epCommit, lateHouse);
        check(lateOutcomes.Count == 2 && Pages(epCommit, lateHouse).Contains("pair") && !Pages(epCommit, lateHouse).Contains("waiting"),
            "The late-commit page does not let the Commander choose.");
        check(Pages(epCommit, World(story, 5, "trickster", "trickster.ever", ChIn, Waiting, "minagho.dead")).Contains("waiting"), "The late page names two women when one is waiting.");
        // Sol INT/BEL: each late acceptance is its own ending, staged to the threshold; regrets is not a romance, and the Last
        // Call coda (played for the rift's committed partners) never reads a late page.
        check(Pages(epCommit, lateHouse).Contains("went") && !Pages(epCommit, lateHouse).Contains("went_alone")
              && Pages(epCommit, World(story, 5, "trickster", "trickster.ever", ChIn, Waiting, "minagho.dead")).Contains("went_alone"),
            "The late acceptances are not distinct, staged endings.");
        // Sol r4: the endings do not outlive an unreturned sacrifice; the owned page brings no dead Minagho; Chivarro alone assumes no palm wound.
        foreach (var ep in new[] { epPair, epChiv, epMin, epCommit })
            check(ep.Forbids.Contains("sacrifice") && ep.ForbidOverrides.TryGetValue("sacrifice", out var back) && back == "trickster.commander_back",
                "A living ending plays for a Commander who stayed dead: " + ep.Id);
        check(epOwned.Nodes[0].Paragraphs.Any(p => p.Requires.Contains(MinIn)),
            "The owned page brings an unreturned Minagho to visit.");
        check(aloneChiv.Nodes.Any(n => n.Id == "threshold_clean"), "Chivarro alone assumes the Goat's wound.");
        // Coordinator rulings (r5): the deposit is offered on Herrax's list as a plain question; an unprepared kill is told plainly
        // (Herrax's letter, the Ledger's secret) and never undone; the red-silk meeting settles the house (no ninth letter).
        var unbought = S(P + "chivarro_dead.unbought");
        var bareKill = World(story, 5, "trickster", "trickster.ever", "chivarro.dead", "chivarro.exile_objective_done", "herrax.asked_kill_chivarro");
        check(Av(unbought, bareKill) && Done(unbought, bareKill).All(r => r.Has("trickster.secret.chivarro_lost"))
              && !Av(unbought, With(bareKill, Deposit)) && !Av(bought, bareKill), "The unprepared kill is not told plainly, or is undone.");
        var wonWorld = World(story, 5, "trickster", "trickster.ever", P + "chivarro_walked", ChIn);
        check(Done(wonBack, wonWorld).Where(r => r.Has(P + "tprev.name")).All(r => r.Has(P + "tprev.house"))
              && !Av(house, Later(story, Done(wonBack, wonWorld).First(r => r.Has(P + "tprev.name")))), "The red-silk path still sends the house letter.");
        var coda = S("minachiv.lastcall.page");
        check(coda.Requires.Contains(Complete) && !Av(coda, With(lateHouse, "trickster.lastcall.taken")),
            "The Last Call coda plays for a late page's Commander.");
        // Sol COX: the coda bleeds the debtor's palm, and names the women the Commander committed to.
        var codaText = string.Join(" ", coda.Nodes.SelectMany(n => new[] { SurfaceIds.Of(story, n) }.Concat(n.Paragraphs.Select(p => SurfaceIds.Of(story, p)))));

        // Sol BEL: a letter commit brings them in person to a threshold and its own morning; the physical morning needs its night.
        var letterYes = Done(roadLetter, World(story, 5, "trickster", "trickster.ever", Reunited, ChIn, MinIn, "minagho.spared_c4", P + "tprev.house",
                                               "minagho_chivarro.presence.chivarro.failed")).Where(r => r.Has(Complete)).ToList();
        check(letterYes.Count == 1 && letterYes[0].Has(P + "night.pair") && letterYes[0].Has(P + "cost.morning_after")
              && Pages(roadLetter, World(story, 5, "trickster", "trickster.ever", Reunited, ChIn, MinIn, "minagho.spared_c4", P + "tprev.house",
                                         "minagho_chivarro.presence.chivarro.failed")).Contains("came")
              && S(P + "after.the_morning_after").Requires.Contains(P + "night.pair")
              && S(P + "alone.chivarro_morning").Requires.Contains(P + "night.chivarro")
              && S(P + "alone.minagho_morning").Requires.Contains(P + "night.minagho"),
            "A letter commit has no night, or a morning plays without one.");
        foreach (var id in new[] { "alone.chivarro_letter", "alone.minagho_letter" })
            check(S(P + id).Nodes.Any(n => n.Id == "came") && S(P + id).Nodes.Any(n => n.Id == "morning"), "A letter commit has no staged night: " + id);

        // Reactions.
        foreach (var id in new[] { "react.daeran", "react.wenduag", "react.socoth_fee", "react.camellia_bill" })
            check(S(P + id).Reaction && S(P + id).Nodes.Count == 1, "Reaction shape: " + id);
        check(Av(S(P + "react.daeran"), World(story, 5, "trickster", "trickster.ever", RetM, "minagho.dead", MinIn))
              && !Av(S(P + "react.daeran"), World(story, 5, "trickster", "trickster.ever", RetM, "minagho.dead", "daeran.dead")), "Daeran's reaction guard.");
        check(Av(S(P + "react.socoth_fee"), World(story, 5, "trickster", "trickster.ever", P + "cost.socoth_owed"))
              && !Av(S(P + "react.socoth_fee"), World(story, 5, "trickster", "trickster.ever", P + "cost.socoth_owed", "socot.gone")), "Socothbenoth's fee outlives him.");
        check(Av(S(P + "react.camellia_bill"), World(story, 5, "trickster", "trickster.ever", RetC, "chivarro.dead", "chivarro.exile_objective_done"))
              && !Av(S(P + "react.camellia_bill"), World(story, 5, "trickster", "trickster.ever", RetC, "chivarro.dead", "chivarro.exile_objective_done", "camellia.dead")), "Camellia's reaction guard.");
        // A returned Camellia whose body died otherwise reacts on her hub; a killed one returns veiled at Fye's, with no hub to react on.
        var camellia = S(P + "react.camellia_bill");
        check(Av(camellia, World(story, 5, "trickster", "trickster.ever", RetC, "chivarro.dead", "chivarro.exile_objective_done", "camellia.trickster.returned"))
              && !camellia.ForbidOverrides.ContainsKey("camellia.killed")
              && !Av(camellia, World(story, 5, "trickster", "trickster.ever", RetC, "chivarro.dead", "chivarro.exile_objective_done", "camellia.killed", "camellia.dead", "camellia.trickster.returned")),
            "Camellia's reaction ignores her return, or claims the veiled Camellia's missing hub.");

        // The registered route (save-safe edits only): lost pages never play for a returned woman; the chain has its own endings.
        foreach (var s in story.Scenes.Where(s => s.Relationship == "minagho_chivarro" && !s.Id.StartsWith(P, StringComparison.Ordinal)
            && !Rules.IsNativeReplacement(story, s))) // eng7-f6c: native text is covered by the selector suite
        {
            if (s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)) check(s.Forbids.Contains(Chain), "A registered ending plays after a Trickster commit: " + s.Id);
            foreach (var death in new[] { ("minagho.dead", RetM), ("chivarro.dead", RetC) })
                if (s.Forbids.Contains(death.Item1)) check(s.ForbidOverrides.TryGetValue(death.Item1, out var o) && o == death.Item2, "G6(b) missing on " + s.Id);
        }
        check(S("minachiv.ending_minagho_lost_completed").Forbids.Contains(RetM) && S("minachiv.ending_chivarro_lost").Forbids.Contains(RetC)
              && S("minachiv.ending_both_lost").Forbids.Contains(RetM) && S("minachiv.ending_both_lost").Forbids.Contains(RetC), "G6(a) missing on a lost page.");

        Snapshot aliveCell0() => World(story, 5, "trickster", "trickster.ever", "minagho.spared_c4", Primed);
        Snapshot With(Snapshot w, params string[] flags)
        {
            var next = Program.Copy(w);
            foreach (var flag in flags) if (next.Flags.Add(flag)) next.Times[flag] = next.Hour - 1000;
            Rules.Complete(story, next);
            return next;
        }
    }
}
