using System;
using System.Linq;
using System.Reflection;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.AreaLogic.Cutscenes;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
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
        public const string Setup = "559deab3edca4764a8475948397113a7";
        public const string KianaRevive = "0d8253caf33f7474799c2130fbe15907";
        public const string DogRevive = "4008e4f363bf551498c3a99a12a60cc3";
        public static readonly string[] NativeIds = { FinalResolve, Verdict, Completion, Setup, KianaRevive, DogRevive };

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
            if (action is PlayCutscene play) return NativeEpilogueEdit.ActionShape(play) + ":" + play.PutInQueue + ":" + play.CheckExistence + ":" + play.Parameters.Parameters.Length
                + string.Concat(play.Parameters.Parameters.Select(p => ":" + Field(p, "Name") + ":" + Field(p, "Type") + ":" + UnitShape(Field(p, "Evaluator"))));
            if (action is StopCutscene stop) return NativeEpilogueEdit.ActionShape(stop) + ":" + UnitShape(Field(stop, "WithUnit"));
            if (action is StartEtude || action is CompleteEtude) return NativeEpilogueEdit.ActionShape(action) + ":" + Field(action, "Evaluate") + ":" + (Field(action, "EtudeEvaluator") == null);
            return "unreviewed";
        }));

        private static string UnitShape(object? unit) => unit is UnitFromSpawner from
            ? from.Spawner.UniqueId + "@" + from.Spawner.SceneAssetGuid : "unreviewed";
        private const string BadWedding = "And[E:d983621f7b887b043acb0c43186bf824:False:False:False:True:False:False]";
        private const string Victim = "5c8fbdc4-67d2-439f-9507-5214166213bf@96778946654e0694da9678eff26d097f";
        private const string Girl = "d08b7760-eafc-43d6-901d-2b1298ebb0fe@96778946654e0694da9678eff26d097f";
        private const string Wife = "935cd45a-387a-46ab-bc8a-42a209657f3f@96778946654e0694da9678eff26d097f";
        private const string Dog = "3a8f7f55-8a41-4987-8825-addaed6e0ab7@96778946654e0694da9678eff26d097f";
        private static string RevivalShape(string unit) => "StopCutscene:03346ed57a7462443a6be887591150ca:" + unit
            + ";PlayCutscene:3644cee8047af074b9f67299adf8e0fb:False:True:1:Unit:Unit:" + unit;


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
            internal CommandAction CompleteCommand = null!, SetupCommand = null!, KianaCommand = null!, DogCommand = null!;
            internal ActionList SetupActions = null!, KianaActions = null!, DogActions = null!, CompletionActions = null!;
            internal GameAction[] SetupOriginal = null!, KianaOriginal = null!, DogOriginal = null!;
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
            plan.CompleteCommand = completion;
            plan.SetupCommand = (CommandAction)resolve(Setup)!;
            plan.KianaCommand = (CommandAction)resolve(KianaRevive)!;
            plan.DogCommand = (CommandAction)resolve(DogRevive)!;
            plan.SetupActions = plan.SetupCommand.Action; plan.SetupOriginal = plan.SetupActions.Actions;
            plan.KianaActions = plan.KianaCommand.Action; plan.KianaOriginal = plan.KianaActions.Actions;
            plan.DogActions = plan.DogCommand.Action; plan.DogOriginal = plan.DogActions.Actions;
            plan.CompletionActions = completion.Action;
            return null;
        }
        public static void Attach(Plan plan, Func<bool> holds, Func<Snapshot>? read = null)
        {
            if (!ReferenceEquals(plan.Etude.ComponentsArray.OfType<EtudePlayTrigger>().Single().Actions, plan.Trigger)
                || !ReferenceEquals(plan.Cue.OnStop, plan.Verdict)
                || !ReferenceEquals(plan.Trigger.Actions, plan.TriggerOriginal) || !ReferenceEquals(plan.Verdict.Actions, plan.VerdictOriginal)
                || !ReferenceEquals(plan.SetupCommand.Action, plan.SetupActions) || !ReferenceEquals(plan.SetupActions.Actions, plan.SetupOriginal)
                || !ReferenceEquals(plan.KianaCommand.Action, plan.KianaActions) || !ReferenceEquals(plan.KianaActions.Actions, plan.KianaOriginal)
                || !ReferenceEquals(plan.DogCommand.Action, plan.DogActions) || !ReferenceEquals(plan.DogActions.Actions, plan.DogOriginal)
                || !ReferenceEquals(plan.CompleteCommand.Action, plan.CompletionActions) || !ReferenceEquals(plan.CompletionActions.Actions, plan.Completion))
                throw new InvalidOperationException("Q3 recovery action lists changed after review; neither branch attached");
            AttachReviewed(plan.Etude, plan.Cue, plan.CompleteCommand, plan.SetupCommand, plan.KianaCommand, plan.DogCommand, holds, read);
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
            if (!(resolve(Setup) is CommandAction setup) || !(resolve(KianaRevive) is CommandAction kiana)
                || !(resolve(DogRevive) is CommandAction dog)) return "Q3 individual recovery evidence missing";
            if (setup.Action.Actions.Length != 5 || !(setup.Action.Actions[0] is Conditional)
                || Shape(new ActionList { Actions = setup.Action.Actions.Take(1).ToArray() }) != "C:" + BadWedding + "{S:" + Victim + "{}}{S:" + Wife + "," + Girl + "{}}"
                || Shape(kiana.Action) != "C:" + BadWedding + "{" + RevivalShape(Victim) + "}{" + RevivalShape(Girl) + "}"
                || Shape(dog.Action) != RevivalShape(Dog)
                || new[] { setup, kiana, dog }.Any(c => c.EntryCondition.Operation != Operation.And || c.EntryCondition.Conditions.Length != 0))
                return "Q3 individual recovery actions differ from the reviewed policy: setup="
                    + Shape(new ActionList { Actions = setup.Action.Actions.Take(1).ToArray() })
                    + "; Kiana=" + Shape(kiana.Action) + "; dog=" + Shape(dog.Action);
            owner = etude;
            return null;
        }

        public static void Attach(BlueprintScriptableObject owner, Func<bool> holds, Func<Snapshot>? read = null)
            => AttachReviewed(owner,
                (BlueprintCue)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(Verdict)),
                (CommandAction)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(Completion)),
                (CommandAction)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(Setup)),
                (CommandAction)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(KianaRevive)),
                (CommandAction)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(DogRevive)), holds, read);

        private static void AttachReviewed(BlueprintScriptableObject owner, BlueprintCue cue, CommandAction completion,
            CommandAction setup, CommandAction kiana, CommandAction dog, Func<bool> holds, Func<Snapshot>? read)
        {
            // The legacy bool-only API denotes a full recovery gate. Main supplies
            // the live snapshot for individual history; the adapter never samples Main itself.
            bool Whole() { if (read == null) return true; var state = read(); return state.Has("trickster.now") && (state.Has("kiana.trickster.guests_ransomed") || state.Has("kiana.trickster.guests_bought_back")); }
            bool KianaOnly() { if (read == null) return false; var state = read(); return state.Has("trickster.now") && !Whole() && state.Has("kiana.trickster.returned") && state.Has("kiana.trickster.cost.guests_robbed") && !state.Has("kiana.trickster.dog_saved"); }
            bool DogOnly() { if (read == null) return false; var state = read(); return state.Has("trickster.now") && !Whole() && state.Has("kiana.trickster.returned") && state.Has("kiana.trickster.cost.guests_robbed") && state.Has("kiana.trickster.dog_saved"); }
            var trigger = owner.ComponentsArray.OfType<EtudePlayTrigger>().Single();
            // Reuse the native awake wife's spawner; never touch the captive Girl_Victim on dog-only runs.
            var setupBranch = setup.Action.Actions[0] is Branch prior ? (Conditional)prior.Original[0] : (Conditional)setup.Action.Actions[0];
            var awake = trigger.Actions.Actions[0] is Branch attached ? (Spawn)attached.Partial!.Last()
                : new Spawn { Spawners = ((Spawn)setupBranch.IfFalse.Actions[0]).Spawners.Take(1).ToArray(),
                    ActionsOnSpawn = new ActionList { Actions = Array.Empty<GameAction>() }, Owner = owner, name = "$Q3AwakeKiana$" };
            if (!owner.ElementsArray.Contains(awake)) owner.ElementsArray.Add(awake);
            Wrap(owner, trigger.Actions, original => original.Take(2).ToArray(), () => holds() && Whole(),
                original => original.Take(2).Concat(new[] { awake }).ToArray(), () => holds() && KianaOnly());
            // Original outcomes run first, then the cutscene's native CompleteEtude. StartsOnComplete is untouched.
            Wrap(cue, cue.OnStop, original => original.Skip(1).Concat(completion.Action.Actions).ToArray(), () => holds() && Whole());
            var first = new ActionList { Actions = setup.Action.Actions.Take(1).ToArray() };
            Wrap(owner, first, _ => new GameAction[] { awake }, () => holds() && KianaOnly());
            setup.Action.Actions[0] = first.Actions[0];
            // Kiana-only recovery comes from the bad wedding; dog-only keeps the native Girl_Victim branch.
            Wrap(owner, kiana.Action, _ => Array.Empty<GameAction>(), () => holds() && KianaOnly());
            Wrap(owner, dog.Action, _ => Array.Empty<GameAction>(), () => holds() && DogOnly());
        }

        private static void Wrap(BlueprintScriptableObject owner, ActionList list, Func<GameAction[], GameAction[]> earned, Func<bool> holds, Func<GameAction[], GameAction[]>? partial = null, Func<bool>? partialHolds = null)
        {
            // eng7-f1: only reuse a bound branch owned by this exact native attachment site.
            if (list.Actions.Length == 1 && list.Actions[0] is Branch existing)
            {
                if (!ReferenceEquals(existing.Owner, owner)) throw new InvalidOperationException("Q3 branch has the wrong owner");
                existing.Holds = holds; existing.PartialHolds = partialHolds;
                return;
            }
            // end eng7-f1
            var branch = new Branch { Original = list.Actions, Earned = earned(list.Actions), Holds = holds, Partial = partial?.Invoke(list.Actions), PartialHolds = partialHolds, Owner = owner, name = "$Q3Recovery$" + System.Guid.NewGuid() };
            owner.ElementsArray.Add(branch);
            list.Actions = new GameAction[] { branch };
        }

        public sealed class Branch : GameAction
        {
            public GameAction[] Original = Array.Empty<GameAction>(), Earned = Array.Empty<GameAction>();
            public Func<bool> Holds = null!;
            public GameAction[]? Partial;
            public Func<bool>? PartialHolds;
            public Exception? LastObservationError { get; private set; }
            public GameAction[] Selected()
            {
                LastObservationError = null;
                try { return Holds() ? Earned : PartialHolds?.Invoke() == true ? Partial! : Original; }
                catch (Exception ex) { LastObservationError = ex; return Original; }
            }
            public override string GetCaption() => "Reviewed Q3 recovery after an earned return";
            public override void RunAction() => new ActionList { Actions = Selected() }.Run();
        }
    }
}
