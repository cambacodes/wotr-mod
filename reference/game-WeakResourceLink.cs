using System;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.ResourceLinks;

[Serializable]
public abstract class WeakResourceLink : IEquatable<WeakResourceLink>
{
	[SerializeField]
	[HideInInspector]
	[FormerlySerializedAs("m_AssetId")]
	[FormerlySerializedAs("guid")]
	public string AssetId;

	public abstract UnityEngine.Object LoadObject();

	private static bool Equals(WeakResourceLink l1, WeakResourceLink l2)
	{
		if ((object)l1 == l2)
		{
			return true;
		}
		if ((object)l1 == null || (object)l2 == null)
		{
			return false;
		}
		return l1.AssetId == l2.AssetId;
	}

	public bool Equals(WeakResourceLink obj)
	{
		return Equals(this, obj);
	}

	public override bool Equals(object obj)
	{
		return Equals(obj as WeakResourceLink);
	}

	public static bool operator ==(WeakResourceLink obj1, WeakResourceLink obj2)
	{
		return Equals(obj1, obj2);
	}

	public static bool operator !=(WeakResourceLink obj1, WeakResourceLink obj2)
	{
		return !Equals(obj1, obj2);
	}

	public override int GetHashCode()
	{
		return AssetId.GetHashCode();
	}
}
