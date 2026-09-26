using System.Collections.Generic;
using System.Linq;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.AreaLogic.SummonPool;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Area;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.EntitySystem.Persistence.JsonUtility;
using Kingmaker.PubSubSystem;
using Kingmaker.Utility;
using Kingmaker.View;
using Newtonsoft.Json;
using Owlcat.Runtime.Core.Utils;

namespace Kingmaker.AreaLogic.Etudes;

public class EtudesSystem : EntityDataBase, IUnlockHandler, IGlobalSubscriber, ISubscriber, IUnlockValueHandler, ICompanionChangeHandler, IPartyHandler, IAreaHandler, IQuestObjectiveHandler, ITimeOfDayChangedHandler, ISummonPoolHandler, IAreaPartHandler
{
	private enum EtudeState
	{
		Unknown,
		Started,
		Completed,
		PreStarted,
		PreCompleted
	}

	[JsonProperty]
	private readonly Dictionary<BlueprintEtude, EtudeState> m_EtudesData = new Dictionary<BlueprintEtude, EtudeState>();

	private readonly Dictionary<BlueprintEtudeConflictingGroup, BlueprintEtude> m_HeldConflictingGroups = new Dictionary<BlueprintEtudeConflictingGroup, BlueprintEtude>();

	private CountingGuard m_IsUpdateForUnload = new CountingGuard();

	private CountingGuard m_UpdateGuard = new CountingGuard();

	private BlueprintAreaPart m_AreaPartBeingLoaded;

	private BlueprintAreaPart m_AreaPartBeingExited;

	public readonly EtudeChangedEvent EtudeChangedEvent = new EtudeChangedEvent();

	public EtudesTree Etudes { get; private set; }

	public bool ConditionsDirty { get; private set; }

	public BlueprintAreaPart LoadEtudesForAreaPart
	{
		get
		{
			object obj;
			if (!m_IsUpdateForUnload)
			{
				obj = SimpleBlueprintExtendAsObject.Or(m_AreaPartBeingLoaded, null);
				if (obj == null)
				{
					return AreaService.Instance.CurrentAreaPart;
				}
			}
			else
			{
				obj = null;
			}
			return (BlueprintAreaPart)obj;
		}
	}

	public BlueprintAreaPart AreaPartBeingExited => m_AreaPartBeingExited;

	public bool EtudeIsNotStarted(BlueprintEtude etude)
	{
		return !m_EtudesData.ContainsKey(etude);
	}

	public bool EtudeIsStarted(BlueprintEtude etude)
	{
		if (m_EtudesData.ContainsKey(etude))
		{
			return !EtudeIsCompleted(etude);
		}
		return false;
	}

	public bool EtudeIsCompleted(BlueprintEtude etude)
	{
		if (etude == null || !m_EtudesData.TryGetValue(etude, out var value))
		{
			return false;
		}
		if (value != EtudeState.Completed)
		{
			return value == EtudeState.PreCompleted;
		}
		return true;
	}

	public bool EtudeIsPreCompleted(BlueprintEtude etude)
	{
		if (!m_EtudesData.TryGetValue(etude, out var value))
		{
			return false;
		}
		return value == EtudeState.PreCompleted;
	}

	private EtudeState GetSavedState(BlueprintEtude bp)
	{
		m_EtudesData.TryGetValue(bp, out var value);
		return value;
	}

	public EtudesSystem(JsonConstructorMark _)
		: base(_)
	{
	}

	public EtudesSystem()
		: base("D9C380301B9648EC93FD75988ACD9412", isInGame: true)
	{
		Etudes = Facts.EnsureFactProcessor<EtudesTree>();
	}

	public void MarkConditionsDirty()
	{
		ConditionsDirty = true;
	}

	public void ClearConditionsDirty()
	{
		ConditionsDirty = false;
	}

	protected override void OnPostLoad()
	{
		base.OnPostLoad();
		Etudes = Facts.EnsureFactProcessor<EtudesTree>();
		Etudes.RestoreTreeStructure();
	}

	protected override void OnApplyPostLoadFixes()
	{
		base.OnApplyPostLoadFixes();
		FixupActorChanges();
		Etudes.FixupEtudesTree(this);
		FixupCompletesParent();
	}

