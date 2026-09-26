using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook14Page001
{
	private static readonly string PageName = "RanRomAranBook14Page001";

	private static readonly string Cue0001Name = "RanRomAranBook14Page001Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook14Page001Ans0002";

	private static readonly string Cue0002Name = "RanRomAranBook14Page001Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook14Page001Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook14Page001Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook14Page001Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook14Page001Cue0004";

	private static readonly string Cue0005Name = "RanRomAranBook14Page001Cue0005";

	private static readonly string Cue0006Name = "RanRomAranBook14Page001Cue0006";

	private static readonly string Cue0007Name = "RanRomAranBook14Page001Cue0007";

	private static readonly string Ans0008Name = "RanRomAranBook14Page001Ans0008";

	public static string Configure()
	{
		//IL_0334: Unknown result type (might be due to invalid IL or missing references)
		//IL_033b: Expected O, but got Unknown
		//IL_033b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0342: Expected O, but got Unknown
		//IL_034e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0353: Unknown result type (might be due to invalid IL or missing references)
		//IL_036a: Unknown result type (might be due to invalid IL or missing references)
		//IL_036f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0376: Expected O, but got Unknown
		//IL_0376: Unknown result type (might be due to invalid IL or missing references)
		//IL_037d: Expected O, but got Unknown
		//IL_037d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0384: Expected O, but got Unknown
		//IL_0384: Unknown result type (might be due to invalid IL or missing references)
		//IL_038b: Expected O, but got Unknown
		//IL_0397: Unknown result type (might be due to invalid IL or missing references)
		//IL_039c: Unknown result type (might be due to invalid IL or missing references)
		//IL_03ad: Unknown result type (might be due to invalid IL or missing references)
		//IL_03b2: Unknown result type (might be due to invalid IL or missing references)
		//IL_03c3: Unknown result type (might be due to invalid IL or missing references)
		//IL_03c8: Unknown result type (might be due to invalid IL or missing references)
		//IL_03fd: Unknown result type (might be due to invalid IL or missing references)
		string text = "fc18390e231648bab036124ac5108772";
		string text2 = "5ad8c429020b4baead019d15c819aa55";
		string text3 = "3c746b361ab6426e8e9a4d1fd6dfc81c";
		string text4 = "6e2f415f75e741649410a82eca4e3ade";
		string text5 = "cfb17c7f14dc40b99f53dd400e4066ff";
		string text6 = "52120e7ce1bb4d399964cf80762276dd";
		string text7 = "1c25291fa8524e2bbcaf998cc23678ad";
		string text8 = "3259bb9b44ac473da5dff5e674c70967";
		string text9 = "f3f713abf7fa4578a97ebf89dce24111";
		string text10 = "7962bb86e03748688be9b1101220ad75";
		string text11 = "bddc857e84e347a88b9803515fb5a7b8";
		string text12 = "324c02306a924aa5a2bced2251288c6e";
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text7).QuestStatus(negate: false, "2865e4ea685865d43bccb36c3d58ee1c", (QuestState)2);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text7).QuestStatus(negate: true, "2865e4ea685865d43bccb36c3d58ee1c", (QuestState)2);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text7).EtudeStatus(null, null, "7fde872463d2d2647b159a733d40ea98", negate: false, null, true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected(text7).EtudeStatus(null, null, "7fde872463d2d2647b159a733d40ea98", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text7);
		BookPageConfigurator.New(PageName, text).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text4)
			.AddToAnswers(text3)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToCues(text9)
			.AddToCues(text10)
			.AddToCues(text11)
			.AddToAnswers(text12)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		BlueprintCueBaseReference val5 = new BlueprintCueBaseReference();
		BlueprintCueBaseReference val6 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook14Page002")).deserializedGuid;
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook14Page003")).deserializedGuid;
		((BlueprintReferenceBase)val6).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook14End")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Cues.Add(val5);
		val3.Cues.Add(val6);
		val3.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook14Page001Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowOnce().SetText("RanRomAranBook14Page001Ans0002.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetConditions(conditions).SetText("RanRomAranBook14Page001Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text5).SetShowOnce().SetText("RanRomAranBook14Page001Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text6).SetConditions(conditions2).SetText("RanRomAranBook14Page001Cue0003.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text7).SetShowOnce().SetText("RanRomAranBook14Page001Ans0004.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0004Name, text8).SetConditions(conditions3).SetText("RanRomAranBook14Page001Cue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text9).SetConditions(conditions4).SetText("RanRomAranBook14Page001Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text10).SetConditions(conditions5).SetText("RanRomAranBook14Page001Cue0006.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0007Name, text11).SetConditions(conditions6).SetText("RanRomAranBook14Page001Cue0007.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0008Name, text12).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook14Page001Ans0008.Text")
			.SetNextCue(val3)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
