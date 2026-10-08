using System;
using System.Collections.Generic;
using System.Linq;

namespace RRT.TestHarness
{
    // Pure policy for forcing Story.Derived keys in forced runs: no Unity or game types, so the offline self-test can load it.
    // A Derived key is an OR of AND-groups over flags and other Derived keys. To force it, pick the first group whose leaves
    // can all be set (persistent flags, or nested Derived keys that resolve the same way), preferring groups made only of
    // persistent flags. Nested keys resolve recursively with a depth limit and a cycle guard.
    public static class DerivedForcing
    {
        public const int MaxDepth = 8;

        /// <summary>
        /// The persistent flags to set so that <paramref name="key"/> holds, or null when no group can be forced.
        /// <paramref name="held"/> reports keys already true; <paramref name="persistent"/> reports flags the harness can set.
        /// An already-held key needs nothing (an empty list).
        /// </summary>
        public static List<string>? Leaves(string key, IDictionary<string, string[][]> derived, Func<string, bool> persistent,
            Func<string, bool> held)
            => Resolve(key, derived, persistent, held, 0, new HashSet<string>(StringComparer.Ordinal));

        static List<string>? Resolve(string key, IDictionary<string, string[][]> derived, Func<string, bool> persistent,
            Func<string, bool> held, int depth, HashSet<string> visiting)
        {
            if (held(key)) return new List<string>();
            if (!derived.TryGetValue(key, out var groups) || groups == null)
                return persistent(key) ? new List<string> { key } : null;
            if (depth >= MaxDepth || !visiting.Add(key)) return null;
            try
            {
                // Groups made only of persistent flags come first; otherwise the authored order.
                var ordered = groups.Where(g => g != null).Select((g, i) => (g, i))
                    .OrderBy(x => x.g.All(persistent) ? 0 : 1).ThenBy(x => x.i).Select(x => x.g);
                foreach (var group in ordered)
                {
                    var leaves = new List<string>();
                    bool ok = true;
                    foreach (var part in group)
                    {
                        var sub = Resolve(part, derived, persistent, held, depth + 1, visiting);
                        if (sub == null) { ok = false; break; }
                        leaves.AddRange(sub);
                    }
                    if (ok) return leaves.Distinct(StringComparer.Ordinal).ToList();
                }
                return null;
            }
            finally { visiting.Remove(key); }
        }
    }
}
