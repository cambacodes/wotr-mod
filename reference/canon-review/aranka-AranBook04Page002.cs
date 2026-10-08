using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook04Page002
{
	private static readonly string PageName = "RanRomAranBook04Page002";

	private static readonly string Cue0001Name = "RanRomAranBook04Page002Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook04Page002Ans0002";

	private static readonly string Cue0002Name = "RanRomAranBook04Page002Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook04Page002Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook04Page002Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook04Page002Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook04Page002Cue0004";

	private static readonly string Ans0005Name = "RanRomAranBook04Page002Ans0005";

	private static readonly string Cue0005Name = "RanRomAranBook04Page002Cue0005";

	private static readonly string Ans0006Name = "RanRomAranBook04Page002Ans0006";

	private static readonly string Ans0007Name = "RanRomAranBook04Page002Ans0007";

	public static string Configure()
	{
		//IL_024e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0255: Expected O, but got Unknown
		//IL_0255: Unknown result type (might be due to invalid IL or missing references)
		//IL_025c: Expected O, but got Unknown
		//IL_0268: Unknown result type (might be due to invalid IL or missing references)
		//IL_026d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0284: Unknown result type (might be due to invalid IL or missing references)
		//IL_0289: Unknown result type (might be due to invalid IL or missing references)
		//IL_0290: Expected O, but got Unknown
		//IL_0290: Unknown result type (might be due to invalid IL or missing references)
		//IL_0297: Expected O, but got Unknown
		//IL_02a3: Unknown result type (might be due to invalid IL or missing references)
		//IL_02a8: Unknown result type (might be due to invalid IL or missing references)
		//IL_02bf: Unknown result type (might be due to invalid IL or missing references)
		//IL_02c4: Unknown result type (might be due to invalid IL or missing references)
		//IL_02cb: Expected O, but got Unknown
		//IL_02cb: Unknown result type (might be due to invalid IL or missing references)
		//IL_02d2: Expected O, but got Unknown
		//IL_02de: Unknown result type (might be due to invalid IL or missing references)
		//IL_02e3: Unknown result type (might be due to invalid IL or missing references)
		//IL_02fa: Unknown result type (might be due to invalid IL or missing references)
		string text = "e983bfab659648f4aba26a301dab9609";
		string text2 = "46285131901a487b981f8cb39228b7bc";
		string text3 = "126df048c7d3497888b3135fd16c5ba4";
		string text4 = "c97ad388ea974973a24d2d80c2e47884";
		string text5 = "fbd05f252edb4b04a6e36150ad2da9e5";
		string text6 = "ca386aef7ece4cb68e50e718ba706414";
		string text7 = "539ebebd2aa84fa695892192fa73b900";
		string text8 = "1ee1172a3ce24a03b9040c1257fe73f9";
		string text9 = "33382e3971b9407f96110224675f01bc";
		string text10 = "527498d896e34fc1a38d6dfb08158595";
		string text11 = "ae140efb49134de2a5fa0e3804a0b25e";
		string text12 = "02b32177fde24e958afe07d2eb9a12c2";
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder showConditions = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().AnswerSelected(text7);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text9);
		ConditionsBuilder showConditions3 = ConditionsBuilder.New().AnswerSelected(text9);
		BookPageConfigurator.New(PageName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text4)
			.AddToAnswers(text3)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToCues(text10)
			.AddToAnswers(text9)
			.AddToAnswers(text11)
			.AddToAnswers(text12)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Page003")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueSelection val5 = new CueSelection();
		BlueprintCueBaseReference val6 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val6).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook04Page004")).deserializedGuid;
		val5.Cues.Add(val6);
		val5.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook04Page002Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowOnce().SetText("RanRomAranBook04Page002Ans0002.Text")
			.SetNextCue(val)
			.SetOnSelect(ActionsBuilder.New().StartEtude("RanRomAranAlurFlirt"))
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetConditions(conditions).SetText("RanRomAranBook04Page002Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text5).SetShowOnce().SetText("RanRomAranBook04Page002Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text6).SetConditions(conditions2).SetText("RanRomAranBook04Page002Cue0003.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text7).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomAranBook04Page002Ans0004.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0004Name, text8).SetConditions(conditions3).SetText("RanRomAranBook04Page002Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text9).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomAranBook04Page002Ans0005.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0005Name, text10).SetConditions(conditions4).SetText("RanRomAranBook04Page002Cue0005.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0006Name, text11).SetShowConditions(showConditions3).SetShowOnce()
			.SetText("RanRomAranBook04Page002Ans0006.Text")
			.SetNextCue(val3)
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text12).SetShowOnce().SetText("RanRomAranBook04Page002Ans0007.Text")
			.SetNextCue(val5)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
