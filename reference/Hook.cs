using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Tere;

public class TereChpt05Dial001
{
	private static readonly string Ans0001Name = "RanRomTereChpt05Dial001Ans0001";

	private static readonly string Cue0001Name = "RanRomTereChpt05Dial001Cue0001";

	private static readonly string Cue0002Name = "RanRomTereChpt05Dial001Cue0002";

	public static string Configure()
	{
		//IL_0099: Unknown result type (might be due to invalid IL or missing references)
		//IL_00a0: Expected O, but got Unknown
		//IL_016b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0172: Expected O, but got Unknown
		//IL_0172: Unknown result type (might be due to invalid IL or missing references)
		//IL_0179: Expected O, but got Unknown
		//IL_0179: Unknown result type (might be due to invalid IL or missing references)
		//IL_0180: Expected O, but got Unknown
		//IL_0188: Unknown result type (might be due to invalid IL or missing references)
		//IL_018d: Unknown result type (might be due to invalid IL or missing references)
		//IL_019a: Unknown result type (might be due to invalid IL or missing references)
		//IL_019f: Unknown result type (might be due to invalid IL or missing references)
		//IL_01c5: Unknown result type (might be due to invalid IL or missing references)
		string text = "694c7f047f424e2e9346cdd5dbd99397";
		string text2 = "7b135f8c0e5e43b58e301b484b5bb817";
		string text3 = "de5e1140b3584194a8476d9a0212fcdd";
		ConditionsBuilder showConditions = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomTereRom", negate: false, null, true);
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected("9b75d66ff0604023956ca414ce2d1742");
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected("9b75d66ff0604023956ca414ce2d1742", null, negate: true);
		DialogSpeaker val = new DialogSpeaker();
		val.NoSpeaker = false;
		val.MoveCamera = true;
		val.NotRevealInFoW = false;
		val.SwitchDual = false;
		val.m_Blueprint = BlueprintTool.GetRef<BlueprintUnitReference>("9e8401e7703907e4d94189d5992dd13e");
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomTereChpt05Dial001Cue0001.Text")
			.SetShowOnce()
			.SetAnswers("f72c50ed389b7a949a5b44b88ec534a0")
			.SetSpeaker(val)
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomTereChpt05Dial001Cue0002.Text")
			.SetShowOnce()
			.SetAnswers("f72c50ed389b7a949a5b44b88ec534a0")
			.SetSpeaker(val)
			.Configure();
		CueSelection val2 = new CueSelection();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text2)).deserializedGuid;
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text3)).deserializedGuid;
		val2.Cues.Add(val3);
		val2.Cues.Add(val4);
		val2.Strategy = (Strategy)0;
		AnswerConfigurator.New(Ans0001Name, text).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomTereChpt05Dial001Ans0001.Text")
			.SetNextCue(val2)
			.Configure();
		AnswersListConfigurator.For("f72c50ed389b7a949a5b44b88ec534a0").ClearAnswers().AddToAnswers(text)
			.AddToAnswers("f0339bf6c8727794aba033e92cf96a78")
			.AddToAnswers("e1459098ee5318c4b8899ec181e8e525")
			.Configure();
		return "";
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
