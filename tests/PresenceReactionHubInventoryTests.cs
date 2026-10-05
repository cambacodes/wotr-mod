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
                // eng7-f3: the Ch6 reaction uses its own camp window below; Drezen stays Ch3/5.
            }
        }
        // eng7-f3
        ShadowCampVisit(story, check);
        // end eng7-f3
    }

    // eng7-f3: traverse real paid-return and shadow choices before offering the visitor reaction.
    private static void ShadowCampVisit(Story story, Action<bool, string> check)
    {
        void Refresh(Snapshot snapshot)
        {
            // Match Main.State: composites are observations, not saved choice flags.
            snapshot.Flags.ExceptWith(story.Derived.Keys);
            snapshot.Flags.ExceptWith(story.Counts.Keys);
            Rules.Complete(story, snapshot);
        }
        const string key = "nenio.presence.threshold";
        const string reactionId = "nocticula.trickster.reaction.nenio";
        var presence = story.Presences[key];
        var reaction = story.Scenes.Single(s => s.Id == reactionId);
        check(Rules.PresenceHubScenes(story, key).Select(s => s.Id).SequenceEqual(new[] { reactionId }),
            "F3: camp visit exposed unrelated Nenio content");
        foreach (var fromArcade in new[] { false, true })
        {
            var returnScene = story.Scenes.Single(s => s.Id == "nenio.trickster.dead.the_price_recreated");
            var state = new Snapshot { Chapter = 5, Hour = 1000, Area = story.Presences["nenio.presence"].Area };
            state.Flags.UnionWith(new[] { "trickster", "chapter_later", "nenio.dead" });
            Refresh(state);
            check(Rules.Available(story, returnScene, state), "F3: normal return producer unavailable");
            state = Program.WalkVia(returnScene, state, "terms", 0).Single();
            Refresh(state);
            check(state.Has("nenio.trickster.returned") && state.Has("nenio.trickster.cost.manuscript_surrendered")
                && state.Has("nenio.trickster.cost.owes_an_answer"), "F3: recreated visitor was not paid for");
            if (fromArcade) state.Flags.Add("nenio.presence.failed");
            var drezenKey = fromArcade ? "nenio.presence.arcade" : "nenio.presence";
            check(Rules.PresenceWanted(story.Presences[drezenKey], state), "F3: earned Drezen visitor missing");
            state.Chapter = 6; state.Area = presence.Area; state.Hour += 48;
            state.Flags.UnionWith(new[] { "noct.dead", "noct.acq.council_fight" });
            Refresh(state);
            check(!Rules.PresenceWanted(presence, state), "F3: shadow reaction before its producer");
            var shadow = story.Scenes.Single(s => s.Id == "nocticula.trickster.defeated.shadow");
            check(Rules.Available(story, shadow, state), "F3: normal shadow producer unavailable");
            state = Program.Walk(shadow, state).Single(s => s.Has("nocticula.trickster.cost.shade_secret"));
            Refresh(state);
            check(Rules.PresenceWanted(presence, state), "F3: earned Ch6 visitor missing");
            check(Rules.PlanPresence(presence, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = true })
                .Contains(PresenceStep.Spawn), "F3: camp visitor cannot spawn");
            check(!Rules.PlanPresence(presence, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = false })
                .Contains(PresenceStep.Spawn), "F3: missing camp anchor still spawns visitor");
            state.AvailableContacts.Add(presence.Unit);
            check(Rules.PresenceHubAvailable(story, key, reaction, state), "F3: earned reaction cannot traverse");
            var outcome = Program.Walk(reaction, state).Single();
            check(outcome.Has(reactionId) && !Rules.PresenceHubAvailable(story, key, reaction, outcome)
                && !Rules.PresenceWanted(presence, outcome), "F3: reaction repeated or visit persisted");
            check(!Rules.Available(story, reaction, outcome), "F3: native entry repeated completed visitor reaction");
            var nativeDone = Program.Copy(state); nativeDone.Flags.Add(reactionId);
            check(!Rules.PresenceHubAvailable(story, key, reaction, nativeDone), "F3: completed native reaction repeated on visitor");
            foreach (var withheld in new[] { "return", "visitor", "secret", "defeat", "path", "contact", "area", "chapter",
                "closed", "nocticula.closed", "dissolved", "sacrifice" })
            {
                var missing = Program.Copy(state);
                if (withheld == "return") missing.Flags.Remove("nenio.trickster.returned");
                if (withheld == "visitor") missing.Flags.Remove("nenio.trickster.cost.recreated");
                if (withheld == "secret") missing.Flags.Remove("nocticula.trickster.cost.shade_secret");
                if (withheld == "defeat") missing.Flags.Remove("noct.acq.council_fight");
                if (withheld == "path") { missing.Flags.Remove("trickster"); missing.Flags.Remove("trickster.ever"); missing.Flags.Add("angel"); }
                if (withheld == "contact") missing.AvailableContacts.Clear();
                if (withheld == "area") missing.Area = story.Presences[drezenKey].Area;
                if (withheld == "chapter") missing.Chapter = 5;
                if (withheld == "closed") missing.Flags.Add("nenio.closed");
                if (withheld == "nocticula.closed") missing.Flags.Add(story.Relationships[reaction.Relationship].ClosedFlag);
                if (withheld == "dissolved") missing.Flags.Add("nenio.dissolved");
                if (withheld == "sacrifice") missing.Flags.Add("sacrifice");
                // Runtime snapshots recompute composites; Complete only adds them to a fresh snapshot.
                missing.Flags.ExceptWith(story.Derived.Keys);
                missing.Flags.ExceptWith(story.Counts.Keys);
                Rules.Complete(story, missing);
                check(!Rules.PresenceHubAvailable(story, key, reaction, missing), "F3: unearned camp reaction: " + withheld);
            }
        }
    }
    // end eng7-f3
}
