using System;
using System.Collections.Generic;
using System.Linq;
using JetBrains.Annotations;
using Kingmaker.Blueprints.Quests;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Persistence.JsonUtility;
using Kingmaker.View;
using Newtonsoft.Json;

namespace Kingmaker.AreaLogic.QuestSystem;

[JsonObject(MemberSerialization.OptIn)]
public class QuestBook : EntityDataBase
{
	public IEnumerable<Quest> Quests => from q in Facts.GetAll<Quest>()
		where q.State != QuestState.None && !q.IsReadOnly
		select q;

	public void GiveObjective(BlueprintQuestObjective bpObjective)
	{
		QuestObjective questObjective = EnsureObjective(bpObjective);
		if (questObjective.State != QuestObjectiveState.Started)
		{
			if (questObjective.State != QuestObjectiveState.None)
			{
				PFLog.Default.Warning("Quest objective has invalid state");
			}
			else
			{
				questObjective.Start();
			}
		}
	}

	public void CompleteObjective(BlueprintQuestObjective bpObjective)
	{
		QuestObjective questObjective = EnsureObjective(bpObjective);
		if (questObjective.State == QuestObjectiveState.None)
		{
			questObjective.Start();
		}
		if (questObjective.State != QuestObjectiveState.Started)
		{
			PFLog.Default.Warning("Quest objective has invalid state");
		}
		else
		{
			questObjective.Complete();
		}
	}

	public void FailObjective(BlueprintQuestObjective bpObjective)
	{
		QuestObjective questObjective = EnsureObjective(bpObjective);
		if (questObjective.State == QuestObjectiveState.None)
		{
			questObjective.Start();
		}
		if (questObjective.State != QuestObjectiveState.Started)
		{
			PFLog.Default.Warning("Quest objective has invalid state");
		}
		else
		{
			questObjective.Fail();
		}
	}

	public void ResetObjective(BlueprintQuestObjective bpObjective)
	{
		QuestObjective questObjective = EnsureObjective(bpObjective);
		if (questObjective.State != QuestObjectiveState.None)
		{
			questObjective.Reset();
		}
	}

	public void ResetQuest(BlueprintQuest bp, BlueprintQuestObjective start, IEnumerable<BlueprintQuestObjective> reset)
	{
		if ((bool)start)
		{
			GetQuest(bp)?.Uncomplete(start, reset);
		}
		else
		{
			GetQuest(bp)?.Remove();
		}
	}

	public void ForceResetQuest(BlueprintQuest bp)
	{
		GetQuest(bp)?.Remove();
	}

	[CanBeNull]
	private Quest GetQuest(BlueprintQuest quest)
	{
		foreach (EntityFact item in Facts.List)
		{
			if (item is Quest quest2 && quest2.Blueprint == quest)
			{
				return quest2;
			}
		}
		return null;
	}

	public void SetState(Quest quest)
	{
		if (GetQuest(quest.Blueprint) == null)
		{
			quest.Detach();
			quest.Attach(Facts);
		}
		else
		{
			PFLog.Default.Error("Cannot import quest as it was already started.");
		}
	}

	public QuestState GetQuestState(BlueprintQuest bpQuest)
	{
		return GetQuest(bpQuest)?.State ?? QuestState.None;
	}

	public QuestObjectiveState GetObjectiveState(BlueprintQuestObjective bpObjective)
	{
		Quest quest = GetQuest(bpObjective.Quest);
		if (quest == null)
		{
			return QuestObjectiveState.None;
		}
		return (quest.TryGetObjective(bpObjective) ?? throw new Exception("Can't find objective in quest")).State;
	}

	[CanBeNull]
	public QuestObjective GetObjective(BlueprintQuestObjective bpObjective)
	{
		Quest quest = GetQuest(bpObjective.Quest);
		if (quest == null)
		{
			return null;
		}
		QuestObjective questObjective = quest.TryGetObjective(bpObjective);
		if (questObjective == null)
		{
			PFLog.Default.Error("Objective not found");
		}
		return questObjective;
	}

	private QuestObjective EnsureObjective(BlueprintQuestObjective bpObjective)
	{
		Quest quest = GetQuest(bpObjective.Quest);
		if (quest == null)
		{
			quest = new Quest(bpObjective.Quest);
			Facts.Add(quest);
		}
		return quest.TryGetObjective(bpObjective) ?? throw new Exception("Can't find objective in quest");
	}

	protected override EntityViewBase CreateViewForData()
	{
		return null;
	}

	public QuestBook(JsonConstructorMark _)
		: base(_)
	{
	}

	public QuestBook()
		: base("quest_book", isInGame: true)
	{
	}
}
