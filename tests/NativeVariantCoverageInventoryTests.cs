using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng7-l03: original native conditions AND When AND Available, using q6b's selector.
internal static class NativeVariantCoverageInventoryTests
{
    private const string Cue = "3a3e561c6b05a284d93eb3bff7b712a6";
    private const string A = "anevia.trickster.returned", B = "irabeth.trickster.returned";
    private const string D = "irabeth.trickster.cost.dug_out", R = "irabeth.trickster.raised_on_record";
    private const string Back = "trickster.commander_back";

    internal static string? Selected(Story story, string cue, Snapshot state, bool original)
    {
        if (!original || !story.NativeEpilogueEdits.TryGetValue(cue, out var edit)) return null;
        var variants = Rules.EditVariants(edit);
        int index = Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), state);
        return index < 0 ? null : variants[index].Replacement;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        using var contracts = NativeContradictionInventoryTests.Load("native_variant_inventory_contracts.json");
        using var inventory = NativeContradictionInventoryTests.Load("native_inventory_expectations.json");
        var fixtures = inventory.RootElement.GetProperty("Fixtures");
        foreach (var legacy in contracts.RootElement.GetProperty("LegacyOrder").EnumerateObject())
        {
            var edit = story.NativeEpilogueEdits[legacy.Name];
            var ids = legacy.Value.EnumerateArray().Select(v => v.GetString()!).ToArray();
            var variants = Rules.EditVariants(edit);
            check(variants.Take(ids.Length).Select(v => v.Replacement).SequenceEqual(ids), "Q7-28: old variant indices changed");
            for (int n = 0; n < ids.Length; n++)
                check(Rules.NativeEditCueName(legacy.Name, edit, n) == "native-edit." + legacy.Name + (n == 0 ? "" : "." + ids[n]),
                    "Q7-28: old native cue save name changed");
        }
        var evidence = new Dictionary<string, List<object>>();
        foreach (var row in contracts.RootElement.GetProperty("Cases").EnumerateArray())
        {
            string cue = row.GetProperty("Target").GetString()!, name = row.GetProperty("Name").GetString()!;
            var state = new Snapshot { Chapter = row.GetProperty("Chapter").GetInt32(), Hour = 100000 };
            foreach (var flag in row.GetProperty("Flags").EnumerateArray().Select(f => f.GetString()!))
                HouseholdTests.Earn(story, state, flag);
            if (state.Flags.Contains("anevia.committed")) HouseholdTests.Earn(story, state, "anevia.payoff.ordinary");
            var before = new HashSet<string>(state.Flags);
            Rules.Complete(story, state);
            var playing = story.Etudes.Where(e => state.Has(e.Key)).Select(e => e.Value).ToList();
            if (row.TryGetProperty("NativePlaying", out var extra)) playing.AddRange(extra.EnumerateArray().Select(g => g.GetString()!));
            bool original = NativeContradictionInventoryTests.OriginalHolds(fixtures.GetProperty(cue).GetProperty("Data").GetProperty("Conditions"), playing);
            string? selected = Selected(story, cue, state, original);
            string? expected = row.GetProperty("Expected").GetString();
            bool passed = selected == expected && original == row.GetProperty("Original").GetBoolean();
            check(passed, $"Q7-28: {name}: original={original}, selected={selected ?? "native"}, expected={expected ?? "native"}");
            var after = new HashSet<string>(state.Flags);
            Selected(story, cue, state, original);
            check(after.SetEquals(state.Flags), "Q7-28: selecting native text mutates run history");
            check(before.Contains(B) || !state.Has(B), "Q7-28: survival grants reconciliation");
            if (!evidence.ContainsKey(cue)) evidence[cue] = new List<object>();
            evidence[cue].Add(new { Name = name, Original = original, Selected = selected, Expected = expected, Passed = passed });
            if (selected != null && state.Has("sacrifice") && !state.Has(Back))
                check(!selected.EndsWith("together") && !selected.EndsWith("widow_committed") && !selected.EndsWith("left_committed"),
                    "Q7-28: dead Commander receives living reunion");
        }
        foreach (var pair in evidence)
            NativeContradictionInventoryTests.Evaluations.Add(new { Target = pair.Key, Passed = true, Cases = pair.Value });
        Sweep(story, check);
        Mutations(story, check);
        NativeContradictionInventoryTests.WriteEvidence();
    }

    private static void Sweep(Story story, Action<bool, string> check)
    {
        // Includes closure, refusal, commitment and every current paid survival
        // history. No row grants a new return or household stance.
        foreach (bool returned in new[] { false, true })
        foreach (string? proof in new string?[] { null, B, D, R })
        foreach (bool committed in new[] { false, true })
        foreach (bool closed in new[] { false, true })
        foreach (bool sacrifice in new[] { false, true })
        foreach (bool commanderReturn in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 6 };
            state.Flags.UnionWith(new[] { "trickster", "trickster.ever", "irabeth_dead", "anevia_gone" });
            if (returned) state.Flags.Add(A);
            if (proof != null) state.Flags.Add(proof);
            if (committed) HouseholdTests.Earn(story, state, "anevia.payoff.ordinary");
            if (closed) state.Flags.UnionWith(new[] { "anevia.closed", "irabeth.closed" });
            if (sacrifice) state.Flags.Add("sacrifice");
            if (commanderReturn) state.Flags.Add("ending.trickster");
            Rules.Complete(story, state);
            string? selected = Selected(story, Cue, state, true);
            check((selected != null) == (returned || proof != null), "Q7-28: paid history falls back to false native disappearance");
            if (proof != null && returned && selected != null)
                check(!selected.Contains("widow"), "Q7-28: surviving Beth selects widow variant");
            if (sacrifice && !state.Has(Back) && returned)
                check(selected != null && selected.Contains("bereavement"), "Q7-28: unreturned sacrifice selects living native correction");
            if (proof == D || proof == R)
            {
                check(!state.Has(B), "Q7-28: refusal is converted into reconciliation");
                check(!Rules.RouteOpen(story.Relationships["irabeth"], state), "Q7-28: text correction reopens Beth's unavailable route");
            }
        }
    }

    private static void Mutations(Story story, Action<bool, string> check)
    {
        // Regressions are tested as failures of the same selection expectation.
        var options = new JsonSerializerOptions { IncludeFields = true };
        Story Copy() => JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(story, options), options)!;
        var state = new Snapshot { Chapter = 6 };
        state.Flags.UnionWith(new[] { "trickster", "trickster.ever", "irabeth_dead", "anevia_gone", A, "sacrifice" });
        Rules.Complete(story, state);
        const string bereavement = "anevia.trickster.epilogue.native_tirabade_bereavement_widow";
        var missing = Copy();
        missing.NativeEpilogueEdits[Cue].Variants = missing.NativeEpilogueEdits[Cue].Variants.Where(v => v.Replacement != bereavement).ToArray();
        check(Selected(missing, Cue, state, true) != bereavement, "Q7-28: missing bereavement mutation escaped");
        var blocked = Copy();
        blocked.Scenes.Single(s => s.Id == bereavement).Forbids = new[] { "sacrifice" };
        check(Selected(blocked, Cue, state, true) != bereavement, "Q7-28: scene availability mutation escaped");
        var unpaid = Program.Copy(state);
        unpaid.Flags.Remove(A);
        check(Selected(story, Cue, unpaid, true) == null, "Q7-28: unpaid return mutation escaped");
        check(Selected(story, Cue, state, false) == null, "Q7-28: ineligible original mutation escaped");
        var degraded = Program.Copy(state);
        degraded.Flags.Add(Rules.DegradedPrefix + "anevia");
        check(Selected(story, Cue, degraded, true) == null, "Q7-28: Available-aware selector bypasses degraded relationship");
        var completed = Program.Copy(state);
        completed.Flags.Add(bereavement);
        check(Selected(story, Cue, completed, true) == null, "Q7-28: consumed replacement is replayed");
        var wrongChapter = Program.Copy(state);
        wrongChapter.Chapter = 5;
        check(Selected(story, Cue, wrongChapter, true) == null, "Q7-28: replacement chapter gate ignored");
        void Reject(string name, Action<Story> mutate)
        {
            var bad = Copy();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Q7-28: native contract mutation accepted: " + name);
        }
        Reject("off-path bereavement", s => s.NativeEpilogueEdits[Cue].Variants.Single(v => v.Replacement == bereavement)
            .When = new[] { new[] { A, "sacrifice" } });
        Reject("unpaid survival", s => s.NativeEpilogueEdits[Cue].Variants.Single(v => v.Replacement.EndsWith("survived_away"))
            .When = new[] { new[] { "trickster.ever", "sacrifice" } });
        Reject("absent snapshot survived flag", s => s.NativeEpilogueEdits[Cue].Variants.Single(v => v.Replacement.EndsWith("survived_away"))
            .When = new[] { new[] { "trickster.ever", "irabeth.trickster.survived" } });
        Reject("paid-survival permission escapes reviewed cue", s => {
            var edit = s.NativeEpilogueEdits[Cue];
            s.NativeEpilogueEdits.Remove(Cue);
            s.NativeEpilogueEdits["00000000000000000000000000000001"] = edit;
        });
        // A matching When is insufficient: scene prerequisites remain part of selection.
        var unmet = Copy();
        unmet.Scenes.Single(s => s.Id == bereavement).Requires = new[] { B };
        check(Selected(unmet, Cue, state, true) == null, "Q7-28: scene Requires mutation escaped");
    }
}
