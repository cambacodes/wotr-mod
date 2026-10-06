using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class NocticulaConcessionTests
{
    // Native disclosure is a fixture boundary; all inherited channel states come from played opening choices.
    internal static void Run(Story story, Action<bool, string> check)
    {
        story = Program.Unfolded(story);   // NM1: judged per letter; the folded deliveries are Nm1BudgetTests
        string[] ids = {
            "noct.acq.borrowed_signature", "noct.acq.the_paid_address",
            "noct.acq.the_retained_copy", "noct.acq.an_answer_of_her_own"
        };
        var concession = story.Scenes.Where(s => ids.Contains(s.Id)).ToArray();
        if (concession.Length == 0) return;
        check(concession.Length == ids.Length, "Nocticula concession is only partially assembled.");
        concession = ids.Select(id => concession.Single(s => s.Id == id)).ToArray();
        var entries = story.Scenes.Where(s => s.Id.StartsWith("noct.acq.audience_", StringComparison.Ordinal)).ToArray();
        check(entries.Length == 3, "Concession requires the three real acquisition entries.");
        var preparation = story.Scenes.Single(s => s.Id == "noct.acq.the_missing_line");
        var reply = story.Scenes.Single(s => s.Id == "noct.acq.her_hand");
        var reached = concession.ToDictionary(s => s.Id, _ => new HashSet<string>());
        var native = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.SeenCues.Keys)
            .Concat(story.SelectedAnswers.Keys).Concat(story.CompletedQuests.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();
        check(concession.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).All(c => c.Revive == null
            && c.Set.All(flag => (flag.StartsWith("noct.acq.", StringComparison.Ordinal)
                || flag.StartsWith("nocticula.partner_", StringComparison.Ordinal)
                || flag == "nocticula.partner.exclusive_chosen"
                || flag == "nocticula.partner.letters_burned") && !native.Contains(flag))),
            "Concession writes native history or requests actor recovery.");

        string[][] histories = {
            Array.Empty<string>(), new[] { "noct.gift" },
            new[] { "noct.parent_rejected" }, new[] { "noct.parent_rejected", "noct.gift" },
            new[] { "noct.parent_active", "noct.acq.original_gift_completed" },
            new[] { "noct.parent_active", "noct.acq.original_gift_completed", "noct.acq.gift_renewed" }
        };
        int trials = 0, agreements = 0, closures = 0, personalDeclines = 0;
        int checkedSuccesses = 0, checkedFailures = 0, manualInquiries = 0, wrapperCallbacks = 0;

        void Preserved(Snapshot expected, Snapshot actual)
        {
            check(expected.Flags.Where(native.Contains).ToHashSet().SetEquals(actual.Flags.Where(native.Contains)),
                "Concession changed native or parent history.");
            check(actual.Has("seelah.committed") && actual.Has("arueshalae.committed"),
                "Concession removed a concurrent romance.");
            check(actual.AvailableContacts.SetEquals(expected.AvailableContacts),
                "Remote concession manufactured a physical contact.");
        }

        foreach (var history in histories)
        {
            var initial = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            initial.Flags.UnionWith(new[] { "trickster", "noct.acq.audience_question", "seelah.committed", "arueshalae.committed",
                // Isolate the existing channel/harbor matrix; new on-page terms have their own route tests.
                "nocticula.partner_terms", "nocticula.partner_stance.share" });
            initial.Flags.UnionWith(history);
            var available = entries.Where(s => Rules.Available(story, s, initial)).ToArray();
            check(available.Length == 1, "Concession fixture does not select exactly one native-history entry.");
            int historyTrials = 0, historyAgreements = 0;
            var channels = new HashSet<string>();
            foreach (var request in Program.Walk(available.Single(), initial))
            {
                if (request.Has("noct.acq.closed")) continue;
                var witnessed = Program.Copy(request);
                witnessed.Hour += preparation.DelayHours;
                check(!Rules.Available(story, preparation, witnessed), "Opening bypasses native Council evidence.");
                // Genuine native dialogue events must supply these outside the addon walker.
                witnessed.Flags.UnionWith(new[] { "noct.acq.council_disclosed", "noct.socoth_plan_exposed" });
                check(Rules.Available(story, preparation, witnessed), "Witnessed request cannot prepare contact.");
                foreach (var prepared in Program.Walk(preparation, witnessed))
                {
                    if (!prepared.Has(preparation.Id)) continue; // An actual postponement, not a trial fixture.
                    var replyReady = Program.Copy(prepared);
                    replyReady.Hour += reply.DelayHours;
                    check(Rules.Available(story, reply, replyReady), "Selected preparation cannot receive its reply.");
                    foreach (var trial in Program.Walk(reply, replyReady))
                    {
                        if (trial.Has("noct.acq.closed")) continue;
                        check(trial.Has("noct.acq.correspondence_trial") && !trial.Has("noct.acq.renewed_agreement"),
                            "Opening did not produce a preliminary, uncommitted trial.");
                        Preserved(witnessed, trial);
                        trials++; historyTrials++;
                        channels.Add(trial.Has("noct.acq.channel_exposed") ? "repaired"
                            : trial.Has("noct.acq.channel_provisional") ? "narrow" : "letters");
                        var states = new List<Snapshot> { trial };
                        foreach (var scene in concession)
                        {
                            var nextStates = new List<Snapshot>();
                            foreach (var previous in states)
                            {
                                check(!Rules.Available(story, scene, previous), "Concession ignores the minimum wait: " + scene.Id);
                                var ready = Program.Copy(previous);
                                ready.Hour += scene.DelayHours;
                                check(Rules.Available(story, scene, ready), "Selected history cannot enter concession: " + scene.Id);
                                foreach (string blocker in new[] { "noct.dead", "noct.acq.council_fight", "noct.acq.closed" })
                                {
                                    var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                                    check(!Rules.Available(story, scene, blocked), "Living concession ignores blocker: " + blocker);
                                }
                                foreach (var result in Program.Walk(scene, ready, (node, partial) =>
                                {
                                    reached[scene.Id].Add(node);
                                    if (scene.Id == "noct.acq.the_paid_address" && new[] { "read", "mistake", "open" }.Contains(node))
                                    {
                                        bool attempted = node != "open";
                                        check(partial.Has("noct.acq.address_check_tried") == attempted,
                                            "Address result does not match the selected roll/manual method.");
                                        if (attempted)
                                        {
                                            var offered = scene.Nodes[0].Choices.Where(c => Rules.Match(c.Requires, c.Forbids, partial)).ToArray();
                                            check(offered.All(c => c.Check == null) && offered.Any(c => c.Next == "open"),
                                                "Attempt flag permits a reroll or removes the ordinary investigation.");
                                        }
                                        if (node == "read") checkedSuccesses++;
                                        else if (node == "mistake") checkedFailures++;
                                        else manualInquiries++;
                                    }
                                    if (scene.Id == "noct.acq.the_retained_copy" && node == "unknown")
                                    {
                                        wrapperCallbacks++;
                                        check(partial.Has("noct.acq.buyers_unknown") && partial.Has("noct.acq.wrapper_recovered"),
                                            "Unknown-buyer callback invents the recovered wrapper.");
                                        var missing = Program.Copy(partial); missing.Flags.Remove("noct.acq.wrapper_recovered");
                                        check(scene.Nodes[0].Choices.Where(c => c.Next == "unknown")
                                            .All(c => !Rules.Match(c.Requires, c.Forbids, missing)),
                                            "Wrapper callback lacks its actual evidence gate.");
                                    }
                                    if (scene.Id == "noct.acq.an_answer_of_her_own")
                                    {
                                        if (node == "accept") check(partial.Has("noct.acq.renewed_agreement")
                                            && partial.Has("noct.acq.personal_risk_accepted"), "Acceptance page lacks selected agreement.");
                                        else check(!partial.Has("noct.acq.renewed_agreement"),
                                            "Personal agreement appears before acceptance or on a refusal.");
                                    }
                                }))
                                {
                                    Preserved(witnessed, result);
                                    check(!Rules.Available(story, scene, result), "Completed concession visit repeats: " + scene.Id);
                                    if (result.Has("noct.acq.closed"))
                                    {
                                        closures++;
                                        if (result.Has("noct.acq.personal_declined")) personalDeclines++;
                                        check(!result.Has("noct.acq.renewed_agreement") && !result.Has("noct.acq.personal_risk_accepted"),
                                            "Declined concession or invitation grants an agreement.");
                                        if (previous.Has("noct.acq.undertaking_held"))
                                            check(result.Has("noct.acq.undertaking_held"), "Withdrawal erased her retained undertaking.");
                                        var later = Program.Copy(result); later.Hour += 1000;
                                        check(concession.All(s => !Rules.Available(story, s, later)),
                                            "Closed concession later reopens by waiting.");
                                        continue;
                                    }
                                    if (scene.Id == "noct.acq.the_paid_address")
                                    {
                                        check(result.Has("noct.acq.buyers_identified") != result.Has("noct.acq.buyers_unknown"),
                                            "Investigation lacks one selected buyer outcome.");
                                        check(result.Has("noct.acq.wrapper_recovered") == result.Has("noct.acq.buyers_unknown"),
                                            "Wrapper recovery does not match the failed/manual investigation.");
                                        check(result.Has("noct.acq.pattern_destroyed") != result.Has("noct.acq.pattern_retained"),
                                            "Concession has overlapping pattern dispositions.");
                                        if (result.Has("noct.acq.buyers_unknown"))
                                            check(result.Has("noct.acq.salven_warned"), "Lost names omit the warned broker.");
                                    }
                                    nextStates.Add(result);
                                }
                            }
                            states = nextStates;
                        }
                        check(states.Count == 6, "Played trial lost a concession approach or investigation outcome.");
                        foreach (var final in states)
                        {
                            check(final.Has("noct.acq.renewed_agreement") && final.Has("noct.acq.personal_risk_accepted")
                                && final.Has("noct.acq.an_answer_of_her_own_done") && final.Has("noct.acq.undertaking_held"),
                                "Completed concession lacks affirmative acceptance or its retained cost.");
                            if (final.Has("noct.acq.pattern_retained"))
                                check(final.Has("noct.acq.first_report_delivered") && final.Has("noct.acq.blank_reports_owed"),
                                    "Retained forwarding business loses its reporting obligations.");
                            foreach (string flag in new[] { "channel_provisional", "channel_letters_only", "channel_exposed", "channel_repaired", "sketch_surrendered" })
                                check(final.Has("noct.acq." + flag) == trial.Has("noct.acq." + flag),
                                    "Concession changes the earned contact limitation: " + flag);
                            agreements++; historyAgreements++;
                        }
                    }
                }
            }
            check(historyTrials == 6 && historyAgreements == 36 && channels.SetEquals(new[] { "narrow", "letters", "repaired" }),
                "Native-history fixture missed a played channel or accepted concession path.");
        }
        check(trials == 36 && agreements == 216 && closures == 576 && personalDeclines == 432,
            "Assembled concession acceptance/refusal counts changed; inspect actual paths before changing expectations.");
        check(checkedSuccesses == 72 && checkedFailures == 72 && manualInquiries == 72 && wrapperCallbacks == 144,
            "Concession did not exercise every investigation method and both wrapper producers.");
        foreach (var scene in concession)
            check(reached[scene.Id].SetEquals(scene.Nodes.Where(n => !n.Id.StartsWith("partner_", StringComparison.Ordinal)).Select(n => n.Id)), "Concession missed delivered nodes: " + scene.Id);
        Console.WriteLine("Nocticula assembled concession: 6 native histories, 36 played trials, 216 agreements, 576 closures; all 35 concession nodes reached. Native execution and prose chronology are not proved by this walker.");
    }
}
