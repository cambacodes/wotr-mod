using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Tirabade;

// E12: presence bindings resolve to the right archive types, the runtime object builds against the real assemblies, and the
// only persisted state (a SettingsList JSON string) round-trips and rejects foreign or ambiguous records.
internal static class PresenceManagedTests
{
    private const string IrabethUnit = "280d4712dceb37f4a88e98f1f4c6e64f";
    private const string Capital = "2570015799edf594daf2f076f2f975d8";

    public static IEnumerable<string> NativeIds(Story story) => new[] { IrabethUnit, Capital, "db064cafc234498ca83a702c472c1a7b" }
        .Concat(story.Presences.Values.Where(p => p.At?.NearUnit != null).Select(p => p.At!.NearUnit!))
        .Concat(story.Presences.Values.SelectMany(p => new[] { p.Unit, p.Area }.Concat(p.AnswerLists)));

    public static void Run(Story story, Dictionary<string, JObject> native, Action<bool, string> check)
    {
        string Type(string guid) => ((string)native[guid]["$type"]!).Split(new[] { ", " }, StringSplitOptions.None).Last();
        check(Type(IrabethUnit) == "BlueprintUnit" && Type(Capital).StartsWith("BlueprintArea", StringComparison.Ordinal),
            "Presence fixture GUIDs have unexpected archive types.");
        foreach (var pair in story.Presences)
        {
            check(Type(pair.Value.Unit) == "BlueprintUnit", "Presence unit is not a BlueprintUnit: " + pair.Key);
            check(Type(pair.Value.Area).StartsWith("BlueprintArea", StringComparison.Ordinal), "Presence area is not a BlueprintArea: " + pair.Key);
            foreach (var list in pair.Value.AnswerLists) check(Type(list) == "BlueprintAnswersList", "Presence host is not an answer list: " + pair.Key);
        }
        var unit = ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(IrabethUnit)) as BlueprintUnit ?? new BlueprintUnit { AssetGuid = BlueprintGuid.Parse(IrabethUnit) };
        var spec = new Presence { Unit = IrabethUnit, Area = Capital, Mode = "spawn-copy", Requires = new[] { "trickster.ever" },
            Position = new PresencePosition { X = 1, Y = 2, Z = 3, Orientation = 90 } };
        var type = typeof(Main).Assembly.GetType("Tirabade.GuestPresence", true)!;
        var presence = Activator.CreateInstance(type, BindingFlags.Instance | BindingFlags.NonPublic, null, new object[] { "irabeth.presence", spec, unit }, null)!;
        check((string)type.GetProperty("SaveKey", BindingFlags.Instance | BindingFlags.NonPublic)!.GetValue(presence)! == "RanRomance.Tirabade.Presence.irabeth.presence",
            "Presence save key changed (saves carry it).");
        var record = new PresenceRecord { Key = "irabeth.presence", UnitId = Guid.NewGuid().ToString(), Submitted = true };
        string json = JsonConvert.SerializeObject(record);
        var back = PresenceRecord.Parse(json, "irabeth.presence");
        check(back != null && back.UnitId == record.UnitId && back.Submitted, "Presence record does not round-trip.");
        check(PresenceRecord.Parse(json, "anevia.presence") == null, "A record for another presence was accepted.");
        check(PresenceRecord.Parse(JsonConvert.SerializeObject(new PresenceRecord { Key = "irabeth.presence", Submitted = true }), "irabeth.presence") == null,
            "A submitted record without a unit id was accepted.");
        check(PresenceRecord.Parse("{not json", "irabeth.presence") == null, "A corrupt record was accepted.");
        // E12b: an anchored presence builds against the real types; its NearUnit anchor is a native BlueprintUnit.
        const string anchorUnit = "db064cafc234498ca83a702c472c1a7b";
        check(Type(anchorUnit) == "BlueprintUnit", "Presence anchor fixture is not a BlueprintUnit.");
        foreach (var pair in story.Presences.Where(p => p.Value.At?.NearUnit != null))
            check(Type(pair.Value.At!.NearUnit!) == "BlueprintUnit", "Presence anchor is not a BlueprintUnit: " + pair.Key);
        var anchored = new Presence { Unit = IrabethUnit, Area = Capital, Mode = "spawn-copy", Requires = new[] { "trickster.ever" },
            At = new PresenceAnchor { NearUnit = anchorUnit, Side = "left", Distance = 1.5f } };
        var built = Activator.CreateInstance(type, BindingFlags.Instance | BindingFlags.NonPublic, null, new object[] { "irabeth.presence", anchored, unit }, null)!;
        check(!(bool)type.GetProperty("AnchorFailed", BindingFlags.Instance | BindingFlags.NonPublic)!.GetValue(built)!, "A fresh anchored presence reports failure.");
        var report = (string[])typeof(Main).GetMethod("PresenceReport", BindingFlags.Static | BindingFlags.NonPublic)!.Invoke(null, null)!;
        check(report.Length == story.Presences.Count, "Harness presence report does not list every presence.");
        Console.WriteLine("PASS: E12 presences resolve archive types; GuestPresence builds; its save record round-trips; harness report hook present.");
    }
}
