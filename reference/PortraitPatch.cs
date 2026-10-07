using System;
using System.IO;
using ExtensionMethods;
using Harmony12;
using Kingmaker;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.GameModes;
using Kingmaker.ResourceLinks;
using Kingmaker.UI.UnitSettings;
using Kingmaker.UnitLogic;
using Kingmaker.UnitLogic.Buffs;
using UnityEngine;

namespace CustomNpcPortraits;

[HarmonyPatch(typeof(UnitUISettings), "Portrait", MethodType.Getter)]
public static class GetPortrait_Patch
{
	public static bool Prefix(UnitUISettings __instance, ref PortraitData __result, BlueprintPortrait ___m_Portrait, BlueprintPortrait ___m_CustomPortrait)
	{
		//IL_0704: Unknown result type (might be due to invalid IL or missing references)
		//IL_070b: Expected O, but got Unknown
		if (!Main.enabled || Main.pauseGetPortraitsafe)
		{
			return true;
		}
		if ((Game.Instance.Player.AllCharacters.Contains(__instance.Owner.Unit) || Main.companions.Contains(__instance.Owner.Unit.CharacterName.cleanCharName())) && __instance.Owner.Unit.CharacterName.cleanCharName() != "Player Character")
		{
			Main.DebugLog("GetPortrait: " + __instance.Owner.Unit.CharacterName.cleanCharName());
			if (!Main.settings.ManageCompanions)
			{
				return true;
			}
			__result = Main.SetPortrait(__instance.Owner.Unit, pickUpOnly: false);
			if (__result != null)
			{
				return false;
			}
			return true;
		}
		if (!Main.enabled || Main.isSetPortrait)
		{
			return true;
		}
		try
		{
			if (Game.Instance == null || Game.Instance.CurrentMode == (GameModeType)null || Game.Instance.CurrentMode != GameModeType.Dialog || Game.Instance.DialogController == null || Game.Instance.DialogController.CurrentSpeaker == (UnitDescriptor)null || Game.Instance.DialogController.CurrentSpeakerBlueprint == null || Game.Instance.DialogController.CurrentSpeakerBlueprint.CharacterName.cleanCharName() == null)
			{
				return true;
			}
			string text = __instance.Owner.Unit.CharacterName.cleanCharName();
			if (Game.Instance.DialogController.CurrentSpeakerName.cleanCharName() != null && Game.Instance.DialogController.CurrentSpeakerName.cleanCharName().Length > 0)
			{
				text = Game.Instance.DialogController.CurrentSpeakerName.cleanCharName();
			}
			if (!__instance.Owner.Unit.IsMainCharacter || (Game.Instance.DialogController.CurrentSpeakerName.cleanCharName().Equals("Wirlong Black Mask") && Game.Instance.DialogController.CurrentCue.Speaker.Blueprint.CharacterName.cleanCharName() != Game.Instance.Player.GetMainPartyUnit().CharacterName.cleanCharName()))
			{
				if ((text.Equals(Main.AstyName) || text.Equals(Main.VelhmName) || text.Equals(Main.TranName)) && (Game.Instance.Player.Dialog.ShownCues.Contains((BlueprintCueBase)(object)ResourcesLibrary.TryGetBlueprint<BlueprintCue>("02f7b70fa8433504dbad8f817bdc4578")) || ((Object)Game.Instance.DialogController.CurrentSpeaker.View).name.ToLower().Contains("drow")))
				{
					text += " - Drow";
				}
				if (text.Equals(Main.IrabethName) && Game.Instance.Player.EtudesSystem.EtudeIsStarted(ResourcesLibrary.TryGetBlueprint<BlueprintEtude>("b4f08736cf124ae4996fcef7c0a33bf1")))
				{
					Directory.CreateDirectory(Path.Combine(Main.GetNpcPortraitsDirectory(), Main.IrabethName + " - Scar"));
					text = Main.IrabethName + " - Scar";
				}
				BlueprintUnit val = Game.Instance.DialogController.CurrentSpeakerBlueprint;
				string unitPortraitPath = GetUnitPortraitPath(val);
				if (Game.Instance.DialogController.CurrentCue.Speaker.Blueprint != null)
				{
					val = Game.Instance.DialogController.CurrentCue.Speaker.Blueprint;
				}
				Main.pauseGetPortraitsafe = true;
				BlueprintPortrait portraitSafe = val.PortraitSafe;
				Main.pauseGetPortraitsafe = false;
				bool flag = false;
				Directory.CreateDirectory(Path.Combine(Main.GetNpcPortraitsDirectory(), text));
				if (text != ((SimpleBlueprint)val).name && !text.Equals(Main.AstyName + " - Drow") && !text.Equals(Main.TranName + " - Drow") && !text.Equals(Main.VelhmName + " - Drow") && !text.Equals(Main.AstyName) && !text.Equals(Main.TranName) && !text.Equals(Main.VelhmName))
				{
					Directory.CreateDirectory(Path.Combine(Main.GetNpcPortraitsDirectory(), text, ((SimpleBlueprint)val).name));
				}
				if (unitPortraitPath == null || unitPortraitPath.Length == 0)
				{
					if (!Main.settings.AutoSecret && portraitSafe.Data.InitiativePortrait)
					{
						return true;
					}
					flag = true;
				}
				else if (Main.settings.AutoBackup)
				{
					flag = !File.Exists(Path.Combine(unitPortraitPath, Main.GetDefaultPortraitsDirName(), Main.mediumName));
				}
				if (flag && !__instance.Owner.Unit.CharacterName.cleanCharName().Equals(Main.AstyName) && !__instance.Owner.Unit.CharacterName.cleanCharName().Equals(Main.TranName) && !__instance.Owner.Unit.CharacterName.cleanCharName().Equals(Main.VelhmName))
				{
					Main.DebugLog("Getportrait() 3 " + __instance.Owner.Unit.CharacterName.cleanCharName());
					Main.DebugLog("Getportrait() 3 " + Main.AstyName);
					Main.DebugLog("Getportrait() 3 " + Main.TranName);
					Main.DebugLog("Getportrait() 3 " + Main.VelhmName);
					BlueprintPortrait val2 = BlueprintReference<BlueprintPortrait>.op_Implicit((BlueprintReference<BlueprintPortrait>)(object)val.m_Portrait);
					if (portraitSafe != null && portraitSafe.Data != null && val2 != null && (text.Contains("Crusader") || !((SimpleBlueprint)val2).name.Contains("BCT_Rand_Crusader_Soldier")))
					{
						SpriteLink halfLengthImage = portraitSafe.Data.m_HalfLengthImage;
						if ((WeakResourceLink)(object)halfLengthImage != (WeakResourceLink)null && ((WeakResourceLink)halfLengthImage).AssetId != null && ((WeakResourceLink)halfLengthImage).AssetId.Length > 5)
						{
							Main.DebugLog("Getportrait() wtf?? " + text);
							if (!text.Equals(Main.IrabethName + " - Scar"))
							{
								Main.SaveOriginals(val, Path.Combine(Main.GetNpcPortraitsDirectory(), text));
							}
							if (text != ((SimpleBlueprint)val).name && !text.Equals(Main.AstyName + " - Drow") && !text.Equals(Main.TranName + " - Drow") && !text.Equals(Main.VelhmName + " - Drow") && !text.Equals(Main.IrabethName + " - Scar"))
							{
								Main.SaveOriginals(val, Path.Combine(Main.GetNpcPortraitsDirectory(), text, ((SimpleBlueprint)val).name));
							}
						}
					}
				}
				unitPortraitPath = ((Main.npcCycle.Length > 1) ? Path.Combine(Main.GetNpcPortraitsDirectory(), text, Main.npcCycle) : ((Main.npcSubCycle.Length <= 1) ? GetUnitPortraitPath(val) : Path.Combine(Main.GetNpcPortraitsDirectory(), text, ((SimpleBlueprint)val).name, Main.npcSubCycle)));
				if (!Directory.Exists(unitPortraitPath))
				{
					return true;
				}
				if (File.Exists(Path.Combine(unitPortraitPath, Main.mediumName)))
				{
					CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(unitPortraitPath, "Medium.png"));
					PortraitData val3 = new PortraitData(unitPortraitPath);
					Main.pauseGetPortraitsafe = true;
					val3.m_PetEyeImage = Game.Instance.DialogController.CurrentSpeakerBlueprint.PortraitSafe.Data.m_PetEyeImage;
					Main.pauseGetPortraitsafe = false;
					__result = val3;
					return false;
				}
				return true;
			}
			return true;
		}
		catch (Exception ex)
		{
			Main.DebugError(ex);
			return true;
		}
	}

	public static void Postfix(UnitUISettings __instance, ref PortraitData __result, BlueprintPortrait ___m_Portrait, BlueprintPortrait ___m_CustomPortrait)
	{
	}

	public unsafe static string GetUnitPortraitPath(BlueprintUnit blueprintUnit = null, string noBpCharname = null)
	{
		//IL_0223: Unknown result type (might be due to invalid IL or missing references)
		//IL_0228: Unknown result type (might be due to invalid IL or missing references)
		//IL_0097: Unknown result type (might be due to invalid IL or missing references)
		//IL_009c: Unknown result type (might be due to invalid IL or missing references)
		//IL_00e5: Unknown result type (might be due to invalid IL or missing references)
		//IL_00ea: Unknown result type (might be due to invalid IL or missing references)
		//IL_0644: Unknown result type (might be due to invalid IL or missing references)
		//IL_04d2: Unknown result type (might be due to invalid IL or missing references)
		//IL_0690: Unknown result type (might be due to invalid IL or missing references)
		//IL_0549: Unknown result type (might be due to invalid IL or missing references)
		//IL_050f: Unknown result type (might be due to invalid IL or missing references)
		//IL_056c: Unknown result type (might be due to invalid IL or missing references)
		//IL_05b1: Unknown result type (might be due to invalid IL or missing references)
		//IL_05d2: Unknown result type (might be due to invalid IL or missing references)
		Main.DebugLog("GetUnitPortraitPath - a");
		string npcPortraitsDirectory = Main.GetNpcPortraitsDirectory();
		string text = noBpCharname;
		if (blueprintUnit != null)
		{
			Main.DebugLog("GetUnitPortraitPath - a2 " + ((SimpleBlueprint)blueprintUnit).name);
			text = ((SimpleBlueprint)blueprintUnit).name;
		}
		Main.DebugLog("GetUnitPortraitPath - b");
		UnitEntityData val = null;
		Main.DebugLog("GetUnitPortraitPath - b2");
		string text2;
		if (Game.Instance.CurrentMode == GameModeType.Dialog && Game.Instance.DialogController != null && Game.Instance.DialogController.CurrentSpeakerBlueprint != null)
		{
			BlueprintGuid assetGuid = ((SimpleBlueprint)Game.Instance.DialogController.CurrentSpeakerBlueprint).AssetGuid;
			Main.DebugLog("GetUnitPortraitPath - c" + ((object)(*(BlueprintGuid*)(&assetGuid))/*cast due to .constrained prefix*/).ToString());
			text2 = Game.Instance.DialogController.CurrentSpeakerName.cleanCharName();
			if (text2.Length < 2)
			{
				EntityPoolEnumerator<UnitEntityData> enumerator = Game.Instance.State.Units.GetEnumerator();
				try
				{
					while (enumerator.MoveNext())
					{
						UnitEntityData current = enumerator.Current;
						if (((SimpleBlueprint)current.Blueprint).name.Equals(((SimpleBlueprint)Game.Instance.DialogController.CurrentSpeakerBlueprint).name))
						{
							val = current;
						}
					}
				}
				finally
				{
					((IDisposable)enumerator/*cast due to .constrained prefix*/).Dispose();
				}
				if (val != (UnitDescriptor)null)
				{
					text2 = val.CharacterName.cleanCharName();
					Main.DebugLog("charcterNameDirectoryName: 1 - " + text2);
				}
				else
				{
					text2 = Game.Instance.DialogController.CurrentSpeakerBlueprint.CharacterName.cleanCharName();
					Main.DebugLog("charcterNameDirectoryName: 2 - " + text2);
				}
			}
		}
		else if (Game.Instance.CurrentMode == GameModeType.Dialog && Game.Instance.DialogController != null && Game.Instance.DialogController.CurrentSpeaker != (UnitDescriptor)null)
		{
			Main.DebugLog("GetUnitPortraitPath - d");
			val = Game.Instance.DialogController.CurrentSpeaker;
			text2 = val.CharacterName.cleanCharName();
			Main.DebugLog("charcterNameDirectoryName: 3 - " + text2);
		}
		else if (blueprintUnit != null)
		{
			Main.DebugLog("GetUnitPortraitPath - e");
			EntityPoolEnumerator<UnitEntityData> enumerator = Game.Instance.State.Units.GetEnumerator();
			try
			{
				while (enumerator.MoveNext())
				{
					UnitEntityData current2 = enumerator.Current;
					if (((SimpleBlueprint)current2.Blueprint).name.Equals(((SimpleBlueprint)blueprintUnit).name))
					{
						val = current2;
					}
				}
			}
			finally
			{
				((IDisposable)enumerator/*cast due to .constrained prefix*/).Dispose();
			}
			text2 = val.CharacterName.cleanCharName();
			Main.DebugLog("charcterNameDirectoryName: 4 - " + text2);
		}
		else
		{
			Main.DebugLog("GetUnitPortraitPath - f");
			text2 = noBpCharname;
			Main.DebugLog("charcterNameDirectoryName: 5 - " + text2);
		}
		Main.DebugLog("GetUnitPortraitPath - f2");
		Main.DebugLog("GetUnit: " + text2);
		if ((text2.Equals(Main.AstyName) || text2.Equals(Main.VelhmName) || text2.Equals(Main.TranName)) && (Game.Instance.Player.Dialog.ShownCues.Contains((BlueprintCueBase)(object)ResourcesLibrary.TryGetBlueprint<BlueprintCue>("02f7b70fa8433504dbad8f817bdc4578")) || ((Object)Game.Instance.DialogController.CurrentSpeaker.View).name.ToLower().Contains("drow")))
		{
			text2 += " - Drow";
			Main.DebugLog("GetUnit (drow): " + text2);
			if (!File.Exists(Path.Combine(npcPortraitsDirectory, text2, Main.GetDefaultPortraitsDirName(), "Medium.png")))
			{
				SimpleBlueprint blueprint = ((BlueprintReferenceBase)val.Blueprint.m_Portrait).GetBlueprint();
				Main.SaveOriginals2(((BlueprintPortrait)((blueprint is BlueprintPortrait) ? blueprint : null)).Data, Path.Combine(npcPortraitsDirectory, text2));
			}
		}
		if (text2.Contains(Main.IrabethName) && Game.Instance.Player.EtudesSystem.EtudeIsStarted(ResourcesLibrary.TryGetBlueprint<BlueprintEtude>("b4f08736cf124ae4996fcef7c0a33bf1")))
		{
			Directory.CreateDirectory(Path.Combine(Main.GetNpcPortraitsDirectory(), Main.IrabethName + " - Scar"));
			text2 = Main.IrabethName + " - Scar";
			if (!File.Exists(Path.Combine(npcPortraitsDirectory, text2, Main.GetDefaultPortraitsDirName(), "Medium.png")))
			{
				Main.SaveOriginals2(ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>("72e025ceac51f2145917e0b8f5b88d8a").Data, Path.Combine(npcPortraitsDirectory, text2));
			}
		}
		Main.DebugLog("GetUnitPortraitPath x:" + text2);
		string text3 = Path.Combine(npcPortraitsDirectory, text2);
		Path.Combine(text2);
		if (val != (UnitDescriptor)null && val.Body.IsPolymorphed && val.CharacterName.cleanCharName().Equals(Main.NenioName) && ((SimpleBlueprint)val.Blueprint).name != null && ((SimpleBlueprint)val.Blueprint).name.Length > 2 && val.Blueprint.CharacterName.cleanCharName().Equals(val.CharacterName.cleanCharName()))
		{
			string path = text3;
			EntityFactComponent runtime = val.GetActivePolymorph().Runtime;
			object path2;
			if (runtime == null)
			{
				path2 = null;
			}
			else
			{
				BlueprintComponent sourceBlueprintComponent = runtime.SourceBlueprintComponent;
				path2 = ((sourceBlueprintComponent == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent.OwnerBlueprint?)).name);
			}
			if (!Directory.Exists(Path.Combine(path, (string)path2)))
			{
				string path3 = text3;
				EntityFactComponent runtime2 = val.GetActivePolymorph().Runtime;
				object path4;
				if (runtime2 == null)
				{
					path4 = null;
				}
				else
				{
					BlueprintComponent sourceBlueprintComponent2 = runtime2.SourceBlueprintComponent;
					path4 = ((sourceBlueprintComponent2 == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent2.OwnerBlueprint?)).name);
				}
				Directory.CreateDirectory(Path.Combine(path3, (string)path4));
			}
			Polymorph component = val.GetActivePolymorph().Component;
			if (((component != null) ? ((BlueprintReferenceBase)component.m_Portrait).GetBlueprint() : null) != null)
			{
				string path5 = text3;
				EntityFactComponent runtime3 = val.GetActivePolymorph().Runtime;
				object path6;
				if (runtime3 == null)
				{
					path6 = null;
				}
				else
				{
					BlueprintComponent sourceBlueprintComponent3 = runtime3.SourceBlueprintComponent;
					path6 = ((sourceBlueprintComponent3 == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent3.OwnerBlueprint?)).name);
				}
				if (!File.Exists(Path.Combine(path5, (string)path6, Main.GetDefaultPortraitsDirName(), "Medium.png")))
				{
					SimpleBlueprint blueprint2 = ((BlueprintReferenceBase)val.GetActivePolymorph().Component.m_Portrait).GetBlueprint();
					PortraitData data = ((BlueprintPortrait)((blueprint2 is BlueprintPortrait) ? blueprint2 : null)).Data;
					string path7 = text3;
					EntityFactComponent runtime4 = val.GetActivePolymorph().Runtime;
					object path8;
					if (runtime4 == null)
					{
						path8 = null;
					}
					else
					{
						BlueprintComponent sourceBlueprintComponent4 = runtime4.SourceBlueprintComponent;
						path8 = ((sourceBlueprintComponent4 == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent4.OwnerBlueprint?)).name);
					}
					Main.SaveOriginals2(data, Path.Combine(path7, (string)path8));
				}
			}
		}
		if (val != (UnitDescriptor)null && val.Body.IsPolymorphed && !val.CharacterName.cleanCharName().Equals(Main.NenioName))
		{
			string path9 = text3;
			EntityFactComponent runtime5 = val.GetActivePolymorph().Runtime;
			object path10;
			if (runtime5 == null)
			{
				path10 = null;
			}
			else
			{
				BlueprintComponent sourceBlueprintComponent5 = runtime5.SourceBlueprintComponent;
				path10 = ((sourceBlueprintComponent5 == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent5.OwnerBlueprint?)).name);
			}
			if (File.Exists(Path.Combine(path9, (string)path10, "Medium.png")))
			{
				Main.DebugLog("GetUnitPortraitPath - 1");
				string path11 = text3;
				EntityFactComponent runtime6 = val.GetActivePolymorph().Runtime;
				object path12;
				if (runtime6 == null)
				{
					path12 = null;
				}
				else
				{
					BlueprintComponent sourceBlueprintComponent6 = runtime6.SourceBlueprintComponent;
					path12 = ((sourceBlueprintComponent6 == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent6.OwnerBlueprint?)).name);
				}
				text3 = Path.Combine(path11, (string)path12);
				goto IL_0a87;
			}
		}
		if (Game.Instance.CurrentMode == GameModeType.Dialog && Game.Instance.DialogController?.Dialog != null && File.Exists(Path.Combine(npcPortraitsDirectory, text2, text, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name, "Medium.png")))
		{
			Main.DebugLog("GetUnitPortraitPath - 2");
			text3 = Path.Combine(npcPortraitsDirectory, text2, text, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name);
		}
		else if (Game.Instance.CurrentMode == GameModeType.Dialog && Game.Instance.DialogController?.Dialog != null && File.Exists(Path.Combine(npcPortraitsDirectory, text2, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name, "Medium.png")))
		{
			Main.DebugLog("GetUnitPortraitPath - 2b");
			text3 = Path.Combine(npcPortraitsDirectory, text2, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name);
		}
		else if (Directory.Exists(Path.Combine(npcPortraitsDirectory, text2, text)) && Directory.GetFiles(Path.Combine(npcPortraitsDirectory, text2, text), "*.current").Length != 0)
		{
			Main.DebugLog("GetUnitPortraitPath - 3");
			string fileNameWithoutExtension = Path.GetFileNameWithoutExtension(Directory.GetFiles(Path.Combine(npcPortraitsDirectory, text2, text), "*.current")[0]);
			Path.Combine(text2, text);
			text3 = (fileNameWithoutExtension.Equals("root") ? Path.Combine(npcPortraitsDirectory, text2, text) : Path.Combine(npcPortraitsDirectory, text2, text, fileNameWithoutExtension));
		}
		else if (Directory.Exists(Path.Combine(npcPortraitsDirectory, text2)) && Directory.GetFiles(Path.Combine(npcPortraitsDirectory, text2), "*.current").Length != 0)
		{
			Main.DebugLog("GetUnitPortraitPath - 4");
			string fileNameWithoutExtension2 = Path.GetFileNameWithoutExtension(Directory.GetFiles(Path.Combine(npcPortraitsDirectory, text2), "*.current")[0]);
			Path.Combine(text2);
			text3 = (fileNameWithoutExtension2.Equals("root") ? Path.Combine(npcPortraitsDirectory, text2) : Path.Combine(npcPortraitsDirectory, text2, fileNameWithoutExtension2));
		}
		else if (File.Exists(Path.Combine(npcPortraitsDirectory, text2, text, "Medium.png")))
		{
			Main.DebugLog("GetUnitPortraitPath - 4b");
			Path.Combine(text2, text);
			text3 = Path.Combine(npcPortraitsDirectory, text2, text);
		}
		else if (File.Exists(Path.Combine(npcPortraitsDirectory, text2, text2, "Medium.png")))
		{
			Main.DebugLog("GetUnitPortraitPath - 6");
			Path.Combine(text2, text2);
			text3 = Path.Combine(npcPortraitsDirectory, text2, text2);
		}
		else if (File.Exists(Path.Combine(npcPortraitsDirectory, text2, "Medium.png")))
		{
			Main.DebugLog("GetUnitPortraitPath - 7");
			Path.Combine(text2);
			text3 = Path.Combine(npcPortraitsDirectory, text2);
		}
		else if ((Main.settings.AutoSecret && File.Exists(Path.Combine(npcPortraitsDirectory, text2, text, Main.GetDefaultPortraitsDirName(), "Medium.png"))) || File.Exists(Path.Combine(npcPortraitsDirectory, text2, text, Main.GetDefaultPortraitsDirName(), "Fulllength.png")))
		{
			Main.DebugLog("GetUnitPortraitPath - 8");
			Path.Combine(text2, text);
			text3 = Path.Combine(npcPortraitsDirectory, text2, text, Main.GetDefaultPortraitsDirName());
		}
		else if ((Main.settings.AutoSecret && File.Exists(Path.Combine(npcPortraitsDirectory, text2, Main.GetDefaultPortraitsDirName(), "Medium.png"))) || File.Exists(Path.Combine(npcPortraitsDirectory, text2, Main.GetDefaultPortraitsDirName(), "Fulllength.png")))
		{
			Main.DebugLog("GetUnitPortraitPath - 9");
			Path.Combine(text2);
			text3 = Path.Combine(npcPortraitsDirectory, text2, Main.GetDefaultPortraitsDirName());
		}
		else
		{
			Main.DebugLog("GetUnitPortraitPath - 10");
		}
		goto IL_0a87;
		IL_0a87:
		Main.DebugLog("GetUnitPortraitPath xx:" + text2);
		return text3;
	}
}