	public void OnAreaBeginUnloading()
	{
		if (!Game.Instance.IsUnloading)
		{
			using (m_IsUpdateForUnload.Scope())
			{
				UpdateEtudes();
			}
		}
	}

	public BlueprintEtude GetConflictingGroupTask(BlueprintEtudeConflictingGroup conflictingGroup)
	{
		if (!conflictingGroup)
		{
			return null;
		}
		return m_HeldConflictingGroups.Get(conflictingGroup);
	}

	public void RemoveConflictingGroupTask(BlueprintEtudeConflictingGroup conflictingGroup, Etude e)
	{
		if (GetConflictingGroupTask(conflictingGroup) == e.Blueprint)
		{
			SetConflictingGroupTask(conflictingGroup, null);
		}
	}

	public void SetConflictingGroupTask(BlueprintEtudeConflictingGroup conflictingGroup, Etude e)
	{
		if ((bool)conflictingGroup)
		{
			if (e != null)
			{
				m_HeldConflictingGroups[conflictingGroup] = e.Blueprint;
			}
			else
			{
				m_HeldConflictingGroups.Remove(conflictingGroup);
			}
		}
	}

	public void StartEtude(BlueprintEtude bp, bool startParent = false, bool force = false)
	{
		if (bp.IsReadOnly && !force)
		{
			PFLog.Default.Log($"Cannot start etude {bp} as it is read-only.");
			return;
		}
		switch (GetSavedState(bp))
		{
		case EtudeState.Started:
			PFLog.Etudes.Log(bp, $"Cannot start etude {bp}: already started");
			return;
		case EtudeState.Completed:
			PFLog.Etudes.Log(bp, $"Cannot start etude {bp}: already completed");
			return;
		}
		if (!bp.Parent.IsEmpty())
		{
			switch (GetSavedState(bp.Parent.Get()))
			{
			case EtudeState.Unknown:
			case EtudeState.PreStarted:
				if (bp.StartsParent || startParent)
				{
					StartEtude(bp.Parent, startParent, force);
					if (GetSavedState(bp) == EtudeState.Started)
					{
						return;
					}
				}
				if (GetSavedState(bp.Parent) != EtudeState.Started)
				{
					m_EtudesData[bp] = EtudeState.PreStarted;
					GameHistoryLog.Instance.EtudeEvent(null, "Etude[" + bp.NameSafe() + "]:PreStarted");
					PFLog.Etudes.Log(bp, $"Starting etude {bp}: parent not started, marking prestart");
					return;
				}
				break;
			case EtudeState.Completed:
			case EtudeState.PreCompleted:
				PFLog.Etudes.Log(bp, $"Cannot start etude {bp}: parent already completed");
				return;
			}
		}
		using PooledHashSet<BlueprintEtude> starting = PooledHashSet<BlueprintEtude>.Get();
		StartEtudeInternal(bp, starting);
	}

	private void StartEtudeInternal(BlueprintEtude bp, PooledHashSet<BlueprintEtude> starting)
	{
		EtudeState savedState = GetSavedState(bp);
		if (savedState == EtudeState.Completed)
		{
			return;
		}
		if (!starting.Add(bp))
		{
			PFLog.Etudes.Error("Starting etude " + bp.name + ": loop in StartsWith detected.");
			return;
		}
		PFLog.Etudes.Log("Starting etude: " + bp.name);
		if (Etudes.GetFact(bp) != null)
		{
			PFLog.Etudes.Error(bp, $"Cannot start etude {bp}: already started");
			return;
		}
		Etude etude = (bp.Parent.IsEmpty() ? null : Etudes.GetFact(bp.Parent.Get()));
		if (etude != null && etude.CompletionInProgress)
		{
			PFLog.Etudes.Log(bp, $"Cannot start etude {bp}: parent is CompletionInProgress");
			return;
		}
		Facts.Add(new Etude(bp, etude));
		if (savedState == EtudeState.PreCompleted)
		{
			MarkEtudeCompleted(bp);
			return;
		}
		m_EtudesData[bp] = EtudeState.Started;
		GameHistoryLog.Instance.EtudeEvent(null, "Etude[" + bp.NameSafe() + "]:State.Started");
		foreach (BlueprintEtudeReference item in bp.StartsWith)
		{
			if (!item.IsEmpty())
			{
				StartEtudeInternal(item.Get(), starting);
			}
		}
		foreach (KeyValuePair<BlueprintEtude, EtudeState> item2 in m_EtudesData.Where((KeyValuePair<BlueprintEtude, EtudeState> p) => p.Key.Parent.Is(bp) && p.Value == EtudeState.PreStarted).ToTempList())
		{
			StartEtudeInternal(item2.Key, starting);
		}
		MarkConditionsDirty();
	}

