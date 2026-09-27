using System;
using System.Collections.Generic;
using System.Collections;
using System.Reflection;
using System.Runtime.Serialization;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.EntitySystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic;
using Kingmaker.View.Spawners;

internal static class NurahMeetingTests
{
    private const BindingFlags Members = BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;
    private static void Set(object value, string name, object data)
    {
        for (Type? type = value.GetType(); type != null; type = type.BaseType)
        {
            var field = type.GetField(name, Members | BindingFlags.DeclaredOnly);
            if (field == null) continue;
            field.SetValue(value, data); return;
        }
        throw new Exception("Missing native fixture field: " + name);
    }
    private static T Bare<T>() => (T)FormatterServices.GetUninitializedObject(typeof(T));

    internal static void Run(Action<bool, string> check)
    {
        var service = typeof(Tirabade.Main).Assembly.GetType("Tirabade.NurahMeeting", true)!;
        string Constant(string name) => (string)service.GetField(name, Members)!.GetRawConstantValue()!;
        SimpleBlueprint Resolve(string id) => id == Constant("Finale")
            ? (SimpleBlueprint)new BlueprintCue { AssetGuid = BlueprintGuid.Parse(id) }
            : new BlueprintEtude { AssetGuid = BlueprintGuid.Parse(id) };
        var observer = Activator.CreateInstance(service, Members, null,
            new object[] { new Func<string, SimpleBlueprint>(Resolve) }, null);
        check(observer != null, "Verified typed parent bindings did not construct observer");
        bool rejected = false;
        try { Activator.CreateInstance(service, Members, null, new object[] {
            new Func<string, SimpleBlueprint>(id => new BlueprintEtude { AssetGuid = BlueprintGuid.Parse(Constant("Romance")) }) }, null); }
        catch (TargetInvocationException error) { rejected = error.InnerException is InvalidOperationException; }
        check(rejected, "Resolver aliases were accepted as independent native bindings");
        var state = new SceneEntitiesState("DrezenCapital_Default_Mechanics");
        var states = new[] { state };
        var registry = new Dictionary<string, EntityDataBase>();
        bool loaded = true;
        string area = Constant("Capital");
        UnitEntityData? Inspect() => (UnitEntityData?)service.GetMethod("Inspect", Members)!.Invoke(null, new object[] {
            area, states, new Func<SceneEntitiesState, bool>(_ => loaded),
            new Func<string, EntityDataBase?>(id => registry.TryGetValue(id, out var value) ? value : null) });
        var spawner = Bare<UnitSpawnerBase.MyData>();
        Set(spawner, "<UniqueId>k__BackingField", Constant("Spawner"));
        Set(spawner, "<HoldingState>k__BackingField", state);
        state.AllEntityData.Add(spawner); registry[spawner.UniqueId] = spawner;
        check(Inspect() == null, "Never-spawned Nurah became correspondence evidence");
        spawner.HasSpawned = true;
        object reference = default(UnitReference);
        Set(reference, "m_UniqueId", "original-nurah");
        Set(spawner, "m_SpawnedUnit", reference);
        check(Inspect() == null, "Missing retained actor became correspondence evidence");
        UnitEntityData Unit(string id)
        {
            var actor = Bare<UnitEntityData>(); var descriptor = Bare<UnitDescriptor>(); var life = Bare<UnitState>();
            Set(actor, "<UniqueId>k__BackingField", id); Set(actor, "<HoldingState>k__BackingField", state);
            Set(actor, "<Descriptor>k__BackingField", descriptor); Set(descriptor, "<Unit>k__BackingField", actor);
            Set(descriptor, "<Blueprint>k__BackingField", new BlueprintUnit { AssetGuid = BlueprintGuid.Parse(Constant("Unit")) });
            Set(descriptor, "State", life); Set(life, "<LifeState>k__BackingField", UnitLifeState.Conscious);
            return actor;
        }
        var actor = Unit("original-nurah");
        state.AllEntityData.Add(actor); registry[actor.UniqueId] = actor;
        check(ReferenceEquals(Inspect(), actor), "Exact retained living actor was rejected");
        check(actor.View == null, "Fixture unexpectedly provided a physical Unity view");
        loaded = false; check(Inspect() == null, "Unloaded source granted access"); loaded = true;
        area = "wrong-area"; check(Inspect() == null, "Wrong area granted access"); area = Constant("Capital");
        spawner.HasDied = true; check(Inspect() == null, "Historical death silently became an authorized revival"); spawner.HasDied = false;
        Set(actor.State, "<LifeState>k__BackingField", UnitLifeState.Dead);
        check(Inspect() == null, "Current dead actor granted access"); Set(actor.State, "<LifeState>k__BackingField", UnitLifeState.Conscious);
        Set(actor.State, "<IsFinallyDead>k__BackingField", true);
        check(Inspect() == null, "Finally dead actor granted access"); Set(actor.State, "<IsFinallyDead>k__BackingField", false);
        Set(actor, "<DestroyMark>k__BackingField", true);
        check(Inspect() == null, "Removed actor granted access"); Set(actor, "<DestroyMark>k__BackingField", false);
        Set(spawner, "<DestroyMark>k__BackingField", true);
        check(Inspect() == null, "Removed spawner granted access"); Set(spawner, "<DestroyMark>k__BackingField", false);
        var duplicate = Unit("duplicate-nurah"); state.AllEntityData.Add(duplicate);
        check(Inspect() == null, "Second capital Nurah was silently ignored"); state.AllEntityData.Remove(duplicate);
        var secondSource = Bare<UnitSpawnerBase.MyData>(); Set(secondSource, "<UniqueId>k__BackingField", "second-source");
        Set(secondSource, "m_SpawnedUnit", reference); state.AllEntityData.Add(secondSource);
        check(Inspect() == null, "Ambiguous spawner provenance was accepted"); state.AllEntityData.Remove(secondSource);
        registry[actor.UniqueId] = duplicate;
        check(Inspect() == null, "Registry replacement was accepted"); registry[actor.UniqueId] = actor;
        states = new[] { state, state };
        check(Inspect() == null, "Duplicate source scene was accepted"); states = new[] { state };
        Set(actor.Descriptor, "<Blueprint>k__BackingField", new BlueprintUnit { AssetGuid = BlueprintGuid.Parse("c44d5c157091e7e46af1f11a4c79303d") });
        check(Inspect() == null, "War-camp representation substituted for capital actor");
        Set(actor.Descriptor, "<Blueprint>k__BackingField", new BlueprintUnit { AssetGuid = BlueprintGuid.Parse(Constant("Unit")) });
        check(ReferenceEquals(Inspect(), actor), "Rejected evidence mutated retained actor or source");

        Etude Playing() { var fact = Bare<Etude>(); Set(fact, "<IsActive>k__BackingField", true); return fact; }
        var romance = Playing(); var personality = Playing(); var personalities = new Etude?[] { personality, null, null };
        bool jailed = false, dead = false, seen = true;
        bool History() => (bool)service.GetMethod("HistoryPermits", Members)!.Invoke(null,
            new object?[] { romance, jailed, dead, personalities, seen })!;
        check(History(), "Accepted active parent romance with one personality was rejected");
        seen = false; check(!History(), "Romance alone substituted for accepted Book5 terminal"); seen = true;
        jailed = true; check(!History(), "Current imprisonment granted a free visit"); jailed = false;
        dead = true; check(!History(), "Recorded native death granted a visit"); dead = false;
        Set(romance, "m_IsCompleted", true); check(!History(), "Completed romance substituted for current relationship"); Set(romance, "m_IsCompleted", false);
        Set(romance, "m_CompletionInProgress", true); check(!History(), "Closing romance granted access"); Set(romance, "m_CompletionInProgress", false);
        Set(romance, "<IsActive>k__BackingField", false); check(!History(), "Dormant romance granted access"); Set(romance, "<IsActive>k__BackingField", true);
        personalities[1] = Playing(); check(!History(), "Conflicting personalities silently chose priority"); personalities[1] = null;
        personalities[0] = null; check(!History(), "Missing personality was accepted"); personalities[2] = personality;
        check(History(), "Alternate current personality was rejected");
        Set(personality, "m_CompletionInProgress", true); check(!History(), "Transitioning personality granted access");

        // Reproduce the native completion interval at the actual dictionary/fact adapter.
        var system = Bare<EtudesSystem>();
        var manager = new EntityFactsManager(system);
        Set(system, "Facts", manager);
        var tree = manager.EnsureFactProcessor<EtudesTree>();
        Set(system, "<Etudes>k__BackingField", tree);
        var savedField = typeof(EtudesSystem).GetField("m_EtudesData", Members)!;
        var saved = (IDictionary)Activator.CreateInstance(savedField.FieldType)!;
        var nativeStateType = savedField.FieldType.GetGenericArguments()[1];
        var nativePrison = new BlueprintEtude { AssetGuid = BlueprintGuid.Parse(Constant("Prison")) };
        saved.Add(nativePrison, Enum.Parse(nativeStateType, "Completed")); savedField.SetValue(system, saved);
        var prisonFact = Playing(); Set(prisonFact, "<Blueprint>k__BackingField", nativePrison);
        Set(prisonFact, "m_CompletionInProgress", true);
        var raw = (IList)typeof(EntityFactsManager).GetField("m_Facts", Members)!.GetValue(manager)!;
        raw.Add(prisonFact);
        check(ReferenceEquals(tree.GetFact(nativePrison), prisonFact), "Prison fixture did not reach actual native fact lookup");
        check(system.EtudeIsCompleted(nativePrison) && !system.EtudeIsStarted(nativePrison)
            && prisonFact.IsPlaying && prisonFact.CompletionInProgress && !prisonFact.IsCompleted,
            "Fixture did not reproduce native early-published completion");
        bool PrisonBlocks() => (bool)service.GetMethod("PrisonBlocks", Members)!.Invoke(null, new object[] { system, nativePrison })!;
        check(PrisonBlocks(), "Completed dictionary bypassed a playing/completing prison fact");
        Set(prisonFact, "<IsActive>k__BackingField", false);
        check(PrisonBlocks(), "Deactivated but still-completing prison granted release");
        Set(prisonFact, "m_CompletionInProgress", false);
        check(PrisonBlocks(), "Unfinished dormant prison fact granted release");
        Set(prisonFact, "m_IsCompleted", true);
        check(!PrisonBlocks(), "Fully finished historical imprisonment blocked released Nurah");
        Set(prisonFact, "<IsActive>k__BackingField", true);
        check(PrisonBlocks(), "Completed but still-playing prison fact granted release");
        Set(prisonFact, "<IsActive>k__BackingField", false);
        saved[nativePrison] = Enum.Parse(nativeStateType, "Started");
        check(PrisonBlocks(), "Started native prison history bypassed confinement");
        manager = new EntityFactsManager(system);
        Set(system, "Facts", manager);
        tree = manager.EnsureFactProcessor<EtudesTree>();
        Set(system, "<Etudes>k__BackingField", tree);
        check(tree.GetFact(nativePrison) == null && PrisonBlocks(), "Pending recorded prison without a live fact was ignored");
        saved[nativePrison] = Enum.Parse(nativeStateType, "Completed");
        check(!PrisonBlocks(), "Completed history without a retained prison fact blocked release");
        saved.Clear();
        check(!PrisonBlocks(), "Never-imprisoned native history was incorrectly treated as confinement");

    }
}
