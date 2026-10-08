using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.DialogSystem;
using Kingmaker.ElementsSystem;

namespace RanRomance.Aran;

public class AranBook02Page004
{
	private static readonly string PageName = "RanRomAranBook02Page004";

	private static readonly string Cue0001Name = "RanRomAranBook02Page004Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook02Page004Ans0002";

	private static readonly string Cue0002Name = "RanRomAranBook02Page004Cue0002";

	private static readonly string Cue0003Name = "RanRomAranBook02Page004Cue0003";

	private static readonly string Cue0004Name = "RanRomAranBook02Page004Cue0004";

	private static readonly string Cue0005Name = "RanRomAranBook02Page004Cue0005";

	private static readonly string Ans0006Name = "RanRomAranBook02Page004Ans0006";

	private static readonly string Cue0006Name = "RanRomAranBook02Page004Cue0006";

	private static readonly string Ans0007Name = "RanRomAranBook02Page004Ans0007";

	private static readonly string Ans0008Name = "RanRomAranBook02Page004Ans0008";

	private static readonly string Ans0009Name = "RanRomAranBook02Page004Ans0009";

	public static string Configure()
	{
		//IL_0051: Unknown result type (might be due to invalid IL or missing references)
		//IL_0058: Expected O, but got Unknown
		//IL_03a3: Unknown result type (might be due to invalid IL or missing references)
		//IL_03aa: Expected O, but got Unknown
		//IL_03aa: Unknown result type (might be due to invalid IL or missing references)
		//IL_03b1: Expected O, but got Unknown
		//IL_03bd: Unknown result type (might be due to invalid IL or missing references)
		//IL_03c2: Unknown result type (might be due to invalid IL or missing references)
		//IL_03d9: Unknown result type (might be due to invalid IL or missing references)
		//IL_03de: Unknown result type (might be due to invalid IL or missing references)
		//IL_03e5: Expected O, but got Unknown
		//IL_03e5: Unknown result type (might be due to invalid IL or missing references)
		//IL_03ec: Expected O, but got Unknown
		//IL_03f8: Unknown result type (might be due to invalid IL or missing references)
		//IL_03fd: Unknown result type (might be due to invalid IL or missing references)
		//IL_0414: Unknown result type (might be due to invalid IL or missing references)
		string text = "f9047640858943f7a29d10ef6aabee4e";
		string text2 = "117023328e974b0a8a84de561a78ed4f";
		string text3 = "59db3146170443dc9a26720d99dafba4";
		string text4 = "0f98f305134a4f24bcb8cce088498ebf";
		string text5 = "44578c53b5224d58b39150577004c8ff";
		string text6 = "b62c70fb99e14824ba6b414e62b717e5";
		string text7 = "d7fc3f614e2f4ce7a1972928db004124";
		string text8 = "e6b8f43f8fce432991246c6a1071b57a";
		string text9 = "3e04ae85df2248dfa3f847c6a970edd5";
		string text10 = "6ca96d6a2f9041289b432b350e901496";
		string text11 = "85b74b2d3f784c06a0c31b4f06e486a6";
		string text12 = "d477dcf13536498b9a9ff9f90c7f858e";
		IntConstant val = new IntConstant();
		val.Value = 1;
		((Element)val).name = "constant1" + PageName;
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "d7169995e449fdc4db861ddf0b9beff8", negate: true, null, true).EtudeStatus(null, null, "9b81cc87781828444bfd451ee2c556f0", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text3).AddOrAndLogic(conditions, negate: true)
			.EtudeStatus(null, null, "RanRomAranHulrun", negate: true, null, true);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text3).EtudeStatus(null, null, "RanRomAranHulrun", negate: false, null, true);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text3).EtudeStatus(null, null, "RanRomAranHulrun", negate: true, null, true)
			.AddOrAndLogic(conditions);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected(text8);
		BookPageConfigurator.New(PageName, text).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text4)
			.AddToAnswers(text3)
			.AddToCues(text5)
			.AddToCues(text6)
			.AddToCues(text7)
			.AddToCues(text9)
			.AddToAnswers(text8)
			.AddToAnswers(text10)
			.AddToAnswers(text11)
			.AddToAnswers(text12)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val2 = new CueSelection();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val2.Cues.Add(val3);
		val2.Strategy = (Strategy)0;
		CueSelection val4 = new CueSelection();
		BlueprintCueBaseReference val5 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook02End")).deserializedGuid;
		val4.Cues.Add(val5);
		val4.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook02Page004Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowOnce().SetText("RanRomAranBook02Page004Ans0002.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetConditions(conditions2).SetText("RanRomAranBook02Page004Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text5).SetConditions(conditions3).SetText("RanRomAranBook02Page004Cue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text6).SetConditions(conditions4).SetText("RanRomAranBook02Page004Cue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text7).SetConditions(conditions5).SetText("RanRomAranBook02Page004Cue0005.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0006Name, text8).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook02Page004Ans0006.Text")
			.SetNextCue(val2)
			.Configure();
		CueConfigurator.New(Cue0006Name, text9).SetConditions(conditions6).SetText("RanRomAranBook02Page004Cue0006.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text10).SetShowOnce().SetText("RanRomAranBook02Page004Ans0007.Text")
			.SetNextCue(val4)
			.Configure();
		AnswerConfigurator.New(Ans0008Name, text11).SetShowOnce().SetText("RanRomAranBook02Page004Ans0008.Text")
			.SetNextCue(val4)
			.SetOnSelect(ActionsBuilder.New().IncrementFlagValue("RanRomAranConf", true, (IntEvaluator?)(object)val))
			.Configure();
		AnswerConfigurator.New(Ans0009Name, text12).SetShowOnce().SetText("RanRomAranBook02Page004Ans0009.Text")
			.SetNextCue(val4)
			.SetOnSelect(ActionsBuilder.New().CompleteEtude("RanRomAranActive"))
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
