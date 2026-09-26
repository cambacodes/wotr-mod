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

public class AranBook02Page003
{
	private static readonly string PageName = "RanRomAranBook02Page003";

	private static readonly string Cue0001Name = "RanRomAranBook02Page003Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook02Page003Cue0002";

	private static readonly string Cue0003Name = "RanRomAranBook02Page003Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook02Page003Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook02Page003Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook02Page003Ans0005";

	private static readonly string Cue0005Name = "RanRomAranBook02Page003Cue0005";

	private static readonly string Cue0006Name = "RanRomAranBook02Page003Cue0006";

	private static readonly string Cue0007Name = "RanRomAranBook02Page003Cue0007";

	private static readonly string Cue0008Name = "RanRomAranBook02Page003Cue0008";

	private static readonly string Cue0009Name = "RanRomAranBook02Page003Cue0009";

	private static readonly string Cue0000Name = "RanRomAranBook02Page003Cue0000";

	private static readonly string Ans0011Name = "RanRomAranBook02Page003Ans0011";

	private static readonly string Cue0011Name = "RanRomAranBook02Page003Cue0011";

	private static readonly string Ans0012Name = "RanRomAranBook02Page003Ans0012";

	private static readonly string Cue0012Name = "RanRomAranBook02Page003Cue0012";

	private static readonly string Ans0013Name = "RanRomAranBook02Page003Ans0013";

	private static readonly string Cue0013Name = "RanRomAranBook02Page003Cue0013";

	private static readonly string Ans0014Name = "RanRomAranBook02Page003Ans0014";

	private static readonly string Cue0014Name = "RanRomAranBook02Page003Cue0014";

	private static readonly string Ans0015Name = "RanRomAranBook02Page003Ans0015";

	private static readonly string Cue0015Name = "RanRomAranBook02Page003Cue0015";

	private static readonly string Ans0016Name = "RanRomAranBook02Page003Ans0016";

	private static readonly string Cue0016Name = "RanRomAranBook02Page003Cue0016";

	private static readonly string Ans0017Name = "RanRomAranBook02Page003Ans0017";

	private static readonly string Cue0017Name = "RanRomAranBook02Page003Cue0017";

	private static readonly string Ans0018Name = "RanRomAranBook02Page003Ans0018";

	private static readonly string Cue0018Name = "RanRomAranBook02Page003Cue0018";

	private static readonly string Ans0019Name = "RanRomAranBook02Page003Ans0019";

