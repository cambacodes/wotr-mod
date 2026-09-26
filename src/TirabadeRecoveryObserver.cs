using System;
using System.Linq;
using Kingmaker;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Persistence;
using Evidence = Tirabade.JerribethRecovery.Evidence;
using Observation = Tirabade.JerribethRecovery.Observation;
using Source = Tirabade.JerribethRecovery.Source;

namespace Tirabade
{
    // Every result describes one saved representation, never the woman's recovery or usable contact.
    internal static class TirabadeRecoveryObserver
    {
        private static readonly Source[] sources = {
            new Source("2570015799edf594daf2f076f2f975d8", "DrezenCapital_Default_Mechanics", "86b332a9-5910-4d46-9951-8e06f7dcf0cf", "b5e867e13503c6f41bb1316705efb4a2"),
            new Source("2570015799edf594daf2f076f2f975d8", "DrezenCapital_Default_Mechanics", "3dc302d8-58ce-44f3-9766-2a437a080108", "280d4712dceb37f4a88e98f1f4c6e64f"),
            new Source("2ccc6731787b6ec41ab5adc13f1b9ce9", "Iz_Default_Mechanics", "8b5b891b-a569-42c0-a7dd-7177760fa64a", "9adfeebc39054544fa0f924022e43c1c"),
            new Source("2ccc6731787b6ec41ab5adc13f1b9ce9", "Iz_Default_Mechanics", "bf142b5f-85f6-439e-9e23-f23646e22401", "9adfeebc39054544fa0f924022e43c1c"),
            new Source("2ccc6731787b6ec41ab5adc13f1b9ce9", "Iz_Default_Mechanics", "d16d93ee-d53c-43da-9d0a-ff27eea9d15e", "9adfeebc39054544fa0f924022e43c1c")
        };

        internal static Observation[] Observe()
        {
            var game = Game.Instance;
            if (game?.Player == null || game.IsLoadingSave || game.IsUnloading
                || LoadingProcess.Instance.IsLoadingInProcess || game.State.LoadedAreaState == null)
                return sources.Select(source => new Observation(source, Evidence.NotLoaded, null, "Native state is not ready.")).ToArray();
            var area = game.State.LoadedAreaState;
            return Inspect(area.Blueprint.AssetGuid.ToString(), area.GetAllSceneStates().ToArray(),
                state => state.IsSceneLoaded && state.IsSceneLoadedThreadSafe && state.IsPostLoadExecuted,
                id => EntityService.Instance.GetEntity(id));
        }

        // Keep all alternatives, including dead and living Iz bodies; no first-match survival inference.
        internal static Observation[] Inspect(string area, SceneEntitiesState[] states,
            Func<SceneEntitiesState, bool> loaded, Func<string, EntityDataBase?> lookup)
        {
            var observations = sources.Select(source => JerribethRecovery.Inspect(source, area, states, loaded, lookup)).ToArray();
            foreach (var group in observations.Where(item => item.ActorId != null).GroupBy(item => item.ActorId).Where(group => group.Count() > 1))
                foreach (var item in group)
                    observations[Array.IndexOf(observations, item)] = new Observation(item.Source, Evidence.Conflict, item.ActorId,
                        "Multiple Tirabade source spawners reference this actor.");
            return observations;
        }
    }
}
