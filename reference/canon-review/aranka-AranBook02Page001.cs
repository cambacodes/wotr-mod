using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook02Page001
{
	private static readonly string PageName = "RanRomAranBook02Page001";

	private static readonly string Cue0001Name = "RanRomAranBook02Page001Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook02Page001Ans0002";

	private static readonly string Ans0003Name = "RanRomAranBook02Page001Ans0003";

	private static readonly string Ans0004Name = "RanRomAranBook02Page001Ans0004";

	public static string Configure()
	{
		//IL_00b9: Unknown result type (might be due to invalid IL or missing references)
		//IL_00c0: Expected O, but got Unknown
		//IL_00c0: Unknown result type (might be due to invalid IL or missing references)
		//IL_00c7: Expected O, but got Unknown
		//IL_00d3: Unknown result type (might be due to invalid IL or missing references)
		//IL_00d8: Unknown result type (might be due to invalid IL or missing references)
		//IL_00ef: Unknown result type (might be due to invalid IL or missing references)
		//IL_00f4: Unknown result type (might be due to invalid IL or missing references)
		//IL_00fb: Expected O, but got Unknown
		//IL_00fb: Unknown result type (might be due to invalid IL or missing references)
		//IL_0102: Expected O, but got Unknown
		//IL_010e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0113: Unknown result type (might be due to invalid IL or missing references)
		//IL_012a: Unknown result type (might be due to invalid IL or missing references)
		string text = "6dd0589c729f4b13bbf334b8af299921";
		string text2 = "b8f05f204c874aa69e7bab5ddf78b7ee";
		string text3 = "675ffa84b9a546abbfc8bc4e9599c575";
		string text4 = "68d8558ec4d94b68bb355fb2946a126b";
		string text5 = "9f0880445a204922840af6c37d463416";
		BookPageConfigurator.New(PageName, text).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToAnswers(text3)
			.AddToAnswers(text4)
			.AddToAnswers(text5)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook02Page002")).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook02End")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook02Page001Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowOnce().SetText("RanRomAranBook02Page001Ans0002.Text")
			.SetNextCue(val)
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text4).SetShowOnce().SetText("RanRomAranBook02Page001Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text5).SetShowOnce().SetText("RanRomAranBook02Page001Ans0004.Text")
			.SetNextCue(val3)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
