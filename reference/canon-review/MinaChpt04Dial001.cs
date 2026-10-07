using BlueprintCore.Actions.Builder;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.AreaLogic.Cutscenes;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;

namespace RanRomance.Mina;

public class MinaChpt04Dial001
{
	private static readonly string PageName = "RanRomMinaChpt04Dial001";

	private static readonly string Ans0001Name = "RanRomMinaChpt04Dial001Ans0001";

	private static readonly string Cue0001Name = "RanRomMinaChpt04Dial001Cue0001";

	private static readonly string Ans0002Name = "RanRomMinaChpt04Dial001Ans0002";

	private static readonly string Cue0002Name = "RanRomMinaChpt04Dial001Cue0002";

	private static readonly string Ans0003Name = "RanRomMinaChpt04Dial001Ans0003";

	private static readonly string Cue0003Name = "RanRomMinaChpt04Dial001Cue0003";

	private static readonly string Ans0004Name = "RanRomMinaChpt04Dial001Ans0004";

	private static readonly string Cue0004Name = "RanRomMinaChpt04Dial001Cue0004";

	private static readonly string Cue0005Name = "RanRomMinaChpt04Dial001Cue0005";

	public static string Configure()
	{
		//IL_00d2: Unknown result type (might be due to invalid IL or missing references)
		//IL_00d9: Expected O, but got Unknown
		//IL_00d9: Unknown result type (might be due to invalid IL or missing references)
		//IL_00e0: Expected O, but got Unknown
		//IL_00e8: Unknown result type (might be due to invalid IL or missing references)
		//IL_00ed: Unknown result type (might be due to invalid IL or missing references)
		//IL_0104: Unknown result type (might be due to invalid IL or missing references)
		//IL_0109: Unknown result type (might be due to invalid IL or missing references)
		//IL_0110: Expected O, but got Unknown
		//IL_0110: Unknown result type (might be due to invalid IL or missing references)
		//IL_0117: Expected O, but got Unknown
		//IL_011f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0124: Unknown result type (might be due to invalid IL or missing references)
		//IL_013b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0140: Unknown result type (might be due to invalid IL or missing references)
		//IL_0147: Expected O, but got Unknown
		//IL_0147: Unknown result type (might be due to invalid IL or missing references)
		//IL_014e: Expected O, but got Unknown
		//IL_0157: Unknown result type (might be due to invalid IL or missing references)
		//IL_015c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0173: Unknown result type (might be due to invalid IL or missing references)
		//IL_0178: Unknown result type (might be due to invalid IL or missing references)
		//IL_017f: Expected O, but got Unknown
		//IL_017f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0186: Expected O, but got Unknown
		//IL_018f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0194: Unknown result type (might be due to invalid IL or missing references)
		//IL_01ab: Unknown result type (might be due to invalid IL or missing references)
		//IL_01b0: Unknown result type (might be due to invalid IL or missing references)
		//IL_01b7: Expected O, but got Unknown
		//IL_01b7: Unknown result type (might be due to invalid IL or missing references)
		//IL_01be: Expected O, but got Unknown
		//IL_01ca: Unknown result type (might be due to invalid IL or missing references)
		//IL_01cf: Unknown result type (might be due to invalid IL or missing references)
		//IL_01e6: Unknown result type (might be due to invalid IL or missing references)
		//IL_028e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0295: Expected O, but got Unknown
		string text = "f88af8790c62488eb09b38f0dadc81f4";
		string text2 = "754852ca0aa34053b96f22cda2b0ee1d";
		string text3 = "dbb36812d7d449d8b7976324e670755a";
		string text4 = "0b733773ca97461099f09248bb93473f";
		string text5 = "81ee1f76a3c34affb32ff7b3483d0a65";
		string text6 = "d4e298a7daeb40fe8314e66fd08bc7e3";
		string text7 = "a08540bf69314cffb24d93d277cf6636";
		string text8 = "b4dcf0ee8d844525a8784ed443abef38";
		string text9 = "f85768fdfa6041a2a312fa8a2d62a5e4";
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected("6b41ce47698b26648b067ff94fdbe739");
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().AnswerSelected(text);
		ConditionsBuilder showConditions3 = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder showConditions4 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder conditions = ConditionsBuilder.New().QuestStatus(negate: false, "5a36e3f02f983314fbe9739e7e3301dc", (QuestState)1);
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text2)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text4)).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueSelection val5 = new CueSelection();
		BlueprintCueBaseReference val6 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val6).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text6)).deserializedGuid;
		val5.Cues.Add(val6);
		val5.Strategy = (Strategy)0;
		CueSelection val7 = new CueSelection();
		BlueprintCueBaseReference val8 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val8).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text8)).deserializedGuid;
		val7.Cues.Add(val8);
		val7.Strategy = (Strategy)0;
		CueSelection val9 = new CueSelection();
		BlueprintCueBaseReference val10 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val10).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("99fdf0f3533316745800d960718e3d19")).deserializedGuid;
		val9.Cues.Add(val10);
		val9.Strategy = (Strategy)0;
		ActionsBuilder onShow = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintCue>("55f9d42958f3914439458912baacb2b7").OnShow.Actions[0]);
		ActionsBuilder onStop = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintCue>("55f9d42958f3914439458912baacb2b7").OnStop.Actions[0]);
		ActionsBuilder onShow2 = ActionsBuilder.New().Add(BlueprintTool.Get<CommandAction>("c3ae431439bec4040a03e8383271e017").Action.Actions[0]);
		ActionsBuilder onSelect = ActionsBuilder.New().Add(BlueprintTool.Get<BlueprintAnswer>("9038e82b2c55e124889a1a4458c62ec8").OnSelect.Actions[0]).Add(BlueprintTool.Get<BlueprintAnswer>("9038e82b2c55e124889a1a4458c62ec8").OnSelect.Actions[1]);
		DialogSpeaker val11 = new DialogSpeaker();
		val11.NoSpeaker = false;
		val11.MoveCamera = true;
		val11.NotRevealInFoW = false;
		val11.SwitchDual = false;
		AnswerConfigurator.New(Ans0001Name, text).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomMinaChpt04Dial001Ans0001.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomMinaChpt04Dial001Cue0001.Text").SetShowOnce()
			.AddToAnswers("82a0c2ad3e6dc41469ec66a7affdc486")
			.SetSpeaker(val11)
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomMinaChpt04Dial001Ans0002.Text")
			.SetNextCue(val3)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetText("RanRomMinaChpt04Dial001Cue0002.Text").SetShowOnce()
			.AddToAnswers("82a0c2ad3e6dc41469ec66a7affdc486")
			.SetSpeaker(val11)
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text5).SetShowConditions(showConditions3).SetShowOnce()
			.SetText("RanRomMinaChpt04Dial001Ans0003.Text")
			.SetNextCue(val5)
			.Configure();
		CueConfigurator.New(Cue0003Name, text6).SetText("RanRomMinaChpt04Dial001Cue0003.Text").SetShowOnce()
			.AddToAnswers("82a0c2ad3e6dc41469ec66a7affdc486")
			.SetSpeaker(val11)
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text7).SetShowConditions(showConditions4).SetShowOnce()
			.SetText("RanRomMinaChpt04Dial001Ans0004.Text")
			.SetNextCue(val7)
			.SetOnSelect(onSelect)
			.Configure();
		CueConfigurator.New(Cue0004Name, text8).SetText("RanRomMinaChpt04Dial001Cue0004.Text").SetShowOnce()
			.SetOnShow(onShow)
			.SetOnStop(onStop)
			.SetContinueValue(val9)
			.SetSpeaker(val11)
			.Configure();
		CueConfigurator.New(Cue0005Name, text9).SetConditions(conditions).SetText("RanRomMinaChpt04Dial001Cue0005.Text")
			.SetShowOnce()
			.SetOnShow(onShow2)
			.Configure();
		AnswersListConfigurator.For("82a0c2ad3e6dc41469ec66a7affdc486").ClearAnswers().AddToAnswers("647f782ef1d9fe74190f87eec234f3ac")
			.AddToAnswers("6b41ce47698b26648b067ff94fdbe739")
			.AddToAnswers("3745da96b3c4b3043b797440f50245eb")
			.AddToAnswers("d45b879d4582a7b4781d3a755da1dcab")
			.AddToAnswers("4b7233b13dea1c04cab083ccd2651d1b")
			.AddToAnswers(text)
			.AddToAnswers(text3)
			.AddToAnswers(text5)
			.AddToAnswers(text7)
			.AddToAnswers("66fb898a9011cbd4e9e0a69cc7ab0d9c")
			.AddToAnswers("7f960f8af1860854ca1cf9e37e5831bd")
			.AddToAnswers("309edad62e592444daebe273a12939ec")
			.AddToAnswers("389362a1dab534644915e78504024bbb")
			.Configure();
		ConditionsBuilder showConditions5 = ConditionsBuilder.New().CueSeen(text6, null, negate: true);
		AnswerConfigurator.For("309edad62e592444daebe273a12939ec").SetShowConditions(showConditions5).Configure();
		CueSequenceConfigurator.For("99fdf0f3533316745800d960718e3d19").ClearCues().AddToCues(text9)
			.AddToCues("ee58894d9c344924e8ee2d1eba860c73")
			.Configure();
		return null;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
