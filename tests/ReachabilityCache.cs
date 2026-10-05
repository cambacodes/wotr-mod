using System;
using System.Collections.Generic;
using System.Text.Json;
using Tirabade;

// Share one ordered traversal across questions about the exact same starting
// world. Keep every yielded flag, including intermediate and aborted outcomes.
// Each cache belongs to one suite invocation; mutated stories get new caches.
internal sealed class ReachabilityCache : IDisposable
{
    private sealed class History
    {
        internal readonly HashSet<string> Flags = new();
        internal readonly IEnumerator<Snapshot> Walk;
        internal bool Finished;
        internal History(IEnumerable<Snapshot> walk) { Walk = walk.GetEnumerator(); }
        internal bool Reaches(string flag)
        {
            while (!Flags.Contains(flag) && !Finished)
            {
                if (!Walk.MoveNext()) { Finished = true; Walk.Dispose(); }
                else Flags.UnionWith(Walk.Current.Flags);
            }
            return Flags.Contains(flag);
        }
    }
    private readonly Dictionary<string, History> histories = new();
    private static readonly JsonSerializerOptions options = new() { IncludeFields = true };
    internal bool Reaches(Snapshot start, string flag, int chapter, Func<IEnumerable<Snapshot>> walk, string partition = "")
    {
        // JSON includes timestamps, resources, contacts and all flags; nothing
        // relevant to guards or payment is projected away for equivalence.
        string key = chapter + ":" + JsonSerializer.Serialize(partition) + ":" + JsonSerializer.Serialize(start, options);
        if (!histories.TryGetValue(key, out var history)) histories[key] = history = new History(walk());
        return history.Reaches(flag);
    }
    public void Dispose()
    {
        foreach (var history in histories.Values) if (!history.Finished) history.Walk.Dispose();
    }
}
