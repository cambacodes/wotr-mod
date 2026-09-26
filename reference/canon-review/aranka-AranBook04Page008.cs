using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook04Page008
{
	private static readonly string PageName = "RanRomAranBook04Page008";

	private static readonly string Cue0001Name = "RanRomAranBook04Page008Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook04Page008Cue0002";

	private static readonly string Cue0003Name = "RanRomAranBook04Page008Cue0003";

	private static readonly string Cue0004Name = "RanRomAranBook04Page008Cue0004";

	private static readonly string Cue0005Name = "RanRomAranBook04Page008Cue0005";

	private static readonly string Ans0006Name = "RanRomAranBook04Page008Ans0006";

	private static readonly string Cue0006Name = "RanRomAranBook04Page008Cue0006";

	private static readonly string Ans0007Name = "RanRomAranBook04Page008Ans0007";

	private static readonly string Cue0007Name = "RanRomAranBook04Page008Cue0007";

	private static readonly string Ans0008Name = "RanRomAranBook04Page008Ans0008";

	private static readonly string Cue0008Name = "RanRomAranBook04Page008Cue0008";

	private static readonly string Ans0009Name = "RanRomAranBook04Page008Ans0009";

	private static readonly string Cue0009Name = "RanRomAranBook04Page008Cue0009";

	private static readonly string Ans0000Name = "RanRomAranBook04Page008Ans0000";

	private static readonly string Ans0011Name = "RanRomAranBook04Page008Ans0011";

	public static string Configure()
	{
		//IL_037f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0386: Expected O, but got Unknown
		//IL_0386: Unknown result type (might be due to invalid IL or missing references)
		//IL_038d: Expected O, but got Unknown
		//IL_0399: Unknown result type (might be due to invalid IL or missing references)
		//IL_039e: Unknown result type (might be due to invalid IL or missing references)
		//IL_03b5: Unknown result type (might be due to invalid IL or missing references)
		//IL_03ba: Unknown result type (might be due to invalid IL or missing references)
		//IL_03c1: Expected O, but got Unknown
		//IL_03c1: Unknown result type (might be due to invalid IL or missing references)
		//IL_03c8: Expected O, but got Unknown
		//IL_03d4: Unknown result type (might be due to invalid IL or missing references)
		//IL_03d9: Unknown result type (might be due to invalid IL or missing references)
		//IL_03f0: Unknown result type (might be due to invalid IL or missing references)
		//IL_03f5: Unknown result type (might be due to invalid IL or missing references)
		//IL_03fc: Expected O, but got Unknown
		//IL_03fc: Unknown result type (might be due to invalid IL or missing references)
		//IL_0403: Expected O, but got Unknown
		//IL_040f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0414: Unknown result type (might be due to invalid IL or missing references)
		//IL_042b: Unknown result type (might be due to invalid IL or missing references)
		string text = "d056de4985c84d9394d9299051dacb77";
		string text2 = "e20f815dbd664d418c1ed87eb10793af";
		string text3 = "b644cb9ccc3544bd84c15736e8853b61";
		string text4 = "9e10b7df69b048d6af4e5b3ca7fde1d9";
		string text5 = "8adaad8eed0442d5aae55097eea402c4";
		string text6 = "321d5d307362431eaf902f644ae72a63";
		string text7 = "dacd0abe65a64b47aa1099cd38d4f6f8";
		string text8 = "1d9fd0a905954eaa89a09c2822b223c9";
		string text9 = "732d2cec6511436ca5f7ae5a246845fa";
		string text10 = "1e3862b4ae7846a9810cffcb516a7af4";
		string text11 = "1117a8e48a1542fcad459e8af61a15d7";
		string text12 = "1f9bee871418462091866b55e70cdd75";
		string text13 = "66c13df7b1db43029960791d3a7bff7b";
		string text14 = "44d2493f278249dcb10f935b8a0a8400";
		string text15 = "e9a4291e237f42369f77d18a5e31a7d5";
		string text16 = "17719f42b636424383107c22477b1062";
		ConditionsBuilder conditions = ConditionsBuilder.New().CueSeen("dbfd1056436c4b0d8abaec9bc1cff4c0", null, negate: true).CueSeen("e4f679c12c4641d9928331ef175534ae", null, negate: true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected("1fc901c8b72e4438a718d2e211dc60a3");
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected("3dc28de79a974579a708e5e07cfe72cd");
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected("0f925d8224ed46eda99134c93d54a77a");
		ConditionsBuilder conditions5 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true).CueSeen("5c7171b9654448f3a301d2c755ab41d0", null, negate: true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected(text9);
		ConditionsBuilder conditions8 = ConditionsBuilder.New().AnswerSelected(text11);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().AnswerSelected(text13);
		ConditionsBuilder showConditions = ConditionsBuilder.New().QuestStatus(negate: false, "2865e4ea685865d43bccb36c3d58ee1c", (QuestState)2);
		BookPageConfigurator.New(PageName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text5)
			.AddToCues(text6)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToCues(text10)
			.AddToAnswers(text9)
			.AddToCues(text12)
			.AddToAnswers(text11)
			.AddToCues(text14)
			.AddToAnswers(text13)
			.AddToAnswers(text15)
			.AddToAnswers(text16)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Azata")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueSelection val5 = new CueSelection();
		BlueprintCueBaseReference val6 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val6).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04End")).deserializedGuid;
		val5.Cues.Add(val6);
		val5.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomAranBook04Page008Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomAranBook04Page008Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions3).SetText("RanRomAranBook04Page008Cue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions4).SetText("RanRomAranBook04Page008Cue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text6).SetConditions(conditions5).SetText("RanRomAranBook04Page008Cue0005.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0006Name, text7).SetShowOnce().SetText("RanRomAranBook04Page008Ans0006.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0006Name, text8).SetConditions(conditions6).SetText("RanRomAranBook04Page008Cue0006.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text9).SetShowOnce().SetText("RanRomAranBook04Page008Ans0007.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0007Name, text10).SetConditions(conditions7).SetText("RanRomAranBook04Page008Cue0007.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0008Name, text11).SetShowOnce().SetText("RanRomAranBook04Page008Ans0008.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0008Name, text12).SetConditions(conditions8).SetText("RanRomAranBook04Page008Cue0008.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0009Name, text13).SetShowOnce().SetText("RanRomAranBook04Page008Ans0009.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0009Name, text14).SetConditions(conditions9).SetText("RanRomAranBook04Page008Cue0009.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0000Name, text15).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook04Page008Ans0000.Text")
			.SetOnSelect(ActionsBuilder.New().StartEtude("RanRomAranAzata"))
			.SetNextCue(val3)
			.Configure();
		AnswerConfigurator.New(Ans0011Name, text16).SetShowOnce().SetText("RanRomAranBook04Page008Ans0011.Text")
			.SetNextCue(val5)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
