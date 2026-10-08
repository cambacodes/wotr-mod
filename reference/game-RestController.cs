using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using JetBrains.Annotations;
using Kingmaker.AreaLogic.Cutscenes;
using Kingmaker.BarkBanters;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Items.Armors;
using Kingmaker.Blueprints.Items.Equipment;
using Kingmaker.Blueprints.Root;
using Kingmaker.Cheats;
using Kingmaker.Controllers.Rest.Cooking;
using Kingmaker.Controllers.Rest.State;
using Kingmaker.Controllers.Units;
using Kingmaker.Craft;
using Kingmaker.Designers.EventConditionActionSystem.NamedParameters;
using Kingmaker.DialogSystem.State;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.EntitySystem.Stats;
using Kingmaker.GameModes;
using Kingmaker.Items;
using Kingmaker.Items.Slots;
using Kingmaker.PubSubSystem;
using Kingmaker.RandomEncounters;
using Kingmaker.RandomEncounters.Settings;
using Kingmaker.ResourceLinks;
using Kingmaker.RuleSystem;
using Kingmaker.RuleSystem.Rules;
using Kingmaker.RuleSystem.Rules.Damage;
using Kingmaker.UI;
using Kingmaker.UI.Common;
using Kingmaker.UnitLogic;
using Kingmaker.UnitLogic.Buffs;
using Kingmaker.UnitLogic.Buffs.Blueprints;
using Kingmaker.UnitLogic.Buffs.Components;
using Kingmaker.UnitLogic.Mechanics.Components;
using Kingmaker.UnitLogic.Parts;
using Kingmaker.Utility;
using Kingmaker.View.MapObjects;
using Kingmaker.Visual.Particles;
using UnityEngine;

namespace Kingmaker.Controllers.Rest;

public class RestController : IController, IControllerStop
{
	private static readonly string UnitCutsceneName = "Unit";

	public static readonly TimeSpan DefaultBuffsSkipTime = 1.Hours();

	[NotNull]
	private readonly List<BlueprintBuff> m_CampingBuffs = new List<BlueprintBuff>();

	[NotNull]
	private readonly List<CutscenePlayerView> m_RunningCutscenes = new List<CutscenePlayerView>();

	private CampPlaceView m_CampPlace;

	private bool m_ResetCampPlaceAfterRest;

	private bool m_ScriptedRest;

	private RestPhase m_CurrentPhase;

	private bool m_FirstPhaseTick;

	private Action<RestStatus> m_Callback;

	[CanBeNull]
	private Coroutine m_PhaseCoroutine;

	[CanBeNull]
	private BarkBanterPlayer m_BanterPlayer;

	private Dictionary<UnitEntityData, CountableFlag> m_CharactersToBanter = new Dictionary<UnitEntityData, CountableFlag>();

	private RestStatus m_Status;

	public static int? ForcedCR;

	public List<UnitEntityData> CharactersToBeHealedOnRest;

	public static TimeSpan IterationRemainingTime { get; private set; }

	public static RestController Instance => Game.Instance.RestController;

	public IEnumerable<UnitEntityData> CharactersToBanter => m_CharactersToBanter.Keys;

	public CountableFlag CookingDisabled { get; } = new CountableFlag();

	public bool CorruptionDisabled
	{
		get
		{
			if (!Game.Instance.Player.Corruption.Disabled)
			{
				return Game.Instance.Player.Corruption.PreventGrowth;
			}
			return true;
		}
	}

	public bool NightWatchDisabled { get; private set; }

	public bool CamouflageDisabled { get; private set; }

	public bool HideScene { get; private set; }

	public bool NotShowUI { get; private set; }

	public bool HasCampPlace => m_CampPlace != null;

	public RestPhase CurrentPhase
	{
		get
		{
			return m_CurrentPhase;
		}
		private set
		{
			EventBus.RaiseEvent(delegate(IRestChangingPhase h)
			{
				h.HandleRestChangingPhase(m_CurrentPhase, value);
			});
			RestPhase phasePrevious = m_CurrentPhase;
			m_CurrentPhase = value;
			m_FirstPhaseTick = true;
			StopCoroutine();
			EventBus.RaiseEvent(delegate(IRestChangedPhase h)
			{
				h.HandleRestChangedPhase(phasePrevious, m_CurrentPhase);
			});
		}
	}

	[NotNull]
	public RestStatus Status
	{
		get
		{
			return m_Status ?? (m_Status = new RestStatus());
		}
		set
		{
			m_Status = value;
		}
	}

