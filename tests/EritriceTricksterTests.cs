using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Eritrice, Trickster (Writer/handoffs/trickster/eritrice.md; F10): "Motion carried".
// One block per spec rules test (Trk_Eritrice_*), the shape of each hook, and the standing debate that makes the motion a
// courtship (eritrice_minutes, eritrice_council): every sitting reachable, the second reading only after the quill, the
// intimate night only after the commit, and her sealed-hall worlds served by letters and the late epilogue page.
internal static class EritriceTricksterTests
{
    private const string List = "d07bffc320b9127459c40869ab3e8ee4";
    private const string Welcome = "2abad22288daf834f950acb6b2b7a812";
    private const string P = "eritrice.trickster.";
    private const string M = "eritrice.minutes.";
    private const string K = "eritrice.council.";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
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
        var motion = S(P + "council.motion");
        var debate = S(P + "council.private_debate");
        var second = S(P + "council.second_reading");
        var third = S(P + "council.third_reading");
        var letter = S(P + "council.minutes_letter");
        var late = S(P + "council.late_motion");
        var tabled = S(P + "fought.tabled");
        var pageCommit = S(P + "epilogue.commit");
        var pageDeclined = S(P + "epilogue.declined");
        var pageMet = S(P + "epilogue.we_did_meet");
        var quill = S(M + "quill");
        var night = S(M + "adjourned");
        var pages = story.Scenes.Where(s => s.Relationship == "eritrice" && s.Owner == "EritriceEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "eritrice" && s.Reaction).ToArray();
        var own = story.Scenes.Where(s => s.Relationship == "eritrice" && !s.Reaction && s.Owner == "Eritrice").ToArray();
        var sittings = own.Where(s => s.Id.StartsWith(M, StringComparison.Ordinal) || s.Id.StartsWith(K, StringComparison.Ordinal)).ToArray();
        List<Snapshot> Play(Scene scene, Snapshot w) => Program.Walk(scene, w).Where(r => r.Has(scene.Id)).ToList();
        Choice Choice(Scene scene, string node, int index) => scene.Nodes.Single(n => n.Id == node).Choices[index];
        // The outcomes of a walk that took the named choice of the named node.
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            var chosen = Choice(scene, node, index);
            var hits = Program.Walk(scene, w).Where(r => chosen.Set.All(r.Has) && (chosen.Set.Length > 0 || r.Has(scene.Id))
                                                          && chosen.Forbids.All(f => !r.Has(f) || chosen.Set.Contains(f))).ToList();
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        Snapshot First(Scene scene, Snapshot w, string node, int index) => After(scene, w, node, index).FirstOrDefault() ?? w;
        // Plays every available Eritrice scene forward and reports whether a flag is ever held.
        bool Reaches(Snapshot start, string flag, int chapter = 5)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 14 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    if (from.Has(flag)) return true;
                    var w = Later(story, from, 100, chapter);
                    foreach (var scene in own.Where(s => Rules.Available(story, s, w)))
                        foreach (var r in Program.Walk(scene, w))
                        {
                            if (r.Has(flag)) return true;
                            if (seen.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                        }
                }
                frontier = next.Take(400).ToList();
            }
            return false;
        }

        // Shape and hooks.
        var rel = story.Relationships["eritrice"];
        check(rel.StartedFlag == "eritrice.started" && rel.ClosedFlag == "eritrice.closed" && rel.CommittedFlag == "eritrice.committed"
              && rel.UnavailableFlags.SequenceEqual(new[] { "eritrice.lost_at_council" })
              && rel.UnavailableOverrides.Single().Key == "eritrice.lost_at_council" && rel.UnavailableOverrides.Single().Value == P + "returned"
              && rel.TricksterAccess.Keys.SequenceEqual(new[] { "eritrice.lost_at_council" }),
            "Eritrice's relationship does not match the spec.");
        foreach (var inline in new[] { motion, debate })
            check(inline.AnswerLists.SequenceEqual(new[] { List }) && inline.NativeReturnCue == Welcome && inline.ContactUnit == null
                  && inline.Areas.Length == 0 && inline.Chapters.SequenceEqual(new[] { 3, 5 }),
                "Not an inline scene on her private list with the clean return cue: " + inline.Id);
        check(Choice(motion, "start", 0).Mythic == "PlayerIsTrickster" && Choice(motion, "start", 0).Alignment?.Direction == "Chaotic"
              && Choice(motion, "start", 0).Alignment!.Value == 1 && Choice(motion, "start", 1).Abort,
            "The motion is not a Trickster answer (Chaotic 1) with a way back.");
        check(motion.Nodes.Single(n => n.Id == "declared").Choices.Count == 2
              && Choice(motion, "declared", 0).Requires.Contains("eritrice.chair_usurped") && Choice(motion, "declared", 1).Forbids.Contains("eritrice.chair_usurped"),
            "The motion does not recognise the usurped chair of Council_3 (Cue_0045).");
        foreach (var hall in own.Where(s => !Rules.IsRemote(s)))
            check(hall.AnswerLists.SequenceEqual(new[] { List }) && hall.ContactUnit == null
                  && hall.Chapters.All(c => c == 3 || c == 5) && hall.Forbids.Contains("eritrice.lost_at_council"),
                "A hall scene is not on her private list in Chapters 3/5 behind the sealed-hall guard: " + hall.Id);
        foreach (var remote in new[] { letter, late, tabled })
            check(Rules.IsRemote(remote) && remote.MinChapter == 5 && remote.MaxChapter == 5, "A sealed-hall letter is not a Chapter 5 letter: " + remote.Id);
        check(tabled.TricksterDevice && tabled.TricksterState == "eritrice.lost_at_council" && tabled.Requires.Contains("trickster")
              && tabled.Requires.Contains("eritrice.lost_at_council.latched"),
            "The tabled grudge is not the ER-2 device of the lost-at-council state.");
        check(second.Requires.Contains("eritrice.started") && second.Requires.Contains(M + "quill") && second.NativeReturnCue == null,
            "The second reading is not a physical entry that waits for the standing debate's quill.");
        check(pages.Length == 3 && pages.All(p => p.MinChapter == 6 && p.EpilogueAfter == null
                                                   && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null && c.Mythic == null))),
            "The epilogue pages are not three effect-free, unanchored Chapter 6 pages (appended in authored order, as Nocticula and Dorgelinda).");
        check(story.Derived[P + "late_committed"].Length == 2, "The late-commit derived key is missing.");
        check(pageCommit.Nodes[0].Choices.Select(c => c.Next).SequenceEqual(new[] { "aye", "nay", "silence" })
              && pageCommit.Nodes.Select(n => n.Id).OrderBy(x => x).SequenceEqual(new[] { "aye", "nay", "page", "silence" }),
            "The late-commit page does not let the Commander answer the forty-first letter (aye, nay or silence).");

        // Trk_Eritrice_Motion.
        var council = World(story, 3, "trickster", "trickster.ever", "council.session_minuted");
        check(Rules.Available(story, motion, council) && !Rules.Available(story, debate, council) && !Rules.Available(story, second, council),
            "Trk_Eritrice_Motion: the motion is not the only door.");
        var primed = First(motion, council, "start", 0);
        check(primed.Has(P + "primed") && primed.Has(P + "cost.censured"), "Trk_Eritrice_Motion: the motion does not prime and censure.");
        check(Rules.Available(story, debate, Later(story, primed, 24)) && !Rules.Available(story, debate, Later(story, primed, 12)),
            "Trk_Eritrice_Motion: the private debate does not open a day later.");
        check(Reaches(primed, "eritrice.committed", 3), "Trk_Eritrice_Motion: no road to the commit.");

        // Trk_Eritrice_Debate.
        var debating = World(story, 3, "trickster.ever", P + "primed", "council.session_minuted");
        var started = First(debate, debating, "honest", 0);
        check(started.Has("eritrice.started") && started.Has(P + "minutes_read") && started.Has(P + "argued_straight"),
            "Trk_Eritrice_Debate: the honest argument does not start the relationship.");
        var cheated = First(debate, debating, "trick", 0);
        check(cheated.Has("eritrice.started") && cheated.Has(P + "cost.caught_lying"), "Trk_Eritrice_Debate: the trick is not minuted.");
        check(!Rules.Available(story, second, Later(story, started, 72)) && Rules.Available(story, S(M + "point_one"), Later(story, started, 24)),
            "Trk_Eritrice_Debate: the second reading opens before the standing debate has begun.");
        check(Reaches(started, M + "quill", 3) && Reaches(started, "eritrice.committed", 3), "Trk_Eritrice_Debate: no road through the quill to the commit.");

        // Trk_Eritrice_Commit.
        var ready = World(story, 5, "trickster.ever", "eritrice.started", M + "quill");
        check(Rules.Available(story, second, ready) && !Rules.Available(story, third, ready), "Trk_Eritrice_Commit: the second reading is not available.");
        check(After(second, ready, "case", 0).All(r => r.Has("eritrice.committed")), "Trk_Eritrice_Commit: calling the question does not commit.");
        check(second.Nodes.Single(n => n.Id == "open").Choices.Count == 2, "The second reading does not open on the lie when there was one.");

        // Trk_Eritrice_Declined.
        var liar = World(story, 5, "trickster.ever", "eritrice.started", M + "quill", P + "cost.caught_lying");
        var declined = First(second, liar, "refused", 0);
        check(declined.Has(P + "declined") && !declined.Has("eritrice.committed"), "Trk_Eritrice_Declined: her refusal is not the soft no.");
        check(Play(second, liar).Any(r => r.Has(P + "declined")) && Program.Walk(second, liar).All(r => !r.Has("eritrice.closed")),
            "Trk_Eritrice_Declined: the second reading closes the relationship.");
        var afterNo = Later(story, declined, 72);
        check(Rules.Available(story, third, afterNo) && !Rules.Available(story, second, afterNo), "Trk_Eritrice_Declined: no third reading after her no.");
        // Polish b6a: the third reading is a debate reversal (the Commander argues the case against), not a crusade fee.
        check(Choice(third, "start", 0).Crusade == null && Choice(third, "start", 0).Set.Contains(P + "cost.on_the_record")
              && Choice(third, "start", 0).Set.Contains("eritrice.committed") && Choice(third, "start", 1).Set.Contains("eritrice.closed"),
            "Trk_Eritrice_Declined: the third reading is not the case-against second ask with a hard no.");
        check(Reaches(declined, "eritrice.committed"), "Trk_Eritrice_Declined: no road to the commit after her no.");

        // Trk_Eritrice_LateMinutes.
        var failed = World(story, 5, "trickster.ever", P + "primed", "trickster.failed");
        check(Rules.Available(story, letter, failed) && !Rules.Available(story, motion, failed), "Trk_Eritrice_LateMinutes: the minutes do not arrive.");
        var lateStart = First(letter, failed, "letter", 0);
        check(lateStart.Has("eritrice.started") && lateStart.Has(P + "cost.late"), "Trk_Eritrice_LateMinutes: countersigning does not start the debate.");

        // Trk_Eritrice_LateMotion.
        var allied = World(story, 5, "trickster", "trickster.ever", "council.debrief_motion");
        check(Rules.Available(story, late, allied) && !Rules.Available(story, letter, allied), "Trk_Eritrice_LateMotion: the circular does not arrive.");
        // Polish b6a: the surety is the mover's own (a sealed truth), not a crusade bond.
        check(Choice(late, "start", 0).Crusade == null && Choice(late, "start", 0).Set.Contains(P + "cost.sealed_truth"),
            "Trk_Eritrice_LateMotion: the sealed truth is not posted as surety.");
        var bonded = First(late, allied, "reply", 0);
        check(bonded.Has(P + "primed") && bonded.Has("eritrice.started") && bonded.Has(P + "cost.late"), "Trk_Eritrice_LateMotion: the reply does not start the debate.");
        check(Rules.Available(story, pageCommit, Later(story, bonded, 100, 6)), "Trk_Eritrice_LateMotion: the late commit page is not reachable.");

        // Trk_Eritrice_Fought.
        var fought = World(story, 5, "trickster", "trickster.ever", "council.fought", "eritrice.lost_at_council.latched");
        check(Rules.Available(story, tabled, fought) && !Rules.Available(story, motion, fought) && !Rules.Available(story, debate, fought)
              && !sittings.Any(s => Rules.Available(story, s, fought)),
            "Trk_Eritrice_Fought: the sealed hall still opens, or the grudge letter does not come.");
        check(Choice(tabled, "stranger", 0).Mythic == "PlayerIsTrickster" && Choice(tabled, "lover", 0).Mythic == "PlayerIsTrickster",
            "Trk_Eritrice_Fought: the point of order is not a Trickster answer.");
        var apology = First(tabled, fought, "ruling", 0);
        check(apology.Has(P + "returned") && apology.Has(P + "cost.grudge") && apology.Has(P + "cost.apologised")
              && Choice(tabled, "ruling", 0).Crusade?.Amount == -200,
            "Trk_Eritrice_Fought: the formal apology is not paid for.");
        check(First(tabled, fought, "ruling", 1).Has(P + "cost.grudge_on_agenda"), "Trk_Eritrice_Fought: the grudge cannot stand on the agenda.");
        var lover = World(story, 5, "trickster", "trickster.ever", "council.fought", "eritrice.lost_at_council.latched", "eritrice.committed");
        check(Program.Walk(tabled, lover).Any(r => r.Has(P + "returned")), "Trk_Eritrice_Fought: a committed Commander cannot table the grudge.");

        // Trk_Eritrice_Fought_Struck.
        var allyFought = World(story, 5, "trickster", "trickster.ever", "council.fought_nocta_allied", "eritrice.lost_at_council.latched");
        var struck = First(tabled, allyFought, "struck", 0);
        check(struck.Has("eritrice.closed") && !struck.Has(P + "returned"), "Trk_Eritrice_Fought_Struck: striking the grudge is not her hard no.");

        // Trk_Eritrice_Fought_Epilogue.
        var ending = World(story, 6, "trickster.ever", "council.fought", P + "returned");
        check(Rules.Available(story, pageCommit, ending) && !Rules.Available(story, pageDeclined, ending),
            "Trk_Eritrice_Fought_Epilogue: the late commit page is not the only page.");
        var committedEnd = World(story, 6, "trickster.ever", "eritrice.committed");
        check(Rules.Available(story, pageMet, committedEnd) && !Rules.Available(story, pageCommit, committedEnd),
            "The committed ending page is not the Council-that-did-meet page.");
        check(Rules.Available(story, pageDeclined, World(story, 6, "trickster.ever", P + "declined"))
              && Rules.Available(story, pageMet, World(story, 6, "trickster.ever", P + "declined", "eritrice.committed")),
            "The refusal page or the declined-then-carried override is wrong.");

        // The standing debate: every sitting reachable, the night only after the commit, and it is the one heated beat.
        var debateStart = World(story, 3, "trickster.ever", "eritrice.started", P + "minutes_read", "council.session_minuted");
        foreach (var sitting in sittings)
            check(sitting.Optional && sitting.Requires.Contains("trickster.ever"), "A sitting is not an optional Trickster-path beat: " + sitting.Id);
        check(sittings.Length >= 30, "The standing debate is missing sittings.");
        check(night.Requires.Contains("eritrice.committed") && !Rules.Available(story, night, Later(story, ready, 24)),
            "The night opens before the commit.");
        check(night.Nodes.Any(n => n.Id == "cut") && night.Nodes.Single(n => n.Id == "look").Choices.Single().Set.Contains(M + "night"),
            "The night does not reach its threshold and cut.");
        check(Reaches(Later(story, ready, 0), M + "adjourned"), "The night is unreachable after the commit.");
        foreach (var id in new[] { M + "point_one", M + "the_convening", M + "a_noble_devil", M + "who_suggested_it", M + "a_narrow_outlook",
                                   K + "celestials_and_beasts", K + "a_sound_proposition", K + "a_proof", K + "luck_is_not_a_position",
                                   K + "the_eldests_version", K + "a_certain_book", K + "the_casualty_lists", K + "the_dagger",
                                   K + "where_the_chair_goes_home", K + "a_motion_to_expel", K + "personal_privilege" })
            check(Reaches(debateStart, id, 3), "Sitting unreachable in Chapter 3: " + id);
        var chapterFive = World(story, 5, "trickster.ever", "eritrice.started", P + "minutes_read", "council.cauldron_given",
            "eritrice.proposed_key", "eritrice.cipher_unread", "eritrice.council_walked_out", "eritrice.nocticula_named", "council.walked_out");
        foreach (var id in new[] { M + "at_worst", M + "the_cipher", M + "stay_in_your_seats", M + "a_serious_matter",
                                   K + "a_lie_for_the_chair", K + "the_lady_in_shadow", K + "so_many_years", K + "just_imagine" })
            check(Reaches(chapterFive, id), "Sitting unreachable in Chapter 5: " + id);
        var committed5 = World(story, 5, "trickster.ever", "eritrice.started", "eritrice.committed", M + "quill", M + "the_convening");
        foreach (var id in new[] { M + "the_record", M + "a_standing_item", K + "his_eyes", K + "accurate_minutes", K + "the_mortal_clock",
                                   K + "twice_nightly", K + "the_fair_copy", K + "rules_of_the_crossroads", K + "the_six_hundred_and_thirteenth" })
            check(Reaches(committed5, id), "Post-commit sitting unreachable: " + id);
        var key = S(M + "at_worst");
        check(Choice(key, "truth", 2).Alignment?.Direction == "Evil" && Choice(key, "truth", 0).Alignment == null,
            "The key's pivotal split has no evil option, or its forgiveness is shifted.");
        check(Reaches(World(story, 5, "trickster.ever", P + "declined"), M + "the_blank_line"), "Her soft no has no sitting of its own.");

        // Reactions: exactly Chadali and Nenio, behind their guards.
        check(reactions.Length == 3 && reactions.All(r => r.Nodes.Count == 1)
              && reactions.Where(r => r.Owner == "Chadali").All(r => r.Forbids.Contains("chadali.lost_at_council"))
              && reactions.Where(r => r.Owner == "Nenio").All(r => r.Forbids.Contains("nenio.dead") && r.Forbids.Contains("nenio.sent_away")),
            "The reactions are not exactly Chadali and Nenio behind their guards.");
        check(letter.Nodes.Any(n => n.Id == "postscript") && late.Nodes.Any(n => n.Id == "postscript"),
            "Chadali's postscript is missing from the letters.");
        Console.WriteLine("PASS: Eritrice Trickster (Trk_Eritrice_*): motion, minutes, second and third readings, the sealed hall's letters, the tabled grudge and the standing debate.");
    }
}
