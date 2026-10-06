using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class SoanaOpeningTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var scenes = new[] { "threshold", "water_carrier", "guardian_question" }
            .Select(id => story.Scenes.Single(s => s.Id == "soana." + id)).ToArray();
        const string contact = "64805abb52739e44280a758f850b300c";
        var nativeFlags = new[] { "soana.after_quest", "soana.old_defender", "soana.bear_dead" };
        var reached = new HashSet<string>();
        foreach (string history in new[] { "old_defender", "bear_dead", "both" })
        {
            var initial = new Snapshot { Chapter = 3, Hour = 1000 };
            initial.Flags.UnionWith(new[] { "soana.after_quest", "seelah.committed", "konomi.committed" });
            if (history != "bear_dead") initial.Flags.Add("soana.old_defender");
            if (history != "old_defender") initial.Flags.Add("soana.bear_dead");
            initial.AvailableContacts.Add(contact);
            var states = new List<Snapshot> { initial };
            foreach (var scene in scenes)
            {
                var continuing = new List<Snapshot>();
                foreach (var input in states)
                {
                    var state = Program.Copy(input);
                    state.Hour += scene.DelayHours;
                    check(Program.CurrentAvailable(story, scene, state), "Soana valid history cannot continue: " + history + "/" + scene.Id);
                    var absent = Program.Copy(state);
                    absent.AvailableContacts.Remove(contact);
                    check(!Program.CurrentAvailable(story, scene, absent), "Soana remains available after native contact disappears: " + scene.Id);
                    check(!Rules.ContactAvailable(story, scene, absent), "Soana resumed dialog ignores vanished contact.");
                    foreach (var result in Program.Walk(scene, state))
                    {
                        foreach (string flag in nativeFlags.Concat(new[] { "seelah.committed", "konomi.committed" }))
                            check(result.Has(flag) == initial.Has(flag), "Soana rewrites native history or another romance: " + flag);
                        check(result.AvailableContacts.SetEquals(initial.AvailableContacts), "Soana dialog fabricates native contact availability.");
                        check(!result.Has("soana.lovers") && !result.Has("soana.committed"), "Soana opening invents a completed romance.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(state.Flags), "Soana deferred entry writes progress.");
                            check(result.Times.Count == state.Times.Count && result.Times.All(p => state.Times.TryGetValue(p.Key, out int hour) && hour == p.Value), "Soana deferred entry changes timestamps.");
                            continue;
                        }
                        check(!Program.CurrentAvailable(story, scene, result), "Soana repeats a completed visit.");
                        check(result.Has("soana.fox_waited") != result.Has("soana.fox_held"), "Soana loses the selected fox rescue method.");
                        check(result.Has("soana.fox_held") == (result.Has("soana.fox_reconsidered") != result.Has("soana.fox_expedience")), "Soana loses the held-fox response.");
                        check(!result.Has("soana.fox_waited") || (!result.Has("soana.fox_reconsidered") && !result.Has("soana.fox_expedience")), "Soana waiting history invents a held-fox consequence.");
                        check(!result.Has("soana.reeds_promised") || result.Has("soana.fox_waited"), "Soana promises reeds on the wrong fox history.");
                        if (scene.Id != "soana.threshold")
                        {
                            check(result.Has("soana.accepted_guidance") != result.Has("soana.tried_weave"), "Soana weaving loses player participation.");
                            check(result.Has("soana.marriage_acknowledged"), "Soana skips acknowledging her existing marriage.");
                            check(!result.Has("soana.flower_thanks") || !result.Has("soana.attraction_named"), "Soana turns a thanks-only flower into declared attraction.");
                        }
                        if (scene.Id == "soana.guardian_question")
                        {
                            check(result.Has("soana.orso_dead_discussed") == initial.Has("soana.bear_dead"), "Soana fails to prioritize the dead-bear outcome.");
                            check(result.Has("soana.orso_bound_discussed") == !initial.Has("soana.bear_dead"), "Soana invents a living bound guardian.");
                            check(result.Has("soana.opening_kept") == !result.Has("soana.closed") && result.Has("soana.inquiry_invited") == !result.Has("soana.closed"), "Soana closure awards an unoffered continuation.");
                            foreach (string flag in new[] { "soana.closed", "soana.seeks_alternative", "soana.accepts_hardship", "soana.fox_waited", "soana.fox_reconsidered", "soana.fox_expedience" })
                                if (result.Has(flag)) reached.Add(flag);
                            if (result.Has("soana.closed"))
                                check(Rules.ContactAvailable(story, scene, result), "Soana cannot finish her authored goodbye after closure.");
                        }
                        continuing.Add(result);
                    }
                }
                check(continuing.Count > 0, "Soana scene has no completed path.");
                states = continuing;
            }
        }
        check(reached.SetEquals(new[] { "soana.closed", "soana.seeks_alternative", "soana.accepts_hardship", "soana.fox_waited", "soana.fox_reconsidered", "soana.fox_expedience" }), "Soana traversal misses a guardian response or fox history.");
        foreach (var scene in scenes)
        {
            check(scene.ContactUnit == contact && !scene.Remote, "Soana opening loses its native in-person contact gate.");
            check(scene.RequiresAny.ToHashSet().SetEquals(new[] { "soana.old_defender", "soana.bear_dead" }), "Soana opening accepts an unreviewed native outcome.");
            var ready = new Snapshot { Chapter = 3, Hour = 1000 };
            ready.Flags.UnionWith(scene.Requires);
            ready.Flags.Add("soana.old_defender");
            ready.AvailableContacts.Add(contact);
            check(Program.CurrentAvailable(story, scene, ready), "Soana availability baseline is invalid.");
            check(Rules.ContactAvailable(story, scene, ready), "Soana resumed contact baseline is invalid.");
            foreach (string blocker in new[] { "soana.closed", "soana.dead", "soana.killed_by_camellia", "soana.forest_dead", "inhuman" })
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                check(!Program.CurrentAvailable(story, scene, blocked), "Soana ignores " + blocker);
                if (story.Relationships[scene.Relationship].UnavailableFlags.Contains(blocker))
                    check(!Rules.ContactAvailable(story, scene, blocked), "Soana resumed dialog ignores native unavailability: " + blocker);
            }
            foreach (string required in scene.Requires.Where(requiredKey => !requiredKey.EndsWith(".present_now", StringComparison.Ordinal) && !requiredKey.EndsWith(".reachable_by_letter", StringComparison.Ordinal)))
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(required);
                check(!Program.CurrentAvailable(story, scene, missing), "Soana skips prerequisite " + required);
                check(!Rules.ContactAvailable(story, scene, missing), "Soana resumed dialog ignores lost prerequisite: " + required);
            }
            var noOutcome = Program.Copy(ready); noOutcome.Flags.Remove("soana.old_defender");
            check(!Program.CurrentAvailable(story, scene, noOutcome), "Soana appears without a supported native outcome.");
            check(!Rules.ContactAvailable(story, scene, noOutcome), "Soana resumed dialog ignores lost native outcome.");
            var noContact = Program.Copy(ready); noContact.AvailableContacts.Clear();
            check(!Program.CurrentAvailable(story, scene, noContact), "Soana appears without the native speaker.");
            noContact.Flags.Add(contact);
            noContact.Flags.Add("soana.contact_available");
            noContact.AvailableContacts.Add("unrelated-unit");
            check(!Program.CurrentAvailable(story, scene, noContact), "Authored flags or another unit bypass Soana's contact gate.");
            check(!Rules.ContactAvailable(story, scene, noContact), "Authored flags bypass resumed Soana contact checks.");
            foreach (int chapter in new[] { 1, 2, 4, 5 })
            {
                var wrongChapter = Program.Copy(ready); wrongChapter.Chapter = chapter;
                check(!Program.CurrentAvailable(story, scene, wrongChapter), "Soana chapter-three opening appears in chapter " + chapter);
                check(!Rules.ContactAvailable(story, scene, wrongChapter), "Soana resumed dialog ignores changed chapter.");
            }
            check(scene.DelayHours == (scene.Id == "soana.threshold" ? 0 : 24), "Soana visit delay changed without review.");
            if (scene.DelayHours > 0)
            {
                ready.Times[scene.Requires.Last()] = ready.Hour;
                check(Rules.ContactAvailable(story, scene, ready), "Soana resumed dialog incorrectly reapplies entry delay after timestamp changes.");
                ready.Hour += scene.DelayHours - 1;
                check(!Program.CurrentAvailable(story, scene, ready), "Soana skips the interval between visits.");
                ready.Hour++;
                check(Program.CurrentAvailable(story, scene, ready), "Soana misses the exact visit delay boundary.");
            }
        }
    }
}
