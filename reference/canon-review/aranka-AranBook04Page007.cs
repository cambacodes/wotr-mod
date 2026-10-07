using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook04Page007
{
	private static readonly string PageName = "RanRomAranBook04Page007";

	private static readonly string Cue0001Name = "RanRomAranBook04Page007Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook04Page007Ans0002";

	private static readonly string Cue0002Name = "RanRomAranBook04Page007Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook04Page007Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook04Page007Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook04Page007Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook04Page007Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook04Page007Ans0005";

	private static readonly string Cue0005Name = "RanRomAranBook04Page007Cue0005";

	private static readonly string Ans0006Name = "RanRomAranBook04Page007Ans0006";

	private static readonly string Ans0007Name = "RanRomAranBook04Page007Ans0007";

	public static string Configure()
	{
		//IL_02d1: Unknown result type (might be due to invalid IL or missing references)
		//IL_02d8: Expected O, but got Unknown
		//IL_02d8: Unknown result type (might be due to invalid IL or missing references)
		//IL_02df: Expected O, but got Unknown
		//IL_02eb: Unknown result type (might be due to invalid IL or missing references)
		//IL_02f0: Unknown result type (might be due to invalid IL or missing references)
		//IL_0307: Unknown result type (might be due to invalid IL or missing references)
		//IL_030c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0313: Expected O, but got Unknown
		//IL_0313: Unknown result type (might be due to invalid IL or missing references)
		//IL_031a: Expected O, but got Unknown
		//IL_0326: Unknown result type (might be due to invalid IL or missing references)
		//IL_032b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0342: Unknown result type (might be due to invalid IL or missing references)
		string text = "30231c52e6654f12b23fdbdecfe98931";
		string text2 = "5c7171b9654448f3a301d2c755ab41d0";
		string text3 = "ffe235e5dd1548199fd7897bc6e95578";
		string text4 = "970194bb71b94298bdc864b31268ad30";
		string text5 = "dab0adee0c5d4743911c88f9f69bd0e2";
		string text6 = "7cb15a0402f14e75876538b3ef85316d";
		string text7 = "a571fe1730a54ff380ceb3d51898516d";
		string text8 = "c97296d85989417f9a5cc57996559a2e";
		string text9 = "bab0b5f03adc4ea7a77d471d14b9cd57";
		string text10 = "cfda5bd67c5d409f9667cf5de74b6b2a";
		string text11 = "0f925d8224ed46eda99134c93d54a77a";
		string text12 = "3dc28de79a974579a708e5e07cfe72cd";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranAlurFlirt", negate: false, null, true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder showConditions3 = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text9);
		ConditionsBuilder showConditions4 = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder showConditions5 = ConditionsBuilder.New().AnswerSelected(text3);
		BookPageConfigurator.New(PageName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text4)
			.AddToAnswers(text3)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToCues(text10)
			.AddToAnswers(text9)
			.AddToAnswers(text11)
			.AddToAnswers(text12)
			.SetConditions(conditions)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Page008")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook04Page007Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowOnce().SetText("RanRomAranBook04Page007Ans0002.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetConditions(conditions2).SetText("RanRomAranBook04Page007Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text5).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook04Page007Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text6).SetConditions(conditions3).SetText("RanRomAranBook04Page007Cue0003.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text7).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranBook04Page007Ans0004.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0004Name, text8).SetConditions(conditions4).SetText("RanRomAranBook04Page007Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text9).SetShowConditions(showConditions3).SetShowOnce()
			.SetText("RanRomAranBook04Page007Ans0005.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0005Name, text10).SetConditions(conditions5).SetText("RanRomAranBook04Page007Cue0005.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0006Name, text11).SetShowConditions(showConditions4).SetShowOnce()
			.SetText("RanRomAranBook04Page007Ans0006.Text")
			.SetNextCue(val3)
			.SetOnSelect(ActionsBuilder.New().StartEtude("RanRomAranAlurRomance"))
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text12).SetShowConditions(showConditions5).SetShowOnce()
			.SetText("RanRomAranBook04Page007Ans0007.Text")
			.SetNextCue(val3)
			.SetOnSelect(ActionsBuilder.New().CompleteEtude("RanRomAranAlurFlirt"))
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
