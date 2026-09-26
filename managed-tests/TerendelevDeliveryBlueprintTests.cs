using System;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Classes.Experience;
using Kingmaker.Blueprints.Classes;
using Tirabade;

internal static class TerendelevDeliveryBlueprintTests
{
    // Uses actual managed BlueprintUnit/component/reference classes, without pretending Unity serialization ran.
    internal static void Run(Action<bool, string> check)
    {
        var service = typeof(TerendelevDeliveryAttempt).Assembly.GetType("Tirabade.TerendelevDelivery", true)!;
        var configure = service.GetMethod("ConfigureBlueprint", BindingFlags.NonPublic | BindingFlags.Static)!;
        var native = new BlueprintUnit { AssetGuid = BlueprintGuid.Parse("9e8401e7703907e4d94189d5992dd13e"),
            Visual = new UnitVisualParams(), ComponentsArray = new BlueprintComponent[] { new Experience(), new AddClassLevels() } };
        SetReference(native, "m_Brain", "5abc8884c6f15204c8604cb01a2efbab");
        SetReference(native, "m_Faction", "d8de50cc80eb4dc409a983991e0b77ad");
        SetReference(native.Visual, "m_Barks", "c19c6b9c2772526409b7cdb5f3364efe");
        var copiedLevels = new AddClassLevels();
        var copy = new BlueprintUnit { AssetGuid = BlueprintGuid.Parse("93578a5a84c7ec724d14de6d5aba6692"),
            Visual = new UnitVisualParams(), ComponentsArray = new BlueprintComponent[] { new Experience(), copiedLevels } };
        SetReference(copy.Visual, "m_Barks", "c19c6b9c2772526409b7cdb5f3364efe");
        configure.Invoke(null, new object[] { copy, native });
        check(copy.ComponentsArray.Length == 1 && ReferenceEquals(copy.ComponentsArray[0], copiedLevels), "Delivery discarded class setup or retained native XP.");
        check(native.ComponentsArray.Length == 2 && native.ComponentsArray.Any(c => c is Experience), "Delivery mutated native components.");
        check(ReferenceId(copy, "m_Brain") == "5718d805516c5ff48bf3e928b6c0e6fd", "Delivery lacks passive brain.");
        check(ReferenceId(native, "m_Brain") == "5abc8884c6f15204c8604cb01a2efbab", "Delivery changed native combat brain.");
        check(ReferenceId(copy, "m_Faction") == "d8de50cc80eb4dc409a983991e0b77ad", "Delivery lacks native neutral faction.");
        check(ReferenceId(copy.Visual, "m_Barks") == null && ReferenceId(native.Visual, "m_Barks") == "c19c6b9c2772526409b7cdb5f3364efe", "Delivery retained bandit barks or mutated native visual data.");
        bool rejected = false;
        try { configure.Invoke(null, new object[] { native, native }); }
        catch (TargetInvocationException e) when (e.InnerException is InvalidOperationException) { rejected = true; }
        check(rejected, "Delivery accepted mutation of the native blueprint.");
        var shared = new BlueprintUnit { Visual = native.Visual };
        rejected = false;
        try { configure.Invoke(null, new object[] { shared, native }); }
        catch (TargetInvocationException e) when (e.InnerException is InvalidOperationException) { rejected = true; }
        check(rejected, "Delivery accepted shared native visual parameters.");
        var sharedComponent = new BlueprintUnit { Visual = new UnitVisualParams(), ComponentsArray = native.ComponentsArray };
        rejected = false;
        try { configure.Invoke(null, new object[] { sharedComponent, native }); }
        catch (TargetInvocationException e) when (e.InnerException is InvalidOperationException) { rejected = true; }
        check(rejected, "Delivery accepted shared native behavior components.");
        var noLevels = new BlueprintUnit { Visual = new UnitVisualParams(), ComponentsArray = new BlueprintComponent[] { new Experience() } };
        rejected = false;
        try { configure.Invoke(null, new object[] { noLevels, native }); }
        catch (TargetInvocationException e) when (e.InnerException is InvalidOperationException) { rejected = true; }
        check(rejected, "Delivery accepted an uninitialized body without class setup.");
    }

    private static FieldInfo Field(Type type, string name) => type.GetField(name, BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.Public)!;
    private static string? ReferenceId(object target, string name)
    {
        var reference = Field(target.GetType(), name).GetValue(target);
        return reference == null ? null : Field(typeof(BlueprintReferenceBase), "deserializedGuid").GetValue(reference).ToString();
    }
    private static void SetReference(object target, string name, string id)
    {
        var field = Field(target.GetType(), name);
        var reference = (BlueprintReferenceBase)Activator.CreateInstance(field.FieldType);
        Field(typeof(BlueprintReferenceBase), "deserializedGuid").SetValue(reference, BlueprintGuid.Parse(id));
        field.SetValue(target, reference);
    }
}
