using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E13: entry-answer native effects (EntryMythic, EntryAlignment) and physical Nurah device scenes on explicit lists.
internal static class EntryEffectTests
{
    private static Story Fixture()
    {
        var story = new Story();
        story.Etudes["trickster"] = "9f486a9c0c9abfc4a952bb22e88a7e96";
        story.Relationships["nurah"] = new Relationship { Title = "Nurah", StartedFlag = "nurah.started", ClosedFlag = "nurah.closed",
            CommittedFlag = "nurah.committed", UnavailableFlags = new[] { "nurah.prison" } };
        story.Relationships["nurah"].TricksterAccess["nurah.prison"] = new TricksterAccess { Detect = new[] { "nurah.prison" },
            Device = "nurah.trickster.prison.pardon", Returned = "nurah.trickster.returned" };
        story.Etudes["nurah.prison"] = "0123456789abcdef0123456789abcdef";
        story.Scenes.Add(new Scene
        {
            Id = "nurah.trickster.prison.pardon", Title = "Pardon", Owner = "Nurah", Relationship = "nurah", MinChapter = 3,
            AnswerLists = new[] { "871af36f2ab2b1f40b5de77976c54276" }, TricksterDevice = true, Requires = new[] { "trickster", "nurah.prison" },
            EntryMythic = "PlayerIsTrickster", EntryAlignment = new AlignmentChoice { Direction = "Chaotic", Value = 1 },
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice { Set = new[] { "nurah.trickster.returned" } } } } }
        });
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);
        var pardon = story.Scenes[0];
        check(Rules.EntryTargets(pardon).SequenceEqual(pardon.AnswerLists), "Physical Nurah device lost its explicit answer list.");
        var state = new Snapshot { Chapter = 3, Hour = 10 };
        state.Flags.UnionWith(new[] { "trickster", "nurah.prison" });
        check(Rules.Available(story, pardon, state), "Physical Nurah device unavailable while she is imprisoned.");
        void Invalid(string what, Action<Scene> mutate)
        {
            var bad = Fixture();
            mutate(bad.Scenes[0]);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid scene accepted: " + what);
        }
        // E6: a reaction to her route is spoken by its reactor on the reactor's own list; a non-reaction there is still refused.
        var reacted = Fixture();
        reacted.Scenes.Add(new Scene
        {
            Id = "nurah.trickster.react.irabeth", Title = "Word", Owner = "Irabeth", Relationship = "nurah", MinChapter = 3, Reaction = true,
            AnswerLists = new[] { "871af36f2ab2b1f40b5de77976c54276" }, Requires = new[] { "nurah.trickster.returned" },
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } }
        });
        Rules.Validate(reacted);
        reacted.Scenes[1].Reaction = false;
        bool refused = false;
        try { Rules.Validate(reacted); } catch (InvalidOperationException) { refused = true; }
        check(refused, "A physical non-device Nurah scene on another character's list was accepted.");
        // The hub contract still applies to her ordinary physical scenes.
        Invalid("non-device physical Nurah scene", s => s.TricksterDevice = false);
        Invalid("device without explicit lists", s => s.AnswerLists = Array.Empty<string>());
        Invalid("unknown entry mythic", s => s.EntryMythic = "Trickster");
        Invalid("unknown entry alignment", s => s.EntryAlignment = new AlignmentChoice { Direction = "Up", Value = 1 });
        Invalid("zero entry alignment", s => s.EntryAlignment = new AlignmentChoice { Direction = "Chaotic", Value = 0 });
        Invalid("entry effects on a letter", s => { s.Remote = true; s.AnswerLists = Array.Empty<string>(); s.Relationship = "nurah"; s.TricksterDevice = true; });
    }
}
