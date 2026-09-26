using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Designers.EventConditionActionSystem.ContextData;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic.Commands.Base;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.UnitLogic.Interaction;

[ComponentName("Dialog/Start On Click")]
[AllowedOn(typeof(BlueprintUnit), false)]
[TypeId("80cbc40757a76fd41a5e5952e7c7bc3b")]
public class DialogOnClick : UnitInteractionComponent, IDialogReference
{
	[SerializeField]
	[FormerlySerializedAs("Dialog")]
	private BlueprintDialogReference m_Dialog;

	public ActionList NoDialogActions;

	public BlueprintDialog Dialog => m_Dialog?.Get();

	public override bool IsAvailable(UnitEntityData initiator, UnitEntityData target)
	{
		if (!base.IsAvailable(initiator, target))
		{
			return false;
		}
		if (Dialog == null || Dialog.FirstCue.Cues.Count <= 0)
		{
			return NoDialogActions.HasActions;
		}
		return true;
	}

	public override UnitCommand.ResultType Interact(UnitEntityData user, UnitEntityData target)
	{
		if (Dialog == null)
		{
			using (ContextData<ClickedUnitData>.Request().Setup(target))
			{
				NoDialogActions.Run();
			}
			return UnitCommand.ResultType.Fail;
		}
		Game.Instance.DialogController.StartDialogWithUnit(Dialog, target, user);
		return UnitCommand.ResultType.Success;
	}

	public DialogReferenceType GetUsagesFor(BlueprintDialog dialog)
	{
		if (dialog != Dialog)
		{
			return DialogReferenceType.None;
		}
		return DialogReferenceType.Start;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
