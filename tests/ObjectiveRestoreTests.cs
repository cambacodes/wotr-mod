using System;
using System.Linq;
using Tirabade;

// Engine-q2 item 2: Main.Update fails a Started relationship objective on a death or departure; a Trickster return that
// answers it, once the partner is committed, reopens and completes the objective (Rules.ObjectiveStep "restore").
internal static class ObjectiveRestoreTests
{
    private static Snapshot State(params string[] flags)
    {
        var state = new Snapshot { Chapter = 5, Hour = 5000 };
        state.Flags.UnionWith(flags);
        return state;
    }

    internal static void Run(Action<bool, string> check)
    {
        var her = new Relationship
        {
            Title = "Her", StartedFlag = "her.started", ClosedFlag = "her.closed", CommittedFlag = "her.committed",
            UnavailableFlags = new[] { "her.dead", "her.gone" }, FailureFlags = new[] { "her.dead", "her.gone" },
            UnavailableOverrides = { ["her.dead"] = "her.trickster.returned" },
        };
        her.TricksterAccess["gone"] = new TricksterAccess { Device = "her.trickster.gone.setup", Returned = "her.trickster.recalled" };
        string? Step(bool started, bool failed, params string[] flags) => Rules.ObjectiveStep(her, State(flags), started, failed);

        check(Step(true, false, "her.dead") == "fail", "A death no longer fails the Started objective.");
        check(Step(true, false, "her.dead", "her.trickster.returned") == null, "A returned partner's objective is failed.");
        check(Step(false, true, "her.dead", "her.trickster.returned", "her.committed") == "restore",
            "A returned, committed partner keeps a Failed objective.");
        check(Step(false, true, "her.trickster.returned", "her.committed") == "restore", "A return recorded after the death read cleared is not restored.");
        check(Step(false, true, "her.dead", "her.trickster.returned") == null, "An uncommitted returned partner's objective is completed.");
        check(Step(false, true, "her.dead", "her.committed") == null, "A dead partner with no return is restored.");
        check(Step(false, true, "her.dead", "her.trickster.returned", "her.committed", "her.closed") == null, "A closed route's objective is restored.");
        // A second loss the return does not answer still blocks.
        check(Step(false, true, "her.dead", "her.gone", "her.trickster.returned", "her.committed") == null,
            "A return restores the objective while another loss still blocks the route.");
        // The TricksterAccess Returned key counts as a return (it carries no override here, so it lifts nothing by itself).
        check(Step(false, true, "her.trickster.recalled", "her.committed") == "restore", "A TricksterAccess return is not a return flag.");
        check(Step(false, false, "her.trickster.returned", "her.committed") == null && Step(false, true) == null,
            "An objective never failed (or nothing held) is touched.");
        // The trio's runtime "loss": answered only when every held input is lifted by the trio's own overrides.
        var trio = new Relationship { Title = "Trio", StartedFlag = "t.started", ClosedFlag = "t.closed", CommittedFlag = "t.committed",
            UnavailableFlags = new[] { "irabeth_dead" }, FailureFlags = new[] { "loss", "inhuman" },
            UnavailableOverrides = { ["irabeth_dead"] = "irabeth.trickster.returned" } };
        string? Trio(params string[] flags) => Rules.ObjectiveStep(trio, State(flags), false, true);
        check(Trio("loss", "irabeth_dead", "irabeth.trickster.returned", "t.committed") == "restore", "The trio's answered loss keeps a Failed objective.");
        check(Trio("loss", "irabeth_dead", "anevia_dead", "irabeth.trickster.returned", "t.committed") == null, "An unanswered loss input restores the trio.");
        check(Trio("loss", "irabeth_dead", "sacrifice", "irabeth.trickster.returned", "t.committed") == null, "The Commander's sacrifice restores the trio.");
        check(Trio("loss", "irabeth_dead", "irabeth.trickster.returned", "t.committed", "inhuman") == null, "An inhuman Commander restores the trio.");
        check(Rules.ReturnFlags(her).OrderBy(x => x).SequenceEqual(new[] { "her.trickster.recalled", "her.trickster.returned" }),
            "ReturnFlags misses an UnavailableOverrides value or a TricksterAccess Returned key.");
    }

    // The generated story: every Trickster return that lifts a failure flag restores a committed partner's objective.
    internal static void RunStory(Story story, Action<bool, string> check)
    {
        int worlds = 0;
        foreach (var pair in story.Relationships)
        {
            var rel = pair.Value;
            foreach (var flag in rel.FailureFlags.Where(rel.UnavailableOverrides.ContainsKey))
            {
                string returned = rel.UnavailableOverrides[flag];
                var dead = State(flag, rel.CommittedFlag);
                check(Rules.ObjectiveStep(rel, State(flag), true, false) == "fail", "Objective restore: " + pair.Key + " / " + flag + " does not fail.");
                var back = State(flag, returned, rel.CommittedFlag);
                Rules.Complete(story, back);
                // A canon-reading override (a Derived key) may need more than its name: only judge worlds where it holds.
                if (!back.Has(returned)) continue;
                worlds++;
                check(Rules.ObjectiveStep(rel, back, false, true) == "restore",
                    "Objective restore: " + pair.Key + " returned from " + flag + " (" + returned + ") and committed keeps a Failed objective.");
                check(Rules.ObjectiveStep(rel, dead, false, true) == null, "Objective restore: " + pair.Key + " / " + flag + " restores without a return.");
            }
        }
        check(worlds >= 3, "Objective restore: too few return worlds checked (" + worlds + ").");
    }
}
