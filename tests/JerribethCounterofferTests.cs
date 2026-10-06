using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class JerribethCounterofferTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "jerribeth." + id);
        var scenes = story.Scenes.Where(s => s.Id.StartsWith("jerribeth.counterfeit_")).ToArray();
        var observed = new HashSet<string>();
        foreach (int chapter in scenes[0].Chapters)   // JER-08: Chapters 4-5
        foreach (bool exposed in new[] { false, true })
        {
            var state = new Snapshot { Chapter = chapter, Area = scenes[0].Areas[chapter == 4 ? 1 : 0], Hour = 1000 };
            state.Flags.UnionWith(new[] { "jerribeth.commission", "jerribeth.terms", "jerribeth.lovers", "seelah.committed" });
            if (exposed) state.Flags.Add("jerribeth.wintersun_known");
            var predecessors = new List<string> { "offered_signature" };
            if (exposed) predecessors.Add("borrowed_sun");
            predecessors.AddRange(new[] { "small_print", "unsold_evening", "purchaser_answer" });
            foreach (string id in predecessors)
            {
                var scene = Find(id);
                state.Hour += scene.DelayHours;
                check(Program.CurrentAvailable(story, scene, state), "Counteroffer predecessor unavailable: " + id);
                state = Program.Walk(scene, state).First(s => s.Has(scene.Id) && (id != "borrowed_sun" || s.Has("jerribeth.sun_exposed")));
            }
            check(state.Has("jerribeth.consequences_kept"), "Counteroffer prerequisite not earned through predecessor.");
            var states = new List<Snapshot> { state };
            foreach (var scene in scenes)
            {
                var next = new List<Snapshot>();
                foreach (var input in states)
                {
                    var ready = Program.Copy(input); ready.Hour += scene.DelayHours;
                    check(Program.CurrentAvailable(story, scene, ready), "Counteroffer chain unavailable: " + scene.Id);
                    foreach (var result in Program.Walk(scene, ready))
                    {
                        check(result.Has("seelah.committed") && result.Has("jerribeth.lovers"), "Counteroffer changes existing relationships.");
                        check(result.Has("jerribeth.sun_exposed") == exposed, "Counteroffer fabricates earlier investigation.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags), "Counteroffer deferral writes progress.");
                            continue;
                        }
                        check(!Program.CurrentAvailable(story, scene, result), "Counteroffer repeats completed scene.");
                        observed.UnionWith(result.Flags.Where(f => f.StartsWith("jerribeth.counter_")));
                        next.Add(result);
                    }
                }
                check(next.Count > 0, "Counteroffer has no complete paths.");
                states = next;
            }
            check(states.All(s => s.Has("jerribeth.counter_public_account") != s.Has("jerribeth.counter_private_archive")), "Counteroffer loses bargain choice.");
        }
        foreach (string outcome in new[] { "counter_cache_intact", "counter_cache_broken", "counter_stage_cut", "counter_clerk_witness", "counter_clerk_rehearsal", "counter_clerk_hidden", "counter_public_account", "counter_private_archive" })
            check(observed.Contains("jerribeth." + outcome), "Counteroffer misses consequential outcome: " + outcome);
        foreach (var scene in scenes)
        {
            var ready = new Snapshot { Chapter = scene.Chapters[0], Area = scene.Areas[scene.Chapters[0] == 4 ? 1 : 0], Hour = 1000 };   // JER-08
            ready.Flags.UnionWith(scene.Requires);
            check(Program.CurrentAvailable(story, scene, ready), "Counteroffer valid baseline unavailable.");
            foreach (string blocker in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                check(!Program.CurrentAvailable(story, scene, blocked), "Counteroffer ignores blocker: " + blocker);
            }
        }
    }
}
