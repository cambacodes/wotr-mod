using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.Designers.Quests.Common;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;

namespace RanRomance.Aran;

public class AranBook14
{
	private static readonly string BookName = "RanRomAranBook14";

	public static string Configure()
	{
		//IL_0086: Unknown result type (might be due to invalid IL or missing references)
		//IL_008c: Expected O, but got Unknown
		//IL_008c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0093: Expected O, but got Unknown
		//IL_009f: Unknown result type (might be due to invalid IL or missing references)
		//IL_00a4: Unknown result type (might be due to invalid IL or missing references)
		//IL_00b9: Unknown result type (might be due to invalid IL or missing references)
		string text = "1650593635d947f0b28fc1900b10d4d6";
		AranBook14End.Configure();
		AranBook14Page004.Configure();
		AranBook14Page003.Configure();
		AranBook14Page002.Configure();
		AranBook14Page001.Configure();
		ActionsBuilder startActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("6b42e534fad5e6347838bf9746190740").StartActions.Actions[0]);
		ActionsBuilder finishActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("6b42e534fad5e6347838bf9746190740").FinishActions.Actions[0]).SetObjectiveStatus("RanRomAranQuestEntry0004", null, (ObjectiveStatus)0);
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook14Page001")).deserializedGuid;
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
