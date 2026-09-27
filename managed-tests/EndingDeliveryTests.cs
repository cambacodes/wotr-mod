using System;
using System.Linq;
using System.Runtime.Serialization;
using HarmonyLib;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.Controllers.Dialog;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.DialogSystem.State;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem;
using Tirabade;

internal static class EndingDeliveryTests
{
    private static bool SkipLog() => false;
    // Keep native PlayCue history writes, but stop before Unity page rendering.
    private static bool SkipRendering(BlueprintBookPage page)
    {
        page.OnShow.Run();
        return false;
    }

    internal static void Run(Story story, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        var instance = AccessTools.Field(typeof(Game), "s_Instance");
        var prior = instance.GetValue(null);
        var harness = new Harmony("RanRomance.Tirabade.EndingDeliveryTests");
        var play = AccessTools.Method(typeof(DialogController), "PlayCue");
        try
        {
            var game = (Game)FormatterServices.GetUninitializedObject(typeof(Game));
            var state = (PersistentState)FormatterServices.GetUninitializedObject(typeof(PersistentState));
            var player = (Player)FormatterServices.GetUninitializedObject(typeof(Player));
            AccessTools.Field(typeof(PersistentState), "PlayerState").SetValue(state, player);
            AccessTools.Field(typeof(Game), "State").SetValue(game, state);
            instance.SetValue(null, game);
            harness.Patch(AccessTools.Method(typeof(DialogController), "PlayBookPage"),
                prefix: new HarmonyMethod(typeof(EndingDeliveryTests), nameof(SkipRendering)));
            harness.Patch(AccessTools.Method(typeof(DialogDebug), "Add",
                new[] { typeof(BlueprintScriptableObject), typeof(string), typeof(UnityEngine.Color) }),
                prefix: new HarmonyMethod(typeof(EndingDeliveryTests), nameof(SkipLog)));
            foreach (var scene in story.Scenes.Where(s => s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)))
            {
                var page = (BlueprintBookPage)ResourcesLibrary.TryGetBlueprint(id("page." + scene.Id + "." + scene.Nodes[0].Id));
                var conditions = page.Conditions;
                var history = new DialogState();
                AccessTools.Field(typeof(Player), "m_Dialog").SetValue(player, history);
                var controller = new DialogController(true);
                try
                {
                    // Route eligibility is covered separately. Isolate native seen-state delivery.
                    page.Conditions = new ConditionsChecker { Conditions = Array.Empty<Condition>() };
                    BlueprintCueSequence Sequence()
                    {
                        var sequence = new BlueprintCueSequence();
                        var reference = new BlueprintCueBaseReference();
                        AccessTools.Field(typeof(BlueprintReferenceBase), "deserializedGuid").SetValue(reference, page.AssetGuid);
                        sequence.Cues.Add(reference);
                        return sequence;
                    }
                    var firstEntry = new CueSequence(Sequence());
                    var secondEntry = new CueSequence(Sequence());
                    check(page.CanShow(), "Unseen ending is suppressed: " + scene.Id);
                    check(ReferenceEquals(firstEntry.PollNextCue(), page), "First sequence skips the unseen ending: " + scene.Id);
                    play.Invoke(controller, new object[] { page });
                    check(history.ShownCues.Contains(page) && controller.LocalShownCues.Contains(page),
                        "Native PlayCue did not record the ending page: " + scene.Id);
                    if (page.Answers.Count == 1 && page.Answers[0].Get() is BlueprintAnswer answer
                        && answer.OnSelect.Actions.Length == 0)
                        answer.OnSelect.Run();
                    controller.LocalShownCues.Clear();
                    check(!page.CanShow(), "A played ending can repeat through another sequence: " + scene.Id);
                    check(secondEntry.PollNextCue() == null, "Second sequence repeats a played ending: " + scene.Id);
                    AccessTools.Field(typeof(Player), "m_Dialog").SetValue(player, new DialogState());
                    check(page.CanShow(), "Ending seen state leaks into a different player's history: " + scene.Id);
                }
                finally { page.Conditions = conditions; }
            }
        }
        finally
        {
            harness.UnpatchAll(harness.Id);
            instance.SetValue(null, prior);
        }
    }
}
