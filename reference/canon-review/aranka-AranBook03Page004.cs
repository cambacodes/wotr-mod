using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Blueprints.References;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.BasicEx;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.DialogSystem;
using Kingmaker.ElementsSystem;

namespace RanRomance.Aran;

public class AranBook03Page004
{
	private static readonly string PageName = "RanRomAranBook03Page004";

	private static readonly string Cue0001Name = "RanRomAranBook03Page004Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook03Page004Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook03Page004Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook03Page004Cue0003";

	private static readonly string Cue0004Name = "RanRomAranBook03Page004Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook03Page004Ans0005";

	private static readonly string Cue0005Name = "RanRomAranBook03Page004Cue0005";

	private static readonly string Cue0006Name = "RanRomAranBook03Page004Cue0006";

	private static readonly string Ans0007Name = "RanRomAranBook03Page004Ans0007";

	private static readonly string Cue0007Name = "RanRomAranBook03Page004Cue0007";

	private static readonly string Cue0008Name = "RanRomAranBook03Page004Cue0008";

	private static readonly string Cue0009Name = "RanRomAranBook03Page004Cue0009";

	private static readonly string Ans0000Name = "RanRomAranBook03Page004Ans0000";

	public static string Configure()
	{
		//IL_005f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0066: Expected O, but got Unknown
		//IL_0534: Unknown result type (might be due to invalid IL or missing references)
		//IL_053b: Expected O, but got Unknown
		//IL_053b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0542: Expected O, but got Unknown
		//IL_054e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0553: Unknown result type (might be due to invalid IL or missing references)
		//IL_056a: Unknown result type (might be due to invalid IL or missing references)
		//IL_056f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0576: Expected O, but got Unknown
		//IL_0576: Unknown result type (might be due to invalid IL or missing references)
		//IL_057d: Expected O, but got Unknown
		//IL_057d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0584: Expected O, but got Unknown
		//IL_0590: Unknown result type (might be due to invalid IL or missing references)
		//IL_0595: Unknown result type (might be due to invalid IL or missing references)
		//IL_05a6: Unknown result type (might be due to invalid IL or missing references)
		//IL_05ab: Unknown result type (might be due to invalid IL or missing references)
		//IL_05d1: Unknown result type (might be due to invalid IL or missing references)
		string text = "9317f74874de4fe38bb68dacf9ca6b31";
		string text2 = "0c54987203ce4fb58a19283310619ee2";
		string text3 = "5bbdfedd2ffe4df1bf4c2a3f5ee30e77";
		string text4 = "e47e36618f1d4b40a01bdf751a00906d";
		string text5 = "a76283e6a3174938a88ca4d862567221";
		string text6 = "b8a9d6f9a90f4fe595607ec0dd271f04";
		string text7 = "5a6b4a5edfdf44efa2de745f57a905a3";
		string text8 = "847f3e5d66e64581a39f6de4d0d2b5fd";
		string text9 = "ed6ee13f7e9b4de2a6cd50dbbb1767c6";
		string text10 = "c984415112ea4e4fbeb464c5a7f2a89a";
		string text11 = "1d5197ae4e11481b9df99cf6a9d777ea";
		string text12 = "7b13e5166df64a3f884d6ecaa3b8c199";
		string text13 = "0b0509d22365495c838dde306cca17a3";
		string text14 = "c766227c6c964c0895b5666b5cbcadfb";
		PlayerCharacter val = new PlayerCharacter();
		((Element)val).name = "pc" + text;
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranFlirt", negate: false, null, true).EtudeStatus(null, null, "RanRomAranFlirtEnd", negate: true, null, true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().DialogSeen("ecec996948b1a83488e5bcadbaf1ac41", negate: true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().DialogSeen("ecec996948b1a83488e5bcadbaf1ac41");
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text4).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text4).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val);
		ConditionsBuilder showConditions = ConditionsBuilder.New().DialogSeen("ecec996948b1a83488e5bcadbaf1ac41", negate: true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected(text7).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected(text7).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().DialogSeen("ecec996948b1a83488e5bcadbaf1ac41");
		ConditionsBuilder conditions8 = ConditionsBuilder.New().AnswerSelected(text10).EtudeStatus(null, null, "5583802599dad444b832f96ff27561c8", negate: false, null, true, true);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().AnswerSelected(text10).EtudeStatus(null, null, "5583802599dad444b832f96ff27561c8", negate: false, null, true, true)
			.EtudeStatus(null, null, "2ac640b89675e084ea39f9f25125efd4", negate: true, null, true, true);
		ConditionsBuilder conditions10 = ConditionsBuilder.New().AnswerSelected(text10).EtudeStatus(null, null, "5583802599dad444b832f96ff27561c8", negate: true, null, true, true);
		BookPageConfigurator.New(PageName, text).SetImageLink("52163ec59b7bf62408b1b24137843bba").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text5)
			.AddToAnswers(text4)
			.AddToCues(text6)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToCues(text9)
			.AddToCues(text11)
			.AddToAnswers(text10)
			.AddToCues(text12)
			.AddToCues(text13)
			.AddToAnswers(text14)
			.SetConditions(conditions)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val2 = new CueSelection();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val2.Cues.Add(val3);
		val2.Strategy = (Strategy)0;
		CueSelection val4 = new CueSelection();
		BlueprintCueBaseReference val5 = new BlueprintCueBaseReference();
		BlueprintCueBaseReference val6 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook03Page005")).deserializedGuid;
		((BlueprintReferenceBase)val6).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook03Page006")).deserializedGuid;
		val4.Cues.Add(val5);
		val4.Cues.Add(val6);
		val4.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions2).SetText("RanRomAranBook03Page004Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions3).SetText("RanRomAranBook03Page004Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text4).SetShowOnce().SetText("RanRomAranBook03Page004Ans0003.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0003Name, text5).SetConditions(conditions4).SetText("RanRomAranBook03Page004Cue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text6).SetConditions(conditions5).SetText("RanRomAranBook03Page004Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text7).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook03Page004Ans0005.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0005Name, text8).SetConditions(conditions6).SetText("RanRomAranBook03Page004Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text9).SetConditions(conditions7).SetText("RanRomAranBook03Page004Cue0006.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text10).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranBook03Page004Ans0007.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0007Name, text11).SetConditions(conditions8).SetText("RanRomAranBook03Page004Cue0007.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0008Name, text12).SetConditions(conditions9).SetText("RanRomAranBook03Page004Cue0008.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0009Name, text13).SetConditions(conditions10).SetText("RanRomAranBook03Page004Cue0009.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0000Name, text14).SetShowOnce().SetText("RanRomAranBook03Page004Ans0000.Text")
			.SetNextCue(val4)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
