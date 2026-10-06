using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KonomiPoliticalConsequenceTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Get(string id) => story.Scenes.Single(s => s.Id == "konomi." + id);
        var offer = Get("the_names_admitted");
        var reply = Get("the_answer_on_record");
        var ordinary = Get("ordinary");
        var reached = new HashSet<string>();
        string[] reports = { "konomi.foreign_report_seen", "konomi.domestic_report_seen", "konomi.crisis_report_seen" };
        string[] guids = { "9980a1ecf3ca24e42ab3b22f858677b5", "60585f7319a294147a54f440865b21a2", "07459f4d09fa81e4b99beea351fb0434" };
        for (int i = 0; i < reports.Length; i++)
            check(story.SeenCues[reports[i]].SequenceEqual(new[] { guids[i] }), "Political report is not exact native cue history.");
        var protectedFlags = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys)
            .Concat(new[] { "trickster", "konomi.committed", "arueshalae.committed", "jerribeth.committed" }).Distinct().ToArray();
        Snapshot Earn(string id, Snapshot state, Func<Snapshot, bool>? choose = null)
        {
            state.Hour += 1000;
            check(Program.CurrentAvailable(story, Get(id), state), "Political consequence predecessor unavailable: " + id);
            return Program.Walk(Get(id), state).First(s => s.Has(Get(id).Id) && !s.Has("konomi.closed") && (choose == null || choose(s)));
        }
        List<Snapshot> Walk(Scene scene, Snapshot state)
        {
            check(Program.CurrentAvailable(story, scene, state), "Political contribution unavailable: " + scene.Id);
            var results = Program.Walk(scene, state, (page, partial) =>
            {
                reached.Add(scene.Id + "/" + page);
                if (scene != ordinary)
                {
                    check(partial.Flags.SetEquals(state.Flags), "Unfinished political page persists a branch.");
                    check(partial.Times.OrderBy(x => x.Key).SequenceEqual(state.Times.OrderBy(x => x.Key)), "Unfinished political page changes timestamps.");
                }
            });
            foreach (var result in results)
            {
                foreach (var flag in protectedFlags)
                    check(result.Has(flag) == state.Has(flag), "Political fiction modifies native or other relationship history: " + flag);
                if (!result.Has(scene.Id)) check(result.Flags.SetEquals(state.Flags), "Political deferral changes history.");
                else check(!Program.CurrentAvailable(story, scene, result), "Political contribution repeats after completion.");
            }
            return results.Where(s => s.Has(scene.Id)).ToList();
        }

        var early = new Snapshot { Chapter = 3, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
        early.Flags.UnionWith(new[] { "konomi.present", "trickster", "arueshalae.committed", "jerribeth.committed" });
        early.AvailableContacts.Add("ca2d58c5c65723945857e04fb85d30ce");
        foreach (string id in new[] { "margin", "reception", "letter", "evening", "disagreement", "leak", "reckoning" }) early = Earn(id, early);
        early.Chapter = 5;
        early = Earn("return", early);
        foreach (string phase in new[] { "unknown", "crisis", "domestic", "foreign" })
        for (int mask = 0; mask < 8; mask++)
        foreach (bool conclusion in new[] { false, true })
        foreach (bool respect in new[] { false, true })
        {
            var state = Program.Copy(early);
            if (phase != "unknown") state.Flags.Add("konomi.rank_six_started");
            if (phase is "domestic" or "foreign") state.Flags.Add("konomi.rank_eight_started");
            if (phase == "foreign") state.Flags.Add("konomi.foreign_help_playing");
            for (int i = 0; i < 3; i++) if ((mask & (1 << i)) != 0) state.Flags.Add(reports[i]);
            if (conclusion) state.Flags.Add("konomi.council_conclusion_seen");
            if (respect) state.Flags.Add("konomi.political_respect_seen");
            state = Earn("political_account", state);
            state.Hour += 1000;
            var context = offer.Nodes.Single(n => n.Id == "context").Choices.Where(c => Rules.Match(c.Requires, c.Forbids, state)).ToArray();
            string expected = phase == "foreign" && (mask & 1) != 0 ? "foreign"
                : phase == "domestic" && (mask & 2) != 0 ? "domestic"
                : phase == "crisis" && (mask & 4) != 0 ? "crisis" : "unconfirmed";
            check(context.Length == 1 && context[0].Next == expected, "Stale/unseen native report supplied false current memory.");
            foreach (var sent in Walk(offer, state))
            {
                check(sent.Has("konomi.political_recognized") != sent.Has("konomi.political_sponsored"), "Political arrangements overlap.");
                check(!Program.CurrentAvailable(story, reply, sent), "Political reply ignores correspondence delay.");
                sent.Hour += 1000;
                var role = reply.Nodes.Single(n => n.Id == "role").Choices.Single(c => Rules.Match(c.Requires, c.Forbids, sent));
                var esteem = reply.Nodes.Single(n => n.Id == "respect").Choices.Single(c => Rules.Match(c.Requires, c.Forbids, sent));
                check(role.Next == (conclusion ? "concluded" : "ongoing"), "Council conclusion invented or dropped.");
                check(esteem.Next == (respect ? "earned" : "unearned"), "Political respect invented or dropped.");
                foreach (var finished in Walk(reply, sent)) check(finished.Has("konomi.political_reply_kept"), "Political result not resolved.");
            }
        }

        // The callback is earned by the actual ordinary experiment/report, not a political-report fixture.
        foreach (bool eveningTrial in new[] { false, true })
        foreach (bool joint in new[] { false, true })
        {
            var state = Earn("political_account", Program.Copy(early));
            state = Earn("power", state, s => s.Has("konomi.committed"));
            foreach (string id in new[] { "a_useful_supper", "the_upper_passage" }) state = Earn(id, state);
            state = Earn("two_bad_prices", state, s => s.Has("konomi.evening_trial") == eveningTrial);
            state = Earn("the_trial_day", state);
            state = Earn("a_name_beside_hers", state, s => s.Has("konomi.joint_offer") == joint);
            state = Earn("the_evening_she_kept", state);
            state.Hour += 1000;
            var pages = new HashSet<string>();
            Program.Walk(ordinary, state, (page, _) => pages.Add(page));
            check(pages.Contains(eveningTrial ? "work_evening" : "work_morning") && !pages.Contains(eveningTrial ? "work_morning" : "work_evening"), "Closing trial memory mismatches actual chosen plan.");
            check(pages.Contains(joint ? "work_joint" : "work_circular") && !pages.Contains(joint ? "work_circular" : "work_joint"), "Closing report memory mismatches actual chosen publication.");
            foreach (var outcome in Walk(ordinary, state)) check(outcome.Has("konomi.at_home"), "New callback loses original ordinary conclusion.");
            check(!ordinary.Requires.Contains(offer.Id) && !ordinary.Requires.Contains(reply.Id), "Political sequel made the ordinary close mandatory.");
            foreach (var gate in new[] { "konomi.ordinary_expanded", "konomi.trial_lived", "konomi.readers_answered" })
            {
                var missing = Program.Copy(state); missing.Flags.Remove(gate);
                var choice = ordinary.Nodes[0].Choices.Single(c => c.Next == "work_remembered");
                check(!Rules.Match(choice.Requires, choice.Forbids, missing), "Unplayed old save receives a completed trial/report memory.");
            }
        }
        foreach (var scene in new[] { offer, reply })
        {
            var ready = Program.Copy(early); ready.Hour = 100000; ready.Flags.UnionWith(scene.Requires);
            check(Program.CurrentAvailable(story, scene, ready), "Political scene baseline unavailable.");
            foreach (string flag in scene.Requires.Where(requiredKey => !requiredKey.EndsWith(".present_now", StringComparison.Ordinal) && !requiredKey.EndsWith(".reachable_by_letter", StringComparison.Ordinal)))
            { var missing = Program.Copy(ready); missing.Flags.Remove(flag); check(!Program.CurrentAvailable(story, scene, missing), "Missing political requirement: " + flag); }
            foreach (string flag in scene.Forbids)
            { var blocked = Program.Copy(ready); blocked.Flags.Add(flag); check(!Program.CurrentAvailable(story, scene, blocked), "Political contact ignores block: " + flag); }
            foreach (string cause in new[] { "contact", "dismissal", "office", "area", "chapter" })
            {
                var changed = Program.Copy(ready);
                if (cause == "contact") changed.AvailableContacts.Clear();
                if (cause == "dismissal") changed.Flags.Add("konomi.dismissed");
                if (cause == "office") changed.Flags.Remove("konomi.present");
                if (cause == "area") changed.Area = "abyss";
                if (cause == "chapter") changed.Chapter = 4;
                check(!Program.CurrentAvailable(story, scene, changed) && !Rules.ContactAvailable(story, scene, changed), "Entry/continuation retained absent political officer: " + cause);
            }
        }
        foreach (var scene in new[] { offer, reply }) foreach (var node in scene.Nodes)
            check(reached.Contains(scene.Id + "/" + node.Id), "New political page never played: " + scene.Id + "/" + node.Id);
        foreach (var node in ordinary.Nodes.Where(n => n.Id.StartsWith("work_", StringComparison.Ordinal)))
            check(reached.Contains(ordinary.Id + "/" + node.Id), "New ordinary callback never played: " + node.Id);
    }
}
