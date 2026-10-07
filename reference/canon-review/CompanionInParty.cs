using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence.Versioning;
using Kingmaker.UnitLogic.Parts;
using Owlcat.QA.Validation;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.Designers.EventConditionActionSystem.Conditions;

[ComponentName("Condition/CompanionInParty")]
[AllowMultipleComponents]
[PlayerUpgraderAllowed(false)]
[TypeId("d2f424beb5ace314887e9cc946b68dfa")]
public class CompanionInParty : Condition
{
	[ValidateNotNull]
	[SerializeField]
	[FormerlySerializedAs("companion")]
	private BlueprintUnitReference m_companion;

	public bool MatchWhenActive = true;

	public bool MatchWhenDetached;

	public bool MatchWhenRemote;

	public bool MatchWhenDead;

	public bool MatchWhenEx;

	public BlueprintUnit companion => m_companion?.Get();

	protected override string GetConditionCaption()
	{
		return $"Companion ({companion}) in party";
	}

	protected override bool CheckCondition()
	{
		foreach (UnitEntityData allCharacter in Game.Instance.Player.AllCharacters)
		{
			if (allCharacter.Blueprint == companion || allCharacter.Blueprint.PrototypeLink == companion)
			{
				CompanionState companionState = allCharacter.Get<UnitPartCompanion>()?.State ?? CompanionState.None;
				if ((MatchWhenActive || companionState != CompanionState.InParty) && (MatchWhenRemote || companionState != CompanionState.Remote) && (MatchWhenDetached || companionState != CompanionState.InPartyDetached) && (MatchWhenDead || !allCharacter.Descriptor.State.IsFinallyDead) && (MatchWhenEx || companionState != CompanionState.ExCompanion))
				{
					return true;
				}
			}
		}
		return false;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
