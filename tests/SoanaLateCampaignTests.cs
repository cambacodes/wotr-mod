using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class SoanaLateCampaignTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string actor = "64805abb52739e44280a758f850b300c";
        const string area = "0a5654e7dc18f074d9356009d55eb51b";
        Scene Get(string id) => story.Scenes.Single(s => s.Id == "soana." + id);
        string[] oldIds = { "threshold", "water_carrier", "guardian_question", "one_account", "watch_line", "price_of_warning", "ordinary_feast", "name_between", "lower_bend", "the_thing_in_the_sack", "the_dry_offering", "the_inherited_debt", "a_voice_in_the_dark", "what_followed_home", "a_promise_still_spoken", "the_unwelcome_path", "after_the_last_visitor" };
        string[] visitIds = { "when_the_road_returns", "a_track_with_two_ends", "what_the_hollow_costs", "where_the_steps_end", "the_days_she_counted", "before_the_far_road" };
        var visits = visitIds.Select(Get).ToArray();
        var firelight = Get("past_the_firelight");
        var endings = story.Scenes.Where(s => s.Relationship == "soana" && s.Owner == "Epilogue" && !s.Id.StartsWith("soana.trickster.", StringComparison.Ordinal)
            && !s.Id.StartsWith("soana.partner.", StringComparison.Ordinal)).ToArray();
        var reached = new HashSet<string>();
        var protectedFlags = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys)
            .Concat(new[] { "konomi.committed", "jerribeth.committed", "committed" }).Distinct().ToArray();
        void Preserve(Snapshot input, Snapshot result)
        {
            check(input.Flags.Where(f => !story.Derived.ContainsKey(f) && !story.Counts.ContainsKey(f)).All(result.Has), "Soana late route erases earned history.");
            foreach (string f in protectedFlags) check(input.Has(f) == result.Has(f), "Soana changes native or other romance history: " + f);
            foreach (var time in input.Times.Where(t => !story.Derived.ContainsKey(t.Key) && !story.Counts.ContainsKey(t.Key))) check(result.Times[time.Key] == time.Value, "Soana rewrites an old timestamp.");
            check(input.AvailableContacts.SetEquals(result.AvailableContacts), "Soana late route invents an actor.");
        }
        Snapshot Earn(string id, Snapshot input, Func<Snapshot, bool> select)
        {
            var ready = Program.Copy(input); ready.Hour += Get(id).DelayHours;
            check(Program.CurrentAvailable(story, Get(id), ready), "Soana actual predecessor unavailable: " + id);
            return Program.Walk(Get(id), ready).First(s => s.Has(Get(id).Id) && !s.Has("soana.closed") && select(s));
        }
        void Ending(Snapshot state, string expected)
        {
            var available = endings.Where(s => Program.CurrentAvailable(story, s, state)).ToList();
            check(available.Count == 1 && available[0].Id == "soana.ending_" + expected, "Soana ending overlap or wrong history: " + expected);
            foreach (var result in Program.Walk(available.Single(), state, (id, _) => reached.Add(available[0].Id + "/" + id)))
            { Preserve(state, result); check(result.Has(available[0].Id), "Soana earned epilogue has no terminal path."); }
        }
        void InterruptedEnding(Snapshot state)
        {
            check(state.Has("soana.progression_kept") && !state.Has("soana.late_campaign_kept"), "Provisional ending fixture is not an unfinished earned history.");
            foreach (var variant in new[] { ("sacrifice", "unfinished_sacrifice"), ("ascended", "unfinished_ascent"), ("inhuman", "unfinished_change"), ("soana.dead", "unfinished_loss"), ("soana.killed_by_camellia", "unfinished_loss"), ("soana.forest_dead", "unfinished_loss") })
            {
                var changed = Program.Copy(state); changed.Flags.Add(variant.Item1);
                Ending(changed, variant.Item2);
                if (variant.Item1 == "inhuman") check(visits.All(v => !Program.CurrentAvailable(story, v, changed)), "Transformation fixture still permits the blocked late romance.");
            }
            var overlapping = Program.Copy(state);
            overlapping.Flags.UnionWith(new[] { "ascended", "inhuman", "soana.dead", "soana.killed_by_camellia", "soana.forest_dead" });   // earned presence: her loss page has a living Commander
            Ending(overlapping, "unfinished_loss");
            var ascended = Program.Copy(state); ascended.Flags.UnionWith(new[] { "ascended" });
            Ending(ascended, "unfinished_ascent");
            ascended.Flags.Add("inhuman"); Ending(ascended, "unfinished_change");
        }
        foreach (string native in new[] { "bound", "dead", "overlap" })
        foreach (string working in new[] { "voice_carried", "voice_interrupted", "ridge_used" })
        foreach (bool cleft in new[] { false, true })
        foreach (bool friends in new[] { false, true })
        foreach (bool trickster in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 3, Hour = 1000, Area = area };
            state.AvailableContacts.Add(actor);
            state.Flags.UnionWith(new[] { "soana.after_quest", trickster ? "trickster" : "angel", "konomi.committed", "jerribeth.committed", "committed" });
            if (native != "dead") state.Flags.Add("soana.old_defender");
            if (native != "bound") state.Flags.Add("soana.bear_dead");
            foreach (string id in oldIds)
                state = Earn(id, state, s =>
                    (id != "name_between" || s.Has("soana." + (friends ? "friendship_chosen" : "courtship_chosen"))) &&
                    (id != "the_inherited_debt" || s.Has("soana." + (working == "ridge_used" ? "rite_ridge" : "rite_voice"))) &&
                    (id != "a_voice_in_the_dark" || s.Has("soana." + working)) &&
                    (id != "a_promise_still_spoken" || s.Has("soana." + (friends ? "later_friends" : "later_courting"))) &&
                    (id != "the_unwelcome_path" || s.Has("soana.path_cleft") == cleft));
            check(state.Has("soana.progression_kept"), "No actual seventeen-scene predecessor.");
            check(!Program.CurrentAvailable(story, visits[0], state), "Late Soana return appears in Chapter 3.");
            state.Chapter = 4;
            check(!Program.CurrentAvailable(story, visits[0], state), "Late Soana return invents Abyss contact.");
            // PP6: the Chapter 4 memory (past_the_firelight), one answer per working so every tale reaches the Chapter 5 greeting.
            string voice = working == "voice_carried" ? "abyss_voice_unanswered" : working == "voice_interrupted" ? "abyss_voice_followed" : "abyss_voice_tested";
            var camp = Program.Copy(state); camp.Hour += firelight.DelayHours; camp.Area = "Abyss"; camp.AvailableContacts.Clear();
            check(Program.CurrentAvailable(story, firelight, camp), "The Abyss memory does not follow the seventeen scenes.");
            var heard = Program.Walk(firelight, camp, (page, _) => reached.Add(firelight.Id + "/" + page)).Where(r => r.Has(firelight.Id)).ToList();
            check(heard.Count == 3 && heard.All(r => new[] { "abyss_voice_unanswered", "abyss_voice_tested", "abyss_voice_followed" }.Count(f => r.Has("soana." + f)) == 1),
                "The Abyss memory does not end in exactly one answer.");
            state = Program.Copy(heard.Single(r => r.Has("soana." + voice))); state.Area = area; state.AvailableContacts.Add(actor);
            check(!Program.CurrentAvailable(story, firelight, state), "The Abyss memory repeats.");
            state.Chapter = 5;
            check(!endings.Any(e => Program.CurrentAvailable(story, e, state)), "Unplayed late campaign earns its finale.");
            InterruptedEnding(state);
            var states = new List<Snapshot> { state };
            foreach (var visit in visits)
            {
                var next = new List<Snapshot>();
                foreach (var input in states)
                {
                    var ready = Program.Copy(input); ready.Hour += visit.DelayHours;
                    check(Program.CurrentAvailable(story, visit, ready), "Earned late Soana visit unavailable: " + visit.Id);
                    if (visit.DelayHours > 0)
                    { var early = Program.Copy(ready); early.Hour--; check(!Program.CurrentAvailable(story, visit, early), "Late Soana wait ignored."); }
                    foreach (var result in Program.Walk(visit, ready, (page, partial) =>
                    {
                        reached.Add(visit.Id + "/" + page);
                        check(partial.Flags.SetEquals(ready.Flags), "Interrupted late Soana scene persists a partial choice.");
                        check(partial.Times.OrderBy(p => p.Key).SequenceEqual(ready.Times.OrderBy(p => p.Key)), "Interrupted late Soana scene changes time.");
                        check(Program.CurrentAvailable(story, visit, partial), "Interrupted late visit cannot restart.");
                        var absent = Program.Copy(partial); absent.AvailableContacts.Clear();
                        check(!Rules.ContactAvailable(story, visit, absent), "Soana continues without original living contact.");
                        foreach (string loss in new[] { "soana.dead", "soana.killed_by_camellia", "soana.forest_dead" })
                        { var gone = Program.Copy(partial); gone.Flags.Add(loss); check(!Rules.ContactAvailable(story, visit, gone), "Native loss does not interrupt Soana."); }
                        if (page == "bound") check(!partial.Has("soana.bear_dead"), "Dead bear gains living text.");
                        if (page == "dead") check(partial.Has("soana.bear_dead"), "Living bear gains death text.");
                        if (page == "changed_role") check(partial.Has("soana.voice_interrupted"), "Soana invents broken practical trust.");
                        if (page == "welcome" || page == "future" || page == "desire") check(!friends, "Established friendship becomes romance without choice.");
                        if (visit.Id.EndsWith("before_the_far_road") && page == "desire") check(!partial.Has("soana.late_friends"), "Ended courtship still offers farewell intimacy.");
                    }))
                    {
                        Preserve(ready, result);
                        if (!result.Has(visit.Id))
                        { check(result.Flags.SetEquals(ready.Flags), "Soana deferral persists a decision."); continue; }
                        check(!Program.CurrentAvailable(story, visit, result), "Completed late Soana visit repeats.");
                        if (result.Has("soana.closed"))
                        {
                            check(!trickster && result.Has("soana.partner_stance.exclusive")
                                && result.Has("soana.partner.agreed") && !result.Has("soana.partner.exclusive_chosen"),
                                "Exclusive refusal closes without its actual non-Trickster history.");
                            check(visits.All(v => !Program.CurrentAvailable(story, v, result)),
                                "Insisting after Soana's refusal permits more late courtship.");
                            continue;
                        }
                        foreach (var group in new[] {
                            new[] { "late_track_read", "late_track_missed", "late_track_slow" },
                            new[] { "late_reserve", "late_harvest" }, new[] { "late_thorn_strong", "late_thorn_soft" },
                            new[] { "committed", "late_open", "late_friends" },
                            new[] { "late_farewell_night", "late_farewell_kiss", "late_farewell_held", "late_farewell_friend" } })
                            check(group.Count(f => result.Has("soana." + f)) <= 1, "Soana late outcomes overlap.");
                        next.Add(result);
                    }
                }
                states = next.GroupBy(s => string.Join("|", s.Flags.OrderBy(f => f))).Select(g => g.First()).ToList();
                if (visit != visits.Last()) InterruptedEnding(states.First());
            }
            foreach (var complete in states)
            {
                check(complete.Has("soana.late_campaign_kept"), "Final visit lacks completion.");
                Ending(complete, complete.Has("soana.committed") ? "kept_life" : complete.Has("soana.late_open") ? "chosen_visits" : "familiar_company");
                foreach (var variant in new[] { ("sacrifice", "sacrifice"), ("ascended", "beyond_the_forest"), ("inhuman", "unrecognizable_return"), ("soana.dead", "native_loss"), ("soana.killed_by_camellia", "native_loss"), ("soana.forest_dead", "native_loss") })
                { var other = Program.Copy(complete); other.Flags.Add(variant.Item1); Ending(other, variant.Item2); }
                var overlapping = Program.Copy(complete);
                overlapping.Flags.UnionWith(new[] { "ascended", "inhuman", "soana.dead", "soana.killed_by_camellia", "soana.forest_dead" });   // earned presence: her loss page has a living Commander
                Ending(overlapping, "native_loss");
                var aeon = Get("ending_aeon");
                check(aeon.Owner == "AeonEpilogue" && Program.CurrentAvailable(story, aeon, complete), "Rewritten-world ending lacks its separate sequence.");
                foreach (var outcome in Program.Walk(aeon, complete, (id, _) => reached.Add(aeon.Id + "/" + id))) Preserve(complete, outcome);
            }
        }
        foreach (var visit in visits)
        {
            check(visit.ContactUnit == actor && visit.Areas.SequenceEqual(new[] { area }) && !Rules.IsRemote(visit), "Soana local native contact changed.");
            check(Rules.EntryTargets(visit).SequenceEqual(new[] { "2b1776f3e398685479ff6b16290b4cc2" }), "Soana native insertion changed.");
            var ready = new Snapshot { Chapter = 5, Hour = 50000, Area = area };
            ready.Flags.UnionWith(visit.Requires); ready.Flags.Add("soana.old_defender"); ready.AvailableContacts.Add(actor);
            check(Program.CurrentAvailable(story, visit, ready), "Late Soana eligibility baseline invalid.");
            foreach (var required in visit.Requires.Where(requiredKey => !requiredKey.EndsWith(".present_now", StringComparison.Ordinal) && !requiredKey.EndsWith(".reachable_by_letter", StringComparison.Ordinal)))
            { var missing = Program.Copy(ready); missing.Flags.Remove(required); check(!Program.CurrentAvailable(story, visit, missing), "Soana missing earned prerequisite admitted: " + required); }
            foreach (var forbidden in visit.Forbids)
            { var blocked = Program.Copy(ready); blocked.Flags.Add(forbidden); check(!Program.CurrentAvailable(story, visit, blocked), "Soana blocker admitted: " + forbidden); }
            foreach (int chapter in new[] { 3, 4, 6 })
            { var wrong = Program.Copy(ready); wrong.Chapter = chapter; check(!Program.CurrentAvailable(story, visit, wrong), "Wrong chapter invents Soana contact."); }
            var elsewhere = Program.Copy(ready); elsewhere.Area = "Drezen";
            check(!Program.CurrentAvailable(story, visit, elsewhere), "Soana invented capital appearance.");
        }
        // PP6: the Chapter 4 memory is a remote page read only on the registered route, never in Chapters 3 or 5, never after a loss.
        check(Rules.IsRemote(firelight) && firelight.Kind == "memory" && firelight.Chapters.SequenceEqual(new[] { 4 }) && firelight.Relationship == "soana"
              && firelight.Requires.SequenceEqual(new[] { "soana.progression_kept" }) && firelight.ContactUnit == null && firelight.AnswerLists.Length == 0,
            "The Abyss memory lost its shape.");
        var abyss = new Snapshot { Chapter = 4, Hour = 50000, Area = "Abyss" }; abyss.Flags.Add("soana.progression_kept");
        check(Program.CurrentAvailable(story, firelight, abyss), "The Abyss memory baseline is invalid.");
        foreach (int chapter in new[] { 3, 5 }) { var wrong = Program.Copy(abyss); wrong.Chapter = chapter; check(!Program.CurrentAvailable(story, firelight, wrong), "The Abyss memory leaves Chapter 4."); }
        foreach (string loss in new[] { "soana.dead", "soana.killed_by_camellia", "soana.forest_dead", "soana.closed", "inhuman" })
        { var lost = Program.Copy(abyss); lost.Flags.Add(loss); check(!Program.CurrentAvailable(story, firelight, lost), "The Abyss memory ignores: " + loss); }
        var greet = Get("when_the_road_returns");
        foreach (string node in new[] { "welcome", "friend" })
        {
            var answers = greet.Nodes.Single(n => n.Id == node).Choices;
            check(answers.Count == 4 && answers[0].Next == "nursery" && answers.Skip(1).Select(a => a.Requires.Single()).SequenceEqual(
                new[] { "soana.abyss_voice_unanswered", "soana.abyss_voice_tested", "soana.abyss_voice_followed" }), "The Abyss tales were not appended to: " + node);
        }
        foreach (var scene in visits.Concat(endings).Concat(new[] { Get("ending_aeon"), firelight }))
            foreach (var page in scene.Nodes.Where(n => !n.Id.Contains("_r3_", StringComparison.Ordinal)
                && n.Id != "round2_affair" && n.Id != "delivered" && n.Id != "partner_exclusive_commit_chosen"
                && !(n.Id.Contains(".explicit.", StringComparison.Ordinal) && scene.Nodes.Any(p => p.Id.StartsWith("quiet_r3_", StringComparison.Ordinal) && p.Choices.Any(a => a.Next == n.Id)))))
                check(reached.Contains(scene.Id + "/" + page.Id) || reached.Contains(scene.Id + "/" + page.Id + "_r3_unanswered"), "Unplayed late Soana page: " + scene.Id + "/" + page.Id);
        var roll = visits.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Single(c => c.Check != null).Check!;
        check(roll.Skill == "SkillLoreNature" && roll.DC == 26 && roll.CommanderOnly, "Soana trail check contract changed.");
    }
}
