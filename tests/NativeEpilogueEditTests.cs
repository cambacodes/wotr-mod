using System;
using System.Collections.Generic;
using System.Linq;
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

        // E14d extension: ordered variants, fate-defied When groups (a Trickster return flag instead of the commitment).
        var variantStory = VariantFixture();
        Rules.Validate(variantStory);
        var edit = variantStory.NativeEpilogueEdits[Cue0409];
        var variants = Rules.EditVariants(edit);
        check(variants.Length == 3 && variants[0].Replacement == "wenduag.lastcall.cue0409" && variants[2].KeepNativeImage,
            "Edit variants are not the spec's own replacement followed by Variants in order.");
        check(Rules.IsNativeReplacement(variantStory, variantStory.Scenes.Single(s => s.Id == "wenduag.native.back")), "Variant replacement not recognized.");
        var world = new Snapshot { Chapter = 6 };
        check(Rules.SelectNativeEditVariant(variants, world) == -1, "A variant applies without a commitment or a return.");
        world.Flags.Add("wenduag.trickster.returned");
        check(Rules.SelectNativeEditVariant(variants, world) == 2, "The fate-defied variant does not apply after the return.");
        world.Flags.Add("wenduag.committed");
        check(Rules.SelectNativeEditVariant(variants, world) == 1, "The earlier (more specific) variant does not win.");
        world.Flags.Add("sacrifice");
        check(Rules.SelectNativeEditVariant(variants, world) == 0, "Variant 0 does not win when it holds.");
        check(Rules.NativeEditCueName(Cue0409, edit, 0) == "native-edit." + Cue0409
              && Rules.NativeEditCueName(Cue0409, edit, 2) == "native-edit." + Cue0409 + ".wenduag.native.back", "Variant cue names changed.");
        void InvalidVariant(string what, Action<Story> mutate)
        {
            var bad = VariantFixture();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid native epilogue variant accepted: " + what);
        }
        InvalidVariant("null variant", s => s.NativeEpilogueEdits[Cue0409].Variants = new NativeEpilogueVariant[] { null! });
        InvalidVariant("null Variants", s => s.NativeEpilogueEdits[Cue0409].Variants = null!);
        InvalidVariant("unknown variant replacement", s => s.NativeEpilogueEdits[Cue0409].Variants[0].Replacement = "nobody");
        InvalidVariant("replacement used twice", s => s.NativeEpilogueEdits[Cue0409].Variants[0].Replacement = "wenduag.lastcall.cue0409");
        InvalidVariant("variant When without commitment or return", s => s.NativeEpilogueEdits[Cue0409].Variants[1].When = new[] { new[] { "sacrifice" } });
        InvalidVariant("variant with empty When", s => s.NativeEpilogueEdits[Cue0409].Variants[1].When = Array.Empty<string[]>());
        InvalidVariant("return flag of another relationship", s =>
        {
            s.Relationships["anevia"] = new Relationship { Title = "Anevia", StartedFlag = "anevia.started", ClosedFlag = "anevia.closed", CommittedFlag = "anevia.committed",
                TricksterAccess = new Dictionary<string, TricksterAccess> { ["gone"] = new TricksterAccess { Returned = "anevia.trickster.returned" } } };
            s.Scenes.Add(new Scene { Id = "anevia.set", Title = "x", Owner = "Anevia", Relationship = "anevia", MinChapter = 1, MaxChapter = 6, Remote = true,
                Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice { Set = new[] { "anevia.trickster.returned" } } } } } });
            s.NativeEpilogueEdits[Cue0409].Variants[1].When = new[] { new[] { "anevia.trickster.returned" } };
        });

        // E14d extension: "!flag" members (absent flag) and suppressions (a native cue hidden, no text of its own).
        var negated = VariantFixture();
        negated.NativeEpilogueEdits[Cue0409].Variants[1].When = new[] { new[] { "wenduag.trickster.returned", "!sacrifice" } };
        Rules.Validate(negated);
        var probe = new Snapshot { Chapter = 6 };
        probe.Flags.Add("wenduag.trickster.returned");
        check(Rules.WhenHolds(negated.NativeEpilogueEdits[Cue0409].Variants[1].When, probe), "A !flag member does not hold while the flag is absent.");
        probe.Flags.Add("sacrifice");
        check(!Rules.WhenHolds(negated.NativeEpilogueEdits[Cue0409].Variants[1].When, probe), "A !flag member holds while the flag is present.");
        InvalidVariant("a group earned only by a negated commitment", s => s.NativeEpilogueEdits[Cue0409].Variants[0].When = new[] { new[] { "!wenduag.committed" } });
        InvalidVariant("negated unknown flag", s => s.NativeEpilogueEdits[Cue0409].Variants[0].When = new[] { new[] { "wenduag.committed", "!never.written" } });
        InvalidVariant("double negation", s => s.NativeEpilogueEdits[Cue0409].Variants[0].When = new[] { new[] { "wenduag.committed", "!!sacrifice" } });
        Story Suppressed()
        {
            var s = VariantFixture();
            s.NativeEpilogueSuppressions["3617a648c06a45d1807fde65aedafb06"] = new NativeEpilogueSuppressionSpec { Page = "503164ff04ac64543ba42561ea9f970f",
                Sequence = "fec3b6f28610c8a48a239f148ed3ed60", Key = "de512bb2-4d4d-4ca2-b20d-9b2d6384c802", Relationship = "wenduag",
                When = new[] { new[] { "wenduag.committed", "!sacrifice" } } };
            return s;
        }
        Rules.Validate(Suppressed());
        void InvalidSuppression(string what, Action<Story> mutate)
        {
            var bad = Suppressed();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid native epilogue suppression accepted: " + what);
        }
        const string Cue16 = "3617a648c06a45d1807fde65aedafb06";
        InvalidSuppression("unknown relationship", s => s.NativeEpilogueSuppressions[Cue16].Relationship = "nobody");
        InvalidSuppression("When without commitment or return", s => s.NativeEpilogueSuppressions[Cue16].When = new[] { new[] { "sacrifice" } });
        InvalidSuppression("empty When", s => s.NativeEpilogueSuppressions[Cue16].When = Array.Empty<string[]>());
        InvalidSuppression("empty group", s => s.NativeEpilogueSuppressions[Cue16].When = new[] { Array.Empty<string>() });
        InvalidSuppression("unknown flag", s => s.NativeEpilogueSuppressions[Cue16].When = new[] { new[] { "wenduag.committed", "never.written" } });
        InvalidSuppression("page not a GUID", s => s.NativeEpilogueSuppressions[Cue16].Page = "BookPage_0347");
        InvalidSuppression("cue also edited", s => { var spec = s.NativeEpilogueSuppressions[Cue16]; s.NativeEpilogueSuppressions.Clear();
            s.NativeEpilogueSuppressions[Cue0409] = spec; });
        InvalidSuppression("null spec", s => s.NativeEpilogueSuppressions[Cue16] = null!);

        // E14i: a common-dialog cue (Parent + Dialog, no page or sequence, no kept picture), and the R2-6 late commitment.
        Story InDialog()
        {
            var s = VariantFixture();
            var e = s.NativeEpilogueEdits[Cue0409];
            s.NativeEpilogueEdits.Remove(Cue0409);
            e.Page = ""; e.Sequence = ""; e.Parent = "5b567bdd747e497cb9f6984b1ca1dfc8"; e.Dialog = "57e18f5158904030a84a772fb361ceb4";
            e.Variants = e.Variants.Take(1).ToArray();
            s.NativeEpilogueEdits["825786e8c5db4511ae30950bb286f0e9"] = e;
            s.Derived["wenduag.trickster.late_committed"] = new[] { new[] { "sacrifice" } };
            return s;
        }
        Rules.Validate(InDialog());
        void InvalidDialog(string what, Action<NativeEpilogueEditSpec> mutate)
        {
            var bad = InDialog();
            mutate(bad.NativeEpilogueEdits["825786e8c5db4511ae30950bb286f0e9"]);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid E14i dialog edit accepted: " + what);
        }
        InvalidDialog("a page as well", e => e.Page = "503164ff04ac64543ba42561ea9f970f");
        InvalidDialog("a sequence as well", e => e.Sequence = "fec3b6f28610c8a48a239f148ed3ed60");
        InvalidDialog("parent not a GUID", e => e.Parent = "Cue_0001");
        InvalidDialog("no dialog", e => e.Dialog = "");
        InvalidDialog("a kept picture", e => e.KeepNativeImage = true);
        var late = InDialog();
        late.NativeEpilogueEdits["825786e8c5db4511ae30950bb286f0e9"].When = new[] { new[] { "wenduag.trickster.late_committed", "!sacrifice" } };
        Rules.Validate(late);
        var unearned = InDialog();
        unearned.Derived.Remove("wenduag.trickster.late_committed");
        unearned.Derived["wenduag.late"] = new[] { new[] { "sacrifice" } };
        unearned.NativeEpilogueEdits["825786e8c5db4511ae30950bb286f0e9"].When = new[] { new[] { "wenduag.late" } };
        bool refused = false;
        try { Rules.Validate(unearned); } catch (InvalidOperationException) { refused = true; }
        check(refused, "A derived key other than <relationship>.trickster.late_committed earned a native edit.");
    }

    // Wenduag's cue with two extra variants: committed (no sacrifice), and returned (fate defied, uncommitted, keeps the image).
    private static Story VariantFixture()
    {
        var story = Fixture();
        story.Relationships["wenduag"].TricksterAccess["gone"] = new TricksterAccess { Detect = new[] { "sacrifice" }, Returned = "wenduag.trickster.returned" };
        story.Scenes[0].Nodes[0].Choices[0].Set = new[] { "wenduag.committed", "wenduag.trickster.returned" };
        foreach (var id in new[] { "wenduag.native.committed", "wenduag.native.back" })
            story.Scenes.Add(new Scene { Id = id, Title = "x", Owner = "WenduagEpilogue", Relationship = "wenduag", MinChapter = 6, MaxChapter = 99,
                Nodes = new List<Node> { new Node { Id = "page", Text = "Text for " + id, Choices = new List<Choice> { new Choice() } } } });
        story.NativeEpilogueEdits[Cue0409].Variants = new[]
        {
            new NativeEpilogueVariant { Replacement = "wenduag.native.committed", When = new[] { new[] { "wenduag.committed" } } },
            new NativeEpilogueVariant { Replacement = "wenduag.native.back", When = new[] { new[] { "wenduag.trickster.returned" } }, KeepNativeImage = true },
        };
        return story;
    }
}
