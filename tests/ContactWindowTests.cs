using System;
using System.Linq;
using Tirabade;

internal static class ContactWindowTests
{
    internal static void Run(Action<bool, string> check)
    {
        var story = TricksterLatchTests.Fixture();
        const string unit = "280d4712dceb37f4a88e98f1f4c6e64f";
        const string area = "2570015799edf594daf2f076f2f975d8";
        var window = new ContactWindow { Flag = "irabeth.trickster.returned", MinAgeHours = 12, MaxAgeHours = 48,
            SupersededBy = new[] { "irabeth.closed" } };
        var presence = new Presence { Unit = unit, Area = area, ContactWindows = new[] { window } };
        story.Presences["irabeth.presence"] = presence;
        var scene = new Scene { Owner = "Irabeth", Relationship = "irabeth", ContactUnit = unit };
        var state = new Snapshot { Area = area, Chapter = 5, Hour = 100 };
        state.AvailableContacts.Add(unit);
        void Both(bool expected, string reason) => check(Rules.PresenceWanted(presence, state) == expected
            && Rules.ContactAvailable(story, scene, state) == expected, "Contact window: " + reason);
        Both(true, "optional event not produced");
        state.Flags.Add(window.Flag);
        Both(false, "missing timestamp");
        foreach (var (at, expected) in new[] { (-1, false), (101, false), (100, false), (89, false), (88, true), (52, true), (51, false) })
        {
            state.Times[window.Flag] = at;
            Both(expected, "timestamp " + at);
        }
        state.Times[window.Flag] = 80;
        state.Flags.Add("irabeth.closed");
        Both(false, "superseded witness");
        state.Flags.Remove("irabeth.closed");
        // Additional actors use the same policy even when the scene has a different primary contact.
        scene.ContactUnit = "0123456789abcdef0123456789abcdef";
        scene.AdditionalContactUnits = new[] { unit };
        state.AvailableContacts.Add(scene.ContactUnit);
        state.Times[window.Flag] = 51;
        check(!Rules.ContactAvailable(story, scene, state), "Additional stale contact escaped its presence window");
        Rules.Validate(story);
        foreach (var invalid in new[] {
            new ContactWindow { Flag = "unknown" }, new ContactWindow { Flag = window.Flag, MinAgeHours = -1 },
            new ContactWindow { Flag = window.Flag, MinAgeHours = 12, MaxAgeHours = 11 },
            new ContactWindow { Flag = window.Flag, SupersededBy = new[] { "unknown" } },
            new ContactWindow { Flag = window.Flag, SupersededBy = new[] { window.Flag } },
            new ContactWindow { Flag = window.Flag, SupersededBy = new[] { "irabeth.closed", "irabeth.closed" } } })
        {
            presence.ContactWindows = new[] { invalid };
            bool refused = false;
            try { Rules.Validate(story); } catch (InvalidOperationException) { refused = true; }
            check(refused, "Invalid contact window accepted");
        }
        presence.ContactWindows = new[] { window, window };
        bool duplicates = false;
        try { Rules.Validate(story); } catch (InvalidOperationException) { duplicates = true; }
        check(duplicates, "Duplicate producing flags accepted");
    }
}
