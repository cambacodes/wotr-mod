using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// eng7-f6c: each supported dependency uses the production Available-aware
// selector, with native original conditions and earned/off-path negatives.
internal static class EngineF6cNativeTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        using var inventory = NativeContradictionInventoryTests.Load("native_inventory_expectations.json");
        var fixtures = inventory.RootElement.GetProperty("Fixtures");
        var evidence = new Dictionary<string, List<object>>();
        void Case(string finding, string target, string[] flags, string[] playing,
            bool originalExpected = true, bool replacementExpected = true, string[]? answers = null)
        {
            var state = new Snapshot { Chapter = target == "661508b5683d140458f6a0908de98d70" ? 4
                : target == "17249a81e2f0d7d4ca67937db86ef858" || target.StartsWith("c68d") || target.StartsWith("ca71") ? 5 : 6,
                Hour = 100000 };
            state.Flags.UnionWith(flags);
            Rules.Complete(story, state);
            bool original = NativeContradictionInventoryTests.OriginalHolds(
                fixtures.GetProperty(target).GetProperty("Data").GetProperty("Conditions"),
                playing.Concat(story.Etudes.Where(e => state.Has(e.Key)).Select(e => e.Value)),
                answers: answers);
            string? selected = NativeVariantCoverageInventoryTests.Selected(story, target, state, original);
            string? expected = replacementExpected && originalExpected ? story.NativeEpilogueEdits[target].Replacement : null;
            bool passed = original == originalExpected && selected == expected;
            check(passed, "eng7-f6c " + finding + ": " + string.Join(",", flags) + ": " + selected);
            if (!evidence.ContainsKey(target)) evidence[target] = new List<object>();
            evidence[target].Add(new { Name = finding + "/" + string.Join(",", flags), Original = original,
                Selected = selected, Expected = expected, Passed = passed });
            var before = new HashSet<string>(state.Flags);
            NativeVariantCoverageInventoryTests.Selected(story, target, state, original);
            check(before.SetEquals(state.Flags), "eng7-f6c native selection writes outcome evidence");
        }
        void Earned(string finding, string target, string[] earned, string[] playing)
        {
            Case(finding, target, new[] { "trickster" }.Concat(earned).ToArray(), playing);
            Case(finding + "/canon", target, earned, playing, replacementExpected: false);
            // Historical commitment cannot authorize a new current-path act.
            Case(finding + "/converted", target,
                new[] { "trickster", "trickster.ever", "trickster.failed" }.Concat(earned).ToArray(), playing,
                replacementExpected: target.StartsWith("c68d") || target.StartsWith("ca71"));
            Case(finding + "/unearned", target, new[] { "trickster" }, playing, replacementExpected: false);
        }
        // eng7-f6c: a condition-only hide retains the native sequence/once-only history.
        const string funeral = "21b10801b6c2b194d92506a137ef1307";
        var funeralData = fixtures.GetProperty(funeral).GetProperty("Data");
        check(funeralData.GetProperty("ShowOnce").GetBoolean()
            && !funeralData.GetProperty("ShowOnceCurrentDialog").GetBoolean()
            && funeralData.GetProperty("ParentAsset").GetString() == "a52fcdb99e9bfca459613b989a9760f9"
            && funeralData.GetProperty("OnShow").GetProperty("Actions").GetArrayLength() == 0
            && funeralData.GetProperty("OnStop").GetProperty("Actions").GetArrayLength() == 0
            && funeralData.GetProperty("Answers").GetArrayLength() == 0
            && funeralData.GetProperty("Continue").GetProperty("Cues").GetArrayLength() == 0,
            "terendelev:001 hide changes an actionable native cue");
        foreach (bool returned in new[] { false, true })
        foreach (string path in new[] { "canon", "trickster", "converted" })
        foreach (bool scale in new[] { false, true })
        foreach (bool answered in new[] { false, true })
        foreach (bool alreadyShown in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 5 };
            if (returned) state.Flags.Add("terendelev.trickster.returned");
            if (path != "canon") state.Flags.Add("trickster");
            if (path == "converted") state.Flags.UnionWith(new[] { "trickster.ever", "trickster.failed" });
            Rules.Complete(story, state);
            bool original = !alreadyShown && NativeContradictionInventoryTests.OriginalHolds(
                funeralData.GetProperty("Conditions"), Array.Empty<string>(),
                answers: answered ? new[] { "53173097d471d3a45bc31e770e2f35f2" } : Array.Empty<string>(),
                items: scale ? new[] { "816f244523b5455a85ae06db452d4330" } : Array.Empty<string>());
            var before = new HashSet<string>(state.Flags);
            bool hidden = Rules.NativeGateHolds(story, "terendelev.funeral_introduction", state);
            bool expectedHide = returned && path != "canon";
            bool passed = original == (!alreadyShown && scale && !answered) && hidden == expectedHide;
            check(passed && before.SetEquals(state.Flags), "terendelev:001 funeral gate/evidence: " + path);
            if (!evidence.ContainsKey(funeral)) evidence[funeral] = new List<object>();
            evidence[funeral].Add(new { Name = $"terendelev:001/{path}/returned={returned}/scale={scale}/answered={answered}/seen={alreadyShown}",
                Original = original, Selected = original && hidden ? "hidden" : null,
                Expected = original && expectedHide ? "hidden" : null, Passed = passed });
            state.Flags.Add(Rules.DegradedPrefix + "terendelev");
            check(!Rules.NativeGateHolds(story, "terendelev.funeral_introduction", state),
                "terendelev:001 degraded route must retain native checker");
        }
        const string herrax = "661508b5683d140458f6a0908de98d70";
        foreach (string branch in new[] { "lesson_given", "knife_restored" })
            Earned("herrax:" + (branch == "lesson_given" ? "001" : "002"), herrax,
                new[] { "herrax.committed", "herrax.trickster." + branch }, Array.Empty<string>());
        Case("herrax/closed", herrax, new[] { "trickster", "herrax.committed", "herrax.closed" },
            Array.Empty<string>(), replacementExpected: false);

        const string guild = "62f20840e6aa33844b641c5c8e10f814", trio = "8ae3220fd0a645809f59f54f8d89985f";
        foreach (string ending in new[] { "a7ad5a841ace4e3cad533b3b886303ba", "26bf0b163f9c4a078c6c48d93cc0fa76" })
        foreach (string cue in new[] { guild, trio })
        {
            var live = cue == trio ? new[] { ending, "709161cd9da156146ac6e3c394caa854" } : new[] { ending };
            Earned("horzalah:" + (cue == guild ? "001" : "002") + "/" + ending, cue,
                new[] { "horzalah.trickster.primed", "horzalah.trickster.returned", "horzalah.committed" }, live);
            Case("horzalah/missed-escape", cue, new[] { "trickster", "horzalah.trickster.primed" }, live,
                replacementExpected: false);
            Case("horzalah/killed", cue, new[] { "trickster", "horzalah.trickster.primed", "horzalah.trickster.returned", "horzalah.dead" }, live,
                replacementExpected: false);
            Case("horzalah/native-not-selected", cue, new[] { "trickster", "horzalah.trickster.primed", "horzalah.trickster.returned" },
                Array.Empty<string>(), originalExpected: false);
        }
        foreach (string finding in new[] { "irabeth:002", "irabeth:003", "irabeth:004" })
        foreach (bool broken in new[] { false, true })
        {
            string cue = broken ? "2d6b09c6508010e49b882741add89dcf" : "cba964e33d0a0704d847629be452b359";
            string fact = "native.history.irabeth." + (broken ? "broken" : "encouraged");
            string etude = broken ? "7a038ff7b70e91844954407b18e8feb6" : "8b0924efc23df3540b4d8b5fbffd522f";
            Earned(finding, cue, new[] { "irabeth.committed", fact }, new[] { etude });
            Case(finding + "/dead", cue, new[] { "trickster", "irabeth.committed", fact, "irabeth_dead" },
                new[] { etude, "b14e13f9359585e498fcd81ab95d4d7e" }, originalExpected: false);
            var local = story.Scenes.Single(s => s.Id == (finding == "irabeth:002" ? "irabeth.ending_lasting"
                : finding == "irabeth:003" ? "irabeth.ending_unfinished" : "irabeth.ending_ascent"));
            var state = new Snapshot(); state.Flags.Add(fact);
            var paragraphs = Rules.VisibleParagraphs(local.Nodes[0], state);
            check(paragraphs.Any(p => p.Text.Contains(broken ? "River Kingdoms" : "served for years")),
                finding + ": native morale lost in local employment");
            check(!local.Nodes[0].Text.Contains("exactly one more year") && !local.Nodes[0].Text.Contains("keeping her post")
                && !local.Nodes[0].Text.Contains("went back to her post"), finding + ": fixed employment remains");
        }
        const string baph = "17249a81e2f0d7d4ca67937db86ef858";
        Earned("minagho-and-chivarro:005", baph, new[] { "minagho_chivarro.trickster.spared.brand" }, Array.Empty<string>());
        foreach (string excluded in new[] { "3b8c0801d5e9a694b848ee13564d2ad7", "1d466fd4271fdc14ea1c077760c63ca5" })
            Case("minagho/native-exclusion", baph, new[] { "trickster", "minagho_chivarro.trickster.spared.brand" },
                new[] { excluded }, originalExpected: false);

        foreach (string cue in new[] { "c68d9b3a2b887f645ac539f996a63a92", "ca71b79bc9a45b741bcc6599ef017fe7" })
            Earned(cue.StartsWith("c68d") ? "terendelev:002" : "terendelev:003", cue,
                new[] { "terendelev.trickster.returned" }, Array.Empty<string>());
        Case("terendelev/claw-investigation-finished", "c68d9b3a2b887f645ac539f996a63a92",
            new[] { "trickster", "terendelev.trickster.returned" }, Array.Empty<string>(), originalExpected: false,
            answers: new[] { "1e368e69e803b574ab5fb82712dd1f67" });
        var future = fixtures.GetProperty("fd39fd84212de2047b6b887c9a9cf28e").GetProperty("Data");
        check(future.GetProperty("OnSelect").GetProperty("Actions").GetArrayLength() == 0,
            "terendelev:003 future question has unreviewed effects");
        string replacement = story.NativeEpilogueEdits["ca71b79bc9a45b741bcc6599ef017fe7"].Replacement;
        var reply = story.Scenes.Single(s => s.Id == replacement);
        check(reply.Nodes.SelectMany(n => n.Choices).All(c => !c.Set.Contains("terendelev.voice_heard"))
            && story.SeenCues["terendelev.voice_heard"].SequenceEqual(new[] { "ca71b79bc9a45b741bcc6599ef017fe7" }),
            "terendelev:003 returned response manufactures trapped-voice history");
        foreach (var pair in evidence)
            NativeContradictionInventoryTests.Evaluations.Add(new { Target = pair.Key, Passed = true, Cases = pair.Value });
    }
}
