using System;
using System.Linq;
using Tirabade;

// Engine queue 7b: Wenduag's BookPage_0349 Cue_0580 ("refused to ascend") for a committed Wenduag, with the E14d delivery
// predicate (Rules.SelectNativeEditVariant with the story: When AND the scene available on one snapshot).
internal static class WenduagNativeAscentTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string Cue0580 = "4bb3706172f1ed54ca11db96254c4638";
        check(story.NativeEpilogueEdits.TryGetValue(Cue0580, out var edit), "Trk_Wenduag_Ascent: Cue_0580 is not replaced.");
        if (edit == null) return;
        var variants = Rules.EditVariants(edit);
        var scenes = Rules.EditScenes(story, variants);
        check(edit.Page == "223fd069ee25c784db2df011adbf10f8" && variants.Length == 1 && scenes[0]?.Relationship == "wenduag"
              && scenes[0]!.Nodes[0].Text.Contains("refused to ascend"), "Trk_Wenduag_Ascent: the edit is not her own refusal on BookPage_0349.");
        var rows = new (string What, string[] Flags, bool Plays)[]
        {
            ("committed", new[] { "trickster", "trickster.ever", "wenduag.committed" }, true),
            ("uncommitted", new[] { "trickster", "trickster.ever", "wenduag.started" }, false),
            ("committed, closed", new[] { "trickster", "trickster.ever", "wenduag.committed", "wenduag.closed" }, false),
            ("committed, Q3 kill", new[] { "trickster", "trickster.ever", "wenduag.committed", "wenduag.q3_killed" }, false),
            ("committed, unsurvived sacrifice", new[] { "trickster", "trickster.ever", "wenduag.committed", "sacrifice" }, false),
            ("committed, the Commander back", new[] { "trickster", "trickster.ever", "wenduag.committed", "sacrifice", "trickster.commander_back" }, true),
            // Engine-q2 (T6a): the edit reads the current path; a run that left it keeps the native slide.
            ("committed, the path failed in Chapter 4", new[] { "trickster.was", "trickster.ever", "trickster.failed", "wenduag.committed" }, false),
            ("committed, a Trickster turned Legend", new[] { "trickster", "trickster.ever", "trickster.failed", "legend", "wenduag.committed" }, false),
            ("committed, degraded", new[] { "trickster", "trickster.ever", "wenduag.committed", Rules.DegradedPrefix + "wenduag" }, false),
        };
        foreach (var row in rows)
        {
            var state = new Snapshot { Chapter = 6 };
            state.Flags.UnionWith(row.Flags);
            Rules.Complete(story, state);
            check((Rules.SelectNativeEditVariant(story, variants, scenes, state) == 0) == row.Plays, "Trk_Wenduag_Ascent, " + row.What);
        }
    }
}
