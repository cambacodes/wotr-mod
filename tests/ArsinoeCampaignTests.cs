using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class ArsinoeCampaignTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        string[] chain = { "arsinoe_after_rain", "arsinoe_two_doors", "arsinoe_a_stone_in_hand",
            "arsinoe_the_first_cart", "arsinoe_what_she_asks", "arsinoe_where_she_stays", "arsinoe_the_window_opens" };
        var departure = story.Scenes.Single(s => s.Id == "arsinoe_before_the_road");
        var physical = chain.Select(id => story.Scenes.Single(s => s.Id == id)).Append(departure).ToArray();
        var visited = physical.ToDictionary(s => s.Id, _ => new HashSet<string>());
        var endings = story.Scenes.Where(s => s.Id.StartsWith("arsinoe_ending_", StringComparison.Ordinal)).ToArray();
        var native = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SelectedAnswers.Keys).Concat(story.SeenCues.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();
        check(!physical.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).Any(native.Contains),
            "Arsinoe campaign fabricates a native outcome.");
        var roll = physical.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Single(c => c.Check != null);
        check(roll.Check!.Skill == "SkillPerception" && roll.Check.DC == 24 && roll.Check.CommanderOnly,
            "Arsinoe's inspection uses the wrong actor or check.");
        check(roll.Set.Length == 0 && roll.Check.Success == "seam" && roll.Check.Failure == "glare",
            "Arsinoe awards a check outcome before the result is acknowledged.");

        foreach (string pace in new[] { "arsinoe.courting", "arsinoe.slow", "arsinoe.friendship" })
        foreach (int chapter in new[] { 3, 5 })
        foreach (bool trickster in new[] { false, true })
        {
            // This is a released predecessor fixture, not a claim to replay all eleven earlier visits.
            var predecessor = story.Scenes.Single(s => s.Id == "arsinoe_the_unprofitable_hour");
            var seed = new Snapshot { Chapter = chapter, Area = predecessor.Areas.Single(), Hour = 1000 };
            seed.Flags.UnionWith(predecessor.Requires);
            seed.Flags.UnionWith(new[] { pace, "arsinoe.interest_games", "lann.committed", "arueshalae.committed" });
            if (trickster) seed.Flags.Add("trickster");
            seed.AvailableContacts.Add(predecessor.ContactUnit!);
            check(Rules.Available(story, predecessor, seed), "Released Arsinoe predecessor fixture is unavailable.");
            var states = Distinct(Program.Walk(predecessor, seed).Where(s => s.Has("arsinoe.continuation_kept")));
            var allFinals = new List<Snapshot>();
            foreach (var scene in physical.Take(chain.Length))
            {
                var next = new List<Snapshot>();
                foreach (var prior in states)
                {
                    if (prior.Has("arsinoe.closed")) continue;
                    var ready = Program.Copy(prior);
                    if (scene.Id == "arsinoe_where_she_stays") ready.Chapter = 5;
                    ready.Hour += scene.DelayHours;
                    check(Rules.Available(story, scene, ready), "Played campaign stranded at " + scene.Id);
                    check(scene.ContactUnit == "a609ed9b2205d034bb3bb04d2a255681" && scene.AnswerLists.SequenceEqual(new[] { "ecaf5cfe8087a4f45a2269974f4885c9" }),
                        "Campaign changes the verified Arsinoe contact.");
                    foreach (string blockedFlag in new[] { "arsinoe.closed", "arsinoe.victims_revived", "swarm", "true_lich" })
                    {
                        var blocked = Program.Copy(ready); blocked.Flags.Add(blockedFlag);
                        check(!Rules.Available(story, scene, blocked), "Arsinoe ignores " + blockedFlag);
                        if (blockedFlag != "arsinoe.closed")
                            check(!Rules.ContactAvailable(story, scene, blocked), "Arsinoe continues during native suppression.");
                    }
                    foreach (string required in scene.Requires)
                    {
                        var missing = Program.Copy(ready); missing.Flags.Remove(required);
                        check(!Rules.Available(story, scene, missing), "Campaign ignores required history " + required);
                    }
                    var displaced = Program.Copy(ready); displaced.Area = "not_drezen";
                    check(!Rules.Available(story, scene, displaced), "Arsinoe starts outside the capital.");
                    displaced.Area = ready.Area; displaced.Chapter = 4;
                    check(!Rules.Available(story, scene, displaced), "Physical Arsinoe visit starts in the Abyss.");
                    var results = Program.Walk(scene, ready, (page, partial) =>
                    {
                        visited[scene.Id].Add(page);
                        check(partial.Flags.SetEquals(ready.Flags), "Campaign writes unacknowledged history at " + scene.Id + "/" + page);
                        var interrupted = Program.Copy(partial); interrupted.AvailableContacts.Clear();
                        check(!Rules.ContactAvailable(story, scene, interrupted), "Campaign ignores lost native contact.");
                        interrupted.AvailableContacts.Add(scene.ContactUnit!);
                        check(Rules.Available(story, scene, interrupted), "An interrupted page cannot be replayed.");
                        if (page == "possibility" || page == "after_possibility") check(trickster, "A non-Trickster uses the future-stone intervention.");
                        if (scene.Id == "arsinoe_what_she_asks" && (page == "lasting" || page == "open"))
                            check(pace != "arsinoe.friendship", "Friendship is silently reopened as romance.");
                        if (scene.Id == "arsinoe_the_window_opens" && page == "night")
                            check(partial.Has("arsinoe.campaign_lover"), "Friendship or slow pace receives a sexual invitation.");
                        if (scene.Id == "arsinoe_where_she_stays" && page == "departure")
                            check(partial.Has("arsinoe.departure_kept"), "Skipped farewell is treated as played history.");
                    });
                    foreach (var result in results)
                    {
                        check(ready.Flags.IsSubsetOf(result.Flags) && result.Has("lann.committed") && result.Has("arueshalae.committed"),
                            "Arsinoe erases history or another romance.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags) && result.Times.Count == ready.Times.Count, "Postponement manufactures a visit.");
                            continue;
                        }
                        check(!Rules.Available(story, scene, result), "Completed Arsinoe scene reopens.");
                        if (result.Has("arsinoe.closed"))
                        {
                            check(result.Has("arsinoe.parted") && !result.Has("arsinoe.committed"), "Parting invents a commitment.");
                            check(endings.Count(e => e.Owner == "Epilogue" && Rules.Available(story, e, result)) == 1,
                                "Parting has a missing or conflicting ordinary ending.");
                            continue;
                        }
                        next.Add(result);
                        if (scene.Id == "arsinoe_what_she_asks")
                        {
                            check(endings.Count(e => e.Owner == "Epilogue" && Rules.Available(story, e, result)) == 1,
                                "The chosen pace or promise lacks a truthful interim ending.");
                            if (chapter == 3)
                            {
                                check(Rules.Available(story, departure, result), "Chapter three cannot play its optional departure.");
                                next.AddRange(Program.Walk(departure, result, (page, partial) =>
                                {
                                    visited[departure.Id].Add(page);
                                    check(partial.Flags.SetEquals(result.Flags), "Departure writes a gift before it is accepted.");
                                }));
                            }
                            else check(!Rules.Available(story, departure, result), "Fresh chapter five invents a pre-Abyss goodbye.");
                        }
                    }
                }
                states = Distinct(next);
                check(states.Count > 0, "No Arsinoe campaign state remains after " + scene.Id);
            }
            allFinals.AddRange(states);
            foreach (var result in allFinals)
            {
                check(result.Has("arsinoe.last_evening_kept"), "Full played route has no final evening.");
                check(endings.Count(e => e.Owner == "Epilogue" && Rules.Available(story, e, result)) == 1,
                    "Complete Arsinoe history has missing/conflicting ordinary epilogues.");
                check(!result.Has("arsinoe.stone_possibility") || trickster, "Ordinary path records a fate intervention.");
                if (pace == "arsinoe.friendship") check(!result.Has("arsinoe.campaign_lover") && !result.Has("arsinoe.night_shared"), "Friendship becomes intimacy.");
                if (chapter == 5) check(!result.Has("arsinoe.departure_kept"), "Late campaign invents early departure.");
                if (!result.Has("arsinoe.campaign_lover")) continue;
                foreach (string special in new[] { "ascended", "sacrifice", "swarm", "true_lich" })
                {
                    var changed = Program.Copy(result); changed.Flags.Add(special);
                    check(endings.Count(e => e.Owner == "Epilogue" && Rules.Available(story, e, changed)) == 1,
                        "Arsinoe has conflicting exceptional endings: " + special);
                }
                // Sol INT/HOW (2026-09-30): the native Trickster punchline undoes the sacrifice (trickster.commander_back,
                // GrandFinal Answer_0011 + Epilogues Cue_0564). A surviving Commander is never mourned, with or without Last Call.
                foreach (string key in new[] { "ending.trickster", "ending.trickster_full", "ending.trickster_allplanes", "ending.trickster_allplanes_fw" })
                foreach (bool lastCall in new[] { false, true })
                {
                    var back = Program.Copy(result);
                    back.Flags.UnionWith(new[] { "sacrifice", "trickster.ever", key });
                    if (lastCall) back.Flags.Add("lastcall.active");
                    Rules.Complete(story, back);
                    var open = endings.Where(e => e.Owner == "Epilogue" && Rules.Available(story, e, back)).ToArray();
                    check(back.Has("trickster.commander_back") && open.Length == 1 && open[0].Id != "arsinoe_ending_sacrifice",
                        "A Trickster back from the sacrifice is mourned, or has no single living ending: " + key + (lastCall ? " +Last Call" : ""));
                }
                var mourned = Program.Copy(result);
                mourned.Flags.Add("sacrifice");
                Rules.Complete(story, mourned);
                var mourning = endings.Where(e => e.Owner == "Epilogue" && Rules.Available(story, e, mourned)).ToArray();
                check(!mourned.Has("trickster.commander_back") && mourning.Length == 1 && mourning[0].Id == "arsinoe_ending_sacrifice",
                    "A genuine sacrifice loses its mourning page.");
            }
            check(states.Any(s => !s.Has("arsinoe.night_shared")), "Campaign forces a night together.");
            if (pace != "arsinoe.friendship") check(states.Any(s => s.Has("arsinoe.night_shared")), "Romantic path cannot choose a night together.");
            if (pace == "arsinoe.slow") check(states.Any(s => s.Has("arsinoe.slow_developed")), "Slow pace is forced to escalate.");
        }
        foreach (var scene in physical)
            check(visited[scene.Id].SetEquals(scene.Nodes.Select(n => n.Id)), "Unreached campaign page: " + scene.Id);
    }

    private static List<Snapshot> Distinct(IEnumerable<Snapshot> states) => states
        .GroupBy(s => string.Join("|", s.Flags.OrderBy(f => f, StringComparer.Ordinal)))
        .Select(g => g.First()).ToList();
}
