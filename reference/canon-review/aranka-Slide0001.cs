using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;

namespace RanRomance.Aran;

public class Slide0001
{
	private static readonly string SlideName = "RanRomAranSlide0001";

	private static readonly string Cue0001Name = "RanRomAranSlide0001Cue0001";

	private static readonly string Cue0002Name = "RanRomAranSlide0001Cue0002";

	private static readonly string Cue0003Name = "RanRomAranSlide0001Cue0003";

	private static readonly string Cue0004Name = "RanRomAranSlide0001Cue0004";

	private static readonly string Cue0005Name = "RanRomAranSlide0001Cue0005";

	private static readonly string Cue0006Name = "RanRomAranSlide0001Cue0006";

	private static readonly string Cue0007Name = "RanRomAranSlide0001Cue0007";

	private static readonly string Cue0008Name = "RanRomAranSlide0001Cue0008";

	private static readonly string Cue0009Name = "RanRomAranSlide0001Cue0009";

	private static readonly string Cue0010Name = "RanRomAranSlide0001Cue0010";

	public static string Configure()
	{
		string text = "47b061d3a35d435cbcdaccc504561818";
		string text2 = "32301939b6e24e56891cfc66192b6db9";
		string text3 = "ea4d27bcc016468c9797417ff5415f68";
		string text4 = "c920ca38855e4219a668724168e4d95e";
		string text5 = "b50d04a6a4164e6992a97a5f32c57851";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranDevil", negate: false, null, true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: false, null, true).EtudeStatus(null, null, "5f72b252bd7fa8d48bd04c27982a4f9c", negate: false, null, true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "5f72b252bd7fa8d48bd04c27982a4f9c", negate: false, null, true)
			.EtudeStatus(null, null, "381a296094804761af0893d2e70dc2df", negate: true, null, true);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "5f72b252bd7fa8d48bd04c27982a4f9c", negate: false, null, true)
			.EtudeStatus(null, null, "381a296094804761af0893d2e70dc2df", negate: false, null, true);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().EtudeStatus(null, null, "5f72b252bd7fa8d48bd04c27982a4f9c", negate: true, null, true);
		BookPageConfigurator.New(SlideName, text).SetImageLink("f96ad5fa9c59d7549adff4c90f0703ab").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text5)
			.SetConditions(conditions)
			.AddToCues("RanRomFiller")
			.AddToAnswers("1afb887108b34ac1b082dabf64a786b6")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions2).SetText("RanRomAranSlide0001Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions3).SetText("RanRomAranSlide0001Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions4).SetText("RanRomAranSlide0001Cue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions5).SetText("RanRomAranSlide0001Cue0004.Text")
			.SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
