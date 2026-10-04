using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;

namespace RRT.TestHarness
{
    public static class NativeGateRows
    {
        // Inspect live attachment sites, including both Q3 action lists. The resolver also lets the offline self-test
        // exercise these rows with real game blueprints without loading a save or launching Unity.
        public static List<string> Read(object? story, List<string> degraded, Func<string, SimpleBlueprint?> resolve)
        {
            var rows = new List<string>();
            if (story == null) return rows;
            if (!(story.GetType().GetField("NativeGates")?.GetValue(story) is IDictionary gates)) return rows;
            static bool IsGuard(object? c) => c?.GetType().FullName == "Tirabade.NativeGate+Guard";
            static IEnumerable<object> Conditions(object? checker) =>
                (checker?.GetType().GetField("Conditions")?.GetValue(checker) as IEnumerable)?.Cast<object>() ?? Enumerable.Empty<object>();
            foreach (DictionaryEntry pair in gates)
            {
                string id = (string)pair.Key;
                string target = (string)(pair.Value.GetType().GetField("Target")?.GetValue(pair.Value) ?? "");
                string relationship = (string)(pair.Value.GetType().GetField("Relationship")?.GetValue(pair.Value) ?? "");
                var bp = resolve(target);
                int guards = 0, expected = 1;
                string mechanism = "guards";
                if (id == "kiana.q3_recovery")
                {
                    expected = 2;
                    mechanism = "action branches";
                    if (target == "2b4a5c01a192d1f4aa8c9d32aa149727" && bp is BlueprintEtude recovery)
                    {
                        var triggers = recovery.ComponentsArray.OfType<EtudePlayTrigger>().ToArray();
                        if (triggers.Length == 1 && HasQ3Branch(triggers[0].Actions, recovery)) guards++;
                        if (resolve("aeccec94d6e3246488d7f13577a8380d") is BlueprintCue verdict && HasQ3Branch(verdict.OnStop, verdict)) guards++;
                    }
                }
                else if (bp is BlueprintEtude etude)
                {
                    expected = 2;
                    foreach (var trigger in etude.ComponentsArray.OfType<EtudePlayTrigger>())
                        foreach (var action in (trigger.Actions?.Actions ?? Array.Empty<GameAction>()).OfType<Conditional>())
                            guards += Conditions(action.ConditionsChecker).Count(IsGuard);
                }
                else if (bp is BlueprintCue cue) { expected = 1; guards = Conditions(cue.Conditions).Count(IsGuard); }
                else if (bp is BlueprintAnswer answer) guards = Conditions(answer.ShowConditions).Count(IsGuard);
                else if (bp is BlueprintDialog dialog) guards = Conditions(dialog.Conditions).Count(IsGuard);
                bool live = !degraded.Contains(relationship);
                rows.Add((live && guards != expected ? "MISSING " : "") + id + " -> " + target + ": " + guards + "/" + expected + " " + mechanism
                    + (live ? "" : " (relationship degraded: canon expected)"));
            }
            return rows;
        }

        static bool HasQ3Branch(ActionList? list, BlueprintScriptableObject owner) => list?.Actions?.Length == 1
            && list.Actions[0].GetType().FullName == "Tirabade.NativeQ3Recovery+Branch"
            && ReferenceEquals(list.Actions[0].Owner, owner)
            && list.Actions[0].GetType().GetField("Holds")?.GetValue(list.Actions[0]) is Func<bool>;
    }
}
