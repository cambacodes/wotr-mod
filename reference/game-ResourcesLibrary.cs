using System;
using System.Collections.Generic;
using System.Diagnostics;
using JetBrains.Annotations;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Blueprints.Root;
using Kingmaker.BundlesLoading;
using Kingmaker.ElementsSystem;
using Kingmaker.Modding;
using Kingmaker.ResourceLinks;
using Kingmaker.Utility;
using Kingmaker.Visual.Particles;
using Owlcat.Runtime.Core.Logging;
using Owlcat.Runtime.Core.Utils;
using Pathfinding.Util;
using UnityEngine;
using UnityEngine.Rendering;

namespace Kingmaker.Blueprints;

public static class ResourcesLibrary
{
	public enum CleanupMode
	{
		UnloadEverything,
		UnloadEverythingWithoutHold,
		UnloadAndCleanRequests,
		UnloadNonRequested
	}

	private class LoadedResource
	{
		[CanBeNull]
		public UnityEngine.Object Resource;

		public string AssetId;

		public int RequestCounter;

		public int HandleCounter;

		public LoadedResource([NotNull] UnityEngine.Object resource)
		{
			Resource = resource;
		}

		public LoadedResource()
		{
		}

		public void Unload()
		{
			if (!string.IsNullOrEmpty(AssetId))
			{
				BundlesLoadService.Instance.UnloadBundleForAsset(AssetId);
			}
		}
	}

	private class BlueprintRootReference : BlueprintReference<BlueprintRoot>
	{
		public BlueprintRootReference()
		{
			deserializedGuid = BlueprintGuid.Parse("2d77316c72b9ed44f888ceefc2a131f6");
		}
	}

	private static bool s_Initialized;

	private static bool s_Preloading;

	private static readonly Queue<Func<UnityEngine.Object>> s_PreloadActionsQueue = new Queue<Func<UnityEngine.Object>>();

	private static bool s_SynchronousPreloading;

	private static bool s_DisablePreloading;

	[NotNull]
	private static readonly Dictionary<string, LoadedResource> s_LoadedResources = new Dictionary<string, LoadedResource>();

	public static readonly BlueprintsCache BlueprintsCache = new BlueprintsCache();

	public static object LoadedResources => s_LoadedResources;

	public static bool Preloading => s_Preloading;

	public static bool UseBundles => true;

	public static BlueprintReference<BlueprintRoot> RootRef { get; } = new BlueprintRootReference();

	public static bool IsAssetInBundle(string assetGuid)
	{
		if (!UseBundles)
		{
			return OwlcatModificationsManager.Instance.GetBundleNameForAsset(assetGuid) != null;
		}
		return true;
	}

	[CanBeNull]
	public static SimpleBlueprint TryGetBlueprint(BlueprintGuid assetId)
	{
		if (assetId == BlueprintGuid.Empty)
		{
			return null;
		}
		return BlueprintsCache.Load(assetId);
	}

	[CanBeNull]
	public static ElementsScriptableObject TryGetScriptable(string assetId)
	{
		if (string.IsNullOrEmpty(assetId))
		{
			return null;
		}
		return TryGetBlueprint(BlueprintGuid.Parse(assetId)) as ElementsScriptableObject;
	}

	public static void StartPreloadingMode()
	{
		s_Preloading = true;
	}

	public static void StopPreloadingMode()
	{
		if (s_PreloadActionsQueue.Count > 0)
		{
			PFLog.Default.Error("Stopping preloading while there are still preload requests pending");
			s_PreloadActionsQueue.Clear();
		}
		s_Preloading = false;
	}

	public static bool TickPreloading()
	{
		Stopwatch stopwatch = Stopwatch.StartNew();
		while (stopwatch.ElapsedMilliseconds < 400 && s_PreloadActionsQueue.Count > 0)
		{
			UnityEngine.Object obj = s_PreloadActionsQueue.Dequeue()();
			try
			{
				(obj as IRecursivePreloadResource)?.DoRecursivePreload();
			}
			catch (Exception ex)
			{
				PFLog.Default.Exception(ex, null);
			}
		}
		stopwatch.Stop();
		return s_PreloadActionsQueue.Count > 0;
	}

