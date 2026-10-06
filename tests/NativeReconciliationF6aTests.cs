using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng7-f6a: real Available-aware selection, including the archive's original checker.
internal static class NativeReconciliationF6aTests
{
    private const string Drawn = "areelu.trickster.graft_drawn";
    private const string Self = "mielarah.trickster.primed.self", Minder = "mielarah.trickster.primed.minder";
    private const string Voyage = "mielarah.voyage_begun";
    private const string Hanging = "dbec675b71e9d5f4d96055f4bb31762e";
    private const string Bread = "ec1219cf3a664baab8987200e0fe1aa7";
    private static readonly (string Target, string Replacement)[] Areelu = {
        ("a9510daab8a04163933d9ecaeffac563", "areelu.trickster.native.crystal_drawn"),
        ("f8d2b851faecddf448fe18db41e17120", "areelu.trickster.native.ascension_shared"),
        ("1c8a6796436a7164fa9d63ec79e0395a", "areelu.trickster.native.ascension_without"),
        ("5b567bdd747e497cb9f6984b1ca1dfc8", "areelu.trickster.afterlogue.former_half_demon"),
        ("0fa64f1d24f706d41b09dee83acf621d", "areelu.trickster.native.cauldron_test")
    };

    // These observations are native GUIDs, kept separate from authored flags.
    private sealed class NativeHistory
    {
        internal HashSet<string> Playing = new(), Completed = new(), Unlocked = new(), Answers = new();
        internal bool Holds(JsonElement checker)
        {
            bool Condition(JsonElement c)
            {
                string Ref(string field) => c.GetProperty(field).GetString()!.Replace("!bp_", "");
                bool result = c.GetProperty("$type").GetString()!.Split(", ").Last() switch {
                    "OrAndLogic" => Holds(c.GetProperty("ConditionsChecker")),
                    "EtudeStatus" when c.GetProperty("Playing").GetBoolean() => Playing.Contains(Ref("m_Etude")),
                    "EtudeStatus" when c.GetProperty("Completed").GetBoolean() => Completed.Contains(Ref("m_Etude")),
                    "FlagUnlocked" => Unlocked.Contains(Ref("m_ConditionFlag")),
                    "AnswerSelected" => Answers.Contains(Ref("m_Answer")),
                    _ => throw new Exception("eng7-f6a: unreviewed native condition " + c)
                };
                return c.GetProperty("Not").GetBoolean() ? !result : result;
            }
            var conditions = checker.GetProperty("Conditions").EnumerateArray().ToArray();
            return checker.GetProperty("Operation").GetString() == "Or" ? conditions.Any(Condition) : conditions.All(Condition);
        }
    }

    private static Snapshot State(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 100000 };
        state.Flags.UnionWith(flags);
        Rules.Complete(story, state);
        return state;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        using var inventory = NativeContradictionInventoryTests.Load("native_inventory_expectations.json");
        var fixtures = inventory.RootElement.GetProperty("Fixtures");
        var evidence = new Dictionary<string, List<object>>();
        void Case(string target, string name, Snapshot state, NativeHistory native, string? expected)
        {
            var before = new HashSet<string>(state.Flags);
            bool original = native.Holds(fixtures.GetProperty(target).GetProperty("Data").GetProperty("Conditions"));
            string? selected = NativeVariantCoverageInventoryTests.Selected(story, target, state, original);
            bool passed = selected == expected;
            check(passed, $"eng7-f6a {target}/{name}: {selected ?? "native"}, expected {expected ?? "native"}");
            check(before.SetEquals(state.Flags), "eng7-f6a: native selection changed history");
            if (!evidence.ContainsKey(target)) evidence[target] = new();
            evidence[target].Add(new { Name = name, Original = original, Selected = selected, Expected = expected, Passed = passed });
        }

