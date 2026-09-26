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

namespace RanRomance.Stor;

public class StorChpt05Dial001
{
	private static readonly string Ans0001Name = "RanRomStorChpt05Dial001Ans0001";

	private static readonly string Cue0001Name = "RanRomStorChpt05Dial001Cue0001";

	private static readonly string Ans0002Name = "RanRomStorChpt05Dial001Ans0002";

	private static readonly string Cue0002Name = "RanRomStorChpt05Dial001Cue0002";

	private static readonly string Cue0003Name = "RanRomStorChpt05Dial001Cue0003";

	private static readonly string Ans0004Name = "RanRomStorChpt05Dial001Ans0004";

	private static readonly string Cue0004Name = "RanRomStorChpt05Dial001Cue0004";

	private static readonly string Cue0005Name = "RanRomStorChpt05Dial001Cue0005";

	private static readonly string Cue0006Name = "RanRomStorChpt05Dial001Cue0006";

	private static readonly string Ans0007Name = "RanRomStorChpt05Dial001Ans0007";

	private static readonly string Cue0007Name = "RanRomStorChpt05Dial001Cue0007";

	private static readonly string Ans0008Name = "RanRomStorChpt05Dial001Ans0008";

	private static readonly string Cue0008Name = "RanRomStorChpt05Dial001Cue0008";

	private static readonly string Ans0009Name = "RanRomStorChpt05Dial001Ans0009";

	private static readonly string Cue0009Name = "RanRomStorChpt05Dial001Cue0009";

	private static readonly string Ans0010Name = "RanRomStorChpt05Dial001Ans0010";

	private static readonly string Cue0010Name = "RanRomStorChpt05Dial001Cue0010";

