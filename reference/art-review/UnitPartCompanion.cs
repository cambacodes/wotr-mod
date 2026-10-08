using System.Collections.Generic;
using System.Linq;
using JetBrains.Annotations;
using Kingmaker.Blueprints;
using Kingmaker.Controllers.Rest.State;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.PubSubSystem;
using Kingmaker.Utility;
using Kingmaker.View.Spawners;
using Newtonsoft.Json;

namespace Kingmaker.UnitLogic.Parts;

public class UnitPartCompanion : UnitPart, IUnitPartSurviveRespec, IAreaHandler, IGlobalSubscriber, ISubscriber, IInGameHandler
{
	[JsonProperty]
	private EntityRef m_Spawner;

	[JsonProperty]
	private bool m_HealOnExit;

	[JsonProperty]
	public bool IsIgnoreFixInGame;

	public readonly CountableFlag Pinned = new CountableFlag();

	public readonly CountableFlag IgnoresSpawners = new CountableFlag();

	public readonly CountableFlag IsPartyChecksDisabled = new CountableFlag();

	public readonly CountableFlag ShouldBeHidden = new CountableFlag();

	[JsonProperty]
	public CompanionState State { get; private set; }

	[JsonProperty]
	public CampingRoleType LastCampingRole { get; set; }

	[JsonProperty(DefaultValueHandling = DefaultValueHandling.Ignore)]
	public bool CanDismiss { get; private set; }

	public bool ShouldSurviveRespec => true;

	[JsonProperty]
	public bool IsEtudeBracketSetCompanionPosition { get; set; }

	public void SetState(CompanionState s)
	{
		if (base.Owner.IsReallyInFactPet)
		{
			PFLog.Default.Error($"Cannot set state for {base.Owner}, it's a pet");
			return;
		}
		State = s;
		UnitPartPetMaster unitPartPetMaster = base.Owner.Get<UnitPartPetMaster>();
		List<EntityPartRef<UnitEntityData, UnitPartPet>> list = unitPartPetMaster?.Pets;
		if (list != null)
		{
			foreach (EntityPartRef<UnitEntityData, UnitPartPet> item in list)
			{
				if (item.Entity != null && !unitPartPetMaster.IsExPet(item.Entity.UniqueId))
				{
					item.Entity.Ensure<UnitPartCompanion>().State = s;
				}
			}
		}
		m_HealOnExit = State == CompanionState.ExCompanion;
		base.Owner.Ensure<UnitPartNonStackBonuses>();
		Game.Instance.Player.InvalidateCharacterLists();
	}

	public void SyncStateWithPet([NotNull] UnitEntityData petUnit)
	{
		UnitPartPetMaster unitPartPetMaster = base.Owner.Get<UnitPartPetMaster>();
		if (unitPartPetMaster == null)
		{
			PFLog.Default.Error("SyncStateWithPet: Owner has no UnitPartPetMaster");
			return;
		}
		foreach (EntityPartRef<UnitEntityData, UnitPartPet> pet in unitPartPetMaster.Pets)
		{
			if (pet.Entity == petUnit && !unitPartPetMaster.IsExPet(petUnit.UniqueId))
			{
				pet.Entity.Ensure<UnitPartCompanion>().State = State;
				return;
			}
		}
		PFLog.Default.Error($"SyncStateWithPet: {base.Owner} has no pet {petUnit}");
	}

	public bool IsControllableInParty()
	{
		if (base.Owner.IsMainCharacter)
		{
			return true;
		}
		UnitEntityData master = base.Owner.Master;
		if ((object)master != null && master.IsMainCharacter)
		{
			return true;
		}
		if (State != CompanionState.InParty)
		{
			return false;
		}
		return !Game.Instance.LoadedAreaState.Settings.CapitalPartyMode;
	}

	public static UnitEntityData FindCompanion(BlueprintUnit bp, CompanionState state)
	{
		return Game.Instance.Player.AllCrossSceneUnits.FirstOrDefault(delegate(UnitEntityData u)
		{
			if (u.Blueprint == bp)
			{
				UnitPartCompanion unitPartCompanion = u.Get<UnitPartCompanion>();
				if (unitPartCompanion == null)
				{
					return false;
				}
				return unitPartCompanion.State == state;
			}
			return false;
		});
	}

	public void SetSpawner(CompanionSpawner spawner)
	{
		GetCurrentSpawner()?.StopControllingCompanion();
		m_Spawner = new EntityRef(spawner?.UniqueId);
	}

	public CompanionSpawner GetCurrentSpawner()
	{
		return m_Spawner.Entity?.View as CompanionSpawner;
	}

	public void CopyAfterRespec(UnitEntityData toUnit)
	{
		UnitPartCompanion unitPartCompanion = toUnit.Parts.Ensure<UnitPartCompanion>();
		unitPartCompanion.SetState(State);
		unitPartCompanion.m_Spawner = m_Spawner;
		base.Owner.IsInGame = State == CompanionState.InParty;
		if (CanDismiss)
		{
			unitPartCompanion.MarkDismissible();
		}
	}

	public void MarkDismissible()
	{
		CanDismiss = true;
	}

	public void OnAreaBeginUnloading()
	{
		if (m_HealOnExit && !base.Owner.State.IsDead)
		{
			RaiseDead.DoRise(base.Owner);
		}
		m_HealOnExit = false;
	}

	public void OnAreaDidLoad()
	{
	}

	public void HandleObjectInGameChanged(EntityDataBase entityData)
	{
		if (IsIgnoreFixInGame && base.Owner == entityData && base.Owner.IsInGame)
		{
			IsIgnoreFixInGame = false;
		}
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
