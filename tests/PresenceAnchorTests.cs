using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E12b: presences anchored At a native unit or locator; never spawned without a live anchor; <key>.failed for the letter twin.
internal static class PresenceAnchorTests
{
    private const string Capital = "2570015799edf594daf2f076f2f975d8";
    private const string Kyado = "db064cafc234498ca83a702c472c1a7b";   // any native BlueprintUnit (fixture: Pharasma)

    internal static void Run(Action<bool, string> check)
    {
        Story Fixture(PresenceAnchor at)
        {
            var story = TricksterLatchTests.Fixture();
            story.Presences["irabeth.presence"] = new Presence { Unit = "280d4712dceb37f4a88e98f1f4c6e64f", Area = Capital, Mode = "spawn-copy",
                Requires = new[] { "trickster.ever" }, At = at };
            // The letter twin waits on the runtime failure observation.
            story.Scenes.Add(new Scene { Id = "irabeth.trickster.letter_twin", Title = "t", Owner = "Memory", Remote = true, Relationship = "irabeth",
                Requires = new[] { "irabeth.presence.failed" },
                Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } } });
            return story;
        }
        var story = Fixture(new PresenceAnchor { NearUnit = Kyado, Side = "right", Distance = 2f });
        Rules.Validate(story);
        Rules.Validate(Fixture(new PresenceAnchor { Locator = "adee9a01-42a3-4850-b2d1-4a3dfcee9369", Offset = new[] { 1f, -0.5f } }));
        check(Rules.PresenceFailedFlag("irabeth.presence") == "irabeth.presence.failed", "Failure flag name changed.");

        // Offsets: facing north (0 deg), "right" is +x; the copy faces back toward the anchor.
        var right = Rules.AnchorOffset(new PresenceAnchor { Side = "right", Distance = 2f }, 0f);
        check(Math.Abs(right.Dx - 2f) < 1e-4 && Math.Abs(right.Dz) < 1e-4 && Math.Abs(right.Facing - 270f) < 1e-3, "Right-of-anchor offset or facing wrong.");
        var front = Rules.AnchorOffset(new PresenceAnchor { Side = "front", Distance = 1.5f }, 90f);
        check(Math.Abs(front.Dx - 1.5f) < 1e-4 && Math.Abs(front.Dz) < 1e-4 && Math.Abs(front.Facing - 270f) < 1e-3, "Front offset ignores the anchor's facing.");
        var raw = Rules.AnchorOffset(new PresenceAnchor { Offset = new[] { 0f, -1f } }, 123f);
        check(raw.Dx == 0f && raw.Dz == -1f && Math.Abs(raw.Facing) < 1e-3, "Explicit offset changed or facing wrong.");

        // Plan: an unresolved anchor never spawns; a resolved one does.
        var p = story.Presences["irabeth.presence"];
        check(Rules.PlanPresence(p, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = false }).SequenceEqual(new[] { PresenceStep.Blocked }),
            "Spawned without a live anchor.");
        check(Rules.PlanPresence(p, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = true }).SequenceEqual(new[] { PresenceStep.Spawn }),
            "Resolved anchor did not spawn.");
        // NM1: the runtime failure observation (GuestPresence.Tick reports Rules.PresenceFailed). A spawn-copy fails only without
        // its anchor; a reuse-native presence also fails at a resolved anchor when no single live, friendly native actor stands there.
        check(Rules.PresenceFailed(p, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = false })
              && !Rules.PresenceFailed(p, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = true })
              && !Rules.PresenceFailed(p, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = false, NativeAlive = true })
              && !Rules.PresenceFailed(p, false, new PresenceObservation { AreaLoaded = true, AnchorResolved = false })
              && !Rules.PresenceFailed(p, true, new PresenceObservation { AreaLoaded = false, AnchorResolved = false }),
            "Spawn-copy failure observation changed.");
        foreach (var native in new[] {
            new Presence { Unit = p.Unit, Area = Capital, Mode = "reuse-native", At = new PresenceAnchor { Locator = "adee9a01-42a3-4850-b2d1-4a3dfcee9369" } },
            new Presence { Unit = p.Unit, Area = Capital, Mode = "reuse-native" } })
        {
            var missing = new PresenceObservation { AreaLoaded = true, AnchorResolved = true, NativeAlive = false };
            check(Rules.PresenceFailed(native, true, missing) && Rules.PlanPresence(native, true, missing).Length == 0,
                "A reuse-native presence with a resolved anchor and no native actor is not reported as failed.");
            check(Rules.PresenceFailed(native, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = false }),
                "A reuse-native presence with neither anchor nor actor is not reported as failed.");
            check(!Rules.PresenceFailed(native, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = true, NativeAlive = true, NativeHidden = true })
                  && !Rules.PresenceFailed(native, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = false, NativeAlive = true })
                  && !Rules.PresenceFailed(native, false, missing) && !Rules.PresenceFailed(native, true, new PresenceObservation { AreaLoaded = false }),
                "A placeable, unwanted or unloaded reuse-native presence is reported as failed.");
        }
        // Eligibility of the letter twin follows the runtime observation.
        var state = new Snapshot { Chapter = 5, Hour = 100 };
        var twin = story.Scenes.Single(s => s.Id == "irabeth.trickster.letter_twin");
        check(!Rules.Available(story, twin, state), "Letter twin available before the presence failed.");
        state.Flags.Add("irabeth.presence.failed");
        check(Rules.Available(story, twin, state), "Letter twin unavailable after the presence failed.");

        foreach (var (what, at) in new List<(string, PresenceAnchor)> {
            ("both anchors", new PresenceAnchor { NearUnit = Kyado, Locator = "x" }),
            ("no anchor", new PresenceAnchor()),
            ("bad unit guid", new PresenceAnchor { NearUnit = "nope" }),
            ("bad side", new PresenceAnchor { NearUnit = Kyado, Side = "above" }),
            ("far distance", new PresenceAnchor { NearUnit = Kyado, Distance = 30f }),
            ("offset and side", new PresenceAnchor { NearUnit = Kyado, Offset = new[] { 1f, 1f }, Side = "left" }),
            ("short offset", new PresenceAnchor { NearUnit = Kyado, Offset = new[] { 1f } }) })
        {
            bool rejected = false;
            try { Rules.Validate(Fixture(at)); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid presence anchor accepted: " + what);
        }
        var authored = Fixture(new PresenceAnchor { NearUnit = Kyado });
        authored.Scenes[0].Nodes[0].Choices[0].Set = new[] { "irabeth.presence.failed" };
        bool authoredRejected = false;
        try { Rules.Validate(authored); } catch (InvalidOperationException) { authoredRejected = true; }
        check(authoredRejected, "The runtime failure observation was authored.");
    }
}
