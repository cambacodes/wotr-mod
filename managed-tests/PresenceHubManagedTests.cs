using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.UnitLogic.Parts;
using Tirabade;

// E12c: Main.BuildPresenceHub builds the generalized hub dialog, and the native click list the interaction joins is not serialized.
internal static class PresenceHubManagedTests
{
    public static void Run(Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        // The interaction list is runtime-only (no JsonProperty), like native SpawnerInteractionDialog's; nothing custom persists.
        var list = typeof(UnitPartInteractions).GetField("m_Interactions", BindingFlags.Instance | BindingFlags.NonPublic)!;
        check(!list.GetCustomAttributes(true).Any(a => a.GetType().Name == "JsonPropertyAttribute"), "UnitPartInteractions.m_Interactions became serialized.");
        var main = typeof(Main);
        var storyField = main.GetField("story", BindingFlags.NonPublic | BindingFlags.Static)!;
        var saved = storyField.GetValue(null);
        var fixture = PresenceHubFixture();
        try
        {
            storyField.SetValue(null, fixture);
            var dialog = (BlueprintDialog)main.GetMethod("BuildPresenceHub", BindingFlags.NonPublic | BindingFlags.Static)!
                .Invoke(null, new object[] { "e12c.presence", fixture.Presences["e12c.presence"] })!;
            var page = (BlueprintBookPage)dialog.FirstCue.Cues.Single().Get();
            check(dialog.Type.ToString() == "Book" && page.AssetGuid == id("page.e12c.presence.hub"), "Hub dialog/page identity wrong.");
            check(page.Answers.Select(a => a.Guid).SequenceEqual(new[] { id("answer.e12c.presence.hub.e12c.visit"), id("answer.e12c.presence.hub.leave") }),
                "Hub answers: one per hub scene, then leave.");
            var entry = (BlueprintAnswer)page.Answers[0].Get();
            check(entry.ShowConditions.Conditions.Single() is Main.RouteCondition shown && shown.Scene == fixture.Scenes[0]
                && entry.OnSelect.Actions.Single() is Main.RouteAction start && start.Start == fixture.Scenes[0], "Hub entry does not gate and start its scene.");
        }
        finally { storyField.SetValue(null, saved); }
        Console.WriteLine("PASS: E12c presence hub dialog built (entries gated per scene, leave last); click list is runtime-only.");
    }

    private static Story PresenceHubFixture()
    {
        var story = new Story();
        story.Relationships["e12c"] = new Relationship { Title = "E12c", StartedFlag = "e12c.started", ClosedFlag = "e12c.closed", CommittedFlag = "e12c.committed" };
        story.Presences["e12c.presence"] = new Presence { Unit = "280d4712dceb37f4a88e98f1f4c6e64f", Area = "2570015799edf594daf2f076f2f975d8", Dialog = "hub" };
        story.Scenes.Add(new Scene { Id = "e12c.visit", Title = "A visit", Owner = "Irabeth", Relationship = "e12c", InteractionHub = "e12c.presence",
            Entry = "\"Walk with me.\"", Nodes = new List<Tirabade.Node> { new Tirabade.Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } } });
        return story;
    }
}