	public void Start([CanBeNull] CampPlaceView campPlace, bool resetCampPlaceAfterRest = false)
	{
		PFLog.Rest.Log("Start rest");
		PFLog.Rest.Log($"Camp place: {campPlace}");
		m_CampPlace = campPlace;
		m_ResetCampPlaceAfterRest = resetCampPlaceAfterRest;
		if (campPlace != null)
		{
			RestStatus restStatus = campPlace.GetRestStatus();
			PFLog.Rest.Log($"Remaning time: {restStatus?.RemainingRestTime ?? TimeSpan.Zero}");
			if (restStatus != null)
			{
				PFLog.Rest.Log("Sleeping state");
				CurrentPhase = RestPhase.ChecksAndSleepIteration;
				IterationRemainingTime = restStatus.RemainingRestTime;
				Status = restStatus;
				Status.WasNightRandomEncounter = restStatus.NightRandomEncounter;
				m_ScriptedRest = true;
			}
			else
			{
				PFLog.Rest.Log("Play camp start visual");
				CurrentPhase = RestPhase.Manage;
				campPlace.PlayStart();
			}
		}
		else
		{
			PFLog.Rest.Log("No camp place");
			CurrentPhase = RestPhase.Manage;
		}
		if (CurrentPhase == RestPhase.Manage && !NotShowUI)
		{
			PFLog.Rest.Log("Send HandleOpenRestCamp event");
			EventBus.RaiseEvent(delegate(IRestCampUIHandler h)
			{
				h.HandleOpenRestCamp();
			});
		}
		Game.Instance.StartMode(GameModeType.Rest);
	}

	public bool StartCamp()
	{
		if (Game.Instance.CurrentMode != GameModeType.Rest)
		{
			PFLog.Default.Error("Trying to start Camp phase without game mode active");
			return false;
		}
		if (!RestHelper.CanRest())
		{
			Game.Instance.StopMode(GameModeType.Rest);
			return false;
		}
		if (m_CampPlace != null)
		{
			m_CampPlace.StartCampSceneSound();
		}
		IterationRemainingTime = Game.Instance.Player.Camping.GetMinimumRestTime();
		CurrentPhase = RestPhase.AnimationsAndBarks;
		return true;
	}

	public void StartScripted(bool immediate, bool restWithCraft)
	{
		NotShowUI = immediate || !restWithCraft;
		m_ScriptedRest = true;
		if (immediate)
		{
			ApplyRestInterval();
			m_ScriptedRest = false;
			NotShowUI = false;
			return;
		}
		HideScene = true;
		CamouflageDisabled = true;
		NightWatchDisabled = true;
		m_CampPlace = null;
		IterationRemainingTime = Game.Instance.Player.Camping.GetMinimumRestTime();
		Start(null);
		if (NotShowUI)
		{
			CurrentPhase = RestPhase.AnimationsAndBarks;
		}
	}

	public void SkipPhase()
	{
		if (m_BanterPlayer != null && !m_BanterPlayer.Finished)
		{
			m_BanterPlayer.InterruptBark();
		}
		else if (!NotShowUI)
		{
			EventBus.RaiseEvent(delegate(IRestCampUIHandler h)
			{
				h.HandleSkipPhase();
			});
		}
	}

	public void FinishRest()
	{
		if (!Game.Instance.LoadedAreaState.Settings.DisableCampingEncounters && Game.Instance.CurrentlyLoadedArea.RandomEncounterSettings.AreRandomEncountersEnabled)
		{
			CampingEncounterIncreaseDifficulty component = Game.Instance.CurrentlyLoadedArea.GetComponent<CampingEncounterIncreaseDifficulty>();
			if (component != null)
			{
				Game.Instance.LoadedAreaState.CampingEncounterChanceIncrease += component.IncreaseChance;
				Game.Instance.LoadedAreaState.CampingEncounterDifficultyIncrease += component.IncreaseDifficulty;
			}
		}
		CurrentPhase = RestPhase.Finished;
		LoadingProcess.Instance.StartLoadingProcess(StopRestProcess(), null, LoadingProcessTag.Camping);
	}

	public void SetCallback(Action<RestStatus> onRestEnd)
	{
		m_Callback = onRestEnd;
	}

	public void FakeRestUnit(UnitEntityData unit)
	{
		ApplyRest(new List<UnitEntityData> { unit });
	}

	public void Tick()
	{
		switch (CurrentPhase)
		{
		case RestPhase.AnimationsAndBarks:
			if (m_FirstPhaseTick)
			{
				m_FirstPhaseTick = false;
				StartCoroutine(CampCoroutine());
			}
			TickCamp();
			break;
		case RestPhase.ChecksAndSleepIteration:
			if (m_FirstPhaseTick)
			{
				m_FirstPhaseTick = false;
				StartSleepPhase();
			}
			TickSleepPhase();
			break;
		case RestPhase.Manage:
		case RestPhase.ShowingResults:
		case RestPhase.Finished:
			break;
		}
	}

	private void TickCamp()
	{
		m_BanterPlayer?.Tick();
	}

	private void CleanupBodies()
	{
		if (m_CampPlace == null)
		{
			return;
		}
		float bodiesCleanupRadius = BlueprintRoot.Instance.Camping.BodiesCleanupRadius;
		FxHelper.DestroyAllBlood();
		foreach (UnitEntityData unit in Game.Instance.State.Units)
		{
			if (!unit.IsPlayerFaction && unit.Descriptor.State.IsFinallyDead && !unit.Descriptor.State.AdditionalFeatures.SuppressedDecomposition && !(unit.DistanceTo(m_CampPlace.transform.position) > bodiesCleanupRadius))
			{
				unit.DropLootToGround();
				unit.IsInGame = false;
			}
		}
	}

