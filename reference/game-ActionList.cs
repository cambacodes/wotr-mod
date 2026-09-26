using System;
using System.Linq;
using Kingmaker.QA;
using Kingmaker.Utility;
using UnityEngine;

namespace Kingmaker.ElementsSystem;

[Serializable]
public class ActionList
{
	[SerializeReference]
	[Hide]
	public GameAction[] Actions = new GameAction[0];

	public bool HasActions
	{
		get
		{
			if (Actions != null)
			{
				return Actions.Length != 0;
			}
			return false;
		}
	}

	public ActionList()
	{
	}

	public ActionList(ActionList source1, ActionList source2)
	{
		if (source1 != null && source2 != null)
		{
			Actions = source1.Actions.Concat(source2.Actions).ToArray();
			return;
		}
		if (source1 != null)
		{
			Actions = source1.Actions;
		}
		if (source2 != null)
		{
			Actions = source2.Actions;
		}
	}

	public void Run()
	{
		GameAction[] actions = Actions;
		foreach (GameAction gameAction in actions)
		{
			if (gameAction == null)
			{
				continue;
			}
			try
			{
				using (ElementsDebugScope.Open(gameAction))
				{
					gameAction.RunAction();
				}
			}
			catch (Exception ex)
			{
				ElementLogicException exception = (ex as ElementLogicException) ?? new ElementLogicException(gameAction, ex);
				PFLog.Actions.ExceptionWithReport(exception, null);
			}
			finally
			{
			}
		}
	}
}
