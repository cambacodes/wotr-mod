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

public class AranBook01Page003
{
	private static readonly string PageName = "RanRomAranBook01Page003";

	private static readonly string Cue0001Name = "RanRomAranBook01Page003Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook01Page003Cue0002";

	private static readonly string Cue0003Name = "RanRomAranBook01Page003Cue0003";

	private static readonly string Cue0004Name = "RanRomAranBook01Page003Cue0004";

	private static readonly string Cue0005Name = "RanRomAranBook01Page003Cue0005";

	private static readonly string Cue0006Name = "RanRomAranBook01Page003Cue0006";

	private static readonly string Ans0008Name = "RanRomAranBook01Page003Ans0008";

	public static string Configure()
	{
		//IL_0035: Unknown result type (might be due to invalid IL or missing references)
		//IL_003c: Expected O, but got Unknown
		//IL_0290: Unknown result type (might be due to invalid IL or missing references)
		//IL_0297: Expected O, but got Unknown
		//IL_0297: Unknown result type (might be due to invalid IL or missing references)
		//IL_029e: Expected O, but got Unknown
		//IL_02aa: Unknown result type (might be due to invalid IL or missing references)
		//IL_02af: Unknown result type (might be due to invalid IL or missing references)
		//IL_02c6: Unknown result type (might be due to invalid IL or missing references)
		string text = "92ae6be1fb5941798dcb293ae88f9eff";
		string text2 = "c44b19b158594cd1b748ae6b38591172";
		string text3 = "7d4cb79fe11d4f198105efb47cc86146";
		string text4 = "6d69b0a8cff04fd3b36282be1bb7c257";
		string text5 = "a5d510cfa7bc4f9985db3dc9d6d8d332";
		string text6 = "66440ec2156b4bed9f822584e3fc3d6b";
		string text7 = "0e7fed613c974e8aa201b413105bc895";
		string text8 = "39c6df2c2db240db9aa8e4023ce097f7";
		IntConstant val = new IntConstant();
		val.Value = 1;
		((Element)val).name = "constant1" + PageName;
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(true, null, "517374d9a40b95548a2c6ce187da3f43").EtudeStatus(null, null, "d7169995e449fdc4db861ddf0b9beff8", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected("1ecd71b3d5bc445d8988c6bbf0c50c75");
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected("1ecd71b3d5bc445d8988c6bbf0c50c75").AddOrAndLogic(conditions);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected("1ecd71b3d5bc445d8988c6bbf0c50c75").AddOrAndLogic(conditions, negate: true);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected("6a2975cc8c1a4ec5a3750502796528bb");
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected("553f62a71a0d4164b8dc46a8896526b7");
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected("ad925f915f7042769fe26164bb8fd499");
		BookPageConfigurator.New(PageName, text).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text5)
			.AddToCues(text6)
			.AddToCues(text7)
			.AddToAnswers(text8)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val2 = new CueSelection();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook01Page004")).deserializedGuid;
		val2.Cues.Add(val3);
		val2.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions2).SetText("RanRomAranBook01Page003Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions3).SetText("RanRomAranBook01Page003Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions4).SetText("RanRomAranBook01Page003Cue0003.Text")
			.SetShowOnce()
			.SetOnShow(ActionsBuilder.New().StartEtude("RanRomAranHulrun").IncrementFlagValue("RanRomAranConf", true, (IntEvaluator?)(object)val))
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions5).SetText("RanRomAranBook01Page003Cue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text6).SetConditions(conditions6).SetText("RanRomAranBook01Page003Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text7).SetConditions(conditions7).SetText("RanRomAranBook01Page003Cue0006.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0008Name, text8).SetShowOnce().SetText("RanRomAranBook01Page003Ans0008.Text")
			.SetNextCue(val2)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
