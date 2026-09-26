using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook04Azata
{
	private static readonly string PageName = "RanRomAranBook04Azata";

	private static readonly string Cue0001Name = "RanRomAranBook04AzataCue0001";

	private static readonly string Cue0002Name = "RanRomAranBook04AzataCue0002";

	private static readonly string Cue0003Name = "RanRomAranBook04AzataCue0003";

	private static readonly string Cue0004Name = "RanRomAranBook04AzataCue0004";

	public static string Configure()
	{
		//IL_01c6: Unknown result type (might be due to invalid IL or missing references)
		//IL_01cd: Expected O, but got Unknown
		//IL_01cd: Unknown result type (might be due to invalid IL or missing references)
		//IL_01d4: Expected O, but got Unknown
		//IL_01e0: Unknown result type (might be due to invalid IL or missing references)
		//IL_01e5: Unknown result type (might be due to invalid IL or missing references)
		//IL_01fc: Unknown result type (might be due to invalid IL or missing references)
		string text = "be8fec3ffe754246a07095c78fdf7621";
		string text2 = "22bd10fea4714daa8c4ac984041545d6";
		string text3 = "61461d05999b46218e7700e6596243b5";
		string text4 = "363860bffda1404db6ec996384fe2f26";
		string text5 = "43936228f4614272a7c7e25ebaaec2c7";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranAlurRomance", negate: false, null, true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranAlurRomance", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: true, null, true);
		BookPageConfigurator.New(PageName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/aranrom/wings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text5)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook04AzataCue0001.Text").SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions).SetText("RanRomAranBook04AzataCue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions2).SetText("RanRomAranBook04AzataCue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions3).SetText("RanRomAranBook04AzataCue0004.Text")
			.SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
