using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Quests;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.Localization;
using Newtonsoft.Json.Linq;
using Tirabade;

internal static class KianaNativeTextManagedTests
{
    internal static IEnumerable<string> NativeIds(Story story) => story.NativeTextEdits.Keys.Select(k => k.Split('/')[0]);

    internal static void Seed(Story story, Dictionary<string, JObject> native, Action<bool, string> check)
    {
        foreach (var pair in story.NativeTextEdits)
        {
            var parts = pair.Key.Split('/');
            var data = native[parts[0]];
            check(((string)data["$type"]!).EndsWith(", " + pair.Value.Type, StringComparison.Ordinal), "Wrong Q3 native text type: " + pair.Key);
            check((string)data[parts[1]]!["m_Key"]! == pair.Value.Key, "Q3 localization key drift: " + pair.Key);
            var guid = BlueprintGuid.Parse(parts[0]);
            var blueprint = ResourcesLibrary.TryGetBlueprint(guid);
            if (blueprint == null)
            {
                blueprint = pair.Value.Type switch
                {
                    "BlueprintCue" => new BlueprintCue(),
                    "BlueprintAnswer" => new BlueprintAnswer(),
                    "BlueprintQuest" => new BlueprintQuest(),
                    "BlueprintQuestObjective" => new BlueprintQuestObjective(),
                    _ => throw new InvalidOperationException("Unreviewed Q3 native text type"),
                };
                blueprint.AssetGuid = guid;
                ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(guid, blueprint);
            }
            var field = NativeTextEditRuntime.Field(blueprint, parts[1]);
            if (field == null)
            {
                field = new LocalizedString();
                blueprint.GetType().GetField(parts[1])!.SetValue(blueprint, field);
            }
            typeof(LocalizedString).GetField("m_Key", BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance)!.SetValue(field, pair.Value.Key);
            check(NativeTextEditRuntime.Check(pair.Key, pair.Value, blueprint) == null, "Installed Q3 text field refused: " + pair.Key);
        }
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        foreach (bool loaded in new[] { false, true })
        foreach (bool copyDead in new[] { false, true })
        foreach (bool nativeKilled in new[] { false, true })
        {
            var seen = new PresenceObservation { AreaLoaded = loaded, CopyFound = copyDead,
                CopyAlive = !copyDead, NativeKilled = nativeKilled, NativeHidden = true, ContactAmbiguous = true };
            check(Rules.PresenceKilled(seen) == (loaded && (copyDead || nativeKilled)),
                "Absence/ambiguity fabricated a Kiana death, or confirmed death was lost.");
        }
        var warnings = new List<string>();
        Snapshot? state = null;
        NativeTextEditRuntime.Install(story, () => state,
            guid => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(guid)), warnings.Add);
        check(warnings.Count == 0, "Q3 text attachment refused: " + string.Join("; ", warnings));
        foreach (var pair in story.NativeTextEdits)
        {
            var parts = pair.Key.Split('/');
            var blueprint = ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(parts[0]));
            var field = NativeTextEditRuntime.Field(blueprint, parts[1])!;
            state = null;
            check(NativeTextEditRuntime.Replacement(field) == null, "Q3 text bypasses disabled/no-save observation.");
            state = new Snapshot { Chapter = 5 };
            state.Flags.Add("trickster.now");
            check(NativeTextEditRuntime.Replacement(field) == null, "Current Trickster alone fabricated native history: " + pair.Key);
            foreach (var variant in pair.Value.Variants)
            {
                foreach (var group in variant.When)
                {
                    state = new Snapshot { Chapter = 5 };
                    state.Flags.UnionWith(group.Where(f => !f.StartsWith("!", StringComparison.Ordinal)));
                    check(NativeTextEditRuntime.Replacement(field) == variant.Text, "Runtime Q3 field selected the wrong earned history: " + pair.Key);
                    var earned = NativeTextEditRuntime.Replacement(field);
                    state.Flags.UnionWith(new[] { "kiana.closed", "seelah.closed", "jannah.closed", "arsinoe.closed" });
                    check(NativeTextEditRuntime.Replacement(field) == earned, "Closure erased earned native history: " + pair.Key);
                    state.Flags.Remove("trickster.now");
                    state.Flags.Add("legend");
                    check(NativeTextEditRuntime.Replacement(field) == null, "Runtime Q3 text changes an off-Trickster save.");
                }
            }
            check(field.Key == pair.Value.Key && ReferenceEquals(field, NativeTextEditRuntime.Field(blueprint, parts[1])), "Native localized field was mutated.");
            var unrelated = new LocalizedString();
            typeof(LocalizedString).GetField("m_Key", BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance)!.SetValue(unrelated, pair.Value.Key);
            check(NativeTextEditRuntime.Replacement(unrelated) == null, "Shared localization key changed an unrelated field.");
            var drift = new NativeTextEdit { Type = pair.Value.Type, Key = "drift", Variants = pair.Value.Variants };
            check(NativeTextEditRuntime.Check(pair.Key, drift, blueprint) != null
                && NativeTextEditRuntime.Check(pair.Key, pair.Value, new BlueprintCue()) != null, "Drifted native text evidence was accepted.");
        }
        NativeTextEditRuntime.Install(story, () => throw new InvalidOperationException("observation failed"),
            guid => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(guid)), warnings.Add);
        var first = story.NativeTextEdits.First();
        var firstParts = first.Key.Split('/');
        check(NativeTextEditRuntime.Replacement(NativeTextEditRuntime.Field(ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(firstParts[0])), firstParts[1])!) == null,
            "Q3 text observation failure did not return native text.");
        Console.WriteLine("PASS: installed Q3 dialogue, answers and journal keys; paid/partial/off-path text, native field preservation and observation fallback.");
    }
}
