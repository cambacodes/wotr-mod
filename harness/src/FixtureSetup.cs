using System;
using System.Linq;
using System.Collections.Generic;
using HarmonyLib;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker;
using Kingmaker.AreaLogic.Etudes;

namespace RRT.TestHarness
{
    internal static class FixtureObservations
    {
        internal static readonly HashSet<string> Failures = new HashSet<string>(StringComparer.Ordinal);
        internal static readonly HashSet<string> Held = new HashSet<string>(StringComparer.Ordinal);
        static readonly Dictionary<string, string> etudeKeys = new Dictionary<string, string>(StringComparer.Ordinal);
        static bool installed;
        internal static void Clear() { Failures.Clear(); Held.Clear(); }
        internal static bool ReadsEtude(string guid) => etudeKeys.Values.Contains(guid, StringComparer.Ordinal);
        internal static void Install(Harmony harmony, RrtBridge bridge)
        {
            etudeKeys.Clear();
            var story = bridge.Assembly.GetType("Tirabade.Main", true)!.GetField("story", System.Reflection.BindingFlags.Static | System.Reflection.BindingFlags.NonPublic)!.GetValue(null)!;
            var etudes = (System.Collections.IDictionary)RrtBridge.Get(story, "Etudes")!;
            foreach (System.Collections.DictionaryEntry pair in etudes) etudeKeys[(string)pair.Key] = (string)pair.Value;
            if (installed) return;
            var rules = bridge.Assembly.GetType("Tirabade.Rules", true)!;
            harmony.Patch(AccessTools.Method(rules, "Complete"), prefix: new HarmonyMethod(typeof(FixtureObservations), nameof(BeforeComplete)));
            installed = true;
        }
        static void BeforeComplete(object state)
        {
            var flags = (HashSet<string>)RrtBridge.Get(state, "Flags")!;
            flags.UnionWith(Failures);
            foreach (var pair in etudeKeys)
                if (Held.Contains(pair.Value)) flags.Add(pair.Key);
        }
    }

    internal sealed partial class HarnessRunner
    {
        // This file belongs only to RRT.TestHarness. Shipped runtime never seeds route state.
        void ApplyFixtureSetup()
        {
            if (rrt == null || !rrt.Initialized) throw new InvalidOperationException("RRT not initialized");
            // Resolve every etude before modifying anything; reject typos/wrong blueprint types.
            var etudes = plan.StartEtudes.Select(guid => Bp<BlueprintEtude>(guid)
                ?? throw new InvalidOperationException("BlueprintEtude missing: " + guid)).ToArray();
            var held = plan.HoldEtudes.Select(guid => Bp<BlueprintEtude>(guid)
                ?? throw new InvalidOperationException("BlueprintEtude missing: " + guid)).ToArray();
            var cues = plan.SeenCues.Select(guid => Bp<BlueprintCueBase>(guid)
                ?? throw new InvalidOperationException("BlueprintCueBase missing: " + guid)).ToArray();
            var companions = plan.RemoveCompanions.Select(guid => Bp<BlueprintUnit>(guid)
                ?? throw new InvalidOperationException("BlueprintUnit missing: " + guid)).ToArray();
            foreach (string key in plan.SetPresenceFailures)
                if (rrt.ProductionPresence(key) == null) throw new InvalidOperationException("Presence key missing: " + key);
            foreach (string flag in plan.SetFlags)
                if (!rrt.Flags.Contains(flag)) throw new InvalidOperationException("Persistent flag missing: " + flag);
            var player = Game.Instance.Player;
            var removed = companions.Select(bp => player.AllCharacters.Where(u => u.Blueprint == bp || u.OriginalBlueprint == bp).ToArray()).ToArray();
            if (removed.Any(matches => matches.Length != 1)) throw new InvalidOperationException("Companion missing or ambiguous");
            var system = player.EtudesSystem;
            if (etudes.Any(system.EtudeIsCompleted))
                throw new InvalidOperationException("A requested etude is completed; fixture setup cannot reset it");
            FixtureObservations.Install(harmony, rrt);
            if (held.Any(etude => !FixtureObservations.ReadsEtude(etude.AssetGuid.ToString())))
                throw new InvalidOperationException("Held etude has no registered RRT native binding");
            foreach (var etude in etudes)
                if (!system.EtudeIsStarted(etude)) system.StartEtude(etude);
            // These observation patches exist only in RRT.TestHarness, only for explicit fixtures.
            // They are cleared before any reload, so synthetic input cannot pass a production reload proof.
            foreach (var etude in held)
                FixtureObservations.Held.Add(etude.AssetGuid.ToString());
            foreach (string key in plan.SetPresenceFailures) FixtureObservations.Failures.Add(key + ".failed");
            foreach (var cue in cues) player.Dialog.ShownCues.Add(cue);
            foreach (var matches in removed) player.RemoveCompanion(matches[0], stayInGame: false);
            foreach (string flag in plan.SetFlags) rrt.Set(flag);
            // Held is an observation fixture: no native play actions or romance etudes are executed.
            // Supply the native read before Rules.Complete, without depending on an inlineable EtudeHeld patch.
            capture.Add("harness", "Info", "F9 synthetic failures=" + string.Join(",", plan.SetPresenceFailures)
                + "; held=" + string.Join(",", plan.HoldEtudes) + "; seen=" + string.Join(",", plan.SeenCues)
                + "; removed=" + string.Join(",", plan.RemoveCompanions), "");
            capture.Add("harness", "Info", "Fixture setup: flags=" + string.Join(",", plan.SetFlags)
                + "; etudes=" + string.Join(",", plan.StartEtudes), "");
        }
    }
}
