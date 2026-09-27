using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E1 (TT-02): Story.Latches records a one-time native fact as an ordinary authored flag.
internal static class TricksterLatchTests
{
    private static Scene Remote(string id, string relationship, string[] requires, string[] sets) => new Scene
    {
        Id = id, Title = id, Owner = "Memory", Relationship = relationship, Remote = true, MinChapter = 3, MaxChapter = 5,
        Requires = requires,
        Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice { Set = sets } } } }
    };

    internal static Story Fixture()
    {
        var story = new Story();
        story.Relationships["irabeth"] = new Relationship { Title = "Irabeth", StartedFlag = "irabeth.started",
            ClosedFlag = "irabeth.closed", CommittedFlag = "irabeth.committed", UnavailableFlags = new[] { "irabeth_dead" } };
        story.Etudes["trickster"] = "9f486a9c0c9abfc4a952bb22e88a7e96";
        story.Etudes["trickster.was"] = "c820b3788f967e14f8bde3c17447157f";
        story.Etudes["irabeth_dead"] = "0123456789abcdef0123456789abcdef";
        story.Latches["trickster.ever"] = new[] { "trickster", "trickster.was" };
        // Setup: the live power. Payoff and continuation: the latch plus the device's own record.
        story.Scenes.Add(Remote("irabeth.trickster.dead.setup", "irabeth", new[] { "trickster" }, new[] { "irabeth.trickster.primed" }));
        story.Scenes.Add(Remote("irabeth.trickster.dead.payoff", "irabeth", new[] { "trickster.ever", "irabeth.trickster.primed" },
            new[] { "irabeth.trickster.returned" }));
        story.Scenes.Add(Remote("irabeth.trickster.dead.after", "irabeth", new[] { "trickster.ever", "irabeth.trickster.returned" },
            new[] { "irabeth.committed" }));
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);
        Scene Get(string id) => story.Scenes.Single(s => s.Id == id);

        // Positive: the live power is observed and latched (Main.State adds it virtually; Update persists it).
        var state = new Snapshot { Chapter = 3, Hour = 100 };
        state.Flags.Add("trickster");
        check(Rules.PendingLatches(story, state).SequenceEqual(new[] { "trickster.ever" }), "Live Trickster power is not latched.");
        Rules.Complete(story, state);
        check(state.Has("trickster.ever"), "Snapshot completion omits an observed latch.");
        check(Rules.Available(story, Get("irabeth.trickster.dead.setup"), state), "Trickster setup unavailable with the live power.");
        state.Flags.Add("irabeth.trickster.primed");

        // Chapter 4 KTC_Fail completes PlayerIsTrickster; only the persisted latch survives.
        var failed = new Snapshot { Chapter = 5, Hour = 5000 };
        failed.Flags.UnionWith(new[] { "trickster.ever", "irabeth.trickster.primed" });
        Rules.Complete(story, failed);
        check(!failed.Has("trickster"), "Fixture error: the failed path still holds the live power.");
        check(Rules.PendingLatches(story, failed).Length == 0, "A recorded latch is recorded twice.");
        check(Rules.Available(story, Get("irabeth.trickster.dead.payoff"), failed), "Device payoff vanished after the Trickster path failed.");
        check(!Rules.Available(story, Get("irabeth.trickster.dead.setup"), failed), "A new device setup opened after the Trickster power was lost.");
        failed.Flags.Add("irabeth.trickster.returned");
        check(Rules.Available(story, Get("irabeth.trickster.dead.after"), failed), "Device continuation vanished after the Trickster path failed.");

        // PlayerWasTrickster alone also latches (a save that never observed the live etude).
        var former = new Snapshot { Chapter = 5, Hour = 5000 };
        former.Flags.Add("trickster.was");
        Rules.Complete(story, former);
        check(former.Has("trickster.ever"), "PlayerWasTrickster does not latch trickster.ever.");

        // Negative: no source observed, no latch.
        var never = new Snapshot { Chapter = 5, Hour = 5000 };
        Rules.Complete(story, never);
        check(!never.Has("trickster.ever") && Rules.PendingLatches(story, never).Length == 0, "A latch was recorded without its source.");

        // Missing bindings: one surviving source keeps the latch; losing all sources loses it.
        var missing = new HashSet<string> { "trickster" };
        Rules.PropagateMissing(story, missing);
        check(!missing.Contains("trickster.ever"), "A latch with a surviving source was marked missing.");
        missing.Add("trickster.was");
        Rules.PropagateMissing(story, missing);
        check(missing.Contains("trickster.ever"), "A latch with no surviving source was not marked missing.");

        void Invalid(string what, Action<Story> mutate)
        {
            var bad = Fixture();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid latch accepted: " + what);
        }
        Invalid("unknown source", s => s.Latches["trickster.ever"] = new[] { "trickster", "no_such_key" });
        Invalid("authored source", s => s.Latches["trickster.ever"] = new[] { "irabeth.trickster.primed" });
        Invalid("empty sources", s => s.Latches["trickster.ever"] = Array.Empty<string>());
        Invalid("duplicate sources", s => s.Latches["trickster.ever"] = new[] { "trickster", "trickster" });
        Invalid("key authored by a choice", s => s.Latches["irabeth.trickster.primed"] = new[] { "trickster" });
        Invalid("key is a scene id", s => s.Latches["irabeth.trickster.dead.setup"] = new[] { "trickster" });
        Invalid("key is a native binding", s => s.Latches["trickster.was"] = new[] { "trickster" });
        Invalid("key is runtime-derived", s => s.Latches["loss"] = new[] { "trickster" });
        Invalid("key is a relationship flag", s => s.Latches["irabeth.closed"] = new[] { "trickster" });
        Invalid("reserved prefix", s => s.Latches["served.irabeth"] = new[] { "trickster" });
        Invalid("hour prefix", s => s.Latches["hour.trickster.ever"] = new[] { "trickster" });
        // Runtime-derived sources are allowed.
        var derivedSource = Fixture();
        derivedSource.Latches["ever_lost"] = new[] { "loss" };
        Rules.Validate(derivedSource);
    }
}
