using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Earned presence (TRICKSTER-RUBRIC "Binding context (3)", storylines/earned_presence.py, tools/earned_presence_lint.py):
// after an unreturned final sacrifice no epilogue page stages a living Commander, for any route; with each earned return
// (the Trickster punchline, Iomedae's bridge or rescue, Last Call's flask) the living pages show again and the mourning
// pages go quiet. Every world is evaluated by the real Rules.Complete + Rules.Available on the generated story.
internal static class EarnedPresenceTests
{
    private const string Sacrifice = "sacrifice";
    private const string Back = "trickster.commander_back";

    // Each earned return as the native/authored state that produces it (trickster_world.DERIVED trickster.commander_back).
    private static readonly (string Name, string[] Flags)[] Returns =
    {
        ("punchline", new[] { "trickster", "trickster.ever", "ending.trickster" }),
        ("punchline (full)", new[] { "trickster", "trickster.ever", "ending.trickster_full" }),
        ("Iomedae's appointment", new[] { "trickster.ever", "iomedae.appointment_kept" }),
        ("Iomedae's rescue", new[] { "trickster.ever", "iomedae.trickster.rescued" }),
        ("Last Call's flask", new[] { "trickster", "trickster.ever", "trickster.lastcall.taken", "ending.wound_closed", "trickster.lastcall.pillar.bottle" }),
    };

    private static readonly string[] Witnesses = { Back, "trickster.cheated_death", "lastcall.active", "lastcall.h1", "lastcall.h2",
        "lastcall.dead_on_record", "iomedae.appointment_kept", "iomedae.trickster.rescued", "iomedae.trickster.buried_alive" };

