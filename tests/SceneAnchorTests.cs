using System;
using System.Collections.Generic;
using Tirabade;

// E14h: EpilogueAfter = "scene:<id>" anchors after another RRT epilogue page of the same sequence.
internal static class SceneAnchorTests
{
    internal static void Run(Action<bool, string> check)
    {
        Scene Page(string id, string owner, string? after, string? sequence = null) => new Scene { Id = id, Title = id, Owner = owner, Relationship = "lastcall",
            MinChapter = 1, MaxChapter = 6, EpilogueAfter = after, EpilogueSequence = sequence,
            Nodes = new List<Node> { new Node { Id = "first", Text = "x", Choices = new List<Choice> { new Choice() } } } };
        Story Wrap(params Scene[] scenes)
        {
            var story = ReturnToListTests.Wrap(scenes[0]);
            for (int i = 1; i < scenes.Length; i++) story.Scenes.Add(scenes[i]);
            return story;
        }
        var story = Wrap(Page("lastcall.a1", "Epilogue", "fb42f8bd123bf1f40a448f6dbc66cbbe", "PlayerFinalChoice"),
            Page("lastcall.a2", "Epilogue", "scene:lastcall.a1", "PlayerFinalChoice"),
            Page("lastcall.c", "LastCallEpilogue", null), Page("lastcall.c2", "Epilogue", "scene:lastcall.c"));
        Rules.Validate(story);
        check(Rules.EpilogueAnchor(story, "scene:lastcall.a1", name => "G(" + name + ")") == "G(page.lastcall.a1.first)", "Scene anchor not resolved to its first page.");
        check(Rules.EpilogueAnchor(story, "fb42f8bd123bf1f40a448f6dbc66cbbe", name => "x") == "fb42f8bd123bf1f40a448f6dbc66cbbe", "Native anchor changed.");
        foreach (var (what, scenes) in new List<(string, Scene[])> {
            ("unknown scene", new[] { Page("lastcall.a2", "Epilogue", "scene:nothing") }),
            ("self anchor", new[] { Page("lastcall.a2", "Epilogue", "scene:lastcall.a2") }),
            ("anchor in another sequence", new[] { Page("lastcall.a1", "Epilogue", "fb42f8bd123bf1f40a448f6dbc66cbbe", "PlayerFinalChoice"), Page("lastcall.a2", "Epilogue", "scene:lastcall.a1") }),
            ("Aeon anchor for a normal page", new[] { Page("lastcall.aeon", "AeonEpilogue", null), Page("lastcall.a2", "Epilogue", "scene:lastcall.aeon") }),
            ("non-epilogue anchor", new[] { Page("lastcall.a2", "Epilogue", "scene:lastcall.letter"), new Scene { Id = "lastcall.letter", Title = "l", Owner = "Memory", Remote = true,
                Relationship = "lastcall", Nodes = new List<Node> { new Node { Id = "s", Text = "x", Choices = new List<Choice> { new Choice() } } } } }) })
        {
            bool rejected = false;
            try { Rules.Validate(Wrap(scenes)); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid scene anchor accepted: " + what);
        }
    }
}
