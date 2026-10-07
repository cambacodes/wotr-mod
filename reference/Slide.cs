using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;

namespace RanRomance.Tere;

public class Slide0001
{
	private static readonly string SlideName = "RanRomTereSlide0001";

	private static readonly string Cue0001Name = "RanRomTereSlide0001Cue0001";

	public static string Configure()
	{
		string text = "c7550e53facf4dd08cc542d18c1502f5";
		string text2 = "bfe1c27e09ca451caa84c855b5bd33e9";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "9fc5161813f1497f8eaad1563ac54211", negate: false, null, true).EtudeStatus(null, null, "07ad18ffb08145b69522f8eee0230857", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomTereRom", negate: false, null, true).EtudeStatus(null, null, "RanRomTereAeonScale", negate: false, null, true)
			.DialogSeen("RanRomTereBook05")
			.AddOrAndLogic(conditions);
		BookPageConfigurator.New(SlideName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/tererom/normal/large.png")
			.AddToCues(text2)
			.SetConditions(conditions2)
			.AddToAnswers("1afb887108b34ac1b082dabf64a786b6")
			.AddToCues("RanRomFiller")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomTereSlide0001Cue0001.Text").SetShowOnce()
			.Configure();
		return text;
	}
}
