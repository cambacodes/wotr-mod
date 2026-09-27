using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

// E6 (TT-25): story_format.reaction() scenes. The JSON below is verbatim reaction() output (physical and remote).
internal static class ReactionTests
{
    private const string Physical = @"{""Id"": ""irabeth.trickster.dead.reaction_seelah"", ""Title"": ""Seelah's word"", ""Owner"": ""Seelah"", ""MinChapter"": 1, ""MaxChapter"": 5, ""Entry"": ""\""What do you make of what happened?\"""", ""Nodes"": [{""Id"": ""start"", ""Speaker"": ""Seelah"", ""Text"": ""\""You brought her back.\"""", ""Choices"": [{""Text"": ""Continue"", ""Next"": null, ""Set"": [], ""Requires"": [], ""Forbids"": [], ""Abort"": false}], ""Portrait"": """"}], ""Requires"": [""trickster.ever"", ""irabeth.trickster.returned""], ""Forbids"": [""seelah_dead""], ""DelayHours"": 0, ""Optional"": false, ""Relationship"": ""irabeth"", ""Reaction"": true, ""AnswerLists"": [""27c7a3a1c7ad4a74f8e4d7b6a1b0d6c0""]}";
    private const string Remote = @"{""Id"": ""irabeth.trickster.dead.reaction_anevia"", ""Title"": ""Anevia's word"", ""Owner"": ""Anevia"", ""MinChapter"": 1, ""MaxChapter"": 5, ""Entry"": """", ""Nodes"": [{""Id"": ""start"", ""Speaker"": ""Anevia"", ""Text"": ""A letter."", ""Choices"": [{""Text"": ""Continue"", ""Next"": null, ""Set"": [], ""Requires"": [], ""Forbids"": [], ""Abort"": false}], ""Portrait"": """"}], ""Requires"": [""irabeth.trickster.returned""], ""Forbids"": [], ""DelayHours"": 0, ""Optional"": false, ""Relationship"": ""irabeth"", ""Reaction"": true, ""Remote"": true}";

    private static Story Fixture()
    {
        var story = TricksterLatchTests.Fixture();
        story.Relationships["irabeth"].UnavailableOverrides["irabeth_dead"] = "irabeth.trickster.returned";
        story.Relationships["seelah"] = new Relationship { Title = "Seelah", StartedFlag = "seelah.started", ClosedFlag = "seelah.closed",
            CommittedFlag = "seelah.committed", UnavailableFlags = new[] { "seelah_dead" } };
        story.Etudes["seelah_dead"] = "00112233445566778899aabbccddeeff";
        var options = new JsonSerializerOptions { IncludeFields = true };
        story.Scenes.Add(JsonSerializer.Deserialize<Scene>(Physical, options)!);
        story.Scenes.Add(JsonSerializer.Deserialize<Scene>(Remote, options)!);
        // Something else writes the other relationships' flags, so negative fixtures fail only for the reaction rule.
        story.Scenes.Add(new Scene { Id = "seelah.plain", Title = "p", Owner = "Memory", Relationship = "seelah", Remote = true,
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice { Set = new[] { "seelah.closed", "seelah.committed" } } } } } });
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);
        var seelah = story.Scenes.Single(s => s.Id == "irabeth.trickster.dead.reaction_seelah");
        var anevia = story.Scenes.Single(s => s.Id == "irabeth.trickster.dead.reaction_anevia");
        check(seelah.Reaction && anevia.Reaction && anevia.Remote && seelah.AnswerLists.Length == 1, "reaction() JSON shape lost its tags.");

        var state = new Snapshot { Chapter = 5, Hour = 5000 };
        state.Flags.UnionWith(new[] { "trickster.ever", "irabeth.trickster.returned" });
        check(Rules.Available(story, seelah, state) && Rules.Available(story, anevia, state), "Reactions unavailable after the device.");
        var rest = Program.Copy(state);
        rest.Flags.Add("irabeth.trickster.dead.after");
        check(Rules.NextRemote(story, rest) == anevia, "Remote reaction is not delivered at rest.");
        state.Flags.Add("seelah_dead");
        check(!Rules.Available(story, seelah, state), "Reactor's own forbid (reactor dead) ignored.");
        // A reaction never closes: completing it leaves every relationship open.
        var after = Program.Copy(state);
        foreach (var choice in seelah.Nodes.SelectMany(n => n.Choices)) after.Flags.UnionWith(choice.Set);
        check(!story.Relationships.Values.Any(r => after.Has(r.ClosedFlag)), "A reaction closed a relationship.");

        void Invalid(string what, Action<Scene, Story> mutate)
        {
            var bad = Fixture();
            mutate(bad.Scenes.Single(s => s.Id == "irabeth.trickster.dead.reaction_seelah"), bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid reaction accepted: " + what);
        }
        Invalid("closes its own relationship", (s, _) => s.Nodes[0].Choices[0].Set = new[] { "irabeth.closed" });
        Invalid("closes another relationship", (s, _) => s.Nodes[0].Choices[0].Set = new[] { "seelah.closed" });
        Invalid("commits another relationship", (s, _) => s.Nodes[0].Choices[0].Set = new[] { "seelah.committed" });
        Invalid("forbids another romance", (s, _) => s.Forbids = new[] { "seelah.committed" });
        Invalid("choice forbids another closure", (s, _) => s.Nodes[0].Choices[0].Forbids = new[] { "seelah.closed" });
        Invalid("two nodes", (s, _) =>
        {
            s.Nodes[0].Choices[0].Next = "more";
            s.Nodes.Add(new Node { Id = "more", Text = "y", Choices = new List<Choice> { new Choice() } });
        });
        Invalid("physical without an answer list", (s, _) => s.AnswerLists = Array.Empty<string>());
        Invalid("epilogue", (s, _) => { s.Owner = "Epilogue"; s.AnswerLists = Array.Empty<string>(); });
    }
}