	public void AddCharacterToBanter(UnitEntityData data)
	{
		if (!m_CharactersToBanter.TryGetValue(data, out var value))
		{
			value = new CountableFlag();
			m_CharactersToBanter.Add(data, value);
		}
		value.Retain();
	}

	public void RemoveCharacterToBanter(UnitEntityData data)
	{
		if (!m_CharactersToBanter.TryGetValue(data, out var value))
		{
			PFLog.Default.Error($"Cannot remove character {data} from the list of characters that are allowed to banter on rest because he/she is not there.");
			return;
		}
		value.Release();
		if (!value)
		{
			m_CharactersToBanter.Remove(data);
		}
	}

	private void PlayVisual(TimeSpan campTime)
	{
		CampPlaceView campPlace = m_CampPlace;
		if (campPlace == null)
		{
			m_BanterPlayer = BarkBanterHelper.SelectBanter(campTime);
			if (m_BanterPlayer != null)
			{
				List<UnitEntityData> speakers = m_BanterPlayer.GetSpeakers();
				if (speakers.Count > 0)
				{
					Game.Instance.SelectionCharacter.EnsureSpeakersVisible(speakers[0], speakers[(speakers.Count > 1) ? 1 : 0]);
					Game.Instance.SelectionCharacter.Tick();
				}
			}
			return;
		}
		CampingState camping = Game.Instance.Player.Camping;
		CampingRoot camping2 = BlueprintRoot.Instance.Camping;
		campPlace.PlayCamp(Status);
		campPlace.TeleportParty(Status);
		m_BanterPlayer = BarkBanterHelper.SelectBanter(campTime);
		foreach (UnitEntityData partyAndPet in Game.Instance.Player.PartyAndPets)
		{
			if (!partyAndPet.Descriptor.State.IsDead && !partyAndPet.Blueprint.GetComponent<NonHumanoidCompanion>())
			{
				Cutscene cutscene = null;
				if (camping.IsCooker(partyAndPet, Status) && Status.CurrentIteration.AlchemyCooking.Success)
				{
					cutscene = camping2.CookingScene;
				}
				else if (camping.IsCamouflageMaster(partyAndPet, Status))
				{
					cutscene = camping2.CamouflageScene;
				}
				else if (camping.IsDivineServant(partyAndPet, Status) && Status.CurrentIteration.DivineService.Success)
				{
					cutscene = camping2.DivineServiceScene;
				}
				else if (camping.IsScrollScriber(partyAndPet) && Status.CurrentIteration.ScrollScribing.Success)
				{
					cutscene = camping2.ScrollScribingScene;
				}
				else if (partyAndPet.IsPet)
				{
					cutscene = camping2.PetScene;
				}
				if (cutscene == null)
				{
					cutscene = camping2.DefaultScene;
				}
				if (!partyAndPet.Descriptor.State.IsDead)
				{
					PlayCutscene(cutscene, partyAndPet);
				}
			}
		}
	}

	private IEnumerator CampCoroutine()
	{
		try
		{
			Status = new RestStatus();
			TimeSpan campTime = Game.Instance.TimeController.GameTime;
			float notificationTime = BlueprintRoot.Instance.Camping.NotificationTime;
			float startupTime = BlueprintRoot.Instance.Camping.StartupNotificationTime;
			SpendTime(DefaultBuffsSkipTime);
			Status.BuffsSkipTime = DefaultBuffsSkipTime;
			yield return null;
			if (!NotShowUI)
			{
				StartCraft();
				PerformCampingChecks();
				EventBus.RaiseEvent(delegate(IRestCampUIHandler h)
				{
					h.HandleVisualCampPhaseFinished();
				});
			}
			Game.Instance.Player.Camping.OverallCampsCount++;
			CleanupBodies();
			if (!NotShowUI)
			{
				PlayVisual(campTime);
				yield return null;
				yield return new WaitForSeconds(startupTime);
				while (m_BanterPlayer != null && !m_BanterPlayer.Finished)
				{
					yield return null;
				}
			}
			ResurrectDeadUnits();
			if (UseRestSpells())
			{
				CampPlaceView playerPlacedInstance = CampPlaceView.PlayerPlacedInstance;
				if (playerPlacedInstance != null)
				{
					FxHelper.SpawnFxOnPoint(BlueprintRoot.Instance.Camping.HealingFx, playerPlacedInstance.transform.position, sourceFromParty: true, Quaternion.identity);
					yield return new WaitForSeconds(notificationTime);
				}
			}
		}
		finally
		{
			RestController restController = this;
			restController.CurrentPhase = RestPhase.ChecksAndSleepIteration;
			EventBus.RaiseEvent(delegate(IRestCampEvents h)
			{
				h.EndCampPhase();
			});
			restController.m_PhaseCoroutine = null;
		}
	}

