using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Pacing pass PP1 (Writer/handoffs/13-PACING-PASS.md sections 2a, 4 and 7; storylines/pacing_pp1.py): Anevia's, Irabeth's
// and Seelah's early beats and Seelah's Chapter 4 night. Per beat: the host and its return, the gate at the right moment and
// its absence at a wrong one on the same list, chapter 0, once-only (abort included), one outcome per terminal path, the
// consequence reader, no native key set, inert readers, no Chapter 3 native-romance key delayed, and the shared Anevia list.
internal static class PacingPP1Tests
{
    private const string AneviaList = "33960c7f7af40cd43b7f801a76c87a0b";
    private const string Neathholm = "61fcf2a352daa394ebae399b1348ba62";

    // Every scene that entered Anevia's hub (NPC_Common/Anevia/AnswersList_0003) before PP1, in authored order (13 section 7 (a)).
    private static readonly string[] AneviaListBaseline = {
        "a_cup", "a_errand", "a_roof", "a_crossing", "a_morning", "reckoning", "a_truth", "table", "ordinary", "a_self", "power",
        "future", "shared_night", "last_watch", "departure", "a_waiting", "return", "parting", "three_locks", "three_outing",
        "three_yard", "three_match", "three_anevia_flour", "three_return_game", "three_small_journeys", "three_stolen_roads",
        "three_lantern_debt", "three_ista_departure", "three_lantern_turn", "three_open_road", "three_borrowed_names",
        "three_back_of_seal", "three_counterclaim", "three_unposted_notice", "three_rooms_unlocked", "three_choose_days",
        "three_more_days", "three_kept_days", "anevia.unborrowed_hour", "anevia.a_question_at_home", "anevia.one_truth",
        "anevia.her_own_answer", "anevia.a_place_of_our_own", "anevia.an_invitation_afterward", "anevia.borrowed_signature",
        "anevia.the_paper_seller", "anevia.the_woman_with_the_basket", "anevia.the_counting_room",
        "anevia.what_the_warning_cost", "anevia.the_evening_without_a_case", "anevia.departure_note",
        "anevia.the_life_she_lived", "anevia.a_key_that_is_hers", "anevia.the_last_ordinary_thing", "anevia.a_grief_with_a_name",
        "irabeth.anevias_answer", "tirabade.negotiated_table", "tirabade.after_local_parting", "anevia.trickster.gone.gate",
        "anevia.trickster.gone.commit", "anevia.trickster.gone.second_ask", "anevia.trickster.gone.muster",
        "kiana.trickster.aftermath_missed.react_anevia", "kiana.trickster.possessed.react_anevia",
        "kiana.trickster.awake.react_anevia", "kiana.trickster.no_wedding.react_anevia", "aranka.trickster.react.anevia_verse",
        "aranka.trickster.react.anevia_verse_alone", "gesmerha.trickster.react.anevia_yard_night",
        "gesmerha.trickster.react.anevia_return", "gesmerha.trickster.react.anevia_footsteps",
        "gesmerha.trickster.react.anevia_confessed", "camellia.trickster.react.anevia_body",
        "kaylessa.trickster.react.anevia_amulet", "kaylessa.trickster.react.anevia_awning",
        "kaylessa.trickster.react.anevia_ravine", "nenio.trickster.react.anevia_gate",
        "terendelev.trickster.react.anevia.kenabres",
    };

    private sealed record Beat(string Id, string Relationship, int Chapter, string List, string? Return, string[] Outcomes, string? Gate);

