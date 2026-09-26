using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;

namespace RanRomance.Aran;

public class Slide0003
{
	private static readonly string SlideName = "RanRomAranSlide0003";

	private static readonly string Cue0001Name = "RanRomAranSlide0003Cue0001";

	private static readonly string Cue0002Name = "RanRomAranSlide0003Cue0002";

	private static readonly string Cue0003Name = "RanRomAranSlide0003Cue0003";

	public static string Configure()
	{
		string text = "692ac68c328b46ff9935c8c7277683e6";
		string text2 = "d6e706835a2c438896aa4507f3742d9c";
		string text3 = "2a3d9fb00d6248fb92ee9cfc6a78a886";
		string text4 = "f24595af9b374ac697d6f8a06c47b323";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "07ad18ffb08145b69522f8eee0230857", negate: false, null, true).EtudeStatus(null, null, "9fc5161813f1497f8eaad1563ac54211", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().DialogSeen("RanRomAranBook04").EtudeStatus(null, null, "RanRomAranAzata", negate: true, null, true)
			.AddOrAndLogic(conditions);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: true, null, true);
		BookPageConfigurator.New(SlideName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.SetConditions(conditions2)
			.AddToCues("RanRomFiller")
			.AddToAnswers("1afb887108b34ac1b082dabf64a786b6")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranSlide0003Cue0001.Text").SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions3).SetText("RanRomAranSlide0003Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions4).SetText("RanRomAranSlide0003Cue0003.Text")
			.SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
