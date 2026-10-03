using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Devarra, Trickster (Writer/handoffs/trickster/devarra.md; device redesign Option A, "She flies",
// Writer/handoffs/trickster/devarra-device-options.md). Nobody dies and nothing is raised: in her lair she buys the
// Commander's plan under her own tariff, flies at the turn (the native escape), and does not answer the golems' call; a
// reviewed native gate (E18) gives the Ivory Sanctum its own absent-dragon branches; the Commander lowers the golems' fists
// with their own password. The lair-kill, no-hunt and unprepared-escape worlds keep canon fate (coordinator ruling,
// 2026-10-01). The moult device is retired by gating; its scenes stay registered for save safety.
internal static class DevarraTricksterTests
{
    private const string P = "devarra.trickster.";
    private const string T = "devarra.tower.";
    private const string StHub = "2f5b7e0b76d3c5a42a431e1e33a8db09";
    private const string StReturn = "34a0d078b4ac51547a8f5e0e1c8e1e2c";
    private const string Spawn = "ivory_sanctum.red_dragon_spawn";
    private const string OverBody = "golems_dragon_eggs.over_body";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, int? chapter = null)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        if (chapter != null) later.Chapter = chapter.Value;
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var retired = new[] { "dead.lair_story", "dead.setup", "dead.storytellers_version", "dead.woken" }.Select(id => S(P + id)).ToArray();
        var pact = S(P + "flight.pact");
        var leash = S(P + "flight.leash");
        var left = S(P + "flight.clutch_left");
        var eggs = S(P + "flight.eggs");
        var tithe = S(P + "after.tithe");
        var lair = S(P + "after.lair");
        var firstClimb = S(T + "first_climb");
        var firstBite = S(T + "first_bite");
        var backUp = S(T + "back_up_the_mountain");
        var pages = story.Scenes.Where(s => s.Relationship == "devarra" && s.Owner == "DevarraEpilogue" && !Rules.IsNativeReplacement(story, s)).ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "devarra" && s.Reaction).ToArray();
        var own = story.Scenes.Where(s => s.Relationship == "devarra" && !s.Reaction && s.Owner == "Devarra").ToArray();
        var tower = own.Where(s => s.Id.StartsWith(T, StringComparison.Ordinal)).ToArray();
        Choice Choice(Scene scene, string node, int index) => scene.Nodes.Single(n => n.Id == node).Choices[index];
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            var hits = Program.WalkVia(scene, w, node, index);
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        // Plays every available Devarra scene forward and reports whether a flag is ever held.
        bool Reaches(Snapshot start, string flag, int chapter = 5)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 14 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    if (from.Has(flag)) return true;
                    var w = Later(story, from, 200, chapter);
                    foreach (var scene in own.Where(s => Rules.Available(story, s, w)))
                        foreach (var r in Program.Walk(scene, w))
                        {
                            if (r.Has(flag)) return true;
                            if (seen.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                        }
                }
                frontier = next;
            }
            return false;
        }
        bool AnyOpen(Snapshot w) => story.Scenes.Where(s => s.Relationship == "devarra" && s.Owner != "DevarraEpilogue")
            .Any(s => Rules.Available(story, s, Later(story, w, 200)));

        // Shape and hooks.
        var rel = story.Relationships["devarra"];
        check(rel.StartedFlag == "devarra.started" && rel.ClosedFlag == "devarra.closed" && rel.CommittedFlag == "devarra.committed"
              && rel.UnavailableFlags.OrderBy(f => f).SequenceEqual(new[] { "devarra.dead_lair", "devarra.dead_sanctum", "inhuman" }),
            "Devarra's relationship does not match the spec.");
        foreach (var s in retired)
        {
            check(s.Forbids.Contains("trickster.ever"), "A moult device scene is not retired by gating: " + s.Id);
            check(!Rules.Available(story, s, World(story, 3, "trickster", "trickster.ever", "devarra.lair_story_heard", "devarra.golems_over_body",
                "devarra.dead_sanctum", P + "primed")), "A retired moult device scene still opens: " + s.Id);
        }
        check(pact.AnswerLists.SequenceEqual(new[] { "c8298f1630fd82046986d313ba35f601" }) && pact.NativeReturnCue == "26650f05010b9ce4cb0202da7e35ce8e"
              && Choice(pact, "terms", 0).NativeNext == "3d5e59ddc658eb947874a1cac31dd6a4" && Choice(pact, "terms", 0).Mythic == "PlayerIsTrickster"
              && Choice(pact, "terms", 0).Alignment?.Direction == "Chaotic" && Choice(pact, "terms", 0).Set.SequenceEqual(new[] { P + "flight.pact" }),
            "The pact is not the Trickster answer on her lair list, before the native fight (Cue_0012).");
        check(leash.ReturnToList && leash.AnswerLists.SequenceEqual(new[] { "04d72f75c1e841747a55b780fccf37fe", "d1f609c764422a24994568d850c99958",
              "ab4a075bbc5d24048bf892697e75f2e3" }), "The leash is not on the golems' master lists (after the native password).");
        check(left.ReturnToList && left.AnswerLists.SequenceEqual(new[] { "b265afc1afe5a4241b1d5d42a4148e75" }), "The clutch is not left on the native egg list.");
        // PP7: the Chapter 4 memory (wrong_sky) is the one tower beat not on his hub: she is on her ridge, the Commander in the Abyss.
        foreach (var s in new[] { tithe }.Concat(tower.Where(t => t.Id != T + "wrong_sky")))
            check(s.AnswerLists.SequenceEqual(new[] { StHub }) && s.NativeReturnCue == StReturn && s.ContactUnit == null
                  && !Rules.IsRemote(s) && s.Forbids.Contains("storyteller.dead"),
                "A Devarra beat is not on the Storyteller's hub, guarded by his death: " + s.Id);
        foreach (var s in tower)
            check(s.Forbids.Contains("devarra.closed"), "A watchtower beat plays after her hard no: " + s.Id);
        var letters = story.Scenes.Where(s => s.Relationship == "devarra" && Rules.IsRemote(s) && s.Owner != "DevarraEpilogue" && !retired.Contains(s)
            && s.Kind != "memory").ToArray();   // PP7: the Chapter 4 memory is no letter (shape checked below)
        check(letters.Select(s => s.Id).OrderBy(i => i).SequenceEqual(new[] { P + "after.lair", P + "flight.eggs" })
              && letters.All(s => s.Chapters.SequenceEqual(new[] { 3, 5 })),
            "Devarra's letters are not exactly the return and the commit, in Chapters 3 and 5.");
        check(eggs.Nodes.SelectMany(n => n.Choices).All(c => !c.Set.Contains("devarra.committed")), "The return commits.");
        check(Choice(tithe, "tithe_free", 0).Crusade?.Resource == "Materials" && Choice(tithe, "tithe_free", 0).Crusade!.Amount == -100
              && Choice(tithe, "tithe_free", 0).Alignment?.Direction == "Evil" && Choice(tithe, "tithe_free", 1).Crusade?.Amount == -200
              && Choice(tithe, "tithe_free", 2).Set.Contains("devarra.closed"),
            "The tithe's hunger is not priced, or presuming to own her is not her hard no.");
        check(reactions.Length == 5 && reactions.All(r => r.Nodes.Count == 1 && r.Requires.Contains(P + "returned"))
              && reactions.Where(r => r.Owner == "Greybor").All(r => r.Forbids.Contains("greybor.dead") && r.Forbids.Contains("greybor.kicked_out"))
              && reactions.Where(r => r.Owner == "Storyteller").All(r => r.Forbids.Contains("storyteller.dead"))
              && reactions.Select(r => r.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Greybor", "Storyteller" })
              && reactions.All(r => r.Requires.Contains(P + "flown") ^ r.Forbids.Contains(P + "flown")),
            "The reactions are not exactly Greybor and the Storyteller, split cleanly between the flight and the legacy worlds.");
        check(pages.Length == 5 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null))),
            "The epilogue pages carry effects or are missing.");
        check(story.Derived[P + "late_committed"].Single().SequenceEqual(new[] { "trickster.ever", P + "tested" }),
            "The late commit is not derived from the tested story.");
        // Every watchtower gate is produced somewhere in the route.
        var produced = new HashSet<string>(story.Scenes.Where(s => s.Relationship == "devarra").SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set));
        foreach (var s in own)
            foreach (var key in s.Requires.Where(k => k.StartsWith(T, StringComparison.Ordinal)))
                check(produced.Contains(key), "A watchtower gate has no producer: " + s.Id + " requires " + key);
        foreach (var s in story.Scenes.Where(s => s.Relationship == "devarra"))
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)))
                check(!(key.EndsWith(".closed", StringComparison.Ordinal) && key != "devarra.closed")
                      && !(key.EndsWith("_dead", StringComparison.Ordinal) || key.EndsWith(".dead", StringComparison.Ordinal))
                      || key == "storyteller.dead",
                    "Devarra needs someone else dead or closed: " + s.Id + " " + key);

        // Trk_Devarra_Pact: her tariff, paid from cover, before the fight.
        var lairWorld = World(story, 3, "trickster", "trickster.ever", "devarra.lair_story_heard");
        check(Rules.Available(story, pact, lairWorld), "Trk_Devarra_Pact: the pact is shut in her lair.");
        var pacted = After(pact, lairWorld, "terms", 0).First();
        check(pacted.Has(P + "flight.pact") && !pacted.Has(P + "flown"), "Trk_Devarra_Pact: the pact alone counts as her flight.");
        check(!Rules.Available(story, pact, World(story, 3, "trickster", "devarra.dead_lair")) && !Rules.Available(story, pact, World(story, 3, "trickster", "devarra.escaped")),
            "The pact opens after she died or flew.");
        check(!Rules.Available(story, pact, World(story, 3, "trickster.ever", "trickster.failed")), "The pact opens off the Trickster path.");

        // Trk_Devarra_Escape: the native escape after the pact is her flight, and it gates the Sanctum.
        var flown = World(story, 3, "trickster", "trickster.ever", P + "flight.pact", "devarra.escaped");
        check(flown.Has(P + "flown"), "Trk_Devarra_Escape: the pact and the native escape are not her flight.");
        var flownLatched = World(story, 3, "trickster", "trickster.ever", P + "flight.pact", "devarra.escaped.latched");
        check(flownLatched.Has(P + "flown"), "Trk_Devarra_Escape: the flight is lost when RedDragonEscaped stops playing.");
        check(story.Latches["devarra.escaped.latched"].SequenceEqual(new[] { "devarra.escaped" }), "The escape is not latched.");

        // Trk_Devarra_SpawnGate: the E18 gates hold in her flight world only.
        var devarraGates = story.NativeGates.Where(g => g.Value.Relationship == "devarra" && g.Key != "dragon_eggs.dialog")   // other routes gate too (Kiana)
            .ToDictionary(g => g.Key, g => g.Value);   // the egg dialog gate (engine queue 9c) is checked in NativeGateManagedTests.RunDevarra
        check(devarraGates.Keys.OrderBy(k => k).SequenceEqual(new[] { OverBody, Spawn })
              && devarraGates[Spawn].Target == "977818b761d048d49a0fe19a1c8fccc4" && devarraGates[OverBody].Target == "b8dfb42d03fc931409f2b80614cfa9de",
            "Trk_Devarra_SpawnGate: the reviewed gates are not the Sanctum spawn and the golems' carcass cue.");
        check(Rules.NativeGateHolds(story, Spawn, flown) && Rules.NativeGateHolds(story, OverBody, flown) && Rules.NativeGateHolds(story, Spawn, flownLatched),
            "Trk_Devarra_SpawnGate: the Sanctum still spawns her after she flew on the pact.");
        foreach (var unprepared in new[] {
            World(story, 3, "trickster", "trickster.ever", "devarra.escaped"),                   // flew without the pact
            World(story, 3, "trickster", "trickster.ever", P + "flight.pact"),                   // the pact, but she has not flown
            World(story, 3, "trickster", "trickster.ever", "devarra.lair_story_heard"),          // no hunt yet
            World(story, 3, "devarra.escaped", P + "flight.pact"),                               // no Trickster
            World(story, 3, "trickster", "trickster.ever", "devarra.dead_lair", P + "flight.pact") })
            check(!Rules.NativeGateHolds(story, Spawn, unprepared) && !Rules.NativeGateHolds(story, OverBody, unprepared),
                "Trk_Devarra_SpawnGate: a native gate holds outside her flight world.");
        var degradedWorld = Program.Copy(flown);
        degradedWorld.Flags.Add(Rules.DegradedPrefix + "devarra");
        check(!Rules.NativeGateHolds(story, Spawn, degradedWorld), "Trk_Devarra_SpawnGate: a degraded route still gates the Sanctum.");

        // Trk_Devarra_Unprepared: canon fate is an entry condition in the lair-kill, no-hunt and unprepared-escape worlds.
        foreach (var fate in new[] {
            World(story, 5, "trickster", "trickster.ever", "devarra.dead_lair"),
            World(story, 5, "trickster", "trickster.ever", "devarra.dead_sanctum"),
            World(story, 5, "trickster", "trickster.ever", "devarra.escaped", "devarra.dead_sanctum"),
            World(story, 5, "trickster", "trickster.ever", "devarra.dead_sanctum", "devarra.golems_over_body", P + "primed") })
            check(!AnyOpen(fate), "Trk_Devarra_Unprepared: a Devarra scene opens after her canon death.");

        // Trk_Devarra_Leash: the golems call an absent dragon; the stone is told she is on an errand; the fists come down.
        var called = World(story, 3, "trickster", "trickster.ever", P + "flight.pact", "devarra.escaped", "devarra.golems_calling", "devarra.golems_met");
        check(Rules.Available(story, leash, called) && !Rules.Available(story, leash, World(story, 3, "trickster", "trickster.ever", "devarra.golems_calling")),
            "Trk_Devarra_Leash: the leash is shut in her flight world, or opens without it.");
        check(After(leash, called, "report", 0).First().Has(P + "flight.struck"), "Trk_Devarra_Leash: lying to the stone does not record it.");
        var cut = World(story, 3, "trickster", "trickster.ever", P + "flight.pact", "devarra.escaped", "devarra.golems_calling", "devarra.golems_met",
            "devarra.golems_deactivated", "devarra.golems_met.latched");
        check(cut.Has(P + "leash_cut"), "Trk_Devarra_Leash: the native Deactivation does not cut the leash.");
        check(Rules.Available(story, left, cut), "The clutch cannot be left for her after the fists come down.");
        var leftFor = After(left, cut, "left", 0).First();
        check(leftFor.Has(P + "flight.clutch_left"), "Leaving the clutch for her is not recorded.");

        // Trk_Devarra_Return: two nights after the golems, she comes for her eggs; the tariff's road reaches the commit.
        var fresh = Program.Copy(leftFor);
        fresh.Times["devarra.golems_met.latched"] = fresh.Hour;
        check(!Rules.Available(story, eggs, Later(story, fresh, 47)) && Rules.Available(story, eggs, Later(story, fresh, 48)),
            "Trk_Devarra_Return: she does not come two nights after the golems.");
        var arrived = Later(story, leftFor, 48);
        check(Rules.Available(story, eggs, arrived), "Trk_Devarra_Return: she does not come for her eggs.");
        var paid = After(eggs, arrived, "clutch", 7).First();
        check(paid.Has(P + "returned") && paid.Has("devarra.started") && paid.Has(P + "cost.woken_hungry") && paid.Has(P + "clutch_collected"),
            "Trk_Devarra_Return: the collected clutch does not return her.");
        check(Reaches(paid, "devarra.committed"), "Trk_Devarra_Return: no road to the commit.");
        check(Rules.Available(story, eggs, Later(story, World(story, 3, "trickster.ever", "trickster.failed", P + "flight.pact", "devarra.escaped.latched",
            "devarra.golems_met.latched", "devarra.golems_deactivated"), 48)), "A pact made as a Trickster does not pay off after the path failed.");

        check(!Rules.Available(story, eggs, Later(story, World(story, 3, "trickster", "trickster.ever", P + "flight.pact", "devarra.escaped.latched",
            "devarra.golems_met.latched"), 48)), "Trk_Devarra_Return: she claims her eggs while the fists are still raised over them.");
        check(!Rules.Available(story, left, World(story, 3, "trickster", "trickster.ever", P + "flight.pact", "devarra.escaped", "devarra.golems_met")),
            "The clutch can be left for her under raised fists.");

        // Trk_Devarra_WrongPassword: the native Destruction; she lives, the eggs do not, and she knows whom to blame.
        var wrong = World(story, 3, "trickster", "trickster.ever", P + "flight.pact", "devarra.escaped", "devarra.golems_calling",
            "devarra.golems_met", "devarra.golems_met.latched", "eggs.destroyed");
        check(!Rules.Available(story, leash, wrong), "Trk_Devarra_WrongPassword: the leash opens over destroyed eggs.");
        var blamed = Later(story, wrong, 48);
        check(Rules.Available(story, eggs, blamed), "Trk_Devarra_WrongPassword: she does not come for her eggs after the wrong word.");
        var marked = After(eggs, blamed, "clutch", 6).First();
        check(marked.Has(P + "returned") && marked.Has(P + "marked") && !marked.Has("devarra.closed"),
            "Trk_Devarra_WrongPassword: the destroyed clutch does not mark the Commander.");
        var xanthir = After(eggs, blamed, "clutch", 5).First();
        check(xanthir.Has(P + "pointed_at_xanthir") && Choice(eggs, "clutch", 5).Alignment?.Direction == "Evil", "Pointing her at Xanthir costs nothing.");
        check(Reaches(marked, "devarra.committed"), "Trk_Devarra_WrongPassword: no road to the commit after the eggs died.");

        // The other native egg fates.
        var omelet = Later(story, World(story, 5, "trickster", "trickster.ever", P + "flight.pact", "devarra.escaped.latched", "devarra.golems_met.latched",
            "eggs.project", "eggs.omelet"), 48);
        var cook = After(eggs, omelet, "clutch", 0).First();
        check(cook.Has(P + "cook_given") && Choice(eggs, "clutch", 0).Alignment?.Direction == "Evil", "Giving her the cook is not an evil choice.");

        // Trk_Devarra_Test: her two demands, carried by the Storyteller, in her flight world.
        var hungry = World(story, 5, "trickster.ever", P + "flight.pact", "devarra.escaped.latched", P + "returned", P + "cost.woken_hungry", "devarra.started");
        check(hungry.Has(P + "flown") && Rules.Available(story, tithe, hungry), "Trk_Devarra_Test: the tithe is shut.");
        var tested = After(tithe, hungry, "ending_free", 0).First();
        check(tested.Has(P + "tested") && tested.Has(P + "ending_true") && !tested.Has("devarra.committed"),
            "Trk_Devarra_Test: the test does not record the true ending, or commits.");
        check(Program.Walk(tithe, hungry, (id, _) => check(id != "tithe" && id != "ending", "The flight world hears the moult's tithe: " + id)).Count > 0,
            "The tithe does not play in the flight world.");
        var owned = After(tithe, hungry, "tithe_free", 2).First();
        check(owned.Has("devarra.closed") && !Reaches(owned, "devarra.committed"), "Presuming to own her is not a hard no.");

        // Trk_Devarra_Commit and Trk_Devarra_Refusal.
        var ready = World(story, 5, "trickster.ever", P + "flight.pact", "devarra.escaped.latched", P + "returned", P + "ruthless", P + "tested",
            P + "ending_true", "devarra.started");
        check(Rules.Available(story, lair, ready), "Trk_Devarra_Commit: the commit is shut.");
        var bitten = After(lair, ready, "terms", 3).First();
        check(bitten.Has("devarra.committed") && bitten.Has(P + "cost.bitten"), "Trk_Devarra_Commit: the forearm does not commit.");
        check(Program.WalkVia(lair, ready, "terms", 0).Count == 0, "The flight world commits through the moult's line.");
        var no = After(lair, ready, "terms", 1).First();
        check(no.Has("devarra.closed") && !no.Has("devarra.committed"), "Trk_Devarra_Refusal: 'No bites' commits.");
        var leftHungry = After(lair, ready, "terms", 2).First();
        check(leftHungry.Has(P + "left_hungry") && Rules.Available(story, backUp, Later(story, leftHungry, 72)),
            "Leaving her the tower does not let the Commander climb back.");
        var noTeller = World(story, 5, "trickster.ever", P + "flight.pact", "devarra.escaped.latched", P + "returned", "storyteller.dead_main", "devarra.started");
        check(Rules.Available(story, lair, noTeller), "The commit is shut when the Storyteller cannot carry the test.");
        check(After(lair, noTeller, "second_question_free", 0).First().Has(P + "tested"), "Her own second question does not test.");

        // The watchtower: the climb follows the test; the bite only after the commit.
        check(Rules.Available(story, firstClimb, Later(story, tested, 24)) && !Rules.Available(story, firstClimb, hungry),
            "The first climb does not follow the test, or opens before it.");
        var bittenClimbed = Program.Copy(bitten);
        bittenClimbed.Flags.Add(T + "climbed");
        check(!Rules.Available(story, firstBite, Later(story, ready, 100)) && !Rules.Available(story, firstBite, Later(story, bitten, 24))
              && Rules.Available(story, firstBite, Later(story, bittenClimbed, 24)),
            "The first bite is not gated on the commit and the first climb.");
        check(Reaches(bitten, T + "first_bite") && Reaches(Later(story, tested, 24), T + "climbed"), "The watchtower beats are not reachable.");
        var oneShort = S(T + "one_short");
        check(oneShort.Nodes.Single(n => n.Id == "start").Choices[0].Forbids.Contains("nidalynn.trickster.eggs.vault")
              && oneShort.Nodes.Single(n => n.Id == "start").Choices[1].Requires.Contains("nidalynn.trickster.eggs.vault"),
            "The missing egg is counted in the Sanctum after a vault theft.");

        // No moult in the flight world: every Devarra page she can reach after flying is free of the retired device's facts.
        var moult = new[] { "moult", "carcass", "new hide", "dead thing", "i died", "got up", "killing blow", "three days", "brine", "dead body",
            "since i died", "while i was dead", "climbed out", "the dead are not" };
        int walked = 0;
        var outcomes = new[] { new string[0], new[] { P + "clutch_collected" }, new[] { "eggs.destroyed", P + "marked" }, new[] { "eggs.destroyed", P + "pointed_at_xanthir" }, new[] { "eggs.project", "eggs.omelet", P + "cook_given" },
            new[] { "eggs.project", "eggs.druids", P + "hunting_druids" }, new[] { "eggs.project", P + "clutch_withheld" },
            new[] { P + "ruthless", P + "tested", P + "ending_true" }, new[] { P + "hunts_demons", P + "tested", P + "ending_withheld" } };
        foreach (var extra in outcomes)
        foreach (var s in own.Concat(reactions).Where(s => !retired.Contains(s)))
        {
            var needs = s.Requires.Concat(s.RequiresAnyGroups.Select(g => g[0])).Where(k => k != "devarra.dead.latched").ToArray();
            var w = World(story, s.Chapters.Length > 0 ? s.Chapters[0] : s.MinChapter, new[] { "trickster", "trickster.ever", P + "flight.pact",
                "devarra.escaped.latched", "devarra.golems_met.latched", P + "returned", "devarra.started" }.Concat(needs).Concat(extra).ToArray());
            w = Later(story, w, s.DelayHours + 1);
            if (!Rules.Available(story, s, w)) continue;
            walked++;
            Program.Walk(s, w, (id, _) =>
            {
                string text = (s.Nodes.Single(n => n.Id == id).Text + " " + string.Join(" ", s.Nodes.Single(n => n.Id == id).Choices
                    .Where(c => Rules.Match(c.Requires, c.Forbids, w)).Select(c => c.Text))).ToLowerInvariant();
                foreach (var word in moult) check(!text.Contains(word), "The flight world reads the moult (" + word + "): " + s.Id + "/" + id);
            });
        }
        check(walked >= 300, "Too few Devarra scenes open in the flight world: " + walked);
        // Every watchtower beat opens in some world (the flight world, or a legacy save that returned her through the moult).
        foreach (var s in tower)
        {
            var needs = s.Requires.Concat(s.RequiresAnyGroups.Select(g => g[0])).ToArray();
            bool legacyOnly = s.Forbids.Contains(P + "flown");
            var basis = legacyOnly ? new[] { "trickster", "trickster.ever", P + "returned", "devarra.started", "devarra.dead.latched" }
                : new[] { "trickster", "trickster.ever", P + "flight.pact", "devarra.escaped.latched", P + "returned", "devarra.started" };
            var w = World(story, s.Chapters[0], basis.Concat(needs).ToArray());
            check(Rules.Available(story, s, Later(story, w, s.DelayHours + 1)), "A watchtower beat never opens: " + s.Id);
        }
        // Q11 history witnesses: what a beat recalls must have happened on this save.
        var abyss = S(T + "after_the_abyss");
        var dwarf = S(T + "the_dwarf");
        var climbCh3 = After(firstClimb, Later(story, World(story, 3, "trickster", "trickster.ever", P + "flight.pact", "devarra.escaped.latched", P + "returned",
            P + "tested", "devarra.started", "devarra.chapter_three"), 30), "leave", 1).First();
        check(climbCh3.Has(T + "climbed") && climbCh3.Has(T + "climbed_before_the_abyss"),
            "A Chapter 3 climb does not record that she was back before the Abyss.");
        var climbCh5 = Program.Walk(firstClimb, Later(story, World(story, 5, "trickster", "trickster.ever", P + "flight.pact", "devarra.escaped.latched",
            P + "returned", P + "tested", "devarra.started"), 30)).ToList();
        check(climbCh5.Count > 0 && climbCh5.All(r => !r.Has(T + "climbed_before_the_abyss")),
            "A Chapter 5 first climb claims she waited out the Abyss.");
        check(Rules.Available(story, abyss, Later(story, climbCh3, 24, 5)) && climbCh5.All(r => !Rules.Available(story, abyss, Later(story, r, 24, 5))),
            "The Abyss vigil is not gated on a Chapter 3 climb.");
        // PP7 (Chapter 4): the wrong sky, a story kept back for her on the voyage out of Alushinyrra; the Abyss vigil reads it.
        var sky = S(T + "wrong_sky");
        string[] skyVariants = { T + "wrong_sky.fear", T + "wrong_sky.view", T + "wrong_sky.spent" };
        string[] skyAnswers = { "sky_fear", "sky_view", "sky_spent" };
        check(sky.Remote && sky.Kind == "memory" && sky.Chapters.SequenceEqual(new[] { 4 }) && sky.MinChapter == 4 && sky.MaxChapter == 4
              && sky.Relationship == "devarra" && new[] { "trickster.ever", T + "climbed_before_the_abyss", "devarra.voyage_begun.latched" }.All(sky.Requires.Contains)
              && story.Latches["devarra.voyage_begun.latched"].SequenceEqual(new[] { "devarra.voyage_begun" })
              && new[] { "devarra.closed", T + "wrong_sky.kept" }.All(sky.Forbids.Contains)
              && story.StartedDialogs["devarra.voyage_begun"] == "a07f6d1f93531e048928c5c9de328a92",
            "The wrong sky lost its shape (remote memory, Chapter 4, after a Chapter 3 climb and the voyage).");
        var skyPages = new HashSet<string>();
        var abyssPages = new HashSet<string>();
        foreach (bool flownOver in new[] { false, true })
        {
            var ashore = Later(story, climbCh3, 24, 4);
            if (flownOver) ashore.Flags.Add(T + "flown");
            check(!Rules.Available(story, sky, ashore), "The wrong sky opens before the voyage.");
            var aboard = Program.Copy(ashore); aboard.Flags.Add("devarra.voyage_begun"); Rules.Complete(story, aboard);
            aboard.Times["devarra.voyage_begun.latched"] = aboard.Hour;   // Main.RecordLatches stamps the hour the voyage began
            check(!Rules.Available(story, sky, aboard) && !Rules.Available(story, sky, Later(story, aboard, sky.DelayHours - 1)),
                "The wrong sky opens before its hours have passed on the voyage (the older climb must not count).");
            check(Rules.Available(story, sky, Later(story, aboard, sky.DelayHours)), "The wrong sky does not open on the voyage.");
            foreach (var chapter in new[] { 3, 5 })
                check(!Rules.Available(story, sky, Later(story, aboard, sky.DelayHours, chapter)), "The wrong sky leaks into chapter " + chapter);
            var closed = Later(story, aboard, sky.DelayHours); closed.Flags.Add("devarra.closed");
            check(!Rules.Available(story, sky, closed), "The wrong sky ignores a closed route.");
            var kept = Program.Walk(sky, Later(story, aboard, sky.DelayHours), (id, _) =>
            {
                skyPages.Add(id);
                if (id == "lamps") check(flownOver, "The wrong sky remembers a flight over Drezen that was not flown.");
                if (id == "planks") check(!flownOver, "The wrong sky forgets the flight over Drezen.");
            }).Where(r => r.Has(sky.Id)).ToList();
            check(kept.Count == 3 && kept.All(r => r.Has(T + "wrong_sky.kept") && skyVariants.Count(r.Has) == 1 && !Rules.Available(story, sky, r)),
                "The wrong sky loses a variant, overlaps, or replays.");
            foreach (var r in kept)
            {
                var home = Later(story, r, 24, 5);
                check(Rules.Available(story, abyss, home), "The Abyss vigil does not follow the wrong sky.");
                Program.Walk(abyss, home, (id, _) =>
                {
                    abyssPages.Add(id);
                    int i = Array.IndexOf(skyAnswers, id);
                    if (i >= 0) check(r.Has(skyVariants[i]), "The Abyss vigil answers a sky that was not kept: " + id);
                });
            }
        }
        foreach (var r in climbCh5)
        {
            var late = Later(story, r, 24, 4); late.Flags.Add("devarra.voyage_begun");
            check(!Rules.Available(story, sky, late), "The wrong sky follows a first climb made after the Abyss.");
        }
        check(skyPages.SetEquals(sky.Nodes.Select(n => n.Id)), "Unreached page of the wrong sky.");
        check(skyAnswers.All(abyssPages.Contains), "The Abyss vigil never answers the wrong sky.");
        var vigil = abyss.Nodes.Single(n => n.Id == "climb").Choices;
        check(vigil.Count == 5 && vigil[0].Next == "back" && vigil[1].Next == "gift" && vigil.Skip(2).Select(c => c.Requires.Single()).SequenceEqual(skyVariants)
              && abyss.Nodes.TakeLast(3).Select(n => n.Id).SequenceEqual(skyAnswers),
            "The wrong sky's answers were not appended to the Abyss vigil, or read the wrong flag.");
        // PP7 (Sol r1): a vault clutch cooked or destroyed after the promise is answered as spent, never as living eggs.
        var withheld = S(T + "the_clutch").Nodes.Single(n => n.Id == "withheld").Choices;
        check(withheld.Count == 5 && withheld[0].Next == "withheld_vault" && withheld[0].Forbids.Contains("eggs.omelet") && withheld[0].Forbids.Contains("eggs.destroyed")
              && withheld.Skip(3).All(c => c.Next == "withheld_spent" && c.Requires.Contains("eggs.project")),
            "The clutch scene offers the vault after its eggs were spent.");
        var hatch = S(P + "epilogue.woken").Nodes[0].Paragraphs.Where(x => x.Requires.Contains(T + "vault_opened")).ToArray();
        check(hatch.Count(x => x.Text.Contains("hatched", StringComparison.Ordinal) && x.Forbids.Contains("eggs.omelet") && x.Forbids.Contains("eggs.destroyed")) == 1
              && hatch.Count(x => x.Text.Contains("emptied the other way", StringComparison.Ordinal)) == 2,
            "The epilogue hatches a clutch that was cooked or destroyed.");
        var noAmbush = World(story, 5, "trickster", "trickster.ever", P + "returned", "devarra.started", T + "climbed");
        check(!Rules.Available(story, dwarf, Later(story, noAmbush, 30)), "Greybor's ambush is recalled without its native cue.");
        check(dwarf.Nodes.Single(n => n.Id == "climb").Choices[2].Requires.Contains("devarra.react.greybor.repeat_work"),
            "The Commander reports Greybor's message without having heard it.");
        check(story.Scenes.Any(s => s.Id == "devarra.lastcall.page") && story.Scenes.Any(s => s.Id == "devarra.lastcall.call"),
            "The egg bill has no Last Call collection.");

        // Legacy: a save that returned her through the moult before the redesign keeps its own lines.
        var legacy = World(story, 5, "trickster.ever", "devarra.dead_sanctum", "devarra.dead.latched", P + "primed", P + "returned", P + "cost.woken_hungry", "devarra.started");
        check(!legacy.Has(P + "flown") && Rules.Available(story, tithe, legacy), "A legacy save loses its continuation.");
        check(Program.Walk(tithe, legacy, (id, _) => check(!id.EndsWith("_free", StringComparison.Ordinal), "A legacy save hears the flight world: " + id)).Count > 0,
            "The legacy tithe does not play.");
        Console.WriteLine("PASS: Devarra Trickster (Trk_Devarra_*): the pact, the escape, the Sanctum gate, the leash, the wrong password, canon fate unprepared, "
            + "the return, the tithe, the tower's terms and " + tower.Length + " watchtower beats (" + walked + " scenes walked in the flight world).");
    }
}
