using System;
using System.Linq;
using Tirabade;

// eng7-l12: render actual native closure and Crossroads paragraph alternatives.
internal static class WorldFactInventoryTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var scene = story.Scenes.Single(s => s.Id == "chadali.trickster.epilogue.lucky_night");
        var page = scene.Nodes.Single(n => n.Id == "page");
        // Only hoped_aloud exists in this integration snapshot; the separate
        // Chadali-spoke paragraph cited by the audit is absent, not reintroduced.
        foreach (var speaker in new[] { "hoped_aloud" })
        {
            var state = new Snapshot { Chapter = 6 };
            state.Flags.Add("chadali.wagers." + speaker);
            state.Flags.Add("trickster");
            state.Flags.Add("ending.trickster_allplanes");
            Rules.Complete(story, state);
            var text = string.Join(" ", Rules.VisibleParagraphs(page, state).Select(p => p.Text));
            check(!text.Contains("Wound closed"), "l12 Chadali false closure: " + speaker);
            check(text.Contains("fighting at Threshold ended"), "l12 Chadali earned wager disappears: " + speaker);
            state.Flags.Remove("ending.trickster_allplanes");
            state.Flags.Add("ending.wound_closed");
            Rules.Complete(story, state);
            text = string.Join(" ", Rules.VisibleParagraphs(page, state).Select(p => p.Text));
            check(text.Contains("Wound closed"), "l12 native closure paragraph lost: " + speaker);
        }
        var aeon = story.Scenes.Single(s => s.Id == "irabeth.ending_aeon").Nodes[0].Text;
        check(aeon.Contains("never started a family") && aeon.Contains("River Kingdoms") && !aeon.Contains("married a spy"), "l12 Aeon marriage contradicts native sequence");
        check(!story.Scenes.Single(s => s.Id == "kaylessa.trickster.epilogue.declined").Nodes[0].Text.Contains("Wound closed"), "l12 declined Kaylessa closes Crossroads");
    }
}
