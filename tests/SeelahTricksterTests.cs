using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Seelah, Trickster (Writer/handoffs/trickster/seelah.md): rob the thief (F07). One block per spec rules test
// (Trk_Seelah_*), plus the registered-route integration (G6 overrides, the retired revive, the presence, Irabeth's barks).
internal static class SeelahTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Npc = "90481a29cc75f424b9891a55c6dcbb53";
    private const string Diamond = "6a7cdeb14fc6ef44580cf639c5cdc113";
    private const string Returned = "seelah.trickster.returned";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        // eng-final E-Q8-10: fund the positive fixture; the walker enforces every debit.
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        // These positive predicate fixtures represent an already accepted route.
        // Coarse-key negatives are independent in PayoffDepartureRulesTests.
        foreach (var rel in story.Relationships)
            if (flags.Contains(rel.Value.CommittedFlag) && story.Derived.ContainsKey(rel.Key + ".payoff.ordinary"))
                HouseholdTests.Earn(story, state, rel.Key + ".payoff.ordinary");
        foreach (var context in flags.Where(story.Derived.ContainsKey))
            HouseholdTests.Earn(story, state, context);
        state.AvailableContacts.Add(Npc);
        Rules.Complete(story, state);
        foreach (var latch in story.Latches.Keys.Where(state.Has)) state.Times[latch] = state.Hour - 48;
        return state;
    }

    // The world after a walk, observed later: the native death etude ends once the retained unit stands up.
    private static Snapshot After(Story story, Snapshot outcome, int hours, params string[] drop)
    {
        var later = Program.Copy(outcome);
        later.Hour += hours;
        foreach (var flag in drop) later.Flags.Remove(flag);
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var lesson = S("seelah.trickster.in_party.lift_lesson");
        var pick = S("seelah.trickster.dead.pickpocket");
        var wakes = S("seelah.trickster.dead.wakes");
        var effects = S("seelah.trickster.dead.pickpocket_effects");
        var setup = S("seelah.trickster.dismissed.setup");
        var late = S("seelah.trickster.dismissed.late");
        var papers = S("seelah.trickster.dismissed.back_for_the_papers");
        var papersLetter = S("seelah.trickster.dismissed.back_for_the_papers_letter");
        var stay = S("seelah.trickster.after.stay_or_go");
        var commit = S("seelah.trickster.dismissed.commit");
        var second = S("seelah.trickster.dismissed.second_ask");
        var devices = new[] { pick, effects, late, papers, papersLetter };
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));
        IEnumerable<Choice> Choices(Scene s) => s.Nodes.SelectMany(n => n.Choices);

        // Hooks and data.
        check(setup.AnswerLists.SequenceEqual(new[] { "64cfedbb85f36a44cb45f568f18152f7" })
              && setup.NativeReturnCue == "3a2c9f56a58b5c1478746c3ebc456986" && setup.EntryMythic == "PlayerIsTrickster"
              && setup.TricksterState == "dismissed", "Dismissal setup left the native dismissal list.");
        var joke = setup.Nodes.Single().Choices.Single();
        check(joke.NativeNext == "6b81c330ca8b1324186cb02bdc8d9c54" && joke.Set.Contains("seelah.trickster.primed")
              && joke.Set.Contains("seelah.trickster.pockets_picked"), "Dismissal joke lost its native farewell or its flags.");
        check(new[] { lesson, wakes }.All(s => s.AnswerLists.SequenceEqual(new[] { "417fa384f3250634bb71859fbc913453" })),
            "Lift lesson or waking left her companion hub.");
        check(new[] { papers, stay, commit, second }.All(s => s.ContactUnit == Npc && s.InteractionHub == "seelah.presence"),
            "Tavern scenes left the presence.");
        check(pick.Remote && pick.Recovery == "seelah" && effects.Remote && late.Remote && papersLetter.Remote,
            "Remote devices mislabelled.");
        check(pick.TricksterState == "dead" && effects.TricksterState == "dead_no_unit" && late.TricksterState == "dismissed"
              && papers.TricksterState == "dismissed", "Device states mislabelled.");
        var rel = story.Relationships["seelah"];
        check(rel.UnavailableOverrides["seelah_dead"] == Returned && rel.UnavailableOverrides["seelah_gone"] == Returned
              && rel.TricksterAccess.Count == 3, "Seelah relationship patch missing.");
        check(story.Presences.TryGetValue("seelah.presence", out var presence) && presence.Unit == Npc && presence.Mode == "spawn-copy"
              && presence.At?.NearUnit == "0f12118177d102f428a3b30b15b132eb", "Seelah presence missing or on the companion unit.");
        check(story.RemovableItems.Contains(Diamond) && story.InventoryItems["seelah.diamond_held"] == Diamond, "Diamond not whitelisted.");

        // Trk_Seelah_InParty: the lesson is planted while she is in the party; no device opens.
        var party = World(story, 3, "trickster", "trickster.ever");
        check(Rules.Available(story, lesson, party) && !Any(party, devices), "Trk_Seelah_InParty failed.");
        var lessons = Program.Walk(lesson, party);
        check(lessons.Count == 2 && lessons.All(r => r.Has("seelah.trickster.lift_lesson")),
            "Trk_Seelah_InParty: both check results must record that she taught the lift.");
        check(Choices(lesson).Single(c => c.Check != null).Check!.Skill == "SkillThievery", "The lesson is not a Thievery check.");

        // Trk_Seelah_Dead: retained unit, a diamond in the coat.
        var dead = World(story, 3, "trickster", "trickster.ever", "seelah_dead", "revive.seelah.available", "seelah.diamond_held");
        check(dead.Has("seelah.finally_dead"), "seelah.finally_dead is not derived from the retained dead unit.");
        check(Rules.Available(story, pick, dead) && !Any(dead, effects, papers, late), "Trk_Seelah_Dead: wrong device set.");
        check(!Rules.Available(story, S("seelah.fate_life"), dead), "The retired revive still opens beside the pickpocket.");
        var joker = Choices(pick).Single(c => c.Mythic == "PlayerIsTrickster");
        check(joker.Alignment?.Direction == "Chaotic" && joker.Alignment.Value == 1, "The pickpocket lost its alignment price.");
        var paid = Choices(pick).Where(c => c.Revive == "seelah").ToList();
        check(paid.Count == 2 && paid.Count(c => c.RemoveItem == Diamond) == 1
              && paid.Count(c => c.Crusade?.Resource == "Favors" && c.Crusade.Amount == -100) == 1, "The rite's two prices are wrong.");
        // Polish b9c: the bowl is filled by a lift on the relic-seller (her list's last line); the lift or the caught lift
        // both fill it, and only the caught one leaves him knowing the Commander's face.
        var raised = Program.Walk(pick, dead).Where(r => r.Has(Returned)).ToList();
        // Q10 r2: the caught lift offers his word (broker_knows), an arrest (seller_taken, Favors) or a buy-off (seller_paid,
        // Finances); exactly one consequence each, and all four roads fill the bowl.
        check(raised.Count == 4 && raised.All(r => r.Has("seelah.revived") && r.Has("seelah.trickster.cost.holds_her_death")
              && !r.Has("seelah.trickster.cost.chaplains_word")) && raised.Count(r => r.Has("seelah.trickster.cost.broker_knows")) == 1
              && raised.Count(r => r.Has("seelah.trickster.cost.seller_taken")) == 1 && raised.Count(r => r.Has("seelah.trickster.cost.seller_paid")) == 1
              && raised.All(r => new[] { "broker_knows", "seller_taken", "seller_paid" }.Count(f => r.Has("seelah.trickster.cost." + f)) <= 1),
            "Trk_Seelah_Dead: the diamond rite sets the wrong flags, or a failed lift closes the road.");
        var liftDcs = Choices(pick).Where(c => c.Check != null).Select(c => (c.Check!.DC, lessoned: c.Requires.Contains("seelah.trickster.lift_lesson"))).ToList();
        check(liftDcs.Count == 2 && liftDcs.Single(d => d.lessoned).DC == 15 && liftDcs.Single(d => !d.lessoned).DC == 25
              && Choices(pick).Where(c => c.Check != null).All(c => c.Check!.Skill == "SkillThievery" && c.Mythic == null),
            "The relic-seller lift is not her lesson's Thievery check, or a mythic power does it.");
        var standing = After(story, raised[0], 1, "seelah_dead", "revive.seelah.available");
        check(Rules.Available(story, wakes, standing) && !Rules.Available(story, S("seelah.fate_return"), standing),
            "Trk_Seelah_Dead: she does not wake into her own scene.");
        check(!Rules.Available(story, wakes, After(story, raised[0], 1)), "She wakes while the death etude still holds.");
        check(!Any(standing, devices), "A second device opened after the rite.");

        // Trk_Seelah_Dead_NoDiamond: the chapel's reserve, on the Commander's word.
        var poor = World(story, 5, "trickster", "trickster.ever", "seelah_dead", "revive.seelah.available");
        var owed = Program.Walk(pick, poor).Where(r => r.Has(Returned)).ToList();
        check(Rules.Available(story, pick, poor) && owed.Count == 4 && owed.All(r => r.Has("seelah.trickster.cost.chaplains_word")),
            "Trk_Seelah_Dead_NoDiamond failed.");

        // Reviewed polish 005–008/011–012: walk each acquisition, then read its
        // one waking account. LESSON records either practice result, never a successful lift.
        foreach (bool trained in new[] { false, true })
        foreach (bool credit in new[] { false, true })
        {
            var source = World(story, 5, "trickster", "trickster.ever", "seelah_dead", "revive.seelah.available");
            if (trained)
            {
                var taught = Program.Walk(lesson, party).First();
                source.Flags.UnionWith(taught.Flags.Where(f => f == "seelah.trickster.lift_lesson" || f == "seelah.started"));
            }
            if (!credit) source.Flags.Add("seelah.diamond_held");
            Rules.Complete(story, source);
            var outcomes = Program.Walk(pick, source).Where(r => r.Has(Returned)).ToList();
            check(outcomes.Count == 4, "Seelah acquisition matrix lost an outcome.");
            foreach (var acquired in outcomes)
            {
                bool bought = acquired.Has("seelah.trickster.cost.seller_paid");
                bool seized = acquired.Has("seelah.trickster.cost.seller_taken");
                var awake = After(story, acquired, 1, "seelah_dead", "revive.seelah.available");
                var first = wakes.Nodes[0].Choices.Where(c => Rules.ChoiceAvailable(c, awake)).ToList();
                check(Rules.Available(story, wakes, awake) && first.Count == 1,
                    "Seelah waking must have one payment account for each acquisition and second stone.");
                check(wakes.Nodes[0].Choices.IndexOf(first.Single()) == (bought ? (credit ? 3 : 2) : (credit ? 1 : 0))
                      && first.Single().Next == (credit ? (bought ? "coin_word_paid" : "coin_word") : "coin"),
                    "Seelah waking confuses purchase, seizure or the second stone.");
                var visited = new HashSet<string>();
                var given = Program.Walk(wakes, awake, (page, _) => visited.Add(page))
                    .Single(r => r.Has("seelah.trickster.death_returned"));
                check(visited.Contains("coin_word_paid") == (bought && credit)
                      && visited.Contains("coin_word") == (!bought && credit),
                    "Seelah credit response claims a robbery on the paid road.");
                check(acquired.CrusadeResources!["Finances"] == 10000 - (bought ? 500 : 0)
                      && acquired.CrusadeResources["Favors"] == 10000 - (seized ? 50 : 0) - (credit ? 100 : 0)
                      && !acquired.Has("seelah.diamond_held"),
                    "Seelah acquisition or second stone was charged twice or lost its price.");
                var end = S("seelah.trickster.epilogue.pickpocket").Nodes.Single();
                var shown = Rules.VisibleParagraphs(end, given).ToList();
                check(shown.Count(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[seelah.ending_unfinished/start][seelah.trickster.epilogue.pickpocket/end/paragraph/0][seelah.trickster.epilogue.pickpocket/end/paragraph/1]")) == 1
                      && SurfaceIds.Has(SurfaceIds.Of(story, shown.Single(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[seelah.ending_unfinished/start][seelah.trickster.epilogue.pickpocket/end/paragraph/0][seelah.trickster.epilogue.pickpocket/end/paragraph/1]"))), "[seelah.trickster.epilogue.pickpocket/end/paragraph/0]")
                      && shown.Any(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[seelah.trickster.epilogue.pickpocket/end/paragraph/12][seelah.trickster.epilogue.papers/end/paragraph/7]")) == bought,
                    "Seelah's epilogue contradicts its acquisition history.");
                // Node-level histories: the neutral refusal covers paid and unpaid roads.
                // Keep the engine-generated abort at answer index 10; no early splice shifts it.
                // The list here was given through the actual waking, not an invented training success.
                foreach (string commitId in new[] { "seelah.trickster.dismissed.commit", "seelah.trickster.dismissed.commit_visit" })
                {
                    var refusal = S(commitId).Nodes.Single(n => n.Id == "answer").Choices
                        .Where(c => c.Next == "no_stones" || c.Next == "no_stones_paid")
                        .Where(c => Rules.ChoiceAvailable(c, given)).ToList();
                    check(refusal.Count == 1 && refusal.Single().Next == "no_stones",
                        "Seelah repayment refusal uses the wrong seller history, including its visit twin.");
                    var page = S(commitId).Nodes.Single(n => n.Id == refusal.Single().Next);
                    check(page.Choices.Single().Set.SequenceEqual(new[] { "seelah.trickster.declined" }),
                        "Seelah repayment refusal invents successful training or changes her no.");
                }
            }
        }

        // Trk_Seelah_Wakes: her price for getting up.
        var woke = Program.Walk(wakes, standing);
        check(woke.Any(r => r.Has("seelah.trickster.death_returned")) && woke.Any(r => r.Has("seelah.trickster.cost.keeps_it"))
              && woke.All(r => r.Has("seelah.trickster.woke")), "Trk_Seelah_Wakes failed.");

        // Trk_Seelah_Dead_NoBody: no retained unit; the rite by rider, and she comes to Drezen.
        var nobody = World(story, 5, "trickster", "trickster.ever", "seelah_dead", "seelah.diamond_held");
        check(Rules.Available(story, effects, nobody) && !Any(nobody, pick, late, papers), "Trk_Seelah_Dead_NoBody: wrong device set.");
        // Q10 r2: the rider's four days are real. Dispatch sets stones_sent only; the chaplain's note waits >= 96 h; she
        // arrives (returned, correspondent, presence) two days after it, never before.
        var reply = S("seelah.trickster.dead.effects_reply");
        var arrival = S("seelah.trickster.dead.effects_arrival");
        var dispatches = Program.Walk(effects, nobody).Where(r => r.Has("seelah.trickster.stones_sent")).ToList();
        check(dispatches.Count == 4 && dispatches.All(r => !r.Has(Returned) && !r.Has("seelah.trickster.correspondent")
              && r.Has("seelah.trickster.cost.holds_her_death")) && Choices(effects).Count(c => c.RemoveItem == Diamond) == 1,
            "Trk_Seelah_Dead_NoBody: the rider rite returns her before the rider is back, or sets the wrong flags.");
        Snapshot NoBodyArrives(Snapshot dispatched, string name)
        {
            var justSent = After(story, dispatched, 1);
            check(!justSent.Has("seelah.trickster.in_drezen") && !Any(justSent, effects, reply, arrival, stay),
                name + ": something opens straight after the rider leaves.");
            var waiting = After(story, dispatched, 95);
            check(!Rules.Available(story, reply, waiting) && !waiting.Has("seelah.trickster.in_drezen"), name + ": the note comes before 96 h.");
            var noted = After(story, dispatched, 96);
            check(Rules.Available(story, reply, noted) && !Rules.Available(story, stay, noted), name + ": no note at 96 h, or she is in Drezen early.");
            var replied = Program.Walk(reply, noted).Single();
            check(!replied.Has(Returned) && !Rules.Available(story, arrival, After(story, replied, 47)), name + ": she arrives with the note.");
            var come = After(story, replied, 48);
            check(Rules.Available(story, arrival, come), name + ": she never arrives.");
            var arrived = Program.Walk(arrival, come).Single();
            check(arrived.Has(Returned) && arrived.Has("seelah.trickster.correspondent") && arrived.Has("seelah.started"),
                name + ": the arrival does not return her.");
            return arrived;
        }
        var inTown = After(story, NoBodyArrives(dispatches[0], "Trk_Seelah_Dead_NoBody"), 30);
        check(inTown.Has("seelah.trickster.in_drezen") && Rules.Available(story, stay, inTown) && !Rules.Available(story, wakes, inTown),
            "Trk_Seelah_Dead_NoBody: she never comes to Drezen, or wakes into a party she is not in.");
        check(!Rules.Available(story, effects, After(story, dispatches[0], 500)), "The rider rite reopens after dispatch.");

        // Q10 r2: Seelah's word on the seller, per caught-lift answer; branch-true epilogue openers.
        var sellerHub = S("seelah.trickster.dead.seller_word");
        var sellerTavern = S("seelah.trickster.dead_no_unit.seller_word");
        foreach (var (flag, page) in new[] { ("broker_knows", "concealed"), ("seller_taken", "taken"), ("seller_paid", "paid") })
        {
            var hubWorld = After(story, raised.Single(r => r.Has("seelah.trickster.cost." + flag)), 1, "seelah_dead", "revive.seelah.available");
            hubWorld = After(story, Program.Walk(wakes, hubWorld).First(), 30);
            var heard = new HashSet<string>();
            Program.Walk(sellerHub, hubWorld, (p, _) => heard.Add(p));
            check(Rules.Available(story, sellerHub, hubWorld) && heard.Contains(page) && heard.Count == 2, "Seelah's word on the seller is wrong for " + flag);
            var noBody = After(story, NoBodyArrives(Program.Walk(effects, nobody).Single(r => r.Has("seelah.trickster.cost." + flag)), flag), 30);
            check(Rules.Available(story, sellerTavern, noBody) && !Rules.Available(story, sellerHub, noBody), "No-unit seller word missing for " + flag);
        }
        var cleanLift = raised.Single(r => !r.Has("seelah.trickster.cost.broker_knows") && !r.Has("seelah.trickster.cost.seller_taken")
            && !r.Has("seelah.trickster.cost.seller_paid"));
        check(!Rules.Available(story, sellerHub, After(story, Program.Walk(wakes, After(story, cleanLift, 1, "seelah_dead", "revive.seelah.available")).First(), 30)),
            "Seelah asks about a seller the Commander never faced.");
        var pocketEnd = S("seelah.trickster.epilogue.pickpocket").Nodes.Single();
        string EndText(Snapshot w) => string.Join("\n", Rules.VisibleParagraphs(pocketEnd, w).Select(p => SurfaceIds.Of(story, p)));
        var bierEnd = EndText(raised[0]);
        var riderEnd = EndText(inTown);
        check(SurfaceIds.Has(bierEnd, "[seelah.trickster.epilogue.pickpocket/end/paragraph/0]") && !SurfaceIds.Has(bierEnd, "[seelah.trickster.epilogue.pickpocket/end/paragraph/1]")
              && SurfaceIds.Has(riderEnd, "[seelah.trickster.epilogue.pickpocket/end/paragraph/1]") && !SurfaceIds.Has(riderEnd, "[seelah.trickster.epilogue.pickpocket/end/paragraph/0]"),
            "The pickpocket epilogue merges the bier and the rider histories.");

        // Trk_Seelah_Dismissed: the papers, primed at the dismissal, come back in person.
        var herded = World(story, 5, "trickster", "trickster.ever", "seelah_gone", "seelah.trickster.primed");
        check(Rules.Available(story, papers, herded) && !Any(herded, late, papersLetter, pick, effects), "Trk_Seelah_Dismissed: wrong device set.");
        var back = Program.Walk(papers, herded);
        check(back.Count == 2 && back.All(r => r.Has(Returned) && r.Has("seelah.trickster.cost.herded")) && back.Count(r => r.Has("seelah.trickster.dared")) == 1,
            "Trk_Seelah_Dismissed: the papers do not return her.");
        check(Rules.Available(story, stay, After(story, back[0], 30)), "Trk_Seelah_Dismissed: no decision after the papers.");
        var failed = Program.Copy(herded); failed.Flags.Add("seelah.presence.failed"); failed.Hour += 200;
        check(Rules.Available(story, papersLetter, failed), "The papers letter twin does not open when the presence fails.");
        var caught = Program.Copy(herded); caught.Flags.Add("seelah.trickster.cost.caught");
        var caughtPages = new HashSet<string>();
        check(Program.Walk(papers, caught, (page, _) => caughtPages.Add(page)).Count == 2 && caughtPages.Contains("papers_caught"),
            "The caught variant blocks the papers or goes unsaid.");

        // Trk_Seelah_Dismissed_Late: the lift, now, at a worse price.
        var unprimed = World(story, 5, "trickster", "trickster.ever", "seelah_gone", "seelah.trickster.lift_lesson");
        check(Rules.Available(story, late, unprimed) && !Rules.Available(story, papers, unprimed), "Trk_Seelah_Dismissed_Late: wrong device set.");
        var lifts = Program.Walk(late, unprimed);
        check(lifts.Any(r => r.Has("seelah.trickster.primed") && r.Has("seelah.trickster.cost.late") && !r.Has("seelah.trickster.cost.caught"))
              && lifts.Any(r => r.Has("seelah.trickster.cost.caught")) && lifts.Any(r => r.Has("seelah.trickster.declined")),
            "Trk_Seelah_Dismissed_Late: lifted, caught or let go is missing.");
        var dcs = Choices(late).Where(c => c.Check != null).Select(c => (c.Check!.DC, lessoned: c.Requires.Contains("seelah.trickster.lift_lesson"))).ToList();
        check(dcs.Single(d => d.lessoned).DC == 15 && dcs.Single(d => !d.lessoned).DC == 25, "The lesson does not make the lift easier.");
        var letGo = lifts.Single(r => r.Has("seelah.trickster.declined"));
        check(!Any(After(story, letGo, 500), devices), "A return survives her being let go.");

        // Trk_Seelah_Commit: a romance, then her choice; the threshold, the cut, the morning.
        var courted = World(story, 5, "trickster", "trickster.ever", "seelah_gone", Returned, "seelah.trickster.stay_decided",
            "seelah.trickster.stays_near", "seelah.started", "seelah.kissed");
        check(courted.Has("seelah.romance") && Rules.Available(story, commit, courted) && !Rules.Available(story, second, courted),
            "Trk_Seelah_Commit: commit unavailable, or a second ask before any no.");
        var pages = new HashSet<string>();
        var kept = Program.Walk(commit, courted, (page, _) => pages.Add(page));
        check(kept.Count(r => r.Has("seelah.committed")) == 2 && pages.Contains("threshold") && pages.Contains("morning_near")
              && !pages.Contains("morning_far"), "Trk_Seelah_Commit: the committing branches or the morning are wrong.");

        // Trk_Seelah_Refusal: without a romance she offers friendship or the door; her no opens one priced ask.
        var friends = World(story, 5, "trickster", "trickster.ever", "seelah_gone", Returned, "seelah.trickster.stay_decided", "seelah.trickster.goes_far",
            "seelah.trickster.courted");
        var answers = Program.Walk(commit, friends);
        check(Rules.Available(story, commit, friends) && answers.All(r => !r.Has("seelah.committed"))
              && answers.Any(r => r.Has("seelah.trickster.friends")), "Trk_Seelah_Refusal: a romantic commit without a romance.");
        var no = answers.Single(r => r.Has("seelah.trickster.declined"));
        check(!no.Has("kiana.closed") && !no.Has("jannah.closed") && !Rules.Available(story, commit, After(story, no, 100)),
            "Trk_Seelah_Refusal: her no touched another route, or the commit reopens.");
        check(!Rules.Available(story, second, After(story, no, 100)), "A second ask without a romance.");
        var loved = After(story, no, 100); loved.Flags.Add("seelah.lovers"); Rules.Complete(story, loved);
        var asked = Program.Walk(second, loved);
        check(Rules.Available(story, second, loved) && asked.Any(r => r.Has("seelah.committed") && r.Has("seelah.trickster.cost.robbed_back"))
              && asked.Any(r => r.Has("seelah.closed")), "Trk_Seelah_Refusal: the priced second ask is wrong.");
        // Q10 r2 (COX): the repaired romance keeps its Last Call coda; the refusal stays as history (declined), the coda's
        // own override (declined -> committed) and the reconciliation flag carry it.
        var coda = S("seelah.lastcall.page");
        Snapshot AtLastCall(Snapshot w)
        {
            var end = After(story, w, 200);
            end.Flags.Add("trickster.lastcall.taken"); end.Flags.Add("ending.trickster");
            Rules.Complete(story, end);
            return end;
        }
        var reconciled = asked.Single(r => r.Has("seelah.committed"));
        check(reconciled.Has("seelah.trickster.declined") && reconciled.Has("seelah.trickster.reconciled")
              && AtLastCall(reconciled).Has("lastcall.active") && Rules.Available(story, coda, AtLastCall(reconciled))
              && !Rules.Available(story, S("seelah.trickster.epilogue.refused"), AtLastCall(reconciled)),
            "The second ask's yes loses Seelah's Last Call coda, or still plays her refusal.");
        check(!Rules.Available(story, coda, AtLastCall(asked.Single(r => r.Has("seelah.closed")))), "Her goodbye still gets the coda.");
        var death = World(story, 5, "trickster", "trickster.ever", "seelah_dead", Returned, "seelah.trickster.correspondent",
            "seelah.trickster.cost.holds_her_death", "seelah.trickster.stay_decided", "seelah.trickster.courted");
        var noPages = new HashSet<string>();
        Program.Walk(commit, death, (page, _) => noPages.Add(page));
        check(noPages.Contains("no_death") && !noPages.Contains("no"), "Her no does not name the death in the Commander's pocket.");

        // Q10 (Sol INT/HOW): a fresh return has no kiss behind it. Walk the actual presence scenes from the native dismissal
        // and from the no-unit death, with no authored romance, to a reachable commit; then the same with Fye's anchor failed
        // and no contact at all, through the visit twins.
        var courtship = S("seelah.trickster.after.courtship");
        check(new[] { courtship }.All(s => s.ContactUnit == Npc && s.InteractionHub == "seelah.presence" && s.AnswerLists.Length == 0),
            "The courtship left the presence hub.");
        Snapshot? Pick(List<Snapshot> outcomes, string flag) => outcomes.FirstOrDefault(r => r.Has(flag));
        void FreshReturnReachesCommit(string name, Snapshot returned, Scene stayScene, Scene courtScene, Scene commitScene)
        {
            check(!returned.Has("seelah.romance") && Rules.Available(story, stayScene, returned), name + ": no decision after the return.");
            var decided = Program.Walk(stayScene, returned).First(r => r.Has("seelah.trickster.stay_decided"));
            var waiting = After(story, decided, 60);
            check(!Rules.Available(story, commitScene, waiting) && Rules.Available(story, courtScene, waiting),
                name + ": the commit opens before any courtship, or the courtship never opens.");
            var courted = Program.Walk(courtScene, waiting);
            check(courted.All(r => r.Has("seelah.trickster.courted")) && courted.Any(r => r.Has("seelah.trickster.tavern_kissed"))
                  && courted.Any(r => !r.Has("seelah.trickster.tavern_kissed")), name + ": the courtship lacks the kiss or the friend.");
            var kissed = After(story, Pick(courted, "seelah.trickster.tavern_kissed")!, 60);
            check(kissed.Has("seelah.romance") && Rules.Available(story, commitScene, kissed)
                  && Program.Walk(commitScene, kissed).Any(r => r.Has("seelah.committed")), name + ": no commit after the kiss.");
            var friendly = After(story, courted.First(r => !r.Has("seelah.trickster.tavern_kissed")), 60);
            var answers = Program.Walk(commitScene, friendly);
            check(Rules.Available(story, commitScene, friendly) && answers.All(r => !r.Has("seelah.committed"))
                  && answers.Any(r => r.Has("seelah.trickster.friends")), name + ": the friend road commits, or is closed.");
        }
        var freshHerded = World(story, 5, "trickster", "trickster.ever", "seelah_gone", "seelah.trickster.primed");
        FreshReturnReachesCommit("Dismissal walk", After(story, Program.Walk(papers, freshHerded)[0], 30), stay, courtship, commit);
        var freshNobody = World(story, 5, "trickster", "trickster.ever", "seelah_dead", "seelah.diamond_held");
        FreshReturnReachesCommit("No-unit walk", After(story, NoBodyArrives(Program.Walk(effects, freshNobody).First(r => r.Has("seelah.trickster.stones_sent")), "No-unit walk"), 30),
            stay, courtship, commit);

        var stayVisit = S("seelah.trickster.after.stay_or_go_visit");
        var courtVisit = S("seelah.trickster.after.courtship_visit");
        var commitVisit = S("seelah.trickster.dismissed.commit_visit");
        var secondVisit = S("seelah.trickster.dismissed.second_ask_visit");
        check(new[] { stayVisit, courtVisit, commitVisit, secondVisit }.All(s => s.Remote && s.ContactUnit == null && s.Kind == "visit"
              && s.Requires.Contains("seelah.presence.failed")), "The failed-anchor visit twins are not remote visits.");
        var noContact = World(story, 5, "trickster", "trickster.ever", "seelah_gone", "seelah.trickster.primed", "seelah.presence.failed");
        noContact.AvailableContacts.Clear();
        noContact.Hour += 200;
        Rules.Complete(story, noContact);
        check(!Any(noContact, papers, stay, courtship, commit, second) && Rules.Available(story, papersLetter, noContact),
            "Failed anchor: a presence scene opens without a contact, or the papers letter does not.");
        var mailed = After(story, Program.Walk(papersLetter, noContact).Single(), 30);
        check(mailed.AvailableContacts.Count == 0, "The failed-anchor walk gained a contact.");
        FreshReturnReachesCommit("Failed-anchor walk", mailed, stayVisit, courtVisit, commitVisit);
        var spurned = Program.Walk(commitVisit, After(story, Pick(Program.Walk(courtVisit, After(story,
            Program.Walk(stayVisit, mailed).First(), 30)), "seelah.trickster.tavern_kissed")!, 60)).Single(r => r.Has("seelah.trickster.declined"));
        var secondAsked = Program.Walk(secondVisit, After(story, spurned, 100));
        check(Rules.Available(story, secondVisit, After(story, spurned, 100)) && secondAsked.Any(r => r.Has("seelah.committed"))
              && secondAsked.Any(r => r.Has("seelah.closed")), "Failed anchor: the second ask is unreachable, or lacks its yes or its no.");
        // Q10 r3: the late entry. Papers -> decision -> the courtship kiss, the commit never taken: the qualified late
        // commit (late_committed + romance) plays the Last Call coda, with seelah.committed never set; the friend road and
        // an unreconciled no do not.
        var lateBack = After(story, Program.Walk(papers, herded)[0], 30);
        var lateDecided = After(story, Program.Walk(stay, lateBack).First(r => r.Has("seelah.trickster.stays_near")), 60);
        var lateCourted = Program.Walk(courtship, lateDecided);
        var lateKissed = AtLastCall(lateCourted.First(r => r.Has("seelah.trickster.tavern_kissed")));
        check(!lateKissed.Has("seelah.committed") && lateKissed.Has("seelah.trickster.late_committed") && lateKissed.Has("seelah.trickster.late_coda")
              && Rules.Available(story, coda, lateKissed) && Rules.Available(story, S("seelah.trickster.epilogue.commit"), lateKissed),
            "The qualified late commit loses Seelah's Last Call coda.");
        check(!Rules.Available(story, coda, AtLastCall(lateCourted.First(r => !r.Has("seelah.trickster.tavern_kissed")))),
            "The friend road (no romance) plays the coda.");
        var lateNo = Program.Walk(commit, After(story, lateCourted.First(r => r.Has("seelah.trickster.tavern_kissed")), 60))
            .First(r => r.Has("seelah.trickster.declined"));
        check(!Rules.Available(story, coda, AtLastCall(lateNo)), "An unreconciled no plays the coda.");
        var lateFriend = Program.Walk(commit, After(story, lateCourted.First(r => !r.Has("seelah.trickster.tavern_kissed")), 60))
            .First(r => r.Has("seelah.trickster.friends"));
        check(!Rules.Available(story, coda, AtLastCall(lateFriend)) && !Rules.Available(story, commitVisit, After(story, lateFriend, 100)),
            "The friend answer plays the coda, or the commit reopens as a visit.");
        var visitYes = secondAsked.Single(r => r.Has("seelah.committed"));
        check(visitYes.Has("seelah.trickster.reconciled") && Rules.Available(story, coda, AtLastCall(visitYes)),
            "Failed anchor: the visit second ask's yes loses the Last Call coda.");

        // Q10 r3: the no-unit seller word has a failed-anchor visit twin; one completion closes both.
        var sellerVisit = S("seelah.trickster.dead_no_unit.seller_word_visit");
        check(sellerVisit.Remote && sellerVisit.ContactUnit == null && sellerVisit.Kind == "visit" && sellerVisit.Requires.Contains("seelah.presence.failed"),
            "The seller word's visit twin is not a remote visit.");
        var anchorless = World(story, 5, "trickster", "trickster.ever", "seelah_dead", "seelah.diamond_held", "seelah.presence.failed");
        anchorless.AvailableContacts.Clear();
        var anchorlessBack = After(story, NoBodyArrives(Program.Walk(effects, anchorless).Single(r => r.Has("seelah.trickster.cost.broker_knows")), "Failed-anchor seller"), 30);
        check(anchorlessBack.AvailableContacts.Count == 0 && Rules.Available(story, sellerVisit, anchorlessBack)
              && !Rules.Available(story, S("seelah.trickster.dead_no_unit.seller_word"), anchorlessBack),
            "Failed anchor: Seelah's word on the seller is unreachable without a contact.");
        var sellerDone = After(story, Program.Walk(sellerVisit, anchorlessBack).Single(), 30);
        sellerDone.AvailableContacts.Add(Npc);
        check(sellerDone.Has("seelah.trickster.seller_heard") && !Any(sellerDone, sellerVisit, S("seelah.trickster.dead_no_unit.seller_word")),
            "The seller word replays through its twin.");
        // Q10 r3: Irabeth's "rob you back" bark only when the list was kept at the waking; the given-back sibling otherwise.
        var irabethKept = S("seelah.trickster.dead.react_irabeth");
        var irabethGiven = S("seelah.trickster.dead.react_irabeth_given");
        check(irabethKept.Requires.Contains("seelah.trickster.woke") && irabethKept.Requires.Contains("seelah.trickster.cost.keeps_it") && irabethGiven.Requires.Contains("seelah.trickster.death_returned"), "Irabeth's rob-you-back line is not gated on the kept list.");

        // Trk_Seelah_PathFailed: canon fate stands after the path fails.
        var failedPath = World(story, 5, "trickster.was", "trickster.ever", "trickster.failed", "seelah_dead", "revive.seelah.available");
        check(!Any(failedPath, pick, effects, late), "Trk_Seelah_PathFailed: a device opened after the path failed.");

        // Registered route: G6(b) overrides; letters lift only for a Seelah back in the party; the retired revive.
        foreach (var s in story.Scenes.Where(s => s.Relationship == "seelah" && !s.Id.StartsWith("seelah.trickster.", StringComparison.Ordinal)))
            foreach (var flag in new[] { "seelah_dead", "seelah_gone" }.Where(s.Forbids.Contains))
                check(s.ForbidOverrides.TryGetValue(flag, out var value)
                      && value == (s.Remote ? "seelah.trickster.rejoined" : Returned), "G6(b) override missing: " + s.Id + "/" + flag);
        check(S("seelah.fate_life").Forbids.Contains("trickster.ever") && S("seelah.fate_return").Forbids.Contains(Returned),
            "The old Trickster revive is not retired.");
        foreach (var id in new[] { "irabeth.trickster.dead.react_seelah", "irabeth.trickster.killed.react_seelah" })
            if (story.Scenes.Any(s => s.Id == id))
                check(S(id).ForbidOverrides.TryGetValue("seelah_dead", out var d) && d == Returned
                      && S(id).ForbidOverrides.TryGetValue("seelah_gone", out var g) && g == Returned, "Irabeth's Seelah bark lacks G6(b): " + id);
        var together = World(story, 5, "seelah.committed", "seelah.chosen_future", "seelah.short_future_chosen", "seelah.souls_returned", "seelah_gone", Returned);
        check(Rules.Available(story, S("seelah.ending_together"), together), "A returned Seelah loses her registered ending.");
        check(story.Scenes.Where(s => s.Relationship == "seelah" && s.Reaction).All(s => Choices(s).All(c => !c.Set.Contains("seelah.closed"))),
            "A reaction closes her route.");
    }
}
