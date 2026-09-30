using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Nurah, Trickster (Writer/handoffs/trickster/nurah.md): the pardon that wasn't forged (F03, at her cell), the bill of sale
// (F24, Ramisa's market) and the dedication (F03, ran off). One block per spec rules test (Trk_Nurah_*), plus the hooks,
// the presences, the reactions and the registered-route overrides.
internal static class NurahTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string CellA = "01d00f006e0e16543b7507ff38e9fb8a";
    private const string CellB = "6201570ac1b1d8c4b878f935a7b0160e";
    private const string Ramisa = "52cca621c1d850641abdde32373ca592";
    private static readonly string[] Deaths = { "nurah.dead_drezen", "nurah.killing_mechanism" };

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, int? chapter = null)
    {
        var later = Program.Copy(state); later.Hour += hours; if (chapter != null) later.Chapter = chapter.Value;
        Rules.Complete(story, later); return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var pardon = S("nurah.trickster.prison.pardon");
        var pardonR = S("nurah.trickster.prison.pardon_recruited");
        var night = S("nurah.trickster.prison.night_out");
        var pProofs = S("nurah.trickster.prison.proofs");
        var pTerms = S("nurah.trickster.prison.terms");
        var rumour = S("nurah.trickster.dead.rumour");
        var bill = S("nurah.trickster.dead.bill_of_sale");
        var courier = S("nurah.trickster.dead.rumour_courier");
        var dedication = S("nurah.trickster.ran_off.dedication");
        var pedlar = S("nurah.trickster.ran_off.second_draft");
        var reply = S("nurah.trickster.ran_off.terms_by_post");
        var proofs = S("nurah.trickster.after.proofs");
        var terms = S("nurah.trickster.terms");
        var ranTerms = S("nurah.trickster.ran_off.terms");
        var epCommit = S("nurah.trickster.epilogue.commit");
        var epRefused = S("nurah.trickster.epilogue.refused");
        bool Commits(Scene scene, Snapshot w) => Program.Walk(scene, w).Any(r => r.Has("nurah.complete"));
        Snapshot After(Scene scene, Snapshot w, string node, int choice)
        {
            // An outcome whose path took this answer (it holds every flag the answer sets).
            var target = scene.Nodes.Single(n => n.Id == node).Choices[choice];
            var hit = Program.Walk(scene, w).FirstOrDefault(o => target.Set.All(o.Has));
            check(hit != null && target.Set.Length > 0, "No outcome through " + scene.Id + "/" + node + "/" + choice);
            return hit ?? w;
        }

        // Hooks and shape.
        check(pardon.AnswerLists.SequenceEqual(new[] { CellA }) && pardon.NativeReturnCue == "c852cfeeaf0fa4744ade8f3e36e01d74"
              && pardonR.AnswerLists.SequenceEqual(new[] { CellB }) && pardonR.NativeReturnCue == "9aab5c83956171d4c8a017dcff3a1554",
            "The pardons left their cell lists or their clean return cues.");
        foreach (var s in new[] { pardon, pardonR, dedication })
            check(s.EntryMythic == "PlayerIsTrickster" && s.EntryAlignment?.Direction == "Chaotic" && s.EntryAlignment.Value == 1,
                "The joke lost its [Trickster] entry: " + s.Id);
        foreach (var s in new[] { night, pProofs, pTerms, dedication })
            check(s.AnswerLists.SequenceEqual(new[] { CellA, CellB }) && s.NativeReturnCue == null && s.TricksterDevice
                  && s.TricksterState == "prison" && !Rules.IsRemote(s), "A cell beat left her cell: " + s.Id);
        check(rumour.AnswerLists.SequenceEqual(new[] { Ramisa }) && rumour.NativeReturnCue == "96301374cccd56d438a5a5069d4821f0"
              && rumour.Chapters.SequenceEqual(new[] { 4 }) && rumour.TricksterState == "dead", "Ramisa's market hook is wrong.");
        check(bill.Remote && bill.Chapters.SequenceEqual(new[] { 4 }) && courier.Remote && courier.Chapters.SequenceEqual(new[] { 5 })
              && pedlar.Remote && pedlar.Chapters.SequenceEqual(new[] { 3 }) && reply.Remote && proofs.Remote,
            "A letter lost its chapter.");
        check(terms.InteractionHub == "nurah.presence.raised" && ranTerms.InteractionHub == "nurah.presence"
              && Rules.IsPresenceHubScene(terms) && Rules.IsPresenceHubScene(ranTerms), "The in-person terms lost their presences.");
        var rel = story.Relationships["nurah"];
        check(rel.TricksterAccess.Count == 3 && rel.TricksterAccess["prison"].Returned == "nurah.trickster.released"
              && rel.TricksterAccess["dead"].Returned == "nurah.trickster.returned" && rel.TricksterAccess["ran_off"].Returned == "nurah.trickster.accepted"
              && rel.UnavailableOverrides["nurah.prison"] == "nurah.trickster.released"
              && Deaths.Concat(new[] { "nurah.dead_camellia" }).All(f => rel.UnavailableOverrides[f] == "nurah.trickster.returned"),
            "Nurah relationship patch missing.");
        check(story.Presences["nurah.presence"].Mode == "reuse-native" && story.Presences["nurah.presence.raised"].Mode == "spawn-copy"
              && story.Presences.Where(p => p.Key.StartsWith("nurah.presence", StringComparison.Ordinal)).All(p => p.Value.Dialog == "hub"
                  && p.Value.Unit == "f999fc37ddb225640b7f98c0a05d6948"
                  && p.Value.At?.Locator == (p.Key == "nurah.presence.cell" ? "336980c3-ad90-4633-aad9-4ef3f40c13f6" : "7b94948a-1954-428f-82d0-94b2adcb1380"))
              && Rules.PresencesExclusive(story.Presences["nurah.presence"], story.Presences["nurah.presence.raised"])
              && Rules.PresencesExclusive(story.Presences["nurah.presence.cell"], story.Presences["nurah.presence"])
              && Rules.PresencesExclusive(story.Presences["nurah.presence.cell"], story.Presences["nurah.presence.raised"]),
            "Nurah presences malformed.");
        // Sol quality pass (CAN): NurahInPrisonCapitalMechanic shows her at the cell only while Chapter 3 plays, so the native-list
        // beats are Chapter 3 only and Chapter 5 has hub twins at her own cell locator (NurahInPrison_Locator 336980c3).
        var cellPresence = story.Presences["nurah.presence.cell"];
        check(cellPresence.Mode == "reuse-native" && cellPresence.MinChapter == 5 && cellPresence.MaxChapter == 5
              && cellPresence.Requires.Contains("nurah.prison") && cellPresence.Forbids.Contains("nurah.ran_off")
              && cellPresence.Forbids.Contains("nurah.trickster.returned"), "The Chapter 5 cell presence is malformed.");
        foreach (var s in new[] { pardon, pardonR, night, pProofs, pTerms, dedication })
            check(s.MaxChapter == 3 && s.Chapters.SequenceEqual(new[] { 3 }), "A native-list cell beat outlives Chapter 3: " + s.Id);
        var lateCell = new[] { "pardon_late", "night_out_late", "proofs_late", "terms_late" }.Select(k => S("nurah.trickster.prison." + k)).ToList();
        foreach (var s in lateCell)
            check(s.InteractionHub == "nurah.presence.cell" && s.ContactUnit == "f999fc37ddb225640b7f98c0a05d6948" && Rules.IsPresenceHubScene(s)
                  && s.Chapters.SequenceEqual(new[] { 5 }) && s.TricksterDevice && s.TricksterState == "prison" && s.Forbids.Contains("nurah.ran_off"),
                "A Chapter 5 cell twin is malformed: " + s.Id);
        var price = rumour.Nodes.Single(n => n.Id == "offer").Choices;
        check(price[0].Crusade?.Resource == "Finances" && price[0].Crusade.Amount == -500 && price[1].Mythic == "PlayerIsTrickster",
            "Ramisa's price lost its cost.");

        // Trk_Nurah_Prison: the pardon in person, primed and lied into the ledger; the night out a day later.
        var prison = World(story, 3, "trickster", "trickster.ever", "nurah.prison");
        check(Rules.Available(story, pardon, prison) && !Rules.Available(story, pardonR, prison) && !Rules.Available(story, rumour, prison),
            "Trk_Nurah_Prison: availability.");
        var pardoned = After(pardon, prison, "read", 0);
        check(pardoned.Has("nurah.trickster.primed") && pardoned.Has("nurah.trickster.cost.ledger_lie"), "Trk_Nurah_Prison: flags.");
        check(!Rules.Available(story, night, Later(story, pardoned, 23)) && Rules.Available(story, night, Later(story, pardoned, 24)),
            "Trk_Nurah_Prison: the night out ignores its day.");

        // Trk_Nurah_PrisonRecruited.
        var recruited = World(story, 3, "trickster", "trickster.ever", "nurah.prison", "nurah.trickster_recruited");
        check(Rules.Available(story, pardonR, recruited) && !Rules.Available(story, pardon, recruited), "Trk_Nurah_PrisonRecruited.");

        // Trk_Nurah_NightOut / NightOutRefused: the return beat and her hard no.
        var primed = World(story, 3, "trickster.ever", "nurah.prison", "nurah.trickster.primed", "nurah.trickster.cost.ledger_lie");
        check(Rules.Available(story, night, primed), "Trk_Nurah_NightOut: unavailable.");
        var chaos = After(night, primed, "start", 1);
        check(chaos.Has("nurah.trickster.released") && chaos.Has("nurah.trickster.accepted") && chaos.Has("nurah.trickster.temper_chaos"),
            "Trk_Nurah_NightOut: flags.");
        check(Rules.Available(story, pProofs, Later(story, chaos, 72)) && !Rules.Available(story, pTerms, Later(story, chaos, 72)),
            "Trk_Nurah_NightOut: proofs next, terms not yet.");
        var owned = After(night, primed, "start", 3);
        check(owned.Has("nurah.closed") && !owned.Has("nurah.trickster.released"), "Trk_Nurah_NightOutRefused.");
        check(!story.Scenes.Where(s => s.Relationship == "nurah" && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
                .Any(s => Rules.Available(story, s, Later(story, owned, 500))), "A Nurah scene survives her ownership refusal.");

        // Trk_Nurah_PrisonProofs / PrisonTerms / PrisonTermsRefused.
        var released = World(story, 3, "trickster.ever", "nurah.prison", "nurah.trickster.released", "nurah.trickster.accepted");
        check(Rules.Available(story, pProofs, released) && !Rules.Available(story, proofs, released), "Trk_Nurah_PrisonProofs.");
        var seen = After(pProofs, released, "start", 1);
        check(seen.Has("nurah.trickster.proofs_seen") && seen.Has("nurah.trickster.cost.signed_proofs"), "Trk_Nurah_PrisonProofs: flags.");
        var readyTerms = Later(story, seen, 72);
        check(Rules.Available(story, pTerms, readyTerms) && Commits(pTerms, readyTerms), "Trk_Nurah_PrisonTerms: no commit at the cell.");
        // NUR-01 item 5 is deferred (nurah.md, polish batch 3): the parent "borrowed author" continuation needs the NurahMeeting
        // actor and correspondence the engine derives from the parent romance, which a Trickster-rescued Nurah lacks. Her
        // Trickster route is a complete arc on its own; the continuation must stay shut rather than open a chain that dead-ends.
        var borrowed = S("nurah.borrowed_name");
        check(!Rules.Available(story, borrowed, readyTerms), "The parent continuation opened for a Trickster-only Nurah (a dead end).");
        var pages = new HashSet<string>();
        Program.Walk(pTerms, readyTerms, (page, _) => pages.Add(page));
        check(pages.Contains("threshold") && pages.Contains("morning") && pages.Contains("terms_signed") && !pages.Contains("partners"),
            "Trk_Nurah_PrisonTerms: the night or the signed variant is missing, or the co-author answer shows without the evil temper.");
        check(Program.Walk(pTerms, readyTerms).Any(r => r.Has("nurah.closed") && r.Has("nurah.trickster.cost.name_above") && !r.Has("nurah.complete")),
            "Trk_Nurah_PrisonTermsRefused.");
        var evil = Program.Copy(readyTerms); evil.Flags.Add("nurah.trickster.temper_evil");
        check(Program.Walk(pTerms, evil).Any(r => r.Has("nurah.trickster.cost.coauthor") && r.Has("nurah.complete")), "The co-author answer is missing.");

        // Trk_Nurah_PardonedThenKilled: death blocks the prison beats; Ramisa's market opens in Chapter 4.
        var killed = World(story, 4, "trickster", "trickster.ever", "nurah.trickster.primed", "nurah.trickster.cost.ledger_lie",
                           "nurah.trickster.released", "nurah.trickster.accepted", "nurah.dead_drezen", "nurah.dead_camellia", "nurah.killing_mechanism");
        check(Rules.Available(story, rumour, killed) && !Rules.Available(story, night, killed) && !Rules.Available(story, pProofs, killed),
            "Trk_Nurah_PardonedThenKilled: availability.");
        var paid = After(rumour, killed, "offer", 0);
        check(paid.Has("nurah.trickster.larva_rumour") && paid.Has("nurah.trickster.cost.ramisa_fee"), "Trk_Nurah_PardonedThenKilled: flags.");
        var billReady = Later(story, paid, 24);
        check(Rules.Available(story, bill, billReady), "Trk_Nurah_PardonedThenKilled: no bill.");
        var billPages = new HashSet<string>();
        Program.Walk(bill, billReady, (page, _) => billPages.Add(page));
        check(billPages.Contains("ledger") && billPages.Contains("surcharge") && billPages.Contains("rite_camellia"),
            "The bill forgets the pardon, the surcharge or Camellia's hand.");

        // Trk_Nurah_Executed: the OR group, executed only.
        var executed = World(story, 4, "trickster", "trickster.ever", "nurah.dead_drezen", "nurah.killing_mechanism");
        check(Rules.Available(story, rumour, executed) && !Rules.Available(story, courier, executed), "Trk_Nurah_Executed: availability.");
        var audience = After(rumour, executed, "offer", 1);
        check(audience.Has("nurah.trickster.cost.ramisa_audience") && !audience.Has("nurah.trickster.cost.ramisa_fee"), "Trk_Nurah_Executed: flags.");
        var dead = World(story, 4, "trickster.ever", "nurah.dead_drezen", "nurah.killing_mechanism");
        check(!Rules.Available(story, rumour, dead), "Trk_Nurah_AfterFailure: the market deal without live Trickster power.");

        // Trk_Nurah_BillOfSale / CamelliaBill.
        foreach (var camellia in new[] { false, true })
        {
            var w = World(story, 4, "trickster.ever", "nurah.trickster.primed", "nurah.trickster.larva_rumour", "nurah.trickster.cost.ramisa_audience",
                          "nurah.dead_drezen", "nurah.killing_mechanism");
            if (camellia) { w.Flags.Add("nurah.dead_camellia"); w.Times["nurah.dead_camellia"] = w.Hour - 200; }
            check(Rules.Available(story, bill, w), "Trk_Nurah_BillOfSale: unavailable.");
            var freed = Program.Walk(bill, w).Where(r => r.Has("nurah.trickster.returned")).ToList();
            check(freed.Count > 0 && freed.All(r => r.Has("nurah.trickster.released") && r.Has("nurah.trickster.accepted") && r.Has("nurah.trickster.pseudonym")
                && r.Has("nurah.trickster.cost.chaplains_writ")),
                "Trk_Nurah_BillOfSale: flags.");
            check(Program.Walk(bill, w).Any(r => r.Has("nurah.closed") && r.Has("nurah.trickster.cost.left_in_stock")), "The bill has no way to leave her in stock.");
            var raised = Later(story, freed[0], 100, 5);
            check(Rules.Available(story, proofs, Later(story, raised, 72)), "Trk_Nurah_BillOfSale: no proofs after the raising.");
        }

        // Trk_Nurah_LateCourier: Chapter 5, no Chapter 4 deal; worse terms; the commit falls to the epilogue page.
        var late = World(story, 5, "trickster", "trickster.ever", "nurah.dead_drezen", "nurah.killing_mechanism");
        check(Rules.Available(story, courier, late) && !Rules.Available(story, rumour, late), "Trk_Nurah_LateCourier: availability.");
        var collected = Program.Walk(courier, late).Where(r => r.Has("nurah.trickster.returned")).ToList();
        check(collected.Count > 0 && collected.All(r => r.Has("nurah.trickster.cost.late")), "Trk_Nurah_LateCourier: flags.");
        check(bill.Nodes.Single(n => n.Id == "sent").Choices.Single().Crusade?.Amount == -300
              && courier.Nodes.Single(n => n.Id == "freed").Choices.Single().Crusade?.Amount == -300
              && collected.All(r => r.Has("nurah.trickster.cost.chaplains_writ")), "The chaplains' price for the rite is missing.");
        var lateProofs = Later(story, collected[0], 72);
        check(Rules.Available(story, proofs, lateProofs), "Trk_Nurah_LateCourier: no proofs.");
        var lateSeen = After(proofs, lateProofs, "proofs", 0);
        check(!Rules.Available(story, terms, Later(story, lateSeen, 72)), "Trk_Nurah_LateCourier: in-play terms after a late collection.");
        var ending = Later(story, lateSeen, 72); ending.Chapter = 6;
        check(Rules.Available(story, epCommit, ending) && ending.Has("nurah.trickster.late_committed"), "Trk_Nurah_LateCourier: no epilogue commit.");

        // Trk_Nurah_DeadProofs / DeadTerms / DeadTermsRefused: in person, at the raised presence.
        var returned = World(story, 5, "trickster.ever", "nurah.dead_drezen", "nurah.killing_mechanism", "nurah.trickster.returned",
                             "nurah.trickster.released", "nurah.trickster.accepted");
        check(Rules.Available(story, proofs, returned) && !Rules.Available(story, terms, returned), "Trk_Nurah_DeadProofs.");
        var deadSeen = Later(story, After(proofs, returned, "proofs", 0), 72);
        check(Rules.Available(story, terms, deadSeen) && !Rules.Available(story, ranTerms, deadSeen) && Commits(terms, deadSeen),
            "Trk_Nurah_DeadTerms.");
        check(Rules.PresenceWanted(story.Presences["nurah.presence.raised"], deadSeen) && !Rules.PresenceWanted(story.Presences["nurah.presence"], deadSeen),
            "The raised Nurah is not placed for her terms.");
        check(Program.Walk(terms, deadSeen).Any(r => r.Has("nurah.closed") && !r.Has("nurah.complete")), "Trk_Nurah_DeadTermsRefused.");
        check(Rules.Available(story, epRefused, Later(story, Program.Walk(terms, deadSeen).First(r => r.Has("nurah.closed")), 1)),
            "The refusal page is missing.");

        // Trk_Nurah_RanOff: the dedication and the pardon are both on the cell lists before her release.
        check(Rules.Available(story, dedication, prison) && Rules.Available(story, pardon, prison), "Trk_Nurah_RanOff: availability.");
        var ghost = After(dedication, prison, "write", 0);
        check(ghost.Has("nurah.trickster.primed") && ghost.Has("nurah.trickster.cost.ghostwritten"), "Trk_Nurah_RanOff: flags.");

        // Trk_Nurah_RanOffReply / RanOffRefused / RanOffTerms.
        var ran = World(story, 3, "trickster", "trickster.ever", "nurah.ran_off", "nurah.trickster.primed", "nurah.trickster.cost.ghostwritten");
        check(!Rules.Available(story, dedication, ran) && !Rules.Available(story, pedlar, ran), "The dedication survives her release.");
        check(Rules.Available(story, reply, ran), "Trk_Nurah_RanOffReply: availability.");
        var fresh = Program.Copy(ran); fresh.Times["nurah.trickster.cost.ghostwritten"] = fresh.Hour - 47;
        check(!Rules.Available(story, reply, fresh), "The reply ignores its two days.");
        var accepted = Program.Walk(reply, ran).Where(r => r.Has("nurah.trickster.accepted")).ToList();
        check(accepted.Count == 3 && Program.Walk(reply, ran).Any(r => r.Has("nurah.closed") && r.Has("nurah.trickster.cost.last_word")),
            "Trk_Nurah_RanOffReply / RanOffRefused.");
        var ran5 = Later(story, accepted[0], 100, 5);
        check(Rules.Available(story, proofs, ran5), "Trk_Nurah_RanOffTerms: no proofs.");
        var ranPages = new HashSet<string>();
        Program.Walk(proofs, ran5, (page, _) => ranPages.Add(page));
        check(ranPages.Contains("proofs_ran") && !ranPages.Contains("proofs") && !ranPages.Contains("raised")
              && !proofs.Nodes.Single(n => n.Id == "proofs_ran").Text.Contains("larva", StringComparison.OrdinalIgnoreCase),
            "The living runaway is given a larva's history.");
        check(!epCommit.Nodes.Single(n => n.Id == "start").Text.Contains("worse", StringComparison.Ordinal),
            "The shared epilogue implies a degradation the runaway never had.");
        var ranSeen = Later(story, After(proofs, ran5, "proofs_ran", 0), 72);
        check(Rules.Available(story, ranTerms, ranSeen) && !Rules.Available(story, terms, ranSeen) && Commits(ranTerms, ranSeen),
            "Trk_Nurah_RanOffTerms.");
        check(Rules.PresenceWanted(story.Presences["nurah.presence"], ranSeen) && !Rules.PresenceWanted(story.Presences["nurah.presence.raised"], ranSeen),
            "The runaway is not placed for her terms.");

        // Trk_Nurah_RanOffLate: the pedlar in Chapter 3; the commit falls to the epilogue page.
        var unprimed = World(story, 3, "trickster", "trickster.ever", "nurah.ran_off");
        check(Rules.Available(story, pedlar, unprimed) && !Rules.Available(story, reply, unprimed), "Trk_Nurah_RanOffLate: availability.");
        var bought = After(pedlar, unprimed, "start", 0);
        check(bought.Has("nurah.trickster.cost.late") && bought.Has("nurah.trickster.cost.ghostwritten"), "Trk_Nurah_RanOffLate: flags.");
        check(!Rules.Available(story, pedlar, World(story, 5, "trickster", "trickster.ever", "nurah.ran_off")), "The Chapter 3 pedlar outside Chapter 3.");

        // Sol quality pass (INT): a runaway first approached in Chapter 5 (the missed primer) walks the late pedlar, the late reply,
        // the proofs and the epilogue commit; a Chapter 3 dedication whose reply fell past Chapter 3 gets the late reply.
        var pedlarLate = S("nurah.trickster.ran_off.second_draft_late");
        var replyLate = S("nurah.trickster.ran_off.terms_by_post_late");
        var ranLate = World(story, 5, "trickster", "trickster.ever", "nurah.ran_off");
        check(pedlarLate.Chapters.SequenceEqual(new[] { 5 }) && replyLate.Chapters.SequenceEqual(new[] { 5 }) && pedlarLate.Remote && replyLate.Remote
              && Rules.Available(story, pedlarLate, ranLate) && !Rules.Available(story, pedlarLate, unprimed), "The late pedlar has the wrong window.");
        var lateCost = pedlarLate.Nodes.Single(n => n.Id == "start").Choices[0];
        check(lateCost.Crusade?.Amount == -400 && pedlar.Nodes.Single(n => n.Id == "start").Choices[0].Crusade?.Amount == -200
              && lateCost.Mythic == "PlayerIsTrickster", "The late pedlar is not dearer.");
        var boughtLate = After(pedlarLate, ranLate, "start", 0);
        check(boughtLate.Has("nurah.trickster.cost.second_edition") && boughtLate.Has("nurah.trickster.cost.ghostwritten")
              && boughtLate.Has("nurah.trickster.cost.late"), "The late pedlar's flags.");
        var lateReplyWorld = Later(story, boughtLate, 48);
        check(Rules.Available(story, replyLate, lateReplyWorld) && !Rules.Available(story, reply, lateReplyWorld)
              && lateReplyWorld.Has("nurah.trickster.printer_paid"), "The late reply does not follow the late pedlar.");
        var lateAccepted = Program.Walk(replyLate, lateReplyWorld).Where(r => r.Has("nurah.trickster.accepted")).ToList();
        check(lateAccepted.Count == 6 && Program.Walk(replyLate, lateReplyWorld).Any(r => r.Has("nurah.closed")), "The late reply's outcomes.");
        // Round 5 (COX): the late reply carries the proofs itself, so the missed-primer runaway uses two Chapter 5 deliveries.
        check(lateAccepted.All(r => r.Has("nurah.trickster.proofs_seen")) && !Rules.Available(story, proofs, Later(story, lateAccepted[0], 72)),
            "The late reply does not carry the proofs, or the proofs arrive twice.");
        var ch5Remote = new HashSet<string>();
        var budgetWalk = ranLate;
        foreach (var step in new[] { pedlarLate, replyLate })
        {
            var w = Later(story, budgetWalk, 72);
            foreach (var s in story.Scenes.Where(s => s.Relationship == "nurah" && Rules.IsRemote(s) && !s.Reaction && Rules.Available(story, s, w)))
                ch5Remote.Add(s.Id);
            budgetWalk = Program.Walk(step, w).First(r => r.Has("nurah.trickster.accepted") || r.Has("nurah.trickster.cost.ghostwritten"));
        }
        foreach (var s in story.Scenes.Where(s => s.Relationship == "nurah" && Rules.IsRemote(s) && !s.Reaction && Rules.Available(story, s, Later(story, budgetWalk, 72))))
            ch5Remote.Add(s.Id);
        check(ch5Remote.Count <= 2, "The late runaway spends more than two Chapter 5 deliveries: " + string.Join(", ", ch5Remote));
        var lateRanSeen = Later(story, lateAccepted[0], 72);
        check(!Rules.Available(story, ranTerms, lateRanSeen), "The late runaway gets the in-person terms.");
        var lateRanEnd = Program.Copy(lateRanSeen); lateRanEnd.Chapter = 6; Rules.Complete(story, lateRanEnd);
        check(Rules.Available(story, epCommit, lateRanEnd), "The late runaway has no epilogue commit.");
        // R2-6 (Sol round 1): both late branches reach the Last Call coda on their late key; a refusal never does.
        var lcPage = S("nurah.lastcall.page");
        check(lcPage.RequiresAnyGroups.Length == 1 && lcPage.RequiresAnyGroups[0].SequenceEqual(new[] { "nurah.trickster.coda_alive" })
              && !lcPage.Requires.Contains("nurah.complete"), "The Last Call coda does not read her living commitment.");
        check(lateRanEnd.Has("nurah.trickster.coda_alive") && ending.Has("nurah.trickster.coda_alive") && !lateRanEnd.Has("nurah.complete"),
            "A late branch does not reach the coda key.");
        // Round 5 (INT): committed in the cell, then executed natively: no living coda; bought back: the coda again.
        var wedThenExecuted = World(story, 6, "trickster.ever", "nurah.complete", "nurah.trickster.released", "nurah.dead_drezen", "nurah.killing_mechanism");
        check(!wedThenExecuted.Has("nurah.trickster.coda_alive"), "An executed Nurah gets the Last Call coda.");
        var wedThenBought = Program.Copy(wedThenExecuted); wedThenBought.Flags.Add("nurah.trickster.returned"); Rules.Complete(story, wedThenBought);
        check(wedThenBought.Has("nurah.trickster.coda_alive")
              && World(story, 6, "trickster.ever", "nurah.complete", "nurah.prison").Has("nurah.trickster.coda_alive"), "A living committed Nurah loses the coda.");
        var refusedLate = Program.Walk(terms, deadSeen).First(r => r.Has("nurah.closed"));
        var refusedEnd = Program.Copy(refusedLate); refusedEnd.Chapter = 6; Rules.Complete(story, refusedEnd);
        check(!refusedEnd.Has("nurah.trickster.coda_alive") && !refusedEnd.Has("nurah.complete"), "A refusal reaches the coda key.");
        // Sol round 2 (TRK): proofs seen in the cell and then an execution never commit her, unless she is bought back.
        var executedAfterProofs = World(story, 6, "trickster.ever", "nurah.trickster.released", "nurah.trickster.accepted",
                                        "nurah.trickster.proofs_seen", "nurah.dead_drezen", "nurah.killing_mechanism");
        var epMargin = S("nurah.trickster.epilogue.the_margin");
        check(!executedAfterProofs.Has("nurah.trickster.late_committed") && !Rules.Available(story, epCommit, executedAfterProofs)
              && !Rules.Available(story, epRefused, World(story, 6, "trickster.ever", "nurah.trickster.proofs_seen", "nurah.closed", "nurah.dead_drezen")),
            "An executed Nurah is narrated alive without the bargain.");
        var boughtBack6 = World(story, 6, "trickster.ever", "nurah.trickster.proofs_seen", "nurah.dead_drezen", "nurah.killing_mechanism",
                                "nurah.trickster.returned");
        // Round 3 (INT): proofs with her terms never answered are a published book, not a romance; only the late branches,
        // which can never reach her in-person terms, commit on the page.
        var epUnanswered = S("nurah.trickster.epilogue.unanswered");
        var cell6 = World(story, 6, "trickster.ever", "nurah.prison", "nurah.trickster.released", "nurah.trickster.proofs_seen");
        foreach (var w in new[] { boughtBack6, cell6 })
            check(!w.Has("nurah.trickster.late_committed") && !Rules.Available(story, epCommit, w) && Rules.Available(story, epUnanswered, w),
                "Unanswered terms are decided as a romance.");
        check(!Rules.Available(story, epUnanswered, executedAfterProofs) && !Rules.Available(story, epUnanswered, ending),
            "The unanswered page plays for an executed Nurah or a late branch.");
        // Round 3 (CAN): no postwar reunion after an unsurvived sacrifice; a bereaved page instead; the return keeps it.
        var epBereaved = S("nurah.trickster.epilogue.bereaved");
        var lost = World(story, 6, "trickster.ever", "nurah.complete", "nurah.ran_off", "sacrifice");
        var back = World(story, 6, "trickster.ever", "nurah.complete", "nurah.ran_off", "sacrifice", "ending.trickster");
        check(!Rules.Available(story, epMargin, lost) && Rules.Available(story, epBereaved, lost)
              && Rules.Available(story, epMargin, back) && !Rules.Available(story, epBereaved, back), "The sacrifice reunites or mourns wrongly.");
        var lateLost = Program.Copy(ending); lateLost.Flags.Add("sacrifice"); Rules.Complete(story, lateLost);
        check(!Rules.Available(story, epCommit, lateLost) && Rules.Available(story, epBereaved, lateLost), "The late page survives the sacrifice.");
        // Round 3 (BEL): the byline paragraphs never contradict the co-author cover.
        var bylines = epMargin.Nodes[0].Paragraphs.Where(q => q.Text.Contains("The Commander's name appeared", StringComparison.Ordinal)).ToList();
        check(bylines.Count == 4 && bylines.Count(q => !q.Requires.Contains("nurah.trickster.cost.coauthor")) == 2
              && bylines.Where(q => !q.Requires.Contains("nurah.trickster.cost.coauthor")).All(q => q.Forbids.Contains("nurah.trickster.cost.coauthor")),
            "The first-page byline contradicts the co-author cover.");
        // Sol round 2 (INT): an in-play commitment has its own page, without Last Call; one publication date throughout.
        foreach (var w in new[] { World(story, 6, "trickster.ever", "nurah.complete", "nurah.trickster.released", "nurah.prison"),
                                  World(story, 6, "trickster.ever", "nurah.complete", "nurah.ran_off"),
                                  World(story, 6, "trickster.ever", "nurah.complete", "nurah.dead_drezen", "nurah.trickster.returned") })
            check(Rules.Available(story, epMargin, w) && !Rules.Available(story, epCommit, w) && !w.Has("trickster.lastcall.active"),
                "A committed Nurah has no page of her own.");
        check(!Rules.Available(story, epMargin, World(story, 6, "trickster.ever", "nurah.complete", "nurah.dead_drezen")),
            "The committed page narrates an executed Nurah.");
        check(epCommit.Nodes[0].Text.Contains("Two years after the Threshold", StringComparison.Ordinal)
              && epMargin.Nodes[0].Text.Contains("Two years after the Threshold", StringComparison.Ordinal)
              && S("nurah.lastcall.page").Nodes[0].Text.Contains("two years after Threshold", StringComparison.Ordinal),
            "Her book has two publication dates.");
        // Round 4 (CAN/VOI/BEL): each in-person terms scene remembers its own history; the parcel answers by post.
        foreach (var t in new[] { terms, ranTerms })
            check(!t.Nodes.Single(n => n.Id == "done").Text.Contains("pardon", StringComparison.Ordinal)
                  && !t.Nodes.Single(n => n.Id == "partners").Text.Contains("pardon", StringComparison.Ordinal)
                  && !t.Nodes.Single(n => n.Id == "done").Text.Contains("Say no", StringComparison.Ordinal), "A terms scene borrows another history: " + t.Id);
        check(terms.Nodes.Single(n => n.Id == "done").Text.Contains("killed", StringComparison.Ordinal)
              && ranTerms.Nodes.Single(n => n.Id == "done").Text.Contains("ran", StringComparison.Ordinal), "The raised and runaway propositions are the same speech.");
        check(proofs.Nodes.Single(n => n.Id == "trusted").Text.Contains("courier", StringComparison.Ordinal)
              && proofs.Nodes.Single(n => n.Id == "signed").Text.Contains("courier", StringComparison.Ordinal), "The parcel's answer is narrated in person.");
        var coPara = epMargin.Nodes[0].Paragraphs.Where(q => q.Requires.Contains("nurah.trickster.cost.coauthor")).ToList();
        check(coPara.Count(q => q.Text.Contains("The Commander's name appeared twice", StringComparison.Ordinal)) == 2
              && coPara.Any(q => q.Requires.Contains("nurah.trickster.cost.signed_proofs")) && coPara.Any(q => q.Forbids.Contains("nurah.trickster.cost.signed_proofs")),
            "Blank proofs followed by co-authorship claim a signature in the gap.");
        // Ramisa's call-in: a soul paid for in gold is no debt; the story (or the duplicate bill, sold on screen) is.
        var lcCall = S("nurah.lastcall.call");
        var owed = lcCall.RequiresAnyGroups.SelectMany(g => g).ToList();
        check(owed.Contains("nurah.trickster.cost.ramisa_audience") && owed.Contains("nurah.trickster.cost.bill_in_your_name")
              && !owed.Contains("nurah.trickster.cost.ramisa_fee"), "Paying Ramisa in gold still leaves a story owed.");
        var callChoices = lcCall.Nodes.Single().Choices;
        check(callChoices.Single(c => c.Requires.Contains("nurah.trickster.cost.ramisa_audience")).Set.All(f => f != "trickster.lastcall.nurah_story_sold")
              && callChoices.Single(c => c.Requires.Contains("nurah.trickster.cost.bill_in_your_name")).Set.Contains("trickster.lastcall.nurah_story_sold"),
            "The duplicate bill's call-in does not sell the story on screen.");
        // Primed in Chapter 3, released too late for the Chapter 3 reply: the Chapter 5 reply picks it up.
        var primedRan5 = World(story, 5, "trickster.ever", "nurah.ran_off", "nurah.trickster.primed", "nurah.trickster.cost.ghostwritten");
        check(!Rules.Available(story, reply, primedRan5) && Rules.Available(story, replyLate, primedRan5), "A Chapter 3 dedication has no Chapter 5 reply.");

        // Sol quality pass (TRK): the early dedication pays a printer only when the player chooses it; the reply tells which.
        var purse = dedication.Nodes.Single(n => n.Id == "write").Choices;
        check(purse.Count == 2 && purse[0].Crusade == null && !purse[0].Set.Contains("nurah.trickster.cost.printer_paid")
              && purse[1].Crusade?.Amount == -250 && purse[1].Set.Contains("nurah.trickster.cost.printer_paid"), "The printer's purse is not a choice.");
        var onePage = new HashSet<string>(); var paidPage = new HashSet<string>();
        Program.Walk(reply, ran, (page, _) => onePage.Add(page));
        var ranPaid = World(story, 3, "trickster", "trickster.ever", "nurah.ran_off", "nurah.trickster.primed", "nurah.trickster.cost.ghostwritten",
                            "nurah.trickster.cost.printer_paid");
        Program.Walk(reply, ranPaid, (page, _) => paidPage.Add(page));
        check(onePage.Contains("letter_one") && !onePage.Contains("letter") && paidPage.Contains("letter") && !paidPage.Contains("letter_one"),
            "The reply blames a printer nobody paid, or forgets the one who was.");
        var pedlarPages = new HashSet<string>();
        Program.Walk(reply, Later(story, bought, 48), (page, _) => pedlarPages.Add(page));
        check(pedlarPages.Contains("letter") && !pedlarPages.Contains("letter_one"), "The pedlar's paid printer is forgotten.");

        // Sol quality pass (CAN/INT): Chapter 5 cell twins, reached only through the unhidden actor at her cell.
        var cell5 = World(story, 5, "trickster", "trickster.ever", "nurah.prison");
        check(Rules.PresenceWanted(cellPresence, cell5) && !Rules.Available(story, lateCell[0], cell5), "The cell twin opens without her actor.");
        cell5.AvailableContacts.Add("f999fc37ddb225640b7f98c0a05d6948");
        check(Rules.Available(story, lateCell[0], cell5) && !Rules.Available(story, pardon, cell5), "Trk_Nurah_Prison5: the late pardon.");
        var pardoned5 = After(lateCell[0], cell5, "read", 0);
        check(pardoned5.Has("nurah.trickster.primed") && pardoned5.Has("nurah.trickster.cost.ledger_lie")
              && lateCell[0].Nodes.Single(n => n.Id == "read").Choices[0].Mythic == "PlayerIsTrickster", "The late pardon's flags or mark.");
        var night5 = Later(story, pardoned5, 24);
        check(Rules.Available(story, lateCell[1], night5) && !Rules.Available(story, night, night5), "The late night out.");
        var released5 = Later(story, After(lateCell[1], night5, "start", 0), 72);
        check(Rules.PresenceWanted(cellPresence, released5) && Rules.Available(story, lateCell[2], released5), "The late proofs.");
        var terms5 = Later(story, After(lateCell[2], released5, "start", 0), 72);
        check(Rules.Available(story, lateCell[3], terms5) && Commits(lateCell[3], terms5), "The late terms do not commit at the cell.");
        var recruited5 = World(story, 5, "trickster", "trickster.ever", "nurah.prison", "nurah.trickster_recruited");
        recruited5.AvailableContacts.Add("f999fc37ddb225640b7f98c0a05d6948");
        var r5 = new HashSet<string>();
        Program.Walk(lateCell[0], recruited5, (page, _) => r5.Add(page));
        check(r5.Contains("start_recruited") && !r5.Contains("start"), "The recruited pawn is greeted as a stranger in Chapter 5.");

        // Reactions: exactly Irabeth and Camellia; a dead reactor hides the line and nothing waits on it.
        var reactions = story.Scenes.Where(s => s.Relationship == "nurah" && s.Reaction).ToList();
        check(reactions.Count == 11 && reactions.All(s => s.Owner == "Irabeth" || s.Owner == "Camellia")
              && reactions.All(s => s.AnswerLists.Length == 1 || s.Remote && s.Id.Contains(".camellia_veiled_", StringComparison.Ordinal)),
            "Nurah reactions: wrong reactors or delivery.");
        // Sol quality pass (INT): a Camellia killed by the Commander and back on her own route is the veiled copy at Fye's, with no
        // companion hub, so her lines come as cards; a Camellia raised from a retained death keeps her companion-hub lines.
        var veiledSupper = World(story, 5, "trickster.ever", "nurah.dead_camellia", "nurah.dead_drezen", "nurah.trickster.returned",
                                 "nurah.trickster.larva_rumour", "camellia.killed", "camellia.trickster.returned");
        check(Rules.Available(story, S("nurah.trickster.react.camellia_veiled_supper"), veiledSupper)
              && !Rules.Available(story, S("nurah.trickster.react.camellia_supper"), veiledSupper)
              && !Rules.Available(story, S("nurah.trickster.react.camellia_veiled_market"), veiledSupper), "The veiled Camellia's supper card.");
        var raisedCamellia = World(story, 5, "trickster.ever", "nurah.dead_camellia", "nurah.dead_drezen", "nurah.trickster.returned",
                                   "nurah.trickster.larva_rumour", "camellia.dead", "camellia.trickster.returned");
        check(Rules.Available(story, S("nurah.trickster.react.camellia_supper"), raisedCamellia)
              && !Rules.Available(story, S("nurah.trickster.react.camellia_veiled_supper"), raisedCamellia), "The raised Camellia's supper line.");
        var plainSupper = World(story, 5, "trickster.ever", "nurah.dead_camellia", "nurah.dead_drezen", "nurah.trickster.returned", "nurah.trickster.larva_rumour");
        check(!Rules.Available(story, S("nurah.trickster.react.camellia_veiled_supper"), plainSupper), "A living Camellia sends a card.");
        foreach (var id in new[] { "pardon", "market", "supper", "draft" })
            check(S("nurah.trickster.react.camellia_veiled_" + id).Requires.Contains("camellia.killed")
                  && S("nurah.trickster.react.camellia_veiled_" + id).Requires.Contains("camellia.trickster.returned"), "A card without the veiled state: " + id);
        var raisedWorld = World(story, 5, "trickster.ever", "nurah.dead_drezen", "nurah.trickster.returned", "irabeth_dead");
        check(!Rules.Available(story, S("nurah.trickster.react.irabeth_raised"), raisedWorld), "A dead Irabeth reacts.");
        raisedWorld.Flags.Add("irabeth.trickster.returned");
        check(Rules.Available(story, S("nurah.trickster.react.irabeth_raised"), raisedWorld), "A returned Irabeth is silent.");
        var supper = World(story, 4, "trickster.ever", "nurah.dead_camellia", "nurah.dead_drezen", "nurah.trickster.returned", "nurah.trickster.larva_rumour");
        check(Rules.Available(story, S("nurah.trickster.react.camellia_supper"), supper) && !Rules.Available(story, S("nurah.trickster.react.camellia_market"), supper),
            "Camellia's supper variant is wrong.");
        foreach (var r in reactions)
            check(!r.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Set).Any(f => f.StartsWith("camellia.", StringComparison.Ordinal) || f.StartsWith("irabeth", StringComparison.Ordinal)),
                "A reaction touches its reactor's state: " + r.Id);

        // Coexistence (C8): no Nurah scene reads or closes another relationship's own state.
        foreach (var s in story.Scenes.Where(s => s.Id.StartsWith("nurah.trickster.", StringComparison.Ordinal)))
            check(!s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Set).Any(f => !f.StartsWith("nurah.", StringComparison.Ordinal)),
                "A Nurah scene sets another route's flag: " + s.Id);

        // G6: the registered visits are no longer held back by the flags her return lifted.
        var visits = story.Scenes.Where(s => s.Relationship == "nurah" && !s.Id.StartsWith("nurah.trickster.", StringComparison.Ordinal)).ToList();
        check(visits.Count > 0 && visits.Where(s => s.Forbids.Contains("nurah.prison")).All(s => s.ForbidOverrides["nurah.prison"] == "nurah.trickster.released")
              && visits.Where(s => s.Forbids.Contains("nurah.dead_drezen")).All(s => s.ForbidOverrides["nurah.dead_drezen"] == "nurah.trickster.returned"),
            "Registered Nurah visits lack their grief overrides.");

        // Not a Trickster: nothing opens.
        var plain = World(story, 3, "nurah.prison");
        check(!story.Scenes.Where(s => s.Id.StartsWith("nurah.trickster.", StringComparison.Ordinal)).Any(s => Rules.Available(story, s, plain)),
            "A Trickster Nurah scene opened on another path.");
    }
}
