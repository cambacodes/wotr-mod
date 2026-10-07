using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Designers.EventConditionActionSystem.ContextData;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic.Commands.Base;
using Kingmaker.UnitLogic.Interaction;
using Kingmaker.UnitLogic.Parts;
using Kingmaker.Utility;
using UnityEngine;

namespace Kingmaker.Blueprints;

[AllowedOn(typeof(BlueprintUnit), false)]
[TypeId("e090ed34b87f41e4e826b4d6dff90462")]
public abstract class UnitInteractionComponent : BlueprintComponent, IUnitInteraction
{
	[SerializeField]
	private float m_OverrideDistance;

	public ConditionsChecker Conditions;

	public bool TriggerOnApproach;

	[ShowIf("TriggerOnApproach")]
	public bool TriggerOnParty = true;

	[ShowIf("TriggerOnApproach")]
	public float Cooldown = 5f;

	public float Distance
	{
		get
		{
			if (!m_OverrideDistance.Equals(0f))
			{
				return m_OverrideDistance;
			}
			return 2f;
		}
	}

	public bool IsApproach => TriggerOnApproach;

	public float ApproachCooldown => Cooldown;

	public bool MainPlayerPreferred => true;

	public UnitPartInteractions.PriorityType Priority => UnitPartInteractions.PriorityType.None;

	public virtual bool IsAvailable(UnitEntityData initiator, UnitEntityData target)
	{
		if (target.Descriptor.State.IsHelpless)
		{
			return false;
		}
		if (TriggerOnApproach && TriggerOnParty)
		{
			if (!initiator.IsDirectlyControllable)
			{
				return false;
			}
			if (initiator.IsPet)
			{
				return false;
			}
			if (initiator.Get<UnitPartSummonedMonster>() != null)
			{
				return false;
			}
		}
		if (!Conditions.HasConditions)
		{
			return true;
		}
		using (ContextData<InteractingUnitData>.Request().Setup(initiator))
		{
			using (ContextData<ClickedUnitData>.Request().Setup(target))
			{
				return Conditions.Check();
			}
		}
	}

	public abstract UnitCommand.ResultType Interact(UnitEntityData user, UnitEntityData target);
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
