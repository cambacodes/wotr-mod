using System;
using System.Collections.Generic;
using System.Linq;
using JetBrains.Annotations;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints.Facts;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Blueprints.Quests.Logic.CrusadeQuests;
using Kingmaker.Blueprints.Root;
using Kingmaker.ElementsSystem;
using Kingmaker.Enums;
using Kingmaker.Localization;
using UnityEngine;

namespace Kingmaker.Blueprints.Quests;

[TypeId("eddc7c1e81adf5144acd394ebc24ca92")]
public class BlueprintQuest : BlueprintFact
{
	[NotNull]
	public LocalizedString Description;

	[NotNull]
	public LocalizedString Title;

	[NotNull]
	public LocalizedString CompletionText;

	[SerializeField]
	private QuestGroupId m_Group;

	[SerializeField]
	private int m_DescriptionPriority;

	[SerializeField]
	private QuestType m_Type;

	[SerializeField]
	private int m_LastChapter;

	[SerializeField]
	private QuestMarkerColors.QuestMarkerColorType m_QuestMarkerColorType;

	[SerializeField]
	[HideInInspector]
	private List<BlueprintQuestObjectiveReference> m_Objectives = new List<BlueprintQuestObjectiveReference>();

	public ActionList OnSetAutoKingdom;

	public QuestMarkerColors.QuestMarkerColorType QuestMarkerColorType => m_QuestMarkerColorType;

	public IEnumerable<BlueprintQuestObjective> AllObjectives => m_Objectives.Select((BlueprintQuestObjectiveReference o) => o.Get());

	public IEnumerable<BlueprintQuestObjective> Addendums
	{
		get
		{
			foreach (BlueprintQuestObjectiveReference objective in m_Objectives)
			{
				foreach (BlueprintQuestObjective addendum in objective.Get().Addendums)
				{
					yield return addendum;
				}
			}
		}
	}

	public IEnumerable<BlueprintQuestObjective> Objectives
	{
		get
		{
			foreach (BlueprintQuestObjectiveReference objective in m_Objectives)
			{
				if (objective != null)
				{
					BlueprintQuestObjective blueprintQuestObjective = objective.Get();
					if (blueprintQuestObjective != null && !blueprintQuestObjective.IsAddendum)
					{
						yield return objective.Get();
					}
				}
			}
		}
	}

	public QuestGroupId Group => m_Group;

	public int DescriptionPriority => m_DescriptionPriority;

	public QuestType Type => m_Type;

	public int LastChapter => m_LastChapter;

	public string GetDescription()
	{
		QuestDescriptionModifier component = this.GetComponent<QuestDescriptionModifier>();
		if (component == null)
		{
			return Description;
		}
		return component.Modify(Description);
	}

	protected override Type GetFactType()
	{
		return typeof(Quest);
	}
}