        var crystals = new NativeHistory();
        crystals.Completed.Add("57362c5c1e804d5fbef392e4a38a2917");
        foreach (var (target, replacement) in Areelu)
        {
            Case(target, "earned extraction", State(story, 6, "trickster", "trickster.ever", Drawn), crystals, replacement);
            Case(target, "unextracted commitment", State(story, 6, "trickster", "trickster.ever", "areelu.committed"), crystals, null);
            Case(target, "off path", State(story, 6, Drawn), crystals, null);
            Case(target, "former Trickster", State(story, 6, "trickster", "trickster.ever", "trickster.failed", Drawn), crystals, null);
            Case(target, "wrong chapter", State(story, 5, "trickster", "trickster.ever", Drawn), crystals, null);
            var used = State(story, 6, "trickster", "trickster.ever", Drawn);
            used.Flags.Add(replacement);
            Case(target, "already consumed", used, crystals, null);
        }
        // Cue_3's crystal transfer remains conditional on dropped, uncollected native blood.
        Case(Areelu[0].Target, "no dropped crystal", State(story, 6, "trickster", Drawn), new NativeHistory(), null);
        crystals.Unlocked.Add("7c9693a0e30e444c9366b91bbd1ae794");
        Case(Areelu[0].Target, "crystal already collected", State(story, 6, "trickster", Drawn), crystals, null);
        crystals.Unlocked.Clear();
        // Extraction corrects identity even when the player chooses a subsequent death or closes the romance.
        foreach (string fate in new[] { "ascend_all", "ascend_areelu", "ascend_alone", "ascend_companions",
            "areelu.dead_fight", "areelu.incinerated", "areelu.sacrifice_wound", "areelu.sacrifice_before",
            "areelu.sacrifice_trickster", "sacrifice", "areelu.closed", "areelu.trickster.stake_only" })
            Case(Areelu[3].Target, "identity after " + fate, State(story, 6, "trickster", "trickster.ever", Drawn, fate), crystals, Areelu[3].Replacement);

        var breadNative = new NativeHistory();
        breadNative.Playing.Add("b14e13f9359585e498fcd81ab95d4d7e"); // IrabethDead deliberately remains true after return.
        foreach (bool aneviaReturned in new[] { false, true })
        {
            string[] flags = new[] { "trickster", "trickster.ever", "irabeth_dead", "irabeth.trickster.returned" }
                .Concat(aneviaReturned ? new[] { "anevia.trickster.returned", "anevia_gone" } : Array.Empty<string>()).ToArray();
            Case(Bread, "Beth returned; Anevia returned=" + aneviaReturned, State(story, 5, flags), breadNative,
                "anevia.trickster.native.bread_returned");
        }
        Case(Bread, "Beth still dead", State(story, 5, "trickster", "trickster.ever", "irabeth_dead", "anevia.trickster.returned"), breadNative, null);
        Case(Bread, "off path", State(story, 5, "irabeth.trickster.returned"), breadNative, null);
        Case(Bread, "former Trickster", State(story, 5, "trickster", "trickster.ever", "trickster.failed", "irabeth.trickster.returned"), breadNative,
            "anevia.trickster.native.bread_returned");
        foreach (string survival in new[] { "irabeth.trickster.cost.dug_out", "irabeth.trickster.raised_on_record" })
            Case(Bread, "Beth survived without reconciliation: " + survival,
                State(story, 5, "trickster.ever", "trickster.failed", "irabeth_dead", survival), breadNative,
                "anevia.trickster.native.bread_returned");

        var raid = new NativeHistory();
        raid.Answers.Add("1eececde9d7a70c44be526ea668f3ed4");
        raid.Playing.Add("8d0fcb697a43a464fa7119e274bf9d7b");
        foreach (var (flag, suffix) in new[] { (Self, "self"), (Minder, "minder"), (Voyage, "uncertain") })
        {
            Case(Hanging, suffix + " native hanging", State(story, 4, "trickster", "trickster.ever", flag), raid,
                "mielarah.trickster.native.hanging_" + suffix);
            Case(Hanging, suffix + " off path", State(story, 4, flag), raid, null);
            Case(Hanging, suffix + " former Trickster", State(story, 4, "trickster", "trickster.ever", "trickster.failed", flag), raid, null);
            Case(Hanging, suffix + " wrong chapter", State(story, 5, "trickster", flag), raid, null);
        }
        Case(Hanging, "paid late return retains the uncertain native account",
            State(story, 4, "trickster", "trickster.ever", Voyage, "mielarah.trickster.returned"), raid,
            "mielarah.trickster.native.hanging_uncertain");
        Case(Hanging, "no preparation or voyage", State(story, 4, "trickster", "trickster.ever"), raid, null);
        Case(Hanging, "unearned return flag only", State(story, 4, "trickster", "mielarah.trickster.returned"), raid, null);
        raid.Answers.Clear();
        Case(Hanging, "raid not selected", State(story, 4, "trickster", Self, Voyage), raid, null);
        raid.Answers.Add("1eececde9d7a70c44be526ea668f3ed4"); raid.Playing.Clear();
        Case(Hanging, "different captain", State(story, 4, "trickster", Minder, Voyage), raid, null);
        foreach (var pair in evidence)
            NativeContradictionInventoryTests.Evaluations.Add(new { Target = pair.Key, Passed = true, Cases = pair.Value });
    }
}