	private void StartCraft()
	{
		CampingState camping = Game.Instance.Player.Camping;
		CraftManager craftManager = Game.Instance.Player.CraftManager;
		UnitReference primaryUnit = camping.CurrentCampingRoles[CampingRoleType.Alchemist].PrimaryUnit;
		if (camping.SelectedPotion != null && primaryUnit != null && BlueprintRoot.Instance.CraftRoot.CheckCraftAvail(primaryUnit, camping.SelectedPotion, craftManager.GetPausedState(camping.SelectedPotion, UsableItemType.Potion) != null).IsAvail)
		{
			Status.PotionCraftState = craftManager.GetCraftSlotState(UsableItemType.Potion).StartFromPauseOrNew(camping.SelectedPotion);
		}
		else
		{
			craftManager.PauseCraft(UsableItemType.Potion);
			camping.SelectedPotion = null;
			Status.PotionCraftState = null;
		}
		UnitReference primaryUnit2 = camping.CurrentCampingRoles[CampingRoleType.ScrollScribe].PrimaryUnit;
		if (camping.SelectedScroll != null && primaryUnit2 != null && BlueprintRoot.Instance.CraftRoot.CheckCraftAvail(primaryUnit2, camping.SelectedScroll, craftManager.GetPausedState(camping.SelectedScroll, UsableItemType.Scroll) != null).IsAvail)
		{
			Status.ScrollCraftState = craftManager.GetCraftSlotState(UsableItemType.Scroll).StartFromPauseOrNew(camping.SelectedScroll);
			return;
		}
		craftManager.PauseCraft(UsableItemType.Scroll);
		camping.SelectedScroll = null;
		Status.ScrollCraftState = null;
	}

	private void StartSleepPhase()
	{
		Status.NightRandomEncounter = TryRollRandomEncounter();
		if (Status.NightRandomEncounter && Status.SpecialCampingEncounter == null)
		{
			string notificationText = string.Format(Game.Instance.BlueprintRoot.LocalizedTexts.UserInterfacesText.Rest.NightEncounter, Status.TimePassedBeforeEncounter.Hours);
			EventBus.RaiseEvent(delegate(IWarningNotificationUIHandler h)
			{
				h.HandleWarning(notificationText);
			});
		}
	}

	private void TickSleepPhase()
	{
		if (Status.NightRandomEncounter)
		{
			CurrentPhase = RestPhase.Finished;
			LoadingProcess.Instance.StartLoadingProcess(StopRestProcess(), null, LoadingProcessTag.Camping);
			return;
		}
		Status.RestSucceeded = true;
		if (Status.AppliedIterations >= Game.Instance.Player.Camping.RestIterationsCount)
		{
			if (NotShowUI)
			{
				FinishRest();
				return;
			}
			CurrentPhase = RestPhase.ShowingResults;
			EventBus.RaiseEvent(delegate(IRestCampUIHandler h)
			{
				h.HandleShowResults();
			});
			return;
		}
		TimeSpan timeSpan = SpendTime(IterationRemainingTime);
		Status.SleepTime += timeSpan;
		Game.Instance.Player.Camping.LastCampTime = Game.Instance.Player.GameTime;
		if (Status.ApplyRest)
		{
			ApplyRestInterval();
		}
		if (Status.IterationNumber < Game.Instance.Player.Camping.RestIterationsCount - 1)
		{
			Status.StartNextIteration();
			IterationRemainingTime = Game.Instance.Player.Camping.GetMinimumRestTime();
			PerformCampingChecks();
			CurrentPhase = RestPhase.ChecksAndSleepIteration;
		}
	}

	private void PerformCampingChecks()
	{
		PerformDivineService();
		PerformCooking();
		PerformCamouflage();
		PerformCraftChecks();
	}

	private void PerformDivineService()
	{
		if (!CorruptionDisabled)
		{
			CampingState camping = Game.Instance.Player.Camping;
			Status.CurrentIteration.DivineService.SetCheckResult(camping.CurrentCampingRoles[CampingRoleType.DivineService].PerformCheck(StatType.SkillLoreReligion, RestHelper.GetDivineServiceDC()));
		}
	}

	private void PerformCooking()
	{
		if ((bool)Game.Instance.Player.CraftManager.Disabled || (bool)CookingDisabled)
		{
			return;
		}
		CampingState camping = Game.Instance.Player.Camping;
		BlueprintCookingRecipe cookingRecipe = camping.CookingRecipe;
		if (cookingRecipe != null && cookingRecipe.CheckIngredients())
		{
			RuleSkillCheck ruleSkillCheck = camping.CurrentCampingRoles[CampingRoleType.Alchemist].PerformCheck(StatType.SkillKnowledgeWorld, RestHelper.GetCookingDC());
			if (ruleSkillCheck != null)
			{
				Status.CurrentIteration.AlchemyCooking.SetCheckResult(ruleSkillCheck);
				cookingRecipe.SpendIngredients();
			}
		}
	}

	private void PerformCamouflage()
	{
		if (!CamouflageDisabled)
		{
			CampingState camping = Game.Instance.Player.Camping;
			Status.CurrentIteration.Camouflage.SetCheckResult(camping.CurrentCampingRoles[CampingRoleType.Camouflage].PerformCheck(StatType.SkillStealth, RestHelper.GetCamouflageDC()));
		}
	}

	private void PerformCraftChecks()
	{
		Game.Instance.Player.CraftManager.SetCheckResult(Status);
	}

