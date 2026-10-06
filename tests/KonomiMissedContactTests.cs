using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KonomiMissedContactTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        story = Program.ArchivedKonomi(story, check); // eng7-l13: live retirement + retained save graph
        var reached = new HashSet<string>();
        const string observed = "konomi.missed_contact_available";
        const string access = "konomi.missed_private_access";
        const string capital = "2570015799edf594daf2f076f2f975d8";
        Scene Get(string id) => story.Scenes.Single(s => s.Id == "konomi." + id);
        Snapshot Earn(string id, Snapshot input, Func<Snapshot, bool>? pick = null)
        {
            var state = Program.Copy(input);
            state.Hour += 1000;
            var scene = Get(id);
            check(Program.CurrentAvailable(story, scene, state), "Played missed-contact continuation unavailable: " + id);
            if (state.Has("konomi.missed_letter_sent"))
            {
                var invalid = Program.Copy(state); invalid.Flags.Add("konomi.missed_contact_invalidated");
                if (!scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
                {
                    check(!Program.CurrentAvailable(story, scene, invalid), "Confirmed incompatible new contact still enters: " + id);
                    check(!Rules.ContactAvailable(story, scene, invalid), "Confirmed incompatible new contact continues: " + id);
                }
            }
            var results = Program.Walk(scene, state, (page, partial) =>
            {
                reached.Add(scene.Id + "/" + page);
                KonomiPolishTests.CheckProvenance(scene, page, partial, check);
            });
            var result = results.First(s => s.Has(scene.Id) && !s.Has("konomi.closed") && (pick == null || pick(s)));
            check(!Program.CurrentAvailable(story, scene, result), "Completed missed-contact scene repeats: " + id);
            return result;
        }

        void InterruptedEnding(Snapshot history)
        {
            foreach (string mythic in new[] { "ordinary", "inhuman", "ascended" })
            {
                var state = Program.Copy(history); state.Chapter = 5;
                state.Flags.Add("konomi.missed_contact_invalidated");
                if (mythic != "ordinary") state.Flags.Add(mythic);
                foreach (var ending in story.Scenes.Where(scene => scene.Relationship == "konomi" && scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                    && !scene.Id.StartsWith("konomi.ending_missed_interrupted", StringComparison.Ordinal)))
                    check(!Program.CurrentAvailable(story, ending, state), "Incompatible new contact still earns living epilogue: " + ending.Id);
                foreach (string id in new[] { "ending_missed_interrupted", "ending_missed_interrupted_aeon" })
                {
                    var ending = Get(id);
                    check(Program.CurrentAvailable(story, ending, state), "Interrupted new history has no honest epilogue: " + id);
                    var pages = new HashSet<string>();
                    var results = Program.Walk(ending, state, (page, _) => pages.Add(page));
                    check(results.All(result => result.Has(ending.Id)), "Interruption ending has no terminal completion.");
                    if (id.EndsWith("_aeon", StringComparison.Ordinal)) continue;
                    string expected = state.Has("konomi.private_consequence_complete") ? "developed"
                        : state.Has("konomi.lovers") ? "affection"
                        : state.Has(access) || state.Has("konomi.private_meeting") ? "meeting" : "invitation";
                    check(pages.Contains(expected), "Interruption ending loses actually earned stage: " + expected);
                    foreach (string other in new[] { "developed", "affection", "meeting", "invitation" }.Where(page => page != expected))
                        check(!pages.Contains(other), "Interruption ending fabricates or downgrades history: " + other);
                    check(pages.Contains("changed") == (mythic == "inhuman") && pages.Contains("ascended") == (mythic == "ascended"),
                        "Interruption ending drops actual mythic state.");
                }
            }
        }

        // This is the observer's explicit contract fixture, not a live native actor observation.
        // No authored predecessor, native dismissal or office completion is seeded.
        foreach (int chapter in new[] { 3, 5 })
        foreach (bool completedOffice in new[] { false, true })
        foreach (bool committed in new[] { false, true })
        {
            var initial = new Snapshot { Chapter = chapter, Hour = 1000, Area = capital };
            initial.Flags.UnionWith(new[] { "trickster", observed, "arueshalae.committed" });
            if (completedOffice) initial.Flags.Add("konomi.office_completed");
            check(!Program.CurrentAvailable(story, Get("fate_post"), initial), "Native-only missed history no longer reproduces old unavailable entry.");
            check(!Program.CurrentAvailable(story, Get("carriers"), initial), "New access invents an already played meeting.");
            var first = Get("the_unintroduced_letter");
            check(Program.CurrentAvailable(story, first, initial), "Observed missed contact has no invitation.");
            foreach (string blocker in new[] { "konomi.present", "konomi.dismissed", "konomi.closed", "konomi.farewell", "inhuman" })
            {
                var blocked = Program.Copy(initial); blocked.Flags.Add(blocker);
                check(!Program.CurrentAvailable(story, first, blocked), "Missed invitation bypasses exclusion " + blocker);
            }
            var unknown = Program.Copy(initial); unknown.Flags.Remove(observed);
            check(!Program.CurrentAvailable(story, first, unknown), "Mere lack of loaded contact proves a correspondent exists.");
            var notTrickster = Program.Copy(initial); notTrickster.Flags.Remove("trickster");
            check(!Program.CurrentAvailable(story, first, notTrickster), "New impossible post lacks current Trickster.");
            var state = Earn("the_unintroduced_letter", initial);
            InterruptedEnding(state);
            check(state.Has("konomi.missed_personal_invitation"), "Invitation with no authored friendship used the wrong branch.");
            state.Flags.Remove("trickster"); state.Flags.Add("legend");
            state.Flags.Remove(observed); // Source unloading is unknown, not evidence of death.
            state.Hour += 1000;
            var refusal = Program.Walk(Get("the_answer_she_addressed"), state).Single(s => s.Has("konomi.missed_declined"));
            InterruptedEnding(refusal);
            check(refusal.Has("konomi.closed") && !refusal.Has(access), "Refusal grants private access.");
            check(!Program.CurrentAvailable(story, Get("the_courtyard_introduction"), refusal), "Refused invitation permits meeting.");
            state = Earn("the_answer_she_addressed", state);
            state = Earn("the_courtyard_introduction", state, s => s.Has("konomi.private_interest"));
            InterruptedEnding(state);
            check(state.Has(access) && !state.Has("konomi.private_meeting"), "New first meeting fabricates old dismissal meeting.");
            if (!completedOffice)
            {
                var nativeTransition = Program.Copy(state);
                nativeTransition.Flags.UnionWith(new[] { "konomi.present", "konomi.missed_contact_invalidated" });
                check(!Program.CurrentAvailable(story, Get("carriers"), nativeTransition), "A later native appointment fails to pause private travel.");
                nativeTransition.Flags.Remove("konomi.present");
                nativeTransition.Flags.Remove("konomi.missed_contact_invalidated");
                nativeTransition.Flags.UnionWith(new[] { "konomi.dismissed", "konomi.office_completed" });
                // Parallel native fixture retains Trickster instead of choosing the Legend transition.
                nativeTransition.Flags.Remove("legend");
                nativeTransition.Flags.Add("trickster");
                foreach (string id in new[] { "fate_post", "fate_reply", "private_meeting" })
                    check(!Program.CurrentAvailable(story, Get(id), nativeTransition), "Established new access replays old acquisition: " + id);
                nativeTransition = Earn("carriers", nativeTransition);
                nativeTransition = Earn("before_road", nativeTransition);
                nativeTransition = Earn("private_departure", nativeTransition);
                check(nativeTransition.Has(access) && nativeTransition.Has("konomi.dismissed") && nativeTransition.Has("konomi.office_completed"),
                    "Later native dismissal cannot continue earned private contact.");
            }
            foreach (string id in new[] { "carriers", "before_road", "private_departure", "capital_letter", "return_offer", "private_reunion", "lease_offer", "chosen_evening" })
                state = Earn(id, state);
            state = Earn("private_future_choice", state, s => s.Has("konomi.committed") == committed);
            state.Chapter = 5;
            // Replay both actual career bargains and both kept-hours choices from this earned undismissed history.
            foreach (bool exclusive in new[] { false, true })
            foreach (bool fullAfternoon in new[] { false, true })
            {
                var visit = Earn("private_return_terms", Program.Copy(state), s => s.Has("konomi.private_career_exclusive") == exclusive);
                visit = Earn("private_kept_hours", visit, s => s.Has("konomi.private_full_afternoon") == fullAfternoon);
                visit = Earn("private_last_visit", visit);
                check(visit.Has("konomi.private_consequence_complete") && !visit.Has("konomi.dismissed"),
                    "Konomi polish: truthful final visit loses its earned career/hours outcome.");
            }
            foreach (string id in new[] { "private_return_terms", "private_kept_hours", "private_last_visit" }) state = Earn(id, state);
            state.Chapter = 5;
            InterruptedEnding(state);
            state = Earn(committed ? "ending_distance_lived" : "ending_distance_open_lived", state);
            check(!state.Has("konomi.dismissed") && state.Has("konomi.office_completed") == completedOffice,
                "Missed-contact campaign rewrites native appointment history.");
            check(state.Has("arueshalae.committed") && state.Has("legend") && !state.Has("trickster"),
                "Private continuation changes another romance or restores lost mythic power.");
        }

        foreach (bool newProvenance in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 3, Hour = 1000, Area = capital };
            state.Flags.UnionWith(new[] { "trickster", "konomi.present" });
            state.AvailableContacts.Add("ca2d58c5c65723945857e04fb85d30ce");
            foreach (string id in new[] { "margin", "reception", "letter", "evening", "disagreement", "leak", "reckoning" })
                state = Earn(id, state);
            check(state.Has("konomi.lovers") && state.Has("konomi.disagreement"), "Established-history witness did not earn its relationship.");
            state.Chapter = 5;
            state.Flags.Remove("konomi.present");
            state.Flags.Add("konomi.office_completed");
            if (newProvenance)
            {
                state.Flags.Add(observed);
                state = Earn("the_unintroduced_letter", state);
                check(state.Has("konomi.missed_lover_invitation") && !state.Has("konomi.missed_personal_invitation"),
                    "Established lover receives a fresh personal introduction.");
                state.Flags.Remove(observed);
                state = Earn("the_answer_she_addressed", state);
                state = Earn("the_courtyard_introduction", state);
            }
            else
            {
                state.Flags.Add("konomi.dismissed");
                foreach (string id in new[] { "fate_post", "fate_reply", "private_meeting" }) state = Earn(id, state);
                check(!state.Has(access), "Old saved dismissal silently imports new provenance.");
            }
            check(!state.Has("konomi.private_history_ready"), "Prior disagreement is skipped by new access.");
            foreach (string id in new[] { "private_history", "carriers", "before_road", "private_departure", "capital_letter", "return_offer", "private_reunion", "private_hearing", "private_hearing_after", "lease_offer", "chosen_evening", "private_future_choice", "private_return_terms", "private_kept_hours", "private_last_visit" })
                state = Earn(id, state);
            check(state.Has("konomi.hearing_finished") && state.Has("konomi.private_consequence_complete"),
                "Established private chain loses its hearing or developed career.");
            check(state.Has("konomi.dismissed") != newProvenance && state.Has(access) == newProvenance,
                "Played alternative rewrites native dismissal or imports access into old history.");
        }

        // Real early personal visits followed by the actual C4 absence and a late C5 catch-up.
        var early = new Snapshot { Chapter = 3, Hour = 1000, Area = capital };
        early.Flags.UnionWith(new[] { "trickster", observed });
        foreach (string id in new[] { "the_unintroduced_letter", "the_answer_she_addressed", "the_courtyard_introduction", "carriers", "before_road", "private_departure" })
            early = Earn(id, early);
        early.Flags.Remove(observed); early.Chapter = 4;
        early = Earn("private_absence", early);
        early.Chapter = 5;
        foreach (string id in new[] { "capital_letter", "return_offer" }) early = Earn(id, early);
        early = Earn("private_reunion", early, result => !result.Has("konomi.private_absence_answered"));
        early = Earn("private_political_account", early);
        foreach (string id in new[] { "lease_offer", "chosen_evening", "private_future_choice", "private_return_terms", "private_kept_hours", "private_last_visit", "private_absence_catchup" })
            early = Earn(id, early);
        check(early.Has("konomi.private_absence_answered") && early.Has("konomi.private_consequence_complete"),
            "Late catch-up loses the earned completed career.");

        // Explore actual ordinary choices, retaining distinct earned histories rather than seeding authored flags.
        var seed = new Snapshot { Chapter = 3, Hour = 1000, Area = capital };
        seed.Flags.UnionWith(new[] { "trickster", "konomi.present" });
        seed.AvailableContacts.Add("ca2d58c5c65723945857e04fb85d30ce");
        var frontier = new List<Snapshot> { seed };
        var beforeReckoning = new List<Snapshot>();
        foreach (string id in new[] { "margin", "reception", "letter", "evening", "disagreement", "leak", "reckoning" })
        {
            if (id == "reckoning") beforeReckoning = frontier.ToList();
            var next = new Dictionary<string, Snapshot>();
            foreach (var state in frontier)
            {
                state.Hour += 1000;
                check(Program.CurrentAvailable(story, Get(id), state), "Ordinary history generator bypassed entry: " + id);
                foreach (var result in Program.Walk(Get(id), state).Where(r => r.Has(Get(id).Id) && !r.Has("konomi.closed")))
                    next[string.Join("|", result.Flags.OrderBy(f => f))] = result;
            }
            frontier = next.Values.ToList();
        }
        // Flags below select genuinely played branches; they are never inserted into the snapshots.
        var histories = frontier.Concat(beforeReckoning).GroupBy(state => string.Join("|", new[] { "konomi.public", "konomi.petition_resolved", "konomi.almost_denied", "konomi.apologized" }
            .Where(state.Has))).Select(group => group.First()).ToList();
        foreach (var prior in histories.Where(state => state.Has("konomi.scandal_answered")).ToArray())
        {
            var heard = Earn("hearing", prior);
            heard = Earn("hearing_after", heard);
            histories.Add(heard);
        }
        foreach (var prior in histories)
        {
            var state = Program.Copy(prior);
            state.Chapter = 4;
            state = Earn("unsent", state);
            state.Chapter = 5;
            if (state.Has("konomi.reckoning")) state = Earn("return", state);
            // Modified completed-office-without-dismissal compatibility, not a claimed ordinary native branch.
            state.Flags.Remove("konomi.present"); state.Flags.Add("konomi.office_completed"); state.Flags.Add(observed);
            foreach (string id in new[] { "the_unintroduced_letter", "the_answer_she_addressed", "the_courtyard_introduction", "private_history", "carriers", "before_road", "private_departure", "capital_letter", "return_offer" })
                state = Earn(id, state);
            state = Earn("private_reunion", state, result => !result.Has("konomi.private_absence_answered"));
            state = Earn("private_absence_catchup", state);
            // Native council testimony is a separate controlled fact for the conditional political text.
            state.Flags.Add("konomi.council_conclusion_seen");
            state = Earn("private_political_account", state);
        }

        foreach (var book in story.Scenes.Where(scene => scene.Relationship == "konomi"))
        foreach (var page in book.Nodes.Where(node => node.Id.StartsWith("missed_", StringComparison.Ordinal)))
            check(reached.Contains(book.Id + "/" + page.Id), "New history variant never reached through played choices: " + book.Id + "/" + page.Id);
    }
}
