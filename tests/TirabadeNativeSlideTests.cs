using System;
using System.Linq;
using Tirabade;

// E14d extension: the native Tirabade slide (Epilogues/BookPage_0307 Cue_0311, "No one ever saw her again.") on the Trickster.
// IrabethDead and AneviaGone stay Playing after a return, so the native cue's own checker still passes; the RRT variants
// decide which text plays. One state per row: exactly the expected variant (or the native cue) is selected.
internal static class TirabadeNativeSlideTests
{
    private const string Cue0311 = "3a3e561c6b05a284d93eb3bff7b712a6";
    private const string Returned = "anevia.trickster.returned";
    private const string IrabethReturned = "irabeth.trickster.returned";
    private const string Committed = "anevia.committed";
    private const string Together = "anevia.trickster.epilogue.native_tirabade_together";
    private const string Back = "anevia.trickster.epilogue.native_tirabade_back";
    private const string WidowCommitted = "anevia.trickster.epilogue.native_tirabade_widow_committed";
    private const string Widow = "anevia.trickster.epilogue.native_tirabade_widow";
    private const string South = "irabeth.trickster.epilogue.native_tirabade_south";

    private static Snapshot World(params string[] flags)
    {
        var state = new Snapshot { Chapter = 6 };
        state.Flags.UnionWith(flags);
        return state;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        check(story.NativeEpilogueEdits.TryGetValue(Cue0311, out var edit), "Trk_Tirabade_NativeSlide: Cue_0311 is not replaced.");
        if (edit == null) return;
        var variants = Rules.EditVariants(edit);
        check(edit.Page == "ae1f824fe248d9f4aac7d39ec2e12140" && edit.Sequence == "f8d7f50e3bb88c143834d234c0b24474"
              && edit.Key == "4c278ba4-5217-4fae-afec-47c6f6597e00",
            "Trk_Tirabade_NativeSlide: Cue_0311 evidence (BookPage_0307, CueSequence_Special, text key) changed.");
        check(variants.Select(v => v.Replacement).SequenceEqual(new[] { Together, Back, WidowCommitted, Widow, South }),
            "Trk_Tirabade_NativeSlide: variant order changed (the most specific state must come first).");
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        string? Selected(Snapshot state)
        {
            int i = Rules.SelectNativeEditVariant(variants, state);
            return i < 0 ? null : variants[i].Replacement;
        }
        // Each row: the world, then the variant that must play (null: the native "No one ever saw her again." plays).
        var rows = new (string What, Snapshot World, string? Expected)[]
        {
            ("neither returned", World("trickster.ever", "irabeth_dead", "anevia_gone"), null),
            ("neither returned, Anevia committed before she left", World("trickster.ever", "irabeth_dead", "anevia_gone", Committed), null),
            ("Anevia returned, Beth dead, uncommitted", World("trickster.ever", "irabeth_dead", "anevia_gone", Returned), Widow),
            ("Anevia returned, Beth dead, declined", World("trickster.ever", "irabeth_dead", "anevia_gone", Returned, "anevia.trickster.declined"), Widow),
            ("Anevia returned, Beth dead, closed", World("trickster.ever", "irabeth_dead", "anevia_gone", Returned, "anevia.closed"), Widow),
            ("Anevia returned, Beth dead, committed", World("trickster.ever", "irabeth_dead", "anevia_gone", Returned, Committed), WidowCommitted),
            ("Anevia returned, Beth killed by the Commander, committed",
                World("trickster.ever", "irabeth_dead", "anevia_gone", Returned, Committed, "anevia.irabeth_killed_by_commander"), WidowCommitted),
            ("both returned, uncommitted", World("trickster.ever", "irabeth_dead", "anevia_gone", Returned, IrabethReturned), Back),
            ("both returned, Irabeth committed only", World("trickster.ever", "irabeth_dead", "anevia_gone", Returned, IrabethReturned, "irabeth.committed"), Back),
            ("both returned, Anevia committed", World("trickster.ever", "irabeth_dead", "anevia_gone", Returned, IrabethReturned, Committed), Together),
            ("Beth returned, Anevia still away", World("trickster.ever", "irabeth_dead", "anevia_gone", IrabethReturned), South),
            ("Beth returned, Anevia away, Beth committed", World("trickster.ever", "irabeth_dead", "anevia_gone", IrabethReturned, "irabeth.committed"), South),
        };
        foreach (var row in rows)
            check(Selected(row.World) == row.Expected,
                "Trk_Tirabade_NativeSlide: " + row.What + " selects " + (Selected(row.World) ?? "the native slide") + ", expected "
                + (row.Expected ?? "the native slide") + ".");
        // Every variant needs a Trickster return: off the Trickster (no return flag) the native slide always plays.
        foreach (var variant in variants)
            check(variant.When.All(group => group.Contains(Returned) || group.Contains(IrabethReturned)),
                "Trk_Tirabade_NativeSlide: a variant plays without a Trickster return: " + variant.Replacement);
        // The picture: Beth back -> the page's pair picture; Beth dead or Anevia away -> the native cue's own image change.
        check(variants.Where(v => v.Replacement == Together || v.Replacement == Back).All(v => !v.KeepNativeImage)
              && variants.Where(v => v.Replacement != Together && v.Replacement != Back).All(v => v.KeepNativeImage),
            "Trk_Tirabade_NativeSlide: the slide picture does not follow who is alive and present.");
        // Ownership and shape: Anevia's states belong to her relationship, Beth-only to Irabeth's; replacements never stand alone.
        foreach (var variant in variants)
        {
            var scene = S(variant.Replacement);
            check(scene.Relationship == (variant.Replacement == South ? "irabeth" : "anevia") && Rules.IsNativeReplacement(story, scene)
                  && scene.Nodes.Count == 1 && scene.Nodes[0].Paragraphs.Count == 0,
                "Trk_Tirabade_NativeSlide: replacement owner or shape is wrong: " + variant.Replacement);
            string text = scene.Nodes[0].Text;
            check(!text.Contains("ever saw her again") && text.Contains("Anevia") && text.Length < 520,
                "Trk_Tirabade_NativeSlide: replacement keeps the native fate or outgrows the slide: " + variant.Replacement);
        }
        // Must-remain-true (anevia.md): she came back by her own choice and on her own terms; Beth comes first.
        check(S(Together).Nodes[0].Text.Contains("own terms") && S(Together).Nodes[0].Text.Contains("Beth always came first")
              && S(WidowCommitted).Nodes[0].Text.Contains("own terms") && S(WidowCommitted).Nodes[0].Text.Contains("Beth's name"),
            "Trk_Tirabade_NativeSlide: a committed slide drops her terms or Beth.");
        check(S(South).Nodes[0].Text.Contains("never came back to Drezen") && !S(Widow).Nodes[0].Text.Contains("door"),
            "Trk_Tirabade_NativeSlide: an uncommitted or absent Anevia is given a door she never walked through.");
        // Save names: variant 0 keeps the original E14d cue name; the others are named after their replacement scene.
        check(Rules.NativeEditCueName(Cue0311, edit, 0) == "native-edit." + Cue0311
              && Rules.NativeEditCueName(Cue0311, edit, 4) == "native-edit." + Cue0311 + "." + South,
            "Trk_Tirabade_NativeSlide: variant cue names changed (save references).");
    }
}
