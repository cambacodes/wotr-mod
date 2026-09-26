using System.Collections.Generic;
using System.Linq;
using Kingmaker.Blueprints;
using Kingmaker.EntitySystem;
using Kingmaker.PubSubSystem;
using Newtonsoft.Json;

namespace Kingmaker.AreaLogic.QuestSystem;

public class UnlockableFlagsManager
{
	[JsonProperty]
	private readonly Dictionary<BlueprintUnlockableFlag, int> m_UnlockedFlags = new Dictionary<BlueprintUnlockableFlag, int>();

	public Dictionary<BlueprintUnlockableFlag, int> UnlockedFlags => m_UnlockedFlags;

	[ShowInStateExplorer]
	private IEnumerable<string> UnlocksInStateExplorer => m_UnlockedFlags.Select((KeyValuePair<BlueprintUnlockableFlag, int> p) => p.Key.name + ": " + p.Value);

	public void Lock(BlueprintUnlockableFlag flag)
	{
		m_UnlockedFlags.Remove(flag);
		EventBus.RaiseEvent(delegate(IUnlockHandler h)
		{
			h.HandleLock(flag);
		});
	}

	public void Unlock(BlueprintUnlockableFlag flag)
	{
		if (!IsUnlocked(flag))
		{
			m_UnlockedFlags.Add(flag, 0);
			EventBus.RaiseEvent(delegate(IUnlockHandler h)
			{
				h.HandleUnlock(flag);
			});
		}
	}

	public void SetFlagValue(BlueprintUnlockableFlag flag, int value)
	{
		bool num = !m_UnlockedFlags.ContainsKey(flag);
		m_UnlockedFlags[flag] = value;
		if (num)
		{
			EventBus.RaiseEvent(delegate(IUnlockHandler h)
			{
				h.HandleUnlock(flag);
			});
		}
		EventBus.RaiseEvent(delegate(IUnlockValueHandler h)
		{
			h.HandleFlagValue(flag, value);
		});
	}

	public int GetFlagValue(BlueprintUnlockableFlag flag)
	{
		m_UnlockedFlags.TryGetValue(flag, out var value);
		return value;
	}

	public bool IsUnlocked(BlueprintUnlockableFlag flag)
	{
		return m_UnlockedFlags.ContainsKey(flag);
	}

	public bool IsLocked(BlueprintUnlockableFlag flag)
	{
		return !m_UnlockedFlags.ContainsKey(flag);
	}

	public override string ToString()
	{
		return "Unlocks";
	}
}
