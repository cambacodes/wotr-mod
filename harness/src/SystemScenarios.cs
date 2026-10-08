using System;
using System.Collections.Generic;
using System.Linq;
using Newtonsoft.Json;

namespace RRT.TestHarness
{
    // Authored test metadata. A fixture is evidence of runtime execution only, never earned campaign history.
    public sealed class SystemScenario
    {
        public string Id = "";
        public string System = "";
        public int Chapter;
        public int? SaveChapter;
        public List<string>? FixtureFlags;
        public List<SystemStep> Steps = new List<SystemStep>();
    }

    public sealed class SystemStep
    {
        public string Scene = "";
        public bool Available = true;
        public bool Table;
        public bool ProbeOnly;
        public bool? RestSucceeded;
        public List<string> Remove = new List<string>();
        public List<string> Add = new List<string>();
        public Dictionary<string, int> RestSpent = new Dictionary<string, int>();
        // Exact scene/node/original-choice-index identities; never indices in the filtered visible answer list.
        public List<string> Answers = new List<string>();
        public List<string> ExpectFlags = new List<string>();
        public Dictionary<string, int> ExpectRestSpent = new Dictionary<string, int>();
        public List<string> LedgerEntries = new List<string>();
        public List<string> HiddenLedgerEntries = new List<string>();
    }

    public sealed class SystemCases
    {
        public int Schema = 1;
        public List<SystemScenario> Cases = new List<SystemScenario>();
        public static SystemCases Parse(string json)
        {
            var cases = JsonConvert.DeserializeObject<SystemCases>(json, new JsonSerializerSettings {
                MissingMemberHandling = MissingMemberHandling.Error, ObjectCreationHandling = ObjectCreationHandling.Replace
            }) ?? throw new FormatException("Empty system scenarios");
            if (cases.Schema != 1 || cases.Cases == null || cases.Cases.Count == 0)
                throw new FormatException("System scenarios need schema 1 and nonempty cases");
            var ids = new HashSet<string>(StringComparer.Ordinal);
            foreach (var c in cases.Cases)
            {
                if (string.IsNullOrWhiteSpace(c.Id) || !ids.Add(c.Id) || string.IsNullOrWhiteSpace(c.System)
                    || c.Chapter < 1 || c.Chapter > 6 || c.SaveChapter.HasValue && (c.SaveChapter < 1 || c.SaveChapter > 6)
                    || c.Steps == null || c.Steps.Count == 0)
                    throw new FormatException("Invalid/duplicate system scenario: " + c.Id);
                foreach (var s in c.Steps)
                    if (string.IsNullOrWhiteSpace(s.Scene) || s.Answers == null || s.Remove == null || s.Add == null
                        || s.RestSpent == null || s.ExpectFlags == null || s.ExpectRestSpent == null || s.LedgerEntries == null || s.HiddenLedgerEntries == null
                        || s.RestSpent.Values.Concat(s.ExpectRestSpent.Values).Any(n => n < 0)
                        || (!s.Available && s.Answers.Count > 0)
                        || s.Answers.Any(a => !a.StartsWith(s.Scene + "/", StringComparison.Ordinal)))
                        throw new FormatException("Invalid system step: " + c.Id + " / " + s.Scene);
            }
            return cases;
        }
    }

    public sealed class SystemCoverage
    {
        public string Scenario = "", System = "", Evidence = "", Result = "running";
        public bool Passed;
        public List<string> AvailabilityChecked = new List<string>();
        public List<string> ScenesTouched = new List<string>();
        public List<string> ChoicesTouched = new List<string>();
        public List<string> LedgerTouched = new List<string>();
        public List<string> Findings = new List<string>();
    }
}
