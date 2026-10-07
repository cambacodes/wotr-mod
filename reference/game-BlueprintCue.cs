using System.Collections.Generic;
using JetBrains.Annotations;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Controllers.Dialog;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.Localization;
using Kingmaker.UnitLogic.Alignments;
using Owlcat.QA.Validation;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.DialogSystem.Blueprints;

[TypeId("8eee9d45ddcfa614d99610c1892993e3")]
public class BlueprintCue : BlueprintCueBase, IAlignmentShiftProvider
{
	public LocalizedString Text;

	public DialogExperience Experience;

	public DialogSpeaker Speaker;

	public bool TurnSpeaker = true;

	public DialogAnimation Animation;

	[CanBeNull]
	[Tooltip("Listener portrait (main character by default)")]
	[SerializeField]
	[FormerlySerializedAs("Listener")]
	private BlueprintUnitReference m_Listener;

	public ActionList OnShow;

	public ActionList OnStop;

	[NotNull]
	public AlignmentShift AlignmentShift = new AlignmentShift();

	public List<BlueprintAnswerBaseReference> Answers = new List<BlueprintAnswerBaseReference>();

	public CueSelection Continue;

	public string DisplayText => Text;

	public BlueprintUnit Listener => m_Listener?.Get();

	AlignmentShift IAlignmentShiftProvider.AlignmentShift => AlignmentShift;

	public override bool CanShow()
	{
		if (!base.CanShow())
		{
			return false;
		}
		if (DialogController.IgnoreRequiredSpeakers)
		{
			return true;
		}
		if (Speaker.NeedsEntity && Speaker.GetEntity(this) == null)
		{
			return false;
		}
		return true;
	}

	public bool HasNewAnswers()
	{
		if (!Game.Instance.Player.Dialog.ShownCues.Contains(this) && CanShow())
		{
			return true;
		}
		foreach (BlueprintAnswerBaseReference answer in Answers)
		{
			BlueprintAnswerBase blueprintAnswerBase = answer?.Get();
			if (blueprintAnswerBase != null)
			{
				if (blueprintAnswerBase is BlueprintAnswer blueprintAnswer && blueprintAnswer.IsNewAndCanShowAndCanSelect())
				{
					return true;
				}
				if (blueprintAnswerBase is BlueprintAnswersList blueprintAnswersList && blueprintAnswersList.HasNewAnswers())
				{
					return true;
				}
			}
		}
		return false;
	}

	protected override void ApplyValidation(ValidationContext context, int parentIndex)
	{
		base.ApplyValidation(context, parentIndex);
		ApplyValidationTeleportParty(context, OnStop, "OnStop");
		ApplyValidationTeleportParty(context, OnShow, "OnShow");
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

	public VoiceOverStatus PlayVoiceOver()
	{
		return Text.PlayVoiceOver();
	}
}
