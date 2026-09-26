using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.BasicEx;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.DialogSystem;
using Kingmaker.ElementsSystem;

namespace RanRomance.Tere;

public class TereBook00End
{
	private static readonly string PageName = "RanRomTereBook00End";

	private static readonly string Cue0001Name = "RanRomTereBook00EndCue0001";

	private static readonly string Cue0002Name = "RanRomTereBook00EndCue0002";

	private static readonly string Cue0003Name = "RanRomTereBook00EndCue0003";

	private static readonly string Cue0004Name = "RanRomTereBook00EndCue0004";

	private static readonly string Ans1001Name = "RanRomStorChpt02Dial001Ans1001";

	private static readonly string Cue1001Name = "RanRomStorChpt02Dial001Cue1001";

	public static string Configure()
	{
		//IL_013e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0145: Expected O, but got Unknown
		//IL_0182: Unknown result type (might be due to invalid IL or missing references)
		//IL_0189: Expected O, but got Unknown
		//IL_03ca: Unknown result type (might be due to invalid IL or missing references)
		//IL_03d1: Expected O, but got Unknown
		//IL_03d1: Unknown result type (might be due to invalid IL or missing references)
		//IL_03d8: Expected O, but got Unknown
		//IL_03e4: Unknown result type (might be due to invalid IL or missing references)
		//IL_03e9: Unknown result type (might be due to invalid IL or missing references)
		//IL_0400: Unknown result type (might be due to invalid IL or missing references)
		//IL_04c5: Unknown result type (might be due to invalid IL or missing references)
		//IL_04cc: Expected O, but got Unknown
		//IL_0534: Unknown result type (might be due to invalid IL or missing references)
		//IL_053b: Expected O, but got Unknown
		//IL_053b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0542: Expected O, but got Unknown
		//IL_054b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0550: Unknown result type (might be due to invalid IL or missing references)
		//IL_0567: Unknown result type (might be due to invalid IL or missing references)
		string text = "5ac36acbc88d424da8d47dffc9b35aa7";
		string text2 = "b94ae2b7f89e4330b0e4a371bceb4f16";
		string text3 = "f81c816a1236438ca91c0a6c22be5309";
		string text4 = "069c46765598432990a14ff4e8927fde";
		string text5 = "56d2fd8538614c6687fb41334e878d6e";
		string guid = "46547a2db24948cbb75843637478be47";
		string text6 = "a14e718c6a6a42678ae0cadcd5692d34";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "df17ab913c348644b9bd3fe3f9781a84", negate: false, null, true).EtudeStatus(null, null, "0e20d73ea0da6a94d94a6b42035a1ce0", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "15e0048c7daf0ac4999c2313b58df0e3", negate: false, null, true).EtudeStatus(null, null, "0e20d73ea0da6a94d94a6b42035a1ce0", negate: false, null, true)
			.UseOr();
		AddItemToPlayer val = new AddItemToPlayer();
		val.Equip = false;
		val.Identify = true;
		val.m_ItemToGive = BlueprintTool.GetRef<BlueprintItemReference>("5230fdfb34834955a25fc04c5aa290fe");
		((Element)val).name = "RanRomScaleAdd";
		val.Quantity = 1;
		val.Silent = false;
		RemoveItemFromPlayer val2 = new RemoveItemFromPlayer();
		val2.Money = false;
		val2.m_ItemToRemove = BlueprintTool.GetRef<BlueprintItemReference>("816f244523b5455a85ae06db452d4330");
		val2.m_Silent = false;
		((Element)val2).name = "RanRomScaleRem";
		val2.Quantity = 1;
		ActionsBuilder onShow = ActionsBuilder.New().Add((GameAction)(object)val).Add((GameAction)(object)val2)
			.Conditional(ConditionsBuilder.New().EtudeStatus(null, null, "df17ab913c348644b9bd3fe3f9781a84", negate: true, null, true), ActionsBuilder.New().GiveObjective("RanRomTereQuestEntry0001"));
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected("395b40ff6bbc4e8085765a34239930f1");
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected("395b40ff6bbc4e8085765a34239930f1").AddOrAndLogic(conditions);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected("395b40ff6bbc4e8085765a34239930f1").AddOrAndLogic(conditions, negate: true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected("57525789d25748d4b4ed3176ffb199af");
		ConditionsBuilder showConditions = ConditionsBuilder.New().AddOrAndLogic(conditions2).ItemsEnough(null, null, null, false, "816f244523b5455a85ae06db452d4330", null, negate: false, 1)
			.AnswerSelected("57525789d25748d4b4ed3176ffb199af");
		BookPageConfigurator.New(PageName, text).SetImageLink("482f509e50aa6484bafee746ddb3849f").SetForeImageLink("5b9b0b8b6f37380409ec0ca2a9142d39")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text5)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions3).SetText("RanRomTereBook00EndCue0001.Text")
			.SetShowOnce()
			.SetOnShow(onShow)
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions4).SetText("RanRomTereBook00EndCue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions5).SetText("RanRomTereBook00EndCue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions6).SetText("RanRomTereBook00EndCue0004.Text")
			.SetShowOnce()
			.Configure();
		DialogSpeaker val5 = new DialogSpeaker();
		val5.NoSpeaker = false;
		val5.MoveCamera = true;
		val5.NotRevealInFoW = false;
		val5.SwitchDual = false;
		CueConfigurator.New(Cue1001Name, text6).SetText("RanRomStorChpt02Dial001Cue1001.Text").SetSpeaker(val5)
			.SetAnswers("2f5b7e0b76d3c5a42a431e1e33a8db09")
			.SetOnShow(onShow)
			.Configure();
		CueSelection val6 = new CueSelection();
		BlueprintCueBaseReference val7 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val7).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text6)).deserializedGuid;
		val6.Cues.Add(val7);
		val6.Strategy = (Strategy)0;
		AnswerConfigurator.New(Ans1001Name, guid).SetText("RanRomStorChpt02Dial001Ans1001.Text").SetShowConditions(showConditions)
			.SetNextCue(val6)
			.SetShowOnce()
			.Configure();
		return text;
	}
}
