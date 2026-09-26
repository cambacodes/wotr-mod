using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook03Page007
{
	private static readonly string PageName = "RanRomAranBook03Page007";

	private static readonly string Cue0001Name = "RanRomAranBook03Page007Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook03Page007Cue0002";

	private static readonly string Cue0003Name = "RanRomAranBook03Page007Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook03Page007Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook03Page007Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook03Page007Ans0005";

	private static readonly string Cue0005Name = "RanRomAranBook03Page007Cue0005";

	private static readonly string Ans0006Name = "RanRomAranBook03Page007Ans0006";

	private static readonly string Cue0006Name = "RanRomAranBook03Page007Cue0006";

	private static readonly string Ans0007Name = "RanRomAranBook03Page007Ans0007";

	private static readonly string Cue0007Name = "RanRomAranBook03Page007Cue0007";

	private static readonly string Ans0008Name = "RanRomAranBook03Page007Ans0008";

	private static readonly string Cue0008Name = "RanRomAranBook03Page007Cue0008";

	private static readonly string Ans0009Name = "RanRomAranBook03Page007Ans0009";

	private static readonly string Cue0009Name = "RanRomAranBook03Page007Cue0009";

	private static readonly string Ans0000Name = "RanRomAranBook03Page007Ans0000";

	private static readonly string Ans0011Name = "RanRomAranBook03Page007Ans0011";

	public static string Configure()
	{
		//IL_044c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0453: Expected O, but got Unknown
		//IL_0453: Unknown result type (might be due to invalid IL or missing references)
		//IL_045a: Expected O, but got Unknown
		//IL_0466: Unknown result type (might be due to invalid IL or missing references)
		//IL_046b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0482: Unknown result type (might be due to invalid IL or missing references)
		//IL_0487: Unknown result type (might be due to invalid IL or missing references)
		//IL_048e: Expected O, but got Unknown
		//IL_048e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0495: Expected O, but got Unknown
		//IL_04a1: Unknown result type (might be due to invalid IL or missing references)
		//IL_04a6: Unknown result type (might be due to invalid IL or missing references)
		//IL_04bd: Unknown result type (might be due to invalid IL or missing references)
		string text = "ead545ebd2624ced9aa623c29e718b68";
		string text2 = "afb30f6ff44941abaf9a32964b965298";
		string text3 = "906d3c8e5b1d46559451b4dfc5c93b14";
		string text4 = "69552ce794c74a6ebf89c275158e9dce";
		string text5 = "ec5b716d474f4a6e854e87528f9e24ea";
		string text6 = "671127c2e20c4e3aa9608e4eeb953631";
		string text7 = "479ade1459834f7286aaaf77ba352a4b";
		string text8 = "2f014179f7a64086823089c3021efc15";
		string text9 = "53a1821d374c425f9c439613b114a064";
		string text10 = "d2f02eefdbb64de89a052ff17eded9bf";
		string text11 = "cebef2c3fb424da48a7391748f52adfd";
		string text12 = "446609cc7d4948a3be9631dca1ca3b87";
		string text13 = "760062c37ae4421494c8fa1561871ccf";
		string text14 = "fb0cc9f3a49a4d539cb48db8f3154289";
		string text15 = "b4bdddc31034453d82df13ff9fc5fac6";
		string text16 = "695a1e57f26641e9abd018a609fce72f";
		string text17 = "8ab68171a8674582bcaa705997840688";
		string text18 = "b2d319a4e87f4ef0a45a489b56906cc8";
		ConditionsBuilder conditions = ConditionsBuilder.New().CueSeen("6a0105c534e9480691d50309bc71f41b");
		ConditionsBuilder conditions2 = ConditionsBuilder.New().CueSeen("6a0105c534e9480691d50309bc71f41b", null, negate: true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text9);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().FlagInRange("5db9ec615236f044083a5c6bd3292432", 999, 1).FlagInRange("RanRomCount", 999, 1)
			.UseOr();
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().AnswerSelected(text7).AddOrAndLogic(conditions6);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected(text11);
		ConditionsBuilder showConditions3 = ConditionsBuilder.New().AnswerSelected(text7).EtudeStatus(null, null, "6a3fdd0758fe78d4aa2c3b26d7614fbc", negate: false, null, true);
		ConditionsBuilder conditions8 = ConditionsBuilder.New().AnswerSelected(text13);
		ConditionsBuilder showConditions4 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().AnswerSelected(text15);
		ConditionsBuilder showConditions5 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder showConditions6 = ConditionsBuilder.New().AnswerSelected(text7);
		BookPageConfigurator.New(PageName, text).SetImageLink("52163ec59b7bf62408b1b24137843bba").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
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
			.AddToCues(text14)
			.AddToCues(text16)
			.AddToAnswers(text15)
			.AddToAnswers(text17)
			.AddToAnswers(text18)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook03End")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomAranBook03Page007Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomAranBook03Page007Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetText("RanRomAranBook03Page007Cue0003.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text5).SetShowOnce().SetText("RanRomAranBook03Page007Ans0004.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0004Name, text6).SetConditions(conditions3).SetText("RanRomAranBook03Page007Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text7).SetShowOnce().SetText("RanRomAranBook03Page007Ans0005.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0005Name, text8).SetConditions(conditions4).SetText("RanRomAranBook03Page007Cue0005.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0006Name, text9).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook03Page007Ans0006.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0006Name, text10).SetConditions(conditions5).SetText("RanRomAranBook03Page007Cue0006.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text11).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranBook03Page007Ans0007.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0007Name, text12).SetConditions(conditions7).SetText("RanRomAranBook03Page007Cue0007.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0008Name, text13).SetShowConditions(showConditions3).SetShowOnce()
			.SetText("RanRomAranBook03Page007Ans0008.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0008Name, text14).SetConditions(conditions8).SetText("RanRomAranBook03Page007Cue0008.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0009Name, text15).SetShowConditions(showConditions4).SetShowOnce()
			.SetText("RanRomAranBook03Page007Ans0009.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0009Name, text16).SetConditions(conditions9).SetText("RanRomAranBook03Page007Cue0009.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0000Name, text17).SetShowConditions(showConditions5).SetShowOnce()
			.SetText("RanRomAranBook03Page007Ans0000.Text")
			.SetNextCue(val3)
			.SetOnSelect(ActionsBuilder.New().StartEtude("RanRomAranRomance"))
			.Configure();
		AnswerConfigurator.New(Ans0011Name, text18).SetShowConditions(showConditions6).SetShowOnce()
			.SetText("RanRomAranBook03Page007Ans0011.Text")
			.SetNextCue(val3)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
