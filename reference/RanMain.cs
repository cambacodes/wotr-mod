using System;
using BlueprintCore.Blueprints.Configurators;
using BlueprintCore.Blueprints.Configurators.DialogSystem;
using BlueprintCore.Blueprints.Configurators.Quests;
using BlueprintCore.Blueprints.Configurators.Root;
using BlueprintCore.Blueprints.CustomConfigurators;
using BlueprintCore.Utils;
using Epilogue.Setup;
using HarmonyLib;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Blueprints.Quests;
using Kingmaker.Blueprints.Root;
using Kingmaker.Enums;
using Kingmaker.Localization;
using RanRomance.Anev;
using RanRomance.Answers;
using RanRomance.Aran;
using RanRomance.Etudes;
using RanRomance.Mina;
using RanRomance.Noct;
using RanRomance.Nura;
using RanRomance.Revisions;
using RanRomance.Stor;
using RanRomance.Targ;
using RanRomance.Tere;
using UnityEngine;
using UnityModManagerNet;

namespace RanRomance;

public static class Main
{
	[HarmonyPatch(typeof(BlueprintsCache))]
	private static class BlueprintsCaches_Patch
	{
		private static bool Initialized;

		[HarmonyPriority(800)]
		[HarmonyPostfix]
		[HarmonyPatch("Init")]
		private static void Init()
		{
			//IL_005c: Unknown result type (might be due to invalid IL or missing references)
			//IL_0062: Expected O, but got Unknown
			//IL_0063: Unknown result type (might be due to invalid IL or missing references)
			//IL_006d: Expected O, but got Unknown
			//IL_007d: Unknown result type (might be due to invalid IL or missing references)
			//IL_0087: Expected O, but got Unknown
			//IL_0092: Unknown result type (might be due to invalid IL or missing references)
			//IL_009c: Expected O, but got Unknown
			//IL_00c1: Unknown result type (might be due to invalid IL or missing references)
			try
			{
				if (Initialized)
				{
					Logger.Info("Already configured blueprints.");
					return;
				}
				Initialized = true;
				Logger.Info("Configuring blueprints.");
				CueConfigurator.New("RanRomFiller", "d741e024073740a69d9c730c2a16fa16").SetText("RanRomFiller.Text").Configure();
				QuestGroup val = new QuestGroup();
				val.Name = new LocalizedString();
				val.Name.Shared = (SharedStringAsset)ScriptableObject.CreateInstance("SharedStringAsset");
				val.Name.Shared.String = new LocalizedString();
				val.Name.Shared.String.m_Key = "RanRomQuest.Text";
				val.Order = 19;
				val.Id = (QuestGroupId)18;
				QuestGroupsConfigurator.For("ef88df6af8491fc45aef8511a33a89a4").AddToGroups(val).Configure();
				RanRomance.Answers.Answers.Configure();
				VarEtudes.Configure();
				RanRomance.Noct.Main.Configure();
				RanRomance.Nura.Main.Configure();
				RanRomance.Targ.Main.Configure();
				RanRomance.Tere.Main.Configure();
				RanRomance.Aran.Main.Configure();
				RanRomance.Mina.Main.Configure();
				RanRomance.Anev.Main.Configure();
				RanRomance.Stor.Main.Configure();
				EpSetup.Configure();
				RanRomance.Revisions.Revisions.Configure();
				UnlockableFlagConfigurator.New("RanRomFinish", "cf151a44c57d437a815b4a23aa8d7022").Configure();
			}
			catch (Exception e)
			{
				Logger.Error("Failed to configure blueprints.", e);
			}
		}
	}

	[HarmonyPatch(typeof(StartGameLoader))]
	private static class StartGameLoader_Patch
	{
		private static bool Initialized;

		[HarmonyPatch("LoadPackTOC")]
		[HarmonyPostfix]
		private static void LoadPackTOC()
		{
			try
			{
				if (Initialized)
				{
					Logger.Info("Already configured delayed blueprints.");
					return;
				}
				Initialized = true;
				RootConfigurator<BlueprintRoot, RootConfigurator>.ConfigureDelayedBlueprints();
			}
			catch (Exception e)
			{
				Logger.Error("Failed to configure delayed blueprints.", e);
			}
		}
	}

	public static bool Enabled;

	private static readonly LogWrapper Logger = LogWrapper.Get("RanRomance");

	public static bool Load(ModEntry modEntry)
	{
		//IL_001f: Unknown result type (might be due to invalid IL or missing references)
		//IL_0025: Expected O, but got Unknown
		try
		{
			modEntry.OnToggle = OnToggle;
			Harmony val = new Harmony(modEntry.Info.Id);
			val.PatchAll();
			Logger.Info("Finished patching.");
		}
		catch (Exception e)
		{
			Logger.Error("Failed to patch", e);
		}
		return true;
	}

	public static bool OnToggle(ModEntry modEntry, bool value)
	{
		Enabled = value;
		return true;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
