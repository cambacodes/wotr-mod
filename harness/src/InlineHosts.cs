using System;
using System.Collections.Generic;
using System.Linq;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace RRT.TestHarness
{
    // Pure data and policy for the -Inline mode: no Unity or game types, so the offline self-test can load it.
    // harness/resolve-inline-hosts.py writes inline-hosts.json from blueprints.zip and Story.json; run-harness.ps1
    // copies it next to the harness DLL.
    public sealed class InlineHosts
    {
        public const string FileName = "inline-hosts.json";

        public JObject? GeneratedFrom;
        public JObject? Summary;
        public Dictionary<string, InlineScene> Scenes = new Dictionary<string, InlineScene>(StringComparer.Ordinal);
        public Dictionary<string, InlineList> Lists = new Dictionary<string, InlineList>(StringComparer.Ordinal);

        public static InlineHosts Parse(string json) =>
            JsonConvert.DeserializeObject<InlineHosts>(json, new JsonSerializerSettings { MissingMemberHandling = MissingMemberHandling.Ignore })
            ?? new InlineHosts();

        /// <summary>
        /// The host to drive a scene through: the first of the scene's live entry lists (Rules.EntryTargets order) that has a
        /// reachable host dialog, fewest clicks first. Null with a reason when none resolves.
        /// </summary>
        public (string List, InlineHost Host)? Choose(IEnumerable<string> entryLists, out string? reason)
        {
            reason = null;
            var problems = new List<string>();
            foreach (var list in entryLists)
            {
                string key = Norm(list);
                if (!Lists.TryGetValue(key, out var entry)) { problems.Add(Short(key) + ": not in " + FileName + " (stale; rerun resolve-inline-hosts.py)"); continue; }
                var host = entry.Hosts.FirstOrDefault(h => h.Reachable);
                if (host != null) return (list, host);
                problems.Add(Short(key) + ": " + (entry.Reason ?? "no reachable host (" + string.Join(", ", entry.Hosts.Select(h => h.DialogName + " " + h.Reason)) + ")"));
            }
            reason = problems.Count == 0 ? "the scene has no native entry list" : string.Join("; ", problems);
            return null;
        }

        public static string Norm(string guid) => (guid ?? "").Replace("-", "").ToLowerInvariant();
        static string Short(string guid) => guid.Length > 8 ? guid.Substring(0, 8) : guid;

        /// <summary>The entry answer blueprint name RRT gives a scene on one list (Main.Build / BuildReturnToList).</summary>
        public static string EntryName(string sceneId, string list, bool returnToList) =>
            "RRT_entry." + sceneId + (returnToList ? "." + list : "");

        /// <summary>One answer shown by the host dialog, as the navigator sees it.</summary>
        public struct Shown
        {
            public string Name, Guid;
            public bool IsContinue, IsExit, Conditioned;
        }

        /// <summary>
        /// Navigation policy through a native host toward the list: the entry answer when it is shown; else the shown answer
        /// with the fewest clicks left (answerDist), least used first, then in order; else the Continue answer; else the
        /// least used unconditioned native answer (never Exit, never another RRT answer). -1 when only Exit or RRT answers remain.
        /// </summary>
        public static int Pick(IList<Shown> shown, string entryName, InlineHost host, IDictionary<string, int> used, out string why)
        {
            for (int i = 0; i < shown.Count; i++)
                if (shown[i].Name == entryName) { why = "entry"; return i; }
            int Used(int i) => used.TryGetValue(shown[i].Guid ?? "", out int n) ? n : 0;
            int best = -1, bestDist = int.MaxValue;
            for (int i = 0; i < shown.Count; i++)
            {
                if (shown[i].IsExit || !host.AnswerDist.TryGetValue(Norm(shown[i].Guid), out int d)) continue;
                if (best < 0 || d < bestDist || d == bestDist && Used(i) < Used(best)) { best = i; bestDist = d; }
            }
            if (best >= 0) { why = "toward list (" + bestDist + " click(s) left)"; return best; }
            for (int i = 0; i < shown.Count; i++)
                if (shown[i].IsContinue) { why = "continue"; return i; }
            var fallback = Enumerable.Range(0, shown.Count)
                .Where(i => !shown[i].IsExit && !(shown[i].Name ?? "").StartsWith("RRT_", StringComparison.Ordinal))
                .OrderBy(i => shown[i].Conditioned ? 1 : 0).ThenBy(Used).ThenBy(i => i).ToList();
            if (fallback.Count > 0) { why = "off the resolved path (first unconditioned, least used)"; return fallback[0]; }
            why = "only Exit or RRT answers are shown";
            return -1;
        }
    }

    public sealed class InlineScene
    {
        public string Kind = "";
        public List<string> Lists = new List<string>();
        public Dictionary<string, string> Entry = new Dictionary<string, string>(StringComparer.Ordinal);
        public bool Resolved;
        public string? Reason;
        public JObject? Host;
    }

    public sealed class InlineList
    {
        public string List = "";
        public string ListName = "";
        public List<InlineHost> Hosts = new List<InlineHost>();
        public string? Reason;
    }

    public sealed class InlineHost
    {
        public string Dialog = "";
        public string DialogName = "";
        public List<string> Cues = new List<string>();
        public List<string> CueNames = new List<string>();
        /// <summary>BlueprintUnit of the dialog's first (or owning) cue speaker, when it names one.</summary>
        public string? Speaker;
        public bool Reachable;
        public int Clicks;
        public string? Reason;
        public List<JObject> Path = new List<JObject>();
        /// <summary>Native answer guid -> clicks from selecting it to a cue that shows the list (offline graph).</summary>
        public Dictionary<string, int> AnswerDist = new Dictionary<string, int>(StringComparer.Ordinal);

        public string PathText() => string.Join(" > ", Path.Select(p => (string?)p["at"] + ":" + (string?)p["take"]));
    }
}
