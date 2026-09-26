using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook01Page006
{
	private static readonly string PageName = "RanRomAranBook01Page006";

	private static readonly string PageName2 = "RanRomAranBook01Page106";

	private static readonly string Cue0001Name = "RanRomAranBook01Page006Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook01Page006Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook01Page006Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook01Page006Cue0003";

	public static string Configure()
	{
		//IL_01ec: Unknown result type (might be due to invalid IL or missing references)
		//IL_01f3: Expected O, but got Unknown
		//IL_01f3: Unknown result type (might be due to invalid IL or missing references)
		//IL_01fa: Expected O, but got Unknown
		//IL_01fa: Unknown result type (might be due to invalid IL or missing references)
		//IL_0201: Expected O, but got Unknown
		//IL_020d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0212: Unknown result type (might be due to invalid IL or missing references)
		//IL_0223: Unknown result type (might be due to invalid IL or missing references)
		//IL_0228: Unknown result type (might be due to invalid IL or missing references)
		//IL_024e: Unknown result type (might be due to invalid IL or missing references)
		string text = "48a8e0f34f6941f298ecb11102529795";
		string guid = "27f4ccaedff2421ebe47e990a2c1a7b3";
		string text2 = "14f90a00816e4bd3a49331166d5c85cc";
		string text3 = "662587c96d244cc4b7ab214a4a2529b1";
		string text4 = "c39d6af6857d4f2ab4564c7dbc9303c1";
		string text5 = "4aeb4b7421ec419fb2729e91c216c827";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "0e20d73ea0da6a94d94a6b42035a1ce0", negate: false, null, true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "0e20d73ea0da6a94d94a6b42035a1ce0", negate: true, null, true);
		BookPageConfigurator.New(PageName, text).SetImageLink("f96ad5fa9c59d7549adff4c90f0703ab").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text5)
			.AddToAnswers(text4)
			.SetConditions(conditions)
			.AddToCues("RanRomFiller")
			.Configure();
		BookPageConfigurator.New(PageName2, guid).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text5)
			.AddToAnswers(text4)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook01End")).deserializedGuid;
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook01End2")).deserializedGuid;
		val.Cues.Add(val2);
		val.Cues.Add(val3);
		val.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomAranBook01Page006Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomAranBook01Page006Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text4).SetShowOnce().SetText("RanRomAranBook01Page006Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text5).SetText("RanRomAranBook01Page006Cue0003.Text").SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
