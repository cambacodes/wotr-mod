using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Area;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Stats;
using Kingmaker.QA;
using Owlcat.QA.Validation;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.DialogSystem.Blueprints;

[TypeId("ab803aaa7a173f84e9172870c15e7493")]
public class BlueprintCheck : BlueprintCueBase
{
	public StatType Type;

	public int DC;

	public bool Hidden;

	public DCModifier[] DCModifiers = new DCModifier[0];

	public bool BanPartyCheckInCamp;

	[SerializeField]
	[FormerlySerializedAs("Success")]
	private BlueprintCueBaseReference m_Success;

	[SerializeField]
	[FormerlySerializedAs("Fail")]
	private BlueprintCueBaseReference m_Fail;

	[SerializeField]
	[SerializeReference]
	private UnitEvaluator m_UnitEvaluator;

	public DialogExperience Experience = DialogExperience.NormalExperience;

	public BlueprintCueBase Success => m_Success?.Get();

	public BlueprintCueBase Fail => m_Fail?.Get();

	public int GetDC()
	{
		int num = DC;
		if (DCModifiers != null)
		{
			DCModifier[] dCModifiers = DCModifiers;
			foreach (DCModifier dCModifier in dCModifiers)
			{
				if (dCModifier != null && dCModifier.Conditions != null && dCModifier.Conditions.Check())
				{
					num += dCModifier.Mod;
				}
			}
		}
		return num;
	}

	protected override void ApplyValidation(ValidationContext context, int parentIndex)
	{
		base.ApplyValidation(context, parentIndex);
		if (Type == StatType.SkillPersuasion)
		{
			context.AddError(ErrorLevel.Normal, BlueprintArea.Designers.EugeneSanin.GetEnumDescription(), $"Using {StatType.SkillPersuasion} in a check. " + "Consider using " + $"{StatType.CheckDiplomacy}, " + $"{StatType.CheckBluff} or " + $"{StatType.CheckIntimidate} instead.");
		}
		if (Success == null)
		{
			context.AddError(ErrorLevel.Normal, BlueprintArea.Designers.EugeneSanin.GetEnumDescription(), $"BlueprintCheck {this} has empty Success field");
		}
		if (Fail == null)
		{
			context.AddError(ErrorLevel.Normal, BlueprintArea.Designers.EugeneSanin.GetEnumDescription(), $"BlueprintCheck {this} has empty Fail field");
		}
	}

	public UnitEntityData GetTargetUnit()
	{
		UnitEntityData value = null;
		if (m_UnitEvaluator != null && !m_UnitEvaluator.TryGetValue(out value))
		{
			PFLog.Default.ErrorWithReport(" BlueprintCheck {0}, AssetGUID {1}: Unit specifed but not found.", name, AssetGuid);
		}
		return value;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
