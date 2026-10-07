using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook01Page004
{
	private static readonly string PageName = "RanRomAranBook01Page004";

	private static readonly string Cue0001Name = "RanRomAranBook01Page004Cue0001";

	private static readonly string Ans0002Name = "RanRomAranBook01Page004Ans0002";

	private static readonly string Cue0002Name = "RanRomAranBook01Page004Cue0002";

	private static readonly string Ans0003Name = "RanRomAranBook01Page004Ans0003";

	private static readonly string Cue0003Name = "RanRomAranBook01Page004Cue0003";

	private static readonly string Ans0004Name = "RanRomAranBook01Page004Ans0004";

	private static readonly string Cue0004Name = "RanRomAranBook01Page004Cue0004";

	private static readonly string Cue0005Name = "RanRomAranBook01Page004Cue0005";

	private static readonly string Cue0006Name = "RanRomAranBook01Page004Cue0006";

	private static readonly string Ans0007Name = "RanRomAranBook01Page004Ans0007";

	private static readonly string Cue0007Name = "RanRomAranBook01Page004Cue0007";

	private static readonly string Cue0008Name = "RanRomAranBook01Page004Cue0008";

	private static readonly string Cue0009Name = "RanRomAranBook01Page004Cue0009";

	private static readonly string Cue0000Name = "RanRomAranBook01Page004Cue0000";

	private static readonly string Cue0011Name = "RanRomAranBook01Page004Cue0011";

	private static readonly string Ans0012Name = "RanRomAranBook01Page004Ans0012";

	public static string Configure()
	{
		//IL_0428: Unknown result type (might be due to invalid IL or missing references)
		//IL_042f: Expected O, but got Unknown
		//IL_042f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0436: Expected O, but got Unknown
		//IL_0442: Unknown result type (might be due to invalid IL or missing references)
		//IL_0447: Unknown result type (might be due to invalid IL or missing references)
		//IL_045e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0463: Unknown result type (might be due to invalid IL or missing references)
		//IL_046a: Expected O, but got Unknown
		//IL_046a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0471: Expected O, but got Unknown
		//IL_047d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0482: Unknown result type (might be due to invalid IL or missing references)
		//IL_0499: Unknown result type (might be due to invalid IL or missing references)
		string text = "2394521186f046b9831bddabcb2a9b10";
		string text2 = "ab5f701050b44a2fac93aa3f642d2ed5";
		string text3 = "ee24d2c57f754d75b061a0056e91a0d7";
		string text4 = "72ac12f69fe24c619b5dcce12d9ec26d";
		string text5 = "790b0e4756794022b1834d4646aa5139";
		string text6 = "ae05ac21854d4fda87d47541befbe1cb";
		string text7 = "8e5eaa0a99ee41cdb5c5e29fd9bc6320";
		string text8 = "60ce5db105c74d14bc2dc1da9555340c";
		string text9 = "b8942264db57478cba876161028b27f7";
		string text10 = "b0da2db1817c4c2989c30f41900fcd5a";
		string text11 = "0d97ff5b67e742cdb8ec140e5f6c5f7f";
		string text12 = "eec014aae31646c2b08869eb43811c27";
		string text13 = "4b9b4ddc09c6463fadb4fa436eecea0a";
		string text14 = "05a9a8c1eeb942618dc75f79e85c1ca1";
		string text15 = "db6c6a0384234d5e98970d8028d84630";
		string text16 = "125d0f62216240dd81792c7d6a52a7e1";
		string text17 = "898a7711f7cb4101a2f95e52f3d85067";
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected(text3);
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected(text5);
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected(text7).CueSeen("6d69b0a8cff04fd3b36282be1bb7c257");
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected(text7).CueSeen("6d69b0a8cff04fd3b36282be1bb7c257", null, negate: true);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected(text7).EtudeStatus(null, null, "d7169995e449fdc4db861ddf0b9beff8", negate: false, null, true);
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected(text11).CueSeen("7d4cb79fe11d4f198105efb47cc86146");
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected(text11).CueSeen("6d69b0a8cff04fd3b36282be1bb7c257");
		ConditionsBuilder conditions8 = ConditionsBuilder.New().AnswerSelected(text11).CueSeen("a5d510cfa7bc4f9985db3dc9d6d8d332");
		ConditionsBuilder conditions9 = ConditionsBuilder.New().AnswerSelected(text11).CueSeen("66440ec2156b4bed9f822584e3fc3d6b");
		ConditionsBuilder conditions10 = ConditionsBuilder.New().AnswerSelected(text11).CueSeen("0e7fed613c974e8aa201b413105bc895");
		BookPageConfigurator.New(PageName, text).SetImageLink("df4a5da19a0a64542929dc8409b29bbe").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text4)
			.AddToAnswers(text3)
			.AddToCues(text6)
			.AddToAnswers(text5)
			.AddToCues(text8)
			.AddToAnswers(text7)
			.AddToCues(text9)
			.AddToCues(text10)
			.AddToCues(text12)
			.AddToAnswers(text11)
			.AddToCues(text13)
			.AddToCues(text14)
			.AddToCues(text15)
			.AddToCues(text16)
			.AddToAnswers(text17)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook01Page004")).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueSelection val3 = new CueSelection();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("RanRomAranBook01Page005")).deserializedGuid;
		val3.Cues.Add(val4);
		val3.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetText("RanRomAranBook01Page004Cue0001.Text").SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0002Name, text3).SetShowOnce().SetText("RanRomAranBook01Page004Ans0002.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0002Name, text4).SetConditions(conditions).SetText("RanRomAranBook01Page004Cue0002.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0003Name, text5).SetShowOnce().SetText("RanRomAranBook01Page004Ans0003.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0003Name, text6).SetConditions(conditions2).SetText("RanRomAranBook01Page004Cue0003.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0004Name, text7).SetShowOnce().SetText("RanRomAranBook01Page004Ans0004.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0004Name, text8).SetConditions(conditions3).SetText("RanRomAranBook01Page004Cue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text9).SetConditions(conditions4).SetText("RanRomAranBook01Page004Cue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text10).SetConditions(conditions5).SetText("RanRomAranBook01Page004Cue0006.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0007Name, text11).SetShowOnce().SetText("RanRomAranBook01Page004Ans0007.Text")
			.SetNextCue(val)
			.Configure();
		CueConfigurator.New(Cue0007Name, text12).SetConditions(conditions6).SetText("RanRomAranBook01Page004Cue0007.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0008Name, text13).SetConditions(conditions7).SetText("RanRomAranBook01Page004Cue0008.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0009Name, text14).SetConditions(conditions8).SetText("RanRomAranBook01Page004Cue0009.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0000Name, text15).SetConditions(conditions9).SetText("RanRomAranBook01Page004Cue0000.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0011Name, text16).SetConditions(conditions10).SetText("RanRomAranBook01Page004Cue0011.Text")
			.SetShowOnce()
			.Configure();
		AnswerConfigurator.New(Ans0012Name, text17).SetShowOnce().SetText("RanRomAranBook01Page004Ans0012.Text")
			.SetNextCue(val3)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
