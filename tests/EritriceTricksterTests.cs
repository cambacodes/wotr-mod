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
        // eng-final E-Q8-10: fund the positive fixture; the walker enforces every debit.
        var state = new Snapshot { Chapter = chapter, Hour = 5000,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        // These positive predicate fixtures represent an already accepted route.
        // Coarse-key negatives are independent in PayoffDepartureRulesTests.
        foreach (var rel in story.Relationships)
            if (flags.Contains(rel.Value.CommittedFlag) && story.Derived.ContainsKey(rel.Key + ".payoff.ordinary"))
                HouseholdTests.Earn(story, state, rel.Key + ".payoff.ordinary");
        foreach (var context in flags.Where(story.Derived.ContainsKey))
            HouseholdTests.Earn(story, state, context);
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
        // Required correspondence notices are not optional Council-hall sittings.
        var sittings = own.Where(s => !Rules.IsRemote(s) && s.Id != K + "chadalis_essence").Where(s => s.Id.StartsWith(M, StringComparison.Ordinal) || s.Id.StartsWith(K, StringComparison.Ordinal)).ToArray();
        List<Snapshot> Play(Scene scene, Snapshot w) => Program.Walk(scene, w).Where(r => r.Has(scene.Id)).ToList();
        Choice Choice(Scene scene, string node, int index) => scene.Nodes.Single(n => n.Id == node).Choices[index];
        // The outcomes of a walk that took the named choice of the named node.
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            var hits = Program.WalkVia(scene, w, node, index);
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        Snapshot First(Scene scene, Snapshot w, string node, int index) => After(scene, w, node, index).FirstOrDefault() ?? w;
        // Plays every available Eritrice scene forward and reports whether a flag is ever held.
        using var reachability = new ReachabilityCache();
        bool Reaches(Snapshot start, string flag, int chapter = 5)
            => reachability.Reaches(start, flag, chapter, () => Explore(Program.Copy(start), chapter));
        IEnumerable<Snapshot> Explore(Snapshot start, int chapter)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 14 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    yield return from;
                    var w = Later(story, from, 100, chapter);
                    foreach (var scene in own.Where(s => Rules.Available(story, s, w)))
                        foreach (var r in Program.Walk(scene, w))
                        {
                            yield return r;
                            if (seen.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                        }
                }
                frontier = next.Take(400).ToList();
            }
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
        foreach (var hall in own.Where(s => !Rules.IsRemote(s) && s.Id != K + "chadalis_essence" && s.ContactUnit == null))
            check(hall.AnswerLists.SequenceEqual(new[] { List }) && hall.ContactUnit == null
                  && hall.Chapters.All(c => c >= 3 && c <= 5) && hall.Forbids.Contains("eritrice.lost_at_council"),
                "A hall scene is not on her private list in Chapters 3-5 behind the sealed-hall guard: " + hall.Id);
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
        // eng7-l13: positive new commitment walks observe current power.
        var debating = World(story, 3, "trickster", "trickster.ever", P + "primed", "council.session_minuted");
        var started = First(debate, debating, "honest", 0);
        check(started.Has("eritrice.started") && started.Has(P + "minutes_read") && started.Has(P + "argued_straight"),
            "Trk_Eritrice_Debate: the honest argument does not start the relationship.");
        var cheated = First(debate, debating, "trick", 0);
        check(cheated.Has("eritrice.started") && cheated.Has(P + "cost.caught_lying"), "Trk_Eritrice_Debate: the trick is not minuted.");
        check(!Rules.Available(story, second, Later(story, started, 72)) && Rules.Available(story, S(M + "point_one"), Later(story, started, 24)),
            "Trk_Eritrice_Debate: the second reading opens before the standing debate has begun.");
        check(Reaches(started, M + "quill", 3) && Reaches(started, "eritrice.committed", 3), "Trk_Eritrice_Debate: no road through the quill to the commit.");

        // Trk_Eritrice_Commit.
        var ready = World(story, 5, "trickster", "trickster.ever", "eritrice.started", M + "quill");
        check(Rules.Available(story, second, ready) && !Rules.Available(story, third, ready), "Trk_Eritrice_Commit: the second reading is not available.");
        check(After(second, ready, "case", 0).All(r => r.Has("eritrice.committed")), "Trk_Eritrice_Commit: calling the question does not commit.");
        // The standing-grudge answer was appended after the original lie/plain answers.
        var opening = second.Nodes.Single(n => n.Id == "open").Choices;
        check(opening.Count == 3 && opening[0].Next == "start_lied"
              && opening[0].Requires.Contains(P + "cost.caught_lying")
              && opening[1].Next == "start" && opening[1].Forbids.Contains(P + "cost.caught_lying")
              && opening[2].Next == "standing_grudge", "The second reading lost its lie/plain or appended grudge opening.");

        // Trk_Eritrice_Declined.
        var liar = World(story, 5, "trickster", "trickster.ever", "eritrice.started", M + "quill", P + "cost.caught_lying");
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
        var fought = World(story, 5, "trickster", "trickster.ever", "council.fought", "eritrice.lost_at_council.latched", "eritrice.threatened_by_force");
        check(Rules.Available(story, tabled, fought) && !Rules.Available(story, motion, fought) && !Rules.Available(story, debate, fought)
              && !sittings.Any(s => Rules.Available(story, s, fought)),
            "Trk_Eritrice_Fought: the sealed hall still opens, or the grudge letter does not come.");
        check(Choice(tabled, "stranger", 0).Mythic == "PlayerIsTrickster" && Choice(tabled, "lover", 0).Mythic == "PlayerIsTrickster",
            "Trk_Eritrice_Fought: the point of order is not a Trickster answer.");
        var apology = First(tabled, fought, "ruling", 0);
        check(!apology.Has(P + "returned") && apology.Has(P + "cost.grudge") && !apology.Has(P + "cost.apologised")
              && apology.Has(P + "apology_arranged")
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
        var ending = World(story, 6, "trickster", "trickster.ever", "council.fought", P + "returned", P + "minutes_read");
        check(Rules.Available(story, pageCommit, ending) && !Rules.Available(story, pageDeclined, ending),
            "Trk_Eritrice_Fought_Epilogue: the late commit page is not the only page.");
        var committedEnd = World(story, 6, "trickster.ever", "eritrice.committed", P + "council.second_reading");
        check(Rules.Available(story, pageMet, committedEnd) && !Rules.Available(story, pageCommit, committedEnd),
            "The committed ending page is not the Council-that-did-meet page.");
        check(Rules.Available(story, pageDeclined, World(story, 6, "trickster.ever", P + "declined"))
              && Rules.Available(story, pageMet, World(story, 6, "trickster.ever", P + "declined", "eritrice.committed", P + "cost.on_the_record")),
            "The refusal page or the declined-then-carried override is wrong.");

        // The standing debate: every sitting reachable, the night only after the commit, and it is the one heated beat.
        var debateStart = World(story, 3, "trickster", "trickster.ever", "eritrice.started", P + "minutes_read", "council.session_minuted", "eritrice.certain_book_said");
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
        // Sol r2 INT: the essence and eve sittings close once the Council has walked out; the walk-out has its own sitting.
        var chapterFive = World(story, 5, "trickster", "trickster.ever", "eritrice.started", P + "minutes_read", "council.cauldron_given",
            "eritrice.proposed_key", "eritrice.cipher_unread", "eritrice.council_walked_out", "eritrice.nocticula_named");
        foreach (var id in new[] { M + "at_worst", M + "the_cipher", M + "stay_in_your_seats", M + "a_serious_matter",
                                   K + "a_lie_for_the_chair", K + "the_lady_in_shadow", K + "just_imagine" })
            check(Reaches(chapterFive, id), "Sitting unreachable in Chapter 5: " + id);
        var walkedOut = World(story, 5, "trickster", "trickster.ever", "eritrice.started", P + "minutes_read", "council.cauldron_given",
            "eritrice.proposed_key", "eritrice.council_walked_out", "council.walked_out");
        check(Reaches(walkedOut, K + "so_many_years") && !Reaches(walkedOut, M + "a_serious_matter") && !Reaches(walkedOut, K + "just_imagine")
              && S(M + "a_serious_matter").Forbids.Contains("eritrice.essence_given"),
            "A preparatory sitting outlives the walk-out or her given essence.");
        var committed5 = World(story, 5, "trickster.ever", "eritrice.started", "eritrice.committed", M + "quill", M + "the_convening");
        foreach (var id in new[] { M + "the_record", M + "a_standing_item", K + "his_eyes", K + "accurate_minutes", K + "the_mortal_clock",
                                   K + "twice_nightly", K + "the_fair_copy", K + "rules_of_the_crossroads", K + "the_six_hundred_and_thirteenth" })
            check(Reaches(committed5, id), "Post-commit sitting unreachable: " + id);
        var key = S(M + "at_worst");
        check(Choice(key, "truth", 2).Alignment?.Direction == "Evil" && Choice(key, "truth", 0).Alignment == null,
            "The key's pivotal split has no evil option, or its forgiveness is shifted.");
        check(Reaches(World(story, 5, "trickster.ever", P + "declined"), M + "the_blank_line"), "Her soft no has no sitting of its own.");

        // Reactions: exactly Chadali and Nenio, behind their guards.
        check(reactions.Length == 5 && reactions.All(r => r.Nodes.Count == 1)
              && reactions.Where(r => r.Owner == "Chadali").All(r => r.Forbids.Contains("chadali.lost_at_council"))
              && reactions.Where(r => r.Owner == "Nenio").All(r => r.Forbids.Contains("nenio.dead") && r.Forbids.Contains("nenio.sent_away")),
            "The reactions are not exactly Chadali and Nenio behind their guards.");
        check(letter.Nodes.Any(n => n.Id == "postscript") && late.Nodes.Any(n => n.Id == "postscript"),
            "Chadali's postscript is missing from the letters.");

        // Sol r1 (2026-09-30). CAN: the Lexicon recollection waits for the native Cue_0054, the cipher callback for her lesson;
        // a Chapter 3 world gets the early variants.
        var eldest = S(K + "the_eldests_version");
        check(story.SeenCues["eritrice.shyka_dull_future"].SequenceEqual(new[] { "1d1c4855bacf5a94fb1e84b7ae8424a3" })
              && Choice(eldest, "start", 1).Requires.Contains("eritrice.shyka_dull_future") && Choice(eldest, "start", 1).Next == "like"
              && Choice(eldest, "start", 3).Forbids.Contains("eritrice.shyka_dull_future") && Choice(eldest, "start", 3).Next == "like_early"
              && Choice(eldest, "start", 0).Requires.Contains(M + "exercise_promised") && Choice(eldest, "start", 2).Forbids.Contains(M + "exercise_promised"),
            "The Eldest's version recalls the second Lexicon or the cipher before they happen.");
        // CAN: the committed page opens outcome-neutral; the denial of acquaintance is only the ceased ending's.
        check(pageMet.Nodes[0].Paragraphs.Where(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[eritrice.trickster.epilogue.we_did_meet/page/paragraph/0]")).All(p => p.Requires.Contains("council.epilogue_ceased")),
            "The committed page imports the ceased-Council ending into every outcome.");
        // INT: the promised lie is not reported as a rescue no scene performs.

        // INT (ledger row 16): the Last Call bottle survival keeps both romance pages; a Commander who stayed dead does not.
        var bottle = new[] { "sacrifice", "ending.wound_closed", "trickster.lastcall.taken", "trickster.lastcall.pillar.bottle" };
        check(Rules.Available(story, pageMet, World(story, 6, new[] { "trickster.ever", "eritrice.committed" }.Concat(bottle).ToArray()))
              && Rules.Available(story, pageCommit, World(story, 6, new[] { "trickster", "trickster.ever", "eritrice.started", P + "minutes_read" }.Concat(bottle).ToArray()))
              && !Rules.Available(story, pageMet, World(story, 6, "trickster.ever", "eritrice.committed", "sacrifice", "ending.wound_closed")),
            "The romance pages do not follow trickster.commander_back.");
        // INT: a returned Nenio reacts; a dissolved one never does.
        foreach (var r in reactions.Where(r => r.Owner == "Nenio"))
            check(r.ForbidOverrides.TryGetValue("nenio.dead", out var o1) && o1 == "nenio.life.recreated" /* eng8-q8a */
                  && r.ForbidOverrides.TryGetValue("nenio.sent_away", out var o2) && o2 == "nenio.life.probation" /* eng8-q8a */
                  && !r.ForbidOverrides.ContainsKey("nenio.dissolved"),
                "A Nenio reaction ignores her return: " + r.Id);
        var nenioMotion = S(P + "react.nenio_motion");
        var nenioBack = World(story, 3, "trickster.ever", "eritrice.started", "nenio.dead", "nenio.trickster.returned", "nenio.trickster.cost.recreated"); // eng8-q8a: paid vessel, not later-dead retained body
        check(Rules.Available(story, nenioMotion, nenioBack)
              && !Rules.Available(story, nenioMotion, World(story, 3, "trickster.ever", "eritrice.started", "nenio.dead")),
            "A returned Nenio is still barred from reacting.");
        // BEL: the cuts land at the initiating motion, and the late aye has its own threshold and aftermath.
        // Sol r2. CAN: the sacrifice recollection waits for the native key proposal; a living visit to Nirvana is possible.
        var standing = S(M + "a_standing_item");
        check(Choice(standing, "start", 0).Requires.Contains("eritrice.proposed_key") && Choice(standing, "start", 3).Forbids.Contains("eritrice.proposed_key")
              && Choice(standing, "start", 3).Next == "honest_early",
            "A standing item recalls the key proposal before it happened, or Nirvana is closed to the living.");
        // INT: only a Commander caught lying is accused of the six voices; the owed vote is cast on the page.
        check(Choice(quill, "held", 0).Requires.Contains(P + "cost.caught_lying") && Choice(quill, "held", 2).Forbids.Contains(P + "cost.caught_lying"),
            "The quill accuses an honest Commander, or the owed vote is never cast.");
        // BEL: the late surety is the sealed truth, and the late aye has its morning.
        // Sol r2. CAN: the Council's age is a century; TRK: the point of order only for a Commander who heard her threat.
        check(story.SeenCues["eritrice.threatened_by_force"].SequenceEqual(new[] { "b138a1a41f4128e43822bb8f3bdc1b4c" })
              && Choice(tabled, "stranger", 0).Requires.Contains("eritrice.threatened_by_force")
              && Choice(tabled, "stranger", 1).Forbids.Contains("eritrice.threatened_by_force") && Choice(tabled, "lover", 1).Next == "ruling_betrayal",
            "The point of order cites a threat the Commander never heard.");
        var alliedNoThreat = World(story, 5, "trickster", "trickster.ever", "council.fought_nocta_allied", "eritrice.lost_at_council.latched");
        check(Program.WalkVia(tabled, alliedNoThreat, "ruling_betrayal", 0).Any(r => r.Has(P + "apology_arranged") && !r.Has(P + "cost.apologised")),
            "The allied betrayal has no priced reconciliation.");
        // Sol r3. CAN: the late surety is her condition for this petition, not Council law; the Lexicon's wound waits for the key
        // proposal; Socothbenoth flirts only while he attends. BEL/COX: no lovers asserted as fact; a sole partner is believed.
        var clock = S(K + "the_mortal_clock");
        check(Choice(clock, "start", 0).Requires.Contains("eritrice.proposed_key") && Choice(clock, "start", 3).Next == "smaller_early", "The mortal clock recalls the key before it is proposed.");
        var eyes = S(K + "his_eyes");
        check(eyes.Forbids.Contains("socot.gone") && eyes.Forbids.Contains("council.walked_out"), "A departed Socothbenoth still flirts at the session.");
        var accurate = S(K + "accurate_minutes");
        check(accurate.Nodes.Single(n => n.Id == "lie").Choices.Any(c => c.Next == "only"), "Other lovers are asserted as fact, or a sole partner cannot say so.");
        // BEL: the motion to expel is resolved for each approach.
        // Sol r4 INT: the session that unlocks the private debate is any of the three minuted sessions (spec binding).
        check(story.SeenCues["council.session_minuted"].Length == 3 && story.SeenCues["council.session_minuted"].Contains("fd991da9cb8bb4a4f9576adbf51de6fd"),
            "The private debate waits on one optional cue.");

        var voted = S(K + "the_motion_to_expel_voted");
        foreach (var flag in new[] { K + "alichino_handled", K + "argued_own_case", K + "chair_recused" })
            check(Rules.Available(story, voted, World(story, 3, "trickster.ever", "eritrice.started", P + "minutes_read", M + "point_one", K + "a_motion_to_expel", K + "expulsion_hearing", flag)),
                "The performed expulsion hearing has no report: " + flag);
        // Sol verify sweep (r5): the book line only if she said it; the Crossroads paragraphs only where the Crossroads was made;
        // the grudge and Alichino's absence at sessions only while the Council convenes.
        check(S(K + "a_certain_book").Requires.Contains("eritrice.certain_book_said")
              && story.SeenCues["eritrice.certain_book_said"].Contains("07c13d2efd8a90b45824a79873b62108"), "The certain book is recalled unheard.");
        var metParas = pageMet.Nodes[0].Paragraphs;
        check(metParas.Where(p => p.Requires.Contains(K + "crossroads_drafted") && SurfaceIds.Has(SurfaceIds.Of(story, p), "[eritrice.trickster.epilogue.we_did_meet/page/paragraph/22]")).All(p => p.AnyGroups.Any(g => g.Contains("ending.trickster_full")))
              && metParas.Where(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[eritrice.trickster.epilogue.we_did_meet/page/paragraph/3]")).All(p => p.Requires.Contains("council.epilogue_convened"))
              && metParas.Where(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[eritrice.trickster.epilogue.we_did_meet/page/paragraph/9]")).All(p => p.Requires.Contains("council.epilogue_convened")),
            "An epilogue paragraph assumes a Crossroads or a convening Council that the ending did not produce.");
        // PP6 (pacing): the two sittings born of the Chapter 4 session open that night in the hall (window [5] -> [4, 5]); every
        // other hall scene keeps its Chapters 3/5 window, and the cipher (looked at "for days") stays in Chapter 5.
        var chapterFour = World(story, 4, "trickster.ever", "eritrice.started", P + "minutes_read", M + "point_one",
            "eritrice.proposed_key", "eritrice.council_walked_out", "eritrice.cipher_unread");
        foreach (var id in new[] { M + "at_worst", M + "stay_in_your_seats" })
        {
            var sitting = S(id);
            check(sitting.Chapters.SequenceEqual(new[] { 4, 5 }) && sitting.MinChapter == 4 && sitting.MaxChapter == 5 && !Rules.IsRemote(sitting)
                  && sitting.AnswerLists.SequenceEqual(new[] { List }) && sitting.Forbids.Contains("eritrice.lost_at_council"),
                "A Chapter 4 sitting lost its hall shape: " + id);
            check(Rules.Available(story, sitting, chapterFour), "A Chapter 4 sitting does not open after the session: " + id);
            check(!Rules.Available(story, sitting, World(story, 3, "trickster.ever", "eritrice.started", P + "minutes_read", M + "point_one")),
                "A Chapter 4 sitting opens before the session: " + id);
            check(!Rules.Available(story, sitting, World(story, 4, "trickster.ever", "eritrice.started", P + "minutes_read", M + "point_one",
                    "eritrice.proposed_key", "eritrice.council_walked_out", "eritrice.lost_at_council")), "A Chapter 4 sitting ignores the sealed hall: " + id);
        }
        check(own.Where(s => !Rules.IsRemote(s) && s.Chapters.Contains(4)).Select(s => s.Id).OrderBy(x => x)
                  .SequenceEqual(new[] { M + "at_worst", M + "stay_in_your_seats" }.OrderBy(x => x))
              && S(M + "the_cipher").Chapters.SequenceEqual(new[] { 5 }), "Chapter 4 holds more of the hall than the session's own night.");
        var keyWays = After(S(M + "at_worst"), chapterFour, "truth", 0).Concat(After(S(M + "at_worst"), chapterFour, "truth", 2)).ToList();
        check(keyWays.Any(r => r.Has(M + "key_forgiven")) && keyWays.Any(r => r.Has(M + "key_used")), "The key's pivotal split does not play in Chapter 4.");
        check(Program.Walk(S(M + "stay_in_your_seats"), chapterFour).Any(r => r.Has(M + "temper_warned"))
              && Program.Walk(S(M + "stay_in_your_seats"), chapterFour).Any(r => r.Has(M + "temper_fed")), "The walk-out's outcomes do not play in Chapter 4.");
        // Reviewed polish: the record names the reading that actually carried.
        var record = S(M + "the_record");
        foreach (var completion in new[] { P + "council.second_reading", P + "council.third_reading" })
        {
            var w = World(story, 5, "trickster", "trickster.ever", "eritrice.committed", M + "adjourned", completion);
            var reads = record.Nodes.Single(n => n.Id == "start").Choices.Where(c => (c.Next == "read" || c.Next == "read_third") && Rules.ChoiceAvailable(c, w)).ToArray();
            check(reads.Length == 1, "The morning has two readings, or none: " + completion);
            var target = completion.EndsWith("third_reading", StringComparison.Ordinal) ? "read_third" : "read";
            check(reads.Single().Next == target,
                "The record names an unplayed reading: " + completion);
            check(Play(record, w).Any(r => r.Has(M + "night_minuted")) && Play(record, w).Any(r => r.Has(M + "night_left_blank")), "A reading variant loses a record outcome.");
        }
        var mixedReadings = World(story, 5, "trickster.ever", P + "council.second_reading", P + "council.third_reading");
        check(!Rules.ChoiceAvailable(Choice(record, "start", 2), mixedReadings) && Rules.ChoiceAvailable(Choice(record, "start", 3), mixedReadings), "Third reading does not take precedence.");
        var request = S(K + "a_lie_for_the_chair");
        check(Choice(request, "want", 0).Set.SequenceEqual(new[] { K + "lied_for_her" })
              && Choice(request, "want", 1).Set.SequenceEqual(new[] { K + "refused_to_lie_for_her" })
              && Choice(request, "want", 2).Set.SequenceEqual(new[] { K + "truth_for_chadali" }), "Private approaches changed order or masquerade as public actions.");
        foreach (var blocker in new[] { "eritrice.closed", "council.fought", "council.walked_out", "council.debrief_motion", M + "extracted" })
            check(!Rules.Available(story, request, World(story, 5, "trickster", "trickster.ever", "eritrice.started", M + "point_one", "council.cauldron_given", blocker)), "A request outlives its opportunity: " + blocker);
        foreach (var aidMoved in new[] { false, true })
        {
            var flags = new List<string> { "trickster.ever", "eritrice.started", M + "point_one" };
            if (aidMoved) flags.Add("eritrice.aid_moved");
            var w = World(story, 5, flags.ToArray());
            var aid = S(K + "a_sound_proposition");
            check(Choice(aid, "forget", 0).Set.Length == 0
                  && Play(aid, w).Any(r => !r.Has(K + "aid_first")), "Withdrawing aid fabricates a later obligation or payment.");
        }
        var pendingTruth = Rules.VisibleParagraphs(pageMet.Nodes[0], World(story, 6, "trickster.ever", "eritrice.committed", K + "truth_for_chadali"));
        check(pendingTruth.Any(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[eritrice.trickster.epilogue.we_did_meet/page/paragraph/28]")) && !pendingTruth.Any(p => p.Requires.Contains(K + "truth_for_chadali_spoken")), "A truth draft becomes a public declaration.");
        var pendingLie = Rules.VisibleParagraphs(pageMet.Nodes[0], World(story, 6, "trickster.ever", "eritrice.committed", K + "lied_for_her"));
        check(pendingLie.Any(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[eritrice.trickster.epilogue.we_did_meet/page/paragraph/25]")), "A promise is reported as a delivered lie.");
        check(pageCommit.Nodes.Single(n => n.Id == "page").Choices.Single(c => c.Next == "silence").Set.Length == 0,
            "Silence invents an affirmative answer.");

        // This scene remains staged until the coordinator supplies E14b append placement.
        // The same rules acceptance runs when that reviewed hook is enabled.
        var publicScene = story.Scenes.FirstOrDefault(s => s.Id == K + "chadalis_essence");
        if (publicScene != null)
        {
            check(publicScene.ReturnToList && publicScene.NativeReturnCue == null && publicScene.AnswerLists.SequenceEqual(new[] { "2e2e6dd9c2bf7d748972de8d5a65b8ad" })
                  && publicScene.DelayHours == 0 && publicScene.Requires.Contains("trickster"), "The intervention changes its native host, replay behavior or path.");
            foreach (var approach in new[] { "lied_for_her", "refused_to_lie_for_her", "truth_for_chadali" })
            {
                var w = World(story, 5, "trickster", "trickster.ever", K + "a_lie_for_the_chair", K + approach);
                check(Rules.Available(story, publicScene, w), "A selected public approach is unavailable: " + approach);
                check(publicScene.Nodes[0].Choices.Count(c => Rules.ChoiceAvailable(c, w)) == 1, "A public approach has competing branches: " + approach);
                var results = Play(publicScene, w);
                check(results.Count > 0, "A public branch cannot complete: " + approach);
                var expected = approach == "lied_for_her" ? new[] { "lie_for_chadali_spoken", "lie_for_chadali_withdrawn" }
                    : approach == "refused_to_lie_for_her" ? new[] { "protection_for_chadali_spoken" } : new[] { "truth_for_chadali_spoken" };
                foreach (var receipt in expected)
                    check(results.Any(r => r.Has(K + receipt)), "The public action has no performed receipt: " + receipt);
                foreach (var result in results)
                {
                    check(expected.Count(f => result.Has(K + f)) == 1 && !result.Has("chadali.essence_given") && !result.Has("eritrice.essence_given") && !result.Has("eritrice.committed"), "A public action grants extraction, commitment or competing receipts.");
                    check(!Rules.Available(story, publicScene, Later(story, result, 0)), "A public intervention can be performed twice.");
                }
                foreach (var blocker in new[] { "council.walked_out", "eritrice.essence_given", "eritrice.closed", "council.fought", "trickster.failed", "crossroute.chadali.unavailable" })
                    check(!Rules.Available(story, publicScene, World(story, 5, "trickster", "trickster.ever", K + "a_lie_for_the_chair", K + approach, blocker)), "An intervention outlives the Council or path: " + blocker);
            }
            foreach (var chapter in new[] { 3, 4, 6 })
                check(!Rules.Available(story, publicScene, World(story, chapter, "trickster", "trickster.ever", K + "a_lie_for_the_chair", K + "lied_for_her")), "The intervention occurs outside the final sitting.");
            check(!Rules.Available(story, publicScene, World(story, 5, "trickster.ever", K + "a_lie_for_the_chair", K + "lied_for_her"))
                  && !Rules.Available(story, publicScene, World(story, 5, "trickster", "trickster.ever", K + "a_lie_for_the_chair")), "A public approach is invented for a former Trickster or a skipped request.");
        }

        Console.WriteLine("PASS: Eritrice Trickster (Trk_Eritrice_*): motion, minutes, second and third readings, the sealed hall's letters, the tabled grudge and the standing debate.");
    }
}