    private static readonly Beat[] Beats = {
        new("anevia.early.watch", "anevia", 0, "65395d8277d3b9b4f82f068616de8a56", "3103585f1550def4c98fbc731ccb3ebc",
            new[] { "anevia.early.watch.splinted", "anevia.early.watch.fumbled", "anevia.early.watch.covered", "anevia.early.watch.horgus", "anevia.early.watch.waved" },
            "neathholm.evening"),
        new("seelah.early.pack", "seelah", 0, "da6ca50574b6c714f9166f37b64b7b59", "843c7cf25f27714439e8dbb6cab06074",
            new[] { "seelah.early.pack.tipped", "seelah.early.pack.lifted", "seelah.early.pack.kept", "seelah.early.pack.returned" }, "prologue.seelah_finished_lift"),
        new("irabeth.early.hands", "irabeth", 1, "4c756b62bc1fcda42b8122f215a9ddd4", null,
            new[] { "irabeth.early.steadied", "irabeth.early.dismissed_help" }, null),
        new("irabeth.early.hook", "irabeth", 2, "b6f914354ceddbf4db19747f12ea4f0d", null,
            new[] { "irabeth.early.hook.shouldered", "irabeth.early.hook.thanked_regill" }, null),
        new("seelah.early.drill", "seelah", 1, "f1e7b7a6740caaa44a3762033c5f0a5a", null,
            new[] { "seelah.early.drill.floored", "seelah.early.drill.landed", "seelah.early.drill.deferred" }, null),
        new("seelah.abyss.night", "seelah", 4, "73260c45aa315c0419fc625f6fcb957d", null,
            new[] { "seelah.abyss.night.listened", "seelah.abyss.night.drilled", "seelah.abyss.night.halved" }, "seelah.abyss_holding_up"),
    };

    // The scenes allowed to read a PP1 flag: the beats themselves and the named consequence readers (13 section 2a item 5).
    private static readonly Dictionary<string, string[]> Readers = new()
    {
        ["anevia.early.watch"] = new[] { "a_cup" },
        ["seelah.early.pack"] = new[] { "seelah.wager" },
        ["irabeth.early.hands"] = new[] { "i_hands" },
        ["irabeth.early.hook"] = new[] { "i_respite" },
        ["seelah.early.drill"] = new[] { "seelah.abyss.night" },
        ["seelah.abyss.night"] = new[] { "seelah.souls" },
    };

