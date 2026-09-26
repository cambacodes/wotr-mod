using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Reflection.Emit;
using System.Runtime.CompilerServices;
using ExtensionMethods;
using Harmony12;
using Kingmaker;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Armies;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Area;
using Kingmaker.Blueprints.Classes;
using Kingmaker.Blueprints.Facts;
using Kingmaker.Blueprints.Items;
using Kingmaker.Blueprints.Items.Armors;
using Kingmaker.Blueprints.Items.Equipment;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Blueprints.Root;
using Kingmaker.BundlesLoading;
using Kingmaker.Cheats;
using Kingmaker.Controllers.Dialog;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.Enums;
using Kingmaker.GameModes;
using Kingmaker.Items;
using Kingmaker.Localization;
using Kingmaker.PubSubSystem;
using Kingmaker.ResourceLinks;
using Kingmaker.UI.Common;
using Kingmaker.UI.MVVM;
using Kingmaker.UI.MVVM._PCView.LoadingScreen;
using Kingmaker.UI.UnitSettings;
using Kingmaker.UnitLogic;
using Kingmaker.UnitLogic.ActivatableAbilities;
using Kingmaker.UnitLogic.Alignments;
using Kingmaker.UnitLogic.Buffs;
using Kingmaker.UnitLogic.Buffs.Blueprints;
using Kingmaker.UnitLogic.Mechanics;
using Kingmaker.Utility;
using Kingmaker.Visual.Particles.FxSpawnSystem;
using Owlcat.Runtime.Core.Utils;
using TMPro;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using UnityModManagerNet;

namespace CustomNpcPortraits;

public static class Main
{
	[HarmonyPriority(800)]
	[HarmonyPatch(typeof(BlueprintsCache), "Init")]
	public static class BlueprintsCache_Patch
	{
		public static bool loaded;

