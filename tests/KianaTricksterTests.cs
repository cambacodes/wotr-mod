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
    private const string Kyana = "180b0eaa5dce387458d2ebf0ee943985";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000,
            // eng-final / E-Q8-10: fund these positive histories; the walker enforces every debit.
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        if (Rules.ChapterFlag(chapter) is string chapterFlag) state.Flags.Add(chapterFlag);
        state.AvailableContacts.Add(Arsinoe);
        state.AvailableContacts.Add(Kyana);   // Q10: her spawned copy stands at Arsinoe's counter
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
        KianaPartnerTests.Run(story, check);
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
        check(story.Presences.TryGetValue("kiana.presence", out var presence) && presence.Unit == Kyana
              && presence.Mode == "spawn-copy" && presence.At?.NearUnit == Arsinoe && presence.Dialog == "hub", "Kiana presence missing.");
        check(temple.AdditionalContactUnits.SequenceEqual(new[] { Kyana }), "Q10: the pivot plays without Kiana's own actor.");
        var terms = gem.Nodes.Single(n => n.Id == "terms").Choices;
        check(terms[0].Mythic == "PlayerIsTrickster" && terms[0].Alignment?.Direction == "Chaotic" && terms[0].Alignment?.Value == 1,
            "The appraisal lost its price.");
        check(terms[2].Crusade?.Resource == "Finances" && terms[2].Crusade?.Amount == -1000, "Sunhammer's price is free.");
        var straight = gem.Nodes.Single(n => n.Id == "appraisal").Choices;
        var bluff = straight.Single(ch => ch.Forbids.Contains("trickster.arcana_tier3")).Check;
        var knowing = straight.Single(ch => ch.Requires.Contains("trickster.arcana_tier3")).Check;
        check(straight.Count == 2 && bluff != null && bluff.Skill == "CheckBluff" && bluff.DC == 20 && bluff.Success == "sold" && bluff.Failure == "bolted"
              && knowing != null && knowing.Skill == "CheckBluff" && knowing.DC < 20 && knowing.Success == "sold" && knowing.Failure == "bolted",
            "The straight face is not a Bluff check, or the arcana does more than lower its DC.");
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
        var missedWidow = World(story, 5, "trickster", "trickster.ever", "chapter_later", "seelah.souls_returned", "seelah.elan_dead", "kiana.wedding_seen");
        check(Rules.Available(story, waited, missedWidow) && !Any(missedWidow, gem, collar, postponed, S("kiana.invitation")),
            "Trk_Kiana_AftermathMissed: the letter is unavailable.");
        var widowLetter = Program.Walk(waited, missedWidow);
        check(widowLetter.All(r => r.Has("kiana.history_widow") && r.Has("kiana.trickster.met") && r.Has("kiana.trickster.cost.letter_late")
                                   && (r.Has("kiana.moon") || r.Has("kiana.guest"))), "Trk_Kiana_AftermathMissed: wrong widow flags.");
        var afterLetter = Later(story, widowLetter[0], 48);
        check(Rules.Available(story, S("kiana.stagecraft"), afterLetter) && Rules.Available(story, S("kiana.widow"), Later(story, widowLetter[0], 168))
              && !Rules.Available(story, S("kiana.marriage"), afterLetter), "Trk_Kiana_AftermathMissed: the stagecraft or widow beat is shut.");
        var missedWife = World(story, 5, "trickster", "trickster.ever", "chapter_later", "seelah.souls_returned", "kiana.wedding_seen");
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
        var boughtParas = Rules.VisibleParagraphs(S("kiana.ending_promised").Nodes[0], boughtEnd).Select(x => SurfaceIds.Of(story, x)).ToArray();
        check(SurfaceIds.Has(boughtParas, "[kiana.ending_promised/start/paragraph/2]") && !SurfaceIds.Has(boughtParas, "[kiana.ending_promised/start/paragraph/0][kiana.ending_promised/start/paragraph/1]"),
            "The ending forgets the guests who came home.");
        var vowEnd = Program.Copy(vowed!); vowEnd.Flags.Add("kiana.committed"); vowEnd.Chapter = 6;
        check(Rules.VisibleParagraphs(S("kiana.ending_promised").Nodes[0], vowEnd).Any(x => SurfaceIds.Has(SurfaceIds.Of(story, x), "[kiana.ending_promised/start/paragraph/3]")),
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
        check(Rules.Available(story, ending, end) && Rules.VisibleParagraphs(ending.Nodes[0], end).Count(p => ending.Nodes[0].Paragraphs.Take(12).Contains(p)) == 2,
            "The committed ending lost the stones or Elan paragraph.");
        var q3Lovers = World(story, 5, "seelah.souls_returned", "kiana.lovers", "kiana.morning");
        check(Rules.Available(story, S("kiana.guest_table"), Later(story, q3Lovers, 48)), "The registered chain is shut on the Q3 route.");
        var plainNight = World(story, 5, "seelah.souls_returned", "kiana.available");
        check(!Pages(S("kiana.date"), plainNight).Contains("threshold"), "The Trickster night plays off the path.");

        // Trk_Kiana_PathFailed: canon fate stands.
        var failed = World(story, 5, "trickster.was", "trickster.ever", "trickster.failed", "chapter_later", "kiana.possessed");
        check(!Any(failed, gem, collar, postponed), "Trk_Kiana_PathFailed: a device opened after the path failed.");

        // Trk_Kiana_LateQ3: a revived Seelah finishing Q3 after the device does not open a second entry.
        var lateQ3 = World(story, 5, "trickster", "trickster.ever", "chapter_later", "kiana.possessed", "kiana.trickster.returned", "kiana.trickster.met",
                           "seelah.souls_returned", "kiana.aftermath_seen");
        check(!Any(lateQ3, gem, waited, S("kiana.invitation")), "Trk_Kiana_LateQ3: a second entry opens.");
        var lateTemple = World(story, 5, "trickster", "trickster.ever", "chapter_later", "kiana.possessed", "kiana.trickster.returned",
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
        var free = betrothalOut.Single(r => r.Has("kiana.available") && r.Has("kiana.separated"));
        check(free.Has("kiana.separated") && free.Has("kiana.waited"), "A broken engagement leaves the later beats without a history.");
        var s4Lovers = Pick(S("kiana.date"), Later(story, free, 168), "kiana.lovers");
        check(Program.Walk(S("kiana.morning"), Later(story, s4Lovers, 48)).Any(r => r.Has("kiana.committed")), "Trk_Kiana_NoWedding: no commit.");
        var decreeEnd = Later(story, Pick(S("kiana.morning"), Later(story, s4Lovers, 48), "kiana.committed"), 1); decreeEnd.Chapter = 6;
        check(Rules.VisibleParagraphs(ending.Nodes[0], decreeEnd).Count(p => ending.Nodes[0].Paragraphs.Take(12).Contains(p)) == 2, "The decree paragraphs are missing: " + string.Join(", ", Rules.VisibleParagraphs(ending.Nodes[0], decreeEnd).Select(p => SurfaceIds.Of(story, p))));

        // Late commit (R2-6) and her "not yet": the page for a spine cut short, the unfinished twin for kiana.uncertain.
        var late = World(story, 6, "trickster", "trickster.ever", "kiana.trickster.met", "kiana.lovers", "kiana.attracted", "kiana.history_married");
        check(Rules.Available(story, epCommit, late) && !Any(late, S("kiana.ending_unfinished"), S("kiana.trickster.ending_unfinished")),
            "Trk_Kiana_EpilogueCommit failed.");
        check(epCommit.Nodes[0].Choices.Count == 8 && epCommit.Nodes[0].Choices.All(ch => ch.Next != null), "The late commit gives no answer.");
        var notYet = World(story, 6, "trickster", "trickster.ever", "kiana.trickster.met", "kiana.lovers", "kiana.attracted", "kiana.morning", "kiana.uncertain");
        check(!Rules.Available(story, epCommit, notYet) && Rules.Available(story, S("kiana.trickster.ending_unfinished"), notYet)
              && !Rules.Available(story, S("kiana.ending_unfinished"), notYet), "Her 'then don't promise it' is not honoured.");
        var attracted = World(story, 6, "trickster", "trickster.ever", "kiana.trickster.met", "kiana.attracted");
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
        var ledger = World(story, 5, "trickster", "trickster.ever", "arsinoe.capital", "arsinoe.trickster.primed", "arsinoe.trickster.cost.lien",
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
        check(reactions.Length == 13 && reactions.Count(r => r.Id.EndsWith(".history_neutral", StringComparison.Ordinal)) == 1 && reactions.All(r => r.Owner == "Arsinoe" || r.Owner == "Anevia" || r.Owner == "Irabeth"),
            "Kiana reactions changed.");
        var aneviaDog = S("kiana.trickster.awake.react_anevia");
        var dogWorld = World(story, 5, "trickster", "trickster.ever", "kiana.trickster.returned", "kiana.trickster.dog_saved", "anevia_gone");
        check(!Rules.Available(story, aneviaDog, dogWorld), "Anevia reacts while gone.");
        dogWorld.Flags.Add("anevia.trickster.returned");
        check(Rules.Available(story, aneviaDog, dogWorld), "Anevia's return does not lift her reaction.");
        check(!Rules.Available(story, S("kiana.trickster.possessed.react_arsinoe_stones"), dogWorld), "The possessed-ward line plays for the dog.");

        // Q10 (HOW): every spine beat waits at most 72 hours (spec section 6 budget).
        foreach (var id in new[] { "kiana.stagecraft", "kiana.marriage", "kiana.widow", "kiana.answer", "kiana.date", "kiana.morning", "kiana.betrothal" })
            check(S(id).DelayHours <= 72, "Q10: a Kiana spine beat waits more than 72 hours: " + id);
        // Q10 (COX): a native Q3 entry on a Trickster run keeps to the Chapter 5 letter budget; off the path the chain stays.
        check(!Rules.Available(story, S("kiana.guest_table"), Later(story, World(story, 5, "trickster", "trickster.ever", "seelah.souls_returned", "kiana.lovers", "kiana.morning"), 48)),
            "Q10: the post-commitment chain opens on a native Q3 entry on a Trickster run.");
        // Q10 (INT): after either ransom Arsinoe answers for the recovered patients on her own hub; Q3 settles it natively.
        var home = S("kiana.trickster.react_arsinoe_souls_home");
        check(home.AnswerLists.SequenceEqual(new[] { ArsinoeHub }), "Q10: the souls-home answer left Arsinoe's hub.");
        // eng7-l02: both paid recoveries speak, with/without the actual native locating vision.
        var homeNeutral = S(home.Id + ".history_neutral");
        foreach (var payPath in new[] { "kiana.trickster.guests_ransomed", "kiana.trickster.guests_bought_back" })
        {
            var recovered = World(story, 5, "trickster", "trickster.ever", "kiana.trickster.met", payPath);
            check(Rules.Available(story, homeNeutral, recovered) && !Rules.Available(story, home, recovered), "Q7-10: missing vision misread after " + payPath);
            foreach (var pair in story.SeenCues.Where(p => p.Value.Contains("a473e5412ffd0f54fbf395770a80a008"))) recovered.Flags.Add(pair.Key);
            Rules.Complete(story, recovered);
            check(Rules.Available(story, home, recovered) && !Rules.Available(story, homeNeutral, recovered), "Q7-10: witnessed vision ignored after " + payPath);
        }
        foreach (var variant in new[] { home, homeNeutral })
            check(!Rules.Available(story, variant, World(story, 5, "trickster", "trickster.ever", "kiana.trickster.met", "kiana.trickster.cost.guests_robbed"))
                  && !Rules.Available(story, variant, World(story, 5, "trickster", "trickster.ever", "kiana.trickster.met", "kiana.trickster.guests_ransomed", "seelah.souls_returned")),
                "Q10: Arsinoe reports souls home that never came home, or after Q3.");
        // eng7-l02 end
        // Q10 (CAN): Sunhammer's witnessed death (JewelerFinal Cue_0042/0043) cancels the favour everywhere.
        var promised = S("kiana.ending_promised").Nodes[0];
        var deadEnd = World(story, 6, "trickster", "trickster.ever", "kiana.trickster.met", "kiana.trickster.cost.sunhammer_favour", "kiana.committed", "kiana.sunhammer_dead");
        var deadParas = Rules.VisibleParagraphs(promised, deadEnd);
        check(deadParas.Any(x => SurfaceIds.Has(SurfaceIds.Of(story, x), "[kiana.ending_promised/start/paragraph/5]")) && !deadParas.Any(x => SurfaceIds.Has(SurfaceIds.Of(story, x), "[kiana.ending_promised/start/paragraph/4]")),
            "Q10: a dead jeweller still holds the Commander's favour.");
        var call = S("kiana.lastcall.call");
        var callDead = Program.Walk(call, deadEnd);
        check(callDead.Count > 0 && callDead.All(r => !r.Has("kiana.lastcall.called") && r.Has("kiana.lastcall.resolved")),
            "Q10: a dead Sunhammer is called in at the rift.");
        var callAlive = Program.Walk(call, World(story, 6, "trickster", "trickster.ever", "kiana.trickster.met", "kiana.trickster.cost.sunhammer_favour", "kiana.committed"));
        // eng8-q8g: the living creditor offers an enacted pardon AND a refusal.
        check(callAlive.Any(r => r.Has("kiana.lastcall.called") && r.Has("trickster.lastcall.kiana_pardon"))
            && callAlive.Any(r => !r.Has("kiana.lastcall.called") && r.Has("kiana.lastcall.resolved")),
            "Q10: a living Sunhammer lacks his pardon or refusal road.");
        // Q10 (BEL): the betrothed keepsake is the cancelled licence, not a live hold.
        var licenceParas = Rules.VisibleParagraphs(promised, World(story, 6, "trickster", "trickster.ever", "kiana.trickster.met", "kiana.history_betrothed",
                                                                   "kiana.trickster.cost.betrothed", "kiana.committed"));
        check(licenceParas.Any(x => SurfaceIds.Has(SurfaceIds.Of(story, x), "[kiana.ending_promised/start/paragraph/7]")),
            "Q10: the licence is both held and framed.");
        // Q10 (HOW, R2-6): the late yes reaches her Last Call coda; her "then don't promise it" and a parting keep it off.
        var coda = S("kiana.lastcall.page");
        var loversOnly = World(story, 6, "trickster", "trickster.ever", "lastcall.active", "kiana.trickster.met", "kiana.lovers");
        check(!loversOnly.Has("kiana.trickster.late_committed") && !Rules.Available(story, coda, loversOnly),
            "Q10 (R2-1): lovers alone establish the late commitment.");
        // The question is asked in person on her presence hub in Chapter 5; the letter twin only when her copy was not placed.
        var question = S("kiana.trickster.late_question");
        var questionLetter = S("kiana.trickster.late_question_letter");
        check(question.InteractionHub == "kiana.presence" && question.ContactUnit == Kyana && Rules.IsPresenceHubScene(question)
              && question.Chapters.SequenceEqual(new[] { 5 }) && Rules.IsRemote(questionLetter) && questionLetter.Chapters.SequenceEqual(new[] { 5 }),
            "Q10: the princess's question is not asked in person in Chapter 5.");
        var asked = World(story, 5, "trickster", "trickster.ever", "kiana.trickster.met", "kiana.lovers");
        var answers = Program.Walk(question, asked);
        check(Rules.Available(story, question, asked) && !Rules.Available(story, questionLetter, asked) && answers.Count == 2
              && answers.Count(r => r.Has("kiana.trickster.late_yes")) == 1 && answers.Count(r => r.Has("kiana.trickster.late_no")) == 1,
            "Q10: the late question lacks its yes or its no, or its letter twin plays beside it.");
        var unplacedAsk = Program.Copy(asked); unplacedAsk.AvailableContacts.Remove(Kyana); unplacedAsk.Flags.Add("kiana.presence.failed");
        check(!Rules.Available(story, question, unplacedAsk) && Rules.Available(story, questionLetter, unplacedAsk),
            "Q10: an unplaced copy strands the question.");
        var saidNo = answers.Single(r => r.Has("kiana.trickster.late_no"));
        check(!saidNo.Has("kiana.trickster.late_committed") && !Rules.Available(story, epCommit, saidNo)
              && Rules.Available(story, S("kiana.trickster.epilogue.late_no"), saidNo), "Q10: the late no does not reach its own ending.");
        var saidYes = answers.Single(r => r.Has("kiana.trickster.late_yes"));
        var yesEnd = Later(story, saidYes, 1); yesEnd.Chapter = 6;
        check(yesEnd.Has("kiana.committed") && yesEnd.Has("kiana.trickster.late_committed") && !Rules.Available(story, epCommit, yesEnd)
              && Rules.Available(story, S("kiana.ending_promised"), yesEnd),
            "Q10: the in-person yes does not commit, or the epilogue asks it again.");
        foreach (var answered in new[] { saidYes, saidNo })
            check(!Rules.Available(story, S("kiana.morning"), Later(story, answered, 100)) && !Rules.Available(story, questionLetter, Later(story, answered, 100)),
                "Q10: the question is asked twice.");
        // Acceptance without the question: lovers who never answered reach the page, may only leave the margin empty, and
        // establish no commitment and no Last Call coda.
        // eng8-q8h: use the actual met -> marriage -> answer -> date producers above.
        var neverAsked = Program.Copy(lovers); neverAsked.Chapter = 6;
        neverAsked.Flags.Add("lastcall.active"); Rules.Complete(story, neverAsked);
        var neverPages = Pages(epCommit, neverAsked);
        check(Rules.Available(story, epCommit, neverAsked) && neverPages.Contains("blank") && neverPages.Contains("margin") && neverPages.Contains("stage"),
            "eng8-q8h: unanswered eligible courtship has no affirmative answer.");
        foreach (var node in new[] { "margin", "stage" })
        {
            var answer = epCommit.Nodes[0].Choices.Single(c => c.Next == node && c.Set.Contains("kiana.trickster.late_yes") && Rules.ChoiceAvailable(c, neverAsked));
            check(Rules.ChoiceAvailable(answer, neverAsked), "Affirmative appended answer blocked: " + node);
            var copy = Program.Copy(neverAsked);
            copy.Flags.UnionWith(answer.Set); Rules.Complete(story, copy);
            check(copy.Has("kiana.trickster.late_committed") && !copy.Has("kiana.committed")
                && Rules.Available(story, coda, copy), "Real affirmative consumer invalidates itself: " + node);
        }
        var refusal = Program.Walk(epCommit, neverAsked).Single(r => r.Has("kiana.trickster.late_no"));
        check(!refusal.Has("kiana.trickster.late_committed") && !Rules.Available(story, coda, refusal), "Real refusal grants a late coda");
        var lateYes = Program.Walk(epCommit, neverAsked).First(r => r.Has("kiana.trickster.late_yes"));
        check(lateYes.Has("kiana.trickster.late_committed") && Rules.Available(story, coda, lateYes), "Q10: the late commit loses her Last Call coda.");
        foreach (var off in new[] { "kiana.uncertain", "kiana.parting" })
        {
            var w = Program.Copy(lateYes); w.Flags.Add(off); Rules.Complete(story, w);
            check(!Rules.Available(story, coda, w), "Q10: her Last Call coda plays after " + off);
        }

        // Q10 (CAN): the pivot's account matches what the Commander did: the Bluff, the bolt, the swap.
        var bolted = gemOut.Single(r => r.Has("kiana.trickster.cost.courier_marked"));
        var swappedOut = swapped[0];
        var soldTold = Pages(temple, Later(story, sold, 24));
        var boltTold = Pages(temple, Later(story, bolted, 24));
        var swapTold = Pages(temple, Later(story, swappedOut, 24));
        check(soldTold.Contains("told_robbed") && !soldTold.Contains("told_bolted") && !soldTold.Contains("told_swapped")
              && boltTold.Contains("told_bolted") && !boltTold.Contains("told_robbed")
              && swapTold.Contains("told_swapped") && !swapTold.Contains("told_robbed") && !swapTold.Contains("told_bolted"),
            "Q10: the pivot recalls a rescue the Commander did not make.");
        // Q10 (INT): no Kiana actor, no pivot at the counter; an unplaced copy opens the letter twin, not before.
        var noKiana = Later(story, sold, 24); noKiana.AvailableContacts.Remove(Kyana);
        var twin = S("kiana.trickster.after.letter");
        check(!Rules.Available(story, temple, noKiana) && !Rules.Available(story, twin, noKiana), "Q10: the pivot plays without Kiana.");
        var unplaced = Later(story, sold, 24); unplaced.AvailableContacts.Remove(Kyana); unplaced.AvailableContacts.Remove(Arsinoe);
        unplaced.Flags.Add("kiana.presence.failed");
        check(Rules.IsRemote(twin) && Rules.Available(story, twin, unplaced) && Program.Walk(twin, unplaced).Any(r => r.Has("kiana.trickster.met")),
            "Q10: a failed anchor strands the pivot.");
        check(Program.Walk(temple, Later(story, sold, 24)).All(r => { var after = Program.Copy(r); after.Flags.Add("kiana.presence.failed"); return !Rules.Available(story, twin, Later(story, after, 48)); }), "Q10: the pivot and its letter twin both play.");
        var presenceSpec = story.Presences["kiana.presence"];
        var placedWorld = Later(story, sold, 24);
        check(Rules.PresenceWanted(presenceSpec, placedWorld)
              && Rules.PlanPresence(presenceSpec, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = true }).SequenceEqual(new[] { PresenceStep.Spawn })
              && Rules.PlanPresence(presenceSpec, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = false }).SequenceEqual(new[] { PresenceStep.Blocked }),
            "Q10: Kiana's copy is not spawned beside Arsinoe, or is spawned without her.");
        var rounds = S("kiana.trickster.ward_rounds");
        check(rounds.InteractionHub == "kiana.presence" && rounds.ContactUnit == Kyana && Rules.IsPresenceHubScene(rounds)
              && !Rules.Available(story, rounds, Later(story, sold, 48)) && Rules.Available(story, rounds, Later(story, met, 24)),
            "Q10: her hub has no beat after the pivot.");

        // Q10 (CAN): a dead Sunhammer sends no apprentice; Anevia does not send the Commander after recovered guests.
        foreach (var device in new[] { gem, collar })
        {
            var w = device == gem ? Program.Copy(possessed) : Program.Copy(plainAwake);
            w.Flags.Add("kiana.sunhammer_dead"); Rules.Complete(story, w);
            check(!Rules.Available(story, device, w), "Q10: a dead jeweller's apprentice brings terms: " + device.Id);
        }
        var offerDead = Later(story, Program.Copy(met), 100); offerDead.Flags.Add("kiana.sunhammer_dead");
        check(!Rules.Available(story, S("kiana.trickster.pouch.second_offer"), offerDead), "Q10: a dead jeweller revises his terms.");
        var aneviaAwake = S("kiana.trickster.awake.react_anevia");
        var dogBase = World(story, 5, "trickster", "trickster.ever", "kiana.trickster.returned", "kiana.trickster.dog_saved");
        check(Rules.Available(story, aneviaAwake, dogBase), "Q10: Anevia's dog line is gone.");
        foreach (var recovered in new[] { "kiana.trickster.guests_bought_back", "seelah.souls_returned" })
        {
            var w = Program.Copy(dogBase); w.Flags.Add(recovered); Rules.Complete(story, w);
            check(!Rules.Available(story, aneviaAwake, w), "Q10: Anevia urges a recovery already made: " + recovered);
        }
        // Q10 (VOI): the kiss at rounds needs an affair or a night together; before that, a joke and the ward.
        var roundsEarly = Later(story, met, 24);
        var earlyPages = Pages(rounds, roundsEarly);
        check(earlyPages.Contains("wrist_early") && !earlyPages.Contains("wrist"), "Q10: a married Kiana kisses at rounds.");
        foreach (var earned in new[] { "kiana.lovers", "kiana.affair" })
        {
            var w = Program.Copy(roundsEarly); w.Flags.Add(earned);
            var pages = Pages(rounds, w);
            check(pages.Contains("wrist") && !pages.Contains("wrist_early"), "Q10: the earned kiss at rounds is missing: " + earned);
        }
        // Q10 (BEL): the decree paragraph names only the other two weddings.
        var kingEnd = World(story, 6, "trickster", "trickster.ever", "kiana.trickster.met", "kiana.history_betrothed", "kiana.trickster.cost.betrothed",
                            "kiana.trickster.decree_king", "kiana.committed");


        // Exclusivity: one device per world.
        foreach (var w in new[] { seen, missedWife, possessed, awake, noKing })
            check(devices.Count(d => Rules.Available(story, d, w)) <= 1, "Two Kiana devices open in one world.");
    }
}
