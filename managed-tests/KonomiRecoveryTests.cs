using System;
using System.Collections.Generic;
using System.Reflection;
using System.Runtime.Serialization;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic;
using Kingmaker.View.Spawners;
using Newtonsoft.Json;

internal static class KonomiRecoveryTests
{
    internal static void Run(Action<bool, string> check)
    {
        const BindingFlags instance = BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance;
        const BindingFlags statics = BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static;
        var service = typeof(Tirabade.Main).Assembly.GetType("Tirabade.KonomiRecovery", true)!;
        var attemptType = service.GetNestedType("Attempt", BindingFlags.NonPublic)!;
        var source = service.GetField("source", statics)!.GetValue(null)!;
        string Read(string key) => (string)source.GetType().GetField(key, instance)!.GetValue(source)!;
        void Set(object value, Type type, string field, object data) => type.GetField(field, instance)!.SetValue(value, data);
        var state = new SceneEntitiesState(Read("Scene"));
        var states = new[] { state };
        var registry = new Dictionary<string, EntityDataBase>();
        bool loaded = true;
        string area = Read("Area");
        UnitEntityData? Inspect() => (UnitEntityData?)service.GetMethod("Inspect", statics)!.Invoke(null, new object[] {
            area, states, new Func<SceneEntitiesState, bool>(_ => loaded),
            new Func<string, EntityDataBase?>(id => registry.TryGetValue(id, out var value) ? value : null) });
        var spawner = (UnitSpawnerBase.MyData)FormatterServices.GetUninitializedObject(typeof(UnitSpawnerBase.MyData));
        Set(spawner, typeof(EntityDataBase), "<UniqueId>k__BackingField", Read("Spawner"));
        Set(spawner, typeof(EntityDataBase), "<HoldingState>k__BackingField", state);
        state.AllEntityData.Add(spawner);
        registry[spawner.UniqueId] = spawner;
        check(Inspect() == null, "Never-spawned Konomi became a recoverable body");
        spawner.HasSpawned = true;
        spawner.HasDied = true;
        const string actorId = "c8e716c2-7efd-4b4a-b4c3-91ab60dfc8dd";
        object reference = default(UnitReference);
        Set(reference, typeof(UnitReference), "m_UniqueId", actorId);
        Set(spawner, typeof(UnitSpawnerBase.MyData), "m_SpawnedUnit", reference);
        check(Inspect() == null, "Recorded death without retained body became recoverable");
        UnitEntityData Unit(string id, UnitLifeState status)
        {
            var unit = (UnitEntityData)FormatterServices.GetUninitializedObject(typeof(UnitEntityData));
            var descriptor = (UnitDescriptor)FormatterServices.GetUninitializedObject(typeof(UnitDescriptor));
            var life = (UnitState)FormatterServices.GetUninitializedObject(typeof(UnitState));
            Set(unit, typeof(EntityDataBase), "<UniqueId>k__BackingField", id);
            Set(unit, typeof(EntityDataBase), "<HoldingState>k__BackingField", state);
            Set(unit, typeof(UnitEntityData), "<Descriptor>k__BackingField", descriptor);
            Set(descriptor, typeof(UnitDescriptor), "<Unit>k__BackingField", unit);
            Set(descriptor, typeof(UnitDescriptor), "<Blueprint>k__BackingField", new BlueprintUnit { AssetGuid = BlueprintGuid.Parse(Read("Blueprint")) });
            Set(descriptor, typeof(UnitDescriptor), "State", life);
            Set(life, typeof(UnitState), "<LifeState>k__BackingField", status);
            return unit;
        }
        var actor = Unit(actorId, UnitLifeState.Dead);
        var commander = Unit("commander-fixture", UnitLifeState.Conscious);
        Set(actor.State, typeof(UnitState), "<IsFinallyDead>k__BackingField", true);
        state.AllEntityData.Add(actor);
        registry[actorId] = actor;
        check(ReferenceEquals(Inspect(), actor), "Actual retained original dead Konomi not identified");
        loaded = false;
        check(Inspect() == null, "Unloaded native body accepted for mutation");
        loaded = true;
        area = "other-area";
        check(Inspect() == null, "Native recovery accepted wrong source area");
        area = Read("Area");
        Set(actor, typeof(EntityDataBase), "<DestroyMark>k__BackingField", true);
        check(Inspect() == null, "Destroyed body accepted for resurrection");
        Set(actor, typeof(EntityDataBase), "<DestroyMark>k__BackingField", false);
        var duplicate = Unit("duplicate", UnitLifeState.Conscious);
        state.AllEntityData.Add(duplicate);
        check(Inspect() == null, "Second Konomi representation was silently ignored");
        state.AllEntityData.Remove(duplicate);

        object Attempt()
        {
            var value = Activator.CreateInstance(attemptType)!;
            Set(value, attemptType, "Request", "konomi.recovery-fixture/explicit-choice");
            Set(value, attemptType, "UnitId", actorId);
            return value;
        }
        object attempt = Attempt();
        string? checkpoint = null;
        int writes = 0;
        bool failWrite = false;
        void Save(object value)
        {
            writes++;
            if (failWrite) throw new InvalidOperationException("Deliberate checkpoint failure");
            checkpoint = JsonConvert.SerializeObject(value);
        }
        string Apply(bool invoke)
        {
            var args = new object[] { attempt, actor, commander, new Func<UnitEntityData?>(Inspect), new Action<object>(Save), invoke, "" };
            return service.GetMethod("Apply", statics)!.Invoke(null, args)!.ToString()!;
        }
        failWrite = true;
        check(Apply(true) == "Pending" && actor.State.IsFinallyDead && checkpoint == null,
            "Failed persistence dispatched native resurrection");
        failWrite = false;
        writes = 0;
        // This calls the real installed ResurrectAndFullRestore. No substituted resurrection delegate exists.
        check(Apply(true) == "Pending", "Incomplete native fixture was credited as a successful resurrection");
        check(writes == 1 && checkpoint != null && !checkpoint.Contains("\"Confirmed\":true"), "Native action preceded checkpoint or credited partial success");
        var error = (Exception?)service.GetProperty("LastError", statics)!.GetValue(null);
        check(error != null, "Actual native failure was silently discarded");
        Console.WriteLine("Native resurrection fixture boundary: " + error!.GetType().FullName + ": " + error.Message);
        Console.WriteLine(error.StackTrace);
        check(error is System.Security.SecurityException && actor.State.IsFinallyDead && actor.State.IsDead,
            "Installed Unity ECall boundary or unchanged dead state differs from the audited fixture");
        check(spawner.HasDied && spawner.HasSpawned && spawner.SpawnedUnit.UniqueId == actorId,
            "Recovery erased native death/spawn history");
        // Native life completion is not simulated as proof of the API. These are controlled post-observation cases.
        attempt = JsonConvert.DeserializeObject(checkpoint!, attemptType)!;
        Set(actor.State, typeof(UnitState), "<IsFinallyDead>k__BackingField", true);
        writes = 0;
        check(Apply(false) == "Pending" && actor.State.IsFinallyDead && writes == 0, "Poll dispatched resurrection");
        Set(actor.State, typeof(UnitState), "<IsFinallyDead>k__BackingField", false);
        Set(actor.State, typeof(UnitState), "<LifeState>k__BackingField", UnitLifeState.Unconscious);
        check(Apply(true) == "Pending" && writes == 0, "Living unconscious actor was resurrected or credited");
        Set(actor.State, typeof(UnitState), "<LifeState>k__BackingField", UnitLifeState.Conscious);
        failWrite = true;
        check(Apply(false) == "Pending" && !(bool)attemptType.GetField("Confirmed", instance)!.GetValue(attempt)!,
            "Failed confirmation write mutated the pending object");
        failWrite = false;
        check(Apply(false) == "Confirmed", "Exact observed living original actor cannot finish pending recovery");
        attempt = JsonConvert.DeserializeObject(checkpoint!, attemptType)!;
        writes = 0;
        check(Apply(true) == "Confirmed" && writes == 0, "Repeated request replayed mutation or rewrote confirmed checkpoint");
        Set(actor.State, typeof(UnitState), "<LifeState>k__BackingField", UnitLifeState.Unconscious);
        check(Apply(false) == "Pending" && writes == 0, "Confirmed history alone satisfied current conscious-return confirmation");
        Set(actor.State, typeof(UnitState), "<LifeState>k__BackingField", UnitLifeState.Dead);
        Set(actor.State, typeof(UnitState), "<IsFinallyDead>k__BackingField", true);
        check(Apply(true) == "Blocked" && actor.State.IsFinallyDead && writes == 0, "Old proof resurrected a new death");
        attempt = Attempt();
        Set(attempt, attemptType, "UnitId", "wrong-actor");
        check(Apply(true) == "Blocked" && actor.State.IsFinallyDead, "Saved identity mismatch dispatched native mutation");
        attempt = Attempt();
        registry[actorId] = spawner;
        check(Apply(true) == "Blocked" && actor.State.IsFinallyDead, "Registry conflict dispatched native mutation");
        registry[actorId] = actor;
        // Exercise real native Player.SettingsList storage and restore the process-global Game instance afterward.
        var gameField = typeof(Game).GetField("s_Instance", statics)!;
        var oldGame = gameField.GetValue(null);
        try
        {
            var game = (Game)FormatterServices.GetUninitializedObject(typeof(Game));
            var persistent = (PersistentState)FormatterServices.GetUninitializedObject(typeof(PersistentState));
            var player = (Player)FormatterServices.GetUninitializedObject(typeof(Player));
            player.SettingsList = new Dictionary<string, object> { ["unrelated.native.history"] = "preserve" };
            Set(persistent, typeof(PersistentState), "PlayerState", player);
            Set(game, typeof(Game), "State", persistent);
            gameField.SetValue(null, game);
            var requestArgs = new object[] { "explicit-choice", false, "" };
            check(service.GetMethod("Request", statics)!.Invoke(null, requestArgs)!.ToString() == "Blocked"
                && player.SettingsList.Count == 1, "Unauthorized request created recovery state");
            var pollArgs = new object[] { true, "" };
            check(service.GetMethod("Poll", statics)!.Invoke(null, pollArgs)!.ToString() == "NotRequested",
                "Polling invented an authored recovery request");
            attempt = Attempt();
            Set(attempt, attemptType, "Confirmed", true);
            service.GetMethod("Save", statics)!.Invoke(null, new[] { attempt });
            const string key = "RanRomance.Tirabade.KonomiRecovery";
            check(player.SettingsList[key] is string, "Recovery checkpoint is not saved as a native SettingsList JSON string");
            bool Proof() => (bool)service.GetMethod("HasVerifiedReturn", statics)!.Invoke(null, new object[] { actor })!;
            check(!Proof(), "Confirmed old proof authorized a currently dead actor");
            Set(actor.State, typeof(UnitState), "<LifeState>k__BackingField", UnitLifeState.Conscious);
            Set(actor.State, typeof(UnitState), "<IsFinallyDead>k__BackingField", false);
            check(Proof() && spawner.HasDied, "Verified same-actor life requires erasing native HasDied history");
            Set(actor.State, typeof(UnitState), "<LifeState>k__BackingField", UnitLifeState.Unconscious);
            check(Proof(), "Temporary unconsciousness erased confirmed historical return");
            Set(attempt, attemptType, "Confirmed", false);
            service.GetMethod("Save", statics)!.Invoke(null, new[] { attempt });
            check(!Proof(), "Pending unconscious actor acquired historical return proof");
            Set(attempt, attemptType, "Confirmed", true);
            service.GetMethod("Save", statics)!.Invoke(null, new[] { attempt });
            Set(actor.State, typeof(UnitState), "<LifeState>k__BackingField", UnitLifeState.Conscious);
            Set(actor, typeof(EntityDataBase), "<DestroyMark>k__BackingField", true);
            check(!Proof(), "Verified proof authorizes a destroyed body");
            Set(actor, typeof(EntityDataBase), "<DestroyMark>k__BackingField", false);
            Set(attempt, attemptType, "UnitId", "another-actor");
            service.GetMethod("Save", statics)!.Invoke(null, new[] { attempt });
            check(!Proof(), "Recovery proof transfers to a different saved identity");
            player.SettingsList[key] = "invalid json";
            check(!Proof(), "Malformed recovery proof grants observer eligibility");
            check((string)player.SettingsList["unrelated.native.history"] == "preserve", "Recovery changed unrelated saved history");
        }
        finally { gameField.SetValue(null, oldGame); }
        check(spawner.HasDied && spawner.SpawnedUnit.UniqueId == actorId && state.AllEntityData.Count == 2,
            "Recovery substituted a body or altered retained native provenance");
    }
}
