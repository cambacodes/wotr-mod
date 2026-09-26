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

public class AranBook03Page002
{
	private static readonly string PageName = "RanRomAranBook03Page002";

	private static readonly string Cue0001Name = "RanRomAranBook03Page002Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook03Page002Ans0002";

	private static readonly string Cue0002Name = "RanRomAranBook03Page002Cue0002";

	private static readonly string Cue0003Name = "RanRomAranBook03Page002Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook03Page002Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook03Page002Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook03Page002Ans0005";

	private static readonly string Cue0005Name = "RanRomAranBook03Page002Cue0005";

	private static readonly string Cue0006Name = "RanRomAranBook03Page002Cue0006";

	private static readonly string Cue0007Name = "RanRomAranBook03Page002Cue0007";

	private static readonly string Cue0008Name = "RanRomAranBook03Page002Cue0008";

	private static readonly string Ans0009Name = "RanRomAranBook03Page002Ans0009";

	private static readonly string Cue0009Name = "RanRomAranBook03Page002Cue0009";

	private static readonly string Ans0000Name = "RanRomAranBook03Page002Ans0000";

	public static string Configure()
	{
		//IL_0066: Unknown result type (might be due to invalid IL or missing references)
		//IL_006d: Expected O, but got Unknown
		//IL_008b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0092: Expected O, but got Unknown
		//IL_0436: Unknown result type (might be due to invalid IL or missing references)
		//IL_043d: Expected O, but got Unknown
		//IL_043d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0444: Expected O, but got Unknown
		//IL_0450: Unknown result type (might be due to invalid IL or missing references)
		//IL_0455: Unknown result type (might be due to invalid IL or missing references)
		//IL_046c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0471: Unknown result type (might be due to invalid IL or missing references)
		//IL_0478: Expected O, but got Unknown
		//IL_0478: Unknown result type (might be due to invalid IL or missing references)
		//IL_047f: Expected O, but got Unknown
		//IL_047f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0486: Expected O, but got Unknown
		//IL_0486: Unknown result type (might be due to invalid IL or missing references)
		//IL_048d: Expected O, but got Unknown
		//IL_0499: Unknown result type (might be due to invalid IL or missing references)
		//IL_049e: Unknown result type (might be due to invalid IL or missing references)
		//IL_04af: Unknown result type (might be due to invalid IL or missing references)
		//IL_04b4: Unknown result type (might be due to invalid IL or missing references)
		//IL_04c5: Unknown result type (might be due to invalid IL or missing references)
		//IL_04ca: Unknown result type (might be due to invalid IL or missing references)
		//IL_04ff: Unknown result type (might be due to invalid IL or missing references)
		string text = "39adc34cb6ed4e8490408bb1f231e4d1";
		string text2 = "c20caf58c6c34b6ba41a3bd508b49064";
		string text3 = "8ba987691e2a4ba19dd56dbd5f7cc57b";
		string text4 = "53445840206549baa52e1cb58ae1eb3a";
		string text5 = "559b391b6774486e91dda98aa5c0c8d5";
		string text6 = "6fa2fbfee97249ab802c5567559e1bc6";
		string text7 = "e1b4f8d099a240f3aa9d7adc3c0358af";
		string text8 = "42dcd31ede2f440f87e639e6ad1d936d";
		string text9 = "c458199ac99841e898d4b485c338ffe9";
		string text10 = "6393fa3463b447f6808a14a729ce4eee";
		string text11 = "8636263df5ce4e0e8953e2e9e12acd5e";
		string text12 = "3f081e6e96fb4ffa82d4301dc37a1fdc";
		string text13 = "3428470153ab4ff19ba62060397d1a8c";
		string text14 = "61e2e258b03342fea536adea55e85747";
		string text15 = "fb76ca51ad514aad943379718646746c";
		IntConstant val = new IntConstant();
		val.Value = 1;
		((Element)val).name = "constant1" + PageName;
		PlayerCharacter val2 = new PlayerCharacter();
		((Element)val2).name = "pc" + text;
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected(text3).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val2);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text3).UnitClass(((object)CharacterClassRefs.AzataMythicClass.Reference).ToString(), null, null, null, null, negate: true, (UnitEvaluator?)(object)val2);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text6);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text8);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text8).FlagInRange("RanRomAranConf", 999, 2);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected(text8).FlagInRange("RanRomAranConf", 1, 1);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected(text8).FlagInRange("RanRomAranConf", 0, -999);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().AnswerSelected(text8).FlagInRange("RanRomAranConf", 999, 1);
		ConditionsBuilder conditions8 = ConditionsBuilder.New().AnswerSelected(text13);
		ConditionsBuilder showConditions3 = ConditionsBuilder.New().AnswerSelected(text8);
		BookPageConfigurator.New(PageName, text).SetImageLink("52163ec59b7bf62408b1b24137843bba").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text4)
			.AddToAnswers(text3)
			.AddToCues(text5)
			.AddToCues(text7)
			.AddToAnswers(text6)
			.AddToCues(text9)
			.AddToAnswers(text8)
			.AddToCues(text10)
			.AddToCues(text11)
			.AddToCues(text12)
			.AddToCues(text14)
			.AddToAnswers(text13)
			.AddToAnswers(text15)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueSelection val5 = new CueSelection();
		BlueprintCueBaseReference val6 = new BlueprintCueBaseReference();
		BlueprintCueBaseReference val7 = new BlueprintCueBaseReference();
		BlueprintCueBaseReference val8 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val6).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook03Page003")).deserializedGuid;
		((BlueprintReferenceBase)val7).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook03Page004")).deserializedGuid;
		((BlueprintReferenceBase)val8).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook03End")).deserializedGuid;
		val5.Cues.Add(val6);
		val5.Cues.Add(val7);
		val5.Cues.Add(val8);
		val5.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook03Page002Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowOnce().SetText("RanRomAranBook03Page002Ans0002.Text")
			.SetNextCue(val3)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetConditions(conditions).SetText("RanRomAranBook03Page002Cue0002.Text")
			.SetShowOnce()
			.SetOnShow(ActionsBuilder.New().IncrementFlagValue("RanRomAranConf", true, (IntEvaluator?)(object)val))
			.Configure();
		CueConfigurator.New(Cue0003Name, text5).SetConditions(conditions2).SetText("RanRomAranBook03Page002Cue0003.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text6).SetShowOnce().SetText("RanRomAranBook03Page002Ans0004.Text")
			.SetNextCue(val3)
			.Configure();
		CueConfigurator.New(Cue0004Name, text7).SetConditions(conditions3).SetText("RanRomAranBook03Page002Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text8).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook03Page002Ans0005.Text")
			.SetNextCue(val3)
			.Configure();
		CueConfigurator.New(Cue0005Name, text9).SetConditions(conditions4).SetText("RanRomAranBook03Page002Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text10).SetConditions(conditions5).SetText("RanRomAranBook03Page002Cue0006.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0007Name, text11).SetConditions(conditions6).SetText("RanRomAranBook03Page002Cue0007.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0008Name, text12).SetConditions(conditions7).SetText("RanRomAranBook03Page002Cue0008.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0009Name, text13).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranBook03Page002Ans0009.Text")
			.SetNextCue(val3)
			.Configure();
		CueConfigurator.New(Cue0009Name, text14).SetConditions(conditions8).SetText("RanRomAranBook03Page002Cue0009.Text")
			.SetShowOnce()
			.SetOnShow(ActionsBuilder.New().IncrementFlagValue("RanRomAranConf", true, (IntEvaluator?)(object)val))
			.Configure();
		AnswerConfigurator.New(Ans0000Name, text15).SetShowConditions(showConditions3).SetShowOnce()
			.SetText("RanRomAranBook03Page002Ans0000.Text")
			.SetNextCue(val5)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
