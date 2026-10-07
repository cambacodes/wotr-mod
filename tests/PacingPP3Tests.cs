using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Pacing pass PP3 (Writer/handoffs/13-PACING-PASS.md sections 2a, 4 and 7, PP3 row and addendum; storylines/pacing_pp3.py):
// Aranka's, Nurah's and Jannah's early beats and Nurah's Chapter 4 packet. Per beat: the host and its return, the gate at the
// right moment and its absence at a wrong one on the same list, once-only (interrupted included), one outcome per terminal
// path, no native key set, no Trickster read, readers limited to the named consequence, and each consequence appended last.
internal static class PacingPP3Tests
{
    private sealed record Beat(string Id, string Relationship, int Chapter, string List, string? Return, string[] Outcomes,
                               string? Gate, string? WrongMoment);

    private static string[] Out(string prefix, params string[] v) => v.Select(x => prefix + x).ToArray();

    private static readonly Beat[] Beats = {
        new("aranka.early.duet", "aranka", 1, "2373bef62ea65d741a8f54ba95f9a8b2", null,
            Out("aranka.early.duet.", "shared", "stolen", "hers", "declined"), null, "aranka.kenabres_contest_won"),
        new("nurah.early.hands", "nurah", 2, "f392d579b9aac6947b65a2473775ffc9", "9b8d54436ef3a9a4597223caacb31e71",
            Out("nurah.early.hands.", "bound", "fumbled", "rag", "bled"), null, null),
        new("nurah.early.hanging", "nurah", 2, "2ce412d70ca0f40468252bec95ab2881", "217204ecd2fdaa74ab397f04a30acc77",
            Out("nurah.early.hanging.", "promised", "doubted", "bargained"), "nurah.siege_asked_to_stay", null),
        new("jannah.early.laugh", "jannah", 1, "7d40d23732cd28b4db2079945eadb89e", null,
            Out("jannah.early.laugh.", "honest", "bravado", "let_be"), "jannah.asked_watch_service", null),
        new("jannah.early.bout", "jannah", 2, "9995876fa83c0f049a84df4ca349f4af", null,
            Out("jannah.early.bout.", "accepted", "deferred", "refused"), null, null),
    };

    // The scenes allowed to read a PP3 flag: the named consequence readers, and the beats that route on or exclude another.
    private static readonly Dictionary<string, string[]> Readers = new()
    {
        ["aranka.early.duet"] = new[] { "aranka.trickster.verse.duet", "aranka.trickster.verse.duet_yard", "aranka.trickster.verse.duet_late", "aranka.trickster.verse.duet_yard_late" },
        ["nurah.early.hands"] = new[] { "nurah.early.hanging", "nurah.trickster.prison.night_out", "nurah.trickster.prison.night_out_late" },
        ["nurah.early.hanging"] = new[] { "nurah.early.hands", "nurah.trickster.prison.night_out", "nurah.trickster.prison.night_out_late" },
        ["jannah.early.laugh"] = new[] { "jannah.early.bout", "jannah.trickster.alive.stories" },
        ["jannah.early.bout"] = new[] { "jannah.trickster.alive.stories" },
    };

    private static readonly string[] Songs = { "aranka.kenabres_song_march", "aranka.kenabres_song_tavern", "aranka.kenabres_song_ballad" };

    private static Snapshot At(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 500 };
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

        // Bindings: the native keys that pin each moment (SelectedAnswers for the player's own choice, SeenCues for an outcome).
        var seenKeys = new Dictionary<string, string> {
            ["aranka.kenabres_voice_failed"] = "2c10c9d004184b7bbb22b6dd35f7fbc2",
            ["aranka.kenabres_contest_won"] = "dd66b8ab824c4b71864130c84bc72e15" };
        var answerKeys = new Dictionary<string, string> {
            ["aranka.kenabres_song_march"] = "44db38d17b9d41b396ab1c801929b2d9",
            ["aranka.kenabres_song_tavern"] = "953139a78ae142869340f88deb52d362",
            ["aranka.kenabres_song_ballad"] = "da10a8e01f6c47508c69f65d26567551",
            ["nurah.siege_asked_to_stay"] = "9f05ff7a6dafa8a41967ff6931723689",
            ["jannah.asked_watch_service"] = "d01295db57dadba4a810bd3e4a3bfdfc" };
        foreach (var kv in seenKeys)
            check(story.SeenCues.TryGetValue(kv.Key, out var cues) && cues.SequenceEqual(new[] { kv.Value }), "PP3: wrong SeenCues binding " + kv.Key);
        foreach (var kv in answerKeys)
            check(story.SelectedAnswers.TryGetValue(kv.Key, out var answer) && answer == kv.Value, "PP3: wrong SelectedAnswers binding " + kv.Key);

