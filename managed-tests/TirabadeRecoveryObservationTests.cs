using System;
using System.Collections.Generic;
using System.Reflection;
using System.Linq;
using System.Runtime.Serialization;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.View.Spawners;
using Kingmaker.Blueprints;
using Kingmaker.UnitLogic;

internal static class TirabadeRecoveryObservationTests
{
    internal static void Run(Action<bool, string> check)
    {
        const BindingFlags instance = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
        var service = typeof(Tirabade.Main).Assembly.GetType("Tirabade.TirabadeRecoveryObserver", true)!;
        var sources = (Array)service.GetField("sources", BindingFlags.NonPublic | BindingFlags.Static)!.GetValue(null)!;
        var inspect = service.GetMethod("Inspect", BindingFlags.NonPublic | BindingFlags.Static)!;
        check(sources.Length == 5, "Observer must retain both capital actors and all three Iz alternatives.");
        foreach (object source in sources)
        {
            string Read(string key) => (string)source.GetType().GetField(key, instance)!.GetValue(source)!;
            var state = new SceneEntitiesState(Read("Scene"));
            var registry = new Dictionary<string, EntityDataBase>();
            bool loaded = true;
            string area = Read("Area");
            var states = new[] { state };
            Array ObserveAll() => (Array)inspect.Invoke(null, new object[] { area, states,
                new Func<SceneEntitiesState, bool>(_ => loaded),
                new Func<string, EntityDataBase?>(id => registry.TryGetValue(id, out var entity) ? entity : null) })!;
            object Observe() => ObserveAll().Cast<object>().Single(result => ReferenceEquals(
                result.GetType().GetField("Source", instance)!.GetValue(result), source));
            string Kind() { var result = Observe(); return result.GetType().GetField("Kind", instance)!.GetValue(result)!.ToString()!; }
            check(Kind() == "Unresolved", "Missing loaded spawner became a death/survival claim.");
            loaded = false;
            check(Kind() == "NotLoaded", "Unloaded source was inspected as a living encounter.");
            loaded = true;
            area = "unrelated";
            check(Kind() == "NotLoaded", "Wrong area accepted by matching scene name.");
            area = Read("Area");
            var data = (UnitSpawnerBase.MyData)FormatterServices.GetUninitializedObject(typeof(UnitSpawnerBase.MyData));
            typeof(EntityDataBase).GetField("<UniqueId>k__BackingField", instance)!.SetValue(data, Read("Spawner"));
            typeof(EntityDataBase).GetField("<HoldingState>k__BackingField", instance)!.SetValue(data, state);
            state.AllEntityData.Add(data);
            registry.Add(data.UniqueId, data);
            check(Kind() == "NotSpawned", "Unspawned native data is not distinguished.");
            data.HasDied = true;
            check(Kind() == "Conflict", "Death with no recorded spawn is accepted as provenance.");
            data.HasDied = false;
            data.HasSpawned = true;
            check(Kind() == "Unresolved", "Missing saved actor ID became permission to create one.");
            // Set the actual saved field without invoking OnSpawn or creating a native proxy.
            object reference = default(UnitReference);
            const string actorId = "9f358ce1-94ad-433a-bfda-e04c7c190abb";
            typeof(UnitReference).GetField("m_UniqueId", instance)!.SetValue(reference, actorId);
            typeof(UnitSpawnerBase.MyData).GetField("m_SpawnedUnit", instance)!.SetValue(data, reference);
            check(data.SpawnedUnit.UniqueId == actorId, "Actual native UnitReference did not retain the saved identity.");
            check(Kind() == "Unresolved", "Missing actor with no death proof was classified as alive or dead.");
            data.HasDied = true;
            check(Kind() == "RecordedDeadMissingActor", "Saved native death with unresolved identity was lost.");
            var observed = Observe();
            check((string)observed.GetType().GetField("ActorId", instance)!.GetValue(observed)! == actorId,
                "Observer substituted the spawner ID for the saved actor ID.");
            registry[actorId] = data;
            check(Kind() == "Conflict", "Wrong registry type accepted as a Tirabade actor.");
            // Real game classes and property getters; only construction is bypassed because it requires Unity.
            var actor = (UnitEntityData)FormatterServices.GetUninitializedObject(typeof(UnitEntityData));
            var descriptor = (UnitDescriptor)FormatterServices.GetUninitializedObject(typeof(UnitDescriptor));
            var life = (UnitState)FormatterServices.GetUninitializedObject(typeof(UnitState));
            var blueprint = new BlueprintUnit { AssetGuid = BlueprintGuid.Parse(Read("Blueprint")) };
            typeof(UnitEntityData).GetField("<Descriptor>k__BackingField", instance)!.SetValue(actor, descriptor);
            typeof(UnitDescriptor).GetField("<Blueprint>k__BackingField", instance)!.SetValue(descriptor, blueprint);
            typeof(UnitDescriptor).GetField("<Unit>k__BackingField", instance)!.SetValue(descriptor, actor);
            typeof(UnitDescriptor).GetField("State", instance)!.SetValue(descriptor, life);
            typeof(EntityDataBase).GetField("<UniqueId>k__BackingField", instance)!.SetValue(actor, actorId);
            typeof(EntityDataBase).GetField("<HoldingState>k__BackingField", instance)!.SetValue(actor, state);
            var lifeField = typeof(UnitState).GetField("<LifeState>k__BackingField", instance)!;
            lifeField.SetValue(life, UnitLifeState.Conscious);
            registry[actorId] = actor;
            state.AllEntityData.Add(actor);
            check(Kind() == "RetainedAlive", "Real retained living actor was not observed, or old HasDied overrode current life.");
            check(actor.View == null, "Fixture must not pretend it has a Unity view.");
            foreach (object result in ObserveAll())
            {
                var resultSource = result.GetType().GetField("Source", instance)!.GetValue(result)!;
                string resultArea = (string)resultSource.GetType().GetField("Area", instance)!.GetValue(resultSource)!;
                if (resultArea != area)
                    check(result.GetType().GetField("Kind", instance)!.GetValue(result)!.ToString() == "NotLoaded",
                        "A loaded capital representation fabricated evidence about the unloaded Iz actor, or vice versa.");
            }
            var alternate = sources.Cast<object>().First(item => !ReferenceEquals(item, source)
                && (string)item.GetType().GetField("Area", instance)!.GetValue(item)! == area);
            var duplicate = (UnitSpawnerBase.MyData)FormatterServices.GetUninitializedObject(typeof(UnitSpawnerBase.MyData));
            typeof(EntityDataBase).GetField("<UniqueId>k__BackingField", instance)!.SetValue(duplicate,
                (string)alternate.GetType().GetField("Spawner", instance)!.GetValue(alternate)!);
            typeof(EntityDataBase).GetField("<HoldingState>k__BackingField", instance)!.SetValue(duplicate, state);
            duplicate.HasSpawned = true;
            typeof(UnitSpawnerBase.MyData).GetField("m_SpawnedUnit", instance)!.SetValue(duplicate, reference);
            registry.Add(duplicate.UniqueId, duplicate);
            state.AllEntityData.Add(duplicate);
            check(Kind() == "Conflict", "Two source spawners claiming one saved actor were silently accepted.");
            var alternatives = ObserveAll().Cast<object>().Where(result => {
                var from = result.GetType().GetField("Source", instance)!.GetValue(result);
                return ReferenceEquals(from, source) || ReferenceEquals(from, alternate);
            }).ToArray();
            check(alternatives.All(result => result.GetType().GetField("Kind", instance)!.GetValue(result)!.ToString() == "Conflict"),
                "Cross-source ambiguity only marked one claimant.");
            state.AllEntityData.Remove(duplicate);
            registry.Remove(duplicate.UniqueId);
            check(Kind() == "RetainedAlive", "Removing conflicting fixture did not restore exact observation.");
            if (area == "2ccc6731787b6ec41ab5adc13f1b9ce9")
            {
                const string secondId = "7b8ca279-bb59-44fb-a04e-842c40b02b65";
                var second = (UnitEntityData)FormatterServices.GetUninitializedObject(typeof(UnitEntityData));
                var secondDescriptor = (UnitDescriptor)FormatterServices.GetUninitializedObject(typeof(UnitDescriptor));
                var secondLife = (UnitState)FormatterServices.GetUninitializedObject(typeof(UnitState));
                typeof(UnitEntityData).GetField("<Descriptor>k__BackingField", instance)!.SetValue(second, secondDescriptor);
                typeof(UnitDescriptor).GetField("<Blueprint>k__BackingField", instance)!.SetValue(secondDescriptor, blueprint);
                typeof(UnitDescriptor).GetField("<Unit>k__BackingField", instance)!.SetValue(secondDescriptor, second);
                typeof(UnitDescriptor).GetField("State", instance)!.SetValue(secondDescriptor, secondLife);
                typeof(EntityDataBase).GetField("<UniqueId>k__BackingField", instance)!.SetValue(second, secondId);
                typeof(EntityDataBase).GetField("<HoldingState>k__BackingField", instance)!.SetValue(second, state);
                lifeField.SetValue(secondLife, UnitLifeState.Dead);
                object secondReference = default(UnitReference);
                typeof(UnitReference).GetField("m_UniqueId", instance)!.SetValue(secondReference, secondId);
                typeof(UnitSpawnerBase.MyData).GetField("m_SpawnedUnit", instance)!.SetValue(duplicate, secondReference);
                duplicate.HasDied = true;
                registry.Add(duplicate.UniqueId, duplicate);
                registry.Add(secondId, second);
                state.AllEntityData.Add(duplicate);
                state.AllEntityData.Add(second);
                var all = ObserveAll().Cast<object>().ToArray();
                var corpse = all.Single(result => ReferenceEquals(result.GetType().GetField("Source", instance)!.GetValue(result), alternate));
                check(Kind() == "RetainedAlive"
                    && corpse.GetType().GetField("Kind", instance)!.GetValue(corpse)!.ToString() == "RetainedDead"
                    && (string)corpse.GetType().GetField("ActorId", instance)!.GetValue(corpse)! == secondId,
                    "Alternative living and dead Iz representations were collapsed into one survival claim.");
                check(all.Length == 5, "Alternative reference removed an unresolved source from the report.");
                state.AllEntityData.Remove(second);
                state.AllEntityData.Remove(duplicate);
                registry.Remove(secondId);
                registry.Remove(duplicate.UniqueId);
            }

            lifeField.SetValue(life, UnitLifeState.Unconscious);
            check(Kind() == "RetainedAlive", "Unconscious actor was falsely reported dead.");
            lifeField.SetValue(life, UnitLifeState.Dead);
            check(Kind() == "RetainedDead", "Actual native dead life state was ignored.");
            lifeField.SetValue(life, UnitLifeState.Conscious);
            typeof(UnitState).GetField("<IsFinallyDead>k__BackingField", instance)!.SetValue(life, true);
            check(Kind() == "RetainedDead", "Finally-dead actor was reported living.");
            typeof(UnitState).GetField("<IsFinallyDead>k__BackingField", instance)!.SetValue(life, false);
            typeof(EntityDataBase).GetField("<DestroyMark>k__BackingField", instance)!.SetValue(actor, true);
            check(Kind() == "Unresolved", "Actor being destroyed was adopted as retained.");
            typeof(EntityDataBase).GetField("<DestroyMark>k__BackingField", instance)!.SetValue(actor, false);
            blueprint.AssetGuid = BlueprintGuid.Parse("64805abb52739e44280a758f850b300c");
            check(Kind() == "Conflict", "Another character under the saved actor ID was accepted.");
            blueprint.AssetGuid = BlueprintGuid.Parse(Read("Blueprint"));
            state.AllEntityData.Add(actor);
            check(Kind() == "Conflict", "Duplicate retained actor storage accepted.");
            state.AllEntityData.RemoveAt(state.AllEntityData.Count - 1);
            typeof(EntityDataBase).GetField("<HoldingState>k__BackingField", instance)!.SetValue(actor, new SceneEntitiesState("elsewhere"));
            check(Kind() == "Conflict", "Stale source entry overrode actual actor holding state.");
            state.AllEntityData.Remove(actor);
            registry.Remove(actorId);
            state.AllEntityData.Add(data);
            check(Kind() == "Conflict", "Duplicate spawner storage accepted.");
            state.AllEntityData.RemoveAt(state.AllEntityData.Count - 1);
            registry.Remove(data.UniqueId);
            check(Kind() == "Conflict", "Spawner storage without matching registry accepted.");
            registry[data.UniqueId] = data;
            states = new[] { state, new SceneEntitiesState(state.SceneName) };
            check(Kind() == "Conflict", "Duplicate source scene state accepted.");
            states = new[] { state };
            check(data.HasSpawned && data.HasDied && data.SpawnedUnit.UniqueId == actorId
                && ReferenceEquals(data.HoldingState, state) && state.AllEntityData.Count == 1,
                "Read-only observation changed saved native data.");
        }
    }
}
