using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook14Page004
{
	private static readonly string PageName = "RanRomAranBook14Page004";

	private static readonly string Cue0001Name = "RanRomAranBook14Page004Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook14Page004Ans0002";

	private static readonly string Cue0002Name = "RanRomAranBook14Page004Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook14Page004Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook14Page004Cue0003";

	private static readonly string Cue0004Name = "RanRomAranBook14Page004Cue0004";

	private static readonly string Cue0005Name = "RanRomAranBook14Page004Cue0005";

	private static readonly string Ans0006Name = "RanRomAranBook14Page004Ans0006";

	private static readonly string Cue0006Name = "RanRomAranBook14Page004Cue0006";

	private static readonly string Ans0007Name = "RanRomAranBook14Page004Ans0007";

	public static string Configure()
	{
		//IL_0240: Unknown result type (might be due to invalid IL or missing references)
		//IL_0247: Expected O, but got Unknown
		//IL_0247: Unknown result type (might be due to invalid IL or missing references)
		//IL_024e: Expected O, but got Unknown
		//IL_025a: Unknown result type (might be due to invalid IL or missing references)
		//IL_025f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0276: Unknown result type (might be due to invalid IL or missing references)
		//IL_027b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0282: Expected O, but got Unknown
		//IL_0282: Unknown result type (might be due to invalid IL or missing references)
		//IL_0289: Expected O, but got Unknown
		//IL_0295: Unknown result type (might be due to invalid IL or missing references)
		//IL_029a: Unknown result type (might be due to invalid IL or missing references)
		//IL_02b1: Unknown result type (might be due to invalid IL or missing references)
		string text = "2f5e70ed81fc4284b39c283623a8c945";
		string text2 = "5af7e83c7c0645db8af34353f498789d";
		string text3 = "6e26cde0b2bb47ef8d2e46df41c5b956";
		string text4 = "d11250697b204dea9e62466dab740ad7";
		string text5 = "0d5c2debc2094ba498ce416ad35e710c";
		string text6 = "249daaa2f54a4ab497980fb920e5462f";
		string text7 = "ddad0a0d0b8841ea864fe314c4137e24";
		string text8 = "1907daca5dc14b77aa02565a20114134";
		string text9 = "565f2ed5e0b64072b458c2217f2dac8a";
		string text10 = "534179c80f414bed96a7232044abf752";
		string text11 = "d6ba4d334fce43f18478737fe02d7dc9";
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text5).QuestStatus(negate: false, "2865e4ea685865d43bccb36c3d58ee1c", (QuestState)2);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text5).QuestStatus(negate: true, "2865e4ea685865d43bccb36c3d58ee1c", (QuestState)2);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text9);
		BookPageConfigurator.New(PageName, text).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text4)
			.AddToAnswers(text3)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text7)
			.AddToCues(text8)
			.AddToCues(text10)
			.AddToAnswers(text9)
			.AddToAnswers(text11)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook14End")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook14Page004Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowOnce().SetText("RanRomAranBook14Page004Ans0002.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetConditions(conditions).SetText("RanRomAranBook14Page004Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text5).SetShowOnce().SetText("RanRomAranBook14Page004Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text6).SetConditions(conditions2).SetText("RanRomAranBook14Page004Cue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text7).SetConditions(conditions3).SetText("RanRomAranBook14Page004Cue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text8).SetConditions(conditions4).SetText("RanRomAranBook14Page004Cue0005.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0006Name, text9).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook14Page004Ans0006.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0006Name, text10).SetConditions(conditions5).SetText("RanRomAranBook14Page004Cue0006.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text11).SetShowOnce().SetText("RanRomAranBook14Page004Ans0007.Text")
			.SetNextCue(val3)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
