using System;
using System.Collections.Generic;
using BlueprintCore.Utils;
using Kingmaker.AreaLogic;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Assets.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.ElementsSystem;
using Kingmaker.Enums;
using Kingmaker.UnitLogic.Alignments;

namespace BlueprintCore.Conditions.Builder.StoryEx;

internal static class ConditionsBuilderStoryEx
{
	public static ConditionsBuilder AlignmentCheck(this ConditionsBuilder builder, AlignmentComponent? alignment = null, bool negate = false)
	{
		//IL_001c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0013: Unknown result type (might be due to invalid IL or missing references)
		//IL_0021: Unknown result type (might be due to invalid IL or missing references)
		AlignmentCheck val = ElementTool.Create<AlignmentCheck>();
		val.Alignment = (AlignmentComponent)(((??)alignment) ?? val.Alignment);
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder AnotherEtudeOfGroupIsPlaying(this ConditionsBuilder builder, Blueprint<BlueprintEtudeConflictingGroupReference>? group = null, bool negate = false)
	{
		AnotherEtudeOfGroupIsPlaying val = ElementTool.Create<AnotherEtudeOfGroupIsPlaying>();
		val.m_Group = group?.Reference ?? val.m_Group;
		if (val.m_Group == null)
		{
			val.m_Group = BlueprintTool.GetRef<BlueprintEtudeConflictingGroupReference>((string?)null);
		}
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder AnswerListShown(this ConditionsBuilder builder, Blueprint<BlueprintAnswersListReference>? answersList = null, bool? currentDialog = null, bool negate = false)
	{
		AnswerListShown val = ElementTool.Create<AnswerListShown>();
		val.m_AnswersList = answersList?.Reference ?? val.m_AnswersList;
		if (val.m_AnswersList == null)
		{
			val.m_AnswersList = BlueprintTool.GetRef<BlueprintAnswersListReference>((string?)null);
		}
		val.CurrentDialog = currentDialog ?? val.CurrentDialog;
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder AnswerSelected(this ConditionsBuilder builder, Blueprint<BlueprintAnswerReference>? answer = null, bool? currentDialog = null, bool negate = false)
	{
		AnswerSelected val = ElementTool.Create<AnswerSelected>();
		val.m_Answer = answer?.Reference ?? val.m_Answer;
		if (val.m_Answer == null)
		{
			val.m_Answer = BlueprintTool.GetRef<BlueprintAnswerReference>((string?)null);
		}
		val.CurrentDialog = currentDialog ?? val.CurrentDialog;
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder BarkBanterPlayed(this ConditionsBuilder builder, Blueprint<BlueprintBarkBanterReference>? banter = null, bool negate = false)
	{
		BarkBanterPlayed val = ElementTool.Create<BarkBanterPlayed>();
		val.m_Banter = banter?.Reference ?? val.m_Banter;
		if (val.m_Banter == null)
		{
			val.m_Banter = BlueprintTool.GetRef<BlueprintBarkBanterReference>((string?)null);
		}
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder CampaignCompleted(this ConditionsBuilder builder, Blueprint<BlueprintCampaignReference>? campaign = null, bool negate = false)
	{
		CampaignCompleted val = ElementTool.Create<CampaignCompleted>();
		val.m_Campaign = campaign?.Reference ?? val.m_Campaign;
		if (val.m_Campaign == null)
		{
			val.m_Campaign = BlueprintTool.GetRef<BlueprintCampaignReference>((string?)null);
		}
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder CheckFailed(this ConditionsBuilder builder, Blueprint<BlueprintCheckReference>? check = null, bool negate = false)
	{
		CheckFailed val = ElementTool.Create<CheckFailed>();
		val.m_Check = check?.Reference ?? val.m_Check;
		if (val.m_Check == null)
		{
			val.m_Check = BlueprintTool.GetRef<BlueprintCheckReference>((string?)null);
		}
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder CheckPassed(this ConditionsBuilder builder, Blueprint<BlueprintCheckReference>? check = null, bool negate = false)
	{
		CheckPassed val = ElementTool.Create<CheckPassed>();
		val.m_Check = check?.Reference ?? val.m_Check;
		if (val.m_Check == null)
		{
			val.m_Check = BlueprintTool.GetRef<BlueprintCheckReference>((string?)null);
		}
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder CompanionStoryUnlocked(this ConditionsBuilder builder, Blueprint<BlueprintCompanionStoryReference>? companionStory = null, bool negate = false)
	{
		CompanionStoryUnlocked val = ElementTool.Create<CompanionStoryUnlocked>();
		val.m_CompanionStory = companionStory?.Reference ?? val.m_CompanionStory;
		if (val.m_CompanionStory == null)
		{
			val.m_CompanionStory = BlueprintTool.GetRef<BlueprintCompanionStoryReference>((string?)null);
		}
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder CueSeen(this ConditionsBuilder builder, Blueprint<BlueprintCueBaseReference>? cue = null, bool? currentDialog = null, bool negate = false)
	{
		CueSeen val = ElementTool.Create<CueSeen>();
		val.m_Cue = cue?.Reference ?? val.m_Cue;
		if (val.m_Cue == null)
		{
			val.m_Cue = BlueprintTool.GetRef<BlueprintCueBaseReference>((string?)null);
		}
		val.CurrentDialog = currentDialog ?? val.CurrentDialog;
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder CurrentChapter(this ConditionsBuilder builder, int? chapter = null, bool negate = false)
	{
		CurrentChapter val = ElementTool.Create<CurrentChapter>();
		val.Chapter = chapter ?? val.Chapter;
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder DayOfTheMonth(this ConditionsBuilder builder, int? day = null, bool negate = false)
	{
		DayOfTheMonth val = ElementTool.Create<DayOfTheMonth>();
		val.Day = day ?? val.Day;
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder DayOfTheWeek(this ConditionsBuilder builder, DayOfWeek? day = null, bool negate = false)
	{
		DayOfTheWeek val = ElementTool.Create<DayOfTheWeek>();
		val.Day = day ?? val.Day;
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder DayTime(this ConditionsBuilder builder, bool negate = false, TimeOfDay? time = null)
	{
		//IL_0023: Unknown result type (might be due to invalid IL or missing references)
		//IL_001a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0028: Unknown result type (might be due to invalid IL or missing references)
		DayTime val = ElementTool.Create<DayTime>();
		((Condition)val).Not = negate;
		val.Time = (TimeOfDay)(((??)time) ?? val.Time);
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder DialogSeen(this ConditionsBuilder builder, Blueprint<BlueprintDialogReference>? dialog = null, bool negate = false)
	{
		DialogSeen val = ElementTool.Create<DialogSeen>();
		val.m_Dialog = dialog?.Reference ?? val.m_Dialog;
		if (val.m_Dialog == null)
		{
			val.m_Dialog = BlueprintTool.GetRef<BlueprintDialogReference>((string?)null);
		}
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder EtudeStatus(this ConditionsBuilder builder, bool? completed = null, bool? completionInProgress = null, Blueprint<BlueprintEtudeReference>? etude = null, bool negate = false, bool? notStarted = null, bool? playing = null, bool? started = null)
	{
		EtudeStatus val = ElementTool.Create<EtudeStatus>();
		val.Completed = completed ?? val.Completed;
		val.CompletionInProgress = completionInProgress ?? val.CompletionInProgress;
		val.m_Etude = etude?.Reference ?? val.m_Etude;
		if (val.m_Etude == null)
		{
			val.m_Etude = BlueprintTool.GetRef<BlueprintEtudeReference>((string?)null);
		}
		((Condition)val).Not = negate;
		val.NotStarted = notStarted ?? val.NotStarted;
		val.Playing = playing ?? val.Playing;
		val.Started = started ?? val.Started;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder FlagInRange(this ConditionsBuilder builder, Blueprint<BlueprintUnlockableFlagReference>? flag = null, int? maxValue = null, int? minValue = null, bool negate = false)
	{
		FlagInRange val = ElementTool.Create<FlagInRange>();
		val.m_Flag = flag?.Reference ?? val.m_Flag;
		if (val.m_Flag == null)
		{
			val.m_Flag = BlueprintTool.GetRef<BlueprintUnlockableFlagReference>((string?)null);
		}
		val.MaxValue = maxValue ?? val.MaxValue;
		val.MinValue = minValue ?? val.MinValue;
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder FlagUnlocked(this ConditionsBuilder builder, Blueprint<BlueprintUnlockableFlagReference>? conditionFlag = null, bool? exceptSpecifiedValues = null, bool negate = false, List<int>? specifiedValues = null)
	{
		FlagUnlocked val = ElementTool.Create<FlagUnlocked>();
		val.m_ConditionFlag = conditionFlag?.Reference ?? val.m_ConditionFlag;
		if (val.m_ConditionFlag == null)
		{
			val.m_ConditionFlag = BlueprintTool.GetRef<BlueprintUnlockableFlagReference>((string?)null);
		}
		val.ExceptSpecifiedValues = exceptSpecifiedValues ?? val.ExceptSpecifiedValues;
		((Condition)val).Not = negate;
		val.SpecifiedValues = specifiedValues ?? val.SpecifiedValues;
		if (val.SpecifiedValues == null)
		{
			val.SpecifiedValues = new List<int>();
		}
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder IsCampaign(this ConditionsBuilder builder, Blueprint<BlueprintCampaignReference>? blueprintCampaign = null, bool negate = false)
	{
		IsCampaign val = ElementTool.Create<IsCampaign>();
		val.m_BlueprintCampaign = blueprintCampaign?.Reference ?? val.m_BlueprintCampaign;
		if (val.m_BlueprintCampaign == null)
		{
			val.m_BlueprintCampaign = BlueprintTool.GetRef<BlueprintCampaignReference>((string?)null);
		}
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder IsCampaignImported(this ConditionsBuilder builder, Blueprint<BlueprintCampaignReference>? blueprintCampaign = null, bool negate = false)
	{
		IsCampaignImported val = ElementTool.Create<IsCampaignImported>();
		val.m_BlueprintCampaign = blueprintCampaign?.Reference ?? val.m_BlueprintCampaign;
		if (val.m_BlueprintCampaign == null)
		{
			val.m_BlueprintCampaign = BlueprintTool.GetRef<BlueprintCampaignReference>((string?)null);
		}
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder IsLegendPathSelected(this ConditionsBuilder builder, bool negate = false)
	{
		IsLegendPathSelected val = ElementTool.Create<IsLegendPathSelected>();
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder MonthFromList(this ConditionsBuilder builder, int[]? months = null, bool negate = false)
	{
		MonthFromList val = ElementTool.Create<MonthFromList>();
		val.Months = months ?? val.Months;
		if (val.Months == null)
		{
			val.Months = new int[0];
		}
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder ObjectiveStatus(this ConditionsBuilder builder, bool negate = false, Blueprint<BlueprintQuestObjectiveReference>? questObjective = null, QuestObjectiveState? state = null)
	{
		//IL_0053: Unknown result type (might be due to invalid IL or missing references)
		//IL_004a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0058: Unknown result type (might be due to invalid IL or missing references)
		ObjectiveStatus val = ElementTool.Create<ObjectiveStatus>();
		((Condition)val).Not = negate;
		val.m_QuestObjective = questObjective?.Reference ?? val.m_QuestObjective;
		if (val.m_QuestObjective == null)
		{
			val.m_QuestObjective = BlueprintTool.GetRef<BlueprintQuestObjectiveReference>((string?)null);
		}
		val.State = (QuestObjectiveState)(((??)state) ?? val.State);
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder PlayerAlignmentIs(this ConditionsBuilder builder, AlignmentMaskType? alignment = null, bool negate = false)
	{
		//IL_001c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0013: Unknown result type (might be due to invalid IL or missing references)
		//IL_0021: Unknown result type (might be due to invalid IL or missing references)
		PlayerAlignmentIs val = ElementTool.Create<PlayerAlignmentIs>();
		val.Alignment = (AlignmentMaskType)(((??)alignment) ?? val.Alignment);
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder PlayerHasNoCharactersOnRoster(this ConditionsBuilder builder, bool negate = false)
	{
		PlayerHasNoCharactersOnRoster val = ElementTool.Create<PlayerHasNoCharactersOnRoster>();
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder PlayerHasRecruitsOnRoster(this ConditionsBuilder builder, bool negate = false)
	{
		PlayerHasRecruitsOnRoster val = ElementTool.Create<PlayerHasRecruitsOnRoster>();
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder PlayerSignificantClassIs(this ConditionsBuilder builder, Blueprint<BlueprintCharacterClassReference>? characterClass = null, Blueprint<BlueprintCharacterClassGroupReference>? characterClassGroup = null, bool? checkGroup = null, bool negate = false)
	{
		PlayerSignificantClassIs val = ElementTool.Create<PlayerSignificantClassIs>();
		val.m_CharacterClass = characterClass?.Reference ?? val.m_CharacterClass;
		if (val.m_CharacterClass == null)
		{
			val.m_CharacterClass = BlueprintTool.GetRef<BlueprintCharacterClassReference>((string?)null);
		}
		val.m_CharacterClassGroup = characterClassGroup?.Reference ?? val.m_CharacterClassGroup;
		if (val.m_CharacterClassGroup == null)
		{
			val.m_CharacterClassGroup = BlueprintTool.GetRef<BlueprintCharacterClassGroupReference>((string?)null);
		}
		val.CheckGroup = checkGroup ?? val.CheckGroup;
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder PlayerTopClassIs(this ConditionsBuilder builder, Blueprint<BlueprintCharacterClassReference>? characterClass = null, Blueprint<BlueprintCharacterClassGroupReference>? characterClassGroup = null, bool? checkGroup = null, bool negate = false)
	{
		PlayerTopClassIs val = ElementTool.Create<PlayerTopClassIs>();
		val.m_CharacterClass = characterClass?.Reference ?? val.m_CharacterClass;
		if (val.m_CharacterClass == null)
		{
			val.m_CharacterClass = BlueprintTool.GetRef<BlueprintCharacterClassReference>((string?)null);
		}
		val.m_CharacterClassGroup = characterClassGroup?.Reference ?? val.m_CharacterClassGroup;
		if (val.m_CharacterClassGroup == null)
		{
			val.m_CharacterClassGroup = BlueprintTool.GetRef<BlueprintCharacterClassGroupReference>((string?)null);
		}
		val.CheckGroup = checkGroup ?? val.CheckGroup;
		((Condition)val).Not = negate;
		return builder.Add((Condition)(object)val);
	}

	public static ConditionsBuilder QuestStatus(this ConditionsBuilder builder, bool negate = false, Blueprint<BlueprintQuestReference>? quest = null, QuestState? state = null)
	{
		//IL_0053: Unknown result type (might be due to invalid IL or missing references)
		//IL_004a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0058: Unknown result type (might be due to invalid IL or missing references)
		QuestStatus val = ElementTool.Create<QuestStatus>();
		((Condition)val).Not = negate;
		val.m_Quest = quest?.Reference ?? val.m_Quest;
		if (val.m_Quest == null)
		{
			val.m_Quest = BlueprintTool.GetRef<BlueprintQuestReference>((string?)null);
		}
		val.State = (QuestState)(((??)state) ?? val.State);
		return builder.Add((Condition)(object)val);
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
