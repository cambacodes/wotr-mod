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
        // Edge-exact (quality pass Q6, HOW): reach the node with this choice open, then take exactly that choice from there.
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            var chosen = Choice(scene, node, index);
            Snapshot? at = null;
            Program.Walk(scene, w, (page, st) => { if (at == null && page == node && Rules.Match(chosen.Requires, chosen.Forbids, st)) at = Program.Copy(st); });
            check(at != null, "Node not reached with its choice open: " + scene.Id + "/" + node + "[" + index + "]");
            if (at == null) return new List<Snapshot> { w };
            var edge = new Scene { Id = scene.Id, Relationship = scene.Relationship, Owner = scene.Owner,
                                   Nodes = new[] { new Node { Id = "__edge", Choices = new List<Choice> { chosen } } }.Concat(scene.Nodes).ToList() };
            var hits = Program.Walk(edge, at).ToList();
            check(hits.Count > 0 && chosen.Set.All(hits[0].Has), "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits.Count > 0 ? hits : new List<Snapshot> { w };
        }
        HashSet<string> Pages(Scene scene, Snapshot w)
        {
            var seen = new HashSet<string>();
            Program.Walk(scene, w, (page, _) => seen.Add(page));
            return seen;
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
        // Quality pass Q6 (COX): the ledger allocates Kyado alone; Ulbrig's and Woljif's lines are retired by gating (ids kept).
        check(reactions.Where(r => r.Owner == "Kyado").Count() == 2 && reactions.All(r => r.Nodes.Count == 1)
              && reactions.Where(r => r.Owner == "Kyado").All(r => r.Forbids.Contains("kyado.dead")),
            "The reactions are not Kyado (twice) behind his guard.");
        var anyReturned = World(story, 5, "trickster.ever", P + "returned", P + "cost.limp", "ulbrig.in_party", "delamere.started");
        check(reactions.Where(r => r.Owner != "Kyado").All(r => !Rules.Available(story, r, Later(story, anyReturned, 100))
                                                           && !Rules.Available(story, r, Later(story, World(story, 3, "trickster.ever", P + "returned", P + "cost.limp", "ulbrig.in_party"), 100))),
            "A retired reactor (Ulbrig, Woljif) still speaks.");
        check(pages.Length == 7 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null))),
            "The epilogue pages carry effects or are missing.");
        check(story.Derived[P + "late_committed"].Length == 3
              && story.Derived[P + "late_committed"].All(g => g.Contains("trickster.ever") && g.Contains(P + "second_hunt_offered"))
              && story.Derived[P + "late_committed"].Select(g => g.Last()).OrderBy(x => x).SequenceEqual(new[] { P + "confessed", P + "told_both", P + "told_truth" })
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

        // Quality pass Q6 (INT): the opened body is read from the tomb's own outcomes, not from starting the book event.
        var visitedUnopened = World(story, 3, "trickster", "trickster.ever", "delamere.tomb_visited", P + "primed");
        var cryptPages = Pages(crypt, visitedUnopened);
        check(cryptPages.Contains("body_sealed") && !cryptPages.Contains("body_open"), "A tomb visited but never opened is shown open.");
        // PP10 (Sol CAN/BEL): the knife openings count as opened (a lid closed again is still a broken seal); a whole seal
        // breaks on the page before she rises; the crypt walk reaches the seal only from an untouched tomb.
        bool SealBreaks(Snapshot w) => Pages(crypt, w).Contains("rise_sealed");
        check(SealBreaks(visitedUnopened) && !cryptPages.Contains("rise") && crypt.Nodes.Single(n => n.Id == "rise_sealed").Text.Contains("the seal goes"),
            "Trk_Delamere_Seal: the whole seal is never broken on the page.");
        check(!drezen.Nodes.Any(n => n.Id == "rise_sealed") && Pages(drezen, World(story, 3, "trickster", "trickster.ever", "delamere.remains_finished", "delamere.tomb_visited")).Contains("rise"),
            "Trk_Delamere_Seal: the open Drezen stone breaks a seal.");
        foreach (var opened in new[] { "delamere.erastil_answered", "delamere.tomb_opened_forced", "delamere.tomb_opened_peaceful",
                                       "delamere.tomb_opened_knife", "delamere.tomb_opened_knife_crack",
                                       "delamere.tomb_opened_prayer", "delamere.tomb_opened_dispelled" })
        {
            var o = World(story, 3, "trickster", "trickster.ever", "delamere.tomb_visited", opened);
            var op = Pages(crypt, o);
            check(o.Has("delamere.tomb_opened") && op.Contains("body_open") && !op.Contains("body_sealed") && !SealBreaks(o),
                "An opened tomb is shown sealed: " + opened);
        }
        foreach (var s in own)
            foreach (var n in s.Nodes)
                check(!n.Text.Contains("breastplate", StringComparison.Ordinal) && !n.Text.Contains("stag-hide over", StringComparison.Ordinal),
                    "Her relic armour is described on her, though the Commander may hold it: " + s.Id + "/" + n.Id);

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
        // PP10 (Sol CAN): the Drezen waking follows the relics; the antler bow is in her hands only if it is not on the Commander's back.
        var remainsHeld = World(story, 3, "trickster", "trickster.ever", "delamere.remains_finished", "delamere.tomb_visited", "delamere.relics_taken", "delamere.bow_held");
        check(Pages(drezen, remains).Contains("body_drezen") && !Pages(drezen, remains).Contains("body_drezen_taken")
              && Pages(drezen, remainsHeld).Contains("body_drezen_taken") && !Pages(drezen, remainsHeld).Contains("body_drezen")
              && !drezen.Nodes.Single(n => n.Id == "body_drezen_taken").Text.Contains("antler bow")
              && Pages(drezen, remainsHeld).Contains("taken_held") && !Pages(drezen, remainsHeld).Contains("in_hands")
              && After(drezen, remainsHeld, "taken_held", 0).First().Has(P + "bow_returned"),
            "Trk_Delamere_Drezen: the chapel puts the Commander's bow back in her hands without taking it.");
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
        // NM1: the count's delivery carries the first meat; a save between them still gets the meat on its own.
        check(given.Has(P + "first_meat") && !given.Has(P + "feasting_table") && !Rules.Available(story, meat, Later(story, given, 24)),
            "Trk_Delamere_SpineFolded: the count does not carry the hunter eats last.");
        given = World(story, 3, "trickster.ever", P + "returned", "delamere.started", P + "cost.limp", P + "cost.hunt_owed", P + "counted", P + "village.given");
        check(Rules.Available(story, meat, Later(story, given, 24)), "The hunter eats last does not follow the count.");
        var fed = After(meat, given, "law", 0).First();
        check(Rules.Available(story, table, Later(story, fed, 24)) && Rules.Available(story, lessons, Later(story, fed, 24)),
            "The feasting table or the prior's lessons do not follow the hunt.");
        var spoken = After(table, fed, "judge", 0).First();
        check(spoken.Has(P + "kyado.spoken_for") && After(table, fed, "judge", 1).First().Has(P + "kyado.judged"),
            "Kyado's judgment is not the Commander's to speak.");
        var mourned = World(story, 3, "trickster.ever", P + "returned", P + "first_meat", "kyado.dead");
        check(After(table, mourned, "kyado_cairn", 0).First().Has(P + "kyado.mourned"), "A dead Kyado is not mourned.");
        // NM1: the table's delivery carries the white stag; a save between them still gets the white stag on its own.
        check(spoken.Has(P + "white_stag_told") && !Rules.Available(story, whiteStag, Later(story, spoken, 24)),
            "Trk_Delamere_SpineFolded: the feasting table does not carry the white stag.");
        var tabled = World(story, 3, "trickster.ever", P + "returned", "delamere.started", P + "cost.limp", P + "cost.hunt_owed", P + "counted", P + "village.given",
            P + "first_meat", P + "feasting_table", P + "kyado.spoken_for");
        check(Rules.Available(story, whiteStag, Later(story, tabled, 24)) && !Rules.Available(story, red, Later(story, tabled, 24)),
            "The white stag does not come between the table and Red.");
        var told = After(whiteStag, tabled, "week", 0).First();
        check(told.Has(P + "white_stag_told") && Rules.Available(story, red, Later(story, told, 24)), "Red does not follow the white stag.");
        var truth = After(red, told, "question", 0).First();
        var lie = After(red, told, "question", 1).First();
        check(truth.Has(P + "told_truth") && lie.Has(P + "lied_erastil") && After(red, told, "question", 2).First().Has(P + "told_both"),
            "The truth about who woke her is not the Commander's choice.");
        // NM1: Red's delivery carries her woods; a save between them still gets her woods on its own.
        check(!Rules.Available(story, woods, Later(story, truth, 24)), "Trk_Delamere_SpineFolded: Red does not carry her woods.");
        var redSeen = Program.Copy(told); redSeen.Flags.Add(P + "red_blood"); redSeen.Flags.Add(P + "told_truth"); redSeen.Times[P + "red_blood"] = redSeen.Hour;
        truth = Later(story, redSeen, 0);
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
        // Quality pass Q6 (BEL): a count made after the Abyss (woken.count_late) never gets the Abyss-absence report.
        var countLate = S(P + "woken.count_late");
        var back5 = World(story, 5, "trickster.ever", P + "returned", "delamere.started", P + "cost.limp", P + "cost.hunt_owed");
        check(!Rules.Available(story, count, back5) && Rules.Available(story, countLate, back5) && !Rules.Available(story, countLate, back),
            "The count is not split by chapter.");
        var givenLate = After(countLate, back5, "unwilling", 0).First();
        check(givenLate.Has(P + "village.given") && givenLate.Has(P + "counted_after_the_abyss") && !Rules.Available(story, village, Later(story, givenLate, 48)),
            "A count made after the Abyss still reports a season of the Commander's absence.");

        // Quality pass Q6 (VOI): Red answers what the Commander actually told her.
        foreach (var (q, exit) in new[] { (0, "time_truth"), (1, "time_lie"), (2, "time_both") })
        {
            var said = After(red, told, "question", q).First();
            var rp = new HashSet<string>();
            Program.Walk(red, told, (page, st) => { if (page == "wants" && Rules.Match(Choice(red, "wants", 3 + q).Requires, Choice(red, "wants", 3 + q).Forbids, st)) rp.Add("ok"); });
            check(Choice(red, "wants", 3 + q).Next == exit && !Rules.Match(Choice(red, "wants", 0).Requires, Choice(red, "wants", 0).Forbids, said) && rp.Contains("ok"),
                "Red's parting line does not follow the answer given: " + exit);
        }
        check(!red.Nodes.Single(n => n.Id == "time_lie").Text.Contains("did not lie", StringComparison.Ordinal), "She praises a liar's honesty.");

        // Quality pass Q6 (INT): the romance pages need a surviving Commander; an unreversed sacrifice has its own page.
        var epCaught = S(P + "epilogue.caught"); var epLate = S(P + "epilogue.late"); var epSac = S(P + "epilogue.sacrifice");
        var wed6 = World(story, 6, "trickster.ever", "delamere.committed");
        var lost6 = World(story, 6, "trickster.ever", "delamere.committed", "sacrifice");
        var back6 = World(story, 6, "trickster.ever", "delamere.committed", "sacrifice", "ending.trickster");
        check(Rules.Available(story, epCaught, wed6) && !Rules.Available(story, epCaught, lost6) && Rules.Available(story, epSac, lost6)
              && (!back6.Has("trickster.commander_back") || Rules.Available(story, epCaught, back6) && !Rules.Available(story, epSac, back6))
              && !Rules.Available(story, epSac, wed6), "A sacrificed Commander still runs at the first frost.");
        var lateLost6 = World(story, 6, "trickster.ever", P + "second_hunt_offered", P + "told_truth", "sacrifice");
        check(!Rules.Available(story, epLate, lateLost6) && Rules.Available(story, epSac, lateLost6), "The late page survives an unreversed sacrifice.");

        // Quality pass Q6 (CAN): the god answered the Commander at her seal only if the Commander heard it; otherwise Haddo guesses.
        var dy = S(P + "woken.old_deadeye");
        var seal = dy.Nodes.Single(n => n.Id == "seal").Choices;
        var chapelTold = Later(story, told, 48);
        var answered = Program.Copy(chapelTold); answered.Flags.Add("delamere.erastil_answered");
        check(!Pages(dy, chapelTold).Contains("stag_seen") && Pages(dy, chapelTold).Contains("stag_haddo")
              && Pages(dy, answered).Contains("stag_seen") && !Pages(dy, answered).Contains("stag_haddo")
              && seal[0].Forbids.Contains(P + "white_stag_told") && !dy.Nodes.Where(n => n.Id != "seal").Any(n => n.Text.Contains("Every time", StringComparison.Ordinal)),
            "Old Deadeye's house still tells an invented history of answered pilgrims.");
        // NM1 (coordinator allocation exception; supersedes Q6 r2): no visit is a mod-menu read any more; every one arrives at a rest.
        check(mine.All(s => !s.ManualOnly) && own.Where(s => Rules.IsRemote(s)).All(Rules.IsMailbagLetter),
            "Trk_Delamere_RestDelivery: a Delamere visit is still read only from the mod menu.");
        // NM1: the spine arrives as three deliveries, each carrying the next visit: the count with the first meat, the table with
        // the white stag, Red with her woods. Every folded path reaches the next visit, nothing arrives twice, no page strands.
        var spineCount = World(story, 3, "trickster", "trickster.ever", P + "returned", "delamere.started");
        var firstDelivery = Program.Walk(count, spineCount);
        check(firstDelivery.Count > 0 && firstDelivery.All(r => r.Has(P + "counted") && r.Has(P + "first_meat"))
              && !Rules.Available(story, S(P + "woken.first_meat"), Later(story, firstDelivery[0], 200))
              && Rules.Available(story, S(P + "woken.feasting_table"), Later(story, firstDelivery[0], 24)),
            "Trk_Delamere_SpineFolded: the count does not carry the first meat, or it arrives twice.");
        var secondDelivery = Program.Walk(S(P + "woken.feasting_table"), Later(story, firstDelivery[0], 24));
        check(secondDelivery.Count > 0 && secondDelivery.All(r => r.Has(P + "feasting_table") && r.Has(P + "white_stag_told"))
              && secondDelivery.All(r => !Rules.Available(story, S(P + "woken.white_stag"), Later(story, r, 200)))
              && Rules.Available(story, S(P + "woken.red_blood"), Later(story, secondDelivery[0], 24)),
            "Trk_Delamere_SpineFolded: the feasting table does not carry the white stag, or it arrives twice.");
        var thirdDelivery = Program.Walk(S(P + "woken.red_blood"), Later(story, secondDelivery[0], 24));
        check(thirdDelivery.Count > 0 && thirdDelivery.All(r => r.Has(P + "red_blood"))
              && thirdDelivery.Any(r => r.Has(P + "second_hunt_offered")) && thirdDelivery.All(r => !Rules.Available(story, S(P + "woken.my_woods"), Later(story, r, 200))),
            "Trk_Delamere_SpineFolded: Red does not carry her woods to the second hunt.");
        // A save already between two visits still receives the next one on its own.
        check(Rules.Available(story, S(P + "woken.first_meat"), Later(story, World(story, 3, "trickster", "trickster.ever", P + "returned", P + "counted"), 24)),
            "Trk_Delamere_SpineFolded: a save between the count and the first meat loses the first meat.");
        // Q6 r2 (BEL): the limp is a kept cost the Commander can refuse; healing ends the hunt and has its own page.
        var healed = After(crypt, visited, "healed", 0).First();
        check(healed.Has(P + "leg_healed") && healed.Has("delamere.closed") && !healed.Has(P + "cost.limp") && !healed.Has(P + "cost.hunt_owed")
              && Rules.Available(story, S(P + "epilogue.healed"), World(story, 6, healed.Flags.ToArray()))
              && !Rules.Available(story, S(P + "epilogue.apart"), World(story, 6, healed.Flags.ToArray())),
            "Healing the leg is not a real choice with its consequence.");
        // Q6 r2 (BEL/CAN): nothing claims Kyado taught the call, and her scar is not from the canon ambush her armour turned.
        check(!whiteStag.Nodes.Any(n => n.Text.Contains("The boy says", StringComparison.Ordinal))
              && !S(P + "woken.old_deadeye").Nodes.Any(n => n.Text.Contains("The boy told you", StringComparison.Ordinal))
              && !hunt.Nodes.Any(n => n.Text.Contains("With the knives", StringComparison.Ordinal)),
            "A scene reports Kyado's lore the player may never have heard, or the knives that never pierced her armour.");

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

        // PP10 (Trk_Delamere_Bark, Chapter 4): the bark from the Abyss. "As you said" only for the Commander who told her the
        // witch's people went west; the old "I don't know" answer (which got "West.") is retired and its replacement gets
        // "Lost.". The Commander may cut an answer into the bark; what came of the count (Chapter 5) and her pages read it.
        var bark = S(P + "woken.bark");
        var abyss = Later(story, World(story, 4, "trickster.ever", P + "returned", "delamere.started", "storyteller.supplies"), 25);
        check(story.SeenCues["storyteller.supplies"].SequenceEqual(new[] { "459bf324a71c81c4ba5f3eead9ba42bb" })
              && !Rules.Available(story, bark, Later(story, World(story, 4, "trickster.ever", P + "returned", "delamere.started"), 25)),
            "Trk_Delamere_Bark: the bark comes before the Storyteller has offered to carry supplies.");
        check(Rules.IsRemote(bark) && bark.Kind == "letter" && bark.Chapters.SequenceEqual(new[] { 4 }) && !bark.ManualOnly && Rules.Available(story, bark, abyss)
              && !Rules.Available(story, bark, Later(story, World(story, 5, "trickster.ever", P + "returned", "delamere.started"), 25)),
            "Trk_Delamere_Bark: the bark is not her one Chapter 4 letter.");
        check(Pages(bark, abyss).Contains("letter_hills") && !Pages(bark, abyss).Contains("letter"),
            "Trk_Delamere_Bark: the letter says 'as you said' to a Commander who never said the witch went west.");
        var westAbyss = Later(story, World(story, 4, "trickster.ever", P + "returned", "delamere.started", "storyteller.supplies", P + "zanedra.told_fled"), 25);
        check(Pages(bark, westAbyss).Contains("letter") && !Pages(bark, westAbyss).Contains("letter_hills"), "Trk_Delamere_Bark: the west letter is lost.");
        var witch = table.Nodes.Single(n => n.Id == "finish").Choices;
        check(witch.Count == 4 && witch[2].Forbids.Contains("chapter_later") && witch[3].Next == "told_lost" && witch[3].Set.Contains(P + "zanedra.told_lost")
              && !witch[3].Set.Contains(P + "zanedra.told_fled") && witch[1].Set.Contains(P + "zanedra.told_fled"),
            "Trk_Delamere_Witch: 'I don't know' still gets her 'West.'");
        var barkRuns = Program.Walk(bark, abyss);
        check(barkRuns.Count(r => r.Has(P + "bark_letter")) == 2 && barkRuns.Count(r => r.Has(P + "bark_answered")) == 1
              && barkRuns.All(r => !Rules.Available(story, bark, Later(story, r, 48))),
            "Trk_Delamere_Bark: keeping and answering are not the two ways out, or the bark comes twice.");
        var countedHome = new[] { "trickster.ever", P + "returned", "delamere.started", P + "counted", P + "village.given", P + "bark_letter" };
        var answeredHome = Later(story, World(story, 5, countedHome.Concat(new[] { P + "bark_answered" }).ToArray()), 25);
        var keptHome = Later(story, World(story, 5, countedHome), 25);
        check(Pages(village, answeredHome).Contains("both_legs_bark") && !Pages(village, answeredHome).Contains("both_legs")
              && Program.Walk(village, answeredHome).Any(r => r.Has(P + "village_seen"))
              && Pages(village, keptHome).Contains("both_legs") && !Pages(village, keptHome).Contains("both_legs_bark"),
            "Trk_Delamere_Bark: what came of the count does not read the answer to her bark.");
        foreach (var id in new[] { "caught", "late", "apart" })
        {
            var node = S(P + "epilogue." + id).Nodes.Last();
            var withAnswer = World(story, 6, "trickster.ever", P + "returned", P + "bark_letter", P + "bark_answered");
            check(Rules.VisibleParagraphs(node, withAnswer).Any(t => t.Text.Contains("Both legs, so far"))
                  && !Rules.VisibleParagraphs(node, World(story, 6, "trickster.ever", P + "returned", P + "bark_letter")).Any(t => t.Text.Contains("Both legs, so far")),
                "Trk_Delamere_Bark: her page does not keep the answered bark: " + id);
        }

        // PP10 (Sol INT): the late commit needs the truth told, or the lie confessed in her woods; a kept lie gets the
        // unfinished page, never the late yes.
        var epLatePage = S(P + "epilogue.late");
        var epUnfinished = S(P + "epilogue.unfinished");
        string[] proposed = { "trickster.ever", P + "returned", "delamere.started", P + "red_blood", P + "second_hunt_offered" };
        var liarEnd = World(story, 6, proposed.Concat(new[] { P + "lied_erastil" }).ToArray());
        check(!liarEnd.Has(P + "late_committed") && !Rules.Available(story, epLatePage, liarEnd) && Rules.Available(story, epUnfinished, liarEnd),
            "Trk_Delamere_LateLie: an unconfessed lie still gets the late yes.");
        foreach (var said in new[] { P + "told_truth", P + "told_both" })
            check(World(story, 6, proposed.Concat(new[] { said }).ToArray()).Has(P + "late_committed")
                  && Rules.Available(story, epLatePage, World(story, 6, proposed.Concat(new[] { said }).ToArray())),
                "Trk_Delamere_LateLie: the late yes is lost for " + said);
        check(World(story, 6, proposed.Concat(new[] { P + "lied_erastil", P + "confessed" }).ToArray()).Has(P + "late_committed"),
            "Trk_Delamere_LateLie: a confessed lie loses the late yes.");
        // PP10 (Sol BEL): the Drezen waking moved her sarcophagus; the feasting table scrubs the bier and the floor.
        var tableDrezen = Later(story, World(story, 3, "trickster.ever", P + "returned", "delamere.started", P + "first_meat", P + "woke_in_drezen", P + "counted"), 25);
        var tableCrypt = Later(story, World(story, 3, "trickster.ever", P + "returned", "delamere.started", P + "first_meat", P + "counted"), 25);
        check(Pages(table, tableDrezen).Contains("stone_drezen") && !Pages(table, tableDrezen).Contains("stone")
              && Pages(table, tableCrypt).Contains("stone") && !Pages(table, tableCrypt).Contains("stone_drezen"),
            "Trk_Delamere_Table: the moved sarcophagus is scrubbed in the temple.");
        foreach (var node in table.Nodes.Where(n => n.Id != "stone"))
            check(!node.Text.Contains("sarcophagus", StringComparison.Ordinal) || node.Id == "stone_drezen",
                "Trk_Delamere_Table: a shared feasting-table node puts the moved sarcophagus back in the temple: " + node.Id);
        // PP10 (Sol CAN): the jester's line from Kyado is his own words alive, or his daybook when he is dead.
        var jester = S(P + "woken.jester");
        var jesterAlive = Later(story, World(story, 5, "trickster.ever", P + "returned", "delamere.started", P + "first_meat"), 49);
        var jesterDead = Later(story, World(story, 5, "trickster.ever", P + "returned", "delamere.started", P + "first_meat", "kyado.dead"), 49);
        check(Pages(jester, jesterAlive).Contains("kyado") && !Pages(jester, jesterAlive).Contains("kyado_book")
              && Pages(jester, jesterDead).Contains("kyado_book") && !Pages(jester, jesterDead).Contains("kyado")
              && Program.Walk(jester, jesterDead).Any(r => r.Has(P + "jester_seen")),
            "Trk_Delamere_Jester: a dead Kyado talks to her about the Commander.");

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
