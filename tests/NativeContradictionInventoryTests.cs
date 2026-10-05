using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text.Json;
using Tirabade;

// eng7-l03: serialized native originals and q6b's actual Available-aware selector.
internal static class NativeContradictionInventoryTests
{
    internal static readonly List<object> Evaluations = new List<object>();
    internal static JsonDocument Load(string name) => JsonDocument.Parse(File.ReadAllText(Path.Combine("tools", name)));

    internal static bool OriginalHolds(JsonElement checker, IEnumerable<string> playing,
        IEnumerable<string>? seen = null, IEnumerable<string>? completed = null, IEnumerable<string>? answers = null,
        IEnumerable<string>? items = null) // eng7-f6c
    {
        var live = new HashSet<string>(playing);
        var cues = new HashSet<string>(seen ?? Array.Empty<string>());
        var quests = new HashSet<string>(completed ?? Array.Empty<string>());
        var selected = new HashSet<string>(answers ?? Array.Empty<string>()); // eng7-f6c
        var inventoryItems = new HashSet<string>(items ?? Array.Empty<string>()); // eng7-f6c
        bool Condition(JsonElement c)
        {
            string type = c.GetProperty("$type").GetString()!.Split(", ").Last();
            string Ref(string key) => c.GetProperty(key).GetString()!.Replace("!bp_", "");
            bool result = type switch
            {
                "EtudeStatus" when c.GetProperty("Playing").GetBoolean() => live.Contains(Ref("m_Etude")),
                "CueSeen" => cues.Contains(Ref("m_Cue")),
                "AnswerSelected" => selected.Contains(Ref("m_Answer")), // eng7-f6c
                "ItemsEnough" when !c.GetProperty("Money").GetBoolean() && c.GetProperty("Quantity").GetInt32() == 1
                    => inventoryItems.Contains(Ref("m_ItemToCheck")), // eng7-f6c: the funeral's single scale
                "QuestStatus" when c.GetProperty("State").GetString() == "Completed" => quests.Contains(Ref("m_Quest")),
                "OrAndLogic" => Checker(c.GetProperty("ConditionsChecker")),
                _ => throw new Exception("Unreviewed native fixture condition: " + type)
            };
            return c.TryGetProperty("Not", out var not) && not.GetBoolean() ? !result : result;
        }
        bool Checker(JsonElement value)
        {
            var conditions = value.GetProperty("Conditions").EnumerateArray().ToArray();
            return value.GetProperty("Operation").GetString() == "Or" ? conditions.Any(Condition) : conditions.All(Condition);
        }
        return Checker(checker);
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        using var doc = Load("native_inventory_expectations.json");
        var root = doc.RootElement;
        check(root.GetProperty("Findings").GetArrayLength() == 45, "Q7-09: mapped finding omitted");
        var fixtures = root.GetProperty("Fixtures");
        foreach (var row in root.GetProperty("Findings").EnumerateArray())
            foreach (var guid in row.GetProperty("Targets").EnumerateArray().Select(g => g.GetString()!))
                check(fixtures.GetProperty(guid).TryGetProperty("Data", out _), "Q7-09: missing original fixture " + guid);
        const string cue = "4bb3706172f1ed54ca11db96254c4638";
        check(story.NativeEpilogueEdits.TryGetValue(cue, out var edit), "Q7-09: existing Wenduag ascension repair missing");
        if (edit == null) return;
        var variants = Rules.EditVariants(edit);
        var scenes = Rules.EditScenes(story, variants);
        var checker = fixtures.GetProperty(cue).GetProperty("Data").GetProperty("Conditions");
        var cases = new List<object>();
        foreach (bool q3 in new[] { false, true })
        foreach (bool path in new[] { false, true })
        foreach (bool committed in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 6 };
            if (path) state.Flags.UnionWith(new[] { "trickster", "trickster.ever" });
            if (committed) state.Flags.Add("wenduag.committed");
            Rules.Complete(story, state);
            bool original = OriginalHolds(checker, Array.Empty<string>(), new[] { "6f95e268d337ddc45be43a11587bc0b6" },
                q3 ? new[] { "5ba83bd1a6b1c884794fbb4858480e7f" } : Array.Empty<string>());
            int index = Rules.SelectNativeEditVariant(story, variants, scenes, state);
            string? selected = original && index >= 0 ? variants[index].Replacement : null;
            string? expected = !q3 && path && committed ? edit.Replacement : null;
            bool passed = selected == expected && original == !q3;
            string name = $"Wenduag Q3={q3}, current Trickster={path}, earned commitment={committed}";
            check(passed, "Q7-09: " + name);
            cases.Add(new { Name = name, Original = original, Selected = selected, Expected = expected, Passed = passed });
        }
        Evaluations.Add(new { Target = cue, Passed = true, Cases = cases });
    }

    internal static void WriteEvidence()
    {
        string? path = Environment.GetEnvironmentVariable("RRT_NATIVE_COVERAGE_OUTPUT");
        if (string.IsNullOrEmpty(path)) return;
        string hash = Convert.ToHexString(SHA256.HashData(File.ReadAllBytes("development/Story.json"))).ToLowerInvariant();
        File.WriteAllText(path, JsonSerializer.Serialize(new { StorySha256 = hash, Evaluations }, new JsonSerializerOptions { WriteIndented = true }));
    }
}
