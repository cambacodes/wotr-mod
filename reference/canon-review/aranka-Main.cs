using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators;
using BlueprintCore.Blueprints.Configurators.AreaLogic.Etudes;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using BlueprintCore.Utils.Assets;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.Enums;
using RanRomance.Chun;
using RanRomance.Meph;
using UnityEngine;
using imagetest.Utilities;

namespace RanRomance.Aran;

public class Main
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
		//IL_007c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0083: Expected O, but got Unknown
		//IL_00a5: Unknown result type (might be due to invalid IL or missing references)
		//IL_00ac: Expected O, but got Unknown
		//IL_00d3: Unknown result type (might be due to invalid IL or missing references)
		//IL_0204: Unknown result type (might be due to invalid IL or missing references)
		//IL_020b: Expected O, but got Unknown
		//IL_0232: Unknown result type (might be due to invalid IL or missing references)
		IntConstant val = new IntConstant();
		val.Value = 6;
		((Element)val).name = "constant6Aran";
		IntConstant val2 = new IntConstant();
		val2.Value = 7;
		((Element)val2).name = "constant7Aran";
		IntConstant val3 = new IntConstant();
		val3.Value = 1;
		((Element)val3).name = "constant1Aran";
		IntConstant val4 = new IntConstant();
		val4.Value = 8;
		((Element)val4).name = "constant8Aran";
		IntConstant val5 = new IntConstant();
		val5.Value = -1;
		((Element)val5).name = "negative1Aran";
		PlayerCharacter val6 = new PlayerCharacter();
		((Element)val6).name = "pcAran";
		PortraitConfigurator.New("RanRomAranPortNorm", "74305ccf427e4dbcb84d5cd632dffeff").Configure();
		PortraitData val7 = new PortraitData();
		Asset<Sprite> asset = "assets/portraits/aranrom/nowings/large.png";
		Asset<Sprite> asset2 = "assets/portraits/aranrom/nowings/medium.png";
		Asset<Sprite> asset3 = "assets/portraits/aranrom/nowings/small.png";
		val7.PortraitCategory = (PortraitCategory)0;
		val7.IsDefault = false;
		val7.InitiativePortrait = false;
		SmallPortraitInjector.Replacements[val7] = asset3.Get();
		HalfPortraitInjector.Replacements[val7] = asset2.Get();
		FullPortraitInjector.Replacements[val7] = asset.Get();
		BlueprintTool.Get<BlueprintPortrait>("74305ccf427e4dbcb84d5cd632dffeff").Data = val7;
		UnitConfigurator.For("b85fdd8481f26f54f9c504fc4d2e031f").SetPortrait("RanRomAranPortNorm").Configure();
		UnitConfigurator.For("430cba7801b149b4e8494ace6baf4f7c").SetPortrait("RanRomAranPortNorm").Configure();
		UnitConfigurator.For("bd0c4fe722aeef94b8495ac284b96bc8").SetPortrait("RanRomAranPortNorm").Configure();
		UnitConfigurator.For("2a07732f97374ec5a1f7ef679b5a5b0f").SetPortrait("RanRomAranPortNorm").Configure();
		UnitConfigurator.For("c513a05dd1e54d36b45fbb97f44c0fbb").SetPortrait("RanRomAranPortNorm").Configure();
		PortraitConfigurator.New("RanRomAranPortWing", "3af0d47f30f34ddbbb8d0406cba9bc52").Configure();
		PortraitData val8 = new PortraitData();
		Asset<Sprite> asset4 = "assets/portraits/aranrom/wings/large.png";
		Asset<Sprite> asset5 = "assets/portraits/aranrom/nowings/medium.png";
		Asset<Sprite> asset6 = "assets/portraits/aranrom/nowings/small.png";
		val8.PortraitCategory = (PortraitCategory)0;
		val8.IsDefault = false;
		val8.InitiativePortrait = false;
		SmallPortraitInjector.Replacements[val8] = asset6.Get();
		HalfPortraitInjector.Replacements[val8] = asset5.Get();
		FullPortraitInjector.Replacements[val8] = asset4.Get();
		BlueprintTool.Get<BlueprintPortrait>("3af0d47f30f34ddbbb8d0406cba9bc52").Data = val8;
		UnlockableFlagConfigurator.New("RanRomAranConf", "3564eeaca9484627bb82958e9bf1b449").Configure();
		EtudeConfigurator.New("RanRomAranActive", "b2dfa8223ee24b84ab2795f86aa66ebb").SetAllowActionStart().Configure();
		EtudeConfigurator.New("RanRomAranFlirtEnd", "285425f788fd41d7860df9a899e1f4a7").SetAllowActionStart().Configure();
		EtudeConfigurator.New("RanRomAranFlirt", "da5580951e64443c8f9ebdb559efad7a").SetActivationCondition(ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranFlirtEnd", negate: true, null, true)).SetAllowActionStart()
			.Configure();
		EtudeConfigurator.New("RanRomAranWarden", "77f1192d6ff8428389351c7ef02c2bfc").SetAllowActionStart().Configure();
		EtudeConfigurator.New("RanRomAranRomance", "2e98dbe685f045cdabf88b66e4cde9ff").AddEtudePlayTrigger(ActionsBuilder.New().IncrementFlagValue("RanRomCount", true, (IntEvaluator?)(object)val3)).AddEtudeCompleteTrigger(ActionsBuilder.New().IncrementFlagValue("RanRomCount", true, (IntEvaluator?)(object)val5))
			.SetAllowActionStart()
			.Configure();
		EtudeConfigurator.New("RanRomAranDevil", "ba279937ec924582805bea281c4b3d1d").SetAllowActionStart().Configure();
		EtudeConfigurator.New("RanRomAranAzata", "342ef983802947e3a52b83769a89d315").SetAllowActionStart().Configure();
		EtudeConfigurator.New("RanRomAranAlurFlirt", "a5235e681a7b484e8deb572b8193ff27").SetAllowActionStart().Configure();
		EtudeConfigurator.New("RanRomAranAlurRomance", "d4dd8a50613e4d528913d0a24d06fca1").SetAllowActionStart().Configure();
		EtudeConfigurator.New("RanRomAranHulrun", "fa8f47ff79d148349f0f6e88fd610d33").SetAllowActionStart().Configure();
		AranQuest.Configure();
		AranBook01.Configure();
		AranBook02.Configure();
		AranBook03.Configure();
		AranBook04.Configure();
		AranBook14.Configure();
		AranEpil.Configure();
		AranChpt01Dial001.Configure();
		AranChpt03Dial001.Configure();
		ChunChpt03Dial001.Configure();
		ChunChpt03Dial002.Configure();
		ChunChpt05Dial001.Configure();
		MephChpt05Dial001.Configure();
		ConditionsBuilder conditions = ConditionsBuilder.New().DialogSeen("14ffcdd473704e5dbc8cfe5f98b582b8").QuestStatus(negate: false, "5ba83bd1a6b1c884794fbb4858480e7f", (QuestState)2)
			.AddOrAndLogic(((BlueprintCueBase)BlueprintTool.Get<BlueprintBookPage>("9f67adedf4dacca439264db537a4b9f3")).Conditions);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().QuestStatus(negate: false, "df19bef39c8aa6a4b9dcaf40450b94dc", (QuestState)2);
		EtudeConfigurator.For("4484a3460335465a992359fac23a2ca5").SetActivationCondition(ConditionsBuilder.New().AddOrAndLogic(conditions).AddOrAndLogic(conditions2)
			.UseOr()).Configure();
		ConditionsBuilder conditions3 = ConditionsBuilder.New().DialogSeen("14ffcdd473704e5dbc8cfe5f98b582b8").QuestStatus(negate: false, "df19bef39c8aa6a4b9dcaf40450b94dc", (QuestState)2)
			.AddOrAndLogic(((BlueprintCueBase)BlueprintTool.Get<BlueprintBookPage>("223fd069ee25c784db2df011adbf10f8")).Conditions);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().QuestStatus(negate: false, "5ba83bd1a6b1c884794fbb4858480e7f", (QuestState)2);
		EtudeConfigurator.For("6eddba9546e84c2fb0bb50af027b7d25").SetActivationCondition(ConditionsBuilder.New().AddOrAndLogic(conditions3).AddOrAndLogic(conditions4)
			.UseOr()).Configure();
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected("e3f0e242a99622c46a43fd6529d44a41");
		EtudeConfigurator.For("9ce50eac84ade7042872352b5d2622e7").SetActivationCondition(ConditionsBuilder.New().AddOrAndLogic(conditions3).AddOrAndLogic(conditions5)
			.UseOr()).Configure();
		ConditionsBuilder conditions6 = ConditionsBuilder.New().EtudeStatus(null, null, "c3a5748e4a44a1649a75e0968c15a0c1", negate: false, null, true).EtudeStatus(null, null, "bf5bb702e577a0a4eaa1a9df7dea253b", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions7 = ConditionsBuilder.New().EtudeStatus(null, null, "381a296094804761af0893d2e70dc2df", negate: true, null, true).EtudeStatus(null, null, "9ce50eac84ade7042872352b5d2622e7", negate: false, null, true)
			.AddOrAndLogic(conditions6);
		CueConfigurator.For("7b5c9401080040d6a7f686b4c06c1167").SetConditions(conditions7).Configure();
		ConditionsBuilder conditions8 = ConditionsBuilder.New().EtudeStatus(null, null, "d7169995e449fdc4db861ddf0b9beff8", negate: false, null, true).EtudeStatus(null, null, "81037254dcdfb5441902e9b23f65aee4", negate: false, null, true);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranHulrun", negate: false, null, true).EtudeStatus(null, null, "5ec3719a546abce46bfbf05735a48e14", negate: true, null, true)
			.EtudeStatus(null, null, "49007180deadcbc4383286982f2ae54e", negate: true, null, true);
		ConditionsBuilder activationCondition = ConditionsBuilder.New().AddOrAndLogic(conditions8).AddOrAndLogic(conditions9)
			.UseOr();
		EtudeConfigurator.For("216528988afe82044958d0660f7b855d").SetActivationCondition(activationCondition).Configure();
		ConditionsBuilder activationCondition2 = ConditionsBuilder.New().EtudeStatus(null, null, "d7169995e449fdc4db861ddf0b9beff8", negate: true, null, true).EtudeStatus(null, null, "RanRomAranHulrun", negate: true, null, true);
		EtudeConfigurator.For("5ec3719a546abce46bfbf05735a48e14").SetActivationCondition(activationCondition2).Configure();
		ActionsBuilder ifTrue = ActionsBuilder.New().IncrementFlagValue("fbb189bb913c4899ad075ef94e91e595", true, (IntEvaluator?)(object)val3);
		ConditionsBuilder conditions10 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true);
		ActionsBuilder actions = ActionsBuilder.New().Conditional(conditions10, ifTrue);
		EtudeConfigurator.For("4beab5b47b0a40d3a2fa59b2b285b3de").AddEtudePlayTrigger(actions).Configure();
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
