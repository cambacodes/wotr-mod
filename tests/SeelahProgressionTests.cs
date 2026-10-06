using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class SeelahProgressionTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Scene(string id) => story.Scenes.Single(s => s.Id == "seelah." + id);
        Snapshot Play(string id, Snapshot input, Func<Snapshot, bool>? select = null)
        {
            var scene = Scene(id);
            var state = Program.Copy(input);
            state.Area = scene.Areas.FirstOrDefault() ?? state.Area;
            state.Hour += scene.DelayHours;
            check(Program.CurrentAvailable(story, scene, state), "Seelah actual chain cannot enter " + id);
            var result = Program.Walk(scene, state).FirstOrDefault(s => s.Has(scene.Id) && !s.Has("seelah.closed") && (select == null || select(s)));
            check(result != null, "Seelah actual chain cannot finish " + id);
            return result!;
        }
        Snapshot Core(int chapter)
        {
            var state = new Snapshot { Chapter = chapter, Hour = 1000, Area = Scene("road").Areas.Single() };
            state.Flags.UnionWith(new[] { "chapter_later", "konomi.committed", "kiana.committed" });
            foreach (string id in new[] { "boots", "wager", "promise", "door", "morning", "weight" })
                state = Play(id, state, id == "promise" ? s => s.Has("seelah.courting") : null);
            return state;
        }
        Snapshot Activity(Snapshot input, bool watching)
        {
            var state = Program.Copy(input); state.Chapter = 5;
            foreach (string id in new[] { "borrowed_saw", "platform_finished", "inheritors_corner", "roof_evening" }) state = Play(id, state);
            state = Play("late_course", state, s => s.Has(watching ? "seelah.late_watching" : "seelah.late_running"));
            state = Play("late_lesson", state);
            return Play("late_page", state);
        }

        var road = Scene("road");
        var core = Core(5);
        core.Hour += road.DelayHours;
        check(Program.CurrentAvailable(story, road, core), "Early future discussion is hidden instead of explaining its requirements.");
        var early = Program.Walk(road, core);
        check(early.All(s => !s.Has("seelah.developed_commitment")), "Old short core still earns developed commitment.");
        var shortRoute = early.First(s => s.Has("seelah.short_future_chosen"));
        check(shortRoute.Has("seelah.committed") && shortRoute.Has("seelah.road"), "Explicit modest future does not preserve compatible progress.");
        foreach (var deferred in early.Where(s => !s.Has(road.Id)))
            check(deferred.Flags.SetEquals(core.Flags), "Readiness deferral grants history or closes road.");
        shortRoute = Play("ordinary", shortRoute);
        var farewell = Scene("farewell");
        shortRoute.Hour += farewell.DelayHours;
        var farewells = Program.Walk(farewell, shortRoute);
        check(farewells.Any(s => !s.Has(farewell.Id) && s.Flags.SetEquals(shortRoute.Flags)), "Farewell cannot be deferred without closing the route.");
        var oldFarewell = farewells.First(s => s.Has(farewell.Id));
        check(!oldFarewell.Has("seelah.developed_commitment"), "Farewell silently upgrades modest history.");
        var catchup = Play("farewell_catchup", oldFarewell);
        check(catchup.Has("seelah.farewell") && catchup.Has("seelah.catchup_requested"), "Catch-up erases farewell history.");
        check(!Program.CurrentAvailable(story, Scene("farewell_catchup"), catchup), "Catch-up invitation repeats after acceptance.");
        var saw = Scene("borrowed_saw");
        oldFarewell.Hour += saw.DelayHours; catchup.Hour += saw.DelayHours;
        check(!Program.CurrentAvailable(story, saw, oldFarewell), "Old farewell reopens expansion without consent.");
        check(Program.CurrentAvailable(story, saw, catchup), "Explicit catch-up does not reopen the first missed scene.");
        foreach (string flag in new[] { "seelah.closed", "seelah_dead", "seelah_gone", "inhuman" })
        {
            var blocked = Program.Copy(catchup); blocked.Flags.Add(flag);
            check(!Program.CurrentAvailable(story, saw, blocked), "Farewell override bypasses " + flag);
        }

        foreach (bool watching in new[] { false, true })
        {
            var prepared = Activity(Core(5), watching);
            var race = Scene("late_race"); prepared.Hour += race.DelayHours;
            var raceResults = Program.Walk(race, prepared).Where(s => s.Has(race.Id)).ToList();
            check(raceResults.Count > 0, "No actual race conclusion.");
            if (!watching)
            {
                check(raceResults.Any(s => s.Has("seelah.late_race_won")), "Race success omitted from commitment test.");
                check(raceResults.Any(s => s.Has("seelah.late_race_stumbled")), "Race failure omitted from commitment test.");
                check(raceResults.Any(s => s.Has("seelah.late_wide_turn")), "Non-roll race alternative omitted.");
            }
            foreach (var result in raceResults)
            {
                result.Hour += road.DelayHours;
                var outcomes = Program.Walk(road, result);
                check(outcomes.Any(s => s.Has("seelah.developed_commitment")), "Legitimate race outcome cannot earn developed commitment.");
                check(outcomes.Where(s => s.Has("seelah.developed_commitment")).All(s => s.Has("seelah.committed") && s.Has("seelah.chosen_future")), "Developed marker appears without acceptance.");
                check(outcomes.All(s => s.Has("konomi.committed") && s.Has("kiana.committed")), "Seelah progression changes other romances.");
            }
        }

        // Leave the real authored Abyss chain at each supported point, then return to Act 5.
        var abyssBase = Core(3); abyssBase.Chapter = 4;
        abyssBase = Play("watch", abyssBase);
        var letter = Scene("letter"); abyssBase.Area = letter.Areas.Single(); abyssBase.Hour += letter.DelayHours;
        foreach (string harm in new[] { "seelah.letter_public", "seelah.letter_burned" })
        {
            var incident = Program.Walk(letter, abyssBase).First(s => s.Has(letter.Id) && s.Has(harm));
            foreach (bool discussed in new[] { false, true })
            {
                var history = discussed ? Play("letter_after", incident) : Program.Copy(incident);
                var prepared = Activity(history, false);
                prepared = Play("late_race", prepared);
                prepared.Hour += road.DelayHours;
                check(Program.Walk(road, prepared).All(s => !s.Has(road.Id) && !s.Has("seelah.developed_commitment")), "Unresolved Abyss harm permits future completion.");
                var bridge = Play("letter_return", prepared);
                check(!bridge.Has("seelah.copyist_followed"), "Return bridge invents the Abyss follow-up.");
                var accepted = Play("road", bridge, s => s.Has("seelah.developed_commitment"));
                check(accepted.Has(harm) && accepted.Has("seelah.letter_unsettled"), "Progression erases the original harm history.");
            }
            var followed = Play("letter_work", Play("letter_after", incident));
            var ready = Play("late_race", Activity(followed, true));
            check(!Program.CurrentAvailable(story, Scene("letter_return"), ready), "Resolved copyist history receives the catch-up.");
            Play("road", ready, s => s.Has("seelah.developed_commitment"));
        }

        // Native outcome changes after the earlier faith conversation must be read afresh.
        var earned = Play("late_race", Activity(Core(5), false));
        foreach (string outcome in new[] { "unfinished", "returned", "moderate", "bad" })
        foreach (bool dead in new[] { false, true })
        {
            var current = Program.Copy(earned);
            if (outcome != "unfinished") current.Flags.Add("seelah.souls_returned");
            if (outcome == "moderate" || outcome == "bad") current.Flags.Add("seelah.ending_moderate");
            if (outcome == "bad") current.Flags.Add("seelah.ending_bad");
            if (dead) current.Flags.Add("seelah.elan_dead");
            var visited = new HashSet<string>();
            Program.Walk(road, current, (id, _) => visited.Add(id));
            string expected = "future_" + outcome;
            check(visited.Contains(expected), "Future conversation misses current quest case " + outcome);
            foreach (string other in new[] { "unfinished", "returned", "moderate", "bad" }.Where(x => x != outcome))
                check(!visited.Contains("future_" + other), "Future conversation uses stale/incompatible quest case " + other);
            if (outcome != "unfinished")
                check(visited.Contains(dead ? "future_elan_dead" : "future_elan_other") && !visited.Contains(dead ? "future_elan_other" : "future_elan_dead"), "Future conversation invents Elan's state.");
        }

        // Already completed road scenes remain completed; migration is a separate played scene.
        var legacy = Program.Copy(core);
        legacy.Flags.UnionWith(new[] { "seelah.road", "seelah.committed", "seelah.chosen_future" });
        check(!Program.CurrentAvailable(story, road, legacy), "Migration replays the original commitment.");
        var followup = Scene("future_followup");
        check(Program.CurrentAvailable(story, followup, legacy), "Legacy promise has no migration invitation.");
        check(Program.Walk(followup, legacy).All(s => !s.Has("seelah.developed_commitment") && !s.Has(followup.Id)), "Legacy invitation fabricates activity or consumes its future upgrade.");
        var legacyReady = Play("late_race", Activity(legacy, false));
        legacyReady = Play("future_followup", legacyReady);
        check(legacyReady.Has("seelah.developed_commitment") && legacyReady.Has("seelah.road"), "Played migration cannot develop the old promise.");

        foreach (string endingId in new[] { "ending_together", "ending_unsettled", "ending_grieving", "ending_unfinished_work", "ending_changed", "ending_ascended" })
        foreach (string history in new[] { "legacy", "short", "developed" })
        {
            var state = new Snapshot();
            if (history != "legacy") state.Flags.Add("seelah.short_future_chosen");
            if (history == "developed") state.Flags.Add("seelah.developed_commitment");
            var visited = new HashSet<string>();
            Program.Walk(Scene(endingId), state, (id, _) => visited.Add(id));
            string expected = history == "legacy" ? "earlier_promise" : history == "short" ? "short_history" : "start";
            check(visited.Contains(expected) && new[] { "start", "short_history", "earlier_promise" }.Count(visited.Contains) == 1, "Ending conflates played and unplayed history: " + endingId + "/" + history);
        }
    }
}
