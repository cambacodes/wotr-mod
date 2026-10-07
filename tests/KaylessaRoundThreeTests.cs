using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// R3: exercise native-history closure in the production rules without the broad romance search.
internal static class KaylessaRoundThreeTests
{
    private const string P = "kaylessa.trickster.";
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Snapshot World(params string[] flags)
        {
            var state = new Snapshot { Chapter = 5, Hour = 1000,
                Area = "2570015799edf594daf2f076f2f975d8",
                CrusadeResources = new Dictionary<string, int> { ["Favors"] = 10000 } };
            state.Flags.UnionWith(flags);
            state.AvailableContacts.Add("a1569a0739314d04cb8af1d47dcffbe0");
            Rules.Complete(story, state);
            foreach (var flag in state.Flags) state.Times[flag] = 0;
            return state;
        }
        foreach (var attack in new[] { "kaylessa.attack_kenabres_masked", "kaylessa.attack_kenabres_drow", "kaylessa.attack_camp" })
            foreach (var council in new[] { "", "shyka.gone", "council.fought", "council.fought_nocta_allied" })
                foreach (bool returned in new[] { false, true })
                {
                    var state = World("trickster", "kaylessa.dead", attack, council, P + "primed",
                        "kaylessa.committed", P + "knife_shown", "kaylessa.wasps.in_the_dark", P + "told_borrowed");
                    if (returned) state.Flags.Add(P + "returned");
                    Rules.Complete(story, state);
                    string history = attack + "/" + council + "/legacy-return=" + returned;
                    check(state.Has("kaylessa.early_player_killed"), "R3: attack reader did not close " + history);
                    check(!Rules.RouteOpen(story.Relationships["kaylessa"], state), "R3: route reopened " + history);
                    check(!state.Has("kaylessa.harem.eligible"), "R3: household admitted " + history);
                    foreach (var id in new[] { "dead.borrow", "dead.borrow_sending", "dead.soldier", "commit" })
                        check(!Rules.Available(story, S(P + id), state), "R3: " + id + " opened " + history);
                }
        var reveal = World("trickster", "kaylessa.dead", "kaylessa.begged_death");
        check(!reveal.Has("kaylessa.early_player_killed") && Rules.Available(story, S(P + "dead.borrow"), reveal),
            "R3: plot-imposed Reveal death lost its Council bargain.");
        foreach (var council in new[] { "shyka.gone", "council.fought", "council.fought_nocta_allied" })
        {
            var sending = World("trickster", "kaylessa.dead", "kaylessa.begged_death", council);
            check(Rules.Available(story, S(P + "dead.borrow_sending"), sending), "R3: Reveal sending blocked after " + council);
            sending.Flags.Add(P + "primed");
            sending.Times[P + "primed"] = sending.Hour;
            Rules.Complete(story, sending);
            sending.Hour += 11;
            check(!Rules.Available(story, S(P + "dead.soldier"), sending), "R3: paid return arrived early.");
            sending.Hour++;
            check(Rules.Available(story, S(P + "dead.soldier"), sending), "R3: paid Reveal return failed to arrive.");
        }
    }
}