        foreach (var b in Beats)
        {
            var scene = S(b.Id);
            check(scene.Relationship == b.Relationship && scene.AnswerLists.SequenceEqual(new[] { b.List })
                  && Rules.EntryTargets(scene).SequenceEqual(new[] { b.List }), b.Id + ": wrong relationship or host list.");
            check(b.Return == null ? scene.ReturnToList && scene.NativeReturnCue == null : scene.NativeReturnCue == b.Return && !scene.ReturnToList,
                b.Id + ": wrong return (a retcheck-failed or replaying cue).");
            check(scene.Chapters.SequenceEqual(new[] { b.Chapter }) && scene.MinChapter == b.Chapter && scene.MaxChapter == b.Chapter && scene.Optional,
                b.Id + ": the window is not its host's chapter.");
            check(!string.IsNullOrWhiteSpace(scene.Entry), b.Id + ": empty inline entry.");

            // Entry: open at its moment; shut a chapter either side; shut on the same list at a wrong moment.
            var gate = b.Gate == null ? Array.Empty<string>() : new[] { b.Gate };
            var open = At(story, b.Chapter, gate);
            check(Rules.Available(story, scene, open), b.Id + ": closed at its own moment.");
            check(!Rules.Available(story, scene, At(story, b.Chapter + 1, gate)), b.Id + ": open a chapter late.");
            check(!Rules.Available(story, scene, At(story, b.Chapter - 1, gate)), b.Id + ": open a chapter early.");
            check(!Rules.Available(story, scene, At(story, 3, gate)), b.Id + ": open in Chapter 3 (a native romance key could wait on it).");
            if (b.Gate != null) check(!Rules.Available(story, scene, At(story, b.Chapter)), b.Id + ": open at a wrong moment on its list (no " + b.Gate + ").");
            if (b.WrongMoment != null) check(!Rules.Available(story, scene, At(story, b.Chapter, gate.Append(b.WrongMoment).ToArray())),
                b.Id + ": open at a wrong moment on its list (" + b.WrongMoment + ").");
            check(Rules.Available(story, scene, At(story, b.Chapter, gate.Append("trickster").ToArray())), b.Id + ": a Trickster run loses the beat (N-all).");

            // Branches: every first-node choice records .seen; every terminal path sets exactly one outcome; nothing native is
            // set or started, nothing aborts, no Trickster or harem key is read, and no check sits on a return-to-list beat.
            check(scene.Nodes[0].Choices.All(c => c.Set.Contains(b.Id + ".seen")), b.Id + ": a first-node choice does not record .seen.");
            check(b.Outcomes.Append(b.Id + ".seen").All(scene.Forbids.Contains), b.Id + ": Forbids lack an outcome or .seen.");
            var worlds = new List<Snapshot> { open };
            if (b.Id == "aranka.early.duet")
                worlds = Songs.Select(song => At(story, 1, "aranka.kenabres_voice_failed", song))
                    .Append(At(story, 1, "aranka.kenabres_voice_failed")).Append(open).ToList();
            if (b.Id == "jannah.early.bout") worlds.Add(At(story, 2, "jannah.early.laugh.seen", "jannah.early.laugh.bravado"));
            var outcomes = worlds.SelectMany(w => Program.Walk(scene, w)).ToList();
            check(outcomes.Count >= b.Outcomes.Length && outcomes.All(o => b.Outcomes.Count(o.Has) == 1 && o.Has(b.Id + ".seen") && o.Has(b.Id)),
                b.Id + ": a terminal path sets no outcome, or more than one.");
            check(b.Outcomes.All(f => outcomes.Any(o => o.Has(f))), b.Id + ": an outcome is unreachable.");
            check(Choices(scene).All(c => !c.Abort && c.StartEtude == null && c.Mythic == null && c.Revive == null && c.NativeNext == null
                                          && c.Crusade == null && c.Alignment == null
                                          && c.Set.All(f => !native.Contains(f) && f.StartsWith(b.Id + ".", StringComparison.Ordinal))),
                b.Id + ": a choice sets a native key or a foreign flag, starts an etude, costs or shifts, or aborts.");
            check(!Reads(scene).Any(f => f == "trickster" || f == "trickster.ever" || f.Contains(".harem") || f.Contains(".trickster.")
                                         || f.EndsWith(".committed", StringComparison.Ordinal) || f == "nurah.complete"),
                b.Id + ": reads the Trickster, a harem, a route or a committed flag.");
            check(!scene.ReturnToList || Choices(scene).All(c => c.Check == null), b.Id + ": a check on a return-to-list beat.");

            // Once: completed, or interrupted after the first answer (.seen alone), it never comes back.
            foreach (var played in outcomes)
            {
                var again = Program.Copy(played); again.Hour += 200;
                check(!Rules.Available(story, scene, again), b.Id + ": replaying the host offers the beat again.");
            }
            check(!Rules.Available(story, scene, At(story, b.Chapter, gate.Append(b.Id + ".seen").ToArray())),
                b.Id + ": an interrupted beat (.seen only) is offered again.");

            // Inert readers: only the named consequence readers (and a sibling beat's router or exclusion) read its flags.
            var mine = new HashSet<string>(b.Outcomes.Append(b.Id + ".seen").Append(b.Id));
            var readers = story.Scenes.Where(s => s.Id != b.Id && Reads(s).Any(mine.Contains)).Select(s => s.Id).OrderBy(x => x).ToArray();
            check(readers.SequenceEqual(Readers[b.Id].OrderBy(x => x)), b.Id + ": unexpected readers: " + string.Join(", ", readers));
            check(!story.Scenes.Where(s => s.Id != b.Id).SelectMany(s => Choices(s)).Any(c => c.Set.Any(mine.Contains)),
                b.Id + ": another scene sets its flags.");
        }

