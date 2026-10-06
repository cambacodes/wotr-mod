using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// eng7-l12: actual Rules.Available, for automatic AND manual Remote delivery.
internal static class LocationInventoryTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    internal static void Run(Story story, Action<bool, string> check)
    {
        foreach (var id in new[] { "hepzamirah.trickster.ghost.body", "hepzamirah.trickster.body.hounds",
            "melazmera.trickster.react.nenio_specimen", "melazmera.trickster.ch4.hunt_found" })
        {
            var scene = story.Scenes.Single(s => s.Id == id);
            var state = new Snapshot { Chapter = scene.MinChapter, Hour = 12000, Area = scene.Areas[0] };
            state.Flags.UnionWith(scene.Requires);
            state.Flags.Remove("trickster.now"); // derive live power from native input
            state.Flags.Add("trickster");
            state.AvailableContacts.UnionWith(new[] { scene.ContactUnit ?? "" });
            Rules.Complete(story, state);
            check(Rules.Available(story, scene, state), "l12 earned venue blocked: " + id);
            state.Area = id.Contains("hunt_found") ? "c876d5303f4a19f4a80b0cc9b313db6f" : "3538511f16d45f44f8249ff710777e2d";
            check(!Rules.Available(story, scene, state), "l12 wrong-area manual/automatic delivery: " + id);
            state.Area = scene.Areas[0];
            check(Rules.Available(story, scene, state), "l12 return to earned venue blocked: " + id);
        }
        var night = story.Scenes.Single(s => s.Id == "horzalah.trickster.late.at_night");
    }
}
