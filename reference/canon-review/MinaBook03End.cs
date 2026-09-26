using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Mina;

public class MinaBook03End
{
	private static readonly string PageName = "RanRomMinaBook03End";

	private static readonly string Cue0001Name = "RanRomMinaBook03EndCue0001";

	private static readonly string Cue0002Name = "RanRomMinaBook03EndCue0002";

	private static readonly string Cue0003Name = "RanRomMinaBook03EndCue0003";

	private static readonly string Cue0004Name = "RanRomMinaBook03EndCue0004";

	private static readonly string Cue0005Name = "RanRomMinaBook03EndCue0005";

	private static readonly string Cue0006Name = "RanRomMinaBook03EndCue0006";

	private static readonly string Cue0007Name = "RanRomMinaBook03EndCue0007";

	public static string Configure()
	{
		//IL_0550: Unknown result type (might be due to invalid IL or missing references)
		//IL_0557: Expected O, but got Unknown
		//IL_0557: Unknown result type (might be due to invalid IL or missing references)
		//IL_055e: Expected O, but got Unknown
		//IL_056a: Unknown result type (might be due to invalid IL or missing references)
		//IL_056f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0586: Unknown result type (might be due to invalid IL or missing references)
		string text = "f9c0ac1a434e450293c244ffc6a54a9f";
		string text2 = "19099aba216e46e98d446709c3f2e0f3";
		string text3 = "5584da70433e4f079d521d40ce77f230";
		string text4 = "c01f7f83a2584555b2f551918f169cdb";
		string text5 = "4dbb41f1fb134b90ab3900dc05488e8f";
		string text6 = "c51a76731dc24865b6c472ffe6bf3e18";
		string text7 = "341b62dd58d14906959d3262b12f1a43";
		string text8 = "98baa5299ae444bfa1ac8ba8e84f2c7c";
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected("56056c49915d468e9a6b469260dd42b3", null, negate: true).AnswerSelected("fd4e6bbef0d4445b8bee465524698520", null, negate: true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaDragon", negate: false, null, true).EtudeStatus(null, null, "RanRomMinaLegend", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomMinaRedemption", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AddOrAndLogic(conditions2).AnswerSelected("56056c49915d468e9a6b469260dd42b3");
		ConditionsBuilder conditions4 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaDemon", negate: false, null, true).AnswerSelected("56056c49915d468e9a6b469260dd42b3");
		ConditionsBuilder conditions5 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaDragon", negate: true, null, true).EtudeStatus(null, null, "RanRomMinaLegend", negate: true, null, true)
			.EtudeStatus(null, null, "RanRomMinaRedemption", negate: true, null, true)
			.EtudeStatus(null, null, "RanRomMinaDemon", negate: true, null, true)
			.AnswerSelected("56056c49915d468e9a6b469260dd42b3");
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AddOrAndLogic(conditions2).AnswerSelected("fd4e6bbef0d4445b8bee465524698520");
		ConditionsBuilder conditions7 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaDemon", negate: false, null, true).AnswerSelected("fd4e6bbef0d4445b8bee465524698520");
		ConditionsBuilder conditions8 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaDragon", negate: true, null, true).EtudeStatus(null, null, "RanRomMinaLegend", negate: true, null, true)
			.EtudeStatus(null, null, "RanRomMinaRedemption", negate: true, null, true)
			.EtudeStatus(null, null, "RanRomMinaDemon", negate: true, null, true)
			.AnswerSelected("fd4e6bbef0d4445b8bee465524698520");
		BookPageConfigurator.New(PageName, text).SetImageLink("482f509e50aa6484bafee746ddb3849f").SetForeImageLink("1abecb015eedf484eab1b0229a7cecf7")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text5)
			.AddToCues(text6)
			.AddToCues(text7)
			.AddToCues(text8)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomMinaBook03EndCue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions3).SetText("RanRomMinaBook03EndCue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions4).SetText("RanRomMinaBook03EndCue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions5).SetText("RanRomMinaBook03EndCue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text6).SetConditions(conditions6).SetText("RanRomMinaBook03EndCue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text7).SetConditions(conditions7).SetText("RanRomMinaBook03EndCue0006.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0007Name, text8).SetConditions(conditions8).SetText("RanRomMinaBook03EndCue0007.Text")
			.SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
