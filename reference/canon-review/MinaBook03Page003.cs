using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Mina;

public class MinaBook03Page003
{
	private static readonly string PageName = "RanRomMinaBook03Page003";

	private static readonly string Cue0001Name = "RanRomMinaBook03Page003Cue0001";

	private static readonly string Cue0002Name = "RanRomMinaBook03Page003Cue0002";

	private static readonly string Cue0003Name = "RanRomMinaBook03Page003Cue0003";

	private static readonly string Ans0004Name = "RanRomMinaBook03Page003Ans0004";

	private static readonly string Cue0004Name = "RanRomMinaBook03Page003Cue0004";

	private static readonly string Ans0005Name = "RanRomMinaBook03Page003Ans0005";

	private static readonly string Cue0005Name = "RanRomMinaBook03Page003Cue0005";

	private static readonly string Cue0006Name = "RanRomMinaBook03Page003Cue0006";

	private static readonly string Ans0007Name = "RanRomMinaBook03Page003Ans0007";

	private static readonly string Cue0007Name = "RanRomMinaBook03Page003Cue0007";

	private static readonly string Cue0008Name = "RanRomMinaBook03Page003Cue0008";

	private static readonly string Cue0009Name = "RanRomMinaBook03Page003Cue0009";

	private static readonly string Ans0000Name = "RanRomMinaBook03Page003Ans0000";

	private static readonly string Ans0011Name = "RanRomMinaBook03Page003Ans0011";

	public static string Configure()
	{
		//IL_0610: Unknown result type (might be due to invalid IL or missing references)
		//IL_0617: Expected O, but got Unknown
		//IL_0617: Unknown result type (might be due to invalid IL or missing references)
		//IL_061e: Expected O, but got Unknown
		//IL_062a: Unknown result type (might be due to invalid IL or missing references)
		//IL_062f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0646: Unknown result type (might be due to invalid IL or missing references)
		//IL_064b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0652: Expected O, but got Unknown
		//IL_0652: Unknown result type (might be due to invalid IL or missing references)
		//IL_0659: Expected O, but got Unknown
		//IL_0665: Unknown result type (might be due to invalid IL or missing references)
		//IL_066a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0681: Unknown result type (might be due to invalid IL or missing references)
		string text = "c20314ead63a446c90140d04f52ee89e";
		string text2 = "5244f58548f9440cab4da66769fbf615";
		string text3 = "1aa2cdb539754f39a29dd1a6626eb670";
		string text4 = "1a3b51700cf3427a8d35f629f7c77e6d";
		string text5 = "03fc55744c414614b7869bf843cc4fa8";
		string text6 = "a1fabe2bd4354649aa1ede9a7bca136d";
		string text7 = "7540dbd308194f6bbff982358bff3359";
		string text8 = "449862085b774d6295949a92f158397e";
		string text9 = "1334e7fe3fc2461bac0ca67599b32878";
		string text10 = "359d4d9df01b4dbebd71322cac3bfda3";
		string text11 = "e15de525c99d40c6a6faf0afa61be756";
		string text12 = "e8af7bdaaece4995bfe1e0e9eec871a9";
		string text13 = "80ad6d6f87d54a43b019e25f69df1c0c";
		string text14 = "56056c49915d468e9a6b469260dd42b3";
		string text15 = "fd4e6bbef0d4445b8bee465524698520";
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaSex2", negate: false, null, true);
		ActionsBuilder onSelect = ActionsBuilder.New().StartEtude("RanRomMinaRomance");
		ActionsBuilder onSelect2 = ActionsBuilder.New().CompleteEtude("RanRomMinaSex1").CompleteEtude("RanRomMinaSex2");
		ConditionsBuilder conditions2 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaDragon", negate: false, null, true).EtudeStatus(null, null, "RanRomMinaLegend", negate: false, null, true)
			.EtudeStatus(null, null, "RanRomMinaRedemption", negate: false, null, true)
			.UseOr();
		ConditionsBuilder conditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaDemon", negate: false, null, true);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().EtudeStatus(null, null, "RanRomMinaDragon", negate: true, null, true).EtudeStatus(null, null, "RanRomMinaLegend", negate: true, null, true)
			.EtudeStatus(null, null, "RanRomMinaRedemption", negate: true, null, true)
			.EtudeStatus(null, null, "RanRomMinaDemon", negate: true, null, true);
		ConditionsBuilder showConditions = ConditionsBuilder.New().CueSeen(text2);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder showConditions2 = ConditionsBuilder.New().CueSeen(text2, null, negate: true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected(text7).CueSeen(text3);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected(text7).CueSeen(text4);
		ConditionsBuilder showConditions3 = ConditionsBuilder.New().EtudeStatus(null, null, "71f85264d9064074f9cf74999ecbffa9", negate: false, null, true);
		ConditionsBuilder conditions8 = ConditionsBuilder.New().AnswerSelected(text10).CueSeen(text2);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().AnswerSelected(text10).CueSeen(text3);
		ConditionsBuilder conditions10 = ConditionsBuilder.New().AnswerSelected(text10).CueSeen(text4);
		BookPageConfigurator.New(PageName, text).SetImageLink("482f509e50aa6484bafee746ddb3849f").SetForeImageLink("1abecb015eedf484eab1b0229a7cecf7")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToCues(text9)
			.AddToCues(text11)
			.AddToAnswers(text10)
			.AddToCues(text12)
			.AddToCues(text13)
			.AddToAnswers(text14)
			.AddToAnswers(text15)
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
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomMinaBook03End")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions2).SetText("RanRomMinaBook03Page003Cue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions3).SetText("RanRomMinaBook03Page003Cue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions4).SetText("RanRomMinaBook03Page003Cue0003.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text5).SetShowConditions(showConditions).SetShowOnce()
			.SetText("RanRomMinaBook03Page003Ans0004.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0004Name, text6).SetConditions(conditions5).SetText("RanRomMinaBook03Page003Cue0004.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0005Name, text7).SetShowConditions(showConditions2).SetShowOnce()
			.SetText("RanRomMinaBook03Page003Ans0005.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0005Name, text8).SetConditions(conditions6).SetText("RanRomMinaBook03Page003Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text9).SetConditions(conditions7).SetText("RanRomMinaBook03Page003Cue0006.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text10).SetShowConditions(showConditions3).SetShowOnce()
			.SetText("RanRomMinaBook03Page003Ans0007.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0007Name, text11).SetConditions(conditions8).SetText("RanRomMinaBook03Page003Cue0007.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0008Name, text12).SetConditions(conditions9).SetText("RanRomMinaBook03Page003Cue0008.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0009Name, text13).SetConditions(conditions10).SetText("RanRomMinaBook03Page003Cue0009.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0000Name, text14).SetShowOnce().SetText("RanRomMinaBook03Page003Ans0000.Text")
			.SetNextCue(val3)
			.SetOnSelect(onSelect)
			.Configure();
		AnswerConfigurator.New(Ans0011Name, text15).SetShowOnce().SetText("RanRomMinaBook03Page003Ans0011.Text")
			.SetNextCue(val3)
			.SetOnSelect(onSelect2)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
