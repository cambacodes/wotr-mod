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
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;

namespace RanRomance.Aran;

public class AranBook01
{
	private static readonly string BookName = "RanRomAranBook01";

	public static string Configure()
	{
		//IL_0007: Unknown result type (might be due to invalid IL or missing references)
		//IL_000d: Expected O, but got Unknown
		//IL_021e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0225: Expected O, but got Unknown
		//IL_0225: Unknown result type (might be due to invalid IL or missing references)
		//IL_022c: Expected O, but got Unknown
		//IL_022c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0233: Expected O, but got Unknown
		//IL_023f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0244: Unknown result type (might be due to invalid IL or missing references)
		//IL_0255: Unknown result type (might be due to invalid IL or missing references)
		//IL_025a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0280: Unknown result type (might be due to invalid IL or missing references)
		string text = "2936ff4e6e234702b7f59b469b57feaa";
		PlayerCharacter val = new PlayerCharacter();
		((Element)val).name = "pc" + text;
		AranBook01End.Configure();
		AranBook01Page006.Configure();
		AranBook01Page005.Configure();
		AranBook01Page004.Configure();
		AranBook01Page003.Configure();
		AranBook01Page002.Configure();
		AranBook01Page001.Configure();
		ActionsBuilder startActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("6b42e534fad5e6347838bf9746190740").StartActions.Actions[0]);
		ConditionsBuilder conditions = ConditionsBuilder.New().DialogSeen("28d2d40f91ea2c64ca8897815d341214").DialogSeen("138076de849b2b3408c04c02e524df06")
			.DialogSeen("9212aa4a0c8a9594bbd5596e83ddae35")
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().DialogSeen("f2d055f18b8265347b837c2ff3b9488a").UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val).AddOrAndLogic(conditions2)
			.UseOr();
		string name = "RanRomAranCamp1";
		string text2 = "b73a3855307e494d8cd45375ac655bfd";
		CampingEncounterConfigurator.New(name, text2).SetConditions(ConditionsBuilder.New().EtudeStatus(null, null, "15e0048c7daf0ac4999c2313b58df0e3", negate: false, null, true).AddOrAndLogic(conditions)
			.AddOrAndLogic(conditions3)).SetEncounterActions(ActionsBuilder.New().StartDialog(null, "b9068ea8642f4c9da4a338ebd5ba316f").RemoveCampingEncounter(text2))
			.SetChance(100)
			.Configure();
		ActionsBuilder finishActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("6b42e534fad5e6347838bf9746190740").FinishActions.Actions[0]).AddCampingEncounter(text2)
			.Conditional(conditions, ActionsBuilder.New().GiveObjective("RanRomAranQuestEntry0001"));
		CueSelection val2 = new CueSelection();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook01Page001")).deserializedGuid;
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook01Page101")).deserializedGuid;
		val2.Cues.Add(val3);
		val2.Cues.Add(val4);
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
