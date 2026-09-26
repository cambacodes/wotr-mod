using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Persistence.Versioning;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.Assets.Designers.EventConditionActionSystem.Conditions;

[PlayerUpgraderAllowed(false)]
[TypeId("34f02a2ceadc2e442bdf2bfe54478571")]
public class DialogSeen : Condition
{
	[SerializeField]
	[FormerlySerializedAs("Dialog")]
	private BlueprintDialogReference m_Dialog;

	public BlueprintDialog Dialog => m_Dialog?.Get();

	protected override string GetConditionCaption()
	{
		return $"Dialog Seen ({Dialog})";
	}

	protected override bool CheckCondition()
	{
		return Game.Instance.Player.Dialog.ShownDialogs.Contains(Dialog);
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
