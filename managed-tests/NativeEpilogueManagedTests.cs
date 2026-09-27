using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Newtonsoft.Json.Linq;
using Tirabade;

// E14a: the native PlayerFinalChoice sequence from blueprints.zip holds both allowed anchors, and a page placed after
// BookPage_0147 lands right after it, leaving every native member in place.
internal static class NativeEpilogueManagedTests
{
    public static IEnumerable<string> NativeIds => new[] { Rules.PlayerFinalChoice };

    public static void Run(Dictionary<string, JObject> native, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        var data = native[Rules.PlayerFinalChoice];
        check(((string)data["$type"]!).EndsWith(", BlueprintCueSequence", StringComparison.Ordinal), "PlayerFinalChoice is not a cue sequence.");
        var members = ((JArray)data["Cues"]!).Select(v => ((string)v!).Replace("!bp_", "")).ToList();
        foreach (var anchor in Rules.NativeEpilogueSequences["PlayerFinalChoice"])
            check(members.Count(m => m == anchor) == 1, "Allowed anchor is not a single member of PlayerFinalChoice: " + anchor);
        BlueprintCueBaseReference Ref(BlueprintGuid guid)
        {
            var reference = new BlueprintCueBaseReference();
            typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!.SetValue(reference, guid);
            return reference;
        }
        var cues = members.Select(m => Ref(BlueprintGuid.Parse(m))).ToList();
        var original = cues.ToArray();
        var page = Ref(id("fixture.e14a.page"));
        var insert = typeof(Main).GetMethod("InsertEpiloguePage", BindingFlags.NonPublic | BindingFlags.Static)!;
        check((bool)insert.Invoke(null, new object?[] { cues, page, "fb42f8bd123bf1f40a448f6dbc66cbbe" })!, "Page not placed after BookPage_0147.");
        int at = members.IndexOf("fb42f8bd123bf1f40a448f6dbc66cbbe");
        check(ReferenceEquals(cues[at + 1], page) && cues.Where(c => !ReferenceEquals(c, page)).SequenceEqual(original),
            "PlayerFinalChoice members moved or the page is not right after BookPage_0147.");
        Console.WriteLine("PASS: E14a PlayerFinalChoice anchors verified in blueprints.zip; page placed after BookPage_0147.");
    }
}
