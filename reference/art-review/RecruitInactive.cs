using System.Collections;
using System.Collections.Generic;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Designers.EventConditionActionSystem.ContextData;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence.Versioning;
using Kingmaker.PubSubSystem;
using Kingmaker.Settings;
using Kingmaker.UnitLogic.Parts;
using Kingmaker.Utility;
using Owlcat.QA.Validation;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.Designers.EventConditionActionSystem.Actions;

[AllowMultipleComponents]
[PlayerUpgraderAllowed(false)]
[TypeId("857993ffeba11124699997a531336700")]
public class RecruitInactive : GameAction
{
	private struct Companion
	{
		public BlueprintUnit CompanionBlueprint;

		public ActionList OnRecruit;
	}

	private static bool s_IsRunCoroutine = false;

	private static Coroutine s_Coroutine = null;

	private static Queue<Companion> s_OnRecruit = new Queue<Companion>();

	[ValidateNotNull]
	[SerializeField]
	[FormerlySerializedAs("CompanionBlueprint")]
	private BlueprintUnitReference m_CompanionBlueprint;

	public ActionList OnRecruit;

	public bool AvailableDelay;

	public BlueprintUnit CompanionBlueprint => m_CompanionBlueprint?.Get();

	public override void RunAction()
	{
		if (AvailableDelay)
		{
			s_OnRecruit.Enqueue(new Companion
			{
				CompanionBlueprint = CompanionBlueprint,
				OnRecruit = OnRecruit
			});
			if (!s_IsRunCoroutine)
			{
				s_IsRunCoroutine = true;
				s_Coroutine = CoroutineRunner.Start(DelayRecruit());
			}
		}
		else
		{
			UnitEntityData unitEntityData = Spawn(CompanionBlueprint);
			if (unitEntityData != null)
			{
				AfterSpawn(unitEntityData, OnRecruit);
			}
		}
	}

	private IEnumerator DelayRecruit()
	{
		yield return new WaitForEndOfFrame();
		while (s_OnRecruit.Count > 0)
		{
			Companion recruit = s_OnRecruit.Dequeue();
			UnitEntityData companion = Spawn(recruit.CompanionBlueprint);
			yield return new WaitForEndOfFrame();
			if (companion != null)
			{
				AfterSpawn(companion, recruit.OnRecruit);
				yield return new WaitForEndOfFrame();
			}
		}
		s_IsRunCoroutine = false;
	}

	private UnitEntityData Spawn(BlueprintUnit companionBlueprint)
	{
		UnitEntityData unitEntityData = Game.Instance.Player.AllCharacters.FirstOrDefault((UnitEntityData c) => c.Blueprint == companionBlueprint);
		if (unitEntityData != null && unitEntityData.Get<UnitPartCompanion>() != null && unitEntityData.Get<UnitPartCompanion>().State != CompanionState.ExCompanion)
		{
			PFLog.Default.Error(this, "Attempted to double-recruit " + companionBlueprint?.ToString() + " in " + this);
			return null;
		}
		UnitEntityData unitEntityData2 = (((object)unitEntityData != null && unitEntityData.Get<UnitPartCompanion>()?.State == CompanionState.ExCompanion) ? unitEntityData : null);
		if (unitEntityData2 == null)
		{
			unitEntityData2 = Game.Instance.EntityCreator.SpawnUnit(companionBlueprint, Vector3.zero, Quaternion.identity, Game.Instance.Player.CrossSceneState);
			unitEntityData2.Ensure<UnitPartCompanion>().SetState(CompanionState.Remote);
			unitEntityData2.IsInGame = false;
			if (!SettingsRoot.Difficulty.OnlyActiveCompanionsReceiveExperience)
			{
				int experience = Game.Instance.Player.MainCharacter.Value.Descriptor.Progression.Experience;
				unitEntityData2.Descriptor.Progression.AdvanceExperienceTo(experience, log: false);
			}
		}
		else
		{
			unitEntityData2.Ensure<UnitPartCompanion>().SetState(CompanionState.Remote);
		}
		return unitEntityData2;
	}

	private void AfterSpawn(UnitEntityData companion, ActionList onRecruit)
	{
		EventBus.RaiseEvent(delegate(IPartyHandler h)
		{
			h.HandleAddCompanion(companion);
		});
		EventBus.RaiseEvent(delegate(IPartyHandler h)
		{
			h.HandleCompanionRemoved(companion, Game.Instance.Player.CapitalPartyMode);
		});
		using (ContextData<RecruitedUnitData>.Request().Setup(companion))
		{
			onRecruit.Run();
		}
		EventBus.RaiseEvent(delegate(ICompanionChangeHandler h)
		{
			h.HandleRecruit(companion);
		});
	}

	public override string GetCaption()
	{
		return $"Recruit ({CompanionBlueprint}) to capital";
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