		private static void Postfix()
		{
			//IL_00db: Unknown result type (might be due to invalid IL or missing references)
			//IL_011b: Unknown result type (might be due to invalid IL or missing references)
			//IL_0120: Unknown result type (might be due to invalid IL or missing references)
			//IL_0136: Unknown result type (might be due to invalid IL or missing references)
			//IL_013b: Unknown result type (might be due to invalid IL or missing references)
			//IL_0187: Unknown result type (might be due to invalid IL or missing references)
			//IL_018c: Unknown result type (might be due to invalid IL or missing references)
			//IL_01a2: Unknown result type (might be due to invalid IL or missing references)
			//IL_01a7: Unknown result type (might be due to invalid IL or missing references)
			//IL_01f3: Unknown result type (might be due to invalid IL or missing references)
			//IL_01f8: Unknown result type (might be due to invalid IL or missing references)
			//IL_020e: Unknown result type (might be due to invalid IL or missing references)
			//IL_0213: Unknown result type (might be due to invalid IL or missing references)
			//IL_025f: Unknown result type (might be due to invalid IL or missing references)
			//IL_0264: Unknown result type (might be due to invalid IL or missing references)
			//IL_027a: Unknown result type (might be due to invalid IL or missing references)
			//IL_027f: Unknown result type (might be due to invalid IL or missing references)
			//IL_02cb: Unknown result type (might be due to invalid IL or missing references)
			//IL_02d0: Unknown result type (might be due to invalid IL or missing references)
			//IL_02e6: Unknown result type (might be due to invalid IL or missing references)
			//IL_02eb: Unknown result type (might be due to invalid IL or missing references)
			//IL_0337: Unknown result type (might be due to invalid IL or missing references)
			//IL_033c: Unknown result type (might be due to invalid IL or missing references)
			//IL_0352: Unknown result type (might be due to invalid IL or missing references)
			//IL_0357: Unknown result type (might be due to invalid IL or missing references)
			//IL_0452: Unknown result type (might be due to invalid IL or missing references)
			//IL_0457: Unknown result type (might be due to invalid IL or missing references)
			//IL_046d: Unknown result type (might be due to invalid IL or missing references)
			//IL_0472: Unknown result type (might be due to invalid IL or missing references)
			//IL_04be: Unknown result type (might be due to invalid IL or missing references)
			//IL_04c3: Unknown result type (might be due to invalid IL or missing references)
			//IL_04d9: Unknown result type (might be due to invalid IL or missing references)
			//IL_04de: Unknown result type (might be due to invalid IL or missing references)
			//IL_052a: Unknown result type (might be due to invalid IL or missing references)
			//IL_052f: Unknown result type (might be due to invalid IL or missing references)
			//IL_0545: Unknown result type (might be due to invalid IL or missing references)
			//IL_054a: Unknown result type (might be due to invalid IL or missing references)
			//IL_0596: Unknown result type (might be due to invalid IL or missing references)
			//IL_059b: Unknown result type (might be due to invalid IL or missing references)
			//IL_05b1: Unknown result type (might be due to invalid IL or missing references)
			//IL_05b6: Unknown result type (might be due to invalid IL or missing references)
			//IL_0602: Unknown result type (might be due to invalid IL or missing references)
			//IL_0607: Unknown result type (might be due to invalid IL or missing references)
			//IL_061d: Unknown result type (might be due to invalid IL or missing references)
			//IL_0622: Unknown result type (might be due to invalid IL or missing references)
			//IL_066e: Unknown result type (might be due to invalid IL or missing references)
			//IL_0673: Unknown result type (might be due to invalid IL or missing references)
			//IL_0689: Unknown result type (might be due to invalid IL or missing references)
			//IL_068e: Unknown result type (might be due to invalid IL or missing references)
			//IL_06da: Unknown result type (might be due to invalid IL or missing references)
			//IL_06df: Unknown result type (might be due to invalid IL or missing references)
			//IL_06f5: Unknown result type (might be due to invalid IL or missing references)
			//IL_06fa: Unknown result type (might be due to invalid IL or missing references)
			//IL_0746: Unknown result type (might be due to invalid IL or missing references)
			//IL_074b: Unknown result type (might be due to invalid IL or missing references)
			//IL_0761: Unknown result type (might be due to invalid IL or missing references)
			//IL_0766: Unknown result type (might be due to invalid IL or missing references)
			//IL_07b2: Unknown result type (might be due to invalid IL or missing references)
			//IL_07b7: Unknown result type (might be due to invalid IL or missing references)
			//IL_07cd: Unknown result type (might be due to invalid IL or missing references)
			//IL_07d2: Unknown result type (might be due to invalid IL or missing references)
			//IL_081e: Unknown result type (might be due to invalid IL or missing references)
			//IL_0823: Unknown result type (might be due to invalid IL or missing references)
			//IL_0839: Unknown result type (might be due to invalid IL or missing references)
			//IL_083e: Unknown result type (might be due to invalid IL or missing references)
			//IL_088a: Unknown result type (might be due to invalid IL or missing references)
			//IL_088f: Unknown result type (might be due to invalid IL or missing references)
			//IL_08a5: Unknown result type (might be due to invalid IL or missing references)
			//IL_08aa: Unknown result type (might be due to invalid IL or missing references)
			//IL_08f6: Unknown result type (might be due to invalid IL or missing references)
			//IL_08fb: Unknown result type (might be due to invalid IL or missing references)
			//IL_0911: Unknown result type (might be due to invalid IL or missing references)
			//IL_0916: Unknown result type (might be due to invalid IL or missing references)
			//IL_0962: Unknown result type (might be due to invalid IL or missing references)
			//IL_0967: Unknown result type (might be due to invalid IL or missing references)
			//IL_097d: Unknown result type (might be due to invalid IL or missing references)
			//IL_0982: Unknown result type (might be due to invalid IL or missing references)
			//IL_09ce: Unknown result type (might be due to invalid IL or missing references)
			//IL_09d3: Unknown result type (might be due to invalid IL or missing references)
			//IL_09e9: Unknown result type (might be due to invalid IL or missing references)
			//IL_09ee: Unknown result type (might be due to invalid IL or missing references)
			//IL_0a3a: Unknown result type (might be due to invalid IL or missing references)
			//IL_0a3f: Unknown result type (might be due to invalid IL or missing references)
			//IL_0a55: Unknown result type (might be due to invalid IL or missing references)
			//IL_0a5a: Unknown result type (might be due to invalid IL or missing references)
			//IL_0aa6: Unknown result type (might be due to invalid IL or missing references)
			//IL_0aab: Unknown result type (might be due to invalid IL or missing references)
			//IL_0ac1: Unknown result type (might be due to invalid IL or missing references)
			//IL_0ac6: Unknown result type (might be due to invalid IL or missing references)
			//IL_0c0e: Unknown result type (might be due to invalid IL or missing references)
			//IL_0c13: Unknown result type (might be due to invalid IL or missing references)
			//IL_0c46: Unknown result type (might be due to invalid IL or missing references)
			//IL_0c4b: Unknown result type (might be due to invalid IL or missing references)
			//IL_0c7e: Unknown result type (might be due to invalid IL or missing references)
			//IL_0c83: Unknown result type (might be due to invalid IL or missing references)
			//IL_0cb6: Unknown result type (might be due to invalid IL or missing references)
			//IL_0cbb: Unknown result type (might be due to invalid IL or missing references)
			//IL_0cee: Unknown result type (might be due to invalid IL or missing references)
			//IL_0cf3: Unknown result type (might be due to invalid IL or missing references)
			//IL_0d26: Unknown result type (might be due to invalid IL or missing references)
			//IL_0d2b: Unknown result type (might be due to invalid IL or missing references)
			//IL_0d5e: Unknown result type (might be due to invalid IL or missing references)
			//IL_0d63: Unknown result type (might be due to invalid IL or missing references)
			//IL_11f4: Unknown result type (might be due to invalid IL or missing references)
			//IL_11fb: Expected O, but got Unknown
			if (loaded)
			{
				return;
			}
			loaded = true;
			string fullPath = Path.GetFullPath(Path.Combine(CustomPortraitsManager.PortraitsRootFolderPath, "..\\"));
			fullPath = Path.Combine(fullPath, "Portraits");
			Directory.CreateDirectory(fullPath);
			DirectoryInfo target = new DirectoryInfo(fullPath);
			CopyFilesRecursively(new DirectoryInfo(Path.Combine(UnityModManager.modsPath, modId, "Portraits")), target);
			BlueprintPortrait val = ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>("9412ffb857efa074eb8e4945c8b94de4");
			SmallPortraitInjector.Replacements[val.Data] = BlueprintRoot.Instance.CharGen.BasePortraitSmall;
			BlueprintPortrait val2 = ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>("9fe4f89ecf15b874db9d1d2bf3ef33d2");
			Directory.CreateDirectory(Path.Combine(UnityModManager.modsPath, modId, ((SimpleBlueprint)val2).name));
			SmallPortraitInjector.Replacements[val2.Data] = PortraitLoader.Image2Sprite.Create(Path.Combine(UnityModManager.modsPath, modId, ((SimpleBlueprint)val2).name, "Small.png"), new Vector2Int(256, 336), (TextureFormat)14);
			Directory.CreateDirectory(GetCompanionPortraitsDirectory());
			GetNpcPortraitsDirectory();
			GetArmyPortraitsDirectory();
			BlueprintUnit val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("1b893f7cf2b150e4f8bc2b3c389ba71d");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			NenioName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("a352873d37ec6c54c9fa8f6da3a6b3e1");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			ArueName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("ea8034769ab7d584e97b5227cbc03296");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			FinneanName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("7ece3afabe2b6f343b17d1eaa409d273");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			CiarName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("e46927657a79db64ea30758db3f42bb9");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			GalfreyName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("766435873b1361c4287c351de194e5f9");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			WoljifName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			IrabethName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("d1e567736abf23943b9f041ba7a0bc23").LocalizedName.String);
			PillarName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("a556fbfa2e0c59e4dad4da70b2e1b1d6").LocalizedName.String);
			AstyName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("d8e2475977bd87b439c4bba8f5f55949").LocalizedName.String);
			TranName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("c35607fd0f8064f42b4d71f7eb50e96c").LocalizedName.String);
			VelhmName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("f9c01a9515cd1f347800685ddbfbcc41").LocalizedName.String);
			EnemyLeaderName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintArmyLeader>("02b369f0cbaa8f14d928446765402db4").LeaderName);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("cb29621d99b902e4da6f5d232352fbda");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			LannName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("2779754eecffd044fbd4842dba55312c");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			EmberName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("942862a48f1644ae85ac5e3c9deb720c");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			PentaName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("54be53f0b35bf3c4592a97ae335fe765");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			SeelahName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("096fc4a96d675bb45a0396bcaa7aa993");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			DaeranName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("0d37024170b172346b3769df92a971f5");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			RegillName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("561036c882a640089b1d42f03ebe3a6c");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			SendriName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("42f0d5ec3dc844feb44b04507a7c1bfc");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			UlbrigName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("0bb1c03b9f7bbcf42bb74478af2c6258");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			TreverName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("ae766624c03058440a036de90a7f2009");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			WenduagName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("3e0014e4be454482a2797fd81123d7b4");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			RekarthName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("f72bb7c48bb3e45458f866045448fb58");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			GreyborName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("397b090721c41044ea3220445300e1b8");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			CamelliaName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("6b1f599497f5cfa42853d095bda6dafd");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			DelamereName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("e551850403d61eb48bb2de010d12c894");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			KestoglyrName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			val3 = ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("1cbbbb892f93c3d439f8417ad7cbb6aa");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), ResourcesLibrary.TryGetBlueprint<BlueprintPortrait>(((object)((BlueprintReferenceBase)val3.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString()).Data);
			SosielName = LocalizedString.op_Implicit(val3.LocalizedName.String);
			companions = new List<string>
			{
				ArueName, CiarName, NenioName, GalfreyName, StauntonName, WoljifName, LannName, EmberName, PentaName, SeelahName,
				DaeranName, RegillName, SendriName, UlbrigName, TreverName, WenduagName, RekarthName, GreyborName, CamelliaName, DelamereName,
				KestoglyrName, SosielName
			};
			BlueprintPortrait blueprintByGuid = Utilities.GetBlueprintByGuid<BlueprintPortrait>("a6e4ff25a8da46a44a24ecc5da296073");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)blueprintByGuid)).Guid/*cast due to .constrained prefix*/).ToString(), blueprintByGuid.Data);
			blueprintByGuid = Utilities.GetBlueprintByGuid<BlueprintPortrait>("484588d56f2c2894ab6d48b91509f5e3");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)blueprintByGuid)).Guid/*cast due to .constrained prefix*/).ToString(), blueprintByGuid.Data);
			blueprintByGuid = Utilities.GetBlueprintByGuid<BlueprintPortrait>("767456b1656ca064dadac544d39d7e40");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)blueprintByGuid)).Guid/*cast due to .constrained prefix*/).ToString(), blueprintByGuid.Data);
			blueprintByGuid = Utilities.GetBlueprintByGuid<BlueprintPortrait>("4e8dfb75015d356469b976145c851087");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)blueprintByGuid)).Guid/*cast due to .constrained prefix*/).ToString(), blueprintByGuid.Data);
			blueprintByGuid = Utilities.GetBlueprintByGuid<BlueprintPortrait>("f2bd5a94ade889444921b4a74b9e34a9");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)blueprintByGuid)).Guid/*cast due to .constrained prefix*/).ToString(), blueprintByGuid.Data);
			blueprintByGuid = Utilities.GetBlueprintByGuid<BlueprintPortrait>("f4bbe08217bcaa54c91fe73bcea70ede");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)blueprintByGuid)).Guid/*cast due to .constrained prefix*/).ToString(), blueprintByGuid.Data);
			blueprintByGuid = Utilities.GetBlueprintByGuid<BlueprintPortrait>("222c3bcbf7e342338416c0e8bdc75109");
			CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)blueprintByGuid)).Guid/*cast due to .constrained prefix*/).ToString(), blueprintByGuid.Data);
			foreach (string animalCompPortrait in animalCompPortraitList)
			{
				blueprintByGuid = Utilities.GetBlueprintByGuid<BlueprintPortrait>(animalCompPortrait);
				CompanionPortraitBackups.Add(animalCompPortrait, blueprintByGuid.Data);
			}
			DebugLog("Trying to run popUnitNames");
			SafeLoad(popUnitNames, "popUnitNames");
			settings = ModSettings.Load<Settings>(ModEntry);
			if (!settings.isCleaned)
			{
				Directory.CreateDirectory(Path.GetFullPath(CustomPortraitsManager.PortraitsRootFolderPath));
				string[] files = Directory.GetFiles(GetCompanionPortraitsDirectory(), GetDefaultPortraitsDirName() + ".current", SearchOption.AllDirectories);
				for (int i = 0; i < files.Length; i++)
				{
					File.Delete(files[i]);
				}
				files = Directory.GetFiles(GetNpcPortraitsDirectory(), GetDefaultPortraitsDirName() + ".current", SearchOption.AllDirectories);
				for (int i = 0; i < files.Length; i++)
				{
					File.Delete(files[i]);
				}
				files = Directory.GetFiles(GetArmyPortraitsDirectory(), GetDefaultPortraitsDirName() + ".current", SearchOption.AllDirectories);
				for (int i = 0; i < files.Length; i++)
				{
					File.Delete(files[i]);
				}
				settings.isCleaned = true;
				((ModSettings)settings).Save(ModEntry);
			}
			if (!settings.isCleaned2)
			{
				Directory.CreateDirectory(Path.GetFullPath(CustomPortraitsManager.PortraitsRootFolderPath));
				string[] files = Directory.GetDirectories(GetCompanionPortraitsDirectory(), "Game Default Portraits", SearchOption.AllDirectories);
				foreach (string text in files)
				{
					if (!Directory.Exists(Path.Combine(Directory.GetParent(text).FullName, GetDefaultPortraitsDirName())))
					{
						Directory.Move(text, Path.Combine(Directory.GetParent(text).FullName, GetDefaultPortraitsDirName()));
						continue;
					}
					Directory.Delete(Path.Combine(Directory.GetParent(text).FullName, GetDefaultPortraitsDirName()), recursive: true);
					Directory.Move(text, Path.Combine(Directory.GetParent(text).FullName, GetDefaultPortraitsDirName()));
				}
				files = Directory.GetDirectories(GetNpcPortraitsDirectory(), "Game Default Portraits", SearchOption.AllDirectories);
				foreach (string text2 in files)
				{
					if (!Directory.Exists(Path.Combine(Directory.GetParent(text2).FullName, GetDefaultPortraitsDirName())))
					{
						Directory.Move(text2, Path.Combine(Directory.GetParent(text2).FullName, GetDefaultPortraitsDirName()));
						continue;
					}
					Directory.Delete(Path.Combine(Directory.GetParent(text2).FullName, GetDefaultPortraitsDirName()), recursive: true);
					Directory.Move(text2, Path.Combine(Directory.GetParent(text2).FullName, GetDefaultPortraitsDirName()));
				}
				files = Directory.GetDirectories(GetArmyPortraitsDirectory(), "Game Default Portraits", SearchOption.AllDirectories);
				foreach (string text3 in files)
				{
					if (!Directory.Exists(Path.Combine(Directory.GetParent(text3).FullName, GetDefaultPortraitsDirName())))
					{
						Directory.Move(text3, Path.Combine(Directory.GetParent(text3).FullName, GetDefaultPortraitsDirName()));
						continue;
					}
					Directory.Delete(Path.Combine(Directory.GetParent(text3).FullName, GetDefaultPortraitsDirName()), recursive: true);
					Directory.Move(text3, Path.Combine(Directory.GetParent(text3).FullName, GetDefaultPortraitsDirName()));
				}
				settings.isCleaned2 = true;
				((ModSettings)settings).Save(ModEntry);
			}
			Polymorph val4 = ((BlueprintScriptableObject)ResourcesLibrary.TryGetBlueprint<BlueprintBuff>("a13e2e71485901045b1722824019d6f5")).ComponentsArray.OfType<Polymorph>().FirstOrDefault();
			if (val4 == null)
			{
				return;
			}
			string companionPortraitDirPrefix = GetCompanionPortraitDirPrefix();
			string companionPortraitsDirectory = GetCompanionPortraitsDirectory();
			string path = companionPortraitDirPrefix + NenioName;
			string text4 = Path.Combine(companionPortraitsDirectory, path);
			if (!Directory.Exists(text4))
			{
				return;
			}
			if (Directory.GetFiles(text4, "*.current").Length != 0)
			{
				fullPath = Path.GetFileNameWithoutExtension(Directory.GetFiles(text4, "*.current")[0]);
				if (!fullPath.Equals("root"))
				{
					text4 = Path.Combine(companionPortraitsDirectory, path, fullPath);
				}
			}
			else if (!File.Exists(Path.Combine(text4, "Medium.png")) && File.Exists(Path.Combine(text4, GetDefaultPortraitsDirName(), "Medium.png")))
			{
				text4 = Path.Combine(text4, GetDefaultPortraitsDirName());
			}
			if (File.Exists(Path.Combine(text4, "Medium.png")))
			{
				PortraitData data = new PortraitData(Path.Combine(text4));
				BlueprintPortrait val5 = BlueprintReference<BlueprintPortrait>.op_Implicit((BlueprintReference<BlueprintPortrait>)(object)val4.m_Portrait);
				val5.Data = data;
				val4.m_Portrait = BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)val5);
			}
		}

		public static void popUnitNames()
		{
			//IL_0194: Unknown result type (might be due to invalid IL or missing references)
			//IL_0199: Unknown result type (might be due to invalid IL or missing references)
			//IL_01bb: Unknown result type (might be due to invalid IL or missing references)
			//IL_01c0: Unknown result type (might be due to invalid IL or missing references)
			//IL_00a3: Unknown result type (might be due to invalid IL or missing references)
			//IL_00aa: Invalid comparison between Unknown and I4
			//IL_00ae: Unknown result type (might be due to invalid IL or missing references)
			//IL_00b5: Invalid comparison between Unknown and I4
			BlueprintList allBlueprints = Utilities.GetAllBlueprints();
			swarmAnswers = 0;
			int num = 0;
			int num2 = 0;
			foreach (Entry entry in allBlueprints.Entries)
			{
				try
				{
					if (settings.SwarmRiddance && entry.Type.Name.Equals("BlueprintAnswersList") && entry.Guid != null)
					{
						BlueprintAnswersList val = ResourcesLibrary.TryGetBlueprint<BlueprintAnswersList>(entry.Guid);
						if (val != null)
						{
							List<BlueprintAnswerBaseReference> list = new List<BlueprintAnswerBaseReference>();
							foreach (BlueprintAnswerBaseReference answer in val.Answers)
							{
								SimpleBlueprint blueprint = ((BlueprintReferenceBase)answer).GetBlueprint();
								BlueprintAnswerBase val2 = (BlueprintAnswerBase)(object)((blueprint is BlueprintAnswerBase) ? blueprint : null);
								if (val2 != null && ((int)val2.MythicRequirement == 9 || (int)val2.MythicRequirement == 18) && !list.Contains(answer))
								{
									list.Add(answer);
									swarmAnswers++;
								}
							}
							if (list.Count() > 0 && val.Answers.Count() > 0)
							{
								foreach (BlueprintAnswerBaseReference item in list)
								{
									val.Answers.Remove(item);
								}
							}
						}
					}
					if (entry.Type.Name.Equals("BlueprintBuff"))
					{
						Polymorph obj = ((BlueprintScriptableObject)Utilities.GetBlueprintByGuid<BlueprintBuff>(entry.Guid)).ComponentsArray.OfType<Polymorph>().FirstOrDefault();
						BlueprintPortrait val3 = ((obj != null) ? obj.Portrait : null);
						if (val3 != null && !CompanionPortraitBackups.ContainsKey(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)val3)).Guid/*cast due to .constrained prefix*/).ToString()))
						{
							CompanionPortraitBackups.Add(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)val3)).Guid/*cast due to .constrained prefix*/).ToString(), val3.Data);
						}
					}
					if (!entry.Type.Name.Equals("BlueprintCue") || entry == null || entry.Guid == null)
					{
						continue;
					}
					BlueprintCue blueprintByGuid = Utilities.GetBlueprintByGuid<BlueprintCue>(entry.Guid);
					if (blueprintByGuid != null && blueprintByGuid.Speaker != null && blueprintByGuid.Speaker.Blueprint != null && !Utils.IsNullOrEmpty(((SimpleBlueprint)blueprintByGuid.Speaker.Blueprint).name) && !Utils.IsNullOrEmpty(blueprintByGuid.Speaker.Blueprint.CharacterName.cleanCharName()) && !unitNames.Contains(((SimpleBlueprint)blueprintByGuid.Speaker.Blueprint).name) && !companions.Contains(blueprintByGuid.Speaker.Blueprint.CharacterName.cleanCharName()) && !blueprintByGuid.Speaker.Blueprint.IsCompanion)
					{
						string name = ((SimpleBlueprint)blueprintByGuid.Speaker.Blueprint).name;
						BlueprintUnit blueprint2 = blueprintByGuid.Speaker.Blueprint;
						if (name != ((blueprint2 != null) ? blueprint2.CharacterName.cleanCharName() : null))
						{
							DebugLog(((SimpleBlueprint)blueprintByGuid.Speaker.Blueprint).name);
							unitNames.Add(((SimpleBlueprint)blueprintByGuid.Speaker.Blueprint).name);
							num++;
						}
					}
					if (blueprintByGuid != null && blueprintByGuid.Listener != null && !Utils.IsNullOrEmpty(((SimpleBlueprint)blueprintByGuid.Listener).name) && !Utils.IsNullOrEmpty(blueprintByGuid.Listener.CharacterName.cleanCharName()) && !unitNames.Contains(((SimpleBlueprint)blueprintByGuid.Listener).name) && !companions.Contains(blueprintByGuid.Listener.CharacterName.cleanCharName()) && !blueprintByGuid.Listener.IsCompanion)
					{
						string name2 = ((SimpleBlueprint)blueprintByGuid.Listener).name;
						BlueprintUnit listener = blueprintByGuid.Listener;
						if (name2 != ((listener != null) ? listener.CharacterName.cleanCharName() : null))
						{
							DebugLog(((SimpleBlueprint)blueprintByGuid.Listener).name);
							unitNames.Add(((SimpleBlueprint)blueprintByGuid.Listener).name);
							num++;
						}
					}
				}
				catch (Exception ex)
				{
					DebugError(ex);
					num2++;
				}
			}
			DebugLog("Found " + num + " units partaking in dialogs. (" + num2 + " are null?)");
		}
	}

	[HarmonyPatch(typeof(LoadingScreenPCView), "SetupLoadingArea")]
	public static class LoadingScreenPCView_Patch
	{
		private static bool Prefix(LoadingScreenPCView __instance, BlueprintArea area, GameObject ___m_MapContainer, Image ___m_Picture, TextMeshProUGUI ___m_CharacterNameText, TextMeshProUGUI ___m_CharacterDescriptionText, Image ___m_CharacterPortrait, Sprite ___m_PrologueCaves1Sprite)
		{
			//IL_00b6: Unknown result type (might be due to invalid IL or missing references)
			//IL_00bb: Unknown result type (might be due to invalid IL or missing references)
			//IL_00f4: Unknown result type (might be due to invalid IL or missing references)
			//IL_00fc: Unknown result type (might be due to invalid IL or missing references)
			___m_MapContainer.SetActive(area?.IsGlobalMap ?? false);
			((Component)___m_Picture).gameObject.SetActive(area == null || !area.IsGlobalMap);
			if (area == null)
			{
				___m_Picture.sprite = UIRoot.Instance.BlueprintLoadingScreenSpriteList.GetLoadingScreen((BlueprintArea)null, (List<SpriteLink>)null);
				return false;
			}
			if (!area.IsGlobalMap)
			{
				___m_Picture.sprite = UIRoot.Instance.BlueprintLoadingScreenSpriteList.GetLoadingScreen(area, (List<SpriteLink>)null);
			}
			else
			{
				List<UnitEntityData> list = TempListExtension.ToTempList<UnitEntityData>(Game.Instance.Player.Party.Where((UnitEntityData rc) => !rc.IsPet && !UnitHelper.IsCustomCompanion(rc) && !rc.IsMainCharacter));
				if (!LinqExtensions.Empty<UnitEntityData>((IList<UnitEntityData>)list))
				{
					UnitReference val = UnitReference.op_Implicit(LinqExtensions.Random<UnitEntityData>((IList<UnitEntityData>)list));
					BlueprintCompanionStory val2 = Game.Instance.Player.CompanionStories.Get(((UnitReference)(ref val)).Value).LastOrDefault();
					string text = ((UnitReference)(ref val)).Value.CharacterName.cleanCharName();
					((TMP_Text)___m_CharacterNameText).text = UIUtility.GetSaberBookFormat(text, default(Color), 140, (Material)null, 0f);
					LocalizedString val3 = val2?.Description;
					LocalizedString val4 = val3;
					((TMP_Text)___m_CharacterDescriptionText).text = ((val4 != null) ? LocalizedString.op_Implicit(val4) : string.Empty);
					___m_CharacterPortrait.sprite = ((UnitReference)(ref val)).Value.Portrait.FullLengthPortrait;
				}
				else
				{
					___m_MapContainer.SetActive(false);
					((Component)___m_Picture).gameObject.SetActive(true);
					___m_Picture.sprite = UIRoot.Instance.BlueprintLoadingScreenSpriteList.GetLoadingScreen((BlueprintArea)null, (List<SpriteLink>)null);
				}
			}
			if ((Object)(object)___m_Picture.sprite == (Object)null && ((SimpleBlueprint)area).name == "Prologue_Caves_1")
			{
				___m_Picture.sprite = ___m_PrologueCaves1Sprite;
			}
			if (((Component)___m_Picture).gameObject.activeInHierarchy && (Object)(object)___m_Picture.sprite == (Object)null)
			{
				((Component)___m_Picture).gameObject.SetActive(false);
			}
			return false;
		}
	}

	[HarmonyPatch(typeof(PortraitData), "get_PetEyePortrait")]
	public static class EyePortraitInjector
	{
		public static Dictionary<PortraitData, Sprite> Replacements = new Dictionary<PortraitData, Sprite>();

		public static bool Prefix(PortraitData __instance, ref Sprite __result)
		{
			if (Replacements.TryGetValue(__instance, out __result))
			{
				return false;
			}
			return true;
		}
	}

	[HarmonyPatch(typeof(PortraitData), "get_SmallPortrait")]
	public static class SmallPortraitInjector
	{
		public static Dictionary<PortraitData, Sprite> Replacements = new Dictionary<PortraitData, Sprite>();

		public static bool Prefix(PortraitData __instance, ref Sprite __result)
		{
			if (Replacements.TryGetValue(__instance, out __result))
			{
				return false;
			}
			return true;
		}
	}

	public static string modId;

	public static Dictionary<string, PortraitData> CompanionPortraitBackups = new Dictionary<string, PortraitData>();

	public static bool GalfreyChurchDoubled = false;

	public static List<string> animalCompList = new List<string>
	{
		"GhostRiderAnimalCompanionUnitHorse", "BlizzardServantUnit", "AnimalCompanionUnitArmoredPony_ForNPC", "AnimalCompanionUnitBear", "AnimalCompanionUnitBoar", "AnimalCompanionUnitBoar_FoolKingMounted", "AnimalCompanionUnitCentipede", "AnimalCompanionUnitDog", "AnimalCompanionUnitElk", "AnimalCompanionUnitHorse",
		"AnimalCompanionUnitHorse_PreorderBonus", "AnimalCompanionUnitLeopard", "AnimalCompanionUnitMammoth", "AnimalCompanionUnitMonitor", "AnimalCompanionUnitSmilodon", "AnimalCompanionUnitSmilodon_PreorderBonus", "AnimalCompanionUnitTriceratops", "AnimalCompanionUnitTriceratops_PreorderBonus", "AnimalCompanionUnitVelociraptor", "AnimalCompanionUnitWolf",
		"MythicLichSkeletonArcherUnit", "MythicLichSkeletonDualWielderUnit", "MythicLichSkeletonTankUnit", "MythicLichSkeletonTwoHandedUnit", "SableMarineAnimalCompanionHippogriff", "NightHagCompanionUnit", "TriceratopsStatuetteUnit", "AzataDragonUnit"
	};

	public static List<string> animalCompPortraitList = new List<string>
	{
		"0897cfee366802b4c827b31b29e0f03f", "1f5bfefa49a8aa2449ad94b1f4f61788", "26b6a7f56b5242d5879b18d5d3d4afe7", "29cdd4313a408584da3813e23c4891fc", "507f0248c7a4e2b4bada154861c374b1", "624c584aae8f4805ba25a68ed84957f5", "6aa66cece6bf87248a0188b934179200", "6cefce842683a634297e2fe8e8db2026", "70c86316f0cd4ea4f98987079a4a5e60", "80bec6f617784a4d8e49fc26e69d787e",
		"8c955a0f5c93e7a40b5c7563b5b321d5", "9d8a2cddc5550da4490ab5b692e0bd98", "af3fe1a30c9e2844eb9af74fca39f322", "b3712a85095646141b2d43129d19983e", "d15759344bba4738a63d8ddc73614b41", "eb4705aeb0e846e2bd644ff279d4bf4e", "eeb495746940435185a04ab3f4c24281", "f03d5a6461a8437facfa77f8c276c45b", "f8f62a718fbcac343a50d495f7d12a29"
	};

	public static Dictionary<string, string> companionIds = new Dictionary<string, string>();

	public static bool isPCNameFcked = false;

	private static GUIStyle boldStyle = new GUIStyle();

	private static GUIStyle boldStyle2 = new GUIStyle();

	private static GUILayoutOption[] defSize = (GUILayoutOption[])(object)new GUILayoutOption[2]
	{
		GUILayout.Width(200f),
		GUILayout.Height(20f)
	};

	private static List<string> allCompNames = new List<string>();

	public static string charcterNameDirectoryName;

	public static string CurrentSpeakerName;

	public static string CurrentSpeakerBlueprintName;

	public static string CompanionPortraitPath;

	public static string NpcPortraitPath;

	public static string portraitDirectorySubPath;

	public static string portraitDirectorySubDialogPath;

	public static bool dirExist1 = false;

	public static bool dirExist2 = false;

	public static bool dirExist3 = false;

	public static bool dirExist4 = false;

	public static bool dirExist5 = false;

	public static bool dirExist6 = false;

	public static bool dirExist7 = false;

	public static bool showNamings = false;

	public static bool QueenOld = false;

	public static string pickedUpDir = "";

	public static int swarmAnswers = 0;

	public static bool swarmCleanRunning = false;

	public static List<string> units = new List<string>
	{
		"CitizenFemale1", "CitizenFemale6", "CitizenMale1", "CitizenMale2", "CommonerFemale01", "CR0_GundrunPeasantMale", "CR4_Bandit_Human_NecromancerSosielq0", "Elf_Citizen_Female", "Vilenia", "CR3_Crusader_Human_PaladinMelee_Male",
		"CR7_Crusader_Human_PaladinMelee_cap", "CrusadeSoldier", "CrusadeSoldier2", "CrusadeSoldier3F", "CrusadeSoldierNearIrabeth", "Megidiah_Retinue_commoner1", "AeonQ3_CapitalGuard_01_Viram", "AeonQ3_CapitalGuard_02_Erwart", "CR0_Sarcorian_Guard_Male", "CR0_Sarcorian_Guard_Male2",
		"Gorvo", "Kermel", "Lellan", "Nexus_PleasureSlaveMale", "SlaveHorgus", "CR1_Crusader_Human_Recruit_Melee_Male", "Recruit_Speaker_1", "Recruit_Speaker_2", "StitchHalflingVIsionByAreelu", "ColyphyrSlave_FemaleAzata",
		"MysticSlave"
	};

	public static int index = 0;

	public static int index2 = 80;

	public static string NenioName = "Nenio";

	public static string ArueName = "Arueshalae";

	public static string FinneanName = "Finnean the Talking Weapon";

	public static string CiarName = "Ciar";

	public static string WoljifName = "Woljif";

	public static string GalfreyName = "Queen Galfrey";

	public static string StauntonName = "Staunton Vhane";

	public static string IrabethName = "Irabeth";

	public static string AstyName = "Asty";

	public static string TranName = "Tran";

	public static string VelhmName = "Velhm";

	public static string LannName = "Lann";

	public static string EmberName = "Ember";

	public static string PentaName = "Penta";

	public static string SeelahName = "Seelah";

	public static string DaeranName = "Daeran";

	public static string RegillName = "Regill";

	public static string SendriName = "Sendri";

	public static string UlbrigName = "Ulbrig";

	public static string TreverName = "Trever";

	public static string WenduagName = "Wenduag";

	public static string RekarthName = "Rekarth";

	public static string GreyborName = "Greybor";

	public static string CamelliaName = "Camellia";

	public static string DelamereName = "Delamere";

	public static string KestoglyrName = "Kestoglyr";

	public static string SosielName = "Sosiel";

	public static string PillarName = "The Pillar of Skulls";

	public static string AethyliaName = "Aethylia";

	public static string EnemyLeaderName = "Enemy Leader";

	public static ModLogger Logger;

	public static List<BlueprintBuff> buffs = new List<BlueprintBuff>();

	public static bool dollRoomxtraFxBrightness = false;

	public static Dictionary<string, IFxHandle> fxHandles = new Dictionary<string, IFxHandle>();

	public static Settings settings;

	public static List<string> unitNames = new List<string>();

	public static BlueprintList blueprintList = new BlueprintList
	{
		Entries = new List<Entry>()
	};

	public static ModEntry ModEntry;

	public static bool areaLoaded = false;

	public static int portraitCounter = 0;

	public static int failCounter = 0;

	public static GameModeType prevMode = GameModeType.None;

	public static bool savedNpc = false;

	public static bool companion = false;

	public static bool savedComp = false;

	public static int i = -1;

	public static int j = -1;

	public static string npcDirlabel = "";

	public static string npcSubDirlabel = "";

	public static string compDirlabel = "";

	public static int k = 400;

	public static BlueprintBuff lastbb;

	public static IFxHandle ifxh;

	public static string npcCycle = "";

	public static string npcSubCycle = "";

	public static string compCycle = "";

	private static bool isDialog = false;

	private static bool isLoadedGame = false;

	private static bool showExperimental = false;

	private static bool showExtra = false;

	public static bool enabled;

	public static string smallName = "Small.png";

	public static string mediumName = "Medium.png";

	public static string fullName = "Fulllength.png";

	public static string[] PortraitFileNames = new string[3] { smallName, mediumName, fullName };

	public static ModLogger logger;

	private static readonly List<string> okLoading = new List<string>();

	private static readonly List<string> failedLoading = new List<string>();

	private static HarmonyInstance harmonyInstance;

	private static readonly Dictionary<Type, bool> typesPatched = new Dictionary<Type, bool>();

	private static readonly List<string> failedPatches = new List<string>();

	private static readonly List<string> okPatches = new List<string>();

	public static List<string> companions;

	public static bool isSetPortrait = false;

	public static bool pauseGetPortraitsafe = false;

	public static Sprite eye;

	public static bool Load(ModEntry modEntry)
	{
		ModEntry = modEntry;
		modId = modEntry.Info.Id;
		logger = modEntry.Logger;
		harmonyInstance = HarmonyInstance.Create(modEntry.Info.Id);
		settings = ModSettings.Load<Settings>(modEntry);
		modEntry.OnGUI = OnGUI;
		modEntry.OnShowGUI = OnShowGUI;
		modEntry.OnToggle = OnToggle;
		modEntry.OnSaveGUI = OnSaveGUI;
		modEntry.OnHideGUI = OnHideGUI;
		if (!ApplyPatch(typeof(GetPortrait_Patch), "GetPortrait_Patch"))
		{
			throw Error("Failed to patch GetPortrait");
		}
		if (!ApplyPatch(typeof(GetPortraitSafe_Patch), "GetPortraitSafe_Patch"))
		{
			throw Error("Failed to patch GetPortraitSafe");
		}
		if (!ApplyPatch(typeof(GetPortraitSafeGeneral_Patch), "GetPortraitSafeGeneral_Patch"))
		{
			throw Error("Failed to patch GetPortraitSafeGeneral");
		}
		if (!ApplyPatch(typeof(GameMode_OnActivate_Patch), "GameMode_OnActivate_Patch"))
		{
			throw Error("Failed to patch GameMode_OnActivate");
		}
		if (!ApplyPatch(typeof(Player_OnAreaLoaded_Patch), "Player_OnAreaLoaded_Patch"))
		{
			throw Error("Failed to patch Player_OnAreaLoaded");
		}
		if (!ApplyPatch(typeof(Player_AddCompanion_Patch), "Player_AddCompanion_Patch"))
		{
			throw Error("Failed to patch Player_AddCompanion");
		}
		if (!ApplyPatch(typeof(InitiativeTrackerUnitVM_Get_Portrait_Patch), "InitiativeTrackerUnitVM_Get_Portrait_Patch"))
		{
			throw Error("Failed to patch InitiativeTrackerUnitVM_Get_Portrait");
		}
		if (!ApplyPatch(typeof(BlueprintsCache_Patch), "BlueprintsCache_Patch"))
		{
			throw Error("Failed to patch BlueprintsCache");
		}
		if (!ApplyPatch(typeof(LoadingScreenPCView_Patch), "LoadingScreenPCView_Patch"))
		{
			throw Error("Failed to patch LoadingScreenPCView");
		}
		if (!ApplyPatch(typeof(DollCamera_OnEnable), "DollCamera_OnEnable"))
		{
			throw Error("Failed to patch DollCamera_OnEnable");
		}
		if (!ApplyPatch(typeof(Character_ApplyAdditionalVisualSettings), "Character_ApplyAdditionalVisualSettings"))
		{
			throw Error("Failed to patch Character_ApplyAdditionalVisualSettings");
		}
		if (!ApplyPatch(typeof(GetGroup_Patch), "GetGroup_Patch"))
		{
			throw Error("Failed to patch GetGroup");
		}
		if (!ApplyPatch(typeof(Polymorph_OnActivate_Patch), "Polymorph_OnActivate_Patch"))
		{
			throw Error("Failed to patch Polymorph_OnActivate_Patch");
		}
		if (!ApplyPatch(typeof(Polymorph_OnDeactivate_Patch), "Polymorph_OnDeactivate_Patch"))
		{
			throw Error("Failed to patch Polymorph_OnDeactivate_Patch");
		}
		if (!ApplyPatch(typeof(GameMode_OnDeactivate_Patch), "GameMode_OnDeActivate_Patch"))
		{
			throw Error("Failed to patch GameMode_OnDeActivate");
		}
		if (!ApplyPatch(typeof(EyePortraitInjector), "EyePortraitInjector"))
		{
			throw Error("EyePortraitInjector");
		}
		if (!ApplyPatch(typeof(SmallPortraitInjector), "SmallPortraitInjector"))
		{
			throw Error("SmallPortraitInjector");
		}
		if (!ApplyPatch(typeof(SaveLoadVM_RequestLoad_Patch), "SaveLoadVM_RequestLoad_Patch"))
		{
			throw Error("SaveLoadVM_RequestLoad_Patch");
		}
		if (!ApplyPatch(typeof(OnLocaleChanged_Patch), "OnLocaleChanged_Patch"))
		{
			throw Error("OnLocaleChanged_Patch");
		}
		if (ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("1b893f7cf2b150e4f8bc2b3c389ba71d") != null)
		{
			NenioName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("1b893f7cf2b150e4f8bc2b3c389ba71d").LocalizedName.String);
			ArueName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("a352873d37ec6c54c9fa8f6da3a6b3e1").LocalizedName.String);
			FinneanName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("ea8034769ab7d584e97b5227cbc03296").LocalizedName.String);
			CiarName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("7ece3afabe2b6f343b17d1eaa409d273").LocalizedName.String);
			WoljifName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("766435873b1361c4287c351de194e5f9").LocalizedName.String);
			GalfreyName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("e46927657a79db64ea30758db3f42bb9").LocalizedName.String);
			StauntonName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("0bcf3c125a28d164191e874e3c0c52de").LocalizedName.String);
			IrabethName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("d1e567736abf23943b9f041ba7a0bc23").LocalizedName.String);
			AstyName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("d8e2475977bd87b439c4bba8f5f55949").LocalizedName.String);
			TranName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("c35607fd0f8064f42b4d71f7eb50e96c").LocalizedName.String);
			VelhmName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("f9c01a9515cd1f347800685ddbfbcc41").LocalizedName.String);
			LannName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("cb29621d99b902e4da6f5d232352fbda").LocalizedName.String);
			EmberName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("2779754eecffd044fbd4842dba55312c").LocalizedName.String);
			PentaName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("942862a48f1644ae85ac5e3c9deb720c").LocalizedName.String);
			SeelahName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("54be53f0b35bf3c4592a97ae335fe765").LocalizedName.String);
			DaeranName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("096fc4a96d675bb45a0396bcaa7aa993").LocalizedName.String);
			RegillName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("0d37024170b172346b3769df92a971f5").LocalizedName.String);
			SendriName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("561036c882a640089b1d42f03ebe3a6c").LocalizedName.String);
			UlbrigName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("42f0d5ec3dc844feb44b04507a7c1bfc").LocalizedName.String);
			TreverName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("0bb1c03b9f7bbcf42bb74478af2c6258").LocalizedName.String);
			WenduagName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("ae766624c03058440a036de90a7f2009").LocalizedName.String);
			RekarthName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("3e0014e4be454482a2797fd81123d7b4").LocalizedName.String);
			GreyborName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("f72bb7c48bb3e45458f866045448fb58").LocalizedName.String);
			CamelliaName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("397b090721c41044ea3220445300e1b8").LocalizedName.String);
			DelamereName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("6b1f599497f5cfa42853d095bda6dafd").LocalizedName.String);
			KestoglyrName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("e551850403d61eb48bb2de010d12c894").LocalizedName.String);
			SosielName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("1cbbbb892f93c3d439f8417ad7cbb6aa").LocalizedName.String);
			PillarName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintUnit>("a556fbfa2e0c59e4dad4da70b2e1b1d6").LocalizedName.String);
			EnemyLeaderName = LocalizedString.op_Implicit(ResourcesLibrary.TryGetBlueprint<BlueprintArmyLeader>("02b369f0cbaa8f14d928446765402db4").LeaderName);
			companions = new List<string>
			{
				ArueName, CiarName, NenioName, GalfreyName, StauntonName, WoljifName, LannName, EmberName, PentaName, SeelahName,
				DaeranName, RegillName, SendriName, UlbrigName, TreverName, WenduagName, RekarthName, GreyborName, CamelliaName, DelamereName,
				KestoglyrName, SosielName
			};
		}
		return true;
	}

	public static void CopyFilesRecursively(DirectoryInfo source, DirectoryInfo target)
	{
		DirectoryInfo[] directories = source.GetDirectories();
		foreach (DirectoryInfo directoryInfo in directories)
		{
			CopyFilesRecursively(directoryInfo, target.CreateSubdirectory(directoryInfo.Name));
		}
		FileInfo[] files = source.GetFiles();
		foreach (FileInfo fileInfo in files)
		{
			try
			{
				if (!File.Exists(Path.Combine(target.FullName, fileInfo.Name)))
				{
					fileInfo.CopyTo(Path.Combine(target.FullName, fileInfo.Name), overwrite: false);
				}
			}
			catch (Exception ex)
			{
				DebugError(ex);
			}
		}
	}

	private static void OnShowGUI(ModEntry modEntry)
	{
		//IL_07c8: Unknown result type (might be due to invalid IL or missing references)
		//IL_07cd: Unknown result type (might be due to invalid IL or missing references)
		//IL_0906: Unknown result type (might be due to invalid IL or missing references)
		//IL_090b: Unknown result type (might be due to invalid IL or missing references)
		//IL_07ed: Unknown result type (might be due to invalid IL or missing references)
		//IL_07f2: Unknown result type (might be due to invalid IL or missing references)
		//IL_0984: Unknown result type (might be due to invalid IL or missing references)
		//IL_09a3: Unknown result type (might be due to invalid IL or missing references)
		dirExist1 = false;
		dirExist2 = false;
		dirExist3 = false;
		dirExist4 = false;
		dirExist5 = false;
		dirExist6 = false;
		QueenOld = false;
		showNamings = false;
		CountSwarm();
		if (((EntityFactsProcessor<Etude>)(object)Game.Instance.Player.EtudesSystem.Etudes).GetFact((BlueprintFact)(object)ResourcesLibrary.TryGetBlueprint<BlueprintEtude>("0ab81986d8f7c484a8fede0d2188125c")) != null && ((EntityFactsProcessor<Etude>)(object)Game.Instance.Player.EtudesSystem.Etudes).GetFact((BlueprintFact)(object)ResourcesLibrary.TryGetBlueprint<BlueprintEtude>("0ab81986d8f7c484a8fede0d2188125c")).IsPlaying)
		{
			QueenOld = true;
		}
		if (Game.Instance.CurrentMode == GameModeType.Dialog)
		{
			DebugLog("a1");
			CurrentSpeakerName = Game.Instance.DialogController.CurrentSpeakerName.cleanCharName();
			DirectoryInfo directoryInfo = new DirectoryInfo(GetPortrait_Patch.GetUnitPortraitPath(Game.Instance.DialogController.CurrentSpeakerBlueprint));
			DebugLog("a1aa: " + directoryInfo.Name);
			if (Utils.IsNullOrEmpty(CurrentSpeakerName) && Game.Instance.DialogController.CurrentSpeakerBlueprint != null && !CurrentSpeakerName.Equals(directoryInfo.Name))
			{
				CurrentSpeakerName = directoryInfo.Name;
			}
			DebugLog("a1a: " + CurrentSpeakerName);
			companion = companions.Contains(CurrentSpeakerName);
			DebugLog("a1b");
			if (companion)
			{
				DebugLog("OnShowGui 1" + Game.Instance.DialogController.CurrentSpeakerName.cleanCharName());
				CurrentSpeakerName = GetCompanionDirName(Game.Instance.DialogController.CurrentSpeakerName.cleanCharName());
				DebugLog("OnShowGui 2" + RealCurrentSpeakerEntity(CurrentSpeakerName).CharacterName);
				SetPortrait(RealCurrentSpeakerEntity(CurrentSpeakerName), pickUpOnly: true);
				DebugLog("OnShowGui 3");
				DebugLog("OnShowGui 4");
				if (Directory.Exists(CompanionPortraitPath))
				{
					dirExist2 = true;
				}
				DebugLog("OnShowGui 5");
				if (Directory.Exists(Path.Combine(CompanionPortraitPath, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name)))
				{
					dirExist5 = true;
				}
				DebugLog("OnShowGui 6");
				CurrentSpeakerBlueprintName = ((SimpleBlueprint)Game.Instance.DialogController.CurrentSpeakerBlueprint).name;
				DebugLog("OnShowGui 7");
				portraitDirectorySubPath = Path.Combine(CompanionPortraitPath, CurrentSpeakerBlueprintName);
				DebugLog("OnShowGui 8");
				if (Directory.Exists(portraitDirectorySubPath))
				{
					dirExist6 = true;
				}
				DebugLog("OnShowGui 9");
			}
			else
			{
				DebugLog("a2");
				BlueprintUnit blueprintUnit = null;
				if (Game.Instance.DialogController.CurrentSpeakerBlueprint != null)
				{
					blueprintUnit = Game.Instance.DialogController.CurrentSpeakerBlueprint;
				}
				DebugLog("a2a");
				pickedUpDir = GetPortrait_Patch.GetUnitPortraitPath(blueprintUnit, CurrentSpeakerName.cleanCharName());
				DebugLog("a2b");
				string text = CurrentSpeakerName.cleanCharName();
				DebugLog("a2c");
				if (text.Equals(AstyName) && ((Object)Game.Instance.DialogController.CurrentSpeaker.View).name.ToLower().Contains("drow"))
				{
					text = AstyName + " - Drow";
				}
				if (text.Equals(VelhmName) && ((Object)Game.Instance.DialogController.CurrentSpeaker.View).name.ToLower().Contains("drow"))
				{
					text = VelhmName + " - Drow";
				}
				if (text.Equals(TranName) && ((Object)Game.Instance.DialogController.CurrentSpeaker.View).name.ToLower().Contains("drow"))
				{
					text = TranName + " - Drow";
				}
				if (text.Contains(IrabethName) && Game.Instance.Player.EtudesSystem.EtudeIsStarted(ResourcesLibrary.TryGetBlueprint<BlueprintEtude>("b4f08736cf124ae4996fcef7c0a33bf1")))
				{
					Directory.CreateDirectory(Path.Combine(GetNpcPortraitsDirectory(), IrabethName + " - Scar"));
					text = IrabethName + " - Scar";
				}
				DebugLog("a3");
				NpcPortraitPath = Path.Combine(GetNpcPortraitsDirectory(), text);
				DebugLog("a4");
				if (Directory.Exists(NpcPortraitPath))
				{
					dirExist1 = true;
				}
				DebugLog("a5");
				CurrentSpeakerBlueprintName = ((SimpleBlueprint)Game.Instance.DialogController.CurrentSpeakerBlueprint).name;
				if (CurrentSpeakerBlueprintName == null)
				{
					CurrentSpeakerBlueprintName = ((SimpleBlueprint)Game.Instance.DialogController.CurrentSpeaker.Blueprint).name;
				}
				if (CurrentSpeakerBlueprintName == null)
				{
					CurrentSpeakerBlueprintName = CurrentSpeakerName;
				}
				DebugLog("a6");
				portraitDirectorySubPath = Path.Combine(NpcPortraitPath, CurrentSpeakerBlueprintName);
				if (Directory.Exists(portraitDirectorySubPath))
				{
					dirExist3 = true;
					portraitDirectorySubDialogPath = Path.Combine(NpcPortraitPath, CurrentSpeakerBlueprintName, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name);
					if (Directory.Exists(portraitDirectorySubDialogPath))
					{
						dirExist7 = true;
					}
				}
				if (Directory.Exists(Path.Combine(GetNpcPortraitsDirectory(), Game.Instance.DialogController.CurrentSpeakerName.cleanCharName(), ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name)))
				{
					dirExist4 = true;
				}
			}
			string text2 = Game.Instance.DialogController.CurrentSpeakerName.cleanCharName();
			try
			{
				if (RealCurrentSpeakerEntity(text2) == (UnitDescriptor)null)
				{
					List<string> list = companions;
					UnitEntityData obj = RealCurrentSpeakerEntity(text2);
					if (!list.Contains((obj != null) ? obj.CharacterName.cleanCharName() : null))
					{
						if ((text2.Equals(AstyName) || text2.Equals(VelhmName) || text2.Equals(TranName)) && ((Object)Game.Instance.DialogController.CurrentSpeaker.View).name.ToLower().Contains("drow"))
						{
							text2 += " - Drow";
						}
						if (text2.Equals(IrabethName) && Game.Instance.Player.EtudesSystem.EtudeIsStarted(ResourcesLibrary.TryGetBlueprint<BlueprintEtude>("b4f08736cf124ae4996fcef7c0a33bf1")))
						{
							Directory.CreateDirectory(Path.Combine(GetNpcPortraitsDirectory(), text2 + " - Scar"));
							text2 += " - Scar";
						}
						string text3 = Path.Combine(GetNpcPortraitsDirectory(), text2);
						if (Directory.Exists(text3))
						{
							if (Directory.GetFiles(Path.Combine(text3), "*.current").Length != 0)
							{
								string[] files = Directory.GetFiles(Path.Combine(text3), "*.current");
								if (!Path.GetFileNameWithoutExtension(files[0]).Equals("root"))
								{
									npcDirlabel = Path.GetFileNameWithoutExtension(files[0]);
								}
								else
								{
									npcDirlabel = " - (Npc root folder)";
								}
							}
							else
							{
								npcDirlabel = "";
							}
						}
						if (Directory.Exists(Path.Combine(text3, ((SimpleBlueprint)Game.Instance.DialogController.CurrentSpeakerBlueprint).name)))
						{
							if (Directory.GetFiles(Path.Combine(text3, ((SimpleBlueprint)Game.Instance.DialogController.CurrentSpeakerBlueprint).name), "*.current").Length != 0)
							{
								string[] files2 = Directory.GetFiles(Path.Combine(text3, ((SimpleBlueprint)Game.Instance.DialogController.CurrentSpeakerBlueprint).name), "*.current");
								if (!Path.GetFileNameWithoutExtension(files2[0]).Equals("root"))
								{
									npcSubDirlabel = Path.GetFileNameWithoutExtension(files2[0]);
								}
								else
								{
									npcSubDirlabel = " - (Npc sub root folder)";
								}
							}
							else
							{
								npcSubDirlabel = "";
							}
						}
					}
				}
			}
			catch (Exception ex)
			{
				DebugError(ex);
			}
		}
		if (((object)RootUIContext.Instance.CurrentServiceWindow/*cast due to .constrained prefix*/).ToString().Equals("CharacterInfo") || ((object)RootUIContext.Instance.CurrentServiceWindow/*cast due to .constrained prefix*/).ToString().Equals("Inventory"))
		{
			try
			{
				UnitEntityData currentSelectedCharacter = Game.Instance.SelectionCharacter.CurrentSelectedCharacter;
				SetPortrait(currentSelectedCharacter, pickUpOnly: true);
				charcterNameDirectoryName = GetCompanionDirName(currentSelectedCharacter.CharacterName.cleanCharName());
				string text4 = Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + charcterNameDirectoryName);
				if (Directory.Exists(text4))
				{
					if (Directory.GetFiles(Path.Combine(text4), "*.current").Length != 0)
					{
						compDirlabel = Path.GetFileNameWithoutExtension(Directory.GetFiles(Path.Combine(text4), "*.current")[0]);
					}
					else
					{
						compDirlabel = "";
					}
				}
			}
			catch (Exception ex2)
			{
				DebugError(ex2);
			}
		}
		i = -1;
		savedNpc = !settings.AutoBackup;
		savedComp = false;
		isDialog = true;
		isLoadedGame = true;
		showExperimental = false;
		npcCycle = "";
		npcSubCycle = "";
		compCycle = "";
		Scene activeScene = SceneManager.GetActiveScene();
		string name = ((Scene)(ref activeScene)).name;
		Game instance = Game.Instance;
		if (((instance != null) ? instance.Player : null) == null || name == "UI_MainMenu_Scene" || name == "Start")
		{
			isLoadedGame = false;
			isDialog = false;
		}
		else if (instance.CurrentMode != GameModeType.Dialog)
		{
			isLoadedGame = true;
			isDialog = false;
		}
		boldStyle.fontStyle = (FontStyle)1;
		boldStyle.normal.textColor = Color.cyan;
		boldStyle2.fontStyle = (FontStyle)1;
		boldStyle2.normal.textColor = Color.red;
	}

	private unsafe static void OnGUI(ModEntry modEntry)
	{
		//IL_0234: Unknown result type (might be due to invalid IL or missing references)
		//IL_0239: Unknown result type (might be due to invalid IL or missing references)
		//IL_02bd: Unknown result type (might be due to invalid IL or missing references)
		//IL_02c2: Unknown result type (might be due to invalid IL or missing references)
		//IL_0258: Unknown result type (might be due to invalid IL or missing references)
		//IL_025d: Unknown result type (might be due to invalid IL or missing references)
		//IL_02e1: Unknown result type (might be due to invalid IL or missing references)
		//IL_02e6: Unknown result type (might be due to invalid IL or missing references)
		//IL_0653: Unknown result type (might be due to invalid IL or missing references)
		//IL_0658: Unknown result type (might be due to invalid IL or missing references)
		//IL_0677: Unknown result type (might be due to invalid IL or missing references)
		//IL_067c: Unknown result type (might be due to invalid IL or missing references)
		//IL_23dd: Unknown result type (might be due to invalid IL or missing references)
		//IL_23e7: Expected O, but got Unknown
		//IL_2787: Unknown result type (might be due to invalid IL or missing references)
		//IL_278c: Unknown result type (might be due to invalid IL or missing references)
		//IL_27b9: Unknown result type (might be due to invalid IL or missing references)
		//IL_27be: Unknown result type (might be due to invalid IL or missing references)
		//IL_05af: Unknown result type (might be due to invalid IL or missing references)
		//IL_28c6: Unknown result type (might be due to invalid IL or missing references)
		//IL_2954: Unknown result type (might be due to invalid IL or missing references)
		//IL_2959: Unknown result type (might be due to invalid IL or missing references)
		//IL_0eb3: Unknown result type (might be due to invalid IL or missing references)
		//IL_0ebd: Expected O, but got Unknown
		//IL_1704: Unknown result type (might be due to invalid IL or missing references)
		//IL_170e: Expected O, but got Unknown
		//IL_2ad9: Unknown result type (might be due to invalid IL or missing references)
		//IL_2ade: Unknown result type (might be due to invalid IL or missing references)
		//IL_2cd0: Unknown result type (might be due to invalid IL or missing references)
		//IL_2db0: Unknown result type (might be due to invalid IL or missing references)
		//IL_2e76: Unknown result type (might be due to invalid IL or missing references)
		//IL_2fe1: Unknown result type (might be due to invalid IL or missing references)
		//IL_302d: Unknown result type (might be due to invalid IL or missing references)
		//IL_3649: Unknown result type (might be due to invalid IL or missing references)
		//IL_308c: Unknown result type (might be due to invalid IL or missing references)
		//IL_3113: Unknown result type (might be due to invalid IL or missing references)
		//IL_3180: Unknown result type (might be due to invalid IL or missing references)
		//IL_3144: Unknown result type (might be due to invalid IL or missing references)
		//IL_3726: Unknown result type (might be due to invalid IL or missing references)
		//IL_376d: Unknown result type (might be due to invalid IL or missing references)
		//IL_32a5: Unknown result type (might be due to invalid IL or missing references)
		//IL_3380: Unknown result type (might be due to invalid IL or missing references)
		//IL_339c: Unknown result type (might be due to invalid IL or missing references)
		//IL_33a1: Unknown result type (might be due to invalid IL or missing references)
		//IL_33a6: Unknown result type (might be due to invalid IL or missing references)
		//IL_33c7: Unknown result type (might be due to invalid IL or missing references)
		//IL_3527: Unknown result type (might be due to invalid IL or missing references)
		//IL_3563: Unknown result type (might be due to invalid IL or missing references)
		//IL_359a: Unknown result type (might be due to invalid IL or missing references)
		if (settings.ManageCompanions)
		{
			GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
			if (GUILayout.Button("Open Party Portraits Directory", (GUILayoutOption[])(object)new GUILayoutOption[2]
			{
				GUILayout.Width(200f),
				GUILayout.Height(20f)
			}))
			{
				Process.Start(GetCompanionPortraitsDirectory());
			}
			GUILayout.Label(GetCompanionPortraitsDirectory(), Array.Empty<GUILayoutOption>());
			GUILayout.EndHorizontal();
		}
		GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
		if (GUILayout.Button("Open NPC portraits dir", (GUILayoutOption[])(object)new GUILayoutOption[2]
		{
			GUILayout.Width(200f),
			GUILayout.Height(20f)
		}))
		{
			Process.Start(GetNpcPortraitsDirectory());
		}
		GUILayout.Label(GetNpcPortraitsDirectory(), Array.Empty<GUILayoutOption>());
		GUILayout.EndHorizontal();
		GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
		if (GUILayout.Button("Open Army portraits dir", (GUILayoutOption[])(object)new GUILayoutOption[2]
		{
			GUILayout.Width(200f),
			GUILayout.Height(20f)
		}))
		{
			Process.Start(GetArmyPortraitsDirectory());
		}
		GUILayout.Label(GetArmyPortraitsDirectory(), Array.Empty<GUILayoutOption>());
		GUILayout.EndHorizontal();
		GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
		if (GUILayout.Button("Open Tactical portraits dir", (GUILayoutOption[])(object)new GUILayoutOption[2]
		{
			GUILayout.Width(200f),
			GUILayout.Height(20f)
		}))
		{
			Process.Start(GetTacticalPortraitsDirectory());
		}
		GUILayout.Label(GetTacticalPortraitsDirectory(), Array.Empty<GUILayoutOption>());
		GUILayout.EndHorizontal();
		GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
		GUILayout.Label("_____________________________________________________", Array.Empty<GUILayoutOption>());
		GUILayout.EndHorizontal();
		GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
		GUILayout.Label("In game", boldStyle, Array.Empty<GUILayoutOption>());
		GUILayout.EndHorizontal();
		if (!isLoadedGame)
		{
			GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
			GUILayout.Label("Load a save or start a new game for more options", Array.Empty<GUILayoutOption>());
			GUILayout.EndHorizontal();
		}
		else
		{
			if (settings.ManageCompanions)
			{
				GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
				if (GUILayout.Button("Refresh Party Portraits", (GUILayoutOption[])(object)new GUILayoutOption[2]
				{
					GUILayout.Width(200f),
					GUILayout.Height(20f)
				}) && settings.ManageCompanions)
				{
					SetPortraits();
				}
				GUILayout.EndHorizontal();
			}
			if (settings.ManageCompanions && (((object)RootUIContext.Instance.CurrentServiceWindow/*cast due to .constrained prefix*/).ToString().Equals("CharacterInfo") || ((object)RootUIContext.Instance.CurrentServiceWindow/*cast due to .constrained prefix*/).ToString().Equals("Inventory")))
			{
				GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
				GUILayout.Label("Currently picked up portrait: " + CompanionPortraitPath, Array.Empty<GUILayoutOption>());
				GUILayout.EndHorizontal();
			}
			GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
			if (settings.ManageCompanions)
			{
				if (((object)RootUIContext.Instance.CurrentServiceWindow/*cast due to .constrained prefix*/).ToString().Equals("CharacterInfo") || ((object)RootUIContext.Instance.CurrentServiceWindow/*cast due to .constrained prefix*/).ToString().Equals("Inventory"))
				{
					string text = Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + charcterNameDirectoryName);
					if (GUILayout.Button("Cycle portraits for " + Game.Instance.SelectionCharacter.CurrentSelectedCharacter.CharacterName.cleanCharName(), (GUILayoutOption[])(object)new GUILayoutOption[2]
					{
						GUILayout.Width(250f),
						GUILayout.Height(20f)
					}))
					{
						List<string> strings = Directory.GetDirectories(text, "*", SearchOption.TopDirectoryOnly).ToList();
						unitNames.ForEach(delegate(string item)
						{
							LinqExtensions.Remove<string>((IList<string>)strings, (Predicate<string>)((string x) => x.Contains(item)));
						});
						strings.RemoveAll((string x) => x.EndsWith("Buff"));
						strings.RemoveAll((string x) => x.Contains("Buff_"));
						UnitEntityData currentSelectedCharacter = Game.Instance.SelectionCharacter.CurrentSelectedCharacter;
						SetPortrait(currentSelectedCharacter, pickUpOnly: true);
						if (File.Exists(Path.Combine(text, "Medium.png")) && !strings.Exists((string x) => x.Equals("companion name Medium png placeholder")))
						{
							strings.Add("companion name Medium png placeholder");
						}
						if (strings.Count() == 1)
						{
							i = -1;
						}
						else if (i == strings.Count() - 1)
						{
							i = -1;
						}
						i++;
						string[] files = Directory.GetFiles(text, "*.current");
						for (int num = 0; num < files.Length; num++)
						{
							File.Delete(files[num]);
						}
						if (strings[i].Equals("companion name Medium png placeholder"))
						{
							compCycle = "";
							compDirlabel = " - (Character root folder)";
							File.WriteAllText(Path.Combine(text, "root.current"), "current");
						}
						else
						{
							compCycle = Path.GetFileName(strings[i]);
							compDirlabel = compCycle;
							File.WriteAllText(Path.Combine(text, compCycle + ".current"), "current");
						}
						SetCustomPortrait(Game.Instance.SelectionCharacter.CurrentSelectedCharacter);
						if (!currentSelectedCharacter.IsMainCharacter)
						{
							Game.Instance.SelectionCharacter.SetSelected(Game.Instance.Player.GetMainPartyUnit());
							Game.Instance.SelectionCharacter.SetSelected(currentSelectedCharacter);
						}
						else
						{
							foreach (UnitReference partyCharacter in Game.Instance.Player.PartyCharacters)
							{
								UnitEntityData val = UnitReference.op_Implicit(partyCharacter);
								if (!val.IsMainCharacter && !val.IsPet)
								{
									Game.Instance.SelectionCharacter.SetSelected(val);
									break;
								}
							}
							Game.Instance.SelectionCharacter.SetSelected(currentSelectedCharacter);
						}
						compCycle = "";
					}
					if (GUILayout.Button("Next", (GUILayoutOption[])(object)new GUILayoutOption[2]
					{
						GUILayout.Width(100f),
						GUILayout.Height(20f)
					}))
					{
						j++;
						if (((object)RootUIContext.Instance.CurrentServiceWindow/*cast due to .constrained prefix*/).ToString().Equals("CharacterInfo") || ((object)RootUIContext.Instance.CurrentServiceWindow/*cast due to .constrained prefix*/).ToString().Equals("Inventory"))
						{
							Game.Instance.SelectionCharacter.SetSelected(Game.Instance.SelectionCharacter.ActualGroup.ToArray()[j]);
							if (j == Game.Instance.SelectionCharacter.ActualGroup.ToArray().Count() - 1)
							{
								j = -1;
							}
							try
							{
								charcterNameDirectoryName = GetCompanionDirName(Game.Instance.SelectionCharacter.CurrentSelectedCharacter.CharacterName.cleanCharName());
								string text2 = Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + charcterNameDirectoryName);
								if (Directory.Exists(text2))
								{
									if (Directory.GetFiles(Path.Combine(text2), "*.current").Length != 0)
									{
										string[] files2 = Directory.GetFiles(Path.Combine(text2), "*.current");
										if (!Path.GetFileNameWithoutExtension(files2[0]).Equals("root"))
										{
											compDirlabel = Path.GetFileNameWithoutExtension(files2[0]);
										}
										else
										{
											compDirlabel = " - (Character root folder)";
										}
									}
									else
									{
										compDirlabel = "";
									}
								}
							}
							catch (Exception ex)
							{
								DebugError(ex);
							}
						}
					}
					GUILayout.Label(Path.Combine(text, compDirlabel), Array.Empty<GUILayoutOption>());
				}
				else
				{
					GUILayout.Label("Open Character Info sheet first for cycle through companion portraits.", Array.Empty<GUILayoutOption>());
				}
			}
			else
			{
				GUILayout.Label("Advanced settings: mod is not managing companion portraits.", Array.Empty<GUILayoutOption>());
			}
			GUILayout.EndHorizontal();
			GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
			GUILayout.Label("_____________________________________________________", Array.Empty<GUILayoutOption>());
			GUILayout.EndHorizontal();
			GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
			if (GUILayout.Button("Create Dirs", (GUILayoutOption[])(object)new GUILayoutOption[2]
			{
				GUILayout.Width(200f),
				GUILayout.Height(20f)
			}))
			{
				makeNpcDirs();
			}
			GUILayout.Label("Create directories for all NPC-s taking part in dialogs.", Array.Empty<GUILayoutOption>());
			GUILayout.EndHorizontal();
			if (!showExperimental)
			{
				GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
				if (GUILayout.Button("Show experimental feature", (GUILayoutOption[])(object)new GUILayoutOption[2]
				{
					GUILayout.Width(200f),
					GUILayout.Height(20f)
				}))
				{
					showExperimental = true;
				}
				GUILayout.EndHorizontal();
			}
			else
			{
				GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
				if (GUILayout.Button("Close", (GUILayoutOption[])(object)new GUILayoutOption[2]
				{
					GUILayout.Width(200f),
					GUILayout.Height(20f)
				}))
				{
					showExperimental = false;
				}
				GUILayout.Label("WARNING! This might hang your game for 1-2 minutes or crash.", boldStyle, Array.Empty<GUILayoutOption>());
				GUILayout.EndHorizontal();
				GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
				if (GUILayout.Button("Save Npc Portraits", (GUILayoutOption[])(object)new GUILayoutOption[2]
				{
					GUILayout.Width(200f),
					GUILayout.Height(20f)
				}))
				{
					saveNpcPortraits();
				}
				GUILayout.Label("Save all NPC-s' turn based portraits in their respective dirs: " + portraitCounter + " have been saved OK! ( " + failCounter + " invalid )", Array.Empty<GUILayoutOption>());
				GUILayout.EndHorizontal();
			}
			GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
			GUILayout.Label("_____________________________________________________", Array.Empty<GUILayoutOption>());
			GUILayout.EndHorizontal();
			GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
			GUILayout.Label("In dialog", boldStyle, Array.Empty<GUILayoutOption>());
			GUILayout.EndHorizontal();
			if (!isDialog)
			{
				GUILayout.Label("Start a dialog for more options!", Array.Empty<GUILayoutOption>());
				GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
				GUILayout.Label("Campaign name: " + ((SimpleBlueprint)Game.Instance.Player.Campaign).name, Array.Empty<GUILayoutOption>());
				GUILayout.EndHorizontal();
				GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
				GUILayout.Label("Enemy Leader localized: " + EnemyLeaderName, Array.Empty<GUILayoutOption>());
				GUILayout.EndHorizontal();
			}
			else
			{
				if (Game.Instance.DialogController.CurrentSpeakerBlueprint != null)
				{
					if (CurrentSpeakerName.Equals(AstyName))
					{
						if (((Object)Game.Instance.DialogController.CurrentSpeaker.View).name.ToLower().Contains("drow"))
						{
							CurrentSpeakerName = AstyName + " - Drow";
						}
						else
						{
							savedNpc = true;
						}
					}
					if (CurrentSpeakerName.Equals(VelhmName))
					{
						if (((Object)Game.Instance.DialogController.CurrentSpeaker.View).name.ToLower().Contains("drow"))
						{
							CurrentSpeakerName = VelhmName + " - Drow";
						}
						else
						{
							savedNpc = true;
						}
					}
					if (CurrentSpeakerName.Equals(TranName))
					{
						if (((Object)Game.Instance.DialogController.CurrentSpeaker.View).name.ToLower().Contains("drow"))
						{
							CurrentSpeakerName = TranName + " - Drow";
						}
						else
						{
							savedNpc = true;
						}
					}
					if (CurrentSpeakerName.Equals(IrabethName))
					{
						if (Game.Instance.Player.EtudesSystem.EtudeIsStarted(ResourcesLibrary.TryGetBlueprint<BlueprintEtude>("b4f08736cf124ae4996fcef7c0a33bf1")))
						{
							CurrentSpeakerName += " - Scar";
						}
						else
						{
							savedNpc = true;
						}
					}
					if (!companion)
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("Actually picked up portrait: " + pickedUpDir, Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
						if (dirExist1)
						{
							if (settings.AutoBackup && !savedNpc)
							{
								SaveOriginals(Game.Instance.DialogController.CurrentSpeakerBlueprint, NpcPortraitPath);
								savedNpc = true;
							}
							GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
							if (GUILayout.Button("Open current speaker dir", (GUILayoutOption[])(object)new GUILayoutOption[2]
							{
								GUILayout.Width(200f),
								GUILayout.Height(20f)
							}))
							{
								Process.Start(NpcPortraitPath);
							}
							if (GUILayout.Button("Cycle through dir", (GUILayoutOption[])(object)new GUILayoutOption[2]
							{
								GUILayout.Width(200f),
								GUILayout.Height(20f)
							}))
							{
								List<string> strings2 = Directory.GetDirectories(NpcPortraitPath, "*", SearchOption.TopDirectoryOnly).ToList();
								unitNames.ForEach(delegate(string item)
								{
									LinqExtensions.Remove<string>((IList<string>)strings2, (Predicate<string>)((string x) => x.Contains(item)));
								});
								strings2.RemoveAll((string x) => x.EndsWith("Buff"));
								strings2.RemoveAll((string x) => x.Contains("Buff_"));
								if (File.Exists(Path.Combine(NpcPortraitPath, "Medium.png")) && !strings2.Exists((string x) => x.Equals("npc name root Medium png placeholder")))
								{
									strings2.Add("npc name root Medium png placeholder");
								}
								if (strings2.Count() == 1)
								{
									i = -1;
								}
								else if (i == strings2.Count() - 1)
								{
									i = -1;
								}
								i++;
								foreach (string item in strings2)
								{
									_ = item;
								}
								string[] files = Directory.GetFiles(NpcPortraitPath, "*.current");
								for (int num = 0; num < files.Length; num++)
								{
									File.Delete(files[num]);
								}
								if (strings2[i].Equals("npc name root Medium png placeholder"))
								{
									npcCycle = "";
									npcDirlabel = " - (Npc root folder)";
									File.WriteAllText(Path.Combine(NpcPortraitPath, "root.current"), "current");
								}
								else
								{
									npcCycle = Path.GetFileName(strings2[i]);
									npcDirlabel = npcCycle;
									File.WriteAllText(Path.Combine(NpcPortraitPath, npcCycle + ".current"), "current");
								}
								CueShowData cueShowDatum = new CueShowData(Game.Instance.DialogController.CurrentCue, (IEnumerable<SkillCheckResult>)new List<SkillCheckResult>(), (IEnumerable<AlignmentShift>)new List<AlignmentShift>());
								EventBus.RaiseEvent<IDialogCueHandler>((Action<IDialogCueHandler>)delegate(IDialogCueHandler h)
								{
									h.HandleOnCueShow(cueShowDatum);
								}, true);
								npcCycle = "";
							}
							GUILayout.Label(Path.Combine(NpcPortraitPath, npcDirlabel), Array.Empty<GUILayoutOption>());
							GUILayout.EndHorizontal();
						}
						else
						{
							GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
							if (GUILayout.Button("Make speaker dir", (GUILayoutOption[])(object)new GUILayoutOption[2]
							{
								GUILayout.Width(200f),
								GUILayout.Height(20f)
							}))
							{
								Directory.CreateDirectory(NpcPortraitPath);
								dirExist1 = true;
							}
							GUILayout.Label(NpcPortraitPath, Array.Empty<GUILayoutOption>());
							GUILayout.EndHorizontal();
						}
					}
					else if (settings.ManageCompanions)
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("Actually picked up portrait: " + CompanionPortraitPath, Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
						if (CurrentSpeakerName.Equals(ArueName + " - Evil") && settings.AutoBackup && !savedComp)
						{
							savedComp = true;
							SaveOriginals2(Utilities.GetBlueprintByGuid<BlueprintPortrait>("484588d56f2c2894ab6d48b91509f5e3").Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + CurrentSpeakerName));
						}
						if (CurrentSpeakerName.Equals(NenioName + "Fox_Portrait") && settings.AutoBackup && !savedComp)
						{
							savedComp = true;
							SaveOriginals2(Utilities.GetBlueprintByGuid<BlueprintPortrait>("a6e4ff25a8da46a44a24ecc5da296073").Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + CurrentSpeakerName));
						}
						if (CurrentSpeakerName.Equals(NenioName) && settings.AutoBackup && !savedComp)
						{
							savedComp = true;
							SaveOriginals2(Utilities.GetBlueprintByGuid<BlueprintPortrait>("2b4b8a23024093e42a5db714c2f52dbc").Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + CurrentSpeakerName));
						}
						if (CurrentSpeakerName.Equals(CiarName + " - Undead") && settings.AutoBackup && !savedComp)
						{
							savedComp = true;
							SaveOriginals2(Utilities.GetBlueprintByGuid<BlueprintPortrait>("dc2f02dd42cfe2b40923eb014591a009").Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + CurrentSpeakerName));
						}
						if (CurrentSpeakerName.Equals(GalfreyName + " - Undead") && settings.AutoBackup && !savedComp)
						{
							savedComp = true;
							SaveOriginals2(Utilities.GetBlueprintByGuid<BlueprintPortrait>("767456b1656ca064dadac544d39d7e40").Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + CurrentSpeakerName));
						}
						if (CurrentSpeakerName.Equals(GalfreyName + " - Old") && settings.AutoBackup && !savedComp)
						{
							savedComp = true;
							SaveOriginals2(Utilities.GetBlueprintByGuid<BlueprintPortrait>("4e8dfb75015d356469b976145c851087").Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + CurrentSpeakerName));
						}
						if (CurrentSpeakerName.Equals(WoljifName + " - Demon") && settings.AutoBackup && !savedComp)
						{
							savedComp = true;
							SaveOriginals2(Utilities.GetBlueprintByGuid<BlueprintPortrait>("f2bd5a94ade889444921b4a74b9e34a9").Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + CurrentSpeakerName));
						}
						if (CurrentSpeakerName.Equals(SendriName + " - ChrystalEye") && settings.AutoBackup && !savedComp)
						{
							savedComp = true;
							SaveOriginals2(Utilities.GetBlueprintByGuid<BlueprintPortrait>("222c3bcbf7e342338416c0e8bdc75109").Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + CurrentSpeakerName));
						}
						if (CurrentSpeakerName.Equals(StauntonName + " - Undead") && settings.AutoBackup && !savedComp)
						{
							savedComp = true;
							SaveOriginals2(Utilities.GetBlueprintByGuid<BlueprintPortrait>("f4bbe08217bcaa54c91fe73bcea70ede").Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + CurrentSpeakerName));
						}
						if (dirExist2)
						{
							if (settings.AutoBackup && !savedComp)
							{
								SaveOriginals(Game.Instance.DialogController.CurrentSpeakerBlueprint, CompanionPortraitPath);
								savedComp = true;
							}
							GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
							if (GUILayout.Button("Open current speaker dir", (GUILayoutOption[])(object)new GUILayoutOption[2]
							{
								GUILayout.Width(200f),
								GUILayout.Height(20f)
							}))
							{
								Process.Start(CompanionPortraitPath);
							}
							GUILayout.Label(CompanionPortraitPath, Array.Empty<GUILayoutOption>());
							GUILayout.EndHorizontal();
						}
						else
						{
							GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
							if (GUILayout.Button("Make speaker dir", (GUILayoutOption[])(object)new GUILayoutOption[2]
							{
								GUILayout.Width(200f),
								GUILayout.Height(20f)
							}))
							{
								Directory.CreateDirectory(CompanionPortraitPath);
								dirExist2 = true;
							}
							GUILayout.Label(CompanionPortraitPath, Array.Empty<GUILayoutOption>());
							GUILayout.EndHorizontal();
						}
					}
					else
					{
						GUILayout.Label("Advanced settings: mod is not managing companion portraits.", Array.Empty<GUILayoutOption>());
					}
					if (!companion)
					{
						if (dirExist3)
						{
							if (settings.AutoBackup && !savedNpc)
							{
								SaveOriginals(Game.Instance.DialogController.CurrentSpeakerBlueprint, portraitDirectorySubPath);
								savedNpc = true;
							}
							GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
							if (GUILayout.Button("Open current speaker subdir", (GUILayoutOption[])(object)new GUILayoutOption[2]
							{
								GUILayout.Width(200f),
								GUILayout.Height(20f)
							}))
							{
								Process.Start(portraitDirectorySubPath);
							}
							if (GUILayout.Button("Cycle through subdirs", (GUILayoutOption[])(object)new GUILayoutOption[2]
							{
								GUILayout.Width(200f),
								GUILayout.Height(20f)
							}))
							{
								List<string> strings3 = Directory.GetDirectories(portraitDirectorySubPath, "*", SearchOption.TopDirectoryOnly).ToList();
								DebugLog("b4");
								unitNames.ForEach(delegate(string item)
								{
									LinqExtensions.Remove<string>((IList<string>)strings3, (Predicate<string>)((string x) => x.Contains(item)));
								});
								strings3.RemoveAll((string x) => x.EndsWith("Buff"));
								strings3.RemoveAll((string x) => x.Contains("Buff_"));
								if (File.Exists(Path.Combine(portraitDirectorySubPath, "Medium.png")) && !strings3.Exists((string x) => x.Equals("npc name subroot Medium png placeholder")))
								{
									strings3.Add("npc name subroot Medium png placeholder");
								}
								if (strings3.Count() == 1)
								{
									i = -1;
								}
								else if (i == strings3.Count() - 1)
								{
									i = -1;
								}
								i++;
								foreach (string item2 in strings3)
								{
									_ = item2;
								}
								string[] files = Directory.GetFiles(portraitDirectorySubPath, "*.current");
								for (int num = 0; num < files.Length; num++)
								{
									File.Delete(files[num]);
								}
								if (strings3[i].Equals("npc name subroot Medium png placeholder"))
								{
									npcSubCycle = "";
									npcSubDirlabel = " - (Npc sub root folder)";
									DebugLog("b5");
									File.WriteAllText(Path.Combine(portraitDirectorySubPath, "root.current"), "current");
								}
								else
								{
									npcSubCycle = Path.GetFileName(strings3[i]);
									npcSubDirlabel = npcSubCycle;
									DebugLog("b6");
									File.WriteAllText(Path.Combine(portraitDirectorySubPath, npcSubCycle + ".current"), "current");
								}
								CueShowData cueShowDatum2 = new CueShowData(Game.Instance.DialogController.CurrentCue, (IEnumerable<SkillCheckResult>)new List<SkillCheckResult>(), (IEnumerable<AlignmentShift>)new List<AlignmentShift>());
								EventBus.RaiseEvent<IDialogCueHandler>((Action<IDialogCueHandler>)delegate(IDialogCueHandler h)
								{
									h.HandleOnCueShow(cueShowDatum2);
								}, true);
								npcSubCycle = "";
							}
							GUILayout.Label(Path.Combine(portraitDirectorySubPath, npcSubDirlabel), Array.Empty<GUILayoutOption>());
							GUILayout.EndHorizontal();
						}
						else if (!CurrentSpeakerName.Equals(CurrentSpeakerBlueprintName) && !CurrentSpeakerName.Contains(" - Drow"))
						{
							GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
							if (GUILayout.Button("Make speaker subcat dir", (GUILayoutOption[])(object)new GUILayoutOption[2]
							{
								GUILayout.Width(200f),
								GUILayout.Height(20f)
							}))
							{
								Directory.CreateDirectory(portraitDirectorySubPath);
								dirExist3 = true;
							}
							GUILayout.Label("..\\" + portraitDirectorySubPath, Array.Empty<GUILayoutOption>());
							GUILayout.EndHorizontal();
						}
					}
					else if (dirExist6)
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						if (GUILayout.Button("Open current speaker subdir", (GUILayoutOption[])(object)new GUILayoutOption[2]
						{
							GUILayout.Width(200f),
							GUILayout.Height(20f)
						}))
						{
							Process.Start(portraitDirectorySubPath);
						}
						GUILayout.Label(Path.Combine(portraitDirectorySubPath), Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
					else
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						if (GUILayout.Button("Make speaker subcat dir", (GUILayoutOption[])(object)new GUILayoutOption[2]
						{
							GUILayout.Width(200f),
							GUILayout.Height(20f)
						}))
						{
							Directory.CreateDirectory(portraitDirectorySubPath);
							dirExist6 = true;
						}
						GUILayout.Label("..\\" + portraitDirectorySubPath, Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
				}
				GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
				if (!companion)
				{
					if (!dirExist4)
					{
						if (GUILayout.Button("Create dialog folder", (GUILayoutOption[])(object)new GUILayoutOption[2]
						{
							GUILayout.Width(200f),
							GUILayout.Height(20f)
						}))
						{
							Directory.CreateDirectory(Path.Combine(NpcPortraitPath, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name));
							dirExist4 = true;
						}
						GUILayout.Label("Create unique folder only for this dialog named: " + ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name, Array.Empty<GUILayoutOption>());
					}
					else
					{
						if (GUILayout.Button("Open dialog folder", (GUILayoutOption[])(object)new GUILayoutOption[2]
						{
							GUILayout.Width(200f),
							GUILayout.Height(20f)
						}))
						{
							Process.Start(Path.Combine(GetNpcPortraitsDirectory(), Game.Instance.DialogController.CurrentSpeakerName.cleanCharName(), ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name));
						}
						GUILayout.Label("Open folder: " + Path.Combine(GetNpcPortraitsDirectory(), Game.Instance.DialogController.CurrentSpeakerName.cleanCharName(), ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name), Array.Empty<GUILayoutOption>());
					}
					if (!dirExist7)
					{
						if (GUILayout.Button("Create dialog sub unit folder", (GUILayoutOption[])(object)new GUILayoutOption[2]
						{
							GUILayout.Width(200f),
							GUILayout.Height(20f)
						}))
						{
							Directory.CreateDirectory(portraitDirectorySubDialogPath);
							dirExist7 = true;
						}
						GUILayout.Label("Create sub unit folder only for this dialog named: " + ((SimpleBlueprint)Game.Instance.DialogController.CurrentSpeakerBlueprint).name + "/" + ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name, Array.Empty<GUILayoutOption>());
					}
					else
					{
						if (GUILayout.Button("Open dialog sub unit folder", (GUILayoutOption[])(object)new GUILayoutOption[2]
						{
							GUILayout.Width(200f),
							GUILayout.Height(20f)
						}))
						{
							Process.Start(portraitDirectorySubDialogPath);
						}
						GUILayout.Label("Open folder: " + portraitDirectorySubDialogPath, Array.Empty<GUILayoutOption>());
					}
				}
				else if (!dirExist5)
				{
					if (GUILayout.Button("Create dialog folder", (GUILayoutOption[])(object)new GUILayoutOption[2]
					{
						GUILayout.Width(200f),
						GUILayout.Height(20f)
					}))
					{
						Directory.CreateDirectory(Path.Combine(CompanionPortraitPath, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name));
						dirExist5 = true;
					}
					GUILayout.Label("Create folder only for this dialog named: " + Path.Combine(CompanionPortraitPath, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name), Array.Empty<GUILayoutOption>());
				}
				else
				{
					if (GUILayout.Button("Open dialog folder", (GUILayoutOption[])(object)new GUILayoutOption[2]
					{
						GUILayout.Width(200f),
						GUILayout.Height(20f)
					}))
					{
						Process.Start(Path.Combine(CompanionPortraitPath, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name));
					}
					GUILayout.Label("Open folder: " + Path.Combine(CompanionPortraitPath, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name), Array.Empty<GUILayoutOption>());
				}
				GUILayout.EndHorizontal();
				GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
				GUILayout.Label("_____________________________________________________", Array.Empty<GUILayoutOption>());
				GUILayout.EndHorizontal();
				if (!showNamings)
				{
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					if (GUILayout.Button("Show namings", (GUILayoutOption[])(object)new GUILayoutOption[2]
					{
						GUILayout.Width(200f),
						GUILayout.Height(20f)
					}))
					{
						showNamings = true;
					}
					GUILayout.EndHorizontal();
				}
				else
				{
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					if (GUILayout.Button("Close", (GUILayoutOption[])(object)new GUILayoutOption[2]
					{
						GUILayout.Width(200f),
						GUILayout.Height(20f)
					}))
					{
						showNamings = false;
					}
					GUILayout.EndHorizontal();
					GUILayoutOption[] array = (GUILayoutOption[])(object)new GUILayoutOption[1] { GUILayout.Width(400f) };
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					GUILayout.Label("__________________Possible names_______________________________", Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					if (QueenOld)
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("The records show Queen Galfrey is old", Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
					else
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("The records show Queen Galfrey is not old", Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
					if (Game.Instance.DialogController.CurrentSpeakerBlueprint.m_AddFacts.Contains(BlueprintReferenceEx.ToReference<BlueprintUnitFactReference>((SimpleBlueprint)(object)ResourcesLibrary.TryGetBlueprint<BlueprintFeature>("734a29b693e9ec346ba2951b27987e33"))))
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("CurrentspeakerBlueprint fact says speaker is undead", Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
					else
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("CurrentspeakerBlueprint fact says speaker is NOT undead", Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
					if (Game.Instance.DialogController.CurrentSpeaker.Descriptor.IsUndead)
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("CurrentSpeaker.Descriptor says speaker is undead", Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
					else
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("CurrentSpeaker.Descriptor says speaker is NOT undead", Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
					if (((Object)Game.Instance.DialogController.CurrentSpeaker.View).name.ToLower().Contains("drow"))
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("CurrentSpeaker.View.name is Drow", Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
					else
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("CurrentSpeaker.View.name is NOT Drow", Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
					if (Game.Instance.Player.EtudesSystem.EtudeIsStarted(ResourcesLibrary.TryGetBlueprint<BlueprintEtude>("b4f08736cf124ae4996fcef7c0a33bf1")))
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("Irabeth has scar", Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
					else
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("Irabeth has NO scar", Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					UnitEntityData currentSpeaker = Game.Instance.DialogController.CurrentSpeaker;
					GUILayout.Label("CurrentSpeaker.CharacterName: " + ((currentSpeaker != null) ? currentSpeaker.CharacterName : null), Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					UnitEntityData currentSpeaker2 = Game.Instance.DialogController.CurrentSpeaker;
					object obj;
					if (currentSpeaker2 == null)
					{
						obj = null;
					}
					else
					{
						BlueprintUnit blueprint = currentSpeaker2.Blueprint;
						obj = ((blueprint != null) ? blueprint.CharacterName : null);
					}
					GUILayout.Label("CurrentSpeaker.Blueprint.CharacterName: " + (string)obj, Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					UnitEntityData currentSpeaker3 = Game.Instance.DialogController.CurrentSpeaker;
					GUILayout.Label("CurrentSpeaker.Blueprint.name: " + ((currentSpeaker3 == null) ? null : ((SimpleBlueprint)(currentSpeaker3.Blueprint?)).name), Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					BlueprintUnit currentSpeakerBlueprint = Game.Instance.DialogController.CurrentSpeakerBlueprint;
					GUILayout.Label("CurrentSpeakerBlueprint.CharacterName: " + ((currentSpeakerBlueprint != null) ? currentSpeakerBlueprint.CharacterName : null), Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					GUILayout.Label("CurrentSpeakerBlueprint.name: " + ((SimpleBlueprint)(Game.Instance.DialogController.CurrentSpeakerBlueprint?)).name, Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					GUILayout.Label("CurrentSpeakerName: " + Game.Instance.DialogController.CurrentSpeakerName, Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					GUILayout.Label("InvolvedUnits: ", Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					foreach (UnitEntityData involvedUnit in Game.Instance.DialogController.InvolvedUnits)
					{
						GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
						GUILayout.Label("\t\tue: " + involvedUnit.CharacterName + " - bp: " + involvedUnit.Blueprint.CharacterName + " - bp: " + ((SimpleBlueprint)involvedUnit.Blueprint).name, Array.Empty<GUILayoutOption>());
						GUILayout.EndHorizontal();
					}
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					BlueprintUnit listener = Game.Instance.DialogController.CurrentCue.Listener;
					GUILayout.Label("CurrentCue.Listener.CharacterName: " + ((listener != null) ? listener.CharacterName : null), Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					GUILayout.Label("CurrentCue.Listener.name: " + ((SimpleBlueprint)(Game.Instance.DialogController.CurrentCue.Listener?)).name, Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					DialogSpeaker speaker = Game.Instance.DialogController.CurrentCue.Speaker;
					object obj2;
					if (speaker == null)
					{
						obj2 = null;
					}
					else
					{
						BlueprintUnit blueprint2 = speaker.Blueprint;
						obj2 = ((blueprint2 != null) ? blueprint2.CharacterName : null);
					}
					GUILayout.Label("CurrentCue.Speaker.Blueprint.CharacterName: " + (string)obj2, Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					DialogSpeaker speaker2 = Game.Instance.DialogController.CurrentCue.Speaker;
					GUILayout.Label("CurrentCue.Speaker.Blueprint.name: " + ((speaker2 == null) ? null : ((SimpleBlueprint)(speaker2.Blueprint?)).name), Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					DialogSpeaker speaker3 = Game.Instance.DialogController.CurrentCue.Speaker;
					object obj3;
					if (speaker3 == null)
					{
						obj3 = null;
					}
					else
					{
						BlueprintUnit blueprint3 = speaker3.Blueprint;
						obj3 = ((blueprint3 != null) ? blueprint3.CharacterName : null);
					}
					GUILayout.Label("CurrentCue.Speaker.Blueprint.CharacterName: " + (string)obj3, Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					GUILayout.Label("CurrentCue.TurnSpeaker: " + Game.Instance.DialogController.CurrentCue.TurnSpeaker, Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					GUILayout.Label("ActingUnit.CharacterName: ", array);
					UnitEntityData actingUnit = Game.Instance.DialogController.ActingUnit;
					GUILayout.Label((actingUnit != null) ? actingUnit.CharacterName : null, Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					UnitEntityData actingUnit2 = Game.Instance.DialogController.ActingUnit;
					object obj4;
					if (actingUnit2 == null)
					{
						obj4 = null;
					}
					else
					{
						BlueprintUnit blueprint4 = actingUnit2.Blueprint;
						obj4 = ((blueprint4 != null) ? blueprint4.CharacterName : null);
					}
					GUILayout.Label("ActingUnit.Blueprint.CharacterName: " + (string)obj4, Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					UnitEntityData actingUnit3 = Game.Instance.DialogController.ActingUnit;
					GUILayout.Label("ActingUnit.Blueprint.name: " + ((actingUnit3 == null) ? null : ((SimpleBlueprint)(actingUnit3.Blueprint?)).name), Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
					GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
					GUILayout.Label("_____________________________________________________", Array.Empty<GUILayoutOption>());
					GUILayout.EndHorizontal();
				}
				GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
				if (GUILayout.Button("Log full dialog diagnostics", (GUILayoutOption[])(object)new GUILayoutOption[2]
				{
					GUILayout.Width(200f),
					GUILayout.Height(20f)
				}))
				{
					CueShowData cueShowDatum3 = new CueShowData(Game.Instance.DialogController.CurrentCue, (IEnumerable<SkillCheckResult>)new List<SkillCheckResult>(), (IEnumerable<AlignmentShift>)new List<AlignmentShift>());
					EventBus.RaiseEvent<IDialogCueHandler>((Action<IDialogCueHandler>)delegate(IDialogCueHandler h)
					{
						h.HandleOnCueShow(cueShowDatum3);
					}, true);
					Log("--------------------------------------------------------------------------------------");
					if (companions.Contains(Game.Instance.DialogController.CurrentSpeakerName.cleanCharName()))
					{
						SetPortrait(RealCurrentSpeakerEntity(Game.Instance.DialogController.CurrentSpeakerName.cleanCharName()), pickUpOnly: true);
						Log("OnGui -> SetPortrait: " + CompanionPortraitPath);
						string text3 = "";
						if (Directory.Exists(CompanionPortraitPath))
						{
							if (Directory.GetFiles(Path.Combine(CompanionPortraitPath), "*.current").Length != 0)
							{
								text3 = Path.GetFileNameWithoutExtension(Directory.GetFiles(Path.Combine(CompanionPortraitPath), "*.current")[0]);
								Log("Manually set subdir found: " + text3);
								if (text3.Equals("root"))
								{
									text3 = "";
								}
							}
							else
							{
								text3 = "";
							}
						}
						if (File.Exists(Path.Combine(CompanionPortraitPath, text3, "Fulllength.png")))
						{
							Log("Found: " + Path.Combine(CompanionPortraitPath, text3, "Fulllength.png"));
						}
						else
						{
							Log("NOT Found: " + Path.Combine(CompanionPortraitPath, text3, "Fulllength.png"));
						}
						if (File.Exists(Path.Combine(CompanionPortraitPath, text3, "Medium.png")))
						{
							Log("Found: " + Path.Combine(CompanionPortraitPath, text3, "Medium.png"));
						}
						else
						{
							Log("NOT Found: " + Path.Combine(CompanionPortraitPath, text3, "Medium.png"));
						}
						if (File.Exists(Path.Combine(CompanionPortraitPath, text3, "Small.png")))
						{
							Log("Found: " + Path.Combine(CompanionPortraitPath, text3, "Small.png"));
						}
						else
						{
							Log("NOT Found: " + Path.Combine(CompanionPortraitPath, text3, "Small.png"));
						}
					}
					else
					{
						pickedUpDir = GetPortrait_Patch.GetUnitPortraitPath(Game.Instance.DialogController.CurrentSpeakerBlueprint);
						Log("OnGui -> GetUnitPortraitPath: " + NpcPortraitPath);
						if (File.Exists(Path.Combine(NpcPortraitPath, "Medium.png")))
						{
							Log("Found: " + Path.GetFullPath(Path.Combine(NpcPortraitPath, "Medium.png")));
						}
						else
						{
							Log("NOT Found: " + Path.GetFullPath(Path.Combine(NpcPortraitPath, "Medium.png")));
						}
						if (File.Exists(Path.Combine(NpcPortraitPath, "Small.png")))
						{
							Log("Found: " + Path.GetFullPath(Path.Combine(NpcPortraitPath, "Small.png")));
						}
						else
						{
							Log("NOT Found: " + Path.GetFullPath(Path.Combine(NpcPortraitPath, "Small.png")));
						}
					}
					Log("CurrentCue.Text: " + LocalizedString.op_Implicit(Game.Instance.DialogController.CurrentCue.Text));
					Log("CurrentCue.name: " + ((SimpleBlueprint)Game.Instance.DialogController.CurrentCue).name);
					Log("CurrentCue.Comment: " + ((BlueprintScriptableObject)Game.Instance.DialogController.CurrentCue).Comment);
					Log("CurrentCue.DisplayText: " + Game.Instance.DialogController.CurrentCue.DisplayText);
					BlueprintGuid assetGuid = ((SimpleBlueprint)Game.Instance.DialogController.CurrentCue).AssetGuid;
					Log("CurrentCue.AssetGuid: " + ((object)(*(BlueprintGuid*)(&assetGuid))/*cast due to .constrained prefix*/).ToString());
					assetGuid = ((SimpleBlueprint)Game.Instance.DialogController.Dialog).AssetGuid;
					Log("Dialog.AssetGuid: " + ((object)(*(BlueprintGuid*)(&assetGuid))/*cast due to .constrained prefix*/).ToString());
					Log("Dialog.Comment: " + ((BlueprintScriptableObject)Game.Instance.DialogController.Dialog).Comment);
					Log("Dialog.name: " + ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name);
					Log("Dialog.Type: " + ((object)System.Runtime.CompilerServices.Unsafe.As<DialogType, DialogType>(ref Game.Instance.DialogController.Dialog.Type)/*cast due to .constrained prefix*/).ToString());
					Log("CurrentSpeakerName: " + Game.Instance.DialogController.CurrentSpeakerName.cleanCharName());
					UnitEntityData currentSpeaker4 = Game.Instance.DialogController.CurrentSpeaker;
					Log("CurrentSpeaker.CharacterName.cleanCharName(): " + ((currentSpeaker4 != null) ? currentSpeaker4.CharacterName.cleanCharName() : null));
					UnitEntityData currentSpeaker5 = Game.Instance.DialogController.CurrentSpeaker;
					Log("CurrentSpeaker.Blueprint.AssetGuid: " + ((currentSpeaker5 != null) ? new BlueprintGuid?(((SimpleBlueprint)currentSpeaker5.Blueprint).AssetGuid) : ((BlueprintGuid?)null)).ToString());
					UnitEntityData currentSpeaker6 = Game.Instance.DialogController.CurrentSpeaker;
					object obj5;
					if (currentSpeaker6 == null)
					{
						obj5 = null;
					}
					else
					{
						PortraitData portrait = currentSpeaker6.Portrait;
						obj5 = ((portrait != null) ? portrait.CustomId : null);
					}
					Log("CurrentSpeaker.Portrait.CustomId: " + (string)obj5);
					Log("Answers: ");
					foreach (BlueprintAnswer answer in Game.Instance.DialogController.Answers)
					{
						assetGuid = ((SimpleBlueprint)answer).AssetGuid;
						Log("Answers.item.AssetGuid: " + ((object)(*(BlueprintGuid*)(&assetGuid))/*cast due to .constrained prefix*/).ToString());
						Log("Answers.item.DisplayText: " + answer.DisplayText);
						Log("Answers.item.name: " + ((SimpleBlueprint)answer).name);
						Log("Conditions: ");
						if (answer.ShowConditions.Conditions.Length != 0)
						{
							Condition[] conditions = answer.ShowConditions.Conditions;
							foreach (Condition val2 in conditions)
							{
								Log("ShowConditions.Conditions.item.name: " + ((Element)val2).name);
								Log("ShowConditions.Conditions.item.GetDescription: " + ((Element)val2).GetDescription());
								Log("ShowConditions.Conditions.item.ToString: " + ((object)val2).ToString());
								Log("ShowConditions.Conditions.item.GetType: " + ((object)val2).GetType());
							}
						}
					}
					Log("Inventory: ");
					UnitEntityData currentSpeaker7 = Game.Instance.DialogController.CurrentSpeaker;
					if (((currentSpeaker7 != null) ? currentSpeaker7.Inventory : null) != null)
					{
						foreach (ItemEntity item3 in Game.Instance.DialogController.CurrentSpeaker.Inventory)
						{
							Log("   item: " + item3.Name + " - " + ((object)item3.Blueprint.ItemType/*cast due to .constrained prefix*/).ToString() + " - " + item3.Blueprint.SubtypeName);
						}
					}
					Log("Body: ");
					UnitEntityData currentSpeaker8 = Game.Instance.DialogController.CurrentSpeaker;
					object obj6;
					if (currentSpeaker8 == null)
					{
						obj6 = null;
					}
					else
					{
						BlueprintUnit blueprint5 = currentSpeaker8.Blueprint;
						if (blueprint5 == null)
						{
							obj6 = null;
						}
						else
						{
							UnitBody body = blueprint5.Body;
							if (body == null)
							{
								obj6 = null;
							}
							else
							{
								BlueprintItemArmor armor = body.Armor;
								obj6 = ((armor != null) ? ((BlueprintItem)armor).NameForAcronym : null);
							}
						}
					}
					Log("CurrentSpeaker.Blueprint.Body.Armor: " + (string)obj6);
					UnitEntityData currentSpeaker9 = Game.Instance.DialogController.CurrentSpeaker;
					object obj7;
					if (currentSpeaker9 == null)
					{
						obj7 = null;
					}
					else
					{
						UnitBody body2 = currentSpeaker9.Blueprint.Body;
						if (body2 == null)
						{
							obj7 = null;
						}
						else
						{
							BlueprintItemEquipmentHead head = body2.Head;
							obj7 = ((head != null) ? ((BlueprintItem)head).NameForAcronym : null);
						}
					}
					Log("CurrentSpeaker.Blueprint.Body.Head: " + (string)obj7);
					UnitEntityData currentSpeaker10 = Game.Instance.DialogController.CurrentSpeaker;
					object obj8;
					if (currentSpeaker10 == null)
					{
						obj8 = null;
					}
					else
					{
						BlueprintUnit blueprint6 = currentSpeaker10.Blueprint;
						if (blueprint6 == null)
						{
							obj8 = null;
						}
						else
						{
							UnitBody body3 = blueprint6.Body;
							if (body3 == null)
							{
								obj8 = null;
							}
							else
							{
								BlueprintItemEquipmentHand primaryHand = body3.PrimaryHand;
								obj8 = ((primaryHand != null) ? ((BlueprintItem)primaryHand).NameForAcronym : null);
							}
						}
					}
					Log("CurrentSpeaker.Blueprint.Body.PrimaryHand: " + (string)obj8);
					UnitEntityData currentSpeaker11 = Game.Instance.DialogController.CurrentSpeaker;
					object obj9;
					if (currentSpeaker11 == null)
					{
						obj9 = null;
					}
					else
					{
						BlueprintUnit blueprint7 = currentSpeaker11.Blueprint;
						if (blueprint7 == null)
						{
							obj9 = null;
						}
						else
						{
							UnitBody body4 = blueprint7.Body;
							if (body4 == null)
							{
								obj9 = null;
							}
							else
							{
								BlueprintItemEquipmentHand secondaryHand = body4.SecondaryHand;
								obj9 = ((secondaryHand != null) ? ((BlueprintItem)secondaryHand).NameForAcronym : null);
							}
						}
					}
					Log("CurrentSpeaker.Blueprint.Body.SecondaryHand: " + (string)obj9);
					UnitEntityData currentSpeaker12 = Game.Instance.DialogController.CurrentSpeaker;
					Log("CurrentSpeaker.Blueprint.name: " + ((currentSpeaker12 == null) ? null : ((SimpleBlueprint)(currentSpeaker12.Blueprint?)).name));
					UnitEntityData currentSpeaker13 = Game.Instance.DialogController.CurrentSpeaker;
					Log("CurrentSpeaker.Blueprint.AssetGuid: " + ((currentSpeaker13 == null) ? ((BlueprintGuid?)null) : ((SimpleBlueprint)(currentSpeaker13.Blueprint?)).AssetGuid).ToString());
					UnitEntityData currentSpeaker14 = Game.Instance.DialogController.CurrentSpeaker;
					object obj10;
					if (currentSpeaker14 == null)
					{
						obj10 = null;
					}
					else
					{
						BlueprintUnit blueprint8 = currentSpeaker14.Blueprint;
						if (blueprint8 == null)
						{
							obj10 = null;
						}
						else
						{
							BlueprintRace race = blueprint8.Race;
							obj10 = ((race != null) ? ((BlueprintUnitFact)race).Name : null);
						}
					}
					Log("CurrentSpeaker.Blueprint.Race: " + (string)obj10);
					UnitEntityData currentSpeaker15 = Game.Instance.DialogController.CurrentSpeaker;
					object obj11;
					if (currentSpeaker15 == null)
					{
						obj11 = null;
					}
					else
					{
						BlueprintUnit blueprint9 = currentSpeaker15.Blueprint;
						obj11 = ((blueprint9 == null) ? null : ((SimpleBlueprint)(blueprint9.Type?)).name);
					}
					Log("CurrentSpeaker.Blueprint.Type: " + (string)obj11);
					UnitEntityData currentSpeaker16 = Game.Instance.DialogController.CurrentSpeaker;
					Log("CurrentSpeaker.Blueprint.Gender: " + ((currentSpeaker16 == null) ? ((Gender?)null) : currentSpeaker16.Blueprint?.Gender).ToString());
					if (Game.Instance.DialogController.CurrentSpeaker != (UnitDescriptor)null && Game.Instance.DialogController.CurrentSpeaker.Progression != null)
					{
						Game.Instance.DialogController.CurrentSpeaker.Progression.Classes.ForEach(delegate(ClassData n)
						{
							Log("CurrentSpeaker.Blueprint.Class: " + ((SimpleBlueprint)n.CharacterClass).name);
						});
					}
					UnitEntityData currentSpeaker17 = Game.Instance.DialogController.CurrentSpeaker;
					Log("CurrentSpeaker.Blueprint.Alignment: " + ((currentSpeaker17 == null) ? ((Alignment?)null) : currentSpeaker17.Blueprint?.Alignment).ToString());
					UnitEntityData currentSpeaker18 = Game.Instance.DialogController.CurrentSpeaker;
					object obj12;
					if (currentSpeaker18 == null)
					{
						obj12 = null;
					}
					else
					{
						BlueprintUnit blueprint10 = currentSpeaker18.Blueprint;
						obj12 = ((blueprint10 != null) ? blueprint10.Faction : null);
					}
					Log("CurrentSpeaker.Blueprint.Faction: " + obj12);
					UnitEntityData currentSpeaker19 = Game.Instance.DialogController.CurrentSpeaker;
					object obj13;
					if (currentSpeaker19 == null)
					{
						obj13 = null;
					}
					else
					{
						BlueprintUnit blueprint11 = currentSpeaker19.Blueprint;
						obj13 = ((blueprint11 != null) ? ((SimpleBlueprint)blueprint11.PortraitSafe).name : null);
					}
					Log("CurrentSpeaker.Blueprint.PortraitSafe.name: " + (string)obj13);
					UnitEntityData currentSpeaker20 = Game.Instance.DialogController.CurrentSpeaker;
					bool? obj14;
					if (currentSpeaker20 == null)
					{
						obj14 = null;
					}
					else
					{
						UnitBody body5 = currentSpeaker20.Body;
						obj14 = ((body5 != null) ? new bool?(body5.IsPolymorphed) : ((bool?)null));
					}
					bool? flag = obj14;
					Log("CurrentSpeaker->isPolymorphed: " + flag);
					if (Game.Instance.DialogController.CurrentSpeaker != (UnitDescriptor)null && Game.Instance.DialogController.CurrentSpeaker.Body != null && Game.Instance.DialogController.CurrentSpeaker.Body.IsPolymorphed)
					{
						Log("---------------------Poly start");
						EntityFactComponent runtime = Game.Instance.DialogController.CurrentSpeaker.GetActivePolymorph().Runtime;
						object obj15;
						if (runtime == null)
						{
							obj15 = null;
						}
						else
						{
							BlueprintComponent sourceBlueprintComponent = runtime.SourceBlueprintComponent;
							obj15 = ((sourceBlueprintComponent == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent.OwnerBlueprint?)).name);
						}
						Log("CurrentSpeaker.GetActivePolymorph().Runtime?.SourceBlueprintComponent.OwnerBlueprint.name: " + (string)obj15);
						EntityFactComponent runtime2 = Game.Instance.DialogController.CurrentSpeaker.GetActivePolymorph().Runtime;
						object obj16;
						if (runtime2 == null)
						{
							obj16 = null;
						}
						else
						{
							BlueprintComponent sourceBlueprintComponent2 = runtime2.SourceBlueprintComponent;
							if (sourceBlueprintComponent2 == null)
							{
								obj16 = null;
							}
							else
							{
								BlueprintScriptableObject ownerBlueprint = sourceBlueprintComponent2.OwnerBlueprint;
								if (ownerBlueprint == null)
								{
									obj16 = null;
								}
								else
								{
									Polymorph component = BlueprintExtenstions.GetComponent<Polymorph>(ownerBlueprint);
									obj16 = ((component == null) ? null : ((SimpleBlueprint)(component.Portrait?)).name);
								}
							}
						}
						Log("CurrentSpeaker.GetActivePolymorph().Runtime?.SourceBlueprintComponent.OwnerBlueprint.GetComponent<Polymorph>().Portrait.name: " + (string)obj16);
						EntityFactComponent runtime3 = Game.Instance.DialogController.CurrentSpeaker.GetActivePolymorph().Runtime;
						object obj17;
						if (runtime3 == null)
						{
							obj17 = null;
						}
						else
						{
							BlueprintComponent sourceBlueprintComponent3 = runtime3.SourceBlueprintComponent;
							if (sourceBlueprintComponent3 == null)
							{
								obj17 = null;
							}
							else
							{
								BlueprintScriptableObject ownerBlueprint2 = sourceBlueprintComponent3.OwnerBlueprint;
								obj17 = ((ownerBlueprint2 != null) ? ownerBlueprint2.ComponentsArray : null);
							}
						}
						BlueprintComponent[] array2 = (BlueprintComponent[])obj17;
						foreach (BlueprintComponent val3 in array2)
						{
							Log("   " + val3.name + " - " + ((object)val3).GetType());
						}
						Polymorph component2 = Game.Instance.DialogController.CurrentSpeaker.GetActivePolymorph().Component;
						if (((component2 != null) ? ((BlueprintReferenceBase)component2.m_Portrait).GetBlueprint() : null) != null)
						{
							SimpleBlueprint blueprint12 = ((BlueprintReferenceBase)Game.Instance.DialogController.CurrentSpeaker.GetActivePolymorph().Component.m_Portrait).GetBlueprint();
							Log("Game.Instance.DialogController.CurrentSpeaker.GetActivePolymorph().Component.m_Portrait.name: " + ((blueprint12 is BlueprintPortrait) ? blueprint12 : null).name);
						}
						Log("Game.Instance.DialogController.CurrentSpeaker.GetActivePolymorph().Runtime.Owner.View.name: " + ((Object)Game.Instance.DialogController.CurrentSpeaker.GetActivePolymorph().Runtime.Owner.View).name);
						BlueprintUnit replaceBlueprintForInspection = Game.Instance.DialogController.CurrentSpeaker.ReplaceBlueprintForInspection;
						Log("CurrentSpeaker.ReplaceBlueprintForInspection.CharacterName.cleanCharName(): " + ((replaceBlueprintForInspection != null) ? replaceBlueprintForInspection.CharacterName.cleanCharName() : null));
						Log("CurrentSpeaker.ReplaceBlueprintForInspection.name: " + ((SimpleBlueprint)(Game.Instance.DialogController.CurrentSpeaker.ReplaceBlueprintForInspection?)).name);
						BlueprintUnit replaceBlueprintForInspection2 = Game.Instance.DialogController.CurrentSpeaker.ReplaceBlueprintForInspection;
						Log("CurrentSpeaker.ReplaceBlueprintForInspection.Race: " + (object)((replaceBlueprintForInspection2 != null) ? replaceBlueprintForInspection2.Race : null));
						BlueprintUnit replaceBlueprintForInspection3 = Game.Instance.DialogController.CurrentSpeaker.ReplaceBlueprintForInspection;
						Log("CurrentSpeaker.ReplaceBlueprintForInspection.Type: " + ((replaceBlueprintForInspection3 == null) ? null : ((SimpleBlueprint)(replaceBlueprintForInspection3.Type?)).name));
						Log("CurrentSpeaker.ReplaceBlueprintForInspection.Alignment: " + (Game.Instance.DialogController.CurrentSpeaker.ReplaceBlueprintForInspection?.Alignment).ToString());
						BlueprintUnit replaceBlueprintForInspection4 = Game.Instance.DialogController.CurrentSpeaker.ReplaceBlueprintForInspection;
						Log("CurrentSpeaker.ReplaceBlueprintForInspection.Faction: " + (object)((replaceBlueprintForInspection4 != null) ? replaceBlueprintForInspection4.Faction : null));
						Log("Inventory: ");
						if (Game.Instance.DialogController.CurrentSpeaker.ReplaceBlueprintForInspection != null)
						{
							BlueprintItemReference[] array3 = Game.Instance.DialogController.CurrentSpeaker.ReplaceBlueprintForInspection?.m_StartingInventory;
							foreach (BlueprintItemReference val4 in array3)
							{
								Log("   item: " + ((BlueprintReference<BlueprintItem>)(object)val4).NameSafe() + " - " + ((SimpleBlueprint)(BlueprintItem)((BlueprintReferenceBase)val4).GetBlueprint()).name + " - " + ((object)((BlueprintItem)((BlueprintReferenceBase)val4).GetBlueprint()).ItemType/*cast due to .constrained prefix*/).ToString() + " - " + ((BlueprintItem)((BlueprintReferenceBase)val4).GetBlueprint()).SubtypeName);
							}
						}
						Log("Body: ");
						BlueprintUnit replaceBlueprintForInspection5 = Game.Instance.DialogController.CurrentSpeaker.ReplaceBlueprintForInspection;
						object obj18;
						if (replaceBlueprintForInspection5 == null)
						{
							obj18 = null;
						}
						else
						{
							UnitBody body6 = replaceBlueprintForInspection5.Body;
							if (body6 == null)
							{
								obj18 = null;
							}
							else
							{
								BlueprintItemArmor armor2 = body6.Armor;
								obj18 = ((armor2 != null) ? ((BlueprintItem)armor2).NameForAcronym : null);
							}
						}
						Log("CurrentSpeaker.ReplaceBlueprintForInspection.Body.Armor: " + (string)obj18);
						BlueprintUnit replaceBlueprintForInspection6 = Game.Instance.DialogController.CurrentSpeaker.ReplaceBlueprintForInspection;
						object obj19;
						if (replaceBlueprintForInspection6 == null)
						{
							obj19 = null;
						}
						else
						{
							UnitBody body7 = replaceBlueprintForInspection6.Body;
							if (body7 == null)
							{
								obj19 = null;
							}
							else
							{
								BlueprintItemEquipmentHead head2 = body7.Head;
								obj19 = ((head2 != null) ? ((BlueprintItem)head2).NameForAcronym : null);
							}
						}
						Log("CurrentSpeaker.ReplaceBlueprintForInspection.Body.Head: " + (string)obj19);
						BlueprintUnit replaceBlueprintForInspection7 = Game.Instance.DialogController.CurrentSpeaker.ReplaceBlueprintForInspection;
						object obj20;
						if (replaceBlueprintForInspection7 == null)
						{
							obj20 = null;
						}
						else
						{
							UnitBody body8 = replaceBlueprintForInspection7.Body;
							if (body8 == null)
							{
								obj20 = null;
							}
							else
							{
								BlueprintItemEquipmentHand primaryHand2 = body8.PrimaryHand;
								obj20 = ((primaryHand2 != null) ? ((BlueprintItem)primaryHand2).NameForAcronym : null);
							}
						}
						Log("CurrentSpeaker.ReplaceBlueprintForInspection.Body.PrimaryHand: " + (string)obj20);
						BlueprintUnit replaceBlueprintForInspection8 = Game.Instance.DialogController.CurrentSpeaker.ReplaceBlueprintForInspection;
						object obj21;
						if (replaceBlueprintForInspection8 == null)
						{
							obj21 = null;
						}
						else
						{
							UnitBody body9 = replaceBlueprintForInspection8.Body;
							if (body9 == null)
							{
								obj21 = null;
							}
							else
							{
								BlueprintItemEquipmentHand secondaryHand2 = body9.SecondaryHand;
								obj21 = ((secondaryHand2 != null) ? ((BlueprintItem)secondaryHand2).NameForAcronym : null);
							}
						}
						Log("CurrentSpeaker.ReplaceBlueprintForInspection.Body.SecondaryHand: " + (string)obj21);
						Log("GetSubscribingUnit().Blueprint.CharacterName.cleanCharName(): " + Game.Instance.DialogController.CurrentSpeaker.GetActivePolymorph().Runtime.GetSubscribingUnit().Blueprint.CharacterName.cleanCharName());
						Log("GetSubscribingUnit().Blueprint.name: " + ((SimpleBlueprint)Game.Instance.DialogController.CurrentSpeaker.GetActivePolymorph().Runtime.GetSubscribingUnit().Blueprint).name);
						Log("GetSubscribingUnit().Blueprint.PortraitSafe.name: " + ((SimpleBlueprint)Game.Instance.DialogController.CurrentSpeaker.GetActivePolymorph().Runtime.GetSubscribingUnit().Blueprint.PortraitSafe).name);
						Log("---------------------Polymorph end");
					}
					BlueprintUnit currentSpeakerBlueprint2 = Game.Instance.DialogController.CurrentSpeakerBlueprint;
					Log("CurrentSpeakerBlueprint.CharacterName.cleanCharName(): " + ((currentSpeakerBlueprint2 != null) ? currentSpeakerBlueprint2.CharacterName.cleanCharName() : null));
					Log("CurrentSpeakerBlueprint.name: " + ((SimpleBlueprint)(Game.Instance.DialogController.CurrentSpeakerBlueprint?)).name);
					Log("CurrentSpeakerBlueprint.AssetGuid: " + (((SimpleBlueprint)(Game.Instance.DialogController.CurrentSpeakerBlueprint?)).AssetGuid).ToString());
					BlueprintUnit currentSpeakerBlueprint3 = Game.Instance.DialogController.CurrentSpeakerBlueprint;
					Log("CurrentSpeakerBlueprint.Name: " + ((currentSpeakerBlueprint3 != null) ? ((BlueprintUnitFact)currentSpeakerBlueprint3).Name : null));
					BlueprintUnit currentSpeakerBlueprint4 = Game.Instance.DialogController.CurrentSpeakerBlueprint;
					Log("CurrentSpeakerBlueprint.Race: " + (object)((currentSpeakerBlueprint4 != null) ? currentSpeakerBlueprint4.Race : null));
					BlueprintUnit currentSpeakerBlueprint5 = Game.Instance.DialogController.CurrentSpeakerBlueprint;
					Log("CurrentSpeakerBlueprint.Type: " + ((currentSpeakerBlueprint5 == null) ? null : ((SimpleBlueprint)(currentSpeakerBlueprint5.Type?)).name));
					Log("CurrentSpeakerBlueprint.Gender: " + (Game.Instance.DialogController.CurrentSpeakerBlueprint?.Gender).ToString());
					Log("CurrentSpeakerBlueprint.Alignment: " + (Game.Instance.DialogController.CurrentSpeakerBlueprint?.Alignment).ToString());
					BlueprintUnit currentSpeakerBlueprint6 = Game.Instance.DialogController.CurrentSpeakerBlueprint;
					Log("CurrentSpeakerBlueprint.Faction: " + (object)((currentSpeakerBlueprint6 != null) ? currentSpeakerBlueprint6.Faction : null));
					BlueprintUnit currentSpeakerBlueprint7 = Game.Instance.DialogController.CurrentSpeakerBlueprint;
					Log("CurrentSpeakerBlueprint.PortraitSafe.name: " + ((currentSpeakerBlueprint7 != null) ? ((SimpleBlueprint)currentSpeakerBlueprint7.PortraitSafe).name : null));
					UnitEntityData firstSpeaker = Game.Instance.DialogController.FirstSpeaker;
					Log("FirstSpeaker.CharacterName.cleanCharName(): " + ((firstSpeaker != null) ? firstSpeaker.CharacterName.cleanCharName() : null));
					Log("m_CustomSpeakerName: " + Game.Instance.DialogController.m_CustomSpeakerName);
					UnitEntityData actingUnit4 = Game.Instance.DialogController.ActingUnit;
					Log("ActingUnit.CharacterName.cleanCharName(): " + ((actingUnit4 != null) ? actingUnit4.CharacterName.cleanCharName() : null));
				}
				GUILayout.EndHorizontal();
			}
		}
		GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
		GUILayout.Label("_____________________________________________________", Array.Empty<GUILayoutOption>());
		GUILayout.EndHorizontal();
		GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
		GUILayout.Label("Advanced", boldStyle, Array.Empty<GUILayoutOption>());
		GUILayout.EndHorizontal();
		settings.ManageCompanions = GUILayout.Toggle(settings.ManageCompanions, "Let the mod manage the portraits of main char, companions, and mercenaries.", (GUILayoutOption[])(object)new GUILayoutOption[0]);
		settings.AutoBackup = GUILayout.Toggle(settings.AutoBackup, "Keep game defaults auto backed up in 'Backup of Game Default Portraits' of each subdir.", (GUILayoutOption[])(object)new GUILayoutOption[0]);
		settings.AutoSecret = GUILayout.Toggle(settings.AutoSecret, "Extract and use the turn based portraits of NPC-s in dialogs where available.", (GUILayoutOption[])(object)new GUILayoutOption[0]);
		settings.RightverseGroupPortraits = GUILayout.Toggle(settings.RightverseGroupPortraits, "Show current party members' portraits first in places like cities on group portrait bar", (GUILayoutOption[])(object)new GUILayoutOption[0]);
		if (!showExtra)
		{
			GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
			if (GUILayout.Button("Show extra options", (GUILayoutOption[])(object)new GUILayoutOption[2]
			{
				GUILayout.Width(200f),
				GUILayout.Height(20f)
			}))
			{
				showExtra = true;
			}
			GUILayout.EndHorizontal();
			return;
		}
		GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
		if (GUILayout.Button("Close", (GUILayoutOption[])(object)new GUILayoutOption[2]
		{
			GUILayout.Width(200f),
			GUILayout.Height(20f)
		}))
		{
			showExtra = false;
		}
		GUILayout.EndHorizontal();
		settings.DollroomHalo = GUILayout.Toggle(settings.DollroomHalo, "Show aasimar halo in Inventory window (if they have the ability and it's turned on)", (GUILayoutOption[])(object)new GUILayoutOption[0]);
		if (isLoadedGame)
		{
			settings.ArueHalo = GUILayout.Toggle(settings.ArueHalo, "Arueshalae needs a halo!", (GUILayoutOption[])(object)new GUILayoutOption[0]);
			if (settings.ArueHalo)
			{
				ArueAddHalo();
				foreach (UnitEntityData item4 in Game.Instance.Player.Party)
				{
					if (item4.CharacterName.cleanCharName() == ArueName)
					{
						BlueprintActivatableAbility val5 = ResourcesLibrary.TryGetBlueprint<BlueprintActivatableAbility>("248bbb747c273684d9fdf2ed38935def");
						if (UnitHelper.HasFact(item4, (BlueprintFact)(object)val5))
						{
							UnitHelper.GetFact<ActivatableAbility>(item4, (BlueprintUnitFact)(object)val5).IsOn = true;
						}
						break;
					}
				}
			}
			if (!settings.ArueHalo)
			{
				ArueAddHalo();
			}
		}
		else
		{
			GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
			GUILayout.Label("Load a game to see Arueshalae halo option here", Array.Empty<GUILayoutOption>());
			GUILayout.EndHorizontal();
		}
		if (isLoadedGame)
		{
			settings.EmberHalo = GUILayout.Toggle(settings.EmberHalo, "Ember is a living saint, she should have a halo too", (GUILayoutOption[])(object)new GUILayoutOption[0]);
			if (settings.EmberHalo)
			{
				EmberAddHalo();
				foreach (UnitEntityData item5 in Game.Instance.Player.Party)
				{
					if (item5.CharacterName.cleanCharName() == EmberName)
					{
						BlueprintActivatableAbility val6 = ResourcesLibrary.TryGetBlueprint<BlueprintActivatableAbility>("248bbb747c273684d9fdf2ed38935def");
						if (UnitHelper.HasFact(item5, (BlueprintFact)(object)val6))
						{
							UnitHelper.GetFact<ActivatableAbility>(item5, (BlueprintUnitFact)(object)val6).IsOn = true;
						}
						break;
					}
				}
			}
			if (!settings.EmberHalo)
			{
				EmberAddHalo();
			}
		}
		else
		{
			GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
			GUILayout.Label("Load a game to see Ember halo option here", Array.Empty<GUILayoutOption>());
			GUILayout.EndHorizontal();
		}
		GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
		settings.SwarmRiddance = GUILayout.Toggle(settings.SwarmRiddance, " Remove retarded swarm dialog options", (GUILayoutOption[])(object)new GUILayoutOption[0]);
		GUILayout.Label("Answers with swarm option: " + swarmAnswers, Array.Empty<GUILayoutOption>());
		if (swarmAnswers > 0 && !swarmCleanRunning && settings.SwarmRiddance)
		{
			swarmCleanRunning = true;
			GetRidOfSwarm();
			CountSwarm();
			swarmCleanRunning = false;
		}
		GUILayout.EndHorizontal();
		GUILayout.BeginHorizontal(Array.Empty<GUILayoutOption>());
		GUILayout.Label("     (Good if you have ToyBox show all dialogs ON, but you don't want to always see \"Eat her?\")", Array.Empty<GUILayoutOption>());
		GUILayout.EndHorizontal();
	}

	public static void CountSwarm()
	{
		//IL_00a7: Unknown result type (might be due to invalid IL or missing references)
		//IL_00ae: Invalid comparison between Unknown and I4
		//IL_00b2: Unknown result type (might be due to invalid IL or missing references)
		//IL_00b9: Invalid comparison between Unknown and I4
		swarmAnswers = 0;
		foreach (Entry entry in Utilities.GetAllBlueprints().Entries)
		{
			if (entry == null || !(entry.Type != null) || Utils.IsNullOrEmpty(entry.Type.Name) || entry.Guid == null || !entry.Type.Name.Equals("BlueprintAnswersList"))
			{
				continue;
			}
			BlueprintAnswersList val = ResourcesLibrary.TryGetBlueprint<BlueprintAnswersList>(entry.Guid);
			if (val == null)
			{
				continue;
			}
			foreach (BlueprintAnswerBaseReference answer in val.Answers)
			{
				SimpleBlueprint blueprint = ((BlueprintReferenceBase)answer).GetBlueprint();
				BlueprintAnswerBase val2 = (BlueprintAnswerBase)(object)((blueprint is BlueprintAnswerBase) ? blueprint : null);
				if (val2 != null && ((int)val2.MythicRequirement == 9 || (int)val2.MythicRequirement == 18))
				{
					swarmAnswers++;
				}
			}
		}
	}

	public static void GetRidOfSwarm()
	{
		//IL_00b2: Unknown result type (might be due to invalid IL or missing references)
		//IL_00b9: Invalid comparison between Unknown and I4
		//IL_00bd: Unknown result type (might be due to invalid IL or missing references)
		//IL_00c4: Invalid comparison between Unknown and I4
		foreach (Entry entry in Utilities.GetAllBlueprints().Entries)
		{
			if (entry == null || !(entry.Type != null) || Utils.IsNullOrEmpty(entry.Type.Name) || !entry.Type.Name.Equals("BlueprintAnswersList") || entry.Guid == null)
			{
				continue;
			}
			BlueprintAnswersList val = ResourcesLibrary.TryGetBlueprint<BlueprintAnswersList>(entry.Guid);
			if (val == null)
			{
				continue;
			}
			List<BlueprintAnswerBaseReference> list = new List<BlueprintAnswerBaseReference>();
			foreach (BlueprintAnswerBaseReference answer in val.Answers)
			{
				SimpleBlueprint blueprint = ((BlueprintReferenceBase)answer).GetBlueprint();
				BlueprintAnswerBase val2 = (BlueprintAnswerBase)(object)((blueprint is BlueprintAnswerBase) ? blueprint : null);
				if (val2 != null && ((int)val2.MythicRequirement == 9 || (int)val2.MythicRequirement == 18) && !list.Contains(answer))
				{
					list.Add(answer);
					swarmAnswers++;
				}
			}
			if (list.Count() <= 0 || val.Answers.Count() <= 0)
			{
				continue;
			}
			foreach (BlueprintAnswerBaseReference item in list)
			{
				val.Answers.Remove(item);
			}
		}
		Log("Removed " + swarmAnswers + " swarn dialog options");
	}

	public static void loctel()
	{
	}

	public static void saveNpcPortraits()
	{
		//IL_000b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0010: Unknown result type (might be due to invalid IL or missing references)
		//IL_001c: Expected O, but got Unknown
		string path = BundlesLoadService.BundlesPath("cheatdata.json");
		BlueprintList val = new BlueprintList
		{
			Entries = new List<Entry>()
		};
		if (File.Exists(path))
		{
			val = JsonUtility.FromJson<BlueprintList>(File.ReadAllText(path));
		}
		Dictionary<string, string> dictionary = new Dictionary<string, string>();
		string npcPortraitsDirectory = GetNpcPortraitsDirectory();
		foreach (Entry entry in val.Entries)
		{
			if (!entry.TypeFullName.Equals("Kingmaker.DialogSystem.Blueprints.BlueprintCue"))
			{
				continue;
			}
			BlueprintCue blueprintByGuid = Utilities.GetBlueprintByGuid<BlueprintCue>(entry.Guid);
			string text = "";
			if (blueprintByGuid.Speaker != null && blueprintByGuid.Speaker.Blueprint != null && !Utils.IsNullOrEmpty(((SimpleBlueprint)blueprintByGuid.Speaker.Blueprint).name))
			{
				text = blueprintByGuid.Speaker.Blueprint.CharacterName.cleanCharName();
				if (blueprintByGuid.Speaker.Blueprint.CharacterName.cleanCharName().Equals(AstyName))
				{
					Directory.CreateDirectory(Path.Combine(npcPortraitsDirectory, AstyName));
					text = AstyName + " - Drow";
				}
				if (blueprintByGuid.Speaker.Blueprint.CharacterName.cleanCharName().Equals(TranName))
				{
					Directory.CreateDirectory(Path.Combine(npcPortraitsDirectory, TranName));
					text = TranName + " - Drow";
				}
				if (blueprintByGuid.Speaker.Blueprint.CharacterName.cleanCharName().Equals(VelhmName))
				{
					Directory.CreateDirectory(Path.Combine(npcPortraitsDirectory, VelhmName));
					text = VelhmName + " - Drow";
				}
				if (blueprintByGuid.Speaker.Blueprint.CharacterName.cleanCharName().Equals(IrabethName))
				{
					Directory.CreateDirectory(Path.Combine(npcPortraitsDirectory, IrabethName));
					text = IrabethName + " - Scar";
				}
				if (!dictionary.ContainsKey(((SimpleBlueprint)blueprintByGuid.Speaker.Blueprint).name) && !companions.Contains(blueprintByGuid.Speaker.Blueprint.CharacterName.cleanCharName()) && !blueprintByGuid.Speaker.Blueprint.IsCompanion)
				{
					try
					{
						dictionary.Add(((SimpleBlueprint)blueprintByGuid.Speaker.Blueprint).name, text);
						string text2 = Path.Combine(npcPortraitsDirectory, text);
						if (((SimpleBlueprint)blueprintByGuid.Speaker.Blueprint).name != blueprintByGuid.Speaker.Blueprint.CharacterName.cleanCharName())
						{
							SaveOriginals(blueprintByGuid.Speaker.Blueprint, Path.Combine(text2, ((SimpleBlueprint)blueprintByGuid.Speaker.Blueprint).name));
						}
						else
						{
							SaveOriginals(blueprintByGuid.Speaker.Blueprint, text2);
						}
						portraitCounter++;
					}
					catch (Exception ex)
					{
						failCounter++;
						DebugError(ex);
					}
				}
			}
			if (blueprintByGuid.Listener == null || Utils.IsNullOrEmpty(((SimpleBlueprint)blueprintByGuid.Listener).name))
			{
				continue;
			}
			try
			{
				text = blueprintByGuid.Listener.CharacterName.cleanCharName();
				if (blueprintByGuid.Listener.CharacterName.cleanCharName().Equals(AstyName))
				{
					Directory.CreateDirectory(Path.Combine(npcPortraitsDirectory, AstyName));
					text = AstyName + " - Drow";
				}
				if (blueprintByGuid.Listener.CharacterName.cleanCharName().Equals(TranName))
				{
					Directory.CreateDirectory(Path.Combine(npcPortraitsDirectory, TranName));
					text = TranName + " - Drow";
				}
				if (blueprintByGuid.Listener.CharacterName.cleanCharName().Equals(VelhmName))
				{
					Directory.CreateDirectory(Path.Combine(npcPortraitsDirectory, VelhmName));
					text = VelhmName + " - Drow";
				}
				if (blueprintByGuid.Listener.CharacterName.cleanCharName().Equals(IrabethName))
				{
					Directory.CreateDirectory(Path.Combine(npcPortraitsDirectory, IrabethName));
					text = IrabethName + " - Scar";
				}
				if (!dictionary.ContainsKey(((SimpleBlueprint)blueprintByGuid.Listener).name) && !companions.Contains(blueprintByGuid.Listener.CharacterName.cleanCharName()) && !blueprintByGuid.Listener.IsCompanion)
				{
					dictionary.Add(((SimpleBlueprint)blueprintByGuid.Listener).name, text);
					string text3 = Path.Combine(npcPortraitsDirectory, text);
					if (((SimpleBlueprint)blueprintByGuid.Listener).name != blueprintByGuid.Listener.CharacterName.cleanCharName())
					{
						SaveOriginals(blueprintByGuid.Listener, Path.Combine(text3, ((SimpleBlueprint)blueprintByGuid.Listener).name));
					}
					else
					{
						SaveOriginals(blueprintByGuid.Listener, text3);
					}
					portraitCounter++;
				}
			}
			catch (Exception ex2)
			{
				failCounter++;
				DebugError(ex2);
			}
		}
		DebugLog(dictionary.Count().ToString());
	}

	public static void makeNpcDirs()
	{
		//IL_000b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0010: Unknown result type (might be due to invalid IL or missing references)
		//IL_001c: Expected O, but got Unknown
		string path = BundlesLoadService.BundlesPath("cheatdata.json");
		BlueprintList val = new BlueprintList
		{
			Entries = new List<Entry>()
		};
		if (File.Exists(path))
		{
			val = JsonUtility.FromJson<BlueprintList>(File.ReadAllText(path));
		}
		new Dictionary<string, string>();
		GetNpcPortraitsDirectory();
		foreach (Entry entry in val.Entries)
		{
			_ = entry;
		}
	}

	public static IEnumerable<T> MoveUp<T>(this IEnumerable<T> enumerable, int itemIndex)
	{
		int i = 0;
		IEnumerator<T> enumerator = enumerable.GetEnumerator();
		while (enumerator.MoveNext())
		{
			i++;
			if (itemIndex.Equals(i))
			{
				T previous = enumerator.Current;
				if (enumerator.MoveNext())
				{
					yield return enumerator.Current;
				}
				yield return previous;
				break;
			}
			yield return enumerator.Current;
		}
		while (enumerator.MoveNext())
		{
			yield return enumerator.Current;
		}
	}

	private static void refreshPortraits()
	{
		//IL_003e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0043: Unknown result type (might be due to invalid IL or missing references)
		foreach (UnitEntityData allCharacter in Game.Instance.Player.AllCharacters)
		{
			Game.Instance.SelectionCharacter.SetSelected(allCharacter);
			UnitReference value = Game.Instance.SelectionCharacter.SelectedUnit.Value;
			((UnitReference)(ref value)).Value.UISettings.SetPortrait(SetPortrait(allCharacter, pickUpOnly: false));
		}
	}

	public static string GetCompanionDirName(string characterName)
	{
		//IL_00d9: Unknown result type (might be due to invalid IL or missing references)
		//IL_00de: Unknown result type (might be due to invalid IL or missing references)
		//IL_0186: Unknown result type (might be due to invalid IL or missing references)
		//IL_018b: Unknown result type (might be due to invalid IL or missing references)
		UnitEntityData val = LinqExtensions.FirstOrDefault<UnitEntityData>((IList<UnitEntityData>)Game.Instance.Player.AllCharacters, (Func<UnitEntityData, bool>)((UnitEntityData c) => c.CharacterName.cleanCharName().Equals(characterName)));
		if (val == (UnitDescriptor)null && (characterName.Equals(GalfreyName) || characterName.Equals(CiarName) || characterName.Equals(ArueName) || characterName.Equals(WoljifName) || characterName.Equals(StauntonName) || characterName.Equals(KestoglyrName) || characterName.Equals(NenioName) || characterName.Equals(SendriName)))
		{
			EntityPoolEnumerator<UnitEntityData> enumerator = Game.Instance.State.Units.GetEnumerator();
			try
			{
				while (enumerator.MoveNext())
				{
					UnitEntityData current = enumerator.Current;
					if (current.CharacterName.Equals(characterName))
					{
						val = current;
					}
				}
			}
			finally
			{
				((IDisposable)enumerator/*cast due to .constrained prefix*/).Dispose();
			}
		}
		if (val != (UnitDescriptor)null)
		{
			string text = val.CharacterName.cleanCharName();
			if (text.Equals(ArueName) && ((SimpleBlueprint)val.Descriptor.Progression.Race).name.ToLower().Contains("succubusrace"))
			{
				text += " - Evil";
			}
			if (text.Equals(CiarName) && (((object)val.Alignment.ValueRaw/*cast due to .constrained prefix*/).ToString().ToLower().Contains("evil") || val.Descriptor.IsUndead))
			{
				text += " - Undead";
			}
			if (text.Equals(GalfreyName))
			{
				if (((object)System.Runtime.CompilerServices.Unsafe.As<Alignment, Alignment>(ref val.Blueprint.Alignment)/*cast due to .constrained prefix*/).ToString().ToLower().Contains("evil") || val.Descriptor.IsUndead)
				{
					text += " - Undead";
				}
				if (((EntityFactsProcessor<Etude>)(object)Game.Instance.Player.EtudesSystem.Etudes).GetFact((BlueprintFact)(object)ResourcesLibrary.TryGetBlueprint<BlueprintEtude>("0ab81986d8f7c484a8fede0d2188125c")) != null && ((EntityFactsProcessor<Etude>)(object)Game.Instance.Player.EtudesSystem.Etudes).GetFact((BlueprintFact)(object)ResourcesLibrary.TryGetBlueprint<BlueprintEtude>("0ab81986d8f7c484a8fede0d2188125c")).IsPlaying)
				{
					text += " - Old";
				}
			}
			if (text.Equals(StauntonName) && (val.Blueprint.m_AddFacts.Contains(BlueprintReferenceEx.ToReference<BlueprintUnitFactReference>((SimpleBlueprint)(object)ResourcesLibrary.TryGetBlueprint<BlueprintFeature>("734a29b693e9ec346ba2951b27987e33"))) || val.Descriptor.IsUndead))
			{
				text += " - Undead";
			}
			if (text.Equals(SendriName) && (Game.Instance.Player.Dialog.ShownCues.Contains((BlueprintCueBase)(object)ResourcesLibrary.TryGetBlueprint<BlueprintCue>("3f0d565178034fecb5a18706b159bf6c")) || ((SimpleBlueprint)Game.Instance.Player.Campaign).name.Equals("Dlc5Campaign")))
			{
				text += " - ChrystalEye";
			}
			if (text.Equals(WoljifName) && Game.Instance.Player.EtudesSystem.EtudeIsStarted(ResourcesLibrary.TryGetBlueprint<BlueprintEtude>("709161cd9da156146ac6e3c394caa854")))
			{
				text += " - Demon";
			}
			if (text.Equals(NenioName))
			{
				if ((!((SimpleBlueprint)Game.Instance.Player.Campaign).name.Equals("MainCampaign") || SimpleBlueprint.op_Implicit((SimpleBlueprint)(object)Game.Instance.Player.UnlockableFlags.UnlockedFlags.Keys.FirstOrDefault((BlueprintUnlockableFlag x) => ((SimpleBlueprint)x).name.Contains("Fox"))) || (Game.Instance.CurrentMode == GameModeType.Dialog && Game.Instance.Player.Dialog.ShownCues.Contains((BlueprintCueBase)(object)ResourcesLibrary.TryGetBlueprint<BlueprintCue>("45450b2f327797e41bce701b91118cb4")))) && !val.Body.IsPolymorphed)
				{
					text = NenioName + "Fox_Portrait";
				}
				if (Game.Instance.CurrentMode == GameModeType.Dialog && ((object)System.Runtime.CompilerServices.Unsafe.As<BlueprintGuid, BlueprintGuid>(ref ((SimpleBlueprint)Game.Instance.DialogController.CurrentCue).AssetGuid)/*cast due to .constrained prefix*/).ToString().Equals("45450b2f327797e41bce701b91118cb4"))
				{
					text = NenioName + "Fox_Portrait";
				}
			}
			return text;
		}
		return characterName;
	}

	public static UnitEntityData RealCurrentSpeakerEntity(string characterName)
	{
		//IL_00f6: Unknown result type (might be due to invalid IL or missing references)
		//IL_00fb: Unknown result type (might be due to invalid IL or missing references)
		//IL_0045: Unknown result type (might be due to invalid IL or missing references)
		//IL_004a: Unknown result type (might be due to invalid IL or missing references)
		if (Game.Instance.CurrentMode == GameModeType.Dialog && Game.Instance.DialogController != null && Game.Instance.DialogController.CurrentSpeakerBlueprint != null)
		{
			EntityPoolEnumerator<UnitEntityData> enumerator = Game.Instance.State.Units.GetEnumerator();
			try
			{
				while (enumerator.MoveNext())
				{
					UnitEntityData current = enumerator.Current;
					if (((SimpleBlueprint)current.Blueprint).name.Equals(((SimpleBlueprint)Game.Instance.DialogController.CurrentSpeakerBlueprint).name))
					{
						return current;
					}
				}
			}
			finally
			{
				((IDisposable)enumerator/*cast due to .constrained prefix*/).Dispose();
			}
		}
		else
		{
			if (Game.Instance.CurrentMode == GameModeType.Dialog && Game.Instance.DialogController != null && Game.Instance.DialogController.CurrentSpeaker != (UnitDescriptor)null)
			{
				return Game.Instance.DialogController.CurrentSpeaker;
			}
			EntityPoolEnumerator<UnitEntityData> enumerator = Game.Instance.State.Units.GetEnumerator();
			try
			{
				while (enumerator.MoveNext())
				{
					UnitEntityData current2 = enumerator.Current;
					if (current2.Blueprint.CharacterName.cleanCharName().Equals(characterName))
					{
						return current2;
					}
				}
			}
			finally
			{
				((IDisposable)enumerator/*cast due to .constrained prefix*/).Dispose();
			}
		}
		return null;
	}

	private static void OnSaveGUI(ModEntry modEntry)
	{
		((ModSettings)settings).Save(modEntry);
	}

	private static void OnHideGUI(ModEntry modEntry)
	{
		((ModSettings)settings).Save(modEntry);
	}

	private static bool OnToggle(ModEntry modEntry, bool value)
	{
		enabled = value;
		if (enabled)
		{
			settings = ModSettings.Load<Settings>(modEntry);
			DebugLog("Mod is enabled");
		}
		else
		{
			DebugLog("Mod is disabled");
			((ModSettings)settings).Save(modEntry);
		}
		return true;
	}

	public static void SetArmyPortraits()
	{
		_ = Game.Instance.Player.GlobalMap.LastActivated;
		Directory.GetDirectories(GetArmyPortraitsDirectory());
	}

	public static string GetNpcPortraitsDirectory()
	{
		string text = Path.Combine(Path.GetFullPath(Path.Combine(CustomPortraitsManager.PortraitsRootFolderPath, "..\\")), NpcPortraitsDirName());
		Directory.CreateDirectory(text);
		return text;
	}

	public static string GetArmyPortraitsDirectory()
	{
		string text = Path.Combine(Path.GetFullPath(Path.Combine(CustomPortraitsManager.PortraitsRootFolderPath, "..\\")), ArmyPortraitsDirName());
		Directory.CreateDirectory(text);
		return text;
	}

	public static string GetTacticalPortraitsDirectory()
	{
		string text = Path.Combine(Path.GetFullPath(Path.Combine(CustomPortraitsManager.PortraitsRootFolderPath, "..\\")), TacticalPortraitsDirName());
		Directory.CreateDirectory(text);
		return text;
	}

	public static string GetCompanionPortraitsDirectory()
	{
		Directory.CreateDirectory(Path.GetFullPath(CustomPortraitsManager.PortraitsRootFolderPath));
		return Path.GetFullPath(CustomPortraitsManager.PortraitsRootFolderPath);
	}

	public static string NpcPortraitsDirName()
	{
		return "Portraits - Npc";
	}

	public static string ArmyPortraitsDirName()
	{
		return "Portraits - Army";
	}

	public static string TacticalPortraitsDirName()
	{
		return "Portraits - Tactical";
	}

	public static string GetCompanionPortraitDirPrefix()
	{
		return "CustomNpcPortraits - ";
	}

	public static string GetDefaultPortraitsDirName()
	{
		return "Backup of Game Default Portraits";
	}

	public static void DebugLog2(string msg)
	{
		if (logger != null)
		{
			logger.Log(msg);
		}
	}

	public static void DebugLog(string msg)
	{
	}

	public static void Log(string msg)
	{
		if (logger != null)
		{
			logger.Log(msg);
		}
	}

	public static void DebugError(Exception ex)
	{
		if (logger != null)
		{
			logger.Log(ex.ToString() + "\n" + ex.StackTrace);
		}
	}

	internal static Exception Error(string message)
	{
		return new InvalidOperationException(message);
	}

	internal static void SafeLoad(Action load, string name)
	{
		try
		{
			load();
			okLoading.Add(name);
		}
		catch (Exception ex)
		{
			okLoading.Remove(name);
			failedLoading.Add(name);
			DebugLog(ex.ToString());
		}
	}

	internal static bool ApplyPatch(Type type, string featureName)
	{
		try
		{
			if (typesPatched.ContainsKey(type))
			{
				return typesPatched[type];
			}
			List<HarmonyMethod> harmonyMethods = type.GetHarmonyMethods();
			if (harmonyMethods == null || harmonyMethods.Count() == 0)
			{
				DebugLog("Failed to apply patch " + featureName + ": could not find Harmony attributes.");
				failedPatches.Add(featureName);
				typesPatched.Add(type, value: false);
				return false;
			}
			if (LinqExtensions.FirstOrDefault<DynamicMethod>((IList<DynamicMethod>)new PatchProcessor(harmonyInstance, type, HarmonyMethod.Merge(harmonyMethods)).Patch()) == null)
			{
				DebugLog("Failed to apply patch " + featureName + ": no dynamic method generated");
				failedPatches.Add(featureName);
				typesPatched.Add(type, value: false);
				return false;
			}
			okPatches.Add(featureName);
			typesPatched.Add(type, value: true);
			return true;
		}
		catch (Exception ex)
		{
			DebugLog("Failed to apply patch " + featureName + ": " + ex?.ToString() + ", type: " + type);
			failedPatches.Add(featureName);
			typesPatched.Add(type, value: false);
			return false;
		}
	}

	public static void SetCustomPortrait(UnitEntityData unitEntityData)
	{
		//IL_00bb: Unknown result type (might be due to invalid IL or missing references)
		//IL_00c2: Expected O, but got Unknown
		//IL_011a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0146: Unknown result type (might be due to invalid IL or missing references)
		string companionPortraitDirPrefix = GetCompanionPortraitDirPrefix();
		string companionPortraitsDirectory = GetCompanionPortraitsDirectory();
		string companionDirName = GetCompanionDirName(unitEntityData.CharacterName.cleanCharName());
		string path = companionPortraitDirPrefix + companionDirName;
		string text = Path.Combine(companionPortraitsDirectory, path);
		if (Directory.GetFiles(text, "*.current").Length != 0)
		{
			string fileNameWithoutExtension = Path.GetFileNameWithoutExtension(Directory.GetFiles(text, "*.current")[0]);
			DebugLog(fileNameWithoutExtension);
			if (!fileNameWithoutExtension.Equals("root"))
			{
				text = Path.Combine(companionPortraitsDirectory, path, fileNameWithoutExtension);
			}
		}
		CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(text, "Small.png"));
		CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(text, "Medium.png"));
		CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(text, "Fulllength.png"));
		PortraitData val = new PortraitData(text);
		pauseGetPortraitsafe = true;
		val.m_PetEyeImage = unitEntityData.Descriptor.Blueprint.PortraitSafe.Data.m_PetEyeImage;
		pauseGetPortraitsafe = false;
		if (File.Exists(Path.Combine(text, "PetEye.png")))
		{
			EyePortraitInjector.Replacements[val] = PortraitLoader.Image2Sprite.Create(Path.Combine(text, "PetEye.png"), new Vector2Int(176, 24), (TextureFormat)14);
		}
		if (companionDirName.Equals(NenioName))
		{
			if (unitEntityData.Body.IsPolymorphed)
			{
				unitEntityData.GetActivePolymorph().Runtime.OnActivate();
			}
		}
		else
		{
			pauseGetPortraitsafe = true;
			unitEntityData.UISettings.SetPortrait(val);
			pauseGetPortraitsafe = false;
		}
	}

	public static PortraitData GetCustomPortrait(UnitEntityData unitEntityData)
	{
		//IL_00bb: Unknown result type (might be due to invalid IL or missing references)
		//IL_00c2: Expected O, but got Unknown
		//IL_0124: Unknown result type (might be due to invalid IL or missing references)
		//IL_0150: Unknown result type (might be due to invalid IL or missing references)
		string companionPortraitDirPrefix = GetCompanionPortraitDirPrefix();
		string companionPortraitsDirectory = GetCompanionPortraitsDirectory();
		string companionDirName = GetCompanionDirName(unitEntityData.CharacterName.cleanCharName());
		string path = companionPortraitDirPrefix + companionDirName;
		string text = Path.Combine(companionPortraitsDirectory, path);
		if (Directory.GetFiles(text, "*.current").Length != 0)
		{
			string fileNameWithoutExtension = Path.GetFileNameWithoutExtension(Directory.GetFiles(text, "*.current")[0]);
			DebugLog(fileNameWithoutExtension);
			if (!fileNameWithoutExtension.Equals("root"))
			{
				text = Path.Combine(companionPortraitsDirectory, path, fileNameWithoutExtension);
			}
		}
		CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(text, "Small.png"));
		CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(text, "Medium.png"));
		CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(text, "Fulllength.png"));
		PortraitData val = new PortraitData(text);
		pauseGetPortraitsafe = true;
		val.m_PetEyeImage = unitEntityData.Descriptor.Blueprint.PortraitSafe.Data.m_PetEyeImage;
		pauseGetPortraitsafe = false;
		DebugLog("SetPortrait() 12");
		if (File.Exists(Path.Combine(text, "PetEye.png")))
		{
			EyePortraitInjector.Replacements[val] = PortraitLoader.Image2Sprite.Create(Path.Combine(text, "PetEye.png"), new Vector2Int(176, 24), (TextureFormat)14);
		}
		if (companionDirName.Equals(NenioName))
		{
			if (unitEntityData.Body.IsPolymorphed)
			{
				unitEntityData.GetActivePolymorph().Runtime.OnActivate();
			}
			return null;
		}
		return val;
	}

	public static PortraitData SetPortrait(UnitEntityData unitEntityData, bool pickUpOnly)
	{
		//IL_0086: Unknown result type (might be due to invalid IL or missing references)
		//IL_008d: Expected O, but got Unknown
		//IL_00b2: Unknown result type (might be due to invalid IL or missing references)
		//IL_00bc: Expected O, but got Unknown
		//IL_0426: Unknown result type (might be due to invalid IL or missing references)
		//IL_05ea: Unknown result type (might be due to invalid IL or missing references)
		//IL_05fa: Unknown result type (might be due to invalid IL or missing references)
		//IL_060f: Unknown result type (might be due to invalid IL or missing references)
		//IL_04a7: Unknown result type (might be due to invalid IL or missing references)
		//IL_0462: Unknown result type (might be due to invalid IL or missing references)
		//IL_0638: Unknown result type (might be due to invalid IL or missing references)
		//IL_04f9: Unknown result type (might be due to invalid IL or missing references)
		//IL_09c4: Unknown result type (might be due to invalid IL or missing references)
		//IL_09cb: Expected O, but got Unknown
		//IL_0679: Unknown result type (might be due to invalid IL or missing references)
		//IL_0515: Unknown result type (might be due to invalid IL or missing references)
		//IL_0fa0: Unknown result type (might be due to invalid IL or missing references)
		//IL_0ce0: Unknown result type (might be due to invalid IL or missing references)
		//IL_0ce5: Unknown result type (might be due to invalid IL or missing references)
		//IL_0a46: Unknown result type (might be due to invalid IL or missing references)
		//IL_0d35: Unknown result type (might be due to invalid IL or missing references)
		//IL_0d3a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0544: Unknown result type (might be due to invalid IL or missing references)
		//IL_0d8a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0d8f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0ddf: Unknown result type (might be due to invalid IL or missing references)
		//IL_0de4: Unknown result type (might be due to invalid IL or missing references)
		//IL_0572: Unknown result type (might be due to invalid IL or missing references)
		//IL_0e34: Unknown result type (might be due to invalid IL or missing references)
		//IL_0e39: Unknown result type (might be due to invalid IL or missing references)
		//IL_0e89: Unknown result type (might be due to invalid IL or missing references)
		//IL_0e8e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0ede: Unknown result type (might be due to invalid IL or missing references)
		//IL_0ee3: Unknown result type (might be due to invalid IL or missing references)
		//IL_0f66: Unknown result type (might be due to invalid IL or missing references)
		//IL_0f6b: Unknown result type (might be due to invalid IL or missing references)
		//IL_0f33: Unknown result type (might be due to invalid IL or missing references)
		//IL_0f38: Unknown result type (might be due to invalid IL or missing references)
		DebugLog("SetPortrait(!!!!!!!) " + unitEntityData.CharacterName.cleanCharName());
		try
		{
			string companionPortraitDirPrefix = GetCompanionPortraitDirPrefix();
			string companionPortraitsDirectory = GetCompanionPortraitsDirectory();
			string companionDirName = GetCompanionDirName(unitEntityData.CharacterName.cleanCharName());
			DebugLog("SetPortrait() 1");
			string path = companionPortraitDirPrefix + companionDirName;
			string text = Path.Combine(companionPortraitsDirectory, path);
			Directory.CreateDirectory(text);
			DebugLog("SetPortrait() 2");
			BlueprintPortrait val = (BlueprintPortrait)typeof(UnitUISettings).GetField("m_Portrait", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(unitEntityData.Descriptor.UISettings);
			if (val == null)
			{
				val = BlueprintReference<BlueprintPortrait>.op_Implicit((BlueprintReference<BlueprintPortrait>)(BlueprintPortraitReference)typeof(BlueprintUnit).GetField("m_Portrait", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(unitEntityData.Blueprint));
			}
			DebugLog("SetPortrait() 2.5");
			if (companionDirName.Equals(ArueName + " - Evil") && settings.AutoBackup)
			{
				val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("484588d56f2c2894ab6d48b91509f5e3");
				SaveOriginals2(val.Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + companionDirName));
			}
			else if (companionDirName.Equals(NenioName + "Fox_Portrait") && settings.AutoBackup)
			{
				val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("2b4b8a23024093e42a5db714c2f52dbc");
				SaveOriginals2(val.Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + companionDirName));
			}
			else if (companionDirName.Equals(NenioName) && settings.AutoBackup)
			{
				val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("a6e4ff25a8da46a44a24ecc5da296073");
				SaveOriginals2(val.Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + companionDirName));
			}
			else if (companionDirName.Equals(CiarName + " - Undead") && settings.AutoBackup)
			{
				val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("dc2f02dd42cfe2b40923eb014591a009");
				SaveOriginals2(val.Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + companionDirName));
			}
			else if (companionDirName.Equals(GalfreyName + " - Undead") && settings.AutoBackup)
			{
				val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("767456b1656ca064dadac544d39d7e40");
				SaveOriginals2(val.Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + companionDirName));
			}
			else if (companionDirName.Equals(GalfreyName + " - Old") && settings.AutoBackup)
			{
				val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("4e8dfb75015d356469b976145c851087");
				SaveOriginals2(val.Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + companionDirName));
			}
			else if (companionDirName.Equals(WoljifName + " - Demon") && settings.AutoBackup)
			{
				val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("f2bd5a94ade889444921b4a74b9e34a9");
				SaveOriginals2(val.Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + companionDirName));
			}
			else if (companionDirName.Equals(SendriName + " - ChrystalEye") && settings.AutoBackup)
			{
				val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("222c3bcbf7e342338416c0e8bdc75109");
				SaveOriginals2(val.Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + companionDirName));
			}
			else if (companionDirName.Equals(StauntonName + " - Undead") && settings.AutoBackup)
			{
				val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("f4bbe08217bcaa54c91fe73bcea70ede");
				SaveOriginals2(val.Data, Path.Combine(GetCompanionPortraitsDirectory(), GetCompanionPortraitDirPrefix() + companionDirName));
			}
			else if (val != null && settings.AutoBackup)
			{
				DebugLog("!!! BACKUP?");
				SaveOriginals2(val.Data, text);
			}
			DebugLog("SetPortrait() 3");
			if (unitEntityData.Body.IsPolymorphed && !unitEntityData.CharacterName.cleanCharName().Equals(NenioName))
			{
				DebugLog("SetPortrait() 3.4");
				string path2 = text;
				EntityFactComponent runtime = unitEntityData.GetActivePolymorph().Runtime;
				object path3;
				if (runtime == null)
				{
					path3 = null;
				}
				else
				{
					BlueprintComponent sourceBlueprintComponent = runtime.SourceBlueprintComponent;
					path3 = ((sourceBlueprintComponent == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent.OwnerBlueprint?)).name);
				}
				if (!Directory.Exists(Path.Combine(path2, (string)path3)))
				{
					string path4 = text;
					EntityFactComponent runtime2 = unitEntityData.GetActivePolymorph().Runtime;
					object path5;
					if (runtime2 == null)
					{
						path5 = null;
					}
					else
					{
						BlueprintComponent sourceBlueprintComponent2 = runtime2.SourceBlueprintComponent;
						path5 = ((sourceBlueprintComponent2 == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent2.OwnerBlueprint?)).name);
					}
					Directory.CreateDirectory(Path.Combine(path4, (string)path5));
				}
				DebugLog("SetPortrait() 3.5");
				string path6 = text;
				EntityFactComponent runtime3 = unitEntityData.GetActivePolymorph().Runtime;
				object path7;
				if (runtime3 == null)
				{
					path7 = null;
				}
				else
				{
					BlueprintComponent sourceBlueprintComponent3 = runtime3.SourceBlueprintComponent;
					path7 = ((sourceBlueprintComponent3 == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent3.OwnerBlueprint?)).name);
				}
				if (!File.Exists(Path.Combine(path6, (string)path7, GetDefaultPortraitsDirName(), "Medium.png")))
				{
					DebugLog("SetPortrait() 3.6");
					if (unitEntityData.GetActivePolymorph().Component?.m_Portrait != null)
					{
						Polymorph component = unitEntityData.GetActivePolymorph().Component;
						object obj;
						if (component == null)
						{
							obj = null;
						}
						else
						{
							BlueprintPortraitReference portrait = component.m_Portrait;
							obj = ((portrait != null) ? ((BlueprintReferenceBase)portrait).GetBlueprint() : null);
						}
						if (obj != null)
						{
							DebugLog("SetPortrait() 3.7");
							Polymorph component2 = unitEntityData.GetActivePolymorph().Component;
							object obj2;
							if (component2 == null)
							{
								obj2 = null;
							}
							else
							{
								BlueprintPortraitReference portrait2 = component2.m_Portrait;
								obj2 = ((portrait2 != null) ? ((BlueprintReferenceBase)portrait2).GetBlueprint() : null);
							}
							PortraitData data = ((BlueprintPortrait)((obj2 is BlueprintPortrait) ? obj2 : null)).Data;
							string path8 = text;
							EntityFactComponent runtime4 = unitEntityData.GetActivePolymorph().Runtime;
							object path9;
							if (runtime4 == null)
							{
								path9 = null;
							}
							else
							{
								BlueprintComponent sourceBlueprintComponent4 = runtime4.SourceBlueprintComponent;
								path9 = ((sourceBlueprintComponent4 == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent4.OwnerBlueprint?)).name);
							}
							SaveOriginals2(data, Path.Combine(path8, (string)path9));
							DebugLog("SetPortrait() 3.8");
						}
					}
				}
			}
			DebugLog("SetPortrait() 4");
			if (unitEntityData.Body.IsPolymorphed && !unitEntityData.CharacterName.cleanCharName().Equals(NenioName) && unitEntityData.GetActivePolymorph().Runtime != null && unitEntityData.GetActivePolymorph().Runtime.SourceBlueprintComponent != null)
			{
				EntityFactComponent runtime5 = unitEntityData.GetActivePolymorph().Runtime;
				object obj3;
				if (runtime5 == null)
				{
					obj3 = null;
				}
				else
				{
					BlueprintComponent sourceBlueprintComponent5 = runtime5.SourceBlueprintComponent;
					obj3 = ((sourceBlueprintComponent5 != null) ? sourceBlueprintComponent5.OwnerBlueprint : null);
				}
				if (obj3 != null)
				{
					string path10 = text;
					EntityFactComponent runtime6 = unitEntityData.GetActivePolymorph().Runtime;
					object path11;
					if (runtime6 == null)
					{
						path11 = null;
					}
					else
					{
						BlueprintComponent sourceBlueprintComponent6 = runtime6.SourceBlueprintComponent;
						path11 = ((sourceBlueprintComponent6 == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent6.OwnerBlueprint?)).name);
					}
					if (File.Exists(Path.Combine(path10, (string)path11, "Medium.png")))
					{
						string path12 = text;
						EntityFactComponent runtime7 = unitEntityData.GetActivePolymorph().Runtime;
						object path13;
						if (runtime7 == null)
						{
							path13 = null;
						}
						else
						{
							BlueprintComponent sourceBlueprintComponent7 = runtime7.SourceBlueprintComponent;
							path13 = ((sourceBlueprintComponent7 == null) ? null : ((SimpleBlueprint)(sourceBlueprintComponent7.OwnerBlueprint?)).name);
						}
						text = Path.Combine(path12, (string)path13);
						DebugLog("SetPortrait() 6");
						goto IL_08b9;
					}
				}
			}
			if (Game.Instance.CurrentMode == GameModeType.Dialog && Game.Instance.DialogController != null && Game.Instance.DialogController.CurrentSpeaker != (UnitDescriptor)null && File.Exists(Path.Combine(text, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name, "Medium.png")))
			{
				text = Path.Combine(text, ((SimpleBlueprint)Game.Instance.DialogController.Dialog).name);
				DebugLog("SetPortrait() 7");
			}
			else if (Directory.GetFiles(text, "*.current").Length != 0)
			{
				string fileNameWithoutExtension = Path.GetFileNameWithoutExtension(Directory.GetFiles(text, "*.current")[0]);
				DebugLog(fileNameWithoutExtension);
				if (!fileNameWithoutExtension.Equals("root"))
				{
					text = Path.Combine(companionPortraitsDirectory, path, fileNameWithoutExtension);
				}
				DebugLog("SetPortrait() 7.5");
			}
			else
			{
				DialogController dialogController = Game.Instance.DialogController;
				if (((dialogController == null) ? null : ((SimpleBlueprint)(dialogController.CurrentSpeakerBlueprint?)).name) != null)
				{
					DialogController dialogController2 = Game.Instance.DialogController;
					if (dialogController2 != null && ((SimpleBlueprint)(dialogController2.CurrentSpeakerBlueprint?)).name?.Length > 2)
					{
						string path14 = text;
						DialogController dialogController3 = Game.Instance.DialogController;
						if (File.Exists(Path.Combine(path14, (dialogController3 == null) ? null : ((SimpleBlueprint)(dialogController3.CurrentSpeakerBlueprint?)).name, "Medium.png")))
						{
							string path15 = text;
							DialogController dialogController4 = Game.Instance.DialogController;
							text = Path.Combine(path15, (dialogController4 == null) ? null : ((SimpleBlueprint)(dialogController4.CurrentSpeakerBlueprint?)).name);
							goto IL_08b9;
						}
					}
				}
				DebugLog("SetPortrait() 8");
				if (!File.Exists(Path.Combine(text, "Medium.png")) && File.Exists(Path.Combine(text, GetDefaultPortraitsDirName(), "Medium.png")))
				{
					text = Path.Combine(text, GetDefaultPortraitsDirName());
				}
			}
			goto IL_08b9;
			IL_08b9:
			bool flag = false;
			DebugLog("SetPortrait() 8.5" + text);
			string[] portraitFileNames = PortraitFileNames;
			foreach (string text2 in portraitFileNames)
			{
				if (!File.Exists(Path.Combine(text, text2)))
				{
					flag = true;
					if ((companionDirName.Equals(CiarName) || animalCompList.Contains(((SimpleBlueprint)unitEntityData.Blueprint).name)) && text2.Contains("Full"))
					{
						flag = false;
					}
				}
			}
			DebugLog("SetPortrait() 9");
			CompanionPortraitPath = text;
			if (!flag)
			{
				DebugLog("SetPortrait() 10");
				if (!pickUpOnly)
				{
					DebugLog("SetPortrait() 10.5 not pickupOnly");
					CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(text, "Small.png"));
					CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(text, "Medium.png"));
					CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(text, "Fulllength.png"));
					DebugLog("SetPortrait() 11" + text);
					PortraitData val2 = new PortraitData(text);
					if (val == null)
					{
						pauseGetPortraitsafe = true;
						val2.m_PetEyeImage = unitEntityData.Descriptor.Blueprint.PortraitSafe.Data.m_PetEyeImage;
						pauseGetPortraitsafe = false;
					}
					else
					{
						val2.m_PetEyeImage = val.Data.m_PetEyeImage;
					}
					DebugLog("SetPortrait() 12");
					if (File.Exists(Path.Combine(text, "PetEye.png")))
					{
						EyePortraitInjector.Replacements[val2] = PortraitLoader.Image2Sprite.Create(Path.Combine(text, "PetEye.png"), new Vector2Int(176, 24), (TextureFormat)14);
					}
					DebugLog("SetPortrait() 13");
					typeof(UnitUISettings).GetField("m_CustomPortrait", BindingFlags.Instance | BindingFlags.NonPublic).SetValue(unitEntityData.UISettings, val2);
					typeof(UnitUISettings).GetField("m_Portrait", BindingFlags.Instance | BindingFlags.NonPublic).SetValue(unitEntityData.UISettings, null);
					return val2;
				}
				DebugLog("SetPortrait() 14  pickupOnly");
				return null;
			}
			DebugLog("SetPortrait() 9.1 - " + unitEntityData.CharacterName.cleanCharName());
			if (val != null && val.Data != null && (Object)(object)val.Data.FullLengthPortrait != (Object)null && (Object)(object)val.Data.HalfLengthPortrait != (Object)null && (Object)(object)val.Data.SmallPortrait != (Object)null)
			{
				pickedUpDir = "";
				if (Utils.IsNullOrEmpty(val.Data.CustomId))
				{
					pickedUpDir = "CustomId? : " + val.Data.CustomId;
				}
				if (!Utils.IsNullOrEmpty(((SimpleBlueprint)val).name))
				{
					pickedUpDir = pickedUpDir + " - Default? : " + ((SimpleBlueprint)val).name;
				}
				DebugLog("SetPortrait() 9.2");
			}
			else
			{
				pauseGetPortraitsafe = true;
				val = unitEntityData.Blueprint.PortraitSafe;
				pickedUpDir = "PortraitSafe -> Default? : " + ((SimpleBlueprint)val).name;
				pauseGetPortraitsafe = false;
				if (val != null && val.Data != null && (Object)(object)val.Data.FullLengthPortrait != (Object)null && (Object)(object)val.Data.HalfLengthPortrait != (Object)null && (Object)(object)val.Data.SmallPortrait != (Object)null)
				{
					DebugLog("SetPortrait() 9.4");
					pickedUpDir = "";
					if (!Utils.IsNullOrEmpty(val.Data.CustomId))
					{
						pickedUpDir = "PortraitSafe - CustomId? : " + val.Data.CustomId;
					}
					if (!Utils.IsNullOrEmpty(((SimpleBlueprint)val).name))
					{
						pickedUpDir = pickedUpDir + " - PortraitSafe - Default? : " + ((SimpleBlueprint)val).name;
					}
				}
				else
				{
					DebugLog("SetPortrait() 9.5");
					if (companions.Contains(unitEntityData.CharacterName.cleanCharName()))
					{
						if (companionDirName.Equals(NenioName))
						{
							val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("a6e4ff25a8da46a44a24ecc5da296073");
							CompanionPortraitBackups.TryGetValue(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)val)).Guid/*cast due to .constrained prefix*/).ToString(), out val.Data);
						}
						else if (companionDirName.Equals(ArueName + " - Evil"))
						{
							val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("484588d56f2c2894ab6d48b91509f5e3");
							CompanionPortraitBackups.TryGetValue(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)val)).Guid/*cast due to .constrained prefix*/).ToString(), out val.Data);
						}
						else if (companionDirName.Equals(GalfreyName + " - Undead"))
						{
							val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("767456b1656ca064dadac544d39d7e40");
							CompanionPortraitBackups.TryGetValue(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)val)).Guid/*cast due to .constrained prefix*/).ToString(), out val.Data);
						}
						else if (companionDirName.Equals(GalfreyName + " - Old"))
						{
							val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("4e8dfb75015d356469b976145c851087");
							CompanionPortraitBackups.TryGetValue(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)val)).Guid/*cast due to .constrained prefix*/).ToString(), out val.Data);
						}
						else if (companionDirName.Equals(WoljifName + " - Demon"))
						{
							val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("f2bd5a94ade889444921b4a74b9e34a9");
							CompanionPortraitBackups.TryGetValue(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)val)).Guid/*cast due to .constrained prefix*/).ToString(), out val.Data);
						}
						else if (companionDirName.Equals(SendriName + " - ChrystalEye"))
						{
							val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("222c3bcbf7e342338416c0e8bdc75109");
							CompanionPortraitBackups.TryGetValue(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)val)).Guid/*cast due to .constrained prefix*/).ToString(), out val.Data);
						}
						else if (companionDirName.Equals(CiarName + " - Undead"))
						{
							val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("dc2f02dd42cfe2b40923eb014591a009");
							CompanionPortraitBackups.TryGetValue(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)val)).Guid/*cast due to .constrained prefix*/).ToString(), out val.Data);
						}
						else if (companionDirName.Equals(StauntonName + " - Undead"))
						{
							val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("f4bbe08217bcaa54c91fe73bcea70ede");
							CompanionPortraitBackups.TryGetValue(((object)((BlueprintReferenceBase)BlueprintReferenceEx.ToReference<BlueprintPortraitReference>((SimpleBlueprint)(object)val)).Guid/*cast due to .constrained prefix*/).ToString(), out val.Data);
						}
						else
						{
							CompanionPortraitBackups.TryGetValue(((object)((BlueprintReferenceBase)unitEntityData.Blueprint.m_Portrait).Guid/*cast due to .constrained prefix*/).ToString(), out val.Data);
						}
						pickedUpDir = "Hardcoded Backup -> Default? : " + ((SimpleBlueprint)val).name;
					}
					else
					{
						if ((int)unitEntityData.Gender == 0)
						{
							DebugLog("male");
							val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("621ada02d0b4bf64387babad3a53067b");
						}
						else
						{
							DebugLog("female");
							val = Utilities.GetBlueprintByGuid<BlueprintPortrait>("9fe4f89ecf15b874db9d1d2bf3ef33d2");
						}
						pickedUpDir = "Failsafe : " + ((SimpleBlueprint)val).name;
						DebugLog("SetPortrait() 9.6");
					}
				}
			}
			DebugLog("SetPortrait() 9.7");
			if (!pickUpOnly)
			{
				PortraitData data2 = val.Data;
				pauseGetPortraitsafe = true;
				data2.m_PetEyeImage = unitEntityData.Descriptor.Blueprint.PortraitSafe.Data.m_PetEyeImage;
				val.Data.m_PetEyeImage = unitEntityData.Descriptor.Blueprint.PortraitSafe.Data.m_PetEyeImage;
				pauseGetPortraitsafe = false;
				DebugLog("SetPortrait() no custom portrait");
				unitEntityData.UISettings.m_CustomPortrait = null;
				unitEntityData.UISettings.m_Portrait = val;
				unitEntityData.UISettings.m_Portrait.Data.m_CustomPortraitId = "";
				return data2;
			}
			return null;
		}
		catch (Exception ex)
		{
			DebugError(ex);
			return null;
		}
	}

	public static void ArueAddHalo()
	{
		if (settings.ArueHalo)
		{
			foreach (UnitEntityData item in Game.Instance.Player.Party)
			{
				if (item.CharacterName.cleanCharName().Equals(ArueName))
				{
					BlueprintFeature val = ResourcesLibrary.TryGetBlueprint<BlueprintFeature>("d3f14f00f675a6341a41d2194186835c");
					Feature fact = ((EntityFactsProcessor<Feature>)(object)item.Progression.Features).GetFact((BlueprintFact)(object)val);
					if (!UnitHelper.HasFact(item, (EntityFact)(object)fact))
					{
						item.Progression.Features.AddFeature(val, (MechanicsContext)null);
					}
					break;
				}
			}
		}
		if (settings.ArueHalo)
		{
			return;
		}
		foreach (UnitEntityData item2 in Game.Instance.Player.Party)
		{
			if (item2.CharacterName.cleanCharName().Equals(ArueName))
			{
				BlueprintFeature val2 = ResourcesLibrary.TryGetBlueprint<BlueprintFeature>("d3f14f00f675a6341a41d2194186835c");
				Feature fact2 = ((EntityFactsProcessor<Feature>)(object)item2.Progression.Features).GetFact((BlueprintFact)(object)val2);
				if (UnitHelper.HasFact(item2, (EntityFact)(object)fact2))
				{
					((EntityFactsProcessor<Feature>)(object)item2.Progression.Features).RemoveFact((EntityFact)(object)fact2);
				}
				break;
			}
		}
	}

	public static void EmberAddHalo()
	{
		if (settings.EmberHalo)
		{
			foreach (UnitEntityData item in Game.Instance.Player.Party)
			{
				if (item.CharacterName.cleanCharName().Equals(EmberName))
				{
					BlueprintFeature val = ResourcesLibrary.TryGetBlueprint<BlueprintFeature>("d3f14f00f675a6341a41d2194186835c");
					Feature fact = ((EntityFactsProcessor<Feature>)(object)item.Progression.Features).GetFact((BlueprintFact)(object)val);
					if (!UnitHelper.HasFact(item, (EntityFact)(object)fact))
					{
						item.Progression.Features.AddFeature(val, (MechanicsContext)null);
					}
					break;
				}
			}
		}
		if (settings.EmberHalo)
		{
			return;
		}
		foreach (UnitEntityData item2 in Game.Instance.Player.Party)
		{
			if (item2.CharacterName.cleanCharName().Equals(EmberName))
			{
				BlueprintFeature val2 = ResourcesLibrary.TryGetBlueprint<BlueprintFeature>("d3f14f00f675a6341a41d2194186835c");
				Feature fact2 = ((EntityFactsProcessor<Feature>)(object)item2.Progression.Features).GetFact((BlueprintFact)(object)val2);
				if (UnitHelper.HasFact(item2, (EntityFact)(object)fact2))
				{
					((EntityFactsProcessor<Feature>)(object)item2.Progression.Features).RemoveFact((EntityFact)(object)fact2);
				}
				break;
			}
		}
	}

	public static void SetPortraits()
	{
		//IL_0384: Unknown result type (might be due to invalid IL or missing references)
		//IL_038e: Expected O, but got Unknown
		//IL_028a: Unknown result type (might be due to invalid IL or missing references)
		//IL_0294: Expected O, but got Unknown
		//IL_039b: Unknown result type (might be due to invalid IL or missing references)
		//IL_03ea: Unknown result type (might be due to invalid IL or missing references)
		//IL_03f4: Expected O, but got Unknown
		//IL_03d0: Unknown result type (might be due to invalid IL or missing references)
		//IL_03da: Expected O, but got Unknown
		//IL_031b: Unknown result type (might be due to invalid IL or missing references)
		if (!settings.ManageCompanions)
		{
			return;
		}
		string companionPortraitDirPrefix = GetCompanionPortraitDirPrefix();
		string companionPortraitsDirectory = GetCompanionPortraitsDirectory();
		List<UnitEntityData> list = new List<UnitEntityData>();
		foreach (UnitEntityData activeCompanion in Game.Instance.Player.ActiveCompanions)
		{
			if (!list.Contains(activeCompanion))
			{
				list.Add(activeCompanion);
			}
		}
		foreach (UnitEntityData unitEntityData in list)
		{
			try
			{
				string companionDirName = GetCompanionDirName(unitEntityData.CharacterName.cleanCharName());
				string path = companionPortraitDirPrefix + companionDirName;
				string text = Path.Combine(companionPortraitsDirectory, path);
				Directory.CreateDirectory(text);
				pauseGetPortraitsafe = true;
				BlueprintPortrait portraitSafe = unitEntityData.Blueprint.PortraitSafe;
				pauseGetPortraitsafe = false;
				if (portraitSafe != null && portraitSafe.Data != null && portraitSafe.Data.IsCustom && !Utils.IsNullOrEmpty(portraitSafe.Data.CustomId))
				{
					text = portraitSafe.Data.CustomId;
				}
				if (Directory.GetFiles(text, "*.current").Length != 0)
				{
					string fileNameWithoutExtension = Path.GetFileNameWithoutExtension(Directory.GetFiles(text, "*.current")[0]);
					if (!fileNameWithoutExtension.Equals("root"))
					{
						text = Path.Combine(text, fileNameWithoutExtension);
					}
				}
				else if (File.Exists(Path.Combine(text, ((SimpleBlueprint)(unitEntityData.Blueprint?)).name, "Medium.png")))
				{
					text = Path.Combine(text, ((SimpleBlueprint)(unitEntityData.Blueprint?)).name);
				}
				else if (!File.Exists(Path.Combine(text, "Medium.png")) && File.Exists(Path.Combine(text, GetDefaultPortraitsDirName(), "Medium.png")))
				{
					text = Path.Combine(text, GetDefaultPortraitsDirName());
				}
				bool flag = false;
				string[] portraitFileNames = PortraitFileNames;
				foreach (string path2 in portraitFileNames)
				{
					if (!File.Exists(Path.Combine(text, path2)))
					{
						flag = true;
					}
				}
				if (!flag)
				{
					portraitSafe = BlueprintRoot.Instance.CharGen.CustomPortrait;
					CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(text, "Small.png"));
					CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(text, "Medium.png"));
					CustomPortraitsManager.Instance.Storage.Unload(Path.Combine(text, "Fulllength.png"));
					portraitSafe.Data = new PortraitData(text);
					if (unitEntityData.IsPet)
					{
						pauseGetPortraitsafe = true;
						portraitSafe.Data.m_PetEyeImage = unitEntityData.Blueprint.PortraitSafe.Data.m_PetEyeImage;
						pauseGetPortraitsafe = false;
					}
					if (companionDirName.Equals(NenioName))
					{
						DebugLog("SetPortraits: " + companionDirName);
						if (unitEntityData.Body.IsPolymorphed)
						{
							DebugLog("SetPortraits poly");
							unitEntityData.GetActivePolymorph().Runtime.OnActivate();
						}
					}
					else
					{
						pauseGetPortraitsafe = true;
						unitEntityData.UISettings.SetPortrait(portraitSafe.Data);
						pauseGetPortraitsafe = false;
					}
					continue;
				}
				portraitSafe = BlueprintReference<BlueprintPortrait>.op_Implicit((BlueprintReference<BlueprintPortrait>)(BlueprintPortraitReference)typeof(BlueprintUnit).GetField("m_Portrait", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(unitEntityData.Descriptor.Blueprint));
				if (portraitSafe == null)
				{
					portraitSafe = (((int)unitEntityData.Gender != 0) ? Utilities.GetBlueprintByGuid<BlueprintPortrait>("9fe4f89ecf15b874db9d1d2bf3ef33d2") : Utilities.GetBlueprintByGuid<BlueprintPortrait>("621ada02d0b4bf64387babad3a53067b"));
				}
				else if (text.Contains(GetDefaultPortraitsDirName()))
				{
					portraitSafe.Data = new PortraitData(text);
				}
				else
				{
					portraitSafe.Data = new PortraitData(Path.Combine(text, GetDefaultPortraitsDirName()));
				}
				if (companionDirName.Equals(NenioName))
				{
					portraitSafe = Utilities.GetBlueprintByGuid<BlueprintPortrait>("a6e4ff25a8da46a44a24ecc5da296073");
				}
				if (companionDirName.Equals(NenioName + "Fox_Portrait"))
				{
					portraitSafe = Utilities.GetBlueprintByGuid<BlueprintPortrait>("2b4b8a23024093e42a5db714c2f52dbc");
				}
				if (companionDirName.Equals(ArueName))
				{
					portraitSafe = Utilities.GetBlueprintByGuid<BlueprintPortrait>("db413e67276547b40b1a6bb8178c6951");
				}
				if (companionDirName.Equals(ArueName + " - Evil"))
				{
					portraitSafe = Utilities.GetBlueprintByGuid<BlueprintPortrait>("484588d56f2c2894ab6d48b91509f5e3");
				}
				if (companionDirName.Equals(GalfreyName))
				{
					portraitSafe = Utilities.GetBlueprintByGuid<BlueprintPortrait>("a3ba06b4723c7a74fb5054ccb2289efb");
				}
				if (companionDirName.Equals(GalfreyName + " - Undead"))
				{
					portraitSafe = Utilities.GetBlueprintByGuid<BlueprintPortrait>("767456b1656ca064dadac544d39d7e40");
				}
				if (companionDirName.Equals(GalfreyName + " - Old"))
				{
					portraitSafe = Utilities.GetBlueprintByGuid<BlueprintPortrait>("4e8dfb75015d356469b976145c851087");
				}
				if (companionDirName.Equals(WoljifName + " - Demon"))
				{
					portraitSafe = Utilities.GetBlueprintByGuid<BlueprintPortrait>("f2bd5a94ade889444921b4a74b9e34a9");
				}
				if (companionDirName.Equals(SendriName + " - ChrystalEye"))
				{
					portraitSafe = Utilities.GetBlueprintByGuid<BlueprintPortrait>("222c3bcbf7e342338416c0e8bdc75109");
				}
				if (companionDirName.Equals(CiarName + " - Undead"))
				{
					portraitSafe = Utilities.GetBlueprintByGuid<BlueprintPortrait>("dc2f02dd42cfe2b40923eb014591a009");
				}
				if (companionDirName.Equals(StauntonName + " - Undead"))
				{
					portraitSafe = Utilities.GetBlueprintByGuid<BlueprintPortrait>("f4bbe08217bcaa54c91fe73bcea70ede");
				}
				if (unitEntityData.IsPet && companionDirName.Equals("Bismuth"))
				{
					pauseGetPortraitsafe = true;
					portraitSafe = unitEntityData.Blueprint.PortraitSafe;
					unitEntityData.UISettings.SetPortrait(portraitSafe.Data);
					pauseGetPortraitsafe = false;
					eye = portraitSafe.Data.PetEyePortrait;
					break;
				}
				typeof(UnitUISettings).GetField("m_CustomPortrait", BindingFlags.Instance | BindingFlags.NonPublic).SetValue(unitEntityData.UISettings, portraitSafe.Data);
				typeof(UnitUISettings).GetField("m_Portrait", BindingFlags.Instance | BindingFlags.NonPublic).SetValue(unitEntityData.UISettings, null);
				EventBus.RaiseEvent<IUnitPortraitChangedHandler>((Action<IUnitPortraitChangedHandler>)delegate(IUnitPortraitChangedHandler h)
				{
					h.HandlePortraitChanged(UnitDescriptor.op_Implicit(unitEntityData.Descriptor));
				}, true);
			}
			catch (Exception ex)
			{
				DebugError(ex);
			}
		}
	}

	public static bool SaveOriginals(BlueprintUnit bup, string path)
	{
		//IL_001e: Unknown result type (might be due to invalid IL or missing references)
		//IL_0028: Expected O, but got Unknown
		//IL_0095: Unknown result type (might be due to invalid IL or missing references)
		//IL_009a: Unknown result type (might be due to invalid IL or missing references)
		bool result = false;
		BlueprintPortrait val = BlueprintReference<BlueprintPortrait>.op_Implicit((BlueprintReference<BlueprintPortrait>)(BlueprintPortraitReference)typeof(BlueprintUnit).GetField("m_Portrait", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(bup));
		if (val != null)
		{
			SpriteLink fullLengthImage = val.Data.m_FullLengthImage;
			SpriteLink halfLengthImage = val.Data.m_HalfLengthImage;
			SpriteLink portraitImage = val.Data.m_PortraitImage;
			string text = Path.Combine(path, GetDefaultPortraitsDirName());
			if (settings.AutoBackup)
			{
				Directory.CreateDirectory(text);
			}
			bool npc = false;
			try
			{
				if (!bup.IsCompanion)
				{
					string text2 = bup.CharacterName.cleanCharName();
					UnitReference mainCharacter = Game.Instance.Player.MainCharacter;
					if (!(text2 == ((UnitReference)(ref mainCharacter)).Value.CharacterName.cleanCharName()) && !companions.Contains(bup.CharacterName.cleanCharName()))
					{
						npc = true;
						bool flag = false;
						if (!File.Exists(Path.Combine(text, mediumName)) && isPortraitMissing(text, bup))
						{
							Sprite val2 = ((WeakResourceLink<Sprite>)(object)halfLengthImage).Load(true, false);
							Sprite val3 = ((WeakResourceLink<Sprite>)(object)portraitImage).Load(true, false);
							if (((Texture)val3.texture).width == ((Texture)val2.texture).width)
							{
								flag = true;
								if (settings.AutoBackup)
								{
									CreateBaseImages(Path.Combine(text, mediumName), ((WeakResourceLink<Sprite>)(object)halfLengthImage).Load(true, false), npc: true, secret: true);
									CreateBaseImages(Path.Combine(text, smallName), val3, npc, secret: false);
								}
							}
							else
							{
								flag = false;
								if (settings.AutoBackup)
								{
									CreateBaseImages(Path.Combine(text, mediumName), val2, npc, flag);
									CreateBaseImages(Path.Combine(text, smallName), val3, npc, flag);
									CreateBaseImages(Path.Combine(text, fullName), ((WeakResourceLink<Sprite>)(object)fullLengthImage).Load(true, false), npc: false, flag);
								}
							}
						}
						if (settings.AutoSecret && flag && !File.Exists(Path.Combine(path, mediumName)))
						{
							Directory.CreateDirectory(path);
							CreateBaseImages(Path.Combine(path, mediumName), ((WeakResourceLink<Sprite>)(object)halfLengthImage).Load(true, false), npc: true, flag);
							CreateBaseImages(Path.Combine(path, smallName), ((WeakResourceLink<Sprite>)(object)portraitImage).Load(true, false), npc: false, flag);
						}
						goto IL_029d;
					}
				}
				if (!File.Exists(Path.Combine(text, mediumName)) && isPortraitMissing(text, bup))
				{
					CreateBaseImages(Path.Combine(text, smallName), ((WeakResourceLink<Sprite>)(object)portraitImage).Load(true, false), npc, secret: false);
					CreateBaseImages(Path.Combine(text, mediumName), ((WeakResourceLink<Sprite>)(object)halfLengthImage).Load(true, false), npc, secret: false);
					CreateBaseImages(Path.Combine(text, fullName), ((WeakResourceLink<Sprite>)(object)fullLengthImage).Load(true, false), npc, secret: false);
				}
				goto IL_029d;
				IL_029d:
				result = true;
			}
			catch (Exception ex)
			{
				failCounter++;
				DebugLog("Disk, The process failed: " + ex.ToString());
				result = false;
			}
		}
		return result;
	}

	public static bool SaveOriginals2(PortraitData pdata, string path)
	{
		if (!settings.AutoBackup)
		{
			return false;
		}
		bool result = false;
		if (pdata != null)
		{
			SpriteLink fullLengthImage = pdata.m_FullLengthImage;
			SpriteLink halfLengthImage = pdata.m_HalfLengthImage;
			SpriteLink portraitImage = pdata.m_PortraitImage;
			string text = Path.Combine(path, GetDefaultPortraitsDirName());
			Directory.CreateDirectory(text);
			bool flag = false;
			try
			{
				flag = true;
				bool flag2 = false;
				if (flag)
				{
					Sprite baseSprite = ((WeakResourceLink<Sprite>)(object)halfLengthImage).Load(true, false);
					Sprite baseSprite2 = ((WeakResourceLink<Sprite>)(object)portraitImage).Load(true, false);
					if (pdata.InitiativePortrait)
					{
						flag2 = true;
						if (settings.AutoBackup && !File.Exists(Path.Combine(text, mediumName)))
						{
							CreateBaseImages(Path.Combine(text, mediumName), ((WeakResourceLink<Sprite>)(object)halfLengthImage).Load(true, false), npc: true, secret: true);
							CreateBaseImages(Path.Combine(text, smallName), baseSprite2, flag, secret: false);
						}
					}
					else
					{
						flag2 = false;
						if (settings.AutoBackup && !File.Exists(Path.Combine(text, mediumName)))
						{
							CreateBaseImages(Path.Combine(text, mediumName), baseSprite, flag, flag2);
							CreateBaseImages(Path.Combine(text, smallName), baseSprite2, flag, flag2);
							CreateBaseImages(Path.Combine(text, fullName), ((WeakResourceLink<Sprite>)(object)fullLengthImage).Load(true, false), npc: false, flag2);
						}
					}
				}
				result = true;
			}
			catch (Exception ex)
			{
				failCounter++;
				DebugLog("Disk, The process failed: " + ex.ToString());
				result = false;
			}
		}
		else
		{
			DebugLog("pdata is null");
		}
		return result;
	}

	public static void CreateBaseImages(string path, Sprite baseSprite, bool npc, bool secret)
	{
		((MonoBehaviour)LoadingProcess.Instance).StartCoroutine(ExportSprite(baseSprite, path));
	}

	private static IEnumerator ExportSprite(Sprite sprite, string filePath)
	{
		if (sprite.packed && (int)sprite.packingMode == 0)
		{
			Log("Skipping tightly-packed sprite " + ((Object)sprite).name);
			yield break;
		}
		Texture2D copy = new Texture2D(((Texture)sprite.texture).width, ((Texture)sprite.texture).height, (TextureFormat)4, false);
		Graphics.ConvertTexture((Texture)(object)sprite.texture, (Texture)(object)copy);
		yield return null;
		if (sprite.packed)
		{
			Rect textureRect = sprite.textureRect;
			int num = (int)((Rect)(ref textureRect)).width;
			textureRect = sprite.textureRect;
			Texture2D val = new Texture2D(num, (int)((Rect)(ref textureRect)).height, (TextureFormat)4, false);
			Texture2D obj = copy;
			textureRect = sprite.textureRect;
			int num2 = (int)((Rect)(ref textureRect)).x;
			textureRect = sprite.textureRect;
			int num3 = (int)((Rect)(ref textureRect)).y;
			textureRect = sprite.textureRect;
			int num4 = (int)((Rect)(ref textureRect)).width;
			textureRect = sprite.textureRect;
			Graphics.CopyTexture((Texture)(object)obj, 0, 0, num2, num3, num4, (int)((Rect)(ref textureRect)).height, (Texture)(object)val, 0, 0, 0, 0);
			Object.Destroy((Object)(object)copy);
			copy = val;
		}
		AsyncGPUReadbackRequest request = AsyncGPUReadback.Request((Texture)(object)copy, 0, (TextureFormat)4, (Action<AsyncGPUReadbackRequest>)delegate(AsyncGPUReadbackRequest r)
		{
			//IL_0003: Unknown result type (might be due to invalid IL or missing references)
			//IL_000e: Unknown result type (might be due to invalid IL or missing references)
			//IL_002a: Unknown result type (might be due to invalid IL or missing references)
			//IL_002f: Unknown result type (might be due to invalid IL or missing references)
			byte[] bytes = ImageConversion.EncodeNativeArrayToPNG<Color32>(((AsyncGPUReadbackRequest)(ref r)).GetData<Color32>(0), ((Texture)copy).graphicsFormat, (uint)((Texture)copy).width, (uint)((Texture)copy).height, 0u).ToArray();
			File.WriteAllBytes(filePath, bytes);
			Object.Destroy((Object)(object)copy);
		});
		while (!((AsyncGPUReadbackRequest)(ref request)).done)
		{
			yield return null;
		}
		request = default(AsyncGPUReadbackRequest);
	}

	public static bool isPortraitMissing(string path, BlueprintUnit bup)
	{
		//IL_0024: Unknown result type (might be due to invalid IL or missing references)
		//IL_0029: Unknown result type (might be due to invalid IL or missing references)
		new DirectoryInfo(path);
		if (!bup.IsCompanion)
		{
			string text = bup.CharacterName.cleanCharName();
			UnitReference mainCharacter = Game.Instance.Player.MainCharacter;
			if (!(text == ((UnitReference)(ref mainCharacter)).Value.CharacterName.cleanCharName()))
			{
				if (!File.Exists(Path.Combine(path, smallName)))
				{
					return true;
				}
				if (!File.Exists(Path.Combine(path, mediumName)))
				{
					return true;
				}
				return false;
			}
		}
		string[] portraitFileNames = PortraitFileNames;
		foreach (string path2 in portraitFileNames)
		{
			if (!File.Exists(Path.Combine(path, path2)))
			{
				return true;
			}
		}
		return false;
	}
}
