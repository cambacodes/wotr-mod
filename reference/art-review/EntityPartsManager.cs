using System;
using System.Collections;
using System.Collections.Generic;
using JetBrains.Annotations;
using Kingmaker.QA;
using Kingmaker.Utility;
using Newtonsoft.Json;
using Owlcat.Runtime.Core.Utils;

namespace Kingmaker.EntitySystem;

public class EntityPartsManager : IDisposable
{
	[JsonProperty]
	private readonly List<EntityPart> m_Parts = new List<EntityPart>();

	private readonly Dictionary<Type, IList> m_CachedLists = new Dictionary<Type, IList>();

	private readonly List<EntityPartCached> m_Cache = new List<EntityPartCached>();

	public EntityDataBase Owner { get; private set; }

	[UsedImplicitly]
	[ShowInStateExplorer]
	private IEnumerable<EntityPart> Parts => m_Parts;

	[CanBeNull]
	private IEntityPartsManagerDelegate Delegate => Owner as IEntityPartsManagerDelegate;

	[JsonConstructor]
	public EntityPartsManager(EntityDataBase owner)
	{
		Owner = owner;
	}

	[CanBeNull]
	public TPart Get<TPart>() where TPart : EntityPart
	{
		EntityPartCached entityPartCached = EntityPartsCacheAccessor<TPart>.Get(m_Cache);
		if (entityPartCached.Cached)
		{
			return (TPart)entityPartCached.Part;
		}
		TPart val = null;
		for (int i = 0; i < m_Parts.Count; i++)
		{
			if (m_Parts[i] is TPart val2)
			{
				val = val2;
				break;
			}
		}
		EntityPartsCacheAccessor<TPart>.Set(m_Cache, val);
		return val;
	}

	public List<TPart> GetAll<TPart>() where TPart : class
	{
		UpdateCache<TPart>();
		return (List<TPart>)m_CachedLists.Get(typeof(TPart));
	}

	public IEnumerable<TPart> GetAll<TPart>(Func<TPart, bool> pred) where TPart : class
	{
		foreach (TPart item in GetAll<TPart>())
		{
			if (pred(item))
			{
				yield return item;
			}
		}
	}

	private TPart Add<TPart>() where TPart : EntityPart, new()
	{
		TPart val = new TPart();
		m_Parts.Add(val);
		AddToCache(val);
		EntityPartsCacheAccessor<TPart>.Add(m_Cache, val);
		val.AttachToEntity(Owner);
		try
		{
			Delegate?.OnPartAdded(val);
		}
		catch (Exception ex)
		{
			PFLog.Entity.Exception(ex, null);
		}
		return val;
	}

	public TPart Ensure<TPart>() where TPart : EntityPart, new()
	{
		TPart val = Get<TPart>();
		if (val != null)
		{
			return val;
		}
		return Add<TPart>();
	}

	public void Remove<TPart>() where TPart : EntityPart
	{
		foreach (EntityPart item in m_Parts.ToTempList())
		{
			if (item is TPart)
			{
				Remove(item);
			}
		}
	}

	public void Remove(EntityPart part)
	{
		if (m_Parts.Remove(part))
		{
			RemoveFromCache(part);
			try
			{
				Delegate?.OnPartRemoved(part);
			}
			catch (Exception ex)
			{
				PFLog.Entity.Exception(ex, null);
			}
			if (Owner != null && Owner.IsTurnedOn)
			{
				part.TurnOff();
			}
			part.Dispose();
			if (part.IndexInCache.HasValue)
			{
				m_Cache[part.IndexInCache.Value] = default(EntityPartCached);
			}
		}
	}

	public void RemoveAll<TPart>(Predicate<TPart> pred) where TPart : EntityPart
	{
		foreach (EntityPart item in m_Parts.ToTempList())
		{
			if (item is TPart obj && pred(obj))
			{
				Remove(item);
			}
		}
	}

	public void ViewDidAttach()
	{
		foreach (EntityPart part in m_Parts)
		{
			part.ViewDidAttach();
		}
	}

	public void ViewWillDetach()
	{
		foreach (EntityPart part in m_Parts)
		{
			part.ViewWillDetach();
		}
	}

	public void PreSave()
	{
		foreach (EntityPart part in m_Parts)
		{
			part.PreSave();
		}
	}

	public void RestoreOwnerLink(EntityDataBase owner)
	{
		Owner = owner;
		foreach (EntityPart part in m_Parts)
		{
			part.RestoreOwnerLink(owner);
		}
	}

	public void PostLoad()
	{
		if (Owner == null)
		{
			PFLog.Entity.ErrorWithReport("Owner is null");
			return;
		}
		foreach (EntityPart item in m_Parts.ToTempList())
		{
			item.PostLoad();
			try
			{
				Delegate?.OnPartPostLoad(item);
			}
			catch (Exception ex)
			{
				PFLog.Entity.Exception(ex, null);
			}
		}
		try
		{
			Delegate?.OnPartsManagerPostLoad(this);
		}
		catch (Exception ex2)
		{
			PFLog.Entity.Exception(ex2, null);
		}
	}

	public void ApplyPostLoadFixes()
	{
		foreach (EntityPart item in m_Parts.ToTempList())
		{
			item.ApplyPostLoadFixes();
		}
	}

	public void TurnOn()
	{
		foreach (EntityPart item in m_Parts.ToTempList())
		{
			item.TurnOn();
		}
	}

	public void TurnOff()
	{
		foreach (EntityPart item in m_Parts.ToTempList())
		{
			item.TurnOff();
		}
	}

	public void Dispose()
	{
		foreach (EntityPart item in m_Parts.ToTempList())
		{
			Remove(item);
		}
		m_Parts.Clear();
		m_CachedLists.Clear();
	}

	private void UpdateCache<TPart>() where TPart : class
	{
		if (typeof(TPart) == typeof(EntityPart))
		{
			return;
		}
		List<TPart> list = (List<TPart>)m_CachedLists.Get(typeof(TPart));
		if (list != null)
		{
			return;
		}
		list = new List<TPart>();
		m_CachedLists.Add(typeof(TPart), list);
		foreach (EntityPart part in m_Parts)
		{
			if (part is TPart item)
			{
				list.Add(item);
			}
		}
	}

	private void AddToCache(EntityPart part)
	{
		foreach (KeyValuePair<Type, IList> cachedList in m_CachedLists)
		{
			if (cachedList.Key.IsInstanceOfType(part))
			{
				cachedList.Value.Add(part);
			}
		}
	}

	private void RemoveFromCache(EntityPart part)
	{
		foreach (KeyValuePair<Type, IList> cachedList in m_CachedLists)
		{
			if (cachedList.Key.IsInstanceOfType(part))
			{
				cachedList.Value.Remove(part);
			}
		}
	}

	public void ClearCache()
	{
		m_Cache.Clear();
		m_CachedLists.Clear();
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
