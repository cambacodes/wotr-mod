using System;
using System.Collections.Generic;
using System.Linq;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;

namespace Tirabade
{
    // E18: a reviewed native gate. One audited native condition checker is wrapped so that, while an earned story state
    // holds, it reads false and the native content takes its own false branch: the branch the game already plays in an
    // existing native world. No native etude is started or completed, no unit is spawned or removed by the mod, nothing is
    // written to the save: the blueprint edit lives in memory only. When the mod is disabled, uninitialized or removed, the
    // wrapped checker is the native one again and canon plays.
    //
    // v1 whitelist (Devarra's flight, Writer/handoffs/trickster/devarra-device-options.md, option A), verified in
    // blueprints.zip and in the IvorySanctum mechanics scene:
    // - IvorySanctum_MainEtude (Chapter03_AreasDefault) spawns RedDragon_CR20 from two once-only EtudePlayTriggers, each a
    //   Conditional on RedDragonDead whose true branch is Spawn [RedDragon_CR20] and whose false branch is SpawnByUnitGroup
    //   [RedDragonReplacementFight_CR15-17] (the lair-kill world). The spawner has SpawnOnSceneInit off, so these two
    //   actions are its only source. Gated, both take the false branch: the replacement fight, as after a lair kill.
    // - Golems_DragonEggs/Cue_0001 ("Get up, lizard!", shown when RedDragonDead is not started) speaks to a carcass. Gated,
    //   the dialog's FirstCue falls through to Cue_0047 ("Hey, dragon, where've you gone?"), the native absent-dragon line.
    public static class NativeGate
    {
        public const string SanctumSpawn = "ivory_sanctum.red_dragon_spawn";
        public const string GolemsOverBody = "golems_dragon_eggs.over_body";
        public const string SanctumEtude = "977818b761d048d49a0fe19a1c8fccc4";
        public const string GolemsCue = "b8dfb42d03fc931409f2b80614cfa9de";
        public const string RedDragonDead = "581521b398fb9dd4eb52bbfffb3b5c43";
        public const string SanctumScene = "1b3609da30e000d4da2f192527f56b0d";
        public const string DragonSpawner = "85c2f3d1-ab00-4d97-8c79-7f50afc946c8";
        public const string ReplacementGroup = "752bcb99-2c77-4f6f-8542-7806575f0e9c";
        public static Dictionary<string, string> Reviewed => Rules.ReviewedNativeGates;

        // Phase 1: the native evidence must match exactly, or the gate is refused (the caller degrades its relationship).
        public static string? Check(string gate, NativeGateSpec spec, Func<string, SimpleBlueprint?> resolve,
            out BlueprintScriptableObject? owner, out ConditionsChecker[] checkers)
        {
            owner = null;
            checkers = Array.Empty<ConditionsChecker>();
            if (!Reviewed.TryGetValue(gate, out var target) || spec.Target != target) return "not a reviewed native gate";
            var blueprint = resolve(target);
            if (gate == SanctumSpawn)
            {
                if (!(blueprint is BlueprintEtude etude)) return "IvorySanctum_MainEtude missing";
                var found = etude.ComponentsArray.OfType<EtudePlayTrigger>()
                    .SelectMany(trigger => trigger.Actions?.Actions ?? Array.Empty<GameAction>())
                    .OfType<Conditional>().Where(IsSpawnBranch).ToArray();
                bool spawnsElsewhere = etude.ComponentsArray.OfType<EtudePlayTrigger>()
                    .SelectMany(trigger => trigger.Actions?.Actions ?? Array.Empty<GameAction>())
                    .Any(action => action is Spawn spawn && spawn.Spawners.Any(IsDragon));
                if (found.Length != 2 || spawnsElsewhere) return "RedDragon_CR20 spawn branches differ from the reviewed pair";
                owner = etude;
                checkers = found.Select(conditional => conditional.ConditionsChecker).ToArray();
                return null;
            }
            if (!(blueprint is BlueprintCue cue)) return "Golems_DragonEggs/Cue_0001 missing";
            var conditions = cue.Conditions?.Conditions;
            if (cue.Conditions == null || cue.Conditions.Operation != Operation.And || conditions == null || conditions.Length != 1
                || !(conditions[0] is EtudeStatus status) || !status.Not || !status.Started || status.Playing || status.Completed
                || status.NotStarted || status.CompletionInProgress || !IsEtude(status, RedDragonDead))
                return "Golems_DragonEggs/Cue_0001 conditions differ from the reviewed policy";
            owner = cue;
            checkers = new[] { cue.Conditions };
            return null;
        }

        private static bool IsEtude(EtudeStatus status, string guid)
        {
            var reference = (BlueprintEtudeReference?)typeof(EtudeStatus).GetField("m_Etude",
                System.Reflection.BindingFlags.Instance | System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Public)!.GetValue(status);
            return reference != null && reference.Guid == BlueprintGuid.Parse(guid);
        }

        private static bool IsDragon(EntityReference reference) => reference != null
            && reference.UniqueId == DragonSpawner && reference.SceneAssetGuid == SanctumScene;

        // Conditional(EtudeStatus on RedDragonDead) ? Spawn [RedDragon_CR20] : SpawnByUnitGroup [RedDragonReplacementFight].
        internal static bool IsSpawnBranch(Conditional conditional)
        {
            var checker = conditional.ConditionsChecker;
            var yes = conditional.IfTrue?.Actions;
            var no = conditional.IfFalse?.Actions;
            return checker != null && checker.Operation == Operation.And && checker.Conditions?.Length == 1
                && checker.Conditions[0] is EtudeStatus status && IsEtude(status, RedDragonDead)
                && yes?.Length == 1 && yes[0] is Spawn spawn && spawn.Spawners?.Length == 1 && IsDragon(spawn.Spawners[0])
                && no?.Length == 1 && no[0] is SpawnByUnitGroup group && group.Group != null
                && group.Group.UniqueId == ReplacementGroup && group.Group.SceneAssetGuid == SanctumScene;
        }

        // Phase 3: wrap each reviewed checker once. A second Build reuses the guard instead of nesting another.
        public static void Attach(BlueprintScriptableObject owner, ConditionsChecker checker, Func<bool> holds)
        {
            if (owner == null) throw new ArgumentNullException(nameof(owner));
            if (checker == null) throw new ArgumentNullException(nameof(checker));
            if (holds == null) throw new ArgumentNullException(nameof(holds));
            if (checker.Conditions?.Length == 1 && checker.Conditions[0] is Guard existing && ReferenceEquals(existing.Owner, owner))
            {
                existing.Holds = holds;
                return;
            }
            var guard = new Guard
            {
                Original = new ConditionsChecker { Operation = checker.Operation, Conditions = checker.Conditions ?? Array.Empty<Condition>() },
                Holds = holds,
                Owner = owner,
                name = "$NativeGate$" + Guid.NewGuid()
            };
            owner.ElementsArray.Add(guard);
            checker.Operation = Operation.And;
            checker.Conditions = new Condition[] { guard };
        }

        public sealed class Guard : Condition
        {
            internal ConditionsChecker? Original;
            internal Func<bool> Holds = null!;
            internal Exception? LastObservationError { get; private set; }
            protected override string GetConditionCaption() => "Native content unless an earned story state holds";
            protected override bool CheckCondition()
            {
                bool gated = false;
                LastObservationError = null;
                try { gated = Holds(); }
                catch (Exception ex) { LastObservationError = ex; }
                return !gated && (Original?.Check() ?? true);
            }
        }
    }
}
