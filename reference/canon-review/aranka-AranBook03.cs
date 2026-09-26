using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.AreaEx;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Blueprints.Configurators.RandomEncounters;
using BlueprintCore.Blueprints.References;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.BasicEx;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.Designers.Quests.Common;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;

namespace RanRomance.Aran;

public class AranBook03
{
	private static readonly string BookName = "RanRomAranBook03";

	public static string Configure()
	{
		//IL_0007: Unknown result type (might be due to invalid IL or missing references)
		//IL_000d: Expected O, but got Unknown
		//IL_001e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0024: Expected O, but got Unknown
		//IL_02b7: Unknown result type (might be due to invalid IL or missing references)
		//IL_02be: Expected O, but got Unknown
		//IL_02be: Unknown result type (might be due to invalid IL or missing references)
		//IL_02c5: Expected O, but got Unknown
		//IL_02d1: Unknown result type (might be due to invalid IL or missing references)
		//IL_02d6: Unknown result type (might be due to invalid IL or missing references)
		//IL_02ed: Unknown result type (might be due to invalid IL or missing references)
		string text = "fe8542a7a90d459c99d29921694f4d0d";
		PlayerCharacter val = new PlayerCharacter();
		((Element)val).name = "pc" + text;
		IntConstant val2 = new IntConstant();
		val2.Value = 7;
		((Element)val2).name = "constant7" + text;
		AranBook03End.Configure();
		AranBook03Page007.Configure();
		AranBook03Page006.Configure();
		AranBook03Page005.Configure();
		AranBook03Page004.Configure();
		AranBook03Page003.Configure();
		AranBook03Page002.Configure();
		AranBook03Page001.Configure();
		ActionsBuilder startActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("6b42e534fad5e6347838bf9746190740").StartActions.Actions[0]).SetObjectiveStatus("RanRomAranQuestEntry0002", null, (ObjectiveStatus)0);
		ConditionsBuilder conditions = ConditionsBuilder.New().FlagInRange("RanRomAranConf", 999, 2).CueSeen("RanRomAranBook03EndCue0001", null, negate: true);
		string name = "RanRomAranCamp3";
		string text2 = "e162f1cea11345b8a0e04eb353ad3a25";
		CampingEncounterConfigurator.New(name, text2).SetConditions(ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).UnitClass(((object)CharacterClassRefs.DevilMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val)
			.UnitClass(((object)CharacterClassRefs.SwarmThatWalksClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val)
			.UnitClass(((object)CharacterClassRefs.LichMythicClass.Reference).ToString(), null, true, null, (IntEvaluator?)(object)val2, negate: true, (UnitEvaluator?)(object)val)
			.UnitClass(((object)CharacterClassRefs.DemonMythicClass.Reference).ToString(), null, true, null, (IntEvaluator?)(object)val2, negate: true, (UnitEvaluator?)(object)val)
			.EtudeStatus(null, null, "0b129925567b68d4fb712b4bee6c0f9a", negate: true, null, true)).SetEncounterActions(ActionsBuilder.New().StartDialog(null, "14ffcdd473704e5dbc8cfe5f98b582b8").RemoveCampingEncounter(text2))
			.SetChance(100)
			.Configure();
		ActionsBuilder finishActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("6b42e534fad5e6347838bf9746190740").FinishActions.Actions[0]).Conditional(conditions, ActionsBuilder.New().AddCampingEncounter(text2));
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook03Page001")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		DialogConfigurator.New(BookName, text).SetStartActions(startActions).SetFinishActions(finishActions)
			.SetFirstCue(val3)
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
