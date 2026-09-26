using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class ArankaContinuationTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        string[] ids = { "the_wrong_refrain", "where_the_breath_goes", "the_name_missing",
            "an_evening_uncommanded", "the_song_afterwards", "no_encore_needed" };
        var scenes = ids.Select(id => story.Scenes.Single(s => s.Id == "aranka." + id)).ToArray();
        const string actor = "430cba7801b149b4e8494ace6baf4f7c";
        const string area = "31bab5549f7ea384186159a238360c8d";
        var seen = scenes.ToDictionary(s => s.Id, _ => new HashSet<string>());
        var parent = story.Etudes.Keys.Concat(story.CompletedQuests.Keys).Concat(story.CompletedEtudes.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();
        check(story.Etudes["aranka.ran_romance"] == "2e98dbe685f045cdabf88b66e4cde9ff", "Aranka needs the existing Playing romance.");
        check(story.Etudes["aranka.ran_reverie_partner"] == "d4dd8a50613e4d528913d0a24d06fca1", "Reverie history uses the wrong parent state.");
        check(story.CompletedQuests["aranka.ran_quest_complete"] == "1dacd3dfe1bf47c8a73074814e40b1c8", "Aranka ignores successful parent completion.");
        check(story.SeenCues["aranka.ran_keep_final"].ToHashSet().SetEquals(new[] { "a16f4be6de0a4f35a9b13eca4395d6e5",
            "61461d05999b46218e7700e6596243b5", "363860bffda1404db6ec996384fe2f26", "43936228f4614272a7c7e25ebaaec2c7" }), "Aranka misses an ordinary or Azata parent finale.");
        check(story.SeenCues["aranka.ran_wing_dream"].ToHashSet().SetEquals(story.SeenCues["aranka.ran_keep_final"].Skip(1)),
            "Aranka wing memory uses an unearned or non-wing ending.");
        check(story.SeenCues["aranka.ran_release_final"].ToHashSet().SetEquals(new[] {
            "599e7c0cc51741cda1bc55b787734c57", "fefc9911dde04a76975e9027118c7935",
            "f9df40d7d6b346298075b435eee6921c", "e16e5b0b3aea426a888e8bb61c521815" }), "Aranka relinquished-artifact endings are incomplete.");
        check(!scenes.Any(s => s.Requires.Contains("aranka.ran_warden")), "Aranka depends on an unverified Warden producer.");

        // Parent checkpoint histories are seeded from the independently traced native actions.
        // Walking these scenes does not simulate or certify playing RanRomance inside Unity.
        foreach (string history in new[] { "keep", "wing", "release", "overlap" })
        foreach (bool reverie in new[] { false, true })
        {
            var initial = new Snapshot { Chapter = 5, Area = area, Hour = 1000 };
            initial.AvailableContacts.Add(actor);
            initial.Flags.UnionWith(new[] { "aranka.ran_romance", "aranka.ran_quest_complete", "azata", "seelah.committed", "arueshalae.committed" });
            if (history != "release") initial.Flags.Add("aranka.ran_keep_final");
            if (history == "release" || history == "overlap") initial.Flags.Add("aranka.ran_release_final");
            if (history == "wing") initial.Flags.Add("aranka.ran_wing_dream");
            if (reverie) initial.Flags.Add("aranka.ran_reverie_partner");
            var states = new List<Snapshot> { initial };
            foreach (var scene in scenes)
            {
                var next = new List<Snapshot>();
                foreach (var before in states)
                {
                    var ready = Program.Copy(before);
                    if (scene != scenes[0])
                    {
                        check(!Rules.Available(story, scene, ready), "Aranka skips the interval between visits.");
                        ready.Hour += scene.DelayHours;
                    }
                    check(Rules.Available(story, scene, ready), "Earned Aranka history cannot enter " + scene.Id);
                    foreach (var result in Program.Walk(scene, ready, (node, partial) =>
                    {
                        seen[scene.Id].Add(node);
                        check(partial.Flags.SetEquals(ready.Flags), "Interrupted Aranka trial commits an intermediate result.");
                        if (node == "keeper") check(history == "keep" || history == "wing", "Relinquished compass silently grants dream access.");
                        if (node == "traveler") check(history == "release" || history == "overlap", "Kept compass is falsely described as surrendered.");
                        if (node == "flight") check(history == "wing", "Aranka recalls an unearned wing dream.");
                        if (node == "reverie") check(reverie && (history == "keep" || history == "wing"), "Shared partner appears without actual supported parent history.");
                        check(Rules.ContactAvailable(story, scene, partial), "Normal Aranka continuation loses contact.");
                        var gone = Program.Copy(partial); gone.AvailableContacts.Clear();
                        check(!Rules.ContactAvailable(story, scene, gone), "Midscene Aranka disappearance is ignored.");
                        var ended = Program.Copy(partial); ended.Flags.Remove("aranka.ran_romance");
                        check(!Rules.ContactAvailable(story, scene, ended), "Parent relationship can end during the extension without stopping contact.");
                    }))
                    {
                        check(ready.Flags.IsSubsetOf(result.Flags), "Aranka deletes pre-existing history.");
                        check(parent.All(f => ready.Has(f) == result.Has(f)), "Aranka changes a native or parent predicate.");
                        check(result.Has("seelah.committed") && result.Has("arueshalae.committed"), "Aranka interferes with concurrent romances.");
                        check(result.AvailableContacts.SetEquals(ready.AvailableContacts), "Aranka invents an actor or a pet.");
                        foreach (var group in new[] {
                            new[] { "open_circle", "rounds" }, new[] { "timing_heard", "timing_missed", "timing_patient" },
                            new[] { "sings_line", "listens_close" }, new[] { "ending_door", "ending_answers" },
                            new[] { "crowd_welcomed", "crowd_ceremony", "crowd_listened" },
                            new[] { "future_road", "future_meetings" }, new[] { "extension_night", "extension_kiss", "extension_quiet" } })
                            check(group.Count(f => result.Has("aranka." + f)) <= 1, "Aranka combines mutually exclusive played results.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags), "Postponing Aranka records progress.");
                            continue;
                        }
                        check(!Rules.Available(story, scene, result), "Completed Aranka scene replays.");
                        next.Add(result);
                    }
                }
                states = next.GroupBy(s => string.Join("|", s.Flags.OrderBy(f => f))).Select(g => g.First()).ToList();
                check(states.Count > 0, "Aranka loses every continuing played history.");
            }
            check(states.All(s => s.Has("aranka.extension_kept")), "Aranka lacks a played extension ending.");
            foreach (string ending in new[] { "extension_night", "extension_kiss", "extension_quiet" })
                check(states.Any(s => s.Has("aranka." + ending)), "Aranka forces a single intimacy pace.");
            check(states.Any(s => s.Has("aranka.timing_missed") && s.Has("aranka.crowd_ceremony") && s.Has("aranka.extension_night")),
                "Failing both musical trials accidentally loses the established romance.");
        }

        foreach (var scene in scenes)
        {
            check(seen[scene.Id].SetEquals(scene.Nodes.Select(n => n.Id)), "Unreachable Aranka prose: " + scene.Id);
            check(scene.ContactUnit == actor && scene.Areas.SequenceEqual(new[] { area }) && scene.Chapters.SequenceEqual(new[] { 5 }), "Aranka claims unsupported native contact.");
            check(scene.AnswerLists.SequenceEqual(new[] { "5ff8a80442182f84e849b4281f98b9ca" }), "Aranka attaches to the wrong native conversation.");
            check(!Rules.IsRemote(scene), "Waking island meeting silently becomes dream correspondence.");
            var ready = new Snapshot { Chapter = 5, Area = area, Hour = 1000 };
            ready.AvailableContacts.Add(actor); ready.Flags.UnionWith(scene.Requires); ready.Flags.Add("aranka.ran_keep_final");
            check(Rules.Available(story, scene, ready), "Aranka baseline gate invalid.");
            foreach (string required in scene.Requires)
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(required);
                check(!Rules.Available(story, scene, missing), "Aranka skips prerequisite " + required);
            }
            foreach (string forbidden in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(forbidden);
                check(!Rules.Available(story, scene, blocked), "Aranka ignores blocked history " + forbidden);
            }
            var noFinal = Program.Copy(ready); noFinal.Flags.Remove("aranka.ran_keep_final");
            check(!Rules.Available(story, scene, noFinal), "Completed quest alone fabricates a parent finale.");
            var noRomance = Program.Copy(ready); noRomance.Flags.Remove("aranka.ran_romance");
            noRomance.Flags.UnionWith(new[] { "aranka.flirt", "aranka.active", "aranka.ran_reverie_partner" });
            check(!Rules.Available(story, scene, noRomance), "Flirt, active or another partner duplicates Aranka acquisition.");
            foreach (int chapter in new[] { 3, 4, 6 })
            {
                var wrong = Program.Copy(ready); wrong.Chapter = chapter;
                check(!Rules.Available(story, scene, wrong), "Aranka ignores actual parent finale timeline.");
            }
            foreach (string place in new[] { "", "2570015799edf594daf2f076f2f975d8" })
            {
                var wrong = Program.Copy(ready); wrong.Area = place;
                check(!Rules.Available(story, scene, wrong), "Aranka invents repeatable Drezen presence.");
            }
            var absent = Program.Copy(ready); absent.AvailableContacts.Clear(); absent.Flags.Add("trickster");
            check(!Rules.Available(story, scene, absent), "Trickster flag fabricates unavailable Aranka contact.");
            check(scene.Nodes.SelectMany(n => n.Choices).All(c => c.Revive == null), "Aranka continuation secretly restores a native actor.");
        }
        var checks = scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Where(c => c.Check != null).Select(c => c.Check!).ToArray();
        check(checks.Length == 2 && checks.All(c => c.CommanderOnly), "Aranka's two played checks were replaced or delegated.");
        check(checks.Any(c => c.Skill == "SkillPerception" && c.DC == 26) && checks.Any(c => c.Skill == "CheckDiplomacy" && c.DC == 25),
            "Aranka check mechanics do not match the presented musical problems.");
    }
}
