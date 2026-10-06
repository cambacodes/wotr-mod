using System;
using System.Linq;
using Tirabade;

// Engine-q2 item 5: Galfrey's native Queen slides (CueSequence_Queen Cue_0259, Cue_0502: "Queen Galfrey died...") give way to
// her reclaimed reign only on the Trickster path, after her return and the crown taken back.
internal static class GalfreyQueenSlideTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        foreach (var cue in new[] { "f5906acda82efd5468cb72aff2e68f7e", "becde70692b74ab4eba1d0cf82d2958f" })
        {
            if (!story.NativeEpilogueEdits.TryGetValue(cue, out var edit)) {  continue; }
            var variants = Rules.EditVariants(edit);
            var scenes = Rules.EditScenes(story, variants);
            check(edit.Sequence == "bb9d36fd37d74bf4792931d6052a7d44" && edit.Key == "e61f5ab8-ec4c-439f-b035-802558deebe0" && variants.Length == 1
                  && scenes[0]?.Relationship == "galfrey" && Rules.IsNativeReplacement(story, scenes[0]!),
                "Galfrey Queen slide: " + cue + " is not her reclaimed reign on CueSequence_Queen.");
            foreach (var (what, flags, plays) in new (string, string[], bool)[] {
                ("returned and crowned", new[] { "trickster", "trickster.ever", "galfrey.dead", "galfrey.trickster.returned", "galfrey.trickster.crown_reclaimed" }, true),
                ("returned and crowned, the path since lost", new[] { "trickster.was", "trickster.ever", "trickster.failed", "galfrey.dead", "galfrey.trickster.returned", "galfrey.trickster.crown_reclaimed" }, true),
                ("returned, crown left (Kitrane)", new[] { "trickster", "trickster.ever", "galfrey.dead", "galfrey.trickster.returned" }, false),
                ("dead, no return", new[] { "trickster", "trickster.ever", "galfrey.dead" }, false),
                ("off the Trickster path", new[] { "galfrey.dead", "galfrey.trickster.returned", "galfrey.trickster.crown_reclaimed" }, false),
                ("closed", new[] { "trickster", "trickster.ever", "galfrey.dead", "galfrey.trickster.returned", "galfrey.trickster.crown_reclaimed", "galfrey.closed" }, false),
                ("the Commander dead in the Wound", new[] { "trickster", "trickster.ever", "galfrey.dead", "galfrey.trickster.returned", "galfrey.trickster.crown_reclaimed", "sacrifice" }, true) })   // the slide never stages the Commander (COMMANDER_ABSENT): her reign outlives an unreturned sacrifice
            {
                var state = new Snapshot { Chapter = 6, Hour = 30000 };
                state.Flags.UnionWith(flags);
                Rules.Complete(story, state);
                check((Rules.SelectNativeEditVariant(story, variants, scenes, state) == 0) == plays, "Galfrey Queen slide " + cue + ", " + what);
            }
        }
    }
}
