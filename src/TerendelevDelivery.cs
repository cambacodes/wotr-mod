using System;
using System.Linq;
using System.Reflection;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Classes.Experience;
using Kingmaker.Blueprints.Classes;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.View;
using Newtonsoft.Json;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace Tirabade
{
    internal static class TerendelevDelivery
    {
        internal static Exception? LastError { get; private set; }
        internal const string BlueprintId = "93578a5a84c7ec724d14de6d5aba6692";
        internal const string NativeHuman = "9e8401e7703907e4d94189d5992dd13e";
        internal const string OutdoorArea = "2570015799edf594daf2f076f2f975d8";
        internal const string OutdoorPart = "8a076e720870a44438d13b9b939933fd";
        internal const string OutdoorScene = "DrezenCapital_Outdoor_Mechanics";
        internal const string SaveKey = "RanRomance.Tirabade.TerendelevDelivery";
        private static readonly Vector3 Anchor = new Vector3(7.49f, 62f, -28.07f);
        private static readonly string[] ConflictingUnits = {
            NativeHuman, "045e2ea911644fa0abaa2f6c76b83feb", "1ee55895e5091bc459d540d42a72bd2c", "59e7482d41d058a4bace7434c67a08be", "376195cab0179734880947969d2b4e9c"
        };

        // Caller registers this deterministic blueprint before saved entities are deserialized.
        internal static BlueprintUnit CreateBlueprint(BlueprintUnit native)
        {
            var id = BlueprintGuid.Parse(BlueprintId);
            if (native.AssetGuid.ToString() != NativeHuman)
                throw new InvalidOperationException("Terendelev requires her native human source and a private blueprint identity.");
            var copy = new BlueprintUnit();
            copy.Become(native);
            if (ReferenceEquals(copy.Body, native.Body) || native.FactionOverrides != null && ReferenceEquals(copy.FactionOverrides, native.FactionOverrides))
                throw new InvalidOperationException("Terendelev's body and faction data were not independently copied.");
            copy.AssetGuid = id;
            copy.name = "RRT_TerendelevLivingDelivery";
            ConfigureBlueprint(copy, native);
            return copy;
        }

        internal static void ConfigureBlueprint(BlueprintUnit copy, BlueprintUnit native)
        {
            if (ReferenceEquals(copy, native) || ReferenceEquals(copy.Visual, native.Visual))
                throw new InvalidOperationException("Terendelev's visual parameters must be independently copied.");
            if (copy.ComponentsArray == null || copy.ComponentsArray.Count(c => c is AddClassLevels) != 1
                || copy.ComponentsArray.Any(c => !(c is Experience) && !(c is AddClassLevels))
                || copy.ComponentsArray.Any(c => native.ComponentsArray.Any(n => ReferenceEquals(n, c)))
                || copy.AlternativeBrains.Length != 0)
                throw new InvalidOperationException("Terendelev's copied behavior differs from the audited human blueprint.");
            copy.ComponentsArray = copy.ComponentsArray.Where(c => !(c is Experience)).ToArray();
            SetReference(copy, "m_Brain", "5718d805516c5ff48bf3e928b6c0e6fd");
            SetReference(copy, "m_Faction", "d8de50cc80eb4dc409a983991e0b77ad");
            Field(copy.Visual.GetType(), "m_Barks").SetValue(copy.Visual, null);
        }

        private static FieldInfo Field(Type type, string name) => type.GetField(name,
            BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)
            ?? throw new InvalidOperationException("Missing verified native field " + name);

        private static void SetReference(object target, string field, string id)
        {
            var member = Field(target.GetType(), field);
            var reference = (BlueprintReferenceBase)Activator.CreateInstance(member.FieldType);
            Field(typeof(BlueprintReferenceBase), "deserializedGuid").SetValue(reference, BlueprintGuid.Parse(id));
            member.SetValue(target, reference);
        }

        internal static TerendelevDeliveryAttempt? Read()
        {
            if (!Game.Instance.Player.SettingsList.TryGetValue(SaveKey, out var value)) return null;
            if (!(value is string json)) throw new InvalidOperationException("Invalid Terendelev delivery checkpoint.");
            var attempt = JsonConvert.DeserializeObject<TerendelevDeliveryAttempt>(json);
            if (attempt == null || !attempt.Valid) throw new InvalidOperationException("Invalid Terendelev delivery identity.");
            return attempt;
        }

        private static void Save(TerendelevDeliveryAttempt attempt) =>
            Game.Instance.Player.SettingsList[SaveKey] = JsonConvert.SerializeObject(attempt);

        // Authorization must represent the caller's current exact mythic/quest/conflict gate, not a remembered success flag.
        internal static TerendelevDeliveryResult Request(string provenance, bool authorized, BlueprintUnit blueprint,
            out UnitEntityData? actor, out string message)
        {
            actor = null;
            LastError = null;
            try
            {
                if (blueprint.AssetGuid.ToString() != BlueprintId) throw new InvalidOperationException("Unexpected delivery blueprint.");
                if (!authorized || string.IsNullOrWhiteSpace(provenance))
                { message = "The conditions for her return are not met."; return TerendelevDeliveryResult.Blocked; }
                var attempt = Read();
                if (attempt == null)
                {
                    attempt = new TerendelevDeliveryAttempt { UnitId = Guid.NewGuid().ToString(), Provenance = provenance };
                    Save(attempt);
                }
                if (attempt.Provenance != provenance)
                { message = "Another promise already governs her return."; return TerendelevDeliveryResult.Blocked; }
                return Poll(authorized, blueprint, out actor, out message);
            }
            catch (Exception ex)
            { LastError = ex; message = "Her return was interrupted. Her arrival has not been confirmed."; return TerendelevDeliveryResult.Blocked; }
        }

        internal static TerendelevDeliveryResult Poll(bool authorized, BlueprintUnit blueprint,
            out UnitEntityData? actor, out string message)
        {
            actor = null;
            LastError = null;
            message = "The meeting place is not ready.";
            try
            {
                if (blueprint.AssetGuid.ToString() != BlueprintId) throw new InvalidOperationException("Unexpected delivery blueprint.");
                var attempt = Read();
                if (attempt == null) return TerendelevDeliveryResult.NotRequested;
                if (!authorized) { message = "The conditions for her return are no longer met."; return TerendelevDeliveryResult.Blocked; }
                var game = Game.Instance;
                var commander = game.Player.MainCharacter.Value;
                if (game.IsLoadingSave || game.IsUnloading || Kingmaker.EntitySystem.Persistence.LoadingProcess.Instance.IsLoadingInProcess || commander == null || !commander.State.IsConscious || game.Player.IsInCombat
                    || game.CurrentlyLoadedArea?.AssetGuid.ToString() != OutdoorArea
                    || game.CurrentlyLoadedAreaPart?.AssetGuid.ToString() != OutdoorPart
                    || !SceneManager.GetSceneByName(OutdoorScene).isLoaded) return TerendelevDeliveryResult.Pending;
                var areaState = game.State.LoadedAreaState;
                if (areaState == null) return TerendelevDeliveryResult.Pending;
                var state = areaState.GetAllSceneStates().SingleOrDefault(s => s.SceneName == OutdoorScene);
                if (state == null || !state.IsSceneLoaded || !state.IsSceneLoadedThreadSafe || state.SkipSerialize)
                    return TerendelevDeliveryResult.Pending;
                var entities = areaState.AllEntityData.ToArray();
                if (entities.OfType<UnitEntityData>().Any(u => ConflictingUnits.Contains(u.Blueprint.AssetGuid.ToString())
                    && !u.Destroyed && !u.State.IsDead && !u.State.IsFinallyDead))
                { message = "Terendelev's present circumstances must be resolved before she can return."; return TerendelevDeliveryResult.Blocked; }
                var registry = EntityService.Instance.GetEntity(attempt.UnitId);
                var matches = entities.Where(e => e.UniqueId == attempt.UnitId).ToArray();
                var queued = game.EntityCreator.CreationQueue.Where(e => e.Entity.UniqueId == attempt.UnitId).ToArray();
                var duplicates = entities.OfType<UnitEntityData>().Where(u => u.Blueprint == blueprint && u.UniqueId != attempt.UnitId).ToArray();
                if (matches.Length > 1 || queued.Length > 1 || duplicates.Length > 0
                    || registry != null && (!(registry is UnitEntityData found) || found.Blueprint != blueprint)
                    || matches.Any(e => !ReferenceEquals(e, registry)) || queued.Any(e => !ReferenceEquals(e.Entity, registry) || !ReferenceEquals(e.State, state)))
                { message = "Her return cannot be completed here."; return TerendelevDeliveryResult.Blocked; }
                if (registry != null)
                {
                    var unit = (UnitEntityData)registry;
                    if (unit.Destroyed || unit.DestroyMark || unit.IsDisposed || unit.State.IsDead || unit.State.IsFinallyDead)
                    { message = "Terendelev is no longer alive. This return cannot be repeated."; return TerendelevDeliveryResult.Blocked; }
                    bool committed = queued.Length == 0 && matches.Length == 1 && ReferenceEquals(unit.HoldingState, state)
                        && state.AllEntityData.Count(e => ReferenceEquals(e, unit)) == 1;
                    bool usable = unit.View != null && unit.IsInGame && !unit.Suppressed && unit.State.IsConscious && !unit.IsEnemy(commander);
                    bool wasConfirmed = attempt.Confirmed;
                    if (attempt.TryConfirm(true, unit.UniqueId == attempt.UnitId && unit.Blueprint == blueprint, committed, usable))
                    { if (!wasConfirmed) Save(attempt); actor = unit; message = "Terendelev has arrived and is ready to speak with you."; return TerendelevDeliveryResult.Confirmed; }
                    message = "Terendelev is not yet ready to speak with you.";
                    return TerendelevDeliveryResult.Pending;
                }
                if (attempt.Submitted)
                { message = "Her return began, but her arrival cannot be confirmed."; return TerendelevDeliveryResult.Blocked; }
                if (!TryPosition(out var position)) return TerendelevDeliveryResult.Pending;
                if (!attempt.Submit(true, true, matches.Length == 0 && queued.Length == 0, () => Save(attempt),
                    () => game.EntityCreator.SpawnUnit(blueprint, position, new Quaternion(0f, -0.08658724f, 0f, 0.99624425f), state, attempt.UnitId)))
                    return TerendelevDeliveryResult.Blocked;
                message = "Her return has begun. Her arrival is not yet confirmed.";
                return TerendelevDeliveryResult.Pending;
            }
            catch (Exception ex)
            { LastError = ex; message = "Her return was interrupted. Her arrival has not been confirmed."; return TerendelevDeliveryResult.Blocked; }
        }

        private static bool TryPosition(out Vector3 position)
        {
            position = Anchor;
            var anchorNode = ObstacleAnalyzer.GetNearestNode(Anchor);
            if (anchorNode.node == null || !anchorNode.node.Walkable || (anchorNode.position - Anchor).sqrMagnitude > 0.25f) return false;
            FreePlaceSelector.PlaceSpawnPlaces(1, 0.5f, Anchor);
            position = FreePlaceSelector.GetRelaxedPosition(0, true);
            var nearest = ObstacleAnalyzer.GetNearestNode(position);
            if (nearest.node == null || !nearest.node.Walkable || nearest.node.Area != anchorNode.node.Area
                || (nearest.position - position).sqrMagnitude > 0.04f || (position - Anchor).sqrMagnitude > 16f) return false;
            // Validate a full collider-width footprint against the active navmesh, not only its center.
            for (int i = 0; i < 8; i++)
            {
                float angle = i * Mathf.PI / 4f;
                var edge = position + new Vector3(Mathf.Cos(angle), 0, Mathf.Sin(angle));
                var node = ObstacleAnalyzer.GetNearestNode(edge);
                if (node.node == null || !node.node.Walkable || node.node.Area != nearest.node.Area
                    || (node.position - edge).sqrMagnitude > 0.04f) return false;
            }
            var chosen = position;
            if (Game.Instance.State.Units.Any(u => u.IsInGame && !u.Destroyed && u.View != null
                && Math.Abs(u.Position.y - chosen.y) < 2f
                && new Vector2(u.Position.x - chosen.x, u.Position.z - chosen.z).sqrMagnitude < Math.Pow(1f + u.View.Corpulence, 2))) return false;
            // Ignore ground below the feet while checking the actual standing volume for static colliders.
            return !Physics.CheckBox(position + Vector3.up * 0.925f, new Vector3(1f, 0.875f, 1f),
                Quaternion.identity, Physics.DefaultRaycastLayers, QueryTriggerInteraction.Ignore);
        }
    }
}
