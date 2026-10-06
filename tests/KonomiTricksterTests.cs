using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Konomi, Trickster (Writer/handoffs/trickster/konomi.md): recess, not farewell (F17), recalled for consultations (F17)
// and credentials deemed presented (F03). One block per spec rules test (Trk_Konomi_*), plus the registered-route edits.
internal static class KonomiTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Contact = "ca2d58c5c65723945857e04fb85d30ce";
    private const string Hub = "0dc8b8604bb33c846a63f3eb62443674";

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
        if (Rules.ChapterFlag(chapter) is string chapterFlag) state.Flags.Add(chapterFlag);
        state.AvailableContacts.Add(Contact);
        Rules.Complete(story, state);
        // Flags and latches are stamped when the runtime records them; here, well before the world is observed.
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours)
    {
        var later = Program.Copy(state); later.Hour += hours; Rules.Complete(story, later); return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var late = S("konomi.trickster.dismissed.late");
        var recess = S("konomi.trickster.dismissed.recess");
        var terms = S("konomi.trickster.dismissed.terms");
        var priv = S("konomi.trickster.dismissed.private");
        var recalled = S("konomi.trickster.dead.recalled");
        var consult = S("konomi.trickster.dead.consultation");
        var accredited = S("konomi.trickster.never_arrived.accredited");
        var audience = S("konomi.trickster.never_arrived.audience");
        var epCommit = S("konomi.trickster.epilogue.commit");
        var epRefused = S("konomi.trickster.epilogue.refused");
        var epEnvoy = S("konomi.trickster.epilogue.envoy");
        var supper = S("konomi.trickster.dismissed.supper");
        var season = S("konomi.trickster.dismissed.a_season");
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));
        bool Commits(Scene scene, Snapshot w) => Program.Walk(scene, w).Any(r => r.Has("konomi.committed"));

        // Hooks and shape: every in-person beat is on her own office hub, on her own actor.
        foreach (var s in new[] { recess, terms, priv, consult, audience })
            check(s.AnswerLists.SequenceEqual(new[] { Hub }) && s.ContactUnit == Contact && !Rules.IsRemote(s)
                  && s.Areas.SequenceEqual(new[] { Drezen }), "Konomi's in-person beat left her office: " + s.Id);
        check(late.Remote && recalled.Remote && accredited.Remote, "A setup lost its letter.");
        check(late.TricksterState == "konomi.dismissed" && recalled.TricksterState == "konomi.retained_dead"
              && accredited.TricksterState == "konomi.missed_contact_available" && recalled.Recovery == "konomi",
            "Device states mislabelled.");
        var rel = story.Relationships["konomi"];
        check(!rel.UnavailableOverrides.ContainsKey("konomi.retained_dead") && rel.TricksterAccess.Count == 3 && rel.TricksterAccess["konomi.dismissed"].Returned == "konomi.trickster.recessed"
              && rel.TricksterAccess["konomi.retained_dead"].Returned == "konomi.retained_return_confirmed", "Konomi access map missing.");
        check(story.Presences.TryGetValue("konomi.presence", out var presence) && presence.Unit == Contact
              && presence.Mode == "reuse-native" && presence.At?.Locator == "e6a7de2a-ce6f-4413-b24d-06daf1990e4c"
              && presence.Requires.Contains("konomi.trickster.presence_on"), "Konomi presence missing.");
        var joke = late.Nodes[0].Choices[0];
        check(joke.Mythic == "PlayerIsTrickster" && joke.Alignment?.Direction == "Chaotic" && joke.Alignment?.Value == 1,
            "The shout after the carriage lost its price.");
        var bluff = recess.Nodes.Single(n => n.Id == "price").Choices[0].Check;
        check(bluff != null && bluff.Skill == "CheckBluff" && bluff.DC == 30 && bluff.Success == "read" && bluff.Failure == "outfoxed",
            "The fox contest is not a Bluff check against her.");

        // Trk_Konomi_InOffice: no Trickster scene in office.
        var office = World(story, 5, "trickster", "trickster.ever", "konomi.present");
        check(!story.Scenes.Where(s => s.Id.StartsWith("konomi.trickster.", StringComparison.Ordinal) && !s.Reaction
                                       && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).Any(s => Rules.Available(story, s, office)),
            "Trk_Konomi_InOffice: a Trickster scene opened while she holds the office.");

        // Trk_Konomi_Dismissed: the joke on the page, a day after the insult.
        var dismissed = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed");
        check(Rules.Available(story, late, dismissed) && !Rules.Available(story, recess, dismissed), "Trk_Konomi_Dismissed: setup unavailable.");
        var fresh = Program.Copy(dismissed); fresh.Times["konomi.dismissed.latched"] = fresh.Hour - 71;
        check(!Rules.Available(story, late, fresh), "The setup is read before the road is behind her (PP5: 72 hours).");
        check(!Rules.Available(story, late, World(story, 3, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed")),
            "The dismissal setup outside Chapter 5.");
        var pages = new HashSet<string>();
        var shouted = Program.Walk(late, dismissed, (page, _) => pages.Add(page)).Where(r => r.Has(late.Id)).ToList();
        check(shouted.Count == 1 && shouted[0].Has("konomi.trickster.primed") && shouted[0].Has("konomi.trickster.cost.late")
              && !pages.Contains("queen"), "Trk_Konomi_Dismissed: the minute sets the wrong flags.");
        // Polish 9b: no word made true. The minute goes to the Chancellor and the driver is bought, on the page, at a price.
        var bought = late.Nodes.Single(n => n.Id == "driver").Choices[2];
        check(pages.Contains("driver") && shouted[0].Has("konomi.trickster.cost.driver_paid") && bought.Crusade?.Resource == "Finances"
              && bought.Crusade?.Amount == -150 && bought.Next == "gate", "The road loops by itself again.");
        var driverChoices = late.Nodes.Single(n => n.Id == "driver").Choices;
        check(driverChoices.Count == 4 && driverChoices[0].Forbids.Contains("konomi.dismissed") && driverChoices[1].Forbids.Contains("konomi.dismissed")
              && driverChoices[3].Abort, "PP5: the driver's choices were reordered instead of retired and appended.");
        check(late.Nodes.Concat(recess.Nodes).All(n => !n.Text.Contains("proud of the others") && !n.Text.Contains("seam in your road")),
            "The paving stone that was not there is back.");
        var crowned = Program.Copy(dismissed); crowned.Flags.Add("coronation.seen");
        var queenPages = new HashSet<string>();
        Program.Walk(late, crowned, (page, _) => queenPages.Add(page));
        check(queenPages.Contains("queen"), "The Queen's eyebrow is missing after the Coronation.");
        crowned.Flags.Add("galfrey.dead");
        queenPages.Clear();
        Program.Walk(late, crowned, (page, _) => queenPages.Add(page));
        check(!queenPages.Contains("queen"), "A dead Queen raises an eyebrow.");
        // PP5 (tier-A Ch5 budget, one delivery): the gate sergeant's note is the setup's last page. The setup waits until the road
        // is behind her (72 hours after the insult), so she is placed only when everything it tells has happened (Sol r2 INT).
        var dismArrival = S("konomi.trickster.dismissed.arrival");
        check(late.DelayHours == 72 && pages.Contains("gate") && shouted[0].Has("konomi.trickster.back_from_the_road")
              && Later(story, shouted[0], 0).Has("konomi.trickster.presence_on") && !Rules.Available(story, dismArrival, Later(story, shouted[0], 48)),
            "PP5: the arrival is still a second Chapter 5 delivery.");
        // A save already on the road (cost.late without back_from_the_road) keeps the old note, and is not placed before it.
        var onRoad = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed", "konomi.trickster.primed",
                           "konomi.trickster.cost.late");
        check(!onRoad.Has("konomi.trickster.presence_on") && Rules.Available(story, dismArrival, onRoad) && !Rules.Available(story, recess, onRoad),
            "A save on the road lost its arrival, or was placed before it.");
        var afterShout = Later(story, shouted[0], 0);
        // Sol r5 INT: an earlier arrival (the jug's) is not proof of this journey.
        var jugThenDismissed = Program.Copy(onRoad); jugThenDismissed.Flags.Add("konomi.trickster.arrived"); Rules.Complete(story, jugThenDismissed);
        check(!jugThenDismissed.Has("konomi.trickster.presence_on") && !Rules.Available(story, recess, Later(story, jugThenDismissed, 47)),
            "An earlier arrival places her while the carriage is on the road.");
        check(Rules.Available(story, recess, afterShout) && !Rules.Available(story, late, afterShout), "Trk_Konomi_Dismissed: no recess.");
        check(afterShout.Has("konomi.trickster.presence_on"), "Konomi not placed after the loop.");
        check(!dismissed.Has("konomi.trickster.presence_on"), "Konomi placed before the loop.");

        // Trk_Konomi_Recess: the fox contest; a failed bluff costs her own terms.
        var primed = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed", "konomi.trickster.primed",
                           "konomi.trickster.cost.late", "konomi.trickster.back_from_the_road");
        check(Rules.Available(story, recess, primed) && !Rules.Available(story, late, primed), "Trk_Konomi_Recess: recess unavailable.");
        var recesses = Program.Walk(recess, primed);
        check(recesses.All(r => r.Has("konomi.trickster.recessed") && r.Has("konomi.trickster.cost.debt_owed")
                                && !r.Has("konomi.private_appointment")), "Trk_Konomi_Recess: the recess does not settle.");
        check(recesses.Any(r => r.Has("konomi.trickster.cost.outfoxed")) && recesses.Any(r => !r.Has("konomi.trickster.cost.outfoxed")),
            "Trk_Konomi_Recess: the bluff does not decide who sets the price.");
        var outfoxed = recesses.First(r => r.Has("konomi.trickster.cost.outfoxed"));
        check(Rules.Available(story, terms, Later(story, outfoxed, 48)), "Trk_Konomi_Recess: no terms after the recess.");
        check(!Rules.Available(story, S("konomi.private_meeting"), Later(story, outfoxed, 200)),
            "The registered courtyard courtship opens beside the recess.");

        // Trk_Konomi_Terms: the price is written exactly; no commit on the beat that bills the crown.
        var recessed = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed", "konomi.trickster.recessed");
        check(Rules.Available(story, terms, recessed), "Trk_Konomi_Terms: terms unavailable.");
        var price = terms.Nodes.Single(n => n.Id == "price").Choices;
        check(price[0].Crusade?.Resource == "Finances" && price[0].Crusade?.Amount == -500 && price[1].Crusade?.Amount == -500,
            "The letter to Nerosyan lost its price.");
        var settled = Program.Walk(terms, recessed);
        check(settled.All(r => !r.Has("konomi.committed")), "Trk_Konomi_Terms: commit on the beat that bills the crown.");
        var paid = settled.Single(r => r.Has("konomi.trickster.debt_paid"));
        check(paid.Has("konomi.trickster.terms_settled") && paid.Has("konomi.private_future"), "Trk_Konomi_Terms: the letter does not settle.");
        check(settled.Any(r => r.Has("konomi.trickster.favour_owed") && r.Has("konomi.private_future_open")), "The different coin is missing.");
        check(settled.Any(r => r.Has("konomi.closed")), "Her hard no is missing from the terms.");
        check(Rules.Available(story, priv, Later(story, paid, 72)) && !Rules.Available(story, priv, Later(story, paid, 71)),
            "Trk_Konomi_Terms: the private beat ignores its delay.");
        var outTerms = Program.Copy(recessed); outTerms.Flags.Add("konomi.trickster.cost.outfoxed");
        var envoyPages = new HashSet<string>();
        Program.Walk(terms, outTerms, (page, _) => envoyPages.Add(page));
        check(envoyPages.Contains("paid_envoy") && !envoyPages.Contains("paid"), "The outfoxed price forgot her name on the letter.");

        // Trk_Konomi_Commit / Trk_Konomi_Refusal: the named producer, and her soft no.
        var lover = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.trickster.terms_settled", "konomi.lovers");
        check(Rules.Available(story, priv, lover), "Trk_Konomi_Commit: the private beat is unavailable.");
        var privPages = new HashSet<string>();
        var privOut = Program.Walk(priv, lover, (page, _) => privPages.Add(page));
        check(privOut.Any(r => r.Has("konomi.committed")) && privPages.Contains("threshold") && privPages.Contains("morning"),
            "Trk_Konomi_Commit: [Take her hand] does not commit through the threshold.");
        var no = privOut.Where(r => r.Has("konomi.trickster.declined")).ToList();
        check(no.Count == 1 && !no[0].Has("konomi.committed") && !no[0].Has("arsinoe.closed") && !no[0].Has("konomi.closed"),
            "Trk_Konomi_Refusal: her soft no closes something.");
        check(!Rules.Available(story, priv, no[0]), "Her no is asked again at once.");
        var threshold = priv.Nodes.Single(n => n.Id == "threshold");
        check(threshold.Choices.Single().Next == "morning" && priv.Nodes.Single(n => n.Id == "answer").Choices[0].Set.Contains("konomi.committed"),
            "The committing answer is not [Take her hand].");
        // Sol BEL: a Commander who never courted her is asked why, at supper, before the private beat can commit.
        var colleague = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.trickster.terms_settled", "konomi.trickster.debt_paid");
        var uncourted = new HashSet<string>();
        var uncourtedOut = Program.Walk(priv, colleague, (page, _) => uncourted.Add(page));
        check(!uncourted.Contains("courted") && uncourtedOut.All(r => !r.Has("konomi.committed")), "The non-lover shortcut still commits.");
        check(Rules.Available(story, supper, colleague) && !Rules.Available(story, supper, lover), "The supper is mistimed or offered to a lover.");
        var supperPages = new HashSet<string>();
        var suppers = Program.Walk(supper, colleague, (page, _) => supperPages.Add(page));
        check(supperPages.Contains("letter") && !supperPages.Contains("favour") && suppers.Count(r => r.Has("konomi.trickster.supper_asked")) == 2
              && suppers.Any(r => r.Has(supper.Id) && !r.Has("konomi.trickster.supper_asked")), "The supper does not ask, or cannot be answered as a Commander.");
        var favoured = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.trickster.terms_settled", "konomi.trickster.favour_owed");
        var favourPages = new HashSet<string>();
        Program.Walk(supper, favoured, (page, _) => favourPages.Add(page));
        check(favourPages.Contains("favour") && !favourPages.Contains("letter"), "The supper bills a favour as a letter.");
        var colleagueTested = Program.Copy(colleague); colleagueTested.Flags.Add("konomi.trickster.supper_asked");
        var colleaguePages = new HashSet<string>();
        var colleagueOut = Program.Walk(priv, colleagueTested, (page, _) => colleaguePages.Add(page));
        check(colleaguePages.Contains("courted") && !colleaguePages.Contains("answer") && colleagueOut.Any(r => r.Has("konomi.trickster.envoy"))
              && colleagueOut.Any(r => r.Has("konomi.committed")) && colleagueOut.Any(r => r.Has("konomi.trickster.declined")),
            "A Commander who never courted her is not courted on the page, or cannot hear her no.");
        // Sol INT: "Give me a season" has its later ask, on her price, and she can still hold to envoy.
        check(!Rules.Available(story, season, no[0]) && Rules.Available(story, season, Later(story, no[0], 168)), "The season is mistimed.");
        var seasonPages = new HashSet<string>();
        var seasons = Program.Walk(season, Later(story, no[0], 168), (page, _) => seasonPages.Add(page));
        check(seasons.Any(r => r.Has("konomi.committed") && r.Has("konomi.trickster.asked_again")) && seasonPages.Contains("council")
              && seasons.Any(r => r.Has("konomi.trickster.envoy") && !r.Has("konomi.committed"))
              && seasons.Any(r => !r.Has(season.Id)), "The second ask: no yes on her price, no no, or no waiting.");

        // Trk_Konomi_RevivedThenDismissed: an earlier return does not block the dismissal device.
        var revived = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed",
                            "konomi.trickster.returned", "konomi.trickster.primed");
        check(Rules.Available(story, late, revived) && !Rules.Available(story, recess, revived),
            "Trk_Konomi_RevivedThenDismissed: the dismissal device is blocked by an earlier return.");

        // Trk_Konomi_FailedPath: canon fate stands; she leaves for Nerosyan.
        var failed = World(story, 5, "trickster.was", "trickster.ever", "trickster.failed", "konomi.dismissed", "konomi.office_completed");
        check(!Any(failed, late, recess), "Trk_Konomi_FailedPath: a device opened after the path failed.");

        // Trk_Konomi_Dead: the rider, the refusal, her fee; she comes back on her own terms.
        var dead = World(story, 3, "trickster", "trickster.ever", "konomi.retained_dead", "revive.konomi.available");
        check(Rules.Available(story, recalled, dead) && !Rules.Available(story, consult, dead), "Trk_Konomi_Dead: device unavailable.");
        check(!Rules.Available(story, S("konomi.retained_inquiry"), dead), "The map inquiry still opens beside the recall.");
        // Q12 (Sol INT): a completed ordinary farewell is a goodbye, not a refusal; it does not bar the recovery.
        var farewellDead = World(story, 3, "trickster", "trickster.ever", "konomi.farewell", "konomi.retained_dead", "revive.konomi.available");
        check(Rules.Available(story, recalled, farewellDead), "Trk_Konomi_Dead: her completed farewell locks out the recovery from a retained death.");
        var rider = recalled.Nodes[0].Choices[0];
        check(rider.Crusade?.Resource == "Finances" && rider.Crusade?.Amount == -300 && rider.Set.Contains("konomi.trickster.cost.recalled")
              && rider.Set.Contains("konomi.trickster.primed"), "Trk_Konomi_Dead: the rider lost its price.");
        var recallPages = new HashSet<string>();
        var recalls = Program.Walk(recalled, dead, (page, _) => recallPages.Add(page));
        var back = recalls.Where(r => r.Has(recalled.Id)).ToList();
        check(back.Count == 1 && back[0].Has("konomi.retained_return_confirmed") && back[0].Has("konomi.trickster.cost.consult_fee")
              && recallPages.Contains("refusal"), "Trk_Konomi_Dead: her soul does not refuse, then consent.");
        // Polish 9b: the recall is a rite by her own people, found through her own ledger; a correction alone raises nobody.
        check(back[0].Has("konomi.trickster.cost.her_people") && recallPages.Contains("ledger") && recallPages.Contains("rite"),
            "The recall works without a rite.");
        var bareCorrection = recalled.Nodes.Single(n => n.Id == "recall").Choices[0];
        check(!Rules.Match(bareCorrection.Requires, bareCorrection.Forbids, dead), "The dispatch correction still raises her on its own.");
        check(recalled.Nodes.SelectMany(n => n.Choices).Count(ch => ch.Revive == "konomi") == 1, "More than one revive in the recall.");
        var halfway = recalls.First(r => !r.Has(recalled.Id) && r.Has("konomi.trickster.cost.recalled"));
        var retry = Program.Walk(recalled, halfway);
        check(recalled.Nodes[0].Choices.Where(ch => Rules.Match(ch.Requires, ch.Forbids, halfway)).All(ch => ch.Crusade == null),
            "A second attempt pays the rider twice.");
        check(retry.Any(r => r.Has("konomi.retained_return_confirmed")), "A second attempt cannot finish the recall.");

        // Trk_Konomi_Consultation: triple, in advance; the registered map aftercare does not also play.
        var confirmed = World(story, 3, "trickster", "trickster.ever", "konomi.trickster.primed", "konomi.trickster.cost.recalled",
                              "konomi.retained_return_confirmed", "konomi.present");
        check(Rules.Available(story, consult, confirmed) && !Rules.Available(story, audience, confirmed),
            "Trk_Konomi_Consultation: consultation unavailable.");
        var consulted = Program.Walk(consult, confirmed);
        check(consulted.All(r => r.Has("konomi.trickster.returned") && !r.Has("konomi.return_meeting_accepted")),
            "Trk_Konomi_Consultation: the consultation does not return her, or reopens the map aftercare.");
        check(consult.Nodes[0].Choices[1].Crusade?.Amount == -300, "The fee paid in advance is free.");
        check(!Rules.Available(story, S("konomi.return_letter"),
                  World(story, 3, "trickster", "trickster.ever", "konomi.trickster.primed", "konomi.retained_return_confirmed",
                        "konomi.return_correspondence_available")), "The registered return letter opens beside the consultation.");
        var rejoined = Program.Copy(consulted[0]); rejoined.Flags.Add("konomi.present");
        check(Rules.Available(story, S("konomi.margin"), rejoined), "The returned Konomi cannot rejoin her registered route.");

        // Trk_Konomi_NeverArrived: the secretary's error on the page, then the audience in person.
        var never = World(story, 3, "trickster", "trickster.ever", "konomi.missed_contact_available");
        check(accredited.Nodes[0].Text.IndexOf("A week ago", StringComparison.Ordinal) < 0, "The informer is caught off the page, a week before.");
        check(audience.Nodes[0].Text.IndexOf("three months ago", StringComparison.Ordinal) < 0, "Arrears from before the register entry.");
        check(Rules.Available(story, accredited, never) && !Rules.Available(story, audience, never), "Trk_Konomi_NeverArrived: setup unavailable.");
        // PP5: the setup waits until its own account (the bow, two days to Nerosyan, two days back) is over.
        // PP5 r2 (Sol INT/HOW): the observation is transient and carries no hour; the latch records when it was first seen.
        check(never.Has("konomi.missed_contact.latched") && accredited.DelayHours == 96 && accredited.Requires.Contains("konomi.missed_contact.latched"),
            "PP5: the jug's account has no recorded start for its four days.");
        foreach (int waited in new[] { 95, 96 })
        {
            var seen = Program.Copy(never);
            seen.Times.Remove("konomi.missed_contact_available"); seen.Times.Remove("trickster"); seen.Times.Remove("trickster.ever");
            seen.Times["konomi.missed_contact.latched"] = seen.Hour - waited;
            check(Rules.Available(story, accredited, seen) == (waited == 96), "PP5: the jug's account ignores its four days at hour " + waited);
        }
        check(!Rules.Available(story, S("konomi.the_unintroduced_letter"), never), "The unintroduced letter still opens beside the jug.");
        var bowPages = new HashSet<string>();
        var bowed = Program.Walk(accredited, never, (page, _) => bowPages.Add(page)).Where(r => r.Has(accredited.Id)).ToList();
        // Two ways to use the chancery's informer (paid, or threatened with the rope); each sets the device flags and its cost.
        check(bowed.Count == 2 && bowed.All(r => r.Has("konomi.trickster.primed") && r.Has("konomi.trickster.cost.accredited")
              && r.Has("konomi.missed_letter_sent") && r.Has("konomi.trickster.slip_read")) && bowPages.Contains("nerosyan")
              && bowPages.Contains("slip") && bowPages.Contains("bow")
              && bowed.Count(r => r.Has("konomi.trickster.cost.steward_paid")) == 1
              && bowed.Count(r => r.Has("konomi.trickster.cost.steward_burned")) == 1, "Trk_Konomi_NeverArrived: wrong flags.");
        // PP5 (tier-A Ch5 budget): the chancery clerk's note is the setup's last page, not a second letter.
        var neverArrival = S("konomi.trickster.never_arrived.arrival");
        check(bowPages.Contains("clerk") && bowed.All(r => r.Has("konomi.trickster.arrived") && Later(story, r, 0).Has("konomi.trickster.presence_on"))
              && !Rules.Available(story, neverArrival, Later(story, bowed[0], 48)), "PP5: the jug's arrival is still a second delivery.");
        // A save between the bow and her arrival keeps the old note, and is not placed before it.
        var bowedOld = World(story, 3, "trickster", "trickster.ever", "konomi.missed_contact_available", "konomi.trickster.primed",
                             "konomi.trickster.cost.accredited", "konomi.missed_letter_sent");
        check(!bowedOld.Has("konomi.trickster.presence_on") && Rules.Available(story, neverArrival, bowedOld) && !Rules.Available(story, audience, bowedOld),
            "A save between the bow and the arrival lost its note, or was placed early.");
        var arrived = Later(story, bowed[0], 0);
        check(Rules.Available(story, audience, arrived) && arrived.Has("konomi.trickster.presence_on"), "Trk_Konomi_NeverArrived: no audience.");
        check(!Rules.Available(story, S("konomi.the_answer_she_addressed"), arrived), "The carrier's answer opens beside the audience.");
        var received = Program.Walk(audience, arrived);
        check(received.All(r => r.Has("konomi.trickster.returned") && r.Has("konomi.missed_appointment")), "The audience does not receive her.");
        var courtyard = S("konomi.the_courtyard_introduction");
        var yardPages = new HashSet<string>();
        var yardWorld = Later(story, received[0], 24);
        check(Rules.Available(story, courtyard, yardWorld), "The courtyard does not follow the audience.");
        Program.Walk(courtyard, yardWorld, (page, _) => yardPages.Add(page));
        check(yardPages.Contains("again_audience") && !yardPages.Contains("again") && !yardPages.Contains("first"),
            "The courtyard thanks her for a letter she never wrote.");
        var yardStart = courtyard.Nodes[0].Choices;
        check(yardStart[0].Next == "first" && yardStart[1].Next == "again" && yardStart.Last().Next == "again_audience",
            "Courtyard choices reordered instead of appended.");
        // Q12 (Sol COX/HOW): the never-arrived road's own short way to an answer, timed from the informer's bow, with no
        // romantic evidence seeded: the account for the jug (72 h after the audience) and her supper terms.
        var rooms = S("konomi.trickster.never_arrived.rooms");
        check(!Rules.Available(story, rooms, Later(story, received[0], 71)) && Rules.Available(story, rooms, Later(story, received[0], 72)),
            "Trk_Konomi_NeverArrived: her account comes before its time, or not at all.");
        var roomPages = new HashSet<string>();
        var roomOutcomes = Program.Walk(rooms, Later(story, received[0], 72), (page, _) => roomPages.Add(page));
        var supperKept = roomOutcomes.Where(r => r.Has("konomi.trickster.rooms_kept")).ToList();
        bool LateCommitted(Snapshot r) => World(story, 5, r.Flags.ToArray()).Has("konomi.trickster.late_committed");
        check(supperKept.Count > 0 && supperKept.All(r => LateCommitted(r) && r.Has("konomi.lovers"))
              && roomOutcomes.Any(r => r.Has("konomi.trickster.envoy") && !LateCommitted(r))
              && roomPages.Contains("accept") && roomPages.Contains("morning"),
            "Trk_Konomi_NeverArrived: her terms give no page, business only gives one, or the accepted terms skip the night.");
        check(48 + 72 <= 504 && Rules.Available(story, epCommit, World(story, 6, supperKept[0].Flags.ToArray()))
              && !Rules.Available(story, epCommit, World(story, 6, roomOutcomes.First(r => r.Has("konomi.trickster.envoy")).Flags.ToArray())),
            "Trk_Konomi_NeverArrived: the accepted terms do not reach her page, or the envoy's do.");
        // PP5 r2 (Sol INT): the journey paid at the audience is credited, the haggle is paid, and her office presence and
        // her account end while the registered chain has her on the road to Nerosyan.
        var auditioned = Program.Walk(audience, arrived).Where(r => r.Has(audience.Id)).ToList();
        var paidJourney = auditioned.Single(r => r.Has("konomi.trickster.journey_paid"));
        var unpaidJourney = auditioned.Single(r => !r.Has("konomi.trickster.journey_paid"));
        var account = rooms.Nodes[0].Choices;
        check(account.Count == 5 && account[0].Forbids.Contains("konomi.trickster.journey_paid") && account[1].Forbids.Contains("konomi.trickster.journey_paid")
              && account[2].Abort && account[3].Requires.Contains("konomi.trickster.journey_paid") && account[3].Crusade?.Amount == -50
              && account[4].Requires.Contains("konomi.trickster.journey_paid"), "PP5 r2: the account's choices were reordered, or bill the journey twice.");
        var paidPages = new HashSet<string>(); Program.Walk(rooms, Later(story, paidJourney, 72), (page, _) => paidPages.Add(page));
        var unpaidPages = new HashSet<string>(); Program.Walk(rooms, Later(story, unpaidJourney, 72), (page, _) => unpaidPages.Add(page));
        check(paidPages.Contains("paid_rest") && paidPages.Contains("haggle_rest") && !paidPages.Contains("paid") && !paidPages.Contains("haggle")
              && unpaidPages.Contains("paid") && unpaidPages.Contains("haggle") && !unpaidPages.Contains("paid_rest"),
            "PP5 r2: the journey paid at her door is billed again in her account.");
        check(rooms.Nodes.Single(n => n.Id == "haggle").Choices[0].Crusade?.Amount == -100
              && rooms.Nodes.Single(n => n.Id == "haggle_rest").Choices[0].Crusade?.Amount == -25, "PP5 r2: the haggled account is never paid.");
        var termsChoices = rooms.Nodes.Single(n => n.Id == "terms").Choices;
        check(termsChoices.Count == 3 && termsChoices[0].Forbids.Contains("konomi.trickster.cost.accredited") && termsChoices[1].Next == "business"
              && termsChoices[2].Next == "supper" && termsChoices[2].Set.Length == 0
              && new[] { "supper", "supper_no", "supper_who", "supper_you", "stay" }.All(unpaidPages.Contains),
            "PP5 r2 (Sol BEL): the threshold comes before the first supper and its personal exchange.");
        var inTown = World(story, 3, received[0].Flags.ToArray());
        var onTheRoad = World(story, 3, received[0].Flags.Concat(new[] { "konomi.private_departed" }).ToArray());
        check(Rules.PresenceWanted(presence!, inTown) && !Rules.PresenceWanted(presence!, onTheRoad)
              && Rules.Available(story, rooms, Later(story, inTown, 72)) && !Rules.Available(story, rooms, Later(story, onTheRoad, 72)),
            "PP5 r2: Konomi keeps her office while the registered chain has her on the road to Nerosyan.");
        // PP5 r2 (Sol COX, R2-6): the late yes reaches her Last Call coda.
        var konomiCoda = S("konomi.lastcall.page");
        check(konomiCoda.RequiresAnyGroups.Length == 1 && konomiCoda.RequiresAnyGroups[0].Contains("konomi.committed")
              && konomiCoda.RequiresAnyGroups[0].Contains("konomi.trickster.late_committed"), "PP5 r2: the late commit is missing from her Last Call coda.");
        // PP5 r2 (Sol VOI): Regill reads the paid informer and the burned one differently.
        var regillPaid = S("konomi.trickster.never_arrived.react_regill");
        var regillBurned = S("konomi.trickster.never_arrived.react_regill_burned");
        check(regillPaid.Requires.Contains("konomi.trickster.cost.steward_paid") && regillBurned.Requires.Contains("konomi.trickster.cost.steward_burned")
              && !regillBurned.Nodes[0].Text.Contains("door you left open"), "PP5 r2: Regill gives one verdict on two different informers.");
        var commitOffer = epCommit.Nodes[0].Choices;
        check(commitOffer.Count == 3 && commitOffer[0].Next == "signed" && commitOffer[1].Next == "terms" && commitOffer[2].Next == "dinner",
            "Trk_Konomi_LatePage: her late page has no unsettled answer, or its choices were reordered.");

        // Exclusivity across the three states (coexistence): one return per world.
        var all = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed", "konomi.retained_dead",
                        "revive.konomi.available", "konomi.missed_contact_available");
        check(!(Rules.Available(story, recalled, all) && Rules.Available(story, late, all)), "Recall and recess both open.");
        check(!Rules.Available(story, accredited, all), "The jug opens for a Konomi who came and was dismissed.");

        // Epilogues: the late commit is the Commander's answer; her soft no is its own page; paragraphs on her endings.
        var lateCommit = World(story, 6, "trickster", "trickster.ever", "konomi.dismissed", "konomi.trickster.recessed",
                               "konomi.trickster.terms_settled", "konomi.trickster.debt_paid", "konomi.private_future", "konomi.attracted",
                               "konomi.lovers");
        // Sol r3 BEL: a supper alone is not an intimate history; only the private beat's threshold commits a non-lover.
        var supperOnly = World(story, 6, "trickster", "trickster.ever", "konomi.dismissed", "konomi.trickster.terms_settled", "konomi.trickster.supper_asked");
        check(!supperOnly.Has("konomi.trickster.late_committed") && !Rules.Available(story, epCommit, supperOnly),
            "A supper completes the romance without an intimate beat.");
        check(Rules.Available(story, epCommit, lateCommit) && !Rules.Available(story, S("konomi.ending_unfinished"), lateCommit),
            "Trk_Konomi_EpilogueCommit failed.");
        check(epCommit.Nodes[0].Choices.Count == 3 && epCommit.Nodes[0].Choices.All(ch => ch.Next != null),
            "The late commit gives the Commander no answer.");
        // Sol r2 INT: a dead Commander (sacrifice without the shared finale's return) is given no living future.
        var diedLate = World(story, 6, lateCommit.Flags.Concat(new[] { "sacrifice", "ending.wound_closed" }).ToArray());
        check(!diedLate.Has("trickster.commander_back") && !Rules.Available(story, epCommit, diedLate), "A dead Commander rides to Nerosyan.");
        var backLate = World(story, 6, lateCommit.Flags.Concat(new[] { "sacrifice", "ending.trickster" }).ToArray());
        check(backLate.Has("trickster.commander_back") && Rules.Available(story, epCommit, backLate), "The surviving Commander loses the late commit.");
        // Sol r4 BEL: the registered living endings also need a living Commander.
        var deadPartner = World(story, 6, "konomi.committed", "konomi.power", "sacrifice");
        check(!Rules.Available(story, S("konomi.ending_private"), deadPartner) && Rules.Available(story, S("konomi.trickster.epilogue.sacrifice"), deadPartner),
            "A dead Commander keeps a living future with Konomi.");
        var backPartner = World(story, 6, "konomi.committed", "konomi.power", "sacrifice", "trickster", "trickster.ever", "ending.trickster");
        check(Rules.Available(story, S("konomi.ending_private"), backPartner) && !Rules.Available(story, S("konomi.trickster.epilogue.sacrifice"), backPartner),
            "The returned Commander is mourned.");
        // Sol r4 INT: the ordinary farewell does not bar the dismissal rescue.
        var farewell = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed", "konomi.farewell");
        check(Rules.Available(story, late, farewell), "A completed farewell blocks the dismissal rescue.");
        // Q12 (Sol INT): nor its courtship continuation, once her terms are settled.
        var farewellSettled = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed", "konomi.farewell",
                                    "konomi.trickster.recessed", "konomi.trickster.terms_settled", "konomi.trickster.cost.late", "konomi.trickster.back_from_the_road");
        check(Rules.Available(story, priv, Later(story, farewellSettled, 72)) && Rules.Available(story, supper, Later(story, farewellSettled, 72))
              && S("konomi.trickster.dismissed.a_season").Forbids.All(f => f != "konomi.farewell"),
            "A completed farewell blocks the courtship after the dismissal rescue.");
        var committedLate = Program.Copy(lateCommit); committedLate.Flags.Add("konomi.committed");
        check(!Rules.Available(story, epCommit, committedLate), "The late commit replays after a commit.");
        var soft = World(story, 6, "trickster", "trickster.ever", "konomi.dismissed", "konomi.trickster.terms_settled", "konomi.trickster.declined");
        check(Rules.Available(story, epRefused, soft) && !Rules.Available(story, epCommit, soft), "Trk_Konomi_EpilogueRefused failed.");
        // Sol INT: settled terms alone are not a romance; the envoy gets the envoy's page.
        var businessOnly = World(story, 6, "trickster", "trickster.ever", "konomi.dismissed", "konomi.trickster.terms_settled", "konomi.trickster.debt_paid");
        check(!businessOnly.Has("konomi.trickster.late_committed") && !Rules.Available(story, epCommit, businessOnly),
            "Settled terms read as a romance.");
        var envoyEnd = World(story, 6, "trickster", "trickster.ever", "konomi.dismissed", "konomi.trickster.terms_settled", "konomi.trickster.supper_asked",
                             "konomi.trickster.envoy");
        check(Rules.Available(story, epEnvoy, envoyEnd) && !Rules.Available(story, epCommit, envoyEnd) && !Rules.Available(story, epRefused, envoyEnd),
            "The envoy gets a romance ending.");
        var distance = S("konomi.ending_distance");
        var endRecess = World(story, 6, "trickster", "trickster.ever", "konomi.dismissed", "konomi.trickster.recessed", "konomi.trickster.cost.outfoxed",
                              "konomi.trickster.terms_settled", "konomi.private_future", "konomi.committed");
        check(Rules.Available(story, distance, endRecess)
              && distance.Nodes.Where(n => n.Paragraphs.Count > 0).All(n => Rules.VisibleParagraphs(n, endRecess).Length == 1),
            "The outfoxed paragraph is missing on her ending.");
        var endRecalled = World(story, 6, "trickster", "trickster.ever", "konomi.trickster.returned", "konomi.trickster.cost.recalled", "konomi.committed");
        check(S("konomi.ending_private").Nodes.Where(n => n.Paragraphs.Count > 0).All(n => Rules.VisibleParagraphs(n, endRecalled).Length == 1),
            "The framed dispatch is missing on her ending.");
        var canon = World(story, 6, "konomi.attracted");
        check(Rules.Available(story, S("konomi.ending_unfinished"), canon), "Off the path, the unfinished ending is lost.");

        // Retired, not deleted: saves already inside the old devices keep their continuations.
        check(!Rules.Available(story, S("konomi.fate_post"), dismissed), "The post office still opens beside the road.");
        check(Rules.Available(story, S("konomi.fate_reply"),
                  World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed", "konomi.post_sent")),
            "A save already inside the post office loses its reply.");
        // Polish 9b: the map attempt (a revive by Trickster power alone) is retired too; a save that prepared it gets the recall.
        var prepared = World(story, 3, "trickster", "trickster.ever", "konomi.retained_dead", "revive.konomi.available", "konomi.return_path_prepared");
        check(!Rules.Available(story, S("konomi.retained_attempt"), prepared) && Rules.Available(story, recalled, prepared),
            "The map attempt still revives her by power alone, or a prepared save has no recall.");

        // Reactions: Regill and Kyado only, one per state each; Kyado's road line needs his own canon observation.
        var reactions = story.Scenes.Where(s => s.Relationship == "konomi" && s.Reaction).ToArray();
        check(reactions.Length == 7 && reactions.All(r => r.Owner == "Regill" || r.Owner == "Kyado"), "Konomi reactions changed.");   // PP5 r2: + react_regill_burned
        var kyadoRoad = S("konomi.trickster.dismissed.react_kyado");
        var road = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.trickster.recessed", "kyado.in_drezen");
        check(!Rules.Available(story, kyadoRoad, road), "Kyado quotes a line he never said to this Commander.");
        road.Flags.Add("konomi.trickster.kyado_said_it");
        check(Rules.Available(story, kyadoRoad, road), "Kyado's road line missing.");
        check(!Rules.Available(story, S("konomi.trickster.dismissed.react_regill"),
                  World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.trickster.recessed", "regill.left_plot")),
            "Regill reacts after he has left.");

        // CommittedFlag reachable in every evaluated state.
        check(Commits(priv, lover), "Dismissed: no commit.");
        check(consulted.All(r => !r.Has("konomi.closed")), "Dead: the return closes her route.");
    }
}
