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
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
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
        check(joke.Mythic == "PlayerIsTrickster" && joke.Alignment?.Direction == "Chaotic" && joke.Alignment.Value == 1,
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
        var fresh = Program.Copy(dismissed); fresh.Times["konomi.dismissed.latched"] = fresh.Hour - 23;
        check(!Rules.Available(story, late, fresh), "The shout ignores the day after the insult.");
        check(!Rules.Available(story, late, World(story, 3, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed")),
            "The dismissal setup outside Chapter 5.");
        var pages = new HashSet<string>();
        var shouted = Program.Walk(late, dismissed, (page, _) => pages.Add(page)).Where(r => r.Has(late.Id)).ToList();
        check(shouted.Count == 1 && shouted[0].Has("konomi.trickster.primed") && shouted[0].Has("konomi.trickster.cost.late")
              && !pages.Contains("queen"), "Trk_Konomi_Dismissed: the minute sets the wrong flags.");
        var crowned = Program.Copy(dismissed); crowned.Flags.Add("coronation.seen");
        var queenPages = new HashSet<string>();
        Program.Walk(late, crowned, (page, _) => queenPages.Add(page));
        check(queenPages.Contains("queen"), "The Queen's eyebrow is missing after the Coronation.");
        crowned.Flags.Add("galfrey.dead");
        queenPages.Clear();
        Program.Walk(late, crowned, (page, _) => queenPages.Add(page));
        check(!queenPages.Contains("queen"), "A dead Queen raises an eyebrow.");
        var afterShout = Later(story, shouted[0], 48);
        check(Rules.Available(story, recess, afterShout) && !Rules.Available(story, late, afterShout), "Trk_Konomi_Dismissed: no recess.");
        check(!Rules.Available(story, recess, Later(story, shouted[0], 47)), "The recess ignores the three days on the road.");
        check(afterShout.Has("konomi.trickster.presence_on"), "Konomi not placed after the loop.");
        check(!dismissed.Has("konomi.trickster.presence_on"), "Konomi placed before the loop.");

        // Trk_Konomi_Recess: the fox contest; a failed bluff costs her own terms.
        var primed = World(story, 5, "trickster.ever", "konomi.dismissed", "konomi.office_completed", "konomi.trickster.primed",
                           "konomi.trickster.cost.late");
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
        var recessed = World(story, 5, "trickster.ever", "konomi.dismissed", "konomi.office_completed", "konomi.trickster.recessed");
        check(Rules.Available(story, terms, recessed), "Trk_Konomi_Terms: terms unavailable.");
        var price = terms.Nodes.Single(n => n.Id == "price").Choices;
        check(price[0].Crusade?.Resource == "Finances" && price[0].Crusade.Amount == -500 && price[1].Crusade?.Amount == -500,
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
        var lover = World(story, 5, "trickster.ever", "konomi.dismissed", "konomi.trickster.terms_settled", "konomi.lovers");
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
        var colleague = World(story, 5, "trickster.ever", "konomi.dismissed", "konomi.trickster.terms_settled");
        var colleagueOut = Program.Walk(priv, colleague);
        var colleaguePages = new HashSet<string>();
        colleagueOut = Program.Walk(priv, colleague, (page, _) => colleaguePages.Add(page));
        check(colleaguePages.Contains("courted") && !colleaguePages.Contains("answer") && colleagueOut.Any(r => r.Has("konomi.trickster.envoy"))
              && colleagueOut.Any(r => r.Has("konomi.committed")) && colleagueOut.Any(r => r.Has("konomi.trickster.declined")),
            "A Commander who never courted her is not courted on the page, or cannot hear her no.");

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
        var rider = recalled.Nodes[0].Choices[0];
        check(rider.Crusade?.Resource == "Finances" && rider.Crusade.Amount == -300 && rider.Set.Contains("konomi.trickster.cost.recalled")
              && rider.Set.Contains("konomi.trickster.primed"), "Trk_Konomi_Dead: the rider lost its price.");
        var recallPages = new HashSet<string>();
        var recalls = Program.Walk(recalled, dead, (page, _) => recallPages.Add(page));
        var back = recalls.Where(r => r.Has(recalled.Id)).ToList();
        check(back.Count == 1 && back[0].Has("konomi.retained_return_confirmed") && back[0].Has("konomi.trickster.cost.consult_fee")
              && recallPages.Contains("refusal"), "Trk_Konomi_Dead: her soul does not refuse, then consent.");
        check(recalled.Nodes.SelectMany(n => n.Choices).Count(ch => ch.Revive == "konomi") == 1, "More than one revive in the recall.");
        var halfway = recalls.First(r => !r.Has(recalled.Id) && r.Has("konomi.trickster.cost.recalled"));
        var retry = Program.Walk(recalled, halfway);
        check(recalled.Nodes[0].Choices.Where(ch => Rules.Match(ch.Requires, ch.Forbids, halfway)).All(ch => ch.Crusade == null),
            "A second attempt pays the rider twice.");
        check(retry.Any(r => r.Has("konomi.retained_return_confirmed")), "A second attempt cannot finish the recall.");

        // Trk_Konomi_Consultation: triple, in advance; the registered map aftercare does not also play.
        var confirmed = World(story, 3, "trickster.ever", "konomi.trickster.primed", "konomi.trickster.cost.recalled",
                              "konomi.retained_return_confirmed", "konomi.present");
        check(Rules.Available(story, consult, confirmed) && !Rules.Available(story, audience, confirmed),
            "Trk_Konomi_Consultation: consultation unavailable.");
        var consulted = Program.Walk(consult, confirmed);
        check(consulted.All(r => r.Has("konomi.trickster.returned") && !r.Has("konomi.return_meeting_accepted")),
            "Trk_Konomi_Consultation: the consultation does not return her, or reopens the map aftercare.");
        check(consult.Nodes[0].Choices[1].Crusade?.Amount == -300, "The fee paid in advance is free.");
        check(!Rules.Available(story, S("konomi.return_letter"),
                  World(story, 3, "trickster.ever", "konomi.trickster.primed", "konomi.retained_return_confirmed",
                        "konomi.return_correspondence_available")), "The registered return letter opens beside the consultation.");
        var rejoined = Program.Copy(consulted[0]); rejoined.Flags.Add("konomi.present");
        check(Rules.Available(story, S("konomi.margin"), rejoined), "The returned Konomi cannot rejoin her registered route.");

        // Trk_Konomi_NeverArrived: the secretary's error on the page, then the audience in person.
        var never = World(story, 3, "trickster", "trickster.ever", "konomi.missed_contact_available");
        check(Rules.Available(story, accredited, never) && !Rules.Available(story, audience, never), "Trk_Konomi_NeverArrived: setup unavailable.");
        check(!Rules.Available(story, S("konomi.the_unintroduced_letter"), never), "The unintroduced letter still opens beside the jug.");
        var bowPages = new HashSet<string>();
        var bowed = Program.Walk(accredited, never, (page, _) => bowPages.Add(page)).Where(r => r.Has(accredited.Id)).ToList();
        // Two ways to use the chancery's informer (paid, or threatened with the rope); each sets the device flags and its cost.
        check(bowed.Count == 2 && bowed.All(r => r.Has("konomi.trickster.primed") && r.Has("konomi.trickster.cost.accredited")
              && r.Has("konomi.missed_letter_sent")) && bowPages.Contains("nerosyan")
              && bowed.Count(r => r.Has("konomi.trickster.cost.steward_paid")) == 1
              && bowed.Count(r => r.Has("konomi.trickster.cost.steward_burned")) == 1, "Trk_Konomi_NeverArrived: wrong flags.");
        var arrived = Later(story, bowed[0], 48);
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

        // Exclusivity across the three states (coexistence): one return per world.
        var all = World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed", "konomi.retained_dead",
                        "revive.konomi.available", "konomi.missed_contact_available");
        check(!(Rules.Available(story, recalled, all) && Rules.Available(story, late, all)), "Recall and recess both open.");
        check(!Rules.Available(story, accredited, all), "The jug opens for a Konomi who came and was dismissed.");

        // Epilogues: the late commit is the Commander's answer; her soft no is its own page; paragraphs on her endings.
        var lateCommit = World(story, 6, "trickster.ever", "konomi.dismissed", "konomi.trickster.recessed",
                               "konomi.trickster.terms_settled", "konomi.trickster.debt_paid", "konomi.private_future", "konomi.attracted");
        check(Rules.Available(story, epCommit, lateCommit) && !Rules.Available(story, S("konomi.ending_unfinished"), lateCommit),
            "Trk_Konomi_EpilogueCommit failed.");
        check(epCommit.Nodes[0].Choices.Count == 2 && epCommit.Nodes[0].Choices.All(ch => ch.Next != null),
            "The late commit gives the Commander no answer.");
        var committedLate = Program.Copy(lateCommit); committedLate.Flags.Add("konomi.committed");
        check(!Rules.Available(story, epCommit, committedLate), "The late commit replays after a commit.");
        var soft = World(story, 6, "trickster.ever", "konomi.dismissed", "konomi.trickster.terms_settled", "konomi.trickster.declined");
        check(Rules.Available(story, epRefused, soft) && !Rules.Available(story, epCommit, soft), "Trk_Konomi_EpilogueRefused failed.");
        var distance = S("konomi.ending_distance");
        var endRecess = World(story, 6, "trickster.ever", "konomi.dismissed", "konomi.trickster.recessed", "konomi.trickster.cost.outfoxed",
                              "konomi.trickster.terms_settled", "konomi.private_future", "konomi.committed");
        check(Rules.Available(story, distance, endRecess)
              && distance.Nodes.Where(n => n.Paragraphs.Count > 0).All(n => Rules.VisibleParagraphs(n, endRecess).Length == 1),
            "The outfoxed paragraph is missing on her ending.");
        var endRecalled = World(story, 6, "trickster.ever", "konomi.trickster.returned", "konomi.trickster.cost.recalled", "konomi.committed");
        check(S("konomi.ending_private").Nodes.Where(n => n.Paragraphs.Count > 0).All(n => Rules.VisibleParagraphs(n, endRecalled).Length == 1),
            "The framed dispatch is missing on her ending.");
        var canon = World(story, 6, "konomi.attracted");
        check(Rules.Available(story, S("konomi.ending_unfinished"), canon), "Off the path, the unfinished ending is lost.");

        // Retired, not deleted: saves already inside the old devices keep their continuations.
        check(!Rules.Available(story, S("konomi.fate_post"), dismissed), "The post office still opens beside the road.");
        check(Rules.Available(story, S("konomi.fate_reply"),
                  World(story, 5, "trickster", "trickster.ever", "konomi.dismissed", "konomi.office_completed", "konomi.post_sent")),
            "A save already inside the post office loses its reply.");
        check(Rules.Available(story, S("konomi.retained_attempt"),
                  World(story, 3, "trickster", "trickster.ever", "konomi.retained_dead", "revive.konomi.available", "konomi.return_path_prepared"))
              && !Rules.Available(story, recalled,
                  World(story, 3, "trickster", "trickster.ever", "konomi.retained_dead", "revive.konomi.available", "konomi.return_path_prepared")),
            "A save already inside the map attempt loses it, or gets two recalls.");

        // Reactions: Regill and Kyado only, one per state each; Kyado's road line needs his own canon observation.
        var reactions = story.Scenes.Where(s => s.Relationship == "konomi" && s.Reaction).ToArray();
        check(reactions.Length == 6 && reactions.All(r => r.Owner == "Regill" || r.Owner == "Kyado"), "Konomi reactions changed.");
        var kyadoRoad = S("konomi.trickster.dismissed.react_kyado");
        var road = World(story, 5, "trickster.ever", "konomi.dismissed", "konomi.trickster.recessed", "kyado.in_drezen");
        check(!Rules.Available(story, kyadoRoad, road), "Kyado quotes a line he never said to this Commander.");
        road.Flags.Add("konomi.trickster.kyado_said_it");
        check(Rules.Available(story, kyadoRoad, road), "Kyado's road line missing.");
        check(!Rules.Available(story, S("konomi.trickster.dismissed.react_regill"),
                  World(story, 5, "trickster.ever", "konomi.dismissed", "konomi.trickster.recessed", "regill.left_plot")),
            "Regill reacts after he has left.");

        // CommittedFlag reachable in every evaluated state.
        check(Commits(priv, lover), "Dismissed: no commit.");
        check(consulted.All(r => !r.Has("konomi.closed")), "Dead: the return closes her route.");
    }
}
