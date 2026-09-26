using BlueprintCore.Blueprints.Configurators.Quests;
using Kingmaker.Blueprints.Quests;
using Kingmaker.Enums;

namespace RanRomance.Aran;

public class AranQuest
{
	private static readonly string PageName = "RanRomAranQuest";

	private static readonly string Entry0001Name = "RanRomAranQuestEntry0001";

	private static readonly string Entry0002Name = "RanRomAranQuestEntry0002";

	private static readonly string Entry0003Name = "RanRomAranQuestEntry0003";

	private static readonly string Entry0004Name = "RanRomAranQuestEntry0004";

	private static readonly string FailName = "RanRomAranQuestEntryFail";

	public static string Configure()
	{
		string text = "1dacd3dfe1bf47c8a73074814e40b1c8";
		string text2 = "de72cd5dc29f4ce882d32e14042bd243";
		string text3 = "af711de489484df5b81ef9996902e6a7";
		string text4 = "b968d14237b94e60af8f01f84f42dcda";
		string text5 = "d1e371f09017417b98b0aed58f3ab6ac";
		string text6 = "4ef00caf2a644f42af5af39f7c381910";
		QuestObjectiveConfigurator.New(Entry0001Name, text2).SetTitle("RanRomAranQuestEntry0001.Text").SetDescription("RanRomAranQuestEntry0001L.Text")
			.SetType((Type)0)
			.SetQuest(text)
			.Configure();
		QuestObjectiveConfigurator.New(Entry0002Name, text3).SetTitle("RanRomAranQuestEntry0002.Text").SetDescription("RanRomAranQuestEntry0002L.Text")
			.SetType((Type)0)
			.SetQuest(text)
			.Configure();
		QuestObjectiveConfigurator.New(Entry0003Name, text4).SetTitle("RanRomAranQuestEntry0003.Text").SetDescription("RanRomAranQuestEntry0003L.Text")
			.SetType((Type)0)
			.SetQuest(text)
			.SetFinishParent()
			.Configure();
		QuestObjectiveConfigurator.New(Entry0004Name, text5).SetTitle("RanRomAranQuestEntry0004.Text").SetDescription("RanRomAranQuestEntry0004L.Text")
			.SetType((Type)0)
			.SetQuest(text)
			.SetFinishParent()
			.Configure();
		QuestObjectiveConfigurator.New(FailName, text6).SetHidden().SetType((Type)0)
			.SetQuest(text)
			.SetFinishParent()
			.Configure();
		QuestConfigurator.New(PageName, text).SetTitle("RanRomAranQuestName.Text").SetDescription("RanRomAranQuestIntro.Text")
			.SetCompletionText("RanRomAranQuestOutro.Text")
			.SetGroup((QuestGroupId)18)
			.SetLastChapter(5)
			.SetType((QuestType)0)
			.AddToObjectives(text2)
			.AddToObjectives(text3)
			.AddToObjectives(text4)
			.AddToObjectives(text5)
			.AddToObjectives(text6)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
