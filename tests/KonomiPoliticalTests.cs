using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KonomiPoliticalTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var ordinary = story.Scenes.Single(s => s.Id == "konomi.political_account");
        var personal = story.Scenes.Single(s => s.Id == "konomi.private_political_account");
        var power = story.Scenes.Single(s => s.Id == "konomi.power");
        var focused = new Story { Scenes = new List<Scene> { ordinary, personal }, Relationships = story.Relationships };
        var visited = new Dictionary<string, HashSet<string>>
        {
            [ordinary.Id] = new HashSet<string>(), [personal.Id] = new HashSet<string>()
        };

        check(story.StartedDialogs["konomi.rank_six_started"] == "30333438aac8d3647bef882fa87e978e"
            && story.StartedDialogs["konomi.rank_eight_started"] == "6178470b05c75484085753b821a6a614",
            "Konomi dialogue-start bindings differ from native DialogSeen targets.");
        check(story.Etudes["konomi.foreign_help_playing"] == "c6e9a69f602a48e18424f4b6d71062b4",
            "Konomi foreign-help predicate is not the native playing etude.");
        check(story.SeenCues["konomi.council_conclusion_seen"].SequenceEqual(new[] { "7f64a30ceb4bfb046990bccbded7ac75" })
            && story.SeenCues["konomi.political_respect_seen"].SequenceEqual(new[] { "8311ef29223c4fe469c95cd8eb80e539" }),
            "Konomi memories do not use the exact conclusion/respect cues.");
        check(story.SelectedAnswers["konomi.dismissed"] == "73c5728c4c6658344bedcc1b666e598c"
            && story.CompletedEtudes["konomi.office_completed"] == "b5f301fbc4c44535a6309d610d5bd28a",
            "Political context replaced native dismissal or office-completion history.");
        check(!ordinary.Optional && !Rules.IsRemote(ordinary) && personal.Optional && personal.ManualOnly,
            "Konomi political scene delivery changes the mandatory or optional contact contract.");
        check(power.Requires.Contains(ordinary.Id), "Konomi's new ordinary future bypasses the political context.");

        Choice Select(Scene scene, string page, Snapshot state)
        {
            var choices = scene.Nodes.Single(n => n.Id == page).Choices
                .Where(c => Rules.Match(c.Requires, c.Forbids, state)).ToArray();
            check(choices.Length == 1, "Konomi political history overlaps or strands a page: " + scene.Id + "/" + page);
            return choices.Single();
        }

        foreach (bool privateContact in new[] { false, true })
        foreach (bool six in new[] { false, true })
        foreach (bool eight in new[] { false, true })
        foreach (bool help in new[] { false, true })
        foreach (bool conclusion in new[] { false, true })
        foreach (bool respect in new[] { false, true })
        {
            var scene = privateContact ? personal : ordinary;
            var state = new Snapshot { Chapter = 5, Area = "2570015799edf594daf2f076f2f975d8", Hour = 1000 };
            if (!privateContact) state.AvailableContacts.Add("ca2d58c5c65723945857e04fb85d30ce");
            state.Flags.UnionWith(privateContact
                ? new[] { "konomi.dismissed", "konomi.office_completed", "konomi.private_returned" }
                : new[] { "konomi.present", "konomi.return" });
            state.Flags.UnionWith(new[] { "konomi.attracted", "konomi.lovers", "seelah.committed", "arueshalae.committed" });
            foreach (var pair in new[] { ("konomi.rank_six_started", six), ("konomi.rank_eight_started", eight),
                ("konomi.foreign_help_playing", help), ("konomi.council_conclusion_seen", conclusion),
                ("konomi.political_respect_seen", respect) })
                if (pair.Item2) state.Flags.Add(pair.Item1);
            state.Times[privateContact ? "konomi.private_returned" : "konomi.return"] = state.Hour - 24;
            check(Rules.Available(story, scene, state), "Valid native history blocks Konomi's political conversation.");
            check(!Rules.Available(story, privateContact ? ordinary : personal, state), "Konomi political contact modes overlap.");
            check(Rules.NextRemote(focused, state) == null, "Manual private political context enters the automatic rest queue.");

            string expected = eight ? help ? "foreign" : "domestic" : six ? "crisis" : "uncertain";
            check(Select(scene, "situation", state).Next == expected,
                "Konomi report does not preserve native rank-eight-over-rank-six precedence.");
            check(Select(scene, "council", state).Next == (conclusion ? "concluded" : "unconcluded"),
                "A started dialogue invents a remembered council conclusion.");
            check(Select(scene, "respect", state).Next == (respect ? "earned" : "unearned"),
                "Political respect is awarded without its native cue.");

            var outcomes = Program.Walk(scene, state, (node, _) => visited[scene.Id].Add(node));
            foreach (var result in outcomes)
            {
                check(result.Flags.Except(state.Flags).All(flag => flag == scene.Id),
                    "Konomi political conversation fabricates native decisions or changes another romance.");
                check(state.Flags.IsSubsetOf(result.Flags), "Konomi political conversation removes existing history.");
                if (!result.Has(scene.Id))
                {
                    check(result.Flags.SetEquals(state.Flags) && result.Times.Count == state.Times.Count,
                        "Deferring political context records an unplayed outcome.");
                    continue;
                }
                check(!Rules.Available(story, scene, result), "Completed political context repeats automatically.");
                if (!privateContact)
                {
                    check(!Rules.Available(story, power, result), "New political predecessor bypasses the future conversation delay.");
                    result.Hour += power.DelayHours;
                    check(Rules.Available(story, power, result), "Completed political conversation strands the ordinary future.");
                }
            }

            foreach (string required in scene.Requires)
            {
                var blocked = Program.Copy(state); blocked.Flags.Remove(required);
                check(!Rules.Available(story, scene, blocked), "Political context ignores contact prerequisite: " + required);
            }
            foreach (string forbidden in scene.Forbids.Append("konomi.closed"))
            {
                var blocked = Program.Copy(state); blocked.Flags.Add(forbidden);
                check(!Rules.Available(story, scene, blocked), "Political context bypasses restriction: " + forbidden);
            }
            var fresh = Program.Copy(state);
            fresh.Times[privateContact ? "konomi.private_returned" : "konomi.return"] = fresh.Hour;
            check(!Rules.Available(story, scene, fresh), "Political context ignores the actual contact timestamp.");
            foreach (int chapter in new[] { 3, 4, 6 })
            {
                var blocked = Program.Copy(state); blocked.Chapter = chapter;
                check(!Rules.Available(story, scene, blocked), "Chapter-five political context is delivered in another chapter.");
            }
            var elsewhere = Program.Copy(state); elsewhere.Area = "elsewhere";
            check(!Rules.Available(story, scene, elsewhere), "Physical political conversation leaves Drezen without delivery support.");
        }
        foreach (var scene in focused.Scenes)
            // The separate missed-contact suite plays every new alternative-history page.
            check(visited[scene.Id].Where(id => !id.StartsWith("missed_", StringComparison.Ordinal)).ToHashSet()
                .SetEquals(scene.Nodes.Where(n => !n.Id.StartsWith("missed_", StringComparison.Ordinal)).Select(n => n.Id)),
                "Political history tests omit an original authored page: " + scene.Id);
    }
}
