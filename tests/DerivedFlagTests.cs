using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E4: Story.Derived composites (OR of AND-groups) computed after natives and latches; TT-22's
// trickster.cheated_death lets an epilogue that forbids `sacrifice` survive the Trickster punchline ending.
internal static class DerivedFlagTests
{
    private static readonly string[] Endings = { "ending.trickster", "ending.trickster_all_planes", "ending.trickster_all_planes_fw", "ending.trickster_full" };

    private static Story Fixture()
    {
        var story = TricksterLatchTests.Fixture();
        story.Etudes["sacrifice"] = "381a296094804761af0893d2e70dc2df";
        story.Etudes["ending.trickster"] = "db5375333382d044089475d256f19582";
        story.Etudes["ending.trickster_all_planes"] = "f7343e290a8d4ed887af8f04d1b3446b";
        story.Etudes["ending.trickster_all_planes_fw"] = "5f63f6d43c9b465f822db70af7d69b92";
        story.Etudes["ending.trickster_full"] = "6ff418aeda24e6e48be844e6258e3c5a";
        story.Derived["trickster.cheated_death"] = Endings.Select(e => new[] { "sacrifice", "trickster.ever", e }).ToArray();
        // A composite over a composite and an authored flag (evaluation order must not matter).
        story.Derived["irabeth.trickster.epilogue_variant"] = new[] { new[] { "trickster.cheated_death", "irabeth.committed" } };
        story.Scenes.Add(new Scene
        {
            Id = "irabeth.ending", Title = "ending", Owner = "Epilogue", Relationship = "irabeth", MinChapter = 1, MaxChapter = 6,
            Requires = new[] { "irabeth.committed" }, Forbids = new[] { "sacrifice", "irabeth_dead" },
            ForbidOverrides = new Dictionary<string, string> { ["sacrifice"] = "trickster.cheated_death" },
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } }
        });
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);
        var ending = story.Scenes.Single(s => s.Id == "irabeth.ending");

        foreach (string finale in Endings)
        {
            var state = new Snapshot { Chapter = 6, Hour = 9000 };
            state.Flags.UnionWith(new[] { "trickster.ever", "sacrifice", finale, "irabeth.committed" });
            Rules.Complete(story, state);
            check(state.Has("trickster.cheated_death"), "TT-22 composite not derived for " + finale);
            check(state.Has("irabeth.trickster.epilogue_variant"), "Nested composite not derived for " + finale);
            check(Rules.Available(story, ending, state), "TT-22: epilogue vanished on the Trickster punchline ending " + finale);
        }
        // Negative: any missing conjunct keeps sacrifice forbidding the epilogue.
        foreach (var missing in new[] { "trickster.ever", "sacrifice", "ending.trickster" })
        {
            var state = new Snapshot { Chapter = 6, Hour = 9000 };
            state.Flags.UnionWith(new[] { "trickster.ever", "sacrifice", "ending.trickster", "irabeth.committed" });
            state.Flags.Remove(missing);
            Rules.Complete(story, state);
            check(!state.Has("trickster.cheated_death"), "Composite derived without " + missing);
            check(missing == "sacrifice" ? Rules.Available(story, ending, state) : !Rules.Available(story, ending, state),
                "Epilogue guard wrong without " + missing);
        }
        // The live latch source feeds the composite in the same snapshot.
        var live = new Snapshot { Chapter = 6, Hour = 9000 };
        live.Flags.UnionWith(new[] { "trickster", "sacrifice", "ending.trickster_full" });
        Rules.Complete(story, live);
        check(live.Has("trickster.ever") && live.Has("trickster.cheated_death"), "Composite does not see a latch observed in the same snapshot.");
        // The override lifts only sacrifice.
        live.Flags.UnionWith(new[] { "irabeth.committed", "irabeth_dead" });
        check(!Rules.Available(story, ending, live), "cheated_death lifted an unrelated epilogue forbid.");

        // Missing bindings propagate through composites.
        var lost = new HashSet<string> { "ending.trickster" };
        Rules.PropagateMissing(story, lost);
        check(lost.Contains("trickster.cheated_death") && lost.Contains("irabeth.trickster.epilogue_variant"), "Missing native input not inherited by composites.");

        void Invalid(string what, Action<Story> mutate)
        {
            var bad = Fixture();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid derived key accepted: " + what);
        }
        Invalid("cycle", s => { s.Derived["a"] = new[] { new[] { "b" } }; s.Derived["b"] = new[] { new[] { "a", "trickster" } }; });
        Invalid("self cycle", s => s.Derived["a"] = new[] { new[] { "a" }, new[] { "trickster" } });
        Invalid("unknown source", s => s.Derived["a"] = new[] { new[] { "nothing_sets_this" } });
        Invalid("empty groups", s => s.Derived["a"] = Array.Empty<string[]>());
        Invalid("empty group", s => s.Derived["a"] = new[] { Array.Empty<string>() });
        Invalid("duplicate member", s => s.Derived["a"] = new[] { new[] { "trickster", "trickster" } });
        Invalid("collides with authored", s => s.Derived["irabeth.trickster.primed"] = new[] { new[] { "trickster" } });
        Invalid("collides with scene id", s => s.Derived["irabeth.ending"] = new[] { new[] { "trickster" } });
        Invalid("collides with native", s => s.Derived["sacrifice"] = new[] { new[] { "trickster" } });
        Invalid("collides with latch", s => s.Derived["trickster.ever"] = new[] { new[] { "trickster" } });
        Invalid("collides with runtime-derived", s => s.Derived["loss"] = new[] { new[] { "trickster" } });
        Invalid("reserved prefix", s => s.Derived["rrt.degraded.x"] = new[] { new[] { "trickster" } });
        Invalid("contact evidence", s => s.Derived["nurah.meeting_arrived"] = new[] { new[] { "trickster" } });
    }
}
