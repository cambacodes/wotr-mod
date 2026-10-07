using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook04Page005
{
	private static readonly string PageName = "RanRomAranBook04Page005";

	private static readonly string Cue0001Name = "RanRomAranBook04Page005Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook04Page005Ans0002";

	private static readonly string Cue0002Name = "RanRomAranBook04Page005Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook04Page005Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook04Page005Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook04Page005Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook04Page005Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook04Page005Ans0005";

	private static readonly string Ans0006Name = "RanRomAranBook04Page005Ans0006";

	public static string Configure()
	{
		//IL_0207: Unknown result type (might be due to invalid IL or missing references)
		//IL_020e: Expected O, but got Unknown
		//IL_020e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0215: Expected O, but got Unknown
		//IL_0221: Unknown result type (might be due to invalid IL or missing references)
		//IL_0226: Unknown result type (might be due to invalid IL or missing references)
		//IL_023d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0242: Unknown result type (might be due to invalid IL or missing references)
		//IL_0249: Expected O, but got Unknown
		//IL_0249: Unknown result type (might be due to invalid IL or missing references)
		//IL_0250: Expected O, but got Unknown
		//IL_025c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0261: Unknown result type (might be due to invalid IL or missing references)
		//IL_0278: Unknown result type (might be due to invalid IL or missing references)
		//IL_027d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0284: Expected O, but got Unknown
		//IL_0284: Unknown result type (might be due to invalid IL or missing references)
		//IL_028b: Expected O, but got Unknown
		//IL_0297: Unknown result type (might be due to invalid IL or missing references)
		//IL_029c: Unknown result type (might be due to invalid IL or missing references)
		//IL_02b3: Unknown result type (might be due to invalid IL or missing references)
		string text = "179ef1d1fdd74652a363531e20d47b19";
		string text2 = "dbfd1056436c4b0d8abaec9bc1cff4c0";
		string text3 = "627ebe72add745528be5c19d1df02b96";
		string text4 = "0ec855e2d8574eb69778dbbccae5e3aa";
		string text5 = "cb154cfaa63d46f7b5172a3aacd4bb9a";
		string text6 = "a1a79b072ff04bb684b9e7f607dd118c";
		string text7 = "ecb8ae31e64943e9af15099116baeac4";
		string text8 = "b062bce74cda4d4fa765963573530b79";
		string text9 = "c124dba5233b42eb869c9ce539b01fd7";
		string text10 = "1fc901c8b72e4438a718d2e211dc60a3";
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().FlagInRange("5db9ec615236f044083a5c6bd3292432", 999, 1).FlagInRange("RanRomCount", 999, 1)
			.UseOr();
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text7);
		BookPageConfigurator.New(PageName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text4)
			.AddToAnswers(text3)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToAnswers(text9)
			.AddToAnswers(text10)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Page006")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueSelection val5 = new CueSelection();
		BlueprintCueBaseReference val6 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val6).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Page008")).deserializedGuid;
		val5.Cues.Add(val6);
		val5.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook04Page005Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowOnce().SetText("RanRomAranBook04Page005Ans0002.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetConditions(conditions).SetText("RanRomAranBook04Page005Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text5).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook04Page005Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text6).SetConditions(conditions2).SetText("RanRomAranBook04Page005Cue0003.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text7).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranBook04Page005Ans0004.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0004Name, text8).SetConditions(conditions3).SetText("RanRomAranBook04Page005Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text9).SetShowOnce().SetText("RanRomAranBook04Page005Ans0005.Text")
			.SetOnSelect(ActionsBuilder.New().StartEtude("RanRomAranRomance"))
			.SetNextCue(val3)
			.Configure();
		AnswerConfigurator.New(Ans0006Name, text10).SetShowOnce().SetText("RanRomAranBook04Page005Ans0006.Text")
			.SetNextCue(val5)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
