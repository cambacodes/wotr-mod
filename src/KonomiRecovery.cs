using System;
using System.Linq;
using Kingmaker;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.View.Spawners;
using Newtonsoft.Json;
using Evidence = Tirabade.JerribethRecovery.Evidence;
using Source = Tirabade.JerribethRecovery.Source;

namespace Tirabade
{
    // Explicit recovery of the retained native body only; polling never repeats resurrection.
    internal static class KonomiRecovery
    {
        internal enum Outcome { NotRequested, Blocked, Pending, Confirmed }
        internal sealed class Attempt
        {
            public int Version = 1;
            public string Request = "";
            public string UnitId = "";
            public bool Confirmed;
        }

        private const string Key = "RanRomance.Tirabade.KonomiRecovery";
        private static readonly Source source = new Source(
            "2570015799edf594daf2f076f2f975d8", "DrezenCapital_Default_Mechanics",
            "c658c4cf-116e-4b61-9ff9-8905bcf4fd6b", "ca2d58c5c65723945857e04fb85d30ce");
        internal static Exception? LastError { get; private set; }

        private static Attempt? Read()
        {
            if (!Game.Instance.Player.SettingsList.TryGetValue(Key, out var value)) return null;
            var attempt = value is string json ? JsonConvert.DeserializeObject<Attempt>(json) : null;
            if (attempt == null || attempt.Version != 1 || string.IsNullOrWhiteSpace(attempt.Request)
                || string.IsNullOrWhiteSpace(attempt.UnitId)) throw new InvalidOperationException("Invalid Konomi recovery checkpoint.");
            return attempt;
        }

        private static void Save(Attempt attempt) => Game.Instance.Player.SettingsList[Key] = JsonConvert.SerializeObject(attempt);

        internal static string? RequestedAction() => Read()?.Request;

        internal static bool ReturnCorrespondenceAvailable()
        {
            try
            {
                return TryLoaded(out var actor, out _) && HasVerifiedReturn(actor!)
                    && actor!.State.IsConscious && !actor.Suppressed;
            }
            catch { return false; }
        }

        internal static bool ReturnContactAvailable()
        {
            try
            {
                if (!TryLoaded(out var actor, out _) || !HasVerifiedReturn(actor!)) return false;
                var visibleCandidates = Game.Instance.State.Units.Where(unit => unit.Blueprint == actor!.Blueprint).Take(2).ToArray();
                return visibleCandidates.Length == 1 && ReferenceEquals(visibleCandidates[0], actor)
                    && NativeContact.IsAvailable(actor!.Blueprint);
            }
            catch { return false; }
        }

        internal static bool CanRequest()
        {
            try
            {
                return TryLoaded(out var actor, out _) && Read()?.Confirmed != true
                    && (actor!.State.IsDead || actor.State.IsFinallyDead);
            }
            catch { return false; }
        }

        internal static bool RetainedDead()
        {
            try { return TryLoaded(out var actor, out _) && (actor!.State.IsDead || actor.State.IsFinallyDead); }
            catch { return false; }
        }

        // E11: the exact retained actor is loaded, alive and hostile to the Commander. Read-only, and observable only while
        // her capital scene is loaded (the same inspection RetainedDead uses); elsewhere it reads false.
        internal static bool RetainedHostile()
        {
            try
            {
                return TryObserve(out var actor, out var commander) && !actor!.State.IsDead && !actor.State.IsFinallyDead
                    && actor.IsEnemy(commander!);
            }
            catch { return false; }
        }

        // authorized represents the caller's current quest, mythic and explicit-choice requirements.
        internal static Outcome Request(string requestIdentity, bool authorized, out string message)
        {
            LastError = null;
            message = "The conditions for her return are not met.";
            if (!authorized || string.IsNullOrWhiteSpace(requestIdentity)) return Outcome.Blocked;
            try
            {
                if (!TryLoaded(out var actor, out var commander)) return Outcome.Pending;
                var attempt = Read();
                if (attempt == null)
                {
                    if (!actor!.State.IsDead && !actor.State.IsFinallyDead)
                    { message = "Konomi is already alive. No restoration was begun."; return Outcome.Blocked; }
                    attempt = new Attempt { Request = requestIdentity, UnitId = actor.UniqueId };
                    Save(attempt);
                }
                if (attempt.Request != requestIdentity)
                { message = "Another promise already governs this return."; return Outcome.Blocked; }
                return Apply(attempt, actor!, commander!, ObserveCurrent, Save, true, out message);
            }
            catch (Exception ex)
            { LastError = ex; message = "Her return was interrupted and has not been confirmed."; return Outcome.Blocked; }
        }

        // Verification only. An authored success flag must wait for Confirmed from this current observation.
        internal static Outcome Poll(bool authorized, out string message)
        {
            LastError = null;
            message = "Konomi's return has not been confirmed.";
            if (!authorized) return Outcome.Blocked;
            try
            {
                var attempt = Read();
                if (attempt == null) return Outcome.NotRequested;
                if (!TryLoaded(out var actor, out var commander)) return Outcome.Pending;
                return Apply(attempt, actor!, commander!, ObserveCurrent, Save, false, out message);
            }
            catch (Exception ex)
            { LastError = ex; return Outcome.Blocked; }
        }

