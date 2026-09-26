using System;
using System.Linq;
using Kingmaker;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.View.Spawners;

namespace Tirabade
{
    // Observation only. Neither a dead marker nor an unresolved actor authorizes a return.
    internal static class JerribethRecovery
    {
        internal enum Evidence { NotLoaded, Unresolved, NotSpawned, RetainedAlive, RetainedDead, RecordedDeadMissingActor, Conflict }

        internal sealed class Source
        {
            internal readonly string Area, Scene, Spawner, Blueprint;
            internal Source(string area, string scene, string spawner, string blueprint)
            { Area = area; Scene = scene; Spawner = spawner; Blueprint = blueprint; }
        }

        private static readonly Source[] sources = {
            new Source("982abcee3e7b25f459bef22ea22b3ab5", "IvorySanctumMainPart_Mechanics", "9fa07641-a8db-4f01-b43e-28658574e4ce", "bb9fe2c12d6941a43bfd5d5090ac97b9"),
            new Source("982abcee3e7b25f459bef22ea22b3ab5", "IvorySanctumMainPart_Mechanics", "b9c46ad9-ea18-462b-bfef-140a1060348c", "bb9fe2c12d6941a43bfd5d5090ac97b9"),
            new Source("8217b05e37078414981d994151f0ffb1", "AlushinyrraHigherCityVellexiaPlace_DefaultEtude_Mechanics", "5f976e09-1f17-4f78-907c-fb133d947090", "417ce3dcf3a9707488f2b9b2a790814b"),
            new Source("8217b05e37078414981d994151f0ffb1", "AlushinyrraHigherCity_VellexiaThirdDate_Mechanics", "da348c4f-6c2a-452c-9c20-0d65fdba7168", "417ce3dcf3a9707488f2b9b2a790814b")
        };

        internal sealed class Observation
        {
            internal readonly Source Source;
            internal readonly Evidence Kind;
            internal readonly string? ActorId;
            internal readonly string Detail;
            internal Observation(Source source, Evidence kind, string? actorId, string detail)
            { Source = source; Kind = kind; ActorId = actorId; Detail = detail; }
        }

        // Returns every audited representation; callers must not choose the first living one.
        // No observation here proves consent, usable contact, or absence in unloaded scenes.
        internal static Observation[] Observe()
        {
            var game = Game.Instance;
            if (game?.Player == null || game.IsLoadingSave || game.IsUnloading
                || LoadingProcess.Instance.IsLoadingInProcess || game.State.LoadedAreaState == null)
                return sources.Select(s => new Observation(s, Evidence.NotLoaded, null, "Native state is not ready.")).ToArray();
            var area = game.State.LoadedAreaState;
            var states = area.GetAllSceneStates().ToArray();
            var observations = sources.Select(source => Inspect(source, area.Blueprint.AssetGuid.ToString(), states,
                state => state.IsSceneLoaded && state.IsSceneLoadedThreadSafe && state.IsPostLoadExecuted,
                id => EntityService.Instance.GetEntity(id))).ToArray();
            // The same saved actor attributed to separate spawners is ambiguous provenance.
            foreach (var group in observations.Where(o => o.ActorId != null).GroupBy(o => o.ActorId).Where(g => g.Count() > 1))
                foreach (var item in group)
                    observations[Array.IndexOf(observations, item)] = new Observation(item.Source, Evidence.Conflict, item.ActorId, "Multiple native spawners reference this actor.");
            return observations;
        }

        // Native saved objects are inspected directly. Delegates isolate only scene loading and registry lookup for managed tests.
        internal static Observation Inspect(Source source, string area, SceneEntitiesState[] states,
            Func<SceneEntitiesState, bool> loaded, Func<string, EntityDataBase?> lookup)
        {
            string? actorId = null;
            Observation Result(Evidence kind, string detail) => new Observation(source, kind, actorId, detail);
            try
            {
                if (area != source.Area) return Result(Evidence.NotLoaded, "The native source area is not loaded.");
                var matchingStates = states.Where(s => s.SceneName == source.Scene).ToArray();
                if (matchingStates.Length > 1) return Result(Evidence.Conflict, "Duplicate source scene states.");
                if (matchingStates.Length == 0 || !loaded(matchingStates[0])) return Result(Evidence.NotLoaded, "The native source scene is not loaded.");
                var state = matchingStates[0];
                var spawners = states.SelectMany(s => s.AllEntityData).Where(e => e.UniqueId == source.Spawner).ToArray();
                if (spawners.Length == 0) return Result(Evidence.Unresolved, "No saved source spawner was found.");
                if (spawners.Length != 1 || !(spawners[0] is UnitSpawnerBase.MyData data)
                    || !ReferenceEquals(data.HoldingState, state) || !state.AllEntityData.Contains(data)
                    || !ReferenceEquals(lookup(source.Spawner), data))
                    return Result(Evidence.Conflict, "Source spawner type, storage or registry differs.");
                if (data.Destroyed || data.DestroyMark || data.IsDisposed)
                    return Result(Evidence.Unresolved, "Native source spawner is being removed or disposed.");
                actorId = data.SpawnedUnit.UniqueId;
                if (!data.HasSpawned)
                    return Result(data.HasDied || !string.IsNullOrEmpty(actorId) ? Evidence.Conflict : Evidence.NotSpawned,
                        "Source spawner has not recorded a spawn.");
                if (string.IsNullOrEmpty(actorId))
                    return Result(Evidence.Unresolved, "Spawned history has no saved actor identity.");
                var entries = states.SelectMany(s => s.AllEntityData).Where(e => e.UniqueId == actorId).ToArray();
                var registered = lookup(actorId!);
                if (entries.Length > 1 || entries.Length == 1 && !ReferenceEquals(entries[0], registered))
                    return Result(Evidence.Conflict, "Actor storage and registry disagree.");
                if (registered == null)
                    return Result(data.HasDied ? Evidence.RecordedDeadMissingActor : Evidence.Unresolved,
                        "Saved actor reference does not resolve; no replacement is authorized.");
                if (!(registered is UnitEntityData actor) || actor.Blueprint.AssetGuid.ToString() != source.Blueprint
                    || entries.Length != 1 || !ReferenceEquals(actor.HoldingState, state)
                    || !state.AllEntityData.Contains(actor))
                    return Result(Evidence.Conflict, "Saved actor type, blueprint or source storage differs.");
                if (actor.Destroyed || actor.DestroyMark || actor.IsDisposed)
                    return Result(Evidence.Unresolved, "Referenced actor is being removed or disposed.");
                return Result(actor.State.IsDead || actor.State.IsFinallyDead ? Evidence.RetainedDead : Evidence.RetainedAlive,
                    "Exact retained native actor; life state is not consent or physical contact.");
            }
            catch (Exception ex)
            {
                return Result(Evidence.Unresolved, "Native observation failed: " + ex.GetType().Name);
            }
        }
    }
}
