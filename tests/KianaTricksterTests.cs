using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Kiana, Trickster (Writer/handoffs/trickster/kiana.md): the property that isn't there (F14) and the licence postponed
// (F02). One block per spec rules test (Trk_Kiana_*), plus the registered-route edits and Arsinoe's wedding line.
internal static class KianaTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Arsinoe = "a609ed9b2205d034bb3bb04d2a255681";
    private const string ArsinoeHub = "ecaf5cfe8087a4f45a2269974f4885c9";
    private const string Counterfeit = "3e4ce583dc71401588f33f8192c252cd";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.AvailableContacts.Add(Arsinoe);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 400;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours)
    {
        var later = Program.Copy(state); later.Hour += hours; Rules.Complete(story, later); return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var waited = S("kiana.trickster.aftermath.letter_waited");
        var gem = S("kiana.trickster.possessed.fake_gem");
        var collar = S("kiana.trickster.awake.dog_collar");
        var postponed = S("kiana.trickster.no_wedding.postponed");
        var temple = S("kiana.trickster.after.temple");
        var betrothal = S("kiana.betrothal");
        var epCommit = S("kiana.trickster.epilogue.commit");
        var devices = new[] { waited, gem, collar, postponed };
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));
        HashSet<string> Pages(Scene scene, Snapshot w) { var pages = new HashSet<string>(); Program.Walk(scene, w, (p, _) => pages.Add(p)); return pages; }
        Snapshot Pick(Scene scene, Snapshot w, params string[] flags)
        {
            var hit = Program.Walk(scene, w).FirstOrDefault(r => r.Has(scene.Id) && flags.All(r.Has));
            check(hit != null, "No path through " + scene.Id + " sets " + string.Join(", ", flags));
            return hit ?? w;
        }

        // Hooks and shape: every device is a Chapter 5 page; the one in-person beat is on Arsinoe's hub, on her actor.
        check(devices.All(d => d.Remote && d.TricksterDevice && d.Chapters.SequenceEqual(new[] { 5 })), "A device lost its page.");
        check(waited.TricksterState == "aftermath_missed" && gem.TricksterState == "possessed_no_rescue"
              && collar.TricksterState == "awake_no_rescue" && postponed.TricksterState == "wedding_never_happened", "Device states mislabelled.");
        check(temple.AnswerLists.SequenceEqual(new[] { ArsinoeHub }) && temple.ContactUnit == Arsinoe && !Rules.IsRemote(temple)
              && temple.Areas.SequenceEqual(new[] { Drezen }), "The pivot left Arsinoe's counter.");
        var rel = story.Relationships["kiana"];
        check(rel.TricksterAccess.Count == 4 && rel.TricksterAccess["aftermath_missed"].Returned == "kiana.trickster.met"
              && rel.TricksterAccess["possessed_no_rescue"].Returned == "kiana.trickster.returned", "Kiana access map missing.");
        check(story.Presences.TryGetValue("kiana.presence", out var presence) && presence.Unit == "180b0eaa5dce387458d2ebf0ee943985"
              && presence.Mode == "reuse-native", "Kiana presence missing.");
        var terms = gem.Nodes.Single(n => n.Id == "terms").Choices;
        check(terms[0].Mythic == "PlayerIsTrickster" && terms[0].Alignment?.Direction == "Chaotic" && terms[0].Alignment.Value == 1,
            "The appraisal lost its price.");
        check(terms[2].Crusade?.Resource == "Finances" && terms[2].Crusade.Amount == -1000, "Sunhammer's price is free.");
        var straight = gem.Nodes.Single(n => n.Id == "appraisal").Choices;
        var bluff = straight.Single(ch => ch.Forbids.Contains("trickster.arcana_tier3")).Check;
        var knowing = straight.Single(ch => ch.Requires.Contains("trickster.arcana_tier3")).Check;
        check(straight.Count == 2 && bluff != null && bluff.Skill == "CheckBluff" && bluff.DC == 20 && bluff.Success == "sold" && bluff.Failure == "bolted"
              && knowing != null && knowing.Skill == "CheckBluff" && knowing.DC < 20 && knowing.Success == "sold" && knowing.Failure == "bolted",
            "The straight face is not a Bluff check, or the arcana does more than lower its DC.");
        check(!gem.Nodes.Concat(collar.Nodes).Any(n => n.Text.Contains("property that is not there") || n.Text.Contains("None of it was true until")),
            "Trk_Kiana_NoPowerCrack (polish batch 9): an appraisal still makes the crack real.");
        var sendBack = gem.Nodes.Single(n => n.Id == "swapped").Choices.Single();
        check(sendBack.RemoveItem == Counterfeit && sendBack.Requires.Contains("kiana.counterfeit_held") && sendBack.Mythic == "PlayerIsTrickster",
            "The swap does not spend the counterfeit.");
        check(story.RemovableItems.Contains(Counterfeit), "Counterfeit not whitelisted for removal.");
        check(collar.Nodes[0].Choices[1].Crusade?.Amount == -1000, "The ransom of the guests is free.");

        // Trk_Kiana_AftermathSeen: the registered route runs; no device opens.
        var seen = World(story, 5, "trickster", "trickster.ever", "chapter_later", "seelah.souls_returned", "kiana.aftermath_seen",
                         "kiana.q2_done", "kiana.wedding_seen");
        check(Rules.Available(story, S("kiana.invitation"), seen) && !Any(seen, devices), "Trk_Kiana_AftermathSeen failed.");

        // Trk_Kiana_AftermathMissed: the letter that waited, for the widow and the wife.
        var missedWidow = World(story, 5, "trickster.ever", "chapter_later", "seelah.souls_returned", "seelah.elan_dead");
        check(Rules.Available(story, waited, missedWidow) && !Any(missedWidow, gem, collar, postponed, S("kiana.invitation")),
            "Trk_Kiana_AftermathMissed: the letter is unavailable.");
        var widowLetter = Program.Walk(waited, missedWidow);
        check(widowLetter.All(r => r.Has("kiana.history_widow") && r.Has("kiana.trickster.met") && r.Has("kiana.trickster.cost.letter_late")
                                   && (r.Has("kiana.moon") || r.Has("kiana.guest"))), "Trk_Kiana_AftermathMissed: wrong widow flags.");
        var afterLetter = Later(story, widowLetter[0], 48);
        check(Rules.Available(story, S("kiana.stagecraft"), afterLetter) && Rules.Available(story, S("kiana.widow"), Later(story, widowLetter[0], 168))
              && !Rules.Available(story, S("kiana.marriage"), afterLetter), "Trk_Kiana_AftermathMissed: the stagecraft or widow beat is shut.");
        var missedWife = World(story, 5, "trickster.ever", "chapter_later", "seelah.souls_returned");
        check(Program.Walk(waited, missedWife).All(r => r.Has("kiana.history_married") && !r.Has("kiana.history_widow")),
            "The letter makes a widow of a wife.");

        // Trk_Kiana_Ransom: the pay path buys the whole pouch and owes the favour.
        var possessed = World(story, 5, "trickster", "trickster.ever", "chapter_later", "kiana.possessed", "trickster.arcana_tier3");
        check(possessed.Has("kiana.soul_lost"), "The soul_lost latch does not hold.");
        check(Rules.Available(story, gem, possessed) && !Any(possessed, collar, postponed, waited), "Trk_Kiana_Ransom: device unavailable.");
        var gemOut = Program.Walk(gem, possessed).Where(r => r.Has(gem.Id)).ToList();
        var ransom = gemOut.Where(r => r.Has("kiana.trickster.cost.sunhammer_favour")).ToList();
        check(ransom.Count == 1 && ransom[0].Has("kiana.trickster.returned") && ransom[0].Has("kiana.trickster.guests_ransomed")
              && !ransom[0].Has("kiana.trickster.cost.guests_robbed") && !ransom[0].Has("kiana.trickster.primed"), "Trk_Kiana_Ransom: wrong flags.");
        check(gemOut.Count(r => r.Has("kiana.trickster.cost.guests_robbed")) == 2, "The appraisal does not reach both Bluff outcomes.");
        check(gemOut.Count(r => r.Has("kiana.trickster.cost.courier_marked")) == 1, "A failed Bluff does not mark the Commander.");
        check(!Pages(gem, possessed).Contains("swapped"), "The swap opens without the counterfeit.");

        // Trk_Kiana_NoArcana (polish batch 9, replacing batch 3): the con is the Commander's, not the arcana's. Without the
        // chosen TricksterKnowledgeArcanaTier3 the paste insult, the chisel and the swap all stay open; the arcana only
        // lowers the Bluff DC.
        var noArcana = World(story, 5, "trickster", "trickster.ever", "chapter_later", "kiana.possessed", "kiana.counterfeit_held");
        var plain = Program.Walk(gem, noArcana).Where(r => r.Has(gem.Id)).ToList();
        check(plain.Count(r => r.Has("kiana.trickster.cost.guests_robbed")) == 3 && plain.Any(r => r.Has("kiana.trickster.cost.counterfeit_spent"))
              && plain.Any(r => r.Has("kiana.trickster.cost.sunhammer_favour")),
            "Trk_Kiana_NoArcana: the chisel or the swap needs the arcana trick.");
        var plainAwake = World(story, 5, "trickster", "trickster.ever", "chapter_later", "kiana.q2_done", "seelah_dead");
        check(Program.Walk(collar, plainAwake).Any(r => r.Has("kiana.trickster.dog_saved")), "Trk_Kiana_NoArcana: the dog's stone needs the arcana trick.");
        // Trk_Kiana_Counterfeit: the preparation replaces the Bluff.
        var carrying = World(story, 5, "trickster", "trickster.ever", "chapter_later", "kiana.possessed", "kiana.counterfeit_held", "trickster.arcana_tier3");
        var swapped = Program.Walk(gem, carrying).Where(r => r.Has("kiana.trickster.cost.counterfeit_spent")).ToList();
        check(swapped.Count == 1 && !swapped[0].Has("kiana.trickster.cost.courier_marked") && swapped[0].Has("kiana.trickster.returned"),
            "Trk_Kiana_Counterfeit failed.");

        // Trk_Kiana_NoQ3: the latch holds after Seelah left; the pivot follows a day later on Arsinoe's hub.
        var noQ3 = World(story, 5, "trickster", "trickster.ever", "chapter_later", "kiana.possessed", "seelah_gone");
        check(Rules.Available(story, gem, noQ3) && !Any(noQ3, collar, postponed, waited), "Trk_Kiana_NoQ3: device unavailable.");
        var sold = gemOut.First(r => r.Has("kiana.trickster.cost.guests_robbed") && !r.Has("kiana.trickster.cost.courier_marked"));
        check(sold.Has("kiana.trickster.primed") && sold.Has("kiana.history_married"), "Trk_Kiana_NoQ3: wrong flags.");
        check(!Rules.Available(story, temple, Later(story, sold, 23)) && Rules.Available(story, temple, Later(story, sold, 24)),
            "Trk_Kiana_NoQ3: the pivot ignores its day.");
        var robbedPages = Pages(temple, Later(story, sold, 24));
        check(robbedPages.Contains("robbed") && robbedPages.Contains("told_robbed") && !robbedPages.Contains("late"), "The pivot opens on the wrong state.");
        var pivoted = Program.Walk(temple, Later(story, sold, 24));
        check(pivoted.All(r => r.Has("kiana.trickster.met") && r.Has("kiana.started")), "The pivot does not meet her.");
        check(pivoted.Any(r => r.Has("kiana.debt_claimed") && r.Has("kiana.closed")) && pivoted.Count(r => r.Has("kiana.closed")) == 1,
            "The evil answer at the pivot is missing, or closes more than itself.");
        var met = pivoted.First(r => !r.Has("kiana.closed"));

        // The guests the joke left behind: Sunhammer's revised terms, in person, three days after the pivot.
        var offer = S("kiana.trickster.pouch.second_offer");
        check(offer.AnswerLists.SequenceEqual(new[] { ArsinoeHub }) && offer.ContactUnit == Arsinoe && !Rules.IsRemote(offer),
            "The revised terms left Arsinoe's counter.");
        check(!Rules.Available(story, offer, Later(story, met, 71)) && Rules.Available(story, offer, Later(story, met, 72)),
            "The revised terms ignore their delay.");
        check(!Rules.Available(story, offer, Later(story, ransom[0], 200)), "The revised terms reach a Commander who bought everyone.");
        check(offer.Nodes[0].Choices[0].Crusade?.Amount == -1000, "Buying the guests back is free.");
        var offered = Program.Walk(offer, Later(story, met, 72)).Where(r => r.Has(offer.Id)).ToList();
        var bought = offered.SingleOrDefault(r => r.Has("kiana.trickster.guests_bought_back"));
        var vowed = offered.SingleOrDefault(r => r.Has("kiana.trickster.pouch_vow"));
        check(bought != null && bought.Has("kiana.trickster.cost.apology") && bought.Has("kiana.trickster.cost.sunhammer_favour")
              && vowed != null && !vowed.Has("kiana.trickster.cost.sunhammer_favour") && offered.All(r => !r.Has("kiana.closed")),
            "The revised terms do not offer the price or the vow.");
        var boughtEnd = Program.Copy(bought!); boughtEnd.Flags.Add("kiana.committed"); boughtEnd.Chapter = 6;
        var boughtParas = Rules.VisibleParagraphs(S("kiana.ending_promised").Nodes[0], boughtEnd).Select(x => x.Text).ToArray();
        check(boughtParas.Any(t => t.Contains("apology")) && !boughtParas.Any(t => t.Contains("never came back")),
            "The ending forgets the guests who came home.");
        var vowEnd = Program.Copy(vowed!); vowEnd.Flags.Add("kiana.committed"); vowEnd.Chapter = 6;
        check(Rules.VisibleParagraphs(S("kiana.ending_promised").Nodes[0], vowEnd).Any(x => x.Text.Contains("promise")),
            "The ending forgets the Commander's word.");
        check(!Rules.Available(story, S("kiana.trickster.possessed.react_arsinoe_stones"), bought!), "Arsinoe mourns guests who came home.");

        // Trk_Kiana_Stagecraft_S2 and the spine to the commit (marriage -> answer -> date -> morning).
        var s2 = Later(story, met, 48);
        check(Rules.Available(story, S("kiana.stagecraft"), s2) && Rules.Available(story, S("kiana.marriage"), s2)
              && !Rules.Available(story, S("kiana.widow"), s2) && !Rules.Available(story, betrothal, s2), "Trk_Kiana_Stagecraft_S2 failed.");
        var wife = Pick(S("kiana.marriage"), s2, "kiana.attracted", "kiana.waited");
        var separated = Pick(S("kiana.answer"), Later(story, wife, 120), "kiana.separated", "kiana.available");
        var datePages = Pages(S("kiana.date"), Later(story, separated, 168));
        check(datePages.Contains("threshold") && datePages.Contains("morning_after"), "The Trickster night stops before the cut.");
        var lovers = Pick(S("kiana.date"), Later(story, separated, 168), "kiana.lovers", "kiana.kissed");
        var committed = Pick(S("kiana.morning"), Later(story, lovers, 48), "kiana.committed");
        check(!Rules.Available(story, S("kiana.guest_table"), Later(story, committed, 200)),
            "The post-commitment chain opens on a Trickster entry (TT-21 cap).");
        var ending = S("kiana.ending_promised");
        var end = Later(story, committed, 1); end.Chapter = 6;
        check(Rules.Available(story, ending, end) && Rules.VisibleParagraphs(ending.Nodes[0], end).Length == 2,
            "The committed ending lost the stones or Elan paragraph.");
        var q3Lovers = World(story, 5, "seelah.souls_returned", "kiana.lovers", "kiana.morning");
        check(Rules.Available(story, S("kiana.guest_table"), Later(story, q3Lovers, 48)), "The registered chain is shut on the Q3 route.");
        var plainNight = World(story, 5, "seelah.souls_returned", "kiana.available");
        check(!Pages(S("kiana.date"), plainNight).Contains("threshold"), "The Trickster night plays off the path.");

        // Trk_Kiana_PathFailed: canon fate stands.
        var failed = World(story, 5, "trickster.was", "trickster.ever", "trickster.failed", "chapter_later", "kiana.possessed");
        check(!Any(failed, gem, collar, postponed), "Trk_Kiana_PathFailed: a device opened after the path failed.");

        // Trk_Kiana_LateQ3: a revived Seelah finishing Q3 after the device does not open a second entry.
        var lateQ3 = World(story, 5, "trickster.ever", "chapter_later", "kiana.possessed", "kiana.trickster.returned", "kiana.trickster.met",
                           "seelah.souls_returned", "kiana.aftermath_seen");
        check(!Any(lateQ3, gem, waited, S("kiana.invitation")), "Trk_Kiana_LateQ3: a second entry opens.");
        var lateTemple = World(story, 5, "trickster.ever", "chapter_later", "kiana.possessed", "kiana.trickster.returned",
                               "kiana.trickster.cost.guests_robbed", "seelah.souls_returned");
        check(!Rules.Available(story, S("kiana.invitation"), lateTemple), "The invitation opens beside the device.");
        var latePages = Pages(temple, lateTemple);
        check(latePages.Contains("late") && latePages.Contains("told_late") && !latePages.Contains("robbed"), "The late-Q3 pivot is missing.");

        // Trk_Kiana_AwakeNoQ3 / AwakePaid: the dog, or every guest for the favour.
        var awake = World(story, 5, "trickster", "trickster.ever", "chapter_later", "kiana.q2_done", "seelah_dead", "trickster.arcana_tier3");
        check(Rules.Available(story, collar, awake) && !Any(awake, gem, postponed, waited), "Trk_Kiana_AwakeNoQ3: device unavailable.");
        var collarOut = Program.Walk(collar, awake).Where(r => r.Has(collar.Id)).ToList();
        var dog = collarOut.Single(r => r.Has("kiana.trickster.dog_saved"));
        check(dog.Has("kiana.trickster.returned") && dog.Has("kiana.trickster.cost.guests_robbed"), "Trk_Kiana_AwakeNoQ3: wrong flags.");
        var paid = collarOut.Single(r => r.Has("kiana.trickster.cost.sunhammer_favour"));
        check(!paid.Has("kiana.trickster.cost.guests_robbed") && !paid.Has("kiana.trickster.primed"), "Trk_Kiana_AwakePaid: wrong flags.");
        check(Pages(temple, Later(story, dog, 24)).Contains("told_dog") && Pages(temple, Later(story, paid, 24)).Contains("ransomed_awake"),
            "The awake pivot opens on the wrong state.");
        var s3 = Later(story, Program.Walk(temple, Later(story, dog, 24)).First(r => !r.Has("kiana.closed")), 48);
        check(Rules.Available(story, S("kiana.stagecraft"), s3) && Rules.Available(story, S("kiana.marriage"), s3), "Trk_Kiana_Stagecraft_S3 failed.");

        // Trk_Kiana_NoWedding_King / _Order: the stamp is a real act; signing is the decline.
        var king = World(story, 5, "trickster", "trickster.ever", "chapter_later", "fool_king.crowned");
        check(Rules.Available(story, postponed, king) && !Any(king, gem, collar, waited), "Trk_Kiana_NoWedding_King: device unavailable.");
        var desk = postponed.Nodes[0].Choices;
        check(desk[0].Crusade?.Amount == -300 && desk[0].Mythic == "PlayerIsTrickster" && desk[1].Crusade?.Amount == -100 && desk[2].Crusade?.Amount == -100,
            "The King's fee or the order's forfeited deposits are wrong.");
        var kingOut = Program.Walk(postponed, king).Where(r => r.Has(postponed.Id)).ToList();
        check(kingOut.Any(r => r.Has("kiana.trickster.decree_king") && r.Has("kiana.trickster.cost.betrothed") && r.Has("kiana.history_betrothed")),
            "Trk_Kiana_NoWedding_King failed.");
        check(!kingOut.Any(r => r.Has("kiana.trickster.cost.betrothed") && !r.Has("kiana.trickster.decree_king")),
            "The war-council order opens beside a sober-less King.");
        var noKing = World(story, 5, "trickster", "trickster.ever", "chapter_later");
        var orderOut = Program.Walk(postponed, noKing).Where(r => r.Has(postponed.Id)).ToList();
        check(orderOut.Any(r => r.Has("kiana.trickster.cost.betrothed") && !r.Has("kiana.trickster.decree_king")), "Trk_Kiana_NoWedding_Order failed.");
        check(orderOut.Any(r => r.Has("kiana.trickster.licence_signed") && r.Has("kiana.closed") && !r.Has("kiana.trickster.returned")),
            "Signing the licence is not the decline.");
        var goneKing = World(story, 5, "trickster", "trickster.ever", "chapter_later", "fool_king.crowned", "fool_king.gone");
        check(Program.Walk(postponed, goneKing).Any(r => r.Has("kiana.trickster.cost.betrothed") && !r.Has("kiana.trickster.decree_king")),
            "Without a living King the order is missing.");

        // Trk_Kiana_Stagecraft_S4: the betrothed history has its own beat; the marriage beats stay shut.
        var fiancee = Pick(postponed, noKing, "kiana.history_betrothed");
        var licencePages = Pages(temple, Later(story, fiancee, 24));
        check(licencePages.Contains("licence") && licencePages.Contains("told_licence") && !licencePages.Contains("pivot"),
            "The betrothed pivot opens on the wrong page.");
        var s4 = Later(story, Program.Walk(temple, Later(story, fiancee, 24)).First(r => !r.Has("kiana.closed")), 48);
        check(Rules.Available(story, S("kiana.stagecraft"), s4) && !Any(s4, S("kiana.marriage"), S("kiana.widow"), betrothal),
            "Trk_Kiana_Stagecraft_S4 failed.");
        var rehearsed = Pick(S("kiana.stagecraft"), s4, "kiana.rehearsed");
        check(!Rules.Available(story, betrothal, Later(story, rehearsed, 71)) && Rules.Available(story, betrothal, Later(story, rehearsed, 72)),
            "The betrothal ignores its delay.");
        var betrothalOut = Program.Walk(betrothal, Later(story, rehearsed, 72));
        check(betrothalOut.Any(r => r.Has("kiana.betrothed_kept") && r.Has("kiana.closed")), "She cannot keep her engagement.");
        var free = betrothalOut.Single(r => r.Has("kiana.available"));
        check(free.Has("kiana.separated") && free.Has("kiana.waited"), "A broken engagement leaves the later beats without a history.");
        var s4Lovers = Pick(S("kiana.date"), Later(story, free, 168), "kiana.lovers");
        check(Program.Walk(S("kiana.morning"), Later(story, s4Lovers, 48)).Any(r => r.Has("kiana.committed")), "Trk_Kiana_NoWedding: no commit.");
        var decreeEnd = Later(story, Pick(S("kiana.morning"), Later(story, s4Lovers, 48), "kiana.committed"), 1); decreeEnd.Chapter = 6;
        check(Rules.VisibleParagraphs(ending.Nodes[0], decreeEnd).Length == 2, "The decree paragraphs are missing.");

        // Late commit (R2-6) and her "not yet": the page for a spine cut short, the unfinished twin for kiana.uncertain.
        var late = World(story, 6, "trickster.ever", "kiana.trickster.met", "kiana.lovers", "kiana.attracted", "kiana.history_married");
        check(Rules.Available(story, epCommit, late) && !Any(late, S("kiana.ending_unfinished"), S("kiana.trickster.ending_unfinished")),
            "Trk_Kiana_EpilogueCommit failed.");
        check(epCommit.Nodes[0].Choices.Count == 2 && epCommit.Nodes[0].Choices.All(ch => ch.Next != null), "The late commit gives no answer.");
        var notYet = World(story, 6, "trickster.ever", "kiana.trickster.met", "kiana.lovers", "kiana.attracted", "kiana.morning", "kiana.uncertain");
        check(!Rules.Available(story, epCommit, notYet) && Rules.Available(story, S("kiana.trickster.ending_unfinished"), notYet)
              && !Rules.Available(story, S("kiana.ending_unfinished"), notYet), "Her 'then don't promise it' is not honoured.");
        var attracted = World(story, 6, "trickster.ever", "kiana.trickster.met", "kiana.attracted");
        check(Rules.Available(story, S("kiana.trickster.ending_unfinished"), attracted) && !Rules.Available(story, epCommit, attracted),
            "An attraction that never became an evening has no ending.");
        check(Rules.Available(story, S("kiana.ending_unfinished"), World(story, 6, "kiana.attracted")), "Off the path, the unfinished ending is lost.");
        var claimedEnd = World(story, 6, "kiana.debt_claimed", "kiana.closed", "kiana.trickster.met");
        check(Rules.Available(story, S("kiana.trickster.epilogue.debt"), claimedEnd), "The claimed debt has no ending.");

        // KIA-14: Seelah speaks while she is in the party; no Forbid on her death or departure.
        var seelah = S("kiana.seelah");
        check(seelah.Requires.Contains("seelah.in_party") && !seelah.Forbids.Contains("seelah_dead") && !seelah.Forbids.Contains("seelah_gone"),
            "KIA-14 not applied.");

        // Arsinoe's collection bills the wedding; choices appended, never reordered.
        var collection = S("arsinoe.trickster.cauldron.collection");
        var cStart = collection.Nodes[0].Choices;
        check(cStart[0].Next == "pledge" && cStart[1].Next == "rider" && cStart[2].Next == "wedding" && cStart[3].Next == "wedding_dog",
            "Collection choices reordered instead of appended.");
        var ledger = World(story, 5, "trickster.ever", "arsinoe.capital", "arsinoe.trickster.primed", "arsinoe.trickster.cost.lien",
                           "arsinoe.trickster.cauldron.lease", "kiana.possessed", "kiana.trickster.cost.guests_robbed");
        var ledgerPages = Pages(collection, ledger);
        check(ledgerPages.Contains("wedding") && !ledgerPages.Contains("rider") && !ledgerPages.Contains("wedding_dog"), "Arsinoe's wedding line is missing.");
        ledger.Flags.Add("konomi.trickster.cost.recalled");
        ledgerPages = Pages(collection, ledger);
        check(ledgerPages.Contains("wedding") && ledgerPages.Contains("rider"), "The wedding line skips the rider.");
        ledger.Flags.Add("seelah.souls_returned");
        ledgerPages = Pages(collection, ledger);
        check(!ledgerPages.Contains("wedding") && ledgerPages.Contains("rider"), "Arsinoe bills a wedding Seelah already settled.");
        ledger.Flags.Remove("seelah.souls_returned"); ledger.Flags.Add("kiana.trickster.guests_bought_back");
        ledgerPages = Pages(collection, ledger);
        check(!ledgerPages.Contains("wedding") && ledgerPages.Contains("rider"), "Arsinoe bills guests the Commander bought back.");

        // Reactions: Arsinoe, Anevia, Irabeth only; Anevia's lift with her return, Irabeth's with hers.
        var reactions = story.Scenes.Where(s => s.Relationship == "kiana" && s.Reaction).ToArray();
        check(reactions.Length == 10 && reactions.All(r => r.Owner == "Arsinoe" || r.Owner == "Anevia" || r.Owner == "Irabeth"),
            "Kiana reactions changed.");
        var aneviaDog = S("kiana.trickster.awake.react_anevia");
        var dogWorld = World(story, 5, "trickster.ever", "kiana.trickster.returned", "kiana.trickster.dog_saved", "anevia_gone");
        check(!Rules.Available(story, aneviaDog, dogWorld), "Anevia reacts while gone.");
        dogWorld.Flags.Add("anevia.trickster.returned");
        check(Rules.Available(story, aneviaDog, dogWorld), "Anevia's return does not lift her reaction.");
        check(!Rules.Available(story, S("kiana.trickster.possessed.react_arsinoe_stones"), dogWorld), "The possessed-ward line plays for the dog.");

        // Exclusivity: one device per world.
        foreach (var w in new[] { seen, missedWife, possessed, awake, noKing })
            check(devices.Count(d => Rules.Available(story, d, w)) <= 1, "Two Kiana devices open in one world.");
    }
}
