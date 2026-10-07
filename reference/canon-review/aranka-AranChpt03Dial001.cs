using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranChpt03Dial001
{
	private static readonly string Ans0001Name = "RanRomAranChpt03Dial001Ans0001";

	private static readonly string Cue0001Name = "RanRomAranChpt03Dial001Cue0001";

	private static readonly string Cue0002Name = "RanRomAranChpt03Dial001Cue0002";

	public static string Configure()
	{
		//IL_007e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0085: Expected O, but got Unknown
		//IL_013d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0144: Expected O, but got Unknown
		//IL_0144: Unknown result type (might be due to invalid IL or missing references)
		//IL_014b: Expected O, but got Unknown
		//IL_014b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0152: Expected O, but got Unknown
		//IL_015a: Unknown result type (might be due to invalid IL or missing references)
		//IL_015f: Unknown result type (might be due to invalid IL or missing references)
		//IL_016c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0171: Unknown result type (might be due to invalid IL or missing references)
		//IL_0197: Unknown result type (might be due to invalid IL or missing references)
		string text = "695280010266469e98863d561fb82735";
		string text2 = "f8310f5f0c3f4900942c411a39517b97";
		string text3 = "b49da9ecaa1a4b81bca519219909b04a";
		ConditionsBuilder showConditions = ConditionsBuilder.New().EtudeStatus(null, null, "15e0048c7daf0ac4999c2313b58df0e3", negate: false, null, true).DialogSeen("2936ff4e6e234702b7f59b469b57feaa");
		ConditionsBuilder conditions = ConditionsBuilder.New().DialogSeen("b9068ea8642f4c9da4a338ebd5ba316f");
		DialogSpeaker val = new DialogSpeaker();
		val.NoSpeaker = false;
		val.MoveCamera = true;
		val.NotRevealInFoW = false;
		val.SwitchDual = false;
		val.m_Blueprint = BlueprintTool.GetRef<BlueprintUnitReference>("430cba7801b149b4e8494ace6baf4f7c");
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomAranChpt03Dial001Cue0001.Text")
			.SetAnswers("5ff8a80442182f84e849b4281f98b9ca")
			.SetSpeaker(val)
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetText("RanRomAranChpt03Dial001Cue0002.Text").SetAnswers("5ff8a80442182f84e849b4281f98b9ca")
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
		AnswerConfigurator.New(Ans0001Name, text).SetShowConditions(showConditions).SetText("RanRomAranChpt03Dial001Ans0001.Text")
			.SetNextCue(val2)
			.Configure();
		AnswersListConfigurator.For("5ff8a80442182f84e849b4281f98b9ca").ClearAnswers().AddToAnswers("63291087be463364e81855f7c859d4d1")
			.AddToAnswers("92de3c8fc255626468a19fd66e9023cc")
			.AddToAnswers("088ca889bae618748b99e9059b58e7b3")
			.AddToAnswers("45f1dc5ac5e111f48b2ddc791458263b")
			.AddToAnswers("89b49087d12eaf6428c75a474563825f")
			.AddToAnswers("a27e7e0e76e7d104e8c70549ba2ec40a")
			.AddToAnswers(text)
			.AddToAnswers("b597f6ec88270cc408469bfa6e38817d")
			.AddToAnswers("2cbcf70d569d0e645bd7b0972fbc3abd")
			.Configure();
		return null;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
