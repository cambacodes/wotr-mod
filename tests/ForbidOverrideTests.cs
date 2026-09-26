using System;
using System.Collections.Generic;
using Tirabade;

internal static class ForbidOverrideTests
{
    internal static void Run(Action<bool, string> check)
    {
        var scene = new Scene {
            Id = "later_visit", Owner = "Memory", Requires = new[] { "prior_visit" },
            Forbids = new[] { "old_farewell", "other_objection" },
            ForbidOverrides = new Dictionary<string, string> { ["old_farewell"] = "catchup_requested" },
            Nodes = new List<Node> { new Node { Id = "start", Text = "Continue", Choices = new List<Choice> {
                new Choice { Set = new[] { "prior_visit", "old_farewell", "catchup_requested", "other_objection" } }
            } } }
        };
        var story = new Story { Scenes = new List<Scene> { scene } };
        Rules.Validate(story);
        var state = new Snapshot { Chapter = 3, Hour = 1000 };
        state.Flags.UnionWith(new[] { "prior_visit", "old_farewell" });
        check(!Rules.Available(story, scene, state), "Old farewell must remain closed without explicit catch-up.");
        state.Flags.Add("catchup_requested");
        check(Rules.Available(story, scene, state) && state.Has("old_farewell"), "Catch-up must preserve historical farewell while enabling the visit.");
        check(Rules.NextRemote(story, state) == scene, "Normal remote visit is not scheduled.");
        scene.ManualOnly = true;
        check(Rules.NextRemote(story, state) == null && Rules.Available(story, scene, state), "Manual offer must remain available without occupying the rest queue.");
        var following = new Scene { Id = "following_visit", Owner = "Memory", Nodes = scene.Nodes };
        story.Scenes.Add(following);
        check(Rules.NextRemote(story, state) == following, "Manual offer starves a subsequent remote visit.");
        story.Scenes.Remove(following);
        scene.ManualOnly = false;
        foreach (string blocker in new[] { "other_objection", "closed", "anevia_dead" })
        {
            state.Flags.Add(blocker);
            check(!Rules.Available(story, scene, state), "Catch-up bypasses unrelated restriction: " + blocker);
            state.Flags.Remove(blocker);
        }
        state.Flags.Remove("prior_visit");
        check(!Rules.Available(story, scene, state), "Catch-up bypasses an earned prerequisite.");
        void Invalid(string key, string value)
        {
            scene.ForbidOverrides.Clear(); scene.ForbidOverrides.Add(key, value);
            bool rejected = false;
            try { Rules.Validate(story); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid catch-up metadata accepted: " + key + "/" + value);
        }
        Invalid("not_forbidden", "catchup_requested");
        Invalid("old_farewell", "unwritten_flag");
        Invalid("old_farewell", "old_farewell");
        scene.Forbids = new[] { "closed", "old_farewell" };
        Invalid("closed", "catchup_requested");
        story.Etudes["old_farewell"] = "3f3fbb973a4ffee47956b4c7714c939a";
        Invalid("old_farewell", "catchup_requested");
    }
}
