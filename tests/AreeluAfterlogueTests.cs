using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E14i: Areelu's afterlogue line (Epilogues_afterlogues/Cue_0001 continues, Strategy First, into one account of how her life
// ended) for a continuing romance. The native selection is modelled from blueprints.zip (the managed suite runs the archive's
// own checkers); the RRT side is the shipped Story, with its Derived keys completed as Main.BuildState does.
internal static class AreeluAfterlogueTests
{
    private const string Cue0004 = "825786e8c5db4511ae30950bb286f0e9", Cue0005 = "1b53c189b767412f921b8294b980a51c";
    private const string Spared = "areelu.trickster.afterlogue.spared", Mortal = "areelu.trickster.afterlogue.mortal";

    // Cue_0001's Continue, in order, with the archive's checkers (etude Started or Playing).
    private static string NativeLine(bool ascended, bool notMyBusiness, bool redeemed, bool aeonInPast, bool dead, bool sacrificeWound, bool persuaded)
    {
        if (ascended) return "Cue_0002";
        if (notMyBusiness) return "Cue_28";
        if (redeemed) return "Cue_0003";
        if (aeonInPast) return "Cue_0006";
        if (!redeemed && !dead) return Cue0004;
        if (sacrificeWound && persuaded) return "Cue_29";
        return Cue0005;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        bool shipped = story.NativeEpilogueEdits.TryGetValue(Cue0004, out var cottage) & story.NativeEpilogueEdits.TryGetValue(Cue0005, out var death);
        check(shipped, "Trk_Areelu_Afterlogue: Cue_0004 and Cue_0005 are not both replaced.");
        if (!shipped) return;
        foreach (var edit in new[] { cottage!, death! })
            check(edit.Parent == "5b567bdd747e497cb9f6984b1ca1dfc8" && edit.Dialog == "57e18f5158904030a84a772fb361ceb4" && edit.Page == "" && edit.Sequence == ""
                  && Rules.EditVariants(edit).Length == (edit.Replacement == Spared ? 4 : 2) && story.Scenes.Single(s => s.Id == edit.Replacement).Relationship == "areelu",
                "Trk_Areelu_Afterlogue: an afterlogue edit is not an E14i dialog edit on Cue_0001 with fate-specific Areelu lines.");
        check(cottage!.Replacement == Spared && death!.Replacement == Mortal, "Trk_Areelu_Afterlogue: the cottage and death lines swapped.");
        string Line(string id) => SurfaceIds.Of(story, story.Scenes.Single(s => s.Id == id).Nodes[0]);
        check(new[] { Spared, Mortal }.All(id => SurfaceIds.Has(Line(id), "[areelu.trickster.afterlogue.spared/line][areelu.trickster.afterlogue.mortal/line]")),
            "Trk_Areelu_Afterlogue: a line does not open as her native account does, or still ends in the cottage.");
        check(SurfaceIds.Has(Line(Mortal), "[areelu.trickster.afterlogue.mortal/line]"),
            "Trk_Areelu_Afterlogue: only the rewritten (graft drawn) line makes her mortal.");

        const string T = "areelu.trickster.";
        var common = new[] { "trickster", "trickster.ever", T + "wager_struck", T + "bet_offered" };
        var rewrite = common.Concat(new[] { "areelu.sacrifice_trickster", "areelu.dead_fight", T + "graft_drawn" }).ToArray();
        var punch = common.Concat(new[] { "sacrifice", "ending.trickster", "trickster.commander_back" }).ToArray();
        // (what, RRT flags or null for the mod disabled, the native etudes: dead (AreeluDead), wound sacrifice, redeemed; expected line)
        var rows = new (string What, string[]? Flags, bool Dead, bool Wound, bool Redeemed, string Expected)[]
        {
            ("rewrite, committed", rewrite.Append("areelu.committed").ToArray(), true, false, false, Mortal),
            ("rewrite, unraised", rewrite, true, false, false, "areelu.trickster.afterlogue.mortal_wager"),
            ("rewrite, declined", rewrite.Append(T + "declined").ToArray(), true, false, false, Cue0005),
            ("rewrite, declined then committed", rewrite.Concat(new[] { T + "declined", "areelu.committed" }).ToArray(), true, false, false, Mortal),
            ("rewrite, stake only", rewrite.Append(T + "stake_only").ToArray(), true, false, false, Cue0005),
            ("rewrite, closed", rewrite.Append("areelu.closed").ToArray(), true, false, false, Cue0005),
            ("rewrite, mod disabled", null, true, false, false, Cue0005),
            ("the sacrifice without the graft drawn", common.Concat(new[] { "areelu.sacrifice_trickster", "areelu.dead_fight", "areelu.committed" }).ToArray(),
                true, false, false, Cue0005),
            ("never on screen (no bet, lens or late terms)", new[] { "trickster.ever", T + "wager_struck", "areelu.sacrifice_trickster", "areelu.dead_fight",
                T + "graft_drawn", "areelu.committed" }, true, false, false, Cue0005),
            ("punchline, committed, she lives", punch.Append("areelu.committed").ToArray(), false, false, false, Spared),
            ("punchline, unraised", punch, false, false, false, "areelu.trickster.afterlogue.spared_wager"),
            ("punchline, closed", punch.Append("areelu.closed").ToArray(), false, false, false, Cue0004),
            ("punchline, but she died in the fight", punch.Concat(new[] { "areelu.dead_fight", "areelu.committed" }).ToArray(), true, false, false, Cue0005),
            ("punchline, incinerated", punch.Concat(new[] { "areelu.incinerated", "areelu.committed" }).ToArray(), false, false, false, Cue0004),
            ("punchline, mod disabled", null, false, false, false, Cue0004),
            ("no wager at all", new[] { "trickster.ever", "sacrifice", "ending.trickster", "trickster.commander_back" }, false, false, false, Cue0004),
            ("wound closed by the Commander's sacrifice", common.Concat(new[] { "sacrifice", "ending.wound_closed", "areelu.committed" }).ToArray(),
                true, false, false, Cue0005),
            ("redeemed (another line plays)", rewrite.Append("areelu.committed").ToArray(), true, false, true, "Cue_0003"),
            ("wound sacrifice, persuaded", common.Concat(new[] { "areelu.sacrifice_wound", "areelu.committed" }).ToArray(), true, true, false, "Cue_29"),
        };
        foreach (var row in rows)
        {
            string native = NativeLine(false, false, row.Redeemed, false, row.Dead, row.Wound, row.Wound);
            string plays = native;
            if (row.Flags != null && story.NativeEpilogueEdits.TryGetValue(native, out var edit))
            {
                var state = new Snapshot { Chapter = 6 };
                state.Flags.UnionWith(row.Flags);
                Rules.Complete(story, state);
                var variants = Rules.EditVariants(edit);
                int i = Rules.SelectNativeEditVariant(variants, state);
                if (i >= 0) plays = variants[i].Replacement;
            }
            check(plays == row.Expected, "Trk_Areelu_Afterlogue, " + row.What + ": plays " + plays + ", expected " + row.Expected);
        }
    }
}
