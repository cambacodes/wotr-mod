using System;
using System.Collections.Generic;
using System.Reflection;
using System.Runtime.Serialization;
using Kingmaker.Blueprints;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic;
using Kingmaker.View.Spawners;

internal static class KonomiContactObservationTests
{
    internal static void Run(Action<bool, string> check)
    {
        const BindingFlags instance = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
        var service = typeof(Tirabade.Main).Assembly.GetType("Tirabade.KonomiContactObservation", true)!;
        var source = service.GetField("source", BindingFlags.Static | BindingFlags.NonPublic)!.GetValue(null)!;
        string Read(string key) => (string)source.GetType().GetField(key, instance)!.GetValue(source)!;
        var inspect = service.GetMethod("Inspect", BindingFlags.Static | BindingFlags.NonPublic)!;
        var state = new SceneEntitiesState(Read("Scene"));
        var states = new[] { state };
        var registry = new Dictionary<string, EntityDataBase>();
        bool loaded = true, office = false;
        string area = Read("Area");
        void Expect(bool available, bool invalidated, string reason)
        {
            var result = inspect.Invoke(null, new object[] { office, area, states,
                new Func<SceneEntitiesState, bool>(_ => loaded),
                new Func<string, EntityDataBase?>(id => registry.TryGetValue(id, out var entity) ? entity : null) })!;
            check((bool)result.GetType().GetField("Available", instance)!.GetValue(result)! == available, reason + ": availability");
            check((bool)result.GetType().GetField("Invalidated", instance)!.GetValue(result)! == invalidated, reason + ": invalidation");
        }
        void Set(object item, Type type, string field, object value) => type.GetField(field, instance)!.SetValue(item, value);
        UnitSpawnerBase.MyData Spawner(string id)
        {
            var value = (UnitSpawnerBase.MyData)FormatterServices.GetUninitializedObject(typeof(UnitSpawnerBase.MyData));
            Set(value, typeof(EntityDataBase), "<UniqueId>k__BackingField", id);
            Set(value, typeof(EntityDataBase), "<HoldingState>k__BackingField", state);
            return value;
        }
        void Reference(UnitSpawnerBase.MyData value, string id)
        {
            object reference = default(UnitReference);
            Set(reference, typeof(UnitReference), "m_UniqueId", id);
            Set(value, typeof(UnitSpawnerBase.MyData), "m_SpawnedUnit", reference);
        }

        // Reproduce the gap: absence of the office does not establish a living correspondent.
        Expect(false, false, "Office absent with no actor evidence");
        var spawner = Spawner(Read("Spawner"));
        state.AllEntityData.Add(spawner);
        registry.Add(spawner.UniqueId, spawner);
        Expect(false, false, "Native never-spawned history");
        spawner.HasSpawned = true;
        Expect(false, false, "Spawned but saved identity missing");
        const string actorId = "a55c2d2b-0b0e-4b61-a426-e0f47a22bfaa";
        Reference(spawner, actorId);
        Expect(false, false, "Unresolved saved actor");
        spawner.HasDied = true;
        Expect(false, true, "Recorded death without retained actor");
        spawner.HasDied = false;

        var actor = (UnitEntityData)FormatterServices.GetUninitializedObject(typeof(UnitEntityData));
        var descriptor = (UnitDescriptor)FormatterServices.GetUninitializedObject(typeof(UnitDescriptor));
        var life = (UnitState)FormatterServices.GetUninitializedObject(typeof(UnitState));
        var blueprint = new BlueprintUnit { AssetGuid = BlueprintGuid.Parse(Read("Blueprint")) };
        Set(actor, typeof(UnitEntityData), "<Descriptor>k__BackingField", descriptor);
        Set(descriptor, typeof(UnitDescriptor), "<Blueprint>k__BackingField", blueprint);
        Set(descriptor, typeof(UnitDescriptor), "<Unit>k__BackingField", actor);
        Set(descriptor, typeof(UnitDescriptor), "State", life);
        Set(actor, typeof(EntityDataBase), "<UniqueId>k__BackingField", actorId);
        Set(actor, typeof(EntityDataBase), "<HoldingState>k__BackingField", state);
        Set(life, typeof(UnitState), "<LifeState>k__BackingField", UnitLifeState.Conscious);
        registry[actorId] = actor;
        state.AllEntityData.Add(actor);
        Expect(true, false, "Exact retained living actor without introduction requirement");
        office = true;
        Expect(false, true, "Active office excludes private acquisition");
        office = false;
        Expect(true, false, "Completed or never-started office permits observed living correspondent");
        loaded = false;
        Expect(false, false, "Unloaded capital does not revoke earned correspondence");
        office = true;
        Expect(false, true, "Known office still invalidates while capital unloaded");
        office = false;
        loaded = true;
        area = "Nexus";
        Expect(false, false, "Other area is unknown, not dead");
        area = Read("Area");
        Expect(true, false, "Return to loaded source restores positive observation");
        spawner.HasDied = true;
        Expect(false, true, "Current living actor does not explain historical death for acquisition");
        spawner.HasDied = false;
        Set(life, typeof(UnitState), "<LifeState>k__BackingField", UnitLifeState.Dead);
        Expect(false, true, "Actual native dead actor");
        Set(life, typeof(UnitState), "<LifeState>k__BackingField", UnitLifeState.Conscious);
        Set(life, typeof(UnitState), "<IsFinallyDead>k__BackingField", true);
        Expect(false, true, "Finally dead actor");
        Set(life, typeof(UnitState), "<IsFinallyDead>k__BackingField", false);
        Set(actor, typeof(EntityDataBase), "<DestroyMark>k__BackingField", true);
        Expect(false, true, "Actor queued for destruction");
        Set(actor, typeof(EntityDataBase), "<DestroyMark>k__BackingField", false);
        Set(spawner, typeof(EntityDataBase), "<DestroyMark>k__BackingField", true);
        Expect(false, true, "Spawner queued for destruction");
        Set(spawner, typeof(EntityDataBase), "<DestroyMark>k__BackingField", false);
        blueprint.AssetGuid = BlueprintGuid.Parse("64805abb52739e44280a758f850b300c");
        Expect(false, true, "Wrong blueprint under retained identity");
        blueprint.AssetGuid = BlueprintGuid.Parse(Read("Blueprint"));
        state.AllEntityData.Add(actor);
        Expect(false, true, "Duplicate saved actor");
        state.AllEntityData.RemoveAt(state.AllEntityData.Count - 1);
        registry[actorId] = spawner;
        Expect(false, true, "Registry collision");
        registry[actorId] = actor;
        var other = Spawner("another-spawner");
        Reference(other, actorId);
        state.AllEntityData.Add(other);
        Expect(false, true, "Another saved spawner claims actor");
        state.AllEntityData.Remove(other);
        states = new[] { state, new SceneEntitiesState(state.SceneName) };
        Expect(false, true, "Duplicate native source states");
        states = new[] { state };
        Expect(true, false, "Restored valid observation");
        var persistent = (PersistentState)FormatterServices.GetUninitializedObject(typeof(PersistentState));
        var savedAreas = new List<AreaPersistentState>();
        Set(persistent, typeof(PersistentState), "SavedAreaStates", savedAreas);
        var savedArea = new AreaPersistentState(BlueprintGuid.Parse(Read("Area")));
        savedArea.GetAdditionalSceneStates().Add(state);
        savedAreas.Add(savedArea);
        var savedMethod = service.GetMethod("InspectSaved", BindingFlags.Static | BindingFlags.NonPublic)!;
        void Saved(bool invalidated, string reason)
        {
            var result = savedMethod.Invoke(null, new object[] { persistent,
                new Func<string, EntityDataBase?>(id => registry.TryGetValue(id, out var entity) ? entity : null) })!;
            check(!(bool)result.GetType().GetField("Available", instance)!.GetValue(result)!, reason + ": saved-only never grants contact");
            check((bool)result.GetType().GetField("Invalidated", instance)!.GetValue(result)! == invalidated, reason);
        }
        // Actual native saved-area constructor and enumerator, with no loaded area or registered actors.
        registry.Clear();
        Saved(false, "Unloaded living saved actor preserves earned correspondence");
        Set(life, typeof(UnitState), "<LifeState>k__BackingField", UnitLifeState.Dead);
        Saved(true, "Leaving capital does not hide retained death");
        Set(life, typeof(UnitState), "<LifeState>k__BackingField", UnitLifeState.Conscious);
        spawner.HasDied = true;
        state.AllEntityData.Remove(actor);
        Saved(true, "Off-area recorded death survives missing actor and empty registry");
        spawner.HasDied = false;
        Saved(false, "Off-area missing actor is unknown");
        state.AllEntityData.Add(actor);
        Set(actor, typeof(EntityDataBase), "<DestroyMark>k__BackingField", true);
        Saved(true, "Off-area saved destruction");
        Set(actor, typeof(EntityDataBase), "<DestroyMark>k__BackingField", false);
        registry[actorId] = spawner;
        Saved(true, "Off-area registry identity conflict");
        registry.Clear();
        savedAreas.Add(new AreaPersistentState(BlueprintGuid.Parse(Read("Area"))));
        Saved(true, "Duplicate saved native areas");
        savedAreas.RemoveAt(1);
        persistent.LoadedAreaState = savedArea;
        Saved(false, "Same loaded and saved area reference is not a duplicate");
        savedAreas.Clear();
        persistent.LoadedAreaState = null;
        Saved(false, "No saved source is unknown");
        registry[spawner.UniqueId] = spawner;
        registry[actorId] = actor;
        check(spawner.HasSpawned && !spawner.HasDied && spawner.SpawnedUnit.UniqueId == actorId
            && ReferenceEquals(actor.HoldingState, state) && state.AllEntityData.Count == 2
            && ReferenceEquals(registry[actorId], actor), "Read-only observation mutated native saved state");
    }
}
