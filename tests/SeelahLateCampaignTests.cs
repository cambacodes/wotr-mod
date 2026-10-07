using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class SeelahLateCampaignTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var scenes = new[] { "late_course", "late_lesson", "late_page", "late_race", "late_afterglow", "late_first_step" }
            .Select(id => story.Scenes.Single(s => s.Id == "seelah." + id)).ToArray();
        var nativeFlags = new[] { "seelah.souls_returned", "seelah.elan_dead", "seelah.ending_bad", "seelah.ending_moderate" };
        var observed = new HashSet<string>();
        var race = scenes[3];
        var closeTurn = race.Nodes.Single(n => n.Id == "running").Choices[0];
        var careful = race.Nodes.Single(n => n.Id == "running").Choices[1];
        check(closeTurn.Check != null && closeTurn.Check.Skill == "SkillMobility" && closeTurn.Check.DC == 26
            && closeTurn.Check.CommanderOnly && closeTurn.Check.Success == "narrow" && closeTurn.Check.Failure == "stumble",
            "Seelah's close turn no longer uses the declared Commander Mobility check.");
        check(closeTurn.Next == null && !closeTurn.Abort && closeTurn.Revive == null
            && closeTurn.Set.SequenceEqual(new[] { "seelah.late_close_turn" }),
            "Seelah's attempted turn records a result or changes affection before rolling.");
        check(careful.Check == null && careful.Next == "wide", "Seelah loses the careful non-roll approach.");
        check(race.Nodes.Single(n => n.Id == "stumble").Choices.All(c => c.Check == null && c.Next == "lost"
            && c.Set.Contains("seelah.late_race_lost") && c.Set.Contains("seelah.late_race_stumbled")
            && !c.Set.Contains("seelah.late_wide_turn")), "Failed close turn is confused with choosing the wide line.");

        foreach (var history in new[] { "unfinished", "rescued", "rescued_dead", "moderate", "bad", "both" })
        foreach (bool committed in new[] { false, true })
        {
            var start = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            start.Flags.UnionWith(new[] { "seelah.courting", "seelah.aftermath_ready", "seelah.lovers", "seelah.weight", "konomi.committed" });
            start.Times["seelah.aftermath_ready"] = start.Hour - scenes[0].DelayHours;
            // Deliberately stale authored reaction must not replace the current native outcome.
            start.Flags.Add("seelah.aftermath_grief");
            if (committed) start.Flags.UnionWith(new[] { "seelah.committed", "seelah.road" });
            if (history != "unfinished") start.Flags.Add("seelah.souls_returned");
            if (history == "rescued_dead" || history == "bad") start.Flags.Add("seelah.elan_dead");
            if (history == "moderate" || history == "both") start.Flags.Add("seelah.ending_moderate");
            if (history == "bad" || history == "both") start.Flags.Add("seelah.ending_bad");
            var states = new List<Snapshot> { start };
            for (int index = 0; index < scenes.Length; index++)
            {
                var scene = scenes[index];
                var continuing = new List<Snapshot>();
                foreach (var state in states)
                {
                    check(Program.CurrentAvailable(story, scene, state), "Seelah late chain cannot continue: " + scene.Id);
                    if (index == 2)
                    {
                        string expected = !state.Has("seelah.souls_returned") ? "unfinished"
                            : state.Has("seelah.ending_bad") ? "grief" : state.Has("seelah.ending_moderate") ? "questions" : "hope";
                        var eligible = scene.Nodes.Single(n => n.Id == "outcome").Choices
                            .Where(c => Rules.Match(c.Requires, c.Forbids, state)).ToArray();
                        check(eligible.Length == 1 && eligible[0].Next == expected, "Seelah's notebook uses stale or contradictory native history.");
                    }
                    foreach (var result in Program.Walk(scene, state))
                    {
                        check(result.Has("seelah.committed") == committed && result.Has("konomi.committed")
                            && result.Has("seelah.lovers") && !result.Has("seelah.closed"), "Seelah's activity changes romance commitments or coerces a breakup.");
                        foreach (var native in nativeFlags)
                            check(result.Has(native) == state.Has(native), "Seelah late scene alters native history: " + native);
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(state.Flags) && result.Times.Count == state.Times.Count
                                && Program.CurrentAvailable(story, scene, result), "Seelah postponement records progress or consumes the invitation.");
                            continue;
                        }
                        check(!Program.CurrentAvailable(story, scene, result), "Seelah late scene can repeat after completion.");
                        if (index == 0)
                        {
                            check(result.Has("seelah.late_running") != result.Has("seelah.late_watching"), "Runner/spectator choice is lost.");
                            check(result.Has("seelah.late_fixed_lessons") != result.Has("seelah.late_shared_lessons"), "Teaching arrangements are not distinct.");
                        }
                        if (index == 2)
                        {
                            check(result.Has("seelah.late_elan_memory") == (state.Has("seelah.souls_returned") && state.Has("seelah.elan_dead")), "Elan memory is missing or invented.");
                            check(result.Has("seelah.late_elan_draft") == (state.Has("seelah.souls_returned") && !state.Has("seelah.elan_dead")), "Elan draft has the wrong native gate.");
                        }
                        if (index == 3)
                        {
                            bool won = result.Has("seelah.late_race_won");
                            check(won != result.Has("seelah.late_race_lost"), "Race outcome is missing or contradictory.");
                            check(!result.Has("seelah.kissed"), "Winning or losing the race awards affection.");
                            if (state.Has("seelah.late_watching"))
                                check(!won && !result.Has("seelah.late_close_turn") && !result.Has("seelah.late_wide_turn")
                                    && !result.Has("seelah.late_race_stumbled"), "Spectator acquires a player's racing result.");
                            else if (result.Has("seelah.late_wide_turn"))
                                check(!won && !result.Has("seelah.late_close_turn") && !result.Has("seelah.late_race_stumbled"), "Careful finish is rewritten as a failed close turn.");
                            else
                                check(result.Has("seelah.late_close_turn") && (won != result.Has("seelah.late_race_stumbled")), "Close-turn check loses its success/failure distinction.");
                        }
                        if (index == 4)
                        {
                            check(new[] { "seelah.late_night_chosen", "seelah.late_kisses_chosen", "seelah.late_quiet_chosen" }.Count(result.Has) == 1,
                                "Intimate evening loses its voluntary alternatives.");
                            if (result.Has("seelah.late_quiet_chosen"))
                                check(!result.Has("seelah.kissed") && !result.Has("seelah.late_night_kept"), "Quiet company is converted into physical intimacy.");
                        }
                        if (index == scenes.Length - 1)
                        {
                            check(result.Has("seelah.late_campaign_kept"), "Seelah late chain has no completed endpoint.");
                            observed.UnionWith(result.Flags.Where(f => f.StartsWith("seelah.late_", StringComparison.Ordinal)));
                        }
                        else
                        {
                            var next = scenes[index + 1];
                            check(!Program.CurrentAvailable(story, next, result), "Seelah next meeting skips its delay.");
                            result.Hour += next.DelayHours - 1;
                            check(!Program.CurrentAvailable(story, next, result), "Seelah next meeting opens early.");
                            result.Hour++;
                            check(Program.CurrentAvailable(story, next, result), "Seelah next meeting misses the exact delay boundary.");
                            continuing.Add(result);
                        }
                    }
                }
                // Merge histories identical for future conditions rather than multiplying equivalent prose choices.
                states = continuing.GroupBy(s => string.Join("\n", s.Flags.OrderBy(f => f, StringComparer.Ordinal)))
                    .Select(group => group.First()).ToList();
            }
        }
        foreach (var milestone in new[] { "late_fixed_lessons", "late_shared_lessons", "late_running", "late_watching", "late_race_won",
            "late_race_lost", "late_race_stumbled", "late_wide_turn", "late_night_chosen", "late_kisses_chosen", "late_quiet_chosen",
            "late_music_quiet", "late_music_quick", "late_shelf_keepsake", "late_shelf_space" })
            check(observed.Contains("seelah." + milestone), "An authored Seelah path cannot reach the campaign endpoint: " + milestone);

        foreach (var scene in scenes)
        {
            var ready = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            ready.Flags.UnionWith(scene.Requires);
            check(scene.Optional && !Rules.IsRemote(scene) && Rules.EntryTargets(scene).SequenceEqual(new[] { "417fa384f3250634bb71859fbc913453" }),
                "Seelah late scene is no longer an optional native-dialogue visit.");
            foreach (var required in scene.Requires.Where(requiredKey => !requiredKey.EndsWith(".present_now", StringComparison.Ordinal) && !requiredKey.EndsWith(".reachable_by_letter", StringComparison.Ordinal)))
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(required);
                if (required == "seelah.trickster.custody_clear")
                    // A derived custody fact is revoked by an outstanding list,
                    // not by deleting the cached result before recomputation.
                    missing.Flags.Add("seelah.trickster.cost.holds_her_death");
                check(!Program.CurrentAvailable(story, scene, missing), "Seelah late scene ignores required history: " + required);
            }
            foreach (var blocker in new[] { "seelah.closed", "seelah_dead", "seelah_gone", "inhuman", "seelah.farewell" })
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                check(!Program.CurrentAvailable(story, scene, blocked), "Seelah late scene ignores unavailability: " + blocker);
            }
            foreach (int chapter in new[] { 3, 4, 6 })
            {
                var elsewhere = Program.Copy(ready); elsewhere.Chapter = chapter;
                check(!Program.CurrentAvailable(story, scene, elsewhere), "Seelah late scene escapes its Chapter 5 scope.");
            }
            check(scene.DelayHours == (scene == race ? 48 : 24), "Seelah late meeting loses its authored delay.");
            ready.Times[scene.Requires.Last(key => !story.Derived.ContainsKey(key))] = ready.Hour;
            ready.Hour += scene.DelayHours - 1;
            check(!Program.CurrentAvailable(story, scene, ready), "Seelah meeting ignores a newly completed prerequisite timestamp.");
            ready.Hour++;
            check(Program.CurrentAvailable(story, scene, ready), "Seelah meeting is unavailable at its exact prerequisite delay.");
            ready.Area = "elsewhere";
            check(!Program.CurrentAvailable(story, scene, ready), "Seelah late scene is available outside Drezen.");
        }
        var oldRoad = story.Scenes.Single(s => s.Id == "seelah.road");
        var legacy = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
        legacy.Flags.UnionWith(new[] { "seelah.courting", "seelah.lovers", "seelah.weight" });
        check(Program.CurrentAvailable(story, oldRoad, legacy), "The optional late campaign strands a pre-aftermath commitment path.");
        // Physical presence is still supplied by native dialogue contact, not proven by this snapshot test.
    }
}
