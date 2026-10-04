using System;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class NativeGateContractParityTests
{
    private static Story Copy(Story story) => JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(story,
        new JsonSerializerOptions { IncludeFields = true }), new JsonSerializerOptions { IncludeFields = true })!;
    internal static void Run(Story shipped, Action<bool, string> check)
    {
        const string id = "kiana.q3_recovery";
        var story = Copy(shipped);
        var spec = story.NativeGates[id];
        check(spec.When.Length == 2 && spec.When.All(g => Rules.Q3RecoveryFullOutcomes.Any(g.Contains)),
            "Route merge unexpectedly reintroduced the audited partial group; review the route producer.");
        var groups = Rules.Q3RecoveryFullOutcomes.Select(f => new[] { "trickster.now", f })
            .Concat(new[] { Rules.Q3RecoveryPartialRequirements }).ToArray();
        foreach (var group in groups)
        {
            spec.When = new[] { group };
            Rules.Validate(story); // Same validator called by Main.Load.
            var state = new Snapshot(); state.Flags.UnionWith(group);
            var expected = Rules.Q3RecoveryFullOutcomes.Any(group.Contains) ? Q3RecoveryOutcome.Full : Q3RecoveryOutcome.Partial;
            check(Rules.Q3RecoverySelection(story, state) == expected, "Supported Q3 group chose the wrong adapter outcome.");
            check(Rules.Q3RecoverySkipsPatients(expected) == (expected == Q3RecoveryOutcome.Full),
                "Partial Kiana release suppressed the other patients' native road home.");
            foreach (var omitted in group)
            {
                var missing = new Snapshot(); missing.Flags.UnionWith(group.Where(f => f != omitted));
                check(Rules.Q3RecoverySelection(story, missing) == Q3RecoveryOutcome.Native, "Unearned Q3 outcome accepted: missing " + omitted);
            }
            state.Flags.Add(Rules.DegradedPrefix + "kiana");
            check(Rules.Q3RecoverySelection(story, state) == Q3RecoveryOutcome.Native, "Degraded adapter suppresses canon.");
        }
        spec.When = groups;
        var both = new Snapshot(); both.Flags.UnionWith(groups.SelectMany(g => g));
        check(Rules.Q3RecoverySelection(story, both) == Q3RecoveryOutcome.Full, "Later buy-back did not supersede partial release.");
        foreach (var unsupported in new[] {
            new[] { "trickster.ever", "kiana.trickster.guests_ransomed" },
            new[] { "trickster.now", "kiana.trickster.returned" },
            new[] { "trickster.now", "kiana.trickster.cost.guests_robbed" },
            new[] { "kiana.trickster.returned", "kiana.trickster.cost.guests_robbed" },
            new[] { "trickster.now", "kiana.trickster.unreviewed" } })
        {
            spec.When = new[] { unsupported };
            bool refused = false;
            try { Rules.Validate(story); } catch (InvalidOperationException) { refused = true; }
            check(refused, "Unsupported Q3 group passed Main.Load/offline validation.");
        }
        // Integration-only full declarations remain accepted, with no partial producer or extra gate required.
        spec.When = groups.Take(2).ToArray(); Rules.Validate(story);
        foreach (var group in spec.When)
        {
            var state = new Snapshot(); state.Flags.UnionWith(group);
            check(Rules.Q3RecoverySelection(story, state) == Q3RecoveryOutcome.Full, "Integration ransom/buy-back regressed.");
        }
        foreach (var path in new[] { "angel", "aeon", "azata", "demon", "devil", "dragon", "legend", "lich", "swarm", "trickster.failed" })
        {
            var state = new Snapshot(); state.Flags.UnionWith(new[] { "trickster.ever", path, "kiana.trickster.guests_ransomed" });
            if (path is "dragon" or "legend" or "swarm" or "trickster.failed") state.Flags.Add("trickster");
            Rules.Complete(story, state);
            check(Rules.Q3RecoverySelection(story, state) == Q3RecoveryOutcome.Native, "Q3 changes canon after conversion/failure: " + path);
        }
        Console.WriteLine("PASS: E-Q7-14 supported full/partial groups, unsupported mutations, and integration-only paid recovery.");
    }
}
