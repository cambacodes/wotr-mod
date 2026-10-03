using System;
using System.Linq;
using Tirabade;

// Binding context (4), TRICKSTER-RUBRIC: every native edit, suppression and gate requires the Trickster path and is inert on
// the other paths (canon stands there). Each is checked in the world where every positive flag it names holds except
// trickster.ever: nothing is replaced, hidden or gated. With trickster.ever added back, each When group alone holds.
internal static class TricksterOnlyNativeTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Snapshot World(string[][] when, bool trickster)
        {
            var state = new Snapshot { Chapter = 6 };
            state.Flags.UnionWith(when.SelectMany(g => g).Where(f => !f.StartsWith("!", StringComparison.Ordinal)));
            if (trickster) state.Flags.Add(Rules.TricksterPath); else state.Flags.Remove(Rules.TricksterPath);
            return state;
        }
        int count = 0;
        foreach (var pair in story.NativeEpilogueEdits)
            foreach (var variant in Rules.EditVariants(pair.Value))
            {
                count++;
                check(variant.When.All(g => g.Contains(Rules.TricksterPath)), "Native edit " + pair.Key + " / " + variant.Replacement + " has a When group without trickster.ever.");
                check(!Rules.WhenHolds(variant.When, World(variant.When, false)), "Native edit " + pair.Key + " / " + variant.Replacement + " holds off the Trickster path.");
                check(Rules.SelectNativeEditVariant(Rules.EditVariants(pair.Value), World(variant.When, false)) == -1,
                    "Native edit " + pair.Key + " selects a variant off the Trickster path.");
            }
        foreach (var pair in story.NativeEpilogueSuppressions)
        {
            count++;
            check(pair.Value.When.All(g => g.Contains(Rules.TricksterPath)) && !Rules.WhenHolds(pair.Value.When, World(pair.Value.When, false)),
                "Native suppression " + pair.Key + " holds off the Trickster path.");
        }
        foreach (var pair in story.NativeGates)
        {
            count++;
            check(!Rules.NativeGateHolds(story, pair.Key, World(pair.Value.When, false)), "Native gate " + pair.Key + " holds off the Trickster path.");
        }
        foreach (var pair in story.NativeObjectiveSettlements)
        {
            count++;
            check(!Rules.NativeObjectiveSettles(story, pair.Key, World(pair.Value.When, false)), "Native objective settlement " + pair.Key + " holds off the Trickster path.");
            check(Rules.NativeObjectiveSettles(story, pair.Key, World(new[] { pair.Value.When[0] }, true)), "Native objective settlement " + pair.Key + " never holds.");
        }
        check(count > 0, "No native edit, suppression or gate was checked.");
        // Validation refuses an edit group without the Trickster path.
        var copy = System.Text.Json.JsonSerializer.Deserialize<Story>(System.Text.Json.JsonSerializer.Serialize(story,
            new System.Text.Json.JsonSerializerOptions { IncludeFields = true }), new System.Text.Json.JsonSerializerOptions { IncludeFields = true })!;
        var edit = copy.NativeEpilogueEdits.First().Value;
        edit.When = edit.When.Select(g => g.Where(f => f != Rules.TricksterPath).ToArray()).ToArray();
        bool refused = false;
        try { Rules.Validate(copy); } catch (InvalidOperationException) { refused = true; }
        check(refused, "Validation accepted a native edit whose When group lacks trickster.ever.");
    }
}
