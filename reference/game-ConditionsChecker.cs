using System;
using JetBrains.Annotations;
using Kingmaker.QA;
using Kingmaker.Utility;
using Owlcat.QA.Validation;
using UnityEngine;

namespace Kingmaker.ElementsSystem;

[Serializable]
public class ConditionsChecker : IValidated
{
	public Operation Operation;

	[SerializeReference]
	[Hide]
	public Condition[] Conditions;

	public bool HasConditions
	{
		get
		{
			if (Conditions != null)
			{
				return Conditions.Length != 0;
			}
			return false;
		}
	}

	public bool Check()
	{
		return Check(null);
	}

	public bool Check([CanBeNull] IConditionDebugContext debugContext)
	{
		if (!HasConditions)
		{
			return true;
		}
		Condition[] conditions = Conditions;
		foreach (Condition condition in conditions)
		{
			if (condition == null)
			{
				continue;
			}
			try
			{
				using (ProfileScope.New("Check Condition"))
				{
					using ElementsDebugScope elementsDebugScope = ElementsDebugScope.Open(condition);
					bool flag = condition.Check(debugContext);
					elementsDebugScope?.SetState(flag);
					if (Operation == Operation.And && !flag)
					{
						return false;
					}
					if (Operation == Operation.Or && flag)
					{
						return true;
					}
				}
			}
			catch (Exception ex)
			{
				if (!(ex is ElementLogicException))
				{
					ex = new ElementLogicException(condition, ex);
				}
				PFLog.Actions.ExceptionWithReport(ex, null);
				return false;
			}
		}
		return Operation == Operation.And;
	}

	public void Validate(ValidationContext context, int parentIndex)
	{
	}
}
