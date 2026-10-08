using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Tere;

public class TereBook00Page001
{
	private static readonly string PageName = "RanRomTereBook00Page001";

	private static readonly string Ans0001Name = "RanRomTereBook00Page001Ans0001";

	private static readonly string Cue0001Name = "RanRomTereBook00Page001Cue0001";

	public static string Configure()
	{
		//IL_0074: Unknown result type (might be due to invalid IL or missing references)
		//IL_007a: Expected O, but got Unknown
		//IL_007a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0081: Expected O, but got Unknown
		//IL_008d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0092: Unknown result type (might be due to invalid IL or missing references)
		//IL_00a7: Unknown result type (might be due to invalid IL or missing references)
		string text = "3e44b82e483b4d159956f293e3e54842";
		string text2 = "5c9b865b06d84b24a372b8d576df7962";
		string text3 = "2d6dd3e109da4b9587944d1b82a0297d";
		BookPageConfigurator.New(PageName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").AddToCues(text3)
			.AddToAnswers(text2)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomTereBook00Page002")).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		AnswerConfigurator.New(Ans0001Name, text2).SetShowOnce().SetText("RanRomTereBook00Page001Ans0001.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0001Name, text3).SetText("RanRomTereBook00Page001Cue0001.Text").SetShowOnce()
			.Configure();
		return text;
	}
}
