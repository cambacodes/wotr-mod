using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class SkillCheckTests
{
    internal static void Run(Action<bool, string> check)
    {
        var roll = new SkillCheck { Skill = "SkillPerception", DC = 25, Success = "found", Failure = "missed" };
        var attempt = new Choice { Check = roll };
        var scene = new Scene { Id = "check_fixture", Owner = "Memory", Nodes = new List<Node> {
            new Node { Id = "start", Text = "Investigate", Choices = new List<Choice> { attempt } },
            new Node { Id = "found", Text = "Find the clue", Choices = new List<Choice> { new Choice { Set = new[] { "clue_found" } } } },
            new Node { Id = "missed", Text = "Follow another lead", Choices = new List<Choice> { new Choice { Set = new[] { "clue_missed" } } } }
        } };
        var story = new Story { Scenes = new List<Scene> { scene } };
        Rules.Validate(story);
        var state = new Snapshot(); state.Flags.Add("konomi.committed");
        var outcomes = Program.Walk(scene, state);
        check(outcomes.Count == 2 && outcomes.All(s => s.Has(scene.Id) && s.Has("konomi.committed")), "Check graph does not preserve both completed paths and unrelated romance.");
        check(outcomes.All(s => s.Has("clue_found") != s.Has("clue_missed")), "Check branches contaminate each other's result.");
        void Invalid(Action change, Action restore)
        {
            change();
            bool rejected = false;
            try { Rules.Validate(story); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Malformed check accepted.");
            restore(); Rules.Validate(story);
        }
        Invalid(() => roll.Skill = "SkillPersuasion", () => roll.Skill = "SkillPerception");
        Invalid(() => roll.DC = 0, () => roll.DC = 25);
        Invalid(() => roll.Failure = "missing", () => roll.Failure = "missed");
        Invalid(() => roll.Failure = "found", () => roll.Failure = "missed");
        Invalid(() => attempt.Next = "found", () => attempt.Next = null);
        Invalid(() => attempt.Abort = true, () => attempt.Abort = false);
        Invalid(() => attempt.Revive = "seelah", () => attempt.Revive = null);
        Invalid(() => scene.Owner = "Epilogue", () => scene.Owner = "Memory");
        Invalid(() => scene.Owner = "AeonEpilogue", () => scene.Owner = "Memory");
    }
}
