using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;

namespace RanRomance.Aran;

public class SlideAeon
{
	private static readonly string SlideName = "RanRomAranSlideAeon";

	private static readonly string Cue0001Name = "RanRomAranSlideAeonCue0001";

	private static readonly string Cue0002Name = "RanRomAranSlideAeonCue0002";

	private static readonly string Cue0003Name = "RanRomAranSlideAeonCue0003";

	public static string Configure()
	{
		string text = "e87bee7465d14293b7a65402dfcb0a1d";
		string text2 = "22eaa37f58d247289ea6fb4eaa77f412";
		string text3 = "2b38b7eb8bf5443aa818819f81710781";
		string text4 = "49e9b1419960481b9359727767133b06";
		ConditionsBuilder conditions = ConditionsBuilder.New().DialogSeen("RanRomAranBook04").DialogSeen("RanRomAranBook14")
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().FlagUnlocked("a8b030ebca6c9744bac633cff609b698");
		ConditionsBuilder conditions3 = ConditionsBuilder.New().FlagUnlocked("a8b030ebca6c9744bac633cff609b698").EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true);
		BookPageConfigurator.New(SlideName, text).SetImageLink("52163ec59b7bf62408b1b24137843bba").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.SetConditions(conditions)
			.AddToCues("RanRomFiller")
			.AddToAnswers("1afb887108b34ac1b082dabf64a786b6")
			.Configure();
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranSlideAeonCue0001.Text").SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomAranSlideAeonCue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions3).SetText("RanRomAranSlideAeonCue0003.Text")
			.SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
