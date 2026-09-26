using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranChpt01Dial001
{
	private static readonly string Ans0001Name = "RanRomAranChpt01Dial001Ans0001";

	private static readonly string Cue0001Name = "RanRomAranChpt01Dial001Cue0001";

	private static readonly string Ans0002Name = "RanRomAranChpt01Dial001Ans0002";

	private static readonly string Cue0002Name = "RanRomAranChpt01Dial001Cue0002";

	public static string Configure()
	{
		//IL_00c2: Unknown result type (might be due to invalid IL or missing references)
		//IL_00c9: Expected O, but got Unknown
		//IL_017d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0184: Expected O, but got Unknown
		//IL_0184: Unknown result type (might be due to invalid IL or missing references)
		//IL_018b: Expected O, but got Unknown
		//IL_0193: Unknown result type (might be due to invalid IL or missing references)
		//IL_0198: Unknown result type (might be due to invalid IL or missing references)
		//IL_01af: Unknown result type (might be due to invalid IL or missing references)
		//IL_01b4: Unknown result type (might be due to invalid IL or missing references)
		//IL_01bb: Expected O, but got Unknown
		//IL_01bb: Unknown result type (might be due to invalid IL or missing references)
		//IL_01c2: Expected O, but got Unknown
		//IL_01ca: Unknown result type (might be due to invalid IL or missing references)
		//IL_01cf: Unknown result type (might be due to invalid IL or missing references)
		//IL_01e6: Unknown result type (might be due to invalid IL or missing references)
		string text = "1a0a7b9d145c4275ba142148199b9f38";
		string text2 = "fcd3f51c7ac049898c8b5d5cf07c47e7";
		string text3 = "ec371a20edb84fa196844763ca6fc6d5";
		string text4 = "72fba9b7d7c4442389c1803cffcedc3a";
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected("44db38d17b9d41b396ab1c801929b2d9").AnswerSelected("953139a78ae142869340f88deb52d362")
			.AnswerSelected("c0e901a0ee9449b2a183f33977e8dd5d")
			.UseOr();
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected("da10a8e01f6c47508c69f65d26567551");
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().AddOrAndLogic(conditions).CueSeen("cc20dfe8789e457b8dcbb8a0818120da", null, negate: true)
			.UseOr();
		DialogSpeaker val = new DialogSpeaker();
		val.NoSpeaker = false;
		val.MoveCamera = true;
		val.NotRevealInFoW = false;
		val.SwitchDual = false;
		val.m_Blueprint = null;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranChpt01Dial001Cue0001.Text").SetShowOnce()
			.SetAnswers("2373bef62ea65d741a8f54ba95f9a8b2")
			.SetSpeaker(val)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetText("RanRomAranChpt01Dial001Cue0002.Text").SetShowOnce()
			.SetAnswers("2373bef62ea65d741a8f54ba95f9a8b2")
			.SetSpeaker(val)
			.Configure();
		CueSelection val2 = new CueSelection();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text2)).deserializedGuid;
		val2.Cues.Add(val3);
		val2.Strategy = (Strategy)0;
		CueSelection val4 = new CueSelection();
		BlueprintCueBaseReference val5 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val5).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text4)).deserializedGuid;
		val4.Cues.Add(val5);
		val4.Strategy = (Strategy)0;
		AnswerConfigurator.New(Ans0001Name, text).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranChpt01Dial001Ans0001.Text")
			.SetOnSelect(ActionsBuilder.New().StartEtude("RanRomAranFlirt"))
			.SetNextCue(val2)
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranChpt01Dial001Ans0002.Text")
			.SetOnSelect(ActionsBuilder.New().StartEtude("RanRomAranFlirt"))
			.SetNextCue(val4)
			.Configure();
		AnswersListConfigurator.For("2373bef62ea65d741a8f54ba95f9a8b2").ClearAnswers().AddToAnswers("3c03b4ab371f45dd8e7a5044e1044962")
			.AddToAnswers("1894d651517a553468d2da0195c9122e")
			.AddToAnswers("1cfee0985e8030c428f2550fce31d14d")
			.AddToAnswers("57d610ec2148cbe4e9ea39c2f65316c9")
			.AddToAnswers("18a663e9622ad4641a3d2909289d1982")
			.AddToAnswers(text)
			.AddToAnswers(text3)
			.AddToAnswers("5f39a71d874ae9440b66314ca16ae8f9")
			.AddToAnswers("8909320b7c073a0468620d06679b5618")
			.AddToAnswers("1073edc1be8d476bade6bfcff9b287e2")
			.AddToAnswers("8616600df197b19448770768f0e411ae")
			.AddToAnswers("293ff8dd6d025534bbf9b9453d6ec2c0")
			.Configure();
		return null;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
