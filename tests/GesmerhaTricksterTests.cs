using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Gesmerha, Trickster (Writer/handoffs/trickster/gesmerha.md): the unfinished work (dead in the ambush, F04) and wrong
// footsteps (missed Chapter 3 window, F04). One block per spec rules test (Trk_Gesmerha_*), plus the shape of each hook,
// the epilogue pages and the registered-route edits.
internal static class GesmerhaTricksterTests
{
    private const string Unit = "3ba3a0ff8575be8419159221177c1411";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Wintersun = "0a5654e7dc18f074d9356009d55eb51b";
    private const string Smith = "15f754455d1d87c42a4e14df456d5415";
    private const string HerList = "dc306897f75a31c4aaf9483ebdff0585";
    private const string HerReturn = "05d66664080144c4bb8fc08b90cc700b";
    private const string P = "gesmerha.trickster.";

    private static Snapshot World(Story story, int chapter, string area, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = area, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Unit);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
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
        var commission = S(P + "dead.commission");
        var pyre = S(P + "dead.pyre");
        var payoff = S(P + "dead.unfinished_work");
        var yard = S(P + "returned.yard");
        var bench = S(P + "returned.bench");
        var secondAsk = S(P + "returned.second_ask");
        var home = S(P + "missed.wrong_footsteps_home");
        var capital = S(P + "missed.wrong_footsteps_capital");
        var pages = story.Scenes.Where(s => s.Id.StartsWith(P + "epilogue.", StringComparison.Ordinal)).ToArray();
        var own = story.Scenes.Where(s => s.Id.StartsWith(P, StringComparison.Ordinal) && !s.Reaction && !pages.Contains(s)).ToArray();
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));
        List<Snapshot> Play(Scene scene, Snapshot w) => Program.Walk(scene, w).Where(r => r.Has(scene.Id)).ToList();
        Snapshot Pick(Scene scene, Snapshot w, params string[] flags)
        {
            var hit = Play(scene, w).Where(r => flags.All(r.Has))
                .OrderBy(r => !flags.Contains("gesmerha.closed") && r.Has("gesmerha.closed") ? 1 : 0).FirstOrDefault();
            check(hit != null, "No outcome of " + scene.Id + " sets " + string.Join(", ", flags));
            return hit ?? w;
        }
        HashSet<string> Pages(Scene scene, Snapshot w)
        {
            var seen = new HashSet<string>();
            foreach (var r in Program.Walk(scene, w, (id, _) => seen.Add(id))) { }
            return seen;
        }
        IEnumerable<Choice> Choices(Scene scene) => scene.Nodes.SelectMany(n => n.Choices);

        // Shape and hooks.
        check(commission.NativeReturnCue == HerReturn && commission.AnswerLists.SequenceEqual(new[] { HerList })
              && commission.ContactUnit == null && !Rules.IsRemote(commission) && commission.Chapters.SequenceEqual(new[] { 3 })
              && commission.EntryMythic == "PlayerIsTrickster" && commission.RequiresAnyGroups.Length == 1
              && commission.RequiresAnyGroups[0].SequenceEqual(new[] { "gesmerha.feared_hands", "gesmerha.took_risk" }),
            "The commission is not an inline Trickster answer on her own hub before the ambush.");
        // The entry is keyed to her own foresight: SeenCues set when she speaks Cue_0028 or Cue_0024, so the offer appears
        // on AnswersList_0008 only after she has said what Marhevok will take next.
        check(story.SeenCues["gesmerha.feared_hands"].SequenceEqual(new[] { "13f2b37e28864ba4b882d13fad90f7c5" })
              && story.SeenCues["gesmerha.took_risk"].SequenceEqual(new[] { "0448dab10df819c43a2f2aa86524f01b" })
              && story.SeenCues["gesmerha.met"].SequenceEqual(new[] { "1e9af5965b5da304c825817c89817c22" }),
            "The commission and the footsteps are not keyed to her own spoken cues.");
        var purse = commission.Nodes.Single(n => n.Id == "start").Choices[0];
        check(purse.Crusade?.Resource == "Finances" && purse.Crusade.Amount == -150 && purse.Alignment?.Direction == "Chaotic"
              && purse.Set.Contains(P + "primed") && purse.Set.Contains(P + "commissioned") && purse.Set.Contains(P + "cost.advance_paid"),
            "The advance is not paid for on the choice that plants it.");
        check(purse.Text.Contains("coin into the block") && commission.Nodes.Single(n => n.Id == "took").Text.Contains("coin goes into the birch"),
            "The commission plants nothing on her bench.");
        check(Rules.IsRemote(pyre) && pyre.Chapters.SequenceEqual(new[] { 3 }) && pyre.TricksterDevice && pyre.TricksterState == "dead"
              && pyre.Requires.Contains("trickster") && pyre.Requires.Contains("gesmerha.dead.latched"),
            "The pyre is not the live Trickster's Chapter 3 letter.");
        var toast = pyre.Nodes[0].Choices[0];
        check(toast.Mythic == "PlayerIsTrickster" && toast.Crusade?.Resource == "Finances" && toast.Crusade.Amount == -300
              && toast.Alignment?.Direction == "Chaotic", "The pyre's purse is not the dearer Trickster act.");
        check(Rules.IsRemote(payoff) && payoff.Chapters.SequenceEqual(new[] { 3, 5 }) && payoff.TricksterDevice
              && payoff.Requires.Contains("trickster.ever") && !payoff.Requires.Contains("trickster"),
            "The payoff is not a letter that outlives a lost path.");
        foreach (var s in new[] { yard, bench, secondAsk })
            check(s.ContactUnit == Unit && s.Areas.SequenceEqual(new[] { Drezen }) && s.InteractionHub == "gesmerha.presence"
                  && !Rules.IsRemote(s) && s.Chapters.SequenceEqual(new[] { 3, 5 }),
                "The returned Gesmerha is not met in person in the smith's yard: " + s.Id);
        var presence = story.Presences["gesmerha.presence"];
        check(presence.Unit == Unit && presence.Area == Drezen && presence.Mode == "spawn-copy" && presence.Dialog == "hub"
              && presence.At?.NearUnit == Smith && presence.MinChapter == 3 && presence.MaxChapter == 5,
            "The presence is not her copy beside the Drezen smith.");
        check(home.AnswerLists.SequenceEqual(new[] { "2063ee21356b772408f5c9cfb3ed5bd0" }) && home.Areas.SequenceEqual(new[] { Wintersun })
              && capital.AnswerLists.SequenceEqual(new[] { "fb3a88e8ed751214c9136f87891ec07b" }) && capital.Areas.SequenceEqual(new[] { Drezen })
              && home.EntryMythic == "PlayerIsTrickster" && capital.EntryMythic == "PlayerIsTrickster"
              && home.NativeReturnCue == null && capital.Requires.Contains("gesmerha.capital_guest"),
            "The wrong footsteps are not on her Wintersun and Drezen lists.");
        check(story.Relationships["gesmerha"].UnavailableOverrides["gesmerha.dead"] == P + "returned",
            "A return does not lift her death.");
        foreach (var s in own)
            foreach (var key in s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(x => x)))
                check(!key.StartsWith("soana.", StringComparison.Ordinal) && !key.StartsWith("jerribeth.", StringComparison.Ordinal),
                    "Gesmerha reads another relationship's fate: " + s.Id + " " + key);

        // Trk_Gesmerha_Commission: planted on her own hub, before the ambush, on her own foresight.
        var risk = World(story, 3, Wintersun, "trickster", "gesmerha.took_risk");
        check(Rules.Available(story, commission, risk), "Trk_Gesmerha_Commission: the braver branch cannot pay in advance.");
        check(Rules.Available(story, commission, World(story, 3, Wintersun, "trickster", "gesmerha.feared_hands")),
            "Trk_Gesmerha_Commission: her fear of losing her hands does not open the commission.");
        check(!Rules.Available(story, commission, World(story, 3, Wintersun, "trickster")),
            "The commission opens before she has said what Marhevok will take.");
        var paid = Pick(commission, risk, P + "primed", P + "commissioned", P + "cost.advance_paid");
        check(!Rules.Available(story, commission, paid), "The commission is paid twice.");
        check(!Rules.Available(story, commission, World(story, 3, Wintersun, "trickster", "gesmerha.took_risk", "gesmerha.dead")),
            "A dead woman is offered a commission.");
        check(!Rules.Available(story, commission, World(story, 3, Wintersun, "trickster.ever", "gesmerha.took_risk")),
            "The commission is a new trick and needs the live path.");

        // Trk_Gesmerha_DeadPrimed: the ambush played as canon; the letter from Wintersun.
        var primed = World(story, 3, Wintersun, "trickster", "trickster.ever", "gesmerha.dead", "gesmerha.dead.latched",
            P + "primed", P + "commissioned", P + "cost.advance_paid");
        check(Rules.Available(story, payoff, primed) && !Any(primed, pyre, home, capital),
            "Trk_Gesmerha_DeadPrimed: the payoff is shut, or the pyre or the footsteps open.");
        var paidPages = Pages(payoff, primed);
        check(paidPages.Contains("paid") && paidPages.Contains("terms") && !paidPages.Contains("late") && !paidPages.Contains("terms_raised"),
            "Trk_Gesmerha_DeadPrimed: the paid letter reads as the pyre's.");
        var back = Pick(payoff, primed, P + "returned", P + "cost.ancestor_debt", "gesmerha.started");
        check(Play(payoff, primed).Any(r => r.Has("gesmerha.closed") && !r.Has(P + "returned")), "The letter cannot be answered with no.");
        check(Choices(payoff).Where(c => c.Set.Contains(P + "returned")).All(c => !c.Set.Contains("gesmerha.committed")),
            "The return commits.");
        var inDrezen = Program.Copy(back); inDrezen.Area = Drezen;
        check(Rules.Available(story, yard, Later(story, inDrezen, 24)) && !Rules.Available(story, yard, Later(story, inDrezen, 23)),
            "Trk_Gesmerha_DeadPrimed: the yard ignores its day.");

        // Trk_Gesmerha_DeadLate: no primer; the pyre, dearer.
        var late = World(story, 3, Wintersun, "trickster", "trickster.ever", "gesmerha.dead", "gesmerha.dead.latched");
        check(Rules.Available(story, pyre, late) && !Rules.Available(story, payoff, late),
            "Trk_Gesmerha_DeadLate: the pyre is shut, or the payoff opens unprimed.");
        var burned = Pick(pyre, late, P + "primed", P + "cost.late", P + "cost.laughed_at_grave");
        check(!Rules.Available(story, pyre, burned), "The pyre is paid twice.");
        check(Rules.Available(story, payoff, Later(story, burned, 72)) && !Rules.Available(story, payoff, Later(story, burned, 71)),
            "Trk_Gesmerha_DeadLate: the payoff ignores its three days.");
        var latePages = Pages(payoff, Later(story, burned, 72));
        check(latePages.Contains("late") && latePages.Contains("terms_raised") && !latePages.Contains("paid"),
            "Trk_Gesmerha_DeadLate: the ancestors do not raise their price for a bargain struck over ashes.");
        var closedAtPyre = Pick(pyre, late, "gesmerha.closed");
        check(!Rules.Available(story, payoff, Later(story, closedAtPyre, 100)), "Owing her nothing still raises her.");
        check(!Rules.Available(story, pyre, World(story, 5, Drezen, "trickster", "trickster.ever", "gesmerha.dead", "gesmerha.dead.latched")),
            "The pyre burns in Chapter 5, after Wintersun is gone.");

        // Trk_Gesmerha_DeadAfterFailure: a lost path loses the new trick; canon stands.
        check(!Any(World(story, 3, Wintersun, "trickster.ever", "trickster.failed", "gesmerha.dead", "gesmerha.dead.latched"), pyre, payoff),
            "Trk_Gesmerha_DeadAfterFailure: an unprimed lost path still raises her.");
        check(Rules.Available(story, payoff, World(story, 5, Drezen, "trickster.ever", "trickster.failed", "gesmerha.dead",
              "gesmerha.dead.latched", P + "primed")), "A primer paid as a Trickster stops paying out after a lost path (ledger 18).");

        // Trk_Gesmerha_Yard: the middle beat and her test.
        var returned = World(story, 5, Drezen, "trickster.ever", "gesmerha.dead", "gesmerha.dead.latched", P + "returned");
        check(Rules.Available(story, yard, returned) && !Rules.Available(story, bench, returned),
            "Trk_Gesmerha_Yard: the yard is shut, or the bench skips it.");
        var away = Program.Copy(returned); away.Area = Wintersun;
        check(!Rules.Available(story, yard, away), "The returned carver is met away from the smith's yard.");
        var yardPages = Pages(yard, returned);
        check(yardPages.IsSupersetOf(new[] { "start", "hold", "pulled", "after", "not_yet" }) && !yardPages.Contains("lie_first"),
            "Trk_Gesmerha_Yard: a page of the yard is unreachable, or the late price applies to a paid-in-advance return.");
        var lateBack = World(story, 5, Drezen, "trickster.ever", "gesmerha.dead", "gesmerha.dead.latched", P + "returned", P + "cost.late");
        check(Pages(yard, lateBack).Contains("lie_first") && Play(yard, lateBack).All(r => !r.Has(P + "statue_new")),
            "A carver bought at her pyre may still carve something new before the lie comes down.");
        var seen = Pick(yard, returned, P + "yard_seen", P + "statue_true", P + "held_still");
        var seenNew = Pick(yard, returned, P + "yard_seen", P + "statue_new", P + "held_still");
        var flinched = Pick(yard, returned, P + "yard_seen", P + "cost.flinched");
        check(Rules.Available(story, bench, Later(story, seen, 72)) && !Rules.Available(story, bench, Later(story, seen, 71)),
            "Trk_Gesmerha_Yard: the bench ignores its three days.");
        check(!Rules.Available(story, yard, seen), "The yard repeats.");

        // Trk_Gesmerha_Commit: her terms, then the night and the morning.
        var atBench = Later(story, seen, 72);
        var committed = Pick(bench, atBench, "gesmerha.committed");
        var benchPages = Pages(bench, atBench);
        check(benchPages.IsSupersetOf(new[] { "start", "monster", "ask", "terms", "postpone", "night", "morning" })
              && !benchPages.Contains("new") && !benchPages.Contains("flinch"),
            "Trk_Gesmerha_Commit: a page of the bench is unreachable, or the wrong statue stands on the trestles.");
        check(Pages(bench, Later(story, seenNew, 72)).Contains("new"), "The new figure never stands on the trestles.");
        check(!Rules.Available(story, bench, committed) && !Rules.Available(story, secondAsk, Later(story, committed, 200)),
            "The bench or the second ask repeats after the commit.");
        check(Choices(bench).Where(c => c.Set.Contains("gesmerha.committed")).All(c => c.Crusade == null),
            "She is paid for the commit.");

        // Trk_Gesmerha_Declined: her soft no, then the one priced second ask.
        var declined = Pick(bench, atBench, P + "declined");
        check(!declined.Has("gesmerha.committed") && !declined.Has("gesmerha.closed"), "Trk_Gesmerha_Declined: her no closes or commits.");
        check(Rules.Available(story, secondAsk, Later(story, declined, 96)) && !Rules.Available(story, secondAsk, Later(story, declined, 95))
              && !Rules.Available(story, bench, Later(story, declined, 96)),
            "Trk_Gesmerha_Declined: the second ask ignores its days, or the bench repeats.");
        var sat = Pick(secondAsk, Later(story, declined, 96), "gesmerha.committed", P + "cost.hands_carved");
        check(Choices(secondAsk).Any(c => c.Crusade?.Resource == "Favors" && c.Crusade.Amount == -100 && c.Set.Contains("gesmerha.committed")),
            "The second ask costs the war nothing.");
        check(Play(secondAsk, Later(story, declined, 96)).Any(r => r.Has("gesmerha.closed") && !r.Has("gesmerha.committed")),
            "The Commander cannot refuse her raised price.");
        check(Pages(secondAsk, Later(story, declined, 96)).IsSupersetOf(new[] { "sat", "night", "morning" }),
            "The second ask skips the three days or the night.");
        var finished = Pick(bench, atBench, "gesmerha.closed");
        check(!finished.Has("gesmerha.committed"), "The Commander's own no commits.");

        // Trk_Gesmerha_Flinched: a Commander who pulled away is refused outright.
        var atFlinch = Later(story, flinched, 72);
        check(Play(bench, atFlinch).All(r => !r.Has("gesmerha.committed")) && Pages(bench, atFlinch).Contains("flinch")
              && !Pages(bench, atFlinch).Contains("terms"),
            "Trk_Gesmerha_Flinched: she commits to someone who flinched.");
        var flinchNo = Pick(bench, atFlinch, P + "declined");
        check(Pages(secondAsk, Later(story, flinchNo, 96)).Contains("price_flinched"), "The second ask forgets the flinch.");

        // Trk_Gesmerha_EpilogueCommit and the other pages: one page per history.
        Snapshot End(Snapshot s) { var e = Program.Copy(s); e.Chapter = 6; Rules.Complete(story, e); return e; }
        string[] Endings(Snapshot s) => pages.Where(x => Rules.Available(story, x, End(s))).Select(x => x.Id).ToArray();
        check(Endings(committed).SequenceEqual(new[] { P + "epilogue.bench" }), "The commit ends on the wrong pages: " + string.Join(",", Endings(committed)));
        check(Endings(sat).SequenceEqual(new[] { P + "epilogue.bench" }), "The second ask ends on the wrong pages.");
        check(Endings(seen).SequenceEqual(new[] { P + "epilogue.commit" }), "Trk_Gesmerha_EpilogueCommit: a finished yard has no late commit page.");
        var failed = Program.Copy(returned); failed.Flags.Add("gesmerha.presence.failed"); Rules.Complete(story, failed);
        check(Endings(failed).SequenceEqual(new[] { P + "epilogue.commit" }), "A failed presence has no late commit page.");
        check(Endings(declined).SequenceEqual(new[] { P + "epilogue.refusal" }), "Her refusal ends on the wrong pages.");
        check(Endings(finished).SequenceEqual(new[] { P + "epilogue.finished" }), "The Commander's no ends on the wrong pages.");
        check(Endings(returned).SequenceEqual(new[] { P + "epilogue.unvisited" }), "A return never visited has no page.");
        foreach (var page in pages)
            check(page.Nodes.SelectMany(n => n.Choices).All(c => c.Mythic == null && c.Alignment == null && c.Crusade == null && c.Set.Length == 0),
                "An epilogue page carries effects: " + page.Id);
        foreach (var loss in new[] { "gesmerha.ending_loss", "gesmerha.late_ending_loss" })
            check(S(loss).Forbids.Contains(P + "returned"), "A returned Gesmerha is mourned: " + loss);
        var lifted = story.Scenes.Where(s => s.Relationship == "gesmerha" && !s.Id.StartsWith(P, StringComparison.Ordinal)
                                             && s.Forbids.Contains("gesmerha.dead")).ToArray();
        check(lifted.Length == 34 && lifted.All(s => s.ForbidOverrides.TryGetValue("gesmerha.dead", out var f) && f == P + "returned"),
            "G6: the registered scenes that Forbid her death are not all lifted by her return (" + lifted.Length + ").");
        foreach (var name in new[] { "gesmerha.ending_living_reunion", "gesmerha.late_ending_lovers" })
            check(S(name).Nodes.SelectMany(n => n.Paragraphs).Count(x => x.Requires.Contains(P + "commissioned")) == 1,
                "The commission leaves no mark on a living ending: " + name);

        // Trk_Gesmerha_Missed: the claimed afternoons, caught and played.
        var missed = World(story, 5, Wintersun, "trickster", "trickster.ever", "gesmerha.wintersun_resolved", "gesmerha.truth", "gesmerha.met");
        check(Rules.Available(story, home, missed) && !Rules.Available(story, payoff, missed) && !Rules.Available(story, capital, missed),
            "Trk_Gesmerha_Missed: the footsteps are shut at home, or the payoff or the capital opens.");
        check(!Rules.Available(story, home, World(story, 5, Wintersun, "trickster", "trickster.ever", "gesmerha.wintersun_resolved", "gesmerha.truth")),
            "The footsteps are claimed without the one native meeting.");
        var played = Pick(home, missed, "gesmerha.campaign_kept", P + "cost.catchup", P + "cost.campaign_slow");
        check(Play(home, missed).Any(r => r.Has("gesmerha.campaign_kept") && r.Has(P + "cost.catchup") && !r.Has(P + "cost.campaign_slow")),
            "The honest answer is charged as the trick.");
        check(Choices(home).Any(c => c.Crusade?.Resource == "Finances" && c.Crusade.Amount == -50 && c.Set.Contains(P + "cost.campaign_slow")),
            "The loser does not pay for the pieces.");
        var guest = World(story, 5, Drezen, "trickster", "trickster.ever", "gesmerha.wintersun_resolved", "gesmerha.illusions",
            "gesmerha.met", "gesmerha.capital_guest");
        check(Rules.Available(story, capital, guest), "Trk_Gesmerha_Missed: the capital guest cannot be told the lie.");
        var playedGuest = Program.Copy(played); playedGuest.Area = Drezen; playedGuest.Flags.Add("gesmerha.capital_guest");
        check(!Rules.Available(story, capital, playedGuest), "The unfinished game is played twice.");
        check(!Rules.Available(story, home, World(story, 5, Wintersun, "trickster.ever", "trickster.failed", "gesmerha.wintersun_resolved",
              "gesmerha.truth", "gesmerha.met")), "A lost path still claims the afternoons.");
        var registered = S("gesmerha.the_things_still_here");
        var visit = Later(story, played, 24); visit.Flags.Add("gesmerha.post_resolution_contact"); Rules.Complete(story, visit);
        check(Rules.Available(story, registered, visit), "The claimed afternoons do not open the registered late chain.");
        var visitPages = Pages(registered, visit);
        check(visitPages.Contains("catchup") && !visitPages.Contains("without_court"),
            "The registered first visit forgets that the afternoons were claimed, not kept.");

        // Reactions: exactly Ulbrig, Lann and Anevia, each with its availability guard.
        var reactions = story.Scenes.Where(s => s.Reaction && s.Id.StartsWith(P, StringComparison.Ordinal)).ToArray();
        check(reactions.Length == 7 && reactions.Select(r => r.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Anevia", "Lann", "Ulbrig" }),
            "The reactors are not exactly Ulbrig, Lann and Anevia.");
        // Sol 2026-09-30 (BEL): the footsteps reactions tell the branch actually played. The trick (she caught the lie; the
        // Commander knew one rule and paid for the pieces as the loser) and the confession (the lie owned before the game).
        var honestResult = Play(home, missed).First(r => r.Has(P + "cost.catchup") && !r.Has(P + "cost.campaign_slow"));
        Snapshot Camp(Snapshot s) { var w = Later(story, s, 24); w.Area = Drezen; w.Flags.Add("lann.in_party"); Rules.Complete(story, w); return w; }
        var trickReact = new[] { S(P + "react.lann_footsteps"), S(P + "react.anevia_footsteps") };
        var honestReact = new[] { S(P + "react.lann_confessed"), S(P + "react.anevia_confessed") };
        check(trickReact.All(r => Rules.Available(story, r, Camp(played))) && !honestReact.Any(r => Rules.Available(story, r, Camp(played))),
            "The trick branch hears the confession's reaction, or loses its own.");
        check(honestReact.All(r => Rules.Available(story, r, Camp(honestResult))) && !trickReact.Any(r => Rules.Available(story, r, Camp(honestResult))),
            "The confession branch hears the trick's reaction, or loses its own.");
        check(trickReact.Concat(honestReact).All(r => !r.Nodes[0].Text.Contains("beat her")),
            "A reaction invents a win the Commander never had.");
        check(honestReact[0].Nodes[0].Text.Contains("took it back") && honestReact[1].Nodes[0].Text.Contains("owned up")
              && trickReact[0].Nodes[0].Text.Contains("paid for the pieces"),
            "A footsteps reaction does not match its branch.");

        // Sol 2026-09-30 (COX): the second work. The ancestors' commission is finished on the bench before Threshold; the
        // Commander's face, begun the morning after, is the work Last Call collects, in the state the player left it.
        var likeness = S(P + "returned.likeness");
        check(likeness.ContactUnit == Unit && likeness.InteractionHub == "gesmerha.presence" && likeness.Areas.SequenceEqual(new[] { Drezen }),
            "The second work is not in the smith's yard.");
        check(!Rules.Available(story, likeness, committed) && Rules.Available(story, likeness, Later(story, committed, 48))
              && Rules.Available(story, likeness, Later(story, sat, 48)) && !Rules.Available(story, likeness, Later(story, declined, 200)),
            "The second work ignores its two days, or opens without the commit.");
        var owed = Pick(likeness, Later(story, committed, 48), P + "cost.likeness_owed");
        var cutFromMemory = Pick(likeness, Later(story, committed, 48), P + "cost.likeness_cut");
        check(!owed.Has(P + "cost.likeness_cut") && !cutFromMemory.Has(P + "cost.likeness_owed") && !Rules.Available(story, likeness, Later(story, owed, 48)),
            "The second work repeats, or leaves both states at once.");
        check(Choices(likeness).All(c => c.Crusade == null), "The unpaid face is paid for.");
        check(bench.Nodes.Where(n => n.Id == "monster" || n.Id == "new").All(n => n.Text.Contains("It is finished.")),
            "The ancestors' commission is not finished on the bench before Threshold.");

        // Last Call and the ordinary pages describe one history: the face, never the finished statue, in wood, never stone.
        var lcPage = S("gesmerha.lastcall.page");
        var lcCall = S("gesmerha.lastcall.call");
        Paragraph[] LcVisible(Snapshot s)
        {
            var e = End(s); e.Flags.UnionWith(new[] { "lastcall.active", "gesmerha.lastcall.called" });
            if (e.Has(P + "returned")) e.Flags.Add(P + "cost.ancestor_debt");   // the letter's answer sets both (the fixtures start at returned)
            Rules.Complete(story, e);
            check(Rules.Available(story, lcPage, e), "The Last Call coda does not play for a committed carver.");
            return Rules.VisibleParagraphs(lcPage.Nodes[0], e);
        }
        check(!lcPage.Nodes[0].Text.Contains("statue") && !lcPage.Nodes[0].Text.Contains("stone")
              && lcPage.Nodes[0].Paragraphs.All(x => !x.Text.Contains("stone")) && !lcCall.Nodes[0].Text.Contains("stone") && !lcCall.Entry.Contains("paid for"),
            "Last Call turns the wood to stone, or re-finishes the finished commission.");
        foreach (var (lcState, lcFlag) in new[] { (owed, "likeness_owed"), (cutFromMemory, "likeness_cut"), (committed, "ancestor_debt"), (sat, "ancestor_debt") })
        {
            var faces = LcVisible(lcState).Where(x => x.Text.Contains("face")).ToArray();
            check(faces.Length == 1 && faces[0].Requires.Contains(P + "cost." + lcFlag),
                "Last Call tells the Commander's face in the wrong state (" + lcFlag + "): " + faces.Length);
            check(LcVisible(lcState).All(x => !x.Requires.Contains(P + "cost.advance_paid")), "Last Call retells the Wintersun advance for a returned carver.");
        }
        foreach (var statue in new[] { seen, seenNew })
        {
            var s2 = Pick(bench, Later(story, statue, 72), "gesmerha.committed");
            check(LcVisible(s2).Count(x => x.Text.Contains("face")) == 1 && LcVisible(s2).All(x => !x.Text.Contains("statue")),
                "Last Call assumes a statue the Commander did not choose.");
        }
        // A living carver who took the advance in Wintersun and committed on the registered route: the birch waits years.
        var livingPaid = World(story, 6, Wintersun, "trickster.ever", "gesmerha.campaign_kept", "gesmerha.committed", "gesmerha.lover",
            "gesmerha.reunion_kept", P + "commissioned", P + "cost.advance_paid");
        var livingLc = LcVisible(livingPaid);
        check(livingLc.Count(x => x.Text.Contains("birch")) == 1 && livingLc.All(x => !x.Text.Contains("face")),
            "Last Call contradicts the living commission.");
        check(S("gesmerha.ending_living_reunion").Nodes.SelectMany(n => n.Paragraphs).Any(x => x.Requires.Contains(P + "commissioned") && x.Text.Contains("birch")),
            "The living ending carves the Wintersun commission in another wood.");

        // Sol 2026-09-30 (INT): the native Trickster survival after the sacrifice (trickster.commander_back) keeps the living
        // endings and retires both mourning pages; a genuine sacrifice still mourns; a Last Call survivor is not mourned either.
        var living = story.Scenes.Where(s => s.Relationship == "gesmerha" && s.Owner == "Epilogue"
                                             && (s.Id.StartsWith("gesmerha.ending_", StringComparison.Ordinal) || s.Id.StartsWith("gesmerha.late_ending_", StringComparison.Ordinal))).ToArray();
        string[] Living(params string[] flags)
        {
            var w = World(story, 6, Wintersun, flags);
            return living.Where(s => Rules.Available(story, s, w)).Select(s => s.Id).ToArray();
        }
        string[] early = { "gesmerha.campaign_kept", "gesmerha.lover", "gesmerha.committed", "gesmerha.reunion_kept" };
        string[] lateLove = { "gesmerha.campaign_kept", "gesmerha.late_arrived", "gesmerha.late_complete", "gesmerha.future_lovers", "gesmerha.committed" };
        string[] lateOpen = { "gesmerha.campaign_kept", "gesmerha.late_arrived" };
        foreach (var key in new[] { "ending.trickster", "ending.trickster_full", "ending.trickster_allplanes", "ending.trickster_allplanes_fw" })
        {
            var native = new[] { "sacrifice", "trickster.ever", key };
            check(Living(early.Concat(native).ToArray()).SequenceEqual(new[] { "gesmerha.ending_living_reunion" }),
                "A native Trickster survivor is mourned (early route): " + key);
            check(Living(lateLove.Concat(native).ToArray()).SequenceEqual(new[] { "gesmerha.late_ending_lovers" }),
                "A native Trickster survivor is mourned (late route): " + key);
            check(Living(lateOpen.Concat(native).ToArray()).SequenceEqual(new[] { "gesmerha.late_ending_unfinished" }),
                "A native Trickster survivor loses the unfinished page: " + key);
        }
        check(Living(early.Concat(new[] { "sacrifice" }).ToArray()).SequenceEqual(new[] { "gesmerha.ending_sacrifice" })
              && Living(lateLove.Concat(new[] { "sacrifice" }).ToArray()).SequenceEqual(new[] { "gesmerha.late_ending_sacrifice" }),
            "A genuine sacrifice is no longer mourned.");
        check(Living(lateLove.Concat(new[] { "sacrifice", "trickster.ever", "trickster.lastcall.taken", "ending.wound_closed",
                                              "trickster.lastcall.pillar.bottle" }).ToArray()).SequenceEqual(new[] { "gesmerha.late_ending_lovers" }),
            "A Last Call survivor is mourned beside the Last Call coda.");

        // The living route's intimacy (Sol 2026-09-30, BEL/VOI): the cut lands on the initiating motion and the aftermath is
        // its own page; each night has a named companion's reaction.
        var asks = S("gesmerha.what_she_asks");
        var room = S("gesmerha.the_room_she_chose");
        foreach (var (sc, cut, after) in new[] { (asks, "private", "after_private"), (room, "night", "after_night"), (room, "first_night", "after_first_night") })
        {
            var beat = sc.Nodes.Single(x => x.Id == cut);
            check(beat.Choices.Count == 1 && beat.Choices[0].Next == after && !beat.Text.Contains("Later"),
                "An intimate beat fades early or carries its own aftermath: " + sc.Id + "/" + cut);
            check(!beat.Text.Contains("May I") && !beat.Text.Contains("Ask me when"), "Consent choreography in " + sc.Id + "/" + cut);
        }
        check(room.Nodes.Single(x => x.Id == "first_kiss").Choices.Any(c => c.Next == "first_night")
              && room.Nodes.Single(x => x.Id == "after_first_night").Choices[0].Set.Contains("gesmerha.committed"),
            "The late commit has no threshold of its own.");
        var afternoonReact = S("gesmerha.react.lann_afternoon");
        var nightReact = S("gesmerha.react.ulbrig_night");
        check(afternoonReact.Reaction && afternoonReact.Requires.Contains("gesmerha.afternoon_shared") && afternoonReact.Requires.Contains("lann.in_party")
              && nightReact.Reaction && nightReact.Requires.Contains("gesmerha.night_shared") && nightReact.Requires.Contains("ulbrig.in_party"),
            "The living route's nights have no named companion reaction.");
        check(asks.Nodes.Single(x => x.Id == "road_private").Choices[0].Set.Contains("gesmerha.afternoon_shared")
              && room.Nodes.Single(x => x.Id == "after_night").Choices[0].Set.Contains("gesmerha.night_shared")
              && new[] { "private", "after_private" }.All(id => asks.Nodes.Single(x => x.Id == id).Choices.All(c => c.Set.Length == 0))
              && new[] { "night", "first_night" }.All(id => room.Nodes.Single(x => x.Id == id).Choices.All(c => c.Set.Length == 0)),
            "The companion reactions read a night nobody records.");
        foreach (var r in reactions.Where(r => r.Owner == "Lann"))
            check(r.Requires.Contains("lann.in_party") && r.Forbids.Contains("lann.dead") && r.Forbids.Contains("lann.kicked_out"),
                "Lann speaks when he is not with the Commander: " + r.Id);
        foreach (var r in reactions.Where(r => r.Owner == "Ulbrig"))
            check(r.Requires.Contains("ulbrig.in_party") && r.Forbids.Contains("ulbrig.dead") && r.Forbids.Contains("ulbrig.kicked_out"),
                "Ulbrig speaks when he is not with the Commander: " + r.Id);
        foreach (var r in reactions.Where(r => r.Owner == "Anevia"))
            check(r.Forbids.Contains("anevia_gone") && r.Forbids.Contains("anevia_dead"), "Anevia speaks after she is gone: " + r.Id);

        // Sol round 1 (HOW/INT): the returned carver's contact is her spawned copy, so derive it from the presence lifecycle
        // (PresenceWanted, PlanPresence) instead of granting it, and open the post-commit scene the way the runtime does.
        var presenceSpec = story.Presences["gesmerha.presence"];
        Snapshot Hub(Snapshot s)
        {
            var w = Program.Copy(s);
            w.AvailableContacts.Remove(Unit);
            bool wanted = Rules.PresenceWanted(presenceSpec, w);
            var spawn = Rules.PlanPresence(presenceSpec, wanted, new PresenceObservation { AreaLoaded = true });
            var kept = Rules.PlanPresence(presenceSpec, wanted, new PresenceObservation { AreaLoaded = true, CopyFound = true, CopyAlive = true, Recorded = true, Submitted = true });
            if (wanted && spawn.SequenceEqual(new[] { PresenceStep.Spawn }) && kept.Length == 0) w.AvailableContacts.Add(Unit);
            return w;
        }
        foreach (var (commitState, label) in new[] { (committed, "the vow"), (sat, "the sitting") })
        {
            var after48 = Hub(Later(story, commitState, 48));
            check(Rules.PresenceWanted(presenceSpec, after48) && after48.AvailableContacts.Contains(Unit),
                "The presence is removed after the commit (" + label + ").");
            check(Rules.Available(story, likeness, after48)
                  && story.Scenes.Any(s => s.InteractionHub == "gesmerha.presence" && Rules.Available(story, s, after48)),
                "The second work cannot be opened through her hub after " + label + ".");
            var afterFace = Hub(Later(story, Pick(likeness, after48, P + "cost.likeness_owed"), 1));
            check(Rules.PresenceWanted(presenceSpec, afterFace), "The presence vanishes once the face is settled (" + label + ").");
        }
        var closedAfter = Program.Copy(committed); closedAfter.Flags.Add("gesmerha.closed");
        check(!Rules.PresenceWanted(presenceSpec, closedAfter), "The presence outlives a closed route.");

        // Sol round 1 (BEL): the bench page tells the promise actually made: the purse oath, or the three days of sitting.
        var benchPage = S(P + "epilogue.bench");
        Paragraph[] BenchText(Snapshot s) => Rules.VisibleParagraphs(benchPage.Nodes[0], End(s));
        check(BenchText(committed).Any(x => x.Text.Contains("oath about purses")) && !BenchText(committed).Any(x => x.Text.Contains("Three days in her yard")),
            "The vow's bench page forgets the oath, or tells the sitting.");
        check(!BenchText(sat).Any(x => x.Text.Contains("oath about purses")) && BenchText(sat).Any(x => x.Text.Contains("Three days in her yard")),
            "The second ask's bench page attributes the oath the Commander declined.");

        // Sol round 1 (BEL/INT): the missed-window fallback, both branches, both locations. Both pay for the pieces; only the
        // trick shifts the alignment and marks the trick; both leave an unresolved courtship the late chain reads.
        foreach (var footstepsScene in new[] { home, capital })
        {
            var gameChoice = footstepsScene.Nodes.Single(x => x.Id == "game").Choices.Single();
            var honestChoice = footstepsScene.Nodes.Single(x => x.Id == "honest").Choices.Single();
            check(gameChoice.Crusade?.Resource == "Finances" && gameChoice.Crusade.Amount == -50
                  && honestChoice.Crusade?.Resource == "Finances" && honestChoice.Crusade.Amount == -50,
                "A footsteps branch does not pay for the pieces: " + footstepsScene.Id);
            check(gameChoice.Alignment?.Direction == "Chaotic" && honestChoice.Alignment == null,
                "The confession is charged the trick's alignment: " + footstepsScene.Id);
            check(gameChoice.Set.Contains("gesmerha.campaign_slow") && gameChoice.Set.Contains(P + "cost.campaign_slow")
                  && honestChoice.Set.Contains("gesmerha.campaign_slow") && !honestChoice.Set.Contains(P + "cost.campaign_slow"),
                "A footsteps branch leaves no courtship, or marks the confession as the trick: " + footstepsScene.Id);
        }
        var guestTrick = Pick(capital, guest, P + "cost.campaign_slow");
        var guestHonest = Play(capital, guest).First(r => r.Has(P + "cost.catchup") && !r.Has(P + "cost.campaign_slow"));
        var lateChain = new[] { "gesmerha.the_things_still_here", "gesmerha.the_box_with_two_names", "gesmerha.the_long_way_with_company",
                                "gesmerha.a_lesson_without_her", "gesmerha.the_room_she_chose" }.Select(S).ToArray();
        foreach (var (start, label) in new[] { (played, "home trick"), (honestResult, "home confession"), (guestTrick, "capital trick"), (guestHonest, "capital confession") })
        {
            check(!start.Has("gesmerha.lover") && start.Has("gesmerha.campaign_slow"), "The footsteps fixture is not the played outcome: " + label);
            var cur = Program.Copy(start); cur.Area = Wintersun; cur.Flags.Add("gesmerha.post_resolution_contact"); Rules.Complete(story, cur);
            var reached = true;
            foreach (var sc in lateChain)
            {
                cur = Later(story, cur, 48);
                if (!Rules.Available(story, sc, cur)) { check(false, "The missed-window fallback cannot enter " + sc.Id + " (" + label + ")."); reached = false; break; }
                var outs = Play(sc, cur).Where(r => !r.Has("gesmerha.closed") && !r.Has("gesmerha.evening_as_friends")
                                                   && !r.Has("gesmerha.late_friends") && !r.Has("gesmerha.late_open")).ToList();
                if (sc == lateChain.Last()) outs = outs.Where(r => r.Has("gesmerha.committed")).ToList();
                if (outs.Count == 0) { check(false, "The missed-window fallback has no romantic way through " + sc.Id + " (" + label + ")."); reached = false; break; }
                cur = outs[0];
            }
            if (reached)
                check(cur.Has("gesmerha.committed") && cur.Has("gesmerha.late_lovers"), "The missed-window fallback cannot commit: " + label);
        }

        // Sol round 1 (BEL): the unmet ending recalls the afternoons actually played; the court reunion (songs, the answer
        // left open) is not offered to a Commander whose only afternoon was the claimed one.
        var unmet = S("gesmerha.ending_unmet_again");
        Paragraph[] Unmet(Snapshot s)
        {
            var e = End(s);
            check(Rules.Available(story, unmet, e), "The unmet ending does not play: " + string.Join(",", e.Flags.Where(f => f.StartsWith("gesmerha.", StringComparison.Ordinal))));
            return Rules.VisibleParagraphs(unmet.Nodes[0], e);
        }
        check(Unmet(played).Count(x => x.Text.Contains("lost the eleventh game")) == 1 && Unmet(played).All(x => !x.Text.Contains("song")),
            "The trick's unmet ending invents the Chapter 3 afternoons.");
        check(Unmet(honestResult).Count(x => x.Text.Contains("owned before")) == 1 && Unmet(honestResult).All(x => !x.Text.Contains("song") && !x.Text.Contains("eleventh")),
            "The confession's unmet ending invents the Chapter 3 afternoons or the game.");
        var registeredCh3 = World(story, 6, Wintersun, "gesmerha.campaign_kept", "gesmerha.lover");
        check(Unmet(registeredCh3).Count(x => x.Text.Contains("song")) == 1 && Unmet(registeredCh3).All(x => !x.Text.Contains("one afternoon")),
            "The registered unmet ending loses its played recollection.");
        check(S("gesmerha.the_voice_at_court").Forbids.Contains(P + "cost.catchup"), "The court reunion recalls songs a claimed afternoon never sang.");
        Console.WriteLine("PASS: Gesmerha Trickster (Trk_Gesmerha_*): commission, pyre, splinters, the yard, the bench and wrong footsteps.");
    }
}
