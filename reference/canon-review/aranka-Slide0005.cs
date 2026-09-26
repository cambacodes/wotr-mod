using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;

namespace RanRomance.Aran;

public class Slide0005
{
	private static readonly string SlideName = "RanRomAranSlide0005";

	private static readonly string Cue0001Name = "RanRomAranSlide0005Cue0001";

	private static readonly string Cue0002Name = "RanRomAranSlide0005Cue0002";

	private static readonly string Cue0003Name = "RanRomAranSlide0005Cue0003";

	private static readonly string Cue0004Name = "RanRomAranSlide0005Cue0004";

	private static readonly string Cue0005Name = "RanRomAranSlide0005Cue0005";

	private static readonly string Cue0006Name = "RanRomAranSlide0005Cue0006";

	private static readonly string Cue0007Name = "RanRomAranSlide0005Cue0007";

	private static readonly string Cue0008Name = "RanRomAranSlide0005Cue0008";

	private static readonly string Cue0009Name = "RanRomAranSlide0005Cue0009";

	private static readonly string Cue0010Name = "RanRomAranSlide0005Cue0010";

	private static readonly string Cue0011Name = "RanRomAranSlide0005Cue0011";

	private static readonly string Cue0012Name = "RanRomAranSlide0005Cue0012";

	public static string Configure()
	{
		string text = "60252aa2f40941aca735fca3d4355ba7";
		string text2 = "b6cf71efea374f08ba1c41fb6ff44cf5";
		string text3 = "ae0095b47f184868bf448f92478062ef";
		string text4 = "b4afc6e7fc75491fbcf18923785ba9c3";
		string text5 = "1df04d757f4a4c0db1c6327202ab839b";
		string text6 = "ec6fec926a6e4e9fbd952b3c611dee06";
		string text7 = "0f00abae3ff646a7a7120c960e19354e";
		string text8 = "be7ee2c6847a4161950780533de5a692";
		string text9 = "151a22d98c9f4ab2acdeb0e42199d63d";
		string text10 = "7121d3df58ee47fc8c426ab8440f7727";
		string text11 = "12b61bb6201d40a8866ab60701dd4669";
		string text12 = "ff9dfab90fbf43b5bd525a6009813551";
		string text13 = "4942d32b09304aeab103fd93a759abd8";
		ConditionsBuilder conditionsBuilder = ConditionsBuilder.New().EtudeStatus(null, null, "07ad18ffb08145b69522f8eee0230857", negate: false, null, true).EtudeStatus(null, null, "9fc5161813f1497f8eaad1563ac54211", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions = ConditionsBuilder.New().DialogSeen("RanRomAranBook04").DialogSeen("RanRomAranBook14")
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AddOrAndLogic(conditions).EtudeStatus(null, null, "RanRomAranAzata", negate: true, null, true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: false, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: false, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: true, null, true);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "7fde872463d2d2647b159a733d40ea98", negate: false, null, true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "7fde872463d2d2647b159a733d40ea98", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomAranAlurRomance", negate: false, null, true);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "84e00414803841e428c3d47572c7d588", negate: false, null, true)
			.DialogSeen("RanRomAranBook14");
		ConditionsBuilder conditions8 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "84e00414803841e428c3d47572c7d588", negate: false, null, true)
			.DialogSeen("RanRomAranBook04");
		ConditionsBuilder conditions9 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "4a78282987fd432595c8a62d363730d7", negate: false, null, true);
		ConditionsBuilder conditions10 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "4a78282987fd432595c8a62d363730d7", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomAranAlurRomance", negate: false, null, true);
		ConditionsBuilder conditions11 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "381a296094804761af0893d2e70dc2df", negate: false, null, true);
		ConditionsBuilder conditions12 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: true, null, true);
		ConditionsBuilder conditions13 = ConditionsBuilder.New().DialogSeen("RanRomAranBook04");
		BookPageConfigurator.New(SlideName, text).SetImageLink("52163ec59b7bf62408b1b24137843bba").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text5)
			.AddToCues(text6)
			.AddToCues(text7)
			.AddToCues(text8)
			.AddToCues(text9)
			.AddToCues(text10)
			.AddToCues(text11)
			.AddToCues(text12)
			.AddToCues(text13)
			.SetConditions(conditions2)
			.AddToCues("RanRomFiller")
			.AddToAnswers("1afb887108b34ac1b082dabf64a786b6")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranSlide0005Cue0001.Text").SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions3).SetText("RanRomAranSlide0005Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions4).SetText("RanRomAranSlide0005Cue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions5).SetText("RanRomAranSlide0005Cue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text6).SetConditions(conditions6).SetText("RanRomAranSlide0005Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text7).SetConditions(conditions7).SetText("RanRomAranSlide0005Cue0006.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0007Name, text8).SetConditions(conditions8).SetText("RanRomAranSlide0005Cue0007.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0008Name, text9).SetConditions(conditions9).SetText("RanRomAranSlide0005Cue0008.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0009Name, text10).SetConditions(conditions10).SetText("RanRomAranSlide0005Cue0009.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0010Name, text11).SetConditions(conditions11).SetText("RanRomAranSlide0005Cue0010.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0011Name, text12).SetConditions(conditions12).SetText("RanRomAranSlide0005Cue0011.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0012Name, text13).SetConditions(conditions13).SetText("RanRomAranSlide0005Cue0012.Text")
			.SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
