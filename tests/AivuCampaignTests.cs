using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class AivuCampaignTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Get(string id) => story.Scenes.Single(s => s.Id == "aivu." + id);
        string[] oldIds = { "a_city_with_wings", "the_roof_below", "a_way_for_feet", "someone_elses_turn" };
        string[] newIds = { "the_wheel_with_no_cart", "the_garden_procession", "the_most_important_tail",
            "a_very_important_guest", "when_the_drum_does_not_come", "a_family_with_too_many_names",
            "paint_for_a_weather_day", "a_small_garden_of_her_own", "the_people_on_the_map",
            "the_turn_the_commander_needs", "a_reply_from_the_other_garden", "the_next_excellent_thing" };
        var first = Get("a_garden_that_can_go"); var late = Get("a_late_garden");
        var castle = Get("a_castle_in_a_bad_place"); var rescue = Get("the_watch_she_chooses");
        var physical = newIds.Select(Get).Concat(new[] { first, late, castle, rescue }).ToArray();
        var endings = story.Scenes.Where(s => s.Id.StartsWith("aivu.ending_", StringComparison.Ordinal)).ToArray();
        var visited = physical.ToDictionary(s => s.Id, _ => new HashSet<string>());
        var outcomes = new HashSet<string>();
        var native = story.Etudes.Keys.Concat(story.CompletedQuests.Keys).Concat(story.CompletedEtudes.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();
        check(physical.All(s => s.ContactUnit == "32a037e97c3d5c54b85da8f639616c57" && !Rules.IsRemote(s)), "Aivu campaign replaces or bypasses the actual pet.");
        check(!physical.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).Any(native.Contains), "Aivu campaign writes native history.");
        check(physical.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).All(c => c.Revive == null), "Friendship introduces a false rescue or new pet.");
        var roll = physical.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Single(c => c.Check != null);
        check(roll.Check!.Skill == "SkillPerception" && roll.Check.DC == 25 && roll.Check.CommanderOnly && roll.Set.Length == 0,
            "Wheel inspection is not a real Commander Perception check.");
        var finalStates = new List<Snapshot>(); Snapshot? gatheringHistory = null;
        foreach (bool early in new[] { true, false })
        foreach (bool nexus in new[] { false, true })
        foreach (bool nativeFearHeard in new[] { false, true })
        {
            if (!early && nexus) continue;
            var initial = new Snapshot { Chapter = early ? 3 : 5, Hour = 1000, Area = first.Areas.Single() };
            initial.Flags.UnionWith(new[] { "azata", "seelah.committed", "konomi.committed" });
            initial.AvailableContacts.Add(first.ContactUnit!);
            var order = (early ? oldIds.Select(Get).Append(first) : new[] { late }).Concat(newIds.Select(Get)).ToList();
            if (nexus)
            {
                var position = order.FindIndex(s => s.Id == "aivu.a_family_with_too_many_names");
                order.InsertRange(position, new[] { castle, rescue });
            }
            var states = new List<Snapshot> { initial };
            for (int index = 0; index < order.Count; index++)
            {
                var scene = order[index]; var next = new List<Snapshot>();
                foreach (var prior in states)
                {
                    var ready = Program.Copy(prior);
                    ready.Area = scene.Areas.Single();
                    if (scene == castle || scene == rescue) ready.Chapter = 4;
                    else if (ready.Chapter == 4 || scene.MinChapter == 5) ready.Chapter = 5;
                    // External native quest progression, never an authored rescue completion.
                    if (scene == rescue)
                    {
                        ready.Flags.Add("aivu.native_rescue_complete");
                        if (nativeFearHeard) ready.Flags.Add("aivu.native_fear_told");
                    }
                    ready.Hour += scene.DelayHours;
                    check(Rules.Available(story, scene, ready), "Played Aivu history stranded at " + scene.Id);
                    Guards(scene, ready);
                    foreach (var result in Program.Walk(scene, ready, (page, partial) =>
                    {
                        if (visited.TryGetValue(scene.Id, out var pages)) pages.Add(page);
                        check(partial.Flags.SetEquals(ready.Flags), "Aivu commits a decision before the terminal acknowledgement.");
                        var missing = Program.Copy(partial); missing.AvailableContacts.Clear();
                        check(!Rules.ContactAvailable(story, scene, missing), "Aivu scene survives actual pet contact loss.");
                        missing.AvailableContacts.Add(scene.ContactUnit!);
                        check(Rules.Available(story, scene, missing), "Aivu interrupted scene cannot restart after contact returns.");
                        if (scene == rescue && page == "remembered") check(partial.Has("aivu.native_fear_told"), "Aivu invents a prior native confession.");
                        if (scene == rescue && page == "present") check(!partial.Has("aivu.native_fear_told"), "Aivu ignores an already heard confession.");
                        if (scene.Id == "aivu.a_small_garden_of_her_own" && page == "potted") check(partial.Has("aivu.cutting_potted"), "Failed or nonroll inspection gets the missed potting lesson.");
                        if (scene.Id == "aivu.a_small_garden_of_her_own" && page == "appointment") check(!partial.Has("aivu.cutting_potted"), "Aivu repeats a completed potting lesson as overdue.");
                        if (scene.Id == "aivu.the_next_excellent_thing" && page.StartsWith("rescue_", StringComparison.Ordinal))
                            check(partial.Has("aivu." + page), "Final visit invents optional Nexus company.");
                    }))
                    {
                        check(ready.Flags.IsSubsetOf(result.Flags), "Aivu rewrites existing native or relationship history.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags) && result.Times.Count == ready.Times.Count, "Aivu postponement grants progress.");
                            continue;
                        }
                        check(!Rules.Available(story, scene, result), "Completed Aivu visit repeats.");
                        if (!early) check(!result.Has("aivu.opening_kept") && !result.Has("aivu.someone_elses_turn"), "Late friendship fabricates original map visits.");
                        outcomes.UnionWith(result.Flags);
                        if (scene.Id == "aivu.when_the_drum_does_not_come") gatheringHistory ??= Program.Copy(result);
                        next.Add(result);
                    }
                }
                states = DistinctForFuture(next, order.Skip(index + 1).Concat(endings));
                check(states.Count > 0, "Aivu has no completed continuation after " + scene.Id);
            }
            foreach (var state in states)
            {
                check(state.Has("aivu.campaign_developed") && state.Has("aivu.trusted"), "Actual full Aivu campaign lacks earned final acknowledgement.");
                check(endings.Count(s => s.Owner == "Epilogue" && Rules.Available(story, s, state)) == 1, "Developed Aivu history has conflicting or missing ordinary endings.");
                foreach (string change in new[] { "aivu.absent", "aivu.detached", "swarm", "sacrifice", "ascended" })
                {
                    var altered = Program.Copy(state); altered.Flags.Add(change);
                    check(endings.Count(s => s.Owner == "Epilogue" && Rules.Available(story, s, altered)) == 1, "Aivu has conflicting or missing ending for " + change);
                }
                foreach (string path in new[] { "legend", "dragon" })
                {
                    var altered = Program.Copy(state); altered.Flags.Remove("azata"); altered.Flags.Add(path);
                    check(endings.Count(s => s.Owner == "Epilogue" && Rules.Available(story, s, altered)) == 1, "Aivu lost-power ending missing for " + path);
                }
                finalStates.Add(state);
            }
        }
        foreach (var scene in physical)
            check(visited[scene.Id].SetEquals(scene.Nodes.Select(n => n.Id)), "Unreached new Aivu page: " + scene.Id);
        foreach (string flag in new[] { "wheel_found", "wheel_missed", "wheel_expert", "garden_procession", "garden_quiet", "sign_finished", "sign_repainted",
            "commander_story", "commander_competitive", "commander_learning", "pella_new_picture", "pella_original_picture", "rescue_story", "rescue_watch" })
            check(outcomes.Contains("aivu." + flag), "Unplayed Aivu outcome: " + flag);

        // Reproduce native absence on an actually played friendship, then only remove the native absence.
        check(gatheringHistory != null, "No actual gathering history captured.");
        var absent = Program.Copy(gatheringHistory!); absent.Chapter = 4; absent.Area = castle.Areas.Single(); absent.Hour += 100;
        check(Rules.Available(story, castle, absent), "Absence witness was unavailable before its blocker.");
        absent.Flags.Add("aivu.absent");
        check(!Rules.Available(story, castle, absent), "Kidnapped pet attends a friendly Nexus visit.");
        absent.Flags.Remove("aivu.absent");
        check(Rules.Available(story, castle, absent), "Completed native absence permanently strands the pet.");
        check(!Rules.Available(story, rescue, absent), "Pet presence alone invents a rescue quest completion.");
        absent.Flags.Add("aivu.native_rescue_complete");
        check(Rules.Available(story, rescue, absent), "Actual rescue completion does not restore its support visit.");
        var trickster = Program.Copy(absent); trickster.Flags.Remove("azata"); trickster.Flags.Add("trickster");
        check(!Rules.Available(story, rescue, trickster) && !Rules.Available(story, castle, trickster), "Trickster is silently granted Azata pet ownership.");

        void Guards(Scene scene, Snapshot ready)
        {
            foreach (string flag in scene.Requires)
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(flag);
                check(!Rules.Available(story, scene, missing), "Aivu ignores prerequisite " + flag);
            }
            foreach (string flag in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag);
                check(!Rules.Available(story, scene, blocked), "Aivu ignores blocker " + flag);
                if (native.Contains(flag))
                    check(!Rules.ContactAvailable(story, scene, blocked), "Aivu continuation ignores native or local blocker " + flag);
            }
            var elsewhere = Program.Copy(ready); elsewhere.Area = "elsewhere";
            check(!Rules.Available(story, scene, elsewhere), "Aivu starts outside the verified native contact area.");
            if (scene.DelayHours > 0)
            {
                var anchors = scene.Requires.Where(ready.Times.ContainsKey).ToArray();
                check(anchors.Length > 0, "Aivu delay has no actual played scene timestamp: " + scene.Id);
                var tooSoon = Program.Copy(ready); tooSoon.Hour = anchors.Max(k => ready.Times[k]) + scene.DelayHours - 1;
                check(!Rules.Available(story, scene, tooSoon), "Aivu ignores the exact waiting boundary.");
            }
        }
    }

    private static List<Snapshot> DistinctForFuture(IEnumerable<Snapshot> states, IEnumerable<Scene> future)
    {
        var flags = new HashSet<string>();
        foreach (var scene in future)
        {
            flags.UnionWith(scene.Requires); flags.UnionWith(scene.Forbids);
            foreach (var choice in scene.Nodes.SelectMany(n => n.Choices))
            { flags.UnionWith(choice.Requires); flags.UnionWith(choice.Forbids); }
        }
        return states.GroupBy(s => string.Join("|", s.Flags.Where(flags.Contains).OrderBy(f => f)))
            .Select(g => g.First()).ToList();
    }
}
