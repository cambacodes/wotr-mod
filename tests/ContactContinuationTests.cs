using System;
using Tirabade;

internal static class ContactContinuationTests
{
    internal static void Run(Action<bool, string> check)
    {
        const string unit = "32a037e97c3d5c54b85da8f639616c57";
        var story = new Story();
        story.Etudes.Add("native_etude", unit);
        story.CompletedEtudes.Add("native_completed_etude", unit);
        story.CompletedQuests.Add("native_quest", unit);
        story.SeenCues.Add("native_cue", new[] { unit });
        story.SelectedAnswers.Add("native_answer", unit);
        story.StartedDialogs.Add("native_dialog", unit);
        var scene = new Scene { Id = "visit", ContactUnit = unit, DelayHours = 72 };
        var state = new Snapshot { Chapter = 3 };
        state.AvailableContacts.Add(unit);
        foreach (string flag in new[] { "native_etude", "native_completed_etude", "native_quest", "native_cue", "native_answer", "native_dialog" })
        {
            scene.Forbids = new[] { flag };
            check(Rules.ContactAvailable(story, scene, state), "Valid continuation blocked before native change: " + flag);
            state.Flags.Add(flag);
            check(!Rules.ContactAvailable(story, scene, state), "Continuation ignores changed native history: " + flag);
            state.Flags.Remove(flag);
        }
        scene.Forbids = new[] { "closed", "authored_goodbye" };
        state.Flags.UnionWith(scene.Forbids);
        state.Flags.Add(scene.Id);
        state.Times[scene.Id] = state.Hour;
        check(Rules.ContactAvailable(story, scene, state), "Authored closing page reapplies closure, completion or cooldown.");
        state.AvailableContacts.Clear();
        check(!Rules.ContactAvailable(story, scene, state), "Authored goodbye bypasses physical contact loss.");
    }
}
