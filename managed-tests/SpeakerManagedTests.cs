using System;
using System.Collections.Generic;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;
using Newtonsoft.Json.Linq;
using Tirabade;

// E14f: Main.InlineSpeaker gives an inline cue a native unit speaker (Pharasma), the dialog's conversant, or the default.
internal static class SpeakerManagedTests
{
    private const string Pharasma = "db064cafc234498ca83a702c472c1a7b";
    public static IEnumerable<string> NativeIds => new[] { Pharasma };

    public static void Run(Dictionary<string, JObject> native, Action<bool, string> check)
    {
        check(((string)native[Pharasma]["$type"]!).EndsWith(", BlueprintUnit", StringComparison.Ordinal), "Pharasma is not a BlueprintUnit.");
        var id = BlueprintGuid.Parse(Pharasma);
        if (!(ResourcesLibrary.TryGetBlueprint(id) is BlueprintUnit))
            ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(id, new BlueprintUnit { AssetGuid = id, name = "NativeFixture_Pharasma" });
        var method = typeof(Main).GetMethod("InlineSpeaker", BindingFlags.NonPublic | BindingFlags.Static)!;
        DialogSpeaker Speak(Tirabade.Node node, DialogSpeaker? fallback) => (DialogSpeaker)method.Invoke(null, new object?[] { node, fallback })!;
        var unit = Speak(new Tirabade.Node { Id = "a", SpeakerUnit = Pharasma }, null);
        check(!unit.NoSpeaker && !unit.MoveCamera && unit.Blueprint?.AssetGuid == id, "Speaker unit not applied.");
        var conversant = Speak(new Tirabade.Node { Id = "b", Speaker = "conversant" }, null);
        check(!conversant.NoSpeaker && conversant.Blueprint == null, "Conversant speaker not applied.");
        var fallback = new DialogSpeaker { NoSpeaker = false };
        check(ReferenceEquals(Speak(new Tirabade.Node { Id = "c", Speaker = "Narrator" }, fallback), fallback), "Default speaker not kept.");
        var missing = Speak(new Tirabade.Node { Id = "d", SpeakerUnit = "0123456789abcdef0123456789abcdef" }, null);
        check(missing.NoSpeaker, "A missing speaker unit must fall back to narration.");
        Console.WriteLine("PASS: E14f inline speakers (unit, conversant, default, missing unit falls back).");
    }
}
