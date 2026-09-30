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
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000 };
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
        var boughtText = string.Join(" ", bought.Nodes.Select(n => n.Text));
        check(!boughtText.Contains("raises what the house sells", StringComparison.Ordinal) && !boughtText.Contains("priestess", StringComparison.Ordinal)
              && !boughtText.Contains("A corpse is not forever", StringComparison.Ordinal) && boughtText.Contains("Sael", StringComparison.Ordinal)
              && boughtText.Contains("buy all of it", StringComparison.Ordinal) && bought.Requires.Contains(Deposit),
            "Chivarro's return is not the prepared double, or a raise came back (memory rrt-unique-devices).");
        check(deposit.Nodes.Any(n => n.Text.Contains("the rings, and whatever the rings are on", StringComparison.Ordinal) && n.Text.Contains("Sael", StringComparison.Ordinal))
              && deposit.Nodes.Single(n => n.Id == "ink").Choices[0].Set.Contains("trickster.secret.chivarro_double"),
            "The deposit no longer plans the double before the kill, or its secret is not kept.");
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
              && new[] { setupC4, setupC3 }.All(s => s.EntryMythic == "PlayerIsTrickster" && s.Entry.Contains("I'm the one who failed him")),
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
        var shove = wardrobe.Nodes.SelectMany(n => n.Choices).Where(c => c.Text.Contains("Mind the corsets")).ToList();
        check(shove.Count > 0 && shove.All(c => c.Mythic == "PlayerIsTrickster" && c.Alignment?.Direction == "Chaotic"), "The shove lost its [Trickster] answer or its price.");
        foreach (var commit in new[] { road, aloneChiv, aloneMin, aloneMinSpared })
            check(commit.Nodes.Any(n => n.Id == "threshold") && commit.Nodes.SelectMany(n => n.Choices).Where(c => c.Set.Contains(Complete)).All(c => c.Next == "threshold" && c.Set.Contains(Chain)),
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
        var delivered = World(story, 5, "trickster.ever", "minagho.dead", Primed, Debt, Terms, Delivered);
        check(Av(brand, delivered) && !Av(collateral, delivered) && !Av(brandLetter, delivered), "Trk_Minagho_DeadReturn: availability.");
        var woken = Done(brand, delivered);
        check(woken.Count == 2 && woken.All(r => r.Has(RetM) && r.Has(P + "cost.palm_scar") && r.Has(MinIn) && r.Has("minachiv.started")),
            "Trk_Minagho_DeadReturn: flags.");
        check(woken.Count(r => r.Has(P + "claimed_debt")) == 1, "The pivotal evil answer is missing.");
        check(Done(brand, World(story, 5, "trickster.ever", "minagho.dead", Primed, Debt, Terms, Delivered, ChIn)).Any(r => r.Has(Reunited)),
            "A waiting Chivarro is not reunited at the wake.");
        var wakePages = Pages(brand, World(story, 5, "trickster.ever", "minagho.dead", Primed, Debt, Terms, Delivered, Knelt, "minagho.killed_by_staunton"));
        check(wakePages.Contains("wake_knelt") && wakePages.Contains("wake_staunton") && !wakePages.Contains("wake_late"), "The wake variants misfire.");
        check(Av(brandLetter, World(story, 5, "trickster.ever", "minagho.dead", Primed, Debt, Terms, Delivered, "minagho_chivarro.presence.minagho.failed")),
            "The brand's letter twin does not open when her presence fails.");

        // Trk_Minagho_DeadNoBargain: collectors bring the corpse; the Goat's own iron.
        var refusedWorld = World(story, 5, "trickster.ever", "minagho.dead", Primed, Debt, "baphomet.parley", Refused);
        check(Av(collateral, refusedWorld) && !Av(brand, refusedWorld) && !Av(parley, refusedWorld), "Trk_Minagho_DeadNoBargain: availability.");
        var ironed = Done(collateral, refusedWorld).Where(r => r.Has(RetM)).ToList();
        check(ironed.Count >= 2 && ironed.All(r => r.Has(P + "cost.palm_scar") && r.Has(Met) && r.Has(P + "cost.baphomet_branded")),
            "Trk_Minagho_DeadNoBargain: flags.");
        check(!Av(collectors, Later(story, ironed[0])), "Trk_Minagho_DeadNoBargain: the collectors come twice.");
        check(Pages(collateral, refusedWorld).Contains("gate_refused"), "The refused gift is not delivered anyway.");

        // Trk_Minagho_DeadHanged.
        var passed = World(story, 5, "trickster.ever", "minagho.dead", Primed, Debt, "baphomet.parley");
        var hanged = Done(collateral, passed).Single(r => r.Has(DeclM));
        check(!hanged.Has(RetM) && !Av(collateral, Later(story, hanged)) && !Av(brand, Later(story, hanged)), "Trk_Minagho_DeadHanged failed.");

        // Trk_Minagho_PathFailedUnprimed.
        var failed = World(story, 5, "trickster.ever", "trickster.failed", "minagho.dead", "baphomet.parley");
        check(!Av(parley, failed) && !Av(collateral, failed) && !Av(brand, failed) && !Av(spared, failed), "Trk_Minagho_PathFailedUnprimed failed.");
        check(Av(parley, World(story, 5, "trickster.ever", "trickster.failed", "minagho.dead", "baphomet.parley", Primed, Debt)),
            "A primer taken as a Trickster no longer pays off after the path failed.");

        // Trk_Minagho_BothDead: the shared-flag blocker is gone.
        var bothDead = World(story, 5, "trickster", "trickster.ever", "minagho.dead", "chivarro.dead", Primed, Debt, Terms, Delivered, Deposit, Favor);
        check(Av(brand, bothDead) && Av(bought, bothDead) && !Av(wardrobe, With(bothDead, "closets.known")), "Trk_Minagho_BothDead failed.");

        // Trk_Minagho_SparedPrimed / _FledUnprimed.
        var sparedWorld = World(story, 5, "trickster.ever", "minagho.spared_c4", Primed, Debt);
        check(Av(spared, sparedWorld) && !Av(brand, sparedWorld), "Trk_Minagho_SparedPrimed: availability.");
        var sparedOut = Done(spared, sparedWorld);
        check(sparedOut.Count(r => r.Has(MinIn)) == 2 && sparedOut.Count(r => r.Has(DeclM)) == 1, "Trk_Minagho_SparedPrimed: flags.");
        var fled = World(story, 5, "trickster", "trickster.ever", "minagho.fled_fane");
        check(Av(spared, fled), "Trk_Minagho_FledUnprimed: availability.");
        check(Done(spared, fled).Where(r => r.Has(MinIn)).All(r => r.Has(Primed) && r.Has(Debt) && r.Has(LateClaim)), "Trk_Minagho_FledUnprimed: flags.");
        check(!Av(spared, World(story, 5, "trickster.ever", "minagho.fled_fane")), "An unprimed spared return is offered after the path ended.");
        check(Pages(spared, With(sparedWorld, "minagho.terrified")).Contains("terrified"), "The terrified variant is missing.");
        check(Av(sparedLetter, With(sparedWorld, "minagho_chivarro.presence.minagho_spared.failed")) && !Av(sparedLetter, sparedWorld),
            "The spared letter twin misfires.");

        // Trk_Minagho_SparedParleyAlive.
        var aliveCell = World(story, 5, "trickster.ever", "minagho.spared_c4", Primed);
        check(Av(parley, aliveCell) && Done(parley, aliveCell).Any(r => r.Has(P + "baphomet_heard")), "Trk_Minagho_SparedParleyAlive failed.");

        // Trk_Minagho_Collectors (the spared presence's copy of the beat).
        var inDrezen = World(story, 5, "trickster.ever", "minagho.spared_c4", Primed, Debt, MinIn);
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
        var pair = World(story, 5, "trickster.ever", Reunited, ChIn, MinIn, "minagho.spared_c4");
        check(Av(offer, pair) && !Av(price, pair), "Trk_Chivarro_PairChain: availability.");
        var offered = Done(offer, pair);
        check(offered.Count == 2 && offered.All(r => r.Has(P + "tprev.offer")) && Av(price, Later(story, offered[0])), "Trk_Chivarro_PairChain: the price does not follow.");
        var priceOut = Done(price, Later(story, offered[0]));
        var named = priceOut.Single(r => r.Has(P + "tprev.name"));
        var walked = priceOut.Where(r => r.Has(P + "chivarro_walked")).ToList();
        check(named.Has(P + "cost.palm_on_table") && walked.Count == 2, "Her refusal gate is not on every branch of the price.");
        check(Av(wonBack, Later(story, walked[0])) && !Av(house, Later(story, walked[0])), "Trk_Chivarro_PriceWalked failed.");
        var won = Done(wonBack, Later(story, walked[0]));
        check(won.Single(r => r.Has(P + "tprev.name")).Has(P + "cost.won_back") && won.Any(r => r.Has(SentBack)), "The priced second ask is missing.");
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

        // Trk_Chivarro_ReunionMinaghoDead: Chivarro first, alone; her own commit.
        var waitingWorld = World(story, 5, "trickster", "trickster.ever", "closets.known", "minagho.dead");
        check(Av(wardrobe, waitingWorld), "Trk_Chivarro_ReunionMinaghoDead: availability.");
        var waiting = Done(wardrobe, waitingWorld).Single(r => r.Has(Waiting));
        check(waiting.Has(ChIn) && Av(aloneChiv, Later(story, waiting)) && Av(epCommit, waiting), "Trk_Chivarro_ReunionMinaghoDead failed.");
        var chivYes = Done(aloneChiv, Later(story, waiting)).Where(r => r.Has(Complete)).ToList();
        check(chivYes.Count == 1 && chivYes[0].Has("minachiv.future_chivarro") && chivYes[0].Has(P + "cost.half_the_pair") && Av(epChiv, chivYes[0]),
            "Chivarro's alone commit failed.");
        // Minagho comes home later: the wake reunites them, and the alone commit closes.
        var bothIn = Done(brand, World(story, 5, "trickster.ever", "minagho.dead", Primed, Debt, Terms, Delivered, ChIn, Waiting)).Single(r => r.Has(Reunited));
        check(!Av(aloneChiv, Later(story, bothIn)) && Av(offer, Later(story, bothIn)), "A reunited pair still sees the alone commit.");

        // Trk_Chivarro_BothDead / _Killed / _Deposit / _KilledNoDepositLate / _DepositSurvivesFailure / _KilledNoDepositFailed / _KeptBill.
        var bd = World(story, 5, "trickster", "trickster.ever", "chivarro.dead", "minagho.dead", Deposit, Favor);
        check(Av(bought, bd) && Av(parley, With(bd, "baphomet.parley")) && !Av(wardrobe, With(bd, "closets.known")), "Trk_Chivarro_BothDead failed.");
        var killed = World(story, 5, "trickster", "trickster.ever", "chivarro.dead", Deposit, Favor);
        var boughtOut = Done(bought, killed);
        check(boughtOut.Any(r => r.Has(RetC) && r.Has(ChIn) && r.Has(P + "bill_burned")) && !Av(wardrobe, With(killed, "closets.known")), "Trk_Chivarro_Killed failed.");
        // Trk_Chivarro_KilledNoDeposit: nothing was prepared, the Commander killed her, and the death stands; Minagho knows.
        var killedBare = World(story, 5, "trickster", "trickster.ever", "chivarro.dead");
        check(!Av(bought, killedBare) && boughtOut.Where(r => r.Has(RetC)).All(r => !r.Has(Late)), "Trk_Chivarro_KilledNoDeposit failed: a witnessed death is undone.");
        var killerWorld = World(story, 5, "trickster.ever", "chivarro.dead", MinIn, "minagho.spared_c4");
        check(Pages(aloneMinSpared, killerWorld).Contains("killer") && !Pages(aloneMinSpared, With(killerWorld, Deposit, DeclC)).Contains("killer"),
            "Minagho does not face the Commander who killed Chivarro.");
        var herrax = World(story, 4, "trickster", "trickster.ever", "herrax.asked_kill_chivarro");
        check(Av(deposit, herrax) && Done(deposit, herrax).Single().Has(Deposit) && Done(deposit, herrax).Single().Has(Favor), "Trk_Chivarro_Deposit failed.");
        var depositFailed = World(story, 5, "trickster.ever", "trickster.failed", "chivarro.dead", Deposit, Favor);
        check(Av(bought, depositFailed) && Done(bought, depositFailed).Where(r => r.Has(RetC)).All(r => !r.Has(Late)), "Trk_Chivarro_DepositSurvivesFailure failed.");
        check(!Av(bought, World(story, 5, "trickster.ever", "trickster.failed", "chivarro.dead")), "Trk_Chivarro_KilledNoDepositFailed failed.");
        var ownedOut = boughtOut.Single(r => r.Has(Owned));
        check(ownedOut.Has(RetC) && !ownedOut.Has("minachiv.started") && !Av(aloneChiv, Later(story, ownedOut, "minagho.dead", DeclM)),
            "Trk_Chivarro_KeptBill failed: keeping the bill starts the relationship.");
        // The kept bill never buys a romance: nothing of the pair moves until Chivarro's bill scene, where it is burned or kept.
        var bill = S(P + "chivarro_dead.the_bill");
        var billLetter = S(P + "chivarro_dead.the_bill_letter");
        var ownedReady = World(story, 5, "trickster.ever", Reunited, ChIn, MinIn, RetC, "chivarro.dead", "minagho.spared_c4", Owned, P + "tprev.house");
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
        check(Pages(price, Later(story, With(burned, P + "tprev.offer"))).Contains("owned"), "The owned variant of the price is missing.");

        // Trk_Chivarro_MinaghoAlone (spared presence copy of the beat) and the dead-returned beat.
        var minAlone = World(story, 5, "trickster.ever", "chivarro.dead", MinIn, "minagho.spared_c4", DeclC);
        check(Av(aloneMinSpared, minAlone) && !Av(aloneMin, minAlone), "Trk_Chivarro_MinaghoAlone: availability.");
        var minYes = Done(aloneMinSpared, minAlone).Where(r => r.Has(Complete)).ToList();
        check(minYes.Count == 1 && minYes[0].Has("minachiv.future_minagho") && Av(epMin, minYes[0]), "Trk_Chivarro_MinaghoAlone: flags.");
        var minReturnedAlone = World(story, 5, "trickster.ever", "minagho.dead", "chivarro.dead", RetM, MinIn, DeclC, Primed, Debt, Terms, Delivered);
        check(Av(aloneMin, minReturnedAlone) && !Av(aloneMinSpared, minReturnedAlone), "The returned Minagho has no alone commit.");

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
        var lateHouse = World(story, 5, "trickster.ever", Reunited, ChIn, MinIn, "minagho.spared_c4", P + "tprev.house");
        var lateOutcomes = Program.Walk(epCommit, lateHouse);
        check(lateOutcomes.Count == 2 && Pages(epCommit, lateHouse).Contains("pair") && !Pages(epCommit, lateHouse).Contains("waiting"),
            "The late-commit page does not let the Commander choose.");
        check(Pages(epCommit, World(story, 5, "trickster.ever", ChIn, Waiting, "minagho.dead")).Contains("waiting"), "The late page names two women when one is waiting.");
        // Sol INT/BEL: each late acceptance is its own ending, staged to the threshold; regrets is not a romance, and the Last
        // Call coda (played for the rift's committed partners) never reads a late page.
        check(Pages(epCommit, lateHouse).Contains("went") && !Pages(epCommit, lateHouse).Contains("went_alone")
              && Pages(epCommit, World(story, 5, "trickster.ever", ChIn, Waiting, "minagho.dead")).Contains("went_alone")
              && epCommit.Nodes.Single(n => n.Id == "went").Text.Contains("bore the Commander down")
              && epCommit.Nodes.Single(n => n.Id == "went_alone").Text.Contains("let the gown fall")
              && !epCommit.Nodes.Single(n => n.Id == "regrets").Text.Contains("bed"),
            "The late acceptances are not distinct, staged endings.");
        var coda = S("minachiv.lastcall.page");
        check(coda.Requires.Contains(Complete) && !Av(coda, With(lateHouse, "trickster.lastcall.taken")),
            "The Last Call coda plays for a late page's Commander.");
        // Sol COX: the coda bleeds the debtor's palm, and names the women the Commander committed to.
        var codaText = string.Join(" ", coda.Nodes.SelectMany(n => new[] { n.Text }.Concat(n.Paragraphs.Select(p => p.Text))));
        check(!codaText.Contains("Minagho's palm", StringComparison.Ordinal) && codaText.Contains("the Commander's palm still opened at dawn", StringComparison.Ordinal)
              && coda.Nodes.SelectMany(n => n.Paragraphs).Any(p => p.Requires.Contains("minachiv.future_chivarro"))
              && coda.Nodes.SelectMany(n => n.Paragraphs).Any(p => p.Requires.Contains("minachiv.future_minagho"))
              && coda.Nodes.SelectMany(n => n.Paragraphs).Any(p => p.Requires.Contains("minachiv.future_two"))
              && !coda.Nodes[0].Text.Contains("Minagho and Chivarro", StringComparison.Ordinal),
            "The Last Call coda contradicts the debt or the committed partners.");
        // Sol BEL: a letter commit brings them in person to a threshold and its own morning; the physical morning needs its night.
        var letterYes = Done(roadLetter, World(story, 5, "trickster.ever", Reunited, ChIn, MinIn, "minagho.spared_c4", P + "tprev.house",
                                               "minagho_chivarro.presence.chivarro.failed")).Where(r => r.Has(Complete)).ToList();
        check(letterYes.Count == 1 && letterYes[0].Has(P + "night.pair") && letterYes[0].Has(P + "cost.morning_after")
              && Pages(roadLetter, World(story, 5, "trickster.ever", Reunited, ChIn, MinIn, "minagho.spared_c4", P + "tprev.house",
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
        check(Av(S(P + "react.daeran"), World(story, 5, "trickster.ever", RetM, "minagho.dead", MinIn))
              && !Av(S(P + "react.daeran"), World(story, 5, "trickster.ever", RetM, "minagho.dead", "daeran.dead")), "Daeran's reaction guard.");
        check(Av(S(P + "react.socoth_fee"), World(story, 5, "trickster.ever", P + "cost.socoth_owed"))
              && !Av(S(P + "react.socoth_fee"), World(story, 5, "trickster.ever", P + "cost.socoth_owed", "socot.gone")), "Socothbenoth's fee outlives him.");
        check(Av(S(P + "react.camellia_bill"), World(story, 5, "trickster.ever", RetC, "chivarro.dead"))
              && !Av(S(P + "react.camellia_bill"), World(story, 5, "trickster.ever", RetC, "chivarro.dead", "camellia.dead")), "Camellia's reaction guard.");
        // A returned Camellia whose body died otherwise reacts on her hub; a killed one returns veiled at Fye's, with no hub to react on.
        var camellia = S(P + "react.camellia_bill");
        check(Av(camellia, World(story, 5, "trickster.ever", RetC, "chivarro.dead", "camellia.dead", "camellia.trickster.returned"))
              && !camellia.ForbidOverrides.ContainsKey("camellia.killed")
              && !Av(camellia, World(story, 5, "trickster.ever", RetC, "chivarro.dead", "camellia.killed", "camellia.dead", "camellia.trickster.returned")),
            "Camellia's reaction ignores her return, or claims the veiled Camellia's missing hub.");

        // The registered route (save-safe edits only): lost pages never play for a returned woman; the chain has its own endings.
        foreach (var s in story.Scenes.Where(s => s.Relationship == "minagho_chivarro" && !s.Id.StartsWith(P, StringComparison.Ordinal)))
        {
            if (s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)) check(s.Forbids.Contains(Chain), "A registered ending plays after a Trickster commit: " + s.Id);
            foreach (var death in new[] { ("minagho.dead", RetM), ("chivarro.dead", RetC) })
                if (s.Forbids.Contains(death.Item1)) check(s.ForbidOverrides.TryGetValue(death.Item1, out var o) && o == death.Item2, "G6(b) missing on " + s.Id);
        }
        check(S("minachiv.ending_minagho_lost_completed").Forbids.Contains(RetM) && S("minachiv.ending_chivarro_lost").Forbids.Contains(RetC)
              && S("minachiv.ending_both_lost").Forbids.Contains(RetM) && S("minachiv.ending_both_lost").Forbids.Contains(RetC), "G6(a) missing on a lost page.");

        Snapshot With(Snapshot w, params string[] flags)
        {
            var next = Program.Copy(w);
            foreach (var flag in flags) if (next.Flags.Add(flag)) next.Times[flag] = next.Hour - 1000;
            Rules.Complete(story, next);
            return next;
        }
    }
}
