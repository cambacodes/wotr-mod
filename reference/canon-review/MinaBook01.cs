using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;

namespace RanRomance.Mina;

public class MinaBook01
{
	private static readonly string BookName = "RanRomMinaBook01";

	public static string Configure()
	{
		//IL_0122: Unknown result type (might be due to invalid IL or missing references)
		//IL_0129: Expected O, but got Unknown
		//IL_0129: Unknown result type (might be due to invalid IL or missing references)
		//IL_0130: Expected O, but got Unknown
		//IL_013c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0141: Unknown result type (might be due to invalid IL or missing references)
		//IL_0158: Unknown result type (might be due to invalid IL or missing references)
		string text = "91a3699b2b12496db23b33dad6746d31";
		MinaBook01End.Configure();
		MinaBook01Page005.Configure();
		MinaBook01Page004.Configure();
		MinaBook01Page003.Configure();
		MinaBook01Page002.Configure();
		MinaBook01Page001.Configure();
		ActionsBuilder startActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("2da74626a86ff364f84bca24ba01662e").StartActions.Actions[0]);
		ConditionsBuilder conditions = ConditionsBuilder.New();
		ActionsBuilder ifTrue = ActionsBuilder.New().StartEtude("faad12cd8c8048309acb37896d8fafc3");
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected("a08540bf69314cffb24d93d277cf6636").EtudeStatus(null, null, "1d466fd4271fdc14ea1c077760c63ca5", negate: true, null, true);
		ActionsBuilder finishActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("c589bdbed55b538449b02711d1a86aa3").FinishActions.Actions[0]).Conditional(conditions, ifTrue)
			.Conditional(conditions2, ActionsBuilder.New().StartEtude("1d466fd4271fdc14ea1c077760c63ca5"));
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomMinaBook01Page001")).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		DialogConfigurator.New(BookName, text).SetStartActions(startActions).SetFinishActions(finishActions)
			.SetFirstCue(val)
			.SetType((DialogType)3)
			.SetTurnFirstSpeaker(turnFirstSpeaker: false)
			.SetTurnPlayer(turnPlayer: false)
			.SetIsLockCameraRotationButtons(isLockCameraRotationButtons: false)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
