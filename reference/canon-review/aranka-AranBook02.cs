using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.AreaEx;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Blueprints.Configurators.RandomEncounters;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.Designers.Quests.Common;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;

namespace RanRomance.Aran;

public class AranBook02
{
	private static readonly string BookName = "RanRomAranBook02";

	public static string Configure()
	{
		//IL_0007: Unknown result type (might be due to invalid IL or missing references)
		//IL_000d: Expected O, but got Unknown
		//IL_0185: Unknown result type (might be due to invalid IL or missing references)
		//IL_018c: Expected O, but got Unknown
		//IL_018c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0193: Expected O, but got Unknown
		//IL_019f: Unknown result type (might be due to invalid IL or missing references)
		//IL_01a4: Unknown result type (might be due to invalid IL or missing references)
		//IL_01bb: Unknown result type (might be due to invalid IL or missing references)
		string text = "b9068ea8642f4c9da4a338ebd5ba316f";
		PlayerCharacter val = new PlayerCharacter();
		((Element)val).name = "pc" + text;
		AranBook02End.Configure();
		AranBook02Page004.Configure();
		AranBook02Page003.Configure();
		AranBook02Page002.Configure();
		AranBook02Page001.Configure();
		ActionsBuilder startActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("6b42e534fad5e6347838bf9746190740").StartActions.Actions[0]).SetObjectiveStatus("RanRomAranQuestEntry0001", null, (ObjectiveStatus)0);
		ConditionsBuilder conditions = ConditionsBuilder.New().CueSeen("5a713cb1c3f642adaab8d1641175c1af", null, negate: true).CueSeen("bc13df0cdde64ac3a1cc9eeae545bec3", null, negate: true);
		string name = "RanRomAranCamp2";
		string text2 = "19701c537d4e476ea9bee8dcc22dba36";
		CampingEncounterConfigurator.New(name, text2).SetConditions(ConditionsBuilder.New().EtudeStatus(null, null, "637a57423a82b044f888677c92f5d6cb", negate: false, null, true)).SetEncounterActions(ActionsBuilder.New().StartDialog(null, "fe8542a7a90d459c99d29921694f4d0d").RemoveCampingEncounter(text2))
			.SetChance(100)
			.Configure();
		ActionsBuilder finishActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("6b42e534fad5e6347838bf9746190740").FinishActions.Actions[0]).Conditional(conditions, ActionsBuilder.New().AddCampingEncounter(text2));
		CueSelection val2 = new CueSelection();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook02Page001")).deserializedGuid;
		val2.Cues.Add(val3);
		val2.Strategy = (Strategy)0;
		DialogConfigurator.New(BookName, text).SetStartActions(startActions).SetFinishActions(finishActions)
			.SetFirstCue(val2)
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
