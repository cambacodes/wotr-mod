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

public class AranBook03Page003
{
	private static readonly string PageName = "RanRomAranBook03Page003";

	private static readonly string Cue0001Name = "RanRomAranBook03Page003Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook03Page003Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook03Page003Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook03Page003Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook03Page003Ans0004";

	private static readonly string Ans0005Name = "RanRomAranBook03Page003Ans0005";

	public static string Configure()
	{
		//IL_002e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0035: Expected O, but got Unknown
		//IL_0230: Unknown result type (might be due to invalid IL or missing references)
		//IL_0237: Expected O, but got Unknown
		//IL_0237: Unknown result type (might be due to invalid IL or missing references)
		//IL_023e: Expected O, but got Unknown
		//IL_024a: Unknown result type (might be due to invalid IL or missing references)
		//IL_024f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0266: Unknown result type (might be due to invalid IL or missing references)
		//IL_026b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0272: Expected O, but got Unknown
		//IL_0272: Unknown result type (might be due to invalid IL or missing references)
		//IL_0279: Expected O, but got Unknown
		//IL_0285: Unknown result type (might be due to invalid IL or missing references)
		//IL_028a: Unknown result type (might be due to invalid IL or missing references)
		//IL_02a1: Unknown result type (might be due to invalid IL or missing references)
		string text = "5fedc221cd864f868c7d7dbb7823e2d2";
		string text2 = "0f077ad32cf24ba4bb72e7149a352e57";
		string text3 = "8758a1fdf5d64679bcc5383947c2911a";
		string text4 = "6b817ca0113a4b22b2fbc506be186b41";
		string text5 = "b96c9f280af5466d8be9aa4363debdf2";
		string text6 = "8c8eaea6fd444542a37939e326fd60cd";
		string text7 = "4a7d20e8a9bf40f5a9a4ae09e729d72e";
		PlayerCharacter val = new PlayerCharacter();
		((Element)val).name = "pc" + text;
		ConditionsBuilder conditions = ConditionsBuilder.New().UnitClass(((object)CharacterClassRefs.DemonMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val).UnitClass(((object)CharacterClassRefs.LichMythicClass.Reference).ToString(), null, null, null, null, negate: false, (UnitEvaluator?)(object)val)
			.UseOr();
		ConditionsBuilder conditionsBuilder = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranFlirt", negate: false, null, true).EtudeStatus(null, null, "RanRomAranFlirtEnd", negate: true, null, true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AddOrAndLogic(conditionsBuilder, negate: true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text4);
		BookPageConfigurator.New(PageName, text).SetImageLink("52163ec59b7bf62408b1b24137843bba").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text5)
			.AddToAnswers(text4)
			.AddToAnswers(text6)
			.AddToAnswers(text7)
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
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook03End")).deserializedGuid;
		val4.Cues.Add(val5);
		val4.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditionsBuilder).SetText("RanRomAranBook03Page003Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomAranBook03Page003Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text4).SetShowConditions(conditionsBuilder).SetShowOnce()
			.SetText("RanRomAranBook03Page003Ans0003.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0003Name, text5).SetConditions(conditions3).SetText("RanRomAranBook03Page003Cue0003.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text6).SetShowOnce().SetText("RanRomAranBook03Page003Ans0004.Text")
			.SetNextCue(val4)
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text7).SetShowOnce().SetText("RanRomAranBook03Page003Ans0005.Text")
			.SetNextCue(val4)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
