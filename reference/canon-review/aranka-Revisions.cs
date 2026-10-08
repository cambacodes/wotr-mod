using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.AreaEx;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.AreaLogic.Etudes;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Designers.Quests.Common;
using Kingmaker.DialogSystem.Blueprints;

namespace RanRomance.Revisions;

public class Revisions
{
	public static void Configure()
	{
		EtudeConfigurator.For("0e20d73ea0da6a94d94a6b42035a1ce0").AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().AnswerSelected("395b40ff6bbc4e8085765a34239930f1").ObjectiveStatus(negate: false, "RanRomTereQuestEntry0001", (QuestObjectiveState)0), ActionsBuilder.New().GiveObjective("RanRomTereQuestEntry0001"))).Configure();
		EtudeConfigurator.For("15e0048c7daf0ac4999c2313b58df0e3").AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().DialogSeen("RanRomTereBook01").ObjectiveStatus(negate: false, "RanRomTereQuestEntry0002", (QuestObjectiveState)0)
			.QuestStatus(negate: false, "RanRomTereQuest", (QuestState)1), ActionsBuilder.New().GiveObjective("RanRomTereQuestEntry0002"))).Configure();
		EtudeConfigurator.For("637a57423a82b044f888677c92f5d6cb").AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().ObjectiveStatus(negate: false, "RanRomTargQuestEntry0001", (QuestObjectiveState)1), ActionsBuilder.New().SetObjectiveStatus("RanRomTargQuestEntryFail", true, (ObjectiveStatus)1))).AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().DialogSeen("RanRomTereBook02").ObjectiveStatus(negate: false, "RanRomTereQuestEntry0003", (QuestObjectiveState)0), ActionsBuilder.New().GiveObjective("RanRomTereQuestEntry0003")))
			.AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().DialogSeen("RanRomAranBook02").CueSeen("5a713cb1c3f642adaab8d1641175c1af", null, negate: true)
				.CueSeen("bc13df0cdde64ac3a1cc9eeae545bec3", null, negate: true)
				.ObjectiveStatus(negate: false, "RanRomAranQuestEntry0002", (QuestObjectiveState)0), ActionsBuilder.New().GiveObjective("RanRomAranQuestEntry0002")))
			.AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().ObjectiveStatus(negate: false, "RanRomNuraQuestEntry0001", (QuestObjectiveState)1), ActionsBuilder.New().SetObjectiveStatus("RanRomNuraQuestEntryFail", true, (ObjectiveStatus)1)))
			.Configure();
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected("a08540bf69314cffb24d93d277cf6636").EtudeStatus(null, null, "1d466fd4271fdc14ea1c077760c63ca5", negate: true, null, true);
		ActionsBuilder actions = ActionsBuilder.New().Conditional(conditions, ActionsBuilder.New().StartEtude("1d466fd4271fdc14ea1c077760c63ca5"));
		EtudeConfigurator.For("5b01aa690202e584888dfc600a4aac0a").AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().DialogSeen("RanRomAranBook03", negate: true).QuestStatus(negate: false, "RanRomAranQuest", (QuestState)1), ActionsBuilder.New().SetObjectiveStatus("RanRomAranQuestEntryFail", true, (ObjectiveStatus)1))).AddEtudePlayTrigger(actions)
			.Configure();
		EtudeConfigurator.For("41bf413e0fa2ea34b937d4445edd5f89").AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().QuestStatus(negate: false, "RanRomTargQuest", (QuestState)1), ActionsBuilder.New().SetObjectiveStatus("RanRomTargQuestEntryFail", true, (ObjectiveStatus)1))).AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().QuestStatus(negate: false, "RanRomTereQuest", (QuestState)1), ActionsBuilder.New().SetObjectiveStatus("RanRomTereQuestEntryFail", true, (ObjectiveStatus)1)))
			.AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().QuestStatus(negate: false, "RanRomNuraQuest", (QuestState)1), ActionsBuilder.New().SetObjectiveStatus("RanRomNuraQuestEntryFail", true, (ObjectiveStatus)1)))
			.AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().QuestStatus(negate: false, "RanRomAranQuest", (QuestState)1), ActionsBuilder.New().SetObjectiveStatus("RanRomAranQuestEntryFail", true, (ObjectiveStatus)1)))
			.AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().QuestStatus(negate: false, "RanRomMinaQuest", (QuestState)1), ActionsBuilder.New().SetObjectiveStatus("RanRomMinaQuestEntryFail", true, (ObjectiveStatus)1)))
			.Configure();
		EtudeConfigurator.For("bc65b234df544a718afc4856eb7f33fc").AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().QuestStatus(negate: false, "RanRomTargQuest", (QuestState)1), ActionsBuilder.New().SetObjectiveStatus("RanRomTargQuestEntryFail", true, (ObjectiveStatus)1))).Configure();
		BlueprintDialog val = BlueprintTool.Get<BlueprintDialog>("28d2d40f91ea2c64ca8897815d341214");
		ActionsBuilder finishActions = ActionsBuilder.New().Add(val.FinishActions.Actions[0]).Add(val.FinishActions.Actions[1])
			.Conditional(ConditionsBuilder.New().DialogSeen("RanRomAranBook01"), ActionsBuilder.New().GiveObjective("RanRomAranQuestEntry0001"));
		DialogConfigurator.For("28d2d40f91ea2c64ca8897815d341214").SetFinishActions(finishActions).Configure();
		DialogConfigurator.For("9212aa4a0c8a9594bbd5596e83ddae35").SetFinishActions(finishActions).Configure();
		BlueprintDialog val2 = BlueprintTool.Get<BlueprintDialog>("28d2d40f91ea2c64ca8897815d341214");
		ActionsBuilder finishActions2 = ActionsBuilder.New().Add(val2.FinishActions.Actions[0]).Add(val2.FinishActions.Actions[1])
			.Conditional(ConditionsBuilder.New().DialogSeen("RanRomAranBook01"), ActionsBuilder.New().GiveObjective("RanRomAranQuestEntry0001"));
		DialogConfigurator.For("138076de849b2b3408c04c02e524df06").SetFinishActions(finishActions2).Configure();
		EtudeConfigurator.For("0b129925567b68d4fb712b4bee6c0f9a").AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().QuestStatus(negate: false, "RanRomAranQuest", (QuestState)1), ActionsBuilder.New().SetObjectiveStatus("RanRomAranQuestEntryFail", true, (ObjectiveStatus)1))).Configure();
		EtudeConfigurator.For("5f72b252bd7fa8d48bd04c27982a4f9c").AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().QuestStatus(negate: false, "RanRomAranQuest", (QuestState)1), ActionsBuilder.New().SetObjectiveStatus("RanRomAranQuestEntryFail", true, (ObjectiveStatus)1))).Configure();
		EtudeConfigurator.For("061d1dfd76f4ea74ea8aa4d013fc8016").AddEtudePlayTrigger(ActionsBuilder.New().Conditional(ConditionsBuilder.New().QuestStatus(negate: false, "RanRomAranQuest", (QuestState)1), ActionsBuilder.New().SetObjectiveStatus("RanRomAranQuestEntryFail", true, (ObjectiveStatus)1))).Configure();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "a837c3bc9cbb4e846ab5565915165c91", negate: true, null, true).EtudeStatus(null, null, "c922e0cbe25a0cf4dad4ce7a3ca81935", negate: true, null, true)
			.EtudeStatus(null, null, "739b9fe9b8998c641b4b3dfed40bc217", negate: true, null, true)
			.EtudeStatus(null, null, "20927a9471c00814b808fd69e88879c7", negate: true, null, true)
			.EtudeStatus(null, null, "a879a3a637a7eeb43b40677e4a8c4450", negate: false, null, true);
		ActionsBuilder finishActions3 = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("6825f92d429082944b504c1f78b4e30a").FinishActions.Actions[0]).Add(BlueprintTool.Get<BlueprintDialog>("6825f92d429082944b504c1f78b4e30a").FinishActions.Actions[1])
			.Add(BlueprintTool.Get<BlueprintDialog>("6825f92d429082944b504c1f78b4e30a").FinishActions.Actions[2])
			.Add(BlueprintTool.Get<BlueprintDialog>("6825f92d429082944b504c1f78b4e30a").FinishActions.Actions[3])
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions2).DialogSeen("c47ffdc9a62b40ac9648ce6006673cb8", negate: true), ActionsBuilder.New().StartDialog(null, "6ce0e47ee5b94576a60c607ec0fc063d"));
		DialogConfigurator.For("6825f92d429082944b504c1f78b4e30a").SetFinishActions(finishActions3).Configure();
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected("7cf020ba98c159649a74ce0268964a18").AnswerSelected("fdda84976ee21474f95dd41460fc8edf")
			.UseOr();
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AddOrAndLogic(conditions2).AddOrAndLogic(conditions3)
			.DialogSeen("aca6f74af98549fab00bb1f82fa24878", negate: true)
			.DialogSeen("c47ffdc9a62b40ac9648ce6006673cb8", negate: true);
		ActionsBuilder finishActions4 = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("611ab69e1ec4ccc4a9dc023762fddf73").FinishActions.Actions[0]).Conditional(conditions4, ActionsBuilder.New().StartDialog(null, "aca6f74af98549fab00bb1f82fa24878"));
		DialogConfigurator.For("611ab69e1ec4ccc4a9dc023762fddf73").SetFinishActions(finishActions4).Configure();
		ActionsBuilder onShow = ActionsBuilder.New().Conditional(ConditionsBuilder.New().EtudeStatus(null, null, "a879a3a637a7eeb43b40677e4a8c4450", negate: false, null, true), ActionsBuilder.New().GiveObjective("RanRomNuraQuestEntry0001")).Conditional(ConditionsBuilder.New().EtudeStatus(null, null, "RanRomTargTimer1Comp", negate: false, null, true), ActionsBuilder.New().GiveObjective("RanRomTargQuestEntry0002"));
		CueConfigurator.For("7568521a8c3ae394a9da03b67a17aa7e").SetOnShow(onShow).Configure();
		ConditionsBuilder conditions5 = ConditionsBuilder.New().DialogSeen("fe8542a7a90d459c99d29921694f4d0d", negate: true).AnswerSelected("26d211d079ef173439fd5ed7e97e674f")
			.DialogSeen("b9068ea8642f4c9da4a338ebd5ba316f")
			.CueSeen("5a713cb1c3f642adaab8d1641175c1af", null, negate: true)
			.CueSeen("bc13df0cdde64ac3a1cc9eeae545bec3", null, negate: true);
		DialogConfigurator.For("fc226ef5f4f26a849b81bf81b9026439").SetFinishActions(ActionsBuilder.New().Conditional(conditions5, ActionsBuilder.New().StartDialog(null, "fe8542a7a90d459c99d29921694f4d0d").RemoveCampingEncounter("19701c537d4e476ea9bee8dcc22dba36"))).Configure();
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
