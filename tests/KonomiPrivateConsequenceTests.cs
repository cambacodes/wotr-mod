using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KonomiPrivateConsequenceTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Get(string id) => story.Scenes.Single(s => s.Id == "konomi." + id);
        var visits = new[] { Get("private_return_terms"), Get("private_kept_hours"), Get("private_last_visit") };
        var reached = new HashSet<string>();
        var protectedFlags = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys)
            .Concat(new[] { "trickster", "legend", "konomi.committed", "konomi.private_future_open",
                "konomi.private_absence_answered", "arueshalae.committed", "jerribeth.committed" }).Distinct().ToArray();

        Snapshot Earn(string id, Snapshot state, Func<Snapshot, bool>? predicate = null)
        {
            state.Hour += 1000;
            var scene = Get(id);
            check(Rules.Available(story, scene, state), "Unavailable played Konomi predecessor: " + id);
            return Program.Walk(scene, state).First(s => s.Has(scene.Id) && !s.Has("konomi.closed") && (predicate == null || predicate(s)));
        }

        List<Snapshot> Walk(Scene scene, Snapshot state)
        {
            check(Rules.Available(story, scene, state), "Unavailable Konomi consequence: " + scene.Id);
            var results = Program.Walk(scene, state, (page, partial) =>
            {
                reached.Add(scene.Id + "/" + page);
                check(partial.Flags.SetEquals(state.Flags), "Unfinished Konomi page persists decisions: " + page);
                check(partial.Times.OrderBy(p => p.Key).SequenceEqual(state.Times.OrderBy(p => p.Key)), "Unfinished Konomi page changes timestamps.");
            });
            foreach (var result in results)
            {
                foreach (string flag in protectedFlags)
                    check(result.Has(flag) == state.Has(flag), "Konomi consequence changes protected history: " + flag);
                if (!result.Has(scene.Id)) check(result.Flags.SetEquals(state.Flags), "Deferring Konomi consequence changes history.");
                else check(!Rules.Available(story, scene, result), "Konomi consequence repeats after completion.");
            }
            return results.Where(s => s.Has(scene.Id)).ToList();
        }

        foreach (bool established in new[] { false, true })
        foreach (bool acceptNow in new[] { false, true })
        foreach (bool committed in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 3, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(new[] { "trickster", "arueshalae.committed", "jerribeth.committed" });
            if (established)
            {
                state.Flags.Add("konomi.present");
                foreach (string id in new[] { "margin", "reception", "letter", "evening", "disagreement", "leak", "reckoning" }) state = Earn(id, state);
                state.Flags.Remove("konomi.present");
            }
            state.Flags.UnionWith(new[] { "konomi.dismissed", "konomi.office_completed" });
            foreach (string id in new[] { "fate_post", "fate_reply", "private_meeting" }) state = Earn(id, state);
            if (!state.Has("konomi.private_history_ready")) state = Earn("private_history", state);
            foreach (string id in new[] { "carriers", "before_road", "private_departure" }) state = Earn(id, state);
            // Only half the histories opt into the new absence; both retain later career access.
            if (established)
            {
                state.Chapter = 4;
                state = Earn("private_absence", state);
            }
            state.Chapter = 5;
            foreach (string id in new[] { "capital_letter", "return_offer", "private_reunion" }) state = Earn(id, state);
            if (established)
            {
                foreach (string id in new[] { "private_hearing", "private_hearing_after" }) state = Earn(id, state);
            }
            state = Earn("lease_offer", state, s => s.Has("konomi.career_accepts_now") == acceptNow);
            state = Earn("chosen_evening", state, s => s.Has("konomi.private_evening_kept"));
            state = Earn("private_future_choice", state, s => s.Has("konomi.committed") == committed);
            // A current Legend keeps the actual prior Trickster acquisition rather than regranting its power.
            if (established) { state.Flags.Remove("trickster"); state.Flags.Add("legend"); }
            state.Hour += 1000;
            string oldEnding = committed ? "ending_distance" : "ending_distance_open";
            string newEnding = committed ? "ending_distance_lived" : "ending_distance_open_lived";
            check(Rules.Available(story, Get(oldEnding), state), "Older private future lost its short-course ending.");
            check(!Rules.Available(story, Get(newEnding), state), "Unplayed consequence earns developed ending.");
            var lateInstall = Program.Copy(state);
            lateInstall.Flags.Add(Get(oldEnding).Id);
            lateInstall.Times[Get(oldEnding).Id] = state.Hour - 1;
            check(Rules.Available(story, visits[0], lateInstall), "Historical ending record prevents explicit late-install opt-in.");
            var latePlayed = Program.Walk(visits[0], lateInstall).First(s => s.Has(visits[0].Id));
            check(latePlayed.Has(Get(oldEnding).Id) && latePlayed.Times[Get(oldEnding).Id] == lateInstall.Times[Get(oldEnding).Id],
                "Late-install opt-in rewrites a recorded old ending.");
            check(visits[0].ManualOnly && visits[2].ManualOnly, "Late-install or final farewell is no longer explicit opt-in.");
            check(!Rules.Available(story, visits[1], state) && !Rules.Available(story, visits[2], state), "Consequences bypass their played prerequisites.");

            foreach (var agreement in Walk(visits[0], state))
            {
                check(agreement.Has("konomi.private_career_exclusive") != agreement.Has("konomi.private_career_portfolio"), "Career arrangements overlap.");
                check(Rules.Available(story, Get(oldEnding), agreement), "Partially played addition lost old ending.");
                check(!Rules.Available(story, visits[1], agreement), "Next visit ignores its wait.");
                agreement.Hour += 1000;
                foreach (var afternoon in Walk(visits[1], agreement))
                {
                    check(afternoon.Has("konomi.private_extra_fee") != afternoon.Has("konomi.private_full_afternoon"), "Visit costs overlap.");
                    check(Rules.Available(story, Get(oldEnding), afternoon), "Skipping optional farewell blocks old ending.");
                    afternoon.Hour += 1000;
                    foreach (var farewell in Walk(visits[2], afternoon))
                    {
                        check(farewell.Has("konomi.private_consequence_complete"), "Played farewell lacks completion.");
                        check(!Rules.Available(story, Get(oldEnding), farewell), "Old and developed endings overlap.");
                        check(Rules.Available(story, Get(newEnding), farewell), "Earned developed ending unavailable.");
                        var wrong = Get(committed ? "ending_distance_open_lived" : "ending_distance_lived");
                        check(!Rules.Available(story, wrong, farewell), "Open and committed endings overlap.");
                        foreach (var end in Walk(Get(newEnding), farewell))
                            check(end.Has(Get(newEnding).Id), "Developed epilogue has no terminal path.");
                    }
                }
            }
        }

        foreach (var scene in visits)
        {
            var ready = new Snapshot { Chapter = 5, Hour = 50000, Area = scene.Areas.Single() };
            ready.Flags.UnionWith(scene.Requires);
            ready.Flags.Add("konomi.career_accepts_now");
            ready.Flags.Add("konomi.private_career_exclusive");
            ready.Flags.Add("konomi.private_extra_fee");
            check(Rules.Available(story, scene, ready), "New visit baseline unavailable.");
            foreach (string flag in scene.Requires)
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(flag);
                check(!Rules.Available(story, scene, missing), "Missing earned prerequisite admitted: " + flag);
            }
            foreach (string flag in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag);
                check(!Rules.Available(story, scene, blocked), "Blocked native/history state admitted: " + flag);
            }
            foreach (int chapter in new[] { 3, 4, 6 })
            { var wrong = Program.Copy(ready); wrong.Chapter = chapter; check(!Rules.Available(story, scene, wrong), "Private finale wrong chapter."); }
            var elsewhere = Program.Copy(ready); elsewhere.Area = "abyss";
            check(!Rules.Available(story, scene, elsewhere), "Private finale outside authored visit location.");
        }
        foreach (var scene in visits.Concat(new[] { Get("ending_distance_lived"), Get("ending_distance_open_lived") }))
            foreach (var node in scene.Nodes)
                check(reached.Contains(scene.Id + "/" + node.Id), "Unplayed new Konomi page: " + scene.Id + "/" + node.Id);
    }
}
