using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Conditions.Builder;
using BlueprintCore.Conditions.Builder.StoryEx;
using BlueprintCore.Utils;
using HarmonyLib;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;

namespace Epilogue.Setup;

public class EpSetup
{
	private static readonly string SeqName = "RanSeq3000";

	public static void Configure()
	{
		//IL_0041: Unknown result type (might be due to invalid IL or missing references)
		//IL_0047: Expected O, but got Unknown
		//IL_05c0: Unknown result type (might be due to invalid IL or missing references)
		//IL_05c6: Expected O, but got Unknown
		//IL_0660: Unknown result type (might be due to invalid IL or missing references)
		//IL_0667: Expected O, but got Unknown
		//IL_0b44: Unknown result type (might be due to invalid IL or missing references)
		//IL_0b4b: Expected O, but got Unknown
		ConditionsBuilder conditions = ConditionsBuilder.New().EtudeStatus(null, null, "9955b661dd7640b19986e453293a3e0a", negate: true, null, true);
		CueSelection val = new CueSelection();
		val.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("fec3b6f28610c8a48a239f148ed3ed60"));
		val.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("20d2a78ccae48434b9008a273bd87f19"));
		if (Harmony.HasAnyPatches("RanEpilogue"))
		{
			val.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("a7a3cbf84ba74f068aa6d76c962323c1"));
		}
		SequenceExitConfigurator.New("RanRomAddExit", "2ea3eef9a1e046ecb1eece775cccba1a").SetContinueValue(val).Configure();
		CueSequenceConfigurator.New("RanRomAdd", "ed4baeaf69394754902344f0598d7e5a").AddToCues("RanRomAranSlideHulr").AddToCues("RanRomNoctSlide0001")
			.AddToCues("RanRomNoctSlide0003")
			.AddToCues("RanRomNoctSlide0002")
			.AddToCues("RanRomNoctSlide0004")
			.AddToCues("RanRomNuraSlide0001")
			.AddToCues("RanRomNuraSlide0002")
			.AddToCues("RanRomNuraSlide0003")
			.AddToCues("RanRomNuraSlide0004")
			.AddToCues("RanRomTargSlideSwarm")
			.AddToCues("RanRomTargSlide0001")
			.AddToCues("RanRomTargSlide2001")
			.AddToCues("RanRomTargSlide0002")
			.AddToCues("RanRomTargSlide2002")
			.AddToCues("RanRomTargSlide0003")
			.AddToCues("RanRomTargSlide0004")
			.AddToCues("RanRomTargSlide2004")
			.AddToCues("RanRomTargSlide0007")
			.AddToCues("RanRomTargSlide2007")
			.AddToCues("RanRomTargSlide1001")
			.AddToCues("RanRomTargSlide3001")
			.AddToCues("RanRomTargSlide0005")
			.AddToCues("RanRomTargSlide2005")
			.AddToCues("RanRomTargSlide0006")
			.AddToCues("RanRomTargSlide2006")
			.AddToCues("RanRomTargSlide0008")
			.AddToCues("RanRomTargSlide2008")
			.AddToCues("RanRomTereSlide0001")
			.AddToCues("RanRomTereSlide0002")
			.AddToCues("RanRomTereSlide0003")
			.AddToCues("RanRomTereSlide0004")
			.AddToCues("RanRomTereSlide0005")
			.AddToCues("RanRomTereSlide0006")
			.AddToCues("RanRomTereSlide0007")
			.AddToCues("RanRomAranSlide0001")
			.AddToCues("RanRomAranSlide0002")
			.AddToCues("RanRomAranSlide0004")
			.AddToCues("RanRomAranSlide0005")
			.AddToCues("RanRomMinaSlide0001")
			.AddToCues("RanRomMinaSlide0002")
			.AddToCues("RanRomMinaSlide0003")
			.AddToCues("RanRomMinaSlide0004")
			.AddToCues("RanRomMinaSlide0005")
			.AddToCues("RanRomMinaSlide0006")
			.AddToCues("RanRomMinaSlide0007")
			.AddToCues("RanRomMinaSlide0008")
			.SetConditions(conditions)
			.SetExit("RanRomAddExit")
			.Configure();
		CueSequenceConfigurator.For("ced82f299d246f448b48afa0b630dd70").AddToCues("RanRomNuraAeon").AddToCues("RanRomTargSlideAeon")
			.AddToCues("RanRomTereSlideAeon")
			.AddToCues("RanRomAranSlideAeon")
			.AddToCues("RanRomMinaSlideAeon")
			.Configure();
		CueSelection val2 = new CueSelection();
		val2.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("RanRomAdd"));
		val2.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("fec3b6f28610c8a48a239f148ed3ed60"));
		val2.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("20d2a78ccae48434b9008a273bd87f19"));
		if (Harmony.HasAnyPatches("RanEpilogue"))
		{
			val2.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("a7a3cbf84ba74f068aa6d76c962323c1"));
		}
		SequenceExitConfigurator.For("d649f17a42a8e0c418bb336ced272934").SetContinueValue(val2).Configure();
		if (Harmony.HasAnyPatches("RanEpilogue"))
		{
			CueSelection val3 = new CueSelection();
			val3.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("e470b652c6cd41ffb60b6ad7d0aaec14"));
			val3.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("988317fc363540c2894a500f0374d654"));
			val3.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("73bd402ad7a94b3cb68a13937d066a90"));
			SequenceExitConfigurator.New("RanRomIntExit", "b0665c9fa44f4fe7b30f2b95b0d22b44").SetContinueValue(val3).Configure();
			CueSequenceConfigurator.New("RanRomInt", "2b9424b1b93e4d0896b0958db79d2339").AddToCues("RanRomAranSlideHulr").AddToCues("RanRomNoctSlide0001")
				.AddToCues("RanRomNoctSlide0003")
				.AddToCues("RanRomNoctSlide0002")
				.AddToCues("RanRomNoctSlide0004")
				.AddToCues("RanRomNuraSlide0001")
				.AddToCues("RanRomNuraSlide0002")
				.AddToCues("RanRomNuraSlide0003")
				.AddToCues("RanRomNuraSlide0004")
				.AddToCues("RanRomTargSlideSwarm")
				.AddToCues("RanRomTargSlide0001")
				.AddToCues("RanRomTargSlide2001")
				.AddToCues("RanRomTargSlide0002")
				.AddToCues("RanRomTargSlide2002")
				.AddToCues("RanRomTargSlide0003")
				.AddToCues("RanRomTargSlide0004")
				.AddToCues("RanRomTargSlide2004")
				.AddToCues("RanRomTargSlide0007")
				.AddToCues("RanRomTargSlide2007")
				.AddToCues("RanRomTargSlide1001")
				.AddToCues("RanRomTargSlide3001")
				.AddToCues("RanRomTargSlide0005")
				.AddToCues("RanRomTargSlide2005")
				.AddToCues("RanRomTargSlide0006")
				.AddToCues("RanRomTargSlide2006")
				.AddToCues("RanRomTargSlide0008")
				.AddToCues("RanRomTargSlide2008")
				.AddToCues("RanRomTereSlide0001")
				.AddToCues("RanRomTereSlide0002")
				.AddToCues("RanRomTereSlide0003")
				.AddToCues("RanRomTereSlide0004")
				.AddToCues("RanRomTereSlide0005")
				.AddToCues("RanRomTereSlide0006")
				.AddToCues("RanRomTereSlide0007")
				.AddToCues("RanRomAranSlide0001")
				.AddToCues("RanRomAranSlide0002")
				.AddToCues("RanRomAranSlide0004")
				.AddToCues("RanRomAranSlide0005")
				.AddToCues("RanRomMinaSlide0001")
				.AddToCues("RanRomMinaSlide0002")
				.AddToCues("RanRomMinaSlide0003")
				.AddToCues("RanRomMinaSlide0004")
				.AddToCues("RanRomMinaSlide0005")
				.AddToCues("RanRomMinaSlide0006")
				.AddToCues("RanRomMinaSlide0007")
				.AddToCues("RanRomMinaSlide0008")
				.SetConditions(conditions)
				.SetExit("RanRomIntExit")
				.Configure();
			CueSelection val4 = new CueSelection();
			val4.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("RanRomInt"));
			val4.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("e470b652c6cd41ffb60b6ad7d0aaec14"));
			val4.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("988317fc363540c2894a500f0374d654"));
			val4.Cues.Add(BlueprintTool.GetRef<BlueprintCueBaseReference>("73bd402ad7a94b3cb68a13937d066a90"));
			SequenceExitConfigurator.For("607351955e174bd8b3d61ba9a4df9b6c").SetContinueValue(val4).Configure();
			BookPageConfigurator.For("992f0460e85f4b2390e3a76f6620bdbd").SetForeImageLink("assets/portraits/tererom/normal/large.png").Configure();
			BookPageConfigurator.For("103516c103f34aa2bac3ea0c9d6a5ed5").SetForeImageLink("assets/portraits/tererom/ravener/large.png").Configure();
		}
	}
}
