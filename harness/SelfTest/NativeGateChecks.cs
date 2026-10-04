using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using RRT.TestHarness;

internal static class NativeGateChecks
{
    public sealed class Story
    {
        public Dictionary<string, Spec> NativeGates = new Dictionary<string, Spec>();
    }
    public sealed class Spec
    {
        public string Target = "2b4a5c01a192d1f4aa8c9d32aa149727";
        public string Relationship = "kiana";
    }

    public static void Run(string rrtDll, Action<bool, string> check)
    {
        var assembly = Assembly.LoadFrom(rrtDll);
        var etude = new BlueprintEtude();
        var cue = new BlueprintCue();
        var trigger = new EtudePlayTrigger { Actions = new ActionList { Actions = Array.Empty<GameAction>() } };
        etude.ComponentsArray = new BlueprintComponent[] { trigger };
        var story = new Story();
        var spec = new Spec();
        story.NativeGates.Add("kiana.q3_recovery", spec);
        var blueprints = new Dictionary<string, SimpleBlueprint> { [spec.Target] = etude, ["aeccec94d6e3246488d7f13577a8380d"] = cue };
        List<string> Rows(params string[] degraded) => NativeGateRows.Read(story, degraded.ToList(), id => blueprints.TryGetValue(id, out var bp) ? bp : null);
        GameAction Branch(BlueprintScriptableObject owner)
        {
            var branch = (GameAction)Activator.CreateInstance(assembly.GetType("Tirabade.NativeQ3Recovery+Branch", true)!)!;
            branch.Owner = owner;
            branch.GetType().GetField("Holds")!.SetValue(branch, (Func<bool>)(() => false));
            return branch;
        }

        trigger.Actions.Actions = new[] { Branch(etude) };
        cue.OnStop = new ActionList { Actions = new[] { Branch(cue) } };
        check(!Rows().Single().StartsWith("MISSING "), "attached Q3 action branches must pass the live gate row");
        cue.OnStop.Actions = Array.Empty<GameAction>();
        check(Rows().Single().StartsWith("MISSING "), "a missing verdict wrapper must fail");
        cue.OnStop.Actions = new[] { Branch(cue) };
        trigger.Actions.Actions = new[] { Branch(cue) };
        check(Rows().Single().StartsWith("MISSING "), "a branch owned by another blueprint must fail");
        trigger.Actions.Actions = new[] { Branch(etude) };
        trigger.Actions.Actions[0].GetType().GetField("Holds")!.SetValue(trigger.Actions.Actions[0], null);
        check(Rows().Single().StartsWith("MISSING "), "an unbound branch must fail");
        trigger.Actions.Actions = new[] { Branch(etude), new Conditional() };
        check(Rows().Single().StartsWith("MISSING "), "extra unwrapped Q3 actions must fail");
        trigger.Actions.Actions = Array.Empty<GameAction>();
        check(Rows().Single().StartsWith("MISSING "), "a missing trigger wrapper must fail");
        check(!Rows("kiana").Single().StartsWith("MISSING "), "a degraded relationship expects canon");
        blueprints.Clear();
        check(Rows().Single().StartsWith("MISSING "), "missing blueprints must fail, never pass as 0/0 guards");

        var guard = (Condition)Activator.CreateInstance(assembly.GetType("Tirabade.NativeGate+Guard", true)!)!;
        ConditionsChecker Guarded() => new ConditionsChecker { Conditions = new[] { guard } };
        story.NativeGates.Clear();
        story.NativeGates.Add("golems_dragon_eggs.over_body", spec);
        blueprints[spec.Target] = cue;
        cue.Conditions = Guarded();
        check(!Rows().Single().StartsWith("MISSING "), "attached cue condition guard passes");
        cue.Conditions.Conditions = Array.Empty<Condition>();
        check(Rows().Single().StartsWith("MISSING "), "missing cue guard fails");
        var answer = new BlueprintAnswer { ShowConditions = Guarded() };
        story.NativeGates.Clear();
        story.NativeGates.Add("arsinoe.souls_search_answer", spec);
        blueprints[spec.Target] = answer;
        check(!Rows().Single().StartsWith("MISSING "), "attached answer condition guard passes");
        answer.ShowConditions.Conditions = Array.Empty<Condition>();
        check(Rows().Single().StartsWith("MISSING "), "missing answer guard fails");
        var dialog = new BlueprintDialog { Conditions = Guarded() };
        story.NativeGates.Clear();
        story.NativeGates.Add("dragon_eggs.dialog", spec);
        blueprints[spec.Target] = dialog;
        check(!Rows().Single().StartsWith("MISSING "), "attached dialog condition guard passes");
        dialog.Conditions.Conditions = Array.Empty<Condition>();
        check(Rows().Single().StartsWith("MISSING "), "missing dialog guard fails");
        story.NativeGates.Clear();
        story.NativeGates.Add("ivory_sanctum.red_dragon_spawn", spec);
        blueprints[spec.Target] = etude;
        trigger.Actions.Actions = new GameAction[] { new Conditional { ConditionsChecker = Guarded() }, new Conditional { ConditionsChecker = Guarded() } };
        check(!Rows().Single().StartsWith("MISSING "), "both sanctum condition guards pass");
        trigger.Actions.Actions = trigger.Actions.Actions.Take(1).ToArray();
        check(Rows().Single().StartsWith("MISSING "), "one sanctum guard must fail");
        trigger.Actions.Actions = new[] { Branch(etude) };
        check(Rows().Single().StartsWith("MISSING "), "a Q3 branch cannot satisfy another gate mechanism");
    }
}
