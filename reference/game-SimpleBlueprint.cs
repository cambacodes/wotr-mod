using System;
using System.Collections.Generic;
using System.Runtime.Serialization;
using JetBrains.Annotations;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.ElementsSystem;
using Kingmaker.Utility;
using Newtonsoft.Json;
using Owlcat.QA.Validation;
using Owlcat.Runtime.Core.Logging;
using UnityEngine;

namespace Kingmaker.Blueprints;

[Serializable]
[TypeId("0b3cc43201601904bb7eb333c9b646ff")]
public class SimpleBlueprint : IScriptableObjectWithAssetId, ICanBeLogContext, IValidated
{
	[JsonIgnore]
	[NonOverridable]
	[InspectorReadOnly]
	public string name;

	public BlueprintGuid AssetGuid;

	[SerializeField]
	[SerializeReference]
	[HideInInspector]
	[JsonIgnore]
	[SkipValidation]
	protected List<Element> m_AllElements;

	[NonSerialized]
	[NonOverridable]
	[NotNull]
	private string[] m_ValidationStatus = Array.Empty<string>();

	string IScriptableObjectWithAssetId.name
	{
		get
		{
			return name;
		}
		set
		{
			name = value;
		}
	}

	BlueprintGuid IScriptableObjectWithAssetId.AssetGuid
	{
		get
		{
			return AssetGuid;
		}
		set
		{
			AssetGuid = value;
		}
	}

	public bool HasErrors => m_ValidationStatus.Length != 0;

	public IEnumerable<string> Errors => m_ValidationStatus;

	public void Become(SimpleBlueprint other)
	{
		JsonUtility.FromJsonOverwrite(JsonUtility.ToJson(other), this);
	}

	[OnDeserializing]
	internal void OnDeserializing(StreamingContext context)
	{
		if (Json.BlueprintBeingRead != null)
		{
			AssetGuid = BlueprintGuid.Parse(Json.BlueprintBeingRead.AssetId);
			Json.BlueprintBeingRead.Data = this;
		}
	}

	public virtual void OnValidate()
	{
	}

	public virtual void OnEnable()
	{
	}

	protected virtual void ApplyValidation(ValidationContext context, int parentIndex)
	{
	}

	public void Validate()
	{
	}

	public virtual void Validate(ValidationContext context, int parentIndex)
	{
	}

	public int GetInstanceID()
	{
		if (!(AssetGuid == BlueprintGuid.Empty))
		{
			return AssetGuid.GetHashCode();
		}
		return 0;
	}

	public static implicit operator bool(SimpleBlueprint o)
	{
		return o != null;
	}

	public static T Instantiate<T>(T obj) where T : UnityEngine.Object
	{
		return UnityEngine.Object.Instantiate(obj);
	}

	public void AddToElementsList(Element e)
	{
		m_AllElements = m_AllElements ?? new List<Element>();
		m_AllElements.Add(e);
		e.Owner = this;
	}

	public void RemoveFromElementsList(Element element)
	{
		m_AllElements?.Remove(m_AllElements.FirstItem((Element e) => e?.name == element.name));
	}
}
