using System;
using System.Diagnostics;
using System.IO;
using System.Text;
using Newtonsoft.Json;
using Tirabade;

internal static class ValidationOnlyRunner
{
    internal static int Run(string storyPath)
    {
        var timer = Stopwatch.StartNew();
        try
        {
            var story = JsonConvert.DeserializeObject<Story>(File.ReadAllText(storyPath, Encoding.UTF8))!;
            var errors = Rules.ValidateAll(story);
            string? report = Environment.GetEnvironmentVariable("RRT_VALIDATE_REPORT");
            if (!string.IsNullOrEmpty(report))
                File.WriteAllText(report, JsonConvert.SerializeObject(new { version = 1, complete = true, errors }), new UTF8Encoding(false));
            foreach (var error in errors) Console.Error.WriteLine(error.detail);
            if (errors.Count > 0) return 1;
            Console.WriteLine("RRT-VALIDATE-OK");
            return 0;
        }
        catch (JsonException ex)
        {
            string? report = Environment.GetEnvironmentVariable("RRT_VALIDATE_REPORT");
            if (!string.IsNullOrEmpty(report))
                File.WriteAllText(report, JsonConvert.SerializeObject(new {
                    version = 1, complete = false,
                    errors = new[] { new ValidationError { code = "invalid_story_json", scene = "", detail = ex.Message } }
                }), new UTF8Encoding(false));
            Console.Error.WriteLine(ex);
            return 1;
        }
        finally
        {
            string? output = Environment.GetEnvironmentVariable("RRT_MANAGED_TIMINGS");
            if (!string.IsNullOrEmpty(output))
                File.WriteAllText(output, JsonConvert.SerializeObject(new[] {
                    new { suite = "ManagedConstructionAndNativeInline", seconds = timer.Elapsed.TotalSeconds, assertions = 0 }
                }), new UTF8Encoding(false));
        }
    }
}