        // Historical return remains established during temporary unconsciousness, after the caller validates saved provenance.
        // It is not a substitute for actor identity, destruction, hostility or office checks.
        internal static bool HasVerifiedReturn(UnitEntityData actor)
        {
            try
            {
                var attempt = Read();
                return attempt?.Confirmed == true && actor.UniqueId == attempt.UnitId
                    && actor.Blueprint.AssetGuid.ToString() == source.Blueprint
                    && !actor.Destroyed && !actor.DestroyMark && !actor.IsDisposed
                    && !actor.State.IsDead && !actor.State.IsFinallyDead;
            }
            catch { return false; }
        }

        private static UnitEntityData? ObserveCurrent() => TryLoaded(out var actor, out _) ? actor : null;

        private static bool TryLoaded(out UnitEntityData? actor, out UnitEntityData? commander) =>
            TryObserve(out actor, out commander) && !actor!.IsEnemy(commander!);

        private static bool TryObserve(out UnitEntityData? actor, out UnitEntityData? commander)
        {
            actor = null;
            commander = null;
            var game = Game.Instance;
            if (game?.Player == null || game.IsLoadingSave || game.IsUnloading
                || LoadingProcess.Instance.IsLoadingInProcess || game.Player.IsInCombat || game.State.LoadedAreaState == null)
                return false;
            commander = game.Player.MainCharacter.Value;
            if (commander == null || !commander.State.IsConscious || commander.State.IsDead || commander.State.IsFinallyDead) return false;
            var area = game.State.LoadedAreaState;
            if (game.State.SavedAreaStates.Any(saved => saved.AreaGuid.ToString() == source.Area
                && !ReferenceEquals(saved, area))) return false;
            actor = Inspect(area.AreaGuid.ToString(), area.GetAllSceneStates().ToArray(),
                state => state.IsSceneLoaded && state.IsSceneLoadedThreadSafe && state.IsPostLoadExecuted && !state.SkipSerialize,
                id => EntityService.Instance.GetEntity(id));
            return actor != null;
        }

        internal static UnitEntityData? Inspect(string area, SceneEntitiesState[] states,
            Func<SceneEntitiesState, bool> loaded, Func<string, EntityDataBase?> lookup)
        {
            var observed = JerribethRecovery.Inspect(source, area, states, loaded, lookup);
            if (observed.Kind != Evidence.RetainedAlive && observed.Kind != Evidence.RetainedDead) return null;
            var entries = states.SelectMany(state => state.AllEntityData).ToArray();
            if (entries.OfType<UnitSpawnerBase.MyData>().Count(spawner => spawner.SpawnedUnit.UniqueId == observed.ActorId) != 1
                || entries.OfType<UnitEntityData>().Count(unit => unit.Blueprint.AssetGuid.ToString() == source.Blueprint) != 1)
                return null;
            return lookup(observed.ActorId!) as UnitEntityData;
        }

        // Tests supply saved storage and persistence; the resurrection operation itself is always native.
        internal static Outcome Apply(Attempt attempt, UnitEntityData actor, UnitEntityData commander,
            Func<UnitEntityData?> inspect, Action<Attempt> persist, bool invoke, out string message)
        {
            LastError = null;
            message = "Konomi's return has not been confirmed.";
            try
            {
                if (attempt.Version != 1 || string.IsNullOrWhiteSpace(attempt.Request) || string.IsNullOrWhiteSpace(attempt.UnitId) || actor.UniqueId != attempt.UnitId
                    || !ReferenceEquals(inspect(), actor)) return Outcome.Blocked;
                bool dead = actor.State.IsDead || actor.State.IsFinallyDead;
                if (attempt.Confirmed && dead)
                { message = "Konomi has fallen again. The earlier return cannot restore her a second time."; return Outcome.Blocked; }
                if (invoke && dead)
                {
                    // Persist even resumed requests before touching native state; a failed write prevents dispatch.
                    persist(attempt);
                    actor.Descriptor.ResurrectAndFullRestore(commander);
                }
                if (!ReferenceEquals(inspect(), actor) || actor.State.IsDead || actor.State.IsFinallyDead || !actor.State.IsConscious)
                    return Outcome.Pending;
                if (!attempt.Confirmed)
                {
                    // Save a separate value so a failed write cannot make the pending object look confirmed.
                    persist(new Attempt { Request = attempt.Request, UnitId = attempt.UnitId, Confirmed = true });
                }
                message = "Konomi is alive and conscious again.";
                return Outcome.Confirmed;
            }
            catch (Exception ex)
            {
                LastError = ex;
                message = "Her return was interrupted. It must be checked before anything more is promised.";
                return Outcome.Pending;
            }
        }
    }
}
