using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Run separately with --completion-parity so the full gate retains its assertion count.
// The reference deliberately keeps the original LINQ evaluator and dependency traversal.
internal static class CompletionParityTests
{
    private static List<string> ReferenceOrder(Story story)
    {
        var order = new List<string>(story.Derived.Count);
        var seen = new HashSet<string>(StringComparer.Ordinal);
        void Visit(string key)
        {
            if (!seen.Add(key)) return;
            foreach (var input in Rules.DerivedInputs(story, key))
                if (story.Derived.ContainsKey(input)) Visit(input);
            order.Add(key);
        }
        foreach (var key in story.Derived.Keys) Visit(key);
        return order;
    }

    private static bool ReferenceRouteOpen(Relationship relationship, Snapshot state) =>
        !state.Has(relationship.ClosedFlag) && !relationship.UnavailableFlags.Any(flag => Rules.Blocks(relationship, flag, state));

    private static void ReferenceComplete(Story story, Snapshot state)
    {
        foreach (var key in story.Latches.Where(pair => !state.Has(pair.Key) && pair.Value.Any(state.Has)).Select(pair => pair.Key).ToArray())
            state.Flags.Add(key);
        foreach (var key in ReferenceOrder(story))
            if (!state.Has(key) && story.Derived[key].Any(group => group.All(state.Has))
                && (!story.DerivedOpenRoutes.TryGetValue(key, out var routes)
                    || routes.All(rel => ReferenceRouteOpen(story.Relationships[rel], state)))
                && !(story.DerivedForbids.TryGetValue(key, out var forbids) && forbids.Any(state.Has)))
                state.Flags.Add(key);
        foreach (var pair in story.Counts)
            if (!state.Has(pair.Key) && (pair.Value.Chapters.Length == 0 || pair.Value.Chapters.Contains(state.Chapter))
                && pair.Value.Of.Count(state.Has) >= pair.Value.Min) state.Flags.Add(pair.Key);
        foreach (var key in Rules.WordMadeTrueKeys) state.Flags.Remove(key);
        int left = Rules.WordMadeTrueLeft(state);
        state.Flags.Add("trickster.wmt.left." + left);
        if (left > 0) state.Flags.Add("trickster.wmt.available");
    }

