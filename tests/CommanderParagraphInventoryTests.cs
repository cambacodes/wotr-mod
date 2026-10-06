using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// eng7-l12: render every sacrifice continuation, then derive a real native return.
internal static class CommanderParagraphInventoryTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var scene = story.Scenes.Single(s => s.Id == "anevia.ending_sacrifice");
        var page = scene.Nodes.Single(n => n.Id == "end");
        foreach (var gate in new[] { "anevia.trickster.terms_kept", "anevia.trickster.cost.her_key", "anevia.trickster.late_committed" })
        {
            var state = new Snapshot { Chapter = 6 };
            state.Flags.UnionWith(new[] { "sacrifice", "trickster", "anevia.trickster.returned", "irabeth.trickster.returned",
                "irabeth_dead", gate, "anevia.trickster.gate_seen", "anevia.trickster.hand_taken" });
            if (gate.EndsWith("late_committed"))
                HouseholdTests.Earn(story, state, "anevia.trickster.late_committed");
            state.Flags.Remove("anevia.trickster.late_committed"); // derive it from the earned gates
            Rules.Complete(story, state);
            var text = string.Join(" ", Rules.VisibleParagraphs(page, state).Select(p => p.Text));
            check(!text.Contains("conversation from the gate picked up") && !text.Contains("carrying both their packs")
                && !text.Contains("made the Commander keep it too") && !text.Contains("second kind of love"), "l12 living future after fatal sacrifice: " + gate);
            state.Flags.Remove("irabeth.trickster.returned");
            state = Fresh(story, state);
            Rules.Complete(story, state);
            text = string.Join(" ", Rules.VisibleParagraphs(page, state).Select(p => p.Text));
            check(!text.Contains("then one winter night she didn't"), "l12 dead Commander enters widow's bed: " + gate);
            state.Flags.Add("ending.trickster_allplanes");
            state.Flags.UnionWith(new[] { "irabeth.trickster.returned", "anevia.open_future", "anevia.developed" });
            state = Fresh(story, state);
            Rules.Complete(story, state);
            check(state.Has("trickster.commander_back"), "l12 native earned return did not derive");
            // The living sibling must retain the same earned continuation. The
            // mourning scene itself correctly excludes a returned Commander.
            var livingScene = story.Scenes.Single(s => s.Id == "anevia.ending_open");
            check(Program.CurrentAvailable(story, livingScene, state), "l12 earned-return living sibling unavailable");
            var living = livingScene.Nodes.Single(n => n.Id == "end");
            text = string.Join(" ", Rules.VisibleParagraphs(living, state).Select(p => p.Text));
            if (gate.EndsWith("late_committed"))
                check(text.Contains("conversation from the gate picked up"), "l12 earned-return reunion overblocked");
            if (gate.EndsWith("terms_kept"))
                check(text.Contains("made the Commander keep it too"), "l12 earned-return door rule overblocked");
        }
    }

    // Main.State observes native inputs into a NEW Snapshot each time. Derived
    // facts are not saved; never reuse yesterday's computed death as an input.
    private static Snapshot Fresh(Story story, Snapshot prior) => new Snapshot { Chapter = prior.Chapter,
        Flags = new HashSet<string>(prior.Flags.Where(f => !story.Derived.ContainsKey(f) && !story.Counts.ContainsKey(f))) };
}
