#if RRT_J01_TESTS
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class J01ContactTests
{
    private static void Check(bool value, string message)
    {
        if (!value) throw new Exception(message);
    }

    private static Snapshot Seed(Story story, Scene scene)
    {
        var state = new Snapshot { Chapter = 5, Hour = 100, Area = scene.Areas.FirstOrDefault() ?? "" };
        state.Flags.UnionWith(scene.Requires.Where(k => k != scene.ContactWitness));
        foreach (var group in scene.RequiresAnyGroups) state.Flags.Add(group[0]);
        // Saved commitments qualify a household seat; they never supply a body.
        foreach (var route in scene.PrivateParticipants ? Array.Empty<string>() : scene.Participants)
            if (story.Derived.TryGetValue(route + ".harem.eligible", out var groups))
                state.Flags.UnionWith(groups[0]);
        foreach (var woman in scene.PrivateParticipants ? Array.Empty<string>() : scene.ParticipantWomen)
            state.Flags.UnionWith(story.SeatWomen[woman].Requires);
        foreach (var contact in scene.ParticipantContacts.Values)
        {
            state.Flags.UnionWith(contact.Requires);
            var option = contact.Options.FirstOrDefault(o => o.Requires.All(state.Has) && !o.Forbids.Any(state.Has));
            if (option != null) state.AvailableContacts.Add(option.Units[0]);
        }
        if (scene.ContactUnit != null) state.AvailableContacts.Add(scene.ContactUnit);
        state.AvailableContacts.UnionWith(scene.AdditionalContactUnits);
        foreach (var key in state.Flags) state.Times[key] = 0;
        return state;
    }

    private static void Main(string[] args)
    {
        var story = JsonSerializer.Deserialize<Story>(File.ReadAllText(args[0]),
            new JsonSerializerOptions { IncludeFields = true })!;
        Rules.Validate(story);
        Check(!story.SeatWomen["arueshalae"].Requires.Contains("household.pair.seelah_arueshalae.arueshalae_body"),
            "Shared Arueshalae seat imports S03a's native recruitment");
        const string prefix = "household.pair.galfrey_arueshalae.";
        foreach (var scene in story.Scenes.Where(s => s.Id.StartsWith(prefix)))
        {
            foreach (bool returned in new[] { false, true })
            {
                var state = Seed(story, scene);
                if (returned)
                {
                    state.Flags.Add("galfrey.trickster.returned");
                    state.AvailableContacts.Remove("8c5dcc93d68d0ed44afd43902201da40");
                    state.AvailableContacts.Add(story.Presences["galfrey.presence"].Unit);
                }
                Check(!state.Has(scene.ContactWitness!), "Attendance was seeded");
                Check(Rules.Available(story, scene, state), scene.Id + " qualified bodies");
                Check(Rules.ContactAvailable(story, scene, state), scene.Id + " live continuation");
                state.AvailableContacts.Clear();
                state.Flags.Add(scene.ContactWitness!);
                Check(!Rules.Available(story, scene, state), scene.Id + " forged attendance");
                foreach (var node in scene.Nodes)
                    Check(!Rules.ContactAvailable(story, scene, state), scene.Id + "/" + node.Id + " lost contact");
            }
            foreach (var loss in new[] { "household.closed", "galfrey.closed", "arueshalae.closed", "galfrey.epoch_unavailable",
                                         "arueshalae.epoch_unavailable", "galfrey.returned_actor_lost" })
            {
                var state = Seed(story, scene); state.Flags.Add(loss);
                Check(!Rules.ContactAvailable(story, scene, state), scene.Id + " continuation after " + loss);
            }
            var elsewhere = Seed(story, scene); elsewhere.Area = "wrong venue";
            Check(!Rules.ContactAvailable(story, scene, elsewhere), "Attendance outside Table venue");
            var recovered = Seed(story, scene);
            var death = scene.Id.EndsWith(".good") ? "arueshalae_dead" : "arueshalae.evil_dead";
            recovered.Flags.UnionWith(new[] { death, "arueshalae.trickster.returned" });
            Check(Rules.ContactAvailable(story, scene, recovered), scene.Id + " registered current Arueshalae return");
            recovered.Flags.Add("arueshalae.epoch_unavailable");
            Check(!Rules.ContactAvailable(story, scene, recovered), scene.Id + " old return versus later loss");
        }
        foreach (var scene in story.Scenes.Where(s => s.PrivateParticipants))
        {
            var state = Seed(story, scene);
            state.Flags.Add("household.closed");
            foreach (var route in scene.Participants) state.Flags.Remove(route + ".harem.eligible");
            Check(!state.Has("nidalynn.committed") && !state.Has("areelu.committed")
                && !state.Has("foresight.page_taken"), scene.Id + " private romance/page prerequisite");
            Check(Rules.Available(story, scene, state), scene.Id + " private unromanced/Table closed");
            foreach (var loss in scene.ParticipantContacts.Values.SelectMany(c => c.Forbids)
                .Concat(new[] { "engine.l12.commander_unreturned" }))
            {
                var lost = Seed(story, scene); lost.Flags.Add(loss);
                Check(!Rules.ContactAvailable(story, scene, lost), scene.Id + " private loss " + loss);
            }
            state.Flags.Remove("trickster.now");
            Check(!Rules.Available(story, scene, state), scene.Id + " off Trickster");
        }
        // The shared contact API keeps every additional body mandatory.
        var extra = story.Scenes.First(s => s.Id.StartsWith(prefix));
        var both = Seed(story, extra);
        extra.ContactUnit = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
        extra.AdditionalContactUnits = new[] { "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb" };
        both.AvailableContacts.Add(extra.ContactUnit);
        Check(!Rules.ContactAvailable(story, extra, both), "Additional body omitted");
        both.AvailableContacts.UnionWith(extra.AdditionalContactUnits);
        Check(Rules.ContactAvailable(story, extra, both), "Additional body present");
        Console.WriteLine("J01 production rules: PASS (runtime attendance, private contacts, loss/venue/additional-body histories)");
    }
}
#endif
