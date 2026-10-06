using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class EngineQ5Tests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        if (!story.Derived.ContainsKey(Rules.TricksterNow)) return;
        // Exercise every placed contact/copy with a fresh snapshot, as Main builds one on each world tick.
        foreach (var pair in story.Presences)
        {
            string rel = Rules.PresenceRelationship(pair.Key)!;
            var relationship = story.Relationships[rel];
            var presence = pair.Value;
            string guard = Rules.PresenceGuard(story, pair.Key);  // eng7-l06
            check(presence.Requires.Contains(guard)
                // eng7-l06: the exported declaration is validated generically by Rules.Validate.
                && (story.PresenceExceptions.ContainsKey(pair.Key)
                    ? !story.DerivedOpenRoutes.ContainsKey(guard) && story.DerivedForbids.ContainsKey(guard)
                    : story.DerivedOpenRoutes.TryGetValue(guard, out var routes) && routes.SequenceEqual(new[] { rel })),
                "Missing central presence route guard: " + pair.Key);
            var flags = presence.Requires.Where(k => k != guard).Concat(presence.RequiresAnyGroups.Select(g => g[0]))
                .Concat(relationship.UnavailableOverrides.Values).ToHashSet();
            flags.ExceptWith(presence.Forbids);
            flags.Remove(relationship.ClosedFlag);
            // eng7-l07: current altered-presence policy reads a native live-path input;
            // do not inject trickster.now into a later failed-path snapshot.
            if (presence.Requires.Contains(Rules.TricksterNow))
            {
                flags.Remove(Rules.TricksterNow);
                flags.Add("trickster");
            }

            Snapshot World(IEnumerable<string> held, bool earned = false)
            {
                var state = new Snapshot { Chapter = presence.MinChapter, Hour = 1000, Area = presence.Area,
                    Flags = new HashSet<string>(held) };
                if (earned) foreach (var key in held.Where(story.Derived.ContainsKey)) HouseholdTests.Earn(story, state, key);
                foreach (var loss in held.Where(relationship.UnavailableFlags.Contains).Where(story.Derived.ContainsKey))
                    HouseholdTests.Earn(story, state, loss);
                state.Flags.Add(Rules.ChapterFlag(state.Chapter)!);
                Rules.Complete(story, state);
                return state;
            }
            var ready = World(flags, true);
            var original = new Presence { Area = presence.Area, MinChapter = presence.MinChapter, MaxChapter = presence.MaxChapter,
                Requires = presence.Requires.Where(k => k != guard).ToArray(), Forbids = presence.Forbids,
                RequiresAnyGroups = presence.RequiresAnyGroups, DelayHours = presence.DelayHours };
            check(Rules.PresenceWanted(presence, ready)
                == (Rules.PresenceWanted(original, ready) && !ready.Has(relationship.ClosedFlag)
                    && !relationship.UnavailableFlags.Any(f => Rules.Blocks(relationship, f, ready)
                        && !Rules.PresenceLossLifted(story, pair.Key, f, ready))),
                "Presence ignores its route state: " + pair.Key);
            var closed = new HashSet<string>(flags) { relationship.ClosedFlag };
            var closedState = World(closed);
            check(!Rules.PresenceWanted(presence, closedState), "Closed partner stands in the world: " + pair.Key);
            check(Rules.PlanPresence(presence, false, new PresenceObservation { AreaLoaded = true, Recorded = true,
                Submitted = true, CopyFound = true, CopyAlive = true, NativeAlive = true, RecordedUnhide = true })
                .Contains(presence.Mode == "spawn-copy" ? PresenceStep.Remove : PresenceStep.Hide),
                "Closed partner is not removed/hidden: " + pair.Key);

            foreach (string lost in relationship.UnavailableFlags)
            {
                var departed = new HashSet<string>(flags) { lost };
                departed.ExceptWith(relationship.UnavailableOverrides.Values);
                // eng7-l07: without the paid coffin ritual, no bootstrap actor is owed.
                if (rel == "camellia") departed.Remove("camellia.trickster.raised");
                // An override that is itself derived (Wenduag's returned_available) is withheld by dropping the flags it derives from.
                foreach (string overrideKey in relationship.UnavailableOverrides.Values)
                    if (story.Derived.TryGetValue(overrideKey, out var sources)) departed.ExceptWith(sources.SelectMany(g => g));
                var absentState = World(departed);
                // eng7-l06: paid bootstraps/absent partners concern contact only; ordinary losses still withhold it.
                if (!Rules.PresenceLossLifted(story, pair.Key, lost, absentState))
                    check(!Rules.PresenceWanted(presence, absentState), "Unreturned partner stands after " + lost + ": " + pair.Key);
                if (Rules.Blocks(relationship, lost, absentState) && !Rules.PresenceLossLifted(story, pair.Key, lost, absentState))
                    check(!absentState.Has(guard), "A loss fails to withhold the central guard: " + pair.Key);
                if (relationship.UnavailableOverrides.TryGetValue(lost, out string? returned))
                {
                    departed.UnionWith(relationship.UnavailableOverrides.Values);
                    departed.UnionWith(new[] { "trickster.ever", "trickster.failed" });
                    var returnedState = World(departed, true);
                    check(returnedState.Has(returned)
                            ? returnedState.Has(guard) && Rules.RouteOpen(relationship, returnedState)
                            : !returnedState.Has(guard),
                        "Earned return lost after leaving Trickster: " + pair.Key + "/" + returned);
                    // A cell or spared-body variant may forbid the return and yield to its sibling presence.
                    if (Rules.Match(presence.Requires, presence.Forbids, returnedState)
                        && presence.RequiresAnyGroups.All(g => g.Any(returnedState.Has)))
                        check(Rules.PresenceWanted(presence, returnedState), "Returned variant hidden: " + pair.Key);
                }
            }
        }

        // These audited producers used the run latch alone. Leaving the path must now withhold the act.
        foreach (string id in new[] { "anevia.trickster.gone.wardrobe", "seelah.trickster.dead.effects_reply",
            "minagho_chivarro.trickster.minagho_dead.brand", "minagho_chivarro.trickster.chivarro_dead.bought" })
        {
            var scene = story.Scenes.Single(s => s.Id == id);
            var state = new Snapshot { Chapter = scene.MinChapter, Hour = 1000,
                Area = scene.Areas.FirstOrDefault() ?? "",
                Flags = new HashSet<string>(scene.Requires.Where(k => !story.Derived.ContainsKey(k))) };
            state.Flags.UnionWith(new[] { "trickster", "trickster.ever", "trickster.failed" });
            Rules.Complete(story, state);
            check(!state.Has(Rules.TricksterNow) && !Program.CurrentAvailable(story, scene, state),
                "Return device completes after leaving Trickster: " + id);
        }
    }
}
