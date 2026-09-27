using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E14b: return-to-list inline scenes (native lists without a clean return cue).
internal static class ReturnToListTests
{
    internal static Scene Fixture() => new Scene
    {
        Id = "trickster.lastcall.threshold", Title = "Last Call", Owner = "Commander", Relationship = "lastcall", MinChapter = 6, MaxChapter = 6,
        AnswerLists = new[] { "294126e3264796e488ce19bfb1851355", "16994192cfa484744bd10852b8dc806f" }, ReturnToList = true,
        ReturnText = "{n}The Wound waits.{/n}", Entry = "[Call last orders]", EntryMythic = "PlayerIsTrickster", Requires = new[] { "trickster" },
        Nodes = new List<Node> {
            new Node { Id = "start", Text = "x", Choices = new List<Choice> {
                new Choice { Text = "Drink", Next = "ledger" }, new Choice { Text = "Not yet", Abort = true } } },
            new Node { Id = "ledger", Text = "y", Choices = new List<Choice> { new Choice { Text = "Done", Set = new[] { "trickster.lastcall.taken" } } } } }
    };

    internal static Story Wrap(Scene scene)
    {
        var story = new Story();
        story.Etudes["trickster"] = "9f486a9c0c9abfc4a952bb22e88a7e96";
        story.Relationships["lastcall"] = new Relationship { Title = "Last Call", StartedFlag = "trickster.lastcall.started",
            ClosedFlag = "trickster.lastcall.closed", CommittedFlag = "trickster.lastcall.taken" };
        story.Scenes.Add(scene);
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Wrap(Fixture());
        Rules.Validate(story);
        check(Rules.EntryTargets(story.Scenes[0]).SequenceEqual(story.Scenes[0].AnswerLists), "Return-to-list scene lost its lists.");
        var state = new Snapshot { Chapter = 6, Hour = 10 };
        state.Flags.Add("trickster");
        check(Rules.Available(story, story.Scenes[0], state), "Return-to-list scene unavailable.");
        state.Flags.Add(story.Scenes[0].Id);
        check(!Rules.Available(story, story.Scenes[0], state), "Completed return-to-list scene still offered.");
        var cases = new List<(string, Action<Scene>)>
        {
            ("with a native return cue", s => s.NativeReturnCue = "3ce3b6fad24c6a847903bd85b0e00627"),
            ("remote", s => { s.Remote = true; s.AnswerLists = Array.Empty<string>(); }),
            ("contact unit", s => s.ContactUnit = "280d4712dceb37f4a88e98f1f4c6e64f"),
            ("no lists", s => s.AnswerLists = Array.Empty<string>()),
            ("duplicate lists", s => s.AnswerLists = new[] { "294126e3264796e488ce19bfb1851355", "294126e3264796e488ce19bfb1851355" }),
            ("long return text", s => s.ReturnText = string.Join(" ", Enumerable.Repeat("word", 26))),
            ("native_next", s => s.Nodes[1].Choices[0].NativeNext = "7fbdff975b455454cbaa97542862cf71"),
            ("skill check", s => { s.Nodes[0].Choices[0].Next = null; s.Nodes[0].Choices[0].Check = new SkillCheck { Skill = "CheckBluff", DC = 10, Success = "ledger", Failure = "start" }; }),
            ("return text without the flag", s => s.ReturnToList = false),
        };
        foreach (var (what, mutate) in cases)
        {
            var scene = Fixture();
            mutate(scene);
            bool rejected = false;
            try { Rules.Validate(Wrap(scene)); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid return-to-list scene accepted: " + what);
        }
    }
}
