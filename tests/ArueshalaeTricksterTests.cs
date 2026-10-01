using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Arueshalae, Trickster (Writer/handoffs/trickster/arueshalae.md; F18): "Treatment".
// One block per spec rules test (Trk_Arueshalae_*), the shape of each hook, the living courtship (arueshalae_treatment:
// she proposes; the second ask has no price), the rulebook placements (the arcade and the awning on two bodies), the
// Lore (Religion) rank 1 gate on the quack's cure, and Nocticula's court.arueshalae.
internal static class ArueshalaeTricksterTests
{
    private const string Unit = "a352873d37ec6c54c9fa8f6da3a6b3e1";
    private const string Hub = "03ebad9587cbea0438d901a0f8df44f1";
    private const string EvilUnit = "e3bc95db7e2181d41847b3a1d858258d";
    private const string EvilNpc = "2c8caedd0a558524ca0ed1ab3132fae1";
    private const string Lair = "fe9eaf819cf03424a9108aa8b777694d";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Jeweler = "bc1093231b1577a4485a730c29595195";
    private const string Tailor = "253cdb8f434e5a6469b75e18428316e3";
    private const string Fye = "0f12118177d102f428a3b30b15b132eb";
    private const string Wilcer = "a380d926e92f70e429681eb9654478f9";
    private const string MeetEvilList = "3ef227bb0ba84104387fd9b4865a4ce0";
    private const string TasteCue = "480082b0c04099540be2ed84be7c9536";
    private const string P = "arueshalae.trickster.";
    private const string T = "arueshalae.treatment.";