	private bool UseRestSpells()
	{
		bool flag = false;
		if (m_ScriptedRest || Game.Instance.Player.Camping.UseSpells)
		{
			UpdateCharactersToBeHealedOnRest();
			foreach (UnitEntityData item in CharactersToBeHealedOnRest)
			{
				try
				{
					flag |= item.UseSpellsOnRest();
				}
				catch (Exception ex)
				{
					PFLog.Default.Exception(ex, null);
				}
			}
		}
		Status.RestSpellsUsed = true;
		return flag;
	}

	private static void ResurrectDeadUnits()
	{
		foreach (UnitEntityData item in CampingState.GetPartyUnitsForRest(removePets: false, includeDeadAndParalyzed: true))
		{
			if (item.Descriptor.State.IsFinallyDead && (bool)item.State.Features.ResurrectOnRest)
			{
				item.Descriptor.Resurrect();
				item.Descriptor.State.UpdateLifeState(UnitLifeState.Conscious);
				item.Damage = (int)item.Stats.HitPoints - Math.Min(1, item.Descriptor.Progression.CharacterLevel);
				if (Game.Instance.IsModeActive(GameModeType.GlobalMap))
				{
					item.IsInGame = false;
				}
				else if (item.Master != null)
				{
					item.Position = ResurrectionLogic.GetResurrectPosition(item.Master, item);
				}
			}
		}
		BlueprintCampaignRestBehaviour component = Game.Instance.Player.Campaign.GetComponent<BlueprintCampaignRestBehaviour>();
		if (component == null || !component.ShouldRemoveDeathDoor())
		{
			return;
		}
		foreach (UnitEntityData item2 in CampingState.GetPartyUnitsForRest(removePets: false, includeDeadAndParalyzed: true))
		{
			item2.Descriptor.State.RemoveConditionAll(UnitCondition.DeathDoor);
		}
	}

	private void UpdateCharactersToBeHealedOnRest()
	{
		CharactersToBeHealedOnRest = (from u in CampingState.GetPartyUnitsForRest(removePets: false, includeDeadAndParalyzed: true)
			where !u.Descriptor.State.IsDead
			select u).ToList();
	}

	private void ApplyRestInterval()
	{
		PFLog.Default.Log("Rest tick");
		ResurrectDeadUnits();
		if (!Status.RestSpellsUsed)
		{
			UseRestSpells();
		}
		ApplyRest();
		foreach (ItemEntity item in Game.Instance.Player.Inventory)
		{
			item.RestoreCharges();
		}
		if (!NotShowUI)
		{
			Game.Instance.Player.CraftManager.TickCraft(Status);
		}
		Game.Instance.Player.Corruption.TickRest(Status);
		Status.AppliedIterations++;
	}

	private void ApplyRest(List<UnitEntityData> overrideUnits = null)
	{
		foreach (UnitEntityData item in overrideUnits ?? CampingState.GetPartyUnitsForRest(removePets: false, includeDeadAndParalyzed: true))
		{
			if (item.Descriptor.State.IsDead)
			{
				continue;
			}
			item.Buffs.Tick(Status.TotalTime);
			if (!IsTired(item))
			{
				HealAndApplyRest(item, Status);
				UnitEntityData pair = UnitPartDualCompanion.GetPair(item);
				if (pair != null)
				{
					HealAndApplyRest(pair, Status);
				}
			}
		}
	}

	private bool IsTired(UnitEntityData unit)
	{
		if (m_ScriptedRest)
		{
			return false;
		}
		if (Status.SpecialCampingEncounter != null)
		{
			if (Status.SpecialCampingEncounter.PartyTired)
			{
				return true;
			}
			if (Status.SpecialCampingEncounter.MainCharacterTired && unit.IsMainCharacter)
			{
				return true;
			}
		}
		return false;
	}

	private void ApplyCooking()
	{
		BlueprintCookingRecipe cookingRecipe = Game.Instance.Player.Camping.CookingRecipe;
		if (cookingRecipe == null || !Status.CurrentIteration.AlchemyCooking.Success)
		{
			return;
		}
		foreach (UnitEntityData item in CampingState.GetPartyUnitsForRest(removePets: false, includeDeadAndParalyzed: true))
		{
			foreach (BlueprintBuff partyBuff in cookingRecipe.PartyBuffs)
			{
				item.Descriptor.AddBuff(partyBuff, item, cookingRecipe.BuffDuration);
			}
			BlueprintCookingRecipe.UnitBuffEntry[] unitBuffs = cookingRecipe.UnitBuffs;
			foreach (BlueprintCookingRecipe.UnitBuffEntry unitBuffEntry in unitBuffs)
			{
				if (item.Blueprint == unitBuffEntry.Unit)
				{
					item.Descriptor.AddBuff(unitBuffEntry.Buff, item, cookingRecipe.BuffDuration);
				}
			}
		}
	}

	private bool TryRollRandomEncounter()
	{
		if (m_ScriptedRest || NightWatchDisabled || (BuildModeUtility.IsCheatsEnabled && !CheatsCommon.RandomEncounters))
		{
			return false;
		}
		CampingRoot camping = BlueprintRoot.Instance.Camping;
		CampingState camping2 = Game.Instance.State.PlayerState.Camping;
		if (TryRollSpecialEncounter(camping2))
		{
			return true;
		}
		if (camping2.DisableRandomEncountersOnce)
		{
			camping2.DisableRandomEncountersOnce = false;
			return false;
		}
		if (!RollEncounter(camping, out var guardSlot, out var timePassed))
		{
			return false;
		}
		if (Game.Instance.IsModeActive(GameModeType.GlobalMap))
		{
			bool num = Game.Instance.RandomEncountersController.RollCampingEncounter(Status);
			if (num)
			{
				FillReData(timePassed, guardSlot);
			}
			return num;
		}
		return TryPerformEncounterInCamp(guardSlot, timePassed);
	}