	public void MarkEtudeCompleted(BlueprintEtude bp, bool ignoreParent = false, bool force = true)
	{
		PFLog.Etudes.Log("Completing etude: " + bp.name);
		Etude fact = Etudes.GetFact(bp);
		m_EtudesData[bp] = ((fact == null) ? EtudeState.PreCompleted : EtudeState.Completed);
		if (!ignoreParent && bp.CompletesParent && !bp.Parent.IsEmpty())
		{
			MarkEtudeCompleted(bp.Parent.Get(), ignoreParent: false, force);
			return;
		}
		if (fact != null)
		{
			fact.MarkCompleted(force);
		}
		else
		{
			GameHistoryLog.Instance.EtudeEvent(null, "Etude[" + bp.NameSafe() + "]:PreCompleted");
		}
		MarkConditionsDirty();
	}

	public void InternalMarkCompleted(BlueprintEtude bp)
	{
		m_EtudesData[bp] = EtudeState.Completed;
	}

	public void ForceUpdateEtudes(BlueprintAreaPart areaPartBeingLoaded)
	{
		m_AreaPartBeingLoaded = areaPartBeingLoaded;
		UpdateEtudes();
		m_AreaPartBeingLoaded = null;
	}

	public void UpdateEtudes()
	{
		if ((bool)m_UpdateGuard)
		{
			PFLog.Etudes.Log("Updating etude system skipped: already underway");
			return;
		}
		using (ProfileScope.New("UpdateEtudes"))
		{
			using (m_UpdateGuard.Scope())
			{
				PFLog.Etudes.Log("Updating etude system");
				ClearConditionsDirty();
				List<BlueprintAreaMechanics> mechanicsSet = (m_AreaPartBeingLoaded ? null : GetActiveAdditionalMechanics(Game.Instance.CurrentlyLoadedArea).ToTempList());
				using (ProfileScope.New("MaybeDeactivateCompletedEtudes"))
				{
					Etudes.MaybeDeactivateCompletedEtudes();
				}
				using (ProfileScope.New("SelectPlayingEtudes"))
				{
					Etudes.SelectPlayingEtudes();
				}
				if (m_AreaPartBeingLoaded != null)
				{
					return;
				}
				if (GetActiveAdditionalMechanics(Game.Instance.CurrentlyLoadedArea).Any((BlueprintAreaMechanics m) => !mechanicsSet.Contains(m)))
				{
					PFLog.Etudes.Log("Etude system causing mechanics reload");
					Game.Instance.ReloadAreaMechanic(clearFx: false);
					LoadingProcess.Instance.StartLoadingProcess(delegate
					{
						EventBus.RaiseEvent(delegate(IEtudesUpdateHandler h)
						{
							h.OnEtudesUpdate();
						});
					});
				}
				else
				{
					EventBus.RaiseEvent(delegate(IEtudesUpdateHandler h)
					{
						h.OnEtudesUpdate();
					});
				}
			}
		}
	}

