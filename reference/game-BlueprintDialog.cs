using System.Collections.Generic;
using JetBrains.Annotations;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Controllers.Dialog;
using Kingmaker.ElementsSystem;
using Owlcat.QA.Validation;
using UnityEngine;

namespace Kingmaker.DialogSystem.Blueprints;

[NonOverridable]
[TypeId("c8ff73feae580b142a9f43e0c61d7f32")]
public class BlueprintDialog : BlueprintScriptableObject, IConditionDebugContext
{
	public CueSelection FirstCue;

	[CanBeNull]
	[SerializeReference]
	public PositionEvaluator StartPosition;

	public ConditionsChecker Conditions = new ConditionsChecker();

	public ActionList StartActions = new ActionList();

	public ActionList FinishActions = new ActionList();

	public ActionList ReplaceActions = new ActionList();

	public bool TurnPlayer = true;

	public bool TurnFirstSpeaker = true;

	[Tooltip("\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\ufffd \ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd")]
	public bool IsLockCameraRotationButtons;

	public DialogType Type;

	[CanBeNull]
	[SerializeField]
	[SerializeReference]
	[Tooltip("Override zone CR")]
	private IntEvaluator m_OverrideAreaCR;

	public IntEvaluator OverrideAreaCR => m_OverrideAreaCR;

	[NotNull]
	public BlueprintAnswer GetContinueAnswer()
	{
		if (Type != DialogType.Common && Type != DialogType.Book)
		{
			return Game.Instance.BlueprintRoot.Dialog.InterchapterContinueAnswer;
		}
		return Game.Instance.BlueprintRoot.Dialog.ContinueAnswer;
	}

	[NotNull]
	public BlueprintAnswer GetExitAnswer()
	{
		if (Type != DialogType.Common && Type != DialogType.Book)
		{
			return Game.Instance.BlueprintRoot.Dialog.InterchapterExitAnswer;
		}
		return Game.Instance.BlueprintRoot.Dialog.ExitAnswer;
	}

	public void AddConditionDebugMessage(string message, Color color)
	{
		DialogDebug.Add(this, message, color);
	}

	public override void Validate(ValidationContext context, int parentIndex)
	{
		base.Validate(context, parentIndex);
		if (FirstCue == null)
		{
			return;
		}
		Stack<SimpleBlueprint> stack = new Stack<SimpleBlueprint>();
		HashSet<SimpleBlueprint> hashSet = new HashSet<SimpleBlueprint>();
		foreach (BlueprintCueBaseReference cue in FirstCue.Cues)
		{
			try
			{
				if (cue.Get() is BlueprintCue item)
				{
					stack.Push(item);
				}
				else if (cue.Get() is BlueprintCueSequence blueprintCueSequence)
				{
					int currentIndex = context.CreateChild(blueprintCueSequence.name, ValidationNodeType.Object, parentIndex).CurrentIndex;
					blueprintCueSequence.Validate(context, currentIndex);
				}
			}
			catch
			{
			}
		}
		while (stack.Count > 0)
		{
			SimpleBlueprint simpleBlueprint = stack.Pop();
			if (hashSet.Contains(simpleBlueprint))
			{
				continue;
			}
			if (!(simpleBlueprint is BlueprintCueSequence blueprintCueSequence2))
			{
				if (simpleBlueprint is BlueprintCue blueprintCue && blueprintCue.Continue?.Cues != null && blueprintCue.Continue.Cues.Count >= 1)
				{
					foreach (BlueprintCueBaseReference cue2 in blueprintCue.Continue.Cues)
					{
						stack.Push((BlueprintCueBase)cue2);
					}
				}
			}
			else
			{
				blueprintCueSequence2.Validate(context, parentIndex);
			}
			hashSet.Add(simpleBlueprint);
		}
	}
}
