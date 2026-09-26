using System.Linq;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.EntitySystem;

namespace Tirabade
{
    internal static class NativeContact
    {
        // Observe the loaded actor without using DialogSpeaker.GetEntity, which
        // can wake or restore speakers as a side effect of finding them.
        internal static bool IsAvailable(BlueprintUnit blueprint)
        {
            var game = Game.Instance;
            var player = game?.Player;
            var commander = player?.MainCharacter.Value;
            if (game?.CurrentlyLoadedArea == null || game.IsLoadingSave || game.IsUnloading || player == null || commander == null
                || player.IsInCombat || !commander.State.IsConscious) return false;
            var matches = game.State.Units.Where(unit => unit.Blueprint == blueprint).Take(2).ToArray();
            if (matches.Length != 1) return false;
            var actor = matches[0];
            var area = game.State.LoadedAreaState;
            var view = actor.View;
            return !actor.Destroyed && !actor.DestroyMark && !actor.IsDisposed
                && area != null && HasCurrentStorage(actor, area, player.CrossSceneState)
                && (ReferenceEquals(actor.HoldingState, player.CrossSceneState) || actor.HoldingState!.IsSceneLoaded)
                && view != null && ReferenceEquals(view.Data, actor)
                && view.gameObject.scene.isLoaded && view.gameObject.activeInHierarchy
                && actor.IsInGame && !actor.Suppressed && actor.State.IsConscious
                && !actor.State.IsDead && !actor.State.IsFinallyDead && !actor.IsEnemy(commander);
        }

        // Native companions and pets keep their saved cross-scene storage even when placed in the capital.
        internal static bool HasCurrentStorage(EntityDataBase actor, AreaPersistentState area, SceneEntitiesState crossScene)
        {
            var holding = actor.HoldingState;
            return holding != null && holding.AllEntityData.Contains(actor)
                && (ReferenceEquals(holding, crossScene) || area.GetAllSceneStates().Contains(holding));
        }
    }
}
