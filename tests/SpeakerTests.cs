using System;
using System.Collections.Generic;
using Tirabade;

// E14f: Node.SpeakerUnit validation.
internal static class SpeakerTests
{
    internal static void Run(Action<bool, string> check)
    {
        Story Fixture(string? unit, string speaker)
        {
            var scene = ReturnToListTests.Fixture();
            scene.Nodes[0].SpeakerUnit = unit;
            scene.Nodes[0].Speaker = speaker;
            return ReturnToListTests.Wrap(scene);
        }
        Rules.Validate(Fixture("db064cafc234498ca83a702c472c1a7b", "Pharasma"));
        Rules.Validate(Fixture(null, "conversant"));
        foreach (var (unit, speaker, what) in new[] { ("nope", "Pharasma", "bad guid"), ("00000000000000000000000000000000", "Pharasma", "empty guid"),
            ("db064cafc234498ca83a702c472c1a7b", "conversant", "unit and conversant") })
        {
            bool rejected = false;
            try { Rules.Validate(Fixture(unit, speaker)); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid speaker accepted: " + what);
        }
    }
}
