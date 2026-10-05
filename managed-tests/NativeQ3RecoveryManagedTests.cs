using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.AreaLogic.Cutscenes;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Newtonsoft.Json.Linq;
using Tirabade;

internal static class NativeQ3RecoveryManagedTests
{
    private const BindingFlags Fields = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
    private static string Type(JToken data) => ((string)data["$type"]!).Split(new[] { ", " }, StringSplitOptions.None).Last();
    private static T Ref<T>(string guid) where T : BlueprintReferenceBase, new()
    {
        var reference = new T();
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", Fields)!.SetValue(reference, BlueprintGuid.Parse(guid.Replace("!bp_", "")));
        return reference;
    }
    private static void Reference(object target, JObject data, string field)
    {
        var info = target.GetType().GetField(field, Fields)!;
        var value = (BlueprintReferenceBase)Activator.CreateInstance(info.FieldType)!;
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", Fields)!.SetValue(value, BlueprintGuid.Parse(((string)data[field]!).Replace("!bp_", "")));
        info.SetValue(target, value);
    }
    private static T Seed<T>(string id) where T : SimpleBlueprint, new()
    {
        var guid = BlueprintGuid.Parse(id);
        if (ResourcesLibrary.TryGetBlueprint(guid) is T existing) return existing;
        var value = new T { AssetGuid = guid, name = "Q3Fixture_" + id };
        ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(guid, value);
        return value;
    }
    private static ConditionsChecker Checker(JObject data)
    {
        Condition Map(JObject item)
        {
            if (Type(item) == "OrAndLogic") return new OrAndLogic { Not = (bool)item["Not"]!, ConditionsChecker = Checker((JObject)item["ConditionsChecker"]!) };
            // eng7-f6d begin: Storyteller Cue_0777 keeps the original objective-none test.
            if (Type(item) == "ObjectiveStatus")
            {
                var objective = new ObjectiveStatus { Not = (bool)item["Not"]! };
                var state = typeof(ObjectiveStatus).GetField("State", Fields)!;
                state.SetValue(objective, Enum.Parse(state.FieldType, (string)item["State"]!));
                Reference(objective, item, "m_QuestObjective");
                return objective;
            }
            // eng7-f6d end
            // Native cue conditions reached by the F6 epilogue edits (archive shape: Not, m_Cue, CurrentDialog).
            if (Type(item) == "CueSeen")
            {
                var seen = new CueSeen { Not = (bool)item["Not"]! };
                typeof(CueSeen).GetField("CurrentDialog", Fields)?.SetValue(seen, (bool?)item["CurrentDialog"] ?? false);
                Reference(seen, item, "m_Cue");
                return seen;
            }
            if (Type(item) != "EtudeStatus") return (Condition)Generic(null, item, typeof(Condition));
            var status = new EtudeStatus { Not = (bool)item["Not"]!, NotStarted = (bool)item["NotStarted"]!, Started = (bool)item["Started"]!,
                Playing = (bool)item["Playing"]!, CompletionInProgress = (bool)item["CompletionInProgress"]!, Completed = (bool)item["Completed"]! };
            Reference(status, item, "m_Etude");
            return status;
        }
        return new ConditionsChecker { Operation = (Operation)Enum.Parse(typeof(Operation), (string)data["Operation"]!), Conditions = ((JArray)data["Conditions"]!).Cast<JObject>().Select(Map).ToArray() };
    }
    // Generic reflection translator: resolves the Kingmaker type from "$type" and fills fields from the archive JSON.
    private static object Generic(BlueprintScriptableObject? owner, JObject item, Type baseType)
    {
        var name = Type(item);
        var type = typeof(GameAction).Assembly.GetTypes().FirstOrDefault(t => t.Name == name && baseType.IsAssignableFrom(t) && !t.IsAbstract)
            ?? throw new InvalidOperationException("Unknown native " + baseType.Name + " type: " + name);
        var created = Activator.CreateInstance(type)!;
        foreach (var property in item.Properties())
        {
            if (property.Name == "$type" || property.Name == "name") continue;
            FieldInfo? field = null;
            for (var t = type; t != null && field == null; t = t.BaseType)
                field = t.GetField(property.Name, Fields | BindingFlags.DeclaredOnly);
            if (field == null) continue;
            field.SetValue(created, Value(owner, field.FieldType, property.Value));
        }
        return created;
    }
    private static object? Value(BlueprintScriptableObject? owner, Type type, JToken token)
    {
        if (token.Type == JTokenType.Null) return null;
        if (typeof(BlueprintReferenceBase).IsAssignableFrom(type))
        {
            var reference = (BlueprintReferenceBase)Activator.CreateInstance(type)!;
            var text = (string)token!;
            if (text.StartsWith("!bp_", StringComparison.Ordinal))
                typeof(BlueprintReferenceBase).GetField("deserializedGuid", Fields)!.SetValue(reference, BlueprintGuid.Parse(text.Replace("!bp_", "")));
            return reference;
        }
        if (type == typeof(ActionList)) return Actions(owner!, (JArray)token["Actions"]!);
        if (type == typeof(ConditionsChecker)) return Checker((JObject)token);
        if (type.IsEnum) return token.Type == JTokenType.Integer ? Enum.ToObject(type, (long)token) : Enum.Parse(type, (string)token!);
        if (type == typeof(string)) return (string?)token;
        if (type.IsPrimitive || type == typeof(decimal)) return token.ToObject(type);
        if (type.IsArray || (type.IsGenericType && type.GetGenericTypeDefinition() == typeof(List<>)))
        {
            var elem = type.IsArray ? type.GetElementType()! : type.GetGenericArguments()[0];
            var items = ((JArray)token).Select(v => Value(owner, elem, v)).ToList();
            var array = Array.CreateInstance(elem, items.Count);
            for (int i = 0; i < items.Count; i++) array.SetValue(items[i], i);
            return type.IsArray ? array : Activator.CreateInstance(type, array);
        }
        if (token is JObject obj)
        {
            var concrete = type;
            if (obj["$type"] != null)
            {
                var n = Type(obj);
                concrete = typeof(GameAction).Assembly.GetTypes().FirstOrDefault(t => t.Name == n && type.IsAssignableFrom(t) && !t.IsAbstract) ?? type;
            }
            var created = Activator.CreateInstance(concrete)!;
            foreach (var property in obj.Properties())
            {
                if (property.Name == "$type") continue;
                FieldInfo? field = null;
                for (var t = concrete; t != null && field == null; t = t.BaseType)
                    field = t.GetField(property.Name, Fields | BindingFlags.DeclaredOnly);
                if (field != null) field.SetValue(created, Value(owner, field.FieldType, property.Value));
            }
            return created;
        }
        return token.ToObject(type);
    }
    public static ActionList Actions(BlueprintScriptableObject owner, JArray data)
    {
        GameAction Map(JObject item)
        {
            GameAction action;
            switch (Type(item))
            {
                case "Conditional": action = new Conditional { ConditionsChecker = Checker((JObject)item["ConditionsChecker"]!),
                    IfTrue = Actions(owner, (JArray)item["IfTrue"]!["Actions"]!), IfFalse = Actions(owner, (JArray)item["IfFalse"]!["Actions"]!) }; break;
                case "Spawn": action = new Spawn { Spawners = ((JArray)item["Spawners"]!).Select(s => new EntityReference {
                    UniqueId = (string)s["_entity_id"]!, SceneAssetGuid = (string)s["SceneAssetGuid"]!, EntityNameInEditor = (string)s["EntityNameInEditor"]! }).ToArray(),
                    ActionsOnSpawn = Actions(owner, (JArray)item["ActionsOnSpawn"]!["Actions"]!) }; break;
                case "PlayCutscene":
                    var play = new PlayCutscene { PutInQueue = (bool)item["PutInQueue"]!, CheckExistence = (bool)item["CheckExistence"]! };
                    Reference(play, item, "m_Cutscene");
                    if (((JArray)item["Parameters"]!["Parameters"]!).Count != 0) throw new InvalidOperationException("Q3 cutscene gained parameters");
                    var parameterField = typeof(PlayCutscene).GetField("Parameters", Fields)!;
                    var parameters = Activator.CreateInstance(parameterField.FieldType)!;
                    var entries = parameters.GetType().GetField("Parameters", Fields)!;
                    entries.SetValue(parameters, Array.CreateInstance(entries.FieldType.GetElementType()!, 0));
                    parameterField.SetValue(play, parameters);
                    action = play; break;
                // eng7-f6d: preserve the Storyteller's quest grant as an actual game action.
                case "GiveObjective": action = new GiveObjective(); Reference(action, item, "m_Objective"); break;
                case "StartEtude": action = new StartEtude(); Reference(action, item, "Etude"); break;
                case "CompleteEtude": action = new CompleteEtude(); Reference(action, item, "Etude"); break;
                default: action = (GameAction)Generic(owner, item, typeof(GameAction)); break;
            }
            action.Owner = owner; action.name = (string)item["name"]!;
            owner.ElementsArray.Add(action);
            return action;
        }
        return new ActionList { Actions = data.Cast<JObject>().Select(Map).ToArray() };
    }
    public static void Seed(Dictionary<string, JObject> native, Action<bool, string> check)
    {
        var data = native[NativeQ3Recovery.FinalResolve];
        var etude = Seed<BlueprintEtude>(NativeQ3Recovery.FinalResolve);
        var triggerData = (JObject)((JArray)data["Components"]!).Single(c => Type(c) == "EtudePlayTrigger");
        check(!(bool)triggerData["m_Once"]!, "FinalResolve trigger changed its once policy");
        var trigger = new EtudePlayTrigger { name = (string)triggerData["name"]!, Conditions = Checker((JObject)triggerData["Conditions"]!),
            Actions = Actions(etude, (JArray)triggerData["Actions"]!["Actions"]!) };
        etude.ComponentsArray = new BlueprintComponent[] { trigger };
        typeof(BlueprintEtude).GetField("m_StartsOnComplete", Fields)!.SetValue(etude,
            ((JArray)data["m_StartsOnComplete"]!).Select(s => Ref<BlueprintEtudeReference>((string)s!)).ToList());
        var complete = Seed<CommandAction>(NativeQ3Recovery.Completion);
        complete.EntryCondition = Checker((JObject)native[NativeQ3Recovery.Completion]["EntryCondition"]!);
        complete.Action = Actions(etude, (JArray)native[NativeQ3Recovery.Completion]["Action"]!["Actions"]!);
        var verdict = Seed<BlueprintCue>(NativeQ3Recovery.Verdict);
        verdict.OnStop = Actions(verdict, (JArray)native[NativeQ3Recovery.Verdict]["OnStop"]!["Actions"]!);
        check(NativeQ3Recovery.Check(id => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(id)), out _) == null,
            "Installed Q3 actions do not match the reviewed branch");
        // Reproduce the contradiction through native actions: victim spawn plus the cutscene after an earlier release.
        check(trigger.Actions.Actions.Last() is Conditional && verdict.OnStop.Actions.First() is PlayCutscene,
            "Native fixture no longer reproduces duplicate recovery");
        var original = trigger.Actions.Actions;
        trigger.Actions.Actions = original.Concat(new GameAction[] { new CompleteEtude() }).ToArray();
        check(NativeQ3Recovery.Check(id => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(id)), out _) != null, "Drifted Q3 action list accepted");
        trigger.Actions.Actions = original;
    }
    public static void Run(Story story, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        var etude = (BlueprintEtude)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(NativeQ3Recovery.FinalResolve));
        var cue = (BlueprintCue)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(NativeQ3Recovery.Verdict));
        var trigger = etude.ComponentsArray.OfType<EtudePlayTrigger>().Single();
        var spawn = (NativeQ3Recovery.Branch)trigger.Actions.Actions.Single();
        var revive = (NativeQ3Recovery.Branch)cue.OnStop.Actions.Single();
        check(spawn.Earned.SequenceEqual(spawn.Original.Take(2)) && revive.Earned.Take(3).SequenceEqual(revive.Original.Skip(1))
            && revive.Earned.Last() is CompleteEtude && !revive.Earned.OfType<PlayCutscene>().Any(),
            "Q3 branch changed native outcomes, lost completion, or retained revival");
        foreach (var flags in new[] { Array.Empty<string>(), new[] { "trickster" }, new[] { "kiana.trickster.guests_ransomed" },
            new[] { "trickster", "kiana.trickster.guests_ransomed" }, new[] { "trickster", "kiana.trickster.guests_bought_back" },
            new[] { "trickster.ever", "legend", "kiana.trickster.guests_ransomed" },
            new[] { "trickster", "kiana.trickster.guests_ransomed", Rules.DegradedPrefix + "kiana" } })
        {
            var state = new Snapshot { Chapter = 5 }; state.Flags.UnionWith(flags); Rules.Complete(story, state);
            bool earned = Rules.NativeGateHolds(story, NativeQ3Recovery.Gate, state);
            spawn.Holds = revive.Holds = () => earned;
            check(ReferenceEquals(spawn.Selected(), earned ? spawn.Earned : spawn.Original)
                && ReferenceEquals(revive.Selected(), earned ? revive.Earned : revive.Original), "Q3 branch selection differs between spawn and revival");
        }
        spawn.Holds = () => throw new InvalidOperationException("observation failure");
        check(ReferenceEquals(spawn.Selected(), spawn.Original) && spawn.LastObservationError != null, "Q3 observation failure suppresses native actions");
        NativeQ3Recovery.Attach(etude, () => false);
        check(ReferenceEquals(trigger.Actions.Actions.Single(), spawn) && ReferenceEquals(cue.OnStop.Actions.Single(), revive), "Q3 attachment nests branches");
        check(Rules.WarningOnlyNativeGates.Contains(NativeQ3Recovery.Gate), "Q3 refusal degrades the relationship");
        var replacement = story.NativeEpilogueEdits[NativeQ3Recovery.Verdict];
        var replacementCue = (BlueprintCue)ResourcesLibrary.TryGetBlueprint(id(Rules.NativeEditCueName(NativeQ3Recovery.Verdict, replacement, 0)));
        check(ReferenceEquals(replacementCue.OnStop, cue.OnStop), "Arsinoe's replacement bypasses the reviewed recovery branch");
        Console.WriteLine("PASS: reviewed Q3 recovery branches preserve native outcomes and completion, skip duplicate recovery, and fail back to canon.");
    }
}
