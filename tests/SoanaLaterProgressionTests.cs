using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class SoanaLaterProgressionTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string actor = "64805abb52739e44280a758f850b300c";
        var oldIds = new[] { "threshold", "water_carrier", "guardian_question", "one_account", "watch_line", "price_of_warning", "ordinary_feast", "name_between", "lower_bend" };
        var ids = new[] { "the_thing_in_the_sack", "the_dry_offering", "the_inherited_debt", "a_voice_in_the_dark", "what_followed_home", "a_promise_still_spoken", "the_unwelcome_path", "after_the_last_visitor" };
        var scenes = ids.Select(id => story.Scenes.Single(s => s.Id == "soana." + id)).ToArray();
        var native = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).Distinct().ToArray();
        var reached = new HashSet<string>();
        var endings = new HashSet<string>();
        foreach (var history in new[] { "bound", "dead", "overlap" })
        foreach (var oldEnding in new[] { "first_kiss", "bend_hand", "slow_courtship", "friendship_kept", "pace_unresolved" })
        {
            string intention = oldEnding == "friendship_kept" ? "friendship_chosen" : oldEnding == "pace_unresolved" ? "courtship_waiting" : "courtship_chosen";
            var initial = new Snapshot { Chapter = 3, Hour = 1000 };
            initial.Flags.UnionWith(new[] { "soana.after_quest", "trickster", "seelah.committed", "committed" });
            if (history != "dead") initial.Flags.Add("soana.old_defender");
            if (history != "bound") initial.Flags.Add("soana.bear_dead");
            initial.AvailableContacts.Add(actor);
            var earned = Program.Copy(initial);
            foreach (var id in oldIds)
            {
                var predecessor = story.Scenes.Single(s => s.Id == "soana." + id);
                earned.Hour += predecessor.DelayHours;
                check(Program.CurrentAvailable(story, predecessor, earned), "Actual Soana predecessor unavailable: " + id);
                earned = Program.Walk(predecessor, earned).First(result => result.Has(predecessor.Id) && !result.Has("soana.closed")
                    && (id != "name_between" || result.Has("soana." + intention))
                    && (id != "lower_bend" || result.Has("soana." + oldEnding)));
            }
            check(earned.Has("soana.continuation_kept"), "Soana later route has no played predecessor.");
            var states = new List<Snapshot> { earned };
            foreach (var scene in scenes)
            {
                bool awaitingPartner = scene.Id == "soana.after_the_last_visitor"
                    && states.All(s => s.Has("soana.later_courting") && !s.Has("soana.round2.partner_answer"));
                var next = new List<Snapshot>();
                foreach (var input in states)
                {
                    var ready = Program.Copy(input); ready.Hour += scene.DelayHours;
                    check(Program.CurrentAvailable(story, scene, ready), "Earned Soana later chain cannot continue: " + scene.Id);
                    var early = Program.Copy(ready); early.Hour--;
                    check(!Program.CurrentAvailable(story, scene, early), "Soana later delay boundary ignored.");
                    foreach (var result in Program.Walk(scene, ready, (page, state) =>
                    {
                        reached.Add(scene.Id + "/" + page);
                        check(state.Flags.SetEquals(ready.Flags), "Soana partial later visit commits an unplayed consequence.");
                        check(Program.CurrentAvailable(story, scene, state), "Soana partial later visit cannot replay.");
                        var absent = Program.Copy(state); absent.AvailableContacts.Clear();
                        check(!Rules.ContactAvailable(story, scene, absent), "Soana later visit continues without actor.");
                        foreach (var loss in story.Relationships["soana"].UnavailableFlags)
                        {
                            var blocked = Program.Copy(state); blocked.Flags.Add(loss);
                            check(!Rules.ContactAvailable(story, scene, blocked), "Soana later visit ignores native loss: " + loss);
                        }
                        if (page == "bound") check(!state.Has("soana.bear_dead"), "Soana later text revives dead bear.");
                        if (page == "dead") check(state.Has("soana.bear_dead"), "Soana later text kills living bear.");
                        if (scene.Id == "soana.what_followed_home")
                        {
                            if (page == "voice") check(state.Has("soana.voice_carried"), "Soana invents endured voice cost.");
                            if (page == "interrupted") check(state.Has("soana.voice_interrupted"), "Soana invents overridden choice.");
                            if (page == "lost") check(state.Has("soana.ridge_used"), "Soana confuses planned and fallback destruction.");
                        }
                        if (scene.Id == "soana.after_the_last_visitor" && new[] { "desire", "night", "kiss", "quiet" }.Contains(page))
                            check(state.Has("soana.later_courting") && !state.Has("soana.later_friends"), "Soana friendship escalates without chosen courtship.");
                    }))
                    {
                        check(earned.Flags.All(result.Has), "Soana later route erases an existing decision.");
                        foreach (var flag in native.Concat(new[] { "soana.committed", "seelah.committed", "committed" }))
                            check(result.Has(flag) == initial.Has(flag), "Soana later route rewrites native or other relationship state: " + flag);
                        check(result.AvailableContacts.SetEquals(initial.AvailableContacts), "Soana later route fabricates an actor.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags), "Soana postponement writes progression.");
                            continue;
                        }
                        check(!Program.CurrentAvailable(story, scene, result), "Soana completed later visit repeats.");
                        foreach (var group in new[] {
                            new[] { "rite_voice", "rite_ridge" }, new[] { "nursery_saved", "nursery_lost" },
                            new[] { "voice_carried", "voice_interrupted", "ridge_used" },
                            new[] { "later_courting", "later_friends" }, new[] { "path_cleft", "path_flood" },
                            new[] { "later_night", "later_kiss", "later_quiet", "later_friend_evening" } })
                            check(group.Count(f => result.Has("soana." + f)) <= 1, "Soana later mutually exclusive consequences overlap.");
                        if (result.Has("soana.promise_spoken") && intention == "friendship_chosen")
                            check(result.Has("soana.later_friends") && !result.Has("soana.later_courting"), "Soana rejected romance silently returns.");
                        if (result.Has("soana.progression_kept"))
                        {
                            check(result.Has("soana.lovers") == result.Has("soana.later_night"), "Soana night outcome recorded before voluntary intimacy.");
                            endings.UnionWith(result.Flags.Where(f => f.StartsWith("soana.later_", StringComparison.Ordinal)));
                        }
                        next.Add(result);
                    }
                }
                states = next.GroupBy(s => string.Join("|", s.Flags.OrderBy(f => f))).Select(g => g.First()).ToList();
                check(states.Count > 0 || awaitingPartner, "Soana later scene lacks a completed path.");
            }
        }
        foreach (var scene in scenes)
        {
            foreach (var page in scene.Nodes.Where(n => !n.Id.Contains("_r3_", StringComparison.Ordinal)
                && n.Id != "round2_affair" && n.Id != "delivered"
                && !(n.Id.Contains(".explicit.", StringComparison.Ordinal) && scene.Nodes.Any(p => p.Id.StartsWith("quiet_r3_", StringComparison.Ordinal) && p.Choices.Any(a => a.Next == n.Id)))))
                check(reached.Contains(scene.Id + "/" + page.Id), "Unplayed Soana later page: " + scene.Id + "/" + page.Id);
            check(scene.ContactUnit == actor && !Rules.IsRemote(scene), "Soana later progression bypasses local native contact.");
            check(Rules.EntryTargets(scene).SequenceEqual(new[] { "2b1776f3e398685479ff6b16290b4cc2" }), "Soana later entry target changed.");
            var ready = new Snapshot { Chapter = 3, Hour = 1000 };
            ready.Flags.UnionWith(scene.Requires); ready.Flags.Add("soana.old_defender"); ready.AvailableContacts.Add(actor);
            check(Program.CurrentAvailable(story, scene, ready), "Soana later gate baseline fails.");
            foreach (var required in scene.Requires.Where(requiredKey => !requiredKey.EndsWith(".present_now", StringComparison.Ordinal) && !requiredKey.EndsWith(".reachable_by_letter", StringComparison.Ordinal)))
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(required);
                check(!Program.CurrentAvailable(story, scene, missing) && !Rules.ContactAvailable(story, scene, missing), "Soana later prerequisite ignored: " + required);
            }
            foreach (var forbidden in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(forbidden);
                check(!Program.CurrentAvailable(story, scene, blocked), "Soana later blocker ignored: " + forbidden);
            }
            foreach (int chapter in new[] { 2, 4, 5, 6 })
            {
                var wrong = Program.Copy(ready); wrong.Chapter = chapter;
                check(!Program.CurrentAvailable(story, scene, wrong) && !Rules.ContactAvailable(story, scene, wrong), "Soana invents later-act local access.");
            }
            var noOutcome = Program.Copy(ready); noOutcome.Flags.Remove("soana.old_defender");
            check(!Program.CurrentAvailable(story, scene, noOutcome), "Soana later progression invents resolved guardian history.");
        }
        foreach (var ending in new[] { "night", "kiss", "quiet", "friend_evening" })
            check(endings.Contains("soana.later_" + ending), "Soana later ending unreachable: " + ending);
        var skill = scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Single(c => c.Check != null).Check!;
        check(skill.Skill == "SkillLoreReligion" && skill.DC == 24 && skill.CommanderOnly, "Soana shrine check loses its contract.");
    }
}
