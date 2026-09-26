using System.Collections.Generic;
using JetBrains.Annotations;
using Kingmaker.Utility;
using Newtonsoft.Json;

namespace Kingmaker.EntitySystem;

public class EntityPartKeyValueStorage : EntityPart
{
	[JsonProperty]
	private readonly Dictionary<string, Dictionary<string, string>> m_Data = new Dictionary<string, Dictionary<string, string>>();

	[NotNull]
	public Dictionary<string, string> GetStorage(string storageName)
	{
		Dictionary<string, string> dictionary = m_Data.Get(storageName);
		if (dictionary == null)
		{
			dictionary = new Dictionary<string, string>();
			m_Data.Add(storageName, dictionary);
		}
		return dictionary;
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
