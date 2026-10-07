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
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.DialogSystem;
using Kingmaker.ElementsSystem;

namespace RanRomance.Anev;

public class AnevChpt03Dial001
{
	private static readonly string Ans0001Name = "RanRomAnevChpt03Dial001Ans0001";

	private static readonly string Cue0001Name = "RanRomAnevChpt03Dial001Cue0001";

	private static readonly string Ans0002Name = "RanRomAnevChpt03Dial001Ans0002";

	private static readonly string Cue0002Name = "RanRomAnevChpt03Dial001Cue0002";

	private static readonly string Ans0003Name = "RanRomAnevChpt03Dial001Ans0003";

	private static readonly string Cue0003Name = "RanRomAnevChpt03Dial001Cue0003";

	private static readonly string Ans0004Name = "RanRomAnevChpt03Dial001Ans0004";

	private static readonly string Cue0004Name = "RanRomAnevChpt03Dial001Cue0004";

	private static readonly string Ans0005Name = "RanRomAnevChpt03Dial001Ans0005";

	private static readonly string Cue0005Name = "RanRomAnevChpt03Dial001Cue0005";

	private static readonly string Ans0006Name = "RanRomAnevChpt03Dial001Ans0006";

	private static readonly string Cue0006Name = "RanRomAnevChpt03Dial001Cue0006";

	private static readonly string Ans0007Name = "RanRomAnevChpt03Dial001Ans0007";

	private static readonly string Cue0007Name = "RanRomAnevChpt03Dial001Cue0007";

	private static readonly string Ans0008Name = "RanRomAnevChpt03Dial001Ans0008";

	private static readonly string Cue0008Name = "RanRomAnevChpt03Dial001Cue0008";

	private static readonly string Ans0009Name = "RanRomAnevChpt03Dial001Ans0009";

	private static readonly string Cue0009Name = "RanRomAnevChpt03Dial001Cue0009";

	private static readonly string Ans0010Name = "RanRomAnevChpt03Dial001Ans0010";

	private static readonly string Cue0010Name = "RanRomAnevChpt03Dial001Cue0010";

