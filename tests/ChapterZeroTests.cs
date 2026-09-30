using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E-new 0: the Prologue is chapter 0 (Player.Chapter stays 0 until SetChapter(1)). A scene may open there with MinChapter 0
// or Chapters [0]; the window, the delay and latches behave as in any other chapter, and Chapter 1+ scenes stay shut.
internal static class ChapterZeroTests
{
    private const string List = "a55fc20c6f0ff56439b40d6ba53cb8d7";
    private const string Return = "159c4442a8672334c9394d9579cfd8f9";

    private static Scene Inline(string id, int min, int max, int[]? chapters = null, string[]? requires = null, int delay = 0) => new Scene
    {
        Id = id, Title = id, Owner = "Anevia", Relationship = "zero", MinChapter = min, MaxChapter = max,
        Chapters = chapters ?? Array.Empty<int>(), Requires = requires ?? Array.Empty<string>(), DelayHours = delay,
        AnswerLists = new[] { List }, NativeReturnCue = Return,
        Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice { Set = new[] { id + ".done" } } } } }
    };

    internal static Story Fixture()
    {
        var story = new Story();
        story.Relationships["zero"] = new Relationship { Title = "Zero", StartedFlag = "zero.started",
            ClosedFlag = "zero.closed", CommittedFlag = "zero.committed", UnavailableFlags = new[] { "zero_dead" } };
        story.Etudes["zero_dead"] = "0123456789abcdef0123456789abcdef";
        story.Etudes["zero.native"] = "fedcba9876543210fedcba9876543210";
        story.Latches["zero.ever"] = new[] { "zero.native" };
        story.Scenes.Add(Inline("zero.only", 0, 5, new[] { 0 }));                              // the Prologue only
        story.Scenes.Add(Inline("zero.window", 0, 1));                                         // Prologue through Chapter 1
        story.Scenes.Add(Inline("zero.delayed", 0, 5, requires: new[] { "zero.seen" }, delay: 4));
        story.Scenes.Add(Inline("zero.latched", 1, 5, requires: new[] { "zero.ever" }));        // a Prologue latch, read later
        story.Scenes.Add(Inline("zero.later", 1, 5, requires: new[] { "chapter_later" }));
        story.Scenes.Add(Inline("zero.default", 1, 5));                                        // every existing scene's shape
        return story;
    }

    private static Snapshot At(int chapter, int hour, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = hour };
        state.Flags.UnionWith(flags);
        if (Rules.ChapterFlag(chapter) is string chapterFlag) state.Flags.Add(chapterFlag);   // as Main.State does
        return state;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);
        Scene Get(string id) => story.Scenes.Single(s => s.Id == id);

        // Chapter flags: the Prologue holds neither chapter_one nor chapter_later.
        check(Rules.ChapterFlag(0) == null, "The Prologue (chapter 0) holds a chapter flag.");
        check(Rules.ChapterFlag(1) == "chapter_one", "Chapter 1 does not hold chapter_one.");
        check(Enumerable.Range(2, 5).All(c => Rules.ChapterFlag(c) == "chapter_later"), "Chapters 2-6 do not hold chapter_later.");

        // Window: Chapters [0] opens in the Prologue and never after it; MinChapter 0 spans into Chapter 1.
        check(Rules.Available(story, Get("zero.only"), At(0, 10)), "A Chapters [0] scene is unavailable in the Prologue.");
        check(!Rules.Available(story, Get("zero.only"), At(1, 10)), "A Chapters [0] scene opened in Chapter 1.");
        check(Rules.Available(story, Get("zero.window"), At(0, 10)) && Rules.Available(story, Get("zero.window"), At(1, 10)),
            "A MinChapter 0..1 scene is unavailable in the Prologue or Chapter 1.");
        check(!Rules.Available(story, Get("zero.window"), At(2, 10)), "A MinChapter 0..1 scene opened in Chapter 2.");
        check(!Rules.Available(story, Get("zero.only"), At(0, 10, "zero.only")), "A completed Prologue scene opened again.");

        // Existing scenes (MinChapter 1) stay shut in the Prologue, including a chapter_later gate.
        check(!Rules.Available(story, Get("zero.default"), At(0, 10)), "A MinChapter 1 scene opened in the Prologue.");
        check(Rules.Available(story, Get("zero.default"), At(1, 10)), "Fixture error: a MinChapter 1 scene is shut in Chapter 1.");
        check(!At(0, 10).Has("chapter_later") && !At(0, 10).Has("chapter_one"), "A chapter flag is held in the Prologue.");
        check(!Rules.Available(story, Get("zero.later"), At(0, 10)), "A chapter_later scene opened in the Prologue.");
        check(Rules.Available(story, Get("zero.later"), At(2, 10)), "Fixture error: chapter_later is shut in Chapter 2.");

        // Delay: counted from the Prologue flag's hour, in the Prologue and across SetChapter(1).
        var early = At(0, 12, "zero.seen"); early.Times["zero.seen"] = 10;
        check(!Rules.Available(story, Get("zero.delayed"), early), "A delayed Prologue scene opened before its DelayHours.");
        var due = At(0, 14, "zero.seen"); due.Times["zero.seen"] = 10;
        check(Rules.Available(story, Get("zero.delayed"), due), "A delayed Prologue scene stayed shut after its DelayHours.");
        var carried = At(1, 14, "zero.seen"); carried.Times["zero.seen"] = 10;
        check(Rules.Available(story, Get("zero.delayed"), carried), "A Prologue delay did not carry into Chapter 1.");

        // Latch: observed in the Prologue, recorded, then read in Chapter 1 after its native source is gone.
        var observed = At(0, 10, "zero.native");
        check(Rules.PendingLatches(story, observed).SequenceEqual(new[] { "zero.ever" }), "A Prologue observation is not latched.");
        Rules.Complete(story, observed);
        check(!Rules.Available(story, Get("zero.latched"), observed), "A MinChapter 1 latch reader opened in the Prologue.");
        var after = At(1, 30, "zero.ever");
        Rules.Complete(story, after);
        check(Rules.PendingLatches(story, after).Length == 0 && Rules.Available(story, Get("zero.latched"), after),
            "A Prologue latch is not readable in Chapter 1.");

        // Validate: Chapters [0] needs a window that admits 0.
        var bad = Fixture();
        bad.Scenes.Add(Inline("zero.bad", 1, 5, new[] { 0 }));
        bool rejected = false;
        try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
        check(rejected, "Validate accepted Chapters [0] outside MinChapter 1.");
    }
}
