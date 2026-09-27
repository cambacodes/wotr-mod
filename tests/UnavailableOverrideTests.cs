using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E2: Relationship.UnavailableOverrides lets an authored Trickster return lift one UnavailableFlag.
// Includes TT-02's acceptance: a returned character stays available after TricksterMythicPathFailed; setups vanish.
internal static class UnavailableOverrideTests
{
    private const string Contact = "280d4712dceb37f4a88e98f1f4c6e64f";

    private static Story Fixture()
    {
        var story = TricksterLatchTests.Fixture();
        var irabeth = story.Relationships["irabeth"];
        irabeth.UnavailableFlags = new[] { "irabeth_dead", "irabeth_gone" };
        irabeth.FailureFlags = new[] { "irabeth_dead" };
        irabeth.UnavailableOverrides["irabeth_dead"] = "irabeth.trickster.returned";
        story.Etudes["irabeth_gone"] = "fedcba9876543210fedcba9876543210";
        story.Etudes["trickster.failed"] = "256f3c081f21ed84fb3612465a76944b"; // TricksterMythicPathFailed
        // The payoff is the device scene that defies the death: it requires the native death explicitly.
        story.Scenes.Single(s => s.Id == "irabeth.trickster.dead.payoff").Requires = new[] { "trickster.ever", "irabeth.trickster.primed", "irabeth_dead" };
        // A physical Chapter 5 visit that needs her actual presence.
        story.Scenes.Add(new Scene
        {
            Id = "irabeth.trickster.dead.visit", Title = "visit", Owner = "Irabeth", Relationship = "irabeth",
            AnswerLists = new[] { "871af36f2ab2b1f40b5de77976c54276" }, ContactUnit = Contact, MinChapter = 5, MaxChapter = 5,
            Requires = new[] { "trickster.ever", "irabeth.trickster.returned" },
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } }
        });
        // An ordinary pre-existing relationship scene with no Trickster gate.
        story.Scenes.Add(new Scene
        {
            Id = "irabeth.ordinary", Title = "ordinary", Owner = "Memory", Relationship = "irabeth", Remote = true, MinChapter = 3,
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } }
        });
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);
        var irabeth = story.Relationships["irabeth"];
        Scene Get(string id) => story.Scenes.Single(s => s.Id == id);

        // Alive: the setup primes the device while the live power holds.
        var alive = new Snapshot { Chapter = 3, Hour = 100 };
        alive.Flags.Add("trickster");
        Rules.Complete(story, alive);
        check(Rules.Available(story, Get("irabeth.trickster.dead.setup"), alive), "Trickster setup unavailable while alive.");
        check(!Rules.Available(story, Get("irabeth.trickster.dead.payoff"), alive), "Death payoff available while she lives.");

        // Dead, not yet returned: every ordinary scene stays blocked; only the device payoff (which requires the death) opens.
        var dead = new Snapshot { Chapter = 5, Hour = 3000 };
        dead.Flags.UnionWith(new[] { "trickster", "irabeth_dead", "irabeth.trickster.primed", "trickster.ever" });
        dead.AvailableContacts.Add(Contact);
        Rules.Complete(story, dead);
        check(!Rules.Available(story, Get("irabeth.ordinary"), dead), "Dead Irabeth reachable without a return.");
        check(!Rules.Available(story, Get("irabeth.trickster.dead.setup"), dead), "Setup that does not require the death bypassed it.");
        check(Rules.Available(story, Get("irabeth.trickster.dead.payoff"), dead), "Trickster death payoff unavailable while she is dead.");
        check(!Rules.Available(story, Get("irabeth.trickster.dead.visit"), dead), "Physical visit available before the return.");
        check(Rules.Failed(irabeth, dead), "Death without a return does not fail the journal objective.");
        check(Rules.Blocks(irabeth, "irabeth_dead", dead), "Death does not block before the return.");
        // Without a declared override, requiring the death does not lift it.
        var plain = Fixture();
        plain.Relationships["irabeth"].UnavailableOverrides.Clear();
        check(!Rules.Available(plain, plain.Scenes.Single(s => s.Id == "irabeth.trickster.dead.payoff"), dead),
            "A scene bypassed an undeclared unavailable flag by requiring it.");

        // Returned: the death stops blocking, including the physical contact guard.
        dead.Flags.Add("irabeth.trickster.returned");
        check(!Rules.Blocks(irabeth, "irabeth_dead", dead), "Return flag does not lift the death.");
        check(Rules.Available(story, Get("irabeth.ordinary"), dead), "Returned Irabeth's ordinary scene still blocked.");
        check(Rules.Available(story, Get("irabeth.trickster.dead.visit"), dead), "Returned Irabeth's physical visit still blocked.");
        check(Rules.ContactAvailable(story, Get("irabeth.trickster.dead.visit"), dead), "Contact guard ignores the return.");
        check(!Rules.Failed(irabeth, dead), "A returned relationship still fails its journal objective.");

        // The override lifts only its own flag: departure still blocks, closure still blocks.
        foreach (string blocker in new[] { "irabeth_gone", "irabeth.closed" })
        {
            var blocked = Program.Copy(dead);
            blocked.Flags.Add(blocker);
            check(!Rules.Available(story, Get("irabeth.ordinary"), blocked), "Return override bypasses an unrelated blocker: " + blocker);
            check(blocker == "irabeth.closed" || !Rules.ContactAvailable(story, Get("irabeth.trickster.dead.visit"), blocked),
                "Return override bypasses an unrelated contact blocker: " + blocker);
        }

        // TT-02 acceptance: Chapter 4 KTC_Fail completes PlayerIsTrickster and starts TricksterMythicPathFailed.
        var failed = Program.Copy(dead);
        failed.Flags.Remove("trickster");
        failed.Flags.Add("trickster.failed");
        failed.Flags.Remove("trickster.ever");
        failed.Flags.Add("trickster.ever"); // persisted by Main.Update when the live power was observed
        Rules.Complete(story, failed);
        foreach (var scene in story.Scenes.Where(s => s.Requires.Contains("trickster.ever")))
            check(Rules.Available(story, scene, failed) || failed.Has(scene.Id), "TT-02: returned Irabeth lost a scene after the path failed: " + scene.Id);
        check(Rules.Available(story, Get("irabeth.trickster.dead.visit"), failed), "TT-02: returned Irabeth's Chapter 5 visit vanished.");
        check(Rules.Available(story, Get("irabeth.ordinary"), failed), "TT-02: returned Irabeth's ordinary scene vanished.");
        foreach (var setup in story.Scenes.Where(s => s.Requires.Contains("trickster")))
            check(!Rules.Available(story, setup, failed), "TT-02: a setup scene is still available after the path failed: " + setup.Id);

        void Invalid(string what, Action<Story> mutate)
        {
            var bad = Fixture();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid unavailable override accepted: " + what);
        }
        Invalid("key not an UnavailableFlag", s => s.Relationships["irabeth"].UnavailableOverrides["trickster"] = "irabeth.trickster.returned");
        Invalid("unwritten value", s => s.Relationships["irabeth"].UnavailableOverrides["irabeth_dead"] = "irabeth.never_written");
        Invalid("native value", s => s.Relationships["irabeth"].UnavailableOverrides["irabeth_dead"] = "trickster.was");
        Invalid("runtime-derived value", s => s.Relationships["irabeth"].UnavailableOverrides["irabeth_dead"] = "loss");
        Invalid("latch value", s => s.Relationships["irabeth"].UnavailableOverrides["irabeth_dead"] = "trickster.ever");
        Invalid("closed-flag value", s => s.Relationships["irabeth"].UnavailableOverrides["irabeth_dead"] = "irabeth.closed");
        Invalid("self value", s => s.Relationships["irabeth"].UnavailableOverrides["irabeth_dead"] = "irabeth_dead");
        Invalid("another unavailable flag as value", s => s.Relationships["irabeth"].UnavailableOverrides["irabeth_dead"] = "irabeth_gone");
    }
}
