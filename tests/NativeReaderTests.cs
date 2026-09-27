using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E10 + ER-5: read-only native readers (UnlockableFlags, QuestObjectives, InventoryItems, StartedQuests).
internal static class NativeReaderTests
{
    private const string Contact = "280d4712dceb37f4a88e98f1f4c6e64f";

    private static Story Fixture()
    {
        var story = new Story();
        story.Relationships["wenduag"] = new Relationship { Title = "Wenduag", StartedFlag = "wenduag.started", ClosedFlag = "wenduag.closed", CommittedFlag = "wenduag.committed" };
        story.UnlockableFlags["wenduag.vellexia_conflict"] = "23cacf7a07480da459b3a59d0fd6da82";           // WenduagRomance_VelexiaConflict_flag
        story.QuestObjectives["seelah.q3_objective_done"] = new[] { "0123456789abcdef0123456789abcdef", "Completed" };
        story.InventoryItems["shamira.syphon_held"] = "d66b1fdc9d313784ca51712640e210c7";                  // EmptySyphon
        story.StartedQuests["seelah.q3_started"] = "5a5a533c9ce630a48b877f9a194840cb";                     // WeightOfMySword_SeelahQ3_quest
        story.Scenes.Add(new Scene
        {
            Id = "wenduag.trickster.conflict.visit", Title = "visit", Owner = "Wenduag", Relationship = "wenduag",
            AnswerLists = new[] { "871af36f2ab2b1f40b5de77976c54276" }, ContactUnit = Contact, MinChapter = 3,
            Requires = new[] { "seelah.q3_started" }, Forbids = new[] { "wenduag.vellexia_conflict", "shamira.syphon_held" },
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } }
        });
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);
        check(Rules.ReaderKeys(story).Count() == 4 && Rules.NativeKeys(story).Contains("seelah.q3_started"), "Reader keys are not native keys.");
        var scene = story.Scenes[0];
        var state = new Snapshot { Chapter = 3, Hour = 10 };
        state.AvailableContacts.Add(Contact);
        check(!Rules.Available(story, scene, state), "Started-quest reader requirement ignored.");
        state.Flags.Add("seelah.q3_started");
        check(Rules.Available(story, scene, state) && Rules.ContactAvailable(story, scene, state), "Reader-gated scene unavailable.");
        // Reader keys are native: the live contact guard honours their forbids (IsNativeFlag).
        foreach (var key in new[] { "wenduag.vellexia_conflict", "shamira.syphon_held" })
        {
            var blocked = Program.Copy(state);
            blocked.Flags.Add(key);
            check(!Rules.ContactAvailable(story, scene, blocked), "Contact guard ignores native reader forbid: " + key);
        }
        // A missing reader binding degrades dependent composites like any native key.
        story.Derived["wenduag.conflicted_returned"] = new[] { new[] { "wenduag.vellexia_conflict", "seelah.q3_started" } };
        Rules.Validate(story);
        var missing = new HashSet<string> { "wenduag.vellexia_conflict" };
        Rules.PropagateMissing(story, missing);
        check(missing.Contains("wenduag.conflicted_returned"), "Missing reader binding not inherited by a composite.");

        void Invalid(string what, Action<Story> mutate)
        {
            var bad = Fixture();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid native reader accepted: " + what);
        }
        Invalid("bad flag guid", s => s.UnlockableFlags["wenduag.vellexia_conflict"] = "nope");
        Invalid("empty item guid", s => s.InventoryItems["shamira.syphon_held"] = "00000000000000000000000000000000");
        Invalid("objective state", s => s.QuestObjectives["seelah.q3_objective_done"] = new[] { "0123456789abcdef0123456789abcdef", "Done" });
        Invalid("objective shape", s => s.QuestObjectives["seelah.q3_objective_done"] = new[] { "0123456789abcdef0123456789abcdef" });
        Invalid("key in two reader kinds", s => s.StartedQuests["wenduag.vellexia_conflict"] = "5a5a533c9ce630a48b877f9a194840cb");
        Invalid("key also an etude", s => s.Etudes["seelah.q3_started"] = "5a5a533c9ce630a48b877f9a194840cb");
        Invalid("key authored by a scene", s => s.InventoryItems["wenduag.trickster.conflict.visit"] = "d66b1fdc9d313784ca51712640e210c7");
        Invalid("key runtime-derived", s => s.UnlockableFlags["loss"] = "23cacf7a07480da459b3a59d0fd6da82");
        Invalid("reserved key", s => s.UnlockableFlags["served.wenduag"] = "23cacf7a07480da459b3a59d0fd6da82");
        Invalid("null collection", s => s.InventoryItems = null!);
    }
}
