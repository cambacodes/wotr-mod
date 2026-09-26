using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.BasicEx;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.Designers.Quests.Common;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook03End
{
	private static readonly string PageName = "RanRomAranBook03End";

	private static readonly string Cue0001Name = "RanRomAranBook03EndCue0001";

	private static readonly string Cue0002Name = "RanRomAranBook03EndCue0002";

	private static readonly string Cue0003Name = "RanRomAranBook03EndCue0003";

	private static readonly string Cue0004Name = "RanRomAranBook03EndCue0004";

	private static readonly string Cue0005Name = "RanRomAranBook03EndCue0005";

	private static readonly string Cue0006Name = "RanRomAranBook03EndCue0006";

	private static readonly string Cue0007Name = "RanRomAranBook03EndCue0007";

	private static readonly string Cue0008Name = "RanRomAranBook03EndCue0008";

	public static string Configure()
	{
		//IL_02f2: Unknown result type (might be due to invalid IL or missing references)
		//IL_02f9: Expected O, but got Unknown
		//IL_02f9: Unknown result type (might be due to invalid IL or missing references)
		//IL_0300: Expected O, but got Unknown
		//IL_030c: Unknown result type (might be due to invalid IL or missing references)
		//IL_0311: Unknown result type (might be due to invalid IL or missing references)
		//IL_0328: Unknown result type (might be due to invalid IL or missing references)
		string text = "5190a877202044c69d98c7f05b8640e6";
		string text2 = "b18d250fa2fb4fdf9fe4eba04e9d1655";
		string text3 = "4b5628ce679446cc887a9d4173c9196d";
		string text4 = "7e5db279e53946f2bacdf91ba8c1ed5a";
		string text5 = "32311b13853d4d19b38e16b897eb099c";
		string text6 = "be931fd1a98a44d7be62ddf1df1b6769";
		string text7 = "d12fa4de60984a1c96eb72cc85d4231d";
		string text8 = "c4aa8d5ab084449a92b495d81e7a9f6e";
		string text9 = "31b1609c0a8b4788b3e4e82f111aba53";
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected("8c8eaea6fd444542a37939e326fd60cd");
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected("4a7d20e8a9bf40f5a9a4ae09e729d72e");
		ConditionsBuilder conditions3 = ConditionsBuilder.New().CueSeen("5fedc221cd864f868c7d7dbb7823e2d2", null, negate: true).CueSeen("9317f74874de4fe38bb68dacf9ca6b31", null, negate: true);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected("bb7b8143322248a29eaffbb44676e141").AnswerSelected("4ebfa28f6ed24fbab9e3bcfb8a251e20")
			.AnswerSelected("b2d319a4e87f4ef0a45a489b56906cc8")
			.UseOr();
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected("8ab68171a8674582bcaa705997840688");
		ConditionsBuilder conditions6 = ConditionsBuilder.New().PcRace(negate: false, (Race)2).PcRace(negate: false, (Race)3)
			.PcRace(negate: false, (Race)5)
			.PcRace(negate: false, (Race)7)
			.UseOr();
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected("8ab68171a8674582bcaa705997840688").AddOrAndLogic(conditions6);
		ConditionsBuilder conditions8 = ConditionsBuilder.New().AnswerSelected("8ab68171a8674582bcaa705997840688").AddOrAndLogic(conditions6, negate: true);
		ConditionsBuilder conditions9 = ConditionsBuilder.New().AnswerSelected("8ab68171a8674582bcaa705997840688");
		ActionsBuilder onStop = ActionsBuilder.New().SetObjectiveStatus("RanRomAranQuestEntryFail", true, (ObjectiveStatus)1);
		BookPageConfigurator.New(PageName, text).SetImageLink("52163ec59b7bf62408b1b24137843bba").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text5)
			.AddToCues(text6)
			.AddToCues(text7)
			.AddToCues(text8)
			.AddToCues(text9)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomAranBook03EndCue0001.Text")
			.SetShowOnce()
			.SetOnStop(onStop)
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomAranBook03EndCue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions3).SetText("RanRomAranBook03EndCue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions4).SetText("RanRomAranBook03EndCue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text6).SetConditions(conditions5).SetText("RanRomAranBook03EndCue0005.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0006Name, text7).SetConditions(conditions7).SetText("RanRomAranBook03EndCue0006.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0007Name, text8).SetConditions(conditions8).SetText("RanRomAranBook03EndCue0007.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0008Name, text9).SetConditions(conditions9).SetText("RanRomAranBook03EndCue0008.Text")
			.SetShowOnce()
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
