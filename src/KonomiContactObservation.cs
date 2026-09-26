using System;
using System.Linq;
using Kingmaker;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.View.Spawners;
using Evidence = Tirabade.JerribethRecovery.Evidence;
using Source = Tirabade.JerribethRecovery.Source;

namespace Tirabade
{
    // Positive correspondence evidence is separate from known interruption and from unknown state.
    internal static class KonomiContactObservation
    {
        private static readonly Source source = new Source(
            "2570015799edf594daf2f076f2f975d8", "DrezenCapital_Default_Mechanics",
            "c658c4cf-116e-4b61-9ff9-8905bcf4fd6b", "ca2d58c5c65723945857e04fb85d30ce");

        internal sealed class Result
        {
            internal readonly bool Available, Invalidated;
            internal Result(bool available, bool invalidated)
            { Available = available; Invalidated = invalidated; }
        }

        internal static Result Observe(bool officeActive)
        {
            if (officeActive) return new Result(false, true);
            var game = Game.Instance;
            if (game?.Player == null || game.IsLoadingSave || game.IsUnloading
                || LoadingProcess.Instance.IsLoadingInProcess || game.State.LoadedAreaState == null)
                return new Result(false, false);
            var retained = InspectSaved(game.State, id => EntityService.Instance.GetEntity(id));
            if (retained.Invalidated) return retained;
            var area = game.State.LoadedAreaState;
            return Inspect(officeActive, area.Blueprint.AssetGuid.ToString(), area.GetAllSceneStates().ToArray(),
                state => state.IsSceneLoaded && state.IsSceneLoadedThreadSafe && state.IsPostLoadExecuted,
                id => EntityService.Instance.GetEntity(id));
        }

        // Unloaded saved storage can disprove eligibility but can never grant initial contact.
        internal static Result InspectSaved(PersistentState persistent, Func<string, EntityDataBase?> lookup)
        {
            try
            {
                var areas = persistent.SavedAreaStates.Concat(persistent.LoadedAreaState == null
                    ? new AreaPersistentState[0] : new[] { persistent.LoadedAreaState })
                    .Distinct().Where(area => area.AreaGuid.ToString() == source.Area).ToArray();
                if (areas.Length > 1) return new Result(false, true);
                if (areas.Length == 0) return new Result(false, false);
                var states = areas[0].GetAllSceneStates().ToArray();
                var scenes = states.Where(state => state.SceneName == source.Scene).ToArray();
                if (scenes.Length > 1) return new Result(false, true);
                if (scenes.Length == 0) return new Result(false, false);
                var entries = states.SelectMany(state => state.AllEntityData).ToArray();
                var matches = entries.Where(entity => entity.UniqueId == source.Spawner).ToArray();
                if (matches.Length == 0) return new Result(false, false);
                if (matches.Length != 1 || !(matches[0] is UnitSpawnerBase.MyData spawner)
                    || !scenes[0].AllEntityData.Contains(spawner)) return new Result(false, true);
                if (spawner.HoldingState != null && !ReferenceEquals(spawner.HoldingState, scenes[0])) return new Result(false, true);
                var registeredSpawner = lookup(source.Spawner);
                if (registeredSpawner != null && !ReferenceEquals(registeredSpawner, spawner)) return new Result(false, true);
                if (spawner.HasDied || spawner.Destroyed || spawner.DestroyMark || spawner.IsDisposed)
                    return new Result(false, true);
                string id = spawner.SpawnedUnit.UniqueId;
                if (string.IsNullOrEmpty(id)) return new Result(false, false);
                if (!spawner.HasSpawned || entries.OfType<UnitSpawnerBase.MyData>().Any(other => !ReferenceEquals(other, spawner)
                    && other.SpawnedUnit.UniqueId == id)) return new Result(false, true);
                var actors = entries.Where(entity => entity.UniqueId == id).ToArray();
                if (actors.Length == 0) return new Result(false, false);
                if (actors.Length != 1 || !(actors[0] is UnitEntityData actor)
                    || !scenes[0].AllEntityData.Contains(actor) || actor.Blueprint.AssetGuid.ToString() != source.Blueprint)
                    return new Result(false, true);
                var registeredActor = lookup(id);
                if (registeredActor != null && !ReferenceEquals(registeredActor, actor)) return new Result(false, true);
                if (actor.HoldingState != null && !ReferenceEquals(actor.HoldingState, scenes[0])) return new Result(false, true);
                return new Result(false, actor.State.IsDead || actor.State.IsFinallyDead
                    || actor.Destroyed || actor.DestroyMark || actor.IsDisposed);
            }
            catch
            {
                return new Result(false, false);
            }
        }

        internal static Result Inspect(bool officeActive, string area, SceneEntitiesState[] states,
            Func<SceneEntitiesState, bool> loaded, Func<string, EntityDataBase?> lookup)
        {
            if (officeActive) return new Result(false, true);
            var observation = JerribethRecovery.Inspect(source, area, states, loaded, lookup);
            if (observation.Kind == Evidence.NotLoaded) return new Result(false, false);
            if (observation.Kind == Evidence.Conflict || observation.Kind == Evidence.RetainedDead
                || observation.Kind == Evidence.RecordedDeadMissingActor) return new Result(false, true);
            try
            {
                var entries = states.SelectMany(state => state.AllEntityData).ToArray();
                var matches = entries.Where(entity => entity.UniqueId == source.Spawner).ToArray();
                if (matches.Length != 1 || !(matches[0] is UnitSpawnerBase.MyData spawner)
                    || !ReferenceEquals(lookup(source.Spawner), spawner)
                    || spawner.HoldingState?.SceneName != source.Scene)
                    return new Result(false, false);
                // This route cannot explain a resurrection, even if current life has been restored.
                if (spawner.HasDied || spawner.Destroyed || spawner.DestroyMark || spawner.IsDisposed)
                    return new Result(false, true);
                string actorId = spawner.SpawnedUnit.UniqueId;
                if (!string.IsNullOrEmpty(actorId))
                {
                    if (entries.OfType<UnitSpawnerBase.MyData>().Any(other => !ReferenceEquals(other, spawner)
                        && other.SpawnedUnit.UniqueId == actorId)) return new Result(false, true);
                    if (lookup(actorId) is UnitEntityData actor && entries.Count(entity => ReferenceEquals(entity, actor)) == 1
                        && actor.Blueprint.AssetGuid.ToString() == source.Blueprint
                        && ReferenceEquals(actor.HoldingState, spawner.HoldingState)
                        && (actor.Destroyed || actor.DestroyMark || actor.IsDisposed)) return new Result(false, true);
                }
                return new Result(observation.Kind == Evidence.RetainedAlive, false);
            }
            catch
            {
                // Incomplete native state is not positive evidence of either survival or death.
                return new Result(false, false);
            }
        }
    }
}
