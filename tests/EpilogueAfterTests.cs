using System;
using System.Collections.Generic;
using Tirabade;

// ER-3: Scene.EpilogueAfter is validated here; its placement (Main.InsertEpiloguePage) is covered by the managed tests.
internal static class EpilogueAfterTests
{
    internal static void Run(Action<bool, string> check)
    {
        Story Fixture(string owner, string? after) => new Story
        {
            Scenes = new List<Scene> { new Scene { Id = "irabeth.trickster.ending", Title = "x", Owner = owner, MinChapter = 1, MaxChapter = 6,
                EpilogueAfter = after, Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } } } }
        };
        Rules.Validate(Fixture("Epilogue", "bfaddf0dbda4724419d597e712a5b322"));   // BookPage_0174_TricksterFinalRewrite
        Rules.Validate(Fixture("AeonEpilogue", "5e3e2282000000000000000000000000".Substring(0, 32)));
        foreach (var (owner, after, what) in new[] { ("Memory", "bfaddf0dbda4724419d597e712a5b322", "non-epilogue"),
            ("Epilogue", "not-a-guid", "bad guid"), ("Epilogue", "00000000000000000000000000000000", "empty guid") })
        {
            bool rejected = false;
            try { Rules.Validate(Fixture(owner, after)); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid EpilogueAfter accepted: " + what);
        }
    }
}
