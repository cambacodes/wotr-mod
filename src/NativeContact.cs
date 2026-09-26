using System.Linq;
using Kingmaker;
using Kingmaker.Blueprints;

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
            if (game?.CurrentlyLoadedArea == null || player == null || commander == null
                || player.IsInCombat || !commander.State.IsConscious) return false;
            var matches = game.State.Units.Where(unit => unit.Blueprint == blueprint).Take(2).ToArray();
            if (matches.Length != 1) return false;
            var actor = matches[0];
            return !actor.Destroyed && !actor.DestroyMark && !actor.IsDisposed
                && actor.HoldingState != null && actor.HoldingState.IsSceneLoaded
                && game.State.LoadedAreaState != null && game.State.LoadedAreaState.AllEntityData.Contains(actor)
                && actor.IsInGame && !actor.Suppressed && actor.State.IsConscious
                && !actor.State.IsDead && !actor.State.IsFinallyDead && !actor.IsEnemy(commander);
        }
    }
}
