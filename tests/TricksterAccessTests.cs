using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

// E7: Relationship.TricksterAccess is verifier metadata (TT-20); Validate checks only its shape.
internal static class TricksterAccessTests
{
    internal static void Run(Action<bool, string> check)
    {
        // Shape written by expansion.normalize_trickster_access (Detect/Device/Returned).
        const string json = @"{""Title"": ""Anevia"", ""StartedFlag"": ""anevia.started"", ""ClosedFlag"": ""anevia.closed"", ""CommittedFlag"": ""anevia.committed"",
            ""UnavailableFlags"": [""anevia_gone""], ""TricksterAccess"": {""anevia_gone"": {""Detect"": [""anevia_gone"", ""!irabeth_dead""],
            ""Device"": ""anevia.trickster.gone.setup"", ""Returned"": ""anevia.trickster.returned""}}}";
        var relationship = JsonSerializer.Deserialize<Relationship>(json, new JsonSerializerOptions { IncludeFields = true })!;
        check(relationship.TricksterAccess["anevia_gone"].Detect.SequenceEqual(new[] { "anevia_gone", "!irabeth_dead" })
            && relationship.TricksterAccess["anevia_gone"].Device == "anevia.trickster.gone.setup", "TricksterAccess did not deserialize.");
        Story Fixture()
        {
            var story = new Story();
            story.Relationships["anevia"] = JsonSerializer.Deserialize<Relationship>(json, new JsonSerializerOptions { IncludeFields = true })!;
            story.Etudes["anevia_gone"] = "09f46662bcd14a03a0874267e16d6e6f";
            story.Scenes.Add(new Scene { Id = "anevia.plain", Title = "x", Owner = "Memory", Relationship = "anevia", Remote = true,
                Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } } });
            return story;
        }
        // Planned device scenes and flags do not exist yet; Validate must not choke on them.
        Rules.Validate(Fixture());
        var state = new Snapshot { Chapter = 3, Hour = 10 };
        var story = Fixture();
        check(Rules.Available(story, story.Scenes[0], state), "Metadata changed availability.");
        state.Flags.Add("anevia_gone");
        check(!Rules.Available(story, story.Scenes[0], state), "Metadata lifted an unavailable flag.");
        void Invalid(string what, Action<Story> mutate)
        {
            var bad = Fixture();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Malformed TricksterAccess accepted: " + what);
        }
        Invalid("null detect", s => s.Relationships["anevia"].TricksterAccess["anevia_gone"].Detect = null!);
        Invalid("blank detect key", s => s.Relationships["anevia"].TricksterAccess["anevia_gone"].Detect = new[] { " " });
        Invalid("null entry", s => s.Relationships["anevia"].TricksterAccess["x"] = null!);
        Invalid("null map", s => s.Relationships["anevia"].TricksterAccess = null!);
    }
}
