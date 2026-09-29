using System;
using System.Collections.Generic;
using System.Linq;

namespace RRT.TestHarness
{
    // Pure policy for satisfying a scene's DelayHours in forced runs: no Unity or game types, so the offline self-test can
    // load it. Rules.Available compares the snapshot hour against the latest "hour.<key>" time of the scene's held Requires
    // (and held RequiresAnyGroups members): the page opens only once DelayHours have passed since then. A forced run sets its
    // flags "now", and a latch such as trickster.ever is recorded "now" by Main.RecordLatches on the first idle tick after a
    // load of a save that predates it, so the delay can never pass. The harness backdates those stored times instead of
    // advancing game time: it writes "hour.<key>" = TargetHour + 1 (the stored value is hour + 1; 0 means unset).
    public static class DelayForcing
    {
        /// <summary>Extra hours past DelayHours, so an hour boundary crossed mid-run cannot close the page again.</summary>
        public const int MarginHours = 2;

        public sealed class Result
        {
            /// <summary>The game hour the backdated keys are recorded at (Hour - DelayHours - margin).</summary>
            public int TargetHour;
            /// <summary>Keys whose "hour.&lt;key&gt;" time is set to TargetHour (and the key itself persisted, if a flag).</summary>
            public List<string> Backdate = new List<string>();
            /// <summary>Why the delay cannot be satisfied from this save, or null.</summary>
            public string? Unmet;
        }

        /// <summary>
        /// What to backdate so that <paramref name="delayHours"/> have passed at <paramref name="hour"/> for every key in
        /// <paramref name="keys"/>. <paramref name="times"/> holds the snapshot's recorded hours; <paramref name="hourSettable"/>
        /// reports whether "hour.&lt;key&gt;" is a flag the harness can write. A key with no time yet is backdated too when it
        /// can be (a latch or a forced flag may be timestamped "now" later in the run); it only makes the delay unmet when
        /// it already carries a time that blocks.
        /// </summary>
        public static Result Plan(int delayHours, int hour, IDictionary<string, int> times, IEnumerable<string> keys,
            Func<string, bool> hourSettable, int margin = MarginHours)
        {
            var result = new Result { TargetHour = hour - delayHours - margin };
            if (delayHours <= 0) return result;
            var unmet = new List<string>();
            foreach (var key in keys.Distinct(StringComparer.Ordinal))
            {
                bool timed = times.TryGetValue(key, out int at);
                if (timed && hour - at >= delayHours + margin) continue;
                bool blocks = timed && hour - at < delayHours;
                if (result.TargetHour < 0)
                {
                    if (blocks) unmet.Add(key + " (save is at hour " + hour + ", needs " + delayHours + " h)");
                    continue;
                }
                if (!hourSettable(key))
                {
                    if (blocks) unmet.Add(key + " (no hour." + key + " flag to backdate)");
                    continue;
                }
                result.Backdate.Add(key);
            }
            if (unmet.Count > 0) result.Unmet = "delay " + delayHours + " h unmet: " + string.Join(", ", unmet);
            return result;
        }
    }
}
