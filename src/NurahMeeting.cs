using System;
using System.Linq;
using Kingmaker;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.View.Spawners;

namespace Tirabade
{
    // Retained living Nurah only. Observation never creates an actor or rewrites native history.
    internal sealed class NurahMeeting
    {
        internal const string Capital = "2570015799edf594daf2f076f2f975d8";
        internal const string SceneAsset = "3e2b5ea054cd5b2479e7f13134363ef4";
        internal const string Spawner = "c2b298fc-d794-4995-8b49-822b75c3bb62";
        internal const string Unit = "f999fc37ddb225640b7f98c0a05d6948";
        internal const string Group = "d0210e61193c8c746bc33bf7d1fff325";
        internal const string Hidden = "245524f91e743b64eaa16445c3ea8e73";
        internal const string Prison = "c922e0cbe25a0cf4dad4ce7a3ca81935";
        internal const string Romance = "9f655e252d334f04884f10188b0d8928";
        internal const string Finale = "f8a7511233524742bc42b25190609f4c";
        internal static readonly string[] Deaths = { "a837c3bc9cbb4e846ab5565915165c91",
            "20927a9471c00814b808fd69e88879c7", "739b9fe9b8998c641b4b3dfed40bc217" };
        internal static readonly string[] Personalities = { "91f7abac0d8e46e19ce8fc45fa3df58e",
            "f74eaab69b3d49d0a222eb1b2834777e", "3d2d02611cd24f579e7b7b411b94263e" };
        private static readonly JerribethRecovery.Source source = new JerribethRecovery.Source(
            Capital, "DrezenCapital_Default_Mechanics", Spawner, Unit);
        private readonly BlueprintEtude romance, prison;
        private readonly BlueprintEtude[] deaths, personalities;
        private readonly BlueprintCue finale;
        internal Exception? LastError { get; private set; }

        internal NurahMeeting(Func<string, SimpleBlueprint> resolve)
        {
            T Get<T>(string id) where T : SimpleBlueprint
            {
                var value = resolve(id);
                if (!(value is T typed) || typed.AssetGuid.ToString() != id)
                    throw new InvalidOperationException("Nurah native binding differs: " + id);
                return typed;
            }
            romance = Get<BlueprintEtude>(Romance);
            prison = Get<BlueprintEtude>(Prison);
            deaths = Deaths.Select(Get<BlueprintEtude>).ToArray();
            personalities = Personalities.Select(Get<BlueprintEtude>).ToArray();
            finale = Get<BlueprintCue>(Finale);
        }

        internal bool CorrespondenceAvailable()
        {
            try
            {
                var game = Game.Instance;
                if (game?.Player == null || RetainedActor() == null) return false;
                var system = game.Player.EtudesSystem;
                return HistoryPermits(system.Etudes.GetFact(romance),
                    PrisonBlocks(system, prison),
                    deaths.Any(etude => system.EtudeIsStarted(etude) || system.EtudeIsCompleted(etude)),
                    personalities.Select(etude => system.Etudes.GetFact(etude)).ToArray(),
                    game.Player.Dialog.ShownCues.Contains(finale));
            }
            catch (Exception ex) { LastError = ex; return false; }
        }

        // Native saved completion is published before the fact finishes deactivating.
        internal static bool PrisonBlocks(EtudesSystem system, BlueprintEtude prison)
        {
            var fact = system.Etudes.GetFact(prison);
            return fact != null && (!fact.IsCompleted || fact.IsPlaying || fact.CompletionInProgress)
                || system.EtudeIsStarted(prison) && !system.EtudeIsCompleted(prison);
        }

        // Historical imprisonment may be complete after release; current imprisonment still blocks.
        internal static bool HistoryPermits(Etude? romance, bool imprisoned, bool deathHistory,
            Etude?[] personalities, bool finaleSeen)
            => finaleSeen && romance != null && romance.IsPlaying && !romance.IsCompleted && !romance.CompletionInProgress
                && !imprisoned && !deathHistory
                && personalities.Length == 3 && personalities.Count(fact => fact != null && fact.IsPlaying
                    && !fact.IsCompleted && !fact.CompletionInProgress) == 1;

        internal static UnitEntityData? Inspect(string area, SceneEntitiesState[] states,
            Func<SceneEntitiesState, bool> loaded, Func<string, EntityDataBase?> lookup)
        {
            var observed = JerribethRecovery.Inspect(source, area, states, loaded, lookup);
            if (observed.Kind != JerribethRecovery.Evidence.RetainedAlive) return null;
            var entries = states.SelectMany(state => state.AllEntityData).ToArray();
            var spawners = entries.OfType<UnitSpawnerBase.MyData>().Where(item => item.SpawnedUnit.UniqueId == observed.ActorId).ToArray();
            if (spawners.Length != 1 || spawners[0].UniqueId != Spawner || spawners[0].HasDied
                || entries.OfType<UnitEntityData>().Count(actor => actor.Blueprint.AssetGuid.ToString() == Unit) != 1) return null;
            return lookup(observed.ActorId!) as UnitEntityData;
        }

        private static UnitEntityData? RetainedActor()
        {
            var game = Game.Instance;
            if (game?.Player == null || game.IsLoadingSave || game.IsUnloading || LoadingProcess.Instance.IsLoadingInProcess
                || game.State.LoadedAreaState?.AreaGuid.ToString() != Capital || game.Player.IsInCombat) return null;
            var commander = game.Player.MainCharacter.Value;
            if (commander == null || !commander.State.IsConscious || commander.State.IsDead || commander.State.IsFinallyDead) return null;
            var area = game.State.LoadedAreaState;
            if (game.State.SavedAreaStates.Any(saved => saved.AreaGuid.ToString() == Capital && !ReferenceEquals(saved, area))) return null;
            var actor = Inspect(Capital, area.GetAllSceneStates().ToArray(),
                state => state.IsSceneLoaded && state.IsSceneLoadedThreadSafe && state.IsPostLoadExecuted && !state.SkipSerialize,
                id => EntityService.Instance.GetEntity(id));
            return actor != null && actor.State.IsConscious && !actor.Suppressed && !actor.IsEnemy(commander) ? actor : null;
        }
    }
}
