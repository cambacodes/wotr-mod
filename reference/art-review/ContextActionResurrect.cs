using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Blueprints.Root;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic.Buffs.Blueprints;
using Kingmaker.UnitLogic.Buffs.Components;
using Kingmaker.UnitLogic.Parts;
using Kingmaker.Utility;
using Owlcat.QA.Validation;
using UnityEngine;

namespace Kingmaker.UnitLogic.Mechanics.Actions;

[TypeId("9b265905a4c4bf7419492ef8dd825e1d")]
public class ContextActionResurrect : ContextAction
{
	public bool FullRestore;

	[HideIf("FullRestore")]
	public float ResultHealth;

	[SerializeField]
	[ValidateHasComponent(typeof(ResurrectionLogic))]
	private BlueprintBuffReference m_CustomResurrectionBuff;

	public override string GetCaption()
	{
		return "Resurrect";
	}

	public override void RunAction()
	{
		UnitEntityData unit = base.Target.Unit;
		if (unit == null)
		{
			PFLog.Default.Error("Can't be applied to point");
			return;
		}
		if (base.Context.MaybeCaster == null)
		{
			PFLog.Default.Error(this, "Caster is missing");
			return;
		}
		UnitEntityData pair = UnitPartDualCompanion.GetPair(unit);
		if (FullRestore)
		{
			unit.Descriptor.ResurrectAndFullRestore(base.Context.MaybeCaster);
			pair?.Descriptor.ResurrectAndFullRestore(base.Context.MaybeCaster);
		}
		else
		{
			unit.Descriptor.Resurrect(base.Context.MaybeCaster, ResultHealth);
			pair?.Descriptor.Resurrect(base.Context.MaybeCaster, ResultHealth);
		}
		BlueprintBuff blueprint = m_CustomResurrectionBuff?.Get() ?? BlueprintRoot.Instance.SystemMechanics.ResurrectionBuff;
		unit.Descriptor.AddBuff(blueprint, base.Context, 1.Rounds().Seconds);
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
