using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence.Versioning;
using Kingmaker.Localization;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.Designers.EventConditionActionSystem.Actions;

[ComponentName("Actions/StartDialog")]
[AllowMultipleComponents]
[TypeId("0e0c1fe99d7862d4492bcd1535939a9a")]
[PlayerUpgraderAllowed(false)]
public class StartDialog : GameAction, IDialogReference
{
	[Tooltip("Unit with BlueprintDialog. If unit have no BlueprintDialog or Null - Dialog from field 'Dialog' will be used.")]
	[SerializeReference]
	public UnitEvaluator DialogueOwner;

	[Tooltip("This dialog overrides dialog in 'Dialogue Owner' if it exists")]
	[SerializeField]
	[FormerlySerializedAs("Dialogue")]
	private BlueprintDialogReference m_Dialogue;

	[Tooltip("Evaluator. Works if Dialogue is null")]
	[SerializeReference]
	public BlueprintEvaluator DialogEvaluator;

	[Tooltip("Interlocutor name. Uses only if 'Dialogue Owner' is Null")]
	public LocalizedString SpeakerName;

	public BlueprintDialog Dialogue => m_Dialogue?.Get();

	public override void RunAction()
	{
		BlueprintDialog blueprintDialog = (Dialogue ? Dialogue : (DialogEvaluator ? ((BlueprintDialog)DialogEvaluator.GetValue()) : null));
		if (DialogueOwner != null)
		{
			UnitEntityData value = DialogueOwner.GetValue();
			StartDialog component = value.Blueprint.GetComponent<StartDialog>();
			BlueprintDialog blueprintDialog2 = ((component != null) ? component.Dialogue : blueprintDialog);
			if ((bool)blueprintDialog2)
			{
				Game.Instance.DialogController.StartDialogWithUnit(blueprintDialog2, value);
			}
		}
		else if ((bool)blueprintDialog)
		{
			Game.Instance.DialogController.StartDialogWithoutTarget(blueprintDialog, SpeakerName);
		}
	}

	public override string GetCaption()
	{
		return string.Format("Start Dialog ({0})", Dialogue ? Dialogue.NameSafe() : (DialogEvaluator ? DialogEvaluator.GetCaption() : (DialogueOwner ? DialogueOwner.GetCaption() : "??")));
	}

	public DialogReferenceType GetUsagesFor(BlueprintDialog dialog)
	{
		if (dialog != Dialogue)
		{
			return DialogReferenceType.None;
		}
		return DialogReferenceType.Start;
	}
}
