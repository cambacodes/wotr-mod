using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;

namespace RanRomance.Mina;

public class Slide0001
{
	private static readonly string SlideName = "RanRomMinaSlide0001";

	private static readonly string Cue0001Name = "RanRomMinaSlide0001Cue0001";

	private static readonly string Cue0002Name = "RanRomMinaSlide0001Cue0002";

	private static readonly string Cue0003Name = "RanRomMinaSlide0001Cue0003";

	private static readonly string Cue0004Name = "RanRomMinaSlide0001Cue0004";

	private static readonly string Cue0005Name = "RanRomMinaSlide0001Cue0005";

	private static readonly string Cue0006Name = "RanRomMinaSlide0001Cue0006";

	private static readonly string Cue0007Name = "RanRomMinaSlide0001Cue0007";

	private static readonly string Cue0008Name = "RanRomMinaSlide0001Cue0008";

	private static readonly string Cue0009Name = "RanRomMinaSlide0001Cue0009";

	private static readonly string Cue0000Name = "RanRomMinaSlide0001Cue0000";

	private static readonly string Cue0011Name = "RanRomMinaSlide0001Cue0011";

	private static readonly string Cue0012Name = "RanRomMinaSlide0001Cue0012";

	public static string Configure()
	{
		string text = "951e4432cf844a36a8a222b27589fb43";
		string text2 = "26789d87b5a44ba988079b4842bad81c";
		string text3 = "e87b43c31c1c4253a7137c7d6c05b246";
		string text4 = "819314e916514a498a8e336371b4788e";
		string text5 = "9bfbb3f217ca476cadbeffc4d389717d";
		string text6 = "e0551b6120c94d70aa9d10a5fcc4ec86";
		string text7 = "7edf5529523a4a9da520138783fdeb93";
		string text8 = "d6b960c14e37492682de6284af1c5417";
		string text9 = "19fd9027465f4cbebe949b26d04a2826";
		string text10 = "84e26e3c483c4e7985ac656de08a5b05";
		string text11 = "f5e580bedafc43f3acb6843fd71d8120";
		string text12 = "59cf28c3824944fd88547bc61bc5cf62";
		string text13 = "92162854b221413984468d2663ffcffb";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "9fc5161813f1497f8eaad1563ac54211", negate: false, null, true).EtudeStatus(null, null, "07ad18ffb08145b69522f8eee0230857", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AddOrAndLogic(conditions).EtudeStatus(null, null, "RanRomMinaBanner", negate: false, null, true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaRedemption", negate: false, null, true);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaRedemption", negate: false, null, true).EtudeStatus(null, null, "71f85264d9064074f9cf74999ecbffa9", negate: false, null, true);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaRedemption", negate: false, null, true).EtudeStatus(null, null, "71f85264d9064074f9cf74999ecbffa9", negate: true, null, true)
			.EtudeStatus(null, null, "RanRomMinaRomance", negate: false, null, true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaRedemption", negate: false, null, true).EtudeStatus(null, null, "71f85264d9064074f9cf74999ecbffa9", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomMinaRomance", negate: false, null, true);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaCult", negate: false, null, true).EtudeStatus(null, null, "e94e751a522748cd9194979e2646d5ec", negate: true, null, true);
		ConditionsBuilder conditions8 = ConditionsBuilder.New().AddOrAndLogic(conditions7).EtudeStatus(null, null, "71f85264d9064074f9cf74999ecbffa9", negate: false, null, true);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().AddOrAndLogic(conditions7).EtudeStatus(null, null, "71f85264d9064074f9cf74999ecbffa9", negate: true, null, true)
			.EtudeStatus(null, null, "RanRomMinaRomance", negate: false, null, true);
		ConditionsBuilder conditions10 = ConditionsBuilder.New().AddOrAndLogic(conditions7).EtudeStatus(null, null, "71f85264d9064074f9cf74999ecbffa9", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomMinaRomance", negate: false, null, true);
		ConditionsBuilder conditions11 = ConditionsBuilder.New().AddOrAndLogic(conditions3, negate: true).AddOrAndLogic(conditions7, negate: true);
		ConditionsBuilder conditions12 = ConditionsBuilder.New().AddOrAndLogic(conditions11).EtudeStatus(null, null, "71f85264d9064074f9cf74999ecbffa9", negate: false, null, true);
		ConditionsBuilder conditions13 = ConditionsBuilder.New().AddOrAndLogic(conditions11).EtudeStatus(null, null, "71f85264d9064074f9cf74999ecbffa9", negate: true, null, true)
			.EtudeStatus(null, null, "RanRomMinaRomance", negate: false, null, true);
		ConditionsBuilder conditions14 = ConditionsBuilder.New().AddOrAndLogic(conditions11).EtudeStatus(null, null, "71f85264d9064074f9cf74999ecbffa9", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomMinaRomance", negate: false, null, true);
		BookPageConfigurator.New(SlideName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("1abecb015eedf484eab1b0229a7cecf7")
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
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions3).SetText("RanRomMinaSlide0001Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions4).SetText("RanRomMinaSlide0001Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions5).SetText("RanRomMinaSlide0001Cue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions6).SetText("RanRomMinaSlide0001Cue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text6).SetConditions(conditions7).SetText("RanRomMinaSlide0001Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text7).SetConditions(conditions8).SetText("RanRomMinaSlide0001Cue0006.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0007Name, text8).SetConditions(conditions9).SetText("RanRomMinaSlide0001Cue0007.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0008Name, text9).SetConditions(conditions10).SetText("RanRomMinaSlide0001Cue0008.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0009Name, text10).SetConditions(conditions11).SetText("RanRomMinaSlide0001Cue0009.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0000Name, text11).SetConditions(conditions12).SetText("RanRomMinaSlide0001Cue0000.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0011Name, text12).SetConditions(conditions13).SetText("RanRomMinaSlide0001Cue0011.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0012Name, text13).SetConditions(conditions14).SetText("RanRomMinaSlide0001Cue0012.Text")
			.SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