	public static string Configure()
	{
		//IL_0089: Unknown result type (might be due to invalid IL or missing references)
		//IL_0090: Expected O, but got Unknown
		//IL_0699: Unknown result type (might be due to invalid IL or missing references)
		//IL_06a0: Expected O, but got Unknown
		//IL_0793: Unknown result type (might be due to invalid IL or missing references)
		//IL_079a: Expected O, but got Unknown
		//IL_0858: Unknown result type (might be due to invalid IL or missing references)
		//IL_085f: Expected O, but got Unknown
		//IL_085f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0866: Expected O, but got Unknown
		//IL_0872: Unknown result type (might be due to invalid IL or missing references)
		//IL_0877: Unknown result type (might be due to invalid IL or missing references)
		//IL_088e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0b84: Unknown result type (might be due to invalid IL or missing references)
		//IL_0b8b: Expected O, but got Unknown
		//IL_0b8b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0b92: Expected O, but got Unknown
		//IL_0b9a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0b9f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0bb6: Unknown result type (might be due to invalid IL or missing references)
		//IL_0bbb: Unknown result type (might be due to invalid IL or missing references)
		//IL_0bc2: Expected O, but got Unknown
		//IL_0bc2: Unknown result type (might be due to invalid IL or missing references)
		//IL_0bc9: Expected O, but got Unknown
		//IL_0bd1: Unknown result type (might be due to invalid IL or missing references)
		//IL_0bd6: Unknown result type (might be due to invalid IL or missing references)
		//IL_0bed: Unknown result type (might be due to invalid IL or missing references)
		string text = "f36eb28e514147d3a9e2217ee7d30ddb";
		string text2 = "317b13ef5732425e8069ffa0c8cc512f";
		string text3 = "559e2aa664364376ad8c2e3147d6fdcf";
		string text4 = "7d3e267cd11744d591dd89d95de3f71b";
		string text5 = "30d8a3b6f8f949feaff81aa82d34486e";
		string text6 = "8e5521e343f14b58acf90463461e78f2";
		string text7 = "464440f178d6483aaae28e5a350631be";
		string text8 = "6ecc6879b9c644c1882882ed5d865655";
		string text9 = "43ff233169e146a78e3218bb47615784";
		string text10 = "df934651ff8846a99cc06cdd38e241d1";
		string text11 = "126b48d9dad94a5bbead2aedc0ec4aa6";
		string text12 = "ea8198c269ce4c93940640a389f6e7c8";
		string text13 = "8de9e133dfed4ac9837f0004844c4647";
		string text14 = "7d090c83df52473f92fd5c14b6728e34";
		string text15 = "669d1b5641f44cdeb809174236c05b9f";
		string text16 = "f925c61df21f43a2bb15515102d64e4d";
		string text17 = "afb03c12c19e4fc988d20d8a0388d8e1";
		string text18 = "d29eb6107e06491c879770c306ed65fa";
		string text19 = "a596d941c18b473ca56a8d82f59d4a03";
		string text20 = "00c3ffc2bd284241bc5681f5a5308088";
		PlayerCharacter val = new PlayerCharacter();
		((Element)val).name = "pcAnev";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "a837c3bc9cbb4e846ab5565915165c91", negate: true, null, true).EtudeStatus(null, null, "c922e0cbe25a0cf4dad4ce7a3ca81935", negate: true, null, true)
			.EtudeStatus(null, null, "739b9fe9b8998c641b4b3dfed40bc217", negate: true, null, true)
			.EtudeStatus(null, null, "20927a9471c00814b808fd69e88879c7", negate: true, null, true)
			.EtudeStatus(null, null, "a879a3a637a7eeb43b40677e4a8c4450", negate: false, null, true);
		ConditionsBuilder conditionsBuilder = ConditionsBuilder.New().EtudeStatus(null, null, "15e0048c7daf0ac4999c2313b58df0e3", negate: false, null, true).AnswerSelected(text5, null, negate: true)
			.AddOrAndLogic(conditions)
			.QuestStatus(negate: false, "c0d0b565f4b725241b96c148000f1910", (QuestState)2)
			.DialogSeen("c47ffdc9a62b40ac9648ce6006673cb8", negate: true)
			.DialogSeen("6ce0e47ee5b94576a60c607ec0fc063d", negate: true);
		ConditionsBuilder conditionsBuilder2 = ConditionsBuilder.New().EtudeStatus(null, null, "15e0048c7daf0ac4999c2313b58df0e3", negate: false, null, true).AnswerSelected(text7, null, negate: true)
			.AddOrAndLogic(conditions)
			.QuestStatus(negate: false, "9b99b2c1b0f8fd74390d4715e757ecce", (QuestState)2)
			.DialogSeen("c47ffdc9a62b40ac9648ce6006673cb8", negate: true)
			.DialogSeen("aca6f74af98549fab00bb1f82fa24878", negate: true);
		ConditionsBuilder conditionsBuilder3 = ConditionsBuilder.New().EtudeStatus(null, null, "15e0048c7daf0ac4999c2313b58df0e3", negate: false, null, true).AnswerSelected(text9, null, negate: true)
			.AddOrAndLogic(conditions)
			.CueSeen("7568521a8c3ae394a9da03b67a17aa7e");
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AddOrAndLogic(conditionsBuilder).AddOrAndLogic(conditionsBuilder2)
			.UseOr();
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AddOrAndLogic(conditions2).AddOrAndLogic(conditionsBuilder3, negate: true);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AddOrAndLogic(conditions2).AddOrAndLogic(conditionsBuilder3);
		ConditionsBuilder conditionsBuilder4 = ConditionsBuilder.New().EtudeStatus(null, null, "0e20d73ea0da6a94d94a6b42035a1ce0", negate: false, null, true).EtudeStatus(null, null, "e6669aad304206c4d969f6602e6b412e", negate: false, null, true)
			.QuestStatus(negate: false, "c21f4a2e26690a043b87339d95546f5e", (QuestState)2)
			.AnswerSelected(text11, null, negate: true)
			.AnswerSelected(text13, null, negate: true);
		ConditionsBuilder conditionsBuilder5 = ConditionsBuilder.New().EtudeStatus(null, null, "15e0048c7daf0ac4999c2313b58df0e3", negate: false, null, true).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val)
			.DialogSeen("6f77c7a835f74ec42b583ba4d1fe2dfc")
			.AnswerSelected(text11, null, negate: true)
			.AnswerSelected(text13, null, negate: true);
		ConditionsBuilder conditionsBuilder6 = ConditionsBuilder.New().EtudeStatus(null, null, "15e0048c7daf0ac4999c2313b58df0e3", negate: false, null, true).AnswerSelected(text15, null, negate: true);
		ConditionsBuilder conditionsBuilder7 = ConditionsBuilder.New().EtudeStatus(null, null, "15e0048c7daf0ac4999c2313b58df0e3", negate: false, null, true).AnswerSelected(text17, null, negate: true);
		ConditionsBuilder conditionsBuilder8 = ConditionsBuilder.New().EtudeStatus(null, null, "15e0048c7daf0ac4999c2313b58df0e3", negate: false, null, true).AnswerSelected(text19, null, negate: true);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AddOrAndLogic(conditionsBuilder).AddOrAndLogic(conditionsBuilder2)
			.AddOrAndLogic(conditionsBuilder3)
			.AddOrAndLogic(conditionsBuilder4)
			.AddOrAndLogic(conditionsBuilder5)
			.UseOr();
		DialogSpeaker val2 = new DialogSpeaker();
		val2.NoSpeaker = false;
		val2.MoveCamera = true;
		val2.NotRevealInFoW = false;
		val2.SwitchDual = false;
		AnswersListConfigurator.New("RanRomAnevChpt03Dial001list", "e9a90d89e6524214991ec7912bfc71dc").AddToAnswers(text5).AddToAnswers(text7)
			.AddToAnswers(text9)
			.AddToAnswers(text11)
			.AddToAnswers(text13)
			.AddToAnswers(text3)
			.Configure();
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAnevChpt03Dial001Cue0001.Text").SetSpeaker(val2)
			.SetAnswers("RanRomAnevChpt03Dial001list")
			.Configure();
		CueSelection val3 = new CueSelection();
		val3.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>(text2));
		SequenceExitConfigurator.New("RanRomAnevChpt03Dial001Exit", "871e69dedbec48cba3fa8472a1e217b2").SetContinueValue(val3).Configure();
		CueSequenceConfigurator.New("RanRomAnevChpt03Dial001Seq", "d19aa0bbc4594acf921e0af50acd7034").AddToCues(text6).AddToCues(text10)
			.AddToCues(text8)
			.AddToCues(text12)
			.AddToCues(text14)
			.SetExit("871e69dedbec48cba3fa8472a1e217b2")
			.Configure();
		CueSelection val4 = new CueSelection();
		BlueprintCueBaseReference val5 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("d19aa0bbc4594acf921e0af50acd7034")).deserializedGuid;
		val4.Cues.Add(val5);
		val4.Strategy = (Strategy)0;
		ActionsBuilder actionsBuilder = ActionsBuilder.New().StartDialog(null, "6ce0e47ee5b94576a60c607ec0fc063d");
		ActionsBuilder actionsBuilder2 = ActionsBuilder.New().StartDialog(null, "aca6f74af98549fab00bb1f82fa24878");
		ActionsBuilder actionsBuilder3 = ActionsBuilder.New().StartDialog(null, "c47ffdc9a62b40ac9648ce6006673cb8");
		ActionsBuilder actionsBuilder4 = ActionsBuilder.New().StartDialog(null, "2936ff4e6e234702b7f59b469b57feaa");
		ActionsBuilder onSelect = ActionsBuilder.New().UnmarkAnswersSelected(text);
		AnswerConfigurator.New(Ans0001Name, text).SetShowConditions(showConditions).SetText("RanRomAnevChpt03Dial001Ans0001.Text")
			.SetNextCue(val4)
			.SetOnSelect(onSelect)
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetText("RanRomAnevChpt03Dial001Ans0002.Text").Configure();
		CueConfigurator.New(Cue0002Name, text4).SetText("RanRomAnevChpt03Dial001Cue0002.Text").SetSpeaker(val2)
			.SetAnswers("33960c7f7af40cd43b7f801a76c87a0b")
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text5).SetShowConditions(conditionsBuilder).SetShowOnce()
			.SetText("RanRomAnevChpt03Dial001Ans0003.Text")
			.Configure();
		CueConfigurator.New(Cue0003Name, text6).SetConditions(conditions3).SetText("RanRomAnevChpt03Dial001Cue0003.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text7).SetShowConditions(conditionsBuilder2).SetShowOnce()
			.SetText("RanRomAnevChpt03Dial001Ans0004.Text")
			.Configure();
		CueConfigurator.New(Cue0004Name, text8).SetConditions(conditions4).SetText("RanRomAnevChpt03Dial001Cue0004.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text9).SetShowConditions(conditionsBuilder3).SetShowOnce()
			.SetText("RanRomAnevChpt03Dial001Ans0005.Text")
			.Configure();
		CueConfigurator.New(Cue0005Name, text10).SetConditions(conditionsBuilder3).SetText("RanRomAnevChpt03Dial001Cue0005.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0006Name, text11).SetShowConditions(conditionsBuilder4).SetShowOnce()
			.SetText("RanRomAnevChpt03Dial001Ans0006.Text")
			.Configure();
		CueConfigurator.New(Cue0006Name, text12).SetConditions(conditionsBuilder4).SetText("RanRomAnevChpt03Dial001Cue0006.Text")
			.SetSpeaker(val2)
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text13).SetShowConditions(conditionsBuilder5).SetShowOnce()
			.SetText("RanRomAnevChpt03Dial001Ans0007.Text")
			.Configure();
		CueConfigurator.New(Cue0007Name, text14).SetConditions(conditionsBuilder5).SetText("RanRomAnevChpt03Dial001Cue0007.Text")
			.SetSpeaker(val2)
			.Configure();
		CueSelection val6 = new CueSelection();
		BlueprintCueBaseReference val7 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val7).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text2)).deserializedGuid;
		val6.Cues.Add(val7);
		val6.Strategy = (Strategy)0;
		CueSelection val8 = new CueSelection();
		BlueprintCueBaseReference val9 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val9).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text4)).deserializedGuid;
		val8.Cues.Add(val9);
		val8.Strategy = (Strategy)0;
		AnswerConfigurator.For(text3).SetNextCue(val8).Configure();
		return "";
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
