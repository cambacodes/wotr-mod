using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KonomiContactTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string actor = "ca2d58c5c65723945857e04fb85d30ce";
        string[] ordinary = { "margin", "reception", "letter", "evening", "disagreement", "leak", "reckoning",
            "return", "power", "ordinary", "farewell", "parting", "hearing", "hearing_after", "new_letter",
            "political_account", "a_useful_supper", "the_upper_passage", "two_bad_prices", "the_trial_day",
            "a_name_beside_hers", "the_evening_she_kept", "a_turn_for_herself" };
        string[] excluded = { "unsent", "another_evening", "fate_post", "fate_reply", "private_meeting",
            "private_history", "carriers", "before_road", "private_departure", "capital_letter", "return_offer",
            "private_reunion", "lease_offer", "chosen_evening", "private_future_choice", "private_hearing",
            "private_hearing_after", "private_new_letter", "private_political_account", "private_absence",
            "private_absence_catchup", "private_return_terms", "private_kept_hours", "private_last_visit",
            "ending_public", "ending_private", "ending_changed", "ending_ascended", "ending_apart",
            "ending_dismissed_apart", "ending_unfinished", "ending_aeon", "ending_distance",
            "ending_distance_open", "ending_distance_apart", "ending_distance_changed_open",
            "ending_distance_ascended_open", "ending_distance_lived", "ending_distance_open_lived" };
        var scenes = story.Scenes.Where(s => s.Relationship == "konomi").ToArray();
        excluded = excluded.Concat(new[] { "the_unintroduced_letter", "the_answer_she_addressed", "the_courtyard_introduction",
            "ending_missed_declined", "ending_missed_interrupted", "ending_missed_interrupted_aeon", "retained_inquiry", "retained_attempt", "return_letter" }
            .Where(id => scenes.Any(s => s.Id == "konomi." + id))).ToArray();
        var aftercare = new[] { "return_first_words", "return_second_visit" }
            .Where(id => scenes.Any(s => s.Id == "konomi." + id)).ToArray();
        // These later visits declare the same audited physical contact in their source.
        ordinary = ordinary.Concat(new[] { "the_names_admitted", "the_answer_on_record" }
            .Where(id => scenes.Any(s => s.Id == "konomi." + id))).ToArray();
        var native = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SelectedAnswers.Keys).Concat(story.SeenCues.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();
        check(story.Etudes["konomi.present"] == "b5f301fbc4c44535a6309d610d5bd28a", "Konomi ordinary contact lost its real presence gate.");
        check(scenes.Select(s => s.Id).ToHashSet().SetEquals(ordinary.Concat(excluded).Concat(aftercare).Select(id => "konomi." + id)),
            "Konomi contact classification needs review for an added or missing scene.");
        check(scenes.Where(s => s.ContactUnit != null).Select(s => s.Id).ToHashSet().SetEquals(ordinary.Concat(aftercare).Select(id => "konomi." + id)),
            "Konomi contact escaped the audited physical scene set.");
        foreach (string id in aftercare)
        {
            var scene = scenes.Single(s => s.Id == "konomi." + id);
            check(scene.ContactUnit == actor && Rules.IsRemote(scene) && scene.AfterRecovery == "konomi",
                "Aftercare must use current physical contact even though delivered as a book: " + id);
            check(scene.Requires.Contains("konomi.retained_return_confirmed") && scene.Requires.Contains("konomi.return_contact_available")
                && !scene.Requires.Contains("konomi.present"), "Aftercare substitutes office history for verified return: " + id);
        }

        foreach (string id in ordinary)
        {
            var scene = scenes.Single(s => s.Id == "konomi." + id);
            check(scene.ContactUnit == actor && !Rules.IsRemote(scene) && scene.Owner == "Konomi", "Wrong Konomi physical-contact contract: " + id);
            check(scene.Areas.SequenceEqual(new[] { "2570015799edf594daf2f076f2f975d8" })
                && scene.AnswerLists.SequenceEqual(new[] { "0dc8b8604bb33c846a63f3eb62443674" })
                && scene.Requires.Contains("konomi.present"), "Konomi lost native place, dialogue or office evidence.");
            foreach (int chapter in scene.Chapters)
            {
                var state = new Snapshot { Chapter = chapter, Area = scene.Areas.Single(), Hour = 1000 };
                state.Flags.UnionWith(scene.Requires);
                if (scene.RequiresAny.Length > 0) state.Flags.Add(scene.RequiresAny[0]);
                var originalFlags = state.Flags.ToHashSet();
                // Reproduce the previous entry and continuation behavior with the exact scene.
                // Restore the metadata before any later check or shared test can observe it.
                try
                {
                    scene.ContactUnit = null;
                    check(Rules.Available(story, scene, state), "Historical-only Konomi entry reproduction failed: " + id);
                    state.Flags.Remove("konomi.present");
                    check(Rules.ContactAvailable(story, scene, state), "Historical-only continuation reproduction failed: " + id);
                    state.Flags.Add("konomi.present");
                }
                finally { scene.ContactUnit = actor; }
                check(!Rules.Available(story, scene, state), "Konomi entry ignores absent loaded actor: " + id);
                check(!Rules.ContactAvailable(story, scene, state), "Konomi continuation ignores absent loaded actor: " + id);
                state.AvailableContacts.Add(actor);
                check(Rules.Available(story, scene, state) && Rules.ContactAvailable(story, scene, state), "Valid Konomi contact is rejected: " + id);

                state.Flags.Remove("konomi.present");
                check(!Rules.Available(story, scene, state) && !Rules.ContactAvailable(story, scene, state), "Living actor bypasses suspended or completed office state: " + id);
                state.Flags.Add("konomi.present");
                check(Rules.Available(story, scene, state) && Rules.ContactAvailable(story, scene, state), "Temporary rank-up displacement cannot recover: " + id);
                state.AvailableContacts.Clear();
                check(!Rules.ContactAvailable(story, scene, state), "Midscene actor loss is ignored: " + id);
                state.AvailableContacts.Add(actor);
                check(Rules.ContactAvailable(story, scene, state), "Actor restoration cannot resume an eligible conversation: " + id);
                check(state.Flags.SetEquals(originalFlags) && state.Times.Count == 0, "Contact observation mutates history or timing.");

                foreach (var choice in scene.Nodes.SelectMany(n => n.Choices).Where(c => c.Next != null || c.Check != null))
                {
                    var partial = Program.Copy(state);
                    partial.Flags.UnionWith(choice.Set);
                    check(Rules.ContactAvailable(story, scene, partial), "Normal authored midscene effects cut off Konomi: " + id);
                }
                foreach (string flag in scene.Forbids.Where(native.Contains))
                {
                    var blocked = Program.Copy(state); blocked.Flags.Add(flag);
                    check(!Rules.Available(story, scene, blocked) && !Rules.ContactAvailable(story, scene, blocked),
                        "Native Konomi exclusion is ignored during continuation: " + flag);
                    blocked.Flags.Remove(flag);
                    check(Rules.ContactAvailable(story, scene, blocked), "Removing a temporary native exclusion leaves an artificial lockout.");
                }
                foreach (string flag in scene.Forbids.Where(f => !native.Contains(f) && f != "inhuman"))
                {
                    var partial = Program.Copy(state); partial.Flags.Add(flag);
                    check(Rules.ContactAvailable(story, scene, partial), "Authored terminal/closure flag is incorrectly reapplied midscene: " + flag);
                }
                var completed = Program.Copy(state); completed.Flags.Add(scene.Id);
                check(!Rules.Available(story, scene, completed), "Completed Konomi scene replays after a contact restoration.");
                var wrongArea = Program.Copy(state); wrongArea.Area = "";
                check(!Rules.ContactAvailable(story, scene, wrongArea), "Konomi remains available after leaving Drezen.");
                var abyss = Program.Copy(state); abyss.Chapter = 4;
                check(!Rules.ContactAvailable(story, scene, abyss), "Ordinary Konomi contact follows the Commander into the Abyss.");
                var tooSoon = Program.Copy(state);
                foreach (string flag in scene.Requires) tooSoon.Times[flag] = tooSoon.Hour;
                check(Rules.ContactAvailable(story, scene, tooSoon), "Continuation rechecks scene-start delays.");
            }
        }

        foreach (string id in excluded)
        {
            var scene = scenes.Single(s => s.Id == "konomi." + id);
            check(scene.ContactUnit == null, "Ordinary actor requirement attached to excluded delivery: " + id);
            check(Rules.IsRemote(scene) || scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal), "Excluded Konomi delivery changed classification: " + id);
            if (scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
            {
                check(Rules.ContactAvailable(story, scene, new Snapshot()), "Konomi epilogue acquired live continuation gating: " + id);
                continue;
            }
            var remote = new Snapshot
            {
                Chapter = scene.Chapters.FirstOrDefault(scene.MinChapter),
                Area = scene.Areas.FirstOrDefault() ?? "",
                Hour = 1000
            };
            remote.Flags.UnionWith(scene.Requires);
            foreach (var group in scene.RequiresAnyGroups) remote.Flags.Add(group[0]);
            if (scene.RequiresAny.Length > 0) remote.Flags.Add(scene.RequiresAny[0]);
            if (scene.Recovery != null)
            {
                check(!Rules.Available(story, scene, remote), "Remote recovery ignores unavailable retained body: " + id);
                remote.Flags.Add("revive." + scene.Recovery + ".available");
            }
            check(Rules.Available(story, scene, remote), "Konomi remote witness cannot enter: " + id);
            check(remote.AvailableContacts.Count == 0 && Rules.ContactAvailable(story, scene, remote),
                "Valid Konomi remote conversation requires a physical officer: " + id);
        }
        var invitation = scenes.Single(s => s.Id == "konomi.another_evening");
        check(invitation.Requires.Contains("konomi.present") && invitation.ManualOnly && invitation.Remote,
            "Presence-gated solitary invitation was confused with an ordinary meeting.");
        var solitary = new Snapshot { Chapter = 5, Area = invitation.Areas.Single(), Hour = 1000 };
        solitary.Flags.UnionWith(invitation.Requires);
        check(Rules.Available(story, invitation, solitary), "Reading an already received invitation requires a loaded officer view.");
    }
}