        // Aranka: one opening per history (the song that failed, a failure with no song recorded, or never sung).
        var duetBeat = S("aranka.early.duet");
        var histories = new Dictionary<string, Snapshot> {
            ["march"] = At(story, 1, "aranka.kenabres_voice_failed", Songs[0]),
            ["tavern"] = At(story, 1, "aranka.kenabres_voice_failed", Songs[1]),
            ["ballad"] = At(story, 1, "aranka.kenabres_voice_failed", Songs[2]),
            ["cracked"] = At(story, 1, "aranka.kenabres_voice_failed"),
            ["fresh"] = At(story, 1) };
        foreach (var h in histories)
        {
            var pages = new HashSet<string>();
            Program.Walk(duetBeat, h.Value, (page, _) => pages.Add(page));
            check(histories.Keys.Count(pages.Contains) == 1 && pages.Contains(h.Key), "PP3: Aranka's beat opens wrong for " + h.Key);
        }

        // Nurah: the two siege branches never both play (each forbids the other's .seen).
        check(S("nurah.early.hands").Forbids.Contains("nurah.early.hanging.seen") && S("nurah.early.hanging").Forbids.Contains("nurah.early.hands.seen"),
            "PP3: Nurah's two siege beats can both play.");
        // Jannah: the Chapter 2 bout remembers a bout owed from Chapter 1.
        var boutPages = new HashSet<string>();
        Program.Walk(S("jannah.early.bout"), At(story, 2, "jannah.early.laugh.seen", "jannah.early.laugh.bravado"), (page, _) => boutPages.Add(page));
        check(boutPages.Contains("owed") && !boutPages.Contains("fresh"), "PP3: the Chapter 2 bout forgets the bout owed at the Defender's Heart.");

