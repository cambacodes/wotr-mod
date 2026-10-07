using System.Collections.Generic;
using System.Linq;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.EntitySystem;
using Kingmaker.Utility;
using Owlcat.Runtime.Core.Utils;

namespace Kingmaker.AreaLogic.Etudes;

public class EtudesTree : EntityFactsProcessor<Etude>
{
	private readonly List<Etude> m_Roots = new List<Etude>();

	private readonly HashSet<Etude> m_StoppingSet = new HashSet<Etude>();

	private readonly HashSet<Etude> m_StartingSet = new HashSet<Etude>();

	private bool m_NeedCleanupCompleted;

	private readonly HashSet<Etude> m_ForceStopOnUpdate = new HashSet<Etude>();

	public IReadOnlyList<Etude> Roots => m_Roots;

	private EtudesSystem EtudesSystem => (EtudesSystem)base.Manager.Owner;

	protected override Etude PrepareFactForAttach(Etude fact)
	{
		fact.SuppressActivationOnAttach = true;
		return fact;
	}

	protected override Etude PrepareFactForDetach(Etude fact)
	{
		return fact;
	}

	protected override void OnFactDidAttach(Etude fact)
	{
		LinkEtudeToTree(fact);
	}

	private void LinkEtudeToTree(Etude fact)
	{
		List<Etude> list = fact.Parent?.Children ?? m_Roots;
		if (!list.Contains(fact))
		{
			list.Add(fact);
		}
	}

	protected override void OnFactWillDetach(Etude fact)
	{
		foreach (Etude item in fact.Children.ToTempList())
		{
			RemoveFact(item);
		}
		(fact.Parent?.Children ?? m_Roots).Remove(fact);
	}

	public void RestoreTreeStructure()
	{
		foreach (Etude rawFact in base.RawFacts)
		{
			LinkEtudeToTree(rawFact);
		}
	}

	public void FixupEtudesTree(EtudesSystem system)
	{
		foreach (Etude item in base.RawFacts.Where((Etude e) => !e.Blueprint.Parent.Is(e.Parent?.Blueprint)).ToTempList())
		{
			FixupEtudeParents(system, item);
		}
		List<BlueprintEtude> list = TempList.Get<BlueprintEtude>();
		foreach (Etude root in m_Roots)
		{
			FixupEtudeStartsWith(system, root, list);
		}
		foreach (BlueprintEtude item2 in list)
		{
			if (system.EtudeIsNotStarted(item2))
			{
				system.StartEtude(item2);
			}
		}
	}

	private void FixupEtudeParents(EtudesSystem system, Etude etude)
	{
		BlueprintEtude blueprintEtude = etude.Blueprint.Parent.Get();
		Etude etude2;
		if ((bool)blueprintEtude)
		{
			etude2 = GetFact(blueprintEtude);
			if (etude2 == null)
			{
				system.StartEtude(blueprintEtude, startParent: true);
				etude2 = GetFact(blueprintEtude);
				if (etude2 == null)
				{
					PFLog.Etudes.Warning($"Etude {etude} cannot change parent to {blueprintEtude.NameSafe()}. Completing instead");
					system.MarkEtudeCompleted(etude.Blueprint, ignoreParent: true);
					return;
				}
			}
		}
		else
		{
			etude2 = null;
		}
		PFLog.Etudes.Log($"Etude {etude} changed parent from {(etude.Parent?.Blueprint).NameSafe()} to {blueprintEtude.NameSafe()}.");
		etude.Parent?.Children.Remove(etude);
		etude2?.Children.Add(etude);
		etude.ChangeParent(etude2);
		if (etude2 == null)
		{
			m_Roots.Add(etude);
		}
	}

	private void FixupEtudeStartsWith(EtudesSystem system, Etude etude, List<BlueprintEtude> toStart)
	{
		foreach (BlueprintEtudeReference item in etude.Blueprint.StartsWith)
		{
			BlueprintEtude blueprint = item.Get();
			if (blueprint != null && !system.EtudeIsCompleted(blueprint) && !base.RawFacts.HasItem((Etude x) => x.Blueprint == blueprint))
			{
				toStart.Add(blueprint);
			}
		}
		foreach (Etude child in etude.Children)
		{
			FixupEtudeStartsWith(system, child, toStart);
		}
	}

