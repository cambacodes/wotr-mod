using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class SoanaContinuationTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string actor = "64805abb52739e44280a758f850b300c";
        var opening = new[] { "threshold", "water_carrier", "guardian_question" }
            .Select(id => story.Scenes.Single(s => s.Id == "soana." + id)).ToArray();
        var scenes = new[] { "one_account", "watch_line", "price_of_warning", "ordinary_feast", "name_between", "lower_bend" }
            .Select(id => story.Scenes.Single(s => s.Id == "soana." + id)).ToArray();
        var native = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).Distinct().ToArray();
        var exclusive = new[]
        {
            new[] { "watch_found", "watch_missed", "watch_patient" },
            new[] { "line_high", "line_daywatch" },
            new[] { "watch_near_cave", "watch_removed" },
            new[] { "courtship_chosen", "friendship_chosen", "courtship_waiting" },
            new[] { "first_kiss", "bend_hand", "friendship_kept", "pace_unresolved", "slow_courtship" }
        }.Select(group => group.Select(f => "soana." + f).ToArray()).ToArray();
        var replayCases = new Dictionary<string, (Scene Scene, Snapshot State)>();
        var reached = new HashSet<string>();
        var outcomes = new HashSet<string>();
        foreach (string history in new[] { "old_defender", "bear_dead", "both" })
        foreach (bool attracted in new[] { false, true })
        {
            var initial = new Snapshot { Chapter = 3, Hour = 1000 };
            initial.AvailableContacts.Add(actor);
            initial.Flags.UnionWith(new[] { "soana.after_quest", "seelah.committed", "kiana.committed" });
            if (history != "bear_dead") initial.Flags.Add("soana.old_defender");
            if (history != "old_defender") initial.Flags.Add("soana.bear_dead");
            var state = initial;
            foreach (var prior in opening)
            {
                state.Hour += 24;
                check(Program.CurrentAvailable(story, prior, state), "Soana actual opening cannot enter " + prior.Id);
                state = Program.Walk(prior, state).First(s => s.Has(prior.Id) && !s.Has("soana.closed")
                    && (prior.Id != "soana.water_carrier" || s.Has("soana.attraction_named") == attracted));
            }
            var states = new List<Snapshot> { state };
            foreach (var scene in scenes)
            {
                var next = new Dictionary<string, Snapshot>();
                foreach (var input in states)
                {
                    var ready = Program.Copy(input); ready.Hour += 24;
                    check(Program.CurrentAvailable(story, scene, ready), "Soana continuing chain cannot enter " + scene.Id);
                    foreach (var result in Program.Walk(scene, ready, (node, snapshot) =>
                    {
                        reached.Add(scene.Id + "/" + node);
                        if (!snapshot.Has("soana.closed"))
                        {
                            var localEffects = scene.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Set).ToHashSet();
                            string replayKey = scene.Id + "/" + node + "/" + history + "/"
                                + string.Join(",", exclusive.SelectMany(g => g).Where(f => localEffects.Contains(f) && snapshot.Has(f)));
                            replayCases.TryAdd(replayKey, (scene, Program.Copy(snapshot)));
                        }
                        if (node == "bound") check(!snapshot.Has("soana.bear_dead"), "Dead bear enters a living-bear conversation.");
                        if (node == "dead") check(snapshot.Has("soana.bear_dead"), "Living bear enters a dead-bear conversation.");
                    }))
                    {
                        foreach (string flag in native.Concat(new[] { "seelah.committed", "kiana.committed", "soana.lovers", "soana.committed" }))
                            check(result.Has(flag) == initial.Has(flag), "Soana continuation rewrites native or unrelated history: " + flag);
                        check(result.AvailableContacts.SetEquals(initial.AvailableContacts), "Soana continuation invents physical contact.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags), "A Soana postponement changes progress.");
                            check(result.Times.Count == ready.Times.Count && result.Times.All(p => ready.Times.TryGetValue(p.Key, out int hour) && hour == p.Value), "A postponed Soana scene changes timestamps.");
                            continue;
                        }
                        check(!Program.CurrentAvailable(story, scene, result), "Soana completed scene repeats.");
                        if (result.Has("soana.closed"))
                        {
                            check(Rules.ContactAvailable(story, scene, result), "Authored Soana goodbye cannot finish after closing the route.");
                            outcomes.Add("closed");
                            continue;
                        }
                        if (result.Has("soana.watch_kept"))
                        {
                            check(result.Has("soana.line_high") != result.Has("soana.line_daywatch"), "Soana warning configurations overlap.");
                            check(new[] { "watch_found", "watch_missed", "watch_patient" }.Count(f => result.Has("soana." + f)) == 1, "Watch result does not distinguish skill success, failure and patience.");
                        }
                        if (result.Has("soana.warning_reckoned"))
                            check(result.Has("soana.watch_near_cave") != result.Has("soana.watch_removed"), "Warning consequence loses the chosen disposition.");
                        if (result.Has("soana.present_named"))
                            check(new[] { "courtship_chosen", "friendship_chosen", "courtship_waiting" }.Count(f => result.Has("soana." + f)) == 1, "Soana relationship pace overlaps.");
                        if (result.Has("soana.continuation_kept"))
                        {
                            var endings = new[] { "first_kiss", "bend_hand", "friendship_kept", "pace_unresolved", "slow_courtship" };
                            check(endings.Count(f => result.Has("soana." + f)) == 1, "Soana final afternoon has contradictory intimacy outcomes.");
                            foreach (string ending in endings.Where(f => result.Has("soana." + f))) outcomes.Add(ending);
                            check(!result.Has("soana.first_kiss") || result.Has("soana.courtship_chosen"), "Friendship or waiting acquires a kiss.");
                            check(result.Has("soana.friendship_kept") == result.Has("soana.friendship_chosen"), "Soana friendship is silently converted to romance.");
                            check(result.Has("soana.pace_unresolved") == result.Has("soana.courtship_waiting"), "Waiting receives an invented romantic decision.");
                        }
                        next[string.Join("|", result.Flags.OrderBy(f => f))] = result;
                    }
                }
                check(next.Count > 0, "Soana continuation has no completed nonclosure path.");
                states = next.Values.ToList();
            }
        }
        check(outcomes.SetEquals(new[] { "closed", "first_kiss", "bend_hand", "friendship_kept", "pace_unresolved", "slow_courtship" }), "Soana continuation traversal misses an ending.");
        foreach (var scene in scenes)
        {
            foreach (var node in scene.Nodes.Where(n => !n.Id.Contains("_r3_", StringComparison.Ordinal)
                && n.Id != "round2_affair" && n.Id != "delivered"
                && !(n.Id.Contains(".explicit.", StringComparison.Ordinal) && scene.Nodes.Any(p => p.Id.StartsWith("quiet_r3_", StringComparison.Ordinal) && p.Choices.Any(a => a.Next == n.Id)))))
                check(reached.Contains(scene.Id + "/" + node.Id), "Soana page not reached by the actual chain: " + scene.Id + "/" + node.Id);
            check(scene.ContactUnit == actor && !Rules.IsRemote(scene), "Soana continuation bypasses physical native contact.");
            check(Rules.EntryTargets(scene).SequenceEqual(new[] { "2b1776f3e398685479ff6b16290b4cc2" }), "Soana continuation changes native entry target.");
            check(scene.MinChapter == 3 && scene.MaxChapter == 3 && scene.Chapters.SequenceEqual(new[] { 3 }), "Soana invents late-campaign contact.");
            check(scene.RequiresAny.ToHashSet().SetEquals(new[] { "soana.old_defender", "soana.bear_dead" }), "Soana continuation changes supported native outcomes.");
            var ready = new Snapshot { Chapter = 3, Hour = 1000 };
            ready.Flags.UnionWith(scene.Requires); ready.Flags.Add("soana.old_defender"); ready.AvailableContacts.Add(actor);
            check(Program.CurrentAvailable(story, scene, ready), "Soana gate baseline is invalid.");
            foreach (string blocker in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                check(!Program.CurrentAvailable(story, scene, blocked), "Soana ignores blocker " + blocker);
                if (story.Relationships["soana"].UnavailableFlags.Contains(blocker))
                    check(!Rules.ContactAvailable(story, scene, blocked), "Soana resumed scene ignores native loss " + blocker);
            }
            foreach (string required in scene.Requires.Where(requiredKey => !requiredKey.EndsWith(".present_now", StringComparison.Ordinal) && !requiredKey.EndsWith(".reachable_by_letter", StringComparison.Ordinal)))
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(required);
                check(!Program.CurrentAvailable(story, scene, missing) && !Rules.ContactAvailable(story, scene, missing), "Soana skips prerequisite " + required);
            }
            var absent = Program.Copy(ready); absent.AvailableContacts.Clear(); absent.Flags.Add(actor); absent.Flags.Add("soana.contact_available");
            check(!Program.CurrentAvailable(story, scene, absent) && !Rules.ContactAvailable(story, scene, absent), "Authored flag bypasses live Soana contact.");
            absent = Program.Copy(ready); absent.Flags.Remove("soana.old_defender");
            check(!Program.CurrentAvailable(story, scene, absent) && !Rules.ContactAvailable(story, scene, absent), "Soana ignores loss of native outcome.");
            foreach (int chapter in new[] { 2, 4, 5 })
            {
                var wrong = Program.Copy(ready); wrong.Chapter = chapter;
                check(!Program.CurrentAvailable(story, scene, wrong) && !Rules.ContactAvailable(story, scene, wrong), "Soana contact escapes chapter 3.");
            }
            ready.Times[scene.Requires.Last()] = ready.Hour;
            check(Rules.ContactAvailable(story, scene, ready), "Resumed Soana scene reapplies delay.");
            ready.Hour += 23; check(!Program.CurrentAvailable(story, scene, ready), "Soana skips visit delay.");
            ready.Hour++; check(Program.CurrentAvailable(story, scene, ready), "Soana misses exact 24-hour boundary.");
        }
        foreach (var example in replayCases.Values)
        {
            var interrupted = Program.Copy(example.State);
            interrupted.AvailableContacts.Remove(actor);
            check(!Rules.ContactAvailable(story, example.Scene, interrupted), "Interrupted Soana dialog ignores lost actor.");
            interrupted.AvailableContacts.Add(actor);
            interrupted.Hour += 24;
            check(Program.CurrentAvailable(story, example.Scene, interrupted), "Interrupted Soana visit cannot reopen after contact returns.");
            foreach (var result in Program.Walk(example.Scene, interrupted))
            {
                foreach (var group in exclusive)
                {
                    check(group.Count(result.Has) <= 1, "Interrupted Soana replay accumulates incompatible outcomes: " + example.Scene.Id);
                    foreach (string flag in group.Where(interrupted.Has))
                        check(result.Has(flag), "Soana replay erases an earlier selected outcome.");
                }
                if (result.Has("soana.friendship_chosen") || result.Has("soana.courtship_waiting"))
                    check(!result.Has("soana.first_kiss"), "Soana replay buys a kiss after choosing friendship or waiting.");
            }
        }
        var skill = scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Single(c => c.Check != null).Check!;
        check(skill.Skill == "SkillPerception" && skill.DC == 22 && skill.CommanderOnly && skill.Success == "found" && skill.Failure == "missed", "Soana observation check changes its reviewed contract.");
    }
}