	public static void PreloadResource<TResource>(string assetId) where TResource : UnityEngine.Object
	{
		if (!s_Preloading)
		{
			PFLog.Default.Error("Resources preloading is only allowed in preloading mode");
		}
		else
		{
			if (string.IsNullOrEmpty(assetId))
			{
				return;
			}
			if (IsAssetInBundle(assetId) && !BundlesLoadService.Instance.HasLocation(assetId))
			{
				PFLog.Default.Error("Resources preloading: {0} has no bundle location", assetId);
				return;
			}
			LoadedResource loadedResource = s_LoadedResources.Get(assetId);
			if (loadedResource != null)
			{
				loadedResource.RequestCounter++;
				return;
			}
			loadedResource = new LoadedResource();
			loadedResource.RequestCounter++;
			s_LoadedResources[assetId] = loadedResource;
			if (s_SynchronousPreloading)
			{
				LoadResource<TResource>(assetId, loadedResource);
			}
			else
			{
				StartPreload<TResource>(assetId, loadedResource);
			}
		}
	}

	public static bool IsLoaded(string assetId)
	{
		return s_LoadedResources.ContainsKey(assetId);
	}

	public static IEnumerable<TResource> GetLoadedResourcesOfType<TResource>() where TResource : UnityEngine.Object
	{
		foreach (string key in s_LoadedResources.Keys)
		{
			if (s_LoadedResources[key].Resource is TResource val)
			{
				yield return val;
			}
		}
	}

	public static IEnumerable<string> GetLoadedAssetIdsOfType<TResource>() where TResource : UnityEngine.Object
	{
		foreach (string key in s_LoadedResources.Keys)
		{
			if (s_LoadedResources[key].Resource is TResource)
			{
				yield return key;
			}
		}
	}

	[CanBeNull]
	public static TResource TryGetResource<TResource>(string assetId, bool ignorePreloadWarning = false, bool hold = false) where TResource : UnityEngine.Object
	{
		if (s_Preloading && !ignorePreloadWarning)
		{
			PFLog.Default.Error("Resources loading is forbidden in preloading mode");
			return null;
		}
		LoadedResource loadedResource = s_LoadedResources.Get(assetId);
		if (loadedResource == null)
		{
			try
			{
				loadedResource = new LoadedResource();
				LoadResource<TResource>(assetId, loadedResource);
				s_LoadedResources[assetId] = loadedResource;
			}
			finally
			{
			}
		}
		loadedResource.RequestCounter++;
		if (hold)
		{
			loadedResource.HandleCounter++;
		}
		if (typeof(TResource) == typeof(GameObject) && (bool)loadedResource.Resource)
		{
			MonoBehaviour monoBehaviour = loadedResource.Resource as MonoBehaviour;
			if (monoBehaviour != null)
			{
				return monoBehaviour.gameObject as TResource;
			}
		}
		return loadedResource.Resource as TResource;
	}

	public static void FreeResourceRequest(string assetId, bool held = false)
	{
		LoadedResource loadedResource = s_LoadedResources.Get(assetId);
		if (loadedResource != null)
		{
			loadedResource.RequestCounter--;
			if (held)
			{
				loadedResource.HandleCounter--;
			}
		}
	}

	public static void HoldResource(string assetId)
	{
		LoadedResource loadedResource = s_LoadedResources.Get(assetId);
		if (loadedResource != null)
		{
			loadedResource.HandleCounter++;
		}
	}

	public static bool HasLoadedResource(string assetId)
	{
		return s_LoadedResources.Get(assetId) != null;
	}

	public static bool TryUnloadResource(string assetId)
	{
		if (s_Preloading)
		{
			return false;
		}
		LoadedResource loadedResource = s_LoadedResources.Get(assetId);
		s_LoadedResources.Remove(assetId);
		if (loadedResource.HandleCounter > 0 && BuildModeUtility.AdvancedLogs)
		{
			PFLog.Default.Error("Unload handled resource. AssetId = " + loadedResource.AssetId);
		}
		loadedResource?.Unload();
		return true;
	}

