using System;
using System.Linq;
using Tirabade;

internal static class PresenceReactionHubInventoryTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var ids = new[] { "nocticula.trickster.reaction.nenio", "eritrice.trickster.react.nenio_motion",
            "eritrice.trickster.react.nenio_tabled", "areelu.trickster.react.nenio_two_drafts", "melazmera.trickster.react.nenio_specimen" };
        foreach (var key in new[] { "nenio.presence", "nenio.presence.arcade" })
        {
            var presence = story.Presences[key];
            var entries = Rules.PresenceHubScenes(story, key);
            foreach (var id in ids)
            {
                var scene = story.Scenes.Single(s => s.Id == id);
                check(entries.Count(s => s.Id == id) == 1, "Q7-29: hub construction lost/duplicated " + key + "/" + id);
                check(Rules.EntryTargets(scene).SequenceEqual(new[] { "1ab909cc3a6194840b1475b99547c263" }), "Q7-29: native entry changed " + id);
                var state = new Snapshot { Chapter = scene.MinChapter, Hour = 1000, Area = presence.Area };
                state.Flags.UnionWith(scene.Requires);
                state.Flags.UnionWith(new[] { "trickster", "chapter_later", "nenio.dead", "nenio.trickster.returned", "nenio.trickster.cost.recreated" });
                if (key.EndsWith(".arcade")) state.Flags.Add("nenio.presence.failed");
                Rules.Complete(story, state);
                check(Rules.PlanPresence(presence, Rules.PresenceWanted(presence, state),
                    new PresenceObservation { AreaLoaded = true, AnchorResolved = true }).Contains(PresenceStep.Spawn)
                    == (scene.MinChapter <= presence.MaxChapter), "Q7-29: visitor placement window changed " + id);
                state.AvailableContacts.Add(presence.Unit); // observed spawned actor, after the placement plan
                bool eligible = scene.MinChapter <= presence.MaxChapter;
                check(Rules.PresenceHubAvailable(story, key, scene, state) == eligible, "Q7-29: hub selection " + key + "/" + id);
                if (eligible)
                {
                    var outcomes = Program.Walk(scene, state).ToArray();
                    check(outcomes.Length > 0 && outcomes.All(s => s.Has(scene.Id)), "Q7-29: reaction not traversed " + id);
                    check(outcomes.All(s => !Rules.PresenceHubAvailable(story, key, scene, s)), "Q7-29: reaction repeated " + id);
                    check(scene.Nodes.All(n => !string.IsNullOrWhiteSpace(n.Text)), "Q7-29: blank rendered reaction " + id);
                    var missing = Program.Copy(state); missing.AvailableContacts.Clear();
                    check(!Rules.PresenceHubAvailable(story, key, scene, missing), "Q7-29: absent speaker offered " + id);
                    missing = Program.Copy(state); missing.Area = "elsewhere";
                    check(!Rules.PresenceHubAvailable(story, key, scene, missing), "Q7-29: wrong area offered " + id);
                    missing = Program.Copy(state); missing.Flags.Remove("nenio.trickster.returned");
                    check(!Rules.PresenceHubAvailable(story, key, scene, missing), "Q7-29: unearned return offered " + id);
                    foreach (var requirement in scene.Requires)
                    {
                        missing = Program.Copy(state); missing.Flags.Remove(requirement);
                        check(!Rules.PresenceHubAvailable(story, key, scene, missing), "Q7-29: lost route requirement " + requirement);
                    }
                }
                else Console.WriteLine("Q7-29 DATA BLOCKER: " + id + " requires Ch6; " + key + " ends at Ch5.");
            }
        }
    }
}
