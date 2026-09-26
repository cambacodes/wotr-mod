using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook04Page003
{
	private static readonly string PageName = "RanRomAranBook04Page003";

	private static readonly string Cue0001Name = "RanRomAranBook04Page003Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook04Page003Ans0002";

	private static readonly string Cue0002Name = "RanRomAranBook04Page003Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook04Page003Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook04Page003Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook04Page003Ans0004";

	public static string Configure()
	{
		//IL_012c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0133: Expected O, but got Unknown
		//IL_0133: Unknown result type (might be due to invalid IL or missing references)
		//IL_013a: Expected O, but got Unknown
		//IL_0146: Unknown result type (might be due to invalid IL or missing references)
		//IL_014b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0162: Unknown result type (might be due to invalid IL or missing references)
		//IL_0167: Unknown result type (might be due to invalid IL or missing references)
		//IL_016e: Expected O, but got Unknown
		//IL_016e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0175: Expected O, but got Unknown
		//IL_0181: Unknown result type (might be due to invalid IL or missing references)
		//IL_0186: Unknown result type (might be due to invalid IL or missing references)
		//IL_019d: Unknown result type (might be due to invalid IL or missing references)
		string text = "d7061b61765b4d75a42a0117b3f4fa63";
		string text2 = "2c4027b7944346f5ae11a4b1f2fc1413";
		string text3 = "90154829de76427ca95a3cd58634c8d4";
		string text4 = "7fcf90d3eee348e0b955e0256b02dbcf";
		string text5 = "b17a736cc8884ee18f83b46ee3aafdc7";
		string text6 = "93cc5005ff084d3ea7c2ab35e795a503";
		string text7 = "ec352b1f8d844ae081420c383598965f";
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text5);
		BookPageConfigurator.New(PageName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text4)
			.AddToAnswers(text3)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToAnswers(text7)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Page004")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook04Page003Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowOnce().SetText("RanRomAranBook04Page003Ans0002.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetConditions(conditions).SetText("RanRomAranBook04Page003Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text5).SetShowOnce().SetText("RanRomAranBook04Page003Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text6).SetConditions(conditions2).SetText("RanRomAranBook04Page003Cue0003.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text7).SetShowOnce().SetText("RanRomAranBook04Page003Ans0004.Text")
			.SetNextCue(val3)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