        // Consequences: each reader keeps its original choices in place and gains the variant last, visible only with the flag.
        void Reader(string sceneId, string node, string newNode, int originals, string[] flags, Snapshot state, string? reaches = null)
        {
            var scene = S(sceneId);
            var choices = scene.Nodes.Single(n => n.Id == node).Choices;
            int at = choices.FindIndex(c => c.Next == newNode);
            check(at >= originals, sceneId + ": the PP3 choice is not appended after the original " + originals + ".");
            check(!Rules.Match(choices[at].Requires, choices[at].Forbids, state), sceneId + "/" + newNode + ": visible without its beat.");
            var with = Program.Copy(state); with.Flags.UnionWith(flags);
            check(Rules.Match(choices[at].Requires, choices[at].Forbids, with), sceneId + "/" + newNode + ": hidden after its beat.");
            var via = Program.WalkVia(scene, with, node, at);
            check(via.Count > 0 && (reaches == null || via.All(r => r.Has(reaches))), sceneId + "/" + newNode + ": the variant does not reach its ending.");
        }
        var plain = new Snapshot { Chapter = 3, Hour = 900 };
        foreach (var duet in new[] { "aranka.trickster.verse.duet", "aranka.trickster.verse.duet_yard", "aranka.trickster.verse.duet_late", "aranka.trickster.verse.duet_yard_late" })
            foreach (var v in new[] { "shared", "stolen", "hers", "declined" })
                Reader(duet, "duet", "parlour_" + v, 2, new[] { "aranka.early.duet.seen", "aranka.early.duet." + v }, plain, "aranka.trickster.duet_sung");
        foreach (var night in new[] { "nurah.trickster.prison.night_out", "nurah.trickster.prison.night_out_late" })
        {
            foreach (var v in new[] { "bound", "fumbled", "rag", "bled" })
                Reader(night, "start", "siege_" + v, 4, new[] { "nurah.early.hands.seen", "nurah.early.hands." + v }, plain);
            Reader(night, "start", "siege_promised", 4, new[] { "nurah.early.hanging.seen", "nurah.early.hanging.promised" }, plain);
            Reader(night, "start", "siege_promised", 4, new[] { "nurah.early.hanging.seen", "nurah.early.hanging.doubted" }, plain);
            Reader(night, "start", "siege_bargained", 4, new[] { "nurah.early.hanging.seen", "nurah.early.hanging.bargained" }, plain);
            // The recalled night asks again, with the same answers: three tempers that return her, and her hard no.
            var scene = S(night);
            var start = scene.Nodes.Single(n => n.Id == "start");
            foreach (var recall in scene.Nodes.Where(n => n.Id.StartsWith("siege_", StringComparison.Ordinal)))
                check(recall.Choices.Select(c => c.Next).SequenceEqual(start.Choices.Take(4).Select(c => c.Next))
                      && recall.Choices.Take(3).All(c => c.Set.Contains("nurah.trickster.released") && c.Set.Contains("nurah.trickster.accepted"))
                      && recall.Choices[3].Set.Contains("nurah.closed"), night + "/" + recall.Id + ": the recalled night changes her question's answers.");
        }
        var bargainedOnly = Program.Copy(plain); bargainedOnly.Flags.UnionWith(new[] { "nurah.early.hanging.seen", "nurah.early.hanging.bargained" });
        check(S("nurah.trickster.prison.night_out").Nodes[0].Choices.Count(c => Rules.Match(c.Requires, c.Forbids, bargainedOnly)) == 5,
            "PP3: a bargained siege also offers the promised recall.");
        foreach (var v in new[] { "honest", "bravado", "let_be" })
            Reader("jannah.trickster.alive.stories", "start", "heart_" + v, 3, new[] { "jannah.early.laugh.seen", "jannah.early.laugh." + v }, plain);
        Reader("jannah.trickster.alive.stories", "start", "camp_bout", 3, new[] { "jannah.early.bout.seen", "jannah.early.bout.accepted" }, plain);
        Reader("jannah.trickster.alive.stories", "start", "camp_bout", 3, new[] { "jannah.early.bout.seen", "jannah.early.bout.deferred" }, plain);
        Reader("jannah.trickster.alive.stories", "start", "camp_record", 3, new[] { "jannah.early.bout.seen", "jannah.early.bout.refused" }, plain);
        var refusedOnly = Program.Copy(plain); refusedOnly.Flags.UnionWith(new[] { "jannah.early.bout.seen", "jannah.early.bout.refused" });
        check(S("jannah.trickster.alive.stories").Nodes.Single(n => n.Id == "start").Choices.Count(c => Rules.Match(c.Requires, c.Forbids, refusedOnly)) == 4,
            "PP3: a refused bout is also remembered as a bout owed.");

