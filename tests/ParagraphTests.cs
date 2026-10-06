using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E14c: conditional paragraphs on epilogue pages (LastCall_Paragraphs_Nonempty, rules-level).
internal static class ParagraphTests
{
    internal static Scene Page(string text) => new Scene
    {
        Id = "anevia.lastcall.page", Title = "Last Call", Owner = "Epilogue", Relationship = "anevia", MinChapter = 1, MaxChapter = 6,
        Requires = new[] { "lastcall.active", "anevia.committed" },
        Nodes = new List<Node> { new Node { Id = "start", Text = text, Choices = new List<Choice> { new Choice() }, Paragraphs = new List<Paragraph> {
            new Paragraph { Text = "She kept the wardrobe.", Requires = new[] { "anevia.committed" } },
            new Paragraph { Text = "The bottle.", Requires = new[] { "trickster.lastcall.pillar.bottle" } },
            new Paragraph { Text = "The creditors.", AnyGroups = new[] { new[] { "trickster.lastcall.pillar.creditors", "anevia.lastcall.called" } } },
            new Paragraph { Text = "Alone.", Forbids = new[] { "irabeth.trickster.returned" } } } } }
    };

    internal static void Run(Action<bool, string> check)
    {
        Story Wrap(Scene scene)
        {
            var story = new Story();
            story.Relationships["anevia"] = new Relationship { Title = "Anevia", StartedFlag = "anevia.started", ClosedFlag = "anevia.closed", CommittedFlag = "anevia.committed" };
            story.Scenes.Add(scene);
            return story;
        }
        var page = Page("");
        Rules.Validate(Wrap(page));
        var node = page.Nodes[0];
        var state = new Snapshot { Chapter = 6 };
        state.Flags.UnionWith(page.Requires);
        check(Rules.VisibleParagraphs(node, state).SequenceEqual(new[] { node.Paragraphs[0], node.Paragraphs[3] }), "Base world paragraphs wrong.");
        state.Flags.UnionWith(new[] { "trickster.lastcall.pillar.bottle", "anevia.lastcall.called", "irabeth.trickster.returned" });
        check(Rules.VisibleParagraphs(node, state).SequenceEqual(new[] { node.Paragraphs[0], node.Paragraphs[1], node.Paragraphs[2] }),
            "Paragraphs not shown in authored order under their conditions.");
        // LastCall_Paragraphs_Nonempty: every world satisfying the page's Requires shows at least one paragraph.
        var rng = new Random(7);
        var optional = new[] { "trickster.lastcall.pillar.bottle", "trickster.lastcall.pillar.creditors", "anevia.lastcall.called", "irabeth.trickster.returned" };
        for (int i = 0; i < 64; i++)
        {
            var world = new Snapshot { Chapter = 6 };
            world.Flags.UnionWith(page.Requires);
            foreach (var f in optional) if (rng.Next(2) == 0) world.Flags.Add(f);
            check(Rules.VisibleParagraphs(node, world).Length >= 1, "A textless page showed no paragraph.");
        }
        void Invalid(string what, Scene scene)
        {
            bool rejected = false;
            try { Rules.Validate(Wrap(scene)); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid paragraphs accepted: " + what);
        }
        var noGuard = Page("");
        noGuard.Nodes[0].Paragraphs.RemoveAt(0);
        noGuard.Nodes[0].Paragraphs.RemoveAt(2);
        Invalid("textless page that can be empty", noGuard);
        var letter = Page("Some text.");
        letter.Owner = "Memory"; letter.Remote = true;
        Rules.Validate(Wrap(letter));
        check(Rules.VisibleParagraphs(letter.Nodes[0], state).Length == 3, "Non-epilogue paragraphs use different visibility rules.");
        var ordinary = Page("Some text.");
        ordinary.Owner = "Anevia"; ordinary.Nodes[0].Speaker = "Anevia";
        ordinary.AnswerLists = new[] { "0123456789abcdef0123456789abcdef" };
        Rules.Validate(Wrap(ordinary));
        var blank = Page("Some text.");
        blank.Nodes[0].Paragraphs[1].Text = " ";
        Invalid("blank paragraph", blank);
        var emptyGroup = Page("Some text.");
        emptyGroup.Nodes[0].Paragraphs[2].AnyGroups = new[] { Array.Empty<string>() };
        Invalid("empty any-group", emptyGroup);
        Rules.Validate(Wrap(Page("Base text keeps any page non-empty.")));
    }
}
