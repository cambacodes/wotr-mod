// eng7-f5: serialized regression evidence. Native contract checks use the production adapter,
// compiled by NativeCuePolicyFixtures.csproj; RulesTests also checks the shipped selector inventory.
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;
#if NATIVE_GAME_POLICY
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.Localization;
using Kingmaker.ResourceLinks;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
#endif

internal static class NativeCuePolicyInventoryTests
{
    internal static string Fixture(string name)
    {
        // RulesTests is also run from outside the repo by the coordinator.
        string? dir = Path.GetDirectoryName(Path.GetFullPath(Environment.GetCommandLineArgs().Last()));
        foreach (string root in new[] { Directory.GetCurrentDirectory(), Path.GetFullPath(Path.Combine(dir ?? ".", "..")) })
        {
            string path = Path.Combine(root, "tests", "native-cue-policy-fixtures", name);
            if (File.Exists(path)) return path;
        }
        throw new FileNotFoundException("eng7-f5 fixture missing: " + name);
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        using var cases = JsonDocument.Parse(File.ReadAllText(Fixture("states.json")));
        var rows = cases.RootElement.GetProperty("Cases").EnumerateArray().ToArray();
        check(rows.Select(r => r.GetProperty("Id").GetString()).Distinct().Count() == rows.Length, "F5 duplicate state case id");
        var covered = rows.Select(r => r.GetProperty("ExpectedCandidate").GetString()).ToHashSet();
        check(story.Scenes.Where(s => s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).All(s => covered.Contains(s.Id)),
            "F5 regenerate states.json: authored epilogue/afterlogue inventory incomplete");
        foreach (var pair in story.NativeEpilogueEdits)
        {
            var variants = Rules.EditVariants(pair.Value);
            check(variants.All(v => covered.Contains(v.Replacement)), "F5 native variant missing: " + pair.Key);
            foreach (var row in rows.Where(r => r.GetProperty("Target").GetString() == pair.Key))
            {
                var state = new Snapshot { Chapter = row.GetProperty("Chapter").GetInt32(),
                    Flags = row.GetProperty("Flags").EnumerateArray().Select(f => f.GetString()!).ToHashSet() };
                var scenes = Rules.EditScenes(story, variants);
                // Synthetic flags deliberately include final derived evidence. They never certify campaign progression.
                int selected = Rules.SelectNativeEditVariant(story, variants, scenes, state);
                check(selected < 0 || Rules.Available(story, scenes[selected]!, state), "F5 selected unavailable replacement");
                state.Flags.RemoveWhere(f => f == "trickster" || f.StartsWith("trickster.", StringComparison.Ordinal));
                check(Rules.SelectNativeEditVariant(story, variants, scenes, state) == -1, "F5 off-Trickster native fallthrough: " + pair.Key);
                foreach (var scene in scenes.Where(s => s != null)) state.Flags.Add(Rules.DegradedPrefix + scene!.Relationship);
                check(Rules.SelectNativeEditVariant(story, variants, scenes, state) == -1, "F5 degraded native fallthrough: " + pair.Key);
            }
        }
        using var policy = JsonDocument.Parse(File.ReadAllText(Fixture("policy.json")));
        foreach (var spec in policy.RootElement.GetProperty("Specs").EnumerateObject())
            check(story.NativeEpilogueEdits.ContainsKey(spec.Name), "F5 serialized native target no longer registered: " + spec.Name);
    }

#if NATIVE_GAME_POLICY
    // No game launch, ResourcesLibrary or Unity object factory. Resolve only the serialized fixture objects.
    internal static void RunNative(Action<bool, string> check)
    {
        using var fixture = JsonDocument.Parse(File.ReadAllText(Fixture("policy.json")));
        var root = fixture.RootElement;
        var objects = new Dictionary<string, SimpleBlueprint>();
        static T Reference<T>(string guid) where T : BlueprintReferenceBase, new()
        {
            var reference = new T();
            typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.Public)!
                .SetValue(reference, BlueprintGuid.Parse(guid));
            return reference;
        }
        static BlueprintCueBaseReference Ref(string guid) => Reference<BlueprintCueBaseReference>(guid);
        static string[] Refs(JsonElement element) => element.EnumerateArray().Select(r => r.GetString()!.Replace("!bp_", "")).ToArray();
        static Kingmaker.DialogSystem.CueSelection Selection(JsonElement data) => new Kingmaker.DialogSystem.CueSelection
        { Strategy = Enum.Parse<Kingmaker.DialogSystem.Strategy>(data.GetProperty("Strategy").GetString()!),
          Cues = Refs(data.GetProperty("Cues")).Select(Ref).ToList() };
        foreach (var asset in root.GetProperty("Assets").EnumerateObject())
        {
            var data = asset.Value.GetProperty("data");
            SimpleBlueprint bp;
            switch (asset.Value.GetProperty("type").GetString())
            {
                case "BlueprintCue":
                    var cue = new BlueprintCue { ShowOnce = data.GetProperty("ShowOnce").GetBoolean(),
                        ShowOnceCurrentDialog = data.GetProperty("ShowOnceCurrentDialog").GetBoolean(),
                        Conditions = new ConditionsChecker { Conditions = Array.Empty<Condition>() },
                        OnShow = new ActionList { Actions = Array.Empty<GameAction>() },
                        OnStop = new ActionList { Actions = Array.Empty<GameAction>() }, Continue = Selection(data.GetProperty("Continue")),
                        Text = new LocalizedString() };
                    typeof(LocalizedString).GetField("m_Key", BindingFlags.Instance | BindingFlags.NonPublic)!.SetValue(cue.Text,
                        data.GetProperty("Text").TryGetProperty("m_Key", out var key) && !string.IsNullOrEmpty(key.GetString()) ? key.GetString()
                        : data.GetProperty("Text").TryGetProperty("Shared", out var shared) && shared.ValueKind == JsonValueKind.Object
                            ? shared.GetProperty("stringkey").GetString() : "");
                    cue.Answers.AddRange(Refs(data.GetProperty("Answers")).Select(Reference<BlueprintAnswerBaseReference>));
                    cue.OnShow.Actions = (root.GetProperty("Specs").TryGetProperty(asset.Name, out _) ?
                        data.GetProperty("OnShow").GetProperty("Actions").EnumerateArray().ToArray() : Array.Empty<JsonElement>()).Select(a =>
                    {
                        if (!a.GetProperty("$type").GetString()!.EndsWith(", ChangeBookEventImage", StringComparison.Ordinal))
                            throw new InvalidOperationException("Unreviewed fixture action");
                        var image = new ChangeBookEventImage();
                        typeof(ChangeBookEventImage).GetField("m_Image", BindingFlags.Instance | BindingFlags.NonPublic)!.SetValue(image,
                            new SpriteLink { AssetId = a.GetProperty("m_Image").GetProperty("AssetId").GetString()! });
                        return (GameAction)image;
                    }).ToArray();
                    if (root.GetProperty("Specs").TryGetProperty(asset.Name, out _))
                    {
                        check(data.GetProperty("OnStop").GetProperty("Actions").GetArrayLength() == 0, "Fixture decoder must preserve OnStop");
                        check(data.GetProperty("Components").GetArrayLength() == 0, "Fixture decoder must preserve Components");
                    }
                    bp = cue; break;
                case "BlueprintBookPage": bp = new BlueprintBookPage { Cues = Refs(data.GetProperty("Cues")).Select(Ref).ToList() }; break;
                case "BlueprintCueSequence": bp = new BlueprintCueSequence { Cues = Refs(data.GetProperty("Cues")).Select(Ref).ToList() }; break;
                case "BlueprintAnswer": bp = new BlueprintAnswer { NextCue = Selection(data.GetProperty("NextCue")) }; break;
                case "BlueprintDialog": bp = new BlueprintDialog { FirstCue = Selection(data.GetProperty("FirstCue")) }; break;
                default: throw new InvalidOperationException("Unknown fixture type");
            }
            bp.AssetGuid = BlueprintGuid.Parse(asset.Name); objects[asset.Name] = bp;
        }
        SimpleBlueprint? Resolve(string id) => objects.TryGetValue(id, out var bp) ? bp : null;
        foreach (var row in root.GetProperty("Specs").EnumerateObject())
        {
            var spec = JsonSerializer.Deserialize<NativeEpilogueEditSpec>(row.Value.GetRawText(), new JsonSerializerOptions { IncludeFields = true })!;
            var cue = (BlueprintCue)objects[row.Name];
            check(NativeEpilogueEdit.Check(row.Name, spec, Resolve, null) == null, "Archive fixture refused: " + row.Name);
            var stop = cue.OnStop;
            cue.OnStop = new ActionList { Actions = new GameAction[] { new ChangeBookEventImage() } };
            check(NativeEpilogueEdit.Check(row.Name, spec, Resolve, null) != null, "Unreviewed OnStop accepted: " + row.Name);
            cue.OnStop = stop;
            var saved = cue.Continue;
            cue.Continue = new Kingmaker.DialogSystem.CueSelection { Strategy = Kingmaker.DialogSystem.Strategy.First,
                Cues = new List<BlueprintCueBaseReference> { Ref("00000000000000000000000000000001") } };
            check(NativeEpilogueEdit.Check(row.Name, spec, Resolve, null) != null, "Unreviewed continuation accepted: " + row.Name);
            cue.Continue = saved;
            if (!string.IsNullOrEmpty(spec.Page))
            {
                var page = (BlueprintBookPage)objects[spec.Page];
                page.Cues.Add(Ref(row.Name));
                check(NativeEpilogueEdit.Check(row.Name, spec, Resolve, null) != null, "Duplicate page member accepted: " + row.Name);
                page.Cues.RemoveAt(page.Cues.Count - 1);
            }
            var state = new Snapshot { Chapter = 6 };
            var group = new NativeEpilogueEdit.Group(spec, () => state);
            foreach (var flag in spec.When[0].Where(f => !f.StartsWith("!", StringComparison.Ordinal))) state.Flags.Add(flag);
            check(group.Selected() == -1, "Unattached group hides native fallthrough: " + row.Name);
            group.Enable();
            check(group.Selected() == 0, "First earned variant does not select: " + row.Name);
            state.Flags.Clear();
            check(group.Selected() == -1, "Unpaid state replaces native cue: " + row.Name);
            check(new NativeEpilogueEdit.Group(spec, () => null).Selected() == -1, "Disabled mod does not fall through");
            if (row.Name == "78ae1bdc3b0824b4ca2ed618782f1faa")
            {
                cue.Continue = new Kingmaker.DialogSystem.CueSelection { Strategy = Kingmaker.DialogSystem.Strategy.First,
                    Cues = Refs(root.GetProperty("ParentMutation").GetProperty("Continue")).Select(Ref).ToList() };
                check(NativeEpilogueEdit.Check(row.Name, spec, Resolve, null) == null, "Repaired Cue_0461 parent continuation refused");
                var evidence = NativeEpilogueEdit.Reviewed[row.Name];
                try
                {
                    NativeEpilogueEdit.Reviewed[row.Name] = new NativeEpilogueEdit.Evidence(evidence.Page, evidence.Sequence, evidence.Key, degradeOnRefusal: false);
                    check(NativeEpilogueEdit.Check(row.Name, spec, Resolve, null) != null, "Historical Cue_0461 policy must reject live parent mutation");
                }
                finally { NativeEpilogueEdit.Reviewed[row.Name] = evidence; }
            }
            var replacement = new BlueprintCue();
            var plan = !string.IsNullOrEmpty(spec.Parent)
                ? NativeEpilogueEdit.PrepareInDialog(row.Name, spec, cue, objects[spec.Parent], replacement, () => true)
                : NativeEpilogueEdit.Prepare(row.Name, spec, cue, (BlueprintBookPage)objects[spec.Page], replacement, () => true);
            check(ReferenceEquals(plan.OriginalChecker, cue.Conditions)
                && replacement.Conditions.Conditions.Single() is NativeEpilogueEdit.Applies applies
                && ReferenceEquals(applies.Original, cue.Conditions), "Replacement lost underlying native eligibility: " + row.Name);
            if (!string.IsNullOrEmpty(spec.Parent) || row.Name == "78ae1bdc3b0824b4ca2ed618782f1faa")
                check(replacement.Continue.Cues.Select(r => r.Guid).SequenceEqual(cue.Continue.Cues.Select(r => r.Guid)), "Lost native/parent continuation: " + row.Name);
            foreach (bool keep in new[] { false, true })
                if (NativeEpilogueEdit.Reviewed[row.Name].Image != null)
                {
                    var kept = new NativeEpilogueEditSpec { KeepNativeImage = keep };
                    NativeEpilogueEdit.Prepare(row.Name, kept, cue, (BlueprintBookPage)objects[spec.Page], replacement, () => true);
                    check(keep ? replacement.OnShow.Actions.SequenceEqual(cue.OnShow.Actions) : replacement.OnShow.Actions.Length == 0,
                        "Cue_0310/0311 selected image action differs");
                    if (keep)
                    {
                        var change = (ChangeBookEventImage)cue.OnShow.Actions.Single();
                        var field = typeof(ChangeBookEventImage).GetField("m_Image", BindingFlags.Instance | BindingFlags.NonPublic)!;
                        var image = field.GetValue(change);
                        field.SetValue(change, new SpriteLink { AssetId = "00000000000000000000000000000001" });
                        check(NativeEpilogueEdit.Check(row.Name, spec, Resolve, null) != null, "Drifted native image accepted: " + row.Name);
                        field.SetValue(change, image);
                    }
                }
            cue.Continue = saved;
            cue.ShowOnce = true;
            check(NativeEpilogueEdit.Check(row.Name, spec, Resolve, null) != null, "Drift must refuse to original: " + row.Name);
            check(!NativeEpilogueEdit.DegradesOnRefusal(row.Name), "Warning-only fixture degrades relationship: " + row.Name);
            cue.ShowOnce = false;
        }
    }
#endif
}
