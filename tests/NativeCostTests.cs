using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E11: native costs on a choice (crusade resources, whitelisted item removal) and the konomi.retained_hostile observation.
internal static class NativeCostTests
{
    private const string Scale = "816f244523b5455a85ae06db452d4330"; // TerendelevScaleItem

    private static Story Fixture()
    {
        var story = new Story();
        story.Relationships["terendelev"] = new Relationship { Title = "Terendelev", StartedFlag = "terendelev.started",
            ClosedFlag = "terendelev.closed", CommittedFlag = "terendelev.committed" };
        story.InventoryItems["terendelev.scale_held"] = Scale;
        story.RemovableItems = new[] { Scale };
        story.Scenes.Add(new Scene
        {
            Id = "terendelev.trickster.killed.stolen_half", Title = "x", Owner = "Memory", Relationship = "terendelev", Remote = true,
            MinChapter = 3, Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> {
                new Choice { Text = "Pay", Requires = new[] { "terendelev.scale_held" }, RemoveItem = Scale,
                    Crusade = new CrusadeChoice { Resource = "Finances", Amount = -500 }, Set = new[] { "terendelev.trickster.cost.scale" } },
                new Choice { Text = "Gain", Crusade = new CrusadeChoice { Resource = "Favors", Amount = 3 } } } } }
        });
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        Rules.Validate(Fixture());
        check(Rules.CrusadeResources.SequenceEqual(new[] { "Finances", "Materials", "Favors" }), "Crusade resource names changed.");
        // A scene-level requirement also gates the removal.
        var sceneGate = Fixture();
        var pay = sceneGate.Scenes[0].Nodes[0].Choices[0];
        pay.Requires = Array.Empty<string>();
        sceneGate.Scenes[0].Requires = new[] { "terendelev.scale_held" };
        Rules.Validate(sceneGate);
        // The runtime-only hostility observation is native evidence: never authored, honoured by the live contact guard.
        var hostile = Fixture();
        hostile.Scenes[0].Forbids = new[] { "konomi.retained_hostile" };
        Rules.Validate(hostile);
        var state = new Snapshot { Chapter = 3, Hour = 10 };
        state.Flags.Add("konomi.retained_hostile");
        check(!Rules.ContactAvailable(hostile, hostile.Scenes[0], state), "konomi.retained_hostile is not native evidence for the live guard.");

        void Invalid(string what, Action<Story, Choice> mutate)
        {
            var bad = Fixture();
            mutate(bad, bad.Scenes[0].Nodes[0].Choices[0]);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid native cost accepted: " + what);
        }
        Invalid("unknown resource", (_, c) => c.Crusade = new CrusadeChoice { Resource = "Gold", Amount = 5 });
        Invalid("zero amount", (_, c) => c.Crusade = new CrusadeChoice { Resource = "Finances", Amount = 0 });
        Invalid("huge amount", (_, c) => c.Crusade = new CrusadeChoice { Resource = "Finances", Amount = 1000000 });
        Invalid("before the crusade exists", (s, _) => s.Scenes[0].MinChapter = 2);
        Invalid("item not whitelisted", (s, _) => s.RemovableItems = Array.Empty<string>());
        Invalid("removal not gated on holding it", (_, c) => c.Requires = Array.Empty<string>());
        Invalid("gate bound to another item", (s, _) => s.InventoryItems["terendelev.scale_held"] = "d66b1fdc9d313784ca51712640e210c7");
        Invalid("bad whitelist guid", (s, _) => s.RemovableItems = new[] { Scale, "nope" });
        Invalid("duplicate whitelist", (s, _) => s.RemovableItems = new[] { Scale, Scale });
        Invalid("authored hostility", (_, c) => c.Set = new[] { "konomi.retained_hostile" });
        Invalid("epilogue cost", (s, _) => { s.Scenes[0].Owner = "Epilogue"; s.Scenes[0].Remote = false; });
    }
}
