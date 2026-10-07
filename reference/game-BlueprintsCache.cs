using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using JetBrains.Annotations;
using Kingmaker.Blueprints.JsonSystem.BinaryFormat;
using Kingmaker.Blueprints.JsonSystem.Converters;
using Kingmaker.BundlesLoading;
using Kingmaker.Modding;
using Kingmaker.Utility;

namespace Kingmaker.Blueprints.JsonSystem;

public class BlueprintsCache
{
	private struct BlueprintCacheEntry
	{
		public uint Offset;

		public SimpleBlueprint Blueprint;
	}

	[NotNull]
	private readonly Dictionary<BlueprintGuid, BlueprintCacheEntry> m_LoadedBlueprints = new Dictionary<BlueprintGuid, BlueprintCacheEntry>();

	private FileStream m_PackFile;

	private ReflectionBasedSerializer m_PackSerializer;

	private object m_Lock = new object();

	public void Init()
	{
		string path = BundlesLoadService.BundlesPath("blueprints-pack.bbp");
		m_PackFile = new FileStream(path, FileMode.Open, FileAccess.Read);
		byte[] array = new byte[16];
		using (BinaryReader binaryReader = new BinaryReader(m_PackFile, Encoding.UTF8, leaveOpen: true))
		{
			using (CodeTimer.New("Loading TOC"))
			{
				int num = binaryReader.ReadInt32();
				for (int i = 0; i < num; i++)
				{
					binaryReader.Read(array, 0, 16);
					BlueprintGuid key = new BlueprintGuid(array);
					uint offset = binaryReader.ReadUInt32();
					m_LoadedBlueprints.Add(key, new BlueprintCacheEntry
					{
						Offset = offset
					});
				}
			}
		}
		m_PackSerializer = new ReflectionBasedSerializer(new PrimitiveSerializer(new BinaryReader(m_PackFile), UnityObjectConverter.AssetList));
	}

	public SimpleBlueprint Load(BlueprintGuid guid)
	{
		lock (m_Lock)
		{
			if (m_LoadedBlueprints.TryGetValue(guid, out var value))
			{
				if (value.Blueprint == null)
				{
					if (value.Offset == 0)
					{
						return null;
					}
					using (ProfileScope.New("LoadBlueprint"))
					{
						m_PackFile.Seek(value.Offset, SeekOrigin.Begin);
						SimpleBlueprint bp = null;
						try
						{
							m_PackSerializer.Blueprint(ref bp);
						}
						catch (Exception)
						{
							PFLog.Default.Error($"Exception when load blueprint. BlueprintGuid = {guid}");
							throw;
						}
						if (bp == null)
						{
							return null;
						}
						OwlcatModificationsManager.Instance.OnResourceLoaded(bp, guid.ToString(), out var replacement);
						bp = (replacement as SimpleBlueprint) ?? bp;
						value.Blueprint = bp;
						value.Blueprint.OnEnable();
						m_LoadedBlueprints[guid] = value;
					}
				}
				return value.Blueprint;
			}
		}
		return null;
	}

	public SimpleBlueprint AddCachedBlueprint(BlueprintGuid guid, SimpleBlueprint bp)
	{
		m_LoadedBlueprints[guid] = new BlueprintCacheEntry
		{
			Blueprint = bp
		};
		return m_LoadedBlueprints[guid].Blueprint;
	}

	public void RemoveCachedBlueprint(BlueprintGuid guid)
	{
		m_LoadedBlueprints.Remove(guid);
	}

	public void ForEachLoaded(Action<BlueprintGuid, SimpleBlueprint> action)
	{
		foreach (var (arg, blueprintCacheEntry2) in m_LoadedBlueprints)
		{
			action(arg, blueprintCacheEntry2.Blueprint);
		}
	}
}