        // Nurah, Chapter 4 (T): the packet in the map case. A letter opened in the Abyss on her living prison branch only.
        var sky = S("nurah.trickster.abyss.sky");
        check(Rules.IsRemote(sky) && sky.Kind == "letter" && sky.Chapters.SequenceEqual(new[] { 4 }) && sky.MinChapter == 4 && sky.MaxChapter == 4
              && sky.Relationship == "nurah" && !sky.TricksterDevice, "PP3: the packet lost its shape (a Chapter 4 letter on her route).");
        string[] living = { "trickster.ever", "nurah.prison", "nurah.trickster.released", "nurah.trickster.accepted" };
        check(Rules.Available(story, sky, At(story, 4, living)), "PP3: the packet does not open in the Abyss.");
        foreach (int ch in new[] { 3, 5 }) check(!Rules.Available(story, sky, At(story, ch, living)), "PP3: the packet opens in Chapter " + ch);
        check(!Rules.Available(story, sky, At(story, 4, "trickster.ever", "nurah.prison")), "PP3: the packet comes from a Nurah who never walked out.");
        check(!Rules.Available(story, sky, At(story, 4, "trickster.ever", "nurah.prison", "nurah.trickster.released")),
            "PP3: the packet comes from a Nurah who never answered why.");
        foreach (var block in new[] { "nurah.closed", "nurah.trickster.returned", "nurah.ran_off", "nurah.dead_drezen", "nurah.dead_camellia", "nurah.killing_mechanism" })
            check(!Rules.Available(story, sky, At(story, 4, living.Append(block).ToArray())), "PP3: the packet ignores " + block);
        var skyOut = new[] { "nurah.trickster.abyss.sky_plain", "nurah.trickster.abyss.sky_pretty", "nurah.trickster.abyss.sky_blank" };
        var opened = Program.Walk(sky, At(story, 4, living)).Where(r => r.Has(sky.Id)).ToList();
        check(opened.Count == 3 && skyOut.All(f => opened.Count(r => r.Has(f)) == 1) && opened.All(r => skyOut.Count(r.Has) == 1)
              && opened.All(r => !Rules.Available(story, sky, Program.Copy(r))), "PP3: the packet cannot be answered three ways, or opens twice.");
        var notePages = new HashSet<string>();
        Program.Walk(sky, At(story, 4, living), (page, _) => notePages.Add(page));
        var keptPages = new HashSet<string>();
        Program.Walk(sky, At(story, 4, living.Append("nurah.complete").ToArray()), (page, _) => keptPages.Add(page));
        check(notePages.Contains("note") && !notePages.Contains("note_kept") && keptPages.Contains("note_kept") && !keptPages.Contains("note"),
            "PP3: the packet's postscript is written to the wrong Nurah.");
        check(Choices(sky).All(c => c.Set.All(f => f.StartsWith("nurah.trickster.abyss.", StringComparison.Ordinal)) && c.Crusade == null && c.Check == null),
            "PP3: the packet sets a foreign flag or costs something.");
        // Its reader: one paragraph per sky on each page that publishes her book, and no other reader.
        foreach (var page in new[] { "nurah.trickster.epilogue.the_margin", "nurah.trickster.epilogue.book_only", "nurah.trickster.epilogue.unanswered",
                                     "nurah.trickster.epilogue.bereaved", "nurah.trickster.epilogue.refused" })
        {
            var paragraphs = S(page).Nodes.Single(n => n.Id == "start").Paragraphs;
            check(skyOut.All(f => paragraphs.Count(p => p.Requires.SequenceEqual(new[] { f })) == 1), "PP3: " + page + " does not print the Abyss chapter.");
        }
        var skyReaders = story.Scenes.Where(s => s.Id != sky.Id && Reads(s).Any(skyOut.Contains)).Select(s => s.Id).OrderBy(x => x).ToArray();
        check(skyReaders.Length == 5, "PP3: unexpected readers of the packet: " + string.Join(", ", skyReaders));
    }
}
