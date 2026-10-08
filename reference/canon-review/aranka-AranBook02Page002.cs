using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Blueprints.References;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.BasicEx;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.DialogSystem;
using Kingmaker.ElementsSystem;

namespace RanRomance.Aran;

public class AranBook02Page002
{
	private static readonly string PageName = "RanRomAranBook02Page002";

	private static readonly string Cue0001Name = "RanRomAranBook02Page002Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook02Page002Cue0002";

	private static readonly string Cue0003Name = "RanRomAranBook02Page002Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook02Page002Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook02Page002Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook02Page002Ans0005";

	private static readonly string Cue0005Name = "RanRomAranBook02Page002Cue0005";

	private static readonly string Ans0006Name = "RanRomAranBook02Page002Ans0006";

	private static readonly string Cue0006Name = "RanRomAranBook02Page002Cue0006";

	private static readonly string Ans0007Name = "RanRomAranBook02Page002Ans0007";

	private static readonly string Cue0007Name = "RanRomAranBook02Page002Cue0007";

	private static readonly string Cue0008Name = "RanRomAranBook02Page002Cue0008";

	private static readonly string Cue0009Name = "RanRomAranBook02Page002Cue0009";

	private static readonly string Cue0000Name = "RanRomAranBook02Page002Cue0000";

	private static readonly string Ans0011Name = "RanRomAranBook02Page002Ans0011";

	private static readonly string Cue0011Name = "RanRomAranBook02Page002Cue0011";

	private static readonly string Cue0012Name = "RanRomAranBook02Page002Cue0012";

	private static readonly string Cue0013Name = "RanRomAranBook02Page002Cue0013";

	private static readonly string Cue0014Name = "RanRomAranBook02Page002Cue0014";

	private static readonly string Ans0015Name = "RanRomAranBook02Page002Ans0015";

	private static readonly string Cue0015Name = "RanRomAranBook02Page002Cue0015";

	private static readonly string Ans0016Name = "RanRomAranBook02Page002Ans0016";

	private static readonly string Cue0016Name = "RanRomAranBook02Page002Cue0016";

	private static readonly string Ans0017Name = "RanRomAranBook02Page002Ans0017";

	private static readonly string Cue0017Name = "RanRomAranBook02Page002Cue0017";

	private static readonly string Cue0018Name = "RanRomAranBook02Page002Cue0018";

	private static readonly string Cue0019Name = "RanRomAranBook02Page002Cue0019";

	private static readonly string Ans0010Name = "RanRomAranBook02Page002Ans0010";

