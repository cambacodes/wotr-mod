using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class IrabethDepartureCampaignTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var scenes = story.Scenes.Where(s => s.AfterDeparture == "irabeth").ToArray();
        Scene Find(string id) => scenes.Single(s => s.Id == "irabeth." + id);
        var request = Find("return_request");
        var reply = Find("return_reply");
        var meeting = Find("return_first_words");
        var reached = new HashSet<string>();
        List<Snapshot> Walk(Scene scene, Snapshot state) => Program.Walk(scene, state,
            (id, _) => reached.Add(scene.Id + "/" + id));
        var initial = new Snapshot { Chapter = 5, Hour = 1000, Area = request.Areas.Single() };
        // Native living-departure observation is an explicit fixture, not a played restoration.
        initial.Flags.UnionWith(new[] { "trickster", "irabeth_gone", "irabeth.return_correspondence_available",
            "seelah.committed", "arueshalae.committed" });
        check(Rules.Available(story, request, initial), "Living departed correspondence cannot start.");
        var requested = Walk(request, initial);
        foreach (var result in requested)
        {
            if (!result.Has(request.Id))
            {
                check(!result.Has("irabeth.return_request_sent") && !Rules.Available(story, reply, result),
                    "Abandoned draft sends a request or earns a reply.");
                var savedEvidence = result.Has("irabeth.return_docket_precise") || result.Has("irabeth.return_docket_uncertain");
                if (savedEvidence)
                {
                    var open = request.Nodes[0].Choices.Where(c => Rules.Match(c.Requires, c.Forbids, result)).ToArray();
                    check(open.All(c => c.Check == null), "Reopening an unfinished letter rerolls established evidence.");
                    foreach (var resumed in Walk(request, result))
                        check(resumed.Has("irabeth.return_docket_precise") == result.Has("irabeth.return_docket_precise")
                            && resumed.Has("irabeth.return_docket_uncertain") == result.Has("irabeth.return_docket_uncertain"),
                            "Resumed request changes its established evidence.");
                }
                continue;
            }
            check(result.Has("irabeth.return_request_sent")
                && result.Has("irabeth.return_docket_precise") != result.Has("irabeth.return_docket_uncertain")
                && result.Has("irabeth.return_public_case") != result.Has("irabeth.return_supplier_trap"),
                "Sent request loses the actual evidence or chosen approach.");
            check(!Rules.Available(story, reply, result), "Request receives an immediate reply.");
            result.Hour += 47;
            check(!Rules.Available(story, reply, result), "Reply arrives before its courier delay.");
            result.Hour++;
            check(Rules.Available(story, reply, result), "Earned reply remains unavailable after 48 hours.");
            foreach (var answer in Walk(reply, result))
            {
                if (!answer.Has(reply.Id))
                {
                    check(!answer.Has("irabeth.return_meeting_accepted") && !answer.Has("irabeth.return_meeting_declined"),
                        "Postponed reply invents a decision.");
                    continue;
                }
                if (answer.Has("irabeth.return_meeting_declined"))
                {
                    answer.Hour += 1000;
                    answer.Flags.Add("irabeth.return_meeting_arrived");
                    answer.AvailableContacts.Add(meeting.ContactUnit!);
                    check(!Rules.Available(story, meeting, answer), "Arrival fixture overrides a declined invitation.");
                    continue;
                }
                check(answer.Has("irabeth.return_meeting_accepted") && !Rules.Available(story, reply, answer),
                    "Accepted reply is missing consent or can repeat.");
                check(!Rules.Available(story, meeting, answer), "Acceptance manufactures physical arrival.");
                answer.Flags.Add("irabeth.return_meeting_arrived");
                answer.AvailableContacts.Add(meeting.ContactUnit!);
                check(!Rules.Available(story, meeting, answer), "Injected arrival skips the consent delay.");
                answer.Hour += 11;
                check(!Rules.Available(story, meeting, answer), "Meeting opens before 12 hours.");
                answer.Hour++;
                check(Rules.Available(story, meeting, answer), "Agreed meeting cannot open with elapsed time and actor evidence.");
                foreach (var visit in Walk(meeting, answer))
                {
                    check(visit.Has(meeting.Id) && visit.Has("irabeth.return_private_hour_kept"), "Private meeting fails to complete.");
                    check(visit.Has("irabeth_gone") && !visit.Has("irabeth.lover") && !visit.Has("irabeth.committed")
                        && visit.Has("seelah.committed") && visit.Has("arueshalae.committed"),
                        "Meeting reinstates Irabeth, invents romance or changes another relationship.");
                    check(!Rules.Available(story, meeting, visit), "Completed first meeting repeats.");
                }
            }
        }
        foreach (var scene in scenes)
            foreach (var node in scene.Nodes)
                check(reached.Contains(scene.Id + "/" + node.Id), "Unplayed departure visit page: " + scene.Id + "/" + node.Id);
    }
}
