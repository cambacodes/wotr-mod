using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence.Versioning;
using Kingmaker.UnitLogic.Parts;
using Kingmaker.Utility;
using Kingmaker.View;
using Owlcat.QA.Validation;
using UnityEngine;

namespace Kingmaker.Designers.EventConditionActionSystem.Actions;

[TypeId("0edf8920d3df9b54c9db189bdad67cac")]
[PlayerUpgraderAllowed(true)]
public class HideUnit : GameAction
{
	[ValidateNotNull]
	[SerializeReference]
	public UnitEvaluator Target;

	public bool Unhide;

	[HideIf("Unhide")]
	public bool Fade;

	[HideIf("Unhide")]
	[Header("Set if there can be a save game while the character is disabled")]
	public bool SetHideInSaves;

	public override string GetDescription()
	{
		return string.Format("{0} ????? {1}", Unhide ? "?????????? " : "??????", Target);
	}

	public override string GetCaption()
	{
		return (Unhide ? "Show " : "Hide") + Target?.GetCaption();
	}

	public override void RunAction()
	{
		UnitEntityData value = Target.GetValue();
		if (Unhide)
		{
			UnitPartPet unitPartPet = value.Get<UnitPartPet>();
			if (unitPartPet == null || !unitPartPet.ShouldBeHidden)
			{
				value.IsInGame = true;
			}
			return;
		}
		if (Fade)
		{
			UnitEntityView view = value.View;
			value.Commands.InterruptAll();
			view.FadeHide();
			value.IsInGame = false;
		}
		else
		{
			value.IsInGame = false;
		}
		if (SetHideInSaves)
		{
			UnitPartCompanion unitPartCompanion = value.Get<UnitPartCompanion>();
			if (unitPartCompanion != null)
			{
				unitPartCompanion.IsIgnoreFixInGame = true;
			}
		}
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