	public static string Configure()
	{
		//IL_00c8: Unknown result type (might be due to invalid IL or missing references)
		//IL_00cf: Expected O, but got Unknown
		//IL_09b5: Unknown result type (might be due to invalid IL or missing references)
		//IL_09bc: Expected O, but got Unknown
		//IL_09bc: Unknown result type (might be due to invalid IL or missing references)
		//IL_09c3: Expected O, but got Unknown
		//IL_09cf: Unknown result type (might be due to invalid IL or missing references)
		//IL_09d4: Unknown result type (might be due to invalid IL or missing references)
		//IL_09eb: Unknown result type (might be due to invalid IL or missing references)
		//IL_09f0: Unknown result type (might be due to invalid IL or missing references)
		//IL_09f7: Expected O, but got Unknown
		//IL_09f7: Unknown result type (might be due to invalid IL or missing references)
		//IL_09fe: Expected O, but got Unknown
		//IL_0a0a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0a0f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0a26: Unknown result type (might be due to invalid IL or missing references)
		string text = "85cbfdcbbf424bd4affb995eba564034";
		string text2 = "0fbede8aed26490e931f2a029f2fd699";
		string text3 = "4fe8c3a04b30431da5f6e277b2404b33";
		string text4 = "8b70f929979d4272bd944483599276be";
		string text5 = "d09a787568014339a82267b91e9d6b3e";
		string text6 = "7e525d797f604e96a170d54614aba2cd";
		string text7 = "1b3948b00f6349d09ac6c647c329d549";
		string text8 = "1e9a95893f014ee8ad47825e00c86187";
		string text9 = "61a4bb5bc1fb448aa80f87c11b5825df";
		string text10 = "379210f94cba40f9a622128f070f91d8";
		string text11 = "0180ada016f34e5bbce2cc95f1cbecb5";
		string text12 = "1a0b01f25e9247219907ffa47e97008c";
		string text13 = "54408cb6773f48bf99d18d2d00ce9217";
		string text14 = "3e9b3eb1e6844e0fb7b517c71a9fbe41";
		string text15 = "8d91ebe0c27143f79b195905a6c49b00";
		string text16 = "46181423cd264a649b98e69b9b9635b8";
		string text17 = "6b829d21e43942eea17f1f142365b199";
		string text18 = "534ef6101dce414388f70ac20357886d";
		string text19 = "29ea09106b9c4cc18f52f2fb975ecd42";
		string text20 = "d2055e7c11b54857a9ad9ab727ef0262";
		string text21 = "b84162f6b8b448dda611390b5d8531fb";
		string text22 = "8cb7273193894bc58038d388c52e5f86";
		string text23 = "e9eda31749a44e26b257b5731ed0f5ee";
		string text24 = "2d695fbcda6b42979e0522bb28166519";
		string text25 = "b2c836188c2044d5a50d924c52b7d8a1";
		string text26 = "02f02708630247d1ab25ea7dc79b8bef";
		string text27 = "82ecceed5df3471a80a0c136c7862f38";
		string text28 = "af8b360632854998873e60fb918ee4f1";
		string text29 = "a07e838e304b44979c5f86fa1deda2a0";
		PlayerCharacter val = new PlayerCharacter();
		((Element)val).name = "pc" + text;
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "d7169995e449fdc4db861ddf0b9beff8", negate: true, null, true).EtudeStatus(null, null, "9b81cc87781828444bfd451ee2c556f0", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected("675ffa84b9a546abbfc8bc4e9599c575");
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected("68d8558ec4d94b68bb355fb2946a126b");
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected(text9);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text9);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected(text11);
		ConditionsBuilder conditions8 = ConditionsBuilder.New().AnswerSelected(text11).AddOrAndLogic(conditions, negate: true);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().AnswerSelected(text11).AddOrAndLogic(conditions);
		ConditionsBuilder conditions10 = ConditionsBuilder.New().AnswerSelected(text11);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().AnswerSelected(text11);
		ConditionsBuilder conditions11 = ConditionsBuilder.New().AnswerSelected(text16).EtudeStatus(null, null, "RanRomAranHulrun", negate: false, null, true);
		ConditionsBuilder conditions12 = ConditionsBuilder.New().AnswerSelected(text16).EtudeStatus(null, null, "RanRomAranHulrun", negate: true, null, true)
			.AddOrAndLogic(conditions)
			.UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val);
		ConditionsBuilder conditions13 = ConditionsBuilder.New().AnswerSelected(text16).EtudeStatus(null, null, "RanRomAranHulrun", negate: true, null, true)
			.AddOrAndLogic(conditions)
			.UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val);
		ConditionsBuilder conditions14 = ConditionsBuilder.New().AnswerSelected(text16).EtudeStatus(null, null, "RanRomAranHulrun", negate: true, null, true)
			.AddOrAndLogic(conditions, negate: true);
		ConditionsBuilder showConditions3 = ConditionsBuilder.New().AnswerSelected(text11);
		ConditionsBuilder conditions15 = ConditionsBuilder.New().AnswerSelected(text21);
		ConditionsBuilder showConditions4 = ConditionsBuilder.New().AnswerSelected(text11).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val);
		ConditionsBuilder conditions16 = ConditionsBuilder.New().AnswerSelected(text23);
		ConditionsBuilder conditions17 = ConditionsBuilder.New().AnswerSelected(text25).EtudeStatus(null, null, "RanRomAranFlirtEnd", negate: true, null, true)
			.EtudeStatus(null, null, "RanRomAranFlirt", negate: false, null, true)
			.CueSeen(text27, null, negate: true);
		ConditionsBuilder conditions18 = ConditionsBuilder.New().AnswerSelected(text25).EtudeStatus(null, null, "RanRomAranFlirtEnd", negate: true, null, true)
			.EtudeStatus(null, null, "RanRomAranFlirt", negate: true, null, true);
		ConditionsBuilder conditions19 = ConditionsBuilder.New().AnswerSelected(text25).EtudeStatus(null, null, "RanRomAranFlirtEnd", negate: false, null, true);
		ConditionsBuilder showConditions5 = ConditionsBuilder.New().AnswerSelected(text21);
		BookPageConfigurator.New(PageName, text).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToCues(text10)
			.AddToAnswers(text9)
			.AddToCues(text12)
			.AddToAnswers(text11)
			.AddToCues(text13)
			.AddToCues(text14)
			.AddToCues(text15)
			.AddToCues(text17)
			.AddToAnswers(text16)
			.AddToCues(text18)
			.AddToCues(text19)
			.AddToCues(text20)
			.AddToCues(text22)
			.AddToAnswers(text21)
			.AddToCues(text24)
			.AddToAnswers(text23)
			.AddToCues(text26)
			.AddToAnswers(text25)
			.AddToCues(text27)
			.AddToCues(text28)
			.AddToAnswers(text29)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val2 = new CueSelection();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val2.Cues.Add(val3);
		val2.Strategy = (Strategy)0;
		CueSelection val4 = new CueSelection();
		BlueprintCueBaseReference val5 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook02Page003")).deserializedGuid;
		val4.Cues.Add(val5);
		val4.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions2).SetText("RanRomAranBook02Page002Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions3).SetText("RanRomAranBook02Page002Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetText("RanRomAranBook02Page002Cue0003.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text5).SetShowOnce().SetText("RanRomAranBook02Page002Ans0004.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0004Name, text6).SetConditions(conditions4).SetText("RanRomAranBook02Page002Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text7).SetShowOnce().SetText("RanRomAranBook02Page002Ans0005.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0005Name, text8).SetConditions(conditions5).SetText("RanRomAranBook02Page002Cue0005.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0006Name, text9).SetShowOnce().SetText("RanRomAranBook02Page002Ans0006.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0006Name, text10).SetConditions(conditions6).SetText("RanRomAranBook02Page002Cue0006.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text11).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook02Page002Ans0007.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0007Name, text12).SetConditions(conditions7).SetText("RanRomAranBook02Page002Cue0007.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0008Name, text13).SetConditions(conditions8).SetText("RanRomAranBook02Page002Cue0008.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0009Name, text14).SetConditions(conditions9).SetText("RanRomAranBook02Page002Cue0009.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0000Name, text15).SetConditions(conditions10).SetText("RanRomAranBook02Page002Cue0000.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0011Name, text16).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranBook02Page002Ans0011.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0011Name, text17).SetConditions(conditions11).SetText("RanRomAranBook02Page002Cue0011.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0012Name, text18).SetConditions(conditions12).SetText("RanRomAranBook02Page002Cue0012.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0013Name, text19).SetConditions(conditions13).SetText("RanRomAranBook02Page002Cue0013.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0014Name, text20).SetConditions(conditions14).SetText("RanRomAranBook02Page002Cue0014.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0015Name, text21).SetShowConditions(showConditions3).SetShowOnce()
			.SetText("RanRomAranBook02Page002Ans0015.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0015Name, text22).SetConditions(conditions15).SetText("RanRomAranBook02Page002Cue0015.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0016Name, text23).SetShowConditions(showConditions4).SetShowOnce()
			.SetText("RanRomAranBook02Page002Ans0016.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0016Name, text24).SetConditions(conditions16).SetText("RanRomAranBook02Page002Cue0016.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0017Name, text25).SetShowOnce().SetText("RanRomAranBook02Page002Ans0017.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0017Name, text26).SetConditions(conditions17).SetText("RanRomAranBook02Page002Cue0017.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0018Name, text27).SetConditions(conditions18).SetText("RanRomAranBook02Page002Cue0018.Text")
			.SetOnStop(ActionsBuilder.New().StartEtude("RanRomAranFlirt"))
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0019Name, text28).SetConditions(conditions19).SetText("RanRomAranBook02Page002Cue0019.Text")
			.SetShowOnce()
			.SetOnShow(ActionsBuilder.New().StartEtude("RanRomAranFlirt"))
			.Configure();
		AnswerConfigurator.New(Ans0010Name, text29).SetShowConditions(showConditions5).SetShowOnce()
			.SetText("RanRomAranBook02Page002Ans0010.Text")
			.SetNextCue(val4)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
