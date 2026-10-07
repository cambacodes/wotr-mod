using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators;
using BlueprintCore.Blueprints.Configurators.AreaLogic.Etudes;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Blueprints.References;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.BasicEx;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Epilogue.Sec1004;
using HarmonyLib;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;

namespace RanRomance.Etudes;

public class VarEtudes
{
	public static void Configure()
	{
		//IL_0001: Unknown result type (might be due to invalid IL or missing references)
		//IL_0007: Expected O, but got Unknown
		//IL_0019: Unknown result type (might be due to invalid IL or missing references)
		//IL_001f: Expected O, but got Unknown
		//IL_0031: Unknown result type (might be due to invalid IL or missing references)
		//IL_0037: Expected O, but got Unknown
		//IL_0049: Unknown result type (might be due to invalid IL or missing references)
		//IL_004f: Expected O, but got Unknown
		//IL_0061: Unknown result type (might be due to invalid IL or missing references)
		//IL_0068: Expected O, but got Unknown
		IntConstant val = new IntConstant();
		val.Value = 6;
		((Element)val).name = "constant6var";
		IntConstant val2 = new IntConstant();
		val2.Value = 7;
		((Element)val2).name = "constant7var";
		IntConstant val3 = new IntConstant();
		val3.Value = 1;
		((Element)val3).name = "constant1var";
		IntConstant val4 = new IntConstant();
		val4.Value = 8;
		((Element)val4).name = "constant8var";
		PlayerCharacter val5 = new PlayerCharacter();
		((Element)val5).name = "pcvar";
		ConditionsBuilder activationCondition = ConditionsBuilder.New().QuestStatus(negate: true, "083019d0509bb1b4d85682338d9e2228", (QuestState)1).QuestStatus(negate: true, "b3fc817f0d6c2a344a59fea71dd149ae", (QuestState)1)
			.QuestStatus(negate: true, "2865e4ea685865d43bccb36c3d58ee1c", (QuestState)1)
			.QuestStatus(negate: true, "f54a7cc2928bb664792c320fa4fb1486", (QuestState)1)
			.QuestStatus(negate: true, "084960ae22f408e4282f537a8a9debc1", (QuestState)1)
			.QuestStatus(negate: true, "17a1f3b5f31fb8649825009b03861fcf", (QuestState)1)
			.QuestStatus(negate: true, "05c331f6c28b03544b39f94917e47abd", (QuestState)1)
			.QuestStatus(negate: true, "653c8dec252da8d4b872d87e6f656cf2", (QuestState)1)
			.UnitClass(((object)CharacterClassRefs.SwarmThatWalksClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val5)
			.EtudeStatus(null, null, "5b01aa690202e584888dfc600a4aac0a", negate: false, null, true)
			.DialogSeen("799827d0a35405b499e0e2f84fcf08be");
		string name = "RanRomC5MythicCompl";
		string guid = "f694258862674009bd7dea2091d74bab";
		ConditionsBuilder conditions = ConditionsBuilder.New().UnitClass(((object)CharacterClassRefs.LichMythicClass.Reference).ToString(), null, true, null, null, negate: true, (UnitEvaluator?)(object)val5).UnitClass(((object)CharacterClassRefs.DemonMythicClass.Reference).ToString(), null, true, null, null, negate: true, (UnitEvaluator?)(object)val5)
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().UnitClass(((object)CharacterClassRefs.GoldenDragonClass.Reference).ToString(), null, true, null, null, negate: false, (UnitEvaluator?)(object)val5).UnitClass(((object)CharacterClassRefs.LegendClass.Reference).ToString(), null, true, null, null, negate: false, (UnitEvaluator?)(object)val5)
			.UseOr();
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AddOrAndLogic(conditions).AddOrAndLogic(conditions2)
			.UseOr();
		ConditionsBuilder conditions4 = ConditionsBuilder.New().DialogSeen("fe8542a7a90d459c99d29921694f4d0d").FlagInRange("3564eeaca9484627bb82958e9bf1b449", 999, 2)
			.CueSeen("b18d250fa2fb4fdf9fe4eba04e9d1655", null, negate: true)
			.UnitClass(((object)CharacterClassRefs.DevilMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val5)
			.UnitClass(((object)CharacterClassRefs.SwarmThatWalksClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val5)
			.AddOrAndLogic(conditions3)
			.EtudeStatus(null, null, "0b129925567b68d4fb712b4bee6c0f9a", negate: true, null, true)
			.QuestStatus(negate: false, "1dacd3dfe1bf47c8a73074814e40b1c8", (QuestState)1)
			.ObjectiveStatus(negate: false, "b968d14237b94e60af8f01f84f42dcda", (QuestObjectiveState)0);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().DialogSeen("fe8542a7a90d459c99d29921694f4d0d").FlagInRange("3564eeaca9484627bb82958e9bf1b449", 1, -999)
			.CueSeen("b18d250fa2fb4fdf9fe4eba04e9d1655", null, negate: true)
			.UnitClass(((object)CharacterClassRefs.DevilMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val5)
			.UnitClass(((object)CharacterClassRefs.SwarmThatWalksClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val5)
			.AddOrAndLogic(conditions3)
			.QuestStatus(negate: false, "1dacd3dfe1bf47c8a73074814e40b1c8", (QuestState)1)
			.ObjectiveStatus(negate: false, "d1e371f09017417b98b0aed58f3ab6ac", (QuestObjectiveState)0);
		ActionsBuilder actions = ActionsBuilder.New().Conditional(ConditionsBuilder.New().QuestStatus(negate: false, "6ec03ce2f763460c8ac89f4c2064c5ad", (QuestState)1).ObjectiveStatus(negate: false, "227778a66d0f478fbb6e1b7e89758d22", (QuestObjectiveState)0), ActionsBuilder.New().GiveObjective("227778a66d0f478fbb6e1b7e89758d22")).Conditional(ConditionsBuilder.New().AddOrAndLogic(ConditionsBuilder.New().EtudeStatus(null, null, "f17a1d19d1b34a9fa469bdfcf819028f", negate: false, null, true).EtudeStatus(null, null, "615479a8a3d3462a9855ff54895a02ee", negate: false, null, true)
			.UseOr()).ObjectiveStatus(negate: false, "58cc5ac6231342f8b0724371a3bcc8a3", (QuestObjectiveState)0), ActionsBuilder.New().GiveObjective("58cc5ac6231342f8b0724371a3bcc8a3"))
			.Conditional(ConditionsBuilder.New().EtudeStatus(null, null, "42e220d5dadc4dfd8bb3ef23cae832eb", negate: true, null, true).EtudeStatus(null, null, "615479a8a3d3462a9855ff54895a02ee", negate: true, null, true)
				.DialogSeen("31a4cbf9316542858c3d03f757a32245")
				.ObjectiveStatus(negate: false, "60914070543e4df4bf3ed47c64f029a5", (QuestObjectiveState)0), ActionsBuilder.New().GiveObjective("60914070543e4df4bf3ed47c64f029a5"))
			.Conditional(conditions4, ActionsBuilder.New().GiveObjective("b968d14237b94e60af8f01f84f42dcda"))
			.Conditional(conditions5, ActionsBuilder.New().GiveObjective("d1e371f09017417b98b0aed58f3ab6ac"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(ConditionsBuilder.New().EtudeStatus(null, null, "9f655e252d334f04884f10188b0d8928", negate: false, null, true).EtudeStatus(null, null, "857c9366224c4b278fcc4ba3273b4b6b", negate: false, null, true)
				.UseOr()).ObjectiveStatus(negate: false, "5e95cccb00fd4deaa3473b3c82b3be8c", (QuestObjectiveState)0), ActionsBuilder.New().GiveObjective("5e95cccb00fd4deaa3473b3c82b3be8c"));
		EtudeConfigurator.New(name, guid).SetActivationCondition(activationCondition).AddEtudePlayTrigger(actions)
			.SetAllowActionStart()
			.Configure();
		UnlockableFlagConfigurator.New("RanRomCount", "9c6b442d6b0642209a45e0487da1a717").Configure();
		if (Harmony.HasAnyPatches("RanEpilogue"))
		{
			BlueprintComponent[] componentsArray = ((BlueprintScriptableObject)BlueprintTool.Get<BlueprintEtude>("4beab5b47b0a40d3a2fa59b2b285b3de")).ComponentsArray;
			if (componentsArray.Length == 0)
			{
				EtudeConfigurator.New("RanEpilWendEnd", "6eddba9546e84c2fb0bb50af027b7d25").SetAllowActionStart().Configure();
				ConditionsBuilder conditions6 = ConditionsBuilder.New().QuestStatus(negate: false, "5ba83bd1a6b1c884794fbb4858480e7f", (QuestState)2);
				EtudeConfigurator.New("RanEpilLannEnd", "4484a3460335465a992359fac23a2ca5").SetAllowActionStart().Configure();
				ConditionsBuilder conditions7 = ConditionsBuilder.New().QuestStatus(negate: false, "df19bef39c8aa6a4b9dcaf40450b94dc", (QuestState)2);
				ActionsBuilder actions2 = ActionsBuilder.New().Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions6), ActionsBuilder.New().StartEtude("RanEpilWendEnd")).Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions7), ActionsBuilder.New().StartEtude("RanEpilLannEnd"));
				EtudeConfigurator.For("4beab5b47b0a40d3a2fa59b2b285b3de").AddEtudePlayTrigger(actions2).Configure();
				ConditionsBuilder conditions8 = ConditionsBuilder.New().AddOrAndLogic(((BlueprintCueBase)BlueprintTool.Get<BlueprintBookPage>("9f67adedf4dacca439264db537a4b9f3")).Conditions).EtudeStatus(null, null, "2553d7c1d4b743e4a1d6871e98e0bbb0", negate: false, null, true)
					.EtudeStatus(null, null, "RanEpilLannEnd", negate: false, null, true);
				BookPageConfigurator.For("2a982f37730c4ac3a75adc2e0ebe5dc8").SetConditions(conditions8).Configure();
				ConditionsBuilder conditions9 = ConditionsBuilder.New().AddOrAndLogic(((BlueprintCueBase)BlueprintTool.Get<BlueprintBookPage>("223fd069ee25c784db2df011adbf10f8")).Conditions).EtudeStatus(null, null, "2553d7c1d4b743e4a1d6871e98e0bbb0", negate: false, null, true)
					.EtudeStatus(null, null, "RanEpilWendEnd", negate: false, null, true);
				BookPageConfigurator.For("84977c2568374f19bcc23947936b5346").SetConditions(conditions9).Configure();
				Slide0009.Configure();
				Slide0010.Configure();
			}
			return;
		}
		ConditionsBuilder conditions10 = ConditionsBuilder.New().UnitClass(CharacterClassRefs.AeonMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val, negate: false, (UnitEvaluator?)(object)val5).UnitClass(CharacterClassRefs.DevilMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: true, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions11 = ConditionsBuilder.New().UnitClass(CharacterClassRefs.AzataMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val, negate: false, (UnitEvaluator?)(object)val5).UnitClass(CharacterClassRefs.DevilMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: true, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions12 = ConditionsBuilder.New().UnitClass(CharacterClassRefs.AngelMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val, negate: false, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions13 = ConditionsBuilder.New().UnitClass(CharacterClassRefs.AeonMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val2, negate: false, (UnitEvaluator?)(object)val5).AddOrAndLogic(conditions10)
			.UseOr();
		ConditionsBuilder conditions14 = ConditionsBuilder.New().AddOrAndLogic(conditions13);
		ConditionsBuilder conditions15 = ConditionsBuilder.New().UnitClass(CharacterClassRefs.AzataMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val2, negate: false, (UnitEvaluator?)(object)val5).AddOrAndLogic(conditions11)
			.UseOr();
		ConditionsBuilder conditions16 = ConditionsBuilder.New().AddOrAndLogic(conditions15);
		ConditionsBuilder conditions17 = ConditionsBuilder.New().UnitClass(CharacterClassRefs.DemonMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val, negate: false, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions18 = ConditionsBuilder.New().UnitClass(CharacterClassRefs.LichMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val, negate: false, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions19 = ConditionsBuilder.New().UnitClass(CharacterClassRefs.TricksterMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val, negate: false, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions20 = ConditionsBuilder.New().UnitClass(CharacterClassRefs.GoldenDragonClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: false, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions21 = ConditionsBuilder.New().UnitClass(CharacterClassRefs.SwarmThatWalksClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: false, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions22 = ConditionsBuilder.New().UnitClass(CharacterClassRefs.DevilMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: false, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions23 = ConditionsBuilder.New().UnitClass(CharacterClassRefs.LegendClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: false, (UnitEvaluator?)(object)val5).UnitClass(CharacterClassRefs.FakeLegendClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: false, (UnitEvaluator?)(object)val5)
			.UseOr();
		ConditionsBuilder conditions24 = ConditionsBuilder.New().AddOrAndLogic(conditions23);
		UnlockableFlagConfigurator.New("RanEpilMythicCount", "bb81623987724ce598c02bd05901e901").Configure();
		ActionsBuilder ifTrue = ActionsBuilder.New().IncrementFlagValue("RanEpilMythicCount", true, (IntEvaluator?)(object)val3);
		ActionsBuilder actions3 = ActionsBuilder.New().Conditional(conditions12, ifTrue);
		ActionsBuilder actions4 = ActionsBuilder.New().Conditional(conditions14, ifTrue);
		ActionsBuilder actions5 = ActionsBuilder.New().Conditional(conditions16, ifTrue);
		ActionsBuilder actions6 = ActionsBuilder.New().Conditional(conditions17, ifTrue);
		ActionsBuilder actions7 = ActionsBuilder.New().Conditional(conditions22, ifTrue);
		ActionsBuilder actions8 = ActionsBuilder.New().Conditional(conditions18, ifTrue);
		ActionsBuilder actions9 = ActionsBuilder.New().Conditional(conditions19, ifTrue);
		ActionsBuilder actions10 = ActionsBuilder.New().Conditional(conditions20, ifTrue);
		ActionsBuilder actions11 = ActionsBuilder.New().Conditional(conditions21, ifTrue);
		ActionsBuilder actions12 = ActionsBuilder.New().Conditional(conditions24, ifTrue);
		EtudeConfigurator.New("RanEpilAngel", "4c845feaff5a4de6828cc81390cf4d58").SetAllowActionStart().AddActivateTrigger(actions3)
			.Configure();
		EtudeConfigurator.New("RanEpilAeon", "c23c1c18ce5044daa954eac7cfaa0513").SetAllowActionStart().AddActivateTrigger(actions4)
			.Configure();
		EtudeConfigurator.New("RanEpilAzata", "1b0ffcfc686147db92a62afa476ed87f").SetAllowActionStart().AddActivateTrigger(actions5)
			.Configure();
		EtudeConfigurator.New("RanEpilDemon", "922ba3587d1e4cd6b49d8869f9d335cb").SetAllowActionStart().AddActivateTrigger(actions6)
			.Configure();
		EtudeConfigurator.New("RanEpilLich", "f34ac256f152463fb682628b30359f06").SetAllowActionStart().AddActivateTrigger(actions8)
			.Configure();
		EtudeConfigurator.New("RanEpilTrickster", "bbb89ac13e2d43a7a66646b2cfb74b18").SetAllowActionStart().AddActivateTrigger(actions9)
			.Configure();
		EtudeConfigurator.New("RanEpilGold", "802dc2feb4ce4ed78dd029c27fb4baf5").SetAllowActionStart().AddActivateTrigger(actions10)
			.Configure();
		EtudeConfigurator.New("RanEpilSwarm", "b1a8cea7540742ed9f36b3f7fab7c0b4").SetAllowActionStart().AddActivateTrigger(actions11)
			.Configure();
		EtudeConfigurator.New("RanEpilDevil", "49999e09f28b4a86ac2c65126cf2414c").SetAllowActionStart().AddActivateTrigger(actions7)
			.Configure();
		EtudeConfigurator.New("RanEpilLegend", "6aa152ed25244445a9a279b1a1ccd697").SetAllowActionStart().AddActivateTrigger(actions12)
			.Configure();
		ConditionsBuilder conditions25 = ConditionsBuilder.New().AddOrAndLogic(conditions17).AddOrAndLogic(conditions18)
			.AddOrAndLogic(conditions21)
			.UseOr();
		EtudeConfigurator.New("RanEpilEvil", "e94e751a522748cd9194979e2646d5ec").SetAllowActionStart().Configure();
		ConditionsBuilder conditions26 = ConditionsBuilder.New().EtudeStatus(null, null, "db5375333382d044089475d256f19582", negate: false, null, true).EtudeStatus(null, null, "6ff418aeda24e6e48be844e6258e3c5a", negate: false, null, true)
			.AnswerSelected("fff2f6e49d4c7bb438ffe7a8f256d252", null, negate: true);
		ConditionsBuilder completionCondition = ConditionsBuilder.New().AnswerSelected("fff2f6e49d4c7bb438ffe7a8f256d252");
		ConditionsBuilder conditions27 = ConditionsBuilder.New().EtudeStatus(null, null, "9955b661dd7640b19986e453293a3e0a", negate: false, null, true).AddOrAndLogic(conditions17)
			.AddOrAndLogic(conditions18)
			.AddOrAndLogic(conditions21)
			.AddOrAndLogic(conditions26)
			.UseOr();
		EtudeConfigurator.New("RanEpilThreat", "3d82393701fe49ad9a81a7d3c2b96137").SetAllowActionStart().SetCompletionCondition(completionCondition)
			.Configure();
		ConditionsBuilder conditions28 = ConditionsBuilder.New().EtudeStatus(null, null, "381a296094804761af0893d2e70dc2df", negate: true, null, true).AddOrAndLogic(conditions17)
			.AddOrAndLogic(conditions18)
			.AddOrAndLogic(conditions21);
		EtudeConfigurator.New("RanEpilPlayThreat", "a23f713e3722447ea4dc13ea7d280512").SetAllowActionStart().Configure();
		ConditionsBuilder conditions29 = ConditionsBuilder.New().AddOrAndLogic(conditions22).AddOrAndLogic(conditions17)
			.AddOrAndLogic(conditions18)
			.AddOrAndLogic(conditions21)
			.UseOr();
		ConditionsBuilder conditions30 = ConditionsBuilder.New().AddOrAndLogic(conditions29).EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: false, null, true);
		EtudeConfigurator.New("RanEpilAscEvil", "e9f88f9b3b1c4a439e8b5955c7b3343f").SetAllowActionStart().Configure();
		ConditionsBuilder conditions31 = ConditionsBuilder.New().AddOrAndLogic(conditions12).AddOrAndLogic(conditions14)
			.AddOrAndLogic(conditions16)
			.AddOrAndLogic(conditions20)
			.UseOr();
		ConditionsBuilder conditions32 = ConditionsBuilder.New().AddOrAndLogic(conditions31).EtudeStatus(null, null, "c6935ff7cbfd4aed8ac479e94e66918d", negate: false, null, true);
		EtudeConfigurator.New("RanEpilAscGood", "8bf71495d3bb47a2acba2c6a4458b1ea").SetAllowActionStart().Configure();
		ConditionsBuilder conditions33 = ConditionsBuilder.New().EtudeStatus(null, null, "9fc5161813f1497f8eaad1563ac54211", negate: false, null, true).EtudeStatus(null, null, "07ad18ffb08145b69522f8eee0230857", negate: false, null, true)
			.UseOr();
		EtudeConfigurator.New("RanEpilPartyAsc", "2553d7c1d4b743e4a1d6871e98e0bbb0").SetAllowActionStart().Configure();
		UnlockableFlagConfigurator.New("RanEpilRomCount", "fbb189bb913c4899ad075ef94e91e595").Configure();
		ActionsBuilder ifTrue2 = ActionsBuilder.New().IncrementFlagValue("RanEpilRomCount", true, (IntEvaluator?)(object)val3);
		ConditionsBuilder conditions34 = ConditionsBuilder.New().EtudeStatus(null, null, "133f3b1b38f04fa44be3200b786e437f", negate: false, null, true).EtudeStatus(null, null, "988a9382fa814042a4bcd4dd8680454e", negate: false, null, true)
			.UseOr();
		ActionsBuilder actions13 = ActionsBuilder.New().Conditional(conditions34, ifTrue2);
		ConditionsBuilder conditions35 = ConditionsBuilder.New().EtudeStatus(null, null, "0f98398a5ddf32e4cb8200f56e4cfbfc", negate: false, null, true).EtudeStatus(null, null, "1454cf86d07cfdf4f8b5daee625cdc5b", negate: false, null, true)
			.UseOr();
		ActionsBuilder actions14 = ActionsBuilder.New().Conditional(conditions35, ifTrue2);
		ConditionsBuilder conditions36 = ConditionsBuilder.New().EtudeStatus(null, null, "2fa85b8a61290084dacc6321a2c28095", negate: false, null, true).EtudeStatus(null, null, "95c9e826d26573d4692e9575a848a477", negate: false, null, true)
			.UseOr();
		ActionsBuilder actions15 = ActionsBuilder.New().Conditional(conditions36, ifTrue2);
		ConditionsBuilder conditions37 = ConditionsBuilder.New().EtudeStatus(null, null, "c3a5748e4a44a1649a75e0968c15a0c1", negate: false, null, true).EtudeStatus(null, null, "bf5bb702e577a0a4eaa1a9df7dea253b", negate: false, null, true)
			.UseOr();
		ActionsBuilder actions16 = ActionsBuilder.New().Conditional(conditions37, ifTrue2);
		ConditionsBuilder conditions38 = ConditionsBuilder.New().EtudeStatus(null, null, "1cf02e18017d5304fb132f5d7d947865", negate: false, null, true).EtudeStatus(null, null, "c9263fe299b6025469d906c770dab332", negate: false, null, true)
			.EtudeStatus(null, null, "83db74d60e659df4f9c88f93f05ba17d", negate: false, null, true)
			.UseOr();
		ActionsBuilder actions17 = ActionsBuilder.New().Conditional(conditions38, ifTrue2);
		ConditionsBuilder conditions39 = ConditionsBuilder.New().EtudeStatus(null, null, "b7c24b1fdb571874a9dd11f2adb3ab57", negate: false, null, true).EtudeStatus(null, null, "57ea188ffa059ef43b821e47093f6ff4", negate: false, null, true)
			.EtudeStatus(null, null, "67a9ac748faaa6b4aae3f31baf3b1c31", negate: false, null, true)
			.UseOr();
		ActionsBuilder actions18 = ActionsBuilder.New().Conditional(conditions39, ifTrue2);
		ConditionsBuilder conditions40 = ConditionsBuilder.New().EtudeStatus(null, null, "6585b428527be344d8224983ee0ba181", negate: false, null, true).EtudeStatus(null, null, "e81129bb979b3dd47bf9459ee03663d8", negate: false, null, true)
			.UseOr();
		ActionsBuilder actions19 = ActionsBuilder.New().Conditional(conditions40, ifTrue2);
		ConditionsBuilder conditions41 = ConditionsBuilder.New().EtudeStatus(null, null, "969b574752d74e7b8e5f50fdb0c4963e", negate: false, null, true).EtudeStatus(null, null, "b1dd59de28dc4b4a9951058a3fe944b9", negate: false, null, true)
			.UseOr();
		ActionsBuilder actions20 = ActionsBuilder.New().Conditional(conditions41, ifTrue2);
		ConditionsBuilder conditions42 = ConditionsBuilder.New().EtudeStatus(null, null, "19d67188186a47fb8f4b0020716aef41", negate: false, null, true).UseOr();
		ActionsBuilder actions21 = ActionsBuilder.New().Conditional(conditions42, ifTrue2);
		UnlockableFlagConfigurator.New("RanEpilFlingCount", "71ec085e669046a4baac8ecacc8d0f3c").Configure();
		ActionsBuilder ifTrue3 = ActionsBuilder.New().IncrementFlagValue("RanEpilFlingCount", true, (IntEvaluator?)(object)val3);
		ConditionsBuilder conditions43 = ConditionsBuilder.New().CueSeen("62d54f591bc9d3a45b3d5ab50b9fc08d").AddOrAndLogic(((BlueprintCueBase)BlueprintTool.Get<BlueprintBookPage>("7937c8393a0e71f438ee49856eacf7e4")).Conditions)
			.UnitClass(CharacterClassRefs.LichMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val4, negate: true, (UnitEvaluator?)(object)val5);
		ActionsBuilder actions22 = ActionsBuilder.New().Conditional(conditions43, ifTrue3);
		ConditionsBuilder conditions44 = ConditionsBuilder.New().AnswerSelected("1d91c763220a55f498fa843656fc4cd1").UseOr();
		ActionsBuilder actions23 = ActionsBuilder.New().Conditional(conditions44, ifTrue3);
		ConditionsBuilder conditions45 = ConditionsBuilder.New().EtudeStatus(null, null, "7561719a9eb527440aff2de1e5ae5c5a", negate: false, null, true).UseOr();
		ActionsBuilder actions24 = ActionsBuilder.New().Conditional(conditions45, ifTrue3);
		ConditionsBuilder conditions46 = ConditionsBuilder.New().FlagUnlocked("RanEpilMythicCount", null, negate: true).UnitClass(CharacterClassRefs.AngelMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: false, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions47 = ConditionsBuilder.New().FlagUnlocked("RanEpilMythicCount", null, negate: true).UnitClass(CharacterClassRefs.AeonMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: false, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions48 = ConditionsBuilder.New().FlagUnlocked("RanEpilMythicCount", null, negate: true).UnitClass(CharacterClassRefs.AzataMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: false, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions49 = ConditionsBuilder.New().FlagUnlocked("RanEpilMythicCount", null, negate: true).UnitClass(CharacterClassRefs.DemonMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: false, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions50 = ConditionsBuilder.New().FlagUnlocked("RanEpilMythicCount", null, negate: true).UnitClass(CharacterClassRefs.LichMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: false, (UnitEvaluator?)(object)val5);
		ConditionsBuilder conditions51 = ConditionsBuilder.New().FlagUnlocked("RanEpilMythicCount", null, negate: true).UnitClass(CharacterClassRefs.TricksterMythicClass.ToString(), null, true, null, (IntEvaluator?)(object)val3, negate: false, (UnitEvaluator?)(object)val5);
		EtudeConfigurator.New("RanEpilWendEnd", "6eddba9546e84c2fb0bb50af027b7d25").SetAllowActionStart().Configure();
		ConditionsBuilder conditions52 = ConditionsBuilder.New().QuestStatus(negate: false, "5ba83bd1a6b1c884794fbb4858480e7f", (QuestState)2);
		EtudeConfigurator.New("RanEpilLannEnd", "4484a3460335465a992359fac23a2ca5").SetAllowActionStart().Configure();
		ConditionsBuilder conditions53 = ConditionsBuilder.New().QuestStatus(negate: false, "df19bef39c8aa6a4b9dcaf40450b94dc", (QuestState)2);
		ActionsBuilder actions25 = ActionsBuilder.New().Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions12), ActionsBuilder.New().StartEtude("RanEpilAngel")).Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions14), ActionsBuilder.New().StartEtude("RanEpilAeon"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions16), ActionsBuilder.New().StartEtude("RanEpilAzata"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions17), ActionsBuilder.New().StartEtude("RanEpilDemon"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions18), ActionsBuilder.New().StartEtude("RanEpilLich"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions19), ActionsBuilder.New().StartEtude("RanEpilTrickster"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions20), ActionsBuilder.New().StartEtude("RanEpilGold"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions21), ActionsBuilder.New().StartEtude("RanEpilSwarm"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions22), ActionsBuilder.New().StartEtude("RanEpilDevil"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions24), ActionsBuilder.New().StartEtude("RanEpilLegend"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions46), ActionsBuilder.New().StartEtude("RanEpilAngel").IncrementFlagValue("RanEpilRomCount", true, (IntEvaluator?)(object)val3))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions47), ActionsBuilder.New().StartEtude("RanEpilAeon").IncrementFlagValue("RanEpilRomCount", true, (IntEvaluator?)(object)val3))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions48), ActionsBuilder.New().StartEtude("RanEpilAzata").IncrementFlagValue("RanEpilRomCount", true, (IntEvaluator?)(object)val3))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions49), ActionsBuilder.New().StartEtude("RanEpilDemon").IncrementFlagValue("RanEpilRomCount", true, (IntEvaluator?)(object)val3))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions50), ActionsBuilder.New().StartEtude("RanEpilLich").IncrementFlagValue("RanEpilRomCount", true, (IntEvaluator?)(object)val3))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions51), ActionsBuilder.New().StartEtude("RanEpilTrickster").IncrementFlagValue("RanEpilRomCount", true, (IntEvaluator?)(object)val3))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions25), ActionsBuilder.New().StartEtude("RanEpilEvil"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions27), ActionsBuilder.New().StartEtude("RanEpilThreat"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions28), ActionsBuilder.New().StartEtude("RanEpilPlayThreat"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions30), ActionsBuilder.New().StartEtude("RanEpilAscEvil"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions32), ActionsBuilder.New().StartEtude("RanEpilAscGood"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions33), ActionsBuilder.New().StartEtude("RanEpilPartyAsc"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions52), ActionsBuilder.New().StartEtude("RanEpilWendEnd"))
			.Conditional(ConditionsBuilder.New().AddOrAndLogic(conditions53), ActionsBuilder.New().StartEtude("RanEpilLannEnd"));
		EtudeConfigurator.New("RanEpilStart", "4beab5b47b0a40d3a2fa59b2b285b3de").SetAllowActionStart().AddEtudePlayTrigger(actions25)
			.AddEtudePlayTrigger(actions13)
			.AddEtudePlayTrigger(actions14)
			.AddEtudePlayTrigger(actions15)
			.AddEtudePlayTrigger(actions16)
			.AddEtudePlayTrigger(actions17)
			.AddEtudePlayTrigger(actions18)
			.AddEtudePlayTrigger(actions19)
			.AddEtudePlayTrigger(actions20)
			.AddEtudePlayTrigger(actions21)
			.AddEtudePlayTrigger(actions22)
			.AddEtudePlayTrigger(actions23)
			.AddEtudePlayTrigger(actions24)
			.Configure();
		ActionsBuilder startActions = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintDialog>("ae58532cb72b28b4eaaccb82eb78eaea").StartActions.Actions[0]).Add(BlueprintTool.Get<BlueprintDialog>("ae58532cb72b28b4eaaccb82eb78eaea").StartActions.Actions[1])
			.Add(BlueprintTool.Get<BlueprintDialog>("ae58532cb72b28b4eaaccb82eb78eaea").StartActions.Actions[2])
			.StartEtude("RanEpilStart");
		DialogConfigurator.For("ae58532cb72b28b4eaaccb82eb78eaea").SetStartActions(startActions).Configure();
		if (Harmony.HasAnyPatches("WOTR_WoljifRomanceMod"))
		{
			ConditionsBuilder conditions54 = ConditionsBuilder.New().EtudeStatus(null, null, "345e7378fdd1425aabd158fc6baa91b7", negate: false, null, true).EtudeStatus(null, null, "34c418afd27d4177a4fd35d097dc794d", negate: false, null, true);
			ActionsBuilder actions26 = ActionsBuilder.New().Conditional(conditions54, ifTrue2);
			EtudeConfigurator.For("4beab5b47b0a40d3a2fa59b2b285b3de").AddEtudePlayTrigger(actions26);
		}
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
