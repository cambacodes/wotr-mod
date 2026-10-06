using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng8-q8e: final production readers, including losses after historical returns.
internal static class ImplicitParticipantInventoryTests
{
    internal static void Observe(Story story, Snapshot state)
    {
        state.Flags.ExceptWith(story.Derived.Keys);
        Rules.Complete(story, state);
    }
    internal static Snapshot World(Story story, Scene scene, params string[] extra)
    {
        var state = new Snapshot { Chapter = scene.Chapters.FirstOrDefault(scene.MinChapter), Hour = 10000,
            Area = scene.Areas.FirstOrDefault() ?? "" };
        var visited = new HashSet<string>();
        bool Compatible(string key, HashSet<string>? seen = null)
        {
            if (scene.Forbids.Contains(key) && !scene.ForbidOverrides.ContainsKey(key)) return false;
            if (!story.Derived.TryGetValue(key, out var groups)) return true;
            seen ??= new HashSet<string>();
            if (!seen.Add(key)) return false;
            bool result = groups.Any(g => g.All(k => Compatible(k, seen)));
            seen.Remove(key); return result;
        }
        void Earn(string key)
        {
            if (!visited.Add(key)) return;
            if (story.Derived.TryGetValue(key, out var groups))
                foreach (var flag in groups.First(g => g.All(k => Compatible(k)))) Earn(flag);
            else state.Flags.Add(key);
        }
        foreach (var key in Program.Prerequisites(scene).Concat(extra)) Earn(key);
        foreach (var contact in scene.AdditionalContactUnits.Concat(new[] { scene.ContactUnit }).Where(c => c != null))
            state.AvailableContacts.Add(contact!);
        state.Flags.Add("trickster");
        Observe(story, state);
        return state;
    }
    internal static void Run(Story story, Action<bool, string> check)
    {
        if (!story.Derived.ContainsKey("participant.vellexia.available")) return; // legacy story
        using var doc = JsonDocument.Parse(File.ReadAllText("tools/implicit_participant_inventory_contracts.json"));
        int count = 0;
        foreach (var row in doc.RootElement.GetProperty("consumers").EnumerateArray())
        {
            count++;
            string id = row.GetProperty("scene").GetString()!, reader = row.GetProperty("reader").GetString()!;
            var scene = story.Scenes.Single(s => s.Id == id);
            var live = World(story, scene, reader);
            check(live.Has(reader), "Q8-05 missing living reader: " + id);
            string[] losses = reader.Contains("chivarro") ? new[] { "minachiv.closed", "minagho_chivarro.trickster.chivarro_sent_back" }
                : reader.Contains("hepzamirah") ? new[] { "hepzamirah.closed", "hepzamirah.trickster.cost.confined" }
                : new[] { "vellexia.closed", "vellexia.parted", "vellexia.trickster.kept_as_mirror" };
            foreach (string loss in losses)
            {
                var absent = Program.Copy(live);
                absent.Flags.Add(loss);
                Observe(story, absent);
                check(!absent.Has(reader), "Q8-05 historical presence survived " + loss);
                if (row.GetProperty("kind").GetString() == "scene")
                {
                    check(Rules.Available(story, scene, live), "Q8-05 valid scene unavailable: " + id);
                    check(!Rules.Available(story, scene, absent), "Q8-05 absent participant: " + id + "/" + loss);
                    var requires = scene.Requires;
                    try {
                        scene.Requires = requires.Where(k => k != reader).ToArray();
                        // L14 independently blocks pair closure. The sent-back witness
                        // isolates this lane's extra departure input after that merge.
                        if (!reader.Contains("chivarro") || loss != "minachiv.closed")
                            check(Rules.Available(story, scene, absent), "Q8-05 mutation did not expose consumer: " + id);
                    } finally { scene.Requires = requires; }
                }
                else
                {
                    var edges = scene.Nodes.SelectMany(n => n.Choices).Where(c => c.Next == "sister").ToArray();
                    check(edges.Length == 4 && edges.All(c => c.Requires.Contains(reader)), "Q8-05 sibling edge omitted");
                    check(edges.All(c => !Rules.ChoiceAvailable(c, absent)), "Q8-05 departed sister at forge");
                    // Each existing conditional incoming edge has an appended exclusive absence twin.
                    foreach (var node in scene.Nodes.Where(n => n.Choices.Any(c => c.Next == "sister")))
                    {
                        var yes = node.Choices.Single(c => c.Next == "sister");
                        var no = node.Choices.Single(c => c.Next == "sister_absent");
                        var ready = Program.Copy(live);
                        foreach (var k in yes.Requires.Where(k => k != reader)) ready.Flags.Add(k);
                        ready.Flags.ExceptWith(yes.Forbids);
                        Observe(story, ready);
                        check(Rules.ChoiceAvailable(yes, ready) && !Rules.ChoiceAvailable(no, ready), "Q8-05 live sister edge unavailable");
                        ready.Flags.Add(loss); Observe(story, ready);
                        check(!Rules.ChoiceAvailable(yes, ready) && Rules.ChoiceAvailable(no, ready), "Q8-05 absence fallback unavailable");
                    }
                }
                if (row.TryGetProperty("presences", out var names)) foreach (var name in names.EnumerateArray())
                {
                    var p = story.Presences[name.GetString()!];
                    foreach (var anchor in new[] { "normal", "fool_king.gone", "herrax.presence.rokhorn.failed" })
                    {
                        var spawned = Program.Copy(absent); spawned.Area = p.Area;
                        foreach (var key in p.Requires.Where(k => k != reader)) spawned.Flags.Add(key);
                        foreach (var group in p.RequiresAnyGroups) spawned.Flags.Add(group[0]);
                        if (anchor != "normal") spawned.Flags.Add(anchor);
                        Observe(story, spawned);
                        check(!Rules.PresenceWanted(p, spawned), "Q8-05 pending ghost discovery spawn: " + name + "/" + anchor);
                    }
                }
            }
        }
        check(count == 5, "Q8-05 omitted consumer");
        Console.WriteLine("Q8-05: five implicit consumers; departure, closure, body, alternate anchors and mutations passed");
    }
}
