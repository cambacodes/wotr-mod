using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Persistence.Versioning;
using Owlcat.QA.Validation;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.Designers.EventConditionActionSystem.Conditions;

[TypeId("ea981728db8a5f84888ecba390671a05")]
[PlayerUpgraderAllowed(false)]
public class EtudeStatus : Condition, IEtudeReference
{
	[ValidateNotNull]
	[SerializeField]
	[FormerlySerializedAs("Etude")]
	private BlueprintEtudeReference m_Etude;

	public bool NotStarted;

	public bool Started;

	public bool Playing;

	public bool CompletionInProgress;

	public bool Completed;

	public BlueprintEtude Etude
	{
		get
		{
			return m_Etude?.Get();
		}
		set
		{
			m_Etude = SimpleBlueprintExtendAsObject.Or(value, null)?.ToReference<BlueprintEtudeReference>();
		}
	}

	public override string GetDescription()
	{
		return "NotStarted - ???? ??????? ?? ?????????, Started - ???? ??????????, ???????????? ? ?? ??? ?? ???????????, Playing - ???????? ? ?????? ?????? ????";
	}

	protected override string GetConditionCaption()
	{
		return string.Format("Etude {0} status is: {1} {2} {3} {4} {5} ", Etude, NotStarted ? "NotStarted;" : "", Started ? "Started;" : "", Playing ? "Playing;" : "", CompletionInProgress ? "CompletionInProgress;" : "", Completed ? "Completed;" : "");
	}

	protected override bool CheckCondition()
	{
		if (Game.Instance.Player.EtudesSystem.EtudeIsNotStarted(Etude))
		{
			return NotStarted;
		}
		if (Game.Instance.Player.EtudesSystem.EtudeIsCompleted(Etude))
		{
			return Completed;
		}
		Etude fact = Game.Instance.Player.EtudesSystem.Etudes.GetFact(Etude);
		if (fact == null || (!fact.IsPlaying && !fact.CompletionInProgress))
		{
			return Started;
		}
		if (fact.CompletionInProgress)
		{
			if (!CompletionInProgress)
			{
				return Started;
			}
			return true;
		}
		if (fact.IsPlaying)
		{
			if (!Playing)
			{
				return Started;
			}
			return true;
		}
		return false;
	}

	public EtudeReferenceType GetUsagesFor(BlueprintEtude f)
	{
		if (Etude != f)
		{
			return EtudeReferenceType.None;
		}
		return EtudeReferenceType.Check;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
