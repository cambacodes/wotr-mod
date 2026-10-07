using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Blueprints.References;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.BasicEx;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.Designers.Quests.Common;
using Kingmaker.DialogSystem;
using Kingmaker.ElementsSystem;

namespace RanRomance.Anev;

public class AnevChpt05Dial001
{
	private static readonly string Ans0001Name = "RanRomAnevChpt05Dial001Ans0001";

	private static readonly string Cue0001Name = "RanRomAnevChpt05Dial001Cue0001";

	private static readonly string Ans0002Name = "RanRomAnevChpt05Dial001Ans0002";

	private static readonly string Cue0002Name = "RanRomAnevChpt05Dial001Cue0002";

	private static readonly string Cue0003Name = "RanRomAnevChpt05Dial001Cue0003";

	private static readonly string Ans0004Name = "RanRomAnevChpt05Dial001Ans0004";

	private static readonly string Cue0004Name = "RanRomAnevChpt05Dial001Cue0004";

	private static readonly string Ans0005Name = "RanRomAnevChpt05Dial001Ans0005";

	private static readonly string Cue0005Name = "RanRomAnevChpt05Dial001Cue0005";

	private static readonly string Cue0006Name = "RanRomAnevChpt05Dial001Cue0006";

	private static readonly string Ans0007Name = "RanRomAnevChpt05Dial001Ans0007";

	private static readonly string Cue0007Name = "RanRomAnevChpt05Dial001Cue0007";

	private static readonly string Cue0008Name = "RanRomAnevChpt05Dial001Cue0008";

	private static readonly string Ans0009Name = "RanRomAnevChpt05Dial001Ans0009";

	private static readonly string Cue0009Name = "RanRomAnevChpt05Dial001Cue0009";

	private static readonly string Cue0010Name = "RanRomAnevChpt05Dial001Cue0010";

	private static readonly string Ans0013Name = "RanRomAnevChpt05Dial001Ans0013";

	private static readonly string Cue0013Name = "RanRomAnevChpt05Dial001Cue0013";

	private static readonly string Ans0014Name = "RanRomAnevChpt05Dial001Ans0014";

	private static readonly string Cue0014Name = "RanRomAnevChpt05Dial001Cue0014";

	private static readonly string Ans0015Name = "RanRomAnevChpt05Dial001Ans0015";

	private static readonly string Cue0015Name = "RanRomAnevChpt05Dial001Cue0015";

	private static readonly string Ans0016Name = "RanRomAnevChpt05Dial001Ans0016";

	private static readonly string Cue0016Name = "RanRomAnevChpt05Dial001Cue0016";

	private static readonly string Ans0017Name = "RanRomAnevChpt05Dial001Ans0017";

	private static readonly string Cue0017Name = "RanRomAnevChpt05Dial001Cue0017";

	private static readonly string Ans0018Name = "RanRomAnevChpt05Dial001Ans0018";

	private static readonly string Cue0018Name = "RanRomAnevChpt05Dial001Cue0018";

	private static readonly string Ans0019Name = "RanRomAnevChpt05Dial001Ans0019";

	private static readonly string Cue0019Name = "RanRomAnevChpt05Dial001Cue0019";

