using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KianaFollowthroughTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var predecessors = new[] { "guest_table", "market_weather", "lenna_door", "blue_room" }
            .Select(id => story.Scenes.Single(s => s.Id == "kiana." + id)).ToArray();
        var scenes = new[] { "bakery_stairs", "last_page", "first_readers", "ink_after", "working_room", "kept_evening" }
            .Select(id => story.Scenes.Single(s => s.Id == "kiana." + id)).ToArray();
        var milestones = new[] { "bakery_visit_kept", "last_page_kept", "readers_kept", "ink_evening_kept", "workroom_taken", "followthrough_kept" };
        var pairs = new[]
        {
            new[] { "audience", "workshop" }, new[] { "long_speech", "short_speech" },
            new[] { "guest_role", "listens" }, new[] { "heard_readers", "asked_readers" },
            new[] { "quiet_desk", "shared_room" }, new[] { "ink_kiss", "ink_walk" },
            new[] { "waited_page", "stopped_page" }, new[] { "market_morning", "music_wish" },
            new[] { "last_kiss", "last_quiet" }
        }.Select(pair => pair.Select(flag => "kiana.follow_" + flag).ToArray()).ToArray();
        var observed = new HashSet<string>();
        var nativeFlags = story.Etudes.Keys.Concat(story.CompletedQuests.Keys).Concat(story.SeenCues.Keys)
            .Concat(story.SelectedAnswers.Keys).Concat(story.CompletedEtudes.Keys).Distinct().ToArray();

        // Six legitimate relationship histories cover both opening scripts and all three
        // stagecraft histories without multiplying unrelated choices across every scene.
        foreach (var history in new[] { "waited", "affair", "widow" })
        foreach (bool committed in new[] { false, true })
        {
            var initial = new Snapshot { Chapter = 5, Hour = 1000, Area = scenes[0].Areas.Single() };
            initial.Flags.UnionWith(new[] { "seelah.souls_returned", "kiana.lovers", "kiana.morning",
                "seelah.committed", "arueshalae.committed", "loss",
                committed ? "kiana.committed" : "kiana.uncertain", committed ? "kiana.moon" : "kiana.guest" });
            initial.Times["kiana.morning"] = initial.Hour;
            if (history == "widow") initial.Flags.UnionWith(new[] { "kiana.bereaved", "seelah.elan_dead" });
            else initial.Flags.UnionWith(new[] { "kiana.separated", "kiana." + history });
            if (history == "waited") initial.Flags.Add("kiana.quiet_entrance");
            if (history == "affair") initial.Flags.Add("kiana.comic_entrance");

            var social = Program.Copy(initial);
            foreach (var predecessor in predecessors)
            {
                social.Hour += predecessor.DelayHours;
                check(Rules.Available(story, predecessor, social), "Kiana follow-through predecessor unavailable: " + history + "/" + predecessor.Id);
                social = Program.Walk(predecessor, social).First(s => s.Has(predecessor.Id));
            }
            check(social.Has("kiana.roof_supper.kept") && social.Has("kiana.consequences_ready"),
                "Kiana follow-through starts without the played Meral introduction.");

            var states = new List<Snapshot> { social };
            for (int index = 0; index < scenes.Length; index++)
            {
                var scene = scenes[index];
                var continuing = new List<Snapshot>();
                foreach (var input in states)
                {
                    var state = Program.Copy(input);
                    int last = scene.Requires.Where(state.Times.ContainsKey).Select(flag => state.Times[flag]).Max();
                    state.Hour = last + scene.DelayHours - 1;
                    check(!Rules.Available(story, scene, state), "Kiana follow-through starts before its delay: " + scene.Id);
                    state.Hour++;
                    check(Rules.Available(story, scene, state), "Kiana follow-through strands a valid history: " + history + "/" + scene.Id);
                    foreach (var result in Program.Walk(scene, state))
                    {
                        check(result.Flags.IsSupersetOf(state.Flags), "Kiana follow-through removes existing progress.");
                        foreach (string flag in nativeFlags.Concat(new[] { "kiana.committed", "kiana.uncertain", "kiana.separated",
                            "kiana.bereaved", "kiana.waited", "kiana.affair", "seelah.committed", "arueshalae.committed", "loss" }))
                            check(result.Has(flag) == initial.Has(flag), "Kiana follow-through rewrites native/relationship history: " + flag);
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(state.Flags) && result.Times.Count == state.Times.Count &&
                                state.Times.All(pair => result.Times.TryGetValue(pair.Key, out int time) && time == pair.Value),
                                "Kiana deferred event changes progress or its clock: " + scene.Id);
                            check(Rules.Available(story, scene, result), "Kiana deferred event cannot be reopened.");
                            continue;
                        }
                        check(result.Has("kiana." + milestones[index]), "Kiana follow-through completes without its next invitation: " + scene.Id);
                        check(!Rules.Available(story, scene, result), "Kiana follow-through repeats a completed event.");
                        foreach (var pair in pairs)
                            check(pair.Count(result.Has) <= 1, "Kiana follow-through combines incompatible choices: " + pair[0]);
                        observed.UnionWith(result.Flags);
                        continuing.Add(result);
                    }
                }
                check(continuing.Count > 0, "Kiana follow-through has no completing path: " + scene.Id);

                // Preserve every state distinction a later condition reads. Earlier choices
                // with no remaining consumer have already been checked and need not multiply.
                var remainingConditions = scenes.Skip(index + 1).SelectMany(next => next.Requires.Concat(next.Forbids)
                    .Concat(next.Nodes.SelectMany(node => node.Choices.SelectMany(choice => choice.Requires.Concat(choice.Forbids)))))
                    .Distinct().OrderBy(flag => flag).ToArray();
                states = continuing.GroupBy(state => string.Join("|", remainingConditions.Where(state.Has)))
                    .Select(group => group.First()).ToList();
            }
            check(states.All(state => state.Has("kiana.followthrough_kept")), "Kiana follow-through does not reach its kept evening.");
        }
        foreach (string flag in pairs.SelectMany(pair => pair))
            check(observed.Contains(flag), "Kiana follow-through lost an activity or intimacy option: " + flag);
        check(scenes.Last().DelayHours >= 168, "Kiana follow-through reports two working afternoons before its planned week.");

        foreach (var scene in scenes)
        {
            check(scene.Nodes.Skip(1).All(node => node.Choices.All(choice => !choice.Abort)),
                "Kiana follow-through can abort after writing partial choices: " + scene.Id);
            check(scene.Nodes[0].Choices.Any(choice => choice.Abort && choice.Set.Length == 0),
                "Kiana follow-through lacks an initial deferral without progress.");
            var ready = new Snapshot { Chapter = 5, Hour = 1000, Area = scene.Areas.Single() };
            ready.Flags.UnionWith(Program.Prerequisites(scene));
            check(Rules.Available(story, scene, ready), "Kiana follow-through eligibility fixture is not ready.");
            foreach (string blocker in new[] { "kiana.closed", "kiana.farewell", "inhuman" })
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                check(!Rules.Available(story, scene, blocked), "Kiana follow-through ignores " + blocker);
            }
            foreach (string required in scene.Requires.Distinct())
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(required);
                check(!Rules.Available(story, scene, missing), "Kiana follow-through skips " + required);
            }
            foreach (var group in scene.RequiresAnyGroups)
            {
                var missing = Program.Copy(ready); missing.Flags.ExceptWith(group);
                check(!Rules.Available(story, scene, missing), "Kiana follow-through skips " + string.Join("|", group));
            }
            foreach (int chapter in new[] { 1, 3, 4, 6 })
            {
                var wrongChapter = Program.Copy(ready); wrongChapter.Chapter = chapter;
                check(!Rules.Available(story, scene, wrongChapter), "Kiana follow-through ignores chapter 5 restriction.");
            }
            ready.Area = "elsewhere";
            check(!Rules.Available(story, scene, ready), "Kiana follow-through ignores its Drezen location.");
        }
    }
}