    internal static void Run(Story shipped, Action<bool, string> check)
    {
        void Compare(Story story, Snapshot state, string name)
        {
            check(Rules.DerivedOrder(story).SequenceEqual(ReferenceOrder(story)), "Dependency order changed: " + name);
            var expected = Program.Copy(state);
            ReferenceComplete(story, expected);
            Rules.Complete(story, state);
            check(state.Flags.SetEquals(expected.Flags), "Completion flags changed: " + name);
            check(state.Times.OrderBy(p => p.Key).SequenceEqual(expected.Times.OrderBy(p => p.Key)), "Completion timestamps changed: " + name);
        }

        // Route closure, override and forbid dependencies must settle before their consumers.
        var fixture = new Story();
        fixture.Relationships["r"] = new Relationship { ClosedFlag = "closed", UnavailableFlags = new[] { "dead" },
            UnavailableOverrides = new Dictionary<string, string> { ["dead"] = "returned" } };
        fixture.Latches["latched"] = new[] { "native" };
        fixture.Latches["latched_second"] = new[] { "latched" };
        fixture.Derived["eligible"] = new[] { new[] { "latched" } };
        fixture.Derived["returned"] = new[] { new[] { "paid" } };
        fixture.Derived["dead"] = new[] { new[] { "loss" } };
        fixture.Derived["closed"] = new[] { new[] { "refused" } };
        fixture.Derived["forbidden"] = new[] { new[] { "veto" } };
        fixture.DerivedOpenRoutes["eligible"] = new[] { "r" };
        fixture.DerivedForbids["eligible"] = new[] { "forbidden" };
        string[] inputs = { "native", "paid", "loss", "refused", "veto" };
        for (int mask = 0; mask < 1 << inputs.Length; mask++)
        {
            var state = new Snapshot();
            for (int bit = 0; bit < inputs.Length; bit++) if ((mask & (1 << bit)) != 0) state.Flags.Add(inputs[bit]);
            Compare(fixture, state, "route inputs " + mask);
            Compare(fixture, state, "repeat " + mask);
        }
        // Stories and arrays are mutable, including after a previous completion.
        fixture.Derived["returned"][0][0] = "eligible";
        Compare(fixture, new Snapshot(), "in-place dependency edit");
        fixture.Derived["returned"] = new[] { Array.Empty<string>() };
        fixture.Derived["empty"] = Array.Empty<string[]>();
        fixture.DerivedForbids["eligible"][0] = "dead";
        fixture.Relationships["r"].UnavailableOverrides["dead"] = "empty";
        Compare(fixture, new Snapshot(), "replacement, empty groups and override edit");

        // Reuse a warm plan while changing every kind of dependency in place.
        // An equal key count is insufficient: later keys can become prerequisites.
        var mutable = new Story();
        mutable.Derived["consumer"] = new[] { new[] { "seed" } };
        mutable.Derived["later"] = new[] { Array.Empty<string>() };
        mutable.Derived["closed"] = new[] { Array.Empty<string>() };
        mutable.Derived["dead"] = new[] { Array.Empty<string>() };
        mutable.Derived["returned"] = new[] { Array.Empty<string>() };
        mutable.Relationships["r"] = new Relationship { ClosedFlag = "not_closed", UnavailableFlags = new[] { "not_dead" } };
        mutable.Relationships["s"] = new Relationship { ClosedFlag = "not_closed", UnavailableFlags = Array.Empty<string>() };
        mutable.DerivedOpenRoutes["consumer"] = new[] { "r" };
        Compare(mutable, new Snapshot(), "cold plan");
        mutable.Derived["consumer"][0][0] = "later";
        Compare(mutable, new Snapshot(), "group input changed at equal size");
        mutable.DerivedForbids["consumer"] = new[] { "seed" };
        Compare(mutable, new Snapshot(), "forbid inserted");
        mutable.DerivedForbids["consumer"][0] = "later";
        Compare(mutable, new Snapshot(), "forbid input changed at equal size");
        mutable.DerivedForbids.Remove("consumer");
        mutable.Relationships["r"].ClosedFlag = "closed";
        Compare(mutable, new Snapshot(), "closure dependency changed");
        mutable.Relationships["r"].ClosedFlag = "not_closed";
        mutable.Relationships["r"].UnavailableFlags[0] = "dead";
        Compare(mutable, new Snapshot(), "unavailable dependency changed");
        mutable.Relationships["r"].UnavailableOverrides["dead"] = "returned";
        Compare(mutable, new Snapshot(), "override dependency inserted");
        mutable.Relationships["r"].UnavailableOverrides["dead"] = "seed";
        Compare(mutable, new Snapshot(), "override dependency changed at equal size");
        mutable.DerivedOpenRoutes["consumer"][0] = "s";
        Compare(mutable, new Snapshot(), "route input changed at equal size");
        mutable.DerivedOpenRoutes.Remove("consumer");
        Compare(mutable, new Snapshot(), "route guard removed");
        mutable.Derived.Remove("later");
        mutable.Derived["seed"] = new[] { Array.Empty<string>() };
        Compare(mutable, new Snapshot(), "derived key replaced at equal size");
        mutable.Derived["consumer"][0][0] = "seed";
        Compare(mutable, new Snapshot(), "replacement key becomes prerequisite");
        // The public list is caller-owned; editing it cannot poison the cached order.
        Rules.DerivedOrder(mutable).Clear();
        Compare(mutable, new Snapshot(), "public order list edited");
        mutable.Derived["extra"] = new[] { new[] { "consumer" } };
        Compare(mutable, new Snapshot(), "derived key inserted");
        mutable.Derived.Remove("extra");
        Compare(mutable, new Snapshot(), "derived key removed");
        mutable.Derived["consumer"][0][0] = "SEED";
        Compare(mutable, new Snapshot(), "case-sensitive dependency");
        mutable.Derived = new Dictionary<string, string[][]>(mutable.Derived, StringComparer.OrdinalIgnoreCase);
        Compare(mutable, new Snapshot(), "dictionary comparer replaced");

        var flags = shipped.Derived.Keys.Concat(shipped.Derived.Keys.SelectMany(key => Rules.DerivedInputs(shipped, key)))
            .Concat(shipped.Latches.Values.SelectMany(sources => sources)).Concat(shipped.Counts.Values.SelectMany(count => count.Of))
            .Concat(new[] { "wenduag.dead_any", "wenduag.killed", Rules.WenduagEchoPrefix + "valid", Rules.WenduagEchoPrefix + "unavailable" })
            .Concat(Enumerable.Range(0, 4).Select(i => Rules.WordMadeTrueUsePrefix + i))
            .Distinct().OrderBy(flag => flag, StringComparer.Ordinal).ToArray();
        var random = new Random(801);
        for (int sample = 0; sample < 512; sample++)
        {
            var state = new Snapshot { Chapter = sample % 8, Hour = sample };
            foreach (var flag in flags)
                if (random.Next(8) < sample % 8) { state.Flags.Add(flag); state.Times[flag] = sample - 1; }
            Compare(shipped, state, "shipped " + sample);
            Compare(shipped, state, "shipped repeated " + sample);
        }
    }
}
