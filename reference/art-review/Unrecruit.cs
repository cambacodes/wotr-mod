using System.Linq;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Designers.EventConditionActionSystem.ContextData;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence.Versioning;
using Kingmaker.PubSubSystem;
using Kingmaker.UnitLogic.Parts;
using Kingmaker.Utility;
using UnityEngine;

namespace Kingmaker.Designers.EventConditionActionSystem.Actions;

[ComponentName("Actions/Unrecruit")]
[AllowMultipleComponents]
[PlayerUpgraderAllowed(false)]
[TypeId("7d6c4f7ff596e5e4086531c0f96ac650")]
public class Unrecruit : GameAction
{
	[SerializeField]
	private bool m_UseEvaluator;

	[SerializeReference]
	[ShowIf("m_UseEvaluator")]
	private UnitEvaluator m_CompanionEvaluator;

	[SerializeField]
	[HideIf("m_UseEvaluator")]
	private BlueprintUnitReference m_CompanionBlueprint;

	public ActionList OnUnrecruit;

	public BlueprintUnit CompanionBlueprint
	{
		get
		{
			return m_CompanionBlueprint?.Get();
		}
		set
		{
			m_CompanionBlueprint = value.ToReference<BlueprintUnitReference>();
		}
	}

	public override void RunAction()
	{
		UnitReference mainCharacter = Game.Instance.Player.MainCharacter;
		UnitEntityData companion;
		if (m_UseEvaluator)
		{
			companion = m_CompanionEvaluator.GetValue();
		}
		else
		{
			companion = Game.Instance.Player.AllCharacters.Where((UnitEntityData u) => u != mainCharacter).FirstOrDefault((UnitEntityData unit) => IsCompanion(unit.Blueprint));
		}
		if (companion == null || !companion.Get<UnitPartCompanion>())
		{
			PFLog.Default.Error("No companion unit found when unrecruiting " + (m_UseEvaluator ? m_CompanionEvaluator.GetCaption() : CompanionBlueprint.ToString()));
			return;
		}
		DoUnrecruit(companion);
		EventBus.RaiseEvent(delegate(ICompanionChangeHandler h)
		{
			h.HandleUnrecruit(companion);
		});
	}

	private void DoUnrecruit(UnitEntityData companion)
	{
		UnitPartCompanion unitPartCompanion = companion.Get<UnitPartCompanion>();
		if (unitPartCompanion != null && unitPartCompanion.State == CompanionState.ExCompanion)
		{
			PFLog.Default.Error($"Companion {companion} already lost, cannot unrecruit again.");
		}
		if ((bool)companion.View)
		{
			companion.View.StopMoving();
		}
		Game.Instance.Player.RemoveCompanion(companion);
		companion.Ensure<UnitPartCompanion>().SetState(CompanionState.ExCompanion);
		using (ContextData<RecruitedUnitData>.Request().Setup(companion))
		{
			OnUnrecruit?.Run();
		}
	}

	private bool IsCompanion(BlueprintUnit unit)
	{
		return unit == CompanionBlueprint;
	}

	public override string GetCaption()
	{
		return $"Unrecruit ({CompanionBlueprint})";
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
