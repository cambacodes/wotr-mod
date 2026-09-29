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
                  && p.Value.Unit == "f999fc37ddb225640b7f98c0a05d6948" && p.Value.At?.Locator == "7b94948a-1954-428f-82d0-94b2adcb1380")
              && Rules.PresencesExclusive(story.Presences["nurah.presence"], story.Presences["nurah.presence.raised"]),
            "Nurah presences malformed.");
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
        var ranSeen = Later(story, After(proofs, ran5, "proofs", 0), 72);
        check(Rules.Available(story, ranTerms, ranSeen) && !Rules.Available(story, terms, ranSeen) && Commits(ranTerms, ranSeen),
            "Trk_Nurah_RanOffTerms.");
        check(Rules.PresenceWanted(story.Presences["nurah.presence"], ranSeen) && !Rules.PresenceWanted(story.Presences["nurah.presence.raised"], ranSeen),
            "The runaway is not placed for her terms.");

        // Trk_Nurah_RanOffLate: the pedlar in Chapter 3; the commit falls to the epilogue page.
        var unprimed = World(story, 3, "trickster", "trickster.ever", "nurah.ran_off");
        check(Rules.Available(story, pedlar, unprimed) && !Rules.Available(story, reply, unprimed), "Trk_Nurah_RanOffLate: availability.");
        var bought = After(pedlar, unprimed, "start", 0);
        check(bought.Has("nurah.trickster.cost.late") && bought.Has("nurah.trickster.cost.ghostwritten"), "Trk_Nurah_RanOffLate: flags.");
        check(!Rules.Available(story, pedlar, World(story, 5, "trickster", "trickster.ever", "nurah.ran_off")), "The pedlar outside Chapter 3.");

        // Reactions: exactly Irabeth and Camellia; a dead reactor hides the line and nothing waits on it.
        var reactions = story.Scenes.Where(s => s.Relationship == "nurah" && s.Reaction).ToList();
        check(reactions.Count == 7 && reactions.All(s => s.Owner == "Irabeth" || s.Owner == "Camellia") && reactions.All(s => s.AnswerLists.Length == 1),
            "Nurah reactions: wrong reactors or delivery.");
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
