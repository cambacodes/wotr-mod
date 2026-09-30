using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// 18-ETUDE-BINDING-AUDIT: every fixed native binding is held where and when its scenes are delivered. The native world is
// simulated the way Main.BuildState reads it: Story.Etudes through Rules.EtudeHeld (Playing, or Completed for permanent
// keys), SeenCues from dialog history, Latches recorded while their source was observed (Main.RecordLatches), then
// Rules.Complete. The broken reads are asserted too, so the fix cannot silently regress.
internal static class EtudeBindingTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Iz = "2ccc6731787b6ec41ab5adc13f1b9ce9";

    private sealed class Native
    {
        public readonly Dictionary<string, (bool Playing, bool Completed)> Etudes = new Dictionary<string, (bool, bool)>();
        public readonly HashSet<string> Cues = new HashSet<string>();
        public readonly HashSet<string> Recorded = new HashSet<string>();
    }

    // Main.BuildState over a simulated native world (only the readers these tests need).
    private static Snapshot Read(Story story, Native world, int chapter, string area, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = area };
        foreach (var pair in story.Etudes)
            if (world.Etudes.TryGetValue(pair.Key, out var fact) && Rules.EtudeHeld(story, pair.Key, fact.Playing, fact.Completed))
                state.Flags.Add(pair.Key);
        foreach (var pair in story.SeenCues)
            if (pair.Value.Any(world.Cues.Contains)) state.Flags.Add(pair.Key);
        state.Flags.UnionWith(world.Recorded);
        state.Flags.UnionWith(flags);
        state.Flags.Add(Rules.ChapterFlag(chapter)!);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    // Main.RecordLatches: persist every latch the (idle) snapshot observes.
    private static void Record(Story story, Native world, Snapshot observed)
    {
        foreach (var key in story.Latches.Keys.Where(observed.Has)) world.Recorded.Add(key);
    }

    private static bool ChoiceOpen(Scene scene, string node, Func<Choice, bool> which, Snapshot state) =>
        scene.Nodes.Single(n => n.Id == node).Choices.Where(which).Any(c => c.Requires.All(state.Has) && !c.Forbids.Any(state.Has));

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        string Cue(string key, int i = 0) => story.SeenCues[key][i];

        // hepzamirah.dead: ColyphyrHepzamirahDead plays only inside Colyphyr, and the c4->c5 interchapter completes Chapter04,
        // cascading Completed onto it. Chapter 5, outside Colyphyr: Playing false, Completed true.
        check(story.Etudes.ContainsKey("hepzamirah.dead") && Rules.EtudeReadsCompleted(story, "hepzamirah.dead"),
            "Etude_Hepzamirah: hepzamirah.dead is not a permanent etude read.");
        var killed = new Native();
        killed.Etudes["hepzamirah.dead"] = (false, true);
        var ch5 = Read(story, killed, 5, "", "trickster", "trickster.ever", "baphomet.parley.latched");
        check(ch5.Has("hepzamirah.dead") && Rules.Available(story, S("hepzamirah.trickster.ghost.deed_by_fire"), ch5),
            "Etude_Hepzamirah: in Chapter 5 the cascaded death does not hold, or the ghost's remote device stays shut.");
        var spared = Read(story, new Native(), 5, "", "trickster", "trickster.ever", "baphomet.parley.latched");
        check(!spared.Has("hepzamirah.dead") && !Rules.Available(story, S("hepzamirah.trickster.ghost.deed_by_fire"), spared),
            "Etude_Hepzamirah: the ghost device opens for a Hepzamirah who never died.");

        // arueshalae.failed: the romance-ending cues (dialog history), not the one-strike warning etude.
        check(!story.Etudes.ContainsKey("arueshalae.failed") && story.SeenCues["arueshalae.failed"].Length == 8,
            "Etude_Arueshalae: arueshalae.failed is not bound to the failure cues.");
        var failed = new Native();
        failed.Cues.Add(Cue("arueshalae.failed", 0));   // After_Wintersun Cue_0023: the second strike
        foreach (var chapter in new[] { 3, 5 })
        {
            var state = Read(story, failed, chapter, Drezen, "trickster", "trickster.ever");
            state.AvailableContacts.Add(S("arueshalae.trickster.failed.chaplain").ContactUnit!);
            check(state.Has("arueshalae.failed") && Rules.Available(story, S("arueshalae.trickster.failed.chaplain"), state),
                "Etude_Arueshalae: the chaplain device is shut after a failed romance in Chapter " + chapter + ".");
        }
        var warned = new Native();
        warned.Etudes["arueshalae.failed"] = (true, false);   // the warning etude playing: no longer a binding at all
        check(!Read(story, warned, 3, Drezen, "trickster", "trickster.ever").Has("arueshalae.failed"),
            "Etude_Arueshalae: a one-strike warning still reads as a failed romance.");

        // Iz: MonsterDead, DidntVisitedEvents and ManuscriptsAnemoraDead play only in Iz (area link, never completed). Observed
        // there and latched; read in Chapter 5 far from Iz (remote letters) and in the Drezen capital (Kaylessa).
        var iz = new Native();
        foreach (var key in new[] { "iz.monster_dead.live", "iz.left_early.live", "iz.anemora_dead.live" }) iz.Etudes[key] = (true, false);
        var inIz = Read(story, iz, 5, Iz);
        check(new[] { "iz.monster_dead.latched", "iz.left_early", "iz.anemora_dead" }.All(inIz.Has),
            "Etude_Iz: the Iz events are not latched while the party is in Iz.");
        Record(story, iz, inIz);
        foreach (var key in iz.Etudes.Keys.ToList()) iz.Etudes[key] = (false, false);   // dormant: the party has left Iz
        var late = S("terendelev.trickster.late.the_wound_calls");
        var away = Read(story, iz, 5, "", "trickster");
        check(away.Has("iz.monster_dead") && away.Has("iz.left_early") && Rules.Available(story, late, away)
              && ChoiceOpen(late, "start", c => c.Requires.Contains("iz.left_early"), away),
            "Etude_Iz: Terendelev's late letter, or its left-early branch, is shut in Chapter 5 away from Iz.");
        var order = S("irabeth.trickster.dead.late_order");
        check(ChoiceOpen(order, "start", c => c.Requires.Contains("iz.left_early"), away)
              && !ChoiceOpen(order, "start", c => c.Requires.Length == 0 && c.Forbids.Contains("iz.left_early"), away),
            "Etude_Iz: Irabeth's late order ignores that the Commander left Iz early.");
        var capital = Read(story, iz, 5, Drezen, "trickster.ever", "kaylessa.trickster.after.rules");
        capital.AvailableContacts.Add(S("kaylessa.wasps.anemora").ContactUnit!);
        check(Rules.Available(story, S("kaylessa.wasps.anemora"), capital)
              && ChoiceOpen(S("kaylessa.wasps.anemora"), "start", c => c.Requires.Contains("iz.anemora_dead"), capital),
            "Etude_Iz: Kaylessa's Anemora-dead branch is shut in the capital.");
        var never = new Native();
        check(!Rules.Available(story, late, Read(story, never, 5, "", "trickster")), "Etude_Iz: the late letter opens without the monster's death.");

        // Jannah: her fate etudes sit under SeelahInParty and go dormant with Seelah dead or dismissed; the Deserter cues do not.
        var jannahDead = new Native();
        jannahDead.Cues.Add(Cue("jannah.dead"));
        var seelahDead = Read(story, jannahDead, 5, "", "trickster", "seelah_dead", "coronation.seen");
        check(seelahDead.Has("jannah.dead") && !Rules.Available(story, S("jannah.trickster.alive.letter"), seelahDead),
            "Etude_Jannah: with Seelah dead, a dead Jannah reads alive and her 'alive' letter opens.");
        var jannahAlive = new Native();
        jannahAlive.Cues.Add(Cue("jannah.prison"));
        var alive = Read(story, jannahAlive, 5, "", "trickster", "seelah_dead", "coronation.seen");
        check(Rules.Available(story, S("jannah.trickster.alive.letter"), alive)
              && ChoiceOpen(S("jannah.trickster.alive.letter"), "open", c => c.Requires.Contains("jannah.prison"), alive),
            "Etude_Jannah: the imprisoned Jannah's letter, or its prison branch, is shut with Seelah dead.");
        // Condemned: JannaInCondemned plays only in the capital (Seelah in party); latched there, read by the remote letter.
        var condemned = new Native();
        condemned.Cues.Add(Cue("jannah.prison"));
        condemned.Etudes["jannah.condemned.live"] = (true, false);
        Record(story, condemned, Read(story, condemned, 5, Drezen));
        condemned.Etudes["jannah.condemned.live"] = (false, false);
        var field = Read(story, condemned, 5, "", "trickster", "coronation.seen");
        check(field.Has("jannah.condemned") && ChoiceOpen(S("jannah.trickster.alive.letter"), "open", c => c.Requires.Contains("jannah.condemned"), field),
            "Etude_Jannah: the condemned branch of the remote letter is shut outside the capital.");

        // Soana: the bear's death plays only in WintersunOutdoor; latched there, read by her remote knot letter.
        var bear = new Native();
        bear.Etudes["soana.bear_dead.live"] = (true, false);
        Record(story, bear, Read(story, bear, 3, "0a5654e7dc18f074d9356009d55eb51b"));
        bear.Etudes["soana.bear_dead.live"] = (false, false);
        var knot = Read(story, bear, 3, "", "trickster", "trickster.ever", "soana.dead");
        check(knot.Has("soana.bear_dead") && Rules.Available(story, S("soana.trickster.killed.knot"), knot)
              && ChoiceOpen(S("soana.trickster.killed.knot"), "start", c => c.Requires.Contains("soana.bear_dead"), knot),
            "Etude_Soana: the knot letter's bear branch is shut away from Wintersun.");
    }
}
