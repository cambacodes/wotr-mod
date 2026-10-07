using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook01End
{
	private static readonly string PageName = "RanRomAranBook01End";

	private static readonly string PageName2 = "RanRomAranBook01End2";

	private static readonly string Cue0001Name = "RanRomAranBook01EndCue0001";

	private static readonly string Cue0002Name = "RanRomAranBook01EndCue0002";

	private static readonly string Cue0003Name = "RanRomAranBook01EndCue0003";

	public static string Configure()
	{
		//IL_0200: Unknown result type (might be due to invalid IL or missing references)
		//IL_0207: Expected O, but got Unknown
		//IL_0207: Unknown result type (might be due to invalid IL or missing references)
		//IL_020e: Expected O, but got Unknown
		//IL_021a: Unknown result type (might be due to invalid IL or missing references)
		//IL_021f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0236: Unknown result type (might be due to invalid IL or missing references)
		string text = "d61664af13144728b43d850f4b879403";
		string guid = "cf26695589dd47b0950b9cfc5e4bca0b";
		string text2 = "7e8f7d9037864ddbbf2857373c472785";
		string text3 = "7bbda77bcd22447f9e3684d2e9a76ad5";
		string text4 = "4a886661ae9d47e3a84f71d23299a939";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "0e20d73ea0da6a94d94a6b42035a1ce0", negate: false, null, true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranFlirt", negate: true, null, true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranFlirt", negate: false, null, true);
		BookPageConfigurator.New(PageName, text).SetImageLink("f96ad5fa9c59d7549adff4c90f0703ab").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.SetConditions(conditions)
			.AddToCues("RanRomFiller")
			.Configure();
		BookPageConfigurator.New(PageName2, guid).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook01EndCue0001.Text").SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomAranBook01EndCue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions3).SetText("RanRomAranBook01EndCue0003.Text")
			.SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
