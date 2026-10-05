using System;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng8-q8h: explicit retirement AND a real positive trace of the surviving plan.
internal static class RescueEndpointInventoryTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        using var doc = JsonDocument.Parse(File.ReadAllText("tools/rescue_endpoint_inventory_contracts.json"));
        foreach (var row in doc.RootElement.GetProperty("retired_offers").EnumerateArray())
        {
            var scene = story.Scenes.Single(s => s.Id == row.GetString());
            check(scene.Requires.Intersect(scene.Forbids).Contains("trickster.ever"), "Live obsolete rescue promise: " + scene.Id);
            var world = LateAcceptanceInventory2Tests.World(story, scene.MinChapter, scene.Requires);
            check(!Rules.Available(story, scene, world), "Retired promise grants a successful bargain: " + scene.Id);
            check(scene.Nodes.Count > 1, "Retirement deleted saved nodes: " + scene.Id);
        }
        const string E = "wenduag.trickster.echo.abyss.";
        var begin = LateAcceptanceInventory2Tests.World(story, 4, "trickster.foresight.accepted", "lann.in_party", E + "adapter_available");
        var prepare = story.Scenes.Single(s => s.Id == E + "prepare");
        foreach (var row in doc.RootElement.GetProperty("legacy_incompatibilities").EnumerateArray())
        {
            string receipt = row.GetProperty("receipt").GetString()!;
            var legacy = story.Scenes.Single(s => s.Id == row.GetProperty("producer").GetString());
            var blocked = story.Scenes.Single(s => s.Id == row.GetProperty("blocked_consumer").GetString());
            check(legacy.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains(receipt))
                && blocked.Forbids.Contains(receipt), "Legacy producer/echo incompatibility lost");
            // A retained old bargain is historical evidence, never a live rescue entitlement.
            var historical = Program.Copy(begin); historical.Flags.Add(receipt);
            LateAcceptanceInventory2Tests.Refresh(story, historical);
            check(!Rules.Available(story, blocked, historical), "Legacy bargain bypasses allocated echo guard");
        }
        var prepared = LateAcceptanceInventory2Tests.Earn(story, check, prepare.Id, begin, E + "ready");
        check(prepared.CrusadeResources!["Finances"] <= begin.CrusadeResources!["Finances"] - 150, "Prepared rescue bypasses its existing cost");
        var skipped = Program.Walk(prepare, begin).First(s => s.Has(E + "abandoned"));
        var pickup = story.Scenes.Single(s => s.Id == E + "pickup");
        Snapshot Encounter(Snapshot before)
        {
            var s = Program.Copy(before);
            // Native encounter + adapter-observed living casualty; never an authored rescue/return.
            s.Flags.UnionWith(new[] { "wenduag.abyss_fell", E + "casualty_available", E + "valid" });
            s.SceneContacts.Add(pickup.Id);
            LateAcceptanceInventory2Tests.Refresh(story, s);
            return s;
        }
        var casualty = Encounter(prepared);
        check(Rules.Available(story, pickup, casualty), "Successful live preparation has no surviving endpoint");
        var rescued = LateAcceptanceInventory2Tests.Earn(story, check, pickup.Id, casualty, E + "rescued");
        check(!Rules.IsRemote(pickup), "Chapter 4 echo became a delivered page");
        foreach (var negative in new[] { Encounter(begin), Encounter(skipped) })
        {
            check(!Rules.Available(story, pickup, negative) && !negative.Has(E + "rescued"), "Unprepared/failed plan obtains rescue");
        }
        var closed = Encounter(prepared); closed.Flags.Add("wenduag.closed");
        LateAcceptanceInventory2Tests.Refresh(story, closed);
        check(!Rules.Available(story, pickup, closed), "Closed plan obtains rescue");
        rescued.Chapter = 5;
        rescued.Flags.Add(E + "return_available"); // adapter-confirmed living placement, not return receipt
        var returned = LateAcceptanceInventory2Tests.Earn(story, check, E + "return", rescued, E + "returned");
        check(returned.Has("wenduag.trickster.returned") && !returned.Has("wenduag.committed"), "Endpoint buys affection or loses return");
        Console.WriteLine("PASS: eng8-q8h six retired legacy promises and paid preparation -> living pickup -> authored return, with negatives.");
    }
}
