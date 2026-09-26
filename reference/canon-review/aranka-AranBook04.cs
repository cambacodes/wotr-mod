using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.Designers.Quests.Common;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;

namespace RanRomance.Aran;

public class AranBook04
{
	private static readonly string BookName = "RanRomAranBook04";

	public static string Configure()
	{
		//IL_00a4: Unknown result type (might be due to invalid IL or missing references)
		//IL_00aa: Expected O, but got Unknown
		//IL_00aa: Unknown result type (might be due to invalid IL or missing references)
		//IL_00b1: Expected O, but got Unknown
		//IL_00bd: Unknown result type (might be due to invalid IL or missing references)
		//IL_00c2: Unknown result type (might be due to invalid IL or missing references)
		//IL_00d7: Unknown result type (might be due to invalid IL or missing references)
		string text = "14ffcdd473704e5dbc8cfe5f98b582b8";
		AranBook04End.Configure();
		AranBook04Azata.Configure();
		AranBook04Page008.Configure();
		AranBook04Page007.Configure();
		AranBook04Page006.Configure();
		AranBook04Page005.Configure();
		AranBook04Page004.Configure();
		AranBook04Page003.Configure();
		AranBook04Page002.Configure();
		AranBook04Page001.Configure();
		ActionsBuilder startActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("6b42e534fad5e6347838bf9746190740").StartActions.Actions[0]);
		ActionsBuilder finishActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("6b42e534fad5e6347838bf9746190740").FinishActions.Actions[0]).SetObjectiveStatus("RanRomAranQuestEntry0003", null, (ObjectiveStatus)0);
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Page001")).deserializedGuid;
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