	private bool TryPerformEncounterInCamp(int guardSlot, TimeSpan timePassed)
	{
		CampingState camping = Game.Instance.Player.Camping;
		if (m_CampPlace == null)
		{
			return false;
		}
		Vector3 position = m_CampPlace.transform.position;
		int cr;
		List<UnitEntityData> list = RandomEncounterUnitSelector.SpawnCampRandomEncounter(out cr, ForcedCR, position);
		if (list.Count <= 0)
		{
			return false;
		}
		CampingRole campingRole = ((guardSlot == 0) ? camping.CurrentCampingRoles[CampingRoleType.GuardFirstWatch] : camping.CurrentCampingRoles[CampingRoleType.GuardSecondWatch]);
		int num = list.Select((UnitEntityData u) => u.Stats.SkillStealth.ModifiedValue).Min();
		CheckStatus obj = ((guardSlot == 0) ? Status.CurrentIteration.GuardFirst : Status.CurrentIteration.GuardSecond);
		RuleSkillCheck ruleSkillCheck = campingRole.PerformCheck(StatType.SkillPerception, num + RestHelper.GetGuardDC());
		obj.SetCheckResult(ruleSkillCheck);
		bool num2 = ruleSkillCheck?.Success ?? false;
		FillReData(timePassed, guardSlot);
		if (m_CampPlace != null)
		{
			m_CampPlace.PlaySleeping(Status);
			m_CampPlace.TeleportParty(Status);
		}
		if (num2)
		{
			RandomEncounterUnitSelector.PlaceUnitsOutsideOfCamp(list, position);
		}
		else
		{
			RandomEncounterUnitSelector.PlaceUnitsInCamp(list, position, campingRole);
			ApplySleepingState(guardSlot);
			Game.Instance.Player.REManager.OnCampEncounterStarted();
		}
		RandomEncounterUnitSelector.StartCombat(list);
		return true;
	}

	private bool RollEncounter(CampingRoot root, out int guardSlot, out TimeSpan timePassed)
	{
		int num = 0;
		if (Game.Instance.CurrentlyLoadedArea.RandomEncounterSettings.AreRandomEncountersEnabled)
		{
			num = Mathf.RoundToInt((Game.Instance.Player.REManager.CampEncounterChance + Game.Instance.LoadedAreaState.CampingEncounterChanceIncrease) * 100f);
			if (Status.CurrentIteration.Camouflage.CriticalFail)
			{
				num += root.CamouflageCriticalFailEncounterChance;
			}
			else if (Status.CurrentIteration.Camouflage.Check != null)
			{
				RuleSkillCheck check = Status.CurrentIteration.Camouflage.Check;
				if (check.Success)
				{
					num -= root.CamouflageSuccessValue;
					num -= (check.RollResult - check.DC) / root.CamouflageExtraCost * root.CamouflageExtraValue;
				}
			}
		}
		guardSlot = UnityEngine.Random.Range(0, 2);
		timePassed = ((float)CampingState.DefaultCampTime.Hours / 2f * (float)guardSlot).Hours();
		int num2 = UnityEngine.Random.Range(1, 101);
		bool hasValue = ForcedCR.HasValue;
		PFLog.Default.Log($"Try roll camping RE: roll={num2}, chance={num}, forced={hasValue}");
		if (num2 > num && !hasValue)
		{
			return false;
		}
		return true;
	}

	private bool TryRollSpecialEncounter(CampingState state)
	{
		foreach (BlueprintCampingEncounter extraEncounter in state.ExtraEncounters)
		{
			if ((!extraEncounter.NotOnGlobalMap || !UIUtility.IsGlobalMap()) && extraEncounter.Conditions.Check() && !((float)UnityEngine.Random.Range(1, 101) > (float)extraEncounter.Chance + Game.Instance.LoadedAreaState.CampingEncounterChanceIncrease * 100f))
			{
				Status.SpecialCampingEncounter = extraEncounter;
				if (extraEncounter.InterruptsRest)
				{
					TimeSpan deltaTime = UnityEngine.Random.Range(1f, 7f).Hours();
					Status.TimePassedBeforeEncounter = SpendTime(deltaTime);
					return true;
				}
				break;
			}
		}
		return false;
	}

	private void FillReData(TimeSpan timePassed, int guardSlot)
	{
		timePassed = SpendTime(timePassed);
		Status.TimePassedBeforeEncounter += timePassed;
		Status.WakeUpGuardsSlot = guardSlot;
		Status.NightRandomEncounter = true;
		Status.RemainingRestTime = IterationRemainingTime;
	}

