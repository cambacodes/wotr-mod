using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Tirabade;

// E14c: Main.BuildScene appends one conditional cue per paragraph to the epilogue page, after the (optional) base cue.
internal static class ParagraphManagedTests
{
    public static void Run(Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        var scene = new Scene
        {
            Id = "e14c.fixture", Title = "E14c", Owner = "Epilogue", Relationship = "anevia", MinChapter = 1, MaxChapter = 6,
            Nodes = new List<Tirabade.Node> { new Tirabade.Node { Id = "start", Text = "", Choices = new List<Choice> { new Choice() },
                Paragraphs = new List<Paragraph> { new Paragraph { Text = "One." }, new Paragraph { Text = "Two.", Requires = new[] { "x" } } } } }
        };
        typeof(Main).GetMethod("BuildScene", BindingFlags.NonPublic | BindingFlags.Static)!.Invoke(null, new object[] { scene });
        var page = (BlueprintBookPage)ResourcesLibrary.TryGetBlueprint(id("page.e14c.fixture.start"))!;
        check(ResourcesLibrary.TryGetBlueprint(id("cue.e14c.fixture.start")) is BlueprintCue, "Textless base cue is not registered (save names must stay stable).");
        check(page.Cues.Select(c => c.Guid).SequenceEqual(new[] { id("cue.e14c.fixture.start.p0"), id("cue.e14c.fixture.start.p1") }),
            "Paragraph cues are missing, out of order, or the textless base cue is on the page.");
        foreach (int i in new[] { 0, 1 })
        {
            var cue = (BlueprintCue)page.Cues[i].Get();
            check(cue.Conditions.Conditions.Single() is Main.ParagraphCondition condition && ReferenceEquals(condition.Paragraph, scene.Nodes[0].Paragraphs[i])
                && cue.Speaker.NoSpeaker && cue.Continue.Cues.Count == 0, "Paragraph cue lacks its condition: p" + i);
        }
        Console.WriteLine("PASS: E14c paragraph cues appended to the epilogue page with their conditions.");
    }
}
