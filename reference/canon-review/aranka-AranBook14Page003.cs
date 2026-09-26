using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook14Page003
{
	private static readonly string PageName = "RanRomAranBook14Page003";

	private static readonly string Cue0001Name = "RanRomAranBook14Page003Cue0001";

	private static readonly string Cue0002Name = "RanRomAranBook14Page003Cue0002";

	private static readonly string Cue0003Name = "RanRomAranBook14Page003Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook14Page003Ans0004";

	private static readonly string Ans0005Name = "RanRomAranBook14Page003Ans0005";

	public static string Configure()
	{
		//IL_0163: Unknown result type (might be due to invalid IL or missing references)
		//IL_016a: Expected O, but got Unknown
		//IL_016a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0171: Expected O, but got Unknown
		//IL_017d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0182: Unknown result type (might be due to invalid IL or missing references)
		//IL_0199: Unknown result type (might be due to invalid IL or missing references)
		//IL_019e: Unknown result type (might be due to invalid IL or missing references)
		//IL_01a5: Expected O, but got Unknown
		//IL_01a5: Unknown result type (might be due to invalid IL or missing references)
		//IL_01ac: Expected O, but got Unknown
		//IL_01b8: Unknown result type (might be due to invalid IL or missing references)
		//IL_01bd: Unknown result type (might be due to invalid IL or missing references)
		//IL_01d4: Unknown result type (might be due to invalid IL or missing references)
		//IL_01d9: Unknown result type (might be due to invalid IL or missing references)
		//IL_01e0: Expected O, but got Unknown
		//IL_01e0: Unknown result type (might be due to invalid IL or missing references)
		//IL_01e7: Expected O, but got Unknown
		//IL_01f3: Unknown result type (might be due to invalid IL or missing references)
		//IL_01f8: Unknown result type (might be due to invalid IL or missing references)
		//IL_020f: Unknown result type (might be due to invalid IL or missing references)
		string text = "d31c89c1713b41af9746e4718ce6c9e1";
		string text2 = "3afd1311d35b47f188e5e2f8e332e0dc";
		string text3 = "83d94c9730b6451f9174b673912dfe1b";
		string text4 = "d87f52ed2be94de0ae0d2150abdf94bc";
		string text5 = "e87a7d4a200d41d7bcff127534e885d6";
		string text6 = "9da942e417684d0d8729f63f94733d4d";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomAranRomance", negate: false, null, true);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().CueSeen("0f077ad32cf24ba4bb72e7149a352e57", null, negate: true);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().CueSeen("0f077ad32cf24ba4bb72e7149a352e57");
		BookPageConfigurator.New(PageName, text).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToAnswers(text5)
			.AddToAnswers(text6)
			.SetConditions(conditions)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook14Page004")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueSelection val5 = new CueSelection();
		BlueprintCueBaseReference val6 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val6).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook14End")).deserializedGuid;
		val5.Cues.Add(val6);
		val5.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions2).SetText("RanRomAranBook14Page003Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions3).SetText("RanRomAranBook14Page003Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetText("RanRomAranBook14Page003Cue0003.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text5).SetShowOnce().SetText("RanRomAranBook14Page003Ans0004.Text")
			.SetNextCue(val3)
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text6).SetShowOnce().SetText("RanRomAranBook14Page003Ans0005.Text")
			.SetNextCue(val5)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
