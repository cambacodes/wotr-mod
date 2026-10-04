using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng7-l05: E-Q7-02. Replays are pure observations; no game, native restoration or harness is run.
internal static class PresenceTransitionInventoryTests
{
    private static readonly JsonSerializerOptions Json = new JsonSerializerOptions { IncludeFields = true };
    private static PresenceObservation Reload(PresenceObservation seen) =>
        JsonSerializer.Deserialize<PresenceObservation>(JsonSerializer.Serialize(seen, Json), Json)!;

    internal static void Run(Story story, Action<bool, string> check)
    {
        if (!story.Presences.ContainsKey("gesmerha.presence")) return;
        var managed = new[] { "gesmerha.presence", "jannah.presence", "jannah.presence.cells", "jannah.presence.back",
            "shamira.presence", "shamira.presence.awning", "kiana.presence" };
        foreach (var key in managed)
        {
            var p = story.Presences[key];
            check(p.ManageNative == managed.Contains(key), key + " native management was not explicitly nominated.");
            PresenceStep[] Plan(PresenceObservation s, bool wanted = true) => Rules.PlanPresence(p, wanted, s);
            bool Failed(PresenceObservation s) => Rules.PresenceFailed(p, true, s);
            var hidden = new PresenceObservation { AreaLoaded = true, NativeCount = 1, NativeAlive = true,
                NativeHidden = true, NativeUsable = false, NativeAtPosition = false };
            if (p.ManageNative)
            {
                check(Plan(hidden).SequenceEqual(new[] { PresenceStep.Adopt, PresenceStep.Unhide, PresenceStep.Move }), key + " leaves its hidden native unreachable.");
                var displaced = Reload(hidden);
                displaced.NativeHidden = false;
                displaced.NativeUsable = true;
                check(Plan(displaced).SequenceEqual(new[] { PresenceStep.Adopt, PresenceStep.Move }), key + " accepts a displaced native at the wrong location.");
                var placed = Reload(hidden);
                placed.Recorded = placed.RecordedNative = placed.NativeUsable = placed.NativeAtPosition = true;
                placed.NativeHidden = false;
                for (int tick = 0; tick < 3; tick++)
                {
                    placed = Reload(placed);
                    check(Plan(placed).Length == 0 && !Failed(placed), key + " placed native is not idempotent across ticks/load.");
                }
                check(Plan(placed, false).SequenceEqual(new[] { PresenceStep.RestoreNative }), key + " teardown loses original native visibility/placement.");
                placed.NativeAlive = false;
                placed.NativeCount = 0;
                check(Plan(placed, false).SequenceEqual(new[] { PresenceStep.Forget }), key + " teardown restores a subsequently dead native.");
                // Mutation of the explicit policy must reproduce the original hidden actor failure.
                p.ManageNative = false;
                check(Plan(hidden).SequenceEqual(new[] { PresenceStep.Blocked }) && Failed(hidden), key + " missing-management mutation does not reproduce failure.");
                p.ManageNative = true;
            }
            else check(Plan(hidden).SequenceEqual(new[] { PresenceStep.Blocked }) && Failed(hidden), key + " hidden native suppresses both placement and failure.");

            var absent = new PresenceObservation { AreaLoaded = true };
            check(Plan(absent).SequenceEqual(new[] { PresenceStep.Spawn }) && !Failed(absent), key + " missing native cannot use earned copy placement.");
            var copy = new PresenceObservation { AreaLoaded = true, Recorded = true, Submitted = true, CopyFound = true, CopyAlive = true };
            check(Plan(copy).Length == 0 && !Failed(copy) && Plan(Reload(copy)).Length == 0, key + " delivered copy repeats placement after load.");
            check(Plan(copy, false).SequenceEqual(new[] { PresenceStep.Remove }), key + " closure keeps an owned copy.");
            var deadCopy = Reload(copy);
            deadCopy.CopyAlive = deadCopy.CopyUsable = false;
            check(Plan(deadCopy).SequenceEqual(new[] { PresenceStep.Blocked }) && Failed(deadCopy), key + " dead copy suppresses accurate failure or is resurrected.");
            var vanished = Reload(copy);
            vanished.CopyFound = vanished.CopyAlive = vanished.CopyUsable = false;
            check(Plan(vanished).SequenceEqual(new[] { PresenceStep.Blocked }) && Failed(vanished), key + " lost submitted copy is respawned or silently accepted.");
            var hostile = new PresenceObservation { AreaLoaded = true, NativeCount = 1, NativeUsable = false, NativeManageable = false };
            check(Plan(hostile).SequenceEqual(new[] { PresenceStep.Blocked }) && Failed(hostile), key + " hostile native is duplicated/adopted.");
            var suppressed = Reload(hidden);
            suppressed.NativeManageable = false;
            check(Plan(suppressed).SequenceEqual(new[] { PresenceStep.Blocked }) && Failed(suppressed), key + " suppressed/unconscious native is awakened.");
            var missingAnchor = Reload(hidden);
            missingAnchor.AnchorResolved = false;
            check(Plan(missingAnchor).SequenceEqual(new[] { PresenceStep.Blocked }) && Failed(missingAnchor), key + " missing anchor permits off-location native placement.");
            var duplicates = Reload(copy);
            duplicates.NativeCount = 2;
            duplicates.NativeAlive = true;
            duplicates.ContactAmbiguous = true;
            check(Plan(duplicates).SequenceEqual(new[] { PresenceStep.Blocked }) && Failed(duplicates), key + " arbitrary living twins are adopted or deleted.");

            // Native Q3 introduces one usable real actor beside the owned copy. Contact stays ambiguous until retirement.
            var arrived = Reload(copy);
            arrived.NativeAlive = arrived.NativeUsable = true;
            arrived.NativeCount = 1;
            arrived.ContactAmbiguous = true;
            check(Plan(arrived).SequenceEqual(new[] { PresenceStep.Remove, PresenceStep.RecordNativeContact }), key + " native-after-copy transition does not retire just the owned copy and record the handoff.");
            var actors = new List<Actor> { new Actor { Usable = true }, new Actor { Usable = true } };
            check(Rules.SingleUsable(actors, a => a.Usable, a => a.Dead) == null, key + " two usable actors were not ambiguous before transition.");
            actors.RemoveAt(0); // executor retires only the UnitId recorded as owned
            check(Rules.SingleUsable(actors, a => a.Usable, a => a.Dead) != null, key + " native cannot supply the surviving contact.");
            arrived.CopyFound = arrived.CopyAlive = false;
            arrived.Recorded = arrived.RecordedNativeContact = true;
            arrived.Submitted = arrived.ContactAmbiguous = false;
            check(Plan(arrived).Length == 0 && !Failed(arrived) && Plan(Reload(arrived)).Length == 0, key + " native handoff is not stable across reload.");
            var lostNative = Reload(arrived);
            lostNative.NativeCount = 0;
            lostNative.NativeAlive = lostNative.NativeUsable = lostNative.NativeManageable = false;
            check(Plan(lostNative).SequenceEqual(new[] { PresenceStep.Blocked }) && Failed(lostNative), key + " subsequently lost native is resurrected by spawning another copy.");
            actors.Insert(0, new Actor { Dead = true });
            check(Rules.SingleUsable(actors, a => a.Usable, a => a.Dead) != null, key + " dead original breaks one usable contact (Wenduag #27).");
        }

        // An observation flag cannot turn its own failure observation off on the next tick.
        var primary = story.Presences["shamira.presence"];
        var hubScene = story.Scenes.First(s => s.InteractionHub == "shamira.presence");
        var failedWorld = ParticipantInventoryTests.World(story, hubScene);
        failedWorld.Flags.Add("shamira.presence.failed");
        check(!Rules.PresenceWanted(primary, failedWorld)
            && Rules.PresenceWanted(primary, failedWorld, "shamira.presence.failed"), "Primary/awning delivery failure oscillates across observations.");
        check(!Rules.ContactAvailable(story, hubScene, failedWorld), "Failed primary hub advertises the fallback's generic native actor.");

        using var backlog = JsonDocument.Parse(File.ReadAllText(Path.Combine("tools", "engine_backlog.json")));
        int physical = 0, postal = 0;
        foreach (var finding in backlog.RootElement.GetProperty("findings").EnumerateArray()
            .Where(f => f.GetProperty("item_id").GetString() == "E-Q7-02"))
        {
            string id = finding.GetProperty("scene").GetString()!;
            var scene = story.Scenes.Single(s => s.Id == id);
            var live = ParticipantInventoryTests.World(story, scene);
            check(Rules.Available(story, scene, live), "Nominated transition consumer is unreachable in its earned history: " + id);
            if (scene.ContactUnit != null)
            {
                physical++;
                live.AvailableContacts.Remove(scene.ContactUnit);
                check(!Rules.Available(story, scene, live), id + " starts without the intended usable actor.");
                live.AvailableContacts.Add(scene.ContactUnit);
                check(Rules.Available(story, scene, live), id + " cannot resume after native handoff/dead-original disambiguation.");
                live.Area = "another-area";
                check(!Rules.Available(story, scene, live), id + " ignores location compliance.");
            }
            else
            {
                postal++;
                live.Flags.Remove("kiana.presence.failed");
                check(!Rules.Available(story, scene, live), id + " postal fallback does not read actual delivery failure.");
                live.Flags.Add("kiana.presence.failed");
                live.Flags.Add("kiana.closed");
                check(!Rules.Available(story, scene, live), id + " delivery failure reopens a deliberate closure.");
            }
        }
        check(physical == 23 && postal == 2, "Mapped actor consumer census changed: " + physical + "/" + postal);
        ContactDisambiguationTests.Run(check);
        Console.WriteLine("presence transition inventory: 7 placements, 23 physical consumers and 2 accurate postal failures; owned-copy/native and reload cases passed.");
    }

    private sealed class Actor { internal bool Usable, Dead; }
}
