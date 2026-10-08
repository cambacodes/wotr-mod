using BlueprintCore.Actions.Builder;
using BlueprintCore.Actions.Builder.BasicEx;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace RanRomance.Mina;

public class MinaBook03Dial001
{
	private static readonly string Cue0001Name = "RanRomMinaBook03Dial001Cue0001";

	public static string Configure()
	{
		//IL_005d: Unknown result type (might be due to invalid IL or missing references)
		//IL_0063: Expected O, but got Unknown
		//IL_0063: Unknown result type (might be due to invalid IL or missing references)
		//IL_0069: Expected O, but got Unknown
		//IL_0069: Unknown result type (might be due to invalid IL or missing references)
		//IL_0070: Expected O, but got Unknown
		//IL_0070: Unknown result type (might be due to invalid IL or missing references)
		//IL_0077: Expected O, but got Unknown
		//IL_007f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0084: Unknown result type (might be due to invalid IL or missing references)
		//IL_0095: Unknown result type (might be due to invalid IL or missing references)
		//IL_009a: Unknown result type (might be due to invalid IL or missing references)
		//IL_00bd: Unknown result type (might be due to invalid IL or missing references)
		//IL_00d2: Unknown result type (might be due to invalid IL or missing references)
		//IL_00d7: Unknown result type (might be due to invalid IL or missing references)
		//IL_00de: Expected O, but got Unknown
		string text = "3604c7da59274d67845db9a521bbc1c8";
		ConditionsBuilder conditions = ConditionsBuilder.New().QuestStatus(negate: false, "a6c08ebd49e56164da590d2f17a819c5", (QuestState)2).EtudeStatus(null, null, "3a25b1f2a81f84a40b4fb658f4d2fe0f", negate: false, false, true);
		CueSelection val = new CueSelection();
		CueSelection val2 = new CueSelection();
		BlueprintCueBaseReference val3 = new BlueprintCueBaseReference();
		BlueprintCueBaseReference val4 = new BlueprintCueBaseReference();
		((BlueprintReferenceBase)val3).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>(text)).deserializedGuid;
		((BlueprintReferenceBase)val4).deserializedGuid = ((BlueprintReferenceBase)BlueprintTool.GetRef<AnyBlueprintReference>("f30fc320424bfed43af0a5fede802258")).deserializedGuid;
		val.Cues.Add(val3);
		val.Cues.Add(val4);
		val.Strategy = (Strategy)0;
		val2.Cues.Add(val4);
		val2.Strategy = (Strategy)0;
		DialogSpeaker val5 = new DialogSpeaker();
		val5.NoSpeaker = false;
		val5.MoveCamera = true;
		val5.NotRevealInFoW = false;
		val5.SwitchDual = false;
		ActionsBuilder onShow = ActionsBuilder.New().GiveItemToPlayer("dac32e88810a20941a53a5960e581b3d", null, 1);
		CueConfigurator.New(Cue0001Name, text).SetConditions(conditions).SetText("RanRomMinaChpt03Dial001Cue0001.Text")
			.SetOnShow(onShow)
			.SetSpeaker(val5)
			.SetShowOnce()
			.SetContinueValue(val2)
			.Configure();
		CueConfigurator.For("34c43055d77be404f906997c93be06aa").SetContinueValue(val).Configure();
		return null;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
