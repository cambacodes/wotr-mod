using System;
using System.Collections.Generic;
using System.Text.Json;
using Tirabade;

internal static class PrerequisiteGroupsTests
{
    internal static void Run(Action<bool, string> check)
    {
        // Alternative provenance must preserve the original two native requirements.
        var scene = new Scene
        {
            Id = "group_witness", Remote = true, Requires = new[] { "invited" },
            RequiresAny = new[] { "friend", "lover" },
            RequiresAnyGroups = new[] { new[] { "dismissed", "earned" }, new[] { "office_done", "earned" } },
            Nodes = new List<Node> { new Node { Id = "start", Text = "An agreed meeting.", Choices = new List<Choice> { new Choice() } } }
        };
        var story = new Story { Scenes = new List<Scene> { scene } };
        Rules.Validate(story);
        for (int mask = 0; mask < 32; mask++)
        {
            var state = new Snapshot { Chapter = 3, Hour = 100 };
            string[] flags = { "dismissed", "office_done", "earned", "invited", "friend" };
            for (int bit = 0; bit < flags.Length; bit++)
                if ((mask & (1 << bit)) != 0) state.Flags.Add(flags[bit]);
            bool expected = ((mask & 3) == 3 || (mask & 4) != 0) && (mask & 24) == 24;
            check(Rules.Available(story, scene, state) == expected, "Grouped entry changed native conjunction at " + mask);
            check(Rules.ContactAvailable(story, scene, state) == expected, "Grouped continuation changed native conjunction at " + mask);
        }
        var ready = new Snapshot { Chapter = 3, Hour = 100 };
        ready.Flags.UnionWith(new[] { "invited", "lover", "earned" });
        ready.Times["earned"] = 90;
        ready.Times["dismissed"] = 99; // A timestamp without its flag cannot delay a different history.
        scene.DelayHours = 24;
        check(!Rules.Available(story, scene, ready), "Newly earned alternative skips the waiting period.");
        check(Rules.ContactAvailable(story, scene, ready), "Continuation incorrectly reapplies entry delay.");
        ready.Hour = 113;
        check(!Rules.Available(story, scene, ready), "Alternative delay opens an hour early.");
        ready.Hour = 114;
        check(Rules.Available(story, scene, ready), "Alternative delay does not open at its boundary.");
        ready.Flags.Remove("earned");
        check(!Rules.ContactAvailable(story, scene, ready), "Lost live alternative still permits continuation.");
        ready.Flags.UnionWith(new[] { "dismissed", "office_done" });
        ready.Hour = 123;
        check(Rules.Available(story, scene, ready), "Legacy provenance no longer works without a migration.");
        ready.Flags.Add("closed");
        check(!Rules.Available(story, scene, ready), "Alternative provenance bypasses relationship closure.");
        check(Rules.ContactAvailable(story, scene, ready), "Authored closure interrupts its own final page.");

        var options = new JsonSerializerOptions { IncludeFields = true };
        var copy = JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(story, options), options)!;
        check(copy.Scenes[0].RequiresAnyGroups[1][0] == "office_done", "Group JSON round trip lost prerequisites.");
        foreach (string[][] invalid in new[] { null!, new string[][] { null! }, new[] { Array.Empty<string>() },
            new[] { new[] { " " } }, new[] { new[] { "earned", "earned" } } })
        {
            scene.RequiresAnyGroups = invalid;
            bool rejected = false;
            try { Rules.Validate(story); }
            catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Malformed prerequisite group accepted.");
        }
        scene.RequiresAnyGroups = Array.Empty<string[]>();
        Rules.Validate(story);
        ready.Flags.Remove("closed");
        ready.Flags.Remove("dismissed");
        ready.Flags.Remove("office_done");
        check(Rules.Available(story, scene, ready), "An omitted group changes existing scene behavior.");
    }
}
