using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class NocticulaAcquisitionTests
{
    // Play selected addon effects through the shared walker; native events are explicit fixture boundaries.
    internal static void Run(Story story, Action<bool, string> check)
    {
        story = Program.Unfolded(story);   // NM1: judged per letter; the folded deliveries are Nm1BudgetTests
        var scenes = story.Scenes.Where(s => s.Relationship == "nocticula.acquisition"
                                             && !s.Id.StartsWith("nocticula.trickster.", StringComparison.Ordinal)).ToArray();
        if (scenes.Length == 0) return;
        var entries = scenes.Where(s => s.Id.StartsWith("noct.acq.audience_", StringComparison.Ordinal)).ToArray();
        check(entries.Length == 3, "Nocticula acquisition must have three reviewed living history entries.");
        var preparation = scenes.Single(s => s.Id == "noct.acq.the_missing_line");
        var reply = scenes.Single(s => s.Id == "noct.acq.her_hand");
        var living = entries.Concat(new[] { preparation, reply }).ToArray();
        var reached = living.ToDictionary(s => s.Id, _ => new HashSet<string>());
        var native = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.SeenCues.Keys)
            .Concat(story.SelectedAnswers.Keys).Concat(story.CompletedQuests.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();
        check(living.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).All(c => c.Revive == null
            && c.Set.All(flag => (flag.StartsWith("noct.acq.", StringComparison.Ordinal)
                                  // 15b T1 (PP4): the request's two Gresilla outcomes keep the spec's exact names.
                                  || flag == "nocticula.gresilla_credited" || flag == "nocticula.gresilla_exposed")
                                 && !native.Contains(flag))),
            "Acquisition writes native evidence, parent state or an actor recovery.");

        string[][] histories = {
            Array.Empty<string>(), new[] { "noct.gift" },
            new[] { "noct.parent_rejected" }, new[] { "noct.parent_rejected", "noct.gift" },
            new[] { "noct.parent_active", "noct.acq.original_gift_completed" },
            new[] { "noct.parent_active", "noct.acq.original_gift_completed", "noct.acq.gift_renewed" }
        };
        int trials = 0, initialDeclines = 0, laterClosures = 0, postponements = 0;
        Snapshot Initial(IEnumerable<string> history)
        {
            var state = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(new[] { "trickster", "noct.acq.audience_question", "seelah.committed", "arueshalae.committed" });
            state.Flags.UnionWith(history);
            return state;
        }
        void NativeUnchanged(Snapshot expected, Snapshot actual)
        {
            check(expected.Flags.Where(native.Contains).ToHashSet().SetEquals(actual.Flags.Where(native.Contains)),
                "Selected acquisition choices changed native or parent history.");
            check(actual.Has("seelah.committed") && actual.Has("arueshalae.committed"),
                "Acquisition removed another romance.");
            check(actual.AvailableContacts.Count == 0, "Correspondence manufactured a physical actor.");
        }
        void Closed(Snapshot state)
        {
            var later = Program.Copy(state); later.Hour += 1000;
            check(living.All(s => !Program.CurrentAvailable(story, s, later)), "Closed acquisition offers another living visit.");
            check(!state.Has("noct.acq.correspondence_trial") && !state.Has("noct.acq.renewed_agreement"),
                "Refusal incorrectly completes a trial or romance.");
        }
        List<Snapshot> Walk(Scene scene, Snapshot state) => Program.Walk(scene, state,
            (node, partial) => reached[scene.Id].Add(node));

        foreach (var history in histories)
        {
            var initial = Initial(history);
            var available = entries.Where(s => Program.CurrentAvailable(story, s, initial)).ToArray();
            check(available.Length == 1, "Native history does not select exactly one acquisition entry.");
            var entry = available.Single();
            var kinds = new HashSet<string>();
            int historyTrials = 0;
            foreach (var requested in Walk(entry, initial))
            {
                NativeUnchanged(initial, requested);
                check(!Program.CurrentAvailable(story, entry, requested), "Completed or declined request repeats.");
                if (requested.Has("noct.acq.closed"))
                {
                    initialDeclines++;
                    check(!requested.Has("noct.acq.requested") && !requested.Has("noct.acq.seal_received"),
                        "Early or late request refusal received the seal or accepted the request.");
                    Closed(requested);
                    continue;
                }
                check(requested.Has("noct.acq.requested") && requested.Has("noct.acq.seal_received")
                    && requested.Has("noct.acq.petition_candid") != requested.Has("noct.acq.petition_watchful"),
                    "Accepted request lacks its selected seal attitude or earned seal.");
                var ready = Program.Copy(requested); ready.Hour += preparation.DelayHours;
                check(!Program.CurrentAvailable(story, preparation, ready), "Remote preparation bypassed genuine Council evidence.");
                // NOC-02: any one native answer at the audience earns the channel; overhearing the scheme alone does not.
                var overheard = Program.Copy(ready); overheard.Flags.Add("noct.socoth_plan_exposed");
                check(!Program.CurrentAvailable(story, preparation, overheard), "Overhearing the scheme alone unlocks remote preparation.");
                foreach (string evidence in new[] { "noct.acq.council_disclosed", "noct.acq.shamira_permission", "noct.acq.shamira_reported", "noct.acq.amused" })
                {
                    var onlyOne = Program.Copy(ready); onlyOne.Flags.Add(evidence);
                    check(Program.CurrentAvailable(story, preparation, onlyOne), "A native audience answer does not unlock remote preparation: " + evidence);
                }
                // The actual native disclosure and reward must occur outside this source walker.
                ready.Flags.UnionWith(new[] { "noct.acq.council_disclosed", "noct.socoth_plan_exposed" });
                check(Program.CurrentAvailable(story, preparation, ready), "Accepted request plus both native events cannot reach preparation.");
                foreach (var sent in Walk(preparation, ready))
                {
                    NativeUnchanged(ready, sent);
                    if (!sent.Has(preparation.Id))
                    {
                        postponements++;
                        check(sent.Flags.SetEquals(ready.Flags) && sent.Times.Count == ready.Times.Count
                            && ready.Times.All(pair => sent.Times.TryGetValue(pair.Key, out int time) && time == pair.Value),
                            "Postponement changes acquisition state or timestamps.");
                        check(Program.CurrentAvailable(story, preparation, sent), "Postponed preparation cannot be retried.");
                        var waited = Program.Copy(sent); waited.Hour += 1000;
                        check(!Program.CurrentAvailable(story, reply, waited), "Postponement fabricates the sent question.");
                        continue;
                    }
                    check(sent.Has("noct.acq.question_sent") && sent.Has("noct.acq.channel_narrow") != sent.Has("noct.acq.channel_slow"),
                        "Prepared request lacks a single selected channel.");
                    check(!Program.CurrentAvailable(story, reply, sent), "Reply ignores its wait after the question.");
                    var answered = Program.Copy(sent); answered.Hour += reply.DelayHours;
                    check(Program.CurrentAvailable(story, reply, answered), "Actually prepared channel cannot reach the reply.");
                    foreach (var final in Walk(reply, answered))
                    {
                        NativeUnchanged(ready, final);
                        check(!final.Has("noct.acq.renewed_agreement") && !final.Has("noct.complete"),
                            "A preliminary reply claims completed courtship or harbor completion.");
                        if (final.Has("noct.acq.closed"))
                        {
                            laterClosures++;
                            check(final.Has("noct.acq.channel_exposed") && !final.Has("noct.acq.sketch_surrendered"),
                                "Reply closure is not the actual refused-sketch branch.");
                            Closed(final);
                            continue;
                        }
                        check(final.Has(reply.Id) && final.Has("noct.acq.correspondence_trial"), "Reply ends without the earned trial.");
                        check(final.Has("noct.acq.channel_provisional") != final.Has("noct.acq.channel_letters_only"),
                            "Trial has overlapping or missing channel outcomes.");
                        if (final.Has("noct.acq.channel_exposed"))
                        {
                            check(final.Has("noct.acq.channel_attempted") && final.Has("noct.acq.sketch_surrendered")
                                && final.Has("noct.acq.channel_repaired") && final.Has("noct.acq.channel_letters_only"),
                                "Exposed channel loses its attempt, surrender cost or repaired letter limitation.");
                            kinds.Add("repaired");
                        }
                        else kinds.Add(final.Has("noct.acq.channel_provisional") ? "narrow" : "letters");
                        check(!Program.CurrentAvailable(story, reply, final), "Completed reply repeats.");
                        trials++; historyTrials++;
                    }
                }
            }
            check(historyTrials == 6 && kinds.SetEquals(new[] { "narrow", "letters", "repaired" }),
                "A living history lost a candid/watchful channel outcome.");
        }
        check(trials == 36 && initialDeclines == 12 && laterClosures == 12 && postponements == 12,
            "Assembled acquisition outcome counts changed; inspect new paths before updating expectations.");
        // PP4 (pacing_pp4.py) appends nodes gated on its own beats (Gresilla's credit, the Chapter 4 hoard); PacingPP4Tests walks them.
        var pp4 = new HashSet<string> { "harp", "author", "hoard_appraised", "hoard_bitten", "hoard_spent",
                                        "call_names", "call_fear", "call_harp", "call_con", "refused", "unsigned" };
        foreach (var scene in living)
            // The scent_* nodes answer the Trickster voice at the audience; NocticulaTricksterTests walks them.
            check(reached[scene.Id].SetEquals(scene.Nodes.Select(n => n.Id).Where(id => !id.StartsWith("scent_", StringComparison.Ordinal) && !pp4.Contains(id))),
                "Assembled acquisition missed authored nodes: " + scene.Id);
        foreach (string blocker in new[] { "noct.dead", "noct.acq.council_fight", "swarm", "legend", "dragon" })
        {
            var blocked = Initial(new[] { blocker });
            check(entries.All(s => !Program.CurrentAvailable(story, s, blocked)), "Blocked acquisition history offers an audience entry: " + blocker);
        }
        var intact = Initial(new[] { "noct.parent_active", "noct.gift" });
        check(entries.All(s => !Program.CurrentAvailable(story, s, intact)), "Intact original patronage incorrectly offers reacquisition.");
        var rejected = Initial(new[] { "noct.parent_active", "noct.parent_rejected" });
        check(entries.Where(s => Program.CurrentAvailable(story, s, rejected)).Select(s => s.Id)
            .SequenceEqual(new[] { "noct.acq.audience_rejected" }), "Rejected history does not take precedence over Active.");
        var ordinary = Initial(Array.Empty<string>()); ordinary.Flags.Remove("trickster");
        check(entries.All(s => !Program.CurrentAvailable(story, s, ordinary)), "Non-Trickster acquired the bespoke audience route.");
        Console.WriteLine("Nocticula assembled acquisition: 6 native-history fixtures, 36 trial outcomes; native audience execution not claimed.");
    }
}