    private static Snapshot At(Story story, int chapter, string area, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 500, Area = area };
        state.Flags.UnionWith(flags);
        if (Rules.ChapterFlag(chapter) is string chapterFlag) state.Flags.Add(chapterFlag);
        Rules.Complete(story, state);
        return state;
    }

    private static IEnumerable<string> Reads(Scene s) => s.Requires.Concat(s.Forbids).Concat(s.RequiresAny)
        .Concat(s.RequiresAnyGroups.SelectMany(g => g))
        .Concat(s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids)))
        .Concat(s.Nodes.SelectMany(n => n.Paragraphs).SelectMany(p => p.Requires.Concat(p.Forbids).Concat(p.AnyGroups.SelectMany(g => g))));

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        IEnumerable<Choice> Choices(Scene s) => s.Nodes.SelectMany(n => n.Choices);
        var native = new HashSet<string>(story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys)
            .Concat(story.UnlockableFlags.Keys).Concat(story.QuestObjectives.Keys).Concat(story.InventoryItems.Keys)
            .Concat(story.StartedQuests.Keys).Concat(story.MainCharacterFacts.Keys));

        // Bindings: the three native keys that pin a moment on a list reached more than once.
        check(story.Etudes.TryGetValue("neathholm.evening", out var evening) && evening == "ec82016fa7508e94aae33cd8be84c8b2",
            "PP1: neathholm.evening is not FreeTime.");
        check(story.SeenCues.TryGetValue("prologue.seelah_finished_lift", out var lifted)
              && lifted.OrderBy(x => x).SequenceEqual(new[] { "d94978ee21c6af642ad95578c3e2f8ea", "deb9827da749a5246b0263578bd68560" }),
            "PP1: the finished-lift key is not MeetSeelahAnevia Cue_0013 / Cue_0054.");
        check(story.SelectedAnswers.TryGetValue("seelah.abyss_holding_up", out var holding) && holding == "829801b14a4b2b344a60ba43cb60821a",
            "PP1: the Abyss key is not Seelah's Answer_0119.");

        var allOutcomes = new HashSet<string>(Beats.SelectMany(b => b.Outcomes.Append(b.Id + ".seen")));
        foreach (var b in Beats)
        {
            var scene = S(b.Id);
            string area = b.Id == "anevia.early.watch" ? Neathholm : "";
            // Hook data: explicit relationship, one host list, the chosen return (retcheck OK) or the list itself.
            check(scene.Relationship == b.Relationship && scene.AnswerLists.SequenceEqual(new[] { b.List })
                  && Rules.EntryTargets(scene).SequenceEqual(new[] { b.List }), b.Id + ": wrong relationship or host list.");
            check(b.Return == null ? scene.ReturnToList && scene.NativeReturnCue == null : scene.NativeReturnCue == b.Return && !scene.ReturnToList,
                b.Id + ": wrong return (a retcheck-failed or replaying cue).");
            check(scene.Chapters.SequenceEqual(new[] { b.Chapter }) && scene.MinChapter == b.Chapter && scene.MaxChapter == b.Chapter && scene.Optional,
                b.Id + ": the window is not its host's chapter.");
            check(!string.IsNullOrWhiteSpace(scene.Entry), b.Id + ": empty inline entry.");

            // Entry: open at its moment; shut a chapter either side; shut on the same list at a wrong moment (gate missing).
            var gate = b.Gate == null ? Array.Empty<string>() : new[] { b.Gate };
            var open = At(story, b.Chapter, area, gate);
            check(Rules.Available(story, scene, open), b.Id + ": closed at its own moment.");
            if (b.Chapter == 0) check(open.Chapter == 0 && !open.Has("chapter_one") && !open.Has("chapter_later"), b.Id + ": chapter 0 fixture.");
            check(!Rules.Available(story, scene, At(story, b.Chapter + 1, area, gate)), b.Id + ": open a chapter late.");
            if (b.Chapter > 0) check(!Rules.Available(story, scene, At(story, b.Chapter - 1, area, gate)), b.Id + ": open a chapter early.");
            if (b.Gate != null) check(!Rules.Available(story, scene, At(story, b.Chapter, area)), b.Id + ": open at a wrong moment on its list (no " + b.Gate + ").");
            if (b.Id == "anevia.early.watch") check(!Rules.Available(story, scene, At(story, 0, "", gate)), b.Id + ": open outside Neathholm.");
            check(Rules.Available(story, scene, At(story, b.Chapter, area, gate.Append("trickster").ToArray())),
                b.Id + ": a Trickster run loses the beat (N-all).");

            // Branches: every first-node choice records .seen (an interrupted dialog never re-offers); every terminal path sets
            // exactly one outcome; nothing native is set or started, no Trickster key is read, no check sits on a return-to-list.
            check(scene.Nodes[0].Choices.All(c => c.Set.Contains(b.Id + ".seen")), b.Id + ": a first-node choice does not record .seen.");
            check(b.Outcomes.Append(b.Id + ".seen").All(scene.Forbids.Contains), b.Id + ": Forbids lack an outcome or .seen.");
            var outcomes = Program.Walk(scene, open);
            // The Abyss night's drill offer reads the Chapter 1 drill: walk that history too.
            var drilledOpen = Program.Copy(open); drilledOpen.Flags.UnionWith(new[] { "seelah.early.drill.seen", "seelah.early.drill.landed" });
            if (b.Id == "seelah.abyss.night") outcomes.AddRange(Program.Walk(scene, drilledOpen));
            check(outcomes.Count >= b.Outcomes.Length && outcomes.All(o => b.Outcomes.Count(o.Has) == 1 && o.Has(b.Id + ".seen") && o.Has(b.Id)),
                b.Id + ": a terminal path sets no outcome, or more than one.");
            check(b.Outcomes.All(f => outcomes.Any(o => o.Has(f))), b.Id + ": an outcome is unreachable.");
            check(Choices(scene).All(c => !c.Abort && c.StartEtude == null && c.Mythic == null && c.Revive == null && c.NativeNext == null
                                          && c.Set.All(f => !native.Contains(f) && f.StartsWith(b.Id.Split('.')[0] + ".", StringComparison.Ordinal))),
                b.Id + ": a choice sets a native key or a foreign flag, starts an etude, or aborts.");
            check(!Reads(scene).Any(f => f == "trickster" || f == "trickster.ever" || f.Contains(".harem") || f.EndsWith(".committed", StringComparison.Ordinal)),
                b.Id + ": reads the Trickster, a harem or a committed flag.");
            check(!scene.ReturnToList || Choices(scene).All(c => c.Check == null), b.Id + ": a check on a return-to-list beat.");

            // Once: completed, or interrupted after the first answer (.seen alone), it never comes back.
            foreach (var played in outcomes)
            {
                var again = Program.Copy(played); again.Hour += 200;
                check(!Rules.Available(story, scene, again), b.Id + ": replaying the host offers the beat again.");
            }
            check(!Rules.Available(story, scene, At(story, b.Chapter, area, gate.Append(b.Id + ".seen").ToArray())),
                b.Id + ": an interrupted beat (.seen only) is offered again.");

            // Inert readers: only the beat itself and its named consequence reader read its flags.
            var mine = new HashSet<string>(b.Outcomes.Append(b.Id + ".seen").Append(b.Id));
            var readers = story.Scenes.Where(s => s.Id != b.Id && Reads(s).Any(mine.Contains)).Select(s => s.Id).OrderBy(x => x).ToArray();
            check(readers.SequenceEqual(Readers[b.Id].OrderBy(x => x)), b.Id + ": unexpected readers: " + string.Join(", ", readers));
            // Unique: no other scene sets these flags.
            check(!story.Scenes.Where(s => s.Id != b.Id).SelectMany(s => Choices(s)).Any(c => c.Set.Any(mine.Contains)),
                b.Id + ": another scene sets its flags.");
        }

        // Chapter 3 native romance keys (13 section 9): no PP1 beat is open in Chapter 3, none rides a native romance dialog's list,
        // and the consequences are appended to RRT scenes only (no native list gains an answer in Chapter 3).
        check(Beats.All(b => !Rules.Available(story, S(b.Id), At(story, 3, "", b.Gate == null ? Array.Empty<string>() : new[] { b.Gate }))),
            "PP1: a beat is open in Chapter 3.");

        // Consequences: each reader keeps its original choices in place and gains the variant last, visible only with the flag.
        void Reader(string sceneId, string node, string newNode, int originals, string[] flags, Snapshot state)
        {
            var scene = S(sceneId);
            var choices = scene.Nodes.Single(n => n.Id == node).Choices;
            int at = choices.FindIndex(c => c.Next == newNode);
            check(at >= originals, sceneId + ": the PP1 choice is not appended after the original " + originals + ".");
            check(!Rules.Match(choices[at].Requires, choices[at].Forbids, state), sceneId + "/" + newNode + ": visible without its beat.");
            var with = Program.Copy(state); with.Flags.UnionWith(flags);
            check(Rules.Match(choices[at].Requires, choices[at].Forbids, with), sceneId + "/" + newNode + ": hidden after its beat.");
            check(Program.Walk(scene, with, (id, _) => { }).Count > 0 && Program.WalkVia(scene, with, node, at).Count > 0,
                sceneId + "/" + newNode + ": the variant does not reach an ending.");
        }
        var plain = new Snapshot { Chapter = 3, Hour = 900 };
        Reader("a_cup", "start", "neath_splint", 3, new[] { "anevia.early.watch.seen", "anevia.early.watch.splinted" }, plain);
        Reader("a_cup", "start", "neath_strip", 3, new[] { "anevia.early.watch.seen", "anevia.early.watch.fumbled" }, plain);
        Reader("a_cup", "start", "neath_cover", 3, new[] { "anevia.early.watch.seen", "anevia.early.watch.covered" }, plain);
        Reader("a_cup", "start", "neath_gwerm", 3, new[] { "anevia.early.watch.seen", "anevia.early.watch.horgus" }, plain);
        Reader("i_hands", "start", "dh_steady", 3, new[] { "irabeth.early.steadied" }, plain);
        Reader("i_hands", "start", "dh_wall", 3, new[] { "irabeth.early.dismissed_help" }, plain);
        Reader("i_respite", "start", "chapel_wrong", 3, new[] { "irabeth.early.hook.shouldered" }, plain);
        Reader("i_respite", "start", "chapel_note", 3, new[] { "irabeth.early.hook.thanked_regill" }, plain);
        Reader("seelah.wager", "start", "button_mine", 3, new[] { "seelah.early.pack.lifted" }, plain);
        Reader("seelah.wager", "start", "button_tip", 3, new[] { "seelah.early.pack.tipped" }, plain);
        Reader("seelah.souls", "start", "abyss_night", 2, new[] { "seelah.abyss.night.seen", "seelah.abyss.night.halved", "seelah.abyss.night" }, plain);
        // An interrupted night (.seen only) is not remembered as a night shared.
        var interrupted = Program.Copy(plain); interrupted.Flags.Add("seelah.abyss.night.seen");
        check(S("seelah.souls").Nodes[0].Choices.Skip(2).All(c => !Rules.Match(c.Requires, c.Forbids, interrupted)), "PP1: an interrupted Abyss night is recalled in seelah.souls.");
        // A waved-off night leaves a_cup exactly as before.
        var waved = Program.Copy(plain); waved.Flags.UnionWith(new[] { "anevia.early.watch.seen", "anevia.early.watch.waved" });
        check(S("a_cup").Nodes[0].Choices.Skip(3).All(c => !Rules.Match(c.Requires, c.Forbids, waved)), "PP1: a waved-off night changes a_cup.");
        // The Ch1 drill is read in the Abyss: a drilled Commander gets the drill offer, a deferred one the owed lesson.
        var night = S("seelah.abyss.night");
        var abyss = At(story, 4, "", "seelah.abyss_holding_up");
        var firstNight = night.Nodes[0].Choices;
        var drilled = Program.Copy(abyss); drilled.Flags.UnionWith(new[] { "seelah.early.drill.seen", "seelah.early.drill.landed" });
        var deferred = Program.Copy(abyss); deferred.Flags.UnionWith(new[] { "seelah.early.drill.seen", "seelah.early.drill.deferred" });
        check(firstNight.Count(c => Rules.Match(c.Requires, c.Forbids, abyss)) == 2
              && firstNight.Count(c => Rules.Match(c.Requires, c.Forbids, drilled)) == 3
              && firstNight.Count(c => Rules.Match(c.Requires, c.Forbids, deferred)) == 3
              && !ReferenceEquals(firstNight[1], firstNight[2]), "PP1: the Abyss night does not read the Chapter 1 drill.");

        // Seelah's Chapter 4 beat is in person on her companion list, so Chapter 4 is not remote-only (13 section 4).
        check(!night.Remote && night.AnswerLists.Single() == "73260c45aa315c0419fc625f6fcb957d", "PP1: Seelah's Chapter 4 beat is not in person.");

        // Sol PP1 audit: Seelah's Drezen-staged rest scenes (the clerk's desk, the chapel steps, the citadel visits) need Drezen.
        foreach (var id in new[] { "seelah.trickster.dismissed.late", "seelah.trickster.dead.pickpocket_effects",
                                   "seelah.trickster.after.stay_or_go_visit", "seelah.trickster.after.courtship_visit",
                                   "seelah.trickster.dismissed.commit_visit", "seelah.trickster.dismissed.second_ask_visit",
                                   "seelah.trickster.dead_no_unit.seller_word_visit" })
            if (story.Scenes.Any(s => s.Id == id))
            {
                var scene = S(id);
                check(scene.Areas.SequenceEqual(new[] { "2570015799edf594daf2f076f2f975d8" }), "PP1: " + id + " is not gated to Drezen.");
                var elsewhere = new Snapshot { Chapter = 5, Hour = 9000, Area = "0a5654e7dc18f074d9356009d55eb51b" };
                elsewhere.Flags.UnionWith(Program.Prerequisites(scene));
                check(!Rules.Available(story, scene, elsewhere), "PP1: " + id + " opens at a Wintersun rest.");
            }

        // The shared Anevia list (13 section 7 (a)): every prior entry still targets it, in its authored order; PP1 adds none.
        var onList = story.Scenes.Where(s => Rules.EntryTargets(s).Contains(AneviaList)).Select(s => s.Id).ToList();
        check(AneviaListBaseline.All(onList.Contains), "PP1: an entry left Anevia's list: " + string.Join(", ", AneviaListBaseline.Where(id => !onList.Contains(id))));
        var order = AneviaListBaseline.Select(id => onList.IndexOf(id)).ToList();
        check(order.Zip(order.Skip(1), (a, b) => a < b).All(x => x), "PP1: Anevia's list entries were reordered.");
        check(!onList.Any(id => Beats.Any(b => b.Id == id)), "PP1: a beat was put on Anevia's shared list.");
    }
}