	public static string Configure()
	{
		//IL_016b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0172: Expected O, but got Unknown
		//IL_0c35: Unknown result type (might be due to invalid IL or missing references)
		//IL_0c3c: Expected O, but got Unknown
		//IL_0d59: Unknown result type (might be due to invalid IL or missing references)
		//IL_0d60: Expected O, but got Unknown
		//IL_0e9c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0ea3: Expected O, but got Unknown
		//IL_0ea3: Unknown result type (might be due to invalid IL or missing references)
		//IL_0eaa: Expected O, but got Unknown
		//IL_0eb6: Unknown result type (might be due to invalid IL or missing references)
		//IL_0ebb: Unknown result type (might be due to invalid IL or missing references)
		//IL_0ed2: Unknown result type (might be due to invalid IL or missing references)
		//IL_1473: Unknown result type (might be due to invalid IL or missing references)
		//IL_147a: Expected O, but got Unknown
		//IL_147a: Unknown result type (might be due to invalid IL or missing references)
		//IL_1481: Expected O, but got Unknown
		//IL_1489: Unknown result type (might be due to invalid IL or missing references)
		//IL_148e: Unknown result type (might be due to invalid IL or missing references)
		//IL_14a5: Unknown result type (might be due to invalid IL or missing references)
		string text = "00df08f8d6f84dadbfa07486e676adf8";
		string text2 = "101be92ed41749eaa1329392ae741e83";
		string text3 = "30aa3d5b098a4ed6a8742e76ac5759a1";
		string text4 = "9bc5e930108241669fb777ca96371762";
		string text5 = "df2df55ec3bb49b68978f6a53b4f06ff";
		string text6 = "78301019d46a49e8b6f7fece0c9d1dda";
		string text7 = "d0e106dcf48a44eca582b161afc4c263";
		string text8 = "41a2ab2b568742fb9afe99ff8cd4f7e9";
		string text9 = "8e43b5f1a7cb40da8f6519e97af196f4";
		string text10 = "787f9ec94fb74f398893d9421c2292a3";
		string text11 = "b7697dde817748e29c69c8ad606a6f9c";
		string text12 = "2be4775ee36344419b4a1e825fd3106c";
		string text13 = "e38c97f0b5224b3d91352dbb2983342d";
		string text14 = "865201b1d94d43e89244809005fe8eec";
		string text15 = "9b69b1772af748368c07718d78b9de29";
		string text16 = "5b18c55967c9424a8d4a8045bc6ab884";
		string text17 = "a19476e2956b4d428613a46470e11b7e";
		string text18 = "6492461a79984903a7f0ad32f20fabbb";
		string text19 = "627ebab39cea4235a376d5fdf82eeae7";
		string text20 = "19e2f53977bc469ab114fb406531fc82";
		string text21 = "1c5b340c7fda462b9497f95466c734fc";
		string text22 = "cd8f4d6d9f474e0cb1b298574839e0ee";
		string text23 = "898b6df8401243e6929ad6c06e3d734e";
		string guid = "0511d52b55da46b6bcaadefc1e713a90";
		string text24 = "c142df56dcc24e7685c3b049ef42f688";
		string guid2 = "7987af57f5394351b54cfe96995a88a1";
		string text25 = "24d6c8716a174f749774b1201e55e892";
		string guid3 = "bdcf066a452c43349c61297580905f3e";
		string text26 = "08dc24e6ec9c46aebb4aaee0a4a90f55";
		string guid4 = "1f468789b9534ea68bd73e2635ba95d0";
		ActionsBuilder onShow = ActionsBuilder.New().SetObjectiveStatus("RanRomNuraQuestEntryFail", true, (ObjectiveStatus)1).CompleteEtude("RanRomNuraRomance")
			.CompleteEtude("RanRomNuraLich");
		ActionsBuilder onStop = ActionsBuilder.New().SetObjectiveStatus("RanRomTereQuestEntryFail", true, (ObjectiveStatus)1);
		ActionsBuilder onStop2 = ActionsBuilder.New().SetObjectiveStatus("RanRomAranQuestEntryFail", true, (ObjectiveStatus)1);
		UnitClass val = (UnitClass)BlueprintTool.Get<ConditionsHolder>("816fcd6fcaf58cf409da0de0c44e9c59").Conditions.Conditions[0];
		UnitEvaluator unit = val.Unit;
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomNuraRomance", negate: false, null, true).EtudeStatus(null, null, "RanRomNuraLich", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).CueSeen(text5, null, negate: true)
			.AddOrAndLogic(conditions)
			.UnitClass(((object)CharacterClassRefs.DevilMythicClass.Reference).ToString(), null, null, null, null, negate: false, unit);
		ConditionsBuilder conditionsBuilder = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).AnswerSelected(text6, null, negate: true)
			.AddOrAndLogic(conditions)
			.UnitClass(((object)CharacterClassRefs.DevilMythicClass.Reference).ToString(), null, null, null, null, negate: true, unit);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomTargAng", negate: false, null, true).EtudeStatus(null, null, "RanRomTargAza", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomTargNone", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions4 = ConditionsBuilder.New().DialogSeen("1603149ca1f4464cbba34ba3757a810b").AddOrAndLogic(conditions3)
			.UseOr();
		ConditionsBuilder conditionsBuilder2 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).AddOrAndLogic(conditions4)
			.AnswerSelected(text8, null, negate: true)
			.EtudeStatus(null, null, "bc65b234df544a718afc4856eb7f33fc", negate: true, null, true);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).CueSeen(text10, null, negate: true)
			.UnitClass(((object)CharacterClassRefs.DevilMythicClass.Reference).ToString(), null, null, null, null, negate: false, unit)
			.EtudeStatus(null, null, "RanRomTereOath", negate: false, null, true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).AnswerSelected(text11, null, negate: true)
			.UnitClass(((object)CharacterClassRefs.DevilMythicClass.Reference).ToString(), null, null, null, null, negate: true, unit)
			.EtudeStatus(null, null, "RanRomTereAeonScale", negate: false, null, true);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).AnswerSelected(text11, null, negate: true)
			.UnitClass(((object)CharacterClassRefs.DevilMythicClass.Reference).ToString(), null, null, null, null, negate: true, unit)
			.EtudeStatus(null, null, "RanRomTereOath", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomTereAeonScale", negate: true, null, true);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AddOrAndLogic(conditions6).AddOrAndLogic(conditions7)
			.UseOr();
		ConditionsBuilder conditionsBuilder3 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).AnswerSelected(text14, null, negate: true)
			.UnitClass(((object)CharacterClassRefs.DevilMythicClass.Reference).ToString(), null, null, null, null, negate: true, unit)
			.EtudeStatus(null, null, "0b129925567b68d4fb712b4bee6c0f9a", negate: true, null, true)
			.FlagInRange("RanRomAranConf", 1, -999)
			.CueSeen("RanRomAranBook03EndCue0001", null, negate: true);
		ConditionsBuilder conditions8 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).CueSeen(text16, null, negate: true)
			.UnitClass(((object)CharacterClassRefs.DevilMythicClass.Reference).ToString(), null, null, null, null, negate: false, unit)
			.EtudeStatus(null, null, "0b129925567b68d4fb712b4bee6c0f9a", negate: true, null, true)
			.FlagInRange("RanRomAranConf", 1, -999)
			.CueSeen("RanRomAranBook03EndCue0001", null, negate: true);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().EtudeStatus(null, null, "1d466fd4271fdc14ea1c077760c63ca5", negate: false, null, true).AnswerSelected("a08540bf69314cffb24d93d277cf6636")
			.UseOr();
		ConditionsBuilder conditionsBuilder4 = ConditionsBuilder.New().AddOrAndLogic(conditions9).QuestStatus(negate: false, "95ff7d975689fcf44b085d10907e711d", (QuestState)2)
			.EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true)
			.AnswerSelected(text17, null, negate: true);
		ConditionsBuilder conditionsBuilder5 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).EtudeStatus(true, null, "faad12cd8c8048309acb37896d8fafc3")
			.AnswerSelected(text19, null, negate: true);
		ConditionsBuilder conditionsBuilder6 = ConditionsBuilder.New().EtudeStatus(true, null, "d5e4f2aa713647cc8d40438b46e0d1ef").AnswerSelected(text21, null, negate: true);
		ConditionsBuilder conditionsBuilder7 = ConditionsBuilder.New().AnswerSelected(text23, null, negate: true);
		ConditionsBuilder conditionsBuilder8 = ConditionsBuilder.New().AnswerSelected(text24, null, negate: true);
		ConditionsBuilder conditionsBuilder9 = ConditionsBuilder.New().AnswerSelected(text25, null, negate: true);
		ConditionsBuilder conditionsBuilder10 = ConditionsBuilder.New().AnswerSelected(text26, null, negate: true);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().AddOrAndLogic(conditions2).AddOrAndLogic(conditionsBuilder)
			.AddOrAndLogic(conditionsBuilder2)
			.AddOrAndLogic(conditions5)
			.AddOrAndLogic(conditions6)
			.AddOrAndLogic(conditions7)
			.AddOrAndLogic(conditionsBuilder3)
			.AddOrAndLogic(conditions8)
			.AddOrAndLogic(conditionsBuilder4)
			.AddOrAndLogic(conditionsBuilder5)
			.AddOrAndLogic(conditionsBuilder6)
			.UseOr();
		DialogSpeaker val2 = new DialogSpeaker();
		val2.NoSpeaker = false;
		val2.MoveCamera = true;
		val2.NotRevealInFoW = false;
		val2.SwitchDual = false;
		AnswersListConfigurator.New("RanRomAnevChpt05Dial001list", "31c23fd4f954444fb18673e78bf6718f").AddToAnswers(text6).AddToAnswers(text8)
			.AddToAnswers(text11)
			.AddToAnswers(text14)
			.AddToAnswers(text17)
			.AddToAnswers(text19)
			.AddToAnswers(text21)
			.AddToAnswers(text3)
			.Configure();
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAnevChpt03Dial001Cue0001.Text").SetSpeaker(val2)
			.SetAnswers("RanRomAnevChpt05Dial001list")
			.Configure();
		CueSelection val3 = new CueSelection();
		val3.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>(text2));
		SequenceExitConfigurator.New("RanRomAnevChpt05Dial001Exit", "db11c584b3f8495985c34b0fde496e61").SetContinueValue(val3).Configure();
		CueSequenceConfigurator.New("RanRomAnevChpt05Dial001Seq", "7dc8ecc532d44c629cc01734080fce07").AddToCues(text5).AddToCues(text7)
			.AddToCues(text9)
			.AddToCues(text10)
			.AddToCues(text12)
			.AddToCues(text13)
			.AddToCues(text15)
			.AddToCues(text16)
			.AddToCues(text18)
			.AddToCues(text20)
			.AddToCues(text22)
			.SetExit("db11c584b3f8495985c34b0fde496e61")
			.Configure();
		CueSelection val4 = new CueSelection();
		BlueprintCueBaseReference val5 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAnevChpt05Dial001Seq")).deserializedGuid;
		val4.Cues.Add(val5);
		val4.Strategy = (Strategy)0;
		ActionsBuilder onSelect = ActionsBuilder.New().UnmarkAnswersSelected(text);
		AnswerConfigurator.New(Ans0001Name, text).SetShowConditions(showConditions2).SetText("RanRomAnevChpt03Dial001Ans0001.Text")
			.SetNextCue(val4)
			.SetOnSelect(onSelect)
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetText("RanRomAnevChpt03Dial001Ans0002.Text").Configure();
		CueConfigurator.New(Cue0002Name, text4).SetText("RanRomAnevChpt03Dial001Cue0002.Text").SetSpeaker(val2)
			.SetAnswers("33960c7f7af40cd43b7f801a76c87a0b")
			.Configure();
		CueConfigurator.New(Cue0003Name, text5).SetConditions(conditions2).SetText("RanRomAnevChpt05Dial001Cue0003.Text")
			.SetSpeaker(val2)
			.SetOnShow(onShow)
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text6).SetShowConditions(conditionsBuilder).SetShowOnce()
			.SetText("RanRomAnevChpt05Dial001Ans0004.Text")
			.Configure();
		CueConfigurator.New(Cue0004Name, text7).SetConditions(conditionsBuilder).SetText("RanRomAnevChpt05Dial001Cue0004.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text8).SetShowConditions(conditionsBuilder2).SetShowOnce()
			.SetText("RanRomAnevChpt05Dial001Ans0005.Text")
			.Configure();
		CueConfigurator.New(Cue0005Name, text9).SetConditions(conditionsBuilder2).SetText("RanRomAnevChpt05Dial001Cue0005.Text")
			.SetSpeaker(val2)
			.Configure();
		CueConfigurator.New(Cue0006Name, text10).SetConditions(conditions5).SetText("RanRomAnevChpt05Dial001Cue0006.Text")
			.SetSpeaker(val2)
			.SetOnStop(onStop)
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text11).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAnevChpt05Dial001Ans0007.Text")
			.Configure();
		CueConfigurator.New(Cue0007Name, text12).SetConditions(conditions6).SetText("RanRomAnevChpt05Dial001Cue0007.Text")
			.SetSpeaker(val2)
			.Configure();
		CueConfigurator.New(Cue0008Name, text13).SetConditions(conditions7).SetText("RanRomAnevChpt05Dial001Cue0008.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0009Name, text14).SetShowConditions(conditionsBuilder3).SetShowOnce()
			.SetText("RanRomAnevChpt05Dial001Ans0009.Text")
			.Configure();
		CueConfigurator.New(Cue0009Name, text15).SetConditions(conditionsBuilder3).SetText("RanRomAnevChpt05Dial001Cue0009.Text")
			.SetSpeaker(val2)
			.Configure();
		CueConfigurator.New(Cue0010Name, text16).SetConditions(conditions8).SetText("RanRomAnevChpt05Dial001Cue0010.Text")
			.SetSpeaker(val2)
			.SetOnStop(onStop2)
			.Configure();
		AnswerConfigurator.New(Ans0013Name, text17).SetShowConditions(conditionsBuilder4).SetShowOnce()
			.SetText("RanRomAnevChpt05Dial001Ans0013.Text")
			.Configure();
		CueConfigurator.New(Cue0013Name, text18).SetConditions(conditionsBuilder4).SetText("RanRomAnevChpt05Dial001Cue0013.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0014Name, text19).SetShowConditions(conditionsBuilder5).SetShowOnce()
			.SetText("RanRomAnevChpt05Dial001Ans0014.Text")
			.Configure();
		CueConfigurator.New(Cue0014Name, text20).SetConditions(conditionsBuilder5).SetText("RanRomAnevChpt05Dial001Cue0014.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0015Name, text21).SetShowConditions(conditionsBuilder6).SetShowOnce()
			.SetText("RanRomAnevChpt05Dial001Ans0015.Text")
			.Configure();
		CueConfigurator.New(Cue0015Name, text22).SetConditions(conditionsBuilder6).SetText("RanRomAnevChpt05Dial001Cue0015.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0016Name, text23).SetShowConditions(conditionsBuilder7).SetShowOnce()
			.SetText("RanRomAnevChpt05Dial001Ans0016.Text")
			.Configure();
		CueConfigurator.New(Cue0016Name, guid).SetConditions(conditionsBuilder7).SetText("RanRomAnevChpt05Dial001Cue0016.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0017Name, text24).SetShowConditions(conditionsBuilder8).SetShowOnce()
			.SetText("RanRomAnevChpt05Dial001Ans0017.Text")
			.Configure();
		CueConfigurator.New(Cue0017Name, guid2).SetConditions(conditionsBuilder8).SetText("RanRomAnevChpt05Dial001Cue0017.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0018Name, text25).SetShowConditions(conditionsBuilder9).SetShowOnce()
			.SetText("RanRomAnevChpt05Dial001Ans0018.Text")
			.Configure();
		CueConfigurator.New(Cue0018Name, guid3).SetConditions(conditionsBuilder9).SetText("RanRomAnevChpt05Dial001Cue0018.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0019Name, text26).SetShowConditions(conditionsBuilder10).SetShowOnce()
			.SetText("RanRomAnevChpt05Dial001Ans0019.Text")
			.Configure();
		CueConfigurator.New(Cue0019Name, guid4).SetConditions(conditionsBuilder10).SetText("RanRomAnevChpt05Dial001Cue0019.Text")
			.SetSpeaker(val2)
			.Configure();
		CueSelection val6 = new CueSelection();
		BlueprintCueBaseReference val7 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val7).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text4)).deserializedGuid;
		val6.Cues.Add(val7);
		val6.Strategy = (Strategy)0;
		AnswerConfigurator.For(text3).SetNextCue(val6).Configure();
		return "";
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
