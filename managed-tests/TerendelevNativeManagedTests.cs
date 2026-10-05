using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Newtonsoft.Json.Linq;
using Tirabade;

// eng7-f6d: real game blueprint/action objects for the two new reviewed policies.
internal static class TerendelevNativeManagedTests
{
    private const BindingFlags Fields = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
    private static T Ref<T>(string value) where T : BlueprintReferenceBase, new()
    {
        var result = new T();
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", Fields)!.SetValue(result, BlueprintGuid.Parse(value.Replace("!bp_", "")));
        return result;
    }
    private static void Reference(object value, string field, string guid)
    {
        var info = value.GetType().GetField(field, Fields)!;
        var reference = (BlueprintReferenceBase)Activator.CreateInstance(info.FieldType)!;
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", Fields)!.SetValue(reference, BlueprintGuid.Parse(guid.Replace("!bp_", "")));
        info.SetValue(value, reference);
    }
    private static Dictionary<string, SimpleBlueprint> Gates(Dictionary<string, JObject> native, Action<bool, string> check)
    {
        const string funeral = "21b10801b6c2b194d92506a137ef1307", question = "fd39fd84212de2047b6b887c9a9cf28e";
        var cue = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(funeral), ShowOnce = (bool)native[funeral]["ShowOnce"]! };
        NativeEpilogueEditManagedTests.LoadArchiveShape(cue, native[funeral], check);
        var parts = (JArray)native[funeral]["Conditions"]!["Conditions"]!;
        var answer = new AnswerSelected { Not = (bool)parts[0]["Not"]!, CurrentDialog = (bool)parts[0]["CurrentDialog"]! };
        Reference(answer, "m_Answer", (string)parts[0]["m_Answer"]!);
        var item = new ItemsEnough { Not = (bool)parts[1]["Not"]!, Money = (bool)parts[1]["Money"]!, Quantity = (int)parts[1]["Quantity"]! };
        Reference(item, "m_ItemToCheck", (string)parts[1]["m_ItemToCheck"]!);
        cue.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = new Condition[] { answer, item } };
        var oldQuestion = new BlueprintAnswer { AssetGuid = BlueprintGuid.Parse(question),
            ShowConditions = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() },
            SelectConditions = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() },
            OnSelect = new ActionList { Actions = Array.Empty<GameAction>() },
            NextCue = new CueSelection { Strategy = Strategy.First, Cues = ((JArray)native[question]["NextCue"]!["Cues"]!).Select(v => Ref<BlueprintCueBaseReference>((string)v!)).ToList() } };
        oldQuestion.Text = new Kingmaker.Localization.LocalizedString();
        typeof(Kingmaker.Localization.LocalizedString).GetField("m_Key", Fields)!.SetValue(oldQuestion.Text, (string)native[question]["Text"]!["m_Key"]!);
        return new Dictionary<string, SimpleBlueprint> { [funeral] = cue, [question] = oldQuestion };
    }
    internal static void Seed(Dictionary<string, JObject> native, Action<bool, string> check)
    {
        foreach (var pair in Gates(native, check))
            ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(BlueprintGuid.Parse(pair.Key), pair.Value);
    }
    private sealed class Truth : Condition
    {
        internal bool Value;
        protected override string GetConditionCaption() => "F6d original predicate";
        protected override bool CheckCondition() => Value;
    }
    private static bool SkipProfiling() => false;   // Unity profiler calls are ECalls the Windows host cannot run (ConditionsChecker.Check)
    internal static void Run(Story story, Dictionary<string, JObject> native, Action<bool, string> check)
    {
        var harness = new HarmonyLib.Harmony("RanRomance.Tirabade.TerendelevNativeManagedTests");
        try
        {
            foreach (var typeName in new[] { "Kingmaker.Utility.ProfileScope", "Kingmaker.ElementsSystem.ElementsDebugScope" })
            {
                var type = HarmonyLib.AccessTools.TypeByName(typeName);
                var methods = (type?.GetMethods(BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic) ?? Array.Empty<MethodInfo>())
                    .Where(m => m.Name == "New" || m.Name == "Open").ToArray();
                check(methods.Length > 0, "F6d host cannot stub " + typeName);
                foreach (var method in methods) harness.Patch(method, prefix: new HarmonyLib.HarmonyMethod(typeof(TerendelevNativeManagedTests), nameof(SkipProfiling)));
            }
            RunGates(story, native, check);
        }
        finally { harness.UnpatchAll("RanRomance.Tirabade.TerendelevNativeManagedTests"); }
    }
    private static void RunGates(Story story, Dictionary<string, JObject> native, Action<bool, string> check)
    {
        foreach (string gate in new[] { "terendelev.scale_funeral", "terendelev.trapped_future" })
        {
            var world = Gates(native, check);
            var spec = story.NativeGates[gate];
            SimpleBlueprint? Resolve(string id) => world.TryGetValue(id, out var blueprint) ? blueprint : null;
            check(NativeGate.Check(gate, spec, Resolve, out var owner, out var checkers) == null, "F6d native gate refused archive: " + gate);
            if (owner is BlueprintCue funeral)
            {
                funeral.ShowOnce = false;
                check(NativeGate.Check(gate, spec, Resolve, out _, out _) != null, "F6d funeral drift accepted");
                funeral.ShowOnce = true;
            }
            else
            {
                var question = (BlueprintAnswer)owner!;
                question.NextCue.Cues.Clear();
                check(NativeGate.Check(gate, spec, Resolve, out _, out _) != null, "F6d question continuation drift accepted");
            }
            var original = new Truth();
            var checker = checkers[0];
            checker.Conditions = new Condition[] { original };
            Snapshot? state = null;
            NativeGate.Attach(owner!, checker, () => state != null && Rules.NativeGateHolds(story, gate, state));
            foreach (bool path in new[] { false, true })
            foreach (bool returned in new[] { false, true })
            foreach (bool eligible in new[] { false, true })
            {
                state = new Snapshot { Chapter = 5 };
                if (path) state.Flags.Add("trickster.ever");
                if (returned) state.Flags.Add("terendelev.trickster.returned");
                original.Value = eligible;
                check(checker.Check() == (eligible && !(path && returned)), "F6d native gate changes unpaid/off-path content: " + gate);
            }
        }
        const string inquiry = "c68d9b3a2b887f645ac539f996a63a92";
        var edit = story.NativeEpilogueEdits[inquiry];
        var cue = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(inquiry), Conditions = new ConditionsChecker { Conditions = Array.Empty<Condition>() } };
        NativeEpilogueEditManagedTests.LoadArchiveShape(cue, native[inquiry], check);
        var parent = new BlueprintAnswer { AssetGuid = BlueprintGuid.Parse(edit.Parent), NextCue = new CueSelection {
            Strategy = Strategy.First, Cues = ((JArray)native[edit.Parent]["NextCue"]!["Cues"]!).Select(v => Ref<BlueprintCueBaseReference>((string)v!)).ToList() } };
        var dialog = new BlueprintDialog { AssetGuid = BlueprintGuid.Parse(edit.Dialog) };
        SimpleBlueprint? ResolveEdit(string id) => id == inquiry ? cue : id == edit.Parent ? parent : id == edit.Dialog ? dialog : null;
        check(NativeEpilogueEdit.Check(inquiry, edit, ResolveEdit, null) == null, "F6d native inquiry refused archive");
        var replacement = new BlueprintCue();
        NativeEpilogueEdit.PrepareInDialog(inquiry, edit, cue, parent, replacement, () => true);
        check(ReferenceEquals(replacement.OnStop, cue.OnStop) && replacement.Continue.Cues.Select(c => c.Guid).SequenceEqual(cue.Continue.Cues.Select(c => c.Guid)),
            "F6d inquiry lost its actual quest grant or continuation");
        var action = (Conditional)cue.OnStop.Actions.Single();
        action.IfTrue.Actions = Array.Empty<GameAction>();
        check(NativeEpilogueEdit.Check(inquiry, edit, ResolveEdit, null) != null, "F6d inquiry quest-action drift accepted");
    }
}
