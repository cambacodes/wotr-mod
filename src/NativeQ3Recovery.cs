using System;
using System.Linq;
using System.Reflection;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.AreaLogic.Cutscenes;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;

namespace Tirabade
{
    // Authored Q3 alternative after the paid ransom/buy-back. Native outcomes and completion still run.
    // Reviewed against blueprints.zip: FinalResolve's trigger, Cue_0032's OnStop, and the revival's final command.
    // The intro conversation remains; the victim spawn and revival cutscene are skipped. Refusal only warns.
    public static class NativeQ3Recovery
    {
        public const string Gate = "kiana.q3_recovery";
        public const string FinalResolve = "2b4a5c01a192d1f4aa8c9d32aa149727";
        public const string Verdict = "aeccec94d6e3246488d7f13577a8380d";
        public const string Completion = "dd2a29da89d7abe47a7342470f56b275";
        public static readonly string[] NativeIds = { FinalResolve, Verdict, Completion };

        private static object? Field(object value, string name) => value.GetType().GetField(name,
            BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance)?.GetValue(value);
        private static string GuidOf(object value, string field) => (Field(value, field) as BlueprintReferenceBase)?.Guid.ToString() ?? "missing";
        private static string Checker(ConditionsChecker checker) => checker.Operation + "[" + string.Join(";", checker.Conditions.Select(c =>
            c is EtudeStatus e ? "E:" + GuidOf(e, "m_Etude") + ":" + e.Not + ":" + e.NotStarted + ":" + e.Started + ":" + e.Playing + ":" + e.CompletionInProgress + ":" + e.Completed
            : c is OrAndLogic logic ? "L:" + logic.Not + ":" + Checker(logic.ConditionsChecker) : "unreviewed")) + "]";

        public static string Shape(ActionList list) => string.Join(";", list.Actions.Select(action =>
        {
            if (action is Conditional c) return "C:" + Checker(c.ConditionsChecker) + "{" + Shape(c.IfTrue) + "}{" + Shape(c.IfFalse) + "}";
            if (action is Spawn spawn) return "S:" + string.Join(",", spawn.Spawners.Select(s => s.UniqueId + "@" + s.SceneAssetGuid)) + "{" + Shape(spawn.ActionsOnSpawn) + "}";
            if (action is PlayCutscene play) return NativeEpilogueEdit.ActionShape(play) + ":" + play.PutInQueue + ":" + play.CheckExistence + ":" + play.Parameters.Parameters.Length;
            if (action is StartEtude || action is CompleteEtude) return NativeEpilogueEdit.ActionShape(action) + ":" + Field(action, "Evaluate") + ":" + (Field(action, "EtudeEvaluator") == null);
            return "unreviewed";
        }));

        // eng7-f1: shared signatures are also validated against the archive at export.
        public const string TriggerShape = "PlayCutscene:0bb31c4bcf97b9a4d8b4c16455645f8d:False:True:0;C:And[E:ded376ed8b73c3e42b0de967fb1d10a9:False:False:False:True:False:False]{StartEtude:148423f1d35917946a5ebeeb4f19246c:False:True}{};C:And[E:d983621f7b887b043acb0c43186bf824:False:False:False:True:False:False]{S:5c8fbdc4-67d2-439f-9507-5214166213bf@96778946654e0694da9678eff26d097f{}}{S:d08b7760-eafc-43d6-901d-2b1298ebb0fe@96778946654e0694da9678eff26d097f{}}";
        public const string VerdictShape = "PlayCutscene:fef1b52002b9af642a8e5169802c3b68:False:True:0;C:And[E:ded376ed8b73c3e42b0de967fb1d10a9:True:False:False:True:False:False;L:False:Or[E:d99770b13ebc47447881d33763209b03:False:False:False:True:False:False;E:46f4524cec981c544964229e3e08c847:False:False:False:True:False:False]]{StartEtude:c959cc3ef25ce834090ba65cd0169588:False:True}{};C:And[E:148423f1d35917946a5ebeeb4f19246c:False:False:False:True:False:False]{C:And[]{C:Or[E:f8129442feebb7c49b209c83b8ee6267:False:False:False:True:False:False;E:699b1ad898227c943b2ee9e0cfd355aa:False:False:False:True:False:False]{StartEtude:e438007efc4f1474eb447031d4b5a60e:False:True}{}}{}}{};C:And[E:c959cc3ef25ce834090ba65cd0169588:False:True:False:False:False:False;E:e438007efc4f1474eb447031d4b5a60e:False:True:False:False:False:False]{StartEtude:2bb1f6f30ca9bb1408f720d6f10c5c05:False:True}{}";
        public const string CompletionShape = "CompleteEtude:2b4a5c01a192d1f4aa8c9d32aa149727:False:True";

