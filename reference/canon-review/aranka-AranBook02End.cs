using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.StoryEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.Blueprints;
using Kingmaker.Designers.Quests.Common;
using Kingmaker.DialogSystem;

namespace RanRomance.Aran;

public class AranBook02End
{
	private static readonly string PageName = "RanRomAranBook02End";

	private static readonly string Cue0001Name = "RanRomAranBook02EndCue0001";

	private static readonly string Cue0002Name = "RanRomAranBook02EndCue0002";

	private static readonly string Cue0003Name = "RanRomAranBook02EndCue0003";

	private static readonly string Cue0004Name = "RanRomAranBook02EndCue0004";

	private static readonly string Cue0005Name = "RanRomAranBook02EndCue0005";

	private static readonly string Cue0006Name = "RanRomAranBook02EndCue0006";

	private static readonly string Cue0007Name = "RanRomAranBook02EndCue0007";

	public static string Configure()
	{
		//IL_02c6: Unknown result type (might be due to invalid IL or missing references)
		//IL_02cd: Expected O, but got Unknown
		//IL_02cd: Unknown result type (might be due to invalid IL or missing references)
		//IL_02d4: Expected O, but got Unknown
		//IL_02e0: Unknown result type (might be due to invalid IL or missing references)
		//IL_02e5: Unknown result type (might be due to invalid IL or missing references)
		//IL_02fc: Unknown result type (might be due to invalid IL or missing references)
		string text = "7e24dc93f5d540c091644467e8eb52a0";
		string text2 = "0b03f923a5174742b7bad5ad18149d4a";
		string text3 = "c4582f7bd4854099a6ddc6a4eef1eccc";
		string text4 = "74dada6cf87d4d45b559c126015917fa";
		string text5 = "aea2ef76409c4dbcb9548792024dc8df";
		string text6 = "5a713cb1c3f642adaab8d1641175c1af";
		string text7 = "0a8d5ff9dda64c6db10784bfcdbbeb14";
		string text8 = "bc13df0cdde64ac3a1cc9eeae545bec3";
		ConditionsBuilder conditions = ConditionsBuilder.New().AnswerSelected("6ca96d6a2f9041289b432b350e901496");
		ConditionsBuilder conditions2 = ConditionsBuilder.New().AnswerSelected("85b74b2d3f784c06a0c31b4f06e486a6");
		ConditionsBuilder conditions3 = ConditionsBuilder.New().AnswerSelected("d477dcf13536498b9a9ff9f90c7f858e", null, negate: true).AnswerSelected("9f0880445a204922840af6c37d463416", null, negate: true)
			.EtudeStatus(null, null, "RanRomAranFlirt", negate: false, null, true);
		ConditionsBuilder conditions4 = ConditionsBuilder.New().AnswerSelected("d477dcf13536498b9a9ff9f90c7f858e", null, negate: true).AnswerSelected("9f0880445a204922840af6c37d463416", null, negate: true)
			.EtudeStatus(null, null, "RanRomAranFlirt", negate: true, null, true);
		ConditionsBuilder conditions5 = ConditionsBuilder.New().AnswerSelected("d477dcf13536498b9a9ff9f90c7f858e");
		ConditionsBuilder conditions6 = ConditionsBuilder.New().AnswerSelected("9f0880445a204922840af6c37d463416", null, negate: true);
		ConditionsBuilder conditions7 = ConditionsBuilder.New().AnswerSelected("9f0880445a204922840af6c37d463416");
		ActionsBuilder onStop = ActionsBuilder.New().SetObjectiveStatus("RanRomAranQuestEntryFail", true, (ObjectiveStatus)1);
		BookPageConfigurator.New(PageName, text).SetImageLink("b8160f03d066dbf46a16466eecb277d5").SetForeImageLink("assets/portraits/aranrom/nowings/large.png")
			.AddToCues(text2)
			.AddToCues(text3)
			.AddToCues(text4)
			.AddToCues(text5)
			.AddToCues(text6)
			.AddToCues(text7)
			.AddToCues(text8)
			.AddToCues("RanRomFiller")
			.Configure();
		CueSelection val = new CueSelection();
		BlueprintCueBaseReference val2 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val2).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(PageName)).deserializedGuid;
		val.Cues.Add(val2);
		val.Strategy = (Strategy)0;
		CueConfigurator.New(Cue0001Name, text2).SetConditions(conditions).SetText("RanRomAranBook02EndCue0001.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0002Name, text3).SetConditions(conditions2).SetText("RanRomAranBook02EndCue0002.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0003Name, text4).SetConditions(conditions3).SetText("RanRomAranBook02EndCue0003.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0004Name, text5).SetConditions(conditions4).SetText("RanRomAranBook02EndCue0004.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0005Name, text6).SetConditions(conditions5).SetText("RanRomAranBook02EndCue0005.Text")
			.SetShowOnce()
			.SetOnStop(onStop)
			.Configure();
		CueConfigurator.New(Cue0006Name, text7).SetConditions(conditions6).SetText("RanRomAranBook02EndCue0006.Text")
			.SetShowOnce()
			.Configure();
		CueConfigurator.New(Cue0007Name, text8).SetConditions(conditions7).SetText("RanRomAranBook02EndCue0007.Text")
			.SetShowOnce()
			.SetOnStop(onStop)
			.Configure();
		return text;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
