using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.Localization;
using Newtonsoft.Json.Linq;
using Tirabade;

// E14d: the three reviewed native cues match their evidence in blueprints.zip, and the edit selects exactly one of
// replacement/original, keeping the native checker and falling back to the native text.
internal static class NativeEpilogueEditManagedTests
{
    public static IEnumerable<string> NativeIds => NativeEpilogueEdit.Reviewed.Keys
        .Concat(NativeEpilogueEdit.Reviewed.Values.Select(e => e.Page)).Append(NativeEpilogueEdit.Companions).Distinct();

    private static T Seed<T>(string guid) where T : SimpleBlueprint, new()
    {
        var id = BlueprintGuid.Parse(guid);
        if (ResourcesLibrary.TryGetBlueprint(id) is T prior) return prior;
        var blueprint = new T { AssetGuid = id, name = "NativeFixture_" + guid };
        ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(id, blueprint);
        return blueprint;
    }

    private static BlueprintCueBaseReference Ref(string guid)
    {
        var reference = new BlueprintCueBaseReference();
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!
            .SetValue(reference, BlueprintGuid.Parse(guid));
        return reference;
    }

    public static void Run(Dictionary<string, JObject> native, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        string[] Refs(JObject data, string field) => ((JArray)data[field]!).Select(v => ((string)v!).Replace("!bp_", "")).ToArray();
        var sequence = Seed<BlueprintCueSequence>(NativeEpilogueEdit.Companions);
        if (sequence.Cues.Count == 0) sequence.Cues.AddRange(Refs(native[NativeEpilogueEdit.Companions], "Cues").Select(Ref));
        foreach (var pair in NativeEpilogueEdit.Reviewed)
        {
            var data = native[pair.Key];
            check((string)data["Text"]!["m_Key"]! == pair.Value.Key && !(bool)data["ShowOnce"]! && ((JArray)data["OnShow"]!["Actions"]!).Count == 0
                && ((JArray)data["Answers"]!).Count == 0 && ((JArray)data["Continue"]!["Cues"]!).Count == 0,
                "Reviewed native cue evidence drifted: " + pair.Key);
            check(Refs(native[pair.Value.Page], "Cues").Count(c => c == pair.Key) == 1, "Reviewed cue is not exactly once on its page: " + pair.Key);
            check(Refs(native[NativeEpilogueEdit.Companions], "Cues").Count(c => c == pair.Value.Page) == 1, "Reviewed page is not in CueSequence_Companions: " + pair.Key);
        }
        // Attach on the Wenduag cue with fixture objects shaped like the archive.
        const string cueId = "86bf0569a9029ae4b8c9d300a41e5739";
        var evidence = NativeEpilogueEdit.Reviewed[cueId];
        var page = Seed<BlueprintBookPage>(evidence.Page);
        if (page.Cues.Count == 0) page.Cues.AddRange(Refs(native[evidence.Page], "Cues").Select(Ref));
        var original = Seed<BlueprintCue>(cueId);
        // The host cannot run Owlcat's element reporting (Game.Instance needs Unity), so the native checker is the empty AND,
        // which is how these three cues' checkers evaluate once their own etude conditions hold.
        original.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() };
        original.OnShow = new ActionList { Actions = Array.Empty<GameAction>() };
        original.OnStop = new ActionList { Actions = Array.Empty<GameAction>() };
        original.Continue = new Kingmaker.DialogSystem.CueSelection { Cues = new List<BlueprintCueBaseReference>() };
        original.Text = new LocalizedString();
        typeof(LocalizedString).GetField("m_Key", BindingFlags.Instance | BindingFlags.NonPublic)!.SetValue(original.Text, evidence.Key);
        var spec = new NativeEpilogueEditSpec { Page = evidence.Page, Sequence = evidence.Sequence, Key = evidence.Key, Replacement = "wenduag.lastcall.cue0409",
            When = new[] { new[] { "wenduag.committed" } } };
        check(NativeEpilogueEdit.Check(cueId, spec, g => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(g)), null) == null, "Reviewed evidence refused.");
        check(NativeEpilogueEdit.Check(cueId, new NativeEpilogueEditSpec { Page = evidence.Page, Sequence = evidence.Sequence, Key = "drifted", Replacement = spec.Replacement },
            g => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(g)), null) != null, "Drifted text key accepted.");
        var replacement = Seed<BlueprintCue>(id("native-edit." + cueId).ToString());
        bool applies = false;
        var plan = NativeEpilogueEdit.Prepare(cueId, spec, original, page, replacement, () => applies);
        var before = page.Cues.Select(c => c.Guid).ToArray();
        NativeEpilogueEdit.Attach(plan, Ref(replacement.AssetGuid.ToString()), () => applies);
        int at = Array.IndexOf(before, BlueprintGuid.Parse(cueId));
        check(page.Cues[at].Guid == replacement.AssetGuid && page.Cues.Where(c => c.Guid != replacement.AssetGuid).Select(c => c.Guid).SequenceEqual(before),
            "Replacement not inserted right before the native cue, or native members moved.");
        foreach (var condition in replacement.Conditions.Conditions) { condition.Owner = replacement; condition.name = "$Applies$fixture"; replacement.ElementsArray.Add(condition); }
        bool Shows(BlueprintCue cue) => cue.Conditions.Conditions.All(c => c.Check());
        check(Shows(original) && !Shows(replacement), "Without the earned condition the native cue must play alone.");
        applies = true;
        check(!Shows(original) && Shows(replacement), "With the earned condition the replacement must play alone.");
        check(replacement.Conditions.Conditions.Single() is NativeEpilogueEdit.Applies applied && ReferenceEquals(
            typeof(NativeEpilogueEdit.Applies).GetField("Original", BindingFlags.Instance | BindingFlags.NonPublic)!.GetValue(applied), plan.OriginalChecker),
            "The replacement does not carry the native cue's own checker.");
        Console.WriteLine("PASS: E14d reviewed native cues match blueprints.zip; replacement and original are mutually exclusive.");
    }
}
