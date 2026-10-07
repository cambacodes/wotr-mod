using System.Collections.Generic;
using JetBrains.Annotations;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Controllers.Dialog;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.DialogSystem.State;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.EntitySystem.Stats;
using Kingmaker.Localization;
using Kingmaker.RuleSystem;
using Kingmaker.RuleSystem.Rules;
using Kingmaker.UnitLogic.Alignments;
using Kingmaker.Utility;
using Owlcat.QA.Validation;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.DialogSystem.Blueprints;

[TypeId("df78945bb9f434e40b897758499cb714")]
public class BlueprintAnswer : BlueprintAnswerBase, IAlignmentShiftProvider
{
	public LocalizedString Text;

	public CueSelection NextCue;

	public bool ShowOnce;

	[ShowIf("ShowOnce")]
	public bool ShowOnceCurrentDialog;

	public ShowCheck ShowCheck;

	public DialogExperience Experience;

	public bool DebugMode;

	public CharacterSelection CharacterSelection;

	public ConditionsChecker ShowConditions;

	public ConditionsChecker SelectConditions;

	[Tooltip("Show this answer only if it is followed by a valid cue.")]
	public bool RequireValidCue;

	public bool AddToHistory = true;

	public ActionList OnSelect;

	[FormerlySerializedAs("CustomChecks")]
	[Tooltip("Show this check on answer in dialog interface. Instead of check calculated from BlueprintCheck node.")]
	public CheckData[] FakeChecks;

	[NotNull]
	public AlignmentShift AlignmentShift = new AlignmentShift();

	public string DisplayText => Text;

	public bool HasShowCheck => ShowCheck.Type != StatType.Unknown;

	public bool CapitalPartyChecksEnabled
	{
		get
		{
			CharacterSelection characterSelection = CharacterSelection;
			if (characterSelection == null || characterSelection.SelectionType != CharacterSelection.Type.Capital)
			{
				CharacterSelection characterSelection2 = CharacterSelection;
				if (characterSelection2 != null && characterSelection2.SelectionType == CharacterSelection.Type.Clear)
				{
					return Game.Instance.Player.CapitalPartyMode;
				}
				return false;
			}
			return true;
		}
	}

	AlignmentShift IAlignmentShiftProvider.AlignmentShift => AlignmentShift;

	public List<SkillCheckDC> SkillChecksDC
	{
		get
		{
			List<SkillCheckDC> list = new List<SkillCheckDC>();
			UnitEntityData unitEntityData = CharacterSelection.SelectUnit(this, Game.Instance.Player.MainCharacter);
			foreach (BlueprintCueBase item2 in NextCue.Cues.Dereference())
			{
				if (item2 is BlueprintCheck { Hidden: false } blueprintCheck)
				{
					UnitEntityData unitEntityData2 = blueprintCheck.GetTargetUnit() ?? unitEntityData;
					if (unitEntityData2 != null)
					{
						RuleStatCheck ruleStatCheck = RuleStatCheck.Create(unitEntityData2, blueprintCheck.Type, blueprintCheck.GetDC());
						ruleStatCheck.Calculate();
						SkillCheckDC item = new SkillCheckDC(unitEntityData2, ruleStatCheck.StatType, ruleStatCheck.NonNegativeDC, ruleStatCheck.StatValue, isBest: false);
						list.Add(item);
					}
					else
					{
						RulePartyStatCheck rulePartyStatCheck = new RulePartyStatCheck(blueprintCheck.Type, blueprintCheck.GetDC(), CapitalPartyChecksEnabled);
						rulePartyStatCheck.Calculate();
						list.Add(new SkillCheckDC(rulePartyStatCheck.Roller, rulePartyStatCheck.StatType, rulePartyStatCheck.NonNegativeDC, rulePartyStatCheck.StatValue, isBest: true));
					}
				}
			}
			return list;
		}
	}

	public bool CanShow()
	{
		DialogState dialog = Game.Instance.Player.Dialog;
		DialogController dialogController = Game.Instance.DialogController;
		if (DebugMode && !Debug.isDebugBuild)
		{
			DialogDebug.Add(this, "not in debug build", Color.red);
			return false;
		}
		if (ShowOnce)
		{
			if (ShowOnceCurrentDialog)
			{
				if (dialogController.LocalSelectedAnswers.Contains(this))
				{
					DialogDebug.Add(this, "(show once) was selected before (in current dialog)", Color.red);
					return false;
				}
			}
			else if (dialog.SelectedAnswers.Contains(this))
			{
				DialogDebug.Add(this, "(show once) was selected before (global)", Color.red);
				return false;
			}
		}
		if (HasShowCheck)
		{
			if (dialog.AnswerChecks.TryGetValue(this, out var value))
			{
				if (value == CheckResult.Failed)
				{
					DialogDebug.Add(this, "check failed (before)", Color.red);
					return false;
				}
			}
			else
			{
				RulePartyStatCheck evt = new RulePartyStatCheck(ShowCheck.Type, ShowCheck.DC, CapitalPartyChecksEnabled);
				evt = Rulebook.Trigger(evt);
				dialog.AnswerChecks[this] = ((!evt.Success) ? CheckResult.Failed : CheckResult.Passed);
				if (!evt.Success)
				{
					DialogDebug.Add(this, "check failed", Color.red);
					return false;
				}
			}
		}
		if (RequireValidCue && NextCue.Select() == null)
		{
			DialogDebug.Add(this, "no valid cue following", Color.red);
			return false;
		}
		if (!ShowConditions.Check(this))
		{
			DialogDebug.Add(this, "conditions failed", Color.red);
			return false;
		}
		DialogDebug.Add(this, "answer shown", Color.green);
		return true;
	}

	public bool CanSelect()
	{
		if (base.IsAlignmentRequirementSatisfied && base.IsMythicRequirementSatisfied)
		{
			return SelectConditions.Check();
		}
		return false;
	}

	public bool IsAlreadySelected()
	{
		return Game.Instance.Player.Dialog.SelectedAnswers.Contains(this);
	}

	public bool IsNewAndCanShowAndCanSelect()
	{
		if (!Game.Instance.Player.Dialog.SelectedAnswers.Contains(this) && CanShow())
		{
			return CanSelect();
		}
		return false;
	}

	protected override void ApplyValidation(ValidationContext context, int parentIndex)
	{
		base.ApplyValidation(context, parentIndex);
		if (CharacterSelection.SelectionType == CharacterSelection.Type.Companion && this.GetComponent<ActingCompanion>() == null)
		{
			context.AddError("You should add ActingCompanion component when using CharacterSelection type Companion");
		}
		ApplyValidationTeleportParty(context, OnSelect, "OnSelect");
	}

	private void ApplyValidationTeleportParty(ValidationContext context, ActionList actionList, string path)
	{
		if (!actionList.HasActions)
		{
			return;
		}
		GameAction[] actions = actionList.Actions;
		foreach (GameAction obj in actions)
		{
			if (obj is TeleportParty { AutoSaveMode: AutoSaveMode.BeforeExit } teleportParty)
			{
				context.AddError($"Teleport party in {path} is set to AutoSaveMode.{teleportParty.AutoSaveMode}");
			}
			if (obj is Conditional conditional)
			{
				ApplyValidationTeleportParty(context, conditional.IfTrue, path + ".IfTrue");
				ApplyValidationTeleportParty(context, conditional.IfFalse, path + ".IfFalse");
			}
		}
	}
}
