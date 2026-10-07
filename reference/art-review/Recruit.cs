using System;
using System.Collections.Generic;
using System.Linq;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Designers.EventConditionActionSystem.ContextData;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.PubSubSystem;
using Kingmaker.Settings;
using Kingmaker.UI.Models.Log;
using Kingmaker.UI.Selection;
using Kingmaker.UnitLogic;
using Kingmaker.UnitLogic.Parts;
using Kingmaker.Utility;
using Kingmaker.View;
using Owlcat.QA.Validation;
using Owlcat.Runtime.Core.Utils;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.Designers.EventConditionActionSystem.Actions;

[ComponentName("Actions/Recruit")]
[AllowMultipleComponents]
[TypeId("b90eea06ce91f564e8793832eea02cef")]
public class Recruit : GameAction
{
	[Serializable]
	public class RecruitData
	{
		[ValidateNotNull]
		[SerializeField]
		[FormerlySerializedAs("CompanionBlueprint")]
		private BlueprintUnitReference m_CompanionBlueprint;

		[Tooltip("Optional. Which unit should be replaced.")]
		[SerializeReference]
		public UnitEvaluator NPCUnit;

		public bool MustBeInParty;

		[NonSerialized]
		public UnitEntityData RecruitedCompanion;

		public BlueprintUnit CompanionBlueprint => m_CompanionBlueprint?.Get();
	}

	public RecruitData[] Recruited;

	public bool AddToParty = true;

	public bool MatchPlayerXpExactly;

	public ActionList OnRecruit;

	public ActionList OnRecruitImmediate;

	public override void RunAction()
	{
		RecruitData[] recruited = Recruited;
		foreach (RecruitData data in recruited)
		{
			SwitchToCompanion(data);
		}
		Game.Instance.EntityCreator.Tick();
		if (Game.Instance.Player.Party.Count > 6)
		{
			recruited = Recruited;
			foreach (RecruitData recruitData in recruited)
			{
				Game.Instance.Player.RemoveCompanion(recruitData.RecruitedCompanion, stayInGame: true);
			}
			ShowPartyInterface();
			return;
		}
		recruited = Recruited;
		foreach (RecruitData recruitData2 in recruited)
		{
			using (ContextData<RecruitedUnitData>.Request().Setup(recruitData2.RecruitedCompanion))
			{
				OnRecruit.Run();
			}
		}
	}

	private void ShowPartyInterface()
	{
		List<RecruitData> list = Recruited.Where((RecruitData recruitData) => recruitData.MustBeInParty).ToList();
		if (list.Count > 5)
		{
			PFLog.Default.Error(this, $"Cannot recruit {list.Count} characters in {this}: too many!!");
			return;
		}
		while (Game.Instance.Player.Party.Count > 6 - list.Count)
		{
			UnitEntityData value = Game.Instance.Player.Party.Last((UnitEntityData c) => c != GameHelper.GetPlayerCharacter());
			Game.Instance.Player.RemoveCompanion(value, stayInGame: true);
		}
		foreach (RecruitData item in list)
		{
			Game.Instance.Player.AddCompanion(item.RecruitedCompanion);
		}
		List<BlueprintUnit> requiredUnits = list.Select((RecruitData r) => r.CompanionBlueprint).ToList();
		EventBus.RaiseEvent(delegate(IGroupChangerHandler h)
		{
			h.HandleCall(delegate
			{
				foreach (UnitEntityData item2 in Game.Instance.Player.RemoteCompanions.ToTempList())
				{
					item2.IsInGame = false;
				}
				Game.Instance.Player.FixPartyAfterChange(ignoreCapitalMode: true);
				Game.Instance.UI.SelectionManager.UpdateSelectedUnits();
				RecruitData[] recruited = Recruited;
				foreach (RecruitData recruitData in recruited)
				{
					using (ContextData<RecruitedUnitData>.Request().Setup(recruitData.RecruitedCompanion))
					{
						OnRecruit.Run();
					}
				}
				List<UnitEntityView> views = Game.Instance.Player.Party.Select((UnitEntityData character) => character.View).ToTempList();
				(Game.Instance.UI.SelectionManager as SelectionManagerPC)?.MultiSelect(views);
			}, delegate
			{
				foreach (UnitEntityData item3 in Game.Instance.Player.RemoteCompanions.ToTempList())
				{
					item3.IsInGame = false;
				}
				RecruitData[] recruited = Recruited;
				foreach (RecruitData recruitData in recruited)
				{
					using (ContextData<RecruitedUnitData>.Request().Setup(recruitData.RecruitedCompanion))
					{
						OnRecruit.Run();
					}
				}
			}, isCapital: false, requiredUnits);
		});
	}

	private void SwitchToCompanion(RecruitData data)
	{
		Player player = Game.Instance.Player;
		UnitEntityData unitEntityData = player.AllCharacters.FirstOrDefault((UnitEntityData u) => u.Blueprint == data.CompanionBlueprint);
		bool flag = (object)unitEntityData != null && unitEntityData.Get<UnitPartCompanion>()?.State == CompanionState.ExCompanion;
		bool flag2 = (object)unitEntityData != null && unitEntityData.Get<UnitPartCompanion>()?.State == CompanionState.Remote;
		UnitEntityData value = null;
		ElementExtendAsObject.Or(data.NPCUnit, null)?.TryGetValue(out value);
		if (unitEntityData == null || flag)
		{
			unitEntityData = GameHelper.RecruitNPC(value, data.CompanionBlueprint);
		}
		else
		{
			if (!flag2)
			{
				PFLog.Default.Error(this, "Attempted to double-recruit " + data.CompanionBlueprint?.ToString() + " in " + this);
				return;
			}
			if (value != null && !value.IsPlayerFaction)
			{
				value.MarkForDestroy();
				unitEntityData.Position = value.Position;
				unitEntityData.Orientation = value.Orientation;
			}
			unitEntityData.IsInGame = true;
			player.AddCompanion(unitEntityData);
		}
		unitEntityData.GroupId = "<directly-controllable-unit>";
		unitEntityData.UpdateGroup();
		if (!SettingsRoot.Difficulty.OnlyActiveCompanionsReceiveExperience || MatchPlayerXpExactly)
		{
			int experience = Game.Instance.Player.MainCharacter.Value.Descriptor.Progression.Experience;
			unitEntityData.Descriptor.Progression.AdvanceExperienceTo(experience, log: false);
		}
		using (ContextData<GameLogDisabled>.Request())
		{
			unitEntityData.Descriptor.Replenish();
		}
		data.RecruitedCompanion = unitEntityData;
		using (ContextData<RecruitedUnitData>.Request().Setup(data.RecruitedCompanion))
		{
			OnRecruitImmediate.Run();
		}
		if (data.RecruitedCompanion.Master != null)
		{
			data.RecruitedCompanion.IsInGame = data.RecruitedCompanion.Master.IsInGame;
			using (ContextData<RecruitedUnitData>.Request().Setup(data.RecruitedCompanion))
			{
				OnRecruit.Run();
				return;
			}
		}
		if (!AddToParty)
		{
			player.RemoveCompanion(data.RecruitedCompanion);
		}
	}

	public override string GetCaption()
	{
		RecruitData[] recruited = Recruited;
		if (recruited != null && recruited.Length == 1)
		{
			return $"Recruit ({Recruited[0].CompanionBlueprint})";
		}
		return $"Recruit {Recruited?.Length} people";
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
