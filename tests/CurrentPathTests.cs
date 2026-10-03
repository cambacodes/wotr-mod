using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Engine-q2 item 1: the GLOBAL current-path reader. trickster.ever is the run latch (the run WAS Trickster); trickster.now
// (Story.Derived [[trickster]] with Story.DerivedForbids) holds only while the Commander still IS on the Trickster path.
internal static class CurrentPathTests
{
    private static readonly string[] Left = { "trickster.failed", "dragon", "legend", "swarm" };

    private static Story Fixture()
    {
        var story = TricksterLatchTests.Fixture();
        story.Etudes["trickster.failed"] = "256f3c081f21ed84fb3612465a76944b";
        story.Etudes["dragon"] = "9b193d30c89a20b409fd3dda9bd109bf";
        story.Etudes["legend"] = "c6165efcd5571c442ae38d7c0601f2df";
        story.Etudes["swarm"] = "439e63fed37f52048887d98f99255e40";
        story.Derived[Rules.TricksterNow] = new[] { new[] { "trickster" } };
        story.DerivedForbids[Rules.TricksterNow] = Left.ToArray();
        // A composite over the current path (the foresight hook shape: a later gated outcome).
        story.Derived["irabeth.trickster.gate_open"] = new[] { new[] { Rules.TricksterNow, "irabeth.trickster.primed" } };
        return story;
    }

    private static Snapshot Completed(Story story, params string[] flags)
    {
        var state = new Snapshot { Chapter = 5, Hour = 5000 };
        state.Flags.UnionWith(flags);
        Rules.Complete(story, state);
        return state;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);

        var live = Completed(story, "trickster", "trickster.was");
        check(live.Has(Rules.TricksterNow) && live.Has("trickster.ever"), "A live Trickster is not on the current path.");
        // Chapter 4 KTC_Fail: TricksterMythicPathFailed, then Chapter04 completes PlayerIsTrickster.
        var failed = Completed(story, "trickster.was", "trickster.ever", "trickster.failed");
        check(!failed.Has(Rules.TricksterNow) && failed.Has("trickster.ever"), "A failed Trickster still reads the current path, or lost the run latch.");
        // The same frame before Chapter04 completes PlayerIsTrickster: the failure alone already drops it.
        var failing = Completed(story, "trickster", "trickster.was", "trickster.failed");
        check(!failing.Has(Rules.TricksterNow), "The current path holds between KTC_Fail and PlayerIsTrickster's completion.");
        // Goddesses' Summit: Legend leaves PlayerIsTrickster playing; MythicPathFailed starts TricksterMythicPathFailed.
        var legend = Completed(story, "trickster", "trickster.was", "trickster.failed", "legend");
        check(!legend.Has(Rules.TricksterNow), "A Trickster turned Legend still reads the current path.");
        // A path etude alone (the frame before MythicPathFailed) is enough for each conversion.
        foreach (var path in new[] { "legend", "dragon", "swarm" })
            check(!Completed(story, "trickster", "trickster.was", path).Has(Rules.TricksterNow), "The current path survives " + path + ".");
        check(!Completed(story, "trickster.was").Has(Rules.TricksterNow), "PlayerWasTrickster alone reads as the current path.");
        check(!Completed(story).Has(Rules.TricksterNow), "A never-Trickster run reads the current path.");
        // A composite over trickster.now follows it (ordering through DerivedInputs).
        check(Completed(story, "trickster", "irabeth.trickster.primed").Has("irabeth.trickster.gate_open")
              && !Completed(story, "trickster", "trickster.failed", "irabeth.trickster.primed").Has("irabeth.trickster.gate_open"),
            "A composite over trickster.now does not follow the current path.");
        check(Rules.DerivedOrder(story).IndexOf(Rules.TricksterNow) < Rules.DerivedOrder(story).IndexOf("irabeth.trickster.gate_open"),
            "trickster.now is not ordered before the composites that read it.");

        // A missing forbid binding marks the key missing (never read as "on the path" when the failure cannot be read).
        var missing = new HashSet<string> { "trickster.failed" };
        Rules.PropagateMissing(story, missing);
        check(missing.Contains(Rules.TricksterNow) && missing.Contains("irabeth.trickster.gate_open"), "A missing path-failure binding does not degrade trickster.now.");

        // Validation.
        void Invalid(string what, Action<Story> mutate)
        {
            var bad = Fixture();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid DerivedForbids accepted: " + what);
        }
        Invalid("not a Derived key", s => s.DerivedForbids["trickster.later"] = new[] { "legend" });
        Invalid("unknown flag", s => s.DerivedForbids[Rules.TricksterNow] = new[] { "no_such_key" });
        Invalid("empty list", s => s.DerivedForbids[Rules.TricksterNow] = Array.Empty<string>());
        Invalid("duplicate flag", s => s.DerivedForbids[Rules.TricksterNow] = new[] { "legend", "legend" });
        Invalid("forbids what it requires", s => s.DerivedForbids[Rules.TricksterNow] = new[] { "trickster" });
        Invalid("forbids itself", s => s.DerivedForbids[Rules.TricksterNow] = new[] { Rules.TricksterNow });
        Invalid("cycle through a forbid", s =>
        {
            s.Derived["loop"] = new[] { new[] { "trickster" } };
            s.DerivedForbids["loop"] = new[] { "irabeth.trickster.gate_open" };
            s.Derived["irabeth.trickster.gate_open"] = new[] { new[] { "loop" } };
        });
    }

    // The generated story: the reader exists with its native evidence, the live setups read the current path, and every
    // native canon change that names the current path holds it in each When group (the T6a choices stay applied).
    internal static void RunStory(Story story, Action<bool, string> check)
    {
        if (!story.Derived.TryGetValue(Rules.TricksterNow, out var groups)) return;
        check(groups.Length == 1 && groups[0].SequenceEqual(new[] { "trickster" })
              && story.DerivedForbids.TryGetValue(Rules.TricksterNow, out var forbids) && Left.All(forbids.Contains)
              && story.Etudes.TryGetValue("trickster.failed", out var failed) && failed == "256f3c081f21ed84fb3612465a76944b",
            "trickster.now is not [[trickster]] minus trickster.failed, dragon, legend and swarm.");
        var leaky = story.Scenes.Where(s => s.Requires.Contains("trickster") && !s.Requires.Contains("trickster.failed")
            && !s.Forbids.Contains("trickster.failed")).Select(s => s.Id).ToArray();
        check(leaky.Length == 0, "Live Trickster scenes that a Trickster turned Legend still opens: " + string.Join(", ", leaky.Take(5)));
        foreach (var pair in new (string Edit, string Flag)[] { ("81109ea8fb20dbc478cf67116740f4a1", "kiana.separated"),
                                                                 ("4bb3706172f1ed54ca11db96254c4638", "wenduag.committed") })
            if (story.NativeEpilogueEdits.TryGetValue(pair.Edit, out var edit))
                check(Rules.EditVariants(edit).First().When.Where(g => g.Contains(pair.Flag)).All(g => g.Contains(Rules.TricksterNow)),
                    "A native edit whose only Trickster evidence is the path reads the run latch: " + pair.Edit);
    }
}
