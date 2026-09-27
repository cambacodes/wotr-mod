using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E14g: Story.Counts (at least Min of Of), computed after Derived.
internal static class CountTests
{
    internal static void Run(Action<bool, string> check)
    {
        Story Fixture()
        {
            var story = TricksterLatchTests.Fixture();
            story.Derived["irabeth.any_trick"] = new[] { new[] { "irabeth.trickster.primed" }, new[] { "irabeth.trickster.returned" } };
            story.Counts["lastcall.creditors_two"] = new CountSpec { Of = new[] { "irabeth.any_trick", "trickster.ever", "irabeth.committed" }, Min = 2 };
            return story;
        }
        var story = Fixture();
        Rules.Validate(story);
        var state = new Snapshot();
        state.Flags.Add("irabeth.trickster.primed");
        Rules.Complete(story, state);
        check(state.Has("irabeth.any_trick") && !state.Has("lastcall.creditors_two"), "Count reached with one source.");
        state.Flags.Add("trickster");
        Rules.Complete(story, state);
        check(state.Has("trickster.ever") && state.Has("lastcall.creditors_two"), "Count not reached with a latch and a composite.");
        var missing = new HashSet<string> { "trickster", "trickster.was" };
        Rules.PropagateMissing(story, missing);
        check(missing.Contains("lastcall.creditors_two"), "A count with a missing source was not marked missing.");
        foreach (var (what, mutate) in new List<(string, Action<Story>)> {
            ("Min above sources", s => s.Counts["lastcall.creditors_two"].Min = 4),
            ("Min zero", s => s.Counts["lastcall.creditors_two"].Min = 0),
            ("unknown source", s => s.Counts["lastcall.creditors_two"].Of = new[] { "never.written" }),
            ("duplicate source", s => s.Counts["lastcall.creditors_two"].Of = new[] { "trickster", "trickster" }),
            ("collides with a derived key", s => s.Counts["irabeth.any_trick"] = new CountSpec { Of = new[] { "trickster" } }),
            ("collides with an authored flag", s => s.Counts["irabeth.committed"] = new CountSpec { Of = new[] { "trickster" } }),
            ("count of counts", s => s.Counts["deeper"] = new CountSpec { Of = new[] { "lastcall.creditors_two" } }) })
        {
            var bad = Fixture();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid count accepted: " + what);
        }
    }
}
