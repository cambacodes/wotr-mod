using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook04Page006
{
	private static readonly string PageName = "RanRomAranBook04Page006";

	private static readonly string Cue0001Name = "RanRomAranBook04Page006Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook04Page006Cue0002";

	private static readonly string Cue0003Name = "RanRomAranBook04Page006Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook04Page006Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook04Page006Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook04Page006Ans0005";

	private static readonly string Cue0005Name = "RanRomAranBook04Page006Cue0005";

	private static readonly string Ans0006Name = "RanRomAranBook04Page006Ans0006";

	private static readonly string Cue0006Name = "RanRomAranBook04Page006Cue0006";

	private static readonly string Cue0007Name = "RanRomAranBook04Page006Cue0007";

	private static readonly string Ans0008Name = "RanRomAranBook04Page006Ans0008";

	public static string Configure()
	{
		//IL_027f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0286: Expected O, but got Unknown
		//IL_0286: Unknown result type (might be due to invalid IL or missing references)
		//IL_028d: Expected O, but got Unknown
		//IL_0299: Unknown result type (might be due to invalid IL or missing references)
		//IL_029e: Unknown result type (might be due to invalid IL or missing references)
		//IL_02b5: Unknown result type (might be due to invalid IL or missing references)
		//IL_02ba: Unknown result type (might be due to invalid IL or missing references)
		//IL_02c1: Expected O, but got Unknown
		//IL_02c1: Unknown result type (might be due to invalid IL or missing references)
		//IL_02c8: Expected O, but got Unknown
		//IL_02c8: Unknown result type (might be due to invalid IL or missing references)
		//IL_02cf: Expected O, but got Unknown
		//IL_02db: Unknown result type (might be due to invalid IL or missing references)
		//IL_02e0: Unknown result type (might be due to invalid IL or missing references)
		//IL_02f1: Unknown result type (might be due to invalid IL or missing references)
		//IL_02f6: Unknown result type (might be due to invalid IL or missing references)
		//IL_031c: Unknown result type (might be due to invalid IL or missing references)
		string text = "5aeed9b4211a4d29b03137828a1aef4f";
		string text2 = "011c15fef41e4d898a7c230317aae7f4";
		string text3 = "61c9db58870046e4921925f06d45c479";
		string text4 = "e4f679c12c4641d9928331ef175534ae";
		string text5 = "d0016c6a9e024d92b87f15389b9b0a8c";
		string text6 = "db5b1fff0af5491a992efa554b0e8d39";
		string text7 = "eabcc0db9f4f42d9822d078d53d1b2b7";
		string text8 = "6b9cfcc2310e40f5be3598466ef9e91b";
		string text9 = "8589a5841fac4c97a27af8b9100f1555";
		string text10 = "7ed1e4ed44554b59a8b4576f301f2a8d";
		string text11 = "978ecc2a473f4f0eadb3e1fba68cd3a3";
		string text12 = "e60eda2c86ce400099552f16282c4a23";
		ConditionsBuilder conditions = ConditionsBuilder.New().CueSeen("dbfd1056436c4b0d8abaec9bc1cff4c0", null, negate: true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().CueSeen("dbfd1056436c4b0d8abaec9bc1cff4c0");
		ConditionsBuilder showConditions = ConditionsBuilder.New().CueSeen("dbfd1056436c4b0d8abaec9bc1cff4c0", null, negate: true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text9);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().EtudeStatus(null, null, "7fde872463d2d2647b159a733d40ea98", negate: false, null, true);
		BookPageConfigurator.New(PageName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToCues(text10)
			.AddToAnswers(text9)
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
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Page007")).deserializedGuid;
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Page008")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Cues.Add(val5);
		val3.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomAranBook04Page006Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomAranBook04Page006Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetText("RanRomAranBook04Page006Cue0003.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text5).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook04Page006Ans0004.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0004Name, text6).SetConditions(conditions3).SetText("RanRomAranBook04Page006Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text7).SetShowOnce().SetText("RanRomAranBook04Page006Ans0005.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0005Name, text8).SetConditions(conditions4).SetText("RanRomAranBook04Page006Cue0005.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0006Name, text9).SetShowOnce().SetText("RanRomAranBook04Page006Ans0006.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0006Name, text10).SetConditions(conditions5).SetText("RanRomAranBook04Page006Cue0006.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0007Name, text11).SetConditions(conditions6).SetText("RanRomAranBook04Page006Cue0007.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0008Name, text12).SetShowOnce().SetText("RanRomAranBook04Page006Ans0008.Text")
			.SetNextCue(val3)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
