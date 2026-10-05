using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng7-f6d: each mapped dependency, original native predicates and real selectors.
internal static class TerendelevNativeDependencyTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        using var inventory = NativeContradictionInventoryTests.Load("native_inventory_expectations.json");
        var fixtures = inventory.RootElement.GetProperty("Fixtures");
        const string returnedFlag = "terendelev.trickster.returned";
        const string funeral = "21b10801b6c2b194d92506a137ef1307";
        const string inquiry = "c68d9b3a2b887f645ac539f996a63a92";
        const string future = "ca71b79bc9a45b741bcc6599ef017fe7";
        const string question = "fd39fd84212de2047b6b887c9a9cf28e";
        var evidence = new Dictionary<string, List<object>>();
        foreach (string target in new[] { funeral, inquiry, future, question }) evidence[target] = new List<object>();
        var authored = story.Scenes.Single(s => s.Id == "terendelev.native.future_question");
        check(authored.AnswerLists.SequenceEqual(new[] { "33501a1edc26b2c4285096b9214c5414" }), "F6d: retired future question lost its saved native list");
        check(authored.ReturnToList && authored.NativeReturnCue == null, "F6d: future question replays the old memory instead of returning to its native list");
        check(!authored.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Set).Any(), "F6d: native correction manufactures route or voice evidence");
        check(!story.NativeGates.Values.Any(g => g.Target == question) && !story.NativeAnswerEdits.ContainsKey(question),
            "Integ3: legitimate native future question was overridden");
        check(!story.SelectedAnswers.Values.Contains(question), "Integ3: corrected future manufactures trapped-voice history");
        foreach (bool path in new[] { false, true })
        foreach (bool returned in new[] { false, true })
        foreach (bool scale in new[] { false, true })
        foreach (bool scaleAnswer in new[] { false, true })
        foreach (bool clawAnswer in new[] { false, true })
        foreach (bool closed in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 5, Hour = 100000 };
            state.Flags.Add("chapter_later"); // Main's Chapter 5 snapshot, including retirement guards.
            if (path) state.Flags.UnionWith(new[] { "trickster", "trickster.ever" });
            if (returned) state.Flags.Add(returnedFlag);
            if (closed) state.Flags.Add("terendelev.closed");
            Rules.Complete(story, state);
            var history = new HashSet<string>();
            if (scaleAnswer) history.Add("53173097d471d3a45bc31e770e2f35f2");
            if (clawAnswer) history.Add("1e368e69e803b574ab5fb82712dd1f67");
            bool Original(string target)
            {
                var data = fixtures.GetProperty(target).GetProperty("Data");
                var conditions = data.GetProperty(target == question ? "ShowConditions" : "Conditions");
                return conditions.GetProperty("Conditions").EnumerateArray().All(c =>
                {
                    string type = c.GetProperty("$type").GetString()!.Split(", ").Last();
                    bool result = type switch
                    {
                        "AnswerSelected" => history.Contains(c.GetProperty("m_Answer").GetString()!.Replace("!bp_", "")),
                        "ItemsEnough" => scale,
                        _ => throw new Exception("F6d: unreviewed original predicate " + type)
                    };
                    return c.GetProperty("Not").GetBoolean() ? !result : result;
                });
            }
            var before = new HashSet<string>(state.Flags);
            foreach (string target in evidence.Keys)
            {
                bool original = Original(target), earned = path && returned;
                string? selected, expected;
                if (target == funeral)
                {
                    selected = original && Rules.NativeGateHolds(story, "terendelev.funeral_introduction", state) ? "hidden" : null;
                    expected = original && earned ? "hidden" : null;
                }
                else if (target == question)
                {
                    selected = story.NativeGates.Values.Any(g => g.Target == question) ? "hidden" : null;
                    expected = null;
                }
                else
                {
                    selected = NativeVariantCoverageInventoryTests.Selected(story, target, state, original);
                    expected = original && earned ? "terendelev.native.eng7_f6c." + (target == inquiry ? "beginning" : "voice") : null;
                }
                bool passed = selected == expected;
                string name = $"F6d {target}: Trickster={path}, return={returned}, scale={scale}, scale answer={scaleAnswer}, claw answer={clawAnswer}, closed={closed}";
                check(passed, name);
                evidence[target].Add(new { Name = name, Original = original, Selected = selected, Expected = expected, Passed = passed });
            }
            check(before.SetEquals(state.Flags), "F6d: selection produces trapped-voice or return history");
            foreach (string retired in new[] { "scale_inquiry", "future_returned", "future_question" })
                check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "terendelev.native." + retired), state),
                    "Integ3: duplicate Terendelev delivery remains selectable: " + retired);
        }
        // eng7-f6d: a text correction is no living audience for an unreturned sacrifice.
        foreach (bool commanderBack in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 6, Hour = 100000 };
            state.Flags.UnionWith(new[] { "trickster", "trickster.ever", returnedFlag, "sacrifice" });
            if (commanderBack) state.Flags.Add("ending.trickster");
            Rules.Complete(story, state);
            foreach (string target in new[] { inquiry, future })
                check((NativeVariantCoverageInventoryTests.Selected(story, target, state, true) != null) == commanderBack,
                    "F6d: unreturned sacrifice receives a living Storyteller correction");
        }
        // A paid historical return stays true after leaving the path; it does
        // not grant a new power. Degraded adapters always preserve the originals.
        var historical = new Snapshot { Chapter = 5, Hour = 100000 };
        historical.Flags.UnionWith(new[] { "trickster.ever", "legend", returnedFlag });
        Rules.Complete(story, historical);
        check(NativeVariantCoverageInventoryTests.Selected(story, inquiry, historical, true) != null,
            "F6d: changing path undoes a paid historical return");
        historical.Flags.Add(Rules.DegradedPrefix + "terendelev");
        check(!Rules.NativeGateHolds(story, "terendelev.funeral_introduction", historical), "F6d: degraded native gate still hides original");
        check(NativeVariantCoverageInventoryTests.Selected(story, inquiry, historical, true) == null,
            "F6d: degraded native selector still overrides original");
        foreach (var pair in evidence)
            NativeContradictionInventoryTests.Evaluations.Add(new { Target = pair.Key, Passed = true, Cases = pair.Value });
        NativeContradictionInventoryTests.WriteEvidence();
    }
}