	public void MaybeDeactivateCompletedEtudes()
	{
		m_NeedCleanupCompleted = false;
		foreach (Etude root in m_Roots)
		{
			MaybeDeactivateCompleted(root);
		}
		if (!m_NeedCleanupCompleted)
		{
			return;
		}
		foreach (Etude item in base.RawFacts.ToTempList())
		{
			if (item.IsCompleted)
			{
				RemoveFact(item);
				EtudesSystem.InternalMarkCompleted(item.Blueprint);
			}
		}
	}

	private void MaybeDeactivateCompleted(Etude etude)
	{
		if (etude.IsCompleted)
		{
			return;
		}
		bool flag = etude.CompletionInProgress;
		List<Etude> list = ListPool<Etude>.Claim();
		list.AddRange(etude.Children);
		foreach (Etude item in list)
		{
			MaybeDeactivateCompleted(item);
			flag = item.IsCompleted && flag;
		}
		ListPool<Etude>.Release(list);
		bool flag2 = !etude.IsPlaying || etude.Blueprint.CompletionCondition.Check();
		if (!(flag && flag2))
		{
			return;
		}
		etude.CallComponents(delegate(IEtudeCompleteTrigger t)
		{
			t.OnComplete();
		});
		if (etude.IsActive)
		{
			etude.Deactivate();
		}
		etude.FinishCompletion();
		m_NeedCleanupCompleted = true;
		if (etude.Parent != null && etude.Parent.CompletionInProgress)
		{
			return;
		}
		PFLog.Etudes.Log("Finally completed etude: " + etude.Blueprint.name);
		foreach (BlueprintEtudeReference item2 in etude.Blueprint.StartsOnComplete)
		{
			if (!item2.IsEmpty())
			{
				EtudesSystem.StartEtude(item2.Get());
			}
		}
	}

	public void SelectPlayingEtudes()
	{
		m_StoppingSet.Clear();
		m_StoppingSet.UnionWith(m_ForceStopOnUpdate);
		m_ForceStopOnUpdate.Clear();
		m_StartingSet.Clear();
		foreach (Etude root in m_Roots)
		{
			ProcessEtudeActivation(root);
		}
		m_StartingSet.RemoveWhere((Etude e) => !IsPlayingOrStarting(e.Parent));
		if (FilterOnActors())
		{
			m_StartingSet.RemoveWhere((Etude e) => !IsPlayingOrStarting(e.Parent));
		}
		if (FilterOnSynchronization())
		{
			m_StartingSet.RemoveWhere((Etude e) => !IsPlayingOrStarting(e.Parent));
		}
		foreach (Etude item in m_StoppingSet)
		{
			Stop(item);
		}
		foreach (Etude item2 in m_StartingSet)
		{
			item2.Activate();
		}
	}

	private bool IsPlayingOrStarting(Etude etude)
	{
		while (etude != null)
		{
			if ((!etude.IsPlaying && !m_StartingSet.Contains(etude)) || m_StoppingSet.Contains(etude))
			{
				return false;
			}
			etude = etude.Parent;
		}
		return true;
	}

	private void ProcessEtudeActivation(Etude etude)
	{
		if (etude.IsCompleted)
		{
			return;
		}
		bool flag = EtudeCanPlay(etude);
		if (etude.IsPlaying)
		{
			if (!flag)
			{
				m_StoppingSet.Add(etude);
			}
		}
		else if (flag)
		{
			m_StartingSet.Add(etude);
		}
		if (!flag)
		{
			return;
		}
		foreach (Etude child in etude.Children)
		{
			ProcessEtudeActivation(child);
		}
	}

	private bool FilterOnActors()
	{
		bool result = false;
		List<Etude> list = (from e in m_StartingSet
			where e.Blueprint.HasActors
			orderby e.Blueprint.Priority descending
			select e).ToTempList();
		for (int num = 0; num < list.Count; num++)
		{
			Etude etude = list[num];
			if ((etude.Parent != null && !IsPlayingOrStarting(etude.Parent)) || CheckBlockConflicts(etude, list, num))
			{
				m_StartingSet.Remove(etude);
				result = true;
			}
			else
			{
				BreakConflictingEtude(etude);
			}
		}
		return result;
	}

