using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using JetBrains.Annotations;
using Kingmaker.EntitySystem.Persistence.JsonUtility;
using Kingmaker.Localization.Shared;
using Kingmaker.Modding;
using Kingmaker.Settings;
using Kingmaker.Stores;
using Kingmaker.Utility;
using Newtonsoft.Json;
using Steamworks;
using UnityEngine;

namespace Kingmaker.Localization;

public class LocalizationManager
{
	private static Locale s_CurrentLocale = Locale.Sound;

	public static Locale LoadingLocale;

	private static Task<LocalizationPack> s_LoadingTask;

	[CanBeNull]
	public static LocalizationPack CurrentPack;

	[CanBeNull]
	public static LocalizationPack SoundPack;

	[NotNull]
	public static Locale[] BackupLocales = new Locale[2]
	{
		Locale.enGB,
		Locale.ruRU
	};

	private static bool s_Initialized = false;

	private static readonly Dictionary<string, Locale> s_SteamCodesToLocales = new Dictionary<string, Locale>
	{
		{
			"english",
			Locale.enGB
		},
		{
			"german",
			Locale.deDE
		},
		{
			"french",
			Locale.frFR
		},
		{
			"russian",
			Locale.ruRU
		},
		{
			"schinese",
			Locale.zhCN
		},
		{
			"tchinese",
			Locale.zhCN
		},
		{
			"spanish",
			Locale.esES
		}
	};

	private static readonly Dictionary<SystemLanguage, Locale> s_UnityCodesToLocales = new Dictionary<SystemLanguage, Locale>
	{
		{
			SystemLanguage.English,
			Locale.enGB
		},
		{
			SystemLanguage.German,
			Locale.deDE
		},
		{
			SystemLanguage.French,
			Locale.frFR
		},
		{
			SystemLanguage.Russian,
			Locale.ruRU
		},
		{
			SystemLanguage.Chinese,
			Locale.zhCN
		},
		{
			SystemLanguage.ChineseSimplified,
			Locale.zhCN
		},
		{
			SystemLanguage.ChineseTraditional,
			Locale.zhCN
		},
		{
			SystemLanguage.Spanish,
			Locale.esES
		},
		{
			SystemLanguage.Portuguese,
			Locale.ptBR
		},
		{
			SystemLanguage.Italian,
			Locale.itIT
		}
	};

	public static Locale CurrentLocale
	{
		get
		{
			return LocaleExtensions.ConvertUILocaleToSystemLocale(SettingsRoot.Game.Main.Localization);
		}
		set
		{
			Locale num = s_CurrentLocale;
			s_CurrentLocale = value;
			if (Application.isPlaying && CurrentPack?.Locale != s_CurrentLocale)
			{
				CurrentPack?.Dispose();
				CurrentPack = LoadPack(s_CurrentLocale);
				OwlcatModificationsManager.Instance.ApplyLocalization();
			}
			if (num != s_CurrentLocale)
			{
				OnLocaleChanged();
			}
			CultureInfo cultureInfo = (CultureInfo.DefaultThreadCurrentUICulture = (CultureInfo.DefaultThreadCurrentCulture = s_CurrentLocale.GetCulture()));
			Thread.CurrentThread.CurrentCulture = cultureInfo;
			Thread.CurrentThread.CurrentUICulture = cultureInfo;
		}
	}

	public static bool Initialized => s_Initialized;

	public static void Init()
	{
		if (s_Initialized)
		{
			return;
		}
		PFLog.System.Log("Initialize in progress.");
		using (CodeTimer.New("LocalizationManager.Initialize()"))
		{
			PFLog.System.Log("Loading localization packs...");
			if (SoundPack == null)
			{
				Task<LocalizationPack> task = LoadPackAsync(Locale.Sound);
				task.ContinueWith((Task<LocalizationPack> t) => SoundPack = t.Result);
				task.Start();
			}
			Locale? locale = null;
			try
			{
				string s = CommandLineArguments.Parse().Get("locale");
				locale = locale ?? Parse(s);
				if (!locale.HasValue)
				{
					if (SettingsRoot.Game.Main.LocalizationWasTouched.GetValue())
					{
						locale = LocaleExtensions.ConvertUILocaleToSystemLocale(SettingsRoot.Game.Main.Localization);
					}
					else
					{
						locale = DetectSystemLanguage();
						SettingsRoot.Game.Main.Localization.SetValueAndConfirm(LocaleExtensions.ConvertSystemLocaleToUILocale(locale.Value));
						SettingsController.SaveAll();
					}
				}
				if (!Enumerable.Contains(LocaleExtensions.GameLanguageValues, locale.Value))
				{
					locale = Locale.enGB;
				}
				PFLog.System.Log($"Loading [{locale.Value}] Pack...");
				LoadingLocale = locale.Value;
				s_LoadingTask = LoadPackAsync(LoadingLocale);
				s_LoadingTask.ContinueWith((Task<LocalizationPack> t) => CurrentPack = t.Result);
				s_LoadingTask.Start();
			}
			catch (Exception ex)
			{
				PFLog.Default.Exception(ex, null);
			}
			s_Initialized = true;
		}
	}

