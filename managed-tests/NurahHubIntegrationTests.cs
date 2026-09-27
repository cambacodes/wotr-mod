using System;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Tirabade;

internal static class NurahHubIntegrationTests
{
    private const BindingFlags Members = BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;

    internal static void Run(Story story, Action<bool, string> check)
    {
        var main = typeof(Main);
        var hub = (BlueprintDialog?)main.GetField("nurahHub", Members)!.GetValue(null);
        var interaction = main.GetField("nurahInteraction", Members)!.GetValue(null);
        check(hub != null && interaction != null, "Main.Build did not register Nurah's private arrival dialog and click interaction");
        check(hub!.Type == DialogType.Book && hub.Conditions.Conditions.Length == 0
            && hub.StartActions.Actions.Length == 0 && hub.FinishActions.Actions.Length == 1,
            "Nurah hub dialog has unexpected entry or finish behavior");

        var page = hub.FirstCue.Cues.Single().Get() as BlueprintBookPage;
        check(page != null && page.ShowOnce == false, "Nurah arrival hub is not an ordinary repeatable book page");
        check(page!.Cues.Count == 1 && page.Cues.Single().Get() is BlueprintCue,
            "Nurah hub greeting cue is missing or ambiguous");

        var scenes = story.Scenes.Where(Rules.IsNurahHubScene).ToArray();
        check(scenes.Length == 11 && page.Answers.Count == scenes.Length + 1,
            "Nurah hub does not offer every physical continuation plus one exit");
        foreach (var scene in scenes)
        {
            var matches = page.Answers.Select(reference => reference.Get()).OfType<BlueprintAnswer>()
                .Where(answer => answer.ShowConditions.Conditions.Length == 1
                    && answer.ShowConditions.Conditions[0] is Main.RouteCondition condition
                    && ReferenceEquals(condition.Scene, scene)).ToArray();
            check(matches.Length == 1, "Nurah hub omits or duplicates physical scene " + scene.Id);
            var answer = matches.Single();
            check(answer.SelectConditions.Conditions.Length == 1
                && answer.SelectConditions.Conditions[0] is Main.RouteCondition selected
                && ReferenceEquals(selected.Scene, scene) && ReferenceEquals(selected.Owner, answer),
                "Nurah hub selection is not guarded by the same current scene contract: " + scene.Id);
            check(answer.OnSelect.Actions.Length == 1 && answer.OnSelect.Actions[0] is Main.RouteAction action
                && ReferenceEquals(action.Start, scene) && ReferenceEquals(action.Owner, answer),
                "Nurah hub choice does not queue its matching physical scene: " + scene.Id);
        }

        var exits = page.Answers.Select(reference => reference.Get()).OfType<BlueprintAnswer>()
            .Where(answer => answer.ShowConditions.Conditions.Length == 0).ToArray();
        check(exits.Length == 1 && exits[0].SelectConditions.Conditions.Length == 0
            && exits[0].OnSelect.Actions.Length == 0 && exits[0].NextCue.Cues.Count == 0,
            "Nurah's ordinary exit is not available without starting or mutating a scene");
    }
}
