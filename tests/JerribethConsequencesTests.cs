using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class JerribethConsequencesTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "jerribeth." + id);
        foreach (int chapter in Find("offered_signature").Chapters)   // JER-08: Chapters 4-5
        foreach (string area in Find("offered_signature").Areas)
        foreach (bool wintersun in new[] { false, true })
        {
            var initial = new Snapshot { Chapter = chapter, Area = area, Hour = 1000 };
            initial.Flags.UnionWith(new[] { "jerribeth.commission", "jerribeth.terms", "jerribeth.lovers", "seelah.committed" });
            if (wintersun) initial.Flags.Add("jerribeth.wintersun_known");
            var ids = new List<string> { "offered_signature" };
            if (wintersun) ids.Add("borrowed_sun");
            ids.AddRange(new[] { "small_print", "unsold_evening", "purchaser_answer" });
            var states = new List<Snapshot> { initial };
            foreach (string id in ids)
            {
                var scene = Find(id);
                var continuing = new List<Snapshot>();
                foreach (var input in states)
                {
                    var state = Program.Copy(input);
                    int latest = scene.Requires.Where(state.Times.ContainsKey).Select(f => state.Times[f]).DefaultIfEmpty(0).Max();
                    state.Hour = Math.Max(state.Hour, latest + scene.DelayHours);
                    check(Program.CurrentAvailable(story, scene, state), "Jerribeth consequence chain stranded: " + id);
                    if (latest > 0)
                    {
                        var early = Program.Copy(state); early.Hour = latest + scene.DelayHours - 1;
                        check(!Program.CurrentAvailable(story, scene, early), "Jerribeth consequence skips delay: " + id);
                    }
                    foreach (var result in Program.Walk(scene, state))
                    {
                        check(result.Has("seelah.committed") && result.Has("jerribeth.lovers") && !result.Has("jerribeth.committed"), "Jerribeth consequence changes relationship commitments.");
                        check(result.Has("jerribeth.wintersun_known") == wintersun, "Jerribeth consequence invents native knowledge.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(state.Flags), "Jerribeth postponement writes progress.");
                            continue;
                        }
                        check(!Program.CurrentAvailable(story, scene, result), "Jerribeth consequence repeats completed scene.");
                        if (result.Has("jerribeth.closed"))
                        {
                            check(ids.Skip(ids.IndexOf(id) + 1).All(next => !Program.CurrentAvailable(story, Find(next), result)), "Jerribeth closure allows continued courtship.");
                            continue;
                        }
                        check(result.Has("jerribeth.offer_performance") != result.Has("jerribeth.offer_design"), "Jerribeth loses selected work.");
                        if (id == "small_print" || id == "unsold_evening" || id == "purchaser_answer")
                            check(result.Has("jerribeth.sale_corrected") != result.Has("jerribeth.sale_withdrawn"), "Jerribeth loses sale outcome.");
                        if (id == "purchaser_answer") check(result.Has("jerribeth.consequences_kept"), "Jerribeth purchaser chain lacks completion.");
                        continuing.Add(result);
                    }
                }
                check(continuing.Count > 0, "Jerribeth consequence has no continuing path: " + id);
                states = continuing;
            }
            if (!wintersun) check(!Program.CurrentAvailable(story, Find("borrowed_sun"), states[0]), "Wintersun scene invents knowledge.");
        }
        foreach (var scene in story.Scenes.Where(s => new[] { "offered_signature", "borrowed_sun", "small_print", "unsold_evening", "purchaser_answer" }.Any(id => s.Id == "jerribeth." + id)))
        {
            var ready = new Snapshot { Chapter = scene.Chapters[0], Area = scene.Areas[scene.Chapters[0] == 4 ? 1 : 0], Hour = 1000 };
            ready.Flags.UnionWith(scene.Requires);
            check(Program.CurrentAvailable(story, scene, ready), "Jerribeth consequence readiness fixture invalid.");
            check(!Rules.EntryTargets(scene).Any(), "Remote Jerribeth scene attaches to native conversation.");
            foreach (string required in scene.Requires.Where(requiredKey => !requiredKey.EndsWith(".present_now", StringComparison.Ordinal) && !requiredKey.EndsWith(".reachable_by_letter", StringComparison.Ordinal)))
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(required);
                check(!Program.CurrentAvailable(story, scene, missing), "Jerribeth ignores prerequisite: " + required);
            }
            foreach (string blocked in new[] { "jerribeth.closed", "jerribeth.unavailable", "jerribeth.farewell" })
            {
                var state = Program.Copy(ready); state.Flags.Add(blocked);
                check(!Program.CurrentAvailable(story, scene, state), "Jerribeth ignores blocker: " + blocked);
            }
            ready.Chapter = 3;   // JER-08: not a Chapter 3 letter any more
            check(!Program.CurrentAvailable(story, scene, ready), "Jerribeth consequence appears too early.");
            ready.Chapter = 5; ready.Area = "elsewhere";
            check(!Program.CurrentAvailable(story, scene, ready), "Jerribeth consequence ignores area.");
        }
    }
}
