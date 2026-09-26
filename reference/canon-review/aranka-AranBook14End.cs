using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook14End
{
	private static readonly string PageName = "RanRomAranBook14End";

	private static readonly string Cue0001Name = "RanRomAranBook14EndCue0001";

	private static readonly string Cue0002Name = "RanRomAranBook14EndCue0002";

	private static readonly string Cue0003Name = "RanRomAranBook14EndCue0003";

	private static readonly string Cue0004Name = "RanRomAranBook14EndCue0004";

	public static string Configure()
	{
		//IL_0171: Unknown result type (might be due to invalid IL or missing references)
		//IL_0178: Expected O, but got Unknown
		//IL_0178: Unknown result type (might be due to invalid IL or missing references)
		//IL_017f: Expected O, but got Unknown
		//IL_018b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0190: Unknown result type (might be due to invalid IL or missing references)
		//IL_01a7: Unknown result type (might be due to invalid IL or missing references)
		string text = "84f1179480ac4211aab52a7c31853e9e";
		string text2 = "599e7c0cc51741cda1bc55b787734c57";
		string text3 = "fefc9911dde04a76975e9027118c7935";
		string text4 = "f9df40d7d6b346298075b435eee6921c";
		string text5 = "e16e5b0b3aea426a888e8bb61c521815";
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected("9a573464ef1e475ab1f87ad7e3411ca9", null, negate: true).AnswerSelected("9da942e417684d0d8729f63f94733d4d", null, negate: true)
			.AnswerSelected("e87a7d4a200d41d7bcff127534e885d6", null, negate: true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected("9a573464ef1e475ab1f87ad7e3411ca9");
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected("9da942e417684d0d8729f63f94733d4d");
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected("e87a7d4a200d41d7bcff127534e885d6");
		BookPageConfigurator.New(PageName, text).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text5)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomAranBook14EndCue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomAranBook14EndCue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions3).SetText("RanRomAranBook14EndCue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions4).SetText("RanRomAranBook14EndCue0004.Text")
			.SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
