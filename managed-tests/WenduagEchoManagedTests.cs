using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.AreaLogic.Cutscenes;
using Kingmaker.AreaLogic.Cutscenes.Commands;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.DialogSystem.Blueprints;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Tirabade;

internal static class WenduagEchoManagedTests
{
    private const BindingFlags All = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
    private static readonly Type Engine = typeof(Main).Assembly.GetType("Tirabade.WenduagEcho", true)!;
    internal static IEnumerable<string> NativeIds => (string[])Engine.GetField("NativeIds", BindingFlags.Static | BindingFlags.NonPublic)!.GetValue(null)!;
    private static string Id(string name) => (string)Engine.GetField(name, BindingFlags.Static | BindingFlags.NonPublic)!.GetValue(null)!;
    private static SimpleBlueprint Blueprint(string id) => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(id));
    private static FieldInfo? Field(Type type, string name)
    {
        for (Type? current = type; current != null; current = current.BaseType)
            if (current.GetField(name, All | BindingFlags.DeclaredOnly) is FieldInfo field) return field;
        return null;
    }

    // Read actual archive values into only the reviewed sequence and dialogue fields.
    // This does not fabricate a Unity actor or simulate a campaign.
    private static object? Map(JToken token, Type expected)
    {
        if (token.Type == JTokenType.Null)
            return typeof(BlueprintReferenceBase).IsAssignableFrom(expected) ? Activator.CreateInstance(expected) : null;
        if (token.Type == JTokenType.String && ((string)token!).StartsWith("!bp_", StringComparison.Ordinal))
        {
            string id = ((string)token!).Substring(4);
            if (typeof(SimpleBlueprint).IsAssignableFrom(expected)) return Blueprint(id);
            var reference = (BlueprintReferenceBase)Activator.CreateInstance(expected)!;
            Field(expected, "deserializedGuid")!.SetValue(reference, BlueprintGuid.Parse(id));
            return reference;
        }
        if (token is JArray values)
        {
            Type element = expected.IsArray ? expected.GetElementType()! : expected.GetGenericArguments()[0];
            var array = Array.CreateInstance(element, values.Count);
            for (int i = 0; i < values.Count; i++) array.SetValue(Map(values[i], element), i);
            if (expected.IsArray) return array;
            var list = (IList)Activator.CreateInstance(expected)!;
            foreach (object? value in array) list.Add(value);
            return list;
        }
        if (!(token is JObject fields)) return expected.IsEnum ? Enum.Parse(expected, (string)token!) : token.ToObject(expected);
        if (fields["$type"] is JToken tagged)
        {
            string name = ((string)tagged!).Split(new[] { ", " }, StringSplitOptions.None).Last();
            expected = typeof(SimpleBlueprint).Assembly.GetTypes().Single(t => t.Name == name && expected.IsAssignableFrom(t));
        }
        var target = Activator.CreateInstance(expected)!;
        foreach (var property in fields.Properties())
            if (Field(expected, property.Name) is FieldInfo field && !field.IsInitOnly)
                field.SetValue(target, Map(property.Value, field.FieldType));
        if (target is Track track)
            track.Commands = fields["m_Commands"]!.Select(value => (CommandBase)Blueprint(((string)value!).Substring(4))).ToList();
        return target;
    }

    internal static void Seed(Dictionary<string, JObject> native, Action<bool, string> check)
    {
        var ids = NativeIds.Except(new[] { Id("Unit"), Id("Lann"), Id("Journey") }).ToArray();
        foreach (string id in ids)
        {
            if (Blueprint(id) != null) continue;
            string name = ((string)native[id]["$type"]!).Split(new[] { ", " }, StringSplitOptions.None).Last();
            var type = typeof(SimpleBlueprint).Assembly.GetTypes().Single(t => t.Name == name && typeof(SimpleBlueprint).IsAssignableFrom(t));
            var blueprint = (SimpleBlueprint)Activator.CreateInstance(type)!;
            blueprint.AssetGuid = BlueprintGuid.Parse(id);
            blueprint.name = "WenduagNativeFixture_" + id;
            ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(blueprint.AssetGuid, blueprint);
        }
        foreach (string id in ids)
        {
            var blueprint = Blueprint(id);
            var fields = native[id];
            IEnumerable<string> names = blueprint is BlueprintCue
                ? new[] { "Text", "OnShow", "OnStop", "Continue", "Answers" }.Concat(id == Id("Cue") ? Array.Empty<string>() : new[] { "Conditions" })
                : blueprint is BlueprintAnswer ? new[] { "Text", "OnSelect", "NextCue" }
                : fields.Properties().Select(p => p.Name).Where(n => n != "Components" && n != "PrototypeLink" && n != "m_Overrides");
            foreach (string name in names)
                if (Field(blueprint.GetType(), name) is FieldInfo field) field.SetValue(blueprint, Map(fields[name]!, field.FieldType));
            if (blueprint is Gate gate)
                gate.StartedTracks = fields["m_Tracks"]!.Select(value => (Track)Map(value, typeof(Track))!).ToList();
        }
        var args = new object[] { Blueprint(Id("Cue")), Blueprint(Id("Sequence")), Blueprint(Id("Death")),
            Blueprint(Id("Attack")), Blueprint(Id("Movement")), Blueprint(Id("End")) };
        var validate = Engine.GetMethod("Validate", BindingFlags.Static | BindingFlags.NonPublic)!;
        var dispatch = (BlueprintCue)args[0];
        check(dispatch.Text != null && dispatch.OnStop?.Actions?.Length == 1, "Fixture lost dispatch text/actions");
        var play = dispatch.OnStop!.Actions[0] as PlayCutscene;
        check(play != null && play.Parameters?.Parameters != null && play.Cutscene != null, "Fixture lost cutscene parameters/reference");
        check(((Cutscene)args[1]).StartedTracks != null && ((Cutscene)args[1]).OnStopped?.Actions != null, "Fixture lost cutscene tracks/actions");
        check(((CommandAction)args[2]).Action?.Actions?.Length == 3, "Fixture lost native death actions");
        validate.Invoke(null, args);
        var kill = (Kill)((CommandAction)args[2]).Action.Actions[2];
        kill.RemoveExp = false;
        bool refused = false;
        try { validate.Invoke(null, args); }
        catch (TargetInvocationException ex) { refused = ex.InnerException is InvalidOperationException; }
        finally { kill.RemoveExp = true; }
        check(refused, "Wenduag death evidence drift was accepted");
        check(((BlueprintCue)args[0]).OnStop.Actions.Single() is PlayCutscene, "Evidence validation mutated native dispatch");
    }

    internal static void Run(Action<bool, string> check)
    {
        var adapter = typeof(Main).GetField("wenduagEcho", BindingFlags.Static | BindingFlags.NonPublic)!.GetValue(null);
        check(adapter != null && (bool)Engine.GetProperty("Installed", All)!.GetValue(adapter)!, "Reviewed Wenduag adapter was not installed");
        var native = (CommandAction)Blueprint(Id("Death"));
        check(native.Action.Actions.Length == 3 && native.Action.Actions[2] is Kill, "Native death command was changed globally");
        var variant = (Cutscene)Engine.GetField("variant", All)!.GetValue(adapter)!;
        check(variant.AssetGuid.ToString() != Id("Sequence"), "Echo clone copied a native save identity");
        check(variant.StartedTracks.Count == 3, "Echo lost native tracks");
        check(variant.StartedTracks.SelectMany(t => t.Commands).All(c => !(c is CommandUnitAttack)), "Echo retained a damaging attack");
        var death = (CommandAction)variant.StartedTracks[2].Commands[1];
        check(ReferenceEquals(death.EntryCondition, native.EntryCondition) && death.OnFail == native.OnFail,
            "Echo changed death-command entry/failure policy");
        check(death.Action.Actions.Length == 3 && ReferenceEquals(death.Action.Actions[0], native.Action.Actions[0])
            && ReferenceEquals(death.Action.Actions[1], native.Action.Actions[1]) && !(death.Action.Actions[2] is Kill),
            "Echo did not retain DetachBuff/SwitchFaction and replace only Kill");
        var sequence = (Cutscene)Blueprint(Id("Sequence"));
        check(variant.StartedTracks[1].Commands.SequenceEqual(sequence.StartedTracks[1].Commands), "Echo changed native movement/timing/collapse track");
        check(variant.StartedTracks[0].EndGate == variant.StartedTracks[2].EndGate
            && variant.StartedTracks[1].EndGate == null, "Echo changed native completion topology");
        check(((BlueprintCue)Blueprint(Id("Cue"))).OnStop.Actions.Single().GetType().Name == "Dispatch", "Echo has no narrowly reviewed dispatch");
        var record = Engine.GetNestedType("Record", BindingFlags.Public)!;
        foreach (string phase in new[] { "pending", "down", "hidden", "transport", "arrived", "released", "departed", "invalid" }) // eng8-q8a
        {
            var data = JObject.Parse("{\"Version\":1,\"ActorId\":\"original\",\"SourceArea\":\"area\",\"SourceStorage\":\"scene\",\"Attempt\":\"4778e4ba-4823-4e7d-b2e8-b6299c9bcb15\",\"Incapacitated\":true,\"PassiveAdded\":true,\"UntargetableAdded\":true,\"JourneyObserved\":true,\"PickupHour\":450}");
            data["Phase"] = phase;
            if (phase == "down") { data["PickupHour"] = -1; data["JourneyObserved"] = false; }
            if (phase == "released" || phase == "departed") data["UntargetableAdded"] = false; // eng8-q8a
            var copy = JsonConvert.DeserializeObject(JsonConvert.SerializeObject(data.ToObject(record)), record)!;
            check((bool)record.GetProperty("WellFormed", All)!.GetValue(copy)!, "Custody JSON lost its phase/identity: " + phase);
            foreach (string field in new[] { "ActorId", "SourceArea", "SourceStorage", "Attempt", "Phase", "Incapacitated", "PassiveAdded", "UntargetableAdded", "JourneyObserved", "PickupHour" })
                check(JToken.DeepEquals(JToken.FromObject(record.GetField(field)!.GetValue(copy)!), data[field]), "Custody JSON lost " + field);
        }
        check(!(bool)record.GetProperty("WellFormed", All)!.GetValue(Activator.CreateInstance(record))!, "Corrupt custody accepted empty identity");
        Console.WriteLine("PASS: archive-backed Wenduag dispatch/action evidence, damage-free clone, original native fallback and custody JSON.");
    }
}
