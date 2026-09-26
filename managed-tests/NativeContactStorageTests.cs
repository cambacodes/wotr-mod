using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;

internal static class NativeContactStorageTests
{
    internal static void Run(Action<bool, string> check)
    {
        var area = (AreaPersistentState)FormatterServices.GetUninitializedObject(typeof(AreaPersistentState));
        var room = new SceneEntitiesState("DrezenCapital_ThroneRoom_Mechanics");
        var crossScene = new SceneEntitiesState("<cross-scene>");
        typeof(AreaPersistentState).GetField("m_MainState", BindingFlags.Instance | BindingFlags.NonPublic)!.SetValue(area, room);
        typeof(AreaPersistentState).GetField("m_AddStates", BindingFlags.Instance | BindingFlags.NonPublic)!.SetValue(area, new List<SceneEntitiesState>());
        var pet = (UnitEntityData)FormatterServices.GetUninitializedObject(typeof(UnitEntityData));
        // Seed saved storage directly; the unit setter invokes the Unity game singleton.
        typeof(EntityDataBase).GetField("<HoldingState>k__BackingField", BindingFlags.Instance | BindingFlags.NonPublic)!.SetValue(pet, crossScene);
        crossScene.AllEntityData.Add(pet);
        check(ReferenceEquals(pet.HoldingState, crossScene) && crossScene.AllEntityData.Contains(pet), "Native pet storage fixture is invalid.");
        check(!area.AllEntityData.Contains(pet), "Cross-scene fixture does not reproduce the old area's mandatory membership rejection.");
        Console.WriteLine("Native contact reproduction: an actual cross-scene unit is excluded from AreaPersistentState.AllEntityData.");
        var method = typeof(Tirabade.Main).Assembly.GetType("Tirabade.NativeContact", true)!
            .GetMethod("HasCurrentStorage", BindingFlags.Static | BindingFlags.NonPublic)!;
        bool Available() => (bool)method.Invoke(null, new object[] { pet, area, crossScene })!;
        void MoveTo(SceneEntitiesState destination)
        {
            pet.HoldingState?.AllEntityData.Remove(pet);
            typeof(EntityDataBase).GetField("<HoldingState>k__BackingField", BindingFlags.Instance | BindingFlags.NonPublic)!.SetValue(pet, destination);
            destination.AllEntityData.Add(pet);
        }
        check(Available(), "Current cross-scene pet storage is rejected.");
        MoveTo(room);
        check(Available(), "Ordinary area-held actor storage is rejected.");
        var oldArea = new SceneEntitiesState("UnloadedPreviousArea");
        MoveTo(oldArea);
        check(!Available(), "An actor stored in another area is accepted.");
        room.AllEntityData.Add(pet);
        check(!Available(), "Stale area-list entry overrides the actor's actual holding state.");
        room.AllEntityData.Remove(pet);
        MoveTo(crossScene);
        crossScene.AllEntityData.Remove(pet);
        check(!Available(), "An orphaned cross-scene holding reference is accepted.");
    }
}
