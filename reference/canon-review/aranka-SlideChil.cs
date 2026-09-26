using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;

namespace RanRomance.Aran;

public class SlideChil
{
	private static readonly string Cue0001Name = "RanRomAranSlideChilCue0001";

	public static string Configure()
	{
		string text = "0567e8d36a7a4eafb5475aba830b96ab";
		ConditionsBuilder conditions = ConditionsBuilder.New().DialogSeen("RanRomAranBook04").FlagUnlocked("d6d8f59e4e9711d408bb67fd3ec029fb", null, negate: true)
			.FlagUnlocked("7edf2f69474c3e143b29d9a5dffec341")
			.FlagUnlocked("bb95467c27cf8d545a7327ecf4069cc9");
		ConditionsBuilder conditions2 = ConditionsBuilder.New().FlagUnlocked("d6d8f59e4e9711d408bb67fd3ec029fb");
		ConditionsBuilder conditions3 = ConditionsBuilder.New().FlagUnlocked("d6d8f59e4e9711d408bb67fd3ec029fb").AddOrAndLogic(conditions)
			.UseOr();
		CueConfigurator.New(Cue0001Name, text).SetConditions(conditions).SetText("RanRomAranSlideChilCue0001.Text")
			.SetShowOnce()
			.Configure();
		BookPageConfigurator.For("1df02d216bdd4e246b66b21074479767").ClearCues().AddToCues("f98fd581cb2838f4dbd8860b88c9b431")
			.AddToCues(text)
			.AddToCues("RanRomFiller")
			.SetConditions(conditions3)
			.Configure();
		CueConfigurator.For("f98fd581cb2838f4dbd8860b88c9b431").SetConditions(conditions2).Configure();
		return null;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
