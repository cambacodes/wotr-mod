using System;
using System.Linq;
using Tirabade;

// E12 contacts (engine queue 7c): NativeContact.IsAvailable picks the one usable unit of a blueprint through Rules.SingleUsable.
// A dead original beside the route-saved living copy (Wenduag's spawn-copy presence) is no longer ambiguous.
internal static class ContactDisambiguationTests
{
    private sealed class Unit { public string Name = ""; public bool Usable, Dead, Destroyed; }

    internal static void Run(Action<bool, string> check)
    {
        string? Pick(params Unit[] units) => Rules.SingleUsable(units, u => u.Usable, u => u.Dead || u.Destroyed)?.Name;
        var copy = new Unit { Name = "copy", Usable = true };
        check(Pick(copy) == "copy", "A single usable unit is not the contact.");
        check(Pick(new Unit { Name = "original", Dead = true }, copy) == "copy", "A dead original beside the living copy is still ambiguous.");
        check(Pick(copy, new Unit { Name = "gone", Destroyed = true }) == "copy", "A destroyed twin beside the living copy is still ambiguous.");
        check(Pick(copy, new Unit { Name = "twin", Usable = true }) == null, "Two usable units are not ambiguous.");
        check(Pick(copy, new Unit { Name = "unloaded" }) == null, "A living but unusable twin (unloaded, suppressed) is ignored.");
        check(Pick(new Unit { Name = "original", Dead = true }) == null, "A dead unit alone is a contact.");
        check(Pick() == null, "No unit is a contact.");
    }
}