	public void FixupActorChanges()
	{
		foreach (KeyValuePair<BlueprintEtudeConflictingGroup, BlueprintEtude> item in m_HeldConflictingGroups.ToTempList())
		{
			if (!item.Value.ConflictingGroups.HasReference(item.Key))
			{
				SetConflictingGroupTask(item.Key, null);
				PFLog.Etudes.Log($"Fixed conflicting group {item.Key}: no longer held by {item.Value}");
			}
		}
		foreach (Etude rawFact in Etudes.RawFacts)
		{
			if (!rawFact.IsPlaying)
			{
				continue;
			}
			foreach (BlueprintEtudeConflictingGroupReference conflictingGroup in rawFact.Blueprint.ConflictingGroups)
			{
				BlueprintEtudeConflictingGroup blueprintEtudeConflictingGroup = conflictingGroup.Get();
				if (blueprintEtudeConflictingGroup == null)
				{
					continue;
				}
				BlueprintEtude conflictingGroupTask = GetConflictingGroupTask(blueprintEtudeConflictingGroup);
				if (conflictingGroupTask == rawFact.Blueprint)
				{
					continue;
				}
				if (conflictingGroupTask == null || conflictingGroupTask.Priority < rawFact.Blueprint.Priority)
				{
					PFLog.Etudes.Log($"Fixed conflicting group {blueprintEtudeConflictingGroup}: should be held by {rawFact} (@{rawFact.Blueprint.Priority}), was {conflictingGroupTask}");
					if (conflictingGroupTask != null)
					{
						Etudes.ScheduleForceStop(conflictingGroupTask);
					}
					SetConflictingGroupTask(blueprintEtudeConflictingGroup, rawFact);
				}
				else
				{
					PFLog.Etudes.Log($"Fixed conflicting group {blueprintEtudeConflictingGroup}: etude {rawFact.Blueprint} cannot play as {conflictingGroupTask} has higher priority");
					Etudes.ScheduleForceStop(rawFact.Blueprint);
				}
			}
		}
	}

	private void FixupCompletesParent()
	{
		foreach (KeyValuePair<BlueprintEtude, EtudeState> item in m_EtudesData.ToTempList())
		{
			if (item.Value == EtudeState.Completed && item.Key.CompletesParent)
			{
				Etude fact = Etudes.GetFact(item.Key.Parent.Get());
				if (fact != null && !fact.CompletionInProgress)
				{
					MarkEtudeCompleted(fact.Blueprint);
				}
			}
		}
	}

	protected override EntityViewBase CreateViewForData()
	{
		return null;
	}

	public void HandleUnlock(BlueprintUnlockableFlag flag)
	{
		MarkConditionsDirty();
	}

	public void HandleLock(BlueprintUnlockableFlag flag)
	{
		MarkConditionsDirty();
	}

	public void HandleFlagValue(BlueprintUnlockableFlag flag, int value)
	{
		MarkConditionsDirty();
	}

	public void HandleRecruit(UnitEntityData companion)
	{
		MarkConditionsDirty();
	}

	public void HandleUnrecruit(UnitEntityData companion)
	{
		MarkConditionsDirty();
	}

	public void HandleAddCompanion(UnitEntityData unit)
	{
		MarkConditionsDirty();
	}

	public void HandleCompanionActivated(UnitEntityData unit)
	{
		MarkConditionsDirty();
	}

	public void HandleCompanionRemoved(UnitEntityData unit, bool stayInGame)
	{
		MarkConditionsDirty();
	}

	public void HandleCapitalModeChanged()
	{
	}

	public string GetDebugInfo(BlueprintEtude bp)
	{
		Etude fact = Etudes.GetFact(bp);
		EtudeState savedState = GetSavedState(bp);
		return $"[{bp.name}] is {savedState}: IsStarted={fact?.IsAttached} IsPlaying={fact?.IsPlaying} Completion={fact?.CompletionInProgress}";
	}

	public IEnumerable<BlueprintAreaMechanics> GetActiveAdditionalMechanics(BlueprintArea area)
	{
		using (ProfileScope.New("GetActiveAdditionalMechanics"))
		{
			foreach (Etude rawFact in Etudes.RawFacts)
			{
				if (!rawFact.IsPlaying)
				{
					continue;
				}
				foreach (BlueprintAreaMechanicsReference addedAreaMechanic in rawFact.Blueprint.AddedAreaMechanics)
				{
					if (!addedAreaMechanic.IsEmpty() && addedAreaMechanic.Get().Area.Is(area))
					{
						yield return addedAreaMechanic.Get();
					}
				}
			}
		}
	}

	private IEnumerable<BlueprintEtude> GetEtudesByState(EtudeState state)
	{
		return from x in m_EtudesData
			where x.Value == state
			select x.Key;
	}

	public IEnumerable<BlueprintEtude> GetStartedEtudes()
	{
		return GetEtudesByState(EtudeState.Started);
	}

	public IEnumerable<BlueprintEtude> GetCompletedEtudes()
	{
		return GetEtudesByState(EtudeState.Completed);
	}

	public void OnAreaDidLoad()
	{
	}

	public void HandleQuestObjectiveStarted(QuestObjective objective)
	{
		MarkConditionsDirty();
	}