        // eng7-f1: capture the two action lists and completion from the evidence resolver. Never resolve
        // a different object at attach time; fail atomically if either verified list drifts meanwhile.
        public sealed class Plan
        {
            internal BlueprintEtude Etude = null!;
            internal BlueprintCue Cue = null!;
            internal ActionList Trigger = null!, Verdict = null!;
            internal GameAction[] TriggerOriginal = null!, VerdictOriginal = null!, Completion = null!;
        }
        public static string? Prepare(Func<string, SimpleBlueprint?> resolve, out Plan? plan)
        {
            plan = null;
            var refusal = Check(resolve, out var owner);
            if (refusal != null) return refusal;
            var etude = (BlueprintEtude)owner!;
            var cue = (BlueprintCue)resolve(Verdict)!;
            var completion = (CommandAction)resolve(Completion)!;
            var trigger = etude.ComponentsArray.OfType<EtudePlayTrigger>().Single();
            plan = new Plan { Etude = etude, Cue = cue, Trigger = trigger.Actions, Verdict = cue.OnStop,
                TriggerOriginal = trigger.Actions.Actions, VerdictOriginal = cue.OnStop.Actions, Completion = completion.Action.Actions };
            return null;
        }
        public static void Attach(Plan plan, Func<bool> holds)
        {
            if (!ReferenceEquals(plan.Etude.ComponentsArray.OfType<EtudePlayTrigger>().Single().Actions, plan.Trigger)
                || !ReferenceEquals(plan.Cue.OnStop, plan.Verdict)
                || !ReferenceEquals(plan.Trigger.Actions, plan.TriggerOriginal) || !ReferenceEquals(plan.Verdict.Actions, plan.VerdictOriginal))
                throw new InvalidOperationException("Q3 recovery action lists changed after review; neither branch attached");
            Wrap(plan.Etude, plan.Trigger, original => original.Take(2).ToArray(), holds);
            Wrap(plan.Cue, plan.Verdict, original => original.Skip(1).Concat(plan.Completion).ToArray(), holds);
        }
        // end eng7-f1

        public static string? Check(Func<string, SimpleBlueprint?> resolve, out BlueprintScriptableObject? owner)
        {
            owner = null;
            if (!(resolve(FinalResolve) is BlueprintEtude etude) || !(resolve(Verdict) is BlueprintCue cue)
                || !(resolve(Completion) is CommandAction complete)) return "Q3 recovery evidence missing";
            var triggers = etude.ComponentsArray.OfType<EtudePlayTrigger>().ToArray();
            // eng7-f1: report the failing attachment site and actual shape, rather than a single opaque refusal.
            if (triggers.Length != 1) return "Q3 recovery FinalResolve trigger count differs: " + triggers.Length;
            if (Shape(triggers[0].Actions) != TriggerShape) return "Q3 recovery FinalResolve actions differ: " + Shape(triggers[0].Actions);
            if (Shape(cue.OnStop) != VerdictShape) return "Q3 recovery Cue_0032 OnStop differs: " + Shape(cue.OnStop);
            if (Shape(complete.Action) != CompletionShape) return "Q3 recovery completion differs: " + Shape(complete.Action);
            // end eng7-f1
            if (triggers[0].Conditions.Operation != Operation.And || triggers[0].Conditions.Conditions.Length != 0
                || Shape(triggers[0].Actions) != TriggerShape || Shape(cue.OnStop) != VerdictShape
                || Shape(complete.Action) != CompletionShape || complete.EntryCondition.Operation != Operation.And || complete.EntryCondition.Conditions.Length != 0
                || !etude.StartsOnComplete.Select(r => r.Guid).SequenceEqual(new[] { BlueprintGuid.Parse("6d3fb96f9b60c0449a01add4be5c4a49") }))
                return "Q3 recovery actions differ from the reviewed policy";
            owner = etude;
            return null;
        }

        public static void Attach(BlueprintScriptableObject owner, Func<bool> holds)
        {
            var trigger = owner.ComponentsArray.OfType<EtudePlayTrigger>().Single();
            var cue = (BlueprintCue)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(Verdict));
            var completion = (CommandAction)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(Completion));
            Wrap(owner, trigger.Actions, original => original.Take(2).ToArray(), holds);
            // Original outcomes run first, then the cutscene's native CompleteEtude. StartsOnComplete is untouched.
            Wrap(cue, cue.OnStop, original => original.Skip(1).Concat(completion.Action.Actions).ToArray(), holds);
        }

        // eng7-l04: the reviewed partial group describes Kiana alone; it must never skip the whole native recovery.
        public static void Attach(BlueprintScriptableObject owner, Func<Q3RecoveryOutcome> outcome)
            => Attach(owner, () => Rules.Q3RecoverySkipsPatients(outcome()));

        private static void Wrap(BlueprintScriptableObject owner, ActionList list, Func<GameAction[], GameAction[]> earned, Func<bool> holds)
        {
            // eng7-f1: only reuse a bound branch owned by this exact native attachment site.
            if (list.Actions.Length == 1 && list.Actions[0] is Branch existing)
            {
                if (!ReferenceEquals(existing.Owner, owner)) throw new InvalidOperationException("Q3 branch has the wrong owner");
                existing.Holds = holds;
                return;
            }
            // end eng7-f1
            var branch = new Branch { Original = list.Actions, Earned = earned(list.Actions), Holds = holds, Owner = owner, name = "$Q3Recovery$" + System.Guid.NewGuid() };
            owner.ElementsArray.Add(branch);
            list.Actions = new GameAction[] { branch };
        }

        public sealed class Branch : GameAction
        {
            public GameAction[] Original = Array.Empty<GameAction>(), Earned = Array.Empty<GameAction>();
            public Func<bool> Holds = null!;
            public Exception? LastObservationError { get; private set; }
            public GameAction[] Selected()
            {
                LastObservationError = null;
                try { return Holds() ? Earned : Original; }
                catch (Exception ex) { LastObservationError = ex; return Original; }
            }
            public override string GetCaption() => "Reviewed Q3 recovery after an earned return";
            public override void RunAction() => new ActionList { Actions = Selected() }.Run();
        }
    }
}