	private static void SetLocalization(LocaleExtensions.UILocale uilocale)
	{
		CurrentLocale = LocaleExtensions.ConvertUILocaleToSystemLocale(uilocale);
	}

	private static Locale? Parse(string s)
	{
		if (string.IsNullOrWhiteSpace(s))
		{
			return null;
		}
		if (Enum.TryParse<Locale>(s, out var result))
		{
			return result;
		}
		return null;
	}

	[CanBeNull]
	private static LocalizationPack LoadPack(Locale locale)
	{
		if (!BuildModeUtility.Data.UsePackedLocalization)
		{
			return LoadPack(Path.Combine(ApplicationPaths.streamingAssetsPath, "Localization/" + locale.ToString() + ".json"), locale);
		}
		return LoadBinPack(Path.Combine(ApplicationPaths.streamingAssetsPath, "Localization/" + locale.ToString() + ".bin"), locale);
	}

	[CanBeNull]
	public static LocalizationPack LoadPack(string packPath, Locale locale)
	{
		if (File.Exists(packPath))
		{
			try
			{
				JsonSerializer jsonSerializer = JsonSerializer.Create(DefaultJsonSettings.DefaultSettings);
				using StreamReader reader = new StreamReader(packPath);
				using (CodeTimer.New("Loc pack loading: " + locale))
				{
					LocalizationPack localizationPack = null;
					PFLog.System.Log($"Loading {locale} Pack Started.");
					using (JsonTextReader reader2 = new JsonTextReader(reader))
					{
						localizationPack = jsonSerializer.Deserialize<LocalizationPack>(reader2);
						localizationPack.Locale = locale;
					}
					PFLog.Default.Log("Loaded localization pack " + locale);
					return localizationPack;
				}
			}
			catch (Exception ex)
			{
				PFLog.Default.Error("Failed to load localization pack " + locale);
				PFLog.Default.Exception(ex, null);
				return null;
			}
		}
		return null;
	}

	private static LocalizationPack LoadBinPack(string packPath, Locale locale)
	{
		if (File.Exists(packPath))
		{
			try
			{
				using (CodeTimer.New("Loc pack loading: " + locale))
				{
					LocalizationPack localizationPack = new LocalizationPack();
					localizationPack.Locale = locale;
					localizationPack.InitFromBinary(packPath);
					PFLog.Default.Log("Loaded localization pack " + locale);
					return localizationPack;
				}
			}
			catch (Exception ex)
			{
				PFLog.Default.Error("Failed to load localization pack " + locale);
				PFLog.Default.Exception(ex, null);
				return null;
			}
		}
		return null;
	}

	private static Task<LocalizationPack> LoadPackAsync(Locale locale)
	{
		PFLog.System.Log($"Loading {locale} Pack Async...");
		return new Task<LocalizationPack>(() => LoadPack(locale));
	}

	private static void OnLocaleChanged()
	{
		LocalizedUIText[] array = Resources.FindObjectsOfTypeAll<LocalizedUIText>();
		for (int i = 0; i < array.Length; i++)
		{
			array[i].UpdateText();
		}
	}

	private static Locale DetectSystemLanguage()
	{
		Locale value;
		if (StoreManager.Store == StoreType.Steam && SteamManager.Initialized)
		{
			string currentGameLanguage = SteamApps.GetCurrentGameLanguage();
			if (s_SteamCodesToLocales.TryGetValue(currentGameLanguage, out value))
			{
				return value;
			}
		}
		if (s_UnityCodesToLocales.TryGetValue(Application.systemLanguage, out value))
		{
			return value;
		}
		return Locale.enGB;
	}

	public static void WaitForInit()
	{
		if (s_LoadingTask != null)
		{
			s_LoadingTask.Wait();
			if (s_LoadingTask.Exception != null)
			{
				PFLog.Default.Exception(s_LoadingTask.Exception, null);
			}
			else
			{
				CurrentPack = s_LoadingTask.Result;
			}
		}
		CurrentPack = CurrentPack ?? new LocalizationPack
		{
			Locale = CurrentLocale
		};
		SoundPack = SoundPack ?? new LocalizationPack
		{
			Locale = Locale.Sound
		};
		if (CurrentPack != null)
		{
			CurrentLocale = CurrentPack.Locale;
		}
		SettingsRoot.Game.Main.Localization.OnValueChanged += SetLocalization;
		SettingsController.GameSettingsController.LocalizationManagerInitialized();
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
