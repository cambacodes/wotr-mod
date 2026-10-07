using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class SlideArue
{
	private static readonly string SlideName = "RanRomAranSlideArue";

	private static readonly string Cue0001Name = "RanRomAranSlideArueCue0001";

	public static string Configure()
	{
		//IL_004a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0050: Expected O, but got Unknown
		//IL_0050: Unknown result type (might be due to invalid IL or missing references)
		//IL_0056: Expected O, but got Unknown
		//IL_005d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0062: Unknown result type (might be due to invalid IL or missing references)
		//IL_0076: Unknown result type (might be due to invalid IL or missing references)
		string text = "959237a34dfe436eb8f088b4be259daa";
		ConditionsBuilder conditions = ConditionsBuilder.New().DialogSeen("RanRomAranBook04");
		CueConfigurator.New(Cue0001Name, text).SetConditions(conditions).SetText("RanRomAranSlideArueCue0001.Text")
			.SetShowOnce()
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueConfigurator.For("78ae1bdc3b0824b4ca2ed618782f1faa").SetContinueValue(val).Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
