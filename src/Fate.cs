using System;
using System.Linq;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic.Parts;
using Newtonsoft.Json;

namespace Tirabade
{
    internal static class Fate
    {
        // Reuse the saved companion, including her equipment and progression.
        // Dismissal, hostile replacements, and missing entities require separate reconciliation.
        internal static UnitEntityData? FindRetainedCompanion(BlueprintUnit blueprint)
        {
            var matches = Game.Instance.Player.AllCrossSceneUnits.Where(unit => unit.Blueprint == blueprint).Take(2).ToArray();
            if (matches.Length != 1) return null;
            var unit = matches[0];
            return IsRetained(unit.Descriptor.IsPlayerFaction, ReferenceEquals(unit.HoldingState, Game.Instance.Player.CrossSceneState),
                unit.Get<UnitPartCompanion>()?.State) ? unit : null;
        }

        // The retained-companion rule, apart from the live Game so a managed fixture can check it: a player-faction unit
        // held in the cross-scene state whose companion roster is InParty or Remote. A companion who dies in the party
        // stays InParty (SeelahNotInParty_Dead is CompanionInParty with MatchWhenDead), so her dead body is retained.
        internal static bool IsRetained(bool playerFaction, bool crossScene, CompanionState? state)
            => playerFaction && crossScene && (state == CompanionState.InParty || state == CompanionState.Remote);

        internal static RecoveryStatus Status(UnitEntityData unit, CompanionState state) => new RecoveryStatus
        {
            UnitId = unit.UniqueId, Roster = (int)state, Eligible = true,
            Dead = unit.State.IsDead || unit.State.IsFinallyDead, Conscious = unit.State.IsConscious
        };

        internal static bool CanRevive(BlueprintUnit blueprint) => Inspect(blueprint).Dead;

        private static string Key(string id) => "RanRomance.Tirabade.Revival." + id;

        internal static RecoveryAttempt? Pending(string id)
        {
            if (!Game.Instance.Player.SettingsList.TryGetValue(Key(id), out var value)) return null;
            if (!(value is string json)) throw new InvalidOperationException("Invalid restoration checkpoint format: " + id);
            var attempt = JsonConvert.DeserializeObject<RecoveryAttempt>(json);
            if (attempt == null || attempt.Version != 1 || string.IsNullOrEmpty(attempt.UnitId)
                || string.IsNullOrEmpty(attempt.SceneId) || string.IsNullOrEmpty(attempt.ChoiceJson))
                throw new InvalidOperationException("Invalid restoration checkpoint: " + id);
            return attempt;
        }

        internal static void Clear(string id) => Game.Instance.Player.SettingsList.Remove(Key(id));

        internal static RecoveryStatus Inspect(BlueprintUnit blueprint)
        {
            var unit = FindRetainedCompanion(blueprint);
            return unit == null ? new RecoveryStatus() : Status(unit, unit.Get<UnitPartCompanion>()!.State);
        }

        internal static bool TryRevive(string id, BlueprintUnit blueprint, Scene scene, Choice choice, out string message)
        {
            try
            {
                var unit = FindRetainedCompanion(blueprint);
                var caster = Game.Instance.Player.MainCharacter.Value;
                var attempt = Pending(id);
                if (unit == null || caster == null || !caster.State.IsConscious || caster.State.IsDead
                    || attempt == null && !unit.State.IsDead && !unit.State.IsFinallyDead)
                {
                    message = "The original fallen companion and a conscious Commander are required to begin restoration.";
                    return false;
                }
                string choiceJson = JsonConvert.SerializeObject(choice);
                if (attempt != null && (attempt.SceneId != scene.Id || attempt.ChoiceJson != choiceJson))
                    throw new InvalidOperationException("The chosen recovery action differs from the saved attempt.");
                if (attempt == null)
                {
                    attempt = new RecoveryAttempt { UnitId = unit.UniqueId, Roster = (int)unit.Get<UnitPartCompanion>()!.State,
                        SceneId = scene.Id, ChoiceJson = choiceJson };
                    Game.Instance.Player.SettingsList[Key(id)] = JsonConvert.SerializeObject(attempt);
                }
                RecoveryStatus Observe()
                {
                    var status = Inspect(blueprint);
                    status.Eligible &= ReferenceEquals(FindRetainedCompanion(blueprint), unit);
                    return status;
                }
                return attempt.TryApply(Observe, () => unit.Descriptor.ResurrectAndFullRestore(caster), out message);
            }
            catch (Exception ex)
            {
                message = "Restoration could not begin or resume. Any existing checkpoint was preserved. " + ex.Message;
                return false;
            }
        }
    }
}
