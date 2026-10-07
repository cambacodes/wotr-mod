using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic.Commands.Base;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.UnitLogic.Interaction;

public class SpawnerInteractionDialog : SpawnerInteraction, IDialogReference
{
	[SerializeField]
	[FormerlySerializedAs("Dialog")]
	private BlueprintDialogReference m_Dialog;

	public BlueprintDialog Dialog => m_Dialog?.Get();

	public override UnitCommand.ResultType Interact(UnitEntityData user, UnitEntityData target)
	{
		if (Dialog == null)
		{
			return UnitCommand.ResultType.Success;
		}
		Game.Instance.DialogController.StartDialogWithUnit(Dialog, target, user);
		return UnitCommand.ResultType.Success;
	}

	public DialogReferenceType GetUsagesFor(BlueprintDialog dialog)
	{
		if (Dialog != dialog)
		{
			return DialogReferenceType.None;
		}
		return DialogReferenceType.Start;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
