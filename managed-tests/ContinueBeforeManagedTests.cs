using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Newtonsoft.Json.Linq;
using Tirabade;

// E14e: the afterlogue verdict cues continue First into Cue_27/25/26 (verified in blueprints.zip); the RRT line is built as one
// conditioned cue that records its choice on show, and is inserted right before Cue_27 without moving the native cues.
internal static class ContinueBeforeManagedTests
{
    private const string Cue27 = "3094c9e9557c43d29610dbd3eec15b35";
    internal static readonly string[] Verdicts = { "da7646b4ce8e4e658ee92aa02877ec17", "abafa9f923204d5a96cb13bec9ab7771",
        "d7c1d87165af414ebffbd4f50151af49", "9377e7d23348467ab12a3de0a94246fc", "f8b124e1f6584f54a9a3f80e85973a0c" };
    public static IEnumerable<string> NativeIds => Verdicts;

    public static void Run(Dictionary<string, JObject> native, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        var scene = new Scene
        {
            Id = "e14e.fixture", Title = "E14e", Owner = "Pharasma", Relationship = "lastcall", MinChapter = 6, MaxChapter = 6,
            ContinueBefore = new ContinueSpec { Cue = Cue27, Parents = Verdicts },
            Nodes = new List<Tirabade.Node> { new Tirabade.Node { Id = "start", Text = "Go. Keep your bottle corked.", SpeakerUnit = "db064cafc234498ca83a702c472c1a7b",
                Choices = new List<Choice> { new Choice { Set = new[] { "trickster.lastcall.court.closed" } } } } }
        };
        typeof(Main).GetMethod("BuildContinueBefore", BindingFlags.NonPublic | BindingFlags.Static)!.Invoke(null, new object[] { scene });
        var line = (BlueprintCue)ResourcesLibrary.TryGetBlueprint(id("cue.e14e.fixture.continue"))!;
        check(line.Conditions.Conditions.Single() is Main.RouteCondition guard && ReferenceEquals(guard.Scene, scene)
            && line.OnShow.Actions.Single() is Main.RouteAction record && ReferenceEquals(record.Complete, scene)
            && ReferenceEquals(record.Choice, scene.Nodes[0].Choices[0]) && line.Speaker.Blueprint?.AssetGuid == BlueprintGuid.Parse("db064cafc234498ca83a702c472c1a7b"),
            "Continue-before line lacks its availability guard, choice record or speaker.");
        var insert = typeof(Main).GetMethod("InsertContinueBefore", BindingFlags.NonPublic | BindingFlags.Static)!;
        var reference = new BlueprintCueBaseReference();
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!.SetValue(reference, line.AssetGuid);
        foreach (var verdict in Verdicts)
        {
            var data = native[verdict];
            var continued = ((JArray)data["Continue"]!["Cues"]!).Select(v => ((string)v!).Replace("!bp_", "")).ToList();
            check((string)data["Continue"]!["Strategy"]! == "First" && continued.IndexOf(Cue27) >= 0, "Verdict no longer continues First into Cue_27: " + verdict);
            var parent = new BlueprintCue { Continue = new CueSelection { Strategy = Strategy.First, Cues = continued.Select(g =>
            {
                var r = new BlueprintCueBaseReference();
                typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!.SetValue(r, BlueprintGuid.Parse(g));
                return r;
            }).ToList() } };
            insert.Invoke(null, new object[] { parent, reference, BlueprintGuid.Parse(Cue27) });
            insert.Invoke(null, new object[] { parent, reference, BlueprintGuid.Parse(Cue27) });   // idempotent
            var after = parent.Continue.Cues.Select(r => r.Guid.ToString()).ToList();
            check(after.Count == continued.Count + 1 && after[continued.IndexOf(Cue27)] == line.AssetGuid.ToString()
                && after.Where(g => g != line.AssetGuid.ToString()).SequenceEqual(continued), "Line not inserted once, right before Cue_27: " + verdict);
        }
        Console.WriteLine("PASS: E14e continue-before line built and inserted ahead of Cue_27 in the " + Verdicts.Length + " afterlogue verdict cues.");
    }
}
