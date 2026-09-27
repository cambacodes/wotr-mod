using System;
using Tirabade;

internal static class NurahContactEvidenceTests
{
    private static Story Fixture(string evidence)
    {
        var story = new Story();
        story.Relationships.Clear();
        story.Relationships.Add("nurah", new Relationship { Title = "Evidence fixture",
            StartedFlag = "nurah.started", ClosedFlag = "nurah.closed", CommittedFlag = "nurah.complete" });
        story.Scenes.Add(new Scene { Id = "nurah.evidence_fixture", Title = "Evidence fixture", Owner = "Memory",
            Relationship = "nurah", Remote = true, Requires = new[] { evidence },
            Nodes = { new Node { Id = "start", Text = "Fixture", Choices = { new Choice() } } } });
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        // Schema and live-contact policy only; these fixtures do not simulate a native meeting.
        foreach (string evidence in new[] { "nurah.correspondence_available", "nurah.meeting_arrived" })
        {
            var story = Fixture(evidence);
            Rules.Validate(story);
            var scene = story.Scenes[0];
            var state = new Snapshot { Chapter = 5, Hour = 1000 };
            check(!Rules.Available(story, scene, state) && !Rules.ContactAvailable(story, scene, state), "Missing Nurah proof grants contact.");
            state.Flags.Add(evidence);
            check(Rules.Available(story, scene, state) && Rules.ContactAvailable(story, scene, state), "Observed Nurah proof is not readable.");
            scene.Requires = Array.Empty<string>(); scene.Forbids = new[] { evidence };
            check(!Rules.ContactAvailable(story, scene, state), "Nurah observation is not checked as live state.");
            state.Flags.Remove(evidence);
            check(Rules.ContactAvailable(story, scene, state), "Nurah observation remains stale after removal.");
            scene.Forbids = Array.Empty<string>(); scene.Requires = new[] { evidence };
            scene.ContactUnit = "f999fc37ddb225640b7f98c0a05d6948";
            state.Flags.Add(evidence);
            check(!Rules.ContactAvailable(story, scene, state), "Nurah observation fabricates a physical actor.");
            state.AvailableContacts.Add(scene.ContactUnit);
            check(Rules.ContactAvailable(story, scene, state), "Observed Nurah contact cannot satisfy the actor guard.");

            void Reject(Action<Story> mutate, string label)
            {
                var forged = Fixture(evidence); mutate(forged);
                bool rejected = false;
                try { Rules.Validate(forged); } catch (InvalidOperationException) { rejected = true; }
                check(rejected, "Authored Nurah proof accepted through " + label);
            }
            Reject(s => s.Scenes[0].Nodes[0].Choices[0].Set = new[] { evidence }, "choice effects");
            Reject(s => s.Scenes[0].Id = evidence, "scene completion");
            Reject(s => s.Relationships["nurah"].StartedFlag = evidence, "relationship progress");
            const string guid = "f999fc37ddb225640b7f98c0a05d6948";
            Reject(s => s.Etudes[evidence] = guid, "etude alias");
            Reject(s => s.CompletedEtudes[evidence] = guid, "completed-etude alias");
            Reject(s => s.CompletedQuests[evidence] = guid, "quest alias");
            Reject(s => s.SeenCues[evidence] = new[] { guid }, "cue alias");
            Reject(s => s.SelectedAnswers[evidence] = guid, "answer alias");
            Reject(s => s.StartedDialogs[evidence] = guid, "dialogue alias");
        }
    }
}
