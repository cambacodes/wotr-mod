using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Focused runtime checks for the round-2 route changes, independently of old reachability sweeps.
internal static class DelamereRound2Tests
{
    private const string P = "delamere.trickster.";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    internal static void Run(Story story, Action<bool, string> check)
    {
        Snapshot World(Scene scene)
        {
            var state = new Snapshot {
                Chapter = scene.Chapters.Length > 0 ? scene.Chapters[0] : scene.MinChapter,
                Hour = 5000, Area = scene.Areas.Length > 0 ? scene.Areas[0] : Drezen,
                CrusadeResources = new Dictionary<string, int> { ["Materials"] = 10000 }
            };
            state.Flags.UnionWith(new[] { "trickster", "trickster.ever", "chapter_later" });
            foreach (var flag in scene.Requires)
            {
                state.Flags.Add(flag);
                if (story.Derived.ContainsKey(flag)) HouseholdTests.Earn(story, state, flag);
            }
            foreach (var group in scene.RequiresAnyGroups)
            {
                state.Flags.Add(group[0]);
                if (story.Derived.ContainsKey(group[0])) HouseholdTests.Earn(story, state, group[0]);
            }
            Rules.Complete(story, state);
            foreach (var flag in state.Flags) state.Times[flag] = 0;
            return state;
        }
        foreach (var scene in story.Scenes.Where(s => s.Relationship == "delamere" && s.Areas.Length > 0 && Rules.IsRemote(s)))
        {
            var state = World(scene);
            check(Rules.Available(story, scene, state), "Round2 local arrival is unavailable: " + scene.Id);
            state.Area = "unrelated-dungeon";
            check(!Rules.Available(story, scene, state), "Round2 encounter travels to unrelated dungeon: " + scene.Id);
        }
        var table = story.Scenes.Single(s => s.Id == P + "woken.feasting_table");
        var reports = table.Nodes.Single(n => n.Id == "finish").Choices;
        foreach (var killed in new[] { false, true })
        foreach (var heard in new[] { false, true })
        {
            var state = World(table);
            if (killed) state.Flags.Add(P + "zanedra.native_killed");
            if (heard) state.Flags.Add(P + "zanedra.west_heard");
            check(Rules.Match(reports[0].Requires, reports[0].Forbids, state) == killed, "Unsupported witch death report");
            check(Rules.Match(reports[1].Requires, reports[1].Forbids, state) == (heard && !killed), "Unsupported west report");
            check(Rules.Match(reports[3].Requires, reports[3].Forbids, state), "Lost report fallback vanished");
        }
        foreach (var suffix in new[] { "woods.second_hunt", "woods.second_hunt_page", "woods.second_hunt_late" })
        foreach (var village in new[] { "given", "forced", "refused", "clans" })
        {
            var hunt = story.Scenes.Single(s => s.Id == P + suffix);
            var state = World(hunt);
            state.Flags.Add(P + "returned");
            state.Flags.Add(P + "told_truth");
            state.Flags.Add(P + "village." + village);
            Rules.Complete(story, state);
            var pages = new HashSet<string>();
            var ends = Program.Walk(hunt, state, (page, _) => pages.Add(page));
            check(ends.Any(e => e.Has("delamere.committed")), "Chosen catch lost commitment: " + suffix);
            check(ends.Any(e => e.Has("delamere.closed")), "Ownership refusal lost closure: " + suffix);
            check(pages.Contains(P + suffix + ".explicit.1") && pages.Contains("boundary_" + village),
                  "First night or earned boundary morning missing: " + suffix);
        }
        Console.WriteLine("PASS: Delamere round-2 native reports, runtime location guards, first-night deliveries and boundary mornings.");
    }
}

