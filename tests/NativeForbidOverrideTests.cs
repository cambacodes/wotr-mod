using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E3: a ForbidOverride may lift a forbidden native binding (Etudes, SeenCues, ...), in Available and in the
// live contact guard; the override value must stay an authored flag.
internal static class NativeForbidOverrideTests
{
    private const string Contact = "280d4712dceb37f4a88e98f1f4c6e64f";

    private static Story Fixture()
    {
        var story = new Story();
        story.Relationships["seelah"] = new Relationship { Title = "Seelah", StartedFlag = "seelah.started",
            ClosedFlag = "seelah.closed", CommittedFlag = "seelah.committed" };
        story.Etudes["sacrifice"] = "381a296094804761af0893d2e70dc2df";
        story.SeenCues["seelah.parting_seen"] = new[] { "81109ea8fb20dbc478cf67116740f4a1" };
        story.Scenes.Add(new Scene
        {
            Id = "seelah.trickster.parting.letter", Title = "letter", Owner = "Memory", Relationship = "seelah", Remote = true,
            MinChapter = 3, Forbids = new[] { "seelah.parting_seen", "sacrifice" },
            ForbidOverrides = new Dictionary<string, string> { ["seelah.parting_seen"] = "seelah.trickster.primed" },
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice { Set = new[] { "seelah.trickster.primed" } } } } }
        });
        story.Scenes.Add(new Scene
        {
            Id = "seelah.trickster.parting.visit", Title = "visit", Owner = "Seelah", Relationship = "seelah",
            AnswerLists = new[] { "871af36f2ab2b1f40b5de77976c54276" }, ContactUnit = Contact, MinChapter = 3,
            Forbids = new[] { "seelah.parting_seen" },
            ForbidOverrides = new Dictionary<string, string> { ["seelah.parting_seen"] = "seelah.trickster.primed" },
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } }
        });
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);
        var letter = story.Scenes[0];
        var visit = story.Scenes[1];
        var state = new Snapshot { Chapter = 3, Hour = 100 };
        state.AvailableContacts.Add(Contact);
        check(Rules.Available(story, letter, state) && Rules.Available(story, visit, state), "Fixture scenes unavailable in a clean world.");

        state.Flags.Add("seelah.parting_seen");
        check(!Rules.Available(story, letter, state), "Native forbid ignored without its override.");
        check(!Rules.Available(story, visit, state) && !Rules.ContactAvailable(story, visit, state), "Native contact forbid ignored without its override.");

        state.Flags.Add("seelah.trickster.primed");
        check(Rules.Available(story, visit, state), "Native forbid override does not open the scene.");
        check(Rules.ContactAvailable(story, visit, state), "Contact guard ignores the native forbid override.");
        var withLetter = Program.Copy(state);
        withLetter.Flags.Remove("seelah.trickster.primed");
        withLetter.Flags.Remove("seelah.trickster.parting.letter");
        check(!Rules.Available(story, letter, withLetter), "Override applied without its value.");

        // The override lifts only its own key.
        state.Flags.Add("sacrifice");
        check(!Rules.Available(story, letter, state), "Native override lifted an unrelated native forbid.");

        void Invalid(string what, Action<Scene, Story> mutate)
        {
            var bad = Fixture();
            mutate(bad.Scenes[0], bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid native forbid override accepted: " + what);
        }
        Invalid("native value", (s, _) => s.ForbidOverrides["seelah.parting_seen"] = "sacrifice");
        Invalid("runtime-derived value", (s, _) => s.ForbidOverrides["seelah.parting_seen"] = "loss");
        Invalid("unwritten value", (s, _) => s.ForbidOverrides["seelah.parting_seen"] = "seelah.never_written");
        Invalid("closed-flag value", (s, b) =>
        {
            s.Nodes[0].Choices[0].Set = new[] { "seelah.trickster.primed", "seelah.closed" };
            s.ForbidOverrides["seelah.parting_seen"] = "seelah.closed";
        });
        Invalid("runtime-derived key", (s, _) => { s.Forbids = new[] { "loss" }; s.ForbidOverrides.Clear(); s.ForbidOverrides["loss"] = "seelah.trickster.primed"; });
        Invalid("unknown key", (s, _) => { s.Forbids = new[] { "mystery" }; s.ForbidOverrides.Clear(); s.ForbidOverrides["mystery"] = "seelah.trickster.primed"; });
        Invalid("key not forbidden", (s, _) => { s.Forbids = new[] { "seelah.parting_seen" }; s.ForbidOverrides["sacrifice"] = "seelah.trickster.primed"; });
        Invalid("key both native and authored", (s, _) => s.Nodes[0].Choices[0].Set = new[] { "seelah.trickster.primed", "seelah.parting_seen" });
        // Native key with an authored value is accepted (the contract case).
        var ok = Fixture();
        ok.Scenes[0].ForbidOverrides["sacrifice"] = "seelah.trickster.primed";
        Rules.Validate(ok);
    }
}
