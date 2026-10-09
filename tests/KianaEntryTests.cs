using System;
using System.Linq;
using Tirabade;

internal static class KianaEntryTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var invitation = story.Scenes.Single(s => s.Id == "kiana.invitation");
        var rehearsal = story.Scenes.Single(s => s.Id == "kiana.rehearsal");
        var initial = new Snapshot { Chapter = 5, Area = invitation.Areas.Single(), Hour = 1000 };
        initial.Flags.UnionWith(invitation.Requires);
        initial.AvailableContacts.Add("180b0eaa5dce387458d2ebf0ee943985");
        // Main.Update opens the relationship journal before the player answers the invitation.
        initial.Flags.Add(story.Relationships["kiana"].StartedFlag);
        foreach (var result in Program.Walk(invitation, initial))
        {
            result.Hour += rehearsal.DelayHours;
            bool replied = result.Has(invitation.Id);
            check(Rules.Available(story, rehearsal, result) == replied,
                "Kiana rehearsal must wait for an answered invitation, not merely an opened journal.");
            if (replied)
                check(Program.Walk(rehearsal, result).Any(s => s.Has("kiana.company")), "Kiana completed invitation cannot reach rehearsal.");
            else
                check(Rules.Available(story, invitation, result), "Kiana cannot return to deferred invitation.");
        }
    }
}
