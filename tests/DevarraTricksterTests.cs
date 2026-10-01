using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Devarra, Trickster (Writer/handoffs/trickster/devarra.md; F08): "Clutch-mother".
// One block per spec rules test (Trk_Devarra_*), the shape of each hook, and the watchtower courtship (devarra_tower):
// every beat on the Storyteller's hub, every gate produced by an earlier beat, the bite only after the commit, and the
// route's letters limited to the return and the commit (her only native unit is a hostile monster).
internal static class DevarraTricksterTests
{
    private const string P = "devarra.trickster.";
    private const string T = "devarra.tower.";
    private const string StHub = "2f5b7e0b76d3c5a42a431e1e33a8db09";
    private const string StReturn = "34a0d078b4ac51547a8f5e0e1c8e1e2c";

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
        var lairStory = S(P + "dead.lair_story");
        var setup = S(P + "dead.setup");
        var fallback = S(P + "dead.storytellers_version");
        var woken = S(P + "dead.woken");
        var tithe = S(P + "after.tithe");
        var lair = S(P + "after.lair");
        var firstClimb = S(T + "first_climb");
        var firstBite = S(T + "first_bite");
        var backUp = S(T + "back_up_the_mountain");
        var pages = story.Scenes.Where(s => s.Relationship == "devarra" && s.Owner == "DevarraEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "devarra" && s.Reaction).ToArray();
        var own = story.Scenes.Where(s => s.Relationship == "devarra" && !s.Reaction && s.Owner == "Devarra").ToArray();
        var tower = own.Where(s => s.Id.StartsWith(T, StringComparison.Ordinal)).ToArray();
        Choice Choice(Scene scene, string node, int index) => scene.Nodes.Single(n => n.Id == node).Choices[index];
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            var chosen = Choice(scene, node, index);
            var hits = Program.Walk(scene, w).Where(r => chosen.Set.All(r.Has) && (chosen.Set.Length > 0 || r.Has(scene.Id))).ToList();
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

        // Shape and hooks.
        var rel = story.Relationships["devarra"];
        check(rel.StartedFlag == "devarra.started" && rel.ClosedFlag == "devarra.closed" && rel.CommittedFlag == "devarra.committed"
              && rel.UnavailableFlags.OrderBy(f => f).SequenceEqual(new[] { "devarra.dead_lair", "devarra.dead_sanctum", "inhuman" })
              && rel.UnavailableOverrides["devarra.dead_lair"] == P + "returned" && rel.UnavailableOverrides["devarra.dead_sanctum"] == P + "returned"
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "dead_lair", "dead_sanctum" })
              && rel.TricksterAccess.Values.All(a => a.Device == P + "dead.woken" && a.Returned == P + "returned"),
            "Devarra's relationship does not match the spec.");
        check(lairStory.AnswerLists.SequenceEqual(new[] { "c8298f1630fd82046986d313ba35f601" })
              && lairStory.NativeReturnCue == "26650f05010b9ce4cb0202da7e35ce8e" && lairStory.TricksterDevice && lairStory.TricksterState == "dead_lair"
              && Choice(lairStory, "story", 0).NativeNext == "3d5e59ddc658eb947874a1cac31dd6a4" && Choice(lairStory, "story", 0).Mythic == "PlayerIsTrickster"
              && Choice(lairStory, "story", 0).Alignment?.Direction == "Chaotic",
            "Primer A is not the Trickster answer on her lair list, before the native fight (Cue_0012).");
        check(setup.AnswerLists.SequenceEqual(new[] { "dd8ac86f25e0f6b4cac75386eb528851" })
              && setup.NativeReturnCue == "d39b1e850904daa43b7e6dab3a6e7f83" && setup.TricksterDevice
              && Choice(setup, "orders", 0).NativeNext == "9c653a907d8549248bd9d202c1fb8964" && setup.Requires.Contains("devarra.golems_over_body"),
            "Primer B is not the golem joke on Golems_DragonEggs, continuing into Cue_0045.");
        foreach (var s in new[] { fallback, tithe }.Concat(tower))
            check(s.AnswerLists.SequenceEqual(new[] { StHub }) && s.NativeReturnCue == StReturn && s.ContactUnit == null
                  && !Rules.IsRemote(s) && s.Forbids.Contains("storyteller.dead"),
                "A Devarra beat is not on the Storyteller's hub, guarded by his death: " + s.Id);
        foreach (var s in tower)
            check(s.Forbids.Contains("devarra.closed"), "A watchtower beat plays after her hard no: " + s.Id);
        var letters = story.Scenes.Where(s => s.Relationship == "devarra" && Rules.IsRemote(s) && s.Owner != "DevarraEpilogue").ToArray();
        check(letters.Select(s => s.Id).OrderBy(i => i).SequenceEqual(new[] { P + "after.lair", P + "dead.woken" })
              && letters.All(s => s.Chapters.SequenceEqual(new[] { 3, 5 })),
            "Devarra's letters are not exactly the return and the commit, in Chapters 3 and 5.");
        check(woken.TricksterDevice && woken.Nodes.SelectMany(n => n.Choices).All(c => !c.Set.Contains("devarra.committed")),
            "The return scene commits, or is not a device.");
        check(Choice(tithe, "tithe", 0).Crusade?.Resource == "Materials" && Choice(tithe, "tithe", 0).Crusade!.Amount == -100
              && Choice(tithe, "tithe", 0).Alignment?.Direction == "Evil" && Choice(tithe, "tithe", 1).Crusade?.Amount == -200
              && Choice(tithe, "tithe", 2).Set.Contains("devarra.closed"),
            "The tithe's hunger is not priced, or presuming to own her is not her hard no.");
        check(reactions.Length == 3 && reactions.All(r => r.Nodes.Count == 1 && r.Requires.Contains(P + "returned"))
              && reactions.Where(r => r.Owner == "Greybor").All(r => r.Forbids.Contains("greybor.dead") && r.Forbids.Contains("greybor.kicked_out"))
              && reactions.Where(r => r.Owner == "Storyteller").All(r => r.Forbids.Contains("storyteller.dead"))
              && reactions.Select(r => r.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Greybor", "Storyteller" }),
            "The reactions are not exactly Greybor and the Storyteller behind their guards.");
        check(pages.Length == 4 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null))),
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

        // Trk_Devarra_Setup: the golems over the fresh carcass.
        var golems = World(story, 3, "trickster", "devarra.golems_over_body", "devarra.dead_sanctum");
        check(Rules.Available(story, setup, golems), "Trk_Devarra_Setup: the golem joke is shut.");
        check(After(setup, golems, "orders", 0).First().Has(P + "primed"), "Trk_Devarra_Setup: the joke does not prime.");

        // Trk_Devarra_LairStory: her own ending, told before the blow.
        var lairWorld = World(story, 3, "trickster", "devarra.lair_story_heard");
        check(Rules.Available(story, lairStory, lairWorld), "Trk_Devarra_LairStory: the lair primer is shut.");
        var told = After(lairStory, lairWorld, "story", 0).First();
        check(told.Has(P + "primed") && told.Has(P + "story_told") && told.Has(P + "cost.ending_owed"),
            "Trk_Devarra_LairStory: the story does not prime, or owe her an ending.");
        check(!Rules.Available(story, lairStory, World(story, 3, "trickster", "devarra.dead_lair")), "The lair primer opens after the blow.");

        // Trk_Devarra_DeadSanctum: the return; the omelet branch gives her the cook.
        var sanctum = World(story, 5, "trickster", "trickster.ever", "devarra.dead_sanctum", P + "primed", "eggs.project", "eggs.omelet");
        check(Rules.Available(story, woken, sanctum) && !Rules.Available(story, fallback, sanctum),
            "Trk_Devarra_DeadSanctum: the return is shut, or the fallback opens after a primer.");
        var cook = After(woken, sanctum, "clutch", 0).First();
        check(cook.Has(P + "returned") && cook.Has("devarra.started") && cook.Has(P + "cost.woken_hungry") && cook.Has(P + "cook_given")
              && Choice(woken, "clutch", 0).Alignment?.Direction == "Evil",
            "Trk_Devarra_DeadSanctum: giving her the cook does not return her, or costs nothing.");
        check(Reaches(cook, "devarra.committed"), "Trk_Devarra_DeadSanctum: no road to the commit.");

        // Trk_Devarra_DeadLair: the destroyed clutch, and the Commander who watched.
        var gorge = World(story, 3, "trickster", "trickster.ever", "devarra.dead_lair", P + "primed", P + "story_told", "eggs.destroyed");
        check(Rules.Available(story, woken, gorge), "Trk_Devarra_DeadLair: the return is shut.");
        var marked = After(woken, gorge, "clutch", 6).First();
        check(marked.Has(P + "returned") && marked.Has(P + "marked"), "Trk_Devarra_DeadLair: watching does not mark the Commander.");
        check(Reaches(marked, "devarra.committed", 3) || Reaches(marked, "devarra.committed"), "Trk_Devarra_DeadLair: no road to the commit.");

        // Trk_Devarra_Unprimed: the Storyteller's price.
        var unprimed = World(story, 5, "trickster", "trickster.ever", "devarra.dead_lair");
        check(Rules.Available(story, fallback, unprimed) && !Rules.Available(story, woken, unprimed),
            "Trk_Devarra_Unprimed: the fallback is shut, or the return opens unprimed.");
        var sold = After(fallback, unprimed, "price", 0).First();
        check(sold.Has(P + "primed") && sold.Has(P + "cost.late") && sold.Has(P + "cost.story_sold"),
            "Trk_Devarra_Unprimed: the sold story does not prime on late terms.");
        check(Rules.Available(story, woken, Later(story, sold, 72)) && !Rules.Available(story, woken, Later(story, sold, 71)),
            "Trk_Devarra_Unprimed: the return does not follow the sale after the promised three days.");
        var twice = After(fallback, unprimed, "raised", 0).First();
        check(twice.Has(P + "cost.shame_sold"), "Threatening the Storyteller does not cost the shameful story.");

        // Trk_Devarra_StorytellerRefused: canon fate stands.
        var refused = After(fallback, unprimed, "price", 2).First();
        check(refused.Has(P + "declined") && !Rules.Available(story, fallback, Later(story, refused, 48))
              && !Rules.Available(story, woken, Later(story, refused, 48)),
            "Trk_Devarra_StorytellerRefused: refusing his price does not leave her dead.");

        // Trk_Devarra_StorytellerDead: no fallback without the buyer of her tariff.
        check(!Rules.Available(story, fallback, World(story, 5, "trickster", "devarra.dead_lair", "storyteller.dead_main")),
            "Trk_Devarra_StorytellerDead: the fallback opens without the Storyteller.");

        // Trk_Devarra_EscapedThenSanctum: the druids' clutch withheld.
        var escaped = World(story, 5, "trickster", "trickster.ever", "devarra.escaped", "devarra.dead_sanctum", P + "primed", "eggs.project", "eggs.druids");
        var withheld = After(woken, escaped, "clutch", 3).First();
        check(withheld.Has(P + "returned") && withheld.Has(P + "clutch_withheld"), "Trk_Devarra_EscapedThenSanctum: the clutch is not withheld.");

        // Trk_Devarra_AfterFailure: an unprimed death after the path failed stays a death.
        var failed = World(story, 5, "trickster.ever", "trickster.failed", "devarra.dead_lair");
        check(!Rules.Available(story, fallback, failed) && !Rules.Available(story, woken, failed),
            "Trk_Devarra_AfterFailure: a failed Trickster raises an unprimed dragon.");
        // A primer taken as a Trickster still pays off after the failure.
        check(Rules.Available(story, woken, World(story, 5, "trickster.ever", "trickster.failed", "devarra.dead_sanctum", P + "primed")),
            "A primer taken before the path failed does not pay off.");

        // Trk_Devarra_Test: her two demands, carried by the Storyteller.
        var hungry = World(story, 5, "trickster.ever", P + "returned", P + "cost.woken_hungry", "devarra.started");
        check(Rules.Available(story, tithe, hungry), "Trk_Devarra_Test: the tithe is shut.");
        var tested = After(tithe, hungry, "ending", 0).First();
        check(tested.Has(P + "tested") && tested.Has(P + "ending_true") && !tested.Has("devarra.committed"),
            "Trk_Devarra_Test: the test does not record the true ending, or commits.");
        var owned = After(tithe, hungry, "tithe", 2).First();
        check(owned.Has("devarra.closed") && !Reaches(owned, "devarra.committed"), "Presuming to own her is not a hard no.");
        check(Reaches(hungry, "devarra.committed"), "Trk_Devarra_Test: no road to the commit.");

        // Trk_Devarra_Commit and Trk_Devarra_Refusal.
        var ready = World(story, 5, "trickster.ever", P + "returned", P + "ruthless", P + "tested", P + "ending_true", "devarra.started");
        check(Rules.Available(story, lair, ready), "Trk_Devarra_Commit: the commit is shut.");
        var bitten = After(lair, ready, "terms", 0).First();
        check(bitten.Has("devarra.committed") && bitten.Has(P + "cost.bitten"), "Trk_Devarra_Commit: the forearm does not commit.");
        var no = After(lair, ready, "terms", 1).First();
        check(no.Has("devarra.closed") && !no.Has("devarra.committed"), "Trk_Devarra_Refusal: 'No bites' commits.");
        var leftHungry = After(lair, ready, "terms", 2).First();
        check(leftHungry.Has(P + "left_hungry") && Rules.Available(story, backUp, Later(story, leftHungry, 72)),
            "Leaving her the tower does not let the Commander climb back.");
        // A dead Storyteller: she asks the second question herself.
        var noTeller = World(story, 5, "trickster.ever", P + "returned", "storyteller.dead_main", "devarra.started");
        check(Rules.Available(story, lair, noTeller), "The commit is shut when the Storyteller cannot carry the test.");
        check(After(lair, noTeller, "second_question", 0).First().Has(P + "tested"), "Her own second question does not test.");

        // The watchtower: the climb follows the test; the bite only after the commit.
        check(Rules.Available(story, firstClimb, Later(story, tested, 24)) && !Rules.Available(story, firstClimb, hungry),
            "The first climb does not follow the test, or opens before it.");
        check(!Rules.Available(story, firstBite, Later(story, ready, 100)) && Rules.Available(story, firstBite, Later(story, bitten, 24)),
            "The first bite is not gated on the commit.");
        check(Reaches(bitten, T + "first_bite") && Reaches(Later(story, tested, 24), T + "climbed"),
            "The watchtower beats are not reachable.");
        foreach (var s in tower)
        {
            var needs = s.Requires.Concat(s.RequiresAnyGroups.Select(g => g[0])).ToArray();
            var w = World(story, s.Chapters[0], new[] { "trickster", "trickster.ever", P + "returned", "devarra.started" }.Concat(needs).ToArray());
            check(Rules.Available(story, s, Later(story, w, s.DelayHours + 1)), "A watchtower beat never opens: " + s.Id);
        }
        // Q11 history witnesses: what a beat recalls must have happened on this save.
        var abyss = S(T + "after_the_abyss");
        var dwarf = S(T + "the_dwarf");
        var climbCh3 = After(firstClimb, Later(story, World(story, 3, "trickster", "trickster.ever", P + "returned", P + "tested", "devarra.started", "devarra.chapter_three"), 30), "leave", 1).First();
        check(climbCh3.Has(T + "climbed") && climbCh3.Has(T + "climbed_before_the_abyss"),
            "A Chapter 3 climb does not record that she was back before the Abyss.");
        var climbCh5 = Program.Walk(firstClimb, Later(story, World(story, 5, "trickster", "trickster.ever", P + "returned", P + "tested", "devarra.started"), 30)).ToList();
        check(climbCh5.Count > 0 && climbCh5.All(r => !r.Has(T + "climbed_before_the_abyss")),
            "A Chapter 5 first climb claims she waited out the Abyss.");
        check(Rules.Available(story, abyss, Later(story, climbCh3, 24, 5)) && climbCh5.All(r => !Rules.Available(story, abyss, Later(story, r, 24, 5))),
            "The Abyss vigil is not gated on a Chapter 3 climb.");
        var noAmbush = World(story, 5, "trickster", "trickster.ever", P + "returned", "devarra.started", T + "climbed");
        check(!Rules.Available(story, dwarf, Later(story, noAmbush, 30)) && Rules.Available(story, dwarf, Later(story, World(story, 5, "trickster", "trickster.ever", P + "returned", "devarra.started", T + "climbed", "devarra.greybor_struck"), 30)),
            "Greybor's ambush is recalled without its native cue.");
        check(dwarf.Nodes.Single(n => n.Id == "climb").Choices[2].Requires.Contains("devarra.react.greybor.repeat_work"),
            "The Commander reports Greybor's message without having heard it.");
        check(story.Scenes.Any(s => s.Id == "devarra.lastcall.page") && story.Scenes.Any(s => s.Id == "devarra.lastcall.call"),
            "The egg bill has no Last Call collection.");
        Console.WriteLine("PASS: Devarra Trickster (Trk_Devarra_*): the lair story, the golems, the Storyteller's price, the moult, the tithe, the tower's terms and " + tower.Length + " watchtower beats.");
    }
}
