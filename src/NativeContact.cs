using System.Linq;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;

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
            // A PretendUnit blueprint (Seelah_NPC_Level1 -> Seelah_Companion) reports the pretended Blueprint once its facts
            // activate; match OriginalBlueprint too, as GuestPresence does (Rules.IsPresenceUnit).
            // A route-saved living copy (an E12 spawn-copy presence, e.g. Wenduag's) shares the blueprint of a dead original; the one
            // usable unit (living, in game, scene-loaded) is the contact when every other match is dead or destroyed. Two usable units,
            // or a usable one beside a living unusable one (e.g. an unloaded or suppressed twin), stay ambiguous (Rules.SingleUsable).
            var matches = game.State.Units.Where(unit => unit.Blueprint == blueprint || unit.OriginalBlueprint == blueprint).ToArray();
            var area = game.State.LoadedAreaState;
            return Rules.SingleUsable(matches, actor => Usable(actor), Ignorable) != null;
        }

        // eng7-l05: observing never restores or awakens an actor. Managed unhide may relax only visibility.
        internal static bool Ignorable(UnitEntityData actor) => actor.Destroyed || actor.DestroyMark || actor.IsDisposed
            || actor.State.IsDead || actor.State.IsFinallyDead;

        internal static bool Usable(UnitEntityData actor, bool allowHidden = false)
        {
            var game = Game.Instance;
            var player = game?.Player;
            var commander = player?.MainCharacter.Value;
            var area = game?.State.LoadedAreaState;
            var view = actor.View;
            return game?.CurrentlyLoadedArea != null && !game.IsLoadingSave && !game.IsUnloading
                && player != null && commander != null && !player.IsInCombat && commander.State.IsConscious
                && !Ignorable(actor) && area != null && HasCurrentStorage(actor, area, player.CrossSceneState)
                && (ReferenceEquals(actor.HoldingState, player.CrossSceneState) || actor.HoldingState!.IsSceneLoaded)
                && (allowHidden && !actor.IsInGame || view != null && ReferenceEquals(view.Data, actor)
                    && view.gameObject.scene.isLoaded && (allowHidden || view.gameObject.activeInHierarchy && actor.IsInGame))
                && !actor.Suppressed && actor.State.IsConscious && !actor.IsEnemy(commander);
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
