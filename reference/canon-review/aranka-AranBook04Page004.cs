using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;

namespace RanRomance.Aran;

public class AranBook04Page004
{
	private static readonly string PageName = "RanRomAranBook04Page004";

	private static readonly string Cue0001Name = "RanRomAranBook04Page004Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook04Page004Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook04Page004Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook04Page004Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook04Page004Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook04Page004Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook04Page004Ans0005";

	private static readonly string Cue0005Name = "RanRomAranBook04Page004Cue0005";

	private static readonly string Cue0006Name = "RanRomAranBook04Page004Cue0006";

	private static readonly string Cue0007Name = "RanRomAranBook04Page004Cue0007";

	private static readonly string Cue0008Name = "RanRomAranBook04Page004Cue0008";

	private static readonly string Ans0009Name = "RanRomAranBook04Page004Ans0009";

	private static readonly string Ans0000Name = "RanRomAranBook04Page004Ans0000";

	private static readonly string Ans0011Name = "RanRomAranBook04Page004Ans0011";

	public static string Configure()
	{
		//IL_0480: Unknown result type (might be due to invalid IL or missing references)
		//IL_0487: Expected O, but got Unknown
		//IL_0487: Unknown result type (might be due to invalid IL or missing references)
		//IL_048e: Expected O, but got Unknown
		//IL_049a: Unknown result type (might be due to invalid IL or missing references)
		//IL_049f: Unknown result type (might be due to invalid IL or missing references)
		//IL_04b6: Unknown result type (might be due to invalid IL or missing references)
		//IL_04bb: Unknown result type (might be due to invalid IL or missing references)
		//IL_04c2: Expected O, but got Unknown
		//IL_04c2: Unknown result type (might be due to invalid IL or missing references)
		//IL_04c9: Expected O, but got Unknown
		//IL_04d5: Unknown result type (might be due to invalid IL or missing references)
		//IL_04da: Unknown result type (might be due to invalid IL or missing references)
		//IL_04f1: Unknown result type (might be due to invalid IL or missing references)
		//IL_04f6: Unknown result type (might be due to invalid IL or missing references)
		//IL_04fd: Expected O, but got Unknown
		//IL_04fd: Unknown result type (might be due to invalid IL or missing references)
		//IL_0504: Expected O, but got Unknown
		//IL_0510: Unknown result type (might be due to invalid IL or missing references)
		//IL_0515: Unknown result type (might be due to invalid IL or missing references)
		//IL_052c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0531: Unknown result type (might be due to invalid IL or missing references)
		//IL_0538: Expected O, but got Unknown
		//IL_0538: Unknown result type (might be due to invalid IL or missing references)
		//IL_053f: Expected O, but got Unknown
		//IL_054b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0550: Unknown result type (might be due to invalid IL or missing references)
		//IL_0567: Unknown result type (might be due to invalid IL or missing references)
		string text = "62984a44f37743419b03c05d32de27d5";
		string text2 = "5ba39debf1f44b08bc6a9c773e576a9a";
		string text3 = "2b96ca2849af49ed9cd2ca65a642dfd7";
		string text4 = "f795d0badffc4e2bb7df291afcfa635b";
		string text5 = "355ba4462aef44afbb6f6a4159b93be6";
		string text6 = "0acf923610054a4788796f6ee08dda4a";
		string text7 = "f95ad7d1afbb408185a62ba91fc6c626";
		string text8 = "1ae155789aa34fe1a6a70e7aa4811cf0";
		string text9 = "0b82312600834f3a9942398af201103d";
		string text10 = "ec9a4b20e2554ab4a97f57a55ed5531d";
		string text11 = "516a4bf58a3b48c19c61be6b420b786a";
		string text12 = "74fbdb2b084e47fa9bfdabcdad944150";
		string text13 = "e81482cad5a7414e908c7b66120c88b0";
		string text14 = "5deec1f762da4b6695de2171b82c4ff1";
		string text15 = "30c1f33f0bd14a6eb5a14a8dc3999844";
		ConditionsBuilder conditions = ConditionsBuilder.New().CueSeen("d7061b61765b4d75a42a0117b3f4fa63", null, negate: true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text4);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text4);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text6).EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().AnswerSelected(text4);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text6).EtudeStatus(null, null, "RanRomAranRomance", negate: true, null, true);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text8);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected(text8).QuestStatus(negate: false, "5ba83bd1a6b1c884794fbb4858480e7f", (QuestState)2)
			.AddOrAndLogic(((BlueprintCueBase)BlueprintTool.Get<BlueprintBookPage>("9f67adedf4dacca439264db537a4b9f3")).Conditions);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected(text8).QuestStatus(negate: false, "df19bef39c8aa6a4b9dcaf40450b94dc", (QuestState)2)
			.AddOrAndLogic(((BlueprintCueBase)BlueprintTool.Get<BlueprintBookPage>("223fd069ee25c784db2df011adbf10f8")).Conditions);
		ConditionsBuilder showConditions3 = ConditionsBuilder.New().CueSeen("0f077ad32cf24ba4bb72e7149a352e57");
		ConditionsBuilder showConditions4 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true);
		ConditionsBuilder showConditions5 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: true, null, true).CueSeen("0f077ad32cf24ba4bb72e7149a352e57", null, negate: true);
		BookPageConfigurator.New(PageName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text5)
			.AddToAnswers(text4)
			.AddToCues(text7)
			.AddToAnswers(text6)
			.AddToCues(text9)
			.AddToAnswers(text8)
			.AddToCues(text10)
			.AddToCues(text11)
			.AddToCues(text12)
			.AddToAnswers(text13)
			.AddToAnswers(text14)
			.AddToAnswers(text15)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Page005")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueSelection val5 = new CueSelection();
		BlueprintCueBaseReference val6 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val6).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Page006")).deserializedGuid;
		val5.Cues.Add(val6);
		val5.Strategy = (Strategy)0;
		CueSelection val7 = new CueSelection();
		BlueprintCueBaseReference val8 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val8).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Page008")).deserializedGuid;
		val7.Cues.Add(val8);
		val7.Strategy = (Strategy)0;
		ConditionsBuilder conditions8 = ConditionsBuilder.New().QuestStatus(negate: false, "7c34b1c9108eddb43935d13cb4c65ca0", (QuestState)2);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().QuestStatus(negate: false, "72b1ede33bb8cf24bb0f24e526e9f887", (QuestState)2);
		ActionsBuilder onShow = ActionsBuilder.New().Conditional(conditions8, ActionsBuilder.New().StartEtude("6eddba9546e84c2fb0bb50af027b7d25").StartEtude("9ce50eac84ade7042872352b5d2622e7")).Conditional(conditions9, ActionsBuilder.New().StartEtude("4484a3460335465a992359fac23a2ca5").UnlockFlag("c885b1c80275e8c4e96e4dfc9908808b"));
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomAranBook04Page004Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetText("RanRomAranBook04Page004Cue0002.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text4).SetShowOnce().SetText("RanRomAranBook04Page004Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text5).SetConditions(conditions2).SetText("RanRomAranBook04Page004Cue0003.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text6).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook04Page004Ans0004.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0004Name, text7).SetConditions(conditions3).SetText("RanRomAranBook04Page004Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text8).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranBook04Page004Ans0005.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0005Name, text9).SetConditions(conditions4).SetText("RanRomAranBook04Page004Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text10).SetConditions(conditions5).SetText("RanRomAranBook04Page004Cue0006.Text")
			.SetOnShow(onShow)
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0007Name, text11).SetConditions(conditions6).SetText("RanRomAranBook04Page004Cue0007.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0008Name, text12).SetConditions(conditions7).SetText("RanRomAranBook04Page004Cue0008.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0009Name, text13).SetShowConditions(showConditions3).SetShowOnce()
			.SetText("RanRomAranBook04Page004Ans0009.Text")
			.SetNextCue(val3)
			.Configure();
		AnswerConfigurator.New(Ans0000Name, text14).SetShowConditions(showConditions4).SetShowOnce()
			.SetText("RanRomAranBook04Page004Ans0000.Text")
			.SetNextCue(val5)
			.Configure();
		AnswerConfigurator.New(Ans0011Name, text15).SetShowConditions(showConditions5).SetShowOnce()
			.SetText("RanRomAranBook04Page004Ans0011.Text")
			.SetNextCue(val7)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
