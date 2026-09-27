using System;
using System.Collections.Generic;
using Tirabade;

// E14a: Scene.EpilogueSequence places an epilogue page in the native PlayerFinalChoice sequence after an allowed anchor.
internal static class NativeEpilogueTests
{
    internal static void Run(Action<bool, string> check)
    {
        Story Fixture(string owner, string? sequence, string? after)
        {
            var story = new Story();
            story.Relationships["lastcall"] = new Relationship { Title = "Last Call", StartedFlag = "trickster.lastcall.started",
                ClosedFlag = "trickster.lastcall.closed", CommittedFlag = "trickster.lastcall.taken" };
            story.Scenes.Add(new Scene { Id = "trickster.lastcall.a1", Title = "A1", Owner = owner, Relationship = "lastcall", MinChapter = 1, MaxChapter = 6,
                EpilogueSequence = sequence, EpilogueAfter = after,
                Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } } });
            return story;
        }
        Rules.Validate(Fixture("Epilogue", "PlayerFinalChoice", "fb42f8bd123bf1f40a448f6dbc66cbbe"));  // after BookPage_0147
        Rules.Validate(Fixture("LastCallEpilogue", "PlayerFinalChoice", "8f234537d0e0e504ba7fa281f02a3601")); // after BookPage_0115
        foreach (var (owner, sequence, after, what) in new[] {
            ("Epilogue", "Companions", "fb42f8bd123bf1f40a448f6dbc66cbbe", "unknown sequence"),
            ("AeonEpilogue", "PlayerFinalChoice", "fb42f8bd123bf1f40a448f6dbc66cbbe", "Aeon page"),
            ("Memory", "PlayerFinalChoice", "fb42f8bd123bf1f40a448f6dbc66cbbe", "not an epilogue"),
            ("Epilogue", "PlayerFinalChoice", "bfaddf0dbda4724419d597e712a5b322", "anchor not allowed (BookPage_0174 is not a member)"),
            ("Epilogue", "PlayerFinalChoice", (string?)null, "no anchor") })
        {
            bool rejected = false;
            try { Rules.Validate(Fixture(owner, sequence, after)); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid native epilogue target accepted: " + what);
        }
    }
}
