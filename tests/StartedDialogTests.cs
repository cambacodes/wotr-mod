using System;
using System.Collections.Generic;
using Tirabade;

internal static class StartedDialogTests
{
    internal static void Run(Action<bool, string> check)
    {
        const string guid = "6178470b05c75484085753b821a6a614";
        var scene = new Scene { Id = "visit", Owner = "Memory", Nodes = new List<Node> {
            new Node { Id = "start", Text = "Visit", Choices = new List<Choice> {
                new Choice { Set = new[] { "authored_choice" } }
            } }
        } };
        var story = new Story { Scenes = new List<Scene> { scene } };
        story.StartedDialogs.Add("council_started", guid);
        Rules.Validate(story);

        void Reject(string key, string value)
        {
            story.StartedDialogs.Clear();
            story.StartedDialogs.Add(key, value);
            bool rejected = false;
            try { Rules.Validate(story); }
            catch (InvalidOperationException error) { rejected = error.Message.StartsWith("Invalid started-dialog binding:", StringComparison.Ordinal); }
            check(rejected, "Started-dialog binding can impersonate another state: " + key);
        }

        Reject("council_started", "invalid-guid");
        foreach (string key in new[] { "", "visit", "authored_choice", "committed", "loss", "hour.visit" }) Reject(key, guid);
        story.Etudes.Add("native_etude", guid);
        story.CompletedEtudes.Add("completed_etude", guid);
        story.CompletedQuests.Add("completed_quest", guid);
        story.SelectedAnswers.Add("selected_answer", guid);
        story.SeenCues.Add("seen_cue", new[] { guid });
        foreach (string key in new[] { "native_etude", "completed_etude", "completed_quest", "selected_answer", "seen_cue" }) Reject(key, guid);

        story.StartedDialogs.Clear();
        story.StartedDialogs.Add("council_started", guid);
        Rules.Validate(story);
        var snapshot = new Snapshot { Chapter = 3, Hour = 1000 };
        scene.Requires = new[] { "council_started" };
        check(!Rules.Available(story, scene, snapshot), "Unobserved dialog unlocks a history-dependent scene");
        snapshot.Flags.Add("council_started");
        check(Rules.Available(story, scene, snapshot), "Observed dialog cannot unlock its history-dependent scene");
    }
}
