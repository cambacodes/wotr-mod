using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class NocticulaHarborJoinTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        string[] ids = { "noct.join.an_unfinished_map", "noct.join.the_room_she_makes", "noct.join.a_chosen_shore" };
        var bridge = story.Scenes.Where(s => ids.Contains(s.Id)).ToArray();
        if (bridge.Length == 0) return;
        check(bridge.Length == ids.Length, "Harbor bridge is only partially assembled.");
        bridge = ids.Select(id => bridge.Single(s => s.Id == id)).ToArray();
        var entries = story.Scenes.Where(s => s.Id.StartsWith("noct.acq.audience_", StringComparison.Ordinal)).ToArray();
        check(entries.Length == 3, "Harbor bridge requires all three actual acquisition entries.");
        string[] priorIds = {
            "noct.acq.the_missing_line", "noct.acq.her_hand", "noct.acq.borrowed_signature",
            "noct.acq.the_paid_address", "noct.acq.the_retained_copy", "noct.acq.an_answer_of_her_own"
        };
        var prior = priorIds.Select(id => story.Scenes.Single(s => s.Id == id)).ToArray();
        var harbor = story.Scenes.Single(s => s.Id == "noct.unlit_quay");
        var native = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.SeenCues.Keys)
            .Concat(story.SelectedAnswers.Keys).Concat(story.CompletedQuests.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();
        check(bridge.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).All(c => c.Revive == null
            && c.Set.All(f => f.StartsWith("noct.join.", StringComparison.Ordinal) && !native.Contains(f))),
            "Harbor bridge writes native aliases, a parent agreement, or actor recovery.");
        var reached = bridge.ToDictionary(s => s.Id, _ => new HashSet<string>());
        var closures = new int[3];
        int agreements = 0, completed = 0, arrivals = 0, exits = 0;
        string[][] histories = {
            Array.Empty<string>(), new[] { "noct.gift" },
            new[] { "noct.parent_rejected" }, new[] { "noct.parent_rejected", "noct.gift" },
            new[] { "noct.parent_active", "noct.acq.original_gift_completed" },
            new[] { "noct.parent_active", "noct.acq.original_gift_completed", "noct.acq.gift_renewed" }
        };
        string[] channelFlags = { "channel_provisional", "channel_letters_only", "channel_exposed", "channel_repaired", "sketch_surrendered" };
        string[] politicalFlags = { "closure_intent", "crossroads_proposed", "power_declared" };

        void Preserved(Snapshot before, Snapshot after)
        {
            check(before.Flags.Where(native.Contains).ToHashSet().SetEquals(after.Flags.Where(native.Contains)),
                "Harbor join changed native history.");
            check(after.Has("seelah.committed") && after.Has("arueshalae.committed"), "Harbor join removed another romance.");
            check(before.AvailableContacts.SetEquals(after.AvailableContacts), "Hosted dream manufactured a physical actor.");
            foreach (var flag in channelFlags)
                check(before.Has("noct.acq." + flag) == after.Has("noct.acq." + flag), "Bridge changed the earned channel: " + flag);
            check(after.Has("noct.acq.undertaking_held") && after.Has("noct.acq.renewed_agreement")
                && !after.Has("noct.acq.closed"), "Bridge erased the existing correspondence or retained undertaking.");
        }

        foreach (var history in histories)
        {
            var initial = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            initial.Flags.UnionWith(new[] { "trickster", "noct.acq.audience_question", "seelah.committed", "arueshalae.committed" });
            initial.Flags.UnionWith(history);
            var available = entries.Where(s => Rules.Available(story, s, initial)).ToArray();
            check(available.Length == 1, "Bridge fixture lacks a unique acquisition entry.");
            var states = Program.Walk(available.Single(), initial).Where(s => !s.Has("noct.acq.closed")).ToList();
            foreach (var requested in states)
            {
                var waited = Program.Copy(requested); waited.Hour += prior[0].DelayHours;
                check(!Rules.Available(story, prior[0], waited), "Remote contact bypasses native Council events.");
                foreach (var witness in new[] { "noct.acq.council_disclosed", "noct.socoth_plan_exposed" })
                {
                    var partial = Program.Copy(waited); partial.Flags.Add(witness);
                    check(!Rules.Available(story, prior[0], partial), "One native witness unlocks remote contact.");
                }
                // Only these genuine native events are supplied externally; channel and agreement effects are played below.
                requested.Flags.UnionWith(new[] { "noct.acq.council_disclosed", "noct.socoth_plan_exposed" });
            }
            foreach (var scene in prior)
            {
                var next = new List<Snapshot>();
                foreach (var previous in states)
                {
                    var ready = Program.Copy(previous); ready.Hour += scene.DelayHours;
                    check(Rules.Available(story, scene, ready), "Played acquisition/concession cannot advance: " + scene.Id);
                    next.AddRange(Program.Walk(scene, ready).Where(s => s.Has(scene.Id) && !s.Has("noct.acq.closed")));
                }
                states = next;
            }
            check(states.Count == 36, "Actual opening and concession did not produce 36 agreements for this history.");
            agreements += states.Count;
            for (int stage = 0; stage < bridge.Length; stage++)
            {
                var scene = bridge[stage];
                var next = new List<Snapshot>();
                foreach (var previous in states)
                {
                    check(!Rules.Available(story, scene, previous), "Bridge skipped its wait: " + scene.Id);
                    var ready = Program.Copy(previous); ready.Hour += scene.DelayHours;
                    check(Rules.Available(story, scene, ready), "Actual preceding choices cannot enter bridge: " + scene.Id);
                    foreach (var blocker in new[] { "noct.dead", "noct.acq.council_fight", "noct.acq.closed", "noct.closed", "noct.join.closed" })
                    {
                        var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                        check(!Rules.Available(story, scene, blocked), "Bridge ignores blocker: " + blocker);
                    }
                    var nonTrickster = Program.Copy(ready); nonTrickster.Flags.Remove("trickster");
                    check(!Rules.Available(story, scene, nonTrickster), "Bespoke bridge admits a non-Trickster.");
                    foreach (var result in Program.Walk(scene, ready, (node, partial) =>
                    {
                        reached[scene.Id].Add(node);
                        if (stage == 0 && node == "gift_present")
                            check(partial.Has("noct.gift") || partial.Has("noct.acq.gift_renewed"), "Gift acknowledgment invents patronage.");
                        if (stage == 0 && node == "gift_absent")
                            check(!partial.Has("noct.gift") && !partial.Has("noct.acq.gift_renewed"), "Giftless reply ignores a present Gift.");
                        if (stage == 1 && node == "exposure")
                            check(new[] { "channel_letters_only", "channel_exposed", "channel_repaired", "sketch_surrendered" }
                                .All(f => partial.Has("noct.acq." + f)), "Exposure callback borrows unearned damage or sketch surrender.");
                        if (stage == 1 && (node == "arrival" || node == "waking"))
                        {
                            check(partial.Has("noct.join.trial_accepted") && !partial.Has("noct.join.recurring_dreams_accepted")
                                && !partial.Has("noct.join.exit_demonstrated"), "Trial skips explicit permission or claims exit before its answer.");
                            if (node == "arrival") arrivals++; else exits++;
                        }
                        if (stage == 2 && node == "yes")
                            check(partial.Has("noct.join.recurring_dreams_accepted") && partial.Has("noct.join.harbor_variant_ready")
                                && !partial.Has("noct.join.a_chosen_shore_done"), "Final reply does not distinguish acceptance from terminal completion.");
                    }))
                    {
                        Preserved(ready, result);
                        check(!Rules.Available(story, scene, result), "Completed bridge scene repeats: " + scene.Id);
                        check(!Rules.Available(story, harbor, result), "Bridge bypasses the untouched original harbor's native agreement.");
                        if (result.Has("noct.join.closed"))
                        {
                            closures[stage]++;
                            check(result.Has("noct.join.letters_retained") && !result.Has("noct.join.harbor_variant_ready")
                                && !result.Has("noct.join.recurring_dreams_accepted"), "Refusal grants harbor readiness or loses retained letters.");
                            var later = Program.Copy(result); later.Hour += 1000;
                            check(bridge.All(s => !Rules.Available(story, s, later)), "Closed bridge reopens after waiting.");
                        }
                        else next.Add(result);
                    }
                }
                states = next;
            }
            check(states.Count == 216, "History lost a political intent, first question, or preceding outcome.");
            foreach (var final in states)
            {
                check(new[] { "trial_accepted", "exit_demonstrated", "recurring_dreams_accepted", "harbor_variant_ready", "a_chosen_shore_done" }
                    .All(f => final.Has("noct.join." + f)), "Completed bridge lacks an explicit permission or witnessed exit.");
                check(politicalFlags.Count(f => final.Has("noct.join." + f)) == 1
                    && final.Has("noct.join.first_question_passengers") != final.Has("noct.join.first_question_profit"),
                    "Completed bridge lacks exclusive political and investigation choices.");
                if (final.Has("noct.join.crossroads_proposed") || final.Has("noct.join.power_declared"))
                    check(final.Has("noct.join.endorsement_withheld"), "Ambitious proposal fabricates her endorsement.");
                completed++;
            }
        }
        check(agreements == 216 && completed == 1296 && closures.SequenceEqual(new[] { 216, 1296, 1296 }),
            "Assembled bridge path counts changed; inspect selected paths before changing expected counts.");
        check(arrivals == 648 && exits == 648, "Accepted trials do not all traverse the actual narrated exit.");
        foreach (var scene in bridge)
            check(reached[scene.Id].SetEquals(scene.Nodes.Select(n => n.Id)), "Bridge did not cover all nodes: " + scene.Id);
        Console.WriteLine("Nocticula harbor bridge: 6 native histories, 216 earned agreements, 1296 completed joins, 2808 closures, all 28 bridge nodes. Native dream execution and inventory controls remain unverified.");
    }
}
