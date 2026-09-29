using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Delamere, Trickster (Writer/handoffs/11-ROSTER-PLAN-2.md §2, "Be the stag"; spec trickster/delamere.md for hooks).
// The device in its three places (the crypt with Kyado, the crypt without him, the Drezen chapel), the chase and the arrow,
// the courtship's gates and pivotal choices, the commit as her letting herself be caught, and the hard and soft no's.
internal static class DelamereTricksterTests
{
    private const string P = "delamere.trickster.";
    private const string KyadoHub = "d7aadaa261a8023489bdba49216cc334";
    private const string KyadoReturn = "5230d5fd7201db04287903ac6a95d30c";
    private const string Bow = "5fd95b425dd0b73488554abcb68382d3";
    private const string CursedBow = "15acf7ada5903ec429f7cd62a6162613";

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
        var lore = S(P + "temple.horn_lore");
        var crypt = S(P + "crypt.stag");
        var alone = S(P + "crypt.stag_alone");
        var late = S(P + "crypt.stag_late");
        var drezen = S(P + "drezen.stag");
        var count = S(P + "woken.count");
        var meat = S(P + "woken.first_meat");
        var table = S(P + "woken.feasting_table");
        var whiteStag = S(P + "woken.white_stag");
        var red = S(P + "woken.red_blood");
        var woods = S(P + "woken.my_woods");
        var hunt = S(P + "woods.second_hunt");
        var huntPage = S(P + "woods.second_hunt_page");
        var huntLate = S(P + "woods.second_hunt_late");
        var village = S(P + "woken.village");
        var owed = S(P + "woken.day_owed");
        var lessons = S(P + "temple.prior_lessons");
        var mine = story.Scenes.Where(s => s.Relationship == "delamere").ToArray();
        var own = mine.Where(s => !s.Reaction && s.Owner == "Delamere").ToArray();
        var pages = mine.Where(s => s.Owner == "DelamereEpilogue").ToArray();
        var reactions = mine.Where(s => s.Reaction).ToArray();
        Choice Choice(Scene scene, string node, int index) => scene.Nodes.Single(n => n.Id == node).Choices[index];
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            var chosen = Choice(scene, node, index);
            var hits = Program.Walk(scene, w).Where(r => chosen.Set.All(r.Has) && (chosen.Set.Length > 0 || r.Has(scene.Id))).ToList();
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        // Plays every available Delamere scene forward (each committing or completing path) and reports whether a flag is held.
        bool Reaches(Snapshot start, string flag, int chapter = 5)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 16 && frontier.Count > 0; depth++)
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
        var rel = story.Relationships["delamere"];
        check(rel.StartedFlag == "delamere.started" && rel.ClosedFlag == "delamere.closed" && rel.CommittedFlag == "delamere.committed"
              && rel.UnavailableFlags.Length == 0
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "crypt", "drezen", "unvisited" })
              && rel.TricksterAccess["crypt"].Device == P + "crypt.stag" && rel.TricksterAccess["drezen"].Device == P + "drezen.stag"
              && rel.TricksterAccess.Values.All(a => a.Returned == P + "returned"),
            "Delamere's relationship does not match 11 §2.");
        foreach (var s in new[] { lore, crypt, hunt, lessons })
            check(s.AnswerLists.SequenceEqual(new[] { KyadoHub }) && s.NativeReturnCue == KyadoReturn && s.Chapters.SequenceEqual(new[] { 3 })
                  && s.Forbids.Contains("kyado.dead") && !Rules.IsRemote(s),
                "A temple beat is not on Kyado's list, in Chapter 3, behind his death: " + s.Id);
        check(!story.Presences.Keys.Any(k => k.StartsWith("delamere", StringComparison.Ordinal)),
            "Delamere spawns a presence; her native units share the undead prefab.");
        foreach (var s in new[] { crypt, alone, late, drezen })
        {
            var checks = s.Nodes.SelectMany(n => n.Choices).Where(c => c.Check != null).Select(c => c.Check!).ToArray();
            check(s.TricksterDevice && s.Requires.Contains("trickster") && s.Forbids.Contains(P + "returned")
                  && checks.Count(k => k.Skill == "SkillLoreNature") == 2 && checks.Count(k => k.Skill == "SkillMobility") == 1
                  && checks.Where(k => k.Skill == "SkillLoreNature").Select(k => k.DC).OrderBy(d => d).SequenceEqual(new[] { 18, 26 }),
                "The waking is not the stag's call (Lore (Nature), 18 with Kyado's lore, 26 without) and the run (Mobility): " + s.Id);
            var lift = s.Nodes.Single(n => n.Id == "lift").Choices;
            check(lift[0].Requires.Contains(P + "primed") && lift[1].Forbids.Contains(P + "primed") && lift.Take(2).All(c => c.Mythic == "PlayerIsTrickster")
                  && lift[2].Abort, "The horn is not a Trickster answer gated on the lore, with a way to hang it back: " + s.Id);
            check(s.Nodes.SelectMany(n => n.Choices).All(c => !c.Set.Contains("delamere.committed")), "The waking commits: " + s.Id);
            check(s.Nodes.Single(n => n.Id == "fumble").Choices.All(c => c.Abort), "A fumbled call does not leave the horn to try again: " + s.Id);
        }
        check(!alone.Forbids.Contains("kyado.dead") && alone.Requires.Contains("kyado.dead") && late.Chapters.SequenceEqual(new[] { 5 })
              && late.Forbids.Contains("kyado.dead") && drezen.Requires.Contains("delamere.remains_finished"),
            "The waking's twins are not gated on Kyado's death, Chapter 5, or the remains in Drezen.");
        var removals = own.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Where(c => c.RemoveItem != null).ToArray();
        check(removals.Length > 0 && removals.All(c => c.RemoveItem == Bow && c.Requires.Contains("delamere.bow_held")
                                                     || c.RemoveItem == CursedBow && c.Requires.Contains("delamere.cursed_bow_held"))
              && story.RemovableItems.Contains(Bow) && story.RemovableItems.Contains(CursedBow),
            "Her bow is taken back without holding it.");
        var committers = own.Where(s => s.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains("delamere.committed"))).Select(s => s.Id).OrderBy(i => i);
        check(committers.SequenceEqual(new[] { P + "woods.second_hunt", P + "woods.second_hunt_late", P + "woods.second_hunt_page" }),
            "Something other than the second hunt commits her.");
        check(reactions.Length == 4 && reactions.All(r => r.Nodes.Count == 1)
              && reactions.Select(r => r.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Kyado", "Ulbrig", "Woljif" })
              && reactions.Where(r => r.Owner == "Kyado").All(r => r.Forbids.Contains("kyado.dead")),
            "The reactions are not Kyado (twice), Ulbrig and Woljif behind their guards.");
        check(pages.Length == 5 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null))),
            "The epilogue pages carry effects or are missing.");
        check(story.Derived[P + "late_committed"].Single().SequenceEqual(new[] { "trickster.ever", P + "second_hunt_offered" })
              && story.Derived["delamere.harem.eligible"].Length == 2 && story.Derived.ContainsKey("delamere.harem.voice.a_village_not_a_city"),
            "The late commit or the household eligibility is not declared.");
        var produced = new HashSet<string>(mine.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set));
        foreach (var s in own)
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)).Where(k => k.StartsWith(P, StringComparison.Ordinal)))
                check(produced.Contains(key), "A Delamere gate has no producer: " + s.Id + " requires " + key);
        foreach (var s in mine)
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)))
                check(!(key.EndsWith(".closed", StringComparison.Ordinal) && key != "delamere.closed")
                      && !(key.EndsWith("_dead", StringComparison.Ordinal) || key.EndsWith(".dead", StringComparison.Ordinal) && key != "kyado.dead"),
                    "Delamere needs someone else dead or closed: " + s.Id + " " + key);

        // Trk_Delamere_HornLore: Kyado's foresight lowers the call.
        var visited = World(story, 3, "trickster", "trickster.ever", "delamere.tomb_visited");
        check(Rules.Available(story, lore, visited), "Trk_Delamere_HornLore: Kyado's lore is shut.");
        check(After(lore, visited, "roar", 0).First().Has(P + "primed"), "Trk_Delamere_HornLore: the roar is not learned.");

        // Trk_Delamere_Crypt: the call, the run, the arrow, the limp; she keeps the hunt.
        check(Rules.Available(story, crypt, visited) && !Rules.Available(story, alone, visited) && !Rules.Available(story, drezen, visited),
            "Trk_Delamere_Crypt: the physical waking is shut, or a twin opens beside it.");
        var woken = After(crypt, visited, "home_kyado", 0).First();
        check(woken.Has(P + "returned") && woken.Has("delamere.started") && woken.Has(P + "cost.limp") && woken.Has(P + "cost.hunt_owed")
              && woken.Has(P + "woke_with_kyado") && !woken.Has("delamere.committed"),
            "Trk_Delamere_Crypt: the waking does not return her with the limp and the hunt owed.");
        check(Program.Walk(crypt, visited).Any(r => r.Has(P + "ran_far")) && Program.Walk(crypt, visited).Any(r => r.Has(P + "ran_short")),
            "Trk_Delamere_Crypt: the run has no far and no short end.");
        check(Reaches(woken, "delamere.committed", 3), "Trk_Delamere_Crypt: no road to the commit in Chapter 3.");
        var sent = After(crypt, visited, "grave", 0).First();
        check(sent.Has("delamere.closed") && sent.Has(P + "declined") && !sent.Has(P + "returned") && !Reaches(sent, "delamere.committed"),
            "Trk_Delamere_Declined: sending her back to her grave is not a hard no.");

        // Trk_Delamere_Unvisited: the initiated key, the sealed tomb.
        var initiated = World(story, 3, "trickster", "trickster.ever", "kyado.initiated");
        check(Rules.Available(story, crypt, initiated), "Trk_Delamere_Unvisited: the initiated key does not open the crypt.");
        check(Program.Walk(crypt, initiated).Any(r => r.Has(P + "returned")), "Trk_Delamere_Unvisited: the sealed tomb cannot be woken.");
        check(!Rules.Available(story, crypt, World(story, 3, "trickster", "trickster.ever", "kyado.crypt_door_seen")),
            "Trk_Delamere_DoorOnly: the crypt opens under Zanedra's curse without the key.");
        check(!own.Any(s => s.TricksterDevice && Rules.Available(story, s, World(story, 3, "trickster", "trickster.ever"))),
            "Trk_Delamere_NoReason: a waking opens with no native reason to go down.");

        // Trk_Delamere_KyadoDead and Trk_Delamere_Late: the page twins.
        var noKyado = World(story, 3, "trickster", "trickster.ever", "delamere.tomb_visited", "kyado.dead");
        check(!Rules.Available(story, crypt, noKyado) && Rules.Available(story, alone, noKyado),
            "Trk_Delamere_KyadoDead: the page twin does not replace the temple scene.");
        var aloneWoken = After(alone, noKyado, "home_alone", 0).First();
        check(aloneWoken.Has(P + "returned") && Reaches(aloneWoken, "delamere.committed"), "Trk_Delamere_KyadoDead: no road to the commit.");
        var chapter5 = World(story, 5, "trickster", "trickster.ever", "delamere.tomb_visited");
        check(Rules.Available(story, late, chapter5) && !Rules.Available(story, crypt, chapter5), "Trk_Delamere_Late: the Chapter 5 waking is shut.");
        check(Reaches(After(late, chapter5, "home_late", 0).First(), "delamere.committed"), "Trk_Delamere_Late: no road to the commit.");

        // Trk_Delamere_Drezen: the remains in Drezen; she wakes in a city and runs you through it.
        var remains = World(story, 3, "trickster", "trickster.ever", "delamere.remains_finished", "delamere.tomb_visited");
        check(Rules.Available(story, drezen, remains) && !Rules.Available(story, crypt, remains) && !Rules.Available(story, alone, remains),
            "Trk_Delamere_Drezen: the chapel waking is shut, or the crypt opens without her.");
        var city = After(drezen, remains, "home_drezen", 0).First();
        check(city.Has(P + "woke_in_drezen") && city.Has(P + "returned") && Reaches(city, "delamere.committed", 3),
            "Trk_Delamere_Drezen: no road to the commit.");

        // Trk_Delamere_AfterFailure: no live Trickster, no waking.
        check(!own.Any(s => s.TricksterDevice && Rules.Available(story, s, World(story, 5, "trickster.ever", "trickster.failed", "delamere.tomb_visited"))),
            "Trk_Delamere_AfterFailure: a lost Trickster wakes her.");

        // Trk_Delamere_Bow: the bow carried off the tomb goes back into her hands, or she hunts with the yew.
        var carried = World(story, 3, "trickster", "trickster.ever", "delamere.tomb_visited", "delamere.relics_taken", "delamere.bow_held");
        var laid = After(crypt, carried, "taken_held", 0).First();
        check(laid.Has(P + "bow_returned") && Choice(crypt, "taken_held", 0).RemoveItem == Bow, "Trk_Delamere_Bow: laying the bow back does not return it.");
        var yew = After(crypt, carried, "taken_held", 1).First();
        check(yew.Has(P + "yew_bow"), "Trk_Delamere_Bow: keeping the bow does not wake her with the yew.");
        var hillBow = World(story, 3, "trickster.ever", P + "returned", P + "counted", P + "yew_bow", "delamere.bow_held", "delamere.started");
        check(After(meat, hillBow, "ask_held", 0).First().Has(P + "bow_returned") && Choice(meat, "ask_held", 0).RemoveItem == Bow,
            "Trk_Delamere_Bow: she cannot ask for the antler bow back on the hill.");

        // The courtship: each beat opens on the last, with its pivotal choices.
        var back = World(story, 3, "trickster.ever", P + "returned", "delamere.started", P + "cost.limp", P + "cost.hunt_owed");
        check(Rules.Available(story, count, back) && !Rules.Available(story, meat, back), "Fifty-three does not come first.");
        var given = After(count, back, "unwilling", 0).First();
        check(given.Has(P + "village.given") && Choice(count, "unwilling", 0).Crusade?.Resource == "Materials", "Volunteers cost no seed.");
        check(After(count, back, "unwilling", 1).First().Has(P + "village.forced") && Choice(count, "unwilling", 1).Alignment?.Direction == "Evil",
            "Driving families out is not the evil choice.");
        check(After(count, back, "unwilling", 2).First().Has(P + "village.refused"), "Refusing her is not recorded.");
        check(Program.Walk(count, back).Any(r => r.Has(P + "village.clans")), "The Trickster's forty villages cannot be argued.");
        check(Rules.Available(story, meat, Later(story, given, 24)), "The hunter eats last does not follow the count.");
        var fed = After(meat, given, "law", 0).First();
        check(Rules.Available(story, table, Later(story, fed, 24)) && Rules.Available(story, lessons, Later(story, fed, 24)),
            "The feasting table or the prior's lessons do not follow the hunt.");
        var spoken = After(table, fed, "judge", 0).First();
        check(spoken.Has(P + "kyado.spoken_for") && After(table, fed, "judge", 1).First().Has(P + "kyado.judged"),
            "Kyado's judgment is not the Commander's to speak.");
        var mourned = World(story, 3, "trickster.ever", P + "returned", P + "first_meat", "kyado.dead");
        check(After(table, mourned, "kyado_cairn", 0).First().Has(P + "kyado.mourned"), "A dead Kyado is not mourned.");
        check(Rules.Available(story, whiteStag, Later(story, spoken, 24)) && !Rules.Available(story, red, Later(story, spoken, 24)),
            "The white stag does not come between the table and Red.");
        var told = After(whiteStag, spoken, "week", 0).First();
        check(told.Has(P + "white_stag_told") && Rules.Available(story, red, Later(story, told, 24)), "Red does not follow the white stag.");
        var truth = After(red, told, "question", 0).First();
        var lie = After(red, told, "question", 1).First();
        check(truth.Has(P + "told_truth") && lie.Has(P + "lied_erastil") && After(red, told, "question", 2).First().Has(P + "told_both"),
            "The truth about who woke her is not the Commander's choice.");
        check(Rules.Available(story, woods, Later(story, truth, 24)), "My woods does not follow Red.");
        var offered = After(woods, truth, "want", 0).First();
        check(offered.Has(P + "second_hunt_offered") && !offered.Has("delamere.committed"), "Her proposal commits, or is not recorded.");
        check(After(woods, truth, "want", 2).First().Has("delamere.closed"), "Refusing to hunt her is not a no.");

        // Trk_Delamere_Commit: she lets herself be caught.
        check(Rules.Available(story, hunt, Later(story, offered, 24)) && !Rules.Available(story, huntPage, Later(story, offered, 24))
              && !Rules.Available(story, huntLate, Later(story, offered, 24)),
            "Trk_Delamere_Commit: the second hunt is not on Kyado's list while he lives, alone.");
        var caught = After(hunt, offered, "choice", 0).First();
        check(caught.Has("delamere.committed") && caught.Has(P + "caught"), "Trk_Delamere_Commit: catching her does not commit.");
        check(Program.Walk(hunt, offered).Any(r => r.Has(P + "tracked_her")) && Program.Walk(hunt, offered).Any(r => r.Has(P + "called_her")),
            "The hunt cannot be won by tracking, or by the horn when the trail is lost.");
        check(Choice(hunt, "choice", 1).Next == "not_tonight" && hunt.Nodes.Single(n => n.Id == "not_tonight").Choices.All(c => c.Abort),
            "Letting her run is not a return to the woods another night.");
        check(After(hunt, offered, "choice", 2).First().Has("delamere.closed"), "Trk_Delamere_Claimed: claiming her as a catch is not a hard no.");
        check(Rules.Available(story, huntPage, Later(story, World(story, 3, "trickster.ever", P + "second_hunt_offered", "kyado.dead"), 24))
              && Rules.Available(story, huntLate, Later(story, World(story, 5, "trickster.ever", P + "second_hunt_offered"), 24)),
            "The second hunt has no page when Kyado is dead, or in Chapter 5.");
        // Trk_Delamere_Lie: a lie about her god must be taken back in her woods.
        var liar = Later(story, After(woods, lie, "want", 0).First(), 24);
        check(After(hunt, liar, "the_lie", 0).First().Has("delamere.committed") || Program.Walk(hunt, liar).Any(r => r.Has(P + "confessed") && r.Has("delamere.committed")),
            "Trk_Delamere_Lie: confessing does not lead to the catch.");
        var kept = After(hunt, liar, "the_lie", 1).First();
        check(kept.Has("delamere.closed") && kept.Has(P + "kept_the_lie") && !kept.Has("delamere.committed"),
            "Trk_Delamere_Lie: keeping the lie is not a hard no.");

        // After the commit: the day owed, and what came of the count.
        check(Rules.Available(story, owed, Later(story, caught, 72)) && After(owed, caught, "cold", 0).First().Has(P + "first_frost"),
            "The day owed is not collected after the commit.");
        check(Rules.Available(story, village, Later(story, given, 24, 5)) && !Rules.Available(story, village, Later(story, given, 24, 3)),
            "What came of the count is not a Chapter 5 beat.");

        // The beats around the fire: the god's answer over her seal, the names, the poachers, the brace.
        var deadeye = S(P + "woken.old_deadeye");
        var names = S(P + "woken.names");
        var poachers = S(P + "woken.poachers");
        var hide = S(P + "woken.hide");
        check(deadeye.Requires.Contains(P + "white_stag_told") && Program.Walk(deadeye, Later(story, told, 48)).All(r => r.Has(P + "old_deadeye")),
            "Old Deadeye's house does not follow the white stag, or does not close.");
        var lieChapel = Later(story, lie, 48);
        check(Program.Walk(deadeye, lieChapel).Any(r => r.Has(P + "old_deadeye")) && deadeye.Nodes.Single(n => n.Id == "stag").Choices[0].Requires.Contains(P + "lied_erastil"),
            "The lie is not deepened in the chapel.");
        check(names.Requires.Contains(P + "feasting_table") && Program.Walk(names, Later(story, spoken, 48)).All(r => r.Has(P + "names_cut")),
            "The names on the crypt wall do not follow the feasting table.");
        var law = poachers.Nodes.Single(n => n.Id == "law").Choices;
        check(law[0].Set.Contains(P + "poachers.provost") && law[1].Set.Contains(P + "poachers.her_law") && law[2].Check?.Skill == "CheckBluff"
              && Program.Walk(poachers, Later(story, fed, 48)).Any(r => r.Has(P + "poachers.tricked"))
              && poachers.Nodes.Single(n => n.Id == "law_again").Choices.Count == 2,
            "Doe in fawn: whose law is not the Commander's choice, or a failed bluff has no plain answer.");
        check(hide.Requires.Contains("delamere.committed") && Rules.Available(story, hide, Later(story, caught, 48))
              && !Rules.Available(story, hide, Later(story, offered, 48)),
            "The brace is not an after-the-commit beat.");

        // Every page beat opens from its own gates.
        foreach (var s in own.Where(x => Rules.IsRemote(x) && !x.TricksterDevice))
        {
            var needs = s.Requires.Concat(s.RequiresAnyGroups.Select(g => g[0])).ToArray();
            var w = World(story, s.Chapters[0], new[] { "trickster", "trickster.ever", P + "returned", "delamere.started" }.Concat(needs).ToArray());
            check(Rules.Available(story, s, Later(story, w, s.DelayHours + 1)), "A Delamere page never opens: " + s.Id);
        }
        Console.WriteLine("PASS: Delamere Trickster (Trk_Delamere_*): the stag's call in three places, the run and the arrow, the bow, "
            + own.Count(s => !s.TricksterDevice) + " courtship beats, the second hunt and its no's, " + reactions.Length + " reactions and " + pages.Length + " pages.");
    }
}
