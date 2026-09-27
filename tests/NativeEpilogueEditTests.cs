using System;
using System.Collections.Generic;
using Tirabade;

// E14d: Story.NativeEpilogueEdits validation and When semantics.
internal static class NativeEpilogueEditTests
{
    private const string Cue0409 = "86bf0569a9029ae4b8c9d300a41e5739";

    internal static Story Fixture()
    {
        var story = new Story();
        story.Relationships["wenduag"] = new Relationship { Title = "Wenduag", StartedFlag = "wenduag.started", ClosedFlag = "wenduag.closed", CommittedFlag = "wenduag.committed" };
        story.Etudes["sacrifice"] = "381a296094804761af0893d2e70dc2df";
        story.Scenes.Add(new Scene { Id = "wenduag.lastcall.cue0409", Title = "x", Owner = "Epilogue", Relationship = "wenduag", MinChapter = 1, MaxChapter = 6,
            Nodes = new List<Node> { new Node { Id = "start", Text = "Her pleas were answered sooner than anyone expected.", Choices = new List<Choice> {
                new Choice { Set = new[] { "wenduag.committed" } } } } } });
        story.NativeEpilogueEdits[Cue0409] = new NativeEpilogueEditSpec { Page = "223fd069ee25c784db2df011adbf10f8", Sequence = "fec3b6f28610c8a48a239f148ed3ed60",
            Key = "0dfe0435-8149-466d-bf0c-88d648651c3a", Replacement = "wenduag.lastcall.cue0409",
            When = new[] { new[] { "wenduag.committed", "sacrifice" } } };
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);
        check(Rules.IsNativeReplacement(story, story.Scenes[0]), "Replacement scene not recognized.");
        var state = new Snapshot { Chapter = 6 };
        state.Flags.Add("sacrifice");
        check(!Rules.WhenHolds(story.NativeEpilogueEdits[Cue0409].When, state), "Replacement applies without the commitment (native text must play).");
        state.Flags.Add("wenduag.committed");
        check(Rules.WhenHolds(story.NativeEpilogueEdits[Cue0409].When, state), "Replacement does not apply for the committed partner.");
        void Invalid(string what, Action<Story> mutate)
        {
            var bad = Fixture();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid native epilogue edit accepted: " + what);
        }
        Invalid("unknown replacement", s => s.NativeEpilogueEdits[Cue0409].Replacement = "nobody");
        Invalid("replacement not an epilogue", s => { s.Scenes[0].Owner = "Memory"; s.Scenes[0].Remote = true; });
        Invalid("replacement with two nodes", s => { s.Scenes[0].Nodes[0].Choices[0].Next = "b"; s.Scenes[0].Nodes.Add(new Node { Id = "b", Text = "y", Choices = new List<Choice> { new Choice() } }); });
        Invalid("When without the commitment", s => s.NativeEpilogueEdits[Cue0409].When = new[] { new[] { "sacrifice" } });
        Invalid("empty When", s => s.NativeEpilogueEdits[Cue0409].When = Array.Empty<string[]>());
        Invalid("unknown When flag", s => s.NativeEpilogueEdits[Cue0409].When = new[] { new[] { "wenduag.committed", "never.written" } });
        Invalid("bad cue guid", s => { var e = s.NativeEpilogueEdits[Cue0409]; s.NativeEpilogueEdits.Clear(); s.NativeEpilogueEdits["nope"] = e; });
    }
}
