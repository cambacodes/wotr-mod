using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Newtonsoft.Json.Linq;
using Tirabade;

// E14b: Main.BuildReturnToList builds, per native list, an entry answer, the inline cue graph and a return cue that shows that
// same list again; terminal choices record completion and return, abort returns without completion.
internal static class ReturnToListManagedTests
{
    public static IEnumerable<string> NativeIds => new[] { "294126e3264796e488ce19bfb1851355", "16994192cfa484744bd10852b8dc806f" };

    public static void Run(Dictionary<string, JObject> native, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        foreach (var list in NativeIds)
            check(((string)native[list]["$type"]!).EndsWith(", BlueprintAnswersList", StringComparison.Ordinal), "GrandFinal hook is not an answer list: " + list);
        var scene = new Scene
        {
            Id = "e14b.fixture", Title = "E14b", Owner = "Commander", Relationship = "lastcall", MinChapter = 6, MaxChapter = 6,
            AnswerLists = NativeIds.ToArray(), ReturnToList = true, ReturnText = "{n}The Wound waits.{/n}", Entry = "[Call last orders]",
            EntryMythic = "PlayerIsTrickster",
            Nodes = new List<Tirabade.Node> {
                new Tirabade.Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice { Text = "Drink", Next = "ledger" }, new Choice { Text = "Not yet", Abort = true } } },
                new Tirabade.Node { Id = "ledger", Text = "y", Choices = new List<Choice> { new Choice { Text = "Done", Set = new[] { "trickster.lastcall.taken" } } } } }
        };
        typeof(Main).GetMethod("BuildReturnToList", BindingFlags.NonPublic | BindingFlags.Static)!.Invoke(null, new object[] { scene });
        T Bp<T>(string name) where T : SimpleBlueprint => (T)ResourcesLibrary.TryGetBlueprint(id(name))!;
        foreach (var list in NativeIds)
        {
            string p = scene.Id + "." + list;
            var entry = Bp<BlueprintAnswer>("entry." + p);
            var start = Bp<BlueprintCue>("cue." + p + ".start");
            var ledger = Bp<BlueprintCue>("cue." + p + ".ledger");
            var back = Bp<BlueprintCue>("cue." + p + ".return");
            check(entry != null && entry.NextCue.Cues.Single().Guid == start.AssetGuid && entry.MythicRequirement == Mythic.PlayerIsTrickster,
                "Entry answer does not open the inline graph with its mythic requirement: " + list);
            check(back.Answers.Single().Guid == BlueprintGuid.Parse(list) && back.Continue.Cues.Count == 0 && back.OnShow.Actions.Length == 0,
                "Return cue does not show its own list again: " + list);
            var drink = Bp<BlueprintAnswer>("answer." + p + ".start.0");
            var notYet = Bp<BlueprintAnswer>("answer." + p + ".start.1");
            var done = Bp<BlueprintAnswer>("answer." + p + ".ledger.0");
            check(drink.NextCue.Cues.Single().Guid == ledger.AssetGuid && done.NextCue.Cues.Single().Guid == back.AssetGuid
                && notYet.NextCue.Cues.Single().Guid == back.AssetGuid, "Inline answers are not wired start -> ledger -> return: " + list);
            check(done.OnSelect.Actions.Single() is Main.RouteAction complete && ReferenceEquals(complete.Complete, scene)
                && notYet.OnSelect.Actions.Single() is Main.RouteAction abort && abort.Complete == null,
                "Terminal choice must record completion and abort must not: " + list);
        }
        Console.WriteLine("PASS: E14b return-to-list graphs built per native list (entry, inline cues, return cue to the same list).");
    }
}