	public static string Configure()
	{
		//IL_00cf: Unknown result type (might be due to invalid IL or missing references)
		//IL_00d6: Expected O, but got Unknown
		//IL_09c2: Unknown result type (might be due to invalid IL or missing references)
		//IL_09c9: Expected O, but got Unknown
		//IL_09c9: Unknown result type (might be due to invalid IL or missing references)
		//IL_09d0: Expected O, but got Unknown
		//IL_09dc: Unknown result type (might be due to invalid IL or missing references)
		//IL_09e1: Unknown result type (might be due to invalid IL or missing references)
		//IL_09f8: Unknown result type (might be due to invalid IL or missing references)
		//IL_09fd: Unknown result type (might be due to invalid IL or missing references)
		//IL_0a04: Expected O, but got Unknown
		//IL_0a04: Unknown result type (might be due to invalid IL or missing references)
		//IL_0a0b: Expected O, but got Unknown
		//IL_0a17: Unknown result type (might be due to invalid IL or missing references)
		//IL_0a1c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0a33: Unknown result type (might be due to invalid IL or missing references)
		string text = "2a4cab14b0bc430bb777ed36b2525953";
		string text2 = "9198a533a24e48dbb4442a8b96353a67";
		string text3 = "1d4e685079254f84a64c07132c3ecb1a";
		string text4 = "1d9705fb064341aa9c579f5b135d9774";
		string text5 = "37e95c43648c491d9b31cf1db3f31107";
		string text6 = "0fd9d7cb8fbc48cd9a568de6cb20d36b";
		string text7 = "82f20f28e5d44c3b95774bf45fa57c50";
		string text8 = "e3c3f22eae744e86b61dcbba902635cf";
		string text9 = "3dbeb3381a8a40f1bba6b07325db4236";
		string text10 = "b9ab9000aafb41dfbb9a559dab10a549";
		string text11 = "870887533441464aa02bedb8bcd21fb2";
		string text12 = "6be963a49fa7493cb385f0bae7982c9d";
		string text13 = "309d4433f40e41719419f696bd6e57d9";
		string text14 = "778af6f520924b74909e0acf7137d541";
		string text15 = "ab24717aa6924bc5a222a9647bf860a0";
		string text16 = "306d4685cbb147df969967729fc26661";
		string text17 = "f04c5d81c25e465a8181a0be74b80f94";
		string text18 = "cbf7cd7eaa964a6cb4927bf0eb8b3cdd";
		string text19 = "3792c1fcf6114fddaa96b92bd8f83106";
		string text20 = "d828d3c58d8c4be099bdf8d5b858023f";
		string text21 = "b4f057c619074b0a9988486a2861b0a6";
		string text22 = "75fa285912dd45d8b518e8afa5187a02";
		string text23 = "761db4bc10b1404b9540555f1e4bc82b";
		string text24 = "bc36ef36b61941868b195cd10fc6e710";
		string text25 = "8271a7728f48483dbf088dead612be34";
		string text26 = "c0d9a7128d994383b7a9f25007dddd73";
		string text27 = "a0169d9c807c45f2932c391792b57a4e";
		string text28 = "c82cd2b1b66a4320a21cc1c5d0b06b63";
		string text29 = "75a4c204c70f46f6ae75c4294c46ea30";
		string text30 = "4fd74e66872b4f0f842aee46746eb6df";
		PlayerCharacter val = new PlayerCharacter();
		((Element)val).name = "pc" + text;
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranFlirt", negate: false, null, true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranFlirt", negate: true, null, true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text7).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected(text7).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val)
			.UnitClass(((object)CharacterClassRefs.AngelMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected(text7).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val)
			.UnitClass(((object)CharacterClassRefs.AngelMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val)
			.UnitClass(((object)CharacterClassRefs.TricksterMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val);
		ConditionsBuilder conditions8 = ConditionsBuilder.New().AnswerSelected(text7).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val)
			.UnitClass(((object)CharacterClassRefs.AngelMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val)
			.UnitClass(((object)CharacterClassRefs.TricksterMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val)
			.UnitClass(((object)CharacterClassRefs.AeonMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().AnswerSelected(text7).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val)
			.UnitClass(((object)CharacterClassRefs.AngelMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val)
			.UnitClass(((object)CharacterClassRefs.TricksterMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val)
			.UnitClass(((object)CharacterClassRefs.AeonMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder conditions10 = ConditionsBuilder.New().AnswerSelected(text14);
		ConditionsBuilder showConditions3 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder conditions11 = ConditionsBuilder.New().AnswerSelected(text16);
		ConditionsBuilder showConditions4 = ConditionsBuilder.New().AnswerSelected(text16);
		ConditionsBuilder conditions12 = ConditionsBuilder.New().AnswerSelected(text18);
		ConditionsBuilder showConditions5 = ConditionsBuilder.New().AnswerSelected(text18);
		ConditionsBuilder conditions13 = ConditionsBuilder.New().AnswerSelected(text20);
		ConditionsBuilder showConditions6 = ConditionsBuilder.New().AnswerSelected(text20);
		ConditionsBuilder conditions14 = ConditionsBuilder.New().AnswerSelected(text22);
		ConditionsBuilder showConditions7 = ConditionsBuilder.New().AnswerSelected(text22);
		ConditionsBuilder conditions15 = ConditionsBuilder.New().AnswerSelected(text24);
		ConditionsBuilder showConditions8 = ConditionsBuilder.New().AnswerSelected(text24);
		ConditionsBuilder conditions16 = ConditionsBuilder.New().AnswerSelected(text26);
		ConditionsBuilder showConditions9 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder conditions17 = ConditionsBuilder.New().AnswerSelected(text28);
		ConditionsBuilder showConditions10 = ConditionsBuilder.New().AnswerSelected(text16);
		BookPageConfigurator.New(PageName, text).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToCues(text9)
			.AddToCues(text10)
			.AddToCues(text11)
			.AddToCues(text12)
			.AddToCues(text13)
			.AddToCues(text15)
			.AddToAnswers(text14)
			.AddToCues(text17)
			.AddToAnswers(text16)
			.AddToCues(text19)
			.AddToAnswers(text18)
			.AddToCues(text21)
			.AddToAnswers(text20)
			.AddToCues(text23)
			.AddToAnswers(text22)
			.AddToCues(text25)
			.AddToAnswers(text24)
			.AddToCues(text27)
			.AddToAnswers(text26)
			.AddToCues(text29)
			.AddToAnswers(text28)
			.AddToAnswers(text30)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val2 = new CueSelection();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val2.Cues.Add(val3);
		val2.Strategy = (Strategy)0;
		CueSelection val4 = new CueSelection();
		BlueprintCueBaseReference val5 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook02Page004")).deserializedGuid;
		val4.Cues.Add(val5);
		val4.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomAranBook02Page003Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomAranBook02Page003Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetText("RanRomAranBook02Page003Cue0003.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text5).SetShowOnce().SetText("RanRomAranBook02Page003Ans0004.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0004Name, text6).SetConditions(conditions3).SetText("RanRomAranBook02Page003Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text7).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook02Page003Ans0005.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0005Name, text8).SetConditions(conditions4).SetText("RanRomAranBook02Page003Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text9).SetConditions(conditions5).SetText("RanRomAranBook02Page003Cue0006.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0007Name, text10).SetConditions(conditions6).SetText("RanRomAranBook02Page003Cue0007.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0008Name, text11).SetConditions(conditions7).SetText("RanRomAranBook02Page003Cue0008.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0009Name, text12).SetConditions(conditions8).SetText("RanRomAranBook02Page003Cue0009.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0000Name, text13).SetConditions(conditions9).SetText("RanRomAranBook02Page003Cue0000.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0011Name, text14).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranBook02Page003Ans0011.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0011Name, text15).SetConditions(conditions10).SetText("RanRomAranBook02Page003Cue0011.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0012Name, text16).SetShowConditions(showConditions3).SetShowOnce()
			.SetText("RanRomAranBook02Page003Ans0012.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0012Name, text17).SetConditions(conditions11).SetText("RanRomAranBook02Page003Cue0012.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0013Name, text18).SetShowConditions(showConditions4).SetShowOnce()
			.SetText("RanRomAranBook02Page003Ans0013.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0013Name, text19).SetConditions(conditions12).SetText("RanRomAranBook02Page003Cue0013.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0014Name, text20).SetShowConditions(showConditions5).SetShowOnce()
			.SetText("RanRomAranBook02Page003Ans0014.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0014Name, text21).SetConditions(conditions13).SetText("RanRomAranBook02Page003Cue0014.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0015Name, text22).SetShowConditions(showConditions6).SetShowOnce()
			.SetText("RanRomAranBook02Page003Ans0015.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0015Name, text23).SetConditions(conditions14).SetText("RanRomAranBook02Page003Cue0015.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0016Name, text24).SetShowConditions(showConditions7).SetShowOnce()
			.SetText("RanRomAranBook02Page003Ans0016.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0016Name, text25).SetConditions(conditions15).SetText("RanRomAranBook02Page003Cue0016.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0017Name, text26).SetShowConditions(showConditions8).SetShowOnce()
			.SetText("RanRomAranBook02Page003Ans0017.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0017Name, text27).SetConditions(conditions16).SetText("RanRomAranBook02Page003Cue0017.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0018Name, text28).SetShowConditions(showConditions9).SetShowOnce()
			.SetText("RanRomAranBook02Page003Ans0018.Text")
			.SetNextCue(val2)
			.SetOnSelect(ActionsBuilder.New().StartEtude("RanRomAranAlurFlirt"))
			.Configure();
		CueConfigurator.New(Cue0018Name, text29).SetConditions(conditions17).SetText("RanRomAranBook02Page003Cue0018.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0019Name, text30).SetShowConditions(showConditions10).SetShowOnce()
			.SetText("RanRomAranBook02Page003Ans0019.Text")
			.SetNextCue(val4)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
