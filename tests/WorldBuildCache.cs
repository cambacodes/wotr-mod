using System;
using System.Collections.Generic;
using System.Text.Json;
using Tirabade;

// Only enabled within audited read-only route suites. A cache never crosses a
// suite boundary or a mutated Story. Keys retain the ENTIRE runtime snapshot;
// results come from production Rules.Complete, not a second implementation.
internal sealed class WorldBuildCache
{
    private readonly Story story;
    private readonly Dictionary<string, Snapshot> worlds = new();
    private static readonly JsonSerializerOptions options = new() { IncludeFields = true };
    internal int Builds { get; private set; }
    internal int Hits { get; private set; }
    internal WorldBuildCache(Story story) { this.story = story; }

    internal void Complete(Snapshot state)
    {
        string key = JsonSerializer.Serialize(state, options);
        if (worlds.TryGetValue(key, out var complete))
        {
            Hits++;
            // Preserve the supplied object and collection identities: callbacks
            // and callers observe the same in-place operation as Complete.
            state.Chapter = complete.Chapter; state.Hour = complete.Hour; state.Area = complete.Area;
            state.Flags.Clear(); state.Flags.UnionWith(complete.Flags);
            state.Times.Clear(); foreach (var pair in complete.Times) state.Times.Add(pair.Key, pair.Value);
            state.RestSpent.Clear(); foreach (var pair in complete.RestSpent) state.RestSpent.Add(pair.Key, pair.Value);
            if (complete.CrusadeResources == null) state.CrusadeResources = null;
            else
            {
                state.CrusadeResources ??= new Dictionary<string, int>();
                state.CrusadeResources.Clear();
                foreach (var pair in complete.CrusadeResources) state.CrusadeResources.Add(pair.Key, pair.Value);
            }
            state.AvailableContacts.Clear(); state.AvailableContacts.UnionWith(complete.AvailableContacts);
            state.SceneContacts.Clear(); state.SceneContacts.UnionWith(complete.SceneContacts);
        }
        else
        {
            Builds++;
            Rules.Complete(story, state);
            // Bounded memory during exhaustive histories. Eviction affects only
            // speed; the next miss calls the production implementation again.
            if (worlds.Count >= 2048) worlds.Clear();
            worlds.Add(key, Program.Copy(state));
        }
    }
}
