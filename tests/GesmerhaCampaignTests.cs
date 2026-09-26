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
                check(Rules.Available(story, scene, ready), "Gesmerha played predecessor cannot enter " + scene.Id);
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
                    foreach (var flag in ready.Flags)
                        check(outcome.Has(flag), "Gesmerha erases native, previous or unrelated history: " + flag);
                    if (!outcome.Has(scene.Id))
                    {
                        check(outcome.Flags.SetEquals(ready.Flags), "Gesmerha defer changes relationship progress.");
                        check(outcome.Times.OrderBy(x => x.Key).SequenceEqual(ready.Times.OrderBy(x => x.Key)), "Gesmerha defer changes recorded times.");
                        continue;
                    }
                    check(!Rules.Available(story, scene, outcome), "Gesmerha finished scene replays.");
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

            // Native fixture: the actual C5 guest has begun and her future answer was heard.
            var visitors = states.Select(s =>
            {
                var v = Program.Copy(s);
                v.Chapter = 5; v.Area = capital;
                v.Flags.UnionWith(new[] { "gesmerha.capital_guest", "gesmerha.heard_future" });
                v.Flags.Add(history == "illusions" ? "gesmerha.heard_staying" : "gesmerha.heard_migration");
                if (history == "both") v.Flags.Add("gesmerha.heard_staying");
                return v;
            }).ToList();
            if (chief)
                foreach (var visitor in visitors) check(!Rules.Available(story, reunion, visitor), "Marhevok's audience manufactures Gesmerha contact.");
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
            check(Rules.Available(story, scene, ready), "Gesmerha gate baseline invalid.");
            foreach (var flag in scene.Requires.Concat(new[] { "gesmerha.truth" }))
            {
                var blocked = Program.Copy(ready); blocked.Flags.Remove(flag);
                check(!Rules.Available(story, scene, blocked), "Gesmerha ignores prerequisite " + flag);
            }
            foreach (var flag in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag);
                check(!Rules.Available(story, scene, blocked), "Gesmerha ignores blocker " + flag);
            }
            foreach (var chapter in new[] { 1, 2, 3, 4, 5, 6 }.Where(c => c != scene.MinChapter))
            {
                var blocked = Program.Copy(ready); blocked.Chapter = chapter;
                check(!Rules.Available(story, scene, blocked), "Gesmerha physical scene leaks into chapter " + chapter);
            }
        }
        check(reunion.DelayHours == 0 && reunion.AnswerLists.SequenceEqual(new[] { "fb3a88e8ed751214c9136f87891ec07b" }), "Gesmerha transient audience requires impossible return or unrelated entry.");
        foreach (var flag in new[] { "gesmerha.lover", "gesmerha.campaign_slow", "gesmerha.campaign_friends", "gesmerha.reunion_lovers", "gesmerha.reunion_quiet", "gesmerha.closed" })
            check(outcomesSeen.Contains(flag), "Missing played Gesmerha outcome: " + flag);

        foreach (var state in earned.GroupBy(s => string.Join("|", new[] { "gesmerha.reunion_kept", "gesmerha.lover", "gesmerha.campaign_slow", "gesmerha.campaign_friends", "gesmerha.closed" }.Where(s.Has))).Select(g => g.First()))
        foreach (var native in new[] { "", "gesmerha.dead", "inhuman", "demon", "devil", "ascended", "sacrifice", "gesmerha.dead|ascended|sacrifice|inhuman|demon|devil", "ascended|sacrifice", "demon|devil" })
        {
            var terminal = Program.Copy(state);
            terminal.Chapter = 5;
            terminal.Flags.UnionWith(native.Split('|', StringSplitOptions.RemoveEmptyEntries));
            var available = endings.Where(s => s.Owner == "Epilogue" && Rules.Available(story, s, terminal)).ToArray();
            check(available.Length == (terminal.Has("gesmerha.closed") && !terminal.Has("gesmerha.dead") ? 0 : 1), "Gesmerha epilogue arbitration overlaps or loses played history: " + native);
            foreach (var scene in available)
            {
                foreach (var outcome in Program.Walk(scene, terminal, (page, _) => reached.Add(scene.Id + "/" + page)))
                    check(outcome.Has(scene.Id), "Gesmerha ending cannot complete.");
            }
        }
        var aeon = Find("ending_aeon");
        var aeonState = earned.First(s => !s.Has("gesmerha.closed"));
        check(Rules.Available(story, aeon, aeonState), "Gesmerha remade-history conclusion loses played campaign.");
        Program.Walk(aeon, aeonState, (page, _) => reached.Add(aeon.Id + "/" + page));
        foreach (var scene in endings)
            foreach (var page in scene.Nodes) check(reached.Contains(scene.Id + "/" + page.Id), "Unplayed Gesmerha provisional ending: " + scene.Id);
    }
}
