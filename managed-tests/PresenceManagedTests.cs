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

    private const string PlayerFaction = "72f240260881111468db610b6c37c099";
    private const string NeutralFaction = "d8de50cc80eb4dc409a983991e0b77ad";   // Neutrals
    private const string SilentAsks = "e7b22776ba8e2b84eaaff98e439639a7";       // PC_None_Barks

    public static IEnumerable<string> NativeIds(Story story) => new[] { IrabethUnit, Capital, "db064cafc234498ca83a702c472c1a7b",
            NeutralFaction, SilentAsks }
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
        PresenceRuntimeF9Tests.Run(check);
        string? jerribethFaction = (string?)native[story.Presences["jerribeth.presence"].Unit]["m_Faction"];
        check(jerribethFaction != null && !jerribethFaction.EndsWith(PlayerFaction, StringComparison.Ordinal)
            && !jerribethFaction.EndsWith(NeutralFaction, StringComparison.Ordinal),
            "F9: Jerribeth native faction fixture no longer demonstrates the non-Player quiet repair");
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
        // E12d: the quiet copy uses two native blueprints; the silent asks list must really be silent (no voice event, text
        // or sound bank), and the state it changes must be the unit's serialized native state, so a save loads without the mod.
        string Constant(string name) => (string)type.GetField(name, BindingFlags.Static | BindingFlags.NonPublic)!.GetRawConstantValue();
        check(Constant("NeutralFaction") == NeutralFaction && Constant("SilentAsks") == SilentAsks, "GuestPresence quiet-copy blueprints differ from the verified ones.");
        check(Type(NeutralFaction) == "BlueprintFaction", "Quiet copy faction is not a BlueprintFaction.");
        check(Type(SilentAsks) == "BlueprintUnitAsksList", "Quiet copy asks is not a BlueprintUnitAsksList.");
        var asks = native[SilentAsks]["Components"]!.Single(c => ((string)c["$type"]!).EndsWith(", UnitAsksComponent", StringComparison.Ordinal));
        check(!asks["SoundBanks"]!.Values<string>().Any(b => !string.IsNullOrEmpty(b)), "The silent asks list loads a sound bank.");
        var voiced = ((JContainer)asks).Descendants().OfType<JProperty>().Where(e => e.Name == "AkEvent" && !string.IsNullOrEmpty((string?)e.Value)
            || e.Name == "Text" && e.Value.Type != JTokenType.Null).Select(e => e.Path).ToArray();
        check(voiced.Length == 0, "The silent asks list has voiced or text barks: " + string.Join(", ", voiced.Take(3)));
        var descriptor = typeof(Kingmaker.UnitLogic.UnitDescriptor);
        check(descriptor.GetField("OverrideAsks")?.GetCustomAttributes(typeof(JsonPropertyAttribute), false).Length == 1
            && descriptor.GetField("m_Faction", BindingFlags.Instance | BindingFlags.NonPublic)?.GetCustomAttributes(typeof(JsonPropertyAttribute), false).Length == 1
            && typeof(Kingmaker.EntitySystem.Entities.UnitEntityData).GetField("m_GroupId", BindingFlags.Instance | BindingFlags.NonPublic)?.GetCustomAttributes(typeof(JsonPropertyAttribute), false).Length == 1,
            "The quiet copy's asks, faction or group is no longer saved native unit state.");
        // Every spawn-copy of a Player-faction blueprint (companions) is what the quiet copy exists for; list them for the log.
        var companions = story.Presences.Where(p => p.Value.Mode == "spawn-copy" && ((string?)native[p.Value.Unit]["m_Faction"])?.EndsWith(PlayerFaction, StringComparison.Ordinal) == true)
            .Select(p => p.Key).OrderBy(k => k, StringComparer.Ordinal).ToArray();
        // E12e: PretendUnit copies report another blueprint as Blueprint; GuestPresence matches them by OriginalBlueprint.
        var pretenders = story.Presences.Where(p => p.Value.Mode == "spawn-copy" && native[p.Value.Unit]["Components"]?
            .Any(c => ((string?)c["$type"])?.EndsWith(", PretendUnit", StringComparison.Ordinal) == true) == true).Select(p => p.Key).OrderBy(k => k, StringComparer.Ordinal).ToArray();
        check(pretenders.Contains("seelah.presence"), "Seelah_NPC_Level1 no longer carries PretendUnit; re-check E12e.");
        Console.WriteLine("E12e: PretendUnit spawn-copies matched by OriginalBlueprint: " + string.Join(", ", pretenders));
        Console.WriteLine("E12d: Player-faction spawn-copies quieted at spawn: " + (companions.Length == 0 ? "none" : string.Join(", ", companions)));
        Console.WriteLine("PASS: E12 presences resolve archive types; GuestPresence builds; its save record round-trips; harness report hook present.");
    }
}
