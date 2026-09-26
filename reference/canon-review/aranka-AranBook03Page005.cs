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

public class AranBook03Page005
{
	private static readonly string PageName = "RanRomAranBook03Page005";

	private static readonly string Cue0001Name = "RanRomAranBook03Page005Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook03Page005Ans0002";

	private static readonly string Cue0002Name = "RanRomAranBook03Page005Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook03Page005Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook03Page005Cue0003";

	private static readonly string Cue0004Name = "RanRomAranBook03Page005Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook03Page005Ans0005";

	private static readonly string Cue0005Name = "RanRomAranBook03Page005Cue0005";

	private static readonly string Ans0006Name = "RanRomAranBook03Page005Ans0006";

	private static readonly string Ans0007Name = "RanRomAranBook03Page005Ans0007";

	public static string Configure()
	{
		//IL_004a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0051: Expected O, but got Unknown
		//IL_038c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0393: Expected O, but got Unknown
		//IL_0393: Unknown result type (might be due to invalid IL or missing references)
		//IL_039a: Expected O, but got Unknown
		//IL_03a6: Unknown result type (might be due to invalid IL or missing references)
		//IL_03ab: Unknown result type (might be due to invalid IL or missing references)
		//IL_03c2: Unknown result type (might be due to invalid IL or missing references)
		//IL_03c7: Unknown result type (might be due to invalid IL or missing references)
		//IL_03ce: Expected O, but got Unknown
		//IL_03ce: Unknown result type (might be due to invalid IL or missing references)
		//IL_03d5: Expected O, but got Unknown
		//IL_03e1: Unknown result type (might be due to invalid IL or missing references)
		//IL_03e6: Unknown result type (might be due to invalid IL or missing references)
		//IL_03fd: Unknown result type (might be due to invalid IL or missing references)
		//IL_0402: Unknown result type (might be due to invalid IL or missing references)
		//IL_0409: Expected O, but got Unknown
		//IL_0409: Unknown result type (might be due to invalid IL or missing references)
		//IL_0410: Expected O, but got Unknown
		//IL_041c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0421: Unknown result type (might be due to invalid IL or missing references)
		//IL_0438: Unknown result type (might be due to invalid IL or missing references)
		string text = "6a0105c534e9480691d50309bc71f41b";
		string text2 = "d6a7d604f83f4891a924528ed2ea4042";
		string text3 = "4596789166a14dcd920e72a822b28beb";
		string text4 = "2466dcbb70634f428c64ef3393bb5979";
		string text5 = "3c2d25f4d3f1482c92b9d5f2bd0b8617";
		string text6 = "15a3cf0630de459abb0fda98cfc3e002";
		string text7 = "5fdedb61a8364586b8aa66a23a2fc781";
		string text8 = "580e747e61c2487398579134ee0abb8a";
		string text9 = "9d394a6681db433ca15811cd5f9a3c5b";
		string text10 = "53949effa6b0467ca2492ef669674cc9";
		string text11 = "bb7b8143322248a29eaffbb44676e141";
		PlayerCharacter val = new PlayerCharacter();
		((Element)val).name = "pc" + text;
		ConditionsBuilder conditions = ConditionsBuilder.New().UnitClass(((object)CharacterClassRefs.AngelMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val).UnitClass(((object)CharacterClassRefs.AeonMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val)
			.UseOr();
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected("3c2d25f4d3f1482c92b9d5f2bd0b8617", null, negate: true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().AnswerSelected("4596789166a14dcd920e72a822b28beb", null, negate: true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected("3c2d25f4d3f1482c92b9d5f2bd0b8617").AnswerSelected("4596789166a14dcd920e72a822b28beb")
			.UseOr();
		ConditionsBuilder showConditions3 = ConditionsBuilder.New().AnswerSelected("3c2d25f4d3f1482c92b9d5f2bd0b8617").AnswerSelected("4596789166a14dcd920e72a822b28beb")
			.UseOr();
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text8);
		ConditionsBuilder showConditions4 = ConditionsBuilder.New().AnswerSelected("3c2d25f4d3f1482c92b9d5f2bd0b8617").AnswerSelected("4596789166a14dcd920e72a822b28beb")
			.UseOr();
		ConditionsBuilder showConditions5 = ConditionsBuilder.New().AnswerSelected("3c2d25f4d3f1482c92b9d5f2bd0b8617").AnswerSelected("4596789166a14dcd920e72a822b28beb")
			.UseOr();
		BookPageConfigurator.New(PageName, text).SetImageLink("52163ec59b7bf62408b1b24137843bba").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text4)
			.AddToAnswers(text3)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text7)
			.AddToCues(text9)
			.AddToAnswers(text8)
			.AddToAnswers(text10)
			.AddToAnswers(text11)
			.SetConditions(conditions)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val2 = new CueSelection();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val2.Cues.Add(val3);
		val2.Strategy = (Strategy)0;
		CueSelection val4 = new CueSelection();
		BlueprintCueBaseReference val5 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook03Page007")).deserializedGuid;
		val4.Cues.Add(val5);
		val4.Strategy = (Strategy)0;
		CueSelection val6 = new CueSelection();
		BlueprintCueBaseReference val7 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val7).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook03End")).deserializedGuid;
		val6.Cues.Add(val7);
		val6.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook03Page005Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook03Page005Ans0002.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetConditions(conditions2).SetText("RanRomAranBook03Page005Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text5).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranBook03Page005Ans0003.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0003Name, text6).SetConditions(conditions3).SetText("RanRomAranBook03Page005Cue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text7).SetConditions(conditions4).SetText("RanRomAranBook03Page005Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text8).SetShowConditions(showConditions3).SetShowOnce()
			.SetText("RanRomAranBook03Page005Ans0005.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0005Name, text9).SetConditions(conditions5).SetText("RanRomAranBook03Page005Cue0005.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0006Name, text10).SetShowConditions(showConditions4).SetShowOnce()
			.SetText("RanRomAranBook03Page005Ans0006.Text")
			.SetNextCue(val4)
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text11).SetShowConditions(showConditions5).SetShowOnce()
			.SetText("RanRomAranBook03Page005Ans0007.Text")
			.SetNextCue(val6)
			.SetOnSelect(ActionsBuilder.New().CompleteEtude("RanRomAranFlirt"))
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
