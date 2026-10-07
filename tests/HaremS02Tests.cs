using System;
using System.Linq;
using Tirabade;

internal static class HaremS02Tests
{
    private const string P = "household.pair.seelah_wenduag.";
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Find(string name) => story.Scenes.Single(s => s.Id == P + name);
        Snapshot State(bool nativeRomance)
        {
            var state = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(new[] { "trickster", "trickster.ever", "trickster.foresight.accepted",
                "trickster.foresight.cost.promise", "household.table.kept", Rules.ChapterFlag(5)!,
                story.Relationships["seelah"].CommittedFlag });
            HouseholdTests.Earn(story, state, "seelah.payoff.ordinary");
            HouseholdTests.Earn(story, state, nativeRomance
                ? "wenduag.romance_finished.latched" : "wenduag.payoff.ordinary");
            Rules.Complete(story, state);
            return state;
        }
        Snapshot Do(Snapshot state, string name, string witness)
        {
            var scene = Find(name);
            check(Rules.Available(story, scene, state), "S02 unavailable: " + name);
            var end = Program.Walk(scene, state).Single(s => s.Has(P + witness));
            // Walk exercises the real answer/check graph; completion spends the
            // production allowance, just as the dialog completion path does.
            check(Rules.SpendRestAllowance(story, scene, state), "S02 allowance missing: " + name);
            end.RestSpent = new System.Collections.Generic.Dictionary<string, int>(state.RestSpent);
            Rules.Complete(story, end);
            return end;
        }
        void Rest(Snapshot state, int hours = 48) { state.Hour += hours; Rules.RestFinished(state, true); }
        foreach (bool nativeRomance in new[] { true, false })
        foreach (bool restraintFirst in new[] { true, false })
        {
            var state = State(nativeRomance);
            state = Do(state, "invite", "invited");
            state = Do(state, "spar", "spar.held"); Rest(state);
            state = Do(state, "watch", "watch.done"); Rest(state);
            state = Do(state, restraintFirst ? "restraint" : "stood",
                restraintFirst ? "restraint_witnessed" : "stood_witnessed"); Rest(state);
            state = Do(state, restraintFirst ? "stood.after_restraint" : "restraint.after_stood",
                restraintFirst ? "stood_witnessed" : "restraint_witnessed"); Rest(state);
            var paid = Do(state, "debt_repayment", "boundary.trick_refused");
            check(!Rules.Available(story, Find("choice"), paid), "S02 repayment skipped the deed delay"); Rest(paid);
            foreach (string loss in new[] { "seelah.closed", "wenduag.closed", "seelah_dead", "wenduag.dead_any" })
            {
                var absent = Program.Copy(paid); absent.Flags.Add(loss); Rules.Complete(story, absent);
                check(!Rules.Available(story, Find("choice"), absent), "S02 attendance leak: " + loss);
            }
            var night = Do(paid, "choice", "choice.both_yes"); Rest(night, 8);
            var morning = Do(night, "morning", "morning.done");
            check(!Rules.Available(story, Find("choice"), morning), "S02 repeated first intimacy");
        }
    }
}
