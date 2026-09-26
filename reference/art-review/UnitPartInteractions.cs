using System;
using System.Collections.Generic;
using System.Linq;
using JetBrains.Annotations;
using Kingmaker.Blueprints;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.QA;
using Kingmaker.UnitLogic.Interaction;
using Kingmaker.Utility;
using Newtonsoft.Json;

namespace Kingmaker.UnitLogic.Parts;

public class UnitPartInteractions : OldStyleUnitPart, IUnitPartSurviveRespec
{
	public enum PriorityType
	{
		None = 0,
		Spawner = 100,
		EtudeBracket = 200
	}

	[NotNull]
	private readonly List<IUnitInteraction> m_Interactions = new List<IUnitInteraction>();

	public readonly Dictionary<UnitEntityData, float> Distances = new Dictionary<UnitEntityData, float>();

	public float Cooldown;

	public bool HasApproachInteractions { get; private set; }

	[JsonProperty]
	public bool AreInteractionsEnabled { get; set; } = true;

	bool IUnitPartSurviveRespec.ShouldSurviveRespec => true;

	public static void SetupBlueprintInteractions(UnitEntityData unit)
	{
		List<IUnitInteraction> interactions = unit.Blueprint.GetComponents<UnitInteractionComponent>().Select((Func<UnitInteractionComponent, IUnitInteraction>)((UnitInteractionComponent i) => i)).ToList();
		AddInteractions(unit, interactions);
	}

	public void AddInteraction(IUnitInteraction interaction)
	{
		m_Interactions.Insert(0, interaction);
		CheckForApproachInteractions();
	}

	private void CheckForApproachInteractions()
	{
		HasApproachInteractions = false;
		if (!AreInteractionsEnabled)
		{
			return;
		}
		foreach (IUnitInteraction interaction in m_Interactions)
		{
			if (interaction.IsApproach)
			{
				HasApproachInteractions = true;
				break;
			}
		}
	}

	[CanBeNull]
	public IUnitInteraction SelectClickInteraction(UnitEntityData initiator)
	{
		if (!AreInteractionsEnabled)
		{
			return null;
		}
		IUnitInteraction unitInteraction = null;
		IUnitInteraction unitInteraction2 = null;
		for (int i = 0; i < m_Interactions.Count; i++)
		{
			IUnitInteraction unitInteraction3 = m_Interactions[i];
			if (!unitInteraction3.IsApproach && (unitInteraction == null || unitInteraction.Priority <= unitInteraction3.Priority) && unitInteraction3.IsAvailable(initiator, base.Owner.Unit))
			{
				if (unitInteraction != null && unitInteraction.Priority == unitInteraction3.Priority)
				{
					unitInteraction2 = unitInteraction;
				}
				unitInteraction = unitInteraction3;
			}
		}
		if (BuildModeUtility.IsDevelopment && unitInteraction != null && unitInteraction2 != null && unitInteraction2.Priority == unitInteraction.Priority)
		{
			PFLog.Default.ErrorWithReport($"Unit {base.Owner} has multiple available interactions: {unitInteraction} and  {unitInteraction2}");
			return null;
		}
		return unitInteraction;
	}

	[CanBeNull]
	public IUnitInteraction SelectApproachInteraction(UnitEntityData initiator, float distance)
	{
		if (!AreInteractionsEnabled)
		{
			return null;
		}
		bool isInStealth = initiator.Descriptor.State.IsInStealth;
		for (int i = 0; i < m_Interactions.Count; i++)
		{
			IUnitInteraction unitInteraction = m_Interactions[i];
			if (unitInteraction.IsApproach)
			{
				bool flag = (unitInteraction as IUnitInteractionApproach)?.AllowStealthed ?? false;
				if ((!isInStealth || flag) && !(distance > unitInteraction.Distance) && unitInteraction.IsAvailable(initiator, base.Owner.Unit))
				{
					return unitInteraction;
				}
			}
		}
		return null;
	}

	public void RemoveInteraction(IUnitInteraction interaction)
	{
		m_Interactions.Remove(interaction);
	}

	public void RemoveInteractions(Predicate<IUnitInteraction> pred)
	{
		m_Interactions.RemoveAll(pred);
	}

	void IUnitPartSurviveRespec.CopyAfterRespec(UnitEntityData toUnit)
	{
		AddInteractions(toUnit, m_Interactions);
	}

	private static void AddInteractions(UnitEntityData unit, List<IUnitInteraction> interactions)
	{
		if (interactions.Count > 0)
		{
			UnitPartInteractions unitPartInteractions = unit.Ensure<UnitPartInteractions>();
			unitPartInteractions.m_Interactions.AddRange(interactions);
			unitPartInteractions.CheckForApproachInteractions();
		}
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
