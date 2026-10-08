using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook14Page002
{
	private static readonly string PageName = "RanRomAranBook14Page002";

	private static readonly string Cue0001Name = "RanRomAranBook14Page002Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook14Page002Ans0002";

	private static readonly string Cue0002Name = "RanRomAranBook14Page002Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook14Page002Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook14Page002Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook14Page002Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook14Page002Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook14Page002Ans0005";

	private static readonly string Ans0006Name = "RanRomAranBook14Page002Ans0006";

	public static string Configure()
	{
		//IL_022f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0236: Expected O, but got Unknown
		//IL_0236: Unknown result type (might be due to invalid IL or missing references)
		//IL_023d: Expected O, but got Unknown
		//IL_0249: Unknown result type (might be due to invalid IL or missing references)
		//IL_024e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0265: Unknown result type (might be due to invalid IL or missing references)
		//IL_026a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0271: Expected O, but got Unknown
		//IL_0271: Unknown result type (might be due to invalid IL or missing references)
		//IL_0278: Expected O, but got Unknown
		//IL_0284: Unknown result type (might be due to invalid IL or missing references)
		//IL_0289: Unknown result type (might be due to invalid IL or missing references)
		//IL_02a0: Unknown result type (might be due to invalid IL or missing references)
		//IL_02a5: Unknown result type (might be due to invalid IL or missing references)
		//IL_02ac: Expected O, but got Unknown
		//IL_02ac: Unknown result type (might be due to invalid IL or missing references)
		//IL_02b3: Expected O, but got Unknown
		//IL_02bf: Unknown result type (might be due to invalid IL or missing references)
		//IL_02c4: Unknown result type (might be due to invalid IL or missing references)
		//IL_02db: Unknown result type (might be due to invalid IL or missing references)
		string text = "693c5375d15747dc8879434b73041d34";
		string text2 = "de36c4af5ea6418dabca067fbc54852d";
		string text3 = "c6a4d4007ee04466939b9081843a005e";
		string text4 = "69f2ef50d15a465b85664c980b8e2d34";
		string text5 = "1b063e8c3af743faa00e21eb689274b1";
		string text6 = "8540651d0c834c0d9fa0f30fe454cdff";
		string text7 = "b72a826273df4cc9814bb9335fa9c21d";
		string text8 = "860a439bdd1447cd9878fa72426adfea";
		string text9 = "d29c1d065bdb43dda550378c6e8edd76";
		string text10 = "9a573464ef1e475ab1f87ad7e3411ca9";
		ConditionsBuilder conditions = ConditionsBuilder.New().CueSeen("0f077ad32cf24ba4bb72e7149a352e57");
		ConditionsBuilder conditionsBuilder = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().FlagInRange("5db9ec615236f044083a5c6bd3292432", 999, 1).FlagInRange("RanRomCount", 999, 1)
			.UseOr();
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text7);
		BookPageConfigurator.New(PageName, text).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text4)
			.AddToAnswers(text3)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToAnswers(text9)
			.AddToAnswers(text10)
			.SetConditions(conditions)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook14Page003")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueSelection val5 = new CueSelection();
		BlueprintCueBaseReference val6 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val6).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook14End")).deserializedGuid;
		val5.Cues.Add(val6);
		val5.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook14Page002Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowOnce().SetText("RanRomAranBook14Page002Ans0002.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetConditions(conditionsBuilder).SetText("RanRomAranBook14Page002Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text5).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook14Page002Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text6).SetConditions(conditions2).SetText("RanRomAranBook14Page002Cue0003.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text7).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranBook14Page002Ans0004.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0004Name, text8).SetConditions(conditions3).SetText("RanRomAranBook14Page002Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text9).SetShowConditions(conditionsBuilder).SetShowOnce()
			.SetText("RanRomAranBook14Page002Ans0005.Text")
			.SetOnSelect(ActionsBuilder.New().StartEtude("RanRomAranRomance"))
			.SetNextCue(val3)
			.Configure();
		AnswerConfigurator.New(Ans0006Name, text10).SetShowConditions(conditionsBuilder).SetShowOnce()
			.SetText("RanRomAranBook14Page002Ans0006.Text")
			.SetNextCue(val5)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
