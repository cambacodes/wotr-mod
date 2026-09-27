using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E12c: click-to-talk presence hubs (Presence.Dialog "hub"; scenes with InteractionHub = "<rel>.presence").
internal static class PresenceHubTests
{
    internal static Story Fixture()
    {
        var story = TricksterLatchTests.Fixture();
        story.Presences["irabeth.presence"] = new Presence { Unit = "280d4712dceb37f4a88e98f1f4c6e64f", Area = "2570015799edf594daf2f076f2f975d8",
            Mode = "reuse-native", Dialog = "hub", Greeting = "{n}Irabeth sets down her report.{/n}" };
        story.Scenes.Add(new Scene { Id = "irabeth.trickster.visit", Title = "A visit", Owner = "Irabeth", Relationship = "irabeth", MinChapter = 5,
            InteractionHub = "irabeth.presence", Requires = new[] { "trickster.ever", "irabeth.trickster.returned" }, Entry = "\"Walk with me.\"",
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } } });
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);
        var visit = story.Scenes.Single(s => s.Id == "irabeth.trickster.visit");
        check(Rules.IsPresenceHubScene(visit) && Rules.EntryTargets(visit).Length == 0, "Presence hub scene attaches to native lists.");
        var state = new Snapshot { Chapter = 5, Hour = 100 };
        state.Flags.UnionWith(new[] { "trickster.ever", "irabeth.trickster.returned" });
        check(Rules.Available(story, visit, state), "Hub scene unavailable when earned.");
        foreach (var (what, mutate) in new List<(string, Action<Story>)> {
            ("hub without Dialog", s => s.Presences["irabeth.presence"].Dialog = null),
            ("unknown Dialog", s => s.Presences["irabeth.presence"].Dialog = "irabeth.custom"),
            ("hub key of another relationship", s => s.Scenes.Single(x => x.Id == "irabeth.trickster.visit").InteractionHub = "anevia.presence"),
            ("hub scene with native lists", s => s.Scenes.Single(x => x.Id == "irabeth.trickster.visit").AnswerLists = new[] { "871af36f2ab2b1f40b5de77976c54276" }),
            ("hub without scenes", s => s.Scenes.RemoveAll(x => x.Id == "irabeth.trickster.visit")),
            ("greeting without hub", s => { s.Presences["irabeth.presence"].Dialog = null; s.Scenes.RemoveAll(x => x.Id == "irabeth.trickster.visit"); }) })
        {
            var bad = Fixture();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid presence hub accepted: " + what);
        }
    }
}
