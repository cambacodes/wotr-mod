using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E14d: Camellia's native departure slides (Epilogues/BookPage_0347) once the Trickster route keeps her. The native
// conditions are modelled from blueprints.zip (the managed suite runs the archive's own checkers); the RRT side is the
// shipped Story: edits select by Rules.SelectNativeEditVariant, suppressions hide by Rules.WhenHolds.
internal static class CamelliaNativeSlideTests
{
    private const string Cue0392 = "84f892d388bba01489145ecd631f23a2", Cue0544 = "c1b1da84c12d3ac448ec65b4342ce77f",
        Cue28 = "4ed8e9723359441dae10ad3068d3f2c7", Cue38 = "36a07840d25540eeac6b1c6631196bcc", Cue0386 = "5011dfa46fbb0464ab624d78bcfbd483",
        Cue16 = "3617a648c06a45d1807fde65aedafb06", Cue0391 = "430ce9767d3ede2479ff9d6aee432304", Cue0390 = "e9a183135b8289544a3144dcf8151920";
    private static readonly string[] PageOrder = { Cue0392, Cue0544, Cue28, Cue38, Cue0386, Cue16, Cue0391, Cue0390 };
    private static readonly string[] Leads = { Cue0392, Cue0544, Cue28, Cue38, Cue0386 };
    private const string P = "camellia.trickster.";
    private const string CamelliaPage = "503164ff04ac64543ba42561ea9f970f";   // Epilogues/BookPage_0347

