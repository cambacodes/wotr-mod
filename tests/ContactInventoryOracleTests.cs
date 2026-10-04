using System;
using System.Collections.Generic;
using RRT.TestHarness;
using Tirabade;

internal static class ContactInventoryOracleTests
{
    static NativeContactObservation Live() => new NativeContactObservation { ContextReady = true,
        CurrentStorage = true, SceneLoaded = true, ViewPresent = true, ViewMatches = true,
        ViewSceneLoaded = true, ViewActive = true, InGame = true, Conscious = true };

    internal static void Run(Story story, Action<bool, string> check)
    {
        foreach (var mutate in new Action<NativeContactObservation>[] { a => a.Suppressed = true,
            a => a.InGame = false, a => a.Dead = true, a => a.FinallyDead = true,
            a => a.ViewPresent = false, a => a.ViewMatches = false, a => a.ViewSceneLoaded = false,
            a => a.ViewActive = false, a => a.SceneLoaded = false, a => a.CurrentStorage = false,
            a => a.Conscious = false, a => a.Enemy = true, a => a.ContextReady = false })
        {
            var actor = Live(); mutate(actor);
            Check(new[] { actor }, false, "skipped-inline");
        }
        var crossScene = Live(); crossScene.Storage = "cross-scene";
        Check(new[] { crossScene }, true, "usable");
        var corpse = Live(); corpse.Dead = true;
        Check(new[] { corpse, Live() }, true, "usable");
        Check(new[] { Live(), Live() }, false, "skipped-inline");
        var suppressed = Live(); suppressed.Suppressed = true;
        Check(new[] { Live(), suppressed }, false, "skipped-inline");
        Check(new[] { Live() }, true, "skipped-native", false);
        var rejected = new ContactInventoryProbe { Actors = new List<ContactInventoryActor> {
            new ContactInventoryActor { Usable = true } }, NativeAccepted = true, SnapshotAccepted = false };
        check(rejected.Verdict == "contact-oracle-failure", "Q7-35: expected usable rejected contact passed as skip.");
        rejected.NativeAccepted = false;
        check(rejected.Verdict == "contact-oracle-failure", "Q7-35: native predicate disagreement passed.");

        // The harness already inspects NativeQ3Recovery.Branch at both native sites;
        // these are its corrected serialized-world inputs, not a count of generic guards.
        check(story.NativeGates["kiana.q3_recovery"].Target == "2b4a5c01a192d1f4aa8c9d32aa149727",
            "Q7-35: Kiana oracle drifted from the native Q3 recovery target.");
        foreach (var partial in new[] { "kiana.trickster.primed", "kiana.trickster.returned", "kiana.trickster.cost.guests_robbed" })
        {
            var state = new Snapshot { Chapter = 5, Hour = 1000 };
            state.Flags.UnionWith(new[] { "trickster", partial }); Rules.Complete(story, state);
            check(!Rules.NativeGateHolds(story, "kiana.q3_recovery", state), "Q7-35: partial Kiana recovery became a full-ransom witness.");
        }
        foreach (var full in new[] { "kiana.trickster.guests_ransomed", "kiana.trickster.guests_bought_back" })
        {
            var state = new Snapshot { Chapter = 5, Hour = 1000 };
            state.Flags.UnionWith(new[] { "trickster", full }); Rules.Complete(story, state);
            check(Rules.NativeGateHolds(story, "kiana.q3_recovery", state), "Q7-35: paid Kiana native branch witness was rejected.");
            var offPath = new Snapshot { Chapter = 5, Hour = 1000 };
            offPath.Flags.UnionWith(new[] { "trickster.ever", full }); Rules.Complete(story, offPath);
            check(!Rules.NativeGateHolds(story, "kiana.q3_recovery", offPath), "Q7-35: Kiana native branch oracle leaked off Trickster.");
        }

        void Check(NativeContactObservation[] actors, bool expected, string verdict, bool witnesses = true)
        {
            bool native = Rules.SingleUsable(actors, a => a.Usable, a => a.Ignorable) != null;
            var probe = new ContactInventoryProbe { NativeAccepted = native, SnapshotAccepted = native, NativeWitnessesPresent = witnesses };
            foreach (var actor in actors) probe.Actors.Add(new ContactInventoryActor { Usable = actor.Usable, Ignorable = actor.Ignorable });
            check(native == expected && probe.ExpectedUsable == expected && probe.Verdict == verdict, "Q7-35: contact inventory verdict " + verdict);
        }
    }
}
