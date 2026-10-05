using System;
using System.Linq;
using Kingmaker;
using Kingmaker.AreaLogic.Etudes;

namespace RRT.TestHarness
{
    internal sealed partial class HarnessRunner
    {
        // This file belongs only to RRT.TestHarness. Shipped runtime never seeds route state.
        void ApplyFixtureSetup()
        {
            if (rrt == null || !rrt.Initialized) throw new InvalidOperationException("RRT not initialized");
            // Resolve every etude before modifying anything; reject typos/wrong blueprint types.
            var etudes = plan.StartEtudes.Select(guid => Bp<BlueprintEtude>(guid)
                ?? throw new InvalidOperationException("BlueprintEtude missing: " + guid)).ToArray();
            var system = Game.Instance.Player.EtudesSystem;
            if (etudes.Any(system.EtudeIsCompleted))
                throw new InvalidOperationException("A requested etude is completed; fixture setup cannot reset it");
            foreach (var etude in etudes)
                if (!system.EtudeIsStarted(etude)) system.StartEtude(etude);
            foreach (string flag in plan.SetFlags) rrt.Set(flag);
            capture.Add("harness", "Info", "Fixture setup: flags=" + string.Join(",", plan.SetFlags)
                + "; etudes=" + string.Join(",", plan.StartEtudes), "");
        }
    }
}
