using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Blueprints.Root;
using Kingmaker.Controllers.Dialog;
using Kingmaker.ElementsSystem;
using Kingmaker.Enums;
using UnityEngine;

namespace Kingmaker.DialogSystem.Blueprints;

[NonOverridable]
[TypeId("e29428d274948784bb31643317d419ba")]
public abstract class BlueprintAnswerBase : BlueprintScriptableObject, IConditionDebugContext
{
	public Mythic MythicRequirement;

	public AlignmentComponent AlignmentRequirement;

	public bool IsMythicRequirementSatisfied
	{
		get
		{
			if (MythicRequirement != Mythic.None)
			{
				return BlueprintRoot.Instance.MythicsSettings.IsMythicsSatisfied(MythicRequirement);
			}
			return true;
		}
	}

	public bool IsAlignmentRequirementSatisfied => Game.Instance.Player.Alignment.HasComponent(AlignmentRequirement);

	public void AddConditionDebugMessage(string message, Color color)
	{
		DialogDebug.Add(this, message, color);
	}
}
