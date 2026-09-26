.class public auto ansi beforefieldinit Kingmaker.UnitLogic.UnitDescriptor
	extends [mscorlib]System.Object
	implements [mscorlib]System.IDisposable
{
	// Nested Types
	.class nested public auto ansi beforefieldinit FactionSwitcher
		extends [mscorlib]System.Object
	{
		// Fields
		.field private class Kingmaker.UnitLogic.UnitDescriptor '<UnitDescriptor>k__BackingField'
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		.field private class Kingmaker.Blueprints.BlueprintFaction '<Faction>k__BackingField'
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		.field private bool '<ResetAttackFactions>k__BackingField'
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		.field private bool IsStarted

		// Methods
		.method public hidebysig specialname 
			instance class Kingmaker.UnitLogic.UnitDescriptor get_UnitDescriptor () cil managed 
		{
			.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
				01 00 00 00
			)
			// Method begins at RVA 0x464551
			// Header size: 1
			// Code size: 7 (0x7)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::'<UnitDescriptor>k__BackingField'
			IL_0006: ret
		} // end of method FactionSwitcher::get_UnitDescriptor

		.method private hidebysig specialname 
			instance void set_UnitDescriptor (
				class Kingmaker.UnitLogic.UnitDescriptor 'value'
			) cil managed 
		{
			.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
				01 00 00 00
			)
			// Method begins at RVA 0x464559
			// Header size: 1
			// Code size: 8 (0x8)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: ldarg.1
			IL_0002: stfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::'<UnitDescriptor>k__BackingField'
			IL_0007: ret
		} // end of method FactionSwitcher::set_UnitDescriptor

		.method public hidebysig specialname 
			instance class Kingmaker.Blueprints.BlueprintFaction get_Faction () cil managed 
		{
			.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
				01 00 00 00
			)
			// Method begins at RVA 0x464562
			// Header size: 1
			// Code size: 7 (0x7)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: ldfld class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::'<Faction>k__BackingField'
			IL_0006: ret
		} // end of method FactionSwitcher::get_Faction

		.method private hidebysig specialname 
			instance void set_Faction (
				class Kingmaker.Blueprints.BlueprintFaction 'value'
			) cil managed 
		{
			.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
				01 00 00 00
			)
			// Method begins at RVA 0x46456a
			// Header size: 1
			// Code size: 8 (0x8)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: ldarg.1
			IL_0002: stfld class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::'<Faction>k__BackingField'
			IL_0007: ret
		} // end of method FactionSwitcher::set_Faction

		.method public hidebysig specialname 
			instance bool get_ResetAttackFactions () cil managed 
		{
			.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
				01 00 00 00
			)
			// Method begins at RVA 0x464573
			// Header size: 1
			// Code size: 7 (0x7)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: ldfld bool Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::'<ResetAttackFactions>k__BackingField'
			IL_0006: ret
		} // end of method FactionSwitcher::get_ResetAttackFactions

		.method private hidebysig specialname 
			instance void set_ResetAttackFactions (
				bool 'value'
			) cil managed 
		{
			.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
				01 00 00 00
			)
			// Method begins at RVA 0x46457b
			// Header size: 1
			// Code size: 8 (0x8)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: ldarg.1
			IL_0002: stfld bool Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::'<ResetAttackFactions>k__BackingField'
			IL_0007: ret
		} // end of method FactionSwitcher::set_ResetAttackFactions

		.method public hidebysig specialname rtspecialname 
			instance void .ctor (
				class Kingmaker.UnitLogic.UnitDescriptor unitDescriptor,
				class Kingmaker.Blueprints.BlueprintFaction faction,
				bool resetAttackFactions
			) cil managed 
		{
			// Method begins at RVA 0x464584
			// Header size: 1
			// Code size: 28 (0x1c)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: call instance void [mscorlib]System.Object::.ctor()
			IL_0006: ldarg.0
			IL_0007: ldarg.1
			IL_0008: call instance void Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::set_UnitDescriptor(class Kingmaker.UnitLogic.UnitDescriptor)
			IL_000d: ldarg.0
			IL_000e: ldarg.2
			IL_000f: call instance void Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::set_Faction(class Kingmaker.Blueprints.BlueprintFaction)
			IL_0014: ldarg.0
			IL_0015: ldarg.3
			IL_0016: call instance void Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::set_ResetAttackFactions(bool)
			IL_001b: ret
		} // end of method FactionSwitcher::.ctor

		.method public hidebysig 
			instance void Start () cil managed 
		{
			// Method begins at RVA 0x4645a1
			// Header size: 1
			// Code size: 58 (0x3a)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: ldfld bool Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::IsStarted
			IL_0006: brfalse.s IL_0009

			IL_0008: ret

			IL_0009: ldarg.0
			IL_000a: ldc.i4.1
			IL_000b: stfld bool Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::IsStarted
			IL_0010: ldarg.0
			IL_0011: call instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_UnitDescriptor()
			IL_0016: ldarg.0
			IL_0017: call instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_Faction()
			IL_001c: ldarg.0
			IL_001d: call instance bool Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_ResetAttackFactions()
			IL_0022: ldc.i4.0
			IL_0023: callvirt instance void Kingmaker.UnitLogic.UnitDescriptor::SwitchFactions(class Kingmaker.Blueprints.BlueprintFaction, bool, bool)
			IL_0028: ldarg.0
			IL_0029: call instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_UnitDescriptor()
			IL_002e: ldfld class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher> Kingmaker.UnitLogic.UnitDescriptor::FactionSwitchers
			IL_0033: ldarg.0
			IL_0034: callvirt instance void class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher>::Add(!0)
			IL_0039: ret
		} // end of method FactionSwitcher::Start

		.method public hidebysig 
			instance void Stop () cil managed 
		{
			// Method begins at RVA 0x4645dc
			// Header size: 12
			// Code size: 108 (0x6c)
			.maxstack 4
			.locals init (
				[0] class Kingmaker.Blueprints.BlueprintFaction
			)

			IL_0000: ldarg.0
			IL_0001: ldfld bool Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::IsStarted
			IL_0006: brtrue.s IL_0009

			IL_0008: ret

			IL_0009: ldarg.0
			IL_000a: ldc.i4.0
			IL_000b: stfld bool Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::IsStarted
			IL_0010: ldarg.0
			IL_0011: call instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_UnitDescriptor()
			IL_0016: ldfld class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher> Kingmaker.UnitLogic.UnitDescriptor::FactionSwitchers
			IL_001b: ldarg.0
			IL_001c: callvirt instance bool class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher>::Remove(!0)
			IL_0021: pop
			IL_0022: ldarg.0
			IL_0023: call instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_UnitDescriptor()
			IL_0028: ldfld class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher> Kingmaker.UnitLogic.UnitDescriptor::FactionSwitchers
			IL_002d: callvirt instance int32 class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher>::get_Count()
			IL_0032: ldc.i4.0
			IL_0033: bgt.s IL_0042

			IL_0035: ldarg.0
			IL_0036: call instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_UnitDescriptor()
			IL_003b: callvirt instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_FactionOriginal()
			IL_0040: br.s IL_0057

			IL_0042: ldarg.0
			IL_0043: call instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_UnitDescriptor()
			IL_0048: ldfld class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher> Kingmaker.UnitLogic.UnitDescriptor::FactionSwitchers
			IL_004d: call !!0 [System.Core]System.Linq.Enumerable::Last<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
			IL_0052: callvirt instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_Faction()

			IL_0057: stloc.0
			IL_0058: ldarg.0
			IL_0059: call instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_UnitDescriptor()
			IL_005e: ldloc.0
			IL_005f: ldarg.0
			IL_0060: call instance bool Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_ResetAttackFactions()
			IL_0065: ldc.i4.0
			IL_0066: callvirt instance void Kingmaker.UnitLogic.UnitDescriptor::SwitchFactions(class Kingmaker.Blueprints.BlueprintFaction, bool, bool)
			IL_006b: ret
		} // end of method FactionSwitcher::Stop

		// Properties
		.property instance class Kingmaker.UnitLogic.UnitDescriptor UnitDescriptor()
		{
			.get instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_UnitDescriptor()
			.set instance void Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::set_UnitDescriptor(class Kingmaker.UnitLogic.UnitDescriptor)
		}
		.property instance class Kingmaker.Blueprints.BlueprintFaction Faction()
		{
			.get instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_Faction()
			.set instance void Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::set_Faction(class Kingmaker.Blueprints.BlueprintFaction)
		}
		.property instance bool ResetAttackFactions()
		{
			.get instance bool Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::get_ResetAttackFactions()
			.set instance void Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::set_ResetAttackFactions(bool)
		}

	} // end of class FactionSwitcher

	.class nested private auto ansi sealed serializable beforefieldinit '<>c'
		extends [mscorlib]System.Object
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Fields
		.field public static initonly class Kingmaker.UnitLogic.UnitDescriptor/'<>c' '<>9'
		.field public static class [mscorlib]System.Func`2<class Kingmaker.EntitySystem.EntityFact, bool> '<>9__149_1'
		.field public static class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.FactLogic.AddAbilityToCharacterComponent, class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility>> '<>9__164_0'
		.field public static class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility, bool> '<>9__164_1'
		.field public static class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.ActivatableAbilities.AddActivatableAbilityComponent, class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility>> '<>9__164_3'
		.field public static class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility, bool> '<>9__164_4'
		.field public static class [mscorlib]System.Action`1<class Kingmaker.PubSubSystem.IOwnerGainLevelHandler> '<>9__175_0'

		// Methods
		.method private hidebysig specialname rtspecialname static 
			void .cctor () cil managed 
		{
			// Method begins at RVA 0x464654
			// Header size: 1
			// Code size: 11 (0xb)
			.maxstack 8

			IL_0000: newobj instance void Kingmaker.UnitLogic.UnitDescriptor/'<>c'::.ctor()
			IL_0005: stsfld class Kingmaker.UnitLogic.UnitDescriptor/'<>c' Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9'
			IL_000a: ret
		} // end of method '<>c'::.cctor

		.method public hidebysig specialname rtspecialname 
			instance void .ctor () cil managed 
		{
			// Method begins at RVA 0x464660
			// Header size: 1
			// Code size: 7 (0x7)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: call instance void [mscorlib]System.Object::.ctor()
			IL_0006: ret
		} // end of method '<>c'::.ctor

		.method assembly hidebysig 
			instance bool '<ApplyPostLoadFixes>b__149_1' (
				class Kingmaker.EntitySystem.EntityFact i
			) cil managed 
		{
			// Method begins at RVA 0x464668
			// Header size: 1
			// Code size: 10 (0xa)
			.maxstack 8

			IL_0000: ldarg.1
			IL_0001: callvirt instance !!0 Kingmaker.EntitySystem.EntityFact::GetComponent<class Kingmaker.UnitLogic.Buffs.Polymorph>()
			IL_0006: ldnull
			IL_0007: cgt.un
			IL_0009: ret
		} // end of method '<>c'::'<ApplyPostLoadFixes>b__149_1'

		.method assembly hidebysig 
			instance class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility> '<Initialize>b__164_0' (
				class Kingmaker.UnitLogic.FactLogic.AddAbilityToCharacterComponent c
			) cil managed 
		{
			// Method begins at RVA 0x464673
			// Header size: 1
			// Code size: 12 (0xc)
			.maxstack 8

			IL_0000: ldarg.1
			IL_0001: callvirt instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility, class Kingmaker.Blueprints.BlueprintAbilityReference> Kingmaker.UnitLogic.FactLogic.AddAbilityToCharacterComponent::get_Abilities()
			IL_0006: box valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility, class Kingmaker.Blueprints.BlueprintAbilityReference>
			IL_000b: ret
		} // end of method '<>c'::'<Initialize>b__164_0'

		.method assembly hidebysig 
			instance bool '<Initialize>b__164_1' (
				class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility a
			) cil managed 
		{
			// Method begins at RVA 0x464680
			// Header size: 1
			// Code size: 7 (0x7)
			.maxstack 8

			IL_0000: ldarg.1
			IL_0001: call bool Kingmaker.Blueprints.SimpleBlueprint::op_Implicit(class Kingmaker.Blueprints.SimpleBlueprint)
			IL_0006: ret
		} // end of method '<>c'::'<Initialize>b__164_1'

		.method assembly hidebysig 
			instance class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility> '<Initialize>b__164_3' (
				class Kingmaker.UnitLogic.ActivatableAbilities.AddActivatableAbilityComponent c
			) cil managed 
		{
			// Method begins at RVA 0x464688
			// Header size: 1
			// Code size: 12 (0xc)
			.maxstack 8

			IL_0000: ldarg.1
			IL_0001: callvirt instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility, class Kingmaker.Blueprints.BlueprintActivatableAbilityReference> Kingmaker.UnitLogic.ActivatableAbilities.AddActivatableAbilityComponent::get_ActivatableAbilities()
			IL_0006: box valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility, class Kingmaker.Blueprints.BlueprintActivatableAbilityReference>
			IL_000b: ret
		} // end of method '<>c'::'<Initialize>b__164_3'

		.method assembly hidebysig 
			instance bool '<Initialize>b__164_4' (
				class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility a
			) cil managed 
		{
			// Method begins at RVA 0x464695
			// Header size: 1
			// Code size: 7 (0x7)
			.maxstack 8

			IL_0000: ldarg.1
			IL_0001: call bool Kingmaker.Blueprints.SimpleBlueprint::op_Implicit(class Kingmaker.Blueprints.SimpleBlueprint)
			IL_0006: ret
		} // end of method '<>c'::'<Initialize>b__164_4'

		.method assembly hidebysig 
			instance void '<OnGainClassLevel>b__175_0' (
				class Kingmaker.PubSubSystem.IOwnerGainLevelHandler h
			) cil managed 
		{
			// Method begins at RVA 0x46469d
			// Header size: 1
			// Code size: 7 (0x7)
			.maxstack 8

			IL_0000: ldarg.1
			IL_0001: callvirt instance void Kingmaker.PubSubSystem.IOwnerGainLevelHandler::HandleUnitGainLevel()
			IL_0006: ret
		} // end of method '<>c'::'<OnGainClassLevel>b__175_0'

	} // end of class <>c

	.class nested private auto ansi sealed beforefieldinit '<>c__DisplayClass164_0'
		extends [mscorlib]System.Object
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Fields
		.field public class Kingmaker.UnitLogic.UnitDescriptor unit

		// Methods
		.method public hidebysig specialname rtspecialname 
			instance void .ctor () cil managed 
		{
			// Method begins at RVA 0x4646a5
			// Header size: 1
			// Code size: 7 (0x7)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: call instance void [mscorlib]System.Object::.ctor()
			IL_0006: ret
		} // end of method '<>c__DisplayClass164_0'::.ctor

		.method assembly hidebysig 
			instance void '<Initialize>b__2' (
				class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility a
			) cil managed 
		{
			// Method begins at RVA 0x4646ad
			// Header size: 1
			// Code size: 16 (0x10)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
			IL_0006: ldarg.1
			IL_0007: ldnull
			IL_0008: ldnull
			IL_0009: call class Kingmaker.EntitySystem.EntityFact Kingmaker.UnitLogic.UnitHelper::AddFact(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.Facts.BlueprintUnitFact, class Kingmaker.UnitLogic.Mechanics.MechanicsContext, class Kingmaker.Blueprints.Classes.Selection.FeatureParam)
			IL_000e: pop
			IL_000f: ret
		} // end of method '<>c__DisplayClass164_0'::'<Initialize>b__2'

		.method assembly hidebysig 
			instance void '<Initialize>b__5' (
				class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility a
			) cil managed 
		{
			// Method begins at RVA 0x4646be
			// Header size: 1
			// Code size: 16 (0x10)
			.maxstack 8

			IL_0000: ldarg.0
			IL_0001: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
			IL_0006: ldarg.1
			IL_0007: ldnull
			IL_0008: ldnull
			IL_0009: call class Kingmaker.EntitySystem.EntityFact Kingmaker.UnitLogic.UnitHelper::AddFact(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.Facts.BlueprintUnitFact, class Kingmaker.UnitLogic.Mechanics.MechanicsContext, class Kingmaker.Blueprints.Classes.Selection.FeatureParam)
			IL_000e: pop
			IL_000f: ret
		} // end of method '<>c__DisplayClass164_0'::'<Initialize>b__5'

		.method assembly hidebysig 
			instance void '<Initialize>b__6' (
				class Kingmaker.UnitLogic.IHandleInventoryInitialized c
			) cil managed 
		{
			// Method begins at RVA 0x4646cf
			// Header size: 1
			// Code size: 13 (0xd)
			.maxstack 8

			IL_0000: ldarg.1
			IL_0001: ldarg.0
			IL_0002: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
			IL_0007: callvirt instance void Kingmaker.UnitLogic.IHandleInventoryInitialized::OnInventoryInitialized(class Kingmaker.UnitLogic.UnitDescriptor)
			IL_000c: ret
		} // end of method '<>c__DisplayClass164_0'::'<Initialize>b__6'

	} // end of class <>c__DisplayClass164_0


	// Fields
	.field public class Kingmaker.Items.ItemsCollection m_Inventory
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 00 00
	)
	.field private int32 m_Damage
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 01 00 54 55 6c 4e 65 77 74 6f 6e 73 6f 66
		74 2e 4a 73 6f 6e 2e 44 65 66 61 75 6c 74 56 61
		6c 75 65 48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77
		74 6f 6e 73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65
		72 73 69 6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43
		75 6c 74 75 72 65 3d 6e 65 75 74 72 61 6c 2c 20
		50 75 62 6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e
		75 6c 6c 14 44 65 66 61 75 6c 74 56 61 6c 75 65
		48 61 6e 64 6c 69 6e 67 01 00 00 00
	)
	.field private initonly class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> m_Spellbooks
	.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.NotNullAttribute::.ctor() = (
		01 00 00 00
	)
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 00 00
	)
	.field private class Kingmaker.Blueprints.BlueprintFaction m_Faction
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 01 00 54 0e 0c 50 72 6f 70 65 72 74 79 4e
		61 6d 65 07 46 61 63 74 69 6f 6e
	)
	.field public initonly class Kingmaker.EntitySystem.Stats.CharacterStats Stats
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 00 00
	)
	.field private class Kingmaker.Items.UnitBody '<Body>k__BackingField'
	.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.field public initonly class Kingmaker.UnitLogic.UnitAttackFactions AttackFactions
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 00 00
	)
	.field private class Kingmaker.Blueprints.BlueprintUnit '<ReplaceBlueprintForInspection>k__BackingField'
	.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.field public initonly class Kingmaker.UnitLogic.UnitAbilityResourceCollection Resources
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 00 00
	)
	.field public initonly class Kingmaker.UnitLogic.UnitProgressionData Progression
	.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.NotNullAttribute::.ctor() = (
		01 00 00 00
	)
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 00 00
	)
	.field public initonly class Kingmaker.UI.UnitSettings.UnitUISettings UISettings
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 00 00
	)
	.field public initonly class Kingmaker.UnitLogic.UnitState State
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 00 00
	)
	.field public initonly class Kingmaker.UnitLogic.UnitProficiency Proficiencies
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 00 00
	)
	.field public initonly class Kingmaker.UnitLogic.Alignments.UnitAlignment Alignment
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 00 00
	)
	.field private class Kingmaker.UnitLogic.UnitBrain '<Brain>k__BackingField'
	.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.field private class Kingmaker.Blueprints.BlueprintUnit '<OriginalBlueprint>k__BackingField'
	.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.field private class Kingmaker.Blueprints.BlueprintUnit '<Blueprint>k__BackingField'
	.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.field public valuetype [mscorlib]System.Nullable`1<valuetype Kingmaker.Blueprints.Gender> CustomGender
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 01 00 54 55 69 4e 65 77 74 6f 6e 73 6f 66
		74 2e 4a 73 6f 6e 2e 4e 75 6c 6c 56 61 6c 75 65
		48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77 74 6f 6e
		73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65 72 73 69
		6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43 75 6c 74
		75 72 65 3d 6e 65 75 74 72 61 6c 2c 20 50 75 62
		6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e 75 6c 6c
		11 4e 75 6c 6c 56 61 6c 75 65 48 61 6e 64 6c 69
		6e 67 01 00 00 00
	)
	.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
		01 00 00 00
	)
	.field public valuetype [mscorlib]System.Nullable`1<bool> LeftHandedOverride
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 01 00 54 55 69 4e 65 77 74 6f 6e 73 6f 66
		74 2e 4a 73 6f 6e 2e 4e 75 6c 6c 56 61 6c 75 65
		48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77 74 6f 6e
		73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65 72 73 69
		6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43 75 6c 74
		75 72 65 3d 6e 65 75 74 72 61 6c 2c 20 50 75 62
		6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e 75 6c 6c
		11 4e 75 6c 6c 56 61 6c 75 65 48 61 6e 64 6c 69
		6e 67 01 00 00 00
	)
	.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
		01 00 00 00
	)
	.field public string CustomName
	.custom instance void [System]System.ComponentModel.DefaultValueAttribute::.ctor(string) = (
		01 00 00 00 00
	)
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 01 00 54 55 6c 4e 65 77 74 6f 6e 73 6f 66
		74 2e 4a 73 6f 6e 2e 44 65 66 61 75 6c 74 56 61
		6c 75 65 48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77
		74 6f 6e 73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65
		72 73 69 6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43
		75 6c 74 75 72 65 3d 6e 65 75 74 72 61 6c 2c 20
		50 75 62 6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e
		75 6c 6c 14 44 65 66 61 75 6c 74 56 61 6c 75 65
		48 61 6e 64 6c 69 6e 67 01 00 00 00
	)
	.field public class Kingmaker.Visual.Sound.BlueprintUnitAsksList CustomAsks
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 01 00 54 55 6c 4e 65 77 74 6f 6e 73 6f 66
		74 2e 4a 73 6f 6e 2e 44 65 66 61 75 6c 74 56 61
		6c 75 65 48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77
		74 6f 6e 73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65
		72 73 69 6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43
		75 6c 74 75 72 65 3d 6e 65 75 74 72 61 6c 2c 20
		50 75 62 6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e
		75 6c 6c 14 44 65 66 61 75 6c 74 56 61 6c 75 65
		48 61 6e 64 6c 69 6e 67 01 00 00 00
	)
	.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
		01 00 00 00
	)
	.field public class Kingmaker.Visual.Sound.BlueprintUnitAsksList OverrideAsks
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 01 00 54 55 6c 4e 65 77 74 6f 6e 73 6f 66
		74 2e 4a 73 6f 6e 2e 44 65 66 61 75 6c 74 56 61
		6c 75 65 48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77
		74 6f 6e 73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65
		72 73 69 6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43
		75 6c 74 75 72 65 3d 6e 65 75 74 72 61 6c 2c 20
		50 75 62 6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e
		75 6c 6c 14 44 65 66 61 75 6c 74 56 61 6c 75 65
		48 61 6e 64 6c 69 6e 67 01 00 00 00
	)
	.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
		01 00 00 00
	)
	.field public bool ForceUseClassEquipment
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 01 00 54 55 6c 4e 65 77 74 6f 6e 73 6f 66
		74 2e 4a 73 6f 6e 2e 44 65 66 61 75 6c 74 56 61
		6c 75 65 48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77
		74 6f 6e 73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65
		72 73 69 6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43
		75 6c 74 75 72 65 3d 6e 65 75 74 72 61 6c 2c 20
		50 75 62 6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e
		75 6c 6c 14 44 65 66 61 75 6c 74 56 61 6c 75 65
		48 61 6e 64 6c 69 6e 67 01 00 00 00
	)
	.field public int32 BirthDay
	.custom instance void [System]System.ComponentModel.DefaultValueAttribute::.ctor(int32) = (
		01 00 ff ff ff ff 00 00
	)
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 01 00 54 55 6c 4e 65 77 74 6f 6e 73 6f 66
		74 2e 4a 73 6f 6e 2e 44 65 66 61 75 6c 74 56 61
		6c 75 65 48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77
		74 6f 6e 73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65
		72 73 69 6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43
		75 6c 74 75 72 65 3d 6e 65 75 74 72 61 6c 2c 20
		50 75 62 6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e
		75 6c 6c 14 44 65 66 61 75 6c 74 56 61 6c 75 65
		48 61 6e 64 6c 69 6e 67 01 00 00 00
	)
	.field public int32 BirthMonth
	.custom instance void [System]System.ComponentModel.DefaultValueAttribute::.ctor(int32) = (
		01 00 ff ff ff ff 00 00
	)
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 01 00 54 55 6c 4e 65 77 74 6f 6e 73 6f 66
		74 2e 4a 73 6f 6e 2e 44 65 66 61 75 6c 74 56 61
		6c 75 65 48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77
		74 6f 6e 73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65
		72 73 69 6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43
		75 6c 74 75 72 65 3d 6e 65 75 74 72 61 6c 2c 20
		50 75 62 6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e
		75 6c 6c 14 44 65 66 61 75 6c 74 56 61 6c 75 65
		48 61 6e 64 6c 69 6e 67 01 00 00 00
	)
	.field public string CustomPrefabGuid
	.custom instance void [System]System.ComponentModel.DefaultValueAttribute::.ctor(string) = (
		01 00 00 00 00
	)
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 01 00 54 55 6c 4e 65 77 74 6f 6e 73 6f 66
		74 2e 4a 73 6f 6e 2e 44 65 66 61 75 6c 74 56 61
		6c 75 65 48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77
		74 6f 6e 73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65
		72 73 69 6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43
		75 6c 74 75 72 65 3d 6e 65 75 74 72 61 6c 2c 20
		50 75 62 6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e
		75 6c 6c 14 44 65 66 61 75 6c 74 56 61 6c 75 65
		48 61 6e 64 6c 69 6e 67 01 00 00 00
	)
	.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.NotNullAttribute::.ctor() = (
		01 00 00 00
	)
	.field private class [mscorlib]System.Collections.Generic.List`1<string> m_AppliedFixers
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 01 00 54 55 6c 4e 65 77 74 6f 6e 73 6f 66
		74 2e 4a 73 6f 6e 2e 44 65 66 61 75 6c 74 56 61
		6c 75 65 48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77
		74 6f 6e 73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65
		72 73 69 6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43
		75 6c 74 75 72 65 3d 6e 65 75 74 72 61 6c 2c 20
		50 75 62 6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e
		75 6c 6c 14 44 65 66 61 75 6c 74 56 61 6c 75 65
		48 61 6e 64 6c 69 6e 67 01 00 00 00
	)
	.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
		01 00 00 00
	)
	.field private initonly class Kingmaker.Utility.CountableFlag m_IsEssentialForGame
	.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
		01 00 00 00
	)
	.field private class Kingmaker.UnitLogic.UnitFact '<MainFact>k__BackingField'
	.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.field private valuetype Kingmaker.UnitLogic.Encumbrance '<Encumbrance>k__BackingField'
	.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.field private bool '<HasOwnInventory>k__BackingField'
	.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.field private valuetype [mscorlib]System.Nullable`1<valuetype [mscorlib]System.TimeSpan> '<LastRestTime>k__BackingField'
	.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.field private class Kingmaker.UnitLogic.DollData m_LoadedDollData
	.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
		01 00 00 00
	)
	.field private class Kingmaker.UnitLogic.Mechanics.MechanicsContext m_Context
	.field private valuetype [mscorlib]System.Nullable`1<bool> m_IsPlayerFactionCached
	.field private class Kingmaker.EntitySystem.Entities.UnitEntityData '<Unit>k__BackingField'
	.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.field private bool '<IsTurnedOn>k__BackingField'
	.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.field private class Kingmaker.Blueprints.BlueprintFaction m_FactionOriginal
	.field private class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher> FactionSwitchers

	// Methods
	.method public hidebysig specialname 
		instance class Kingmaker.Items.UnitBody get_Body () cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ac58
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::'<Body>k__BackingField'
		IL_0006: ret
	} // end of method UnitDescriptor::get_Body

	.method public hidebysig specialname 
		instance void set_Body (
			class Kingmaker.Items.UnitBody 'value'
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ac60
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::'<Body>k__BackingField'
		IL_0007: ret
	} // end of method UnitDescriptor::set_Body

	.method public hidebysig specialname 
		instance class Kingmaker.Blueprints.BlueprintUnit get_ReplaceBlueprintForInspection () cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ac69
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::'<ReplaceBlueprintForInspection>k__BackingField'
		IL_0006: ret
	} // end of method UnitDescriptor::get_ReplaceBlueprintForInspection

	.method public hidebysig specialname 
		instance void set_ReplaceBlueprintForInspection (
			class Kingmaker.Blueprints.BlueprintUnit 'value'
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ac71
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::'<ReplaceBlueprintForInspection>k__BackingField'
		IL_0007: ret
	} // end of method UnitDescriptor::set_ReplaceBlueprintForInspection

	.method public hidebysig specialname 
		instance class Kingmaker.UnitLogic.UnitBrain get_Brain () cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ac7a
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UnitLogic.UnitBrain Kingmaker.UnitLogic.UnitDescriptor::'<Brain>k__BackingField'
		IL_0006: ret
	} // end of method UnitDescriptor::get_Brain

	.method private hidebysig specialname 
		instance void set_Brain (
			class Kingmaker.UnitLogic.UnitBrain 'value'
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ac82
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld class Kingmaker.UnitLogic.UnitBrain Kingmaker.UnitLogic.UnitDescriptor::'<Brain>k__BackingField'
		IL_0007: ret
	} // end of method UnitDescriptor::set_Brain

	.method public hidebysig specialname 
		instance class Kingmaker.Blueprints.BlueprintUnit get_OriginalBlueprint () cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ac8b
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::'<OriginalBlueprint>k__BackingField'
		IL_0006: ret
	} // end of method UnitDescriptor::get_OriginalBlueprint

	.method private hidebysig specialname 
		instance void set_OriginalBlueprint (
			class Kingmaker.Blueprints.BlueprintUnit 'value'
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ac93
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::'<OriginalBlueprint>k__BackingField'
		IL_0007: ret
	} // end of method UnitDescriptor::set_OriginalBlueprint

	.method public hidebysig specialname 
		instance class Kingmaker.Blueprints.BlueprintUnit get_Blueprint () cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ac9c
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::'<Blueprint>k__BackingField'
		IL_0006: ret
	} // end of method UnitDescriptor::get_Blueprint

	.method private hidebysig specialname 
		instance void set_Blueprint (
			class Kingmaker.Blueprints.BlueprintUnit 'value'
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31aca4
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::'<Blueprint>k__BackingField'
		IL_0007: ret
	} // end of method UnitDescriptor::set_Blueprint

	.method public hidebysig specialname 
		instance class Kingmaker.UnitLogic.UnitFact get_MainFact () cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31acad
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UnitLogic.UnitFact Kingmaker.UnitLogic.UnitDescriptor::'<MainFact>k__BackingField'
		IL_0006: ret
	} // end of method UnitDescriptor::get_MainFact

	.method private hidebysig specialname 
		instance void set_MainFact (
			class Kingmaker.UnitLogic.UnitFact 'value'
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31acb5
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld class Kingmaker.UnitLogic.UnitFact Kingmaker.UnitLogic.UnitDescriptor::'<MainFact>k__BackingField'
		IL_0007: ret
	} // end of method UnitDescriptor::set_MainFact

	.method public hidebysig specialname 
		instance valuetype Kingmaker.UnitLogic.Encumbrance get_Encumbrance () cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31acbe
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld valuetype Kingmaker.UnitLogic.Encumbrance Kingmaker.UnitLogic.UnitDescriptor::'<Encumbrance>k__BackingField'
		IL_0006: ret
	} // end of method UnitDescriptor::get_Encumbrance

	.method public hidebysig specialname 
		instance void set_Encumbrance (
			valuetype Kingmaker.UnitLogic.Encumbrance 'value'
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31acc6
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld valuetype Kingmaker.UnitLogic.Encumbrance Kingmaker.UnitLogic.UnitDescriptor::'<Encumbrance>k__BackingField'
		IL_0007: ret
	} // end of method UnitDescriptor::set_Encumbrance

	.method public hidebysig specialname 
		instance bool get_HasOwnInventory () cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31accf
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld bool Kingmaker.UnitLogic.UnitDescriptor::'<HasOwnInventory>k__BackingField'
		IL_0006: ret
	} // end of method UnitDescriptor::get_HasOwnInventory

	.method private hidebysig specialname 
		instance void set_HasOwnInventory (
			bool 'value'
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31acd7
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld bool Kingmaker.UnitLogic.UnitDescriptor::'<HasOwnInventory>k__BackingField'
		IL_0007: ret
	} // end of method UnitDescriptor::set_HasOwnInventory

	.method public hidebysig specialname 
		instance valuetype [mscorlib]System.Nullable`1<valuetype [mscorlib]System.TimeSpan> get_LastRestTime () cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ace0
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld valuetype [mscorlib]System.Nullable`1<valuetype [mscorlib]System.TimeSpan> Kingmaker.UnitLogic.UnitDescriptor::'<LastRestTime>k__BackingField'
		IL_0006: ret
	} // end of method UnitDescriptor::get_LastRestTime

	.method public hidebysig specialname 
		instance void set_LastRestTime (
			valuetype [mscorlib]System.Nullable`1<valuetype [mscorlib]System.TimeSpan> 'value'
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ace8
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld valuetype [mscorlib]System.Nullable`1<valuetype [mscorlib]System.TimeSpan> Kingmaker.UnitLogic.UnitDescriptor::'<LastRestTime>k__BackingField'
		IL_0007: ret
	} // end of method UnitDescriptor::set_LastRestTime

	.method private hidebysig specialname 
		instance void set_Doll (
			class Kingmaker.UnitLogic.DollData 'value'
		) cil managed 
	{
		// Method begins at RVA 0x31acf1
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld class Kingmaker.UnitLogic.DollData Kingmaker.UnitLogic.UnitDescriptor::m_LoadedDollData
		IL_0007: ret
	} // end of method UnitDescriptor::set_Doll

	.method public hidebysig specialname 
		instance class Kingmaker.EntitySystem.Entities.UnitEntityData get_Unit () cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31acfa
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::'<Unit>k__BackingField'
		IL_0006: ret
	} // end of method UnitDescriptor::get_Unit

	.method private hidebysig specialname 
		instance void set_Unit (
			class Kingmaker.EntitySystem.Entities.UnitEntityData 'value'
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ad02
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::'<Unit>k__BackingField'
		IL_0007: ret
	} // end of method UnitDescriptor::set_Unit

	.method public hidebysig specialname 
		instance bool get_IsTurnedOn () cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ad0b
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld bool Kingmaker.UnitLogic.UnitDescriptor::'<IsTurnedOn>k__BackingField'
		IL_0006: ret
	} // end of method UnitDescriptor::get_IsTurnedOn

	.method private hidebysig specialname 
		instance void set_IsTurnedOn (
			bool 'value'
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31ad13
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld bool Kingmaker.UnitLogic.UnitDescriptor::'<IsTurnedOn>k__BackingField'
		IL_0007: ret
	} // end of method UnitDescriptor::set_IsTurnedOn

	.method public hidebysig specialname 
		instance class Kingmaker.Blueprints.BlueprintFaction get_Faction () cil managed 
	{
		// Method begins at RVA 0x31ad1c
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::m_Faction
		IL_0006: ret
	} // end of method UnitDescriptor::get_Faction

	.method private hidebysig specialname 
		instance void set_Faction (
			class Kingmaker.Blueprints.BlueprintFaction 'value'
		) cil managed 
	{
		// Method begins at RVA 0x31ad24
		// Header size: 1
		// Code size: 53 (0x35)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: stfld class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::m_Faction
		IL_0007: ldarg.0
		IL_0008: ldarg.0
		IL_0009: ldfld class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::m_Faction
		IL_000e: call class Kingmaker.Blueprints.Root.BlueprintRoot Kingmaker.Blueprints.Root.BlueprintRoot::get_Instance()
		IL_0013: callvirt instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.Blueprints.Root.BlueprintRoot::get_PlayerFaction()
		IL_0018: ceq
		IL_001a: newobj instance void valuetype [mscorlib]System.Nullable`1<bool>::.ctor(!0)
		IL_001f: stfld valuetype [mscorlib]System.Nullable`1<bool> Kingmaker.UnitLogic.UnitDescriptor::m_IsPlayerFactionCached
		IL_0024: ldarg.0
		IL_0025: ldfld class Kingmaker.UnitLogic.UnitAttackFactions Kingmaker.UnitLogic.UnitDescriptor::AttackFactions
		IL_002a: dup
		IL_002b: brtrue.s IL_002f

		IL_002d: pop
		IL_002e: ret

		IL_002f: call instance void Kingmaker.UnitLogic.UnitAttackFactions::UpdateIsPlayerEnemy()
		IL_0034: ret
	} // end of method UnitDescriptor::set_Faction

	.method public hidebysig specialname 
		instance class Kingmaker.Blueprints.BlueprintFaction get_FactionOriginal () cil managed 
	{
		// Method begins at RVA 0x31ad5c
		// Header size: 12
		// Code size: 26 (0x1a)
		.maxstack 3
		.locals init (
			[0] class Kingmaker.Blueprints.BlueprintFaction
		)

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::m_FactionOriginal
		IL_0006: dup
		IL_0007: brtrue.s IL_0019

		IL_0009: pop
		IL_000a: ldarg.0
		IL_000b: ldarg.0
		IL_000c: call instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_Faction()
		IL_0011: dup
		IL_0012: stloc.0
		IL_0013: stfld class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::m_FactionOriginal
		IL_0018: ldloc.0

		IL_0019: ret
	} // end of method UnitDescriptor::get_FactionOriginal

	.method public hidebysig specialname 
		instance int32 get_Damage () cil managed 
	{
		// Method begins at RVA 0x31ad82
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld int32 Kingmaker.UnitLogic.UnitDescriptor::m_Damage
		IL_0006: ret
	} // end of method UnitDescriptor::get_Damage

	.method public hidebysig specialname 
		instance void set_Damage (
			int32 'value'
		) cil managed 
	{
		// Method begins at RVA 0x31ad8a
		// Header size: 1
		// Code size: 14 (0xe)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldc.i4.0
		IL_0002: ldarg.1
		IL_0003: call int32 [mscorlib]System.Math::Max(int32, int32)
		IL_0008: stfld int32 Kingmaker.UnitLogic.UnitDescriptor::m_Damage
		IL_000d: ret
	} // end of method UnitDescriptor::set_Damage

	.method public hidebysig specialname 
		instance class Kingmaker.UnitLogic.Abilities.AbilityCollection get_Abilities () cil managed 
	{
		// Method begins at RVA 0x31ad99
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0006: callvirt instance class Kingmaker.UnitLogic.Abilities.AbilityCollection Kingmaker.EntitySystem.Entities.UnitEntityData::get_Abilities()
		IL_000b: ret
	} // end of method UnitDescriptor::get_Abilities

	.method public hidebysig specialname 
		instance class Kingmaker.UnitLogic.ActivatableAbilities.ActivatableAbilityCollection get_ActivatableAbilities () cil managed 
	{
		// Method begins at RVA 0x31ada6
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0006: callvirt instance class Kingmaker.UnitLogic.ActivatableAbilities.ActivatableAbilityCollection Kingmaker.EntitySystem.Entities.UnitEntityData::get_ActivatableAbilities()
		IL_000b: ret
	} // end of method UnitDescriptor::get_ActivatableAbilities

	.method public hidebysig specialname 
		instance class Kingmaker.UnitLogic.Buffs.BuffCollection get_Buffs () cil managed 
	{
		// Method begins at RVA 0x31adb3
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0006: callvirt instance class Kingmaker.UnitLogic.Buffs.BuffCollection Kingmaker.EntitySystem.Entities.UnitEntityData::get_Buffs()
		IL_000b: ret
	} // end of method UnitDescriptor::get_Buffs

	.method public hidebysig specialname 
		instance int32 get_DamageNonLethal () cil managed 
	{
		// Method begins at RVA 0x31adc0
		// Header size: 1
		// Code size: 17 (0x11)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0006: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValue Kingmaker.EntitySystem.Stats.CharacterStats::DamageNonLethal
		IL_000b: callvirt instance int32 Kingmaker.EntitySystem.Stats.ModifiableValue::get_ModifiedValue()
		IL_0010: ret
	} // end of method UnitDescriptor::get_DamageNonLethal

	.method public hidebysig specialname 
		instance valuetype Kingmaker.Blueprints.Gender get_Gender () cil managed 
	{
		// Method begins at RVA 0x31add4
		// Header size: 12
		// Code size: 36 (0x24)
		.maxstack 1
		.locals init (
			[0] valuetype [mscorlib]System.Nullable`1<valuetype Kingmaker.Blueprints.Gender>
		)

		IL_0000: ldarg.0
		IL_0001: ldfld valuetype [mscorlib]System.Nullable`1<valuetype Kingmaker.Blueprints.Gender> Kingmaker.UnitLogic.UnitDescriptor::CustomGender
		IL_0006: stloc.0
		IL_0007: ldloca.s 0
		IL_0009: call instance bool valuetype [mscorlib]System.Nullable`1<valuetype Kingmaker.Blueprints.Gender>::get_HasValue()
		IL_000e: brtrue.s IL_001c

		IL_0010: ldarg.0
		IL_0011: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()
		IL_0016: ldfld valuetype Kingmaker.Blueprints.Gender Kingmaker.Blueprints.BlueprintUnit::Gender
		IL_001b: ret

		IL_001c: ldloca.s 0
		IL_001e: call instance !0 valuetype [mscorlib]System.Nullable`1<valuetype Kingmaker.Blueprints.Gender>::GetValueOrDefault()
		IL_0023: ret
	} // end of method UnitDescriptor::get_Gender

	.method public hidebysig specialname 
		instance bool get_IsLeftHanded () cil managed 
	{
		// Method begins at RVA 0x31ae04
		// Header size: 12
		// Code size: 36 (0x24)
		.maxstack 1
		.locals init (
			[0] valuetype [mscorlib]System.Nullable`1<bool>
		)

		IL_0000: ldarg.0
		IL_0001: ldfld valuetype [mscorlib]System.Nullable`1<bool> Kingmaker.UnitLogic.UnitDescriptor::LeftHandedOverride
		IL_0006: stloc.0
		IL_0007: ldloca.s 0
		IL_0009: call instance bool valuetype [mscorlib]System.Nullable`1<bool>::get_HasValue()
		IL_000e: brtrue.s IL_001c

		IL_0010: ldarg.0
		IL_0011: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()
		IL_0016: ldfld bool Kingmaker.Blueprints.BlueprintUnit::IsLeftHanded
		IL_001b: ret

		IL_001c: ldloca.s 0
		IL_001e: call instance !0 valuetype [mscorlib]System.Nullable`1<bool>::GetValueOrDefault()
		IL_0023: ret
	} // end of method UnitDescriptor::get_IsLeftHanded

	.method public hidebysig specialname 
		instance string get_CharacterName () cil managed 
	{
		// Method begins at RVA 0x31ae34
		// Header size: 1
		// Code size: 57 (0x39)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_ReplaceBlueprintForInspection()
		IL_0006: call bool Kingmaker.Blueprints.SimpleBlueprint::op_Implicit(class Kingmaker.Blueprints.SimpleBlueprint)
		IL_000b: brfalse.s IL_0019

		IL_000d: ldarg.0
		IL_000e: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_ReplaceBlueprintForInspection()
		IL_0013: callvirt instance string Kingmaker.Blueprints.BlueprintUnit::get_CharacterName()
		IL_0018: ret

		IL_0019: ldarg.0
		IL_001a: ldfld string Kingmaker.UnitLogic.UnitDescriptor::CustomName
		IL_001f: call bool [mscorlib]System.String::IsNullOrEmpty(string)
		IL_0024: brtrue.s IL_002d

		IL_0026: ldarg.0
		IL_0027: ldfld string Kingmaker.UnitLogic.UnitDescriptor::CustomName
		IL_002c: ret

		IL_002d: ldarg.0
		IL_002e: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()
		IL_0033: callvirt instance string Kingmaker.Blueprints.BlueprintUnit::get_CharacterName()
		IL_0038: ret
	} // end of method UnitDescriptor::get_CharacterName

	.method public hidebysig specialname 
		instance class Kingmaker.Visual.Sound.BlueprintUnitAsksList get_Asks () cil managed 
	{
		// Method begins at RVA 0x31ae6e
		// Header size: 1
		// Code size: 47 (0x2f)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Visual.Sound.BlueprintUnitAsksList Kingmaker.UnitLogic.UnitDescriptor::OverrideAsks
		IL_0006: brfalse.s IL_000f

		IL_0008: ldarg.0
		IL_0009: ldfld class Kingmaker.Visual.Sound.BlueprintUnitAsksList Kingmaker.UnitLogic.UnitDescriptor::OverrideAsks
		IL_000e: ret

		IL_000f: ldarg.0
		IL_0010: ldfld class Kingmaker.Visual.Sound.BlueprintUnitAsksList Kingmaker.UnitLogic.UnitDescriptor::CustomAsks
		IL_0015: brfalse.s IL_001e

		IL_0017: ldarg.0
		IL_0018: ldfld class Kingmaker.Visual.Sound.BlueprintUnitAsksList Kingmaker.UnitLogic.UnitDescriptor::CustomAsks
		IL_001d: ret

		IL_001e: ldarg.0
		IL_001f: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()
		IL_0024: ldfld class Kingmaker.Blueprints.UnitVisualParams Kingmaker.Blueprints.BlueprintUnit::Visual
		IL_0029: callvirt instance class Kingmaker.Visual.Sound.BlueprintUnitAsksList Kingmaker.Blueprints.UnitVisualParams::get_Barks()
		IL_002e: ret
	} // end of method UnitDescriptor::get_Asks

	.method public hidebysig specialname 
		instance bool get_UseClassEquipment () cil managed 
	{
		// Method begins at RVA 0x31aea0
		// Header size: 12
		// Code size: 92 (0x5c)
		.maxstack 2
		.locals init (
			[0] valuetype Kingmaker.EntitySystem.EntityRef`1<class Kingmaker.EntitySystem.Entities.UnitEntityData>
		)

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0006: callvirt instance valuetype Kingmaker.EntitySystem.EntityRef`1<class Kingmaker.EntitySystem.Entities.UnitEntityData> Kingmaker.EntitySystem.Entities.UnitEntityData::get_PreviewOf()
		IL_000b: stloc.0
		IL_000c: ldloca.s 0
		IL_000e: call instance !0 valuetype Kingmaker.EntitySystem.EntityRef`1<class Kingmaker.EntitySystem.Entities.UnitEntityData>::get_Entity()
		IL_0013: ldnull
		IL_0014: call bool Kingmaker.EntitySystem.Entities.UnitEntityData::op_Inequality(class Kingmaker.EntitySystem.Entities.UnitEntityData, class Kingmaker.UnitLogic.UnitDescriptor)
		IL_0019: brtrue.s IL_003e

		IL_001b: ldarg.0
		IL_001c: ldfld bool Kingmaker.UnitLogic.UnitDescriptor::ForceUseClassEquipment
		IL_0021: brtrue.s IL_003c

		IL_0023: ldarg.0
		IL_0024: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0029: callvirt instance bool Kingmaker.EntitySystem.Entities.UnitEntityData::get_IsMainCharacter()
		IL_002e: brtrue.s IL_003c

		IL_0030: ldarg.0
		IL_0031: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0036: call bool Kingmaker.UnitLogic.UnitHelper::IsCustomCompanion(class Kingmaker.EntitySystem.Entities.UnitEntityData)
		IL_003b: ret

		IL_003c: ldc.i4.1
		IL_003d: ret

		IL_003e: ldarg.0
		IL_003f: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0044: callvirt instance valuetype Kingmaker.EntitySystem.EntityRef`1<class Kingmaker.EntitySystem.Entities.UnitEntityData> Kingmaker.EntitySystem.Entities.UnitEntityData::get_PreviewOf()
		IL_0049: stloc.0
		IL_004a: ldloca.s 0
		IL_004c: call instance !0 valuetype Kingmaker.EntitySystem.EntityRef`1<class Kingmaker.EntitySystem.Entities.UnitEntityData>::get_Entity()
		IL_0051: callvirt instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.EntitySystem.Entities.UnitEntityData::get_Descriptor()
		IL_0056: callvirt instance bool Kingmaker.UnitLogic.UnitDescriptor::get_UseClassEquipment()
		IL_005b: ret
	} // end of method UnitDescriptor::get_UseClassEquipment

	.method public hidebysig specialname 
		instance valuetype Kingmaker.Enums.Size get_OriginalSize () cil managed 
	{
		// Method begins at RVA 0x31af08
		// Header size: 1
		// Code size: 39 (0x27)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_0006: callvirt instance class Kingmaker.Blueprints.Classes.BlueprintRace Kingmaker.UnitLogic.UnitProgressionData::get_Race()
		IL_000b: ldnull
		IL_000c: call !!0 Kingmaker.Blueprints.SimpleBlueprintExtendAsObject::Or<class Kingmaker.Blueprints.Classes.BlueprintRace>(!!0, !!0)
		IL_0011: dup
		IL_0012: brtrue.s IL_0021

		IL_0014: pop
		IL_0015: ldarg.0
		IL_0016: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()
		IL_001b: ldfld valuetype Kingmaker.Enums.Size Kingmaker.Blueprints.BlueprintUnit::Size
		IL_0020: ret

		IL_0021: ldfld valuetype Kingmaker.Enums.Size Kingmaker.Blueprints.Classes.BlueprintRace::Size
		IL_0026: ret
	} // end of method UnitDescriptor::get_OriginalSize

	.method public hidebysig specialname 
		instance class Kingmaker.UnitLogic.Mechanics.MechanicsContext get_Context () cil managed 
	{
		// Method begins at RVA 0x31af30
		// Header size: 12
		// Code size: 44 (0x2c)
		.maxstack 7
		.locals init (
			[0] class Kingmaker.UnitLogic.Mechanics.MechanicsContext
		)

		IL_0000: ldarg.0
		IL_0001: ldarg.0
		IL_0002: ldfld class Kingmaker.UnitLogic.Mechanics.MechanicsContext Kingmaker.UnitLogic.UnitDescriptor::m_Context
		IL_0007: dup
		IL_0008: brtrue.s IL_0023

		IL_000a: pop
		IL_000b: ldarg.0
		IL_000c: ldnull
		IL_000d: ldarg.0
		IL_000e: ldarg.0
		IL_000f: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_OriginalBlueprint()
		IL_0014: ldnull
		IL_0015: ldnull
		IL_0016: newobj instance void Kingmaker.UnitLogic.Mechanics.MechanicsContext::.ctor(class Kingmaker.EntitySystem.Entities.UnitEntityData, class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.BlueprintScriptableObject, class Kingmaker.UnitLogic.Mechanics.MechanicsContext, class Kingmaker.Utility.TargetWrapper)
		IL_001b: dup
		IL_001c: stloc.0
		IL_001d: stfld class Kingmaker.UnitLogic.Mechanics.MechanicsContext Kingmaker.UnitLogic.UnitDescriptor::m_Context
		IL_0022: ldloc.0

		IL_0023: dup
		IL_0024: stloc.0
		IL_0025: stfld class Kingmaker.UnitLogic.Mechanics.MechanicsContext Kingmaker.UnitLogic.UnitDescriptor::m_Context
		IL_002a: ldloc.0
		IL_002b: ret
	} // end of method UnitDescriptor::get_Context

	.method public hidebysig specialname 
		instance class Kingmaker.EntitySystem.EntityFactsManager get_Facts () cil managed 
	{
		// Method begins at RVA 0x31af68
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0006: ldfld class Kingmaker.EntitySystem.EntityFactsManager Kingmaker.EntitySystem.EntityDataBase::Facts
		IL_000b: ret
	} // end of method UnitDescriptor::get_Facts

	.method public hidebysig specialname 
		instance class Kingmaker.Items.ItemsCollection get_Inventory () cil managed 
	{
		// Method begins at RVA 0x31af75
		// Header size: 1
		// Code size: 7 (0x7)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::m_Inventory
		IL_0006: ret
	} // end of method UnitDescriptor::get_Inventory

	.method public hidebysig specialname 
		instance int32 get_HPLeft () cil managed 
	{
		// Method begins at RVA 0x31af7d
		// Header size: 1
		// Code size: 24 (0x18)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0006: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueHitPoints Kingmaker.EntitySystem.Stats.CharacterStats::HitPoints
		IL_000b: call int32 Kingmaker.EntitySystem.Stats.ModifiableValue::op_Implicit(class Kingmaker.EntitySystem.Stats.ModifiableValue)
		IL_0010: ldarg.0
		IL_0011: call instance int32 Kingmaker.UnitLogic.UnitDescriptor::get_Damage()
		IL_0016: sub
		IL_0017: ret
	} // end of method UnitDescriptor::get_HPLeft

	.method public hidebysig specialname 
		instance int32 get_MaxHP () cil managed 
	{
		// Method begins at RVA 0x31af96
		// Header size: 1
		// Code size: 17 (0x11)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0006: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueHitPoints Kingmaker.EntitySystem.Stats.CharacterStats::HitPoints
		IL_000b: call int32 Kingmaker.EntitySystem.Stats.ModifiableValue::op_Implicit(class Kingmaker.EntitySystem.Stats.ModifiableValue)
		IL_0010: ret
	} // end of method UnitDescriptor::get_MaxHP

	.method public hidebysig specialname 
		instance int32 get_TemporaryHP () cil managed 
	{
		// Method begins at RVA 0x31afa8
		// Header size: 1
		// Code size: 17 (0x11)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0006: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueTemporaryHitPoints Kingmaker.EntitySystem.Stats.CharacterStats::TemporaryHitPoints
		IL_000b: call int32 Kingmaker.EntitySystem.Stats.ModifiableValue::op_Implicit(class Kingmaker.EntitySystem.Stats.ModifiableValue)
		IL_0010: ret
	} // end of method UnitDescriptor::get_TemporaryHP

	.method public hidebysig specialname 
		instance class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.Spellbook> get_Spellbooks () cil managed 
	{
		// Method begins at RVA 0x31afba
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::m_Spellbooks
		IL_0006: callvirt instance class [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection<!0, !1> class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::get_Values()
		IL_000b: ret
	} // end of method UnitDescriptor::get_Spellbooks

	.method public hidebysig specialname 
		instance bool get_IsPlayerFaction () cil managed 
	{
		// Method begins at RVA 0x31afc8
		// Header size: 12
		// Code size: 72 (0x48)
		.maxstack 3

		IL_0000: ldarg.0
		IL_0001: ldflda valuetype [mscorlib]System.Nullable`1<bool> Kingmaker.UnitLogic.UnitDescriptor::m_IsPlayerFactionCached
		IL_0006: call instance bool valuetype [mscorlib]System.Nullable`1<bool>::get_HasValue()
		IL_000b: brtrue.s IL_002a

		IL_000d: ldarg.0
		IL_000e: ldarg.0
		IL_000f: call instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_Faction()
		IL_0014: call class Kingmaker.Blueprints.Root.BlueprintRoot Kingmaker.Blueprints.Root.BlueprintRoot::get_Instance()
		IL_0019: callvirt instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.Blueprints.Root.BlueprintRoot::get_PlayerFaction()
		IL_001e: ceq
		IL_0020: newobj instance void valuetype [mscorlib]System.Nullable`1<bool>::.ctor(!0)
		IL_0025: stfld valuetype [mscorlib]System.Nullable`1<bool> Kingmaker.UnitLogic.UnitDescriptor::m_IsPlayerFactionCached

		IL_002a: ldarg.0
		IL_002b: ldflda valuetype [mscorlib]System.Nullable`1<bool> Kingmaker.UnitLogic.UnitDescriptor::m_IsPlayerFactionCached
		IL_0030: call instance !0 valuetype [mscorlib]System.Nullable`1<bool>::get_Value()
		IL_0035: brfalse.s IL_0044

		IL_0037: ldarg.0
		IL_0038: ldfld class Kingmaker.UnitLogic.UnitAttackFactions Kingmaker.UnitLogic.UnitDescriptor::AttackFactions
		IL_003d: callvirt instance bool Kingmaker.UnitLogic.UnitAttackFactions::get_IsPlayerEnemy()
		IL_0042: brfalse.s IL_0046

		IL_0044: ldc.i4.0
		IL_0045: ret

		IL_0046: ldc.i4.1
		IL_0047: ret
	} // end of method UnitDescriptor::get_IsPlayerFaction

	.method public hidebysig specialname 
		instance bool get_HasUMDSkill () cil managed 
	{
		// Method begins at RVA 0x31b01c
		// Header size: 1
		// Code size: 20 (0x14)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0006: callvirt instance class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::get_ActualSkillUseMagicDevice()
		IL_000b: callvirt instance int32 Kingmaker.EntitySystem.Stats.ModifiableValue::get_BaseValue()
		IL_0010: ldc.i4.0
		IL_0011: cgt
		IL_0013: ret
	} // end of method UnitDescriptor::get_HasUMDSkill

	.method public hidebysig specialname 
		instance bool get_IsImmuneToVisualEffects () cil managed 
	{
		// Method begins at RVA 0x31b031
		// Header size: 1
		// Code size: 30 (0x1e)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_0006: ldc.i4.1
		IL_0007: callvirt instance bool Kingmaker.UnitLogic.UnitState::HasCondition(valuetype Kingmaker.UnitLogic.UnitCondition)
		IL_000c: brtrue.s IL_001c

		IL_000e: ldarg.0
		IL_000f: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_0014: ldc.i4.s 18
		IL_0016: callvirt instance bool Kingmaker.UnitLogic.UnitState::HasCondition(valuetype Kingmaker.UnitLogic.UnitCondition)
		IL_001b: ret

		IL_001c: ldc.i4.1
		IL_001d: ret
	} // end of method UnitDescriptor::get_IsImmuneToVisualEffects

	.method public hidebysig specialname 
		instance bool get_IsSeeInvisibility () cil managed 
	{
		// Method begins at RVA 0x31b050
		// Header size: 1
		// Code size: 31 (0x1f)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_0006: ldc.i4.s 17
		IL_0008: callvirt instance bool Kingmaker.UnitLogic.UnitState::HasCondition(valuetype Kingmaker.UnitLogic.UnitCondition)
		IL_000d: brtrue.s IL_001d

		IL_000f: ldarg.0
		IL_0010: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_0015: ldc.i4.s 18
		IL_0017: callvirt instance bool Kingmaker.UnitLogic.UnitState::HasCondition(valuetype Kingmaker.UnitLogic.UnitCondition)
		IL_001c: ret

		IL_001d: ldc.i4.1
		IL_001e: ret
	} // end of method UnitDescriptor::get_IsSeeInvisibility

	.method public hidebysig specialname 
		instance bool get_IsUndead () cil managed 
	{
		// Method begins at RVA 0x31b070
		// Header size: 1
		// Code size: 22 (0x16)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call class Kingmaker.Blueprints.Root.BlueprintRoot Kingmaker.Blueprints.Root.BlueprintRoot::get_Instance()
		IL_0006: ldfld class Kingmaker.Blueprints.Root.SystemMechanicsRoot Kingmaker.Blueprints.Root.BlueprintRoot::SystemMechanics
		IL_000b: callvirt instance class Kingmaker.Blueprints.Classes.BlueprintFeature Kingmaker.Blueprints.Root.SystemMechanicsRoot::get_UndeadType()
		IL_0010: call bool Kingmaker.UnitLogic.UnitHelper::HasFact(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.Facts.BlueprintFact)
		IL_0015: ret
	} // end of method UnitDescriptor::get_IsUndead

	.method public hidebysig specialname 
		instance bool get_IsEssentialForGame () cil managed 
	{
		// Method begins at RVA 0x31b087
		// Header size: 1
		// Code size: 22 (0x16)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Utility.CountableFlag Kingmaker.UnitLogic.UnitDescriptor::m_IsEssentialForGame
		IL_0006: call bool Kingmaker.Utility.CountableFlag::op_Implicit(class Kingmaker.Utility.CountableFlag)
		IL_000b: brtrue.s IL_0014

		IL_000d: ldarg.0
		IL_000e: call instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsMainCharacter()
		IL_0013: ret

		IL_0014: ldc.i4.1
		IL_0015: ret
	} // end of method UnitDescriptor::get_IsEssentialForGame

	.method public hidebysig specialname 
		instance bool get_UseMartialArts () cil managed 
	{
		// Method begins at RVA 0x31b09e
		// Header size: 1
		// Code size: 22 (0x16)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_0006: ldfld class Kingmaker.UnitLogic.UnitMechanicFeatures Kingmaker.UnitLogic.UnitState::Features
		IL_000b: ldfld class Kingmaker.Utility.CountableFlag Kingmaker.UnitLogic.UnitMechanicFeatures::ImprovedUnarmedStrike
		IL_0010: call bool Kingmaker.Utility.CountableFlag::op_Implicit(class Kingmaker.Utility.CountableFlag)
		IL_0015: ret
	} // end of method UnitDescriptor::get_UseMartialArts

	.method public hidebysig specialname 
		instance class Kingmaker.Blueprints.PortraitData get_Portrait () cil managed 
	{
		// Method begins at RVA 0x31b0b5
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UI.UnitSettings.UnitUISettings Kingmaker.UnitLogic.UnitDescriptor::UISettings
		IL_0006: callvirt instance class Kingmaker.Blueprints.PortraitData Kingmaker.UI.UnitSettings.UnitUISettings::get_Portrait()
		IL_000b: ret
	} // end of method UnitDescriptor::get_Portrait

	.method public hidebysig specialname 
		instance class Kingmaker.Blueprints.PortraitData get_OverridePortrait () cil managed 
	{
		// Method begins at RVA 0x31b0c2
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UI.UnitSettings.UnitUISettings Kingmaker.UnitLogic.UnitDescriptor::UISettings
		IL_0006: callvirt instance class Kingmaker.Blueprints.PortraitData Kingmaker.UI.UnitSettings.UnitUISettings::get_OverridePortrait()
		IL_000b: ret
	} // end of method UnitDescriptor::get_OverridePortrait

	.method public hidebysig specialname 
		instance class Kingmaker.Blueprints.PortraitData get_CrossPortrait () cil managed 
	{
		// Method begins at RVA 0x31b0cf
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UI.UnitSettings.UnitUISettings Kingmaker.UnitLogic.UnitDescriptor::UISettings
		IL_0006: callvirt instance class Kingmaker.Blueprints.PortraitData Kingmaker.UI.UnitSettings.UnitUISettings::get_CrossPortrait()
		IL_000b: ret
	} // end of method UnitDescriptor::get_CrossPortrait

	.method public hidebysig specialname 
		instance bool get_IsMainCharacter () cil managed 
	{
		// Method begins at RVA 0x31b0dc
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0006: callvirt instance bool Kingmaker.EntitySystem.Entities.UnitEntityData::get_IsMainCharacter()
		IL_000b: ret
	} // end of method UnitDescriptor::get_IsMainCharacter

	.method public hidebysig specialname 
		instance class Kingmaker.Blueprints.BlueprintUnit get_BlueprintForInspection () cil managed 
	{
		// Method begins at RVA 0x31b0e9
		// Header size: 1
		// Code size: 23 (0x17)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_ReplaceBlueprintForInspection()
		IL_0006: ldnull
		IL_0007: call !!0 Kingmaker.Blueprints.SimpleBlueprintExtendAsObject::Or<class Kingmaker.Blueprints.BlueprintUnit>(!!0, !!0)
		IL_000c: dup
		IL_000d: brtrue.s IL_0016

		IL_000f: pop
		IL_0010: ldarg.0
		IL_0011: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()

		IL_0016: ret
	} // end of method UnitDescriptor::get_BlueprintForInspection

	.method public hidebysig 
		instance !!TPart Get<(Kingmaker.UnitLogic.OldStyleUnitPart) TPart> () cil managed 
	{
		.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31b101
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0006: callvirt instance !!0 Kingmaker.EntitySystem.EntityDataBase::Get<!!TPart>()
		IL_000b: ret
	} // end of method UnitDescriptor::Get

	.method public hidebysig 
		instance !!TPart Ensure<.ctor (Kingmaker.UnitLogic.OldStyleUnitPart) TPart> () cil managed 
	{
		// Method begins at RVA 0x31b10e
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0006: callvirt instance !!0 Kingmaker.EntitySystem.EntityDataBase::Ensure<!!TPart>()
		IL_000b: ret
	} // end of method UnitDescriptor::Ensure

	.method public hidebysig 
		instance void Remove<(Kingmaker.UnitLogic.OldStyleUnitPart) TPart> () cil managed 
	{
		// Method begins at RVA 0x31b11b
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0006: callvirt instance void Kingmaker.EntitySystem.EntityDataBase::Remove<!!TPart>()
		IL_000b: ret
	} // end of method UnitDescriptor::Remove

	.method public hidebysig 
		instance void TurnOn () cil managed 
	{
		// Method begins at RVA 0x31b128
		// Header size: 12
		// Code size: 66 (0x42)
		.maxstack 2

		IL_0000: ldarg.0
		IL_0001: ldc.i4.1
		IL_0002: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_IsTurnedOn(bool)
		IL_0007: ldarg.0
		IL_0008: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_000d: callvirt instance void Kingmaker.UnitLogic.UnitProgressionData::CheckStatPrerequisitesAndUpdate()
		IL_0012: ldarg.0
		IL_0013: call instance class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::get_Inventory()
		IL_0018: callvirt instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.Items.ItemsCollection::get_OwnerUnit()
		IL_001d: ldarg.0
		IL_001e: bne.un.s IL_002b

		IL_0020: ldarg.0
		IL_0021: call instance class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::get_Inventory()
		IL_0026: callvirt instance void Kingmaker.Items.ItemsCollection::TurnOn()

		IL_002b: ldarg.0
		IL_002c: call instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		IL_0031: callvirt instance void Kingmaker.Items.UnitBody::TurnOn()
		IL_0036: ldarg.0
		IL_0037: call instance class Kingmaker.UnitLogic.UnitBrain Kingmaker.UnitLogic.UnitDescriptor::get_Brain()
		IL_003c: callvirt instance void Kingmaker.UnitLogic.UnitBrain::TurnOn()
		IL_0041: ret
	} // end of method UnitDescriptor::TurnOn

	.method public hidebysig 
		instance void TurnOff () cil managed 
	{
		// Method begins at RVA 0x31b176
		// Header size: 1
		// Code size: 55 (0x37)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldc.i4.0
		IL_0002: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_IsTurnedOn(bool)
		IL_0007: ldarg.0
		IL_0008: call instance class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::get_Inventory()
		IL_000d: callvirt instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.Items.ItemsCollection::get_OwnerUnit()
		IL_0012: ldarg.0
		IL_0013: bne.un.s IL_0020

		IL_0015: ldarg.0
		IL_0016: call instance class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::get_Inventory()
		IL_001b: callvirt instance void Kingmaker.Items.ItemsCollection::TurnOff()

		IL_0020: ldarg.0
		IL_0021: call instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		IL_0026: callvirt instance void Kingmaker.Items.UnitBody::TurnOff()
		IL_002b: ldarg.0
		IL_002c: call instance class Kingmaker.UnitLogic.UnitBrain Kingmaker.UnitLogic.UnitDescriptor::get_Brain()
		IL_0031: callvirt instance void Kingmaker.UnitLogic.UnitBrain::TurnOff()
		IL_0036: ret
	} // end of method UnitDescriptor::TurnOff

	.method public hidebysig 
		instance void PreSave () cil managed 
	{
		// Method begins at RVA 0x31b1b0
		// Header size: 12
		// Code size: 115 (0x73)
		.maxstack 2
		.locals init (
			[0] valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>
		)

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		IL_0006: callvirt instance void Kingmaker.Items.UnitBody::PreSave()
		IL_000b: ldarg.0
		IL_000c: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_0011: callvirt instance void Kingmaker.UnitLogic.UnitProgressionData::PreSave()
		IL_0016: ldarg.0
		IL_0017: ldfld class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::m_Spellbooks
		IL_001c: callvirt instance class [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection<!0, !1> class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::get_Values()
		IL_0021: callvirt instance valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<!0, !1> class [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::GetEnumerator()
		IL_0026: stloc.0
		.try
		{
			IL_0027: br.s IL_0035
			// loop start (head: IL_0035)
				IL_0029: ldloca.s 0
				IL_002b: call instance !1 valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::get_Current()
				IL_0030: callvirt instance void Kingmaker.UnitLogic.Spellbook::PreSave()

				IL_0035: ldloca.s 0
				IL_0037: call instance bool valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::MoveNext()
				IL_003c: brtrue.s IL_0029
			// end loop

			IL_003e: leave.s IL_004e
		} // end .try
		finally
		{
			IL_0040: ldloca.s 0
			IL_0042: constrained. valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>
			IL_0048: callvirt instance void [mscorlib]System.IDisposable::Dispose()
			IL_004d: endfinally
		} // end handler

		IL_004e: ldarg.0
		IL_004f: call instance class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::get_Inventory()
		IL_0054: callvirt instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.Items.ItemsCollection::get_OwnerUnit()
		IL_0059: ldarg.0
		IL_005a: bne.un.s IL_0067

		IL_005c: ldarg.0
		IL_005d: call instance class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::get_Inventory()
		IL_0062: callvirt instance void Kingmaker.Items.ItemsCollection::PreSave()

		IL_0067: ldarg.0
		IL_0068: call instance class Kingmaker.UnitLogic.UnitBrain Kingmaker.UnitLogic.UnitDescriptor::get_Brain()
		IL_006d: callvirt instance void Kingmaker.UnitLogic.UnitBrain::PreSave()
		IL_0072: ret
	} // end of method UnitDescriptor::PreSave

	.method public hidebysig 
		instance void PostLoad (
			class Kingmaker.EntitySystem.Entities.UnitEntityData entity
		) cil managed 
	{
		// Method begins at RVA 0x31b240
		// Header size: 12
		// Code size: 249 (0xf9)
		.maxstack 2
		.locals init (
			[0] valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>
		)

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_Unit(class Kingmaker.EntitySystem.Entities.UnitEntityData)
		IL_0007: ldarg.0
		IL_0008: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_OriginalBlueprint()
		IL_000d: brtrue.s IL_001b

		IL_000f: ldarg.0
		IL_0010: ldarg.0
		IL_0011: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()
		IL_0016: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_OriginalBlueprint(class Kingmaker.Blueprints.BlueprintUnit)

		IL_001b: ldarg.0
		IL_001c: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0021: ldarg.0
		IL_0022: callvirt instance void Kingmaker.EntitySystem.Stats.CharacterStats::PostLoad(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_0027: ldarg.0
		IL_0028: ldfld class Kingmaker.UnitLogic.Alignments.UnitAlignment Kingmaker.UnitLogic.UnitDescriptor::Alignment
		IL_002d: ldarg.0
		IL_002e: callvirt instance void Kingmaker.UnitLogic.Alignments.UnitAlignment::PostLoad(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_0033: ldarg.0
		IL_0034: ldfld class Kingmaker.UnitLogic.UnitAbilityResourceCollection Kingmaker.UnitLogic.UnitDescriptor::Resources
		IL_0039: ldarg.0
		IL_003a: callvirt instance void Kingmaker.UnitLogic.UnitAbilityResourceCollection::PostLoad(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_003f: call !0 class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.EntitySystem.Entities.UnitEntityData/Respec>::get_Current()
		IL_0044: call bool class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.EntitySystem.Entities.UnitEntityData/Respec>::op_Implicit(class Kingmaker.ElementsSystem.ContextData`1<!0>)
		IL_0049: brtrue.s IL_0057

		IL_004b: ldarg.0
		IL_004c: call instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		IL_0051: ldarg.0
		IL_0052: callvirt instance void Kingmaker.Items.UnitBody::PostLoad(class Kingmaker.UnitLogic.UnitDescriptor)

		IL_0057: ldarg.0
		IL_0058: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_005d: ldarg.0
		IL_005e: callvirt instance void Kingmaker.UnitLogic.UnitProgressionData::PostLoad(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_0063: ldarg.0
		IL_0064: ldfld class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::m_Spellbooks
		IL_0069: callvirt instance class [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection<!0, !1> class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::get_Values()
		IL_006e: callvirt instance valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<!0, !1> class [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::GetEnumerator()
		IL_0073: stloc.0
		.try
		{
			IL_0074: br.s IL_0083
			// loop start (head: IL_0083)
				IL_0076: ldloca.s 0
				IL_0078: call instance !1 valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::get_Current()
				IL_007d: ldarg.0
				IL_007e: callvirt instance void Kingmaker.UnitLogic.Spellbook::PostLoad(class Kingmaker.UnitLogic.UnitDescriptor)

				IL_0083: ldloca.s 0
				IL_0085: call instance bool valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::MoveNext()
				IL_008a: brtrue.s IL_0076
			// end loop

			IL_008c: leave.s IL_009c
		} // end .try
		finally
		{
			IL_008e: ldloca.s 0
			IL_0090: constrained. valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>
			IL_0096: callvirt instance void [mscorlib]System.IDisposable::Dispose()
			IL_009b: endfinally
		} // end handler

		IL_009c: ldarg.0
		IL_009d: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_00a2: ldarg.0
		IL_00a3: callvirt instance void Kingmaker.UnitLogic.UnitState::PostLoad(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_00a8: ldarg.0
		IL_00a9: ldfld class Kingmaker.UnitLogic.UnitAttackFactions Kingmaker.UnitLogic.UnitDescriptor::AttackFactions
		IL_00ae: ldarg.0
		IL_00af: callvirt instance void Kingmaker.UnitLogic.UnitAttackFactions::PostLoad(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_00b4: ldarg.0
		IL_00b5: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_00ba: call class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.Designers.GameHelper::GetPlayerCharacter()
		IL_00bf: call class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.EntitySystem.Entities.UnitEntityData::op_Implicit(class Kingmaker.EntitySystem.Entities.UnitEntityData)
		IL_00c4: call bool Kingmaker.EntitySystem.Entities.UnitEntityData::op_Equality(class Kingmaker.EntitySystem.Entities.UnitEntityData, class Kingmaker.UnitLogic.UnitDescriptor)
		IL_00c9: brfalse.s IL_00ec

		IL_00cb: ldarg.0
		IL_00cc: call instance class Kingmaker.UnitLogic.UnitBrain Kingmaker.UnitLogic.UnitDescriptor::get_Brain()
		IL_00d1: ldarg.0
		IL_00d2: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()
		IL_00d7: callvirt instance class Kingmaker.AI.Blueprints.BlueprintBrain Kingmaker.Blueprints.BlueprintUnit::get_DefaultBrain()
		IL_00dc: callvirt instance void Kingmaker.UnitLogic.UnitBrain::SetBrain(class Kingmaker.AI.Blueprints.BlueprintBrain)
		IL_00e1: ldarg.0
		IL_00e2: call instance class Kingmaker.UnitLogic.UnitBrain Kingmaker.UnitLogic.UnitDescriptor::get_Brain()
		IL_00e7: callvirt instance void Kingmaker.UnitLogic.UnitBrain::RestoreAvailableActions()

		IL_00ec: ldarg.0
		IL_00ed: call instance class Kingmaker.UnitLogic.UnitBrain Kingmaker.UnitLogic.UnitDescriptor::get_Brain()
		IL_00f2: ldarg.0
		IL_00f3: callvirt instance void Kingmaker.UnitLogic.UnitBrain::PostLoad(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_00f8: ret
	} // end of method UnitDescriptor::PostLoad

	.method public hidebysig 
		instance void OnComponentsDidPostLoad () cil managed 
	{
		// Method begins at RVA 0x31b358
		// Header size: 1
		// Code size: 13 (0xd)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UI.UnitSettings.UnitUISettings Kingmaker.UnitLogic.UnitDescriptor::UISettings
		IL_0006: ldarg.0
		IL_0007: callvirt instance void Kingmaker.UI.UnitSettings.UnitUISettings::PostLoad(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_000c: ret
	} // end of method UnitDescriptor::OnComponentsDidPostLoad

	.method public hidebysig 
		instance void ApplyPostLoadFixes () cil managed 
	{
		// Method begins at RVA 0x31b368
		// Header size: 12
		// Code size: 481 (0x1e1)
		.maxstack 6
		.locals init (
			[0] class Kingmaker.UnitLogic.FactLogic.AddPostLoadActions,
			[1] valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<valuetype [mscorlib]System.Collections.Generic.KeyValuePair`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>>,
			[2] class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook,
			[3] class Kingmaker.UnitLogic.Spellbook,
			[4] class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook,
			[5] class Kingmaker.UnitLogic.Spellbook,
			[6] class Kingmaker.UnitLogic.Mechanics.MechanicsContext/Data
		)

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UnitLogic.DollData Kingmaker.UnitLogic.UnitDescriptor::m_LoadedDollData
		IL_0006: brfalse.s IL_001e

		IL_0008: ldarg.0
		IL_0009: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_000e: callvirt instance !!0 Kingmaker.EntitySystem.EntityDataBase::Ensure<class Kingmaker.UnitLogic.Parts.UnitPartDollData>()
		IL_0013: ldarg.0
		IL_0014: ldfld class Kingmaker.UnitLogic.DollData Kingmaker.UnitLogic.UnitDescriptor::m_LoadedDollData
		IL_0019: callvirt instance void Kingmaker.UnitLogic.Parts.UnitPartDollData::SetDefault(class Kingmaker.UnitLogic.DollData)

		IL_001e: ldarg.0
		IL_001f: call instance void Kingmaker.UnitLogic.UnitDescriptor::OnDifficultyChanged()
		IL_0024: ldarg.0
		IL_0025: call instance void Kingmaker.UnitLogic.UnitDescriptor::EnsureNaturalProficiencies()
		IL_002a: ldarg.0
		IL_002b: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0030: callvirt instance void Kingmaker.EntitySystem.Stats.CharacterStats::ApplyPostLoadFixes()
		IL_0035: ldarg.0
		IL_0036: call instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		IL_003b: callvirt instance void Kingmaker.Items.UnitBody::ApplyPostLoadFixes()
		IL_0040: ldarg.0
		IL_0041: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_0046: callvirt instance void Kingmaker.UnitLogic.UnitState::ApplyPostLoadFixes()
		IL_004b: ldarg.0
		IL_004c: call instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsMainCharacter()
		IL_0051: brfalse.s IL_006b

		IL_0053: ldarg.0
		IL_0054: ldfld class Kingmaker.Utility.CountableFlag Kingmaker.UnitLogic.UnitDescriptor::m_IsEssentialForGame
		IL_0059: call bool Kingmaker.Utility.CountableFlag::op_Implicit(class Kingmaker.Utility.CountableFlag)
		IL_005e: brtrue.s IL_006b

		IL_0060: ldarg.0
		IL_0061: ldfld class Kingmaker.Utility.CountableFlag Kingmaker.UnitLogic.UnitDescriptor::m_IsEssentialForGame
		IL_0066: callvirt instance void Kingmaker.Utility.CountableFlag::Retain()

		IL_006b: ldarg.0
		IL_006c: ldfld class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::m_Spellbooks
		IL_0071: call class [mscorlib]System.Collections.Generic.List`1<valuetype [mscorlib]System.Collections.Generic.KeyValuePair`2<!!0, !!1>> [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Utils.TempListExtension::ToTempList<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>(class [mscorlib]System.Collections.Generic.Dictionary`2<!!0, !!1>)
		IL_0076: callvirt instance valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<!0> class [mscorlib]System.Collections.Generic.List`1<valuetype [mscorlib]System.Collections.Generic.KeyValuePair`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>>::GetEnumerator()
		IL_007b: stloc.1
		.try
		{
			IL_007c: br.s IL_00bb
			// loop start (head: IL_00bb)
				IL_007e: ldloca.s 1
				IL_0080: call instance !0 valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<valuetype [mscorlib]System.Collections.Generic.KeyValuePair`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>>::get_Current()
				IL_0085: ldloca.s 4
				IL_0087: ldloca.s 5
				IL_0089: call void Kingmaker.Utility.LinqExtensions::Deconstruct<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>(valuetype [mscorlib]System.Collections.Generic.KeyValuePair`2<!!0, !!1>, !!0&, !!1&)
				IL_008e: ldloc.s 4
				IL_0090: stloc.2
				IL_0091: ldloc.s 5
				IL_0093: stloc.3
				IL_0094: ldloc.3
				IL_0095: callvirt instance int32 Kingmaker.UnitLogic.Spellbook::get_RawBaseLevel()
				IL_009a: ldc.i4.1
				IL_009b: bge.s IL_00b5

				IL_009d: ldloc.3
				IL_009e: callvirt instance int32 Kingmaker.UnitLogic.Spellbook::get_MythicLevel()
				IL_00a3: ldc.i4.1
				IL_00a4: bge.s IL_00b5

				IL_00a6: ldarg.0
				IL_00a7: ldfld class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::m_Spellbooks
				IL_00ac: ldloc.2
				IL_00ad: callvirt instance bool class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::Remove(!0)
				IL_00b2: pop
				IL_00b3: br.s IL_00bb

				IL_00b5: ldloc.3
				IL_00b6: callvirt instance void Kingmaker.UnitLogic.Spellbook::ApplyPostLoadFixes()

				IL_00bb: ldloca.s 1
				IL_00bd: call instance bool valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<valuetype [mscorlib]System.Collections.Generic.KeyValuePair`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>>::MoveNext()
				IL_00c2: brtrue.s IL_007e
			// end loop

			IL_00c4: leave.s IL_00d4
		} // end .try
		finally
		{
			IL_00c6: ldloca.s 1
			IL_00c8: constrained. valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<valuetype [mscorlib]System.Collections.Generic.KeyValuePair`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>>
			IL_00ce: callvirt instance void [mscorlib]System.IDisposable::Dispose()
			IL_00d3: endfinally
		} // end handler

		IL_00d4: ldarg.0
		IL_00d5: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()
		IL_00da: call !!0 Kingmaker.Blueprints.BlueprintExtenstions::GetComponent<class Kingmaker.UnitLogic.FactLogic.AddPostLoadActions>(class Kingmaker.Blueprints.BlueprintScriptableObject)
		IL_00df: stloc.0
		IL_00e0: ldloc.0
		IL_00e1: brfalse.s IL_0125

		IL_00e3: ldloc.0
		IL_00e4: ldfld class Kingmaker.ElementsSystem.ActionList Kingmaker.UnitLogic.FactLogic.AddPostLoadActions::Actions
		IL_00e9: callvirt instance bool Kingmaker.ElementsSystem.ActionList::get_HasActions()
		IL_00ee: brfalse.s IL_0125

		IL_00f0: ldarg.0
		IL_00f1: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_00f6: ldarg.0
		IL_00f7: ldarg.0
		IL_00f8: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()
		IL_00fd: ldnull
		IL_00fe: ldnull
		IL_00ff: newobj instance void Kingmaker.UnitLogic.Mechanics.MechanicsContext::.ctor(class Kingmaker.EntitySystem.Entities.UnitEntityData, class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.BlueprintScriptableObject, class Kingmaker.UnitLogic.Mechanics.MechanicsContext, class Kingmaker.Utility.TargetWrapper)
		IL_0104: ldnull
		IL_0105: callvirt instance class Kingmaker.UnitLogic.Mechanics.MechanicsContext/Data Kingmaker.UnitLogic.Mechanics.MechanicsContext::GetDataScope(class Kingmaker.Utility.TargetWrapper)
		IL_010a: stloc.s 6
		.try
		{
			IL_010c: ldloc.0
			IL_010d: ldfld class Kingmaker.ElementsSystem.ActionList Kingmaker.UnitLogic.FactLogic.AddPostLoadActions::Actions
			IL_0112: callvirt instance void Kingmaker.ElementsSystem.ActionList::Run()
			IL_0117: leave.s IL_0125
		} // end .try
		finally
		{
			IL_0119: ldloc.s 6
			IL_011b: brfalse.s IL_0124

			IL_011d: ldloc.s 6
			IL_011f: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_0124: endfinally
		} // end handler

		IL_0125: ldarg.0
		IL_0126: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()
		IL_012b: ldarg.0
		IL_012c: ldftn instance void Kingmaker.UnitLogic.UnitDescriptor::'<ApplyPostLoadFixes>b__149_0'(class Kingmaker.UnitLogic.Mechanics.Components.Fixers.FixUnitOnPostLoad)
		IL_0132: newobj instance void class [mscorlib]System.Action`1<class Kingmaker.UnitLogic.Mechanics.Components.Fixers.FixUnitOnPostLoad>::.ctor(object, native int)
		IL_0137: call void Kingmaker.Blueprints.BlueprintExtenstions::CallComponents<class Kingmaker.UnitLogic.Mechanics.Components.Fixers.FixUnitOnPostLoad>(class Kingmaker.Blueprints.BlueprintScriptableObject, class [mscorlib]System.Action`1<!!0>)
		IL_013c: ldarg.0
		IL_013d: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_0142: callvirt instance bool Kingmaker.UnitLogic.UnitState::get_IsFinallyDead()
		IL_0147: brtrue.s IL_014f

		IL_0149: ldarg.0
		IL_014a: call instance void Kingmaker.UnitLogic.UnitDescriptor::RemoveBuffsOnResurrect()

		IL_014f: ldarg.0
		IL_0150: ldfld class Kingmaker.UnitLogic.UnitAttackFactions Kingmaker.UnitLogic.UnitDescriptor::AttackFactions
		IL_0155: ldarg.0
		IL_0156: call instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_Faction()
		IL_015b: callvirt instance bool Kingmaker.UnitLogic.UnitAttackFactions::Contains(class Kingmaker.Blueprints.BlueprintFaction)
		IL_0160: brfalse.s IL_018c

		IL_0162: ldarg.0
		IL_0163: ldfld class Kingmaker.UnitLogic.UnitAttackFactions Kingmaker.UnitLogic.UnitDescriptor::AttackFactions
		IL_0168: ldarg.0
		IL_0169: call instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_Faction()
		IL_016e: callvirt instance void Kingmaker.UnitLogic.UnitAttackFactions::Remove(class Kingmaker.Blueprints.BlueprintFaction)
		IL_0173: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
		IL_0178: ldstr "AttackFactions of unit can't contains unit's own Faction, fixed ({0})"
		IL_017d: ldc.i4.1
		IL_017e: newarr [mscorlib]System.Object
		IL_0183: dup
		IL_0184: ldc.i4.0
		IL_0185: ldarg.0
		IL_0186: stelem.ref
		IL_0187: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Error(string, object[])

		IL_018c: ldarg.0
		IL_018d: call instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		IL_0192: callvirt instance bool Kingmaker.Items.UnitBody::get_IsPolymorphed()
		IL_0197: brfalse.s IL_01d5

		IL_0199: ldarg.0
		IL_019a: call instance class Kingmaker.EntitySystem.EntityFactsManager Kingmaker.UnitLogic.UnitDescriptor::get_Facts()
		IL_019f: callvirt instance class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.EntitySystem.EntityFact> Kingmaker.EntitySystem.EntityFactsManager::get_List()
		IL_01a4: ldsfld class [mscorlib]System.Func`2<class Kingmaker.EntitySystem.EntityFact, bool> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9__149_1'
		IL_01a9: dup
		IL_01aa: brtrue.s IL_01c3

		IL_01ac: pop
		IL_01ad: ldsfld class Kingmaker.UnitLogic.UnitDescriptor/'<>c' Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9'
		IL_01b2: ldftn instance bool Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<ApplyPostLoadFixes>b__149_1'(class Kingmaker.EntitySystem.EntityFact)
		IL_01b8: newobj instance void class [mscorlib]System.Func`2<class Kingmaker.EntitySystem.EntityFact, bool>::.ctor(object, native int)
		IL_01bd: dup
		IL_01be: stsfld class [mscorlib]System.Func`2<class Kingmaker.EntitySystem.EntityFact, bool> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9__149_1'

		IL_01c3: call bool Kingmaker.Utility.LinqExtensions::HasItem<class Kingmaker.EntitySystem.EntityFact>(class [mscorlib]System.Collections.Generic.IList`1<!!0>, class [mscorlib]System.Func`2<!!0, bool>)
		IL_01c8: brtrue.s IL_01d5

		IL_01ca: ldarg.0
		IL_01cb: call instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		IL_01d0: callvirt instance void Kingmaker.Items.UnitBody::CancelPolymorphEffect()

		IL_01d5: ldarg.0
		IL_01d6: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_01db: callvirt instance void Kingmaker.UnitLogic.UnitProgressionData::ApplyPostLoadFixes()
		IL_01e0: ret
	} // end of method UnitDescriptor::ApplyPostLoadFixes

	.method private hidebysig 
		instance void EnsureNaturalProficiencies () cil managed 
	{
		// Method begins at RVA 0x31b574
		// Header size: 12
		// Code size: 68 (0x44)
		.maxstack 2
		.locals init (
			[0] class [mscorlib]System.Collections.Generic.IEnumerator`1<valuetype Kingmaker.Enums.WeaponCategory>,
			[1] valuetype Kingmaker.Enums.WeaponCategory
		)

		IL_0000: ldc.i4.5
		IL_0001: call class [mscorlib]System.Collections.Generic.IEnumerable`1<valuetype Kingmaker.Enums.WeaponCategory> Kingmaker.Enums.WeaponCategoryExtension::GetAllCategories(valuetype Kingmaker.Enums.WeaponSubCategory)
		IL_0006: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<!0> class [mscorlib]System.Collections.Generic.IEnumerable`1<valuetype Kingmaker.Enums.WeaponCategory>::GetEnumerator()
		IL_000b: stloc.0
		.try
		{
			IL_000c: br.s IL_002f
			// loop start (head: IL_002f)
				IL_000e: ldloc.0
				IL_000f: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<valuetype Kingmaker.Enums.WeaponCategory>::get_Current()
				IL_0014: stloc.1
				IL_0015: ldarg.0
				IL_0016: ldfld class Kingmaker.UnitLogic.UnitProficiency Kingmaker.UnitLogic.UnitDescriptor::Proficiencies
				IL_001b: ldloc.1
				IL_001c: callvirt instance bool Kingmaker.UnitLogic.UnitProficiency::Contains(valuetype Kingmaker.Enums.WeaponCategory)
				IL_0021: brtrue.s IL_002f

				IL_0023: ldarg.0
				IL_0024: ldfld class Kingmaker.UnitLogic.UnitProficiency Kingmaker.UnitLogic.UnitDescriptor::Proficiencies
				IL_0029: ldloc.1
				IL_002a: callvirt instance void Kingmaker.UnitLogic.UnitProficiency::Add(valuetype Kingmaker.Enums.WeaponCategory)

				IL_002f: ldloc.0
				IL_0030: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
				IL_0035: brtrue.s IL_000e
			// end loop

			IL_0037: leave.s IL_0043
		} // end .try
		finally
		{
			IL_0039: ldloc.0
			IL_003a: brfalse.s IL_0042

			IL_003c: ldloc.0
			IL_003d: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_0042: endfinally
		} // end handler

		IL_0043: ret
	} // end of method UnitDescriptor::EnsureNaturalProficiencies

	.method public final hidebysig newslot virtual 
		instance void Dispose () cil managed 
	{
		// Method begins at RVA 0x31b5d4
		// Header size: 12
		// Code size: 134 (0x86)
		.maxstack 2
		.locals init (
			[0] valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>
		)

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		IL_0006: brfalse.s IL_0021

		IL_0008: ldarg.0
		IL_0009: call instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		IL_000e: callvirt instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.Items.UnitBody::get_Owner()
		IL_0013: ldarg.0
		IL_0014: bne.un.s IL_0021

		IL_0016: ldarg.0
		IL_0017: call instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		IL_001c: callvirt instance void Kingmaker.Items.UnitBody::Dispose()

		IL_0021: ldarg.0
		IL_0022: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_0027: callvirt instance void Kingmaker.UnitLogic.UnitProgressionData::Dispose()
		IL_002c: ldarg.0
		IL_002d: ldfld class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::m_Spellbooks
		IL_0032: callvirt instance class [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection<!0, !1> class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::get_Values()
		IL_0037: callvirt instance valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<!0, !1> class [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::GetEnumerator()
		IL_003c: stloc.0
		.try
		{
			IL_003d: br.s IL_004b
			// loop start (head: IL_004b)
				IL_003f: ldloca.s 0
				IL_0041: call instance !1 valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::get_Current()
				IL_0046: callvirt instance void Kingmaker.UnitLogic.Spellbook::Dispose()

				IL_004b: ldloca.s 0
				IL_004d: call instance bool valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::MoveNext()
				IL_0052: brtrue.s IL_003f
			// end loop

			IL_0054: leave.s IL_0064
		} // end .try
		finally
		{
			IL_0056: ldloca.s 0
			IL_0058: constrained. valuetype [mscorlib]System.Collections.Generic.Dictionary`2/ValueCollection/Enumerator<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>
			IL_005e: callvirt instance void [mscorlib]System.IDisposable::Dispose()
			IL_0063: endfinally
		} // end handler

		IL_0064: ldarg.0
		IL_0065: call instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsPlayerFaction()
		IL_006a: brtrue.s IL_0085

		IL_006c: ldarg.0
		IL_006d: call instance class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::get_Inventory()
		IL_0072: callvirt instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.Items.ItemsCollection::get_OwnerUnit()
		IL_0077: ldarg.0
		IL_0078: bne.un.s IL_0085

		IL_007a: ldarg.0
		IL_007b: call instance class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::get_Inventory()
		IL_0080: callvirt instance void Kingmaker.Items.ItemsCollection::Dispose()

		IL_0085: ret
	} // end of method UnitDescriptor::Dispose

	.method public hidebysig 
		instance class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher GetFactionSwitcher (
			class Kingmaker.Blueprints.BlueprintFaction faction,
			[opt] bool resetAttackFactions
		) cil managed 
	{
		.param [2] = bool(false)
		// Method begins at RVA 0x31b678
		// Header size: 1
		// Code size: 9 (0x9)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: ldarg.2
		IL_0003: newobj instance void Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher::.ctor(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.BlueprintFaction, bool)
		IL_0008: ret
	} // end of method UnitDescriptor::GetFactionSwitcher

	.method public hidebysig 
		instance void SwitchFactions (
			class Kingmaker.Blueprints.BlueprintFaction faction,
			[opt] bool resetAttackFactions
		) cil managed 
	{
		.param [2] = bool(false)
		// Method begins at RVA 0x31b682
		// Header size: 1
		// Code size: 10 (0xa)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: ldarg.2
		IL_0003: ldc.i4.1
		IL_0004: call instance void Kingmaker.UnitLogic.UnitDescriptor::SwitchFactions(class Kingmaker.Blueprints.BlueprintFaction, bool, bool)
		IL_0009: ret
	} // end of method UnitDescriptor::SwitchFactions

	.method private hidebysig 
		instance void SwitchFactions (
			class Kingmaker.Blueprints.BlueprintFaction faction,
			bool resetAttackFactions,
			bool permanently
		) cil managed 
	{
		// Method begins at RVA 0x31b690
		// Header size: 12
		// Code size: 383 (0x17f)
		.maxstack 3
		.locals init (
			[0] class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.Blueprints.BlueprintFaction>,
			[1] class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.Blueprints.BlueprintFaction>,
			[2] valuetype Kingmaker.EntitySystem.EntityPoolEnumerator`1<class Kingmaker.EntitySystem.Entities.UnitEntityData>,
			[3] class Kingmaker.UnitLogic.Parts.UnitPartSummonedMonster
		)

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_Faction()
		IL_0006: ldarg.1
		IL_0007: bne.un.s IL_0023

		IL_0009: ldarg.2
		IL_000a: brfalse.s IL_0022

		IL_000c: ldarg.0
		IL_000d: ldfld class Kingmaker.UnitLogic.UnitAttackFactions Kingmaker.UnitLogic.UnitDescriptor::AttackFactions
		IL_0012: ldarg.1
		IL_0013: callvirt instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.BlueprintFaction, class Kingmaker.Blueprints.BlueprintFactionReference> Kingmaker.Blueprints.BlueprintFaction::get_AttackFactions()
		IL_0018: box valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.BlueprintFaction, class Kingmaker.Blueprints.BlueprintFactionReference>
		IL_001d: callvirt instance void Kingmaker.UnitLogic.UnitAttackFactions::Match(class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Blueprints.BlueprintFaction>)

		IL_0022: ret

		IL_0023: ldarg.2
		IL_0024: brfalse.s IL_003e

		IL_0026: ldarg.0
		IL_0027: ldfld class Kingmaker.UnitLogic.UnitAttackFactions Kingmaker.UnitLogic.UnitDescriptor::AttackFactions
		IL_002c: ldarg.1
		IL_002d: callvirt instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.BlueprintFaction, class Kingmaker.Blueprints.BlueprintFactionReference> Kingmaker.Blueprints.BlueprintFaction::get_AttackFactions()
		IL_0032: box valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.BlueprintFaction, class Kingmaker.Blueprints.BlueprintFactionReference>
		IL_0037: callvirt instance void Kingmaker.UnitLogic.UnitAttackFactions::Match(class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Blueprints.BlueprintFaction>)
		IL_003c: br.s IL_00a2

		IL_003e: ldarg.0
		IL_003f: ldfld class Kingmaker.UnitLogic.UnitAttackFactions Kingmaker.UnitLogic.UnitDescriptor::AttackFactions
		IL_0044: ldarg.0
		IL_0045: call instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_Faction()
		IL_004a: callvirt instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.BlueprintFaction, class Kingmaker.Blueprints.BlueprintFactionReference> Kingmaker.Blueprints.BlueprintFaction::get_AttackFactions()
		IL_004f: box valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.BlueprintFaction, class Kingmaker.Blueprints.BlueprintFactionReference>
		IL_0054: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> [System.Core]System.Linq.Enumerable::Except<class Kingmaker.Blueprints.BlueprintFaction>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>, class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
		IL_0059: call class [mscorlib]System.Collections.Generic.List`1<!!0> [System.Core]System.Linq.Enumerable::ToList<class Kingmaker.Blueprints.BlueprintFaction>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
		IL_005e: stloc.0
		IL_005f: ldarg.0
		IL_0060: call instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_Faction()
		IL_0065: callvirt instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.BlueprintFaction, class Kingmaker.Blueprints.BlueprintFactionReference> Kingmaker.Blueprints.BlueprintFaction::get_AttackFactions()
		IL_006a: box valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.BlueprintFaction, class Kingmaker.Blueprints.BlueprintFactionReference>
		IL_006f: ldarg.0
		IL_0070: ldfld class Kingmaker.UnitLogic.UnitAttackFactions Kingmaker.UnitLogic.UnitDescriptor::AttackFactions
		IL_0075: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> [System.Core]System.Linq.Enumerable::Except<class Kingmaker.Blueprints.BlueprintFaction>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>, class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
		IL_007a: call class [mscorlib]System.Collections.Generic.List`1<!!0> [System.Core]System.Linq.Enumerable::ToList<class Kingmaker.Blueprints.BlueprintFaction>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
		IL_007f: stloc.1
		IL_0080: ldarg.0
		IL_0081: ldfld class Kingmaker.UnitLogic.UnitAttackFactions Kingmaker.UnitLogic.UnitDescriptor::AttackFactions
		IL_0086: ldarg.1
		IL_0087: callvirt instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.BlueprintFaction, class Kingmaker.Blueprints.BlueprintFactionReference> Kingmaker.Blueprints.BlueprintFaction::get_AttackFactions()
		IL_008c: box valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.BlueprintFaction, class Kingmaker.Blueprints.BlueprintFactionReference>
		IL_0091: ldloc.1
		IL_0092: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> [System.Core]System.Linq.Enumerable::Except<class Kingmaker.Blueprints.BlueprintFaction>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>, class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
		IL_0097: ldloc.0
		IL_0098: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> [System.Core]System.Linq.Enumerable::Concat<class Kingmaker.Blueprints.BlueprintFaction>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>, class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
		IL_009d: callvirt instance void Kingmaker.UnitLogic.UnitAttackFactions::Match(class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Blueprints.BlueprintFaction>)

		IL_00a2: ldarg.0
		IL_00a3: ldarg.3
		IL_00a4: brtrue.s IL_00b8

		IL_00a6: ldarg.0
		IL_00a7: ldfld class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::m_FactionOriginal
		IL_00ac: dup
		IL_00ad: brtrue.s IL_00b9

		IL_00af: pop
		IL_00b0: ldarg.0
		IL_00b1: call instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_Faction()
		IL_00b6: br.s IL_00b9

		IL_00b8: ldarg.1

		IL_00b9: stfld class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::m_FactionOriginal
		IL_00be: ldarg.0
		IL_00bf: ldarg.1
		IL_00c0: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_Faction(class Kingmaker.Blueprints.BlueprintFaction)
		IL_00c5: ldarg.0
		IL_00c6: ldc.i4.0
		IL_00c7: call instance void Kingmaker.UnitLogic.UnitDescriptor::SetupInventory(bool)
		IL_00cc: ldarg.0
		IL_00cd: ldftn instance void Kingmaker.UnitLogic.UnitDescriptor::'<SwitchFactions>b__154_0'(class Kingmaker.PubSubSystem.IUnitFactionHandler)
		IL_00d3: newobj instance void class [mscorlib]System.Action`1<class Kingmaker.PubSubSystem.IUnitFactionHandler>::.ctor(object, native int)
		IL_00d8: ldc.i4.1
		IL_00d9: call bool Kingmaker.PubSubSystem.EventBus::RaiseEvent<class Kingmaker.PubSubSystem.IUnitFactionHandler>(class [mscorlib]System.Action`1<!!0>, bool)
		IL_00de: pop
		IL_00df: ldarg.0
		IL_00e0: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_00e5: callvirt instance class Kingmaker.UnitLogic.Groups.UnitGroup Kingmaker.EntitySystem.Entities.UnitEntityData::get_Group()
		IL_00ea: callvirt instance void Kingmaker.UnitLogic.Groups.UnitGroup::UpdateAttackFactionsCache()
		IL_00ef: ldarg.0
		IL_00f0: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_00f5: callvirt instance bool Kingmaker.EntitySystem.Entities.UnitEntityData::get_IsInCombat()
		IL_00fa: brfalse.s IL_0119

		IL_00fc: ldarg.0
		IL_00fd: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0102: callvirt instance class Kingmaker.UnitLogic.Groups.UnitGroup Kingmaker.EntitySystem.Entities.UnitEntityData::get_Group()
		IL_0107: callvirt instance bool Kingmaker.UnitLogic.Groups.UnitGroup::HasEnemyInCombat()
		IL_010c: brtrue.s IL_0119

		IL_010e: ldarg.0
		IL_010f: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0114: callvirt instance void Kingmaker.EntitySystem.Entities.UnitEntityData::LeaveCombat()

		IL_0119: call class Kingmaker.Game Kingmaker.Game::get_Instance()
		IL_011e: ldfld class Kingmaker.EntitySystem.PersistentState Kingmaker.Game::State
		IL_0123: ldfld class Kingmaker.EntitySystem.EntityPool`1<class Kingmaker.EntitySystem.Entities.UnitEntityData> Kingmaker.EntitySystem.PersistentState::Units
		IL_0128: callvirt instance valuetype Kingmaker.EntitySystem.EntityPoolEnumerator`1<!0> class Kingmaker.EntitySystem.EntityPool`1<class Kingmaker.EntitySystem.Entities.UnitEntityData>::GetEnumerator()
		IL_012d: stloc.2
		.try
		{
			IL_012e: br.s IL_0165
			// loop start (head: IL_0165)
				IL_0130: ldloca.s 2
				IL_0132: call instance !0 valuetype Kingmaker.EntitySystem.EntityPoolEnumerator`1<class Kingmaker.EntitySystem.Entities.UnitEntityData>::get_Current()
				IL_0137: callvirt instance !!0 Kingmaker.EntitySystem.EntityDataBase::Get<class Kingmaker.UnitLogic.Parts.UnitPartSummonedMonster>()
				IL_013c: stloc.3
				IL_013d: ldloc.3
				IL_013e: brfalse.s IL_0165

				IL_0140: ldloc.3
				IL_0141: callvirt instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.Parts.UnitPartSummonedMonster::get_Summoner()
				IL_0146: ldarg.0
				IL_0147: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
				IL_014c: call class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.EntitySystem.Entities.UnitEntityData::op_Implicit(class Kingmaker.EntitySystem.Entities.UnitEntityData)
				IL_0151: call bool Kingmaker.EntitySystem.Entities.UnitEntityData::op_Equality(class Kingmaker.EntitySystem.Entities.UnitEntityData, class Kingmaker.UnitLogic.UnitDescriptor)
				IL_0156: brfalse.s IL_0165

				IL_0158: ldloc.3
				IL_0159: callvirt instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.OldStyleUnitPart::get_Owner()
				IL_015e: ldarg.1
				IL_015f: ldarg.2
				IL_0160: callvirt instance void Kingmaker.UnitLogic.UnitDescriptor::SwitchFactions(class Kingmaker.Blueprints.BlueprintFaction, bool)

				IL_0165: ldloca.s 2
				IL_0167: call instance bool valuetype Kingmaker.EntitySystem.EntityPoolEnumerator`1<class Kingmaker.EntitySystem.Entities.UnitEntityData>::MoveNext()
				IL_016c: brtrue.s IL_0130
			// end loop

			IL_016e: leave.s IL_017e
		} // end .try
		finally
		{
			IL_0170: ldloca.s 2
			IL_0172: constrained. valuetype Kingmaker.EntitySystem.EntityPoolEnumerator`1<class Kingmaker.EntitySystem.Entities.UnitEntityData>
			IL_0178: callvirt instance void [mscorlib]System.IDisposable::Dispose()
			IL_017d: endfinally
		} // end handler

		IL_017e: ret
	} // end of method UnitDescriptor::SwitchFactions

	.method public hidebysig 
		instance void FixInventoryOnPlayerPostLoad () cil managed 
	{
		// Method begins at RVA 0x31b82c
		// Header size: 1
		// Code size: 36 (0x24)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsPlayerFaction()
		IL_0006: brfalse.s IL_001c

		IL_0008: ldarg.0
		IL_0009: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_000e: callvirt instance bool Kingmaker.EntitySystem.Entities.UnitEntityData::get_IsPet()
		IL_0013: brfalse.s IL_001c

		IL_0015: ldarg.0
		IL_0016: ldc.i4.0
		IL_0017: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_HasOwnInventory(bool)

		IL_001c: ldarg.0
		IL_001d: ldc.i4.1
		IL_001e: call instance void Kingmaker.UnitLogic.UnitDescriptor::SetupInventory(bool)
		IL_0023: ret
	} // end of method UnitDescriptor::FixInventoryOnPlayerPostLoad

	.method private hidebysig 
		instance void SetupInventory (
			[opt] bool restoreOnPlayerPostLoad
		) cil managed 
	{
		.param [1] = bool(false)
		// Method begins at RVA 0x31b854
		// Header size: 12
		// Code size: 277 (0x115)
		.maxstack 5
		.locals init (
			[0] class Kingmaker.Items.ItemsCollection,
			[1] class Kingmaker.Items.ItemsCollection/DoNotRemoveFromSlot,
			[2] class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Items.ItemEntity>,
			[3] class Kingmaker.Items.ItemEntity
		)

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::m_Inventory
		IL_0006: stloc.0
		IL_0007: ldarg.0
		IL_0008: call instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsPlayerFaction()
		IL_000d: brfalse.s IL_0029

		IL_000f: ldarg.0
		IL_0010: call instance bool Kingmaker.UnitLogic.UnitDescriptor::get_HasOwnInventory()
		IL_0015: brtrue.s IL_0029

		IL_0017: call class Kingmaker.Game Kingmaker.Game::get_Instance()
		IL_001c: callvirt instance class Kingmaker.Player Kingmaker.Game::get_Player()
		IL_0021: callvirt instance class Kingmaker.Items.ItemsCollection Kingmaker.Player::EnsureInventory()
		IL_0026: stloc.0
		IL_0027: br.s IL_004a

		IL_0029: ldarg.0
		IL_002a: ldfld class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::m_Inventory
		IL_002f: dup
		IL_0030: brtrue.s IL_0036

		IL_0032: pop
		IL_0033: ldnull
		IL_0034: br.s IL_003b

		IL_0036: call instance class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.Items.ItemsCollection::get_OwnerUnit()

		IL_003b: ldarg.0
		IL_003c: beq.s IL_004a

		IL_003e: ldarg.0
		IL_003f: call class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::op_Implicit(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_0044: newobj instance void Kingmaker.Items.ItemsCollection::.ctor(class Kingmaker.EntitySystem.EntityDataBase)
		IL_0049: stloc.0

		IL_004a: ldloc.0
		IL_004b: brtrue.s IL_0062

		IL_004d: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
		IL_0052: ldstr "New inventory is null"
		IL_0057: call !!0[] [mscorlib]System.Array::Empty<object>()
		IL_005c: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Error(string, object[])
		IL_0061: ret

		IL_0062: ldarg.0
		IL_0063: ldfld class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::m_Inventory
		IL_0068: ldloc.0
		IL_0069: bne.un.s IL_006c

		IL_006b: ret

		IL_006c: ldarg.1
		IL_006d: brfalse.s IL_0095

		IL_006f: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
		IL_0074: ldarg.0
		IL_0075: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_OriginalBlueprint()
		IL_007a: ldstr "Fix inventory for unit {0} (faction: {1})"
		IL_007f: ldarg.0
		IL_0080: ldarg.0
		IL_0081: call instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_Faction()
		IL_0086: call string [mscorlib]System.String::Format(string, object, object)
		IL_008b: call !!0[] [mscorlib]System.Array::Empty<object>()
		IL_0090: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Error(class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.ICanBeLogContext, string, object[])

		IL_0095: ldarg.0
		IL_0096: ldloc.0
		IL_0097: stfld class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::m_Inventory
		IL_009c: call !0 class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.Items.ItemsCollection/DoNotRemoveFromSlot>::Request()
		IL_00a1: stloc.1
		.try
		{
			IL_00a2: ldarg.0
			IL_00a3: call instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
			IL_00a8: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Items.ItemEntity> Kingmaker.Items.UnitBody::get_Items()
			IL_00ad: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<!0> class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Items.ItemEntity>::GetEnumerator()
			IL_00b2: stloc.2
			.try
			{
				IL_00b3: br.s IL_00f6
				// loop start (head: IL_00f6)
					IL_00b5: ldloc.2
					IL_00b6: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Items.ItemEntity>::get_Current()
					IL_00bb: stloc.3
					IL_00bc: ldloc.3
					IL_00bd: callvirt instance class Kingmaker.Items.ItemsCollection Kingmaker.Items.ItemEntity::get_Collection()
					IL_00c2: brfalse.s IL_00f6

					IL_00c4: ldloc.3
					IL_00c5: callvirt instance class Kingmaker.Items.ItemsCollection Kingmaker.Items.ItemEntity::get_Collection()
					IL_00ca: ldloc.0
					IL_00cb: beq.s IL_00f6

					IL_00cd: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
					IL_00d2: ldstr "{0}: move item {1} to actual inventory"
					IL_00d7: ldarg.0
					IL_00d8: ldloc.3
					IL_00d9: call string [mscorlib]System.String::Format(string, object, object)
					IL_00de: call !!0[] [mscorlib]System.Array::Empty<object>()
					IL_00e3: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Log(string, object[])
					IL_00e8: ldloc.3
					IL_00e9: callvirt instance class Kingmaker.Items.ItemsCollection Kingmaker.Items.ItemEntity::get_Collection()
					IL_00ee: ldloc.3
					IL_00ef: ldloc.0
					IL_00f0: callvirt instance class Kingmaker.Items.ItemEntity Kingmaker.Items.ItemsCollection::Transfer(class Kingmaker.Items.ItemEntity, class Kingmaker.Items.ItemsCollection)
					IL_00f5: pop

					IL_00f6: ldloc.2
					IL_00f7: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
					IL_00fc: brtrue.s IL_00b5
				// end loop

				IL_00fe: leave.s IL_0114
			} // end .try
			finally
			{
				IL_0100: ldloc.2
				IL_0101: brfalse.s IL_0109

				IL_0103: ldloc.2
				IL_0104: callvirt instance void [mscorlib]System.IDisposable::Dispose()

				IL_0109: endfinally
			} // end handler
		} // end .try
		finally
		{
			IL_010a: ldloc.1
			IL_010b: brfalse.s IL_0113

			IL_010d: ldloc.1
			IL_010e: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_0113: endfinally
		} // end handler

		IL_0114: ret
	} // end of method UnitDescriptor::SetupInventory

	.method public hidebysig 
		instance void SetFakeBlueprint (
			class Kingmaker.Blueprints.BlueprintUnit fake
		) cil managed 
	{
		.param [1]
			.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
				01 00 00 00
			)
		// Method begins at RVA 0x31b994
		// Header size: 1
		// Code size: 24 (0x18)
		.maxstack 8

		IL_0000: ldarg.1
		IL_0001: brtrue.s IL_0010

		IL_0003: ldarg.0
		IL_0004: ldarg.0
		IL_0005: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_OriginalBlueprint()
		IL_000a: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_Blueprint(class Kingmaker.Blueprints.BlueprintUnit)
		IL_000f: ret

		IL_0010: ldarg.0
		IL_0011: ldarg.1
		IL_0012: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_Blueprint(class Kingmaker.Blueprints.BlueprintUnit)
		IL_0017: ret
	} // end of method UnitDescriptor::SetFakeBlueprint

	.method public hidebysig specialname rtspecialname 
		instance void .ctor (
			class Kingmaker.Blueprints.BlueprintUnit blueprint,
			class Kingmaker.EntitySystem.Entities.UnitEntityData data
		) cil managed 
	{
		// Method begins at RVA 0x31b9b0
		// Header size: 12
		// Code size: 345 (0x159)
		.maxstack 4
		.locals init (
			[0] class Kingmaker.View.Spawners.UnitSpawningData,
			[1] class Kingmaker.Blueprints.BlueprintUnit
		)

		IL_0000: ldarg.0
		IL_0001: newobj instance void class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::.ctor()
		IL_0006: stfld class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::m_Spellbooks
		IL_000b: ldarg.0
		IL_000c: newobj instance void Kingmaker.UnitLogic.UnitProficiency::.ctor()
		IL_0011: stfld class Kingmaker.UnitLogic.UnitProficiency Kingmaker.UnitLogic.UnitDescriptor::Proficiencies
		IL_0016: ldarg.0
		IL_0017: ldstr ""
		IL_001c: stfld string Kingmaker.UnitLogic.UnitDescriptor::CustomName
		IL_0021: ldarg.0
		IL_0022: ldc.i4.m1
		IL_0023: stfld int32 Kingmaker.UnitLogic.UnitDescriptor::BirthDay
		IL_0028: ldarg.0
		IL_0029: ldc.i4.m1
		IL_002a: stfld int32 Kingmaker.UnitLogic.UnitDescriptor::BirthMonth
		IL_002f: ldarg.0
		IL_0030: ldstr ""
		IL_0035: stfld string Kingmaker.UnitLogic.UnitDescriptor::CustomPrefabGuid
		IL_003a: ldarg.0
		IL_003b: newobj instance void Kingmaker.Utility.CountableFlag::.ctor()
		IL_0040: stfld class Kingmaker.Utility.CountableFlag Kingmaker.UnitLogic.UnitDescriptor::m_IsEssentialForGame
		IL_0045: ldarg.0
		IL_0046: newobj instance void class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher>::.ctor()
		IL_004b: stfld class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher> Kingmaker.UnitLogic.UnitDescriptor::FactionSwitchers
		IL_0050: ldarg.0
		IL_0051: call instance void [mscorlib]System.Object::.ctor()
		IL_0056: call !0 class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.View.Spawners.UnitSpawningData>::get_Current()
		IL_005b: stloc.0
		IL_005c: ldarg.0
		IL_005d: ldarg.2
		IL_005e: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_Unit(class Kingmaker.EntitySystem.Entities.UnitEntityData)
		IL_0063: ldarg.0
		IL_0064: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0069: ldarg.0
		IL_006a: callvirt instance void Kingmaker.EntitySystem.Entities.UnitEntityData::set_Descriptor(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_006f: ldarg.0
		IL_0070: ldarg.0
		IL_0071: ldarg.1
		IL_0072: dup
		IL_0073: stloc.1
		IL_0074: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_OriginalBlueprint(class Kingmaker.Blueprints.BlueprintUnit)
		IL_0079: ldloc.1
		IL_007a: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_Blueprint(class Kingmaker.Blueprints.BlueprintUnit)
		IL_007f: ldarg.0
		IL_0080: ldarg.1
		IL_0081: callvirt instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.Blueprints.BlueprintUnit::get_Faction()
		IL_0086: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_Faction(class Kingmaker.Blueprints.BlueprintFaction)
		IL_008b: ldarg.0
		IL_008c: ldarg.0
		IL_008d: newobj instance void Kingmaker.UnitLogic.UnitAttackFactions::.ctor(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_0092: stfld class Kingmaker.UnitLogic.UnitAttackFactions Kingmaker.UnitLogic.UnitDescriptor::AttackFactions
		IL_0097: ldarg.0
		IL_0098: ldarg.0
		IL_0099: newobj instance void Kingmaker.EntitySystem.Stats.CharacterStats::.ctor(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_009e: stfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_00a3: ldarg.0
		IL_00a4: ldloc.0
		IL_00a5: brtrue.s IL_00aa

		IL_00a7: ldnull
		IL_00a8: br.s IL_00b0

		IL_00aa: ldloc.0
		IL_00ab: call instance class Kingmaker.Items.ItemsCollection Kingmaker.View.Spawners.UnitSpawningData::get_Inventory()

		IL_00b0: dup
		IL_00b1: brtrue.s IL_00d8

		IL_00b3: pop
		IL_00b4: ldarg.0
		IL_00b5: call instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsPlayerFaction()
		IL_00ba: brtrue.s IL_00c9

		IL_00bc: ldarg.0
		IL_00bd: call class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::op_Implicit(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_00c2: newobj instance void Kingmaker.Items.ItemsCollection::.ctor(class Kingmaker.EntitySystem.EntityDataBase)
		IL_00c7: br.s IL_00d8

		IL_00c9: call class Kingmaker.Game Kingmaker.Game::get_Instance()
		IL_00ce: callvirt instance class Kingmaker.Player Kingmaker.Game::get_Player()
		IL_00d3: callvirt instance class Kingmaker.Items.ItemsCollection Kingmaker.Player::EnsureInventory()

		IL_00d8: stfld class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::m_Inventory
		IL_00dd: ldarg.0
		IL_00de: ldarg.0
		IL_00df: newobj instance void Kingmaker.UnitLogic.UnitProgressionData::.ctor(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_00e4: stfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_00e9: ldarg.0
		IL_00ea: ldloc.0
		IL_00eb: brtrue.s IL_00f0

		IL_00ed: ldnull
		IL_00ee: br.s IL_00f6

		IL_00f0: ldloc.0
		IL_00f1: call instance class Kingmaker.Items.UnitBody Kingmaker.View.Spawners.UnitSpawningData::get_Body()

		IL_00f6: dup
		IL_00f7: brtrue.s IL_0100

		IL_00f9: pop
		IL_00fa: ldarg.0
		IL_00fb: newobj instance void Kingmaker.Items.UnitBody::.ctor(class Kingmaker.UnitLogic.UnitDescriptor)

		IL_0100: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_Body(class Kingmaker.Items.UnitBody)
		IL_0105: ldarg.0
		IL_0106: ldarg.0
		IL_0107: newobj instance void Kingmaker.UnitLogic.UnitBrain::.ctor(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_010c: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_Brain(class Kingmaker.UnitLogic.UnitBrain)
		IL_0111: ldarg.0
		IL_0112: ldarg.0
		IL_0113: newobj instance void Kingmaker.UnitLogic.UnitAbilityResourceCollection::.ctor(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_0118: stfld class Kingmaker.UnitLogic.UnitAbilityResourceCollection Kingmaker.UnitLogic.UnitDescriptor::Resources
		IL_011d: ldarg.0
		IL_011e: ldarg.0
		IL_011f: newobj instance void Kingmaker.UnitLogic.UnitState::.ctor(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_0124: stfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_0129: ldarg.0
		IL_012a: ldarg.0
		IL_012b: newobj instance void Kingmaker.UnitLogic.Alignments.UnitAlignment::.ctor(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_0130: stfld class Kingmaker.UnitLogic.Alignments.UnitAlignment Kingmaker.UnitLogic.UnitDescriptor::Alignment
		IL_0135: ldarg.0
		IL_0136: ldarg.0
		IL_0137: newobj instance void Kingmaker.UI.UnitSettings.UnitUISettings::.ctor(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_013c: stfld class Kingmaker.UI.UnitSettings.UnitUISettings Kingmaker.UnitLogic.UnitDescriptor::UISettings
		IL_0141: ldarg.0
		IL_0142: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()
		IL_0147: ldarg.0
		IL_0148: ldftn instance void Kingmaker.UnitLogic.UnitDescriptor::'<.ctor>b__158_0'(class Kingmaker.UnitLogic.Mechanics.Components.Fixers.FixUnitOnPostLoad)
		IL_014e: newobj instance void class [mscorlib]System.Action`1<class Kingmaker.UnitLogic.Mechanics.Components.Fixers.FixUnitOnPostLoad>::.ctor(object, native int)
		IL_0153: call void Kingmaker.Blueprints.BlueprintExtenstions::CallComponents<class Kingmaker.UnitLogic.Mechanics.Components.Fixers.FixUnitOnPostLoad>(class Kingmaker.Blueprints.BlueprintScriptableObject, class [mscorlib]System.Action`1<!!0>)
		IL_0158: ret
	} // end of method UnitDescriptor::.ctor

	.method public hidebysig 
		instance void EnsureOwnInventory () cil managed 
	{
		// Method begins at RVA 0x31bb15
		// Header size: 1
		// Code size: 28 (0x1c)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::m_Inventory
		IL_0006: callvirt instance bool Kingmaker.Items.ItemsCollection::get_IsPlayerInventory()
		IL_000b: brfalse.s IL_001b

		IL_000d: ldarg.0
		IL_000e: ldc.i4.1
		IL_000f: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_HasOwnInventory(bool)
		IL_0014: ldarg.0
		IL_0015: ldc.i4.0
		IL_0016: call instance void Kingmaker.UnitLogic.UnitDescriptor::SetupInventory(bool)

		IL_001b: ret
	} // end of method UnitDescriptor::EnsureOwnInventory

	.method public hidebysig 
		instance void SetupSharedInventoryForPet () cil managed 
	{
		// Method begins at RVA 0x31bb32
		// Header size: 1
		// Code size: 36 (0x24)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsPlayerFaction()
		IL_0006: brfalse.s IL_0023

		IL_0008: ldarg.0
		IL_0009: ldfld class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::m_Inventory
		IL_000e: callvirt instance bool Kingmaker.Items.ItemsCollection::get_IsPlayerInventory()
		IL_0013: brtrue.s IL_0023

		IL_0015: ldarg.0
		IL_0016: ldc.i4.0
		IL_0017: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_HasOwnInventory(bool)
		IL_001c: ldarg.0
		IL_001d: ldc.i4.0
		IL_001e: call instance void Kingmaker.UnitLogic.UnitDescriptor::SetupInventory(bool)

		IL_0023: ret
	} // end of method UnitDescriptor::SetupSharedInventoryForPet

	.method public hidebysig virtual 
		instance string ToString () cil managed 
	{
		// Method begins at RVA 0x31bb57
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_OriginalBlueprint()
		IL_0006: callvirt instance string [mscorlib]System.Object::ToString()
		IL_000b: ret
	} // end of method UnitDescriptor::ToString

	.method private hidebysig specialname rtspecialname 
		instance void .ctor (
			valuetype Kingmaker.EntitySystem.Persistence.JsonUtility.JsonConstructorMark _
		) cil managed 
	{
		.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.UsedImplicitlyAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31bb64
		// Header size: 12
		// Code size: 87 (0x57)
		.maxstack 2

		IL_0000: ldarg.0
		IL_0001: newobj instance void class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::.ctor()
		IL_0006: stfld class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::m_Spellbooks
		IL_000b: ldarg.0
		IL_000c: newobj instance void Kingmaker.UnitLogic.UnitProficiency::.ctor()
		IL_0011: stfld class Kingmaker.UnitLogic.UnitProficiency Kingmaker.UnitLogic.UnitDescriptor::Proficiencies
		IL_0016: ldarg.0
		IL_0017: ldstr ""
		IL_001c: stfld string Kingmaker.UnitLogic.UnitDescriptor::CustomName
		IL_0021: ldarg.0
		IL_0022: ldc.i4.m1
		IL_0023: stfld int32 Kingmaker.UnitLogic.UnitDescriptor::BirthDay
		IL_0028: ldarg.0
		IL_0029: ldc.i4.m1
		IL_002a: stfld int32 Kingmaker.UnitLogic.UnitDescriptor::BirthMonth
		IL_002f: ldarg.0
		IL_0030: ldstr ""
		IL_0035: stfld string Kingmaker.UnitLogic.UnitDescriptor::CustomPrefabGuid
		IL_003a: ldarg.0
		IL_003b: newobj instance void Kingmaker.Utility.CountableFlag::.ctor()
		IL_0040: stfld class Kingmaker.Utility.CountableFlag Kingmaker.UnitLogic.UnitDescriptor::m_IsEssentialForGame
		IL_0045: ldarg.0
		IL_0046: newobj instance void class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher>::.ctor()
		IL_004b: stfld class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.UnitDescriptor/FactionSwitcher> Kingmaker.UnitLogic.UnitDescriptor::FactionSwitchers
		IL_0050: ldarg.0
		IL_0051: call instance void [mscorlib]System.Object::.ctor()
		IL_0056: ret
	} // end of method UnitDescriptor::.ctor

	.method public hidebysig 
		instance void Initialize () cil managed 
	{
		// Method begins at RVA 0x31bbc7
		// Header size: 1
		// Code size: 13 (0xd)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.0
		IL_0002: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_OriginalBlueprint()
		IL_0007: call void Kingmaker.UnitLogic.UnitDescriptor::Initialize(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.BlueprintUnit)
		IL_000c: ret
	} // end of method UnitDescriptor::Initialize

	.method private hidebysig static 
		void Initialize (
			class Kingmaker.UnitLogic.UnitDescriptor unit,
			class Kingmaker.Blueprints.BlueprintUnit blueprint
		) cil managed 
	{
		// Method begins at RVA 0x31bbd8
		// Header size: 12
		// Code size: 1502 (0x5de)
		.maxstack 5
		.locals init (
			[0] class Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0',
			[1] bool,
			[2] bool,
			[3] class Kingmaker.View.Spawners.UnitSpawningData,
			[4] valuetype [mscorlib]System.Nullable`1<valuetype Kingmaker.Blueprints.Gender>,
			[5] valuetype [mscorlib]System.Nullable`1<bool>,
			[6] class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Blueprints.Facts.BlueprintUnitFact>,
			[7] class Kingmaker.Blueprints.Facts.BlueprintUnitFact,
			[8] class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Blueprints.BlueprintUnitTemplate>,
			[9] class Kingmaker.Blueprints.BlueprintUnitTemplate,
			[10] class [mscorlib]System.IDisposable,
			[11] class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Spellbook>
		)

		IL_0000: newobj instance void Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::.ctor()
		IL_0005: stloc.0
		IL_0006: ldloc.0
		IL_0007: ldarg.0
		IL_0008: stfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_000d: ldarg.1
		IL_000e: brtrue.s IL_0025

		IL_0010: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
		IL_0015: ldstr "Unit created without blueprint"
		IL_001a: call !!0[] [mscorlib]System.Array::Empty<object>()
		IL_001f: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Error(string, object[])
		IL_0024: ret

		IL_0025: ldloc.0
		IL_0026: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_002b: callvirt instance !!0 Kingmaker.UnitLogic.UnitDescriptor::Ensure<class Kingmaker.UnitLogic.Parts.LevelUpPlanUnitHolder>()
		IL_0030: pop
		IL_0031: ldloc.0
		IL_0032: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0037: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_003c: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueHitPoints Kingmaker.EntitySystem.Stats.CharacterStats::HitPoints
		IL_0041: ldarg.1
		IL_0042: ldfld int32 Kingmaker.Blueprints.BlueprintUnit::MaxHP
		IL_0047: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_004c: ldloc.0
		IL_004d: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0052: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0057: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat Kingmaker.EntitySystem.Stats.CharacterStats::Strength
		IL_005c: ldarg.1
		IL_005d: ldfld int32 Kingmaker.Blueprints.BlueprintUnit::Strength
		IL_0062: call void Kingmaker.UnitLogic.UnitDescriptor::InitializeStat(class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat, int32)
		IL_0067: ldloc.0
		IL_0068: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_006d: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0072: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat Kingmaker.EntitySystem.Stats.CharacterStats::Dexterity
		IL_0077: ldarg.1
		IL_0078: ldfld int32 Kingmaker.Blueprints.BlueprintUnit::Dexterity
		IL_007d: call void Kingmaker.UnitLogic.UnitDescriptor::InitializeStat(class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat, int32)
		IL_0082: ldloc.0
		IL_0083: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0088: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_008d: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat Kingmaker.EntitySystem.Stats.CharacterStats::Constitution
		IL_0092: ldarg.1
		IL_0093: ldfld int32 Kingmaker.Blueprints.BlueprintUnit::Constitution
		IL_0098: call void Kingmaker.UnitLogic.UnitDescriptor::InitializeStat(class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat, int32)
		IL_009d: ldloc.0
		IL_009e: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_00a3: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_00a8: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat Kingmaker.EntitySystem.Stats.CharacterStats::Intelligence
		IL_00ad: ldarg.1
		IL_00ae: ldfld int32 Kingmaker.Blueprints.BlueprintUnit::Intelligence
		IL_00b3: call void Kingmaker.UnitLogic.UnitDescriptor::InitializeStat(class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat, int32)
		IL_00b8: ldloc.0
		IL_00b9: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_00be: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_00c3: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat Kingmaker.EntitySystem.Stats.CharacterStats::Wisdom
		IL_00c8: ldarg.1
		IL_00c9: ldfld int32 Kingmaker.Blueprints.BlueprintUnit::Wisdom
		IL_00ce: call void Kingmaker.UnitLogic.UnitDescriptor::InitializeStat(class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat, int32)
		IL_00d3: ldloc.0
		IL_00d4: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_00d9: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_00de: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat Kingmaker.EntitySystem.Stats.CharacterStats::Charisma
		IL_00e3: ldarg.1
		IL_00e4: ldfld int32 Kingmaker.Blueprints.BlueprintUnit::Charisma
		IL_00e9: call void Kingmaker.UnitLogic.UnitDescriptor::InitializeStat(class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat, int32)
		IL_00ee: ldloc.0
		IL_00ef: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_00f4: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_00f9: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSpeed Kingmaker.EntitySystem.Stats.CharacterStats::Speed
		IL_00fe: ldarg.1
		IL_00ff: ldflda valuetype Kingmaker.Utility.Feet Kingmaker.Blueprints.BlueprintUnit::Speed
		IL_0104: call instance int32 Kingmaker.Utility.Feet::get_Value()
		IL_0109: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_010e: ldloc.0
		IL_010f: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0114: ldarg.1
		IL_0115: ldfld class Kingmaker.Blueprints.BlueprintUnit/UnitSkills Kingmaker.Blueprints.BlueprintUnit::Skills
		IL_011a: callvirt instance void Kingmaker.UnitLogic.UnitDescriptor::SetSkills(class Kingmaker.Blueprints.BlueprintUnit/UnitSkills)
		IL_011f: ldloc.0
		IL_0120: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0125: callvirt instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsPlayerFaction()
		IL_012a: brtrue.s IL_0138

		IL_012c: ldloc.0
		IL_012d: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0132: ldc.i4.1
		IL_0133: callvirt instance void Kingmaker.UnitLogic.UnitDescriptor::set_HasOwnInventory(bool)

		IL_0138: ldloc.0
		IL_0139: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_013e: callvirt instance void Kingmaker.UnitLogic.UnitDescriptor::EnsureNaturalProficiencies()
		IL_0143: ldloc.0
		IL_0144: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0149: ldfld class Kingmaker.UnitLogic.Alignments.UnitAlignment Kingmaker.UnitLogic.UnitDescriptor::Alignment
		IL_014e: ldarg.1
		IL_014f: ldfld valuetype Kingmaker.Enums.Alignment Kingmaker.Blueprints.BlueprintUnit::Alignment
		IL_0154: callvirt instance void Kingmaker.UnitLogic.Alignments.UnitAlignment::Initialize(valuetype Kingmaker.Enums.Alignment)
		IL_0159: ldc.i4.1
		IL_015a: stloc.1
		IL_015b: ldc.i4.1
		IL_015c: stloc.2
		IL_015d: call !0 class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.View.Spawners.UnitSpawningData>::get_Current()
		IL_0162: stloc.3
		IL_0163: ldloc.3
		IL_0164: brfalse IL_026b

		IL_0169: ldloc.3
		IL_016a: callvirt instance class Kingmaker.Blueprints.Classes.BlueprintRace Kingmaker.View.Spawners.UnitSpawningData::get_Race()
		IL_016f: brfalse.s IL_0187

		IL_0171: ldloc.0
		IL_0172: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0177: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_017c: ldloc.3
		IL_017d: callvirt instance class Kingmaker.Blueprints.Classes.BlueprintRace Kingmaker.View.Spawners.UnitSpawningData::get_Race()
		IL_0182: callvirt instance void Kingmaker.UnitLogic.UnitProgressionData::SetRace(class Kingmaker.Blueprints.Classes.BlueprintRace)

		IL_0187: ldloc.3
		IL_0188: callvirt instance class Kingmaker.Visual.Sound.BlueprintUnitAsksList Kingmaker.View.Spawners.UnitSpawningData::get_Voice()
		IL_018d: brfalse.s IL_01a0

		IL_018f: ldloc.0
		IL_0190: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0195: ldloc.3
		IL_0196: callvirt instance class Kingmaker.Visual.Sound.BlueprintUnitAsksList Kingmaker.View.Spawners.UnitSpawningData::get_Voice()
		IL_019b: stfld class Kingmaker.Visual.Sound.BlueprintUnitAsksList Kingmaker.UnitLogic.UnitDescriptor::CustomAsks

		IL_01a0: ldloc.3
		IL_01a1: callvirt instance valuetype [mscorlib]System.Nullable`1<valuetype Kingmaker.Blueprints.Gender> Kingmaker.View.Spawners.UnitSpawningData::get_Gender()
		IL_01a6: stloc.s 4
		IL_01a8: ldloca.s 4
		IL_01aa: call instance bool valuetype [mscorlib]System.Nullable`1<valuetype Kingmaker.Blueprints.Gender>::get_HasValue()
		IL_01af: brfalse.s IL_01c2

		IL_01b1: ldloc.0
		IL_01b2: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_01b7: ldloc.3
		IL_01b8: callvirt instance valuetype [mscorlib]System.Nullable`1<valuetype Kingmaker.Blueprints.Gender> Kingmaker.View.Spawners.UnitSpawningData::get_Gender()
		IL_01bd: stfld valuetype [mscorlib]System.Nullable`1<valuetype Kingmaker.Blueprints.Gender> Kingmaker.UnitLogic.UnitDescriptor::CustomGender

		IL_01c2: ldloc.3
		IL_01c3: callvirt instance valuetype [mscorlib]System.Nullable`1<bool> Kingmaker.View.Spawners.UnitSpawningData::get_LeftHanded()
		IL_01c8: stloc.s 5
		IL_01ca: ldloca.s 5
		IL_01cc: call instance bool valuetype [mscorlib]System.Nullable`1<bool>::get_HasValue()
		IL_01d1: brfalse.s IL_01e4

		IL_01d3: ldloc.0
		IL_01d4: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_01d9: ldloc.3
		IL_01da: callvirt instance valuetype [mscorlib]System.Nullable`1<bool> Kingmaker.View.Spawners.UnitSpawningData::get_LeftHanded()
		IL_01df: stfld valuetype [mscorlib]System.Nullable`1<bool> Kingmaker.UnitLogic.UnitDescriptor::LeftHandedOverride

		IL_01e4: ldloc.0
		IL_01e5: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_01ea: callvirt instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		IL_01ef: callvirt instance bool Kingmaker.Items.UnitBody::get_IsPolymorphed()
		IL_01f4: brtrue.s IL_0207

		IL_01f6: ldloc.0
		IL_01f7: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_01fc: ldloc.3
		IL_01fd: callvirt instance string Kingmaker.View.Spawners.UnitSpawningData::get_PrefabGuid()
		IL_0202: stfld string Kingmaker.UnitLogic.UnitDescriptor::CustomPrefabGuid

		IL_0207: ldloc.3
		IL_0208: callvirt instance class Kingmaker.Items.ItemsCollection Kingmaker.View.Spawners.UnitSpawningData::get_Inventory()
		IL_020d: brtrue.s IL_021a

		IL_020f: ldloc.3
		IL_0210: callvirt instance bool Kingmaker.View.Spawners.UnitSpawningData::get_IsFromPlaceholder()
		IL_0215: ldc.i4.0
		IL_0216: ceq
		IL_0218: br.s IL_021b

		IL_021a: ldc.i4.0

		IL_021b: stloc.1
		IL_021c: ldloc.3
		IL_021d: callvirt instance class Kingmaker.Items.UnitBody Kingmaker.View.Spawners.UnitSpawningData::get_Body()
		IL_0222: ldnull
		IL_0223: ceq
		IL_0225: stloc.2
		IL_0226: ldloc.3
		IL_0227: callvirt instance class Kingmaker.Items.UnitBody Kingmaker.View.Spawners.UnitSpawningData::get_Body()
		IL_022c: dup
		IL_022d: brtrue.s IL_0232

		IL_022f: pop
		IL_0230: br.s IL_023d

		IL_0232: ldloc.0
		IL_0233: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0238: call instance void Kingmaker.Items.UnitBody::SetOwner(class Kingmaker.UnitLogic.UnitDescriptor)

		IL_023d: ldloc.3
		IL_023e: callvirt instance class Kingmaker.Items.ItemsCollection Kingmaker.View.Spawners.UnitSpawningData::get_Inventory()
		IL_0243: dup
		IL_0244: brtrue.s IL_0249

		IL_0246: pop
		IL_0247: br.s IL_0254

		IL_0249: ldloc.0
		IL_024a: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_024f: call instance void Kingmaker.Items.ItemsCollection::SetOwner(class Kingmaker.UnitLogic.UnitDescriptor)

		IL_0254: ldloc.3
		IL_0255: callvirt instance class Kingmaker.Items.UnitBody Kingmaker.View.Spawners.UnitSpawningData::get_Body()
		IL_025a: dup
		IL_025b: brtrue.s IL_0260

		IL_025d: pop
		IL_025e: br.s IL_026b

		IL_0260: ldloc.0
		IL_0261: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0266: call instance void Kingmaker.Items.UnitBody::PrePostLoad(class Kingmaker.UnitLogic.UnitDescriptor)

		IL_026b: ldloc.0
		IL_026c: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0271: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_0276: callvirt instance class Kingmaker.Blueprints.Classes.BlueprintRace Kingmaker.UnitLogic.UnitProgressionData::get_Race()
		IL_027b: brtrue.s IL_029b

		IL_027d: ldarg.1
		IL_027e: callvirt instance class Kingmaker.Blueprints.Classes.BlueprintRace Kingmaker.Blueprints.BlueprintUnit::get_Race()
		IL_0283: brfalse.s IL_029b

		IL_0285: ldloc.0
		IL_0286: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_028b: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_0290: ldarg.1
		IL_0291: callvirt instance class Kingmaker.Blueprints.Classes.BlueprintRace Kingmaker.Blueprints.BlueprintUnit::get_Race()
		IL_0296: callvirt instance void Kingmaker.UnitLogic.UnitProgressionData::SetRace(class Kingmaker.Blueprints.Classes.BlueprintRace)

		IL_029b: ldloc.0
		IL_029c: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_02a1: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_02a6: ldloc.0
		IL_02a7: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_02ac: callvirt instance valuetype Kingmaker.Enums.Size Kingmaker.UnitLogic.UnitDescriptor::get_OriginalSize()
		IL_02b1: callvirt instance void Kingmaker.UnitLogic.UnitState::set_Size(valuetype Kingmaker.Enums.Size)
		IL_02b6: ldloc.0
		IL_02b7: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_02bc: callvirt instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_Faction()
		IL_02c1: call bool Kingmaker.Blueprints.SimpleBlueprint::op_Implicit(class Kingmaker.Blueprints.SimpleBlueprint)
		IL_02c6: brtrue.s IL_02ef

		IL_02c8: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
		IL_02cd: ldarg.1
		IL_02ce: ldstr "Faction not set for "
		IL_02d3: ldarg.1
		IL_02d4: dup
		IL_02d5: brtrue.s IL_02db

		IL_02d7: pop
		IL_02d8: ldnull
		IL_02d9: br.s IL_02e0

		IL_02db: callvirt instance string [mscorlib]System.Object::ToString()

		IL_02e0: call string [mscorlib]System.String::Concat(string, string)
		IL_02e5: call !!0[] [mscorlib]System.Array::Empty<object>()
		IL_02ea: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Error(class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.ICanBeLogContext, string, object[])

		IL_02ef: ldloc.0
		IL_02f0: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_02f5: ldfld class Kingmaker.UnitLogic.UnitAttackFactions Kingmaker.UnitLogic.UnitDescriptor::AttackFactions
		IL_02fa: ldarg.1
		IL_02fb: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Blueprints.BlueprintFaction> Kingmaker.Blueprints.BlueprintUnit::get_AttackFactions()
		IL_0300: callvirt instance void Kingmaker.UnitLogic.UnitAttackFactions::UnionWith(class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Blueprints.BlueprintFaction>)
		IL_0305: ldloc.0
		IL_0306: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_030b: ldloc.0
		IL_030c: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0311: callvirt instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0316: ldfld class Kingmaker.EntitySystem.EntityFactsManager Kingmaker.EntitySystem.EntityDataBase::Facts
		IL_031b: ldarg.1
		IL_031c: newobj instance void Kingmaker.UnitLogic.MainUnitFact::.ctor(class Kingmaker.Blueprints.BlueprintUnit)
		IL_0321: callvirt instance !!0 Kingmaker.EntitySystem.EntityFactsManager::Add<class Kingmaker.UnitLogic.MainUnitFact>(!!0)
		IL_0326: callvirt instance void Kingmaker.UnitLogic.UnitDescriptor::set_MainFact(class Kingmaker.UnitLogic.UnitFact)
		IL_032b: ldloc.0
		IL_032c: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0331: call class Kingmaker.Blueprints.Root.BlueprintRoot Kingmaker.Blueprints.Root.BlueprintRoot::get_Instance()
		IL_0336: ldfld class Kingmaker.Blueprints.Root.SystemMechanicsRoot Kingmaker.Blueprints.Root.BlueprintRoot::SystemMechanics
		IL_033b: callvirt instance class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility Kingmaker.Blueprints.Root.SystemMechanicsRoot::get_ChargeAbility()
		IL_0340: ldnull
		IL_0341: ldnull
		IL_0342: call class Kingmaker.EntitySystem.EntityFact Kingmaker.UnitLogic.UnitHelper::AddFact(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.Facts.BlueprintUnitFact, class Kingmaker.UnitLogic.Mechanics.MechanicsContext, class Kingmaker.Blueprints.Classes.Selection.FeatureParam)
		IL_0347: pop
		IL_0348: ldarg.1
		IL_0349: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> Kingmaker.Blueprints.BlueprintExtenstions::GetComponents<class Kingmaker.UnitLogic.FactLogic.AddAbilityToCharacterComponent>(class Kingmaker.Blueprints.BlueprintScriptableObject)
		IL_034e: ldsfld class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.FactLogic.AddAbilityToCharacterComponent, class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility>> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9__164_0'
		IL_0353: dup
		IL_0354: brtrue.s IL_036d

		IL_0356: pop
		IL_0357: ldsfld class Kingmaker.UnitLogic.UnitDescriptor/'<>c' Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9'
		IL_035c: ldftn instance class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<Initialize>b__164_0'(class Kingmaker.UnitLogic.FactLogic.AddAbilityToCharacterComponent)
		IL_0362: newobj instance void class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.FactLogic.AddAbilityToCharacterComponent, class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility>>::.ctor(object, native int)
		IL_0367: dup
		IL_0368: stsfld class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.FactLogic.AddAbilityToCharacterComponent, class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility>> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9__164_0'

		IL_036d: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!1> [System.Core]System.Linq.Enumerable::SelectMany<class Kingmaker.UnitLogic.FactLogic.AddAbilityToCharacterComponent, class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>, class [mscorlib]System.Func`2<!!0, class [mscorlib]System.Collections.Generic.IEnumerable`1<!!1>>)
		IL_0372: ldsfld class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility, bool> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9__164_1'
		IL_0377: dup
		IL_0378: brtrue.s IL_0391

		IL_037a: pop
		IL_037b: ldsfld class Kingmaker.UnitLogic.UnitDescriptor/'<>c' Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9'
		IL_0380: ldftn instance bool Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<Initialize>b__164_1'(class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility)
		IL_0386: newobj instance void class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility, bool>::.ctor(object, native int)
		IL_038b: dup
		IL_038c: stsfld class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility, bool> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9__164_1'

		IL_0391: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> [System.Core]System.Linq.Enumerable::Where<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>, class [mscorlib]System.Func`2<!!0, bool>)
		IL_0396: ldloc.0
		IL_0397: ldftn instance void Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::'<Initialize>b__2'(class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility)
		IL_039d: newobj instance void class [mscorlib]System.Action`1<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility>::.ctor(object, native int)
		IL_03a2: call void Kingmaker.Utility.LinqExtensions::ForEach<class Kingmaker.UnitLogic.Abilities.Blueprints.BlueprintAbility>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>, class [mscorlib]System.Action`1<!!0>)
		IL_03a7: ldarg.1
		IL_03a8: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> Kingmaker.Blueprints.BlueprintExtenstions::GetComponents<class Kingmaker.UnitLogic.ActivatableAbilities.AddActivatableAbilityComponent>(class Kingmaker.Blueprints.BlueprintScriptableObject)
		IL_03ad: ldsfld class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.ActivatableAbilities.AddActivatableAbilityComponent, class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility>> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9__164_3'
		IL_03b2: dup
		IL_03b3: brtrue.s IL_03cc

		IL_03b5: pop
		IL_03b6: ldsfld class Kingmaker.UnitLogic.UnitDescriptor/'<>c' Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9'
		IL_03bb: ldftn instance class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<Initialize>b__164_3'(class Kingmaker.UnitLogic.ActivatableAbilities.AddActivatableAbilityComponent)
		IL_03c1: newobj instance void class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.ActivatableAbilities.AddActivatableAbilityComponent, class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility>>::.ctor(object, native int)
		IL_03c6: dup
		IL_03c7: stsfld class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.ActivatableAbilities.AddActivatableAbilityComponent, class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility>> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9__164_3'

		IL_03cc: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!1> [System.Core]System.Linq.Enumerable::SelectMany<class Kingmaker.UnitLogic.ActivatableAbilities.AddActivatableAbilityComponent, class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>, class [mscorlib]System.Func`2<!!0, class [mscorlib]System.Collections.Generic.IEnumerable`1<!!1>>)
		IL_03d1: ldsfld class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility, bool> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9__164_4'
		IL_03d6: dup
		IL_03d7: brtrue.s IL_03f0

		IL_03d9: pop
		IL_03da: ldsfld class Kingmaker.UnitLogic.UnitDescriptor/'<>c' Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9'
		IL_03df: ldftn instance bool Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<Initialize>b__164_4'(class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility)
		IL_03e5: newobj instance void class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility, bool>::.ctor(object, native int)
		IL_03ea: dup
		IL_03eb: stsfld class [mscorlib]System.Func`2<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility, bool> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9__164_4'

		IL_03f0: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> [System.Core]System.Linq.Enumerable::Where<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>, class [mscorlib]System.Func`2<!!0, bool>)
		IL_03f5: ldloc.0
		IL_03f6: ldftn instance void Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::'<Initialize>b__5'(class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility)
		IL_03fc: newobj instance void class [mscorlib]System.Action`1<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility>::.ctor(object, native int)
		IL_0401: call void Kingmaker.Utility.LinqExtensions::ForEach<class Kingmaker.UnitLogic.ActivatableAbilities.BlueprintActivatableAbility>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>, class [mscorlib]System.Action`1<!!0>)
		IL_0406: ldarg.1
		IL_0407: callvirt instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.Facts.BlueprintUnitFact, class Kingmaker.Blueprints.BlueprintUnitFactReference> Kingmaker.Blueprints.BlueprintUnit::get_AddFacts()
		IL_040c: box valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.Facts.BlueprintUnitFact, class Kingmaker.Blueprints.BlueprintUnitFactReference>
		IL_0411: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> Kingmaker.Utility.LinqExtensions::EmptyIfNull<class Kingmaker.Blueprints.Facts.BlueprintUnitFact>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
		IL_0416: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<!0> class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Blueprints.Facts.BlueprintUnitFact>::GetEnumerator()
		IL_041b: stloc.s 6
		.try
		{
			IL_041d: br.s IL_0441
			// loop start (head: IL_0441)
				IL_041f: ldloc.s 6
				IL_0421: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Blueprints.Facts.BlueprintUnitFact>::get_Current()
				IL_0426: stloc.s 7
				IL_0428: ldloc.s 7
				IL_042a: call bool Kingmaker.Blueprints.SimpleBlueprint::op_Implicit(class Kingmaker.Blueprints.SimpleBlueprint)
				IL_042f: brfalse.s IL_0441

				IL_0431: ldloc.0
				IL_0432: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
				IL_0437: ldloc.s 7
				IL_0439: ldnull
				IL_043a: ldnull
				IL_043b: call class Kingmaker.EntitySystem.EntityFact Kingmaker.UnitLogic.UnitHelper::AddFact(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.Facts.BlueprintUnitFact, class Kingmaker.UnitLogic.Mechanics.MechanicsContext, class Kingmaker.Blueprints.Classes.Selection.FeatureParam)
				IL_0440: pop

				IL_0441: ldloc.s 6
				IL_0443: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
				IL_0448: brtrue.s IL_041f
			// end loop

			IL_044a: leave.s IL_0458
		} // end .try
		finally
		{
			IL_044c: ldloc.s 6
			IL_044e: brfalse.s IL_0457

			IL_0450: ldloc.s 6
			IL_0452: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_0457: endfinally
		} // end handler

		IL_0458: ldarg.1
		IL_0459: callvirt instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.BlueprintUnitTemplate, class Kingmaker.Blueprints.BlueprintUnitTemplateReference> Kingmaker.Blueprints.BlueprintUnit::get_AdditionalTemplates()
		IL_045e: box valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.BlueprintUnitTemplate, class Kingmaker.Blueprints.BlueprintUnitTemplateReference>
		IL_0463: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> Kingmaker.Utility.LinqExtensions::EmptyIfNull<class Kingmaker.Blueprints.BlueprintUnitTemplate>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
		IL_0468: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<!0> class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Blueprints.BlueprintUnitTemplate>::GetEnumerator()
		IL_046d: stloc.s 8
		.try
		{
			IL_046f: br.s IL_0487
			// loop start (head: IL_0487)
				IL_0471: ldloc.s 8
				IL_0473: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Blueprints.BlueprintUnitTemplate>::get_Current()
				IL_0478: stloc.s 9
				IL_047a: ldloc.0
				IL_047b: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
				IL_0480: ldloc.s 9
				IL_0482: call void Kingmaker.UnitLogic.UnitDescriptor::ApplyTemplate(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.BlueprintUnitTemplate)

				IL_0487: ldloc.s 8
				IL_0489: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
				IL_048e: brtrue.s IL_0471
			// end loop

			IL_0490: leave.s IL_049e
		} // end .try
		finally
		{
			IL_0492: ldloc.s 8
			IL_0494: brfalse.s IL_049d

			IL_0496: ldloc.s 8
			IL_0498: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_049d: endfinally
		} // end handler

		IL_049e: call !0 class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.EntitySystem.Entities.UnitEntityData/ChargenUnit>::get_Current()
		IL_04a3: call bool class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.EntitySystem.Entities.UnitEntityData/ChargenUnit>::op_Implicit(class Kingmaker.ElementsSystem.ContextData`1<!0>)
		IL_04a8: brtrue.s IL_0502

		IL_04aa: ldloc.2
		IL_04ab: brfalse.s IL_04d8

		IL_04ad: ldstr "Body"
		IL_04b2: ldnull
		IL_04b3: call class [mscorlib]System.IDisposable Kingmaker.Utility.ProfileScope::New(string, class [UnityEngine.CoreModule]UnityEngine.Object)
		IL_04b8: stloc.s 10
		.try
		{
			IL_04ba: ldloc.0
			IL_04bb: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
			IL_04c0: callvirt instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
			IL_04c5: callvirt instance void Kingmaker.Items.UnitBody::Initialize()
			IL_04ca: leave.s IL_04d8
		} // end .try
		finally
		{
			IL_04cc: ldloc.s 10
			IL_04ce: brfalse.s IL_04d7

			IL_04d0: ldloc.s 10
			IL_04d2: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_04d7: endfinally
		} // end handler

		IL_04d8: ldloc.1
		IL_04d9: brfalse.s IL_0512

		IL_04db: ldstr "Starting Inventory"
		IL_04e0: ldnull
		IL_04e1: call class [mscorlib]System.IDisposable Kingmaker.Utility.ProfileScope::New(string, class [UnityEngine.CoreModule]UnityEngine.Object)
		IL_04e6: stloc.s 10
		.try
		{
			IL_04e8: ldloc.0
			IL_04e9: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
			IL_04ee: ldarg.1
			IL_04ef: call void Kingmaker.UnitLogic.UnitDescriptor::AddStartingInventory(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.BlueprintUnit)
			IL_04f4: leave.s IL_0512
		} // end .try
		finally
		{
			IL_04f6: ldloc.s 10
			IL_04f8: brfalse.s IL_0501

			IL_04fa: ldloc.s 10
			IL_04fc: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_0501: endfinally
		} // end handler

		IL_0502: ldloc.0
		IL_0503: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0508: callvirt instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		IL_050d: callvirt instance void Kingmaker.Items.UnitBody::EnsureActiveHands()

		IL_0512: ldstr "Brain"
		IL_0517: ldnull
		IL_0518: call class [mscorlib]System.IDisposable Kingmaker.Utility.ProfileScope::New(string, class [UnityEngine.CoreModule]UnityEngine.Object)
		IL_051d: stloc.s 10
		.try
		{
			IL_051f: ldloc.0
			IL_0520: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
			IL_0525: callvirt instance class Kingmaker.UnitLogic.UnitBrain Kingmaker.UnitLogic.UnitDescriptor::get_Brain()
			IL_052a: callvirt instance void Kingmaker.UnitLogic.UnitBrain::RestoreAvailableActions()
			IL_052f: leave.s IL_053d
		} // end .try
		finally
		{
			IL_0531: ldloc.s 10
			IL_0533: brfalse.s IL_053c

			IL_0535: ldloc.s 10
			IL_0537: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_053c: endfinally
		} // end handler

		IL_053d: ldstr "HandleInventoryInitialized Event"
		IL_0542: ldnull
		IL_0543: call class [mscorlib]System.IDisposable Kingmaker.Utility.ProfileScope::New(string, class [UnityEngine.CoreModule]UnityEngine.Object)
		IL_0548: stloc.s 10
		.try
		{
			IL_054a: ldarg.1
			IL_054b: ldloc.0
			IL_054c: ldftn instance void Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::'<Initialize>b__6'(class Kingmaker.UnitLogic.IHandleInventoryInitialized)
			IL_0552: newobj instance void class [mscorlib]System.Action`1<class Kingmaker.UnitLogic.IHandleInventoryInitialized>::.ctor(object, native int)
			IL_0557: call void Kingmaker.Blueprints.BlueprintExtenstions::CallComponents<class Kingmaker.UnitLogic.IHandleInventoryInitialized>(class Kingmaker.Blueprints.BlueprintScriptableObject, class [mscorlib]System.Action`1<!!0>)
			IL_055c: leave.s IL_056a
		} // end .try
		finally
		{
			IL_055e: ldloc.s 10
			IL_0560: brfalse.s IL_0569

			IL_0562: ldloc.s 10
			IL_0564: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_0569: endfinally
		} // end handler

		IL_056a: ldloc.0
		IL_056b: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0570: callvirt instance void Kingmaker.UnitLogic.UnitDescriptor::Remove<class Kingmaker.UnitLogic.Parts.LevelUpPlanUnitHolder>()
		IL_0575: ldloc.0
		IL_0576: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_057b: callvirt instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsPlayerFaction()
		IL_0580: brfalse.s IL_058e

		IL_0582: ldloc.0
		IL_0583: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0588: callvirt instance !!0 Kingmaker.UnitLogic.UnitDescriptor::Ensure<class Kingmaker.UnitLogic.Parts.UnitPartPartyWeatherBuff>()
		IL_058d: pop

		IL_058e: ldloc.0
		IL_058f: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_0594: ldc.i4.1
		IL_0595: callvirt instance void Kingmaker.UnitLogic.UnitDescriptor::set_IsTurnedOn(bool)
		IL_059a: ldloc.0
		IL_059b: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_05a0: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::get_Spellbooks()
		IL_05a5: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<!0> class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.Spellbook>::GetEnumerator()
		IL_05aa: stloc.s 11
		.try
		{
			IL_05ac: br.s IL_05bb
			// loop start (head: IL_05bb)
				IL_05ae: ldloc.s 11
				IL_05b0: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Spellbook>::get_Current()
				IL_05b5: ldc.i4.1
				IL_05b6: callvirt instance void Kingmaker.UnitLogic.Spellbook::UpdateAllSlotsSize(bool)

				IL_05bb: ldloc.s 11
				IL_05bd: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
				IL_05c2: brtrue.s IL_05ae
			// end loop

			IL_05c4: leave.s IL_05d2
		} // end .try
		finally
		{
			IL_05c6: ldloc.s 11
			IL_05c8: brfalse.s IL_05d1

			IL_05ca: ldloc.s 11
			IL_05cc: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_05d1: endfinally
		} // end handler

		IL_05d2: ldloc.0
		IL_05d3: ldfld class Kingmaker.UnitLogic.UnitDescriptor Kingmaker.UnitLogic.UnitDescriptor/'<>c__DisplayClass164_0'::unit
		IL_05d8: call void Kingmaker.UnitLogic.UnitHelper::Replenish(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_05dd: ret
	} // end of method UnitDescriptor::Initialize

	.method public hidebysig 
		instance void AddStartingInventory () cil managed 
	{
		// Method begins at RVA 0x31c21c
		// Header size: 1
		// Code size: 13 (0xd)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.0
		IL_0002: call instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_OriginalBlueprint()
		IL_0007: call void Kingmaker.UnitLogic.UnitDescriptor::AddStartingInventory(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.BlueprintUnit)
		IL_000c: ret
	} // end of method UnitDescriptor::AddStartingInventory

	.method private hidebysig static 
		void AddStartingInventory (
			class Kingmaker.UnitLogic.UnitDescriptor unit,
			class Kingmaker.Blueprints.BlueprintUnit blueprint
		) cil managed 
	{
		// Method begins at RVA 0x31c22c
		// Header size: 12
		// Code size: 153 (0x99)
		.maxstack 6
		.locals init (
			[0] valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2/Enumerator<class Kingmaker.Blueprints.Items.BlueprintItem, class Kingmaker.Blueprints.BlueprintItemReference>,
			[1] valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.Items.BlueprintItem, class Kingmaker.Blueprints.BlueprintItemReference>,
			[2] class Kingmaker.Blueprints.Items.BlueprintItem,
			[3] class [mscorlib]System.IDisposable,
			[4] class Kingmaker.Items.ItemsCollection/SuppressEvents
		)

		IL_0000: call !0 class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.EntitySystem.Entities.UnitEntityData/DoNotCreateItems>::get_Current()
		IL_0005: call bool class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.EntitySystem.Entities.UnitEntityData/DoNotCreateItems>::op_Implicit(class Kingmaker.ElementsSystem.ContextData`1<!0>)
		IL_000a: brfalse.s IL_000d

		IL_000c: ret

		IL_000d: ldarg.1
		IL_000e: callvirt instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.Items.BlueprintItem, class Kingmaker.Blueprints.BlueprintItemReference> Kingmaker.Blueprints.BlueprintUnit::get_StartingInventory()
		IL_0013: stloc.1
		IL_0014: ldloca.s 1
		IL_0016: call instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2/Enumerator<!0, !1> valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.Items.BlueprintItem, class Kingmaker.Blueprints.BlueprintItemReference>::GetEnumerator()
		IL_001b: stloc.0
		.try
		{
			IL_001c: br.s IL_007f
			// loop start (head: IL_007f)
				IL_001e: ldloca.s 0
				IL_0020: call instance !0 valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2/Enumerator<class Kingmaker.Blueprints.Items.BlueprintItem, class Kingmaker.Blueprints.BlueprintItemReference>::get_Current()
				IL_0025: stloc.2
				IL_0026: ldloc.2
				IL_0027: call bool Kingmaker.Blueprints.SimpleBlueprint::op_Implicit(class Kingmaker.Blueprints.SimpleBlueprint)
				IL_002c: brfalse.s IL_0066

				IL_002e: ldstr "Add Item"
				IL_0033: ldnull
				IL_0034: call class [mscorlib]System.IDisposable Kingmaker.Utility.ProfileScope::New(string, class [UnityEngine.CoreModule]UnityEngine.Object)
				IL_0039: stloc.3
				.try
				{
					IL_003a: call !0 class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.Items.ItemsCollection/SuppressEvents>::Request()
					IL_003f: stloc.s 4
					.try
					{
						IL_0041: ldarg.0
						IL_0042: callvirt instance class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::get_Inventory()
						IL_0047: ldloc.2
						IL_0048: callvirt instance class Kingmaker.Items.ItemEntity Kingmaker.Items.ItemsCollection::Add(class Kingmaker.Blueprints.Items.BlueprintItem)
						IL_004d: pop
						IL_004e: leave.s IL_007f
					} // end .try
					finally
					{
						IL_0050: ldloc.s 4
						IL_0052: brfalse.s IL_005b

						IL_0054: ldloc.s 4
						IL_0056: callvirt instance void [mscorlib]System.IDisposable::Dispose()

						IL_005b: endfinally
					} // end handler
				} // end .try
				finally
				{
					IL_005c: ldloc.3
					IL_005d: brfalse.s IL_0065

					IL_005f: ldloc.3
					IL_0060: callvirt instance void [mscorlib]System.IDisposable::Dispose()

					IL_0065: endfinally
				} // end handler

				IL_0066: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
				IL_006b: ldstr "Unit '{0}' has NULL in StartingInventory"
				IL_0070: ldc.i4.1
				IL_0071: newarr [mscorlib]System.Object
				IL_0076: dup
				IL_0077: ldc.i4.0
				IL_0078: ldarg.1
				IL_0079: stelem.ref
				IL_007a: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Error(string, object[])

				IL_007f: ldloca.s 0
				IL_0081: call instance bool valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2/Enumerator<class Kingmaker.Blueprints.Items.BlueprintItem, class Kingmaker.Blueprints.BlueprintItemReference>::MoveNext()
				IL_0086: brtrue.s IL_001e
			// end loop

			IL_0088: leave.s IL_0098
		} // end .try
		finally
		{
			IL_008a: ldloca.s 0
			IL_008c: constrained. valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2/Enumerator<class Kingmaker.Blueprints.Items.BlueprintItem, class Kingmaker.Blueprints.BlueprintItemReference>
			IL_0092: callvirt instance void [mscorlib]System.IDisposable::Dispose()
			IL_0097: endfinally
		} // end handler

		IL_0098: ret
	} // end of method UnitDescriptor::AddStartingInventory

	.method private hidebysig static 
		void InitializeStat (
			class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat stat,
			int32 'value'
		) cil managed 
	{
		// Method begins at RVA 0x31c2fc
		// Header size: 1
		// Code size: 35 (0x23)
		.maxstack 8

		IL_0000: call !0 class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.EntitySystem.Entities.UnitEntityData/DoNotInitializeStats>::get_Current()
		IL_0005: call bool class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.EntitySystem.Entities.UnitEntityData/DoNotInitializeStats>::op_Implicit(class Kingmaker.ElementsSystem.ContextData`1<!0>)
		IL_000a: brfalse.s IL_0010

		IL_000c: ldc.i4.s 10
		IL_000e: starg.s 'value'

		IL_0010: ldarg.1
		IL_0011: ldc.i4.1
		IL_0012: bge.s IL_001b

		IL_0014: ldarg.0
		IL_0015: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat::RetainDisabled()
		IL_001a: ret

		IL_001b: ldarg.0
		IL_001c: ldarg.1
		IL_001d: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_0022: ret
	} // end of method UnitDescriptor::InitializeStat

	.method private hidebysig 
		instance void SetSkills (
			class Kingmaker.Blueprints.BlueprintUnit/UnitSkills skills
		) cil managed 
	{
		// Method begins at RVA 0x31c320
		// Header size: 12
		// Code size: 256 (0x100)
		.maxstack 2

		IL_0000: call !0 class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.EntitySystem.Entities.UnitEntityData/DoNotInitializeStats>::get_Current()
		IL_0005: call bool class Kingmaker.ElementsSystem.ContextData`1<class Kingmaker.EntitySystem.Entities.UnitEntityData/DoNotInitializeStats>::op_Implicit(class Kingmaker.ElementsSystem.ContextData`1<!0>)
		IL_000a: brfalse.s IL_000d

		IL_000c: ret

		IL_000d: ldarg.0
		IL_000e: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0013: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillMobility
		IL_0018: ldarg.1
		IL_0019: ldfld int32 Kingmaker.Blueprints.BlueprintUnit/UnitSkills::Acrobatics
		IL_001e: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_0023: ldarg.0
		IL_0024: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0029: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillAthletics
		IL_002e: ldarg.1
		IL_002f: ldfld int32 Kingmaker.Blueprints.BlueprintUnit/UnitSkills::Physique
		IL_0034: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_0039: ldarg.0
		IL_003a: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_003f: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillPersuasion
		IL_0044: ldarg.1
		IL_0045: ldfld int32 Kingmaker.Blueprints.BlueprintUnit/UnitSkills::Diplomacy
		IL_004a: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_004f: ldarg.0
		IL_0050: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0055: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillThievery
		IL_005a: ldarg.1
		IL_005b: ldfld int32 Kingmaker.Blueprints.BlueprintUnit/UnitSkills::Thievery
		IL_0060: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_0065: ldarg.0
		IL_0066: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_006b: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillPerception
		IL_0070: ldarg.1
		IL_0071: ldfld int32 Kingmaker.Blueprints.BlueprintUnit/UnitSkills::Perception
		IL_0076: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_007b: ldarg.0
		IL_007c: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0081: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillStealth
		IL_0086: ldarg.1
		IL_0087: ldfld int32 Kingmaker.Blueprints.BlueprintUnit/UnitSkills::Stealth
		IL_008c: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_0091: ldarg.0
		IL_0092: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0097: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillUseMagicDevice
		IL_009c: ldarg.1
		IL_009d: ldfld int32 Kingmaker.Blueprints.BlueprintUnit/UnitSkills::UseMagicDevice
		IL_00a2: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_00a7: ldarg.0
		IL_00a8: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_00ad: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillLoreNature
		IL_00b2: ldarg.1
		IL_00b3: ldfld int32 Kingmaker.Blueprints.BlueprintUnit/UnitSkills::LoreNature
		IL_00b8: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_00bd: ldarg.0
		IL_00be: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_00c3: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillKnowledgeArcana
		IL_00c8: ldarg.1
		IL_00c9: ldfld int32 Kingmaker.Blueprints.BlueprintUnit/UnitSkills::KnowledgeArcana
		IL_00ce: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_00d3: ldarg.0
		IL_00d4: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_00d9: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillLoreReligion
		IL_00de: ldarg.1
		IL_00df: ldfld int32 Kingmaker.Blueprints.BlueprintUnit/UnitSkills::LoreReligion
		IL_00e4: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_00e9: ldarg.0
		IL_00ea: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_00ef: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillKnowledgeWorld
		IL_00f4: ldarg.1
		IL_00f5: ldfld int32 Kingmaker.Blueprints.BlueprintUnit/UnitSkills::KnowledgeWorld
		IL_00fa: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
		IL_00ff: ret
	} // end of method UnitDescriptor::SetSkills

	.method public hidebysig static 
		void ApplyTemplate (
			class Kingmaker.UnitLogic.UnitDescriptor unit,
			class Kingmaker.Blueprints.BlueprintUnitTemplate template
		) cil managed 
	{
		// Method begins at RVA 0x31c42c
		// Header size: 12
		// Code size: 361 (0x169)
		.maxstack 6
		.locals init (
			[0] class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Blueprints.Facts.BlueprintUnitFact>,
			[1] class Kingmaker.Blueprints.Facts.BlueprintUnitFact,
			[2] class Kingmaker.Blueprints.Facts.BlueprintUnitFact,
			[3] class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Blueprints.BlueprintUnitTemplate/StatAdjustment>,
			[4] class Kingmaker.Blueprints.BlueprintUnitTemplate/StatAdjustment,
			[5] class Kingmaker.EntitySystem.Stats.ModifiableValue,
			[6] class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat
		)

		IL_0000: ldarg.1
		IL_0001: brtrue.s IL_0004

		IL_0003: ret

		IL_0004: ldarg.1
		IL_0005: callvirt instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.Facts.BlueprintUnitFact, class Kingmaker.Blueprints.BlueprintUnitFactReference> Kingmaker.Blueprints.BlueprintUnitTemplate::get_AddFacts()
		IL_000a: box valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.Facts.BlueprintUnitFact, class Kingmaker.Blueprints.BlueprintUnitFactReference>
		IL_000f: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> Kingmaker.Utility.LinqExtensions::EmptyIfNull<class Kingmaker.Blueprints.Facts.BlueprintUnitFact>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
		IL_0014: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<!0> class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Blueprints.Facts.BlueprintUnitFact>::GetEnumerator()
		IL_0019: stloc.0
		.try
		{
			IL_001a: br.s IL_004b
			// loop start (head: IL_004b)
				IL_001c: ldloc.0
				IL_001d: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Blueprints.Facts.BlueprintUnitFact>::get_Current()
				IL_0022: stloc.1
				IL_0023: ldloc.1
				IL_0024: call bool Kingmaker.Blueprints.SimpleBlueprint::op_Implicit(class Kingmaker.Blueprints.SimpleBlueprint)
				IL_0029: brfalse.s IL_0037

				IL_002b: ldarg.0
				IL_002c: ldloc.1
				IL_002d: ldnull
				IL_002e: ldnull
				IL_002f: call class Kingmaker.EntitySystem.EntityFact Kingmaker.UnitLogic.UnitHelper::AddFact(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.Facts.BlueprintUnitFact, class Kingmaker.UnitLogic.Mechanics.MechanicsContext, class Kingmaker.Blueprints.Classes.Selection.FeatureParam)
				IL_0034: pop
				IL_0035: br.s IL_004b

				IL_0037: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
				IL_003c: ldstr "NULL fact in template"
				IL_0041: call !!0[] [mscorlib]System.Array::Empty<object>()
				IL_0046: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Warning(string, object[])

				IL_004b: ldloc.0
				IL_004c: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
				IL_0051: brtrue.s IL_001c
			// end loop

			IL_0053: leave.s IL_005f
		} // end .try
		finally
		{
			IL_0055: ldloc.0
			IL_0056: brfalse.s IL_005e

			IL_0058: ldloc.0
			IL_0059: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_005e: endfinally
		} // end handler

		IL_005f: ldarg.1
		IL_0060: callvirt instance valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.Facts.BlueprintUnitFact, class Kingmaker.Blueprints.BlueprintUnitFactReference> Kingmaker.Blueprints.BlueprintUnitTemplate::get_RemoveFacts()
		IL_0065: box valuetype Kingmaker.Blueprints.ReferenceArrayProxy`2<class Kingmaker.Blueprints.Facts.BlueprintUnitFact, class Kingmaker.Blueprints.BlueprintUnitFactReference>
		IL_006a: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> Kingmaker.Utility.LinqExtensions::EmptyIfNull<class Kingmaker.Blueprints.Facts.BlueprintUnitFact>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
		IL_006f: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<!0> class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Blueprints.Facts.BlueprintUnitFact>::GetEnumerator()
		IL_0074: stloc.0
		.try
		{
			IL_0075: br.s IL_00a6
			// loop start (head: IL_00a6)
				IL_0077: ldloc.0
				IL_0078: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Blueprints.Facts.BlueprintUnitFact>::get_Current()
				IL_007d: stloc.2
				IL_007e: ldloc.2
				IL_007f: call bool Kingmaker.Blueprints.SimpleBlueprint::op_Implicit(class Kingmaker.Blueprints.SimpleBlueprint)
				IL_0084: brfalse.s IL_0092

				IL_0086: ldarg.0
				IL_0087: ldloc.2
				IL_0088: ldnull
				IL_0089: ldnull
				IL_008a: call class Kingmaker.EntitySystem.EntityFact Kingmaker.UnitLogic.UnitHelper::AddFact(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.Facts.BlueprintUnitFact, class Kingmaker.UnitLogic.Mechanics.MechanicsContext, class Kingmaker.Blueprints.Classes.Selection.FeatureParam)
				IL_008f: pop
				IL_0090: br.s IL_00a6

				IL_0092: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
				IL_0097: ldstr "NULL buff in template"
				IL_009c: call !!0[] [mscorlib]System.Array::Empty<object>()
				IL_00a1: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Warning(string, object[])

				IL_00a6: ldloc.0
				IL_00a7: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
				IL_00ac: brtrue.s IL_0077
			// end loop

			IL_00ae: leave.s IL_00ba
		} // end .try
		finally
		{
			IL_00b0: ldloc.0
			IL_00b1: brfalse.s IL_00b9

			IL_00b3: ldloc.0
			IL_00b4: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_00b9: endfinally
		} // end handler

		IL_00ba: ldarg.1
		IL_00bb: ldfld class Kingmaker.Blueprints.BlueprintUnitTemplate/StatAdjustment[] Kingmaker.Blueprints.BlueprintUnitTemplate::StatAdjustments
		IL_00c0: call class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> Kingmaker.Utility.LinqExtensions::EmptyIfNull<class Kingmaker.Blueprints.BlueprintUnitTemplate/StatAdjustment>(class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0>)
		IL_00c5: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<!0> class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Blueprints.BlueprintUnitTemplate/StatAdjustment>::GetEnumerator()
		IL_00ca: stloc.3
		.try
		{
			IL_00cb: br IL_0151
			// loop start (head: IL_0151)
				IL_00d0: ldloc.3
				IL_00d1: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Blueprints.BlueprintUnitTemplate/StatAdjustment>::get_Current()
				IL_00d6: stloc.s 4
				IL_00d8: ldarg.0
				IL_00d9: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
				IL_00de: ldloc.s 4
				IL_00e0: ldfld valuetype Kingmaker.EntitySystem.Stats.StatType Kingmaker.Blueprints.BlueprintUnitTemplate/StatAdjustment::Stat
				IL_00e5: callvirt instance class Kingmaker.EntitySystem.Stats.ModifiableValue Kingmaker.EntitySystem.Stats.CharacterStats::GetStat(valuetype Kingmaker.EntitySystem.Stats.StatType)
				IL_00ea: stloc.s 5
				IL_00ec: ldloc.s 5
				IL_00ee: brfalse.s IL_0127

				IL_00f0: ldloc.s 5
				IL_00f2: isinst Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat
				IL_00f7: stloc.s 6
				IL_00f9: ldloc.s 6
				IL_00fb: brfalse.s IL_0110

				IL_00fd: ldloc.s 6
				IL_00ff: callvirt instance bool Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat::get_Enabled()
				IL_0104: brfalse.s IL_0151

				IL_0106: ldloc.s 6
				IL_0108: callvirt instance int32 Kingmaker.EntitySystem.Stats.ModifiableValue::get_BaseValue()
				IL_010d: ldc.i4.2
				IL_010e: ble.s IL_0151

				IL_0110: ldloc.s 5
				IL_0112: dup
				IL_0113: callvirt instance int32 Kingmaker.EntitySystem.Stats.ModifiableValue::get_BaseValue()
				IL_0118: ldloc.s 4
				IL_011a: ldfld int32 Kingmaker.Blueprints.BlueprintUnitTemplate/StatAdjustment::Adjustment
				IL_011f: add
				IL_0120: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::set_BaseValue(int32)
				IL_0125: br.s IL_0151

				IL_0127: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
				IL_012c: ldstr "Cannot change stat {0}: stat not found"
				IL_0131: ldloc.s 4
				IL_0133: ldfld valuetype Kingmaker.EntitySystem.Stats.StatType Kingmaker.Blueprints.BlueprintUnitTemplate/StatAdjustment::Stat
				IL_0138: box Kingmaker.EntitySystem.Stats.StatType
				IL_013d: call string [mscorlib]System.String::Format(string, object)
				IL_0142: ldc.i4.1
				IL_0143: newarr [mscorlib]System.Object
				IL_0148: dup
				IL_0149: ldc.i4.0
				IL_014a: ldarg.1
				IL_014b: stelem.ref
				IL_014c: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Warning(string, object[])

				IL_0151: ldloc.3
				IL_0152: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
				IL_0157: brtrue IL_00d0
			// end loop

			IL_015c: leave.s IL_0168
		} // end .try
		finally
		{
			IL_015e: ldloc.3
			IL_015f: brfalse.s IL_0167

			IL_0161: ldloc.3
			IL_0162: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_0167: endfinally
		} // end handler

		IL_0168: ret
	} // end of method UnitDescriptor::ApplyTemplate

	.method public hidebysig 
		instance class Kingmaker.UnitLogic.Spellbook GetSpellbook (
			class Kingmaker.Blueprints.Classes.BlueprintCharacterClass characterClass
		) cil managed 
	{
		.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
			01 00 00 00
		)
		.param [1]
			.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.NotNullAttribute::.ctor() = (
				01 00 00 00
			)
		// Method begins at RVA 0x31c5cc
		// Header size: 12
		// Code size: 42 (0x2a)
		.maxstack 2
		.locals init (
			[0] class Kingmaker.UnitLogic.ClassData
		)

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_0006: ldarg.1
		IL_0007: callvirt instance class Kingmaker.UnitLogic.ClassData Kingmaker.UnitLogic.UnitProgressionData::GetClassData(class Kingmaker.Blueprints.Classes.BlueprintCharacterClass)
		IL_000c: stloc.0
		IL_000d: ldloc.0
		IL_000e: brtrue.s IL_0013

		IL_0010: ldnull
		IL_0011: br.s IL_0019

		IL_0013: ldloc.0
		IL_0014: call instance class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook Kingmaker.UnitLogic.ClassData::get_Spellbook()

		IL_0019: brtrue.s IL_001d

		IL_001b: ldnull
		IL_001c: ret

		IL_001d: ldarg.0
		IL_001e: ldloc.0
		IL_001f: callvirt instance class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook Kingmaker.UnitLogic.ClassData::get_Spellbook()
		IL_0024: call instance class Kingmaker.UnitLogic.Spellbook Kingmaker.UnitLogic.UnitDescriptor::GetSpellbook(class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook)
		IL_0029: ret
	} // end of method UnitDescriptor::GetSpellbook

	.method public hidebysig 
		instance class Kingmaker.UnitLogic.Spellbook DemandSpellbook (
			class Kingmaker.Blueprints.Classes.BlueprintCharacterClass characterClass
		) cil managed 
	{
		.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.NotNullAttribute::.ctor() = (
			01 00 00 00
		)
		.param [1]
			.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.NotNullAttribute::.ctor() = (
				01 00 00 00
			)
		// Method begins at RVA 0x31c604
		// Header size: 12
		// Code size: 155 (0x9b)
		.maxstack 4
		.locals init (
			[0] class Kingmaker.UnitLogic.ClassData
		)

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_0006: ldarg.1
		IL_0007: callvirt instance class Kingmaker.UnitLogic.ClassData Kingmaker.UnitLogic.UnitProgressionData::GetClassData(class Kingmaker.Blueprints.Classes.BlueprintCharacterClass)
		IL_000c: stloc.0
		IL_000d: ldloc.0
		IL_000e: brtrue.s IL_0063

		IL_0010: ldarg.1
		IL_0011: callvirt instance class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook Kingmaker.Blueprints.Classes.BlueprintCharacterClass::get_Spellbook()
		IL_0016: brfalse.s IL_0040

		IL_0018: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
		IL_001d: ldstr "Demanding spellbook for class unit doesnt have: {0}, {1}. Returning default"
		IL_0022: ldarg.0
		IL_0023: ldarg.1
		IL_0024: call string [mscorlib]System.String::Format(string, object, object)
		IL_0029: call !!0[] [mscorlib]System.Array::Empty<object>()
		IL_002e: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Warning(string, object[])
		IL_0033: ldarg.0
		IL_0034: ldarg.1
		IL_0035: callvirt instance class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook Kingmaker.Blueprints.Classes.BlueprintCharacterClass::get_Spellbook()
		IL_003a: call instance class Kingmaker.UnitLogic.Spellbook Kingmaker.UnitLogic.UnitDescriptor::DemandSpellbook(class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook)
		IL_003f: ret

		IL_0040: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
		IL_0045: ldstr "Demanding spellbook for class unit doesnt have: {0}, {1}. Class doesnt have default spellbook."
		IL_004a: ldarg.0
		IL_004b: ldarg.1
		IL_004c: call string [mscorlib]System.String::Format(string, object, object)
		IL_0051: call !!0[] [mscorlib]System.Array::Empty<object>()
		IL_0056: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Error(string, object[])
		IL_005b: ldarg.0
		IL_005c: ldnull
		IL_005d: newobj instance void Kingmaker.UnitLogic.Spellbook::.ctor(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook)
		IL_0062: ret

		IL_0063: ldloc.0
		IL_0064: callvirt instance class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook Kingmaker.UnitLogic.ClassData::get_Spellbook()
		IL_0069: brtrue.s IL_008e

		IL_006b: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
		IL_0070: ldstr "Demanding spellbook for class without one: {0}, {1}."
		IL_0075: ldarg.0
		IL_0076: ldarg.1
		IL_0077: call string [mscorlib]System.String::Format(string, object, object)
		IL_007c: call !!0[] [mscorlib]System.Array::Empty<object>()
		IL_0081: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Error(string, object[])
		IL_0086: ldarg.0
		IL_0087: ldnull
		IL_0088: newobj instance void Kingmaker.UnitLogic.Spellbook::.ctor(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook)
		IL_008d: ret

		IL_008e: ldarg.0
		IL_008f: ldloc.0
		IL_0090: callvirt instance class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook Kingmaker.UnitLogic.ClassData::get_Spellbook()
		IL_0095: call instance class Kingmaker.UnitLogic.Spellbook Kingmaker.UnitLogic.UnitDescriptor::DemandSpellbook(class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook)
		IL_009a: ret
	} // end of method UnitDescriptor::DemandSpellbook

	.method public hidebysig 
		instance class Kingmaker.UnitLogic.Spellbook GetSpellbook (
			class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook blueprint
		) cil managed 
	{
		.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
			01 00 00 00
		)
		.param [1]
			.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.NotNullAttribute::.ctor() = (
				01 00 00 00
			)
		// Method begins at RVA 0x31c6ab
		// Header size: 1
		// Code size: 19 (0x13)
		.maxstack 8

		IL_0000: ldarg.1
		IL_0001: brtrue.s IL_0005

		IL_0003: ldnull
		IL_0004: ret

		IL_0005: ldarg.0
		IL_0006: ldfld class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::m_Spellbooks
		IL_000b: ldarg.1
		IL_000c: ldnull
		IL_000d: call !!1 Kingmaker.Utility.LinqExtensions::Get<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>(class [mscorlib]System.Collections.Generic.IDictionary`2<!!0, !!1>, !!0, !!1)
		IL_0012: ret
	} // end of method UnitDescriptor::GetSpellbook

	.method public hidebysig 
		instance class Kingmaker.UnitLogic.Spellbook DemandSpellbook (
			class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook blueprint
		) cil managed 
	{
		.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.NotNullAttribute::.ctor() = (
			01 00 00 00
		)
		.param [1]
			.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.NotNullAttribute::.ctor() = (
				01 00 00 00
			)
		// Method begins at RVA 0x31c6c0
		// Header size: 12
		// Code size: 40 (0x28)
		.maxstack 3
		.locals init (
			[0] class Kingmaker.UnitLogic.Spellbook
		)

		IL_0000: ldarg.0
		IL_0001: ldfld class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::m_Spellbooks
		IL_0006: ldarg.1
		IL_0007: ldnull
		IL_0008: call !!1 Kingmaker.Utility.LinqExtensions::Get<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>(class [mscorlib]System.Collections.Generic.IDictionary`2<!!0, !!1>, !!0, !!1)
		IL_000d: stloc.0
		IL_000e: ldloc.0
		IL_000f: brtrue.s IL_0026

		IL_0011: ldarg.0
		IL_0012: ldarg.1
		IL_0013: newobj instance void Kingmaker.UnitLogic.Spellbook::.ctor(class Kingmaker.UnitLogic.UnitDescriptor, class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook)
		IL_0018: stloc.0
		IL_0019: ldarg.0
		IL_001a: ldfld class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::m_Spellbooks
		IL_001f: ldarg.1
		IL_0020: ldloc.0
		IL_0021: callvirt instance void class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::set_Item(!0, !1)

		IL_0026: ldloc.0
		IL_0027: ret
	} // end of method UnitDescriptor::DemandSpellbook

	.method public hidebysig 
		instance void DeleteSpellbook (
			class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook spellbook
		) cil managed 
	{
		// Method begins at RVA 0x31c6f4
		// Header size: 1
		// Code size: 14 (0xe)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::m_Spellbooks
		IL_0006: ldarg.1
		IL_0007: callvirt instance bool class [mscorlib]System.Collections.Generic.Dictionary`2<class Kingmaker.Blueprints.Classes.Spells.BlueprintSpellbook, class Kingmaker.UnitLogic.Spellbook>::Remove(!0)
		IL_000c: pop
		IL_000d: ret
	} // end of method UnitDescriptor::DeleteSpellbook

	.method public hidebysig 
		instance void OnGainClassLevel (
			class Kingmaker.Blueprints.Classes.BlueprintCharacterClass 'class'
		) cil managed 
	{
		// Method begins at RVA 0x31c703
		// Header size: 1
		// Code size: 60 (0x3c)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0006: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueHitPoints Kingmaker.EntitySystem.Stats.CharacterStats::HitPoints
		IL_000b: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::UpdateValue()
		IL_0010: ldarg.0
		IL_0011: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0016: ldsfld class [mscorlib]System.Action`1<class Kingmaker.PubSubSystem.IOwnerGainLevelHandler> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9__175_0'
		IL_001b: dup
		IL_001c: brtrue.s IL_0035

		IL_001e: pop
		IL_001f: ldsfld class Kingmaker.UnitLogic.UnitDescriptor/'<>c' Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9'
		IL_0024: ldftn instance void Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<OnGainClassLevel>b__175_0'(class Kingmaker.PubSubSystem.IOwnerGainLevelHandler)
		IL_002a: newobj instance void class [mscorlib]System.Action`1<class Kingmaker.PubSubSystem.IOwnerGainLevelHandler>::.ctor(object, native int)
		IL_002f: dup
		IL_0030: stsfld class [mscorlib]System.Action`1<class Kingmaker.PubSubSystem.IOwnerGainLevelHandler> Kingmaker.UnitLogic.UnitDescriptor/'<>c'::'<>9__175_0'

		IL_0035: call bool Kingmaker.PubSubSystem.EventBus::RaiseEvent<class Kingmaker.PubSubSystem.IOwnerGainLevelHandler>(class Kingmaker.EntitySystem.Entities.UnitEntityData, class [mscorlib]System.Action`1<!!0>)
		IL_003a: pop
		IL_003b: ret
	} // end of method UnitDescriptor::OnGainClassLevel

	.method public hidebysig 
		instance void Resurrect (
			[opt] class Kingmaker.EntitySystem.Entities.UnitEntityData initiator,
			[opt] float32 resultHealthPart,
			[opt] bool restoreHealth
		) cil managed 
	{
		.param [1] = nullref
		.param [2] = float32(0.0)
		.param [3] = bool(true)
		// Method begins at RVA 0x31c740
		// Header size: 1
		// Code size: 11 (0xb)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: ldarg.2
		IL_0003: ldarg.3
		IL_0004: ldc.i4.0
		IL_0005: call instance void Kingmaker.UnitLogic.UnitDescriptor::Resurrect(class Kingmaker.EntitySystem.Entities.UnitEntityData, float32, bool, bool)
		IL_000a: ret
	} // end of method UnitDescriptor::Resurrect

	.method public hidebysig 
		instance void ResurrectAndFullRestore (
			[opt] class Kingmaker.EntitySystem.Entities.UnitEntityData initiator
		) cil managed 
	{
		.param [1] = nullref
		// Method begins at RVA 0x31c74c
		// Header size: 1
		// Code size: 15 (0xf)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldarg.1
		IL_0002: ldc.r4 0.0
		IL_0007: ldc.i4.0
		IL_0008: ldc.i4.1
		IL_0009: call instance void Kingmaker.UnitLogic.UnitDescriptor::Resurrect(class Kingmaker.EntitySystem.Entities.UnitEntityData, float32, bool, bool)
		IL_000e: ret
	} // end of method UnitDescriptor::ResurrectAndFullRestore

	.method private hidebysig 
		instance void Resurrect (
			class Kingmaker.EntitySystem.Entities.UnitEntityData initiator,
			float32 resultHealthPart,
			bool restoreHealth,
			bool fullRestore
		) cil managed 
	{
		.param [1]
			.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
				01 00 00 00
			)
		// Method begins at RVA 0x31c75c
		// Header size: 12
		// Code size: 1199 (0x4af)
		.maxstack 5
		.locals init (
			[0] bool,
			[1] class Kingmaker.UnitLogic.Parts.UnitPartNegativeLevels,
			[2] class Kingmaker.UnitLogic.Parts.UnitPartDualCompanion,
			[3] valuetype Kingmaker.EntitySystem.Stats.StatType[],
			[4] int32,
			[5] valuetype Kingmaker.EntitySystem.Stats.StatType,
			[6] class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat,
			[7] int32,
			[8] int32,
			[9] int32,
			[10] valuetype [UnityEngine.CoreModule]UnityEngine.Vector3,
			[11] valuetype [mscorlib]System.Nullable`1<uint32>,
			[12] valuetype [mscorlib]System.Nullable`1<uint32>,
			[13] valuetype [mscorlib]System.Nullable`1<uint32>,
			[14] valuetype [UnityEngine.CoreModule]UnityEngine.Vector3,
			[15] class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Buffs.Buff>,
			[16] class Kingmaker.UnitLogic.Buffs.Buff,
			[17] class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.FactLogic.AddCondition>,
			[18] class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Designers.Mechanics.Buffs.BuffStatusCondition>
		)

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_0006: callvirt instance bool Kingmaker.UnitLogic.UnitState::get_IsFinallyDead()
		IL_000b: stloc.0
		IL_000c: ldarg.0
		IL_000d: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_0012: ldc.i4.0
		IL_0013: callvirt instance void Kingmaker.UnitLogic.UnitState::set_IsFinallyDead(bool)
		IL_0018: ldarg.0
		IL_0019: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_001e: ldc.i4.5
		IL_001f: ldnull
		IL_0020: callvirt instance void Kingmaker.UnitLogic.UnitState::RemoveConditionAll(valuetype Kingmaker.UnitLogic.UnitCondition, class Kingmaker.UnitLogic.FactLogic.UnitConditionExceptions)
		IL_0025: ldarg.0
		IL_0026: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_002b: ldc.i4.s 47
		IL_002d: ldnull
		IL_002e: callvirt instance void Kingmaker.UnitLogic.UnitState::RemoveConditionAll(valuetype Kingmaker.UnitLogic.UnitCondition, class Kingmaker.UnitLogic.FactLogic.UnitConditionExceptions)
		IL_0033: ldarg.0
		IL_0034: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_0039: ldc.i4.0
		IL_003a: callvirt instance void Kingmaker.UnitLogic.UnitState::set_ForceKill(bool)
		IL_003f: ldarg.0
		IL_0040: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_0045: ldc.i4.0
		IL_0046: callvirt instance void Kingmaker.UnitLogic.UnitState::set_MarkedForDeath(bool)
		IL_004b: ldarg.s fullRestore
		IL_004d: brfalse.s IL_0056

		IL_004f: ldarg.0
		IL_0050: ldc.i4.0
		IL_0051: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_Damage(int32)

		IL_0056: ldarg.0
		IL_0057: call instance int32 Kingmaker.UnitLogic.UnitDescriptor::get_Damage()
		IL_005c: ldarg.0
		IL_005d: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0062: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueHitPoints Kingmaker.EntitySystem.Stats.CharacterStats::HitPoints
		IL_0067: call int32 Kingmaker.EntitySystem.Stats.ModifiableValue::op_Implicit(class Kingmaker.EntitySystem.Stats.ModifiableValue)
		IL_006c: ldarg.0
		IL_006d: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_0072: callvirt instance int32 Kingmaker.UnitLogic.UnitProgressionData::get_CharacterLevel()
		IL_0077: sub
		IL_0078: ble.s IL_00cc

		IL_007a: ldarg.0
		IL_007b: ldarg.3
		IL_007c: brtrue.s IL_0086

		IL_007e: ldarg.0
		IL_007f: call instance int32 Kingmaker.UnitLogic.UnitDescriptor::get_Damage()
		IL_0084: br.s IL_00c7

		IL_0086: ldarg.0
		IL_0087: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_008c: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueHitPoints Kingmaker.EntitySystem.Stats.CharacterStats::HitPoints
		IL_0091: call int32 Kingmaker.EntitySystem.Stats.ModifiableValue::op_Implicit(class Kingmaker.EntitySystem.Stats.ModifiableValue)
		IL_0096: ldc.i4.1
		IL_0097: ldarg.0
		IL_0098: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_009d: callvirt instance int32 Kingmaker.UnitLogic.UnitProgressionData::get_CharacterLevel()
		IL_00a2: call int32 [mscorlib]System.Math::Max(int32, int32)
		IL_00a7: sub
		IL_00a8: ldarg.0
		IL_00a9: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_00ae: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueHitPoints Kingmaker.EntitySystem.Stats.CharacterStats::HitPoints
		IL_00b3: call int32 Kingmaker.EntitySystem.Stats.ModifiableValue::op_Implicit(class Kingmaker.EntitySystem.Stats.ModifiableValue)
		IL_00b8: conv.r4
		IL_00b9: ldc.r4 1
		IL_00be: ldarg.2
		IL_00bf: sub
		IL_00c0: mul
		IL_00c1: conv.i4
		IL_00c2: call int32 [mscorlib]System.Math::Min(int32, int32)

		IL_00c7: call instance void Kingmaker.UnitLogic.UnitDescriptor::set_Damage(int32)

		IL_00cc: ldsfld valuetype Kingmaker.EntitySystem.Stats.StatType[] Kingmaker.EntitySystem.Stats.StatTypeHelper::Attributes
		IL_00d1: stloc.3
		IL_00d2: ldc.i4.0
		IL_00d3: stloc.s 4
		IL_00d5: br IL_0166
		// loop start (head: IL_0166)
			IL_00da: ldloc.3
			IL_00db: ldloc.s 4
			IL_00dd: ldelem.i4
			IL_00de: stloc.s 5
			IL_00e0: ldarg.0
			IL_00e1: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
			IL_00e6: ldloc.s 5
			IL_00e8: callvirt instance !!0 Kingmaker.EntitySystem.Stats.CharacterStats::GetStat<class Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat>(valuetype Kingmaker.EntitySystem.Stats.StatType)
			IL_00ed: stloc.s 6
			IL_00ef: ldarg.s fullRestore
			IL_00f1: brfalse.s IL_0103

			IL_00f3: ldloc.s 6
			IL_00f5: ldc.i4.0
			IL_00f6: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat::set_Damage(int32)
			IL_00fb: ldloc.s 6
			IL_00fd: ldc.i4.0
			IL_00fe: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat::set_Drain(int32)

			IL_0103: ldloc.s 6
			IL_0105: callvirt instance int32 Kingmaker.EntitySystem.Stats.ModifiableValue::get_ModifiedValueRaw()
			IL_010a: ldc.i4.1
			IL_010b: bge.s IL_0160

			IL_010d: ldloc.s 6
			IL_010f: callvirt instance int32 Kingmaker.EntitySystem.Stats.ModifiableValue::get_ModifiedValueRaw()
			IL_0114: neg
			IL_0115: ldc.i4.1
			IL_0116: add
			IL_0117: stloc.s 7
			IL_0119: ldloc.s 6
			IL_011b: callvirt instance int32 Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat::get_Damage()
			IL_0120: ldloc.s 7
			IL_0122: call int32 [mscorlib]System.Math::Min(int32, int32)
			IL_0127: stloc.s 8
			IL_0129: ldloc.s 6
			IL_012b: dup
			IL_012c: callvirt instance int32 Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat::get_Damage()
			IL_0131: ldloc.s 8
			IL_0133: sub
			IL_0134: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat::set_Damage(int32)
			IL_0139: ldloc.s 7
			IL_013b: ldloc.s 8
			IL_013d: sub
			IL_013e: stloc.s 7
			IL_0140: ldloc.s 6
			IL_0142: callvirt instance int32 Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat::get_Drain()
			IL_0147: ldloc.s 7
			IL_0149: call int32 [mscorlib]System.Math::Min(int32, int32)
			IL_014e: stloc.s 9
			IL_0150: ldloc.s 6
			IL_0152: dup
			IL_0153: callvirt instance int32 Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat::get_Drain()
			IL_0158: ldloc.s 9
			IL_015a: sub
			IL_015b: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValueAttributeStat::set_Drain(int32)

			IL_0160: ldloc.s 4
			IL_0162: ldc.i4.1
			IL_0163: add
			IL_0164: stloc.s 4

			IL_0166: ldloc.s 4
			IL_0168: ldloc.3
			IL_0169: ldlen
			IL_016a: conv.i4
			IL_016b: blt IL_00da
		// end loop

		IL_0170: ldarg.0
		IL_0171: call instance !!0 Kingmaker.UnitLogic.UnitDescriptor::Get<class Kingmaker.UnitLogic.Parts.UnitPartNegativeLevels>()
		IL_0176: stloc.1
		IL_0177: ldloc.1
		IL_0178: call bool Kingmaker.EntitySystem.EntityPart::op_Implicit(class Kingmaker.EntitySystem.EntityPart)
		IL_017d: ldarg.s fullRestore
		IL_017f: and
		IL_0180: brfalse.s IL_01b4

		IL_0182: ldloc.1
		IL_0183: callvirt instance void Kingmaker.UnitLogic.Parts.UnitPartNegativeLevels::RemoveAll()
		IL_0188: br.s IL_01b4
		// loop start (head: IL_01b4)
			IL_018a: ldloc.1
			IL_018b: ldc.i4.0
			IL_018c: callvirt instance int32 Kingmaker.UnitLogic.Parts.UnitPartNegativeLevels::RemoveTemporary(bool)
			IL_0191: ldc.i4.1
			IL_0192: bge.s IL_01b4

			IL_0194: ldloc.1
			IL_0195: ldc.i4.0
			IL_0196: callvirt instance int32 Kingmaker.UnitLogic.Parts.UnitPartNegativeLevels::RemovePermanent(bool)
			IL_019b: ldc.i4.1
			IL_019c: bge.s IL_01b4

			IL_019e: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
			IL_01a3: ldstr "Can't remove negative levels, something wrong"
			IL_01a8: call !!0[] [mscorlib]System.Array::Empty<object>()
			IL_01ad: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Error(string, object[])
			IL_01b2: br.s IL_01cf

			IL_01b4: ldloc.1
			IL_01b5: call bool Kingmaker.EntitySystem.EntityPart::op_Implicit(class Kingmaker.EntitySystem.EntityPart)
			IL_01ba: brfalse.s IL_01cf

			IL_01bc: ldloc.1
			IL_01bd: callvirt instance int32 Kingmaker.UnitLogic.Parts.UnitPartNegativeLevels::get_Count()
			IL_01c2: ldarg.0
			IL_01c3: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
			IL_01c8: callvirt instance int32 Kingmaker.UnitLogic.UnitProgressionData::get_CharacterLevel()
			IL_01cd: bge.s IL_018a
		// end loop

		IL_01cf: ldarg.0
		IL_01d0: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_01d5: callvirt instance class Kingmaker.View.UnitEntityView Kingmaker.EntitySystem.Entities.UnitEntityData::get_View()
		IL_01da: call bool [UnityEngine.CoreModule]UnityEngine.Object::op_Implicit(class [UnityEngine.CoreModule]UnityEngine.Object)
		IL_01df: brfalse IL_039d

		IL_01e4: ldarg.0
		IL_01e5: call instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsPlayerFaction()
		IL_01ea: brfalse IL_031b

		IL_01ef: ldarg.1
		IL_01f0: dup
		IL_01f1: brtrue.s IL_0203

		IL_01f3: pop
		IL_01f4: call class Kingmaker.Game Kingmaker.Game::get_Instance()
		IL_01f9: callvirt instance class Kingmaker.Player Kingmaker.Game::get_Player()
		IL_01fe: callvirt instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.Player::GetMainPartyUnit()

		IL_0203: starg.s initiator
		IL_0205: ldarg.0
		IL_0206: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_020b: callvirt instance bool Kingmaker.EntitySystem.Entities.UnitEntityData::get_IsHiddenBecauseDead()
		IL_0210: brfalse.s IL_024f

		IL_0212: ldarg.1
		IL_0213: ldarg.0
		IL_0214: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0219: ldc.i4.1
		IL_021a: call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 Kingmaker.UnitLogic.Buffs.Components.ResurrectionLogic::GetResurrectPosition(class Kingmaker.EntitySystem.Entities.UnitEntityData, class Kingmaker.EntitySystem.Entities.UnitEntityData, bool)
		IL_021f: stloc.s 10
		IL_0221: ldarg.0
		IL_0222: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0227: ldloc.s 10
		IL_0229: callvirt instance void Kingmaker.EntitySystem.EntityDataBase::set_Position(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
		IL_022e: ldarg.0
		IL_022f: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0234: callvirt instance class Kingmaker.View.UnitEntityView Kingmaker.EntitySystem.Entities.UnitEntityData::get_View()
		IL_0239: callvirt instance class [UnityEngine.CoreModule]UnityEngine.GameObject [UnityEngine.CoreModule]UnityEngine.Component::get_gameObject()
		IL_023e: callvirt instance class [UnityEngine.CoreModule]UnityEngine.Transform [UnityEngine.CoreModule]UnityEngine.GameObject::get_transform()
		IL_0243: ldloc.s 10
		IL_0245: callvirt instance void [UnityEngine.CoreModule]UnityEngine.Transform::set_position(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
		IL_024a: br IL_031b

		IL_024f: ldloc.0
		IL_0250: brfalse IL_031b

		IL_0255: ldsfld class [AstarPathfindingProject]AstarPath [AstarPathfindingProject]AstarPath::active
		IL_025a: ldarg.0
		IL_025b: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0260: callvirt instance valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 Kingmaker.EntitySystem.EntityDataBase::get_Position()
		IL_0265: callvirt instance valuetype [AstarPathfindingProject]Pathfinding.NNInfo [AstarPathfindingProject]AstarPath::GetNearest(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
		IL_026a: ldfld class [AstarPathfindingProject]Pathfinding.GraphNode [AstarPathfindingProject]Pathfinding.NNInfo::node
		IL_026f: dup
		IL_0270: brtrue.s IL_027f

		IL_0272: pop
		IL_0273: ldloca.s 12
		IL_0275: initobj valuetype [mscorlib]System.Nullable`1<uint32>
		IL_027b: ldloc.s 12
		IL_027d: br.s IL_0289

		IL_027f: call instance uint32 [AstarPathfindingProject]Pathfinding.GraphNode::get_Area()
		IL_0284: newobj instance void valuetype [mscorlib]System.Nullable`1<uint32>::.ctor(!0)

		IL_0289: stloc.s 11
		IL_028b: ldsfld class [AstarPathfindingProject]AstarPath [AstarPathfindingProject]AstarPath::active
		IL_0290: ldarg.1
		IL_0291: callvirt instance valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 Kingmaker.EntitySystem.EntityDataBase::get_Position()
		IL_0296: callvirt instance valuetype [AstarPathfindingProject]Pathfinding.NNInfo [AstarPathfindingProject]AstarPath::GetNearest(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
		IL_029b: ldfld class [AstarPathfindingProject]Pathfinding.GraphNode [AstarPathfindingProject]Pathfinding.NNInfo::node
		IL_02a0: dup
		IL_02a1: brtrue.s IL_02b0

		IL_02a3: pop
		IL_02a4: ldloca.s 12
		IL_02a6: initobj valuetype [mscorlib]System.Nullable`1<uint32>
		IL_02ac: ldloc.s 12
		IL_02ae: br.s IL_02ba

		IL_02b0: call instance uint32 [AstarPathfindingProject]Pathfinding.GraphNode::get_Area()
		IL_02b5: newobj instance void valuetype [mscorlib]System.Nullable`1<uint32>::.ctor(!0)

		IL_02ba: ldloc.s 11
		IL_02bc: stloc.s 12
		IL_02be: stloc.s 13
		IL_02c0: ldloca.s 12
		IL_02c2: call instance !0 valuetype [mscorlib]System.Nullable`1<uint32>::GetValueOrDefault()
		IL_02c7: ldloca.s 13
		IL_02c9: call instance !0 valuetype [mscorlib]System.Nullable`1<uint32>::GetValueOrDefault()
		IL_02ce: ceq
		IL_02d0: ldloca.s 12
		IL_02d2: call instance bool valuetype [mscorlib]System.Nullable`1<uint32>::get_HasValue()
		IL_02d7: ldloca.s 13
		IL_02d9: call instance bool valuetype [mscorlib]System.Nullable`1<uint32>::get_HasValue()
		IL_02de: ceq
		IL_02e0: and
		IL_02e1: brtrue.s IL_031b

		IL_02e3: ldarg.1
		IL_02e4: ldarg.0
		IL_02e5: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_02ea: ldc.i4.1
		IL_02eb: call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 Kingmaker.UnitLogic.Buffs.Components.ResurrectionLogic::GetResurrectPosition(class Kingmaker.EntitySystem.Entities.UnitEntityData, class Kingmaker.EntitySystem.Entities.UnitEntityData, bool)
		IL_02f0: stloc.s 14
		IL_02f2: ldarg.0
		IL_02f3: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_02f8: ldloc.s 14
		IL_02fa: callvirt instance void Kingmaker.EntitySystem.EntityDataBase::set_Position(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
		IL_02ff: ldarg.0
		IL_0300: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0305: callvirt instance class Kingmaker.View.UnitEntityView Kingmaker.EntitySystem.Entities.UnitEntityData::get_View()
		IL_030a: callvirt instance class [UnityEngine.CoreModule]UnityEngine.GameObject [UnityEngine.CoreModule]UnityEngine.Component::get_gameObject()
		IL_030f: callvirt instance class [UnityEngine.CoreModule]UnityEngine.Transform [UnityEngine.CoreModule]UnityEngine.GameObject::get_transform()
		IL_0314: ldloc.s 14
		IL_0316: callvirt instance void [UnityEngine.CoreModule]UnityEngine.Transform::set_position(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)

		IL_031b: ldarg.0
		IL_031c: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0321: callvirt instance class Kingmaker.View.UnitEntityView Kingmaker.EntitySystem.Entities.UnitEntityData::get_View()
		IL_0326: ldfld class Kingmaker.Visual.CharactersRigidbody.RigidbodyCreatureController Kingmaker.View.UnitEntityView::RigidbodyController
		IL_032b: dup
		IL_032c: brtrue.s IL_0331

		IL_032e: pop
		IL_032f: br.s IL_0336

		IL_0331: call instance void Kingmaker.Visual.CharactersRigidbody.RigidbodyCreatureController::CancelRagdoll()

		IL_0336: ldarg.0
		IL_0337: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_033c: ldfld class Kingmaker.UnitLogic.ProneState Kingmaker.UnitLogic.UnitState::Prone
		IL_0341: ldc.i4.0
		IL_0342: callvirt instance void Kingmaker.UnitLogic.ProneState::set_Active(bool)
		IL_0347: ldarg.0
		IL_0348: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_034d: callvirt instance class Kingmaker.View.UnitEntityView Kingmaker.EntitySystem.Entities.UnitEntityData::get_View()
		IL_0352: callvirt instance void Kingmaker.View.UnitEntityView::LeaveProneState()
		IL_0357: ldarg.0
		IL_0358: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_035d: callvirt instance class Kingmaker.View.UnitEntityView Kingmaker.EntitySystem.Entities.UnitEntityData::get_View()
		IL_0362: callvirt instance class Kingmaker.Visual.Animation.Kingmaker.UnitAnimationManager Kingmaker.View.UnitEntityView::get_AnimationManager()
		IL_0367: dup
		IL_0368: brtrue.s IL_036d

		IL_036a: pop
		IL_036b: br.s IL_0372

		IL_036d: call instance void Kingmaker.Visual.Animation.Kingmaker.UnitAnimationManager::StandUpImmediately()

		IL_0372: call class Kingmaker.Game Kingmaker.Game::get_Instance()
		IL_0377: callvirt instance class Kingmaker.Controllers.Units.UnitHandEquipmentController Kingmaker.Game::get_HandsEquipmentController()
		IL_037c: dup
		IL_037d: brtrue.s IL_0382

		IL_037f: pop
		IL_0380: br.s IL_038d

		IL_0382: ldarg.0
		IL_0383: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0388: call instance void Kingmaker.Controllers.Units.UnitHandEquipmentController::ScheduleUpdate(class Kingmaker.EntitySystem.Entities.UnitEntityData)

		IL_038d: ldarg.0
		IL_038e: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0393: callvirt instance class Kingmaker.View.UnitEntityView Kingmaker.EntitySystem.Entities.UnitEntityData::get_View()
		IL_0398: callvirt instance void Kingmaker.View.UnitEntityView::ResetMouseHighlighted()

		IL_039d: ldarg.0
		IL_039e: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_03a3: ldc.i4.0
		IL_03a4: callvirt instance void Kingmaker.EntitySystem.Entities.UnitEntityData::set_IsHiddenBecauseDead(bool)
		IL_03a9: ldarg.0
		IL_03aa: call instance !!0 Kingmaker.UnitLogic.UnitDescriptor::Get<class Kingmaker.UnitLogic.Parts.UnitPartDualCompanion>()
		IL_03af: stloc.2
		IL_03b0: ldloc.2
		IL_03b1: brfalse.s IL_03ba

		IL_03b3: ldloc.2
		IL_03b4: ldc.i4.0
		IL_03b5: stfld bool Kingmaker.UnitLogic.Parts.UnitPartDualCompanion::IsDead

		IL_03ba: ldarg.0
		IL_03bb: call instance void Kingmaker.UnitLogic.UnitDescriptor::RemoveBuffsOnResurrect()
		IL_03c0: ldarg.0
		IL_03c1: ldftn instance void Kingmaker.UnitLogic.UnitDescriptor::'<Resurrect>b__178_0'(class Kingmaker.PubSubSystem.IUnitResurrectedHandler)
		IL_03c7: newobj instance void class [mscorlib]System.Action`1<class Kingmaker.PubSubSystem.IUnitResurrectedHandler>::.ctor(object, native int)
		IL_03cc: ldc.i4.1
		IL_03cd: call bool Kingmaker.PubSubSystem.EventBus::RaiseEvent<class Kingmaker.PubSubSystem.IUnitResurrectedHandler>(class [mscorlib]System.Action`1<!!0>, bool)
		IL_03d2: pop
		IL_03d3: ldarg.0
		IL_03d4: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_03d9: callvirt instance bool Kingmaker.UnitLogic.UnitState::get_IsConscious()
		IL_03de: brtrue IL_04ae

		IL_03e3: ldarg.0
		IL_03e4: call instance class Kingmaker.UnitLogic.Buffs.BuffCollection Kingmaker.UnitLogic.UnitDescriptor::get_Buffs()
		IL_03e9: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Buffs.Buff> Kingmaker.UnitLogic.Buffs.BuffCollection::GetEnumerator()
		IL_03ee: stloc.s 15
		.try
		{
			IL_03f0: br IL_047c
			// loop start (head: IL_047c)
				IL_03f5: ldloc.s 15
				IL_03f7: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Buffs.Buff>::get_Current()
				IL_03fc: stloc.s 16
				IL_03fe: ldloc.s 16
				IL_0400: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> Kingmaker.EntitySystem.EntityFact::SelectComponents<class Kingmaker.UnitLogic.FactLogic.AddCondition>()
				IL_0405: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<!0> class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.FactLogic.AddCondition>::GetEnumerator()
				IL_040a: stloc.s 17
				.try
				{
					IL_040c: br.s IL_0426
					// loop start (head: IL_0426)
						IL_040e: ldloc.s 17
						IL_0410: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.FactLogic.AddCondition>::get_Current()
						IL_0415: ldfld valuetype Kingmaker.UnitLogic.UnitCondition Kingmaker.UnitLogic.FactLogic.AddCondition::Condition
						IL_041a: ldc.i4.8
						IL_041b: bne.un.s IL_0426

						IL_041d: ldloc.s 16
						IL_041f: callvirt instance void Kingmaker.UnitLogic.Buffs.Buff::Remove()
						IL_0424: leave.s IL_043d

						IL_0426: ldloc.s 17
						IL_0428: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
						IL_042d: brtrue.s IL_040e
					// end loop

					IL_042f: leave.s IL_043d
				} // end .try
				finally
				{
					IL_0431: ldloc.s 17
					IL_0433: brfalse.s IL_043c

					IL_0435: ldloc.s 17
					IL_0437: callvirt instance void [mscorlib]System.IDisposable::Dispose()

					IL_043c: endfinally
				} // end handler

				IL_043d: ldloc.s 16
				IL_043f: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerable`1<!!0> Kingmaker.EntitySystem.EntityFact::SelectComponents<class Kingmaker.Designers.Mechanics.Buffs.BuffStatusCondition>()
				IL_0444: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<!0> class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.Designers.Mechanics.Buffs.BuffStatusCondition>::GetEnumerator()
				IL_0449: stloc.s 18
				.try
				{
					IL_044b: br.s IL_0465
					// loop start (head: IL_0465)
						IL_044d: ldloc.s 18
						IL_044f: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.Designers.Mechanics.Buffs.BuffStatusCondition>::get_Current()
						IL_0454: ldfld valuetype Kingmaker.UnitLogic.UnitCondition Kingmaker.Designers.Mechanics.Buffs.BuffStatusCondition::Condition
						IL_0459: ldc.i4.8
						IL_045a: bne.un.s IL_0465

						IL_045c: ldloc.s 16
						IL_045e: callvirt instance void Kingmaker.UnitLogic.Buffs.Buff::Remove()
						IL_0463: leave.s IL_047c

						IL_0465: ldloc.s 18
						IL_0467: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
						IL_046c: brtrue.s IL_044d
					// end loop

					IL_046e: leave.s IL_047c
				} // end .try
				finally
				{
					IL_0470: ldloc.s 18
					IL_0472: brfalse.s IL_047b

					IL_0474: ldloc.s 18
					IL_0476: callvirt instance void [mscorlib]System.IDisposable::Dispose()

					IL_047b: endfinally
				} // end handler

				IL_047c: ldloc.s 15
				IL_047e: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
				IL_0483: brtrue IL_03f5
			// end loop

			IL_0488: leave.s IL_0496
		} // end .try
		finally
		{
			IL_048a: ldloc.s 15
			IL_048c: brfalse.s IL_0495

			IL_048e: ldloc.s 15
			IL_0490: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_0495: endfinally
		} // end handler

		IL_0496: ldarg.0
		IL_0497: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_049c: ldc.i4.8
		IL_049d: ldnull
		IL_049e: callvirt instance void Kingmaker.UnitLogic.UnitState::RemoveConditionAll(valuetype Kingmaker.UnitLogic.UnitCondition, class Kingmaker.UnitLogic.FactLogic.UnitConditionExceptions)
		IL_04a3: ldarg.0
		IL_04a4: call class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::op_Implicit(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_04a9: call void Kingmaker.Controllers.Units.UnitLifeController::ForceUnitConscious(class Kingmaker.EntitySystem.Entities.UnitEntityData)

		IL_04ae: ret
	} // end of method UnitDescriptor::Resurrect

	.method public hidebysig 
		instance void RemoveBuffsOnResurrect () cil managed 
	{
		// Method begins at RVA 0x31cc40
		// Header size: 12
		// Code size: 134 (0x86)
		.maxstack 2
		.locals init (
			[0] class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.Buffs.Buff>,
			[1] class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Buffs.Buff>,
			[2] class Kingmaker.UnitLogic.Buffs.Buff,
			[3] valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<class Kingmaker.UnitLogic.Buffs.Buff>,
			[4] class Kingmaker.UnitLogic.Buffs.Buff
		)

		IL_0000: ldnull
		IL_0001: stloc.0
		IL_0002: ldarg.0
		IL_0003: call instance class Kingmaker.UnitLogic.Buffs.BuffCollection Kingmaker.UnitLogic.UnitDescriptor::get_Buffs()
		IL_0008: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Buffs.Buff> Kingmaker.UnitLogic.Buffs.BuffCollection::GetEnumerator()
		IL_000d: stloc.1
		.try
		{
			IL_000e: br.s IL_0036
			// loop start (head: IL_0036)
				IL_0010: ldloc.1
				IL_0011: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Buffs.Buff>::get_Current()
				IL_0016: stloc.2
				IL_0017: ldloc.2
				IL_0018: callvirt instance !0 class Kingmaker.UnitLogic.UnitFact`1<class Kingmaker.UnitLogic.Buffs.Blueprints.BlueprintBuff>::get_Blueprint()
				IL_001d: callvirt instance bool Kingmaker.UnitLogic.Buffs.Blueprints.BlueprintBuff::get_RemoveOnResurrect()
				IL_0022: brfalse.s IL_0036

				IL_0024: ldloc.0
				IL_0025: dup
				IL_0026: brtrue.s IL_002e

				IL_0028: pop
				IL_0029: newobj instance void class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.Buffs.Buff>::.ctor()

				IL_002e: stloc.0
				IL_002f: ldloc.0
				IL_0030: ldloc.2
				IL_0031: callvirt instance void class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.Buffs.Buff>::Add(!0)

				IL_0036: ldloc.1
				IL_0037: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
				IL_003c: brtrue.s IL_0010
			// end loop

			IL_003e: leave.s IL_004a
		} // end .try
		finally
		{
			IL_0040: ldloc.1
			IL_0041: brfalse.s IL_0049

			IL_0043: ldloc.1
			IL_0044: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_0049: endfinally
		} // end handler

		IL_004a: ldloc.0
		IL_004b: brfalse.s IL_0085

		IL_004d: ldloc.0
		IL_004e: callvirt instance valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<!0> class [mscorlib]System.Collections.Generic.List`1<class Kingmaker.UnitLogic.Buffs.Buff>::GetEnumerator()
		IL_0053: stloc.3
		.try
		{
			IL_0054: br.s IL_006c
			// loop start (head: IL_006c)
				IL_0056: ldloca.s 3
				IL_0058: call instance !0 valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<class Kingmaker.UnitLogic.Buffs.Buff>::get_Current()
				IL_005d: stloc.s 4
				IL_005f: ldarg.0
				IL_0060: call instance class Kingmaker.UnitLogic.Buffs.BuffCollection Kingmaker.UnitLogic.UnitDescriptor::get_Buffs()
				IL_0065: ldloc.s 4
				IL_0067: callvirt instance void class Kingmaker.EntitySystem.EntityFactsProcessor`1<class Kingmaker.UnitLogic.Buffs.Buff>::RemoveFact(class Kingmaker.EntitySystem.EntityFact)

				IL_006c: ldloca.s 3
				IL_006e: call instance bool valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<class Kingmaker.UnitLogic.Buffs.Buff>::MoveNext()
				IL_0073: brtrue.s IL_0056
			// end loop

			IL_0075: leave.s IL_0085
		} // end .try
		finally
		{
			IL_0077: ldloca.s 3
			IL_0079: constrained. valuetype [mscorlib]System.Collections.Generic.List`1/Enumerator<class Kingmaker.UnitLogic.Buffs.Buff>
			IL_007f: callvirt instance void [mscorlib]System.IDisposable::Dispose()
			IL_0084: endfinally
		} // end handler

		IL_0085: ret
	} // end of method UnitDescriptor::RemoveBuffsOnResurrect

	.method public hidebysig 
		instance void UpdateSizeModifiers () cil managed 
	{
		// Method begins at RVA 0x31ccf0
		// Header size: 12
		// Code size: 222 (0xde)
		.maxstack 3
		.locals init (
			[0] class Kingmaker.Enums.WeaponSizeExtension/SizeModifiers
		)

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0006: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValue Kingmaker.EntitySystem.Stats.CharacterStats::AdditionalAttackBonus
		IL_000b: ldc.i4.s 20
		IL_000d: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::RemoveModifiers(valuetype Kingmaker.Enums.ModifierDescriptor)
		IL_0012: ldarg.0
		IL_0013: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0018: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueArmorClass Kingmaker.EntitySystem.Stats.CharacterStats::AC
		IL_001d: ldc.i4.s 20
		IL_001f: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::RemoveModifiers(valuetype Kingmaker.Enums.ModifierDescriptor)
		IL_0024: ldarg.0
		IL_0025: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_002a: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillStealth
		IL_002f: ldc.i4.s 20
		IL_0031: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::RemoveModifiers(valuetype Kingmaker.Enums.ModifierDescriptor)
		IL_0036: ldarg.0
		IL_0037: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_003c: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValue Kingmaker.EntitySystem.Stats.CharacterStats::Reach
		IL_0041: ldc.i4.s 20
		IL_0043: callvirt instance void Kingmaker.EntitySystem.Stats.ModifiableValue::RemoveModifiers(valuetype Kingmaker.Enums.ModifierDescriptor)
		IL_0048: ldarg.0
		IL_0049: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_004e: callvirt instance class Kingmaker.View.UnitEntityView Kingmaker.EntitySystem.Entities.UnitEntityData::get_View()
		IL_0053: ldnull
		IL_0054: call !!0 [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Utils.ObjectExtensions::Or<class Kingmaker.View.UnitEntityView>(!!0, !!0)
		IL_0059: dup
		IL_005a: brtrue.s IL_005f

		IL_005c: pop
		IL_005d: br.s IL_0064

		IL_005f: call instance void Kingmaker.View.UnitEntityView::ResetSizeScale()

		IL_0064: ldarg.0
		IL_0065: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_006a: callvirt instance valuetype Kingmaker.Enums.Size Kingmaker.UnitLogic.UnitState::get_Size()
		IL_006f: call class Kingmaker.Enums.WeaponSizeExtension/SizeModifiers Kingmaker.Enums.WeaponSizeExtension::GetModifiers(valuetype Kingmaker.Enums.Size)
		IL_0074: stloc.0
		IL_0075: ldloc.0
		IL_0076: brtrue.s IL_0079

		IL_0078: ret

		IL_0079: ldarg.0
		IL_007a: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_007f: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValue Kingmaker.EntitySystem.Stats.CharacterStats::AdditionalAttackBonus
		IL_0084: ldloc.0
		IL_0085: ldfld int32 Kingmaker.Enums.WeaponSizeExtension/SizeModifiers::AttackAndAC
		IL_008a: ldc.i4.s 20
		IL_008c: callvirt instance class Kingmaker.EntitySystem.Stats.ModifiableValue/Modifier Kingmaker.EntitySystem.Stats.ModifiableValue::AddModifier(int32, valuetype Kingmaker.Enums.ModifierDescriptor)
		IL_0091: pop
		IL_0092: ldarg.0
		IL_0093: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0098: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueArmorClass Kingmaker.EntitySystem.Stats.CharacterStats::AC
		IL_009d: ldloc.0
		IL_009e: ldfld int32 Kingmaker.Enums.WeaponSizeExtension/SizeModifiers::AttackAndAC
		IL_00a3: ldc.i4.s 20
		IL_00a5: callvirt instance class Kingmaker.EntitySystem.Stats.ModifiableValue/Modifier Kingmaker.EntitySystem.Stats.ModifiableValue::AddModifier(int32, valuetype Kingmaker.Enums.ModifierDescriptor)
		IL_00aa: pop
		IL_00ab: ldarg.0
		IL_00ac: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_00b1: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValueSkill Kingmaker.EntitySystem.Stats.CharacterStats::SkillStealth
		IL_00b6: ldloc.0
		IL_00b7: ldfld int32 Kingmaker.Enums.WeaponSizeExtension/SizeModifiers::Stealth
		IL_00bc: ldc.i4.s 20
		IL_00be: callvirt instance class Kingmaker.EntitySystem.Stats.ModifiableValue/Modifier Kingmaker.EntitySystem.Stats.ModifiableValue::AddModifier(int32, valuetype Kingmaker.Enums.ModifierDescriptor)
		IL_00c3: pop
		IL_00c4: ldarg.0
		IL_00c5: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_00ca: ldfld class Kingmaker.EntitySystem.Stats.ModifiableValue Kingmaker.EntitySystem.Stats.CharacterStats::Reach
		IL_00cf: ldloc.0
		IL_00d0: ldfld int32 Kingmaker.Enums.WeaponSizeExtension/SizeModifiers::Reach
		IL_00d5: ldc.i4.s 20
		IL_00d7: callvirt instance class Kingmaker.EntitySystem.Stats.ModifiableValue/Modifier Kingmaker.EntitySystem.Stats.ModifiableValue::AddModifier(int32, valuetype Kingmaker.Enums.ModifierDescriptor)
		IL_00dc: pop
		IL_00dd: ret
	} // end of method UnitDescriptor::UpdateSizeModifiers

	.method public hidebysig 
		instance valuetype Kingmaker.Utility.Feet GetWeaponRange (
			[opt] class Kingmaker.Blueprints.Items.Weapons.BlueprintItemWeapon weapon
		) cil managed 
	{
		.param [1] = nullref
			.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
				01 00 00 00
			)
		// Method begins at RVA 0x31cddc
		// Header size: 12
		// Code size: 86 (0x56)
		.maxstack 2
		.locals init (
			[0] valuetype Kingmaker.Utility.Feet,
			[1] valuetype Kingmaker.Utility.Feet
		)

		IL_0000: ldarg.1
		IL_0001: ldnull
		IL_0002: call !!0 Kingmaker.Blueprints.SimpleBlueprintExtendAsObject::Or<class Kingmaker.Blueprints.Items.Weapons.BlueprintItemWeapon>(!!0, !!0)
		IL_0007: dup
		IL_0008: brtrue.s IL_0012

		IL_000a: pop
		IL_000b: ldsfld valuetype Kingmaker.Utility.Feet Kingmaker.Utility.GameConsts::MinWeaponRange
		IL_0010: br.s IL_0017

		IL_0012: call instance valuetype Kingmaker.Utility.Feet Kingmaker.Blueprints.Items.Weapons.BlueprintItemWeapon::get_AttackRange()

		IL_0017: stloc.0
		IL_0018: ldarg.0
		IL_0019: ldfld class Kingmaker.UnitLogic.UnitState Kingmaker.UnitLogic.UnitDescriptor::State
		IL_001e: ldfld class Kingmaker.UnitLogic.UnitMechanicFeatures Kingmaker.UnitLogic.UnitState::Features
		IL_0023: ldfld class Kingmaker.Utility.CountableFlag Kingmaker.UnitLogic.UnitMechanicFeatures::PointBlankRange
		IL_0028: call bool Kingmaker.Utility.CountableFlag::op_Implicit(class Kingmaker.Utility.CountableFlag)
		IL_002d: brfalse.s IL_0042

		IL_002f: ldloca.s 0
		IL_0031: call instance int32 Kingmaker.Utility.Feet::get_Value()
		IL_0036: ldc.i4.s 30
		IL_0038: ble.s IL_0042

		IL_003a: ldc.i4.s 30
		IL_003c: call valuetype Kingmaker.Utility.Feet Kingmaker.Utility.FeetExtension::Feet(int32)
		IL_0041: stloc.0

		IL_0042: ldarg.0
		IL_0043: ldfld class Kingmaker.EntitySystem.Stats.CharacterStats Kingmaker.UnitLogic.UnitDescriptor::Stats
		IL_0048: callvirt instance valuetype Kingmaker.Utility.Feet Kingmaker.EntitySystem.Stats.CharacterStats::get_ReachRange()
		IL_004d: stloc.1
		IL_004e: ldloc.0
		IL_004f: ldloc.1
		IL_0050: call valuetype Kingmaker.Utility.Feet Kingmaker.Utility.Feet::op_Addition(valuetype Kingmaker.Utility.Feet, valuetype Kingmaker.Utility.Feet)
		IL_0055: ret
	} // end of method UnitDescriptor::GetWeaponRange

	.method public hidebysig 
		instance void OnDifficultyChanged () cil managed 
	{
		// Method begins at RVA 0x31ce40
		// Header size: 12
		// Code size: 167 (0xa7)
		.maxstack 2
		.locals init (
			[0] class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Feature>,
			[1] class Kingmaker.UnitLogic.Feature,
			[2] class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Buffs.Buff>,
			[3] class Kingmaker.UnitLogic.Buffs.Buff
		)

		IL_0000: ldarg.0
		IL_0001: call instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsPlayerFaction()
		IL_0006: brfalse.s IL_0009

		IL_0008: ret

		IL_0009: ldarg.0
		IL_000a: ldfld class Kingmaker.UnitLogic.UnitProgressionData Kingmaker.UnitLogic.UnitDescriptor::Progression
		IL_000f: callvirt instance class Kingmaker.UnitLogic.FeatureCollection Kingmaker.UnitLogic.UnitProgressionData::get_Features()
		IL_0014: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Feature> Kingmaker.UnitLogic.FeatureCollection::GetEnumerator()
		IL_0019: stloc.0
		.try
		{
			IL_001a: br.s IL_0046
			// loop start (head: IL_0046)
				IL_001c: ldloc.0
				IL_001d: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Feature>::get_Current()
				IL_0022: stloc.1
				IL_0023: ldloc.1
				IL_0024: callvirt instance class Kingmaker.UnitLogic.Mechanics.MechanicsContext Kingmaker.UnitLogic.Feature::get_Context()
				IL_0029: ldfld class Kingmaker.Blueprints.BlueprintScriptableObject Kingmaker.UnitLogic.Mechanics.MechanicsContext::AssociatedBlueprint
				IL_002e: call !!0 Kingmaker.Blueprints.BlueprintExtenstions::GetComponent<class Kingmaker.UnitLogic.Mechanics.Components.ContextAbilityParamsCalculator>(class Kingmaker.Blueprints.BlueprintScriptableObject)
				IL_0033: call bool Kingmaker.Blueprints.BlueprintComponent::op_Implicit(class Kingmaker.Blueprints.BlueprintComponent)
				IL_0038: brfalse.s IL_0046

				IL_003a: ldloc.1
				IL_003b: callvirt instance class Kingmaker.UnitLogic.Mechanics.MechanicsContext Kingmaker.UnitLogic.Feature::get_Context()
				IL_0040: ldc.i4.0
				IL_0041: callvirt instance void Kingmaker.UnitLogic.Mechanics.MechanicsContext::RecalculateAbilityParams(bool)

				IL_0046: ldloc.0
				IL_0047: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
				IL_004c: brtrue.s IL_001c
			// end loop

			IL_004e: leave.s IL_005a
		} // end .try
		finally
		{
			IL_0050: ldloc.0
			IL_0051: brfalse.s IL_0059

			IL_0053: ldloc.0
			IL_0054: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_0059: endfinally
		} // end handler

		IL_005a: ldarg.0
		IL_005b: call instance class Kingmaker.UnitLogic.Buffs.BuffCollection Kingmaker.UnitLogic.UnitDescriptor::get_Buffs()
		IL_0060: callvirt instance class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Buffs.Buff> Kingmaker.UnitLogic.Buffs.BuffCollection::GetEnumerator()
		IL_0065: stloc.2
		.try
		{
			IL_0066: br.s IL_0092
			// loop start (head: IL_0092)
				IL_0068: ldloc.2
				IL_0069: callvirt instance !0 class [mscorlib]System.Collections.Generic.IEnumerator`1<class Kingmaker.UnitLogic.Buffs.Buff>::get_Current()
				IL_006e: stloc.3
				IL_006f: ldloc.3
				IL_0070: callvirt instance class Kingmaker.UnitLogic.Mechanics.MechanicsContext Kingmaker.UnitLogic.Buffs.Buff::get_Context()
				IL_0075: ldfld class Kingmaker.Blueprints.BlueprintScriptableObject Kingmaker.UnitLogic.Mechanics.MechanicsContext::AssociatedBlueprint
				IL_007a: call !!0 Kingmaker.Blueprints.BlueprintExtenstions::GetComponent<class Kingmaker.UnitLogic.Mechanics.Components.ContextAbilityParamsCalculator>(class Kingmaker.Blueprints.BlueprintScriptableObject)
				IL_007f: call bool Kingmaker.Blueprints.BlueprintComponent::op_Implicit(class Kingmaker.Blueprints.BlueprintComponent)
				IL_0084: brfalse.s IL_0092

				IL_0086: ldloc.3
				IL_0087: callvirt instance class Kingmaker.UnitLogic.Mechanics.MechanicsContext Kingmaker.UnitLogic.Buffs.Buff::get_Context()
				IL_008c: ldc.i4.0
				IL_008d: callvirt instance void Kingmaker.UnitLogic.Mechanics.MechanicsContext::RecalculateAbilityParams(bool)

				IL_0092: ldloc.2
				IL_0093: callvirt instance bool [mscorlib]System.Collections.IEnumerator::MoveNext()
				IL_0098: brtrue.s IL_0068
			// end loop

			IL_009a: leave.s IL_00a6
		} // end .try
		finally
		{
			IL_009c: ldloc.2
			IL_009d: brfalse.s IL_00a5

			IL_009f: ldloc.2
			IL_00a0: callvirt instance void [mscorlib]System.IDisposable::Dispose()

			IL_00a5: endfinally
		} // end handler

		IL_00a6: ret
	} // end of method UnitDescriptor::OnDifficultyChanged

	.method public hidebysig specialname static 
		class Kingmaker.EntitySystem.Entities.UnitEntityData op_Implicit (
			class Kingmaker.UnitLogic.UnitDescriptor unit
		) cil managed 
	{
		// Method begins at RVA 0x31cf10
		// Header size: 1
		// Code size: 12 (0xc)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: brtrue.s IL_0005

		IL_0003: ldnull
		IL_0004: ret

		IL_0005: ldarg.0
		IL_0006: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_000b: ret
	} // end of method UnitDescriptor::op_Implicit

	.method public hidebysig 
		instance void AddEssentialMark () cil managed 
	{
		// Method begins at RVA 0x31cf1d
		// Header size: 1
		// Code size: 54 (0x36)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Utility.CountableFlag Kingmaker.UnitLogic.UnitDescriptor::m_IsEssentialForGame
		IL_0006: callvirt instance void Kingmaker.Utility.CountableFlag::Retain()
		IL_000b: ldsfld class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog/History::Party
		IL_0010: ldstr "AddEssentialMark: {0}, count {1}"
		IL_0015: ldarg.0
		IL_0016: ldarg.0
		IL_0017: ldfld class Kingmaker.Utility.CountableFlag Kingmaker.UnitLogic.UnitDescriptor::m_IsEssentialForGame
		IL_001c: callvirt instance int32 Kingmaker.Utility.CountableFlag::get_Count()
		IL_0021: box [mscorlib]System.Int32
		IL_0026: call string [mscorlib]System.String::Format(string, object, object)
		IL_002b: call !!0[] [mscorlib]System.Array::Empty<object>()
		IL_0030: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Log(string, object[])
		IL_0035: ret
	} // end of method UnitDescriptor::AddEssentialMark

	.method public hidebysig 
		instance void RemoveEssentialMark () cil managed 
	{
		// Method begins at RVA 0x31cf54
		// Header size: 1
		// Code size: 54 (0x36)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class Kingmaker.Utility.CountableFlag Kingmaker.UnitLogic.UnitDescriptor::m_IsEssentialForGame
		IL_0006: callvirt instance void Kingmaker.Utility.CountableFlag::Release()
		IL_000b: ldsfld class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog/History::Party
		IL_0010: ldstr "RemoveEssentialMark: {0}, count {1}"
		IL_0015: ldarg.0
		IL_0016: ldarg.0
		IL_0017: ldfld class Kingmaker.Utility.CountableFlag Kingmaker.UnitLogic.UnitDescriptor::m_IsEssentialForGame
		IL_001c: callvirt instance int32 Kingmaker.Utility.CountableFlag::get_Count()
		IL_0021: box [mscorlib]System.Int32
		IL_0026: call string [mscorlib]System.String::Format(string, object, object)
		IL_002b: call !!0[] [mscorlib]System.Array::Empty<object>()
		IL_0030: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Log(string, object[])
		IL_0035: ret
	} // end of method UnitDescriptor::RemoveEssentialMark

	.method private hidebysig 
		instance void '<ApplyPostLoadFixes>b__149_0' (
			class Kingmaker.UnitLogic.Mechanics.Components.Fixers.FixUnitOnPostLoad a
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31cf8c
		// Header size: 12
		// Code size: 97 (0x61)
		.maxstack 4

		IL_0000: ldarg.0
		IL_0001: ldfld class [mscorlib]System.Collections.Generic.List`1<string> Kingmaker.UnitLogic.UnitDescriptor::m_AppliedFixers
		IL_0006: ldarg.1
		IL_0007: ldfld string Kingmaker.Blueprints.BlueprintComponent::name
		IL_000c: call bool Kingmaker.Utility.LinqExtensions::HasItem<string>(class [mscorlib]System.Collections.Generic.IList`1<!!0>, !!0)
		IL_0011: brtrue.s IL_0060

		IL_0013: ldarg.1
		IL_0014: ldarg.0
		IL_0015: callvirt instance void Kingmaker.UnitLogic.Mechanics.Components.Fixers.FixUnitOnPostLoad::OnPostLoad(class Kingmaker.UnitLogic.UnitDescriptor)
		IL_001a: ldarg.0
		IL_001b: ldarg.0
		IL_001c: ldfld class [mscorlib]System.Collections.Generic.List`1<string> Kingmaker.UnitLogic.UnitDescriptor::m_AppliedFixers
		IL_0021: dup
		IL_0022: brtrue.s IL_002a

		IL_0024: pop
		IL_0025: newobj instance void class [mscorlib]System.Collections.Generic.List`1<string>::.ctor()

		IL_002a: stfld class [mscorlib]System.Collections.Generic.List`1<string> Kingmaker.UnitLogic.UnitDescriptor::m_AppliedFixers
		IL_002f: ldarg.0
		IL_0030: ldfld class [mscorlib]System.Collections.Generic.List`1<string> Kingmaker.UnitLogic.UnitDescriptor::m_AppliedFixers
		IL_0035: ldarg.1
		IL_0036: ldfld string Kingmaker.Blueprints.BlueprintComponent::name
		IL_003b: callvirt instance void class [mscorlib]System.Collections.Generic.List`1<string>::Add(!0)
		IL_0040: call class [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel Kingmaker.PFLog::get_Default()
		IL_0045: ldstr "Fixer applied to unit: {0} ({1})"
		IL_004a: ldarg.0
		IL_004b: ldarg.1
		IL_004c: ldfld string Kingmaker.Blueprints.BlueprintComponent::name
		IL_0051: call string [mscorlib]System.String::Format(string, object, object)
		IL_0056: call !!0[] [mscorlib]System.Array::Empty<object>()
		IL_005b: callvirt instance void [Owlcat.Runtime.Core]Owlcat.Runtime.Core.Logging.LogChannel::Log(string, object[])

		IL_0060: ret
	} // end of method UnitDescriptor::'<ApplyPostLoadFixes>b__149_0'

	.method private hidebysig 
		instance void '<SwitchFactions>b__154_0' (
			class Kingmaker.PubSubSystem.IUnitFactionHandler h
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31cff9
		// Header size: 1
		// Code size: 13 (0xd)
		.maxstack 8

		IL_0000: ldarg.1
		IL_0001: ldarg.0
		IL_0002: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0007: callvirt instance void Kingmaker.PubSubSystem.IUnitFactionHandler::HandleFactionChanged(class Kingmaker.EntitySystem.Entities.UnitEntityData)
		IL_000c: ret
	} // end of method UnitDescriptor::'<SwitchFactions>b__154_0'

	.method private hidebysig 
		instance void '<.ctor>b__158_0' (
			class Kingmaker.UnitLogic.Mechanics.Components.Fixers.FixUnitOnPostLoad a
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31d007
		// Header size: 1
		// Code size: 58 (0x3a)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: ldfld class [mscorlib]System.Collections.Generic.List`1<string> Kingmaker.UnitLogic.UnitDescriptor::m_AppliedFixers
		IL_0006: ldarg.1
		IL_0007: ldfld string Kingmaker.Blueprints.BlueprintComponent::name
		IL_000c: call bool Kingmaker.Utility.LinqExtensions::HasItem<string>(class [mscorlib]System.Collections.Generic.IList`1<!!0>, !!0)
		IL_0011: brtrue.s IL_0039

		IL_0013: ldarg.0
		IL_0014: ldarg.0
		IL_0015: ldfld class [mscorlib]System.Collections.Generic.List`1<string> Kingmaker.UnitLogic.UnitDescriptor::m_AppliedFixers
		IL_001a: dup
		IL_001b: brtrue.s IL_0023

		IL_001d: pop
		IL_001e: newobj instance void class [mscorlib]System.Collections.Generic.List`1<string>::.ctor()

		IL_0023: stfld class [mscorlib]System.Collections.Generic.List`1<string> Kingmaker.UnitLogic.UnitDescriptor::m_AppliedFixers
		IL_0028: ldarg.0
		IL_0029: ldfld class [mscorlib]System.Collections.Generic.List`1<string> Kingmaker.UnitLogic.UnitDescriptor::m_AppliedFixers
		IL_002e: ldarg.1
		IL_002f: ldfld string Kingmaker.Blueprints.BlueprintComponent::name
		IL_0034: callvirt instance void class [mscorlib]System.Collections.Generic.List`1<string>::Add(!0)

		IL_0039: ret
	} // end of method UnitDescriptor::'<.ctor>b__158_0'

	.method private hidebysig 
		instance void '<Resurrect>b__178_0' (
			class Kingmaker.PubSubSystem.IUnitResurrectedHandler h
		) cil managed 
	{
		.custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Method begins at RVA 0x31d042
		// Header size: 1
		// Code size: 13 (0xd)
		.maxstack 8

		IL_0000: ldarg.1
		IL_0001: ldarg.0
		IL_0002: call instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		IL_0007: callvirt instance void Kingmaker.PubSubSystem.IUnitResurrectedHandler::HandleUnitResurrected(class Kingmaker.EntitySystem.Entities.UnitEntityData)
		IL_000c: ret
	} // end of method UnitDescriptor::'<Resurrect>b__178_0'

	// Properties
	.property instance class Kingmaker.Items.UnitBody Body()
	{
		.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
			01 00 00 00
		)
		.get instance class Kingmaker.Items.UnitBody Kingmaker.UnitLogic.UnitDescriptor::get_Body()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_Body(class Kingmaker.Items.UnitBody)
	}
	.property instance class Kingmaker.Blueprints.BlueprintUnit ReplaceBlueprintForInspection()
	{
		.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
			01 00 01 00 54 55 6c 4e 65 77 74 6f 6e 73 6f 66
			74 2e 4a 73 6f 6e 2e 44 65 66 61 75 6c 74 56 61
			6c 75 65 48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77
			74 6f 6e 73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65
			72 73 69 6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43
			75 6c 74 75 72 65 3d 6e 65 75 74 72 61 6c 2c 20
			50 75 62 6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e
			75 6c 6c 14 44 65 66 61 75 6c 74 56 61 6c 75 65
			48 61 6e 64 6c 69 6e 67 01 00 00 00
		)
		.get instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_ReplaceBlueprintForInspection()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_ReplaceBlueprintForInspection(class Kingmaker.Blueprints.BlueprintUnit)
	}
	.property instance class Kingmaker.UnitLogic.UnitBrain Brain()
	{
		.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
			01 00 00 00
		)
		.get instance class Kingmaker.UnitLogic.UnitBrain Kingmaker.UnitLogic.UnitDescriptor::get_Brain()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_Brain(class Kingmaker.UnitLogic.UnitBrain)
	}
	.property instance class Kingmaker.Blueprints.BlueprintUnit OriginalBlueprint()
	{
		.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
			01 00 00 00
		)
		.get instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_OriginalBlueprint()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_OriginalBlueprint(class Kingmaker.Blueprints.BlueprintUnit)
	}
	.property instance class Kingmaker.Blueprints.BlueprintUnit Blueprint()
	{
		.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
			01 00 00 00
		)
		.get instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_Blueprint()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_Blueprint(class Kingmaker.Blueprints.BlueprintUnit)
	}
	.property instance class Kingmaker.UnitLogic.UnitFact MainFact()
	{
		.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
			01 00 00 00
		)
		.get instance class Kingmaker.UnitLogic.UnitFact Kingmaker.UnitLogic.UnitDescriptor::get_MainFact()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_MainFact(class Kingmaker.UnitLogic.UnitFact)
	}
	.property instance valuetype Kingmaker.UnitLogic.Encumbrance Encumbrance()
	{
		.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
			01 00 00 00
		)
		.get instance valuetype Kingmaker.UnitLogic.Encumbrance Kingmaker.UnitLogic.UnitDescriptor::get_Encumbrance()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_Encumbrance(valuetype Kingmaker.UnitLogic.Encumbrance)
	}
	.property instance bool HasOwnInventory()
	{
		.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
			01 00 00 00
		)
		.get instance bool Kingmaker.UnitLogic.UnitDescriptor::get_HasOwnInventory()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_HasOwnInventory(bool)
	}
	.property instance valuetype [mscorlib]System.Nullable`1<valuetype [mscorlib]System.TimeSpan> LastRestTime()
	{
		.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
			01 00 01 00 54 55 69 4e 65 77 74 6f 6e 73 6f 66
			74 2e 4a 73 6f 6e 2e 4e 75 6c 6c 56 61 6c 75 65
			48 61 6e 64 6c 69 6e 67 2c 20 4e 65 77 74 6f 6e
			73 6f 66 74 2e 4a 73 6f 6e 2c 20 56 65 72 73 69
			6f 6e 3d 38 2e 30 2e 30 2e 30 2c 20 43 75 6c 74
			75 72 65 3d 6e 65 75 74 72 61 6c 2c 20 50 75 62
			6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 6e 75 6c 6c
			11 4e 75 6c 6c 56 61 6c 75 65 48 61 6e 64 6c 69
			6e 67 01 00 00 00
		)
		.get instance valuetype [mscorlib]System.Nullable`1<valuetype [mscorlib]System.TimeSpan> Kingmaker.UnitLogic.UnitDescriptor::get_LastRestTime()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_LastRestTime(valuetype [mscorlib]System.Nullable`1<valuetype [mscorlib]System.TimeSpan>)
	}
	.property instance class Kingmaker.UnitLogic.DollData Doll()
	{
		.custom instance void [Newtonsoft.Json]Newtonsoft.Json.JsonPropertyAttribute::.ctor() = (
			01 00 00 00
		)
		.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
			01 00 00 00
		)
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_Doll(class Kingmaker.UnitLogic.DollData)
	}
	.property instance class Kingmaker.EntitySystem.Entities.UnitEntityData Unit()
	{
		.get instance class Kingmaker.EntitySystem.Entities.UnitEntityData Kingmaker.UnitLogic.UnitDescriptor::get_Unit()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_Unit(class Kingmaker.EntitySystem.Entities.UnitEntityData)
	}
	.property instance bool IsTurnedOn()
	{
		.get instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsTurnedOn()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_IsTurnedOn(bool)
	}
	.property instance class Kingmaker.Blueprints.BlueprintFaction Faction()
	{
		.get instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_Faction()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_Faction(class Kingmaker.Blueprints.BlueprintFaction)
	}
	.property instance class Kingmaker.Blueprints.BlueprintFaction FactionOriginal()
	{
		.get instance class Kingmaker.Blueprints.BlueprintFaction Kingmaker.UnitLogic.UnitDescriptor::get_FactionOriginal()
	}
	.property instance int32 Damage()
	{
		.get instance int32 Kingmaker.UnitLogic.UnitDescriptor::get_Damage()
		.set instance void Kingmaker.UnitLogic.UnitDescriptor::set_Damage(int32)
	}
	.property instance class Kingmaker.UnitLogic.Abilities.AbilityCollection Abilities()
	{
		.get instance class Kingmaker.UnitLogic.Abilities.AbilityCollection Kingmaker.UnitLogic.UnitDescriptor::get_Abilities()
	}
	.property instance class Kingmaker.UnitLogic.ActivatableAbilities.ActivatableAbilityCollection ActivatableAbilities()
	{
		.get instance class Kingmaker.UnitLogic.ActivatableAbilities.ActivatableAbilityCollection Kingmaker.UnitLogic.UnitDescriptor::get_ActivatableAbilities()
	}
	.property instance class Kingmaker.UnitLogic.Buffs.BuffCollection Buffs()
	{
		.get instance class Kingmaker.UnitLogic.Buffs.BuffCollection Kingmaker.UnitLogic.UnitDescriptor::get_Buffs()
	}
	.property instance int32 DamageNonLethal()
	{
		.get instance int32 Kingmaker.UnitLogic.UnitDescriptor::get_DamageNonLethal()
	}
	.property instance valuetype Kingmaker.Blueprints.Gender Gender()
	{
		.get instance valuetype Kingmaker.Blueprints.Gender Kingmaker.UnitLogic.UnitDescriptor::get_Gender()
	}
	.property instance bool IsLeftHanded()
	{
		.get instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsLeftHanded()
	}
	.property instance string CharacterName()
	{
		.get instance string Kingmaker.UnitLogic.UnitDescriptor::get_CharacterName()
	}
	.property instance class Kingmaker.Visual.Sound.BlueprintUnitAsksList Asks()
	{
		.custom instance void [UnityEngine.CoreModule]JetBrains.Annotations.CanBeNullAttribute::.ctor() = (
			01 00 00 00
		)
		.get instance class Kingmaker.Visual.Sound.BlueprintUnitAsksList Kingmaker.UnitLogic.UnitDescriptor::get_Asks()
	}
	.property instance bool UseClassEquipment()
	{
		.get instance bool Kingmaker.UnitLogic.UnitDescriptor::get_UseClassEquipment()
	}
	.property instance valuetype Kingmaker.Enums.Size OriginalSize()
	{
		.get instance valuetype Kingmaker.Enums.Size Kingmaker.UnitLogic.UnitDescriptor::get_OriginalSize()
	}
	.property instance class Kingmaker.UnitLogic.Mechanics.MechanicsContext Context()
	{
		.get instance class Kingmaker.UnitLogic.Mechanics.MechanicsContext Kingmaker.UnitLogic.UnitDescriptor::get_Context()
	}
	.property instance class Kingmaker.EntitySystem.EntityFactsManager Facts()
	{
		.get instance class Kingmaker.EntitySystem.EntityFactsManager Kingmaker.UnitLogic.UnitDescriptor::get_Facts()
	}
	.property instance class Kingmaker.Items.ItemsCollection Inventory()
	{
		.get instance class Kingmaker.Items.ItemsCollection Kingmaker.UnitLogic.UnitDescriptor::get_Inventory()
	}
	.property instance int32 HPLeft()
	{
		.get instance int32 Kingmaker.UnitLogic.UnitDescriptor::get_HPLeft()
	}
	.property instance int32 MaxHP()
	{
		.get instance int32 Kingmaker.UnitLogic.UnitDescriptor::get_MaxHP()
	}
	.property instance int32 TemporaryHP()
	{
		.get instance int32 Kingmaker.UnitLogic.UnitDescriptor::get_TemporaryHP()
	}
	.property instance class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.Spellbook> Spellbooks()
	{
		.get instance class [mscorlib]System.Collections.Generic.IEnumerable`1<class Kingmaker.UnitLogic.Spellbook> Kingmaker.UnitLogic.UnitDescriptor::get_Spellbooks()
	}
	.property instance bool IsPlayerFaction()
	{
		.get instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsPlayerFaction()
	}
	.property instance bool HasUMDSkill()
	{
		.get instance bool Kingmaker.UnitLogic.UnitDescriptor::get_HasUMDSkill()
	}
	.property instance bool IsImmuneToVisualEffects()
	{
		.get instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsImmuneToVisualEffects()
	}
	.property instance bool IsSeeInvisibility()
	{
		.get instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsSeeInvisibility()
	}
	.property instance bool IsUndead()
	{
		.get instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsUndead()
	}
	.property instance bool IsEssentialForGame()
	{
		.get instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsEssentialForGame()
	}
	.property instance bool UseMartialArts()
	{
		.get instance bool Kingmaker.UnitLogic.UnitDescriptor::get_UseMartialArts()
	}
	.property instance class Kingmaker.Blueprints.PortraitData Portrait()
	{
		.get instance class Kingmaker.Blueprints.PortraitData Kingmaker.UnitLogic.UnitDescriptor::get_Portrait()
	}
	.property instance class Kingmaker.Blueprints.PortraitData OverridePortrait()
	{
		.get instance class Kingmaker.Blueprints.PortraitData Kingmaker.UnitLogic.UnitDescriptor::get_OverridePortrait()
	}
	.property instance class Kingmaker.Blueprints.PortraitData CrossPortrait()
	{
		.get instance class Kingmaker.Blueprints.PortraitData Kingmaker.UnitLogic.UnitDescriptor::get_CrossPortrait()
	}
	.property instance bool IsMainCharacter()
	{
		.get instance bool Kingmaker.UnitLogic.UnitDescriptor::get_IsMainCharacter()
	}
	.property instance class Kingmaker.Blueprints.BlueprintUnit BlueprintForInspection()
	{
		.get instance class Kingmaker.Blueprints.BlueprintUnit Kingmaker.UnitLogic.UnitDescriptor::get_BlueprintForInspection()
	}

} // end of class Kingmaker.UnitLogic.UnitDescriptor