	public static string Configure()
	{
		//IL_008a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0091: Expected O, but got Unknown
		//IL_08ec: Unknown result type (might be due to invalid IL or missing references)
		//IL_08f3: Expected O, but got Unknown
		//IL_09e6: Unknown result type (might be due to invalid IL or missing references)
		//IL_09ed: Expected O, but got Unknown
		//IL_0aea: Unknown result type (might be due to invalid IL or missing references)
		//IL_0af1: Expected O, but got Unknown
		//IL_0af1: Unknown result type (might be due to invalid IL or missing references)
		//IL_0af8: Expected O, but got Unknown
		//IL_0b04: Unknown result type (might be due to invalid IL or missing references)
		//IL_0b09: Unknown result type (might be due to invalid IL or missing references)
		//IL_0b20: Unknown result type (might be due to invalid IL or missing references)
		//IL_0e89: Unknown result type (might be due to invalid IL or missing references)
		//IL_0e90: Expected O, but got Unknown
		//IL_0e90: Unknown result type (might be due to invalid IL or missing references)
		//IL_0e97: Expected O, but got Unknown
		//IL_0e9f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0ea4: Unknown result type (might be due to invalid IL or missing references)
		//IL_0ebb: Unknown result type (might be due to invalid IL or missing references)
		string text = "3af67c71de8d4d7682dcc87777e9dee0";
		string text2 = "b07c3f3e05a644519bb4d22e87276dd2";
		string text3 = "c4f6d861686943fa84562cd798f4562e";
		string text4 = "d7d257b1631847c298107160ab567a7d";
		string text5 = "c234f20de79a466f991ffde925f56a30";
		string text6 = "66465c3e60c9450da0054b9090cbf93e";
		string text7 = "78707ddfe7d942dcb9dcb23c3ea61e2b";
		string text8 = "04e2b4e62bc94e6abb754f957f066316";
		string text9 = "6603452c33da40a7aa229a12329cdd1b";
		string text10 = "ef1d696cfe3444969b0655ebb3a2d473";
		string text11 = "588a0f2f64014329817cca0452fbca40";
		string text12 = "6fd942ab20644c5a94a92c25dd700dd5";
		string text13 = "01a8d99fed0241dfa70f13e6ab15bd44";
		string text14 = "0fa6df22921b4e8d8178f33fa56f99f5";
		string text15 = "f80fc9ca06eb446fa41648d8adc0cfa6";
		string text16 = "904e03e8533349bfbe911ef5175f620d";
		string text17 = "0f9748ee00154114a1c412a5fbf42808";
		UnitClass val = (UnitClass)BlueprintTool.Get<ConditionsHolder>("816fcd6fcaf58cf409da0de0c44e9c59").Conditions.Conditions[0];
		UnitEvaluator unit = val.Unit;
		ActionsBuilder onStop = ActionsBuilder.New().SetObjectiveStatus("RanRomTargQuestEntryFail", true, (ObjectiveStatus)1);
		ActionsBuilder onStop2 = ActionsBuilder.New().SetObjectiveStatus("RanRomNuraQuestEntryFail", true, (ObjectiveStatus)1);
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "6125c10886d6465091f4e092618ca55a", negate: false, null, true).EtudeStatus(null, null, "ba365d0ae03c414a8f6f906837a4fe91", negate: false, null, true)
			.EtudeStatus(null, null, "09f46662bcd14a03a0874267e16d6e6f", negate: false, null, true)
			.EtudeStatus(null, null, "9ce3448490564fbebed24d077f54f2b3", negate: false, null, true)
			.EtudeStatus(null, null, "061d1dfd76f4ea74ea8aa4d013fc8016", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomNuraRomance", negate: false, null, true).EtudeStatus(null, null, "RanRomNuraLich", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).AddOrAndLogic(conditions)
			.CueSeen(text5, null, negate: true)
			.AddOrAndLogic(conditions2)
			.UnitClass(((object)CharacterClassRefs.DevilMythicClass.Reference).ToString(), null, null, null, null, negate: false, unit);
		ConditionsBuilder conditionsBuilder = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).AddOrAndLogic(conditions)
			.AnswerSelected(text6, null, negate: true)
			.AddOrAndLogic(conditions2)
			.UnitClass(((object)CharacterClassRefs.DevilMythicClass.Reference).ToString(), null, null, null, null, negate: true, unit);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).AddOrAndLogic(conditions)
			.DialogSeen("1603149ca1f4464cbba34ba3757a810b")
			.EtudeStatus(null, null, "RanRomTargRomance", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomTargNone", negate: false, null, true)
			.CueSeen(text8, null, negate: true);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).AddOrAndLogic(conditions)
			.DialogSeen("1603149ca1f4464cbba34ba3757a810b")
			.EtudeStatus(null, null, "RanRomTargRomance", negate: true, null, true)
			.EtudeStatus(null, null, "RanRomTargNone", negate: false, null, true)
			.CueSeen(text9, null, negate: true);
		ConditionsBuilder conditionsBuilder2 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).AddOrAndLogic(conditions)
			.DialogSeen("1603149ca1f4464cbba34ba3757a810b")
			.EtudeStatus(null, null, "RanRomTargNone", negate: true, null, true)
			.AnswerSelected(text10, null, negate: true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().EtudeStatus(null, null, "1d466fd4271fdc14ea1c077760c63ca5", negate: false, null, true).AnswerSelected("a08540bf69314cffb24d93d277cf6636")
			.UseOr();
		ConditionsBuilder conditionsBuilder3 = ConditionsBuilder.New().AddOrAndLogic(conditions).EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true)
			.QuestStatus(negate: false, "95ff7d975689fcf44b085d10907e711d", (QuestState)2)
			.AddOrAndLogic(conditions6)
			.AnswerSelected(text12, null, negate: true);
		ConditionsBuilder conditionsBuilder4 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).AddOrAndLogic(conditions)
			.EtudeStatus(true, null, "faad12cd8c8048309acb37896d8fafc3")
			.AnswerSelected(text14, null, negate: true);
		ConditionsBuilder conditionsBuilder5 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomC5MythicCompl", negate: false, null, true).AddOrAndLogic(conditions)
			.EtudeStatus(true, null, "d5e4f2aa713647cc8d40438b46e0d1ef")
			.AnswerSelected(text16, null, negate: true);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AddOrAndLogic(conditions3).AddOrAndLogic(conditionsBuilder)
			.AddOrAndLogic(conditions4)
			.AddOrAndLogic(conditions5)
			.AddOrAndLogic(conditionsBuilder2)
			.AddOrAndLogic(conditionsBuilder3)
			.AddOrAndLogic(conditionsBuilder4)
			.AddOrAndLogic(conditionsBuilder5)
			.UseOr();
		DialogSpeaker val2 = new DialogSpeaker();
		val2.NoSpeaker = false;
		val2.MoveCamera = true;
		val2.NotRevealInFoW = false;
		val2.SwitchDual = false;
		AnswersListConfigurator.New("RanRomStorChpt05Dial001list", "bfb14ac649fb40bfab605f1d992001e5").AddToAnswers(text6).AddToAnswers(text10)
			.AddToAnswers(text12)
			.AddToAnswers(text14)
			.AddToAnswers(text16)
			.AddToAnswers(text3)
			.Configure();
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomStorChpt05Dial001Cue0001.Text").SetSpeaker(val2)
			.SetAnswers("RanRomStorChpt05Dial001list")
			.Configure();
		CueSelection val3 = new CueSelection();
		val3.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>(text2));
		SequenceExitConfigurator.New("RanRomStorChpt05Dial001Exit", "619b8806ef61462298d27eaf7e1203af").SetContinueValue(val3).Configure();
		CueSequenceConfigurator.New("RanRomStorChpt05Dial001Seq", "b07daaf6ee8944b88a3f0c088230a1b0").AddToCues(text5).AddToCues(text7)
			.AddToCues(text8)
			.AddToCues(text9)
			.AddToCues(text11)
			.AddToCues(text13)
			.AddToCues(text15)
			.AddToCues(text17)
			.SetExit("619b8806ef61462298d27eaf7e1203af")
			.Configure();
		CueSelection val4 = new CueSelection();
		BlueprintCueBaseReference val5 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomStorChpt05Dial001Seq")).deserializedGuid;
		val4.Cues.Add(val5);
		val4.Strategy = (Strategy)0;
		ActionsBuilder actionsBuilder = ActionsBuilder.New().StartDialog(null, "9947a33fcd4543d18a6ab92ea292119f");
		ActionsBuilder actionsBuilder2 = ActionsBuilder.New().StartDialog(null, "ddcf04165a604410888aac8e752b1f92");
		ActionsBuilder onSelect = ActionsBuilder.New().UnmarkAnswersSelected(text);
		AnswerConfigurator.New(Ans0001Name, text).SetText("RanRomStorChpt05Dial001Ans0001.Text").SetShowConditions(showConditions)
			.SetNextCue(val4)
			.SetOnSelect(onSelect)
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetText("RanRomStorChpt05Dial001Ans0002.Text").Configure();
		CueConfigurator.New(Cue0002Name, text4).SetText("RanRomStorChpt05Dial001Cue0002.Text").SetSpeaker(val2)
			.SetAnswers("2f5b7e0b76d3c5a42a431e1e33a8db09")
			.Configure();
		CueConfigurator.New(Cue0003Name, text5).SetConditions(conditions3).SetText("RanRomStorChpt05Dial001Cue0003.Text")
			.SetSpeaker(val2)
			.SetOnStop(onStop2)
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text6).SetShowConditions(conditionsBuilder).SetShowOnce()
			.SetText("RanRomStorChpt05Dial001Ans0004.Text")
			.Configure();
		CueConfigurator.New(Cue0004Name, text7).SetConditions(conditionsBuilder).SetText("RanRomStorChpt05Dial001Cue0004.Text")
			.SetSpeaker(val2)
			.Configure();
		CueConfigurator.New(Cue0005Name, text8).SetConditions(conditions4).SetText("RanRomStorChpt05Dial001Cue0005.Text")
			.SetSpeaker(val2)
			.SetOnStop(onStop)
			.Configure();
		CueConfigurator.New(Cue0006Name, text9).SetConditions(conditions5).SetText("RanRomStorChpt05Dial001Cue0006.Text")
			.SetSpeaker(val2)
			.SetOnStop(onStop)
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text10).SetShowConditions(conditionsBuilder2).SetShowOnce()
			.SetText("RanRomStorChpt05Dial001Ans0007.Text")
			.Configure();
		CueConfigurator.New(Cue0007Name, text11).SetConditions(conditionsBuilder2).SetText("RanRomStorChpt05Dial001Cue0007.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0008Name, text12).SetShowConditions(conditionsBuilder3).SetShowOnce()
			.SetText("RanRomStorChpt05Dial001Ans0008.Text")
			.Configure();
		CueConfigurator.New(Cue0008Name, text13).SetConditions(conditionsBuilder3).SetText("RanRomStorChpt05Dial001Cue0008.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0009Name, text14).SetShowConditions(conditionsBuilder4).SetShowOnce()
			.SetText("RanRomStorChpt05Dial001Ans0009.Text")
			.Configure();
		CueConfigurator.New(Cue0009Name, text15).SetConditions(conditionsBuilder4).SetText("RanRomStorChpt05Dial001Cue0009.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0010Name, text16).SetShowConditions(conditionsBuilder5).SetShowOnce()
			.SetText("RanRomStorChpt05Dial001Ans0010.Text")
			.Configure();
		CueConfigurator.New(Cue0010Name, text17).SetConditions(conditionsBuilder5).SetText("RanRomStorChpt05Dial001Cue0010.Text")
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