	public void ApplySleepingState(int guardSlot, bool fromGlobalMap = false)
	{
		CampingState camping = Game.Instance.Player.Camping;
		CampingRole campingRole = ((guardSlot == 0) ? camping.CurrentCampingRoles[CampingRoleType.GuardFirstWatch] : camping.CurrentCampingRoles[CampingRoleType.GuardSecondWatch]);
		BlueprintBuff sleepingBuff = BlueprintRoot.Instance.SystemMechanics.SleepingBuff;
		foreach (UnitEntityData partyAndPet in Game.Instance.Player.PartyAndPets)
		{
			if (campingRole.HasUnit(partyAndPet))
			{
				continue;
			}
			partyAndPet.Descriptor.AddBuff(sleepingBuff, partyAndPet);
			m_CampingBuffs.Add(sleepingBuff);
			UnitProneController.Tick(partyAndPet);
			partyAndPet.Descriptor.State.Prone.Duration = 3f.Seconds();
			if (partyAndPet.View.AnimationManager != null)
			{
				partyAndPet.View.AnimationManager.IsProne = true;
				partyAndPet.View.AnimationManager.IsSleeping = true;
				partyAndPet.View.AnimationManager.IsSleepingInCamp = true;
				if (!fromGlobalMap)
				{
					partyAndPet.View.AnimationManager.FastForwardProneAnimation();
				}
			}
			ArmorSlot armor = partyAndPet.Body.Armor;
			if (armor.HasItem)
			{
				ArmorProficiencyGroup armorProficiencyGroup = armor.Armor.ArmorType();
				if ((armorProficiencyGroup == ArmorProficiencyGroup.Medium && !partyAndPet.Descriptor.State.Features.Endurance) || armorProficiencyGroup == ArmorProficiencyGroup.Heavy)
				{
					BlueprintBuff disableArmorInRestEncounterBuff = BlueprintRoot.Instance.SystemMechanics.DisableArmorInRestEncounterBuff;
					partyAndPet.Descriptor.AddBuff(disableArmorInRestEncounterBuff, partyAndPet);
					m_CampingBuffs.Add(disableArmorInRestEncounterBuff);
				}
			}
		}
	}

	private void PlayCutscene([CanBeNull] Cutscene cutscene, [NotNull] UnitEntityData unit)
	{
		if (cutscene != null)
		{
			CutscenePlayerView item = CutscenePlayerView.Play(cutscene, new ParametrizedContextSetter
			{
				AdditionalParams = { 
				{
					UnitCutsceneName,
					(object)(UnitReference)unit
				} }
			});
			m_RunningCutscenes.Add(item);
		}
	}

	public static void HealAndApplyRest([NotNull] UnitEntityData unit, RestStatus status)
	{
		UnitRestInfo unitRestInfo = new UnitRestInfo(unit.Descriptor, status);
		Rulebook.Trigger(new RuleHealDamage(unit, unit, Instance.m_ScriptedRest ? unit.Damage : unitRestInfo.HealedDamage));
		StatType[] attributes = StatTypeHelper.Attributes;
		foreach (StatType stat in attributes)
		{
			if (unitRestInfo.HealedStatDamage > 0)
			{
				Rulebook.Trigger(new RuleHealStatDamage(unit, unit, stat, unitRestInfo.HealedStatDamage));
			}
			if (unitRestInfo.HealedStatDrain > 0)
			{
				Rulebook.Trigger(new RuleHealStatDamage(unit, unit, stat, unitRestInfo.HealedStatDrain)
				{
					ShouldHealDrain = true
				});
			}
		}
		ApplyRest(unit.Descriptor);
		unit.Descriptor.LastRestTime = Game.Instance.TimeController.GameTime;
	}

	public static void ApplyRest([NotNull] UnitDescriptor unit)
	{
		unit.Replenish();
		unit.Buffs.Enumerable.Where((Buff b) => b.Blueprint.RemoveOnRest).ToArray().ForEach(delegate(Buff b)
		{
			b.Remove();
		});
		UnitPartDualCompanion unitPartDualCompanion = unit.Get<UnitPartDualCompanion>();
		if (unitPartDualCompanion != null)
		{
			unitPartDualCompanion.IsDead = false;
		}
		EventBus.RaiseEvent(delegate(IUnitRestHandler h)
		{
			h.HandleUnitRest(unit.Unit);
		});
	}

	private void Reset()
	{
		IterationRemainingTime = TimeSpan.Zero;
		Status = new RestStatus();
		m_ScriptedRest = false;
		NotShowUI = false;
		CamouflageDisabled = false;
		NightWatchDisabled = false;
		HideScene = false;
		m_BanterPlayer = null;
		Game.Instance.Player.CraftManager.PauseCraft(UsableItemType.Scroll);
		Game.Instance.Player.CraftManager.PauseCraft(UsableItemType.Potion);
		StopCoroutine();
		m_Callback = null;
	}

	public void Activate()
	{
		foreach (UnitEntityData unit in Game.Instance.State.Units)
		{
			if (!CutsceneControlledUnit.GetControllingPlayer(unit))
			{
				unit.Commands.InterruptAll();
			}
		}
		Game.Instance.ProjectileController.Clear();
	}

	public void Deactivate()
	{
	}