    private static Snapshot World(Story story, Scene scene, IEnumerable<string> extra, bool sacrifice)
    {
        var state = new Snapshot { Chapter = Math.Min(Math.Max(6, scene.MinChapter), scene.MaxChapter), Hour = 100000 };
        // fix-inherited2: the accepted Soana fixture must earn a real partner stance.
        // The non-Trickster fallback stops holding when a Trickster return is added;
        // a coarse commitment is not an agreement with Soana about Corven.
        if (scene.Relationship == "soana" && scene.Requires.Any(k => k == "soana.round2.current_love"
                || k == "soana.round2.current_courtship" || k == "soana.round2.postwar_ready"))
            state.Flags.UnionWith(new[] { "soana.partner_stance.secret", "soana.partner.agreed" });
        foreach (var flag in scene.Requires.Where(requiredKey => !requiredKey.EndsWith(".present_now", StringComparison.Ordinal) && !requiredKey.EndsWith(".reachable_by_letter", StringComparison.Ordinal)))
        {
            HouseholdTests.Earn(story, state, flag);
            Rules.Complete(story, state); // preserve the already earned late branch when a partner predicate follows
        }
        foreach (var group in scene.RequiresAnyGroups) HouseholdTests.Earn(story, state, group[0]);
        foreach (var flag in extra) HouseholdTests.Earn(story, state, flag);
        if (sacrifice) state.Flags.Add(Sacrifice);
        else state.Flags.Remove(Sacrifice);
        Rules.Complete(story, state);
        return state;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        int living = 0, restored = 0, mourning = 0, bare = 0;
        var leaks = new List<string>();
        foreach (var scene in story.Scenes.Where(s => s.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && s.Owner != "AeonEpilogue"))
        {
            if (scene.Requires.Any(Witnesses.Contains)) continue;   // plays only beside a Commander who came back
            // Requires "sacrifice", or a composite that holds only with it (Areelu's commander_burned).
            bool mourns = scene.Requires.Any(k => k == Sacrifice
                || story.Derived.TryGetValue(k, out var groups) && groups.All(g => g.Contains(Sacrifice)));
            if (mourns)
            {
                // A mourning page plays only while the Commander stays dead.
                var dead = World(story, scene, Array.Empty<string>(), true);
                if (dead.Has(Back) || !Program.CurrentAvailable(story, scene, dead)) continue;
                mourning++;
                foreach (var (name, flags) in Returns)
                {
                    var back = World(story, scene, flags, true);
                    check(back.Has(Back), "Earned return '" + name + "' does not produce " + Back);
                    check(!Program.CurrentAvailable(story, scene, back), "Mourning page " + scene.Id + " plays beside a Commander who came back (" + name + ").");
                }
                continue;
            }
            if (!scene.Forbids.Contains(Sacrifice)) continue;   // COMMANDER_ABSENT: never stages the Commander alive
            var alive = World(story, scene, Array.Empty<string>(), false);
            if (!Program.CurrentAvailable(story, scene, alive)) continue;    // unavailable for reasons of its own
            var unreturned = World(story, scene, Array.Empty<string>(), true);
            if (unreturned.Has(Back)) continue;
            living++;
            if (Program.CurrentAvailable(story, scene, unreturned)) leaks.Add(scene.Id + " [" + scene.Relationship + "]");
            // A bare Forbid "sacrifice" (legacy native-path pages such as the trio's) never returns; only the commander_dead
            // guard (Forbid + override trickster.commander_back) is lifted by an earned return.
            if (!scene.ForbidOverrides.TryGetValue(Sacrifice, out var lift) || lift != Back) { bare++; continue; }
            foreach (var (name, flags) in Returns)
            {
                var back = World(story, scene, flags, true);
                // A page may legitimately refuse one return world (Areelu's finale forbids Iomedae's appointment).
                if (scene.Forbids.Any(f => f != Sacrifice && Rules.ForbidHolds(scene, f, back) && !Rules.ForbidHolds(scene, f, alive))) continue;
                check(Program.CurrentAvailable(story, scene, back), "Living page " + scene.Id + " does not return with the Commander (" + name + ").");
                restored++;
            }
        }
        check(leaks.Count == 0, "Living postwar pages after an unreturned sacrifice: " + string.Join(", ", leaks));
        check(living > 300, "Too few living postwar pages exercised (" + living + "); the fixture worlds are not reaching them.");
        Console.WriteLine($"earned presence: {living} living pages dark after an unreturned sacrifice ({bare} with a bare forbid), "
            + $"{restored} return worlds restored, {mourning} mourning pages quiet after every return.");
        check(restored > (living - bare) * 3, "Too few earned-return worlds restored a living page (" + restored + " for " + living + " pages).");
        check(mourning >= 40, "Too few mourning pages exercised (" + mourning + ").");

        // fix-inherited2: every return restores an accepted Soana history, while
        // the return itself earns neither her partner stance nor renewed love.
        var soana = story.Scenes.Single(s => s.Id == "soana.ending_kept_life");
        foreach (var (name, flags) in Returns)
        {
            var accepted = World(story, soana, flags, true);
            check(accepted.Has("soana.partner_stance.secret") && accepted.Has("soana.partner.agreed")
                  && Program.CurrentAvailable(story, soana, accepted), "Soana's accepted history is lost after " + name + ".");
            var unagreed = Program.Copy(accepted);
            unagreed.Flags.Remove("soana.partner_stance.secret");
            unagreed.Flags.Remove("soana.partner.agreed");
            unagreed.Flags.Add("trickster"); // exercise the current-path stance gate even in an Iomedae fixture
            Rules.Complete(story, unagreed);
            check(!Program.CurrentAvailable(story, soana, unagreed), "The Commander return invents Soana's partner agreement: " + name + ".");
        }

        // The audited case (Seelah, GrandFinal Answer_0017): no "Now we're even" and no fireside after the Commander died.
        foreach (var id in new[] { "seelah.trickster.epilogue.commit", "seelah.ending_together" })
        {
            var scene = story.Scenes.Single(s => s.Id == id);
            check(!Program.CurrentAvailable(story, scene, World(story, scene, Array.Empty<string>(), true)), id + " plays after an unreturned sacrifice.");
            check(Program.CurrentAvailable(story, scene, World(story, scene, Returns[0].Flags, true)), id + " is lost after the punchline return.");
        }
        foreach (var id in new[] { "seelah.ending_sacrifice", "kiana.ending_sacrifice", "jerribeth.ending_sacrifice", "devarra.trickster.epilogue.sacrifice" })
        {
            var scene = story.Scenes.Single(s => s.Id == id);
            check(Program.CurrentAvailable(story, scene, World(story, scene, new[] { "trickster.ever" }, true)), id + " (mourning) does not play after an unreturned sacrifice.");
        }

        // E14d native-slide replacements: a replacement that stages a living Commander yields to the native slide.
        foreach (var pair in story.NativeEpilogueEdits)
        {
            var variants = Rules.EditVariants(pair.Value);
            for (int v = 0; v < variants.Length; v++)
            {
                var scene = story.Scenes.Single(s => s.Id == variants[v].Replacement);
                var state = new Snapshot { Chapter = 6, Hour = 100000 };
                foreach (var flag in variants[v].When[0]) HouseholdTests.Earn(story, state, flag);
                state.Flags.Add("trickster.ever");
                state.Flags.Add(Sacrifice);
                Rules.Complete(story, state);
                int selected = Rules.SelectNativeEditVariant(story, variants, state);
                if (selected >= 0)
                {
                    var chosen = story.Scenes.Single(s => s.Id == variants[selected].Replacement);
                    check(!chosen.Forbids.Contains(Sacrifice) || state.Has(Back),
                        "Native edit " + pair.Key + " shows " + chosen.Id + " beside a dead Commander.");
                }
                foreach (var flag in Returns[0].Flags) HouseholdTests.Earn(story, state, flag);
                Rules.Complete(story, state);
                check(Rules.SelectNativeEditVariant(story, variants, state) == Rules.SelectNativeEditVariant(variants, state),
                    "Native edit " + pair.Key + " variant " + v + " is not restored by the punchline return.");
            }
        }
    }
}
