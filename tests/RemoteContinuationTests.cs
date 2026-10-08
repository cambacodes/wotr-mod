using System;
using System.Linq;
using Tirabade;

internal static class RemoteContinuationTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == id);
        Snapshot Ready(Scene scene)
        {
            var state = new Snapshot
            {
                Chapter = scene.Chapters.FirstOrDefault(scene.MinChapter),
                Area = scene.Areas.FirstOrDefault() ?? "",
                Hour = 1000
            };
            foreach (var required in scene.Requires) HouseholdTests.Earn(story, state, required);
            if (scene.RequiresAny.Length > 0) state.Flags.Add(scene.RequiresAny[0]);
            foreach (var group in scene.RequiresAnyGroups) state.Flags.Add(group[0]);
            if (scene.Recovery != null) state.Flags.Add("revive." + scene.Recovery + ".available");
            if (scene.ContactUnit != null) state.AvailableContacts.Add(scene.ContactUnit);
            state.AvailableContacts.UnionWith(scene.AdditionalContactUnits);
            check(Program.CurrentAvailable(story, scene, state), "Remote regression fixture cannot enter " + scene.Id);
            check(Rules.ContactAvailable(story, scene, state), "Valid continuation rejected for " + scene.Id);
            return state;
        }

        var widow = Find("kiana.former_grief");
        var grief = Ready(widow);
        check(grief.Has("seelah.elan_dead") && Rules.ContactAvailable(story, widow, grief),
            "A required historical death incorrectly blocks a grief conversation.");
        var refuge = Find("jerribeth.refuge");
        var patronLost = Ready(refuge);
        patronLost.Flags.Add("jerribeth.patron_lost");   // a variant read since the Trickster COX edit, no longer a gate
        check(patronLost.Has("jerribeth.patron_lost") && Rules.ContactAvailable(story, refuge, patronLost),
            "A required patron loss incorrectly blocks the refuge conversation.");

        var dismissed = Find("konomi.private_absence");
        var privateLetter = Ready(dismissed);
        var officeRestored = Program.Copy(privateLetter);
        officeRestored.Flags.Add("konomi.present");
        check(!Rules.ContactAvailable(story, dismissed, officeRestored),
            "Private letter retains a now-false native dismissed-office premise.");
        officeRestored.Flags.Remove("konomi.present");
        check(Rules.ContactAvailable(story, dismissed, officeRestored), "Valid private letter cannot resume.");
        officeRestored.Flags.Remove("konomi.office_completed");
        check(!Rules.ContactAvailable(story, dismissed, officeRestored), "Lost native requirement permits continuation.");

        var invitation = Find("jerribeth.invitation");
        var invited = Ready(invitation);
        var unavailable = Program.Copy(invited);
        unavailable.Flags.Add("jerribeth.unavailable");
        check(!Rules.ContactAvailable(story, invitation, unavailable), "Remote relationship ignores native unavailability.");
        var authored = Program.Copy(invited);
        authored.Flags.Add("jerribeth.fate_note_prepared");
        check(!Program.CurrentAvailable(story, invitation, authored), "Authored forbid witness does not block new entry.");
        check(Rules.ContactAvailable(story, invitation, authored), "Authored mid-conversation forbid interrupts the page.");
        authored.Flags.Add("jerribeth.fate_note_read");
        check(Program.CurrentAvailable(story, invitation, authored), "Existing authored ForbidOverride was lost.");
        authored.Flags.Add(story.Relationships[invitation.Relationship].ClosedFlag);
        authored.Flags.Add(invitation.Id);
        check(Rules.ContactAvailable(story, invitation, authored), "Authored closure/completion interrupts its own continuation.");
        var question = Find("jerribeth.question");
        var delayed = Ready(question);
        delayed.Times[question.Requires[0]] = delayed.Hour;
        check(question.DelayHours > 0 && !Program.CurrentAvailable(story, question, delayed), "Delay witness does not block fresh entry.");
        check(Rules.ContactAvailable(story, question, delayed), "Continuation reapplies the scene delay.");

        // The legacy recovery graph is retained; its live retirement stays enforced.
        var recovery = Find("seelah.fate_life");
        check(recovery.Forbids.Contains("trickster.ever"), "Legacy Seelah recovery retirement was removed.");
        story = Program.Unfolded(story);
        recovery = Find("seelah.fate_life");
        recovery.Forbids = recovery.Forbids.Where(f => f != "trickster.ever").ToArray();
        var fallen = Ready(recovery);
        check(fallen.Has("seelah_dead") && Rules.ContactAvailable(story, recovery, fallen),
            "Historical target death prevents the actual recovery scene.");
        foreach (string blocker in story.Relationships[recovery.Relationship].UnavailableFlags.Where(f => f != "seelah_dead"))
        {
            check(Rules.ContactAvailable(story, recovery, fallen), "Recovery blocker has no positive witness.");
            var changed = Program.Copy(fallen);
            changed.Flags.Add(blocker);
            check(!Rules.ContactAvailable(story, recovery, changed), "Recovery bypasses unrelated unavailability: " + blocker);
        }
        foreach (string required in new[] { "trickster", "revive.seelah.available" })
        {
            check(Rules.ContactAvailable(story, recovery, fallen), "Recovery requirement has no positive witness.");
            var changed = Program.Copy(fallen);
            changed.Flags.Remove(required);
            check(!Rules.ContactAvailable(story, recovery, changed), "Recovery continues without " + required);
        }

        var ending = Find("ember.ending_dead");
        var remembrance = Ready(ending);
        check(remembrance.Has("ember_dead") && Rules.ContactAvailable(story, ending, remembrance),
            "Epilogue about death inherits living-contact exclusions.");
        var physical = Find("konomi.margin");
        var contact = Ready(physical);
        contact.AvailableContacts.Clear();
        check(!Rules.ContactAvailable(story, physical, contact), "Physical actor loss stopped being enforced.");
        contact.AvailableContacts.Add(physical.ContactUnit!);
        check(Rules.ContactAvailable(story, physical, contact), "Physical actor restoration stopped working.");

        if (story.Scenes.Any(s => s.Id == "vellexia.the_second_invitation")) RunVellexia(story, check);
    }

    // Requires the actual staged campaign; the ordinary export does not fabricate a substitute scene.
    internal static void RunVellexia(Story story, Action<bool, string> check)
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "vellexia." + id);
        string[] local = { "unfinished_likeness", "second_painter", "price_of_novelty", "two_observers",
            "unadvertised_hour", "a_question_kept", "the_unused_reply", "the_price_of_tomorrow" };
        var current = new Snapshot { Chapter = 4, Hour = 1000, Area = Find(local[0]).Areas.Single() };
        current.Flags.Add("vellexia.greeted");
        current.AvailableContacts.Add(Find(local[0]).ContactUnit!);
        foreach (string id in local)
        {
            var scene = Find(id);
            current.Hour += scene.DelayHours + 24;
            check(Program.CurrentAvailable(story, scene, current), "Actual Vellexia predecessor unavailable: " + id);
            current = Program.Walk(scene, current).First(s => s.Has(scene.Id) && !s.Has("vellexia.closed"));
        }
        // Native peaceful dismissal is an observed external game transition, not an authored effect.
        current.Flags.UnionWith(new[] { "vellexia.arena_invited", "vellexia.native_finished", "vellexia.dismissed_native" });
        current.Area = "7847c3e3537104f4694167af0b9fcd0e";
        current.AvailableContacts.Clear();
        var echo = Find("the_second_invitation");
        current.Hour += echo.DelayHours;
        check(Rules.IsRemote(echo) && echo.ContactUnit == null, "Witness is not the real remote echo scene.");
        check(Program.CurrentAvailable(story, echo, current), "Earned echo invitation is not available.");
        Snapshot? opened = null;
        Program.Walk(echo, current, (page, partial) => { if (page == "evidence" && opened == null) opened = Program.Copy(partial); });
        check(opened != null && !opened.Has(echo.Id), "No actual uncompleted echo page was reached.");
        foreach (string blocker in new[] { "vellexia.dead", "vellexia.early_fight", "vellexia.final_fight", "vellexia.mirrored", "vellexia.native_coercion", "inhuman" })
        {
            check(Rules.ContactAvailable(story, echo, opened!), "Native blocker lacks a valid open-page witness: " + blocker);
            var changed = Program.Copy(opened!);
            changed.Flags.Add(blocker);
            check(!Program.CurrentAvailable(story, echo, changed), "Native blocker does not invalidate fresh echo entry: " + blocker);
            check(!Rules.ContactAvailable(story, echo, changed), "Opened echo survives native blocker: " + blocker);
            changed.Flags.Remove(blocker);
            Program.CurrentAvailable(story, echo, changed);
            check(Rules.ContactAvailable(story, echo, changed) == !story.DepartureEpochs["vellexia"].Losses.Contains(blocker),
                "Removing a blocker invents a return from a recorded loss: " + blocker);
        }
        var departedArea = Program.Copy(opened!);
        departedArea.Area = "2570015799edf594daf2f076f2f975d8";
        check(!Rules.ContactAvailable(story, echo, departedArea), "Nexus echo page survives area change.");
        var laterChapter = Program.Copy(opened!);
        laterChapter.Chapter = 5;
        check(!Rules.ContactAvailable(story, echo, laterChapter), "Act-four echo page survives chapter change.");
    }
}
