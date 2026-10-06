using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Camellia, Trickster (Writer/handoffs/trickster/camellia.md; F12, the spoken death): "Go on, then. Die convincingly."
// One block per spec rules test (Trk_Camellia_*), the shape of each hook, and the arc around the device (camellia_masks,
// camellia_evenings, camellia_cards, camellia_days, camellia_last): every beat reachable on its own branch, the intimate
// scenes only after the commit, and the other routes' Camellia reactions lifted by her return.
internal static class CamelliaTricksterTests
{
    private const string Unit = "397b090721c41044ea3220445300e1b8";
    private const string Hub = "589d83230bbbfd04bb1220ee4fef1ce1";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Fye = "0f12118177d102f428a3b30b15b132eb";
    private const string P = "camellia.trickster.";
    private const string Killed = "camellia.killed";
    private const string Dead = "camellia.dead";
    private const string Returned = P + "returned";
    private const string Committed = "camellia.committed";
    private const string Closed = "camellia.closed";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        // eng8-q8f: the late-coffin positive pays its existing sexton price.
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 100 } };
        // end eng8-q8f
        state.Flags.UnionWith(flags);
        // Paid coffin-copy positives retain the native death witness from the actual prior death.
        if (flags.Contains(Killed) && flags.Contains(Returned) && flags.Contains(P + "cost.knows_you_tried"))
            state.Flags.Add(P + "native_death_observed");
        // These positive predicate fixtures represent an already accepted route.
        // Coarse-key negatives are independent in PayoffDepartureRulesTests.
        foreach (var rel in story.Relationships)
            if (flags.Contains(rel.Value.CommittedFlag) && story.Derived.ContainsKey(rel.Key + ".payoff.ordinary"))
                HouseholdTests.Earn(story, state, rel.Key + ".payoff.ordinary");
        foreach (var context in flags.Where(story.Derived.ContainsKey))
            HouseholdTests.Earn(story, state, context);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Unit);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 300;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        Rules.Complete(story, later);
        foreach (var flag in later.Flags.Where(f => !later.Times.ContainsKey(f)).ToList()) later.Times[flag] = state.Hour;
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        bool Avail(Scene s, Snapshot w) => Rules.Available(story, s, w);
        Choice Ch(Scene s, string node, int index) => s.Nodes.Single(n => n.Id == node).Choices[index];
        // eng8-q8f: outcomes that actually traverse the named node and saved answer index.
        List<Snapshot> Through(Scene scene, Snapshot w, string node, int index)
        {
            // eng8-q8f: prove the edge, including empty/shared Set arrays.
            var hits = Program.WalkVia(scene, w, node, index);
            // end eng8-q8f
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        Snapshot Take(Scene scene, Snapshot w, string node, int index, params string[] also)
        {
            var hit = Through(scene, w, node, index).FirstOrDefault(r => also.All(r.Has));
            check(hit != null, "No outcome of " + scene.Id + " through " + node + "[" + index + "] with " + string.Join(", ", also));
            return hit ?? w;
        }

        var rel = story.Relationships["camellia"];
        var setupHub = S(P + "killed.setup_hub");
        var setupQ3 = S(P + "killed.setup_q3");
        var setupQ1 = S(P + "killed.setup_q1");
        var late = S(P + "killed.late_curtain");
        var performance = S(P + "killed.performance");
        var letter = S(P + "killed.performance_letter");
        var overacting = S(P + "dead.overacting");
        var grave = S(P + "beat.her_own_grave");
        var due = S(P + "beat.spirits_due");
        var lesson = S(P + "beat.lesson");
        var lessonCamp = S(P + "beat.lesson_camp");
        var terms = S(P + "returned.terms");
        var termsCamp = S(P + "returned.terms_camp");
        var test = S(P + "returned.test");
        var testCamp = S(P + "returned.test_camp");
        var oath = S(P + "kills_answered.oath");
        var oathCamp = S(P + "kills_answered.oath_camp");
        var body = S(P + "react.anevia_body");

        // --- Shape: the relationship, the revival, the presence. ------------------------------------------------------
        check(rel.StartedFlag == "camellia.started" && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.SequenceEqual(new[] { Killed, Dead, "camellia.kicked_out" })
              && rel.UnavailableOverrides.Count == 3 && rel.UnavailableOverrides[Killed] == P + "cost.knows_you_tried" && rel.UnavailableOverrides[Dead] == P + "coffin_life"
              // Q8 (Sol INT): the native Q3 kill co-holds kicked_out; only a kick-out WITHOUT the kill stays closure.
              && rel.UnavailableOverrides["camellia.kicked_out"] == P + "killed_held"
              && story.Derived[P + "killed_held"].Single().SequenceEqual(new[] { Killed })
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "dead_otherwise", "killed_by_commander" })
              && rel.TricksterAccess["killed_by_commander"].Detect.SequenceEqual(new[] { Killed, Dead })
              && rel.TricksterAccess["dead_otherwise"].Detect.SequenceEqual(new[] { Dead, "!" + Killed }),
            "Camellia's relationship does not match the spec (a kick-out is closure, never lifted).");
        check(story.Revivals.TryGetValue("camellia", out var revival) && revival.Unit == Unit && revival.DeathFlag == Dead
              && revival.Relationship == "camellia", "Her revival entry is missing or wrong.");
        check(story.Presences.TryGetValue("camellia.presence", out var presence) && presence.Unit == Unit && presence.Mode == "spawn-copy"
              && presence.At?.NearUnit == Fye && presence.At.Side == "left" && presence.Dialog == "hub" && presence.AnswerLists.Length == 0
              && presence.Requires.Contains(Killed) && presence.Requires.Contains(P + "primed") && presence.Forbids.Contains(Closed)
              && presence.MinChapter == 3 && presence.MaxChapter == 5,
            "The veiled Camellia at the far end of Fye's bar is missing or malformed.");

        // --- The joke, inline at each kill (E13 entry mythic, native continuation into the kill). ------------------------
        check(setupHub.AnswerLists.SequenceEqual(new[] { "74f66c9edaa71a644ba091fb1ff4a435" }) && setupHub.NativeReturnCue == "6f6ceeffe5e77dc42896e3e8b937b752"
              && setupHub.EntryMythic == "PlayerIsTrickster" && setupHub.ContactUnit == null
              && setupHub.Nodes.SelectMany(n => n.Choices).Where(c => c.NativeNext != null).All(c => c.NativeNext == "e433ac35761daa84b86b6b5e5c4fae11" && c.Set.Contains(P + "primed")),
            "The hub setup is not an inline Trickster answer on the kill list that continues into the native kill.");
        check(setupQ3.AnswerLists.SequenceEqual(new[] { "2199689753593844a8caceef5150ff4e" }) && setupQ3.NativeReturnCue == "1d0757c2ccde7034baa737419150bacd"
              && setupQ3.Chapters.SequenceEqual(new[] { 5 }) && Ch(setupQ3, "start", 0).NativeNext == "be5af575d343fdb49badcd32d8336996",
            "The Q3 setup is not on the verdict list in Chapter 5.");
        check(setupQ1.AnswerLists.SequenceEqual(new[] { "d977fae7974bb88419e51e2c33876aac" }) && setupQ1.EntryAlignment?.Direction == "Chaotic"
              && setupQ1.EntryAlignment.Value == 1 && Ch(setupQ1, "start", 0).NativeNext == "6d583904c4659fe478c2e26e9305ad4d",
            "The Q1 order is not on Anevia's results list with the native order's alignment.");
        foreach (var setup in new[] { setupHub, setupQ3, setupQ1 })
            check(setup.Forbids.Contains(Killed) && setup.Forbids.Contains(Dead) && setup.Forbids.Contains(P + "primed") && setup.Requires.Contains("trickster"),
                "A setup runs after the death or without live Trickster power: " + setup.Id);

        // Trk_Camellia_KilledQ1Order
        var q1 = World(story, 3, "trickster");
        check(Avail(setupQ1, q1), "Trk_Camellia_KilledQ1Order: the order is not offered.");
        Take(setupQ1, q1, "start", 0, P + "primed", P + "primed_by_order");

        // Trk_Camellia_KilledPrimed
        // The device is hers: before the kill the Commander bleeds into her bowl and bargains with her battle spirits
        // (cards.a_bowl_for_mireya, node bargain); on the third night they give her back and she claws at the lid
        // (killed.third_night). Unbargained, the Commander may bargain at the open coffin, dearer (Evil 1).
        var third = S(P + "killed.third_night");
        var bowl = S(P + "cards.a_bowl_for_mireya");
        check(bowl.Forbids.Contains(Killed) && Ch(bowl, "paid", 0).Set.Contains(P + "spirits_bargained") && Ch(bowl, "paid", 0).Set.Contains(P + "cost.blood_bargain"),
            "The bargain with her spirits is not made in blood, before the kill.");
        var buried = World(story, 3, "trickster", "trickster.ever", Killed, Dead, P + "primed", P + "spirits_bargained");
        check(!Avail(performance, buried) && Avail(third, Later(story, buried, 100)), "The third night does not stand between the kill and her return.");
        check(third.Remote && third.Chapters.SequenceEqual(new[] { 3, 5 }), "The third night is not a Drezen rest page.");
        var raisedNight = Take(third, Later(story, buried, 100), "dug", 0, P + "raised");
        var cold = Later(story, World(story, 3, "trickster", "trickster.ever", Killed, Dead, P + "primed"), 100);
        Take(third, cold, "unbargained", 0, P + "raised", P + "cost.bargain_late", P + "spirits_bargained");
        check(Ch(third, "unbargained", 0).Alignment?.Direction == "Evil", "The late bargain at the coffin is not dearer (Evil 1).");
        // ENGINE-Q5: priming or paying a bargain does not perform the later return off the live path.
        var failedPrimed = Later(story, World(story, 3, "trickster.ever", "trickster.failed", Killed, Dead, P + "primed"), 100);
        check(!Avail(third, failedPrimed)
              && Ch(third, "unbargained", 0).Requires.Contains("trickster"),
            "A lost path still opens a new bargain over her coffin.");
        var failedPaid = Later(story, World(story, 3, "trickster.ever", "trickster.failed", Killed, Dead, P + "primed", P + "spirits_bargained"), 100);
        check(!Avail(third, failedPaid), "A paid bargain performs a return after the path failed.");
        // Q8 (Sol BEL): the scratching belongs to the prepared branch only.
        check(Avail(performance, Later(story, raisedNight, 100)), "The veiled mourner does not follow the raise.");
        var primed = World(story, 5, "trickster", "trickster.ever", Killed, Dead, P + "primed", P + "raised");
        check(Avail(performance, primed) && !Avail(overacting, primed) && !Avail(late, primed) && !Avail(letter, primed),
            "Trk_Camellia_KilledPrimed: only the veiled mourner should be available.");
        check(performance.InteractionHub == "camellia.presence" && performance.ContactUnit == Unit && performance.Areas.SequenceEqual(new[] { Drezen }),
            "The return is not met in person at her presence.");
        var back = Take(performance, primed, "primed", 0, Returned, P + "cost.knows_you_tried", "camellia.started");
        // The trick's mechanism and price are on the page: the stolen scroll read over her coffin (how), and her death kept
        // by the Commander's own hands: her empty coffin filled, with a hanged deserter (Evil 1) or stones; refusing ends it.
        check(performance.Nodes.Any(n => n.Id == "how") && Ch(performance, "primed", 0).Next == "register",
            "The return does not show how she got out, or skips the empty coffin.");
        Take(performance, primed, "fill", 0, P + "cost.grave_filled", P + "cost.gallows", Returned);
        Take(performance, primed, "fill", 1, P + "cost.grave_filled", Returned);
        check(Ch(performance, "fill", 0).Alignment?.Direction == "Evil" && Ch(performance, "fill", 1).Alignment == null,
            "Carrying a hanged man to her grave is not an Evil act, or the stones are.");
        check(Through(performance, primed, "unsigned", 0).All(r => r.Has(Closed) && r.Has(P + "declined")),
            "Refusing to fill her grave does not end the return.");

        // Trk_Camellia_KilledWithDeadEtude
        check(Avail(performance, World(story, 3, "trickster", "trickster.ever", Killed, Dead, P + "primed", P + "raised")),
            "Trk_Camellia_KilledWithDeadEtude: the killed state co-holds her retained-death etude and must still return.");

        // Trk_Camellia_KilledLate
        var unprimed = World(story, 3, "trickster", "trickster.ever", Killed, Dead);
        check(Avail(late, unprimed) && !Avail(performance, unprimed), "Trk_Camellia_KilledLate: the late curtain should be the only way in.");
        check(late.Remote && late.Chapters.SequenceEqual(new[] { 3, 5 }), "The late curtain is not a Chapter 3 and 5 rest page.");
        // A kill taken through the native verdict in Chapter 5 (FinalTruth) has the same way back, on the same terms.
        check(Avail(late, World(story, 5, "trickster", "trickster.ever", Killed, Dead)), "Trk_Camellia_KilledLate: a Chapter 5 kill has no way back.");
        // eng8-q8d: Chapter 5 failure folds the price into either coffin delivery.
        check(letter.Chapters.SequenceEqual(new[] { 3 }) && new[] { late, third }.All(s => s.Nodes.Any(n => n.Id == "eng8.price")),
            "Chapter 5 failed placement lacks its folded coffin agreement, or still adds a letter.");
        // end eng8-q8d
        check(Ch(late, "choose", 0).Crusade?.Resource == "Finances" && Ch(late, "choose", 0).Crusade!.Amount == -100,
            "The sexton is not paid for in Finances (-100).");
        check(Ch(late, "coffin", 0).Mythic == "PlayerIsTrickster", "The line said to the corpse is not a native [Trickster] answer.");
        Take(late, unprimed, "coffin", 0, P + "primed", P + "cost.late", P + "raised");
        check(Ch(late, "scroll", 0).Set.Contains(P + "cost.blood_bargain"), "The late curtain's bargain is not paid in the Commander's blood.");
        Take(late, unprimed, "choose", 1, P + "declined", Closed);

        // Trk_Camellia_KilledAfterFailure
        var q3Kill = World(story, 5, "trickster", "trickster.ever", Killed, Dead, "camellia.kicked_out");
        check(Avail(late, q3Kill), "A Q3 kill (kicked_out co-held with the kill) is closed as a dismissal.");
        var failed = World(story, 3, "trickster.ever", "trickster.failed", Killed);
        check(!Avail(late, failed) && !Avail(performance, failed), "Trk_Camellia_KilledAfterFailure: a lost path must not open a new trick.");

        // Trk_Camellia_DeadOtherwise
        var body_ = World(story, 5, "trickster", "trickster.ever", Dead, "revive.camellia.available");
        check(Avail(overacting, body_) && !Avail(performance, body_), "Trk_Camellia_DeadOtherwise: the body should hear it's overacting.");
        check(overacting.Recovery == "camellia" && Ch(overacting, "waking", 0).Revive == "camellia", "Her price does not raise her.");
        var raised = Take(overacting, body_, "waking", 0, Returned, P + "cost.spirits_owed", "camellia.started");
        // eng7-l07: the selected native resurrection clears the live companion death observation.
        raised.Flags.Remove(Dead); raised.Flags.Add("camellia.native_alive");
        Rules.RecordAvailabilityEvents(story, raised, new[] { "camellia.native_alive" }); Rules.Complete(story, raised);
        Take(overacting, body_, "refused", 0, P + "declined", Closed);

        // Trk_Camellia_Terms (killed branch; the lesson is its prerequisite)
        var termsWorld = World(story, 3, "trickster", "trickster.ever", Killed, Returned, P + "cost.knows_you_tried", P + "beat.lesson");
        check(Avail(terms, termsWorld) && !Avail(test, termsWorld), "Trk_Camellia_Terms: her price should come before her test.");
        var named = Take(terms, termsWorld, "price", 1, P + "cost.marked", P + "terms_named");
        check(Avail(test, Later(story, named, 100)), "Trk_Camellia_Terms: the test does not open after her price.");
        // Directive 2: no death is the price of her romance. Her prices are the Commander's own blood, or the Commander's name.
        check(Ch(terms, "price", 0).Set.Contains(P + "cost.bled") && Ch(terms, "price", 1).Set.Contains(P + "cost.marked")
              && Ch(terms, "price", 0).Alignment == null,
            "Her price is not the Commander's blood or the Commander's name.");

        // Trk_Camellia_Commit / Trk_Camellia_CommitRefused
        var commitWorld = World(story, 5, "trickster", "trickster.ever", Killed, Returned, P + "cost.knows_you_tried", P + "cost.marked", P + "terms_named");
        check(Avail(test, commitWorld), "Trk_Camellia_Commit: the test is not available.");
        var yes = Ch(test, "yes", 0);
        check(yes.Set.SequenceEqual(new[] { Committed }) && yes.Next == "threshold", "The named commit producer is not test/yes[0].");
        Take(test, commitWorld, "yes", 0, Committed);
        var refused = Through(test, commitWorld, "no", 0);
        check(refused.All(r => r.Has(Closed) && r.Has(P + "cost.asked_her_tame") && !r.Has(Committed)),
            "Trk_Camellia_CommitRefused: asking her to be tame must be her hard no.");
        check(Through(test, commitWorld, "guard", 0).All(r => r.Has(Closed) && !r.Has(Committed)), "Calling the guard must end it.");

        // Trk_Camellia_KickedOut: explicit closure; nothing of hers returns.
        var kicked = World(story, 5, "trickster", "trickster.ever", "camellia.kicked_out");
        check(!story.Scenes.Where(s => s.Relationship == "camellia" && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
                  .Any(s => s.TricksterDevice && Avail(s, kicked)), "Trk_Camellia_KickedOut: a dismissal must stay closed.");

        // Trk_Camellia_Oath (Nurah pair only; the Kaylessa pair waits for her route)
        var oathWorld = World(story, 5, "trickster", "trickster.ever", "nurah.trickster.returned", "nurah.dead_camellia");
        check(Avail(oathCamp, oathWorld), "Trk_Camellia_Oath: the living Camellia should hear about her kill that didn't take.");
        check(!Avail(oathCamp, World(story, 5, "trickster", "trickster.ever", "nurah.trickster.returned")),
            "Trk_Camellia_Oath: a Nurah the Commander executed is not Camellia's kill.");
        Take(oathCamp, oathWorld, "loophole", 0, P + "oath_loophole");
        check(oath.Nodes.Single(n => n.Id == "start").Choices.Count(c => c.Next == "nurah") == 1, "The oath does not route Nurah first.");
        check(Ch(oathCamp, "ask", 1).Alignment?.Direction == "Evil", "Feeding her someone else is not an Evil act.");
        // Trk_Camellia_OathSoana, and exclusivity: with both of her kills returned, exactly one route is offered (Nurah).
        var soanaWorld = World(story, 5, "trickster", "trickster.ever", "soana.trickster.returned", "soana.killed_by_camellia");
        check(Avail(oathCamp, soanaWorld), "Trk_Camellia_OathSoana: the Soana kill that didn't take does not open the oath.");
        foreach (var w in new[] { oathWorld, soanaWorld,
                                  World(story, 5, "trickster", "trickster.ever", "nurah.trickster.returned", "nurah.dead_camellia", "soana.trickster.returned", "soana.killed_by_camellia"),
                                  World(story, 5, "trickster", "trickster.ever", "nurah.dead_camellia", "soana.trickster.returned", "soana.killed_by_camellia") })
        {
            var shown = oathCamp.Nodes.Single(n => n.Id == "start").Choices.Where(c => Rules.Match(c.Requires, c.Forbids, w)).ToList();
            check(Avail(oathCamp, w) && shown.Count == 1, "The oath does not offer exactly one route for its world.");
        }
        check(!Avail(oathCamp, World(story, 5, "trickster", "trickster.ever", "soana.killed_by_camellia")),
            "Trk_Camellia_OathSoana: a Soana still dead is not a kill that didn't take.");
        // Trk_Camellia_OathKaylessa (closed with the Kaylessa route, its producer): her kill alone does not open the oath; her
        // return does, and the Kaylessa branch steps aside for an earlier pair (exactly one route per world).
        check(!Avail(oathCamp, World(story, 5, "trickster", "trickster.ever", "kaylessa.camellia_killed")),
            "The oath opened on a Kaylessa kill that is still dead.");
        var kaylessaWorld = World(story, 5, "trickster", "trickster.ever", "kaylessa.trickster.returned", "kaylessa.camellia_killed");
        check(Avail(oathCamp, kaylessaWorld), "Trk_Camellia_OathKaylessa: the Kaylessa kill that didn't take does not open the oath.");
        foreach (var w in new[] { kaylessaWorld,
                                  World(story, 5, "trickster", "trickster.ever", "kaylessa.trickster.returned", "kaylessa.camellia_killed", "nurah.trickster.returned", "nurah.dead_camellia"),
                                  World(story, 5, "trickster", "trickster.ever", "kaylessa.trickster.returned", "kaylessa.camellia_killed", "soana.trickster.returned", "soana.killed_by_camellia"),
                                  World(story, 5, "trickster", "trickster.ever", "kaylessa.trickster.returned", "kaylessa.camellia_killed", "nurah.dead_camellia") })
        {
            var shown = oathCamp.Nodes.Single(n => n.Id == "start").Choices.Where(c => Rules.Match(c.Requires, c.Forbids, w)).ToList();
            check(Avail(oathCamp, w) && shown.Count == 1, "The oath does not offer exactly one route for a world with Kaylessa's return.");
        }
        check(oathCamp.Nodes.Single(n => n.Id == "start").Choices.Where(c => Rules.Match(c.Requires, c.Forbids, kaylessaWorld)).Single().Next == "kaylessa",
            "Trk_Camellia_OathKaylessa: Kaylessa's world is not routed to her own node.");

        // Trk_Camellia_AneviaBody: the spirits' due arrives as Anevia's report.
        // Her killing is her nature after her return, not a price anyone paid: Anevia reports it once the lesson is taught.
        var owed = World(story, 3, "trickster", "trickster.ever", Returned, P + "beat.lesson");
        check(Avail(body, owed), "Trk_Camellia_AneviaBody: Anevia should report the body.");
        check(!Avail(body, World(story, 3, "trickster", "trickster.ever", Returned)), "The body turns up before her return has settled.");
        Take(body, owed, "start", 1, P + "cost.covered_murder");
        check(body.AnswerLists.SequenceEqual(new[] { "33960c7f7af40cd43b7f801a76c87a0b" }) && body.Reaction
              && body.ForbidOverrides["anevia_gone"] == "anevia.trickster.returned", "Anevia's report is not on her own hub, lifted by her return.");

        // --- The arc: before the kill (on her own companion hub, while the Trickster's ear is live). ------------------
        var living = new[] { "masks.two_lies", "masks.mireya", "masks.flies_at_a_window", "masks.the_funeral_i_would_like",
            "masks.a_dance_with_a_knife_in_it", "evening.the_puppy", "evening.the_salle", "evening.a_table_for_strangers",
            "cards.the_old_womans_deck", "cards.a_bowl_for_mireya", "day.the_language_of_flowers", "evening.the_gloves" }.Select(id => S(P + id)).ToArray();
        foreach (var s in living)
            check(s.AnswerLists.SequenceEqual(new[] { Hub }) && s.ContactUnit == Unit && s.Requires.Contains("trickster")
                  && s.Forbids.Contains(Killed) && s.Forbids.Contains(Dead) && s.Forbids.Contains("camellia.kicked_out"),
                "A living scene is not on her own hub, or runs after her death: " + s.Id);
        var alive = World(story, 3, "trickster");
        check(Avail(living[0], alive), "Two lies and a truth does not open the courtship.");
        var played = Take(living[0], alive, "yours", 0, P + "masks.game", P + "masks.out_lied");
        var later = Later(story, played, 100);
        check(Avail(S(P + "masks.mireya"), later) && Avail(S(P + "evening.the_puppy"), later), "The courtship does not continue after the game.");
        check(!Avail(S(P + "masks.flies_at_a_window"), later), "The Abyss scene opened outside Chapter 4.");
        var abyss = Later(story, played, 100); abyss.Chapter = 4; Rules.Complete(story, abyss);
        check(Avail(S(P + "masks.flies_at_a_window"), abyss), "The Abyss scene is not available in Chapter 4.");
        var ch5 = Later(story, played, 100); ch5.Chapter = 5; Rules.Complete(story, ch5);
        check(Avail(S(P + "masks.the_funeral_i_would_like"), ch5), "The funeral scene is not available in Chapter 5.");

        // --- After the return: the killed branch at her presence, the raised branch on her companion hub. -------------
        var killedBack = Later(story, back, 100);
        check(Avail(grave, killedBack) && !Avail(due, killedBack), "The killed Camellia does not take the Commander to her grave.");
        var visited = Take(grave, killedBack, "last", 0, P + "beat.grave");
        var toLesson = Later(story, visited, 100);
        check(Avail(lesson, toLesson) && !Avail(lessonCamp, toLesson), "The lesson is not met at her presence after the grave.");
        var taught = Take(lesson, toLesson, "steady", 0, P + "beat.lesson", P + "lesson.steady");
        check(Avail(terms, Later(story, taught, 100)), "Her price does not follow the lesson.");
        foreach (var twin in story.Scenes.Where(s => s.Id.StartsWith(P, StringComparison.Ordinal) && s.Id.EndsWith("_camp", StringComparison.Ordinal)))
        {
            var killedTwin = S(twin.Id.Substring(0, twin.Id.Length - "_camp".Length));
            check(killedTwin.InteractionHub == "camellia.presence" && killedTwin.Requires.Contains(Killed) && killedTwin.Requires.Contains(Returned)
                  && twin.AnswerLists.SequenceEqual(new[] { Hub }) && twin.InteractionHub == null && twin.Forbids.Contains(Killed),
                "Scene twins do not split the two hosts: " + twin.Id);
            check(!killedTwin.Nodes.SelectMany(n => n.Choices).Any(c => c.Forbids.Contains(Killed))
                  && !twin.Nodes.SelectMany(n => n.Choices).Any(c => c.Requires.Contains(Killed)),
                "A twin keeps the other branch's choices: " + twin.Id);
        }
        var raisedBack = Later(story, raised, 100);
        check(Avail(due, raisedBack) && !Avail(grave, raisedBack), "The raised Camellia does not name the spirits' due.");
        var dueNamed = Take(due, raisedBack, "after", 0, P + "beat.spirits_due");
        check(Avail(lessonCamp, Later(story, dueNamed, 100)), "The lesson is not on her companion hub after the spirits' due.");
        check(Avail(termsCamp, Later(story, Take(lessonCamp, Later(story, dueNamed, 100), "flinched", 0, P + "beat.lesson"), 100)),
            "Her price does not follow the lesson on her companion hub.");
        check(!testCamp.Requires.Contains(Killed), "The raised branch's test requires the killed state.");

        // --- Death is never the entry price: a Camellia who was never killed reaches the same lesson, price, test and commit
        // on her own companion hub, after the courtship's dance (the _alive twins). -------------------------------------
        foreach (var twin in story.Scenes.Where(s => s.Relationship == "camellia" && s.Id.EndsWith("_alive", StringComparison.Ordinal)))
            check(twin.AnswerLists.SequenceEqual(new[] { Hub }) && twin.InteractionHub == null && twin.Forbids.Contains(Killed)
                  && twin.Forbids.Contains(Dead) && twin.Forbids.Contains(Returned) && !twin.Requires.Contains(Returned)
                  && !twin.Nodes.SelectMany(n => n.Choices).Any(c => c.Requires.Contains(Killed) || c.Requires.Contains(Returned) || c.Requires.Contains(Dead)),
                "A living twin needs her death, or keeps the dead branches' choices: " + twin.Id);
        // Q8: the living test and the life after it are staged in Drezen (Chapters 3 and 5), so the walk resumes there.
        var danced = World(story, 5, "trickster", "trickster.ever", P + "masks.game", P + "masks.two_lies", P + "masks.mireya",
                           P + "masks.a_dance_with_a_knife_in_it", P + "masks.danced");
        var lessonAlive = S(P + "beat.lesson_alive");
        check(Avail(lessonAlive, Later(story, danced, 100)), "The living Camellia's lesson does not follow the dance.");
        var taughtAlive = Take(lessonAlive, Later(story, danced, 100), "steady", 0, P + "beat.lesson");
        var termsAlive = S(P + "returned.terms_alive");
        check(Avail(termsAlive, Later(story, taughtAlive, 100)), "Her price does not follow the lesson, alive.");
        var pricedAlive = Take(termsAlive, Later(story, taughtAlive, 100), "price", 0, P + "cost.bled", P + "terms_named");
        var testAlive = S(P + "returned.test_alive");
        check(Avail(testAlive, Later(story, pricedAlive, 100)), "Her test does not follow her price, alive.");
        var yesAlive = Take(testAlive, Later(story, pricedAlive, 100), "yes_a", 0, Committed);
        check(!yesAlive.Has(Killed) && !yesAlive.Has(Returned), "The living commit passed through a death.");
        check(Avail(S(P + "bond.shelf_alive"), Later(story, yesAlive, 100)), "The life after her answer does not follow a living commit.");

        // --- After her answer: the intimate scenes sit only behind the commit; the life goes on. ----------------------
        var afterCommit = new[] { "bond.shelf", "bond.witness", "bond.not_today", "evening.breakfast", "evening.a_gift_for_a_dead_woman",
            "evening.the_prisoner", "evening.the_mirror", "cards.the_deck_again", "cards.two_lies_again", "cards.the_amulet",
            "day.the_anniversary", "day.the_second_dance", "day.a_new_friend", "day.the_eve" };
        foreach (var id in afterCommit)
            foreach (var s in new[] { S(P + id), S(P + id + "_camp") })
                check(s.Requires.Contains(Committed) || s.RequiresAnyGroups.Any(g => g.Contains(Committed)),
                    "A scene of the life after her answer does not require the commit: " + s.Id);
        var quarters = S(P + "react.regill_quarters");
        check(quarters.Reaction && quarters.Requires.Contains(Committed) && quarters.Requires.Contains("regill.in_party")
              && quarters.AnswerLists.SequenceEqual(new[] { "2366a8db6481070439fee222c0c52e45" })
              && Avail(quarters, World(story, 5, "trickster", "trickster.ever", Committed, "regill.in_party")),
            "Nobody in the party notices the commit (Directive 12: a companion reaction to the intimacy).");
        check(test.Nodes.Any(n => n.Id == "threshold") && Ch(test, "threshold", 0).Next == "morning",
            "The night after her answer does not cut at the start of the act and wake to the morning.");
        var together = World(story, 5, "trickster", "trickster.ever", Killed, Returned, P + "cost.knows_you_tried", Committed);
        check(Avail(S(P + "bond.shelf"), together), "The shelf does not follow the commit.");
        var shelved = Take(S(P + "bond.shelf"), together, "kept", 0, P + "bond.shelf", P + "bond.list_kept");
        var witnessed = Take(S(P + "bond.witness"), Later(story, shelved, 100), "lied_after", 0, P + "bond.witness_lied");
        check(Avail(S(P + "bond.not_today"), Later(story, witnessed, 100)), "Not today does not follow the witness.");

        // --- The nine authorized other-route reactions read Camellia's current death (engine-q3). ----------------
        foreach (var id in new[] { "jerribeth.trickster.reaction.camellia", "jerribeth.trickster.reaction.camellia_host",
            "nurah.trickster.react.camellia_pardon", "nurah.trickster.react.camellia_market", "nurah.trickster.react.camellia_supper",
            "nurah.trickster.react.camellia_draft", "soana.trickster.react.camellia_portion", "soana.trickster.react.camellia_knot",
            "minagho_chivarro.trickster.react.camellia_bill" })
        {
            var s = story.Scenes.SingleOrDefault(x => x.Id == id);
            if (s == null) continue;
            check(s.Forbids.Contains(Dead) && !s.ForbidOverrides.ContainsKey(Dead),
                "A Camellia reaction overrides her current death: " + id);
            check(Rules.ForbidHolds(s, Dead, World(story, 5, Dead, Returned))
                && !Rules.ForbidHolds(s, Dead, World(story, 5, Returned)), "A later death leaks into a foreign reaction: " + id);
            check(!s.ForbidOverrides.ContainsKey(Killed), "A foreign reaction claims the veiled Camellia's presence hub: " + id);
        }

        // --- Pages: the late commit, her refusal, and the kept page's sibling for a Commander on the roll of the dead. --
        // E14d native-slide replacements (camellia_native) are cue texts, not pages; CamelliaNativeSlideTests covers them.
        var pages = story.Scenes.Where(s => s.Relationship == "camellia" && s.Owner == "CamelliaEpilogue" && !Rules.IsNativeReplacement(story, s))
            .Select(s => s.Id).ToArray();
        check(pages.OrderBy(x => x).SequenceEqual(new[] { P + "epilogue.commit", P + "epilogue.commit_on_record", P + "epilogue.kept", P + "epilogue.kept_on_record", P + "epilogue.refused" }),
            "Camellia's epilogue pages do not match: " + string.Join(", ", pages));
        check(S(P + "epilogue.commit").Requires.Contains(P + "terms_named") && S(P + "epilogue.commit").Forbids.Contains(Committed),
            "The late commit page does not rest on her named price.");
        // Q8 (Sol INT): a Last Call bottle survivor (commander_back, no cheated_death) keeps her pages; a dead Commander gets the
        // memorial sibling, for the commit and for the late commit alike.
        var alive6 = World(story, 6, "trickster", "trickster.ever", Committed, "sacrifice", "trickster.commander_back");
        var dead6 = World(story, 6, "trickster", "trickster.ever", Committed, "sacrifice");
        check(Avail(S(P + "epilogue.kept"), alive6) && !Avail(S(P + "epilogue.kept_on_record"), alive6)
              && !Avail(S(P + "epilogue.kept"), dead6) && Avail(S(P + "epilogue.kept_on_record"), dead6),
            "Her kept page and its memorial do not follow whether the Commander lived.");
        var lateAlive = World(story, 6, "trickster", "trickster.ever", P + "terms_named", "sacrifice", "trickster.commander_back");
        var lateDead = World(story, 6, "trickster", "trickster.ever", P + "terms_named", "sacrifice");
        check(Avail(S(P + "epilogue.commit"), lateAlive) && !Avail(S(P + "epilogue.commit_on_record"), lateAlive)
              && !Avail(S(P + "epilogue.commit"), lateDead) && Avail(S(P + "epilogue.commit_on_record"), lateDead),
            "The late commit narrates a life with a dead Commander, or loses a living one.");
        // Q8 (Sol CAN): the eve of the Threshold is Chapter 5, after Iz, on every twin; the living twin never recalls dying.
        foreach (var id in new[] { "day.the_eve", "day.the_eve_camp", "day.the_eve_alive" })
            check(S(P + id).Chapters.SequenceEqual(new[] { 5 }) && S(P + id).MinChapter == 5 && S(P + id).Requires.Contains("iz.done"),
                "The eve of the Threshold opens outside its window: " + id);
        // Q8 (Sol CAN/INT): Drezen-staged hub twins stay in Drezen, Chapters 3 and 5, like the veiled twin.
        foreach (var id in new[] { "returned.test", "cards.the_cutler", "bond.shelf", "evening.breakfast", "day.the_second_dance" })
            foreach (var suffix in new[] { "_camp", "_alive" })
            {
                var twin = story.Scenes.SingleOrDefault(s => s.Id == P + id + suffix);
                if (twin == null) continue;
                check(twin.Areas.SequenceEqual(new[] { Drezen }) && !twin.Chapters.Contains(4), "A Drezen scene travels with the companion hub: " + twin.Id);
            }
        foreach (var id in new[] { "masks.the_funeral_i_would_like", "evening.a_table_for_strangers" })
            check(S(P + id).Areas.SequenceEqual(new[] { Drezen }), "A Drezen courtship scene travels with the companion hub: " + id);
        // Q8 (Sol INT): a commitment followed by her native death or dismissal, with no return, has no kept page.
        check(!Avail(S(P + "epilogue.kept"), World(story, 6, "trickster", "trickster.ever", Committed, Killed))
              && !Avail(S(P + "epilogue.kept"), World(story, 6, "trickster", "trickster.ever", Committed, "camellia.kicked_out"))
              && Avail(S(P + "epilogue.kept"), World(story, 6, "trickster", "trickster.ever", Committed, Killed, Returned, P + "cost.knows_you_tried"))
              && Avail(S(P + "epilogue.kept"), World(story, 6, "trickster", "trickster.ever", Committed, Killed, Returned, P + "cost.knows_you_tried", "camellia.kicked_out")),
            "The kept page outlives her death or dismissal.");
        // Q8 (Sol INT): the presence-failure letter waits 96 hours past the physical twin's 72; a refused test closes the coda.
        check(letter.DelayHours == 168, "The fallback letter arrives before its physical twin has had its 96 hours.");
        var coda = story.Scenes.SingleOrDefault(s => s.Id == "camellia.lastcall.page");
        // Q8 coordinator ruling: the coda needs her commitment and does not play after her death or dismissal unless she returned.
        check(coda != null && coda.Requires.Contains(Committed), "The Last Call coda does not require her commitment.");
        var lc = new[] { "trickster.ever", "lastcall.active", Committed };
        check(Avail(coda!, World(story, 6, lc)) && !Avail(coda!, World(story, 6, lc.Append(Killed).ToArray()))
              && !Avail(coda!, World(story, 6, lc.Append(Dead).ToArray())) && !Avail(coda!, World(story, 6, lc.Append("camellia.kicked_out").ToArray()))
              && Avail(coda!, World(story, 6, lc.Concat(new[] { Killed, Returned, P + "cost.knows_you_tried", "camellia.kicked_out" }).ToArray()))
              && !Avail(coda!, World(story, 6, "trickster", "trickster.ever", "lastcall.active", P + "terms_named")),
            "The Last Call coda plays for a Camellia killed or dismissed after committing, or without her commitment.");
        // Q8 (Sol INT): the veiled widow sits at Fye's bar only once the third night has given her back.
        check(story.Presences["camellia.presence"].Requires.Contains(P + "raised"), "The veiled copy sits in the tavern while she is still underground.");
        // Q8 (Sol BEL): "you caught it" plays only when the Commander did win the first game.
        var again = S(P + "cards.two_lies_again");
        check(Ch(again, "two", 0).Requires.Contains(P + "masks.out_lied") && Ch(again, "two", 1).Forbids.Contains(P + "masks.out_lied"),
            "The second game rewrites a lost first game as a win.");
        // eng7-l13: preparation also requires the live outcome contract.
        check(story.Derived[P + "late_committed"].Length == 1 && story.Derived[P + "late_committed"][0].SequenceEqual(new[] { "trickster.ever", P + "terms_named", "camellia.outcome.route_open", "camellia.trickster.late_committed.without.camellia.trickster.declined" }),
            "The Derived late commit does not rest on her named price.");

        Console.WriteLine("PASS: Camellia Trickster (Trk_Camellia_*): the joke at every kill, the late curtain, the veiled mourner, the body told it's overacting, her price, her test, the oath, and the life around them.");
    }
}
