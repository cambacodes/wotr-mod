using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class IrabethDepartureVisitTests
{
    private const string Correspondence = "irabeth.return_correspondence_available";
    private const string Arrival = "irabeth.return_meeting_arrived";
    private const string Accepted = "irabeth.return_meeting_accepted";
    private const string Declined = "irabeth.return_meeting_declined";
    private const string Unit = "280d4712dceb37f4a88e98f1f4c6e64f";
    private static readonly JsonSerializerOptions Json = new JsonSerializerOptions { IncludeFields = true };
    private static T Copy<T>(T value) => JsonSerializer.Deserialize<T>(JsonSerializer.Serialize(value, Json), Json)!;

    internal static void Run(Story source, Action<bool, string> check)
    {
        // Keep mutation tests small while testing the caller's actual authored scene contracts.
        var story = new Story();
        story.Relationships["irabeth"] = Copy(source.Relationships["irabeth"]);
        // The Trickster return (irabeth.trickster.returned) is produced by scenes this mini story leaves out.
        story.Relationships["irabeth"].UnavailableOverrides.Clear();
        story.Relationships["irabeth"].TricksterAccess.Clear();
        story.Etudes = new Dictionary<string, string>(source.Etudes);
        foreach (string id in new[] { "irabeth.return_request", "irabeth.return_reply", "irabeth.return_first_words" })
            story.Scenes.Add(Copy(source.Scenes.Single(s => s.Id == id)));
        Rules.Validate(story);
        check(Copy(story).Scenes.All(s => s.AfterDeparture == "irabeth"), "Departure metadata did not survive JSON roundtrip.");
        foreach (var scene in story.Scenes)
        {
            var state = new Snapshot { Chapter = 5, Hour = 1000, Area = scene.Areas.Single() };
            state.Flags.UnionWith(scene.Requires);
            state.Flags.UnionWith(new[] { "seelah.committed", "arueshalae.committed" });
            foreach (string flag in scene.Requires) state.Times[flag] = state.Hour - scene.DelayHours;
            if (scene.ContactUnit != null) state.AvailableContacts.Add(Unit);
            var originalFlags = state.Flags.ToArray();
            check(Rules.Available(story, scene, state) && Rules.ContactAvailable(story, scene, state), "Earned visit remains blocked: " + scene.Id);
            var unmarked = Copy(scene); unmarked.AfterDeparture = null;
            check(!Rules.Available(story, unmarked, state) && !Rules.ContactAvailable(story, unmarked, state), "Ordinary departed scene acquired the exception.");
            foreach (string flag in scene.Requires)
            {
                state.Flags.Remove(flag);
                check(!Rules.Available(story, scene, state) && !Rules.ContactAvailable(story, scene, state), "Missing visit evidence accepted: " + flag);
                state.Flags.Add(flag);
            }
            foreach (string flag in new[] { "irabeth_dead", "closed", "irabeth.closed", Declined, "inhuman", "swarm", "true_lich" })
            {
                state.Flags.Add(flag);
                check(!Rules.Available(story, scene, state) && !Rules.ContactAvailable(story, scene, state), "Visit ignored live refusal, closure or death: " + flag);
                state.Flags.Remove(flag);
            }
            foreach (int chapter in new[] { 3, 4, 6 })
            {
                state.Chapter = chapter;
                check(!Rules.Available(story, scene, state) && !Rules.ContactAvailable(story, scene, state), "Departure visit escaped Chapter 5.");
            }
            state.Chapter = 5; state.Area = "other";
            check(!Rules.Available(story, scene, state) && !Rules.ContactAvailable(story, scene, state), "Departure visit escaped Drezen.");
            state.Area = scene.Areas.Single();
            if (scene.DelayHours > 0)
            {
                state.Hour--;
                check(!Rules.Available(story, scene, state), "Visit ignored earned delay.");
                state.Hour++;
                string waitedFor = scene.Id == "irabeth.return_reply" ? "irabeth.return_request_sent" : Accepted;
                int timestamp = state.Times[waitedFor]; state.Times.Remove(waitedFor);
                check(!Rules.Available(story, scene, state), "Missing sent or accepted timestamp skipped the wait.");
                state.Times[waitedFor] = state.Hour + 1;
                check(!Rules.Available(story, scene, state), "Future consent timestamp skipped the wait.");
                state.Times[waitedFor] = -1;
                check(!Rules.Available(story, scene, state), "Negative consent timestamp skipped the wait.");
                state.Times[waitedFor] = timestamp;
            }
            if (scene.ContactUnit != null)
            {
                state.AvailableContacts.Clear();
                check(!Rules.Available(story, scene, state) && !Rules.ContactAvailable(story, scene, state), "Arrival flag alone manufactured actor contact.");
                state.AvailableContacts.Add("b5e867e13503c6f41bb1316705efb4a2");
                check(!Rules.Available(story, scene, state), "Wife actor substituted for Irabeth.");
                state.AvailableContacts.Clear(); state.AvailableContacts.Add(Unit);
                state.Flags.Remove(Arrival); state.Flags.Add(Correspondence);
                check(!Rules.Available(story, scene, state) && !Rules.ContactAvailable(story, scene, state), "Accepted correspondence substituted for physical arrival.");
                state.Flags.Remove(Correspondence); state.Flags.Add(Arrival);
            }
            check(state.Flags.SetEquals(originalFlags) && state.Has("seelah.committed") && state.Has("arueshalae.committed"), "Visit checks changed history or another romance.");
        }
        void Reject(Action<Story> change, string label)
        {
            var invalid = Copy(story); change(invalid);
            bool rejected = false;
            try { Rules.Validate(invalid); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Malformed departure metadata accepted: " + label);
        }
        foreach (int index in new[] { 0, 1, 2 })
        {
            Reject(s => s.Scenes[index].AfterDeparture = "anevia", "foreign departure");
            Reject(s => s.Scenes[index].Id += "_future", "unbounded route expansion");
            Reject(s => s.Scenes[index].Relationship = "tirabade", "shared romance exception");
            Reject(s => s.Scenes[index].Owner = "Epilogue", "epilogue bypass");
            Reject(s => s.Scenes[index].MinChapter = 3, "early chapter");
            Reject(s => s.Scenes[index].MaxChapter = 6, "late chapter");
            Reject(s => s.Scenes[index].Areas = Array.Empty<string>(), "unrestricted area");
            Reject(s => s.Scenes[index].AfterRecovery = "konomi", "combined recovery exception");
            Reject(s => s.Scenes[index].Recovery = "konomi", "combined revival exception");
            Reject(s => s.Scenes[index].AdditionalContactUnits = new[] { "b5e867e13503c6f41bb1316705efb4a2" }, "extra actor contract");
            Reject(s => s.Scenes[index].ForbidOverrides[Declined] = Accepted, "decline override");
            foreach (string flag in new[] { "irabeth_gone", "irabeth_dead", "irabeth.committed", "irabeth.started", "seelah.committed", "arueshalae.committed" })
                Reject(s => s.Scenes[index].Nodes[0].Choices[0].Set = new[] { flag }, "native or relationship history write");
            foreach (string flag in new[] { "trickster", "irabeth_gone" })
                Reject(s => s.Scenes[index].Requires = s.Scenes[index].Requires.Where(f => f != flag).ToArray(), "missing " + flag);
            foreach (string flag in new[] { "closed", "irabeth.closed", Declined, "irabeth_dead", "inhuman", "swarm", "true_lich" })
                Reject(s => s.Scenes[index].Forbids = s.Scenes[index].Forbids.Where(f => f != flag).ToArray(), "missing live guard " + flag);
        }
        foreach (int index in new[] { 0, 1 })
        {
            Reject(s => s.Scenes[index].Requires = s.Scenes[index].Requires.Where(f => f != Correspondence).ToArray(), "missing remote proof");
            Reject(s => s.Scenes[index].ContactUnit = Unit, "remote requires inaccessible body");
            Reject(s => s.Scenes[index].Remote = false, "physical request or reply");
        }
        Reject(s => s.Scenes[1].DelayHours = 47, "reply has no travel time");
        Reject(s => s.Scenes[1].Forbids = s.Scenes[1].Forbids.Where(f => f != Accepted).ToArray(), "reply repeats after acceptance");
        foreach (string flag in new[] { "irabeth.return_request", "irabeth.return_request_sent" })
            Reject(s => s.Scenes[1].Requires = s.Scenes[1].Requires.Where(f => f != flag).ToArray(), "reply lacks request");
        Reject(s => s.Scenes[2].DelayHours = 11, "first visit skips consent delay");
        Reject(s => s.Scenes[2].Remote = true, "physical scene made remote");
        Reject(s => s.Scenes[2].ContactUnit = null, "physical contact removed");
        Reject(s => s.Scenes[2].ContactUnit = "b5e867e13503c6f41bb1316705efb4a2", "wrong physical actor");
        Reject(s => s.Scenes[2].AnswerLists = Array.Empty<string>(), "unbound physical entry");
        foreach (string flag in new[] { "irabeth.return_reply", Accepted, Arrival })
            Reject(s => s.Scenes[2].Requires = s.Scenes[2].Requires.Where(f => f != flag).ToArray(), "physical proof removed");
        foreach (string flag in new[] { Correspondence, Arrival })
        {
            Reject(s => s.Scenes[0].Nodes[0].Choices[0].Set = new[] { flag }, "authored proof");
            Reject(s => s.Scenes[0].Id = flag, "scene completion proof");
            Reject(s => s.Relationships["irabeth"].StartedFlag = flag, "relationship proof");
            Reject(s => s.Etudes[flag] = Unit, "etude proof alias");
            Reject(s => s.CompletedEtudes[flag] = Unit, "completed etude proof alias");
            Reject(s => s.CompletedQuests[flag] = Unit, "quest proof alias");
            Reject(s => s.SeenCues[flag] = new[] { Unit }, "cue proof alias");
            Reject(s => s.SelectedAnswers[flag] = Unit, "answer proof alias");
            Reject(s => s.StartedDialogs[flag] = Unit, "dialog proof alias");
        }
    }
}