	private void StopCutscenes()
	{
		foreach (CutscenePlayerView runningCutscene in m_RunningCutscenes)
		{
			if (!(runningCutscene == null) && runningCutscene.PlayerData != null && !runningCutscene.PlayerData.Destroyed)
			{
				runningCutscene.PlayerData.Stop();
			}
		}
		m_RunningCutscenes.Clear();
	}

	private void RemoveCampingBuffs()
	{
		foreach (BlueprintBuff campingBuff in m_CampingBuffs)
		{
			foreach (UnitEntityData partyAndPet in Game.Instance.Player.PartyAndPets)
			{
				partyAndPet.Descriptor.Buffs.RemoveFact(campingBuff);
			}
		}
		m_CampingBuffs.Clear();
	}

	public void Stop()
	{
		bool flag = Status.RestSucceeded || Status.SkipTime;
		if (Status.RestSucceeded)
		{
			Game.Instance.Player.Camping.LastCampTime = Game.Instance.Player.GameTime;
		}
		if (HideScene)
		{
			Game.Instance.AdvanceGameTime(Status.TotalTime);
		}
		ApplyCooking();
		if (CurrentPhase != RestPhase.Manage)
		{
			foreach (UnitEntityData item in CampingState.GetPartyUnitsForRest())
			{
				UnitPartWeariness unitPartWeariness = item.Ensure<UnitPartWeariness>();
				if (unitPartWeariness.LastStackTime != TimeSpan.Zero)
				{
					unitPartWeariness.AddWearinessHours((float)(0.0 - Status.TotalTime.TotalHours));
				}
			}
		}
		if (m_CampPlace != null)
		{
			switch (Status.Result)
			{
			case RestResult.Unknown:
				m_CampPlace.Reset();
				break;
			case RestResult.Success:
			case RestResult.SkipTime:
			{
				if (m_ResetCampPlaceAfterRest)
				{
					m_CampPlace.Reset();
					m_CampPlace.TeleportParty(Status);
					break;
				}
				MapObjectView mapObjectView = m_CampPlace.ReplaceWithInactiveCamp();
				if (mapObjectView != null)
				{
					new CampPositionsSelector(mapObjectView.gameObject).TeleportParty(Status);
				}
				else
				{
					m_CampPlace.TeleportParty(Status);
				}
				break;
			}
			}
		}
		if (Status.SpecialCampingEncounter != null && (Status.RestSucceeded || Status.SpecialCampingEncounter.InterruptsRest))
		{
			Status.SpecialCampingEncounter.EncounterActions.Run();
		}
		EventBus.RaiseEvent(delegate(IRestFinishedHandler h)
		{
			h.HandleRestFinished(Status);
		});
		if (Status.Result != RestResult.NightRandomEncounter)
		{
			RemoveCampingBuffs();
		}
		m_Callback?.Invoke(Status);
		Reset();
		StopCutscenes();
		Game.Instance.Player.Camping.CleanupRoles();
		if (flag && Game.Instance.SaveManager.IsSaveAllowed(SaveInfo.SaveType.Auto))
		{
			Game.Instance.SaveGame(Game.Instance.SaveManager.GetNextAutoslot());
		}
		if (CurrentPhase > RestPhase.Manage)
		{
			Game.Instance.MatchTimeOfDay();
		}
		DialogState dialog = Game.Instance.Player.Dialog;
		if (dialog.Scheduled != null && !dialog.Scheduled.IsScheduled && CurrentPhase == RestPhase.ShowingResults)
		{
			Game.Instance.DialogController.StartScheduledDialog();
		}
	}

	private IEnumerator StopRestProcess()
	{
		Game.Instance.StopMode(GameModeType.Rest);
		StopCutscenes();
		yield return null;
		Game.Instance.EntityCreator.Tick();
		Game.Instance.EntityDestroyer.Tick();
		using (CodeTimer.New("Preload Unit Resources After Rest"))
		{
			try
			{
				ResourcesLibrary.StartPreloadingMode();
				ResourcesPreload.PreloadUnitResources();
				while (ResourcesLibrary.TickPreloading())
				{
					yield return null;
				}
			}
			finally
			{
				ResourcesLibrary.StopPreloadingMode();
			}
		}
		yield return null;
	}

	private TimeSpan SpendTime(TimeSpan deltaTime)
	{
		TimeSpan timeSpan = IterationRemainingTime - deltaTime;
		TimeSpan timeSpan2 = deltaTime;
		if (timeSpan < TimeSpan.Zero)
		{
			timeSpan2 = deltaTime + timeSpan;
		}
		IterationRemainingTime -= timeSpan2;
		if (!HideScene)
		{
			Game.Instance.AdvanceGameTime(timeSpan2);
		}
		return timeSpan2;
	}

	private void StartCoroutine(IEnumerator coroutine)
	{
		UICommon common = Game.Instance.UI.Common;
		m_PhaseCoroutine = common.StartCoroutine(coroutine);
	}

	private void StopCoroutine()
	{
		if (m_PhaseCoroutine != null)
		{
			Game.Instance.UI.Common.StopCoroutine(m_PhaseCoroutine);
			m_PhaseCoroutine = null;
		}
	}

	public void OnEventAboutToTrigger(RuleSkillCheck evt)
	{
	}
}
