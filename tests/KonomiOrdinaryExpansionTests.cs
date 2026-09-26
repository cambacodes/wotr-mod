using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KonomiOrdinaryExpansionTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "konomi." + id);
        var visits = new[] { "a_useful_supper", "the_upper_passage", "two_bad_prices", "the_trial_day", "a_name_beside_hers", "the_evening_she_kept" }.Select(Find).ToArray();
        var offer = Find("another_evening");
        var ordinary = Find("ordinary");
        var protectedFlags = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.StartedDialogs.Keys).Concat(story.SelectedAnswers.Keys)
            .Concat(new[] { "konomi.committed", "konomi.ordinary", "konomi.at_home", "konomi.farewell", "konomi.farewell_kept", "seelah.committed", "arueshalae.committed" }).Distinct().ToArray();
        var reached = new HashSet<string>();
        var outcomeFlags = new HashSet<string>();
        var replay = new Dictionary<string, (Scene Scene, Snapshot State)>();
        var pairs = new[] { new[] { "yard_precise", "yard_slow" }, new[] { "evening_trial", "morning_trial" },
            new[] { "trial_kissed", "trial_rested" }, new[] { "joint_offer", "circular_offer" }, new[] { "ordinary_night", "ordinary_walk" } };
        string Key(Snapshot s) => string.Join("|", s.Flags.OrderBy(f => f));
        void Preserve(Snapshot before, Snapshot after)
        {
            foreach (string flag in protectedFlags)
            {
                check(before.Has(flag) == after.Has(flag), "Konomi ordinary expansion changes existing history: " + flag);
                if (before.Times.TryGetValue(flag, out int hour))
                    check(after.Times.TryGetValue(flag, out int nextHour) && nextHour == hour, "Konomi ordinary expansion retimes history: " + flag);
            }
            foreach (var pair in pairs) check(pair.Count(f => after.Has("konomi." + f)) <= 1, "Konomi ordinary outcomes overlap.");
        }
        Snapshot Play(string id, Snapshot input)
        {
            var s = Find(id); var ready = Program.Copy(input); ready.Hour += s.DelayHours;
            check(Rules.Available(story, s, ready), "Konomi predecessor unavailable: " + id);
            return Program.Walk(s, ready).Where(o => o.Has(s.Id) && !o.Has("konomi.closed")).OrderByDescending(o => o.Flags.Count).First();
        }
        foreach (bool trickster in new[] { false, true })
        foreach (string history in new[] { "fresh", "ordinary_done", "farewell_done" })
        {
            var state = new Snapshot { Chapter = 3, Hour = 1000, Area = ordinary.Areas.Single() };
            state.Flags.UnionWith(new[] { "konomi.present", "seelah.committed", "arueshalae.committed" });
            if (trickster) state.Flags.Add("trickster");
            foreach (string id in new[] { "margin", "reception", "letter", "evening", "disagreement", "leak", "reckoning" }) state = Play(id, state);
            state.Chapter = 5;
            state.Flags.UnionWith(new[] { "konomi.rank_eight_started", "konomi.council_conclusion_seen", "konomi.political_respect_seen" });
            foreach (string id in new[] { "return", "political_account", "power" }) state = Play(id, state);
            check(!Rules.Available(story, ordinary, state), "Fresh Konomi ordinary skips played extension.");
            if (history != "fresh")
            {
                // Older serialized saves already have these completions; do not replay or erase them.
                foreach (string f in new[] { "konomi.ordinary", "konomi.at_home" }) { state.Flags.Add(f); state.Times[f] = 500; }
                if (history == "farewell_done")
                    foreach (string f in new[] { "konomi.farewell", "konomi.farewell_kept" }) { state.Flags.Add(f); state.Times[f] = 600; }
                check(!Rules.Available(story, visits[0], state), "Older Konomi extension starts without opt-in.");
                check(Rules.Available(story, offer, state), "Older Konomi invitation unavailable.");
                foreach (var outcome in Program.Walk(offer, state))
                {
                    Preserve(state, outcome);
                    if (!outcome.Has(offer.Id)) check(outcome.Flags.SetEquals(state.Flags), "Konomi invitation deferral changes history.");
                }
                state = Play("another_evening", state);
            }
            else check(!Rules.Available(story, offer, state), "Fresh Konomi sees old-save invitation.");
            var states = new List<Snapshot> { state };
            foreach (var scene in visits)
            {
                var nextStates = new List<Snapshot>();
                foreach (var input in states)
                {
                    var ready = Program.Copy(input); ready.Hour += scene.DelayHours;
                    check(Rules.Available(story, scene, ready), "Konomi extension chain blocked: " + scene.Id);
                    foreach (var result in Program.Walk(scene, ready, (id, partial) =>
                    {
                        reached.Add(scene.Id + "/" + id);
                        replay.TryAdd(scene.Id + "/" + id + "/" + Key(partial), (scene, Program.Copy(partial)));
                        check(partial.Flags.SetEquals(ready.Flags), "Konomi extension awards an outcome before its final page.");
                    }))
                    {
                        Preserve(ready, result);
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags), "Konomi extension deferral changes flags.");
                            check(result.Times.OrderBy(p => p.Key).SequenceEqual(ready.Times.OrderBy(p => p.Key)), "Konomi extension deferral changes timestamps.");
                            continue;
                        }
                        nextStates.Add(result); outcomeFlags.UnionWith(result.Flags);
                    }
                }
                states = nextStates.GroupBy(Key).Select(g => g.First()).ToList();
                check(states.Count > 0, "Konomi extension has no earned continuation.");
            }
            foreach (var result in states)
            {
                check(result.Has("konomi.ordinary_expanded"), "Konomi extension lacks final completion.");
                check(!Rules.Available(story, offer, result), "Finished Konomi extension repeats opt-in.");
                if (history == "fresh")
                {
                    var finished = Play("ordinary", result); finished = Play("farewell", finished);
                    check(finished.Has("konomi.farewell_kept"), "Konomi expanded sequence strands final farewell.");
                }
            }
        }
        foreach (var pair in pairs) foreach (string flag in pair)
            check(outcomeFlags.Contains("konomi." + flag), "Konomi traversal missed authored outcome: " + flag);
        foreach (var scene in visits)
        {
            foreach (var node in scene.Nodes) check(reached.Contains(scene.Id + "/" + node.Id), "Unplayed Konomi expansion page.");
            var ready = new Snapshot { Chapter = 5, Hour = 10000, Area = ordinary.Areas.Single() };
            ready.Flags.UnionWith(scene.Requires);
            check(Rules.Available(story, scene, ready), "Konomi availability baseline invalid.");
            foreach (string flag in new[] { "konomi.closed", "konomi.dismissed", "inhuman" })
            {
                var blocked = Program.Copy(ready); blocked.Flags.UnionWith(new[] { flag, "konomi.ordinary_expansion_requested" });
                check(!Rules.Available(story, scene, blocked), "Konomi opt-in bypasses hard restriction: " + flag);
            }
            var absent = Program.Copy(ready); absent.Flags.Remove("konomi.present");
            check(!Rules.Available(story, scene, absent), "Konomi extension survives lost appointment presence.");
            var elsewhere = Program.Copy(ready); elsewhere.Area = "elsewhere";
            check(!Rules.Available(story, scene, elsewhere), "Konomi extension ignores location.");
            var chapter = Program.Copy(ready); chapter.Chapter = 3;
            check(!Rules.Available(story, scene, chapter), "Konomi extension starts before Chapter 5.");
            foreach (var prerequisite in scene.Requires)
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(prerequisite);
                check(!Rules.Available(story, scene, missing), "Konomi extension skips prerequisite " + prerequisite);
            }
            ready.Times[scene.Requires.Last()] = ready.Hour;
            ready.Hour += scene.DelayHours - 1;
            check(!Rules.Available(story, scene, ready), "Konomi extension skips delay.");
            ready.Hour++;
            check(Rules.Available(story, scene, ready), "Konomi extension misses delay boundary.");
        }
        foreach (var item in replay.Values)
        {
            check(Rules.Available(story, item.Scene, item.State), "Konomi interrupted scene cannot restart.");
            foreach (var result in Program.Walk(item.Scene, item.State)) Preserve(item.State, result);
        }
        var transformed = new Snapshot { Chapter = 5, Hour = 10000, Area = ordinary.Areas.Single() };
        transformed.Flags.UnionWith(ordinary.Requires); transformed.Flags.Add("inhuman");
        check(Rules.Available(story, ordinary, transformed), "Konomi expansion removes existing transformed companionship.");
        check(offer.ManualOnly && Rules.IsRemote(offer), "Konomi older-save opt-in loses manual delivery.");
        var focused = new Story { Scenes = new List<Scene> { offer }, Relationships = story.Relationships };
        check(Rules.NextRemote(focused, transformed) == null, "Konomi manual opt-in enters automatic queue.");
        var roll = visits.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Single(c => c.Check != null).Check!;
        check(roll.Skill == "SkillPerception" && roll.DC == 26 && roll.CommanderOnly, "Konomi trial check changed.");
    }
}
