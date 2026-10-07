using System.Collections.Generic;
using System.Linq;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Area;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Controllers.Dialog;
using Owlcat.QA.Validation;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.DialogSystem.Blueprints;

[TypeId("eea0d7fdafd8fe047a81a3208e5ed9ab")]
public class BlueprintCueSequence : BlueprintCueBase
{
	public List<BlueprintCueBaseReference> Cues = new List<BlueprintCueBaseReference>();

	[SerializeField]
	[FormerlySerializedAs("Exit")]
	private BlueprintSequenceExitReference m_Exit;

	public BlueprintSequenceExit Exit => m_Exit?.Get();

	public override bool CanShow()
	{
		if (!base.CanShow())
		{
			return false;
		}
		if (!Cues.Where((BlueprintCueBaseReference cue) => !cue.IsEmpty()).Any((BlueprintCueBaseReference cue) => cue.Get().CanShow()))
		{
			DialogDebug.Add(this, "no valid cues", Color.red);
			return false;
		}
		return true;
	}

	public override void Validate(ValidationContext context, int parentIndex)
	{
		base.Validate(context, parentIndex);
		Stack<SimpleBlueprint> stack = new Stack<SimpleBlueprint>();
		HashSet<SimpleBlueprint> hashSet = new HashSet<SimpleBlueprint>();
		foreach (BlueprintCueBaseReference cue in Cues)
		{
			if (cue.GetBlueprint() is BlueprintCueSequence blueprintCueSequence)
			{
				int currentIndex = context.CreateChild(blueprintCueSequence.name, ValidationNodeType.Object, parentIndex).CurrentIndex;
				blueprintCueSequence.Validate(context, currentIndex);
			}
			else
			{
				stack.Push((BlueprintCueBase)cue);
			}
		}
		stack.Push(Exit);
		while (stack.Count > 0)
		{
			SimpleBlueprint simpleBlueprint = stack.Pop();
			if (hashSet.Contains(simpleBlueprint))
			{
				continue;
			}
			if (!(simpleBlueprint is BlueprintAnswer blueprintAnswer))
			{
				if (!(simpleBlueprint is BlueprintAnswersList blueprintAnswersList))
				{
					if (!(simpleBlueprint is BlueprintCueSequence blueprintCueSequence2))
					{
						if (simpleBlueprint is BlueprintCue blueprintCue)
						{
							foreach (BlueprintAnswerBaseReference answer in blueprintCue.Answers)
							{
								stack.Push((BlueprintAnswerBase)answer);
							}
							if (blueprintCue.Continue?.Cues != null && blueprintCue.Continue.Cues.Count >= 1)
							{
								foreach (BlueprintCueBaseReference cue2 in blueprintCue.Continue.Cues)
								{
									stack.Push((BlueprintCueBase)cue2);
								}
							}
						}
					}
					else
					{
						blueprintCueSequence2.Validate(context, parentIndex);
					}
				}
				else
				{
					foreach (BlueprintAnswerBaseReference answer2 in blueprintAnswersList.Answers)
					{
						stack.Push((BlueprintAnswerBase)answer2);
					}
				}
			}
			else if (blueprintAnswer.NextCue == null)
			{
				context.AddError(ErrorLevel.Critical, BlueprintArea.Designers.AlexanderKomzolov.GetEnumDescription(), "Answer " + blueprintAnswer.NameSafe() + " NextCue is null!");
			}
			else if (blueprintAnswer.NextCue.Cues == null || !blueprintAnswer.NextCue.Cues.Any((BlueprintCueBaseReference x) => x != null && x.Get() != null))
			{
				context.AddError(ErrorLevel.Critical, BlueprintArea.Designers.AlexanderKomzolov.GetEnumDescription(), "Answer " + blueprintAnswer.NameSafe() + " NextCue Cues is null or empty!");
			}
			hashSet.Add(simpleBlueprint);
		}
	}
}
