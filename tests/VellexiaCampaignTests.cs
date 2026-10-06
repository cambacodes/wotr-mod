using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class VellexiaCampaignTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string actor = "a32a07903e428d34cb0e98a804d40569";
        const string nexus = "7847c3e3537104f4694167af0b9fcd0e";
        const string drezen = "2570015799edf594daf2f076f2f975d8";
        var openingIds = new[] { "unfinished_likeness", "second_painter", "price_of_novelty", "two_observers", "unadvertised_hour", "a_question_kept" };
        var newIds = new[] { "the_unused_reply", "the_price_of_tomorrow", "the_second_invitation", "the_claim_before_the_event", "the_clerks_own_price", "the_wager_with_an_edge", "an_hour_that_counts", "the_question_after_business", "the_voice_after_the_abyss", "two_unremarkable_pleasures", "the_cover_before_the_battle" };
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "vellexia." + id);
        var chain = openingIds.Concat(newIds).Select(Find).ToArray();
        var endings = story.Scenes.Where(s => s.Id.StartsWith("vellexia.ending_", StringComparison.Ordinal)).ToArray();
        var reached = new HashSet<string>();
        var produced = new HashSet<string>();
        var final = new List<Snapshot>();
        var latePartial = new List<Snapshot>();
        var localReady = new List<Snapshot>();
        var remoteReady = new List<Snapshot>();
        var bound = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).Distinct().ToArray();
        var groups = new[] {
            new[] { "clerk_terms", "shared_account" }, new[] { "method_first", "challenge_first" },
            new[] { "named_sample", "limited_sample" }, new[] { "published_accounts", "drawn_order", "commander_order" },
            new[] { "account_published", "wager_won", "wager_lost", "fate_hour" },
            new[] { "renewed_lovers", "renewed_slow", "renewed_company" },
            new[] { "farewell_lovers", "farewell_friends", "farewell_slow" }
        }.Select(g => g.Select(f => "vellexia." + f).ToArray()).ToArray();

        // Native dated quest progression is a fixture input between the played local and remote visits.
        // Every authored prerequisite comes from an actual earlier player choice. Q11: each native ending of the affair
        // (the bored dismissal Cue_0076, the mercy Cue_0098 after the final fight, the passionate farewell Cue_0106) is played.
        var nativeEndings = new[] { new[] { "vellexia.dismissed_native" }, new[] { "vellexia.spared", "vellexia.final_fight" }, new[] { "vellexia.farewell" } };
        foreach (var nativeEnding in nativeEndings)
        foreach (bool trickster in new[] { false, true })
        foreach (bool giftSeen in new[] { false, true })
        {
            var start = new Snapshot { Chapter = 4, Hour = 1000, Area = chain[0].Areas.Single() };
            start.AvailableContacts.Add(actor);
            start.Flags.UnionWith(new[] { "vellexia.greeted", "jerribeth.committed", "wenduag.committed" });
            if (trickster) start.Flags.Add("trickster");
            var states = new List<Snapshot> { start };
            for (int index = 0; index < chain.Length; index++)
            {
                var scene = chain[index];
                var next = new List<Snapshot>();
                foreach (var input in states)
                {
                    var ready = Program.Copy(input);
                    ready.Hour += scene.DelayHours + 24;
                    if (index == 8)
                    {
                        ready.Flags.UnionWith(new[] { "vellexia.arena_invited", "vellexia.native_finished" });
                        ready.Flags.UnionWith(nativeEnding);
                        Rules.Complete(story, ready);   // fight_survived (spared OR returned) lifts the final fight
                        if (giftSeen) ready.Flags.Add("vellexia.coin_given");
                        ready.Area = nexus;
                        ready.AvailableContacts.Clear();
                    }
                    if (index == 9) { ready.Chapter = 5; ready.Area = drezen; }   // Q11: only the second invitation is a Chapter 4 call
                    check(Program.CurrentAvailable(story, scene, ready), "Vellexia earned predecessor cannot enter " + scene.Id);
                    if (index == 6) localReady.Add(Program.Copy(ready));
                    if (index >= 8) remoteReady.Add(Program.Copy(ready));
                    foreach (var result in Program.Walk(scene, ready, (page, partial) =>
                    {
                        if (index >= 6) reached.Add(scene.Id + "/" + page);
                        check(partial.Flags.SetEquals(ready.Flags), "Vellexia interrupted scene records premature choice flags.");
                        check(Rules.ContactAvailable(story, scene, partial), "Vellexia playable page rejects actual contact.");
                        if (index >= 6)
                        {
                            var killed = Program.Copy(partial); killed.Flags.Add("vellexia.dead");
                            check(!Program.CurrentAvailable(story, scene, killed), "Vellexia entry survives native death.");
                            if (scene.ContactUnit != null) check(!Rules.ContactAvailable(story, scene, killed), "Vellexia local page survives native death.");
                            if (scene.Owner == "Memory")
                                check(scene.Remote && scene.ContactUnit == null && partial.AvailableContacts.Count == 0,
                                    "Vellexia correspondence manufactures a physical actor.");
                            if (page == "fate_offer" || page == "fate" || page == "fate_end")
                                check(trickster && giftSeen && partial.Has("vellexia.commander_order"), "Vellexia fate option lacks native gift history/path/played wager choice.");
                            if (scene.Id.EndsWith("the_price_of_tomorrow") && new[] { "touch", "kiss", "hand" }.Contains(page))
                                check(partial.Has("vellexia.courting"), "Vellexia hand/kiss assumes unchosen initial romance.");
                            if (scene.Id.EndsWith("the_cover_before_the_battle") && page == "new_terms")
                                check(partial.Has("vellexia.renewed_slow"), "Vellexia farewell turns settled friendship into a romance invitation.");
                        }
                    }))
                    {
                        foreach (var flag in bound) check(result.Has(flag) == ready.Has(flag), "Vellexia writes native history: " + flag);
                        foreach (var flag in Program.PersistentFlags(story, ready)) check(result.Has(flag), "Vellexia erases earlier history: " + flag);
                        check(result.AvailableContacts.SetEquals(ready.AvailableContacts), "Vellexia creates a physical actor.");
                        check(result.Has("jerribeth.committed") && result.Has("wenduag.committed"), "Vellexia changes unrelated romances.");
                        foreach (var group in groups) check(group.Count(result.Has) <= 1, "Vellexia incompatible outcomes overlap.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags), "Vellexia deferral writes an outcome.");
                            check(result.Times.OrderBy(x => x.Key).SequenceEqual(ready.Times.OrderBy(x => x.Key)), "Vellexia deferral changes time history.");
                            continue;
                        }
                        check(!Program.CurrentAvailable(story, scene, result), "Vellexia finished visit replays.");
                        produced.UnionWith(result.Flags);
                        if (index >= 7) latePartial.Add(Program.Copy(result));
                        if (index == chain.Length - 1) final.Add(result);
                        if (!result.Has("vellexia.closed")) next.Add(result);
                    }
                }
                // Retain a played witness for every combination read by later choices and endings.
                // Discarding redundant witnesses does not synthesize or remove flags from any history.
                var future = chain.Skip(index + 1).Concat(endings).ToArray();
                var reads = future.SelectMany(s => s.Requires.Concat(s.RequiresAny).Concat(s.Forbids)
                    .Concat(s.Nodes.SelectMany(n => n.Choices.SelectMany(c => c.Requires.Concat(c.Forbids))))).ToHashSet();
                states = next.GroupBy(s => string.Join("|", s.Flags.Where(reads.Contains).OrderBy(f => f))).Select(g => g.First()).ToList();
            }
        }
        foreach (var scene in chain.Skip(6))
        foreach (var page in scene.Nodes)
            check(reached.Contains(scene.Id + "/" + page.Id), "Vellexia unplayed authored page " + scene.Id + "/" + page.Id);
        foreach (var flag in groups.SelectMany(x => x)) check(produced.Contains(flag), "Vellexia unearned outcome " + flag);
        var local = Find("the_unused_reply");
        foreach (var ready in localReady.Take(4))
        {
            var missing = Program.Copy(ready); missing.AvailableContacts.Clear();
            check(!Program.CurrentAvailable(story, local, missing), "Vellexia initial token offered without native manor actor.");
            foreach (var flag in new[] { "vellexia.arena_invited", "vellexia.native_finished", "vellexia.dead", "vellexia.early_fight" })
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag);
                check(!Program.CurrentAvailable(story, local, blocked), "Vellexia token bypasses native local window: " + flag);
            }
        }
        foreach (var ready in remoteReady)
        {
            var scene = chain.Skip(8).First(s => Program.CurrentAvailable(story, s, ready));
            foreach (var flag in new[] { "vellexia.dead", "vellexia.early_fight", "vellexia.final_fight", "vellexia.mirrored", "vellexia.native_coercion", "inhuman", "vellexia.closed" })
            {
                if (flag == "vellexia.final_fight" && ready.Has("vellexia.spared")) continue;   // the mercy follows the final fight
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag);
                check(!Program.CurrentAvailable(story, scene, blocked), "Vellexia remote contact bypasses native/history blocker: " + flag);
            }
            // The two evenings after the return call Require only their predecessor beat (a Trickster return reaches them
            // without the native dismissal); the predecessor itself is gated on the dismissal, so the old path is unchanged.
            var ended = new[] { "vellexia.dismissed_native", "vellexia.spared", "vellexia.farewell" };
            bool nativeGated = scene.RequiresAnyGroups.Any(g => ended.All(g.Contains));
            var originalRequires = scene.Requires.Where(k => !k.EndsWith(".present_now", StringComparison.Ordinal) && !k.EndsWith(".reachable_by_letter", StringComparison.Ordinal));
            check(nativeGated && scene.Requires.Contains("vellexia.native_finished") || originalRequires.SequenceEqual(new[] { "vellexia.return_kept" })
                  || originalRequires.SequenceEqual(new[] { "vellexia.private_kept" }), "Vellexia remote conversation lost its native ending: " + scene.Id);
            if (nativeGated)
            {
                var unended = Program.Copy(ready); unended.Flags.ExceptWith(ended);
                check(!Program.CurrentAvailable(story, scene, unended), "Vellexia remote conversation assumes an unfinished native affair.");
                var unfinished = Program.Copy(ready); unfinished.Flags.Remove("vellexia.native_finished");
                check(!Program.CurrentAvailable(story, scene, unfinished), "Vellexia remote conversation assumes an unfinished native quest.");
            }
            else
                foreach (var flag in scene.Requires.Where(requiredKey => !requiredKey.EndsWith(".present_now", StringComparison.Ordinal) && !requiredKey.EndsWith(".reachable_by_letter", StringComparison.Ordinal)))
                {
                    var missing = Program.Copy(ready); missing.Flags.Remove(flag);
                    check(!Program.CurrentAvailable(story, scene, missing), "Vellexia evening skips its predecessor: " + flag);
                }
            var absent = Program.Copy(ready); absent.Area = "missing-area";
            check(!Program.CurrentAvailable(story, scene, absent), "Vellexia remote entry has no location constraint.");
        }
        IEnumerable<Scene> Ending(Snapshot state) => endings.Where(s => s.Owner == "Epilogue" && Program.CurrentAvailable(story, s, state));
        foreach (var state in final)
        {
            var result = Ending(state).ToArray();
            check(result.Length == 1, "Vellexia final outcome missing or ambiguous.");
            var suffix = state.Has("vellexia.closed") ? "closed" : state.Has("vellexia.farewell_lovers") ? "lovers" : state.Has("vellexia.farewell_friends") ? "friends" : "slow";
            check(result[0].Id == "vellexia.ending_" + suffix, "Vellexia ending contradicts actual final choice.");
        }
        var special = new[] { ("vellexia.dead", "dead"), ("vellexia.mirrored", "mirror"), ("vellexia.native_coercion", "coercion"), ("vellexia.final_fight", "hostility"), ("vellexia.early_fight", "hostility"), ("inhuman", "changed"), ("ascended", "ascent"), ("sacrifice", "sacrifice") };
        foreach (var state in latePartial.Where(s => !s.Has("vellexia.closed") && s.Has("vellexia.dismissed_native")))
        {
            check(Ending(state).Count() == 1, "Vellexia played partial history lacks a truthful outcome.");
            foreach (var (flag, suffix) in special)
            {
                var changed = Program.Copy(state); changed.Flags.Add(flag);
                var result = Ending(changed).ToArray();
                check(result.Length == 1 && result[0].Id == "vellexia.ending_" + suffix, "Vellexia special ending contradicts played history: " + flag);
                changed.Flags.Add("vellexia.dead");
                // Earned presence (rubric Binding context (3)): her death page has the Commander remembering her; beside an
                // unreturned sacrifice it does not play, and the native slides stand.
                if (flag == "sacrifice") check(!Ending(changed).Any(), "Vellexia's death page stages a living Commander after the sacrifice.");
                else check(Ending(changed).Single().Id == (flag == "vellexia.mirrored" ? "vellexia.ending_mirror" : "vellexia.ending_dead"), "Vellexia native mirror/death precedence is false.");
            }
        }
        check(Find("an_hour_that_counts").Nodes.Single(n => n.Id == "sealed").Choices.Any(c => c.Requires.Contains("vellexia.coin_given")), "Vellexia Trickster connection no longer reads historical gift.");
    }
}

