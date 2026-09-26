using System;
using System.Linq;
using Tirabade;

internal static class TirabadeChronologyTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == id);
        Node Page(string scene, string id) => Find(scene).Nodes.Single(n => n.Id == id);
        Snapshot Ready(Scene scene, Snapshot state)
        {
            var copy = Program.Copy(state);
            copy.Hour += scene.DelayHours + 1;
            return copy;
        }
        Snapshot Play(string id, Snapshot state)
        {
            var scene = Find(id);
            var ready = Ready(scene, state);
            check(Rules.Available(story, scene, ready), "Chronology played predecessor unavailable: " + id);
            return Program.Walk(scene, ready).Where(s => s.Has(id) && !s.Has("closed") && Program.LegacyTirabadeOutcome(s))
                .OrderByDescending(s => s.Flags.Count).First();
        }
        var sequence = "a_cup i_watch a_errand i_hands a_roof i_respite a_crossing i_crossing a_morning i_morning reckoning a_truth i_truth table ordinary a_self i_self".Split(' ');
        Snapshot NewState(int chapter)
        {
            var state = new Snapshot { Chapter = chapter, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            state.AvailableContacts.UnionWith(new[] { "b5e867e13503c6f41bb1316705efb4a2", "280d4712dceb37f4a88e98f1f4c6e64f" });
            state.Flags.UnionWith(new[] { "trickster", "seelah.committed", "arueshalae.committed" });
            return state;
        }
        var late = NewState(5);
        foreach (var id in sequence) late = Play(id, late);
        check(!late.Has("departure") && !late.Has("wrote_letter"), "Fresh Chapter 5 witness acquired pre-Abyss history.");
        var returnScene = Find("return");
        check(Rules.Available(story, returnScene, Ready(returnScene, late)), "Fresh Chapter 5 cannot reach the chronology witness.");
        check(!Page("return", "now").Text.Contains("when you were not there")
            && !Page("return", "back").Text.Contains("where you left us"), "Fresh Chapter 5 still invents a pre-Abyss relationship.");
        var start = Page("return", "start");
        check(start.Choices[0].Next == "letter" && start.Choices[1].Next == "now", "Original return answer indices changed.");
        var rememberedDeparture = start.Choices.Single(c => c.Next == "before_the_abyss");
        check(!Rules.Match(rememberedDeparture.Requires, rememberedDeparture.Forbids, late), "Fresh relationship may claim the earlier departure.");
        var letterOnly = Program.Copy(late);
        letterOnly.Flags.UnionWith(new[] { "abyss_letter", "wrote_letter" });
        check(!Rules.Match(rememberedDeparture.Requires, rememberedDeparture.Forbids, letterOnly), "Affair-era letter is misread as a negotiated pre-Abyss triad.");

        var early = NewState(3);
        foreach (var id in sequence) early = Play(id, early);
        early = Play("departure", early);
        early.Chapter = 5;
        check(Rules.Match(rememberedDeparture.Requires, rememberedDeparture.Forbids, early), "Played Chapter 3 departure loses its reunion callback.");
        var earlyPages = new System.Collections.Generic.HashSet<string>();
        var earlyResults = Program.Walk(returnScene, Ready(returnScene, early), (id, _) => earlyPages.Add(id));
        check(earlyPages.Contains("before_the_abyss") && earlyResults.All(s => s.Has("departure")), "Reunion callback loses established departure history.");
        var oldResume = Page("return", "now");
        check(oldResume.Choices[0].Next == "future" && oldResume.Choices[1].Next == "back", "Saved return page choice indices changed.");

        late = Play("return", late);
        late = Play("power", late);
        late = Play("future", late);
        var night = Find("shared_night");
        var near = Page("shared_night", "near");
        check(near.Choices[0].Next == "close" && near.Choices[1].Next == "quiet", "Original shared-night answers changed.");
        check(!Page("shared_night", "close").Text.Contains("unfamiliarity"), "Old close page still assumes first shared intimacy.");
        var callbacks = near.Choices.Where(c => c.Next == "familiar").ToArray();
        check(callbacks.Length == 3, "Missing a completed-night history callback.");
        check(callbacks.All(c => !Rules.Match(c.Requires, c.Forbids, late)), "Unplayed nights supply an intimate memory.");
        var developed = Program.Copy(late);
        foreach (var id in "three_locks three_outing three_yard three_match three_beth_score three_anevia_flour three_return_game three_small_journeys three_stolen_roads three_lantern_debt three_beth_steps three_ista_departure three_lantern_turn three_open_road three_borrowed_names three_back_of_seal three_beth_account three_counterclaim three_unposted_notice three_rooms_unlocked".Split(' '))
            developed = Play(id, developed);
        check(callbacks.Count(c => Rules.Match(c.Requires, c.Forbids, developed)) == 3,
            "Played expanded intimate nights do not supply their earned callbacks.");
        foreach (var pair in new[] { ("three_small_journeys", "three_small_journeys.night"), ("three_open_road", "three_open_road.night"), ("three_rooms_unlocked", "three_rooms_unlocked.night") })
        {
            var interrupted = Program.Copy(late);
            interrupted.Flags.Add(pair.Item2);
            check(callbacks.All(c => !Rules.Match(c.Requires, c.Forbids, interrupted)), "Interrupted night is credited as completed intimacy: " + pair.Item1);
            var quiet = Program.Copy(late);
            quiet.Flags.Add(pair.Item1);
            check(callbacks.All(c => !Rules.Match(c.Requires, c.Forbids, quiet)), "Quiet or departed visit is credited as an intimate night: " + pair.Item1);
            interrupted.Flags.Add(pair.Item1);
            check(callbacks.Count(c => Rules.Match(c.Requires, c.Forbids, interrupted)) == 1, "Completed historical night has no unique matching memory.");
            var visited = new System.Collections.Generic.HashSet<string>();
            var results = Program.Walk(night, Ready(night, interrupted), (id, _) => visited.Add(id));
            check(visited.Contains("familiar") && results.All(s => s.Has("shared_evening") && s.Has(pair.Item2)), "Historical intimacy callback does not rejoin the complete existing night.");
            foreach (var result in results)
                check(result.Has("seelah.committed") && result.Has("arueshalae.committed") && !result.Has("closed"), "Chronology callback changes another relationship or closes the route.");
        }
        // Loss can follow the developed capstone as well as an early unfinished route.
        var loss = Program.Copy(late);
        loss.Flags.UnionWith(new[] { "three_progression.developed", "irabeth_dead", "loss" });
        check(Rules.Available(story, Find("ending_loss"), loss), "Developed loss witness is not an eligible ending.");
        check(!Page("ending_loss", "end").Text.Contains("scarcely learned to imagine"), "Loss ending minimizes completed shared development.");
        check(Page("ending_loss", "end").Choices.Count == 1 && Page("ending_loss", "end").Choices[0].Next == null,
            "Loss repair changes the terminal ending contract.");
        var departure = Find("departure");
        check(departure.MaxChapter == 3 && (departure.Requires.Contains("table")
            || departure.Requires.Contains("trying") && departure.RequiresAny.SequenceEqual(new[] { "table", "tirabade.negotiated_table" })),
            "Departure no longer requires an actual Chapter 3 shared agreement.");
    }
}
