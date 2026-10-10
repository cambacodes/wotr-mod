using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Tirabade;

internal static class ValidationReportTests
{
#if C2_STANDALONE
    private static int Main(string[] args)
    {
        try
        {
            if (Environment.GetEnvironmentVariable("RRT_VALIDATE_ONLY") == "1") return ValidationOnlyRunner.Run(args[1]);
            Run((condition, message) => { if (!condition) throw new InvalidOperationException(message); }, args[0]);
            Console.WriteLine("C2-VALIDATION-TESTS-OK");
            return 0;
        }
        catch (Exception ex) { Console.Error.WriteLine(ex); return 1; }
    }
#endif
    private static Story Fixture()
    {
        var story = new Story();
        story.Relationships["her"] = new Relationship {
            Title = "fixture", StartedFlag = "her.started", ClosedFlag = "her.closed", CommittedFlag = "her.committed"
        };
        foreach (string id in new[] { "first", "second" })
            story.Scenes.Add(new Scene { Id = id, Relationship = "her", Remote = true,
                Nodes = new List<Tirabade.Node> { new Tirabade.Node { Id = "end", Text = "fixture",
                    Choices = new List<Choice> { new Choice { Id = "finish", Set = new[] { "her.done" } } } } } });
        return story;
    }

    internal static void Run(Action<bool, string> check, string game)
    {
        var valid = Fixture();
        check(Rules.ValidateAll(valid).Count == 0, "Valid control rejected");
        Rules.Validate(valid);
        var invalid = Fixture();
        invalid.Scenes[0].Kind = "invalid";
        invalid.Scenes[1].Nodes[0].Choices[0].Next = "absent";
        invalid.Scenes[1].Nodes[0].Choices.Add(new Choice { Id = "finish", Mythic = "invalid" });
        invalid.CompletedQuests["bad.quest"] = "invalid";
        invalid.Derived["bad.derived"] = new[] { new[] { "unknown" } };
        invalid.Counts["bad.count"] = new CountSpec { Min = 0, Of = new[] { "her.done" } };
        var errors = Rules.ValidateAll(invalid);
        var expectedErrors = new[] {
            ("invalid_scene_kind", "first"), ("invalid_completed_quest_binding", ""),
            ("derived_key_reads_an_unknown_flag", ""), ("invalid_count_composite", ""),
            ("invalid_answer_identity", "second"), ("missing_node", "second"), ("invalid_mythic_requirement", "second")
        };
        check(errors.Select(e => (e.code, e.scene)).SequenceEqual(expectedErrors) && errors.All(e => e.detail.Length > 0),
            "Incomplete/incorrect engine violations");
        string? first = null;
        try { Rules.Validate(invalid); } catch (InvalidOperationException ex) { first = ex.Message; }
        check(first == errors[0].detail, "Runtime did not throw first diagnostic");
        check(errors.Select(e => (e.code, e.scene, e.detail)).SequenceEqual(
            Rules.ValidateAll(invalid).Select(e => (e.code, e.scene, e.detail))), "Unstable report order");
        check(invalid.Scenes.Select(s => s.Id).SequenceEqual(new[] { "first", "second" })
            && invalid.Scenes[1].Nodes[0].Id == "end"
            && invalid.Scenes[1].Nodes[0].Choices.Select(c => c.Id).SequenceEqual(new[] { "finish", "finish" })
            && invalid.Scenes[1].Nodes[0].Choices[0].Next == "absent"
            && invalid.Scenes[0].Nodes[0].Choices[0].Set.SequenceEqual(new[] { "her.done" }), "Validation changed authored identities/state");

        foreach (var mutation in new Action<Story>[] {
            s => s.Scenes[0].Nodes.Clear(),
            s => s.Scenes[0].Nodes.Add(s.Scenes[0].Nodes[0]),
            s => s.Scenes[0].Relationship = "missing",
            s => { s.Scenes[0].Relationship = "missing"; s.Scenes[0].Reaction = true; s.Scenes[0].TricksterDevice = true; },
            s => s.Scenes[0].Nodes[0].Paragraphs = null!,
            s => s.Scenes[0].Nodes[0].Choices.Add(null!),
            s => s.Books = null!,
            s => { s.Derived["cycle.a"] = new[] { new[] { "cycle.b" } }; s.Derived["cycle.b"] = new[] { new[] { "cycle.a" } }; },
            s => s.Derived["null.groups"] = null!,
            s => s.Presences["missing.presence"] = new Presence { Unit = "bad" },
            s => s.NativeGates["unknown"] = new NativeGateSpec(),
            s => s.NativeTextEdits["unknown"] = new NativeTextEdit(),
            s => s.NativeWorldReconciliations["unknown"] = new NativeWorldSpec(),
            s => s.NativeAnswerEdits["unknown"] = new NativeAnswerEditSpec(),
            s => s.NativeObjectiveSettlements["unknown"] = new NativeGateSpec(),
            s => s.NativeEpilogueEdits["unknown"] = new NativeEpilogueEditSpec(),
            s => s.NativeEpilogueSuppressions["unknown"] = new NativeEpilogueSuppressionSpec(),
            s => s.PresenceFailureReceipts["unknown.presence"] = new PresenceFailureReceipt(),
            s => s.Books["bad"] = new BookSpec(),
            s => s.Glossary["bad"] = new GlossaryText(),
            s => s.ParentEpilogueEdits["bad"] = new ParentEndingEdit(),
            s => { s.Scenes[0].Remote = false; s.Scenes[0].Owner = "unknown"; },
            s => s.Scenes[0].InteractionHub = "unknown"
        })
        {
            var sibling = Fixture();
            mutation(sibling);
            sibling.Scenes[1].DelayHours = -1;
            var found = Rules.ValidateAll(sibling);
            check(found.Count >= 2 && found.Any(e => e.code == "invalid_chapter_or_timing_constraints" && e.scene == "second"),
                "Sibling violation stopped validation");
        }
        var nullStory = Rules.ValidateAll(null!);
        check(nullStory.Count == 1 && nullStory[0].code == "null_story", "Null story not diagnosed");
        ProcessReport(check, game, valid, 0, Array.Empty<(string, string)>(), true);
        ProcessReport(check, game, invalid, 1, expectedErrors, true);
        ProcessReport(check, game, invalid, 1, Array.Empty<(string, string)>(), false);
        ProcessReport(check, game, null!, 1, new[] { ("null_story", "") }, true);
        ProcessReport(check, game, valid, 1, new[] { ("invalid_story_json", "") }, true, false, "{");
    }

