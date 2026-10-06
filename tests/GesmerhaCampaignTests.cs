using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class GesmerhaCampaignTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string actor = "3ba3a0ff8575be8419159221177c1411";
        const string capital = "2570015799edf594daf2f076f2f975d8";
        var openingIds = new[] { "unbought_work", "along_the_grain", "whose_mark", "the_first_game", "the_unclaimed_hour", "against_the_current" };
        var nextIds = new[] { "a_story_from_elsewhere", "the_unfinished_verse", "the_evening_answer", "what_she_asks" };
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "gesmerha." + id);
        var opening = openingIds.Select(Find).ToArray();
        var next = nextIds.Select(Find).ToArray();
        var reunion = Find("the_voice_at_court");
        // PP7 (Chapter 4): the travelers' song carried in the Abyss (a remote memory; nothing crosses the planes).
        var song = Find("the_road_home");
        var songPages = new HashSet<string>();
        string[] songVariants = { "gesmerha.abyss_song.sung", "gesmerha.abyss_song.verse", "gesmerha.abyss_song.hushed" };
        check(song.Remote && song.Kind == "memory" && song.Chapters.SequenceEqual(new[] { 4 }) && song.MinChapter == 4 && song.MaxChapter == 4
              && song.Relationship == "gesmerha" && !song.Requires.Any(f => f.StartsWith("trickster", StringComparison.Ordinal))
              && song.Requires.SequenceEqual(new[] { "gesmerha.campaign_kept", "gesmerha.verse_kept" })
              && new[] { "gesmerha.dead", "gesmerha.closed", "gesmerha.abyss_song" }.All(song.Forbids.Contains),
            "Gesmerha's Abyss song lost its shape (remote memory, Chapter 4, path-neutral, after the kept chain).");
        var endings = story.Scenes.Where(s => s.Id.StartsWith("gesmerha.ending_", StringComparison.Ordinal)).ToArray();
        var reached = new HashSet<string>();
        var outcomesSeen = new HashSet<string>();
        var earned = new List<Snapshot>();

        List<Snapshot> Play(Scene scene, IEnumerable<Snapshot> inputs, bool inspect)
        {
            var results = new List<Snapshot>();
            foreach (var input in inputs)
            {
                var ready = Program.Copy(input);
                ready.Hour += scene.DelayHours + 24;
                check(Program.CurrentAvailable(story, scene, ready), "Gesmerha played predecessor cannot enter " + scene.Id);
                foreach (var outcome in Program.Walk(scene, ready, (page, state) =>
                {
                    if (!inspect) return;
                    reached.Add(scene.Id + "/" + page);
                    check(Rules.ContactAvailable(story, scene, state), "Gesmerha valid page loses contact.");
                    check(state.Flags.SetEquals(ready.Flags), "Gesmerha interrupted page records an unplayed outcome.");
                    var missing = Program.Copy(state);
                    missing.AvailableContacts.Clear();
                    check(!Rules.ContactAvailable(story, scene, missing), "Gesmerha page ignores vanished actor.");
                    var dead = Program.Copy(state);
                    dead.Flags.Add("gesmerha.dead");
                    check(!Rules.ContactAvailable(story, scene, dead), "Gesmerha page continues after native death.");
                    if (page == "offer") check(state.Has("trickster"), "Gesmerha fate experiment leaks outside Trickster.");
                    if (scene == reunion)
                    {
                        var departed = Program.Copy(state);
                        departed.Flags.Remove("gesmerha.capital_guest");
                        check(!Rules.ContactAvailable(story, scene, departed), "Gesmerha reunion outlives active native guest.");
                        if (page == "trays") check(state.Has("gesmerha.grain_missed"), "Gesmerha remembers unmade trays.");
                        if (page == "board") check(!state.Has("gesmerha.grain_missed"), "Gesmerha remembers an unmade hinged board.");
                        if (page == "lover" || page == "kiss" || page == "part") check(state.Has("gesmerha.lover"), "Gesmerha friendship treated as established lovers.");
                        if (page == "shelter") check(state.Has("gesmerha.heard_staying") && !state.Has("gesmerha.heard_migration"), "Gesmerha invents or overrides observed future.");
                        if (page == "leaving") check(state.Has("gesmerha.heard_migration"), "Gesmerha invents migration report.");
                    }
                }))
                {
                    foreach (var flag in Program.PersistentFlags(story, ready))
                        check(outcome.Has(flag), "Gesmerha erases native, previous or unrelated history: " + flag);
                    if (!outcome.Has(scene.Id))
                    {
                        check(outcome.Flags.SetEquals(ready.Flags), "Gesmerha defer changes relationship progress.");
                        check(outcome.Times.OrderBy(x => x.Key).SequenceEqual(ready.Times.OrderBy(x => x.Key)), "Gesmerha defer changes recorded times.");
                        continue;
                    }
                    check(!Program.CurrentAvailable(story, scene, outcome), "Gesmerha finished scene replays.");
                    if (inspect) outcomesSeen.UnionWith(outcome.Flags);
                    results.Add(outcome);
                }
            }
            return results.GroupBy(s => string.Join("|", s.Flags.OrderBy(x => x))).Select(g => g.First()).ToList();
        }

        foreach (var history in new[] { "truth", "illusions", "both" })
        foreach (bool chief in new[] { false, true })
        foreach (bool trickster in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 3, Hour = 1000, Area = opening[0].Areas.Single() };
            state.AvailableContacts.Add(actor);
            state.Flags.UnionWith(new[] { "gesmerha.wintersun_resolved", "seelah.committed", "jerribeth.committed" });
            if (history != "illusions") state.Flags.Add("gesmerha.truth");
            if (history != "truth") state.Flags.Add("gesmerha.illusions");
            if (chief) state.Flags.Add("gesmerha.marhevok_rules");
            if (trickster) state.Flags.Add("trickster");
            var states = new List<Snapshot> { state };
            foreach (var scene in opening) states = Play(scene, states, false);
            foreach (var scene in next) states = Play(scene, states, true);
            check(states.Count > 0, "Gesmerha full predecessor chain has no result.");
            foreach (var result in states)
            {
                check(result.Has("gesmerha.campaign_kept"), "Gesmerha campaign ending has no completion.");
                check(new[] { "lover", "campaign_slow", "campaign_friends" }.Count(x => result.Has("gesmerha." + x)) == 1, "Gesmerha new relationship decisions overlap.");
                check(result.Has("gesmerha.committed") == result.Has("gesmerha.lover"), "Gesmerha commitment not earned by mutual terms.");
                check(!result.Has("gesmerha.lover") || !result.Has("gesmerha.friendship"), "Established friendship forcibly becomes romance.");
            }
            earned.AddRange(states);
            // PP7: the song is optional, so both the sung and the unplayed histories reach Chapter 5.
            var carried = new List<Snapshot>(states);
            foreach (var kept in states)
            {
                check(!Program.CurrentAvailable(story, song, kept), "Gesmerha's Abyss song opens before the Abyss.");
                var abyss = Program.Copy(kept); abyss.Chapter = 4; abyss.Hour += song.DelayHours;
                check(Program.CurrentAvailable(story, song, abyss), "Gesmerha's Abyss song does not follow the kept chain.");
                foreach (var blocker in song.Forbids)
                {
                    var blocked = Program.Copy(abyss); blocked.Flags.Add(blocker);
                    check(!Program.CurrentAvailable(story, song, blocked), "Gesmerha's Abyss song ignores blocker " + blocker);
                }
                var pages = new HashSet<string>();
                var sung = Program.Walk(song, abyss, (page, _) => { songPages.Add(page); pages.Add(page); }).Where(r => r.Has(song.Id)).ToList();
                check(pages.Contains("shared") == kept.Has("gesmerha.song_shared") && pages.Contains("answer") == !kept.Has("gesmerha.song_shared"),
                    "Gesmerha's Abyss song remembers a version of the song that was not settled.");
                check(sung.Count == 3 && sung.All(r => r.Has("gesmerha.abyss_song") && songVariants.Count(r.Has) == 1 && !Program.CurrentAvailable(story, song, r))
                      && songVariants.All(v => sung.Any(r => r.Has(v))),
                    "Gesmerha's Abyss song loses a variant, overlaps, or replays.");
                carried.AddRange(sung);
            }

            // Native fixture: the actual C5 guest has begun and her future answer was heard.
            var visitors = carried.Select(s =>
            {
                var v = Program.Copy(s);
                v.Chapter = 5; v.Area = capital;
                v.Flags.UnionWith(new[] { "gesmerha.capital_guest", "gesmerha.heard_future" });
                v.Flags.Add(history == "illusions" ? "gesmerha.heard_staying" : "gesmerha.heard_migration");
                if (history == "both") v.Flags.Add("gesmerha.heard_staying");
                return v;
            }).ToList();
            if (chief)
                foreach (var visitor in visitors) check(!Program.CurrentAvailable(story, reunion, visitor), "Marhevok's audience manufactures Gesmerha contact.");
            else
                earned.AddRange(Play(reunion, visitors, true));
        }

        foreach (var scene in next.Concat(new[] { reunion }))
        {
            foreach (var page in scene.Nodes) check(reached.Contains(scene.Id + "/" + page.Id), "Unplayed Gesmerha campaign page: " + scene.Id + "/" + page.Id);
            check(scene.ContactUnit == actor && !scene.Remote, "Gesmerha loses actual physical contact requirement.");
            var ready = new Snapshot { Chapter = scene.MinChapter, Hour = 10000, Area = scene.Areas.Single() };
            ready.Flags.UnionWith(scene.Requires);
            ready.Flags.Add("gesmerha.truth");
            ready.AvailableContacts.Add(actor);
            check(Program.CurrentAvailable(story, scene, ready), "Gesmerha gate baseline invalid.");
            foreach (var flag in scene.Requires.Concat(new[] { "gesmerha.truth" }).Where(k => !story.Derived.ContainsKey(k)))
            {
                var blocked = Program.Copy(ready); blocked.Flags.Remove(flag);
                check(!Program.CurrentAvailable(story, scene, blocked), "Gesmerha ignores prerequisite " + flag);
            }
            foreach (var flag in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag);
                check(!Program.CurrentAvailable(story, scene, blocked), "Gesmerha ignores blocker " + flag);
            }
            foreach (var chapter in new[] { 1, 2, 3, 4, 5, 6 }.Where(c => c != scene.MinChapter))
            {
                var blocked = Program.Copy(ready); blocked.Chapter = chapter;
                check(!Program.CurrentAvailable(story, scene, blocked), "Gesmerha physical scene leaks into chapter " + chapter);
            }
        }
        check(songPages.SetEquals(song.Nodes.Select(n => n.Id)), "Unreached page of Gesmerha's Abyss song.");
        // Each variant is answered only by its own line at court, appended after the original two.
        var songs = reunion.Nodes.Single(n => n.Id == "songs").Choices;
        check(songs.Count == 5 && songs[0].Next == "trays" && songs[1].Next == "board"
              && songs.Skip(2).Select(c => c.Requires.Single()).SequenceEqual(songVariants)
              && songs.Skip(2).Select(c => c.Next).SequenceEqual(new[] { "abyss_sung", "abyss_verse", "abyss_hushed" }),
            "Gesmerha's Abyss song answers were not appended, or read the wrong flag.");
        check(reunion.Nodes.TakeLast(3).Select(n => n.Id).SequenceEqual(new[] { "abyss_sung", "abyss_verse", "abyss_hushed" }),
            "Gesmerha's Abyss song pages were not appended at the end of the audience.");
        check(reunion.DelayHours == 0 && reunion.AnswerLists.SequenceEqual(new[] { "fb3a88e8ed751214c9136f87891ec07b" }), "Gesmerha transient audience requires impossible return or unrelated entry.");
        foreach (var flag in new[] { "gesmerha.lover", "gesmerha.campaign_slow", "gesmerha.campaign_friends", "gesmerha.reunion_lovers", "gesmerha.reunion_quiet", "gesmerha.closed" })
            check(outcomesSeen.Contains(flag), "Missing played Gesmerha outcome: " + flag);

        foreach (var state in earned.GroupBy(s => string.Join("|", new[] { "gesmerha.reunion_kept", "gesmerha.lover", "gesmerha.campaign_slow", "gesmerha.campaign_friends", "gesmerha.closed" }.Where(s.Has))).Select(g => g.First()))
        foreach (var native in new[] { "", "gesmerha.dead", "inhuman", "demon", "devil", "ascended", "sacrifice", "gesmerha.dead|ascended|sacrifice|inhuman|demon|devil", "ascended|sacrifice", "demon|devil" })
        {
            var terminal = Program.Copy(state);
            terminal.Chapter = 5;
            terminal.Flags.UnionWith(native.Split('|', StringSplitOptions.RemoveEmptyEntries));
            var available = endings.Where(s => s.Owner == "Epilogue" && Program.CurrentAvailable(story, s, terminal)).ToArray();
            // Earned presence (rubric Binding context (3)): beside an unreturned sacrifice only the mourning page may play, and it
            // does not cover her own death or a changed Commander, so those overlaps leave the native slides alone.
            bool mournedOut = terminal.Has("sacrifice") && new[] { "gesmerha.dead", "ascended", "inhuman", "demon", "devil" }.Any(terminal.Has);
            check(available.Length == (terminal.Has("gesmerha.closed") && !terminal.Has("gesmerha.dead") || mournedOut ? 0 : 1), "Gesmerha epilogue arbitration overlaps or loses played history: " + native);
            foreach (var scene in available)
            {
                foreach (var outcome in Program.Walk(scene, terminal, (page, _) => reached.Add(scene.Id + "/" + page)))
                    check(outcome.Has(scene.Id), "Gesmerha ending cannot complete.");
            }
        }
        var aeon = Find("ending_aeon");
        var aeonState = earned.First(s => !s.Has("gesmerha.closed"));
        check(Program.CurrentAvailable(story, aeon, aeonState), "Gesmerha remade-history conclusion loses played campaign.");
        Program.Walk(aeon, aeonState, (page, _) => reached.Add(aeon.Id + "/" + page));
        foreach (var scene in endings)
            foreach (var page in scene.Nodes) check(reached.Contains(scene.Id + "/" + page.Id), "Unplayed Gesmerha provisional ending: " + scene.Id);
    }
}
