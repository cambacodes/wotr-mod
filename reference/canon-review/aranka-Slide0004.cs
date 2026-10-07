using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;

namespace RanRomance.Aran;

public class Slide0004
{
	private static readonly string SlideName = "RanRomAranSlide0004";

	private static readonly string Cue0001Name = "RanRomAranSlide0004Cue0001";

	private static readonly string Cue0002Name = "RanRomAranSlide0004Cue0002";

	private static readonly string Cue0003Name = "RanRomAranSlide0004Cue0003";

	private static readonly string Cue0004Name = "RanRomAranSlide0004Cue0004";

	private static readonly string Cue0005Name = "RanRomAranSlide0004Cue0005";

	private static readonly string Cue0006Name = "RanRomAranSlide0004Cue0006";

	private static readonly string Cue0007Name = "RanRomAranSlide0004Cue0007";

	private static readonly string Cue0008Name = "RanRomAranSlide0004Cue0008";

	private static readonly string Cue0009Name = "RanRomAranSlide0004Cue0009";

	private static readonly string Cue0010Name = "RanRomAranSlide0004Cue0010";

	private static readonly string Cue0011Name = "RanRomAranSlide0004Cue0011";

	private static readonly string Cue0012Name = "RanRomAranSlide0004Cue0012";

	private static readonly string Cue0013Name = "RanRomAranSlide0004Cue0013";

	private static readonly string Cue0014Name = "RanRomAranSlide0004Cue0014";

	public static string Configure()
	{
		string text = "b1c703e139ad454d83de7e9260371807";
		string text2 = "f9db645af3e048f6b9d647b6f56c10e1";
		string text3 = "09e000c0ac21485e8d9a981386ecf2c6";
		string text4 = "8ccaecca7d9141e8bfca64404923c106";
		string text5 = "74c975812f294ed89ea3d1baa298ee2c";
		string text6 = "5ebbaaf2804c4a88b09fb597bd35809a";
		string text7 = "dfabe31062654feaa35c2b060931439b";
		string text8 = "cfae2a0cf2e34bd48acf4eaecd9d1d7d";
		string text9 = "dba625629b1649ae9de8e4f857519569";
		string text10 = "1c194cc46f254d5fbd5439e51ea90c01";
		string text11 = "d9c4f98e207847bba5a7d10a7fec5248";
		string text12 = "7986354882b14e55a66516e51e186142";
		string text13 = "100dbfc430ff48ebbb5c3ce48274af17";
		string text14 = "3de21613f9074615b3f3b7080b5bdbbc";
		string text15 = "caec5f656004426396ee00bd420c7d1d";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "07ad18ffb08145b69522f8eee0230857", negate: false, null, true).EtudeStatus(null, null, "9fc5161813f1497f8eaad1563ac54211", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().DialogSeen("RanRomAranBook04").EtudeStatus(null, null, "RanRomAranAzata", negate: false, null, true)
			.AddOrAndLogic(conditions, negate: true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: true, null, true);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: false, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: false, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: true, null, true);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "7fde872463d2d2647b159a733d40ea98", negate: false, null, true);
		ConditionsBuilder conditions8 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "7fde872463d2d2647b159a733d40ea98", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomAranAlurRomance", negate: false, null, true);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "84e00414803841e428c3d47572c7d588", negate: false, null, true);
		ConditionsBuilder conditions10 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "4a78282987fd432595c8a62d363730d7", negate: false, null, true);
		ConditionsBuilder conditions11 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "4a78282987fd432595c8a62d363730d7", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomAranAlurRomance", negate: true, null, true);
		ConditionsBuilder conditions12 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "4a78282987fd432595c8a62d363730d7", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomAranAlurRomance", negate: false, null, true);
		ConditionsBuilder conditions13 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true)
			.EtudeStatus(null, null, "381a296094804761af0893d2e70dc2df", negate: false, null, true);
		ConditionsBuilder conditions14 = ConditionsBuilder.New().EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: true, null, true).EtudeStatus(null, null, "RanRomAranRomance", negate: true, null, true);
		BookPageConfigurator.New(SlideName, text).SetImageLink("52163ec59b7bf62408b1b24137843bba").SetForeImageLink("assets/portraits/aranrom/wings/large.png")
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
			.AddToCues(text14)
			.AddToCues(text15)
			.SetConditions(conditions2)
			.AddToCues("RanRomFiller")
			.AddToAnswers("1afb887108b34ac1b082dabf64a786b6")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranSlide0004Cue0001.Text").SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions3).SetText("RanRomAranSlide0004Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions4).SetText("RanRomAranSlide0004Cue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions5).SetText("RanRomAranSlide0004Cue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text6).SetConditions(conditions6).SetText("RanRomAranSlide0004Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text7).SetConditions(conditions7).SetText("RanRomAranSlide0004Cue0006.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0007Name, text8).SetConditions(conditions8).SetText("RanRomAranSlide0004Cue0007.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0008Name, text9).SetConditions(conditions9).SetText("RanRomAranSlide0004Cue0008.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0009Name, text10).SetConditions(conditions10).SetText("RanRomAranSlide0004Cue0009.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0010Name, text11).SetConditions(conditions11).SetText("RanRomAranSlide0004Cue0010.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0011Name, text12).SetConditions(conditions12).SetText("RanRomAranSlide0004Cue0011.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0012Name, text13).SetConditions(conditions13).SetText("RanRomAranSlide0004Cue0012.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0013Name, text14).SetConditions(conditions14).SetText("RanRomAranSlide0004Cue0013.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0014Name, text15).SetText("RanRomAranSlide0004Cue0014.Text").SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
