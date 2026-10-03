using System;
using System.Linq;
using Tirabade;

// E14i on non-epilogue dialog cues (engine queue 9a Devarra's DragonEggs/Cue_0007, 8c Kiana's ElandKianaAftermath/Cue_0001):
// the edit's parent is an answer (NextCue) or the dialog itself (FirstCue); the delivery predicate reads the line's scene.
internal static class NativeDialogEditTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        void Rows(string cue, string parent, (string What, string[] Flags, bool Plays)[] rows)
        {
            check(story.NativeEpilogueEdits.TryGetValue(cue, out var edit) && edit.Parent == parent && edit.Page == "", "E14i dialog edit missing or not on its parent: " + cue);
            if (edit == null) return;
            var variants = Rules.EditVariants(edit);
            var scenes = Rules.EditScenes(story, variants);
            foreach (var row in rows)
            {
                var state = new Snapshot { Chapter = 3 };
                state.Flags.UnionWith(row.Flags);
                Rules.Complete(story, state);
                check((Rules.SelectNativeEditVariant(story, variants, scenes, state) == 0) == row.Plays, "E14i dialog edit " + cue + ", " + row.What);
            }
        }
        Rows("164c14743ee768f409a04f93a040e678", "2330b54637738fe4fb92b6cd80eb68f7", new[]
        {
            ("flight (pact struck, she escaped)", new[] { "trickster.ever", "devarra.trickster.flight.pact", "devarra.escaped" }, true),
            ("pact struck, she did not escape", new[] { "trickster.ever", "devarra.trickster.flight.pact" }, false),
            ("escaped without the pact", new[] { "trickster.ever", "devarra.escaped" }, false),
            ("the dragon killed", new[] { "trickster.ever" }, false),
            ("flight, off the Trickster path", new[] { "devarra.trickster.flight.pact", "devarra.escaped" }, false),
        });
        Rows("81109ea8fb20dbc478cf67116740f4a1", "27bc5f6c94108a446b8273800f7da48b", new[]
        {
            ("separated", new[] { "trickster.ever", "kiana.separated" }, true),
            ("separated, off the Trickster path", new[] { "kiana.separated" }, false),
            ("separated, then bereaved", new[] { "trickster.ever", "kiana.separated", "kiana.bereaved" }, false),
            ("married", new[] { "trickster.ever" }, false),
        });
        // 6b: a ransom or buy-back already brought the guests home; native Q3's bowl (Cue_0051) and the aftermath (variant 1) say so.
        void Selects(string cue, (string What, string[] Flags, int Variant)[] rows)
        {
            if (!story.NativeEpilogueEdits.TryGetValue(cue, out var edit)) { check(false, "E14i edit missing: " + cue); return; }
            var variants = Rules.EditVariants(edit);
            var scenes = Rules.EditScenes(story, variants);
            foreach (var row in rows)
            {
                var state = new Snapshot { Chapter = 5 };
                state.Flags.UnionWith(row.Flags);
                Rules.Complete(story, state);
                int selected = Rules.SelectNativeEditVariant(story, variants, scenes, state);
                check(selected == row.Variant, "E14i dialog edit " + cue + ", " + row.What + ": variant " + selected + ", expected " + row.Variant);
            }
        }
        const string Ransomed = "kiana.trickster.guests_ransomed", Bought = "kiana.trickster.guests_bought_back";
        Selects("4255f49c18c69aa4ab4d5582d0b6f39e", new[]
        {
            ("ransomed", new[] { "trickster.ever", Ransomed }, 0),
            ("bought back", new[] { "trickster.ever", "kiana.trickster.cost.guests_robbed", Bought }, 0),
            ("robbed, never bought back", new[] { "trickster.ever", "kiana.trickster.cost.guests_robbed" }, -1),
            ("no device (native Q3 only)", new[] { "trickster.ever" }, -1),
            ("ransomed, off the Trickster path", new[] { Ransomed }, -1),
        });
        Selects("81109ea8fb20dbc478cf67116740f4a1", new[]
        {
            ("ransomed", new[] { "trickster.ever", Ransomed }, 1),
            ("ransomed, then separated", new[] { "trickster.ever", Ransomed, "kiana.separated" }, 0),
            ("bought back", new[] { "trickster.ever", Bought }, 1),
            ("ransomed, off the Trickster path", new[] { Ransomed }, -1),
            ("native Q3 only", new[] { "trickster.ever" }, -1),
        });
        check(story.Scenes.Single(s => s.Id == "kiana.native.q3_bowl_emptied").Nodes[0].Text.Contains("Let's go, {name}!"),
            "The bowl line no longer ends on Seelah's native exit.");
        check(story.Scenes.Single(s => s.Id == "devarra.trickster.native.eggs_flown").Nodes[0].Text.Contains("flew") && 
              !story.Scenes.Single(s => s.Id == "devarra.trickster.native.eggs_flown").Nodes[0].Text.Contains("killed"),
            "The flight egg line still says the dragon was killed.");
    }
}