    private static Snapshot World(Story story, int chapter, string area, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = area, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Unit);
        state.AvailableContacts.Add(EvilUnit);
        state.AvailableContacts.Add(EvilNpc);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, int? chapter = null)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        if (chapter != null) later.Chapter = chapter.Value;
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Choice Ch(Scene scene, string node, int index) => scene.Nodes.Single(n => n.Id == node).Choices[index];
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            var chosen = Ch(scene, node, index);
            var hits = Program.Walk(scene, w).Where(r => chosen.Set.All(r.Has) && (chosen.Set.Length > 0 || r.Has(scene.Id))
                                                          && chosen.Forbids.All(f => !r.Has(f) || chosen.Set.Contains(f))).ToList();
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        Snapshot First(Scene scene, Snapshot w, string node, int index) => After(scene, w, node, index).FirstOrDefault() ?? w;
        bool Avail(Scene scene, Snapshot w) => Rules.Available(story, scene, w);
        var own = story.Scenes.Where(s => s.Relationship == "arueshalae" && !s.Reaction && s.Owner == "Arueshalae").ToArray();
        // Plays every available Arueshalae scene forward (in the given area) and reports whether a flag is ever held.
        bool Reaches(Snapshot start, string flag, int chapter, string area)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 24 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    if (from.Has(flag)) return true;
                    var w = Later(story, from, 100, chapter);
                    w.Area = area;
                    foreach (var scene in own.Where(s => Avail(s, w)))
                        foreach (var r in Program.Walk(scene, w))
                        {
                            if (r.Has(flag)) return true;
                            if (seen.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                        }
                }
                frontier = next.Take(300).ToList();
            }
            return false;
        }

        // --- Shape: relationship, revival, presences (06-ROUTE-REGISTRY placements) --------------------------------
        var rel = story.Relationships["arueshalae"];
        check(rel.StartedFlag == "arueshalae.started" && rel.ClosedFlag == "arueshalae.closed" && rel.CommittedFlag == "arueshalae.committed"
              && rel.UnavailableFlags.SequenceEqual(new[] { "arueshalae_dead", "arueshalae.evil_dead", "arueshalae.kicked_out", "arueshalae.kicked_out_evil" })
              && rel.UnavailableOverrides["arueshalae_dead"] == P + "returned" && rel.UnavailableOverrides["arueshalae.evil_dead"] == P + "returned"
              && !rel.UnavailableOverrides.ContainsKey("arueshalae.kicked_out")
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "dead", "evil_dead", "failed" }),
            "Arueshalae's relationship does not match the spec (kick-out is closure, never overridden).");
        check(story.Revivals["arueshalae"].Unit == Unit && story.Revivals["arueshalae"].DeathFlag == "arueshalae_dead",
            "Her revival is not her companion unit behind her death etude.");
        var arcade = story.Presences["arueshalae.presence.evil_drezen"];
        var awning = story.Presences["arueshalae.presence.evil_awning"];
        var lairPresence = story.Presences["arueshalae.presence.evil"];
        check(arcade.At?.NearUnit == Jeweler && awning.At?.NearUnit == Tailor && arcade.Unit == EvilUnit && awning.Unit == EvilNpc
              && awning.Requires.Contains("arueshalae.presence.evil_drezen.failed") && arcade.Dialog == "hub" && awning.Dialog == "hub",
            "The evil Drezen beats are not at the jeweller with the tailor's awning as a second-body fallback.");
        foreach (var pr in new[] { arcade, awning, lairPresence })
            check(pr.At?.NearUnit != Fye && pr.At?.NearUnit != Wilcer, "A presence sits at a crowded anchor (Fye or Wilcer Garms).");
        check(lairPresence.At?.Locator == "8b58ebe0-42a8-4be6-96dc-75926e191cb6" && lairPresence.Area == Lair,
            "The lair presence is not at her own native locator.");
        foreach (var s in own.Where(s => !Rules.IsRemote(s) && s.InteractionHub == null && s.AnswerLists.Contains(Hub)))
            check(s.ContactUnit == Unit, "A hub scene is not hers: " + s.Id);
        foreach (var s in story.Scenes.Where(s => s.Relationship == "arueshalae" && s.Id.EndsWith("_yard")))
            check(s.ContactUnit == EvilNpc && s.InteractionHub == "arueshalae.presence.evil_awning"
                  && s.Requires.Contains("arueshalae.presence.evil_drezen.failed"),
                "An awning twin is not on the second body behind the arcade's failure: " + s.Id);

        // --- Trk_Arueshalae_Dead / DeadEvilChoice / DeadAfterFailure / DeadDeclined --------------------------------
        var starving = S(P + "dead.starving");
        check(starving.TricksterDevice && starving.TricksterState == "dead" && starving.Recovery == "arueshalae" && Rules.IsRemote(starving)
              && Ch(starving, "start", 0).Mythic == "PlayerIsTrickster" && Ch(starving, "start", 0).Requires.Contains("trickster.religion_tier1")
              && Ch(starving, "start", 2).Mythic == "PlayerIsTrickster" && Ch(starving, "start", 2).Forbids.Contains("trickster.religion_tier1")
              && Ch(starving, "wake", 0).Check?.Skill == "SkillLoreReligion" && Ch(starving, "rite_fails", 0).Abort
              && Ch(starving, "plea", 0).Revive == "arueshalae"
              && Ch(starving, "plea", 1).Revive == "arueshalae" && Ch(starving, "plea", 0).Next == null && Ch(starving, "plea", 1).Next == null,
            "'Starving, not dead' is not a terminal Trickster recovery.");
        // Q11: the unprepared wager is retired; without the gift tied in life, the diagnosis returns nobody.
        var unprepared = Later(story, World(story, 3, "", "trickster", "trickster.ever", "trickster.religion_tier1", "arueshalae_dead", "arueshalae_dead.latched", "revive.arueshalae.available"), 30);
        check(Program.Walk(starving, unprepared).All(r => !r.Has(P + "returned")), "An unprepared Commander still revives her by touch.");
        var dead = World(story, 3, "", "trickster", "trickster.ever", P + "gift_held", "arueshalae_dead", "arueshalae_dead.latched", "revive.arueshalae.available");
        dead = Later(story, dead, 30);
        check(Avail(starving, dead), "Trk_Arueshalae_Dead: the diagnosis is not available.");
        var fed = First(starving, dead, "plea", 0);
        check(fed.Has(P + "returned") && fed.Has(P + "cost.fed_on_you") && fed.Has("arueshalae.started"), "Trk_Arueshalae_Dead: wrist does not return her.");
        check(!Avail(S(P + "evil.second_opinion"), dead) && !Avail(S(P + "failed.chaplain"), dead), "Trk_Arueshalae_Dead: another device opens.");
        check(Reaches(fed, "arueshalae.committed", 5, ""), "Trk_Arueshalae_Dead: no commit is reachable after the return.");
        var ate = First(starving, dead, "plea", 1);
        check(ate.Has(P + "cost.fed_on_prisoner") && Ch(starving, "plea", 1).Alignment?.Direction == "Evil" && Ch(starving, "plea", 1).Alignment!.Value == 2,
            "Trk_Arueshalae_DeadEvilChoice: the cultist is not Evil 2.");
        var failedPath = World(story, 3, "", "trickster.ever", "trickster.failed", "arueshalae_dead", "arueshalae_dead.latched", "revive.arueshalae.available");
        check(!Avail(starving, Later(story, failedPath, 30)), "Trk_Arueshalae_DeadAfterFailure: a new trick after a Ch4 failure.");
        var vow = First(starving, dead, "plea", 2);
        check(vow.Has(P + "declined") && !vow.Has("arueshalae.closed") && !Avail(starving, Later(story, vow, 24)),
            "Trk_Arueshalae_DeadDeclined: the vow is not a soft decline that ends the diagnosis.");

        // --- Polish batch 9: no mythic power lifts the death. The lore lowers a DC; the gift is prepared in life ------
        check(Ch(starving, "treat", 0).Next == "work" && Ch(starving, "treat", 1).Next == "work"
              && Ch(starving, "work", 0).Check?.Skill == "SkillLoreReligion" && Ch(starving, "work", 0).Check!.DC < 22
              && Ch(starving, "wake", 0).Check!.DC == 22,
            "Trk_Arueshalae_NoPowerLift: the lore path revives without a check, or does not lower the DC.");
        check(!starving.Nodes.Any(n => n.Text.Contains("negative condition")), "Trk_Arueshalae_NoPowerLift: death is still read as a negative condition.");
        var insurance = S(P + "insurance");
        var aliveGift = Later(story, World(story, 3, "", "trickster", "trickster.ever"), 30);
        check(Avail(insurance, aliveGift), "Trk_Arueshalae_Insurance: the gift cannot be asked for in life.");
        var holding = First(insurance, aliveGift, "reason", 0);
        check(holding.Has(P + "gift_held") && !Avail(insurance, Later(story, holding, 30)), "Trk_Arueshalae_Insurance: the gift is not kept.");
        check(!Avail(insurance, dead), "Trk_Arueshalae_Insurance: the gift is asked of a corpse.");
        var gifted = Later(story, World(story, 3, "", "trickster", "trickster.ever", P + "gift_held", "arueshalae_dead", "arueshalae_dead.latched", "revive.arueshalae.available"), 30);
        var giftChoices = starving.Nodes.Single(n => n.Id == "start").Choices.Where(ch => Rules.Match(ch.Requires, ch.Forbids, gifted)).ToList();
        check(giftChoices.Count(ch => ch.Next == "thread") == 1 && !giftChoices.Any(ch => ch.Next == "treat" || ch.Next == "wake")
              && starving.Nodes.Single(n => n.Id == "thread").Choices.All(ch => ch.Check == null && ch.Set.Contains(P + "cost.gift_torn")),
            "Trk_Arueshalae_Gift: the prepared thread is not the sure road, or it costs nothing.");
        var threaded = First(starving, gifted, "plea", 0);
        check(threaded.Has(P + "returned") && threaded.Has(P + "cost.gift_torn"), "Trk_Arueshalae_Gift: the thread does not return her.");

        // --- Aftertaste / Terms / TermsRefusal / TermsAgain --------------------------------------------------------
        var aftertaste = S(P + "returned.aftertaste");
        var returned3 = Later(story, World(story, 3, "", "trickster.ever", P + "returned", P + "cost.fed_on_you"), 30);
        check(Avail(aftertaste, returned3), "Trk_Arueshalae_Aftertaste: not available after the return.");
        var tasted = First(aftertaste, returned3, "test", 0);
        check(tasted.Has(P + "aftertaste") && tasted.Has(P + "said_every_time"), "Trk_Arueshalae_Aftertaste: the test does not record her answer.");
        var terms = S(P + "terms");
        check(!Avail(terms, Later(story, tasted, 100)), "Trk_Arueshalae_Aftertaste: the commit opens in Chapter 3.");
        var ch5Returned = Later(story, World(story, 5, "", "trickster.ever", P + "returned", P + "aftertaste"), 100);
        check(Avail(terms, ch5Returned), "Trk_Arueshalae_TermsCommit: terms not available in Chapter 5.");
        check(First(terms, ch5Returned, "question", 0).Has("arueshalae.committed"), "Trk_Arueshalae_TermsCommit: 'Both' does not commit.");
        var notYet = First(terms, ch5Returned, "question", 2);
        check(notYet.Has(P + "declined") && !notYet.Has("arueshalae.committed"), "Trk_Arueshalae_TermsRefusal: not a soft no.");
        var again = S(P + "terms_again");
        check(Avail(again, Later(story, notYet, 170)), "Trk_Arueshalae_TermsRefusal: the second ask does not open.");
        var sworn = First(again, Later(story, notYet, 170), "start", 0);
        check(sworn.Has("arueshalae.committed") && sworn.Has(P + "cost.no_second_joke"), "Trk_Arueshalae_TermsAgain: the promise does not commit.");
        check(!Avail(again, Later(story, notYet, 100)), "Trk_Arueshalae_TermsAgain: the week is shorter than seven days.");

        // --- Evil: Setup / Late / Primed / Haggle / Refused / AfterFailure / InHiding ------------------------------
        var diagnosis = S(P + "evil.diagnosis");
        check(diagnosis.AnswerLists.SequenceEqual(new[] { MeetEvilList }) && diagnosis.ContactUnit == null && diagnosis.EntryMythic == "PlayerIsTrickster"
              && Ch(diagnosis, "start", 0).NativeNext == TasteCue && diagnosis.TricksterDevice && diagnosis.TricksterState == "evil_dead",
            "Trk_Arueshalae_EvilSetup: the referral is not the inline primer into Cue_0015.");
        check(First(diagnosis, World(story, 5, "", "trickster"), "start", 0).Has(P + "primed"), "Trk_Arueshalae_EvilSetup: the primer does not prime.");
        var lateRef = S(P + "evil.late_referral");
        var evilLate = Later(story, World(story, 5, "", "trickster", "trickster.ever", "arueshalae.evil_dead", "arueshalae.evil_dead.latched"), 30);
        check(Avail(lateRef, evilLate), "Trk_Arueshalae_EvilLate: the late referral is not available.");
        var lateSent = First(lateRef, evilLate, "start", 0);
        check(lateSent.Has(P + "primed") && lateSent.Has(P + "cost.late"), "Trk_Arueshalae_EvilLate: the vrock's message does not prime with the surcharge.");
        var second = S(P + "evil.second_opinion");
        check(Avail(second, Later(story, lateSent, 80)), "Trk_Arueshalae_EvilLate: the second opinion does not follow.");
        var primed = Later(story, World(story, 5, "", "trickster.ever", "arueshalae.evil_dead", P + "primed"), 80);
        check(Avail(second, primed), "Trk_Arueshalae_EvilPrimed: the second opinion is not available.");
        var paid = First(second, primed, "queen", 0);
        check(paid.Has(P + "returned") && paid.Has(P + "cost.nocticula_debt") && paid.Has("arueshalae.started"), "Trk_Arueshalae_EvilPrimed: the fee does not return her.");
        check(First(second, primed, "queen", 1).Has(P + "cost.nocticula_favour"), "Trk_Arueshalae_EvilHaggle: the fine print does not move the debt.");
        var refused = First(second, primed, "queen", 2);
        check(refused.Has(P + "declined") && refused.Has("arueshalae.closed"), "Trk_Arueshalae_EvilRefused: refusing is not closure.");
        var evilFailed = Later(story, World(story, 5, "", "trickster.ever", "trickster.failed", "arueshalae.evil_dead", "arueshalae.evil_dead.latched"), 30);
        check(!Avail(lateRef, evilFailed), "Trk_Arueshalae_EvilAfterFailure: a new trick after a Ch4 failure.");
        var hiding = Later(story, World(story, 5, "", "trickster.ever", "arueshalae.evil_dead", P + "primed", "noct.dead", "noct.acq.council_fight"), 80);
        var signedHiding = First(second, hiding, "unanswered", 0);
        var hidingPages = new HashSet<string>();
        Program.Walk(second, hiding, (page, _) => hidingPages.Add(page));
        check(hidingPages.Contains("unanswered") && !hidingPages.Contains("queen") && !hidingPages.Contains("late") && !hidingPages.Contains("fooled"),
            "Trk_Arueshalae_EvilInHiding: the queen writes while she is in hiding (the unanswered page is unreachable).");
        check(signedHiding.Has(P + "returned") && signedHiding.Has(P + "cost.nocticula_debt"), "Trk_Arueshalae_EvilInHiding: the in-hiding answer does not return her.");

        // --- Evil: Reunion (a third way) / Letter / Terms / Refusal / the night -------------------------------------
        var reunion = S(P + "evil.reunion");
        check(reunion.InteractionHub == "arueshalae.presence.evil" && reunion.ContactUnit == EvilUnit && reunion.Areas.SequenceEqual(new[] { Lair }),
            "The reunion is not on the lair presence.");
        var back = Later(story, World(story, 5, Lair, "trickster.ever", "arueshalae.evil_dead", P + "returned", P + "cost.nocticula_debt"), 30);
        check(Avail(reunion, back), "Trk_Arueshalae_EvilReunion: not available.");
        check(Ch(reunion, "price", 2).Set.Contains(P + "cost.fed_on_demon") && Ch(reunion, "price", 2).Requires.Contains(P + "cost.late")
              && Ch(reunion, "price", 4).Set.Contains(P + "cost.fed_on_demon") && Ch(reunion, "price", 4).Forbids.Contains(P + "cost.late")
              && Ch(reunion, "price", 2).Alignment == null && Ch(reunion, "price", 4).Alignment == null,
            "The reunion's third way does not match the path (the vrock only after the late referral; the babau otherwise).");
        check(First(reunion, back, "price", 4).Has(P + "cost.fed_on_demon"), "The primed path's third way (the babau) is not playable.");
        var hungry = First(reunion, back, "price", 3);
        check(hungry.Has(P + "reunited") && hungry.Has(P + "cost.sent_away_hungry"), "Trk_Arueshalae_EvilReunion: refusing does not reunite, hungry.");
        var letterTwin = S(P + "evil.reunion_letter");
        var lairFailed = Program.Copy(back); lairFailed.Flags.Add("arueshalae.presence.evil.failed");
        check(Avail(letterTwin, Later(story, lairFailed, 130)), "Trk_Arueshalae_EvilReunionLetter: no letter when the lair copy fails.");
        var evilTerms = S(P + "evil.terms");
        var reunitedW = Later(story, World(story, 5, Drezen, "trickster.ever", "arueshalae.evil_dead", P + "returned", P + "reunited", P + "cost.nocticula_debt"), 60);
        check(Avail(evilTerms, reunitedW) && evilTerms.InteractionHub == "arueshalae.presence.evil_drezen", "Trk_Arueshalae_EvilTermsCommit: not available at the arcade.");
        var open = First(evilTerms, reunitedW, "ask", 0);
        check(open.Has("arueshalae.committed") && open.Has(P + "cost.open_door"), "Trk_Arueshalae_EvilTermsCommit: the open door does not commit.");
        var stay = First(evilTerms, reunitedW, "ask", 1);
        check(stay.Has(P + "ally") && !stay.Has("arueshalae.committed"), "Trk_Arueshalae_EvilTermsRefusal: 'stay' is not her refusal.");
        var window = S(P + "evil.window");
        check(Avail(window, Later(story, open, 30)), "The fallen's night does not follow the open door.");

        // --- Failed: the chaplain -------------------------------------------------------------------------------
        var chaplain = S(P + "failed.chaplain");
        var failed = Later(story, World(story, 3, "", "trickster", "trickster.ever", "arueshalae.failed"), 5);
        check(Avail(chaplain, failed) && chaplain.EntryMythic == "PlayerIsTrickster" && chaplain.TricksterState == "failed",
            "Trk_Arueshalae_Failed: the appointment is not available.");
        var appointed = First(chaplain, failed, "sword", 0);
        check(appointed.Has(P + "cost.chaplain") && appointed.Has("arueshalae.started"), "Trk_Arueshalae_Failed: the job does not stick.");
        var ch5Chaplain = Later(story, World(story, 5, "", "trickster.ever", P + "cost.chaplain"), 100);
        check(First(terms, ch5Chaplain, "question", 3).Has("arueshalae.closed"), "Trk_Arueshalae_FailedTermsNeither: 'Neither' does not close.");
        check(First(terms, ch5Chaplain, "question", 1).Has("arueshalae.committed"), "Trk_Arueshalae_FailedTermsCommit: 'the saint' does not commit.");

        // --- The treatment: the living courtship -----------------------------------------------------------------
        var intake = S(T + "intake");
        var study = S(T + "studied");
        var reader = World(story, 3, "", "trickster", "trickster.ever");
        check(Avail(study, reader) && !Avail(intake, reader), "The intake opens before the Commander has done the reading.");
        check(study.Nodes.Single(n => n.Id == "why").Choices.Any(c => c.Check?.Skill == "SkillLoreReligion" && c.Forbids.Contains("trickster.religion_tier1")),
            "The reading has no Lore (Religion) check for a Commander without the trick.");
        var alive = World(story, 3, "", "trickster", "trickster.ever", T + "studied");
        check(Avail(intake, alive) && intake.EntryMythic == "PlayerIsTrickster", "The treatment's intake is not open after the reading.");
        check(!Avail(intake, World(story, 3, "", "trickster.ever")), "The intake opens without the live Trickster path.");
        var patient = First(intake, alive, "her", 0);
        check(patient.Has(T + "intake") && patient.Has("arueshalae.started"), "The intake does not start the relationship.");
        check(Reaches(patient, T + "relapse_two", 5, ""), "The treatment cannot reach its second relapse.");
        var touch = S(T + "touched");
        check(Ch(touch, "explain", 0).Requires.Contains("trickster.religion_tier1") && Ch(touch, "explain", 1).Forbids.Contains("trickster.religion_tier1"),
            "The quack's cure is not keyed to the chosen Lore (Religion) rank 1 trick, with an honest path without it.");
        var slip = S(T + "rite_slipped");
        var slipW = Later(story, World(story, 5, "", "trickster.ever", T + "intake", T + "touched", T + "kitchen"), 60);
        check(Avail(slip, slipW) && slip.Nodes.Single(n => n.Id == "distance").Choices.All(c => c.Set.Contains("arueshalae.trickster.cost.drained")),
            "The missed rite is not a priced, visible cost with her distance to answer.");
        check(S(T + "relapse_two").Requires.Contains(T + "rite_slipped"), "The second relapse does not follow the missed rite.");
        var proposal = S(T + "prescription");
        var ask = proposal.Nodes.Single(n => n.Id == "ask");
        check(ask.Choices.Count == 4 && ask.Choices.All(c => c.Crusade == null && c.Alignment == null),
            "The proposal is not hers alone (yes / the saint / not yet / no, no price).");
        var ready = Later(story, World(story, 5, "", "trickster.ever", T + "intake", T + "relapse_two", T + "her_call"), 100);
        check(Avail(proposal, ready), "The proposal is not available after the second relapse.");
        var yes = First(proposal, ready, "ask", 0);
        check(yes.Has("arueshalae.committed"), "Her proposal does not commit on yes.");
        var later = First(proposal, ready, "ask", 2);
        var again2 = S(T + "prescription_again");
        check(Avail(again2, Later(story, later, 60)) && again2.Nodes.SelectMany(n => n.Choices).All(c => c.Crusade == null && c.Alignment == null),
            "The second ask is missing, or priced.");
        check(First(again2, Later(story, later, 60), "roof", 0).Has("arueshalae.committed"), "The Commander's ask does not commit.");
        var night = S(T + "night");
        check(night.Requires.Contains("arueshalae.committed") && !Avail(night, Later(story, ready, 50)), "The night opens before any yes.");
        check(Avail(night, Later(story, yes, 30)), "The night does not follow the yes.");
        foreach (var n in night.Nodes)
            check(!n.Text.Contains(" cot") && !n.Text.Contains("narrow bed"), "The night is staged on a cot: " + n.Id);

        // --- Nocticula's court.arueshalae (collects the favour once) -----------------------------------------------
        var court = S("nocticula.trickster.court.arueshalae");
        var owed = Later(story, World(story, 5, "", "trickster.ever", "arueshalae.started", P + "returned", P + "cost.nocticula_favour", "noct.started"), 30);
        check(Rules.IsRemote(court) && court.Relationship == "nocticula" && Avail(court, owed), "Trk_Nocticula_CourtArueshalae: not available.");
        var noContact = Later(story, World(story, 5, "", "trickster.ever", "arueshalae.started", P + "returned", P + "cost.nocticula_favour"), 30);
        check(!Avail(court, noContact), "Trk_Nocticula_CourtArueshalae_NoContact: available without contact.");
        var burned = First(court, owed, "raised", 0);
        check(burned.Has("nocticula.trickster.favour_called.arueshalae") && burned.Has("nocticula.trickster.cost.favour_burned"),
            "The burned letter does not pay the favour.");
        check(!Avail(court, Later(story, burned, 30)), "The favour is collected twice.");

        // --- Reactions: exactly Sosiel and Lann, each behind its reactor's guard ---------------------------------
        var reactions = story.Scenes.Where(s => s.Relationship == "arueshalae" && s.Reaction).ToArray();
        check(reactions.Length > 0 && reactions.All(r => r.Owner == "Sosiel" || r.Owner == "Lann"), "A reactor beyond Sosiel and Lann.");
        foreach (var r in reactions)
            check(r.Forbids.Contains(r.Owner == "Sosiel" ? "sosiel.dead" : "lann.dead")
                  && r.Forbids.Contains(r.Owner == "Sosiel" ? "sosiel.kicked_out" : "lann.kicked_out"),
                "A reaction without its reactor's guard: " + r.Id);

        // --- The Abyss night and the old name are told in Drezen, after the crossing (Chapter 5 only) ----------------
        foreach (var id in new[] { T + "abyss_dose", T + "old_name" })
        {
            var scene = S(id);
            var ch4 = Later(story, World(story, 4, "", "trickster.ever", T + "intake", T + "touched"), 100);
            var ch5 = Later(story, World(story, 5, "", "trickster.ever", T + "intake", T + "touched"), 100);
            check(!Avail(scene, ch4), "A physical Abyss-memory scene is offered in Chapter 4, where the hub cannot play it: " + id);
            check(Avail(scene, ch5), "The Abyss-memory scene is not available in Chapter 5, where it is told: " + id);
        }

        // --- Never another route's state; never a key token; never a crusade fee as the device's price --------------
        foreach (var s in story.Scenes.Where(s => s.Relationship == "arueshalae"))
        {
            foreach (var flag in s.Requires.Concat(s.Forbids).Concat(s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids))))
                check(!flag.EndsWith(".closed") || flag == "arueshalae.closed", "An Arueshalae scene reads another route's closure: " + s.Id);
            check(s.Nodes.SelectMany(n => n.Choices).All(c => c.Crusade == null), "A crusade fee in her route: " + s.Id);
        }

        // Q11 witnesses: a failed reading can be retried; the living, recruited fallen Arueshalae has a romance; the
        // Elysium morning drains nothing; elapsed-time claims are enforced; the torn gift costs something the game counts.
        var studied = S(T + "studied");
        var reading = World(story, 3, Drezen, "trickster", "trickster.ever");
        var failedReading = Program.WalkVia(studied, reading, "not_yet", 0);
        check(failedReading.Count > 0 && failedReading.All(r => !r.Has(T + "studied"))
              && Rules.Available(story, studied, Later(story, failedReading[0], 24))
              && !Rules.Available(story, S(T + "intake"), Later(story, failedReading[0], 24)),
            "A failed night reading records the rite as learned, or forbids the promised retry.");
        var learned = Program.WalkVia(studied, reading, "fit", 0);
        check(learned.Count > 0 && learned.All(r => r.Has(T + "studied")) && Rules.Available(story, S(T + "intake"), Later(story, learned[0], 24)),
            "A successful night reading does not open the intake.");
        var houseCall = S(P + "fallen.house_call");
        var recruited = World(story, 5, Drezen, "trickster", "trickster.ever", "arueshalae.evil_recruited");
        check(Rules.Available(story, houseCall, recruited) && !recruited.Has("arueshalae.evil_dead")
              && !Rules.Available(story, houseCall, World(story, 5, Drezen, "trickster", "trickster.ever")),
            "The living recruited fallen Arueshalae has no courtship, or it opens without her recruitment.");
        var doorOpen = Program.WalkVia(houseCall, recruited, "ask", 0);
        check(doorOpen.Count > 0 && doorOpen.All(r => r.Has("arueshalae.committed") && r.Has(P + "cost.open_door")),
            "The recruited fallen commit does not commit.");
        check(Rules.Available(story, S(P + "fallen.roof"), Later(story, doorOpen[0], 30))
              && Program.Walk(S(P + "fallen.roof"), Later(story, doorOpen[0], 30)).All(r => r.Has(P + "evil.dawn")),
            "The recruited fallen night is unreachable after the open door.");
        var notTonight = Program.WalkVia(houseCall, recruited, "ask", 1);
        check(notTonight.Count > 0 && Rules.Available(story, S(P + "fallen.lock"), Later(story, notTonight[0], 80))
              && !Rules.Available(story, S(P + "fallen.lock"), Later(story, notTonight[0], 10)),
            "'Not tonight' does not keep a reachable yes.");
        check(Rules.Available(story, S(P + "epilogue.fallen"), Later(story, doorOpen[0], 100, 6))
              && !Rules.Available(story, S(T + "epilogue.together"), Later(story, World(story, 6, Drezen, "trickster.ever", "arueshalae.committed", T + "intake", "arueshalae.evil_recruited"), 1)),
            "The recruited fallen commit has no ending, or reads the redeemed daybook ending.");
        var morning = S(T + "morning");
        var elysium = Later(story, World(story, 5, Drezen, "trickster", "trickster.ever", "arueshalae.committed", T + "night", "arueshalae.elysium"), 10);
        check(Rules.Available(story, morning, elysium) && Program.WalkVia(morning, elysium, "start", 0).Count == 0
              && Program.WalkVia(morning, elysium, "start", 1).Count > 0,
            "After the native Elysium ending, the morning still counts a drain.");
        check(S(T + "prescription").DelayHours >= 168, "The proposal opens before the fast's seven days have passed.");
        // Ledger row 2: native Nocticula keys reach her route only through Derived aliases, never a choice or scene gate.
        foreach (var s in story.Scenes.Where(s => s.Relationship == "arueshalae"))
            check(s.Requires.Concat(s.Forbids).Concat(s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids)))
                      .All(k => !k.StartsWith("noct.", StringComparison.Ordinal)),
                "An Arueshalae scene gates on a native Nocticula key: " + s.Id);
        // A soft 'not yet' at the proposal, then the native Elysium ending: the discharge still offers the yes.
        var deferred = World(story, 5, Drezen, "trickster", "trickster.ever", T + "intake", P + "declined", "arueshalae.elysium");
        check(Rules.Available(story, S(T + "discharged"), deferred) && !Rules.Available(story, S(T + "prescription_again"), deferred)
              && Program.WalkVia(S(T + "discharged"), deferred, "ask", 0).All(r => r.Has("arueshalae.committed")),
            "A deferred proposal followed by Elysium locks the treatment out of every commit.");
        // The failed-presence letter serves the late referral as well.
        check(Rules.Available(story, S(P + "evil.reunion_letter"), Later(story, World(story, 5, Drezen, "trickster", "trickster.ever", P + "returned",
                  "arueshalae.evil_dead", P + "cost.late", "arueshalae.presence.evil.failed"), 130)),
            "The late referral has no reunion when the lair presence fails.");
        Console.WriteLine("PASS: Arueshalae Trickster (Trk_Arueshalae_*): the diagnosis, the second opinion, the chaplain, the treatment and her proposal, the arcade, and the queen's favour.");
    }
}