	public static void ForceUnloadResource(string assetId)
	{
		LoadedResource loadedResource = s_LoadedResources.Get(assetId);
		s_LoadedResources.Remove(assetId);
		if (loadedResource == null)
		{
			return;
		}
		UnityEngine.Object resource = loadedResource.Resource;
		if (loadedResource.HandleCounter > 0 && BuildModeUtility.AdvancedLogs)
		{
			PFLog.Default.Error("Unload handled resource. AssetId = " + loadedResource.AssetId);
		}
		loadedResource.Unload();
		if (!UseBundles)
		{
			return;
		}
		if (BundlesLoadService.Instance.IsAssetBundleLoaded(assetId))
		{
			PFLog.Bundles.Warning("Force-Unloaded resource " + assetId + " but its bundle is still loaded");
		}
		else if (!(resource is GameObject obj))
		{
			if (!(resource is Component component))
			{
				if ((object)resource != null)
				{
					Resources.UnloadAsset(resource);
				}
			}
			else
			{
				UnityEngine.Object.Destroy(component.gameObject);
			}
		}
		else
		{
			UnityEngine.Object.Destroy(obj);
		}
	}

	public static void CleanupLoadedCache(CleanupMode mode = CleanupMode.UnloadAndCleanRequests)
	{
		if (s_Preloading)
		{
			PFLog.Default.Error("Cannot Cleanup cache in preloading mode");
			return;
		}
		List<string> list = global::Pathfinding.Util.ListPool<string>.Claim();
		try
		{
			foreach (KeyValuePair<string, LoadedResource> s_LoadedResource in s_LoadedResources)
			{
				if (IsPooledResource(s_LoadedResource.Value.Resource))
				{
					continue;
				}
				if ((s_LoadedResource.Value.RequestCounter <= 0 && s_LoadedResource.Value.HandleCounter <= 0) || mode == CleanupMode.UnloadEverything || (mode == CleanupMode.UnloadEverythingWithoutHold && s_LoadedResource.Value.HandleCounter <= 0))
				{
					if (s_LoadedResource.Value.HandleCounter > 0 && BuildModeUtility.AdvancedLogs)
					{
						PFLog.Default.Error("Unload handled resource. AssetId = " + s_LoadedResource.Value.AssetId);
					}
					s_LoadedResource.Value.Unload();
					list.Add(s_LoadedResource.Key);
				}
				if (mode == CleanupMode.UnloadAndCleanRequests && s_LoadedResource.Value.HandleCounter <= 0)
				{
					s_LoadedResource.Value.RequestCounter = 0;
				}
			}
			foreach (string item in list)
			{
				s_LoadedResources.Remove(item);
			}
		}
		finally
		{
			global::Pathfinding.Util.ListPool<string>.Release(list);
		}
	}

	private static bool IsPooledResource(UnityEngine.Object resource)
	{
		GameObject gameObject = resource as GameObject;
		if (gameObject == null)
		{
			MonoBehaviour monoBehaviour = resource as MonoBehaviour;
			if (monoBehaviour != null)
			{
				gameObject = monoBehaviour.gameObject;
			}
		}
		if (gameObject == null)
		{
			return false;
		}
		PooledGameObject component = gameObject.GetComponent<PooledGameObject>();
		if (component != null)
		{
			return GameObjectsPool.HasPoolInstances(component);
		}
		return false;
	}

