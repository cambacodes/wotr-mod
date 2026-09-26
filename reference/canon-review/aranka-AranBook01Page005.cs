using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook01Page005
{
	private static readonly string PageName = "RanRomAranBook01Page005";

	private static readonly string Cue0001Name = "RanRomAranBook01Page005Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook01Page005Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook01Page005Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook01Page005Cue0003";

	public static string Configure()
	{
		//IL_00fe: Unknown result type (might be due to invalid IL or missing references)
		//IL_0105: Expected O, but got Unknown
		//IL_0105: Unknown result type (might be due to invalid IL or missing references)
		//IL_010c: Expected O, but got Unknown
		//IL_010c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0113: Expected O, but got Unknown
		//IL_011f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0124: Unknown result type (might be due to invalid IL or missing references)
		//IL_0135: Unknown result type (might be due to invalid IL or missing references)
		//IL_013a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0160: Unknown result type (might be due to invalid IL or missing references)
		string text = "68c82816255748508b58db82225ae95b";
		string text2 = "dedfa46d23f143ee9e87ffb399cbf72e";
		string text3 = "ea5cad22bee74ac5b0e107fcdd942452";
		string text4 = "e72b2c8c783c4a3087d07714e3c1aba6";
		string text5 = "b7192eb176dd4bd183cf79fb7e368ce2";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranFlirt", negate: false, null, true);
		BookPageConfigurator.New(PageName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text5)
			.AddToAnswers(text4)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook01Page006")).deserializedGuid;
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook01Page106")).deserializedGuid;
		val.Cues.Add(val2);
		val.Cues.Add(val3);
		val.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook01Page005Cue0001.Text").SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions).SetText("RanRomAranBook01Page005Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text4).SetShowOnce().SetText("RanRomAranBook01Page005Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text5).SetText("RanRomAranBook01Page005Cue0003.Text").SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
