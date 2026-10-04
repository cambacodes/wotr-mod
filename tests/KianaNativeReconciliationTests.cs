// eng7-f6b: one native dependency contract per Kiana finding 009-032.
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class KianaNativeReconciliationTests
{
    private const string Returned = "kiana.trickster.returned";
    private const string Ransom = "kiana.trickster.guests_ransomed", Bought = "kiana.trickster.guests_bought_back";
    private static readonly HashSet<int> Individual = new HashSet<int> { 10, 11, 17, 18, 23, 25, 26 };
    private static Snapshot State(Story story, params string[] flags)
    {
        var state = new Snapshot { Chapter = 5, Hour = 100000, Area = "2570015799edf594daf2f076f2f975d8" };
        state.Flags.UnionWith(flags);
        Rules.Complete(story, state);
        return state;
    }
    private static bool Original(JsonElement checker, bool eligible)
    {
        // Supply a native history satisfying each reviewed condition. Negating it
        // proves the original eligibility still dominates presentation.
        bool Condition(JsonElement c)
        {
            string type = c.GetProperty("$type").GetString()!.Split(", ").Last();
            bool value = type switch
            {
                "EtudeStatus" => c.GetProperty("Playing").GetBoolean(),
                "CueSeen" => true,
                "AnswerSelected" => true,
                "OrAndLogic" => Checker(c.GetProperty("ConditionsChecker")),
                _ => throw new Exception("Unreviewed Kiana native condition: " + type)
            };
            return c.TryGetProperty("Not", out var not) && not.GetBoolean() ? !value : value;
        }
        bool Checker(JsonElement c)
        {
            var rows = c.GetProperty("Conditions").EnumerateArray();
            // A negated EtudeStatus is supplied as NOT playing in the fixture.
            bool Holds(JsonElement row) => row.GetProperty("$type").GetString()!.EndsWith(", EtudeStatus")
                && row.TryGetProperty("Not", out var not) && not.GetBoolean() ? true : Condition(row);
            return c.GetProperty("Operation").GetString() == "Or" ? rows.Any(Holds) : rows.All(Holds);
        }
        return eligible && Checker(checker);
    }
    internal static void Run(Story story, Action<bool, string> check)
    {
        using var inventory = NativeContradictionInventoryTests.Load("native_inventory_expectations.json");
        var fixtures = inventory.RootElement.GetProperty("Fixtures");
        var rows = inventory.RootElement.GetProperty("Findings").EnumerateArray()
            .Where(r => r.GetProperty("Route").GetString() == "kiana").ToArray();
        check(rows.Length == 24, "eng7-f6b: Kiana dependency omitted");
        foreach (var row in rows)
        {
            string finding = row.GetProperty("Id").GetString()!;
            int num = int.Parse(finding.Split(':')[1]);
            string target = row.GetProperty("Targets")[0].GetString()!;
            bool answer = num is 20 or 21 or 27;
            var data = fixtures.GetProperty(target).GetProperty("Data");
            var cases = new List<object>();
            void Case(string name, Snapshot state, string? expected, bool eligible = true)
            {
                var before = new HashSet<string>(state.Flags);
                bool original = Original(data.GetProperty(answer ? "ShowConditions" : "Conditions"), eligible);
                string? selected = answer ? original && Rules.NativeAnswerHolds(story, target, state) ? "answer" : null
                    : NativeVariantCoverageInventoryTests.Selected(story, target, state, original);
                bool passed = selected == expected;
                check(passed, $"{finding}: {name}: got {selected ?? "native"}, expected {expected ?? "native"}");
                check(before.SetEquals(state.Flags), finding + ": text selection changed native history");
                cases.Add(new { Name = name, Original = original, Selected = selected, Expected = expected, Passed = passed });
            }
            string full = answer ? "answer" : $"kiana.native.q3_reconcile_{num:000}_full";
            string single = $"kiana.native.q3_reconcile_{num:000}_single";
            if (num == 32)
            {
                Case("separated and bereaved", State(story, "trickster", "kiana.separated", "kiana.bereaved"), full);
                Case("separated with native death", State(story, "trickster", "kiana.separated", "seelah.elan_dead"), full);
                Case("native branch not eligible", State(story, "trickster", "kiana.separated", "kiana.bereaved"), null, false);
                Case("degraded", State(story, "trickster", "kiana.separated", "kiana.bereaved", Rules.DegradedPrefix + "kiana"), null);
                var elsewhere = State(story, "trickster", "kiana.separated", "kiana.bereaved");
                elsewhere.Area = "";
                Case("outside the native hospital", elsewhere, null);
                Case("separated but Elan alive", State(story, "trickster", "kiana.separated"), null);
                Case("bereaved but still married", State(story, "trickster", "kiana.bereaved"), null);
            }
            else
            {
                foreach (string paid in new[] { Ransom, Bought })
                {
                    Case(paid, State(story, "trickster", paid), full);
                    Case(paid + " after individual rescue", State(story, "trickster", paid, Returned), full);
                    Case("native branch not eligible", State(story, "trickster", paid), null, false);
                    Case("degraded", State(story, "trickster", paid, Rules.DegradedPrefix + "kiana"), null);
                }
                Case("Kiana alone", State(story, "trickster", Returned), Individual.Contains(num) ? single : null);
            }
            Case("no earned recovery", State(story, "trickster", "kiana.committed", "foresight.page_taken"), null);
            // Test every other current mythic path, including converted/failed Trickster histories.
            foreach (string path in new[] { "angel", "aeon", "azata", "demon", "devil", "dragon", "legend", "lich", "swarm", "trickster.failed" })
                Case("canon " + path, State(story, path, "trickster.ever", Ransom, Returned,
                    "kiana.separated", "kiana.bereaved"), null);
            var closed = State(story, "trickster", Ransom, "kiana.closed");
            var closedBefore = new HashSet<string>(closed.Flags);
            if (answer) Rules.NativeAnswerHolds(story, target, closed);
            else NativeVariantCoverageInventoryTests.Selected(story, target, closed, true);
            check(closedBefore.SetEquals(closed.Flags) && closed.Has("kiana.closed"), finding + ": text edit reopens a closure");
            if (!answer)
            {
                var wrongChapter = State(story, "trickster", Ransom, "kiana.separated", "kiana.bereaved");
                wrongChapter.Chapter = 4;
                Case("before recovery chapter", wrongChapter, null);
                Case("unreturned fatal sacrifice", State(story, "trickster", Ransom, "kiana.separated", "kiana.bereaved", "sacrifice"), null);
            }
            NativeContradictionInventoryTests.Evaluations.Add(new { Target = target, Passed = true, Cases = cases });
        }
        // Original cue identity is essential for both the native hideout answers
        // and the existing read-only native_facts divination observation.
        check(story.SeenCues["native.history.arsinoe.souls_vision_heard"].Contains("a473e5412ffd0f54fbf395770a80a008"),
            "eng7-f6b: divination recollection lost its native_facts source");
        NativeContradictionInventoryTests.WriteEvidence();
        Console.WriteLine("PASS: eng7-f6b Kiana 009-032 native eligibility, paid/individual histories, off-path and closure negatives.");
    }
}
