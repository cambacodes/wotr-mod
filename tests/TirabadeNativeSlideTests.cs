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

    private static Snapshot World(Story story, params string[] flags)
    {
        var state = new Snapshot { Chapter = 6 };
        state.Flags.UnionWith(flags);
        if (state.Has(Committed))
            state.Flags.UnionWith(new[] { "anevia.trickster.gate_seen", "anevia.trickster.terms_kept" });
        Rules.Complete(story, state);
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
        // eng7-l03: old variants retain their indices; coverage of appended variants lives in the inventory suite.
        check(variants.Take(5).Select(v => v.Replacement).SequenceEqual(new[] { Together, Back, WidowCommitted, Widow, South }),
            "Trk_Tirabade_NativeSlide: variant order changed (the most specific state must come first).");
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        string? Selected(Snapshot state)
        {
            int i = Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), state); // eng7-l03
            return i < 0 ? null : variants[i].Replacement;
        }
        // Each row: the world, then the variant that must play (null: the native "No one ever saw her again." plays).
        var rows = new (string What, Snapshot World, string? Expected)[]
        {
            ("neither returned", World(story, "trickster.ever", "irabeth_dead", "anevia_gone"), null),
            ("neither returned, Anevia committed before she left", World(story, "trickster.ever", "irabeth_dead", "anevia_gone", Committed), null),
            ("Anevia returned, Beth dead, uncommitted", World(story, "trickster.ever", "irabeth_dead", "anevia_gone", Returned), Widow),
            ("Anevia returned, Beth dead, declined", World(story, "trickster.ever", "irabeth_dead", "anevia_gone", Returned, "anevia.trickster.declined"), Widow),
            ("Anevia returned, Beth dead, closed", World(story, "trickster.ever", "irabeth_dead", "anevia_gone", Returned, "anevia.closed"), Widow),
            ("Anevia returned, Beth dead, committed", World(story, "trickster.ever", "irabeth_dead", "anevia_gone", Returned, Committed), WidowCommitted),
            ("Anevia returned, Beth killed by the Commander, committed",
                World(story, "trickster.ever", "irabeth_dead", "anevia_gone", Returned, Committed, "anevia.irabeth_killed_by_commander"), Widow),
            ("Anevia returned, murder confessed publicly with its cost",
                World(story, "trickster.ever", "irabeth_dead", "anevia_gone", Returned, Committed,
                    "anevia.irabeth_killed_by_commander", "anevia.lover", "anevia.trickster.said_it", "anevia.trickster.cost.muster_confession"), WidowCommitted),
            ("both returned, uncommitted", World(story, "trickster.ever", "irabeth_dead", "anevia_gone", Returned, IrabethReturned), Back),
            ("both returned, Irabeth committed only", World(story, "trickster.ever", "irabeth_dead", "anevia_gone", Returned, IrabethReturned, "irabeth.committed"), Back),
            ("both returned, Anevia committed", World(story, "trickster.ever", "irabeth_dead", "anevia_gone", Returned, IrabethReturned, Committed), Together),
            ("Beth returned, Anevia still away", World(story, "trickster.ever", "irabeth_dead", "anevia_gone", IrabethReturned), South),
            ("Beth returned, Anevia away, Beth committed", World(story, "trickster.ever", "irabeth_dead", "anevia_gone", IrabethReturned, "irabeth.committed"), South),
        };
        foreach (var row in rows)
            check(Selected(row.World) == row.Expected,
                "Trk_Tirabade_NativeSlide: " + row.What + " selects " + (Selected(row.World) ?? "the native slide") + ", expected "
                + (row.Expected ?? "the native slide") + ".");
        // Every variant needs a Trickster return: off the Trickster (no return flag) the native slide always plays.
        foreach (var variant in variants.Take(5)) // eng7-l03: retained save contracts
            check(variant.When.All(group => group.Contains(Returned) || group.Contains(IrabethReturned)),
                "Trk_Tirabade_NativeSlide: a variant plays without a Trickster return: " + variant.Replacement);
        // The picture: Beth back -> the page's pair picture; Beth dead or Anevia away -> the native cue's own image change.
        check(variants.Where(v => v.Replacement == Together || v.Replacement == Back).All(v => !v.KeepNativeImage)
              && variants.Take(5).Where(v => v.Replacement != Together && v.Replacement != Back).All(v => v.KeepNativeImage), // eng7-l03
            "Trk_Tirabade_NativeSlide: the slide picture does not follow who is alive and present.");
        // Ownership and shape: Anevia's states belong to her relationship, Beth-only to Irabeth's; replacements never stand alone.
        foreach (var variant in variants.Take(5)) // eng7-l03: appended ownership/shape checked by inventory
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
        RunLeft(story, check);
    }

    // Cue_0310 (IrabethGone + AneviaGone, both left at the Coronation after the Commander's betrayal): only Anevia's return
    // changes it (Irabeth has no Trickster return from that departure); Beth stays alive and away, so the native picture stays.
    private const string Cue0310 = "ccd140dbf2603734aa323261c2445bec";
    private const string Left = "anevia.trickster.epilogue.native_tirabade_left";
    private const string LeftCommitted = "anevia.trickster.epilogue.native_tirabade_left_committed";

    private static void RunLeft(Story story, Action<bool, string> check)
    {
        check(story.NativeEpilogueEdits.TryGetValue(Cue0310, out var edit), "Trk_Tirabade_NativeSlideLeft: Cue_0310 is not replaced.");
        if (edit == null) return;
        var variants = Rules.EditVariants(edit);
        check(edit.Page == "ae1f824fe248d9f4aac7d39ec2e12140" && edit.Sequence == "f8d7f50e3bb88c143834d234c0b24474"
              && edit.Key == "cc716238-3702-4913-977d-6189665672b7"
              && variants.Take(2).Select(v => v.Replacement).SequenceEqual(new[] { LeftCommitted, Left }) && variants.All(v => v.KeepNativeImage), // eng7-l03
            "Trk_Tirabade_NativeSlideLeft: Cue_0310 evidence, variant order or picture changed.");
        check(!story.Relationships["irabeth"].TricksterAccess.Values.Any(access => access.Detect.Contains("irabeth_gone")),
            "Trk_Tirabade_NativeSlideLeft: Irabeth gained a return from IrabethGone; Cue_0310 needs her variant.");
        string? Selected(Snapshot state)
        {
            int i = Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), state); // eng7-l03
            return i < 0 ? null : variants[i].Replacement;
        }
        var rows = new (string What, Snapshot World, string? Expected)[]
        {
            ("both left, nothing returned", World(story, "trickster.ever", "irabeth_gone", "anevia_gone"), null),
            ("both left, Anevia committed before she left", World(story, "trickster.ever", "irabeth_gone", "anevia_gone", Committed), null),
            ("both left, Anevia returned, uncommitted", World(story, "trickster.ever", "irabeth_gone", "anevia_gone", Returned), Left),
            ("both left, Anevia returned and closed", World(story, "trickster.ever", "irabeth_gone", "anevia_gone", Returned, "anevia.closed"), Left),
            ("both left, Anevia returned, committed", World(story, "trickster.ever", "irabeth_gone", "anevia_gone", Returned, Committed), LeftCommitted),
        };
        foreach (var row in rows)
            check(Selected(row.World) == row.Expected, "Trk_Tirabade_NativeSlideLeft: " + row.What + " selects "
                + (Selected(row.World) ?? "the native slide") + ", expected " + (row.Expected ?? "the native slide") + ".");
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        foreach (var id in new[] { Left, LeftCommitted })
        {
            var scene = S(id);
            string text = scene.Nodes[0].Text;
            check(scene.Relationship == "anevia" && Rules.IsNativeReplacement(story, scene) && scene.Nodes.Count == 1
                  && text.Contains("betrayal") && text.Length < 520 && !text.Contains("Kenabres"),
                "Trk_Tirabade_NativeSlideLeft: replacement owner, shape or canon frame is wrong: " + id);
        }
        // Must-remain-true: the resentment never evaporates; her terms and Beth first when committed; no door when not.
        check(S(LeftCommitted).Nodes[0].Text.Contains("own terms") && S(LeftCommitted).Nodes[0].Text.Contains("never forgave the betrayal")
              && S(LeftCommitted).Nodes[0].Text.Contains("Beth always came first") && !S(Left).Nodes[0].Text.Contains("door"),
            "Trk_Tirabade_NativeSlideLeft: the committed slide drops her terms, Beth or the grudge, or the uncommitted one gains a door.");
    }
}