	[CanBeNull]
	private static void LoadResource<TResource>(string assetId, LoadedResource loaded) where TResource : UnityEngine.Object
	{
		using (CodeTimerTraceScope.New("Load resource", assetId))
		{
			try
			{
				if (string.IsNullOrEmpty(assetId))
				{
					return;
				}
				bool isPC = true;
				if (IsAssetInBundle(assetId))
				{
					TResource val = null;
					AssetBundle assetBundle = BundlesLoadService.Instance.RequestBundleForAsset(assetId);
					if ((bool)assetBundle)
					{
						loaded.AssetId = assetId;
						using (AddContextToUnityLog.New(assetId))
						{
							UnityEngine.Object obj = null;
							GameObject gameObject = null;
							if (typeof(TResource).IsSubclassOf(typeof(MonoBehaviour)))
							{
								obj = assetBundle.LoadAsset(assetId);
								ProfilingTrace.CurrentTrace?.AddArg(obj ? obj.name : "<null>");
								gameObject = obj as GameObject;
								if (gameObject != null)
								{
									val = gameObject.GetComponent<TResource>();
								}
							}
							else
							{
								val = assetBundle.LoadAsset<TResource>(assetId);
							}
							gameObject = ObjectExtensions.Or(gameObject, null) ?? (val as GameObject);
							TryToModifyResourceContent(gameObject, isPC);
						}
					}
					if (val == null)
					{
						PFLog.Default.Warning("Could not load resource (id = " + assetId + ", bundleName = " + (assetBundle ? assetBundle.ToString() : "<null>") + ", type = " + typeof(TResource).Name + ")");
						if (loaded.HandleCounter > 0 && BuildModeUtility.AdvancedLogs)
						{
							PFLog.Default.Error("Unload handled resource. AssetId = " + loaded.AssetId);
						}
						loaded.Unload();
					}
					else
					{
						StoreResource<TResource>(loaded, val);
					}
					return;
				}
				throw new InvalidOperationException("LibraryObject does not exist");
			}
			finally
			{
			}
		}
	}

	private static void TryToModifyResourceContent(GameObject go, bool isPC)
	{
		if (!(go != null))
		{
			return;
		}
		using (ProfileScope.New("RemoveObjectOnPlatform"))
		{
			foreach (RemoveObjectOnPlatform item in go.EnumerateComponentsInChildren<RemoveObjectOnPlatform>(includeInactive: true))
			{
				if ((isPC && item.RemoveOnPC) || (!isPC && item.RemoveOnConsole))
				{
					UnityEngine.Object.DestroyImmediate(item.gameObject, allowDestroyingAssets: true);
				}
				else
				{
					item.gameObject.SetActive(value: true);
				}
			}
		}
		using (ProfileScope.New("DisableShadowsOnDynamicObjects"))
		{
			if (!BuildModeUtility.Data.DisableShadowsOnDynamicObjects)
			{
				return;
			}
			foreach (Renderer item2 in go.EnumerateComponentsInChildren<Renderer>(includeInactive: true))
			{
				item2.shadowCastingMode = ShadowCastingMode.Off;
			}
		}
	}

	private static void StartPreload<TResource>(string assetId, LoadedResource loaded) where TResource : UnityEngine.Object
	{
		if (Application.isPlaying)
		{
			s_PreloadActionsQueue.Enqueue(delegate
			{
				LoadResource<TResource>(assetId, loaded);
				return s_LoadedResources.Get(assetId)?.Resource;
			});
		}
	}

	private static void StoreResource<TResource>(LoadedResource loaded, UnityEngine.Object resource) where TResource : UnityEngine.Object
	{
		if (typeof(TResource) == typeof(GameObject))
		{
			GameObject gameObject = resource as GameObject;
			if (gameObject != null)
			{
				MonoBehaviour monoBehaviour = gameObject.GetComponent<IResource>() as MonoBehaviour;
				if (monoBehaviour != null)
				{
					loaded.Resource = monoBehaviour;
				}
				else
				{
					loaded.Resource = gameObject;
				}
			}
		}
		else
		{
			loaded.Resource = resource as TResource;
		}
		string assetId = loaded.AssetId;
		OwlcatModificationsManager.Instance.OnResourceLoaded(resource, assetId, out var _);
	}

	[CanBeNull]
	public static TBlueprint TryGetBlueprint<TBlueprint>(string assetId) where TBlueprint : BlueprintScriptableObject
	{
		return (TBlueprint)TryGetBlueprint(BlueprintGuid.Parse(assetId));
	}

	[CanBeNull]
	public static TBlueprint TryGetBlueprint<TBlueprint>(BlueprintGuid assetId) where TBlueprint : BlueprintScriptableObject
	{
		return (TBlueprint)TryGetBlueprint(assetId);
	}

	[CanBeNull]
	public static T TryGetScriptable<T>(string assetId) where T : ElementsScriptableObject
	{
		return (T)TryGetScriptable(assetId);
	}

	public static BlueprintRoot GetRoot()
	{
		return RootRef.Get();
	}
}