    // The archive's checkers (BookPage_0347): TE = Cue_0102/Cue_0105 seen; romance = CamRomDefault or CamRomTrue Playing.
    private static bool NativeShows(string cue, bool te, bool q3, bool romDefault, bool romTrue, bool sacrifice)
    {
        bool romance = romDefault || romTrue;
        switch (cue)
        {
            case Cue0392: return te && q3;
            case Cue0544: return te && !q3;
            case Cue28: return !te && romance && !sacrifice;
            case Cue38: return !te && romance && sacrifice;
            case Cue0386: return !te && !romance;
            case Cue16: return !te;
            case Cue0391: return !sacrifice && romTrue;
            case Cue0390: return !te && (romDefault && !sacrifice || romance && sacrifice);
            default: throw new ArgumentException(cue);
        }
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        var edited = new[] { Cue0392, Cue0544, Cue28, Cue38, Cue0386 };
        var hidden = new[] { Cue16, Cue0390, Cue0391 };
        check(edited.All(story.NativeEpilogueEdits.ContainsKey) && hidden.All(story.NativeEpilogueSuppressions.ContainsKey),
            "Trk_Camellia_NativeSlides: the lead slides are not all replaced, or the follow-ons not all hidden.");
        if (!edited.All(story.NativeEpilogueEdits.ContainsKey) || !hidden.All(story.NativeEpilogueSuppressions.ContainsKey)) return;
        // The reviewed evidence (warning-only, Cue_0386's continuation) is NativeEpilogueEdit.Reviewed, checked by the managed suite.
        foreach (var cue in edited.Concat(hidden))
        {
            var page = story.NativeEpilogueEdits.TryGetValue(cue, out var e) ? e.Page : story.NativeEpilogueSuppressions[cue].Page;
            check(page == CamelliaPage, "Trk_Camellia_NativeSlides: not on BookPage_0347: " + cue);
        }
        check(story.NativeEpilogueEdits.Where(p => p.Value.Page == CamelliaPage).All(p => Rules.EditVariants(p.Value).Length == 1
                && story.Scenes.Single(s => s.Id == p.Value.Replacement).Relationship == "camellia"),
            "Trk_Camellia_NativeSlides: a Camellia slide has variants, or another relationship's text.");
        check(story.NativeEpilogueEdits[Cue0392].KeepNativeImage && !story.NativeEpilogueEdits[Cue0544].KeepNativeImage,
            "Trk_Camellia_NativeSlides: the semidivine slide must keep its native picture (she still has the power).");

        // Every RRT world: kept, terms named, closed after either, declined, returned only, never returned, the mod's flags
        // with a dead Commander (sacrifice, not back) or a returned one, a dismissal (kicked_out without the kill).
        var worlds = new (string What, string[] Flags, string Kind)[]
        {
            ("never returned", new[] { "trickster.ever" }, "native"),
            ("living committed", new[] { "trickster.ever", "camellia.committed" }, "kept"),
            ("actual second death without return", new[] { "trickster.ever", "camellia.committed", "camellia.dead" }, "native"),
            ("living terms", new[] { "trickster.ever", P + "terms_named" }, "terms"),
            ("returned only", new[] { "trickster.ever", P + "returned" }, "native"),
            ("returned, declined", new[] { "trickster.ever", P + "returned", P + "declined" }, "native"),
            ("kept", new[] { "trickster.ever", P + "returned", "camellia.committed" }, "kept"),
            ("kept, killed (kicked_out is the kill)", new[] { "trickster.ever", P + "returned", "camellia.committed", "camellia.killed",
                "camellia.kicked_out", P + "killed_held", P + "cost.knows_you_tried" }, "kept"),
            ("kept, then dismissed", new[] { "trickster.ever", P + "returned", "camellia.committed", "camellia.kicked_out" }, "native"),
            ("kept, then closed", new[] { "trickster.ever", P + "returned", "camellia.committed", "camellia.closed" }, "native"),
            ("terms named", new[] { "trickster.ever", P + "returned", P + "terms_named" }, "terms"),
            ("terms named, declined", new[] { "trickster.ever", P + "returned", P + "terms_named", P + "declined" }, "native"),
            ("terms named, closed", new[] { "trickster.ever", P + "returned", P + "terms_named", "camellia.closed" }, "native"),
            ("terms named and committed", new[] { "trickster.ever", P + "returned", P + "terms_named", "camellia.committed" }, "kept"),
        };
        var bools = new[] { false, true };
        foreach (var world in worlds)
            foreach (bool sacrifice in bools)
                foreach (bool back in bools)
                    foreach (bool te in bools)
                        foreach (bool q3 in bools)
                            foreach (var (romDefault, romTrue) in new[] { (false, false), (true, false), (false, true), (true, true) })
                            {
                                if (back && !sacrifice) continue;
                                var state = new Snapshot { Chapter = 6 };
                                state.Flags.UnionWith(world.Flags);
                                state.Flags.Add("trickster");
                                if (sacrifice) state.Flags.Add("sacrifice");
                                if (back) state.Flags.Add("trickster.commander_back");
                                Rules.Complete(story, state);
                                string kind = world.Kind != "native" && sacrifice && !back ? "native" : world.Kind;
                                string what = $"{world.What}, sacrifice={sacrifice}, back={back}, TE={te}, Q3={q3}, rom={romDefault}/{romTrue}";
                                var shown = new List<string>();
                                foreach (var cue in PageOrder)
                                {
                                    if (!NativeShows(cue, te, q3, romDefault, romTrue, sacrifice)) continue;
                                    if (story.NativeEpilogueEdits.TryGetValue(cue, out var edit))
                                    {
                                        var variants = Rules.EditVariants(edit);
                                        int i = Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), state);
                                        shown.Add(i < 0 ? cue : variants[i].Replacement);
                                    }
                                    else if (!Rules.WhenHolds(story.NativeEpilogueSuppressions[cue].When, state)) shown.Add(cue);
                                }
                                check(shown.Count(id => Leads.Contains(id) || id.StartsWith(P + "epilogue.native_", StringComparison.Ordinal)) == 1,
                                    "Trk_Camellia_NativeSlides: the page must open with exactly one lead slide: " + what + " -> " + string.Join(", ", shown));
                                var native = PageOrder.Where(cue => NativeShows(cue, te, q3, romDefault, romTrue, sacrifice)).ToArray();
                                if (kind == "native")
                                    check(shown.SequenceEqual(native), "Trk_Camellia_NativeSlides: a native slide changed outside the kept or terms state: " + what);
                                else if (kind == "kept")
                                    check(shown.Count == 1 && shown[0].StartsWith(P + "epilogue.native_", StringComparison.Ordinal),
                                        "Trk_Camellia_NativeSlides: a kept Camellia still vanishes, leaves or goes to Varisia: " + what + " -> " + string.Join(", ", shown));
                                else
                                    check(shown.SequenceEqual(native.Where(cue => cue != Cue0391)),
                                        "Trk_Camellia_NativeSlides: with her terms named only 'she left again' (Cue_0391) is hidden: " + what);
                            }
        // The kept lead names the state it replaces: Cue_38_master keeps the ruins of Threshold, the semidivine slide the power.
        string Text(string cue) => story.Scenes.Single(s => s.Id == story.NativeEpilogueEdits[cue].Replacement).Nodes[0].Text;
        check(Text(Cue38).Contains("Threshold") && Text(Cue0392).Contains("semidivine") && Text(Cue0544).Contains("semidivine"),
            "Trk_Camellia_NativeSlides: a replacement lost the native state it stands in for.");
        check(edited.All(cue => !Text(cue).Contains("vanished") && !Text(cue).Contains("Varisia")),
            "Trk_Camellia_NativeSlides: a kept slide still says she vanished or went to Varisia.");
    }
}