    private static void ProcessReport(Action<bool, string> check, string game, Story story, int exit,
        (string, string)[] expected, bool requestReport, bool complete = true, string? raw = null)
    {
        string scratch = Path.Combine(Path.GetTempPath(), "rrt-c2-" + Guid.NewGuid().ToString("N"));
        Directory.CreateDirectory(scratch);
        try
        {
            string input = Path.Combine(scratch, "story.json"), report = Path.Combine(scratch, "report.json"), timings = Path.Combine(scratch, "timings.json");
            File.WriteAllText(input, raw ?? JsonConvert.SerializeObject(story), new UTF8Encoding(false));
            // Seed stale content to prove both success and failure replace the report.
            File.WriteAllText(report, "stale", new UTF8Encoding(false));
            var start = new ProcessStartInfo("mono", "\"" + Assembly.GetExecutingAssembly().Location + "\" \"" + game + "\" \"" + input + "\"") {
                UseShellExecute = false, RedirectStandardOutput = true, RedirectStandardError = true
            };
            start.EnvironmentVariables.Remove("RRT_TEST_VALIDATION_REPORT");
            start.EnvironmentVariables.Remove("RRT_TEST_LOAD");
            start.EnvironmentVariables["RRT_VALIDATE_ONLY"] = "1";
            start.EnvironmentVariables["RRT_MANAGED_TIMINGS"] = timings;
            if (requestReport) start.EnvironmentVariables["RRT_VALIDATE_REPORT"] = report;
            else start.EnvironmentVariables.Remove("RRT_VALIDATE_REPORT");
            using (var process = Process.Start(start)!)
            {
                string stdout = process.StandardOutput.ReadToEnd(), stderr = process.StandardError.ReadToEnd();
                process.WaitForExit();
                check(process.ExitCode == exit, "Wrong validation exit: " + stdout + stderr);
            }
            var timingData = JArray.Parse(File.ReadAllText(timings, Encoding.UTF8));
            check(timingData.Count > 0 && timingData.All(t => (double)t["seconds"]! >= 0 && (int)t["assertions"]! >= 0), "Missing timings");
            if (!requestReport) { check(File.ReadAllText(report, Encoding.UTF8) == "stale", "Unrequested report written"); return; }
            var data = JObject.Parse(File.ReadAllText(report, Encoding.UTF8));
            check((int)data["version"]! == 1 && (bool)data["complete"]! == complete, "Wrong report envelope");
            var findings = (JArray)data["errors"]!;
            check(findings.Count == expected.Length, "Incomplete process report");
            check(findings.Select(e => ((string)e["code"]!, (string)e["scene"]!)).SequenceEqual(expected), "Wrong report identities/order");
            check(findings.All(e => ((JObject)e).Properties().Select(p => p.Name).OrderBy(n => n)
                .SequenceEqual(new[] { "code", "detail", "scene" }) && ((string)e["detail"]!).Length > 0), "Wrong violation shape");
        }
        finally { Directory.Delete(scratch, true); }
    }
}
