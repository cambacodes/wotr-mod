using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class SeelahAftermathTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var scenes = new[] { "borrowed_saw", "platform_finished", "inheritors_corner", "roof_evening" }
            .Select(id => story.Scenes.Single(s => s.Id == "seelah." + id)).ToArray();
        var morning = story.Scenes.Single(s => s.Id == "seelah.morning");
        var weight = story.Scenes.Single(s => s.Id == "seelah.weight");
        var beforeMorning = new Snapshot { Chapter = 5, Hour = 1000, Area = scenes[0].Areas.Single() };
        beforeMorning.Flags.UnionWith(morning.Requires);
        beforeMorning.Flags.Add("seelah.courting");
        var afterMorning = Program.Walk(morning, beforeMorning).First(s => s.Has(morning.Id));
        check(afterMorning.Has("seelah.knows_need"), "Actual morning no longer establishes the learned history.");
        afterMorning.Hour += weight.DelayHours;
        check(Rules.Available(story, weight, afterMorning), "Morning cannot reach the judgment conversation.");
        foreach (var terms in Program.Walk(weight, afterMorning).Where(s => !s.Has("seelah.closed")))
        {
            terms.Hour += scenes[0].DelayHours;
            var visited = new HashSet<string>();
            check(Rules.Available(story, scenes[0], terms), "Actual judgment history cannot reach the saw scene.");
            Program.Walk(scenes[0], terms, (node, state) => visited.Add(node));
            check(!visited.Contains("hasty"), "Fresh learned history repeats the unlearned interruption.");
            string expected = terms.Has("seelah.frank_terms") ? "remember_frank" : terms.Has("seelah.hear_terms") ? "remember_heard" : "remember_demand";
            check(visited.Contains(expected), "Earlier judgment choice has no reachable callback after actual morning: " + expected);
        }
        foreach (var term in new[] { "frank_terms", "hear_terms", "corrected_demand" })
        foreach (var native in new[] { "unfinished", "rescued", "rescued_dead", "moderate", "bad", "both" })
        foreach (bool committed in new[] { false, true })
        {
            var start = new Snapshot { Chapter = 5, Hour = 1000, Area = scenes[0].Areas.Single() };
            start.Flags.UnionWith(scenes[0].Requires);
            start.Flags.UnionWith(new[] { "seelah.lovers", "seelah.knows_need", "seelah." + term, "konomi.committed" });
            if (term == "frank_terms") start.Flags.Add("seelah.check_person");
            if (term == "hear_terms") start.Flags.Add("seelah.check_signal");
            if (committed) start.Flags.UnionWith(new[] { "seelah.committed", "seelah.road" });
            else start.Flags.Add("seelah.day_" + (term == "frank_terms" ? "home" : term == "hear_terms" ? "road" : "uncertain"));
            if (native != "unfinished") start.Flags.Add("seelah.souls_returned");
            if (native == "rescued_dead" || native == "bad") start.Flags.Add("seelah.elan_dead");
            if (native == "moderate" || native == "both") start.Flags.Add("seelah.ending_moderate");
            if (native == "bad" || native == "both") start.Flags.Add("seelah.ending_bad");
            var states = new List<Snapshot> { start };
            foreach (var scene in scenes)
            {
                var continuing = new List<Snapshot>();
                foreach (var input in states)
                {
                    var state = Program.Copy(input);
                    // Native quest progress may change between the civilian work and prayer.
                    if (scene.Id == "seelah.inheritors_corner" && native == "unfinished" && term == "hear_terms")
                        state.Flags.UnionWith(new[] { "seelah.souls_returned", "seelah.ending_moderate" });
                    check(Rules.Available(story, scene, state), "Seelah aftermath cannot continue: " + scene.Id);
                    check(Rules.EntryTargets(scene).SequenceEqual(new[] { "417fa384f3250634bb71859fbc913453" }), "Seelah aftermath changes native contact attachment.");
                    foreach (var result in Program.Walk(scene, state))
                    {
                        check(result.Has("seelah.committed") == committed && result.Has("konomi.committed"), "Seelah aftermath invents or erases commitments.");
                        foreach (var flag in new[] { "seelah.souls_returned", "seelah.elan_dead", "seelah.ending_bad", "seelah.ending_moderate" })
                            check(result.Has(flag) == state.Has(flag), "Seelah aftermath changes native history: " + flag);
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(state.Flags) && Rules.Available(story, scene, result), "Seelah postponement records unplayed progress.");
                            continue;
                        }
                        check(!Rules.Available(story, scene, result), "Seelah aftermath repeats a completed event.");
                        if (scene.Id == "seelah.borrowed_saw")
                            check(result.Has("seelah.saw_gift") != result.Has("seelah.saw_loan"), "Seelah repair loses the gift/loan decision.");
                        if (scene.Id == "seelah.platform_finished")
                            check(result.Has("seelah.prayer_company") != result.Has("seelah.prayer_private"), "Seelah prayer invitation loses its privacy choice.");
                        if (scene.Id == "seelah.inheritors_corner")
                        {
                            string expected = !state.Has("seelah.souls_returned") ? "unfinished" : state.Has("seelah.ending_bad") ? "grief" : state.Has("seelah.ending_moderate") ? "questions" : "hope";
                            foreach (var outcome in new[] { "unfinished", "grief", "questions", "hope" })
                                check(result.Has("seelah.aftermath_" + outcome) == (outcome == expected), "Seelah faith conversation uses a stale or contradictory native outcome.");
                        }
                        if (scene.Id == "seelah.roof_evening")
                        {
                            check(result.Has("seelah.aftermath_ready"), "Seelah roof evening loses completion.");
                            check(result.Has("seelah.roof_kissed") != result.Has("seelah.roof_quiet"), "Seelah roof evening confuses kiss and quiet company.");
                            continue;
                        }
                        var next = scenes[Array.IndexOf(scenes, scene) + 1];
                        check(!Rules.Available(story, next, result), "Seelah aftermath skips the next-day delay.");
                        result.Hour += 23;
                        check(!Rules.Available(story, next, result), "Seelah aftermath opens before the delay boundary.");
                        result.Hour++;
                        continuing.Add(result);
                    }
                }
                states = continuing;
            }
        }
        foreach (var scene in scenes)
        {
            var ready = new Snapshot { Chapter = 5, Hour = 1000, Area = scene.Areas.Single() };
            ready.Flags.UnionWith(scene.Requires);
            foreach (var required in scene.Requires)
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(required);
                check(!Rules.Available(story, scene, missing), "Seelah aftermath ignores " + required);
            }
            foreach (var blocker in new[] { "seelah.closed", "seelah_dead", "seelah_gone", "inhuman", "seelah.farewell" })
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                check(!Rules.Available(story, scene, blocked), "Seelah aftermath ignores " + blocker);
            }
            ready.Times[scene.Requires.Last()] = 1000;
            ready.Hour = 1023;
            check(!Rules.Available(story, scene, ready), "Seelah aftermath ignores its latest prerequisite timestamp.");
            ready.Hour++;
            check(Rules.Available(story, scene, ready), "Seelah aftermath misses the exact delay boundary.");
            ready.Chapter = 4;
            check(!Rules.Available(story, scene, ready), "Seelah aftermath appears before Chapter 5.");
            ready.Chapter = 5; ready.Area = "elsewhere";
            check(!Rules.Available(story, scene, ready), "Seelah aftermath appears outside Drezen.");
        }
    }
}
