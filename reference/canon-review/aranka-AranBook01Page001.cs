using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook01Page001
{
	private static readonly string PageName = "RanRomAranBook01Page001";

	private static readonly string PageName2 = "RanRomAranBook01Page101";

	private static readonly string Cue0001Name = "RanRomAranBook01Page001Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook01Page001Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook01Page001Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook01Page001Cue0003";

	private static readonly string Cue0004Name = "RanRomAranBook01Page001Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook01Page001Ans0005";

	private static readonly string Cue0005Name = "RanRomAranBook01Page001Cue0005";

	private static readonly string Cue0006Name = "RanRomAranBook01Page001Cue0006";

	private static readonly string Ans0007Name = "RanRomAranBook01Page001Ans0007";

	private static readonly string Cue0007Name = "RanRomAranBook01Page001Cue0007";

	private static readonly string Ans0008Name = "RanRomAranBook01Page001Ans0008";

	private static readonly string Cue0008Name = "RanRomAranBook01Page001Cue0008";

	private static readonly string Ans0009Name = "RanRomAranBook01Page001Ans0009";

	private static readonly string Cue0009Name = "RanRomAranBook01Page001Cue0009";

	private static readonly string Cue0000Name = "RanRomAranBook01Page001Cue0000";

	private static readonly string Ans0011Name = "RanRomAranBook01Page001Ans0011";

	private static readonly string Cue0011Name = "RanRomAranBook01Page001Cue0011";

	private static readonly string Ans0012Name = "RanRomAranBook01Page001Ans0012";

	private static readonly string Cue0012Name = "RanRomAranBook01Page001Cue0012";

	private static readonly string Ans0013Name = "RanRomAranBook01Page001Ans0013";

	public static string Configure()
	{
		//IL_08b5: Unknown result type (might be due to invalid IL or missing references)
		//IL_08bc: Expected O, but got Unknown
		//IL_08bc: Unknown result type (might be due to invalid IL or missing references)
		//IL_08c3: Expected O, but got Unknown
		//IL_08c3: Unknown result type (might be due to invalid IL or missing references)
		//IL_08ca: Expected O, but got Unknown
		//IL_08d6: Unknown result type (might be due to invalid IL or missing references)
		//IL_08db: Unknown result type (might be due to invalid IL or missing references)
		//IL_08ec: Unknown result type (might be due to invalid IL or missing references)
		//IL_08f1: Unknown result type (might be due to invalid IL or missing references)
		//IL_0917: Unknown result type (might be due to invalid IL or missing references)
		//IL_091c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0923: Expected O, but got Unknown
		//IL_0923: Unknown result type (might be due to invalid IL or missing references)
		//IL_092a: Expected O, but got Unknown
		//IL_0936: Unknown result type (might be due to invalid IL or missing references)
		//IL_093b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0952: Unknown result type (might be due to invalid IL or missing references)
		string text = "5573fd69c9f04efebb8d6a276da2188e";
		string guid = "430140ab7d674b33adb2637b57aef160";
		string text2 = "ae2410c49fb44f298f9d7b7cf25fa4ff";
		string text3 = "ad619d38269642209e6daf8a423e57fc";
		string text4 = "f133fde32f4c458e8684d06ba86d35ad";
		string text5 = "bb0ed9027cc94a7c8076f85fdf54e038";
		string text6 = "ac8d32b0f33d4c79b30f8fec3891678d";
		string text7 = "e33f0d1516a44c28b0f2e03e6c6babaa";
		string text8 = "3c6b397b55314faca3ddd53bf8d612eb";
		string text9 = "fa8fa9d277e54a0eaef85db899e48a3d";
		string text10 = "a3f897431dcf4684ae41e13f862ec318";
		string text11 = "91a9975c4dfa479ebdff77fa42aa0812";
		string text12 = "f8a9bc4b98b3440986a5e301ea74a8be";
		string text13 = "936ec0dc158747049b9c04fa8c665908";
		string text14 = "0896daf6e31446f4816cfd26d224cd20";
		string text15 = "b401d374d0a644ccaf4b5bdf99346f72";
		string text16 = "db06d2d27025412d9a97e706e23a2f1c";
		string text17 = "0b5fa4a552fb48cb9427b0ea3f1139cb";
		string text18 = "af2e3cb574bc48868d5d4fa1dbf77036";
		string text19 = "5a295f8c5e824899bfb7378076ee464b";
		string text20 = "1b29fe58cc274c15ad41a513a870b082";
		string text21 = "55376eb3a369497a8ad9056e47b2b2b8";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "0e20d73ea0da6a94d94a6b42035a1ce0", negate: false, null, true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "0e20d73ea0da6a94d94a6b42035a1ce0", negate: true, null, true);
		ConditionsBuilder showConditions = ConditionsBuilder.New().EtudeStatus(null, null, "0e20d73ea0da6a94d94a6b42035a1ce0", negate: false, null, true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text4).EtudeStatus(null, null, "d7169995e449fdc4db861ddf0b9beff8", negate: true, null, true);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text4).EtudeStatus(null, null, "d7169995e449fdc4db861ddf0b9beff8", negate: false, null, true);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().AnswerSelected(text4);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text7).EtudeStatus(null, null, "d7169995e449fdc4db861ddf0b9beff8", negate: true, null, true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected(text7).EtudeStatus(null, null, "d7169995e449fdc4db861ddf0b9beff8", negate: false, null, true);
		ConditionsBuilder showConditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "0e20d73ea0da6a94d94a6b42035a1ce0", negate: true, null, true);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected(text10);
		ConditionsBuilder conditions8 = ConditionsBuilder.New().AnswerSelected(text12);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().AnswerSelected(text14).EtudeStatus(null, null, "0e20d73ea0da6a94d94a6b42035a1ce0", negate: false, null, true);
		ConditionsBuilder conditions10 = ConditionsBuilder.New().AnswerSelected(text14).EtudeStatus(null, null, "0e20d73ea0da6a94d94a6b42035a1ce0", negate: true, null, true);
		ConditionsBuilder showConditions4 = ConditionsBuilder.New().AnswerSelected(text14);
		ConditionsBuilder conditions11 = ConditionsBuilder.New().AnswerSelected(text17);
		ConditionsBuilder showConditions5 = ConditionsBuilder.New().AnswerSelected(text14);
		ConditionsBuilder conditions12 = ConditionsBuilder.New().AnswerSelected(text19);
		ConditionsBuilder showConditions6 = ConditionsBuilder.New().AnswerSelected(text17).AnswerSelected(text19);
		BookPageConfigurator.New(PageName, text).SetImageLink("f96ad5fa9c59d7549adff4c90f0703ab").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text5)
			.AddToAnswers(text4)
			.AddToCues(text6)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToCues(text9)
			.AddToCues(text11)
			.AddToAnswers(text10)
			.AddToCues(text13)
			.AddToAnswers(text12)
			.AddToCues(text15)
			.AddToAnswers(text14)
			.AddToCues(text16)
			.AddToCues(text18)
			.AddToAnswers(text17)
			.AddToCues(text20)
			.AddToAnswers(text19)
			.AddToAnswers(text21)
			.SetConditions(conditions)
			.AddToCues("RanRomFiller")
			.Configure();
		BookPageConfigurator.New(PageName2, guid).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text5)
			.AddToAnswers(text4)
			.AddToCues(text6)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToCues(text9)
			.AddToCues(text11)
			.AddToAnswers(text10)
			.AddToCues(text13)
			.AddToAnswers(text12)
			.AddToCues(text15)
			.AddToAnswers(text14)
			.AddToCues(text16)
			.AddToCues(text18)
			.AddToAnswers(text17)
			.AddToCues(text20)
			.AddToAnswers(text19)
			.AddToAnswers(text21)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName2)).deserializedGuid;
		val.Cues.Add(val2);
		val.Cues.Add(val3);
		val.Strategy = (Strategy)0;
		CueSelection val4 = new CueSelection();
		BlueprintCueBaseReference val5 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook01Page002")).deserializedGuid;
		val4.Cues.Add(val5);
		val4.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomAranBook01Page001Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomAranBook01Page001Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text4).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook01Page001Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text5).SetConditions(conditions3).SetText("RanRomAranBook01Page001Cue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text6).SetConditions(conditions4).SetText("RanRomAranBook01Page001Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text7).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranBook01Page001Ans0005.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0005Name, text8).SetConditions(conditions5).SetText("RanRomAranBook01Page001Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text9).SetConditions(conditions6).SetText("RanRomAranBook01Page001Cue0006.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text10).SetShowConditions(showConditions3).SetShowOnce()
			.SetText("RanRomAranBook01Page001Ans0007.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0007Name, text11).SetConditions(conditions7).SetText("RanRomAranBook01Page001Cue0007.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0008Name, text12).SetShowOnce().SetText("RanRomAranBook01Page001Ans0008.Text")
			.SetNextCue(val)
			.SetOnSelect(ActionsBuilder.New().StartEtude("RanRomAranFlirt"))
			.Configure();
		CueConfigurator.New(Cue0008Name, text13).SetConditions(conditions8).SetText("RanRomAranBook01Page001Cue0008.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0009Name, text14).SetShowOnce().SetText("RanRomAranBook01Page001Ans0009.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0009Name, text15).SetConditions(conditions9).SetText("RanRomAranBook01Page001Cue0009.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0000Name, text16).SetConditions(conditions10).SetText("RanRomAranBook01Page001Cue0000.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0011Name, text17).SetShowConditions(showConditions4).SetShowOnce()
			.SetText("RanRomAranBook01Page001Ans0011.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0011Name, text18).SetConditions(conditions11).SetText("RanRomAranBook01Page001Cue0011.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0012Name, text19).SetShowConditions(showConditions5).SetShowOnce()
			.SetText("RanRomAranBook01Page001Ans0012.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0012Name, text20).SetConditions(conditions12).SetText("RanRomAranBook01Page001Cue0012.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0013Name, text21).SetShowConditions(showConditions6).SetShowOnce()
			.SetText("RanRomAranBook01Page001Ans0013.Text")
			.SetNextCue(val4)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
