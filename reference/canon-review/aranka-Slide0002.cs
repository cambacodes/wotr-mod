using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;

namespace RanRomance.Aran;

public class Slide0002
{
	private static readonly string SlideName = "RanRomAranSlide0002";

	private static readonly string Cue0001Name = "RanRomAranSlide0002Cue0001";

	private static readonly string Cue0002Name = "RanRomAranSlide0002Cue0002";

	private static readonly string Cue0003Name = "RanRomAranSlide0002Cue0003";

	private static readonly string Cue0004Name = "RanRomAranSlide0002Cue0004";

	private static readonly string Cue0005Name = "RanRomAranSlide0002Cue0005";

	private static readonly string Cue0006Name = "RanRomAranSlide0002Cue0006";

	public static string Configure()
	{
		string text = "4f17f3eefe374b5b8c8c98012f7f8322";
		string text2 = "9d18a95ed6654f2fb7cc0a169f2605f8";
		string text3 = "f9913d0397384fc29a310c02bd9db74a";
		string text4 = "905d0a52b7cc448aa9fc0d89321cd7cb";
		string text5 = "4ab2f0b947e444bfa9e5192f9d3a1db7";
		string text6 = "9c44b02266bd4e2ea0b2a34cc2a766c2";
		string text7 = "7a345c9e6fb44e25a2b24493cb124240";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "07ad18ffb08145b69522f8eee0230857", negate: false, null, true).EtudeStatus(null, null, "9fc5161813f1497f8eaad1563ac54211", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().DialogSeen("RanRomAranBook04").EtudeStatus(null, null, "RanRomAranAzata", negate: false, null, true)
			.AddOrAndLogic(conditions);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true).EtudeStatus(null, null, "RanRomAranAlurRomance", negate: false, null, true);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true).EtudeStatus(null, null, "RanRomAranAlurRomance", negate: true, null, true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true).EtudeStatus(null, null, "6a3fdd0758fe78d4aa2c3b26d7614fbc", negate: false, null, true);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: true, null, true);
		BookPageConfigurator.New(SlideName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/aranrom/wings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text5)
			.AddToCues(text6)
			.AddToCues(text7)
			.SetConditions(conditions2)
			.AddToCues("RanRomFiller")
			.AddToAnswers("1afb887108b34ac1b082dabf64a786b6")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranSlide0002Cue0001.Text").SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions3).SetText("RanRomAranSlide0002Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions4).SetText("RanRomAranSlide0002Cue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions5).SetText("RanRomAranSlide0002Cue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text6).SetConditions(conditions6).SetText("RanRomAranSlide0002Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text7).SetConditions(conditions7).SetText("RanRomAranSlide0002Cue0006.Text")
			.SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
