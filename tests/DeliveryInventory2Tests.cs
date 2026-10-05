using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng8-q8d: positive production histories, with separate sentinel mutations.
internal static class DeliveryInventory2Tests
{
    private static readonly JsonSerializerOptions Options = new() { IncludeFields = true };
    private sealed class Step
    {
        public string? scene, area;
        public int? chapter;
        public string[] native = Array.Empty<string>(), require = Array.Empty<string>(), require_absent = Array.Empty<string>();
    }
    private sealed class History
    {
        public string name = "", character = "", area = "", origin = "";
        public string[] native = Array.Empty<string>(), missing = Array.Empty<string>();
        public int chapter, maximum_deliveries;
        public int? budget_chapter, maximum_hours;
        public bool expectedFailure;
        public Step[] steps = Array.Empty<Step>();
    }
    private sealed class Inventory
    {
        public History[] histories = Array.Empty<History>();
        public string[] reactors = Array.Empty<string>(), retired_reactors = Array.Empty<string>();
    }
    private sealed class Delivery
    {
        public string scene = "";
        public int chapter, hour;
        public bool remote;
    }

    private static List<Delivery> Execute(Story story, History fixture, string? absentContact = null)
    {
        InventoryWorldBuilder.Require(!fixture.expectedFailure, "Production history expects failure: " + fixture.name);
        var world = new InventoryWorldBuilder(story, fixture.chapter, fixture.area);
        world.State.Hour = 0;
        foreach (var key in fixture.native) world.Native(key);
        if (fixture.chapter == 5) world.Native("longcon.chapter_five");
        if (fixture.chapter == 6) world.Native("chapter.six");
        var deliveries = new List<Delivery>();
        var missing = fixture.missing.ToHashSet();
        void Place(Scene scene)
        {
            // Native contact is an observation, not a fabricated return. Copies
            // must pass their real Requires and PlanPresence at their own anchor.
            if (absentContact != null && scene.ContactUnit == absentContact) return;
            if (scene.InteractionHub == null)
            {
                if (scene.ContactUnit != null) world.ObserveActor(scene.ContactUnit);
                return;
            }
            var key = scene.InteractionHub;
            if (key.EndsWith(".stall", StringComparison.Ordinal) || key == "galfrey.presence.sergeant_stall")
            {
                var primary = key == "galfrey.presence.sergeant_stall" ? "galfrey.presence.sergeant" : key[..^6];
                if (missing.Contains(primary)) { world.MissingAnchor(primary); world.Tick(primary); }
            }
            if (key.EndsWith(".arcade", StringComparison.Ordinal) || key.EndsWith(".awning", StringComparison.Ordinal))
            {
                var primary = key[..key.LastIndexOf('.')];
                if (missing.Contains(primary)) { world.MissingAnchor(primary); world.Tick(primary); }
            }
            if (missing.Contains(key)) world.MissingAnchor(key);
            else world.Anchor(key);
            world.Tick(key);
        }
        foreach (var step in fixture.steps)
        {
            if (step.chapter is int chapter)
            {
                world.Travel(chapter, step.area ?? world.State.Area);
                if (chapter == 6)
                {
                    // A live chapter etude stops playing on transition; clear
                    // every existing alias of Chapter05, retaining its latches.
                    foreach (var key in story.Etudes.Where(p => p.Value == "5b01aa690202e584888dfc600a4aac0a").Select(p => p.Key))
                        world.State.Flags.Remove(key);
                    world.Native("chapter.six");
                }
            }
            foreach (var key in step.native)
            {
                world.Native(key);
                if (key == "camellia.killed")
                    foreach (var actor in world.Actors.Where(a => a.Unit == "397b090721c41044ea3220445300e1b8"))
                        actor.Alive = false;
                world.Refresh();
            }
            if (step.scene == null) continue;
            var scene = world.Scene(step.scene);
            // A failed Camellia placement becomes observable inside the coffin
            // producer when Raised is set. Keep its actual anchor missing now.
            foreach (var key in missing.Where(k => story.Presences[k].Area == world.State.Area)) world.MissingAnchor(key);
            Place(scene);
            int deadline = world.State.Hour + 504;
            while (!world.Available(scene.Id) && world.State.Hour < deadline) world.Advance(1);
            InventoryWorldBuilder.Require(world.Available(scene.Id), "History cannot reach " + fixture.name + ": " + scene.Id);
            Place(scene);
            if (Rules.IsRemote(scene) && !scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
            {
                // Exactly what the production rest can deliver now, with the
                // real authored order/rotation competition still in the Story.
                var arrivals = Rules.MailbagArrivals(story, world.State);
                InventoryWorldBuilder.Require(arrivals.Any(s => s.Id == scene.Id),
                    "No actual mailbag arrival " + fixture.name + ": " + scene.Id
                    + "; arrived=" + string.Join(",", arrivals.Select(s => s.Id)));
            }
            var outcomes = world.Walk(scene.Id);
            var end = outcomes.FirstOrDefault(w => w.State.Has(scene.Id) && step.require.All(w.State.Has)
                && !step.require_absent.Any(w.State.Has));
            InventoryWorldBuilder.Require(end != null, "No positive outcome " + fixture.name + ": " + scene.Id
                + "; wanted=" + string.Join(",", step.require)
                + "; outcomes=" + string.Join(" | ", outcomes.Select(w => string.Join(",", w.State.Flags.Where(f => f.StartsWith("camellia") || f.StartsWith("chapter"))))));
            world = end!;
            deliveries.Add(new Delivery { scene = scene.Id, chapter = world.State.Chapter, hour = world.State.Hour,
                remote = Rules.IsRemote(scene) && !scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal) });
        }
        using var ledger = JsonDocument.Parse(File.ReadAllText("tools/remote_allocation_contracts.json"));
        var allocation = ledger.RootElement.GetProperty("allocations").EnumerateArray()
            .Single(a => a.GetProperty("character").GetString() == fixture.character);
        foreach (var chapter in deliveries.Select(d => d.chapter).Distinct())
        {
            int count = deliveries.Count(d => d.chapter == chapter && d.remote);
            int limit = allocation.GetProperty("limits").GetProperty(chapter.ToString()).GetInt32();
            InventoryWorldBuilder.Require(count <= limit, "Over-budget production history " + fixture.name + ": " + count + "/" + limit);
        }
        int budgetChapter = fixture.budget_chapter ?? fixture.chapter;
        InventoryWorldBuilder.Require(deliveries.Count(d => d.chapter == budgetChapter && d.remote) <= fixture.maximum_deliveries,
            "Exceeded declared history budget " + fixture.name);
        if (fixture.maximum_hours is int maximum)
        {
            InventoryWorldBuilder.Require(world.State.Times.TryGetValue(fixture.origin, out int origin), "Missing cumulative origin");
            InventoryWorldBuilder.Require(world.State.Hour - origin <= maximum,
                "Cumulative pacing exceeds " + maximum + "h: " + fixture.name + " at " + (world.State.Hour - origin));
        }
        Console.WriteLine("eng8-q8d delivered history " + JsonSerializer.Serialize(new { fixture.name,
            fixture.character, deliveries, hour = world.State.Hour, origin = fixture.origin,
            times = world.State.Times.Where(p => p.Key == fixture.origin).ToDictionary(p => p.Key, p => p.Value),
            evidence = "MailbagArrivals_and_observed_contacts_and_paid_choices", expectedFailure = false }, Options));
        return deliveries;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        var inventory = JsonSerializer.Deserialize<Inventory>(File.ReadAllText("tools/delivery_inventory2_contracts.json"), Options)!;
        foreach (var fixture in inventory.histories) Execute(story, fixture);
        check(inventory.histories.Length >= 20, "Missing delivered-history coverage");
        foreach (var sid in inventory.retired_reactors)
            check(story.Scenes.Single(s => s.Id == sid).Forbids.Contains("trickster.ever"), "Active unallocated reactor " + sid);
        check(story.Scenes.Where(s => s.Id.StartsWith("galfrey.trickster.react.", StringComparison.Ordinal)
            && !s.Forbids.Contains("trickster.ever")).Select(s => s.Owner).Distinct().OrderBy(s => s)
            .SequenceEqual(inventory.reactors.OrderBy(s => s)), "Wrong active Galfrey reactor allocation");

        // Independent diagnostic mutations are expected to be rejected; no
        // production-positive history is marked expectedFailure=true.
        void Reject(string label, Action<Story> mutate, History fixture, string? absentContact = null)
        {
            var changed = JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(story, Options), Options)!;
            mutate(changed);
            bool rejected = false;
            try { Execute(changed, fixture, absentContact); }
            catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Delivery mutation survived: " + label);
        }
        var galfrey = inventory.histories.First(h => h.name == "galfrey-scarred-stall-sworn");
        Reject("96h scarred return", s => s.Scenes.Single(a => a.Id == "galfrey.trickster.return.kitrane_scarred_stall").DelayHours = 96, galfrey);
        Reject("remote tent", s => s.Scenes.Single(a => a.Id == "galfrey.trickster.visit.tent_stall").Remote = true, galfrey);
        Reject("missing sergeant contact", _ => { }, galfrey, absentContact: "8a23e71893cf8ab428e7ebd64b10ad27");
        var horzalah = inventory.histories.First(h => h.name == "horzalah-fresh-unmet.knife-tested");
        Reject("missing gift test", s => {
            foreach (var n in s.Scenes.Single(a => a.Id == "horzalah.trickster.unmet.knife").Nodes)
                foreach (var c in n.Choices) c.Set = c.Set.Where(f => f != "horzalah.trickster.tested").ToArray();
        }, horzalah);
        Reject("unfolded second Chapter 6 rest", s => {
            var n = s.Scenes.Single(a => a.Id == "horzalah.trickster.unmet.knife").Nodes.Single(n => n.Id == "exit");
            n.Choices.Last().Next = null;
        }, horzalah);
        Console.WriteLine("PASS: E-Q8-07 delivered histories, cumulative pacing, allocated reactors and negative mutations");
    }
}
