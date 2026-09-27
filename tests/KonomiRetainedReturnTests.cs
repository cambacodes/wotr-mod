using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KonomiRetainedReturnTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string unit = "ca2d58c5c65723945857e04fb85d30ce";
        const string capital = "2570015799edf594daf2f076f2f975d8";
        const string dead = "konomi.retained_dead";
        const string contact = "konomi.return_contact_available";
        Scene Get(string id) => story.Scenes.Single(scene => scene.Id == "konomi." + id);
        var inquiry = Get("retained_inquiry");
        var attempt = Get("retained_attempt");
        var first = Get("return_first_words");
        var second = Get("return_second_visit");
        var scenes = new[] { inquiry, attempt, first, second };
        var reached = new HashSet<string>();
        var preserved = new[] { "konomi.present", "konomi.dismissed", "konomi.office_completed", "konomi.closed",
            "konomi.farewell", "konomi.private_parted", "konomi.returned", "konomi.margin", "konomi.lovers", "konomi.committed",
            "konomi.missed_private_access", "konomi.private_meeting", "arueshalae.committed", "seelah.committed" };
        var action = attempt.Nodes.SelectMany(node => node.Choices).Single(choice => choice.Revive != null);
        check(action.Revive == "konomi" && action.Set.SequenceEqual(new[] { "konomi.retained_return_confirmed" }),
            "Retained revival must award only the verified return marker.");
        check(scenes.SelectMany(scene => scene.Nodes).SelectMany(node => node.Choices)
            .All(choice => !choice.Set.Intersect(preserved).Any()), "Recovery writes native office or relationship history.");
        check(inquiry.Recovery == "konomi" && attempt.Recovery == "konomi", "Preparation or attempt lost retained-corpse gating.");
        check(first.AfterRecovery == "konomi" && second.AfterRecovery == "konomi"
            && first.ContactUnit == unit && second.ContactUnit == unit, "Aftercare lost its explicit live-actor contract.");
        check(inquiry.Nodes.SelectMany(node => node.Choices).Count(choice => choice.Check != null) == 1,
            "The earned fate investigation lost its skill-check alternative.");

        // Existing personal/native histories are input fixtures. This is not a replay of their original acquisition.
        foreach (int chapter in new[] { 3, 5 })
        foreach (string history in new[] { "new", "known", "private", "address", "lover" })
        foreach (string ending in new[] { "open", "closed", "farewell", "parted" })
        foreach (string office in new[] { "active", "dismissed", "unappointed" })
        {
            var initial = new Snapshot { Chapter = chapter, Hour = 1000, Area = capital };
            initial.Flags.UnionWith(new[] { "trickster", dead, "revive.konomi.available", "arueshalae.committed", "seelah.committed" });
            if (history == "known") initial.Flags.Add("konomi.margin");
            if (history == "private") initial.Flags.Add("konomi.private_meeting");
            if (history == "address") initial.Flags.Add("konomi.missed_private_access");
            if (history == "lover") initial.Flags.UnionWith(new[] { "konomi.lovers", "konomi.committed" });
            if (ending == "closed") initial.Flags.Add("konomi.closed");
            if (ending == "farewell") initial.Flags.Add("konomi.farewell");
            if (ending == "parted") initial.Flags.Add("konomi.private_parted");
            if (office == "active") initial.Flags.Add("konomi.present");
            if (office == "dismissed") initial.Flags.UnionWith(new[] { "konomi.dismissed", "konomi.office_completed" });
            check(Rules.Available(story, inquiry, initial), "Valid retained-death history cannot begin inquiry.");
            check(!Rules.Available(story, attempt, initial), "Native action bypasses the earned investigation.");
            foreach (string needed in new[] { "trickster", dead, "revive.konomi.available" })
            {
                var absent = Program.Copy(initial); absent.Flags.Remove(needed);
                check(!Rules.Available(story, inquiry, absent), "Recovery entry bypasses " + needed);
            }
            var investigation = Program.Walk(inquiry, initial, (page, _) => reached.Add(inquiry.Id + "/" + page));
            check(investigation.Any(state => state.Has("konomi.return_distinction"))
                && investigation.Any(state => state.Has("konomi.return_patient_reading")), "Investigation loses a roll outcome.");
            foreach (var prepared in investigation.Where(state => state.Has("konomi.return_path_prepared")))
            {
                check(!prepared.Has("konomi.retained_return_confirmed"), "Investigation fabricates resurrection success.");
                check(Rules.Available(story, attempt, prepared), "Prepared investigation cannot reach attempt.");
                var pages = new HashSet<string>();
                Program.Walk(attempt, prepared, (page, _) => { reached.Add(attempt.Id + "/" + page); pages.Add(page); });
                check(pages.Contains("attempt"), "Explicit native dispatch choice is unreachable.");
                check(!Rules.Available(story, first, prepared), "Pending attempt opens living aftermath.");
                // Explicit service-result fixture: the pure walker does not execute or certify resurrection.
                var verified = Program.Copy(prepared);
                verified.Flags.Remove(dead); verified.Flags.Remove("revive.konomi.available");
                verified.Flags.UnionWith(new[] { "konomi.retained_return_confirmed", contact });
                verified.AvailableContacts.Add(unit);
                verified.Flags.Remove("trickster"); verified.Flags.Add("legend");
                check(Rules.Available(story, first, verified), "Verified return cannot receive aftercare after an earned Legend transition.");
                foreach (string needed in new[] { "konomi.retained_return_confirmed", contact })
                {
                    var absent = Program.Copy(verified); absent.Flags.Remove(needed);
                    check(!Rules.Available(story, first, absent) && !Rules.ContactAvailable(story, first, absent),
                        "Aftercare invents current positive evidence: " + needed);
                }
                var lostView = Program.Copy(verified); lostView.AvailableContacts.Clear();
                check(!Rules.Available(story, first, lostView) && !Rules.ContactAvailable(story, first, lostView),
                    "Unavailable actor can begin or continue physical aftercare.");
                var lostLife = Program.Copy(verified); lostLife.Flags.Add(dead);
                check(!Rules.Available(story, first, lostLife) && !Rules.ContactAvailable(story, first, lostLife),
                    "New death still offers living aftercare.");
                var firstPages = new HashSet<string>();
                var after = Program.Walk(first, verified, (page, _) => { reached.Add(first.Id + "/" + page); firstPages.Add(page); });
                string expected = ending != "open" ? "boundary" : history == "lover" ? "love"
                    : history == "address" || history == "private" ? "private" : history == "known" ? "acquainted" : "introduction";
                check(firstPages.Contains(expected), "Aftercare loses actual personal history: " + expected);
                check(new[] { "boundary", "love", "private", "acquainted", "introduction" }
                    .Where(page => page != expected).All(page => !firstPages.Contains(page)), "Aftercare invents incompatible personal history.");
                foreach (var state in after.Where(state => state.Has("konomi.return_followup_invited")))
                {
                    check(!Rules.Available(story, second, state), "Follow-up bypasses the invited recovery interval.");
                    state.Hour += 48;
                    check(Rules.Available(story, second, state), "Invited follow-up cannot open after its interval.");
                    var secondPages = new HashSet<string>();
                    var finishes = Program.Walk(second, state, (page, _) => { reached.Add(second.Id + "/" + page); secondPages.Add(page); });
                    string officePage = office == "active" ? "office" : office == "dismissed" ? "dismissed" : "unappointed";
                    check(secondPages.Contains(officePage), "Return misstates the current native office history.");
                    check(new[] { "office", "dismissed", "unappointed" }.Where(page => page != officePage)
                        .All(page => !secondPages.Contains(page)), "Return fabricates an appointment or dismissal.");
                    if (ending != "open")
                        check(secondPages.Contains("closed") && !secondPages.Overlaps(new[] { "familiar", "address", "begin" }),
                            "Aftercare reopens a previously closed or parted relationship.");
                    foreach (var finish in finishes)
                    {
                        foreach (string flag in preserved)
                            check(finish.Has(flag) == initial.Has(flag), "Recovery changes preserved history: " + flag);
                        if (ending != "open") check(!finish.Has("konomi.return_hand_kissed")
                            && !finish.Has("konomi.return_invitation_welcome"), "Closed-history aftercare awards renewed intimacy.");
                    }
                }
            }
        }
        foreach (var scene in scenes)
            foreach (var node in scene.Nodes)
                check(reached.Contains(scene.Id + "/" + node.Id), "Retained-return page was not reached through predecessors: " + scene.Id + "/" + node.Id);
    }
}
