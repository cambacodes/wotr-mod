using System;
using System.Linq;
using Tirabade;

// Shared by RulesTests and the real-assembly Mono suite. No Unity view is constructed:
// the observations reproduce its delayed activation deterministically.
internal static class PresenceRuntimeF9Tests
{
    public static void Run(Action<bool, string> check)
    {
        var primary = new Presence { Mode = "spawn-copy", At = new PresenceAnchor { NearUnit = "anchor" },
            Forbids = new[] { "fixture.failed" } };
        int Simulate(bool fixedEngine, bool anchor, bool activates)
        {
            var readiness = new PresenceReadiness();
            bool failed = false, submitted = false;
            int spawns = 0, removals = 0, fallbackEntries = 0, copyAge = 0, fallbackSpawns = 0;
            bool fallback = false;
            bool fallbackCopy = false;
            var alternate = new Presence { Mode = "spawn-copy", At = new PresenceAnchor { NearUnit = "other-anchor" } };
            for (int tick = 0; tick < 80; tick++)
            {
                if (submitted) copyAge++;
                bool wanted = !failed;
                var seen = new PresenceObservation { AreaLoaded = true, AnchorResolved = anchor,
                    Submitted = submitted, Recorded = submitted, CopyFound = submitted, CopyAlive = submitted,
                    CopyUsable = submitted && activates && copyAge >= 2,
                    NativeCount = fallbackCopy ? 1 : 0, NativeAlive = fallbackCopy, NativeUsable = fallbackCopy,
                    NativeOwnedCopy = fallbackCopy };
                if (fixedEngine) seen.CopyInitializing = readiness.Pending(submitted ? "same-copy" : null, seen, !seen.CopyUsable, tick * 0.25);
                var steps = Rules.PlanPresence(primary, fixedEngine || wanted, seen);
                if (fallbackCopy) check(!steps.Contains(PresenceStep.RecordNativeContact),
                    "F9: primary adopted its fallback copy as a native and cleared failure");
                if (steps.Contains(PresenceStep.Spawn)) { submitted = true; spawns++; copyAge = 0; }
                if (steps.Contains(PresenceStep.Remove)) { submitted = false; removals++; }
                seen.Submitted = seen.Recorded = seen.CopyFound = seen.CopyAlive = submitted;
                seen.CopyUsable = submitted && activates && copyAge >= 2;
                if (fixedEngine) seen.CopyInitializing = readiness.Pending(submitted ? "same-copy" : null, seen, !seen.CopyUsable, tick * 0.25);
                // Old runtime already calculated demand separately, but planned removal from wanted.
                failed = Rules.PresenceFailed(primary, true, seen);
                if (failed && !fallback) fallbackEntries++;
                fallback = failed;
                // The legitimate absent-anchor case delivers the same blueprint at its alternate anchor.
                if (!anchor)
                {
                    var alternateSeen = new PresenceObservation { AreaLoaded = true, AnchorResolved = true,
                        Recorded = fallbackCopy, Submitted = fallbackCopy, CopyFound = fallbackCopy,
                        CopyAlive = fallbackCopy, CopyUsable = fallbackCopy };
                    var alternateSteps = Rules.PlanPresence(alternate, failed, alternateSeen);
                    if (alternateSteps.Contains(PresenceStep.Spawn)) { fallbackSpawns++; fallbackCopy = true; }
                    if (alternateSteps.Contains(PresenceStep.Remove)) fallbackCopy = false;
                }
            }
            if (fixedEngine && anchor && activates) check(spawns == 1 && removals == 0 && fallbackEntries == 0,
                "F9: inactive spawn view removed the primary or entered fallback");
            if (fixedEngine && (!anchor || !activates)) check(fallbackEntries == 1 && removals == 0,
                "F9: genuine failure must enter fallback once, without respawn cycles");
            if (fixedEngine && !anchor) check(spawns == 0 && fallbackSpawns == 1 && fallbackCopy,
                "F9: absent primary anchor must spawn and retain its legitimate fallback exactly once");
            return spawns;
        }
        check(Simulate(false, true, true) >= 20, "F9: legacy simulation must reproduce the spawn/failure/removal loop before a view can activate");
        Simulate(true, true, true);
        Simulate(true, true, false);
        Simulate(true, false, false);

        var lease = new PresenceReadiness();
        var copy = new PresenceObservation { AreaLoaded = true, Submitted = true, CopyFound = true, CopyAlive = true, CopyUsable = false };
        check(lease.Pending("copy", copy, false, 0), "F9: fresh live copy failed before its view/state finished initializing");
        check(lease.Pending("copy", copy, true, 0), "F9: spawn tick has no grace");
        check(!lease.Pending("copy", copy, true, PresenceReadiness.GraceSeconds), "F9: never usable copy grace is unbounded");
        copy.CopyUsable = true; lease.Pending("copy", copy, false, 11);
        copy.CopyUsable = false;
        copy.CopyInitializing = lease.Pending("copy", copy, true, 100);
        check(!Rules.PresenceFailed(primary, true, copy), "F9: distance-culled view invalidated a previously usable placement");
        copy.CopyFound = false;
        check(!lease.Pending("copy", copy, true, 100), "F9: a missing previously usable actor was confused with a culled view");
        copy.CopyFound = true;
        var sibling = new PresenceObservation { AreaLoaded = true, NativeCount = 1, NativeAlive = true, NativeUsable = true, NativeOwnedCopy = true };
        check(Rules.PresenceFailed(primary, true, sibling)
            && !Rules.PlanPresence(primary, true, sibling).Contains(PresenceStep.Spawn),
            "F9: a sibling's saved copy must neither clear primary failure nor permit duplication");
        copy.AnchorResolved = false;
        copy.CopyInitializing = true;
        check(Rules.PresenceFailed(primary, true, copy), "F9: grace concealed an absent anchor");
        copy.AnchorResolved = true; copy.CopyAlive = false; copy.CopyInitializing = false;
        check(Rules.PresenceFailed(primary, true, copy), "F9: grace concealed a dead copy");
        copy.CopyAlive = true;
        check(Rules.PlanPresence(primary, false, copy).Contains(PresenceStep.Remove), "F9: closed demand did not retire its copy");
        copy.AreaLoaded = false; lease.Pending("copy", copy, true, 101);
        copy.AreaLoaded = true;
        check(lease.Pending("copy", copy, true, 200), "F9: reload/area arrival did not give the view a fresh grace");

        var hostile = new CopyObservation { Enemy = true, Silenced = true, Passive = true };
        check(Rules.PlanQuiet(hostile) == (CopyQuiet.Faction | CopyQuiet.Group), "F9: hostile non-Player copy was left an enemy");
        hostile.Enemy = false;
        check(Rules.PlanQuiet(hostile) == CopyQuiet.None, "F9: repaired neutral copy was repaired again");
        Console.WriteLine("PASS: F9 delayed view/legacy oscillation, grace expiry, absent-anchor fallback once, culling/loss and hostile-copy repair.");
    }
}
