using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Chadali, Trickster (Writer/handoffs/trickster/chadali.md; F21): "The lucky charm".
// One block per spec rules test (Trk_Chadali_*), the shape of each hook, and the wagers that make the coin a courtship
// (chadali_wagers, chadali_fortunes, chadali_sessions): every sitting reachable, the question only after the real wager,
// the honey night only after the commit, and her sealed-hall worlds served by letters and the late epilogue page.
internal static class ChadaliTricksterTests
{
    private const string List = "e649f211c6b002a49a0c633061877927";
    private const string Cookie = "ed7a31d6f063e0c4aa4ec4e08fab57c0";
    private const string P = "chadali.trickster.";
    private const string W = "chadali.wagers.";
    private const string F = "chadali.fortunes.";
    private const string S = "chadali.sessions.";
    private const string H = "chadali.hours.";

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
        Scene Sc(string id) => story.Scenes.Single(s => s.Id == id);
        var coin = Sc(P + "council.coin");
        var orange = Sc(P + "council.orange");
        var second = Sc(P + "council.second_cookie");
        var tree = Sc(P + "after.orange_tree");
        var letter = Sc(P + "council.orange_letter");
        var lucky = Sc(P + "fought.lucky");
        var pageCommit = Sc(P + "epilogue.commit");
        var pageDeclined = Sc(P + "epilogue.declined");
        var pageNight = Sc(P + "epilogue.lucky_night");
        var wager = Sc(W + "the_real_wager");
        var night = Sc(F + "honey");
        var pages = story.Scenes.Where(s => s.Relationship == "chadali" && s.Owner == "ChadaliEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "chadali" && s.Reaction).ToArray();
        var own = story.Scenes.Where(s => s.Relationship == "chadali" && !s.Reaction && s.Owner == "Chadali").ToArray();
        var sittings = own.Where(s => s.Id.StartsWith(W, StringComparison.Ordinal) || s.Id.StartsWith(F, StringComparison.Ordinal)
                                      || s.Id.StartsWith(S, StringComparison.Ordinal) || s.Id.StartsWith(H, StringComparison.Ordinal)).ToArray();
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
        // Plays every available Chadali scene forward and reports whether a flag is ever held.
        bool Reaches(Snapshot start, string flag, int chapter = 5)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 16 && frontier.Count > 0; depth++)
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
        var rel = story.Relationships["chadali"];
        check(rel.StartedFlag == "chadali.started" && rel.ClosedFlag == "chadali.closed" && rel.CommittedFlag == "chadali.committed"
              && rel.UnavailableFlags.SequenceEqual(new[] { "chadali.lost_at_council" })
              && rel.UnavailableOverrides.Single().Key == "chadali.lost_at_council" && rel.UnavailableOverrides.Single().Value == P + "returned"
              && rel.TricksterAccess.Keys.SequenceEqual(new[] { "chadali.lost_at_council" }),
            "Chadali's relationship does not match the spec.");
        foreach (var inline in new[] { coin, orange })
            check(inline.AnswerLists.SequenceEqual(new[] { List }) && inline.NativeReturnCue == Cookie && inline.ContactUnit == null
                  && inline.Areas.Length == 0 && inline.Chapters.SequenceEqual(new[] { 3, 5 }),
                "Not an inline scene on her private list with the clean return cue: " + inline.Id);
        check(Choice(coin, "start", 0).Mythic == "PlayerIsTrickster" && Choice(coin, "start", 0).Alignment?.Direction == "Chaotic"
              && Choice(coin, "start", 0).Alignment!.Value == 1 && Choice(coin, "start", 1).Abort,
            "The coin is not a Trickster answer (Chaotic 1) with a way back.");
        check(orange.Nodes.Single(n => n.Id == "open").Choices.Count == 2
              && Choice(orange, "open", 0).Requires.Contains("council.orange_called") && Choice(orange, "open", 1).Forbids.Contains("council.orange_called"),
            "The payoff does not branch on the Commander's own orange (Council_5-1/Cue_0020).");
        foreach (var hall in own.Where(s => !Rules.IsRemote(s)))
            check(hall.AnswerLists.SequenceEqual(new[] { List }) && hall.ContactUnit == null
                  && hall.Chapters.All(c => c == 3 || c == 5) && hall.Forbids.Contains("chadali.lost_at_council"),
                "A hall scene is not on her private list in Chapters 3/5 behind the sealed-hall guard: " + hall.Id);
        foreach (var remote in new[] { letter, lucky })
            check(Rules.IsRemote(remote) && remote.MinChapter == 5 && remote.MaxChapter == 5, "A sealed-hall letter is not a Chapter 5 letter: " + remote.Id);
        check(own.Count(Rules.IsRemote) == 2, "Chadali has letters beyond the spec's one-per-branch budget.");
        check(lucky.TricksterDevice && lucky.TricksterState == "chadali.lost_at_council" && lucky.Requires.Contains("trickster")
              && lucky.Requires.Contains("chadali.lost_at_council.latched"),
            "'Lucky you' is not the ER-2 device of the lost-at-council state.");
        check(second.Requires.Contains("chadali.started") && second.Requires.Contains(W + "the_real_wager") && second.NativeReturnCue == null,
            "The second cookie is not a physical entry that waits for the real wager.");
        check(pages.Length == 3 && pages.All(p => p.MinChapter == 6 && p.EpilogueAfter == "b2fd1f720322d6749b921cdd34328c3a"
                                                   && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null && c.Mythic == null))),
            "The epilogue pages are not three effect-free Chapter 6 pages after the Council's page.");
        check(story.Derived[P + "late_committed"].Length == 2, "The late-commit derived key is missing.");
        check(pageCommit.Nodes[0].Choices.Select(c => c.Next).SequenceEqual(new[] { "stay", "half", "coin" }),
            "The late-commit page does not let the Commander answer her (stay, half the orange, or the coin).");

        // Trk_Chadali_Coin.
        var council = World(story, 3, "trickster", "trickster.ever", "chadali.chance_asked");
        check(Rules.Available(story, coin, council) && !Rules.Available(story, orange, council) && !Rules.Available(story, second, council),
            "Trk_Chadali_Coin: the coin is not the only door.");
        var primed = First(coin, council, "start", 0);
        check(primed.Has(P + "primed") && primed.Has(P + "cost.luck_lent"), "Trk_Chadali_Coin: the coin does not prime and lend.");
        check(Rules.Available(story, orange, Later(story, primed, 24)) && !Rules.Available(story, orange, Later(story, primed, 12)),
            "Trk_Chadali_Coin: the orange does not open a day later.");
        check(Reaches(primed, "chadali.committed", 3), "Trk_Chadali_Coin: no road to the commit.");

        // Trk_Chadali_Payoff.
        var paying = World(story, 5, "trickster", "trickster.ever", P + "primed", "council.cauldron_given", "council.orange_called");
        check(Rules.Available(story, orange, paying), "Trk_Chadali_Payoff: the orange is not available.");
        var started = First(orange, paying, "confession", 0);
        check(started.Has("chadali.started") && started.Has(P + "courted"), "Trk_Chadali_Payoff: keeping the luck does not start the relationship.");
        check(First(orange, paying, "confession", 1).Has(P + "cost.luck_owed"), "Trk_Chadali_Payoff: the luck cannot be asked back.");
        check(!Rules.Available(story, second, Later(story, started, 72)) && Rules.Available(story, Sc(W + "the_recipe"), Later(story, started, 24)),
            "Trk_Chadali_Payoff: the question opens before the wagers have begun.");
        check(Reaches(started, W + "the_real_wager") && Reaches(started, "chadali.committed"), "Trk_Chadali_Payoff: no road through the real wager to the commit.");

        // Trk_Chadali_Commit.
        var ready = World(story, 5, "trickster.ever", "chadali.started", W + "the_real_wager");
        check(Rules.Available(story, second, ready) && !Rules.Available(story, tree, ready), "Trk_Chadali_Commit: the second cookie is not available.");
        check(After(second, ready, "her_test", 0).All(r => r.Has("chadali.committed")), "Trk_Chadali_Commit: asking her does not commit.");

        // Trk_Chadali_Declined.
        var declined = First(second, ready, "refused", 0);
        check(declined.Has(P + "declined") && !declined.Has("chadali.committed"), "Trk_Chadali_Declined: her refusal is not the soft no.");
        check(First(second, ready, "luck", 0).Has(P + "declined"), "Trk_Chadali_Declined: flattery does not lead to her no.");
        check(Program.Walk(second, ready).All(r => !r.Has("chadali.closed")), "Trk_Chadali_Declined: the second cookie closes the relationship.");
        var afterNo = Later(story, declined, 72);
        check(Rules.Available(story, tree, afterNo) && !Rules.Available(story, second, afterNo), "Trk_Chadali_Declined: no seed after her no.");
        check(Choice(tree, "start", 0).Crusade?.Resource == "Materials" && Choice(tree, "start", 0).Crusade!.Amount == -100
              && Choice(tree, "start", 0).Set.Contains("chadali.committed") && Choice(tree, "start", 1).Set.Contains("chadali.closed"),
            "Trk_Chadali_Declined: the seed is not the priced second ask with a hard no.");
        check(Reaches(declined, "chadali.committed"), "Trk_Chadali_Declined: no road to the commit after her no.");
        check(Reaches(declined, W + "a_coin_lying_flat"), "Her soft no has no sitting of its own.");

        // Trk_Chadali_LateOrange.
        var sealedHall = World(story, 5, "trickster.ever", P + "primed", "council.debrief_motion");
        check(Rules.Available(story, letter, sealedHall) && !Rules.Available(story, coin, sealedHall), "Trk_Chadali_LateOrange: the orange does not arrive.");
        var lateStart = First(letter, sealedHall, "letter", 0);
        check(lateStart.Has("chadali.started") && lateStart.Has(P + "cost.late"), "Trk_Chadali_LateOrange: eating the orange does not start her.");
        check(Rules.Available(story, pageCommit, Later(story, lateStart, 100, 6)), "Trk_Chadali_LateOrange: the late commit page is not reachable.");

        // Trk_Chadali_Fought.
        var fought = World(story, 5, "trickster", "trickster.ever", "council.fought_nocta_allied", "chadali.lost_at_council.latched");
        check(Rules.Available(story, lucky, fought) && !Rules.Available(story, coin, fought) && !Rules.Available(story, second, fought)
              && !sittings.Any(s => Rules.Available(story, s, fought)),
            "Trk_Chadali_Fought: the sealed hall still opens, or her letter does not come.");
        check(Choice(lucky, "hurt", 0).Mythic == "PlayerIsTrickster" && Choice(lucky, "hurt", 0).Alignment?.Direction == "Chaotic",
            "Trk_Chadali_Fought: the bet on her luck is not a Trickster answer (Chaotic 1).");
        var apology = First(lucky, fought, "refusal", 0);
        check(apology.Has(P + "returned") && apology.Has(P + "cost.grudge") && apology.Has(P + "cost.apologised")
              && Choice(lucky, "refusal", 0).Crusade?.Resource == "Favors" && Choice(lucky, "refusal", 0).Crusade!.Amount == -200,
            "Trk_Chadali_Fought: the public apology is not paid for.");
        check(First(lucky, fought, "refusal", 1).Has(P + "cost.needle_owed"), "Trk_Chadali_Fought: the needle cannot be promised.");

        // Trk_Chadali_Fought_Refused.
        var hostile = World(story, 5, "trickster", "trickster.ever", "council.fought", "chadali.lost_at_council.latched");
        var refused = First(lucky, hostile, "refusal", 2);
        check(refused.Has("chadali.closed") && !refused.Has(P + "returned"), "Trk_Chadali_Fought_Refused: refusing her terms is not her hard no.");

        // Trk_Chadali_Fought_Epilogue.
        var ending = World(story, 6, "trickster.ever", "council.fought", P + "returned");
        check(Rules.Available(story, pageCommit, ending) && !Rules.Available(story, pageDeclined, ending),
            "Trk_Chadali_Fought_Epilogue: the late commit page is not the only page.");
        check(Rules.Available(story, pageNight, World(story, 6, "trickster.ever", "chadali.committed"))
              && !Rules.Available(story, pageCommit, World(story, 6, "trickster.ever", "chadali.committed")),
            "The committed ending page is not the lucky night page.");
        check(Rules.Available(story, pageDeclined, World(story, 6, "trickster.ever", P + "declined"))
              && Rules.Available(story, pageNight, World(story, 6, "trickster.ever", P + "declined", "chadali.committed")),
            "The refusal page or the declined-then-committed override is wrong.");
        check(pageNight.Nodes[0].Paragraphs.Count >= 20, "The committed page is missing the courtship's consequences.");

        // The courtship: every sitting reachable, the question only after the wager, the night only after the commit.
        foreach (var sitting in sittings)
            check(sitting.Optional && sitting.Requires.Contains("trickster.ever"), "A sitting is not an optional Trickster-path beat: " + sitting.Id);
        check(sittings.Length >= 44, "The wagers are missing sittings.");
        check(wager.Requires.Contains(W + "so_gloomy") && wager.Requires.Contains(W + "a_free_space"), "The real wager does not wait for the gloom and the dream.");
        check(night.Requires.Contains("chadali.committed") && !Rules.Available(story, night, Later(story, ready, 24)),
            "The honey night opens before the commit.");
        check(night.Nodes.Any(n => n.Id == "cut") && night.Nodes.Single(n => n.Id == "look").Choices.Single().Set.Contains(F + "night"),
            "The night does not reach its threshold and cut.");
        var courting3 = World(story, 3, "trickster.ever", "chadali.started", "chadali.called_babbling", "chadali.cobblehoof_stopped", "eritrice.proposed_key");
        foreach (var id in new[] { W + "the_recipe", W + "born_lucky", W + "her_worshippers", W + "a_lucky_charm", W + "the_old_fellow",
                                   W + "just_joking", W + "odious_questions", W + "knucklebones", W + "a_free_space", W + "so_gloomy",
                                   W + "the_real_wager", S + "what_you_said", S + "a_dull_future", S + "an_interesting_way",
                                   S + "a_drinking_song", S + "a_parcel_for_the_shrine", S + "two_patrons", H + "make_some_stronger",
                                   H + "an_unlucky_day", H + "our_new_friend", H + "who_brought_you", H + "a_cookie_for_the_enemy",
                                   H + "not_today", H + "a_lucky_number" })
            check(Reaches(courting3, id, 3), "Sitting unreachable in Chapter 3: " + id);
        check(Reaches(courting3, W + "loaded_dice", 3), "The hidden cheat is never caught.");
        var old = Sc(W + "the_old_fellow");
        check(old.Nodes.Single(n => n.Id == "stopped").Choices.Any(c => c.Alignment?.Direction == "Evil")
              && old.Nodes.Single(n => n.Id == "stopped").Choices.Any(c => c.Alignment == null),
            "The old fellow's pivotal split has no evil option, or its mending is shifted.");
        var chapterFive = World(story, 5, "trickster.ever", "chadali.started", "council.cauldron_given", "chadali.fair_proposed",
            "chadali.bows_for_nocticula", "chadali.worthless_essence", "chadali.needle_hurt", "chadali.pressed_on_essence");
        foreach (var id in new[] { F + "will_it_hurt", F + "a_great_big_fair", F + "matching_ribbons", F + "worthless",
                                   F + "sharp_needles", S + "we_are_friends_right", H + "pretend_we_never_met" })
            check(Reaches(chapterFive, id), "Sitting unreachable in Chapter 5: " + id);
        var committed5 = World(story, 5, "trickster.ever", "chadali.started", "chadali.committed", W + "the_real_wager", W + "cobblehoof_left_cursed");
        foreach (var id in new[] { F + "honey", F + "burnt_edges", F + "rigged", F + "the_meadows", F + "a_yellow_ribbon", F + "sharing",
                                   F + "paid_back", S + "what_chance_wishes", S + "you_bet_with_people", S + "the_old_fellow_again",
                                   S + "the_last_evening", H + "for_luck", H + "the_seat_beside_her" })
            check(Reaches(committed5, id), "Post-commit sitting unreachable: " + id);

        // Reactions: exactly Eritrice and Ember, behind their guards; Eritrice's own Chadali reaction honours her return.
        check(reactions.Length == 3 && reactions.All(r => r.Nodes.Count == 1)
              && reactions.Where(r => r.Owner == "Eritrice").All(r => r.Forbids.Contains("eritrice.lost_at_council"))
              && reactions.Where(r => r.Owner == "Ember").All(r => r.Forbids.Contains("ember_dead") && r.Forbids.Contains("ember_gone")),
            "The reactions are not exactly Eritrice and Ember behind their guards.");
        // Eritrice's Chadali reaction is a hall scene: both women's loss keys derive from the same two fight etudes, so it
        // stays behind the sealed-hall guard (a derived key takes no ForbidOverride; the Eritrice backlog item is moot).
        var motion = Sc("eritrice.trickster.react.chadali_motion");
        check(motion.Forbids.Contains("chadali.lost_at_council") && motion.AnswerLists.SequenceEqual(new[] { List }),
            "Eritrice's Chadali reaction is not a hall scene behind Chadali's sealed-hall guard.");
        check(letter.Nodes.Any(n => n.Id == "postscript"), "Eritrice's postscript is missing from the orange letter.");
        Console.WriteLine("PASS: Chadali Trickster (Trk_Chadali_*): coin, orange, second cookie, the seed, the sealed hall's letters, 'Lucky you' and the wagers.");
    }
}
