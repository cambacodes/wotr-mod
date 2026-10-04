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
            // eng7-l11: one observational predicate for contact selection and harness evidence.
            var observations = matches.Select(Observe).ToArray();
            return Rules.SingleUsable(observations, actor => actor.Usable, actor => actor.Ignorable) != null;
            // end eng7-l11
        }

        // eng7-l11: no restoration, awakening, relocation or dialog speaker resolution.
        private static NativeContactObservation Observe(UnitEntityData actor)
        {
            // Preserve the native selector's short circuit for destroyed/dead originals.
            var ignored = new NativeContactObservation { Id = actor.UniqueId, Destroyed = actor.Destroyed,
                DestroyMark = actor.DestroyMark, Disposed = actor.IsDisposed, Storage = "not sampled (dead/destroyed)" };
            if (!ignored.Destroyed && !ignored.DestroyMark && !ignored.Disposed)
            {
                ignored.Dead = actor.State.IsDead;
                ignored.FinallyDead = actor.State.IsFinallyDead;
            }
            if (ignored.Ignorable) return ignored;
            var game = Game.Instance;
            var player = game?.Player;
            var commander = player?.MainCharacter.Value;
            var area = game?.State.LoadedAreaState;
            var holding = actor.HoldingState;
            var view = actor.View;
            return new NativeContactObservation {
                Id = actor.UniqueId,
                ContextReady = game?.CurrentlyLoadedArea != null && !game.IsLoadingSave && !game.IsUnloading
                    && player != null && commander != null && !player.IsInCombat && commander.State.IsConscious,
                Storage = holding == null ? "none" : ReferenceEquals(holding, player?.CrossSceneState) ? "cross-scene"
                    : area != null && area.GetAllSceneStates().Contains(holding) ? "current-area" : "other-scene",
                Position = new[] { actor.Position.x, actor.Position.y, actor.Position.z },
                Destroyed = actor.Destroyed, DestroyMark = actor.DestroyMark, Disposed = actor.IsDisposed,
                Dead = actor.State.IsDead, FinallyDead = actor.State.IsFinallyDead,
                CurrentStorage = area != null && player != null && HasCurrentStorage(actor, area, player.CrossSceneState),
                SceneLoaded = holding != null && (ReferenceEquals(holding, player?.CrossSceneState) || holding.IsSceneLoaded),
                ViewPresent = view != null, ViewMatches = view != null && ReferenceEquals(view.Data, actor),
                ViewSceneLoaded = view != null && view.gameObject.scene.isLoaded,
                ViewActive = view != null && view.gameObject.activeInHierarchy,
                InGame = actor.IsInGame, Suppressed = actor.Suppressed, Conscious = actor.State.IsConscious,
                Enemy = commander != null && actor.IsEnemy(commander)
            };
        }

        internal static NativeContactObservation[] Inventory(string guid)
        {
            var game = Game.Instance;
            if (game?.Player == null) return System.Array.Empty<NativeContactObservation>();
            var id = BlueprintGuid.Parse(guid);
            return game.State.Units.Where(unit => unit.Blueprint?.AssetGuid == id || unit.OriginalBlueprint?.AssetGuid == id)
                .Select(Observe).ToArray();
        }

        internal static bool InventoryAvailable(string guid) =>
            Rules.SingleUsable(Inventory(guid), actor => actor.Usable, actor => actor.Ignorable) != null;
        // end eng7-l11

        // Native companions and pets keep their saved cross-scene storage even when placed in the capital.
        internal static bool HasCurrentStorage(EntityDataBase actor, AreaPersistentState area, SceneEntitiesState crossScene)
        {
            var holding = actor.HoldingState;
            return holding != null && holding.AllEntityData.Contains(actor)
                && (ReferenceEquals(holding, crossScene) || area.GetAllSceneStates().Contains(holding));
        }
    }
}
