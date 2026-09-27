using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E14e: Scene.ContinueBefore validation and availability.
internal static class ContinueBeforeTests
{
    internal static Scene Fixture() => new Scene
    {
        Id = "trickster.lastcall.court.closing", Title = "Closing", Owner = "Pharasma", Relationship = "lastcall", MinChapter = 6, MaxChapter = 6,
        Requires = new[] { "trickster.lastcall.court.dealt" },
        ContinueBefore = new ContinueSpec { Cue = "3094c9e9557c43d29610dbd3eec15b35", Parents = new[] { "da7646b4ce8e4e658ee92aa02877ec17", "abafa9f923204d5a96cb13bec9ab7771" } },
        Nodes = new List<Node> { new Node { Id = "start", Text = "Go.", Choices = new List<Choice> { new Choice() } } }
    };

    internal static void Run(Action<bool, string> check)
    {
        Story Wrap(Scene scene)
        {
            var story = ReturnToListTests.Wrap(scene);
            story.Scenes.Add(new Scene { Id = "setter", Title = "s", Owner = "Memory", Remote = true, Relationship = "lastcall",
                Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice { Set = new[] { "trickster.lastcall.court.dealt" } } } } } });
            return story;
        }
        var story = Wrap(Fixture());
        Rules.Validate(story);
        check(Rules.EntryTargets(story.Scenes[0]).Length == 0, "Continue-before line has native entry targets.");
        var state = new Snapshot { Chapter = 6 };
        check(!Rules.Available(story, story.Scenes[0], state), "Closing line available without the deal.");
        state.Flags.Add("trickster.lastcall.court.dealt");
        check(Rules.Available(story, story.Scenes[0], state), "Closing line unavailable after the deal.");
        var cases = new List<(string, Action<Scene>)>
        {
            ("remote", s => s.Remote = true),
            ("answer lists", s => s.AnswerLists = new[] { "2a46b86fb27c4662a6159388aaa44773" }),
            ("two choices", s => s.Nodes[0].Choices.Add(new Choice())),
            ("conditioned choice", s => s.Nodes[0].Choices[0].Requires = new[] { "x" }),
            ("no parents", s => s.ContinueBefore!.Parents = Array.Empty<string>()),
            ("parent equals anchor", s => s.ContinueBefore!.Parents = new[] { s.ContinueBefore.Cue }),
            ("bad anchor", s => s.ContinueBefore!.Cue = "nope"),
        };
        foreach (var (what, mutate) in cases)
        {
            var scene = Fixture();
            mutate(scene);
            bool rejected = false;
            try { Rules.Validate(Wrap(scene)); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid continue-before line accepted: " + what);
        }
    }
}
