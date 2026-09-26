using System.Collections.Generic;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Cheats;
using Kingmaker.ElementsSystem;
using Newtonsoft.Json;
using Owlcat.QA.Validation;
using Owlcat.Runtime.Core.Logging;
using UnityEngine;

namespace Kingmaker.Blueprints;

[TypeId("3ec4f91d40b87d34197f44f40a969d92")]
public class BlueprintScriptableObject : SimpleBlueprint, IElementsOwner, IHavePrototype
{
	[NonOverridable]
	[SerializeField]
	[JsonProperty(PropertyName = "PrototypeLink")]
	[HideInInspector]
	private string m_PrototypeId;

	[NonOverridable]
	[SerializeField]
	[JsonProperty(PropertyName = "m_Overrides", DefaultValueHandling = DefaultValueHandling.Ignore)]
	[HideInInspector]
	private List<string> m_Overrides = new List<string>();

	[NonOverridable]
	[SkipValidation]
	[HideInInspector]
	[SerializeField]
	[SerializeReference]
	private BlueprintComponent[] Components;

	[SerializeField]
	[TextArea(5, 6)]
	public string Comment;

	public BlueprintComponent[] ComponentsArray
	{
		get
		{
			BlueprintComponent[] obj = Components ?? new BlueprintComponent[0];
			BlueprintComponent[] result = obj;
			Components = obj;
			return result;
		}
		set
		{
			Components = value ?? new BlueprintComponent[0];
		}
	}

	public List<Element> ElementsArray
	{
		get
		{
			List<Element> obj = m_AllElements ?? new List<Element>();
			List<Element> result = obj;
			m_AllElements = obj;
			return result;
		}
	}

	public string AssetGuidThreadSafe => AssetGuid.ToString();

	public BlueprintScriptableObject PrototypeLink => null;

	public override string ToString()
	{
		return name;
	}

	public override void OnValidate()
	{
		if (BlueprintValidationHelper.AllowOnValidate)
		{
			base.OnValidate();
		}
	}

	public virtual void OnEnableWithLibrary()
	{
	}

	public override void OnEnable()
	{
		base.OnEnable();
		BlueprintComponent[] componentsArray = ComponentsArray;
		for (int i = 0; i < componentsArray.Length; i++)
		{
			componentsArray[i].OwnerBlueprint = this;
		}
		foreach (Element item in ElementsArray)
		{
			if (item != null)
			{
				item.Owner = this;
			}
			else
			{
				LogChannel.System.Warning("BlueprintScriptableObject.OnEnable: blueprint has null in ElementsArray (" + Utilities.GetBlueprintPath(this) + ")");
			}
		}
		OnEnableWithLibrary();
	}
}
