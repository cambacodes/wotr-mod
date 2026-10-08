using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook03Page001
{
	private static readonly string PageName = "RanRomAranBook03Page001";

	private static readonly string Cue0001Name = "RanRomAranBook03Page001Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook03Page001Ans0002";

	private static readonly string Cue0002Name = "RanRomAranBook03Page001Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook03Page001Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook03Page001Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook03Page001Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook03Page001Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook03Page001Ans0005";

	public static string Configure()
	{
		//IL_019f: Unknown result type (might be due to invalid IL or missing references)
		//IL_01a6: Expected O, but got Unknown
		//IL_01a6: Unknown result type (might be due to invalid IL or missing references)
		//IL_01ad: Expected O, but got Unknown
		//IL_01b9: Unknown result type (might be due to invalid IL or missing references)
		//IL_01be: Unknown result type (might be due to invalid IL or missing references)
		//IL_01d5: Unknown result type (might be due to invalid IL or missing references)
		//IL_01da: Unknown result type (might be due to invalid IL or missing references)
		//IL_01e1: Expected O, but got Unknown
		//IL_01e1: Unknown result type (might be due to invalid IL or missing references)
		//IL_01e8: Expected O, but got Unknown
		//IL_01f4: Unknown result type (might be due to invalid IL or missing references)
		//IL_01f9: Unknown result type (might be due to invalid IL or missing references)
		//IL_0210: Unknown result type (might be due to invalid IL or missing references)
		string text = "63bd07a93543434a98dc5a5f1d34fd35";
		string text2 = "286b92d6cf274639b768b0371bedb618";
		string text3 = "29e5ed0f4b364d53b6a53375b8a6f754";
		string text4 = "26ce5d18b36a4481947e18ce36633c81";
		string text5 = "0849c62f1aa74df998b92e2a0ef46529";
		string text6 = "563ec5cf98c8480794e4d7e1f5d11d9d";
		string text7 = "bce4a745a73b44a89f9558bcd8f9dba9";
		string text8 = "47c1f5f1a19a47fba577e793934e3b63";
		string text9 = "7d797f4ee1bb41dd8c923e959463eec7";
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text7);
		BookPageConfigurator.New(PageName, text).SetImageLink("52163ec59b7bf62408b1b24137843bba").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text4)
			.AddToAnswers(text3)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToAnswers(text9)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook03Page002")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook03Page001Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowOnce().SetText("RanRomAranBook03Page001Ans0002.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetConditions(conditions).SetText("RanRomAranBook03Page001Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text5).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook03Page001Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text6).SetConditions(conditions2).SetText("RanRomAranBook03Page001Cue0003.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text7).SetShowOnce().SetText("RanRomAranBook03Page001Ans0004.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0004Name, text8).SetConditions(conditions3).SetText("RanRomAranBook03Page001Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text9).SetShowOnce().SetText("RanRomAranBook03Page001Ans0005.Text")
			.SetNextCue(val3)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
