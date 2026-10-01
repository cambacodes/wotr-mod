using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class NocticulaAcquiredHarborTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string marker = ".acquired.";
        var acquired = story.Scenes.Where(s => s.Id.Contains(marker)).ToArray();
        if (acquired.Length == 0) return;
        var original = story.Scenes.Where(s => s.Relationship == "nocticula" && !s.Id.Contains(marker)
                                               && !s.Id.StartsWith("nocticula.trickster.", StringComparison.Ordinal)
                                               // PP4 pacing beats (pacing_pp4.py; PacingPP4Tests) are not the harbor campaign.
                                               && !s.Id.StartsWith("nocticula.early.", StringComparison.Ordinal)
                                               && !s.Id.StartsWith("nocticula.ch4.", StringComparison.Ordinal)).ToArray();
        var visits = original.Where(s => s.Owner == "Memory").ToArray();
        var endings = acquired.Where(s => s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        check(acquired.Length == 102 && visits.Length == 24 && original.Length == 32,
            "Acquired harbor delivery families or original campaign changed.");
        check(original.All(s => s.Forbids.Contains("noct.join.harbor_variant_ready")),
            "Original harbor export lacks mutual exclusion with the acquired family.");
        var native = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.SeenCues.Keys)
            .Concat(story.SelectedAnswers.Keys).Concat(story.CompletedQuests.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();
        string[] bridgeFacts = { "noct.join.harbor_variant_ready", "noct.join.recurring_dreams_accepted",
            "noct.join.exit_demonstrated", "noct.join.a_chosen_shore_done" };
        string[] decisions = { "noct.chosen_company", "noct.chosen_alliance", "noct.chosen_limit" };
        string[] priorIds = { "noct.acq.the_missing_line", "noct.acq.her_hand", "noct.acq.borrowed_signature",
            "noct.acq.the_paid_address", "noct.acq.the_retained_copy", "noct.acq.an_answer_of_her_own",
            "noct.join.an_unfinished_map", "noct.join.the_room_she_makes", "noct.join.a_chosen_shore" };
        var prior = priorIds.Select(id => story.Scenes.Single(s => s.Id == id)).ToArray();
        var entries = story.Scenes.Where(s => s.Id.StartsWith("noct.acq.audience_", StringComparison.Ordinal)).ToArray();
        var reached = acquired.ToDictionary(s => s.Id, _ => new HashSet<string>());
        var rollTargets = acquired.ToDictionary(s => s.Id, _ => new HashSet<string>());
        var finals = new Dictionary<string, Snapshot>();
        int joins = 0, traversals = 0, closures = 0, postponements = 0, giftProbes = 0, endingProbes = 0;

        string Alias(Scene scene) => scene.Id.Substring(0, scene.Id.IndexOf(marker, StringComparison.Ordinal));
        IEnumerable<string> Reads(Scene scene) => scene.Requires.Concat(scene.Forbids).Concat(scene.RequiresAny)
            .Concat(scene.RequiresAnyGroups.SelectMany(g => g))
            .Concat(scene.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids)));
        List<Snapshot> Reduce(IEnumerable<Snapshot> states, IEnumerable<Scene> future)
        {
            var used = future.SelectMany(Reads).Concat(native).Concat(decisions).ToHashSet();
            // Keep an actual played state, including timestamps; only future-equivalent witnesses are merged.
            return states.GroupBy(s => s.Hour + ":" + string.Join("|", s.Flags.Where(used.Contains).OrderBy(f => f)))
                .Select(g => g.First()).ToList();
        }
        void Preserved(Snapshot before, Snapshot after)
        {
            check(before.Flags.IsSubsetOf(after.Flags), "Acquired harbor removed existing history or another romance.");
            check(before.Flags.Where(native.Contains).ToHashSet().SetEquals(after.Flags.Where(native.Contains)),
                "Acquired harbor writes native state.");
            check(before.AvailableContacts.SetEquals(after.AvailableContacts), "Dream manufactures a physical contact.");
        }
        foreach (var scene in acquired)
        {
            string alias = Alias(scene);
            check(scene.Forbids.Contains(alias), "Acquired scene permits replay after shared completion: " + scene.Id);
            foreach (var choice in scene.Nodes.SelectMany(n => n.Choices))
            {
                bool terminal = !choice.Abort && choice.Check == null && string.IsNullOrEmpty(choice.Next);
                check(choice.Set.Contains(alias) == terminal, "Shared completion is not terminal-only: " + scene.Id);
                check(choice.Revive == null && choice.Set.All(f => !native.Contains(f)), "Acquired choice changes native state.");
            }
        }
        string[][] histories = {
            Array.Empty<string>(), new[] { "noct.gift" },
            new[] { "noct.parent_rejected" }, new[] { "noct.parent_rejected", "noct.gift" },
            new[] { "noct.parent_active", "noct.acq.original_gift_completed" },
            new[] { "noct.parent_active", "noct.acq.original_gift_completed", "noct.acq.gift_renewed" }
        };
        foreach (var history in histories)
        {
            var initial = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            initial.Flags.UnionWith(new[] { "trickster", "noct.acq.audience_question", "seelah.committed", "arueshalae.committed" });
            initial.Flags.UnionWith(history);
            var entry = entries.Where(s => Rules.Available(story, s, initial)).ToArray();
            check(entry.Length == 1, "Acquired harbor fixture lacks a unique native-history entry.");
            var states = Program.Walk(entry.Single(), initial).Where(s => !s.Has("noct.acq.closed")).ToList();
            // These two native Council witnesses are the only externally supplied acquisition boundary.
            foreach (var state in states)
                state.Flags.UnionWith(new[] { "noct.acq.council_disclosed", "noct.socoth_plan_exposed" });
            foreach (var scene in prior)
            {
                var next = new List<Snapshot>();
                foreach (var before in states)
                {
                    var ready = Program.Copy(before); ready.Hour += scene.DelayHours;
                    check(Rules.Available(story, scene, ready), "Actual acquisition cannot advance: " + scene.Id);
                    next.AddRange(Program.Walk(scene, ready).Where(s => s.Has(scene.Id)
                        && !s.Has("noct.acq.closed") && !s.Has("noct.join.closed")));
                }
                states = next;
            }
            check(states.Count == 216, "Actual opening, concession and bridge no longer yield 216 joins per native history.");
            joins += states.Count;
            states = Reduce(states, acquired);
            string family = history.Contains("noct.parent_rejected") ? "refused"
                : history.Contains("noct.parent_active") ? "prior" : "new";
            foreach (var state in states)
                check(bridgeFacts.All(state.Has) && state.Has("noct.join.history_" + family), "Bridge did not earn the selected acquired history.");
            for (int index = 0; index < visits.Length; index++)
            {
                var donor = visits[index];
                var variants = acquired.Where(s => Alias(s) == donor.Id).ToArray();
                var next = new List<Snapshot>();
                foreach (var before in states)
                {
                    var ready = Program.Copy(before); ready.Hour += donor.DelayHours;
                    var available = variants.Where(s => Rules.Available(story, s, ready)).ToArray();
                    check(available.Length == 1, "Played acquired history lacks one delivery: " + donor.Id);
                    var scene = available.Single();
                    check(scene.Id.Contains(marker + family), "Acquired delivery borrowed a different native history.");
                    check(!Rules.Available(story, donor, ready), "Original and acquired harbor overlap.");
                    foreach (string prerequisite in bridgeFacts.Concat(new[] { "trickster", "noct.acq.renewed_agreement" }))
                    {
                        var missing = Program.Copy(ready); missing.Flags.Remove(prerequisite);
                        check(!variants.Any(s => Rules.Available(story, s, missing)), "Acquired harbor bypasses " + prerequisite);
                    }
                    foreach (string blocker in new[] { "noct.closed", "noct.dead", "noct.acq.closed", "noct.join.closed", "noct.acq.council_fight" })
                    {
                        var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                        check(!variants.Any(s => Rules.Available(story, s, blocked)), "Acquired harbor ignores " + blocker);
                    }
                    if (donor.Id == "noct.her_own_face")
                    for (int gift = 0; gift < 4; gift++)
                    {
                        // Explicit native Gift-transition probes applied to a played face-ready witness.
                        var current = Program.Copy(ready);
                        current.Flags.Remove("noct.gift"); current.Flags.Remove("noct.acq.gift_renewed");
                        if ((gift & 1) != 0) current.Flags.Add("noct.gift");
                        if ((gift & 2) != 0) current.Flags.Add("noct.acq.gift_renewed");
                        var faces = variants.Where(s => Rules.Available(story, s, current)).ToArray();
                        string suffix = (gift & 2) != 0 ? "renewed" : gift == 1 ? "original" : "absent";
                        check(faces.Length == 1 && faces[0].Id.EndsWith("." + suffix, StringComparison.Ordinal), "Current Gift delivery precedence is wrong.");
                        foreach (var result in Program.Walk(faces.Single(), current))
                        {
                            Preserved(current, result);
                            check(result.Has(donor.Id), "Gift-specific face lacks shared completion.");
                            result.Flags.Add("noct.gift"); result.Flags.Add("noct.acq.gift_renewed");
                            check(!variants.Any(s => Rules.Available(story, s, result)), "Changing Gift replays a completed face scene.");
                        }
                        giftProbes++;
                    }
                    foreach (var result in Program.Walk(scene, ready, (node, partial) =>
                    {
                        reached[scene.Id].Add(node);
                        foreach (var choice in scene.Nodes.Single(n => n.Id == node).Choices)
                            if (choice.Check != null && Rules.Match(choice.Requires, choice.Forbids, partial))
                                rollTargets[scene.Id].UnionWith(Rules.NextNodes(choice));
                        check(!partial.Has(donor.Id), "Shared completion appeared before terminal choice: " + scene.Id);
                        check(Rules.ContactAvailable(story, scene, partial), "Played acquired scene loses remote contact.");
                    }))
                    {
                        traversals++;
                        Preserved(ready, result);
                        if (result.Has("noct.closed"))
                        {
                            closures++;
                            var later = Program.Copy(result); later.Hour += 1000;
                            check(!later.Has("noct.complete") && !acquired.Any(s => Rules.Available(story, s, later)),
                                "Closed acquired undertaking reopens or receives a completed ending.");
                            continue;
                        }
                        if (!result.Has(scene.Id))
                        {
                            postponements++;
                            check(donor.Id == "noct.unlit_quay" && result.Flags.SetEquals(ready.Flags)
                                && result.Times.Count == ready.Times.Count && ready.Times.All(p => result.Times.TryGetValue(p.Key, out int t) && t == p.Value)
                                && Rules.Available(story, scene, result), "Postponement consumes acquired acceptance or cannot retry.");
                            continue;
                        }
                        check(result.Has(donor.Id) && result.Times[donor.Id] == ready.Hour, "Acquired visit lacks timed shared completion.");
                        // In-memory restoration tests Rules persistence policy, not Unity save serialization.
                        var restored = Program.Copy(result); restored.Hour += 1000;
                        check(!variants.Any(s => Rules.Available(story, s, restored)) && !Rules.Available(story, donor, restored),
                            "Restored completion permits original or acquired replay.");
                        next.Add(result);
                    }
                }
                var laterIds = visits.Skip(index + 1).Select(s => s.Id).ToHashSet();
                states = Reduce(next, acquired.Where(s => laterIds.Contains(Alias(s))).Concat(endings));
                check(states.Count > 0, "Acquired undertaking has no continuing path after " + donor.Id);
            }
            foreach (var state in states)
            {
                check(state.Has("noct.complete") && decisions.Count(state.Has) == 1, "Acquired harbor lacks one final relationship decision.");
                finals[family + "/" + decisions.Single(state.Has)] = state;
            }
        }
        check(finals.Count == 9 && joins == 1296 && closures > 0 && postponements > 0 && giftProbes > 0,
            "Acquired harbor omitted a history, final decision, refusal, postponement, or Gift state.");
        foreach (var pair in finals)
        {
            var resting = Program.Copy(pair.Value);
            resting.Hour += 24;
            var harborOnly = new Story { Scenes = original.Concat(acquired).ToList(), Relationships = story.Relationships };
            var next = Rules.NextRemote(harborOnly, resting);
            check(next == null || !next.Owner.EndsWith("Epilogue", StringComparison.Ordinal),
                "Rest after earned harbor completion schedules an epilogue: " + next?.Id);
        }
        foreach (var pair in finals)
        for (int mask = 0; mask < 16; mask++)
        {
            // External endgame outcome fixtures; this does not claim native death or ascension was played.
            var state = Program.Copy(pair.Value);
            string[] outcomes = { "noct.dead", "inhuman", "ascended", "sacrifice" };
            for (int bit = 0; bit < outcomes.Length; bit++) if ((mask & (1 << bit)) != 0) state.Flags.Add(outcomes[bit]);
            var available = endings.Where(s => s.Owner == "Epilogue" && Rules.Available(story, s, state)).ToArray();
            string expected = state.Has("noct.dead") ? "death" : state.Has("inhuman") ? "changed"
                : state.Has("ascended") ? "ascent" : state.Has("sacrifice") ? "sacrifice"
                : state.Has("noct.chosen_company") ? "company" : state.Has("noct.chosen_alliance") ? "alliance" : "limit";
            check(available.Length == 1 && available[0].Id == "noct.ending_" + expected + marker + pair.Key.Split('/')[0],
                "Acquired ending overlaps, loses history, or contradicts outcome precedence.");
            check(!original.Any(s => s.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && Rules.Available(story, s, state)),
                "Acquired completion exposes an original-family ending.");
            foreach (var result in Program.Walk(available.Single(), state))
            {
                Preserved(state, result);
                check(result.Has(Alias(available[0])) && !Rules.Available(story, available[0], result), "Acquired ending lacks shared completion.");
            }
            state.Flags.Remove("noct.complete");
            check(!endings.Any(s => Rules.Available(story, s, state)), "Unfinished acquired harbor receives an ending.");
            endingProbes++;
        }
        foreach (var donor in visits)
        foreach (string family in new[] { "new", "refused", "prior" })
            check(acquired.Where(s => Alias(s) == donor.Id && s.Id.Contains(marker + family)).Any(s => reached[s.Id].Count > 0),
                "A history skipped a campaign visit: " + donor.Id + "/" + family);
        foreach (var scene in acquired)
            check(rollTargets[scene.Id].IsSubsetOf(reached[scene.Id]), "An eligible check lacks both played callbacks: " + scene.Id);
        foreach (string family in new[] { "new", "refused", "prior" })
            check(new[] { "first_passengers", "first_profit" }.All(reached["noct.unlit_quay.acquired." + family].Contains),
                "Acquired harbor skipped an earned bridge question: " + family);
        Console.WriteLine($"Acquired harbor: 6 native histories, {joins} played joins, 24 visits per history, {traversals} projected local outcomes, {closures} closures, {postponements} postponements, {giftProbes} Gift probes, {endingProbes} ending probes. Native execution and disk saves remain unverified.");
    }
}
