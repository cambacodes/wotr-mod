using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E12 (GLOBAL-07-lite): Story.Presences validation, eligibility (Rules.PresenceWanted) and the runtime plan (Rules.PlanPresence).
internal static class PresenceTests
{
    private const string Capital = "2570015799edf594daf2f076f2f975d8";
    private const string IrabethUnit = "280d4712dceb37f4a88e98f1f4c6e64f";

    private static Story Fixture()
    {
        var story = TricksterLatchTests.Fixture();
        story.Relationships["irabeth"].UnavailableOverrides["irabeth_dead"] = "irabeth.trickster.returned";
        story.Presences["irabeth.presence"] = new Presence
        {
            Unit = IrabethUnit, Area = Capital, Mode = "spawn-copy", MinChapter = 5, MaxChapter = 5,
            Requires = new[] { "trickster.ever", "irabeth.trickster.returned" }, Forbids = new[] { "irabeth.closed" },
            Position = new PresencePosition { X = 7.5f, Y = 62f, Z = -28f, Orientation = 180f },
            AnswerLists = new[] { "871af36f2ab2b1f40b5de77976c54276" }
        };
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);
        var p = story.Presences["irabeth.presence"];
        var state = new Snapshot { Chapter = 5, Hour = 100, Area = Capital };
        check(!Rules.PresenceWanted(p, state), "Presence wanted before the return.");
        state.Flags.UnionWith(new[] { "trickster.ever", "irabeth.trickster.returned", "irabeth_dead" });
        check(Rules.PresenceWanted(p, state), "Returned presence not wanted in its area and chapter.");
        foreach (var (what, mutate) in new (string, Action<Snapshot>)[] {
            ("another area", s => s.Area = "0123456789abcdef0123456789abcdef"), ("chapter 4", s => s.Chapter = 4),
            ("closed", s => s.Flags.Add("irabeth.closed")), ("no latch", s => s.Flags.Remove("trickster.ever")) })
        {
            var other = Program.Copy(state);
            mutate(other);
            check(!Rules.PresenceWanted(p, other), "Presence wanted with " + what);
        }

        // spawn-copy plan: spawn once; never while a native unit stands; never twice for one record; remove when unwanted.
        PresenceStep[] Plan(bool wanted, PresenceObservation seen) => Rules.PlanPresence(p, wanted, seen);
        check(Plan(true, new PresenceObservation()).Length == 0, "Acted without the area loaded.");
        check(Plan(true, new PresenceObservation { AreaLoaded = true }).SequenceEqual(new[] { PresenceStep.Spawn }), "No spawn for a wanted absent guest.");
        check(Plan(true, new PresenceObservation { AreaLoaded = true, NativeAlive = true }).Length == 0, "Spawned beside a live native unit.");
        check(Plan(true, new PresenceObservation { AreaLoaded = true, Recorded = true, Submitted = true }).SequenceEqual(new[] { PresenceStep.Blocked }),
            "A submitted copy that vanished was spawned again.");
        check(Plan(true, new PresenceObservation { AreaLoaded = true, Recorded = true, Submitted = true, CopyFound = true, CopyAlive = true }).Length == 0,
            "A standing copy was touched.");
        check(Plan(true, new PresenceObservation { AreaLoaded = true, Recorded = true, Submitted = true, CopyFound = true }).SequenceEqual(new[] { PresenceStep.Blocked }),
            "A dead copy was replaced.");
        check(Plan(false, new PresenceObservation { AreaLoaded = true, Recorded = true, Submitted = true, CopyFound = true, CopyAlive = true })
            .SequenceEqual(new[] { PresenceStep.Remove }), "An unwanted copy was not removed.");
        check(Plan(false, new PresenceObservation { AreaLoaded = true, Recorded = true, Submitted = true }).SequenceEqual(new[] { PresenceStep.Forget }),
            "A stale record was kept.");

        // reuse-native plan: unhide/move only an existing live unit; re-hide only what we unhid.
        var reuse = new Presence { Unit = IrabethUnit, Area = Capital, Mode = "reuse-native", Position = p.Position };
        check(Rules.PlanPresence(reuse, true, new PresenceObservation { AreaLoaded = true }).Length == 0, "reuse-native created a unit.");
        check(Rules.PlanPresence(reuse, true, new PresenceObservation { AreaLoaded = true, NativeAlive = true, NativeHidden = true, NativeAtPosition = false })
            .SequenceEqual(new[] { PresenceStep.Unhide, PresenceStep.Move }), "reuse-native did not unhide and move the native unit.");
        check(Rules.PlanPresence(reuse, false, new PresenceObservation { AreaLoaded = true, NativeAlive = true, RecordedUnhide = true, Recorded = true })
            .SequenceEqual(new[] { PresenceStep.Hide }), "reuse-native did not re-hide what it unhid.");
        check(Rules.PlanPresence(reuse, false, new PresenceObservation { AreaLoaded = true, NativeAlive = true }).Length == 0,
            "reuse-native hid a unit it never unhid.");

        void Invalid(string what, Action<Story, Presence> mutate)
        {
            var bad = Fixture();
            mutate(bad, bad.Presences["irabeth.presence"]);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid presence accepted: " + what);
        }
        Invalid("unknown relationship key", (s, x) => { s.Presences.Remove("irabeth.presence"); s.Presences["nobody.presence"] = x; });
        Invalid("key without .presence", (s, x) => { s.Presences.Remove("irabeth.presence"); s.Presences["irabeth"] = x; });
        Invalid("bad unit guid", (_, x) => x.Unit = "nope");
        Invalid("bad area guid", (_, x) => x.Area = "00000000000000000000000000000000");
        Invalid("unknown mode", (_, x) => x.Mode = "teleport");
        Invalid("copy without position", (_, x) => x.Position = null);
        Invalid("ungated copy", (_, x) => x.Requires = Array.Empty<string>());
        Invalid("unknown gate", (_, x) => x.Requires = new[] { "never.written" });
        Invalid("gate both required and forbidden", (_, x) => x.Forbids = new[] { "trickster.ever" });
        Invalid("chapter window", (_, x) => x.MinChapter = 6);
        Invalid("bad host list", (_, x) => x.AnswerLists = new[] { "nope" });
        Invalid("duplicate unit in one area", (s, x) =>
        {
            s.Relationships["anevia"] = new Relationship { Title = "Anevia", StartedFlag = "anevia.started", ClosedFlag = "anevia.closed", CommittedFlag = "anevia.committed" };
            s.Presences["anevia.presence"] = x;
        });
        // reuse-native needs no position or gate.
        var plain = Fixture();
        plain.Presences["irabeth.presence"] = new Presence { Unit = IrabethUnit, Area = Capital };
        Rules.Validate(plain);
    }
}
