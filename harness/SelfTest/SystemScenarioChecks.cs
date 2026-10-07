using System;
using RRT.TestHarness;

internal static class SystemScenarioChecks
{
    internal static void Run(Action<bool, string> check)
    {
        var cases = SystemCases.Parse(@"{""Schema"":1,""Cases"":[{""Id"":""pair"",""System"":""table"",""Chapter"":3,""Steps"":[{""Scene"":""a"",""Available"":false}]}]}");
        check(cases.Cases.Count == 1, "scenario parsed");
        foreach (var json in new[] { @"{""Schema"":1,""Cases"":[]}", @"{""Schema"":2,""Cases"":[]}",
            @"{""Schema"":1,""Cases"":[{""Id"":""bad"",""System"":""table"",""Chapter"":3,""Steps"":[{""Scene"":""a"",""Answers"":[""b/start/0""]}]}]}" })
        {
            bool rejected = false;
            try { SystemCases.Parse(json); } catch (FormatException) { rejected = true; }
            check(rejected, "invalid scenario rejected");
        }
        var report = new HarnessReport { Status = "complete", Plan = new HarnessPlan { SystemCasesJson = "fixture" },
            Init = new InitState { RrtModFound = true, Initialized = true } };
        report.Saves.Add(new SaveReport { Save = "fixture", LoadOk = true });
        report.ComputeSummary(); check(!report.Summary.Passed, "empty coverage cannot pass");
        report.Saves[0].Systems.Add(new SystemCoverage { Scenario = "missing", Result = "missing-scene" });
        report.ComputeSummary(); check(!report.Summary.Passed, "missing integration cannot pass");
    }
}