	private bool CheckBlockConflicts(Etude etude, List<Etude> startingByPrio, int index)
	{
		foreach (BlueprintEtudeConflictingGroupReference actorReference in etude.Blueprint.ConflictingGroups)
		{
			if (actorReference.IsEmpty())
			{
				continue;
			}
			BlueprintEtude task = Game.Instance.Player.EtudesSystem.GetConflictingGroupTask(actorReference.Get());
			if (!task || task.Priority < etude.Blueprint.Priority || m_StoppingSet.Any((Etude t) => IsSameOrParentOf(t.Blueprint, task)))
			{
				for (int num = 0; num < index; num++)
				{
					Etude etude2 = startingByPrio[num];
					if (m_StartingSet.Contains(etude2) && etude2.Blueprint.ConflictingGroups.Any((BlueprintEtudeConflictingGroupReference r) => r.Guid == actorReference.Guid))
					{
						task = startingByPrio[num].Blueprint;
						break;
					}
				}
			}
			if ((bool)task && task.Priority >= etude.Blueprint.Priority)
			{
				return true;
			}
		}
		return false;
	}

	private void BreakConflictingEtude(Etude etude)
	{
		foreach (BlueprintEtudeConflictingGroupReference conflictingGroup in etude.Blueprint.ConflictingGroups)
		{
			if (!conflictingGroup.IsEmpty())
			{
				BlueprintEtude conflictingGroupTask = Game.Instance.Player.EtudesSystem.GetConflictingGroupTask(conflictingGroup.Get());
				if ((bool)conflictingGroupTask)
				{
					PFLog.Etudes.Log("Etude " + conflictingGroupTask.name + " interrupted: conflict with " + etude.Blueprint.name + " on " + conflictingGroup.Get().name);
					m_StoppingSet.Add(GetFact(conflictingGroupTask));
				}
			}
		}
	}

	private void RemoveChildTreeFromStarting(Etude parent)
	{
		foreach (Etude child in parent.Children)
		{
			m_StartingSet.Remove(child);
			RemoveChildTreeFromStarting(child);
		}
	}

	private bool FilterOnSynchronization()
	{
		bool result = false;
		foreach (Etude rawFact in base.RawFacts)
		{
			if (!rawFact.Blueprint.IsSynchronized || !IsPlayingOrStarting(rawFact) || rawFact.Blueprint.HasActors)
			{
				continue;
			}
			foreach (BlueprintEtudeReference item in rawFact.Blueprint.Synchronized)
			{
				if (item.IsEmpty() || item.Get().IsSynchronized)
				{
					continue;
				}
				Etude fact = GetFact(item.Get());
				if (fact == null || !IsPlayingOrStarting(fact))
				{
					if (rawFact.IsPlaying)
					{
						PFLog.Etudes.Log($"Stopping etude {rawFact.Blueprint} because sync etude {item.Get()} is not playing");
						m_StoppingSet.Add(rawFact);
					}
					else
					{
						m_StartingSet.Remove(rawFact);
					}
					result = true;
				}
			}
		}
		return result;
	}

	private bool IsSameOrParentOf(BlueprintEtude e1, BlueprintEtude e2)
	{
		if (e1 != e2)
		{
			if (!e1.Parent.IsEmpty())
			{
				return IsSameOrParentOf(e1.Parent.Get(), e2);
			}
			return false;
		}
		return true;
	}

	private bool EtudeCanPlay(Etude etude)
	{
		if ((!etude.Blueprint.HasLinkedAreaPart || etude.Blueprint.IsLinkedAreaPart(EtudesSystem.LoadEtudesForAreaPart)) && etude.IsLinkedCampaign(Game.Instance.Player.Campaign))
		{
			return etude.Blueprint.ActivationCondition.Check();
		}
		return false;
	}

	private void Stop(Etude etude)
	{
		if (etude.Blueprint.IsReadOnly)
		{
			PFLog.Default.Log($"Cannot stop etude {etude} as it is read-only.");
			return;
		}
		foreach (Etude child in etude.Children)
		{
			Stop(child);
		}
		if (etude.IsPlaying)
		{
			etude.Deactivate();
		}
	}

	public void AddToPlaying(Etude etude)
	{
		foreach (BlueprintEtudeConflictingGroupReference conflictingGroup in etude.Blueprint.ConflictingGroups)
		{
			((EtudesSystem)base.Manager.Owner).SetConflictingGroupTask(conflictingGroup.Get(), etude);
		}
	}

	public void RemoveFromPlaying(Etude etude)
	{
		foreach (BlueprintEtudeConflictingGroupReference conflictingGroup in etude.Blueprint.ConflictingGroups)
		{
			((EtudesSystem)base.Manager.Owner).RemoveConflictingGroupTask(conflictingGroup.Get(), etude);
		}
	}

	public void ScheduleForceStop(BlueprintEtude holder)
	{
		Etude fact = GetFact(holder);
		if (fact != null)
		{
			m_ForceStopOnUpdate.Add(fact);
		}
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
