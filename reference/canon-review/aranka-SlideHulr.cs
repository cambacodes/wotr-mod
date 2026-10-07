using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using Kingmaker.AreaLogic.QuestSystem;

namespace RanRomance.Aran;

public class SlideHulr
{
	private static readonly string SlideName = "RanRomAranSlideHulr";

	private static readonly string Cue0001Name = "RanRomAranSlideHulrCue0001";

	private static readonly string Cue0002Name = "RanRomAranSlideHulrCue0002";

	private static readonly string Cue0003Name = "RanRomAranSlideHulrCue0003";

	public static string Configure()
	{
		string text = "35629f2caf6c4e37bbb5cd9852b38ce3";
		string text2 = "91179adfc07349589ab9786e33e89d99";
		string text3 = "62fe9294865d43dba2ce0342c745a107";
		string text4 = "f81e4e5548fd42828c541f7319b80de5";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranHulrun", negate: false, null, true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().QuestStatus(negate: false, "476c9e81420b4a25941c486a2ebfb752", (QuestState)2);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "a23f713e3722447ea4dc13ea7d280512", negate: false, null, true).QuestStatus(negate: true, "476c9e81420b4a25941c486a2ebfb752", (QuestState)2);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().EtudeStatus(null, null, "a23f713e3722447ea4dc13ea7d280512", negate: true, null, true).QuestStatus(negate: true, "476c9e81420b4a25941c486a2ebfb752", (QuestState)2);
		BookPageConfigurator.New(SlideName, text).SetImageLink("482f509e50aa6484bafee746ddb3849f").SetForeImageLink("781d4f97ada0d394db52bd3e9b3dc8b8")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.SetConditions(conditions)
			.AddToCues("RanRomFiller")
			.AddToAnswers("1afb887108b34ac1b082dabf64a786b6")
			.Configure();
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions2).SetText("RanRomAranSlideHulrCue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions3).SetText("RanRomAranSlideHulrCue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions4).SetText("RanRomAranSlideHulrCue0003.Text")
			.SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