	public void HandleQuestObjectiveBecameVisible(QuestObjective objective)
	{
		MarkConditionsDirty();
	}

	public void HandleQuestObjectiveCompleted(QuestObjective objective)
	{
		MarkConditionsDirty();
	}

	public void HandleQuestObjectiveFailed(QuestObjective objective)
	{
		MarkConditionsDirty();
	}

	public void OnTimeOfDayChanged()
	{
		MarkConditionsDirty();
	}

	public void HandleUnitAdded(ISummonPool pool, UnitEntityData unit)
	{
	}

	public void HandleUnitRemoved(ISummonPool pool, UnitEntityData unit)
	{
	}

	public void HandleLastUnitRemoved(ISummonPool pool, UnitEntityData unit)
	{
		MarkConditionsDirty();
	}

	public void OnAreaPartChanged(BlueprintAreaPart previous)
	{
		m_AreaPartBeingExited = SimpleBlueprintExtendAsObject.Or(previous, Game.Instance.CurrentlyLoadedArea);
		UpdateEtudes();
		m_AreaPartBeingExited = null;
	}

	public void OnEtudeStateChanged(Etude etude)
	{
		EtudeChangedEvent.Raise(etude);
	}

	public void UnstartEtude(BlueprintEtude bp, bool markPreStarted = false)
	{
		if (bp.IsReadOnly)
		{
			PFLog.Default.Log($"Cannot unstart etude {this} as it is read-only.");
			return;
		}
		Etude fact = Etudes.GetFact(bp);
		if (fact == null)
		{
			m_EtudesData.Remove(bp);
		}
		else
		{
			foreach (Etude item in fact.Children.ToTempList())
			{
				UnstartEtude(item.Blueprint, markPreStarted: true);
			}
		}
		foreach (KeyValuePair<BlueprintEtude, EtudeState> item2 in m_EtudesData.Where((KeyValuePair<BlueprintEtude, EtudeState> p) => p.Value == EtudeState.Completed).ToTempList())
		{
			if (IsDescendant(bp, item2.Key))
			{
				m_EtudesData[item2.Key] = EtudeState.PreCompleted;
			}
		}
		if (fact != null)
		{
			Etudes.RemoveFact(fact);
			m_EtudesData.Remove(bp);
		}
		if (markPreStarted)
		{
			m_EtudesData[bp] = EtudeState.PreStarted;
		}
		static bool IsDescendant(BlueprintEtude a, BlueprintEtude b)
		{
			if (!b.Parent.Is(a))
			{
				if (!b.Parent.IsEmpty())
				{
					return IsDescendant(a, b.Parent);
				}
				return false;
			}
			return true;
		}
	}

	public void SetState(EtudesSystem etudesSystem, IEnumerable<BlueprintEtude> importEtudes, IEnumerable<BlueprintEtude> skipEtudes)
	{
		foreach (BlueprintEtude importEtude in importEtudes)
		{
			Etude etude = etudesSystem.Facts.Get<Etude>(importEtude);
			SetStateSoftRecurcively(etude, etudesSystem, skipEtudes);
		}
		OnPostLoad();
		UpdateEtudes();
	}

	private void SetStateSoftRecurcively(Etude etude, EtudesSystem etudesSystem, IEnumerable<BlueprintEtude> skipEtudes)
	{
		if (etude == null || (skipEtudes != null && skipEtudes.Contains(etude.Blueprint)) || !etudesSystem.m_EtudesData.TryGetValue(etude.Blueprint, out var value))
		{
			return;
		}
		switch (value)
		{
		case EtudeState.Started:
			if (GetSavedState(etude.Blueprint) == EtudeState.Unknown)
			{
				StartEtude(etude.Blueprint, startParent: true, force: true);
			}
			break;
		case EtudeState.Completed:
			if (GetSavedState(etude.Blueprint) == EtudeState.Unknown)
			{
				StartEtude(etude.Blueprint, startParent: true, force: true);
				etude.MarkCompleted(force: true);
				etude.FinishCompletion();
			}
			break;
		}
		if (etude.Children == null)
		{
			return;
		}
		foreach (Etude item in etude.Children.ToList())
		{
			SetStateSoftRecurcively(item, etudesSystem, skipEtudes);
		}
	}
}
