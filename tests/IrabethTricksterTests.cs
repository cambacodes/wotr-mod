using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Irabeth, Trickster (Writer/handoffs/trickster/irabeth.md): relieved, not dismissed (F04) and the step she learned (F19).
// One test block per spec rules test (Trk_Irabeth_*), plus the registered-route integration (G6, presence, epilogue).
internal static class IrabethTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Contact = "280d4712dceb37f4a88e98f1f4c6e64f";
    private const string Returned = "irabeth.trickster.returned";
    private const string Killed = "anevia.irabeth_killed_by_commander";
    private const string Vell = "irabeth.trickster.cost.vell";
    private const string Dug = "irabeth.trickster.cost.dug_out";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000,
            // eng-final / E-Q8-10: fund these positive histories; the walker enforces every debit.
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        // These positive predicate fixtures represent an already accepted route.
        // Coarse-key negatives are independent in PayoffDepartureRulesTests.
        foreach (var rel in story.Relationships)
            if (flags.Contains(rel.Value.CommittedFlag) && story.Derived.ContainsKey(rel.Key + ".payoff.ordinary"))
                HouseholdTests.Earn(story, state, rel.Key + ".payoff.ordinary");
        foreach (var context in flags.Where(story.Derived.ContainsKey))
            HouseholdTests.Earn(story, state, context);
        state.AvailableContacts.Add(Contact);
        Rules.Complete(story, state);
        // Latches are stamped when the runtime records them; here, a day before the world is observed.
        foreach (var latch in story.Latches.Keys.Where(state.Has)) state.Times[latch] = state.Hour - 24;
        if (state.Has("trickster.ever")) state.Times["trickster.ever"] = state.Hour - 1000;   // the path was taken long before
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours)
    {
        var later = Program.Copy(state); later.Hour += hours; Rules.Complete(story, later); return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var standing = S("irabeth.trickster.dead.standing_order");
        var setup = S("irabeth.trickster.dead.setup");
        var lateOrder = S("irabeth.trickster.dead.late_order");
        var relieved = S("irabeth.trickster.dead.relieved_not_dismissed");
        var drill = S("irabeth.trickster.killed.drill");
        var lateStep = S("irabeth.trickster.killed.late_step");
        var blow = S("irabeth.trickster.killed.blow_missed");
        var duty = S("irabeth.trickster.back_on_duty");
        var commit = S("irabeth.trickster.commit");
        var second = S("irabeth.trickster.second_ask");
        var raiseList = S("irabeth.trickster.dead.raise_list");
        var dig = S("irabeth.trickster.killed.dig");
        var otherStory = S("irabeth.trickster.the_other_story");
        var reply = S("irabeth.trickster.nevi_reply");
        var returns = new[] { relieved, blow };
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));

        // Hooks: the deathbed line is inline beside "I relieve you." and continues into her native reply.
        check(setup.AnswerLists.SequenceEqual(new[] { "09b65ca563cc63141aebf70b7abe7270" })
              && setup.NativeReturnCue == "12f0d4c8dc3024a4cb86ab222ed3be66" && setup.EntryMythic == "PlayerIsTrickster",
            "Deathbed setup left the native deathbed list.");
        var joke = setup.Nodes.Single().Choices.Single();
        check(joke.NativeNext == "dc5a8da498d2cd945a50f4e6a107e6fc" && joke.Alignment?.Direction == "Chaotic"
              && joke.Set.Contains("irabeth.trickster.primed"), "Deathbed line lost its native continuation or price.");
        check(standing.AnswerLists.SequenceEqual(new[] { "06184e4f0a65650488e36600d8274d26" }) && standing.NativeReturnCue == null,
            "Standing order must stay a non-inline scene on the Storyteller's siege list.");
        check(new[] { relieved, blow, duty, commit, second, drill }.All(s => s.AnswerLists.SequenceEqual(new[] { "871af36f2ab2b1f40b5de77976c54276" })
              && s.ContactUnit == Contact), "Irabeth's return, test and commit left her own hub.");
        check(lateOrder.Remote && lateStep.Remote && lateOrder.TricksterState == "dead" && lateStep.TricksterState == "killed"
              && relieved.TricksterState == "dead" && blow.TricksterState == "killed", "Device states mislabelled.");
        var rel = story.Relationships["irabeth"];
        check(rel.UnavailableOverrides.TryGetValue("irabeth_dead", out var over) && over == Returned
              && rel.TricksterAccess.Count == 2, "Irabeth relationship patch missing.");
        check(story.Presences.TryGetValue("irabeth.presence", out var presence) && presence.Unit == Contact
              && presence.Mode == "reuse-native" && presence.Requires.Contains("irabeth.trickster.presence_on"), "Irabeth presence missing.");

        // Trk_Irabeth_Alive: W1, she lives; nothing to defy.
        var alive = World(story, 5, "trickster", "trickster.ever", "iz.fought_with_galfrey", "coronation.after");
        check(!Any(alive, setup, lateOrder, relieved, blow, lateStep), "Trk_Irabeth_Alive: a device opened while she lives.");
        check(!Rules.Available(story, setup, World(story, 5, "trickster")), "Deathbed line offered without the deathbed.");
        check(Rules.Available(story, setup, World(story, 5, "trickster", "irabeth.deathbed")), "Deathbed line missing at the deathbed.");

        // Trk_Irabeth_Drill: planted before Iz; a failed check is retried, success sets drilled.
        var ch3 = World(story, 3, "trickster");
        check(Rules.Available(story, drill, ch3), "Trk_Irabeth_Drill: drill unavailable in Chapter 3.");
        check(!Rules.Available(story, drill, World(story, 4, "trickster")), "Physical drill offered in the Abyss.");
        var drills = Program.Walk(drill, ch3);
        check(drills.Any(r => r.Has("irabeth.trickster.drilled")) && drills.Any(r => !r.Has(drill.Id) && r.Flags.SetEquals(ch3.Flags)),
            "Trk_Irabeth_Drill: the step cannot be both learned and failed.");
        check(drill.Nodes[0].Choices.Single().Check!.Skill == "SkillMobility", "The drill is not a Mobility check.");

        // Trk_Irabeth_StandingOrder: a primer only; it never primes the return by itself.
        var siege = World(story, 5, "trickster", "storyteller.asked_queen");
        check(Rules.Available(story, standing, siege) && !Any(siege, lateOrder, relieved), "Trk_Irabeth_StandingOrder failed.");
        check(!Rules.Available(story, standing, World(story, 5, "trickster")), "Standing order before the Storyteller's warning.");
        var ordered = Program.Walk(standing, siege).Where(r => r.Has(standing.Id)).ToList();
        check(ordered.Count == 1 && ordered[0].Has("irabeth.trickster.standing_order") && !ordered[0].Has("irabeth.trickster.primed"),
            "Standing order sets the wrong flags.");

        // Trk_Irabeth_DeadAtIz_Primed: the deathbed line, then her report a day after the Coronation.
        var listed = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", "irabeth.sacrificed", "irabeth.trickster.primed", "coronation.after");
        listed.Times["irabeth.trickster.primed"] = listed.Hour - 48;
        // Polish 9b: the order is why she answers; the chapel's one diamond, taken from Teodor Vell, is what calls her.
        check(Rules.Available(story, raiseList, listed) && !Rules.Available(story, relieved, listed),
            "Trk_Irabeth_RaiseList: the report opens before the chapel's list is struck.");
        var lists = Program.Walk(raiseList, listed);
        var struck = lists.Where(r => r.Has(Vell) && !r.Has("irabeth.trickster.cost.second_diamond")).ToList();
        check(struck.Count == 1 && lists.Any(r => r.Has("irabeth.trickster.declined") && !r.Has(Vell)), "Raise list: no strike, or no letting her rest.");
        var call = raiseList.Nodes.Single(n => n.Id == "call").Choices.Single();
        check(call.Crusade?.Resource == "Favors" && call.Crusade?.Amount == -100, "Striking the boy's name is free.");
        // Sol r1: the boy's death is never the compulsory price; a second diamond calls both, at the treasury's cost.
        var both = raiseList.Nodes.Single(n => n.Id == "call_both").Choices.Single();
        check(lists.Count(r => r.Has("irabeth.trickster.cost.second_diamond") && r.Has(Vell)) == 1 && both.Crusade?.Resource == "Finances"
              && both.Crusade?.Amount == -600, "No costly way to call both knights.");
        check(story.Scenes.Where(s => s.Id.StartsWith("irabeth.trickster.", StringComparison.Ordinal))
                  .SelectMany(s => s.Nodes).All(n => !n.Choices.Any(ch => ch.Revive != null)), "A revive by fiat crept back in.");
        var primed = Program.Copy(listed); primed.Flags.Add(Vell); primed.Times[Vell] = primed.Hour - 24; Rules.Complete(story, primed);
        check(Rules.Available(story, relieved, primed), "Trk_Irabeth_DeadAtIz_Primed: report unavailable.");
        check(!Any(primed, lateOrder, blow, lateStep), "Trk_Irabeth_DeadAtIz_Primed: a second device opened.");
        var early = Program.Copy(primed); early.Times["coronation.seen"] = early.Hour - 23;
        check(!Rules.Available(story, relieved, early), "Report ignores the Coronation delay.");
        foreach (bool torn in new[] { false, true })
        foreach (bool order in new[] { false, true })
        {
            var start = Program.Copy(primed);
            if (torn) start.Flags.Add("irabeth.trickster.soul_wound_told");
            if (order) start.Flags.Add("irabeth.trickster.standing_order");
            var pages = new HashSet<string>();
            var back = Program.Walk(relieved, start, (page, _) => pages.Add(page));
            check(pages.Contains("torn") == torn && pages.Contains("standing") == order && !pages.Contains("toasted") && pages.Contains("vell"),
                "Report variants ignore the soul wound or the standing order.");
            check(back.All(r => r.Has(Returned) && r.Has("irabeth.trickster.cost.under_orders") && r.Has("irabeth.started")),
                "Trk_Irabeth_DeadAtIz_Primed: the report does not return her.");
            foreach (var r in back)
            {
                check(!Any(r, returns) && !Rules.Available(story, lateOrder, r), "A second return after the report.");
                check(!Rules.Failed(rel, r), "Journal still fails after her return.");
            }
        }
        var gone = Program.Copy(primed); gone.Flags.Add("anevia_gone"); Rules.Complete(story, gone);
        check(Program.Walk(relieved, gone).Count == 1, "Anevia's departure branch is not the only answer when she has gone.");

        // Trk_Irabeth_DeadAtIz_Unprimed: no deathbed line (she died alone, W4) -> the late toast, at a price.
        var unprimed = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", "iz.left_early");
        check(Rules.Available(story, lateOrder, unprimed) && !Rules.Available(story, relieved, unprimed),
            "Trk_Irabeth_DeadAtIz_Unprimed: fallback unavailable, or report before any setup.");
        var toast = lateOrder.Nodes.Single(n => n.Id == "cup").Choices[0];
        check(toast.Crusade?.Resource == "Favors" && toast.Crusade?.Amount == -150 && toast.Alignment?.Direction == "Chaotic"
              && toast.Alignment?.Value == 1 && toast.Mythic == "PlayerIsTrickster", "The late toast lost its price.");
        var toastPages = new HashSet<string>();
        var toasts = Program.Walk(lateOrder, unprimed, (page, _) => toastPages.Add(page));
        var toasted = toasts.First(r => r.Has("irabeth.trickster.primed") && r.Has(Vell));
        check(toasted.Has("irabeth.trickster.cost.late") && toastPages.Contains("l_list") && toastPages.Contains("l_argue"),
            "Late toast is free, or the chapel's list is a second delivery.");
        check(toasts.Any(r => r.Has("irabeth.trickster.cost.second_diamond")) && !Rules.Available(story, raiseList, Later(story, toasted, 12)),
            "The late toast cannot buy the second diamond, or the list is offered twice.");
        var reported = World(story, 5, toasted.Flags.Concat(new[] { "coronation.after" }).ToArray());
        reported.Times["irabeth.trickster.primed"] = reported.Hour - 48;
        check(Rules.Available(story, relieved, reported), "Report unreachable after the late toast.");
        var discharge = relieved.Nodes.Single(n => n.Id == "discharge");
        check(discharge.Choices.Count(c => Rules.Match(c.Requires, c.Forbids, reported)) == 1
              && Rules.Match(discharge.Choices[1].Requires, discharge.Choices[1].Forbids, reported), "Late variant of the payoff line not shown.");

        // Trk_Irabeth_Declined: the only way she stays dead on a live Trickster run.
        var declined = toasts.Single(r => r.Has("irabeth.trickster.declined") && !r.Has("irabeth.trickster.primed"));
        var afterRest = Later(story, declined, 500); afterRest.Flags.Add("coronation.after"); Rules.Complete(story, afterRest);
        check(!Any(afterRest, returns) && !Rules.Available(story, lateOrder, afterRest) && !Rules.Available(story, raiseList, afterRest)
              && !declined.Has("anevia.trickster.primed")
              && !declined.Has("galfrey.closed"), "Trk_Irabeth_Declined: a return survives the decline, or it touched another route.");

        // Trk_Irabeth_Killed / _Lie / _BlowStands: the drill pays off at her hub.
        var drilledKill = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", Killed, "irabeth.trickster.drilled", "coronation.after");
        check(Rules.Available(story, dig, drilledKill) && !Any(drilledKill, blow, relieved, lateOrder, lateStep, raiseList),
            "Trk_Irabeth_Killed_Dig: the step pays off without the Commander sending anyone back.");
        var digs = Program.Walk(dig, drilledKill);
        check(digs.Count(r => r.Has(Dug)) == 2 && digs.Any(r => r.Has("irabeth.trickster.declined") && !r.Has(Dug))
              && dig.Nodes[0].Choices[0].Crusade?.Amount == -150 && dig.Nodes[0].Choices[2].Crusade?.Amount == -400
              && digs.Any(r => r.Has("irabeth.trickster.cost.hired_healer")), "Dig: no diggers, no price, no bought surgeon, or no letting the blow stand.");
        var killed = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", Killed, "irabeth.trickster.drilled", Dug, "coronation.after");
        check(Rules.Available(story, blow, killed) && !Any(killed, relieved, lateOrder, lateStep), "Trk_Irabeth_Killed: wrong device.");
        var blows = Program.Walk(blow, killed);
        var truth = blows.Where(r => r.Has("irabeth.trickster.accounting_truth")).ToList();
        var lie = blows.Where(r => r.Has("irabeth.trickster.cost.accounting_lied")).ToList();
        var stands = blows.Where(r => r.Has("irabeth.trickster.declined")).ToList();
        check(truth.Count == 1 && truth[0].Has(Returned) && truth[0].Has("irabeth.accounting_kept") && truth[0].Has("irabeth.trickster.blow_rewritten"),
            "Trk_Irabeth_Killed: the honest account is not kept.");
        check(lie.Count == 1 && lie[0].Has(Returned) && !lie[0].Has("irabeth.accounting_kept"), "Trk_Irabeth_Killed_Lie failed.");
        check(stands.Count == 1 && !stands[0].Has(Returned) && !Any(stands[0], blow, lateStep), "Trk_Irabeth_Killed_BlowStands failed.");
        check(stands[0].Has("irabeth.trickster.blow_stands") && presence?.Forbids.Contains("irabeth.trickster.blow_stands") == true,
            "She stays on watch after the blow was let stand.");

        // Trk_Irabeth_Killed_Late: no drill -> the raise list, with the kill entered in the chapel's book in the Commander's words.
        var undrilled = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", Killed, "coronation.after");
        check(Rules.Available(story, lateStep, undrilled) && !Rules.Available(story, blow, undrilled) && !Rules.Available(story, dig, undrilled),
            "Trk_Irabeth_Killed_Late: wrong device.");
        var dictate = lateStep.Nodes[0].Choices[0];
        check(!Rules.Match(dictate.Requires, dictate.Forbids, undrilled), "The dictated step (a report that rewrites the blow) is still offered.");
        var lateOutcomes = Program.Walk(lateStep, undrilled);
        check(lateOutcomes.All(r => !r.Has("irabeth.trickster.drilled")), "The late report still teaches the step after the fact.");
        var onRecord = lateOutcomes.Single(r => r.Has("irabeth.trickster.raised_on_record"));
        var entered = lateStep.Nodes.Single(n => n.Id == "record").Choices;
        check(onRecord.Has("irabeth.trickster.cost.late") && !onRecord.Has(Vell) && onRecord.Has("irabeth.trickster.cost.remembers_the_blow")
              && !Rules.Match(entered[0].Requires, entered[0].Forbids, undrilled)
              && entered[1].Crusade?.Resource == "Finances" && entered[1].Crusade?.Amount == -600, "The raise on the record is free, or strikes the boy.");
        var raisedBack = Later(story, onRecord, 24);
        check(Rules.Available(story, blow, raisedBack), "Blow unrecoverable after the raise on the record.");
        var raisedPages = new HashSet<string>();
        var raisedOutcomes = Program.Walk(blow, raisedBack, (page, _) => raisedPages.Add(page));
        // Q12 (Sol HOW): the aftermath is covered on both returns: Seelah hears of the sappers, or reads the chapel's book.
        var raisedTruth = raisedOutcomes.First(r => r.Has(Returned));
        check(Rules.Available(story, S("irabeth.trickster.killed.react_seelah_raised"), Later(story, raisedTruth, 24))
              && !Rules.Available(story, S("irabeth.trickster.killed.react_seelah"), Later(story, raisedTruth, 24))
              && Rules.Available(story, S("irabeth.trickster.killed.react_seelah"), Later(story, truth[0], 24))
              && !Rules.Available(story, S("irabeth.trickster.killed.react_seelah_raised"), Later(story, truth[0], 24)),
            "Seelah's reaction tells the raised Irabeth's story with sappers, or the dug one's with a diamond.");
        var kitraneBack = Later(story, raisedTruth, 24); kitraneBack.Flags.Add("galfrey.trickster.returned"); Rules.Complete(story, kitraneBack);
        check(Rules.Available(story, S("irabeth.trickster.killed.react_kitrane"), kitraneBack)
              && !Rules.Available(story, S("irabeth.trickster.dead.react_kitrane"), kitraneBack),
            "The Queen who came back as Kitrane has no word for the Irabeth the Commander struck down.");
        check(raisedPages.Contains("raised") && !raisedPages.Contains("both") && !raisedPages.Contains("dug")
              && raisedOutcomes.Any(r => r.Has(Returned) && r.Has("irabeth.trickster.accounting_truth"))
              && raisedOutcomes.Any(r => r.Has("irabeth.trickster.blow_stands") && !r.Has(Returned)),
            "The raised Irabeth is told she stepped, or cannot let the blow stand.");

        // Trk_Irabeth_Killed_PathFailed / Trk_Irabeth_PathFailed: canon fate stands once the path is lost.
        var failedKilled = World(story, 5, "trickster.was", "trickster.failed", "irabeth_dead", Killed, "irabeth.trickster.drilled", "coronation.after");
        check(!Any(failedKilled, blow, lateStep), "Trk_Irabeth_Killed_PathFailed: a device survives the lost path.");
        var failed = World(story, 5, "trickster.was", "trickster.failed", "irabeth_dead", "coronation.after");
        check(!Any(failed, setup, lateOrder, blow, relieved), "Trk_Irabeth_PathFailed: a device survives the lost path.");
        // TT: a return recorded before the path failed keeps her scenes.
        var kept = World(story, 5, "trickster.was", "trickster.failed", "irabeth_dead", Returned, "coronation.after");
        kept.Times[Returned] = kept.Hour - 48;
        check(Rules.Available(story, duty, kept), "A recorded return is lost with the path.");

        // Trk_Irabeth_Commit / Trk_Irabeth_Refusal: Anevia is still on the road, so her answer is no, then a priced ask.
        foreach (string answer in new[] { "irabeth.trickster.answered_her", "irabeth.trickster.answered_crusade" })
        foreach (bool lied in new[] { false, true })
        {
            var ask = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", Returned, "irabeth.trickster.back_on_duty", answer, "anevia_gone");
            if (lied) ask.Flags.Add("irabeth.trickster.cost.accounting_lied");
            ask.Times["irabeth.trickster.back_on_duty"] = ask.Hour - 72;
            check(Rules.Available(story, commit, ask) && !Rules.Available(story, second, ask), "Trk_Irabeth_Commit: commit unavailable.");
            var pages = new HashSet<string>();
            var outcomes = Program.Walk(commit, ask, (page, _) => pages.Add(page));
            check(pages.Contains("lied") == lied && pages.Contains("her") == answer.EndsWith("her"), "Commit ignores what she heard.");
            check(outcomes.All(r => !r.Has("irabeth.committed") && !r.Has("anevia.closed") && !r.Has("tirabade.group_closed")),
                "Commit lands while Anevia is still gone.");
            var no = outcomes.Single(r => r.Has("irabeth.trickster.declined"));
            check(pages.Contains("no") && !pages.Contains("no_house"), "Her no forgets that Nevi is on the road.");
            if (lied)
            {
                // Sol BEL: "Ask me again when you've told me the other one." The second ask waits for the other story.
                check(!Rules.Available(story, second, Later(story, no, 200)), "The second ask forgives the lie by omission.");
                check(!Rules.Available(story, otherStory, Later(story, no, 47)) && Rules.Available(story, otherStory, Later(story, no, 48)),
                    "The other story is mistimed.");
                var told = Program.Walk(otherStory, Later(story, no, 48));
                check(told.Any(r => !r.Has(otherStory.Id)) && told.Count(r => r.Has("irabeth.trickster.told_the_other_story")) == 1,
                    "The other story cannot be told, or cannot be put off.");
                no = told.Single(r => r.Has("irabeth.trickster.told_the_other_story"));
                check(no.Has("irabeth.trickster.cost.accounting_lied"), "Telling the truth erased the lie.");
            }
            check(!Rules.Available(story, second, Later(story, no, 200)), "The priced ask sends a new letter without current contact with Anevia.");
            no.Flags.Add("anevia.trickster.returned");
            Rules.RecordAvailabilityEvents(story, no, new[] { "anevia.trickster.returned" });
            Rules.Complete(story, no);
            check(!Rules.Available(story, commit, no) && (lied || !Rules.Available(story, second, Later(story, no, 23)))
                  && Rules.Available(story, second, Later(story, no, 24)), "Trk_Irabeth_Refusal: the priced second ask is mistimed.");
            var asked = new HashSet<string>();
            var finals = Program.Walk(second, Later(story, no, 24), (page, _) => asked.Add(page));
            check(finals.All(r => !r.Has("irabeth.committed")) && finals.Any(r => r.Has("irabeth.closed")), "Second ask: commits before the courier, or no hard no.");
            check(finals.Any(r => !r.Has("irabeth.committed") && !r.Has("irabeth.closed")),
                "The returned Anevia's waiting branch cannot defer the request.");
            var consent = Later(story, no, 24);
            consent.Flags.Add("anevia.trickster.shares_beth");
            Rules.Complete(story, consent);
            var replies = Program.Walk(second, consent);
            check(replies.Any(r => r.Has("irabeth.committed")) && replies.Any(r => r.Has("irabeth.trickster.asked_as_commander")),
                "Existing returned-partner consent bypasses Irabeth's own answer.");
        }

        // Sol r1 BEL: after the Commander's own blade, her test comes before any yes.
        var watch = S("irabeth.trickster.killed.the_watch");
        var struckDown = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", Killed, Returned, "irabeth.trickster.back_on_duty",
                               "irabeth.trickster.cost.remembers_the_blow", "irabeth.trickster.answered_her", "anevia_gone");
        struckDown.Times["irabeth.trickster.back_on_duty"] = struckDown.Hour - 72;
        // Q12 (Sol BEL): with no lover's history, she must want the Commander (the roll of the dead) before her test.
        var roll = S("irabeth.trickster.killed.the_roll");
        check(!Rules.Available(story, commit, struckDown) && !Rules.Available(story, watch, struckDown) && Rules.Available(story, roll, struckDown),
            "A yes after the blow without her test, or her test before any reason to want the Commander.");
        var rolls = Program.Walk(roll, struckDown);
        check(rolls.Count(r => r.Has("irabeth.trickster.drawn")) == 2 && rolls.Any(r => !r.Has("irabeth.trickster.drawn")),
            "The roll of the dead has no refusal, or no way to be drawn.");
        struckDown = Later(story, rolls.First(r => r.Has("irabeth.trickster.drawn")), 24);
        check(Rules.Available(story, watch, struckDown), "Her test does not follow the roll of the dead.");
        var watched = Program.Walk(watch, struckDown).Where(r => r.Has("irabeth.trickster.slept_under_her_sword")).ToList();
        check(watched.Count == 1 && Rules.Available(story, commit, watched[0]), "Her test cannot be passed, or passing it does not reopen the ask.");
        var blowPages = new HashSet<string>();
        Program.Walk(commit, watched[0], (page, _) => blowPages.Add(page));
        check(!blowPages.Contains("no") || blowPages.Contains("reasons") || !blowPages.Contains("threshold"), "The killed history borrows the rescue's threshold.");
        check(!blowPages.Contains("threshold"), "The killed history reaches the rescue's threshold.");

        // Sol INT: a wife who never left Drezen. Irabeth asks her in person, not by the south-road courier.
        var home = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", Returned, "irabeth.trickster.back_on_duty", "irabeth.trickster.answered_her");
        home.Times["irabeth.trickster.back_on_duty"] = home.Hour - 72;
        var homePages = new HashSet<string>();
        var homeNo = Program.Walk(commit, home, (page, _) => homePages.Add(page)).Single(r => r.Has("irabeth.trickster.declined"));
        check(homePages.Contains("no_house") && !homePages.Contains("no"), "Irabeth sends a wife in Drezen out onto the road.");
        var homeAsk = new HashSet<string>();
        var homeFinals = Program.Walk(second, Later(story, homeNo, 96), (page, _) => homeAsk.Add(page));
        check(homeFinals.Any(r => r.Has("irabeth.committed") && r.Has("irabeth.trickster.asked_nevi")) && homeAsk.Contains("sent_home")
              && !homeAsk.Contains("sent") && homeAsk.Contains("morning_house") && !homeAsk.Contains("morning"),
            "The pen goes south to a wife four streets away.");

        // Sol COX: the shared finale's surviving Commander never gets the mourning page.
        var survived = World(story, 6, "trickster", "trickster.ever", "ending.trickster", "sacrifice", "irabeth.lover");
        check(survived.Has("trickster.commander_back") && !Rules.Available(story, S("irabeth.ending_sacrifice"), survived)
              && Rules.Available(story, S("irabeth.ending_unfinished"), survived), "A living Commander is mourned.");

        // back_on_duty: the test between return and commit; physical only after the return.
        var justBack = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", Returned);
        justBack.Times[Returned] = justBack.Hour - 23;
        check(!Rules.Available(story, duty, justBack) && Rules.Available(story, duty, Later(story, justBack, 1)), "Test beat mistimed.");
        check(Program.Walk(duty, Later(story, justBack, 1)).All(r => r.Has("irabeth.trickster.back_on_duty")), "Test beat does not record.");
        var dutyPages = new HashSet<string>();
        Program.Walk(duty, Later(story, justBack, 1), (page, _) => dutyPages.Add(page));
        check(dutyPages.Contains("unsigned"), "The unsigned discharge cannot be offered: the sword clause costs nothing.");

        // Registered route: her pre-Iz private scenes stay closed; her endings return with her (G6).
        var registered = story.Scenes.Where(s => s.Relationship == "irabeth" && !s.Id.StartsWith("irabeth.trickster.", StringComparison.Ordinal)
                                                 && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToList();
        var dead = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", Returned, "irabeth.lover", "irabeth.personal_ready");
        check(registered.All(s => !Rules.Available(story, s, dead)), "A pre-Iz scene reopens for the returned Irabeth.");
        var end = World(story, 6, "trickster", "trickster.ever", "irabeth_dead", Returned, "irabeth.lover", "irabeth.trickster.cost.under_orders", Vell);
        check(Rules.Available(story, S("irabeth.ending_unfinished"), end) && !Rules.Available(story, S("irabeth.ending_loss"), end)
              && !Rules.Available(story, S("irabeth.trickster.epilogue.under_orders"), end), "G6 epilogue arbitration wrong for a lover.");
        check(Rules.VisibleParagraphs(S("irabeth.ending_unfinished").Nodes[0], end).Count(p => p.Requires.Contains(Vell)) == 1, "Under-orders paragraph missing on her ending.");
        var endFriend = World(story, 6, "trickster", "trickster.ever", "irabeth_dead", Returned, "irabeth.trickster.cost.under_orders", Vell);
        check(Rules.Available(story, S("irabeth.trickster.epilogue.under_orders"), endFriend)
              && !story.Scenes.Where(s => s.Id.StartsWith("irabeth.ending_", StringComparison.Ordinal)).Any(s => Rules.Available(story, s, endFriend)),
            "Returned non-lover gets no page or two pages.");
        // Sol r4 INT: an early lover who dies at Iz, returns and recommits gets the recommitted page, not "unfinished".
        var recommitted = World(story, 6, "trickster", "trickster.ever", "irabeth_dead", Returned, "irabeth.lover", "irabeth.committed", Vell);
        var recommittedPages = story.Scenes.Where(s => s.Relationship == "irabeth" && s.Owner == "Epilogue" && Rules.Available(story, s, recommitted)).ToList();
        check(recommittedPages.Count == 1 && recommittedPages[0].Id == "irabeth.trickster.epilogue.off_the_record",
            "The recommitted lover gets the unfinished ending: " + string.Join(",", recommittedPages.Select(s => s.Id)));
        var endDead = World(story, 6, "irabeth_dead", "irabeth.lover");
        check(Rules.Available(story, S("irabeth.ending_loss"), endDead), "Canon loss page lost.");

        // Reactions: the two allocated reactors. Seelah per state (the dug and the raised returns apart), Galfrey's letter for
        // the sacrifice, and (Q12) Galfrey come back as Kitrane, whose word Irabeth reports on her own hub (no delivery).
        var reactions = story.Scenes.Where(s => s.Relationship == "irabeth" && s.Reaction).ToArray();
        check(reactions.Length == 6 && reactions.All(r => r.Owner == "Seelah" || r.Owner == "Galfrey"
                  || r.Owner == "Irabeth" && r.Requires.Contains("galfrey.trickster.returned") && !r.Remote),
            "Irabeth reactions changed.");
        if (story.Scenes.Any(s => s.Id == "anevia.trickster.gone.setup")) RunWithAnevia(story, check);
    }

    // The items that waited on Anevia's return: the gate closing of her report, the settling line, Kiss / Wait
    // (appended), her no at home, the signed request read at the gate, G6(b) anevia_gone, the shared ending.
    private static void RunWithAnevia(Story story, Action<bool, string> check)
    {
        const string AneviaReturned = "anevia.trickster.returned";
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
                var relieved = S("irabeth.trickster.dead.relieved_not_dismissed");
        var report = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", "irabeth.trickster.primed", "irabeth.trickster.cost.vell",
                           "coronation.after", "anevia_gone", AneviaReturned);
        var reportPages = new HashSet<string>();
        check(Program.Walk(relieved, report, (page, _) => reportPages.Add(page)).Count == 1 && reportPages.Contains("gate") && !reportPages.Contains("south"),
            "Irabeth's report sends her south to a wife who is at the gate.");
        var irabethCommit = S("irabeth.trickster.commit");
        foreach (bool lie in new[] { false, true })
        {
            var ask = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", Returned, "irabeth.trickster.back_on_duty",
                            "irabeth.trickster.answered_her", "anevia_gone", AneviaReturned, "anevia.trickster.shares_beth");
            if (lie) ask.Flags.Add("irabeth.trickster.cost.accounting_lied");
            ask.Times["irabeth.trickster.back_on_duty"] = ask.Hour - 72;
            var pages = new HashSet<string>();
            var outcomes = Program.Walk(irabethCommit, ask, (page, _) => pages.Add(page));
            check(pages.Contains("talked") && pages.Contains("no_home") && !pages.Contains("no")
                  && (lie || pages.Contains("reckon") && pages.Contains("threshold") && pages.Contains("morning")),
                "Irabeth's commit ignores Nevi's return.");
            // Wait-for-her no longer commits by the answer: she decides in node decides, and after an exposed lie she says not tonight.
            check(lie ? outcomes.All(r => !r.Has("irabeth.committed"))
                      : outcomes.Count(r => r.Has("irabeth.committed")) >= 2
                        && outcomes.Where(r => r.Has("irabeth.committed")).All(r => r.Has("irabeth.partner_stance.share")),
                "Kiss offered after an exposed lie, or accepted sharing missing.");
            check(outcomes.All(r => r.Has("irabeth.trickster.asked_nevi")), "Irabeth told the Commander she asked Nevi, and nothing recorded it.");
            check(!lie || pages.Contains("not_tonight"), "After an exposed lie, her decision is not her no.");
            check(outcomes.Any(r => r.Has("irabeth.trickster.declined") && !r.Has("irabeth.committed")), "Her no is gone once Nevi is home.");
        }
        // Anevia back but silent: no intimate choice, and Irabeth's no names the silence.
        var silent = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", Returned, "irabeth.trickster.back_on_duty",
                           "irabeth.trickster.answered_her", "anevia_gone", AneviaReturned);
        silent.Times["irabeth.trickster.back_on_duty"] = silent.Hour - 72;
        var silentPages = new HashSet<string>();
        var silentOutcomes = Program.Walk(irabethCommit, silent, (page, _) => silentPages.Add(page));
        check(silentOutcomes.All(r => !r.Has("irabeth.committed")) && silentPages.Contains("no_gate") && !silentPages.Contains("talked"),
            "Irabeth commits before Anevia has said her piece.");
        var answer = irabethCommit.Nodes.Single(n => n.Id == "answer").Choices;
        check(answer[1].Next == "no" && answer.Skip(2).Any(ch => SurfaceIds.Has(SurfaceIds.Of(story, ch), "[irabeth.trickster.commit/answer/choice/3]")),
            "Irabeth's commit choices were reordered instead of appended.");
        foreach (var id in new[] { "irabeth.one_truth_to_tell", "irabeth.anevias_answer", "irabeth.the_evening_she_chose", "irabeth.a_day_of_our_own",
                                   "irabeth.after_the_shared_answer" })
            check(S(id).ForbidOverrides.TryGetValue("anevia_gone", out var lifted) && lifted == AneviaReturned, "G6(b) anevia_gone override missing: " + id);

        var together = World(story, 6, "trickster", "trickster.ever", "irabeth_dead", "anevia_gone", Returned, AneviaReturned, "committed");
        var shared = story.Scenes.Where(s => s.Owner == "Epilogue" && (s.Relationship == "anevia" || s.Relationship == "irabeth" || s.Relationship == "tirabade")
                                             && Rules.Available(story, s, together)).ToList();
        check(shared.Count == 1 && shared[0].Id == "ending_promised" && Rules.VisibleParagraphs(shared[0].Nodes.Last(), together).Length >= 1,
            "The shared Tirabade ending does not own the committed trio's epilogue.");

        var second = S("irabeth.trickster.second_ask");
        var declined = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", Returned, "irabeth.trickster.back_on_duty", "irabeth.trickster.declined",
                             "anevia_gone", AneviaReturned, "anevia.trickster.shares_beth");
        declined.Times["irabeth.trickster.declined"] = declined.Hour - 96;
        var asked = new HashSet<string>();
        check(Program.Walk(second, declined, (page, _) => asked.Add(page)).Any(r => r.Has("irabeth.committed"))
              && asked.Contains("sent_gate") && !asked.Contains("sent") && asked.Contains("morning_home"),
            "The signed request still travels south to a wife at the gate.");
        // Anevia back but silent: the signed request waits in the roster; nothing commits and the scene stays open.
        var quiet = Program.Copy(declined); quiet.Flags.Remove("anevia.trickster.shares_beth");
        var quietPages = new HashSet<string>();
        var quietOutcomes = Program.Walk(second, quiet, (page, _) => quietPages.Add(page));
        check(quietOutcomes.All(r => !r.Has("irabeth.committed")) && quietPages.Contains("held") && !quietPages.Contains("threshold")
              && !quietPages.Contains("morning_home") && quietOutcomes.Any(r => !r.Has(second.Id)),
            "The signed request commits past Anevia's silence.");
    }
}
