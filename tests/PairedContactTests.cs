using System;
using System.Collections.Generic;
using System.Text.Json;
using Tirabade;

internal static class PairedContactTests
{
    internal static void Run(Action<bool, string> check)
    {
        const string anevia = "b5e867e13503c6f41bb1316705efb4a2";
        const string irabeth = "280d4712dceb37f4a88e98f1f4c6e64f";
        var scene = new Scene {
            Id = "paired_meeting", Owner = "Together", ContactUnit = anevia,
            AdditionalContactUnits = new[] { irabeth }, Chapters = new[] { 3, 5 },
            Areas = new[] { "2570015799edf594daf2f076f2f975d8" },
            Nodes = new List<Node> { new Node { Id = "start", Text = "A shared meeting.",
                Choices = new List<Choice> { new Choice { Set = new[] { "closed" } } } } }
        };
        var story = new Story { Scenes = new List<Scene> { scene } };
        Rules.Validate(story);
        var state = new Snapshot { Chapter = 3, Area = scene.Areas[0] };
        state.AvailableContacts.Add(anevia);
        check(!Rules.Available(story, scene, state) && !Rules.ContactAvailable(story, scene, state),
            "A joint meeting starts or continues with only its primary actor present.");
        state.AvailableContacts.Add(irabeth);
        check(Rules.Available(story, scene, state) && Rules.ContactAvailable(story, scene, state),
            "Both available actors cannot meet.");
        foreach (var actor in new[] { anevia, irabeth })
        {
            state.AvailableContacts.Remove(actor);
            check(!Rules.Available(story, scene, state) && !Rules.ContactAvailable(story, scene, state),
                "Joint entry or continuation ignores missing actor " + actor);
            state.AvailableContacts.Add(actor);
            check(Rules.ContactAvailable(story, scene, state), "Returning actor cannot restore contact.");
        }
        state.Flags.Add("closed");
        check(!Rules.Available(story, scene, state) && Rules.ContactAvailable(story, scene, state),
            "An authored closing answer either reopens entry or prevents its closing page.");
        state.AvailableContacts.Remove(irabeth);
        check(!Rules.ContactAvailable(story, scene, state), "Closing prose bypasses second actor loss.");
        state.AvailableContacts.Add(irabeth);
        state.Flags.Add("irabeth_dead");
        check(!Rules.ContactAvailable(story, scene, state), "Actor list bypasses native unavailability.");
        state.Flags.Remove("irabeth_dead");
        state.Chapter = 4;
        check(!Rules.ContactAvailable(story, scene, state), "Joint conversation ignores changed chapter.");
        state.Chapter = 3;
        state.Area = "";
        check(!Rules.ContactAvailable(story, scene, state), "Joint conversation ignores changed area.");

        var options = new JsonSerializerOptions { IncludeFields = true };
        var restored = JsonSerializer.Deserialize<Scene>(JsonSerializer.Serialize(scene, options), options)!;
        check(restored.ContactUnit == anevia && restored.AdditionalContactUnits.Length == 1
            && restored.AdditionalContactUnits[0] == irabeth, "Contact requirements lost in JSON.");
        var legacy = JsonSerializer.Deserialize<Scene>("{\"ContactUnit\":\"" + anevia + "\"}", options)!;
        check(legacy.AdditionalContactUnits.Length == 0, "Legacy single-contact scene acquired additional requirements.");

        void Invalid(string? primary, params string[] others)
        {
            scene.ContactUnit = primary;
            scene.AdditionalContactUnits = others;
            bool rejected = false;
            try { Rules.Validate(story); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid paired contact declaration accepted.");
        }
        Invalid(null, irabeth);
        Invalid(anevia, "not-a-unit");
        Invalid(anevia, irabeth, irabeth);
        Invalid(anevia, anevia.ToUpperInvariant());
        Invalid(anevia, null!);
    }
}
