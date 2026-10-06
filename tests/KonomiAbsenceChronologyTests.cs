using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KonomiAbsenceChronologyTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        story = Program.ArchivedKonomi(story, check); // exercise the retained save graph after verifying live retirement
        Scene Get(string id) => story.Scenes.Single(s => s.Id == "konomi." + id);
        var catchup = Get("private_absence_catchup");
        var reached = new HashSet<string>();
        Snapshot Earn(string id, Snapshot input, Func<Snapshot, bool>? select = null)
        {
            var state = Program.Copy(input);
            state.Hour += 1000;
            var scene = Get(id);
            check(Program.CurrentAvailable(story, scene, state), "Chronology predecessor unavailable: " + id);
            return Program.Walk(scene, state).First(s => s.Has(scene.Id) && !s.Has("konomi.closed") && (select == null || select(s)));
        }
        void Inspect(Snapshot state, string? expected)
        {
            check(Program.CurrentAvailable(story, catchup, state), "Deferred catch-up lost eligibility.");
            foreach (string origin in new[] { "absence_now", "absence_her_days" })
            {
                var page = catchup.Nodes.Single(n => n.Id == origin);
                var career = page.Choices.Where(c => c.Next != null && c.Next.StartsWith("absence_career_") && Rules.Match(c.Requires, c.Forbids, state)).ToList();
                check(career.Count == (expected == null ? 0 : 1), "Career stage overlaps or is absent at " + origin);
                if (expected != null) check(career.Single().Next == "absence_career_" + expected, "Catch-up recalls the wrong earned stage.");
                check(page.Choices.Take(3).All(c => c.Next is "absence_legend" or "absence_trickster" or "absence_mortal"), "Existing mythic answer indices moved.");
            }
            var pages = new HashSet<string>();
            var outcomes = Program.Walk(catchup, state, (id, partial) =>
            {
                pages.Add(id); reached.Add(id);
                check(partial.Flags.SetEquals(state.Flags), "Unfinished recollection persists history.");
                check(partial.Times.OrderBy(p => p.Key).SequenceEqual(state.Times.OrderBy(p => p.Key)), "Unfinished recollection changes timestamps.");
            });
            if (expected != null) check(pages.Contains("absence_career_" + expected), "Earned recollection cannot be played.");
            check(!catchup.Nodes.Single(n => n.Id == "absence_now").Text.Contains("do not yet know which job"), "Catch-up forgets the played career.");
            check(outcomes.Any(s => !s.Has(catchup.Id) && s.Flags.SetEquals(state.Flags)), "Catch-up cannot be deferred unchanged.");
            foreach (var result in outcomes.Where(s => s.Has(catchup.Id)))
            {
                check(state.Flags.IsSubsetOf(result.Flags), "Catch-up removes existing history.");
                foreach (var pair in state.Times) check(result.Times[pair.Key] == pair.Value, "Catch-up rewrites an earned timestamp.");
                check(result.Flags.Except(state.Flags).All(f => f == catchup.Id || f == "konomi.private_absence_answered" || f == "konomi.absence_reunion_kissed"), "Catch-up changes a career, partner or native flag.");
                check(result.Has("konomi.private_absence_answered") && !Program.CurrentAvailable(story, catchup, result), "Acknowledged catch-up replays.");
            }
            foreach (string flag in catchup.Forbids.Concat(new[] { "konomi.closed" }))
            {
                var blocked = Program.Copy(state); blocked.Flags.Add(flag);
                check(!Program.CurrentAvailable(story, catchup, blocked), "Catch-up ignores native/relationship blocker: " + flag);
            }
        }

        // Native rank-six dismissal is a Chapter 5 endpoint, not a Chapter 3 dismissal fixture.
        var beginning = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
        beginning.Flags.UnionWith(new[] { "trickster", "konomi.dismissed", "konomi.office_completed", "arueshalae.committed", "jerribeth.committed" });
        foreach (string id in new[] { "fate_post", "fate_reply", "private_meeting", "carriers", "before_road", "private_departure", "capital_letter", "return_offer", "private_reunion" })
            beginning = Earn(id, beginning, s => !s.Has("konomi.private_absence_answered"));
        Inspect(beginning, null);
        check(!beginning.Has("konomi.private_absence_kept"), "Chapter 5 acquisition invented an Abyss private absence.");
        foreach (bool immediate in new[] { false, true })
        {
            var decision = Earn("lease_offer", beginning, s => s.Has("konomi.career_accepts_now") == immediate);
            string initial = immediate ? "decision_now" : "decision_wait";
            Inspect(decision, initial);
            var evening = Earn("chosen_evening", decision, s => s.Has("konomi.private_evening_kept"));
            Inspect(evening, initial);
            foreach (bool committed in new[] { false, true })
            {
                var future = Earn("private_future_choice", evening, s => s.Has("konomi.committed") == committed);
                foreach (bool exclusive in new[] { false, true })
                {
                    string agreement = exclusive ? "exclusive" : "portfolio";
                    var sent = Earn("private_return_terms", future, s => s.Has("konomi.private_career_exclusive") == exclusive);
                    Inspect(sent, "terms_" + agreement);
                    foreach (bool extraFee in new[] { false, true })
                    {
                        var paid = Earn("private_kept_hours", sent, s => s.Has("konomi.private_extra_fee") == extraFee);
                        Inspect(paid, "paid_" + agreement);
                        var finished = Earn("private_last_visit", paid);
                        check(finished.Has("konomi.private_consequence_complete"), "Reproduction did not finish the career farewell.");
                        foreach (string mythic in new[] { "trickster", "legend", "other" })
                        {
                            var current = Program.Copy(finished); current.Flags.Remove("trickster");
                            if (mythic != "other") current.Flags.Add(mythic);
                            Inspect(current, "settled_" + agreement);
                        }
                        // Retained historical record compatibility only, not native proof of early dismissal.
                        var legacy = Program.Copy(finished);
                        legacy.Flags.UnionWith(new[] { "konomi.private_absence_kept", "konomi.absence_memory", "konomi.absence_changed" });
                        Inspect(legacy, "settled_" + agreement);
                    }
                }
            }
        }
        foreach (var page in catchup.Nodes.Where(n => n.Id.StartsWith("absence_career_")))
            check(reached.Contains(page.Id), "Unplayed chronology repair page: " + page.Id);
        check(Get("private_reunion").Nodes.All(n => !n.Id.StartsWith("absence_career_")), "Later career recollection leaked into initial reunion.");
        check(catchup.ManualOnly && catchup.Remote, "Optional acknowledgement entered mandatory progression.");
    }
}
