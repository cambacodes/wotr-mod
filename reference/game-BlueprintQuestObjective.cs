using System;
using System.Collections.Generic;
using JetBrains.Annotations;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints.Area;
using Kingmaker.Blueprints.Facts;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Enums;
using Kingmaker.Globalmap.Blueprints;
using Kingmaker.Localization;
using Kingmaker.Utility;
using Owlcat.QA.Validation;
using UnityEngine;

namespace Kingmaker.Blueprints.Quests;

[TypeId("9d27cf036b8dcef408e34b42d5234400")]
public class BlueprintQuestObjective : BlueprintFact, IQuestReference, IQuestObjectiveReference
{
	public enum Type
	{
		Objective,
		Addendum,
		AddendumStartingAutomatically
	}

	[SerializeField]
	[HideInInspector]
	private List<BlueprintQuestObjectiveReference> m_Addendums = new List<BlueprintQuestObjectiveReference>();

	[SerializeField]
	private List<BlueprintAreaReference> m_Areas = new List<BlueprintAreaReference>();

	[NotNull]
	public LocalizedString Title;

	public List<BlueprintGlobalMapPoint.Reference> Locations;

	public List<BlueprintMultiEntranceEntry.Reference> MultiEntranceEntries;

	[NotNull]
	public LocalizedString Description;

	public int AutoFailDays;

	public bool IsFakeFail;

	public bool StartOnKingdomTime;

	[SerializeField]
	[HideInInspector]
	private bool m_FinishParent;

	[SerializeField]
	private bool m_Hidden;

	[SerializeField]
	[HideInInspector]
	private List<BlueprintQuestObjectiveReference> m_NextObjectives = new List<BlueprintQuestObjectiveReference>();

	[SerializeField]
	[InspectorReadOnly]
	private BlueprintQuestReference m_Quest;

	[SerializeField]
	[InspectorReadOnly]
	private Type m_Type;

	private ReferenceListProxy<BlueprintQuestObjective, BlueprintQuestObjectiveReference> m_NextObjectivesProxy;

	private ReferenceListProxy<BlueprintQuestObjective, BlueprintQuestObjectiveReference> m_AddendumsProxy;

	private ReferenceListProxy<BlueprintArea, BlueprintAreaReference> m_AreasProxy;

	public BlueprintQuest Quest => m_Quest.Get();

	public IList<BlueprintQuestObjective> NextObjectives
	{
		get
		{
			ReferenceListProxy<BlueprintQuestObjective, BlueprintQuestObjectiveReference> obj = m_NextObjectivesProxy ?? ((ReferenceListProxy<BlueprintQuestObjective, BlueprintQuestObjectiveReference>)m_NextObjectives);
			ReferenceListProxy<BlueprintQuestObjective, BlueprintQuestObjectiveReference> result = obj;
			m_NextObjectivesProxy = obj;
			return result;
		}
	}

	public IList<BlueprintQuestObjective> Addendums
	{
		get
		{
			ReferenceListProxy<BlueprintQuestObjective, BlueprintQuestObjectiveReference> obj = m_AddendumsProxy ?? ((ReferenceListProxy<BlueprintQuestObjective, BlueprintQuestObjectiveReference>)m_Addendums);
			ReferenceListProxy<BlueprintQuestObjective, BlueprintQuestObjectiveReference> result = obj;
			m_AddendumsProxy = obj;
			return result;
		}
	}

	public bool IsFinishParent => m_FinishParent;

	public bool IsErrandObjective
	{
		get
		{
			if (!IsAddendum)
			{
				if (m_Quest == null || m_Quest.IsEmpty())
				{
					return false;
				}
				return Quest.Type == QuestType.Errand;
			}
			return false;
		}
	}

	public bool IsAddendum => m_Type != Type.Objective;

	public bool IsAutomaticallyStartingAddendum => m_Type == Type.AddendumStartingAutomatically;

	public bool IsHidden
	{
		get
		{
			return m_Hidden;
		}
		set
		{
			m_Hidden = value;
		}
	}

	public IList<BlueprintArea> Areas
	{
		get
		{
			ReferenceListProxy<BlueprintArea, BlueprintAreaReference> obj = m_AreasProxy ?? ((ReferenceListProxy<BlueprintArea, BlueprintAreaReference>)m_Areas);
			ReferenceListProxy<BlueprintArea, BlueprintAreaReference> result = obj;
			m_AreasProxy = obj;
			return result;
		}
	}

	public LocalizedString GetTitile()
	{
		if (!IsErrandObjective)
		{
			return Title;
		}
		return m_Quest.Get().Title;
	}

	public LocalizedString GetDescription()
	{
		if (!IsErrandObjective)
		{
			return Description;
		}
		return m_Quest.Get().Description;
	}

	public override string ToString()
	{
		return $"{base.ToString()} [{Quest}]";
	}

	public QuestObjectiveReferenceType GetUsagesFor(BlueprintQuestObjective questObj)
	{
		if (m_NextObjectives.HasItem((BlueprintQuestObjectiveReference r) => r.Is(questObj)))
		{
			return QuestObjectiveReferenceType.Give;
		}
		return QuestObjectiveReferenceType.None;
	}

	public QuestReferenceType GetUsagesFor(BlueprintQuest quest)
	{
		if (quest == Quest && IsFinishParent && !IsAddendum)
		{
			return QuestReferenceType.Complete;
		}
		return QuestReferenceType.None;
	}

	protected override System.Type GetFactType()
	{
		return typeof(QuestObjective);
	}

	protected override void ApplyValidation(ValidationContext context, int parentIndex)
	{
		base.ApplyValidation(context, parentIndex);
		if (m_Quest.IsEmpty())
		{
			context.AddError("Quest is missing");
		}
		for (int i = 0; i < m_Addendums.Count; i++)
		{
			BlueprintQuestObjectiveReference addendum = m_Addendums[i];
			if (addendum == null || addendum.IsEmpty())
			{
				context.AddError($"Addendum {i} is null!");
				context.AddFixup(delegate
				{
					m_Addendums.Remove(addendum);
				});
			}
		}
	}
}
