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
            var text = string.Join(" ", Rules.VisibleParagraphs(page, state).Select(p => SurfaceIds.Of(story, p)));
            check(!SurfaceIds.Has(text, "[chadali.trickster.epilogue.lucky_night/page/paragraph/15]"), "l12 Chadali false closure: " + speaker);
            check(SurfaceIds.Has(text, "[chadali.trickster.epilogue.lucky_night/page/paragraph/48]"), "l12 Chadali earned wager disappears: " + speaker);
            state.Flags.Remove("ending.trickster_allplanes");
            state.Flags.Add("ending.wound_closed");
            Rules.Complete(story, state);
            text = string.Join(" ", Rules.VisibleParagraphs(page, state).Select(p => SurfaceIds.Of(story, p)));
            check(SurfaceIds.Has(text, "[chadali.trickster.epilogue.lucky_night/page/paragraph/15]"), "l12 native closure paragraph lost: " + speaker);
        }
    }
}
