using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Mielarah, Trickster (Writer/handoffs/11-ROSTER-PLAN-2.md §2; F15): "Zyphus picks the nearest".
// One block per rules test (Trk_Mielarah_*): the shape of each hook, the reading of the curse's rule at her table, the
// bosun posted at her elbow, the hanging (the curse takes the man on the rope), the storm (word left for a survivor),
// the landfall and the charter, the canon kill at Colyphyr, and the Chapter 5 courtship on her presence (mielarah_deck):
// every beat reachable, the commit only in flight, the quarterdeck only after it, and her soft no kept soft.
internal static class MielarahTricksterTests
{
    private const string P = "mielarah.trickster.";
    private const string D = "mielarah.deck.";
    private const string TavernList = "5cb721033c29ca04dab453de7c13b607";
    private const string TavernReturn = "2437e93b015b82d47900667402e01a9c";
    private const string ColyphyrList = "ef7be5c16b82f734096f5a5f9fd497ce";
    private const string ColyphyrReturn = "2f275eb40f32b5c4996bc077b597e5e3";
    private const string Unit = "9d9c523bc2b17434bb66df212b127187";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Fye = "0f12118177d102f428a3b30b15b132eb";
    private const string Wilcer = "a380d926e92f70e429681eb9654478f9";
    private const string Smith = "15f754455d1d87c42a4e14df456d5415";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = chapter == 5 ? Drezen : "" };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Unit);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, int? chapter = null)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        if (chapter != null)
        {
            later.Chapter = chapter.Value;
            if (chapter.Value == 5) later.Area = Drezen;
        }
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var arithmetic = S(P + "tavern.arithmetic");
        var secondLook = S(P + "tavern.second_look");
        var repeat = S(P + "tavern.repeat");
        var charts = S(P + "tavern.charts");
        var captains = S(P + "tavern.captains");
        var minder = S(P + "tavern.minder");
        var charter = S(P + "tavern.charter");
        var landfall = S(P + "colyphyr.landfall");
        var landfallLetter = S(P + "colyphyr.letter");
        var rope = S(P + "raid.rope");
        var rock = S(P + "raid.rock");
        var word = S(P + "storm.word");
        var survivor = S(P + "storm.survivor");
        var charterLetter = S(P + "charter.letter");
        var dream = S(P + "spade.dream");
        var cargo = S(D + "cargo");
        var wheel = S(D + "wheel");
        var quarterdeck = S(D + "quarterdeck");
        var morning = S(D + "morning");
        var pages = story.Scenes.Where(s => s.Relationship == "mielarah" && s.Owner == "MielarahEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "mielarah" && s.Reaction).ToArray();
        var own = story.Scenes.Where(s => s.Relationship == "mielarah" && !s.Reaction && s.Owner == "Mielarah").ToArray();
        var deck = own.Where(s => s.Id.StartsWith(D, StringComparison.Ordinal)).ToArray();
        Choice Choice(Scene scene, string node, int index) => scene.Nodes.Single(n => n.Id == node).Choices[index];
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            var chosen = Choice(scene, node, index);
            var hits = Program.Walk(scene, w).Where(r => chosen.Set.All(r.Has) && (chosen.Set.Length > 0 || r.Has(scene.Id))).ToList();
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        // Plays every available Mielarah scene forward (Chapter 5, in Drezen) and reports whether a flag is ever held.
        bool Reaches(Snapshot start, string flag, int chapter = 5)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 20 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    if (from.Has(flag)) return true;
                    var w = Later(story, from, 200, chapter);
                    foreach (var scene in own.Where(s => !s.Id.EndsWith(".arcade", StringComparison.Ordinal) && Rules.Available(story, s, w)))
                        foreach (var r in Program.Walk(scene, w))
                        {
                            if (r.Has(flag)) return true;
                            if (seen.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                        }
                }
                frontier = next.Take(400).ToList();
            }
            return false;
        }

        // Shape and hooks.
        var rel = story.Relationships["mielarah"];
        check(rel.StartedFlag == "mielarah.started" && rel.ClosedFlag == "mielarah.closed" && rel.CommittedFlag == "mielarah.committed"
              && rel.UnavailableFlags.OrderBy(f => f).SequenceEqual(new[] { "mielarah.dead", "mielarah.expelled", "mielarah.killed_at_colyphyr" })
              && rel.UnavailableOverrides.Count == 1 && rel.UnavailableOverrides["mielarah.dead"] == P + "returned"
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "raid", "storm" })
              && rel.TricksterAccess["raid"].Device == P + "raid.rope" && rel.TricksterAccess["storm"].Device == P + "storm.word",
            "Mielarah's relationship does not match the plan (killed at Colyphyr must never be overridden).");
        foreach (var s in new[] { arithmetic, secondLook, repeat, charts, captains, minder, charter })
            check(s.AnswerLists.SequenceEqual(new[] { TavernList }) && s.NativeReturnCue == TavernReturn && s.ContactUnit == null
                  && s.Forbids.Contains("mielarah.voyage_begun") && s.MaxChapter == 4,
                "A table scene is not inline at the Bad Luck, before the voyage: " + s.Id);
        foreach (var s in new[] { arithmetic, secondLook, minder })
            check(s.TricksterDevice && s.TricksterState == "raid", "A device's preparation is not flagged for the raid state: " + s.Id);
        check(landfall.AnswerLists.SequenceEqual(new[] { ColyphyrList }) && landfall.NativeReturnCue == ColyphyrReturn
              && landfall.Requires.Contains("mielarah.arrived"), "The landfall is not inline on her Colyphyr list.");
        check(Choice(arithmetic, "list", 0).Mythic == "PlayerIsTrickster" && Choice(arithmetic, "list", 0).Requires.Contains("trickster.perception_tier1")
              && Choice(arithmetic, "list", 1).Check?.Skill == "SkillLoreReligion" && Choice(arithmetic, "list", 2).Check?.Skill == "SkillPerception",
            "The reading is not keyed to the Trickster's sight, Lore (Religion) and Perception.");
        check(rope.TricksterDevice && rope.TricksterState == "raid" && Rules.IsRemote(rope) && rope.Requires.Contains(P + "primed.minder"),
            "The hanging's payoff is not the prepared device.");
        check(word.TricksterDevice && word.TricksterState == "storm", "The storm's word is not the storm device.");
        check(deck.All(s => s.ContactUnit == Unit && s.Areas.SequenceEqual(new[] { Drezen }) && s.Chapters.SequenceEqual(new[] { 5 })
                            && (s.InteractionHub == "mielarah.presence" || s.InteractionHub == "mielarah.presence.arcade")
                            && s.Forbids.Contains("mielarah.closed")),
            "A Chapter 5 beat is not on her presence in Drezen.");
        foreach (var s in deck.Where(s => !s.Id.EndsWith(".arcade", StringComparison.Ordinal)))
        {
            var twin = S(s.Id + ".arcade");
            check(s.Forbids.Contains(twin.Id) && twin.Forbids.Contains(s.Id) && twin.Requires.Contains("mielarah.presence.failed")
                  && twin.InteractionHub == "mielarah.presence.arcade", "A beat has no arcade twin: " + s.Id);
        }
        var hub = story.Presences["mielarah.presence"];
        var arcade = story.Presences["mielarah.presence.arcade"];
        foreach (var p in new[] { hub, arcade })
            check(p.Unit == Unit && p.Area == Drezen && p.Mode == "spawn-copy" && p.Dialog == "hub" && p.MinChapter == 5 && p.MaxChapter == 5
                  && p.At?.NearUnit != Fye && p.At?.NearUnit != Wilcer && p.At?.NearUnit != Smith && p.At!.Distance >= 2f,
                "A presence is misplaced or at a crowded anchor.");
        check(hub.Forbids.Contains("mielarah.presence.failed") && arcade.Requires.Contains("mielarah.presence.failed"),
            "The arcade is not the stall's fallback.");
        // Coexistence: no scene needs another woman dead, gone or closed.
        foreach (var s in story.Scenes.Where(s => s.Relationship == "mielarah" && !s.Reaction))
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)))
                check(!(key.EndsWith(".closed", StringComparison.Ordinal) && key != "mielarah.closed")
                      && !((key.EndsWith("_dead", StringComparison.Ordinal) || key.EndsWith(".dead", StringComparison.Ordinal)) && !key.StartsWith("mielarah.", StringComparison.Ordinal)),
                    "Mielarah needs someone else dead or closed: " + s.Id + " " + key);
        // Every gate of hers is produced somewhere in the route.
        var produced = new HashSet<string>(story.Scenes.Where(s => s.Relationship == "mielarah").SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set));
        foreach (var s in own)
            foreach (var key in s.Requires.Where(k => k.StartsWith(P, StringComparison.Ordinal) || k.StartsWith(D, StringComparison.Ordinal)))
                check(produced.Contains(key) || story.Derived.ContainsKey(key), "A gate has no producer: " + s.Id + " requires " + key);
        check(!produced.Contains("mielarah.committed") || wheel.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains("mielarah.committed")),
            "The commit is not set in flight.");
        check(own.Where(s => s != wheel && !s.Id.StartsWith(D + "wheel", StringComparison.Ordinal))
                 .SelectMany(s => s.Nodes).SelectMany(n => n.Choices).All(c => !c.Set.Contains("mielarah.committed")),
            "Something other than holding the wheel commits.");

        // Trk_Mielarah_Pattern: the reading at her table, after the Gravedragger story.
        var table = World(story, 4, "trickster", "mielarah.told_curse", "mielarah.met");
        check(Rules.Available(story, arithmetic, table) && !Rules.Available(story, arithmetic, World(story, 4, "trickster", "mielarah.met")),
            "Trk_Mielarah_Pattern: the reading is shut, or opens before she has told the curse.");
        check(!Rules.Available(story, arithmetic, World(story, 4, "trickster", "mielarah.told_curse", "mielarah.voyage_begun")),
            "Trk_Mielarah_Pattern: the table opens after the voyage has begun.");
        var read = After(arithmetic, table, "rule", 0).First();
        check(read.Has(P + "primed.pattern") && read.Has("mielarah.started"), "Trk_Mielarah_Pattern: reading the rule does not prime.");
        var sight = World(story, 4, "trickster", "mielarah.told_curse", "trickster.perception_tier1");
        check(After(arithmetic, sight, "sight", 0).Any(r => r.Has(P + "primed.pattern")), "Trk_Mielarah_Pattern: the Trickster's sight does not read the rule.");
        // Trk_Mielarah_SecondLook: both readings failed; the Commander sits nearest and bleeds for it.
        var missed = After(arithmetic, table, "fail_both", 0).First();
        check(missed.Has(P + "pattern_missed") && !missed.Has(P + "primed.pattern"), "Trk_Mielarah_SecondLook: failing both checks is not recorded.");
        var again = Later(story, missed, 8);
        check(Rules.Available(story, secondLook, again), "Trk_Mielarah_SecondLook: the fallback is shut.");
        var cut = After(secondLook, again, "rule", 0).First();
        check(cut.Has(P + "primed.pattern") && cut.Has(P + "cost.cut"), "Trk_Mielarah_SecondLook: the evening at her elbow costs nothing, or reads nothing.");

        // Trk_Mielarah_Minder: after she is hired, before the portal; truth or a lie (a Ledger secret).
        var hired = World(story, 4, "trickster", "mielarah.told_curse", P + "primed.pattern", "mielarah.hired");
        check(Rules.Available(story, minder, hired) && !Rules.Available(story, minder, World(story, 4, "trickster", P + "primed.pattern")),
            "Trk_Mielarah_Minder: the bosun is posted without her being hired, or not at all.");
        var told = After(minder, hired, "order", 0).First();
        var lied = After(minder, hired, "order", 1).First();
        check(told.Has(P + "primed.minder") && told.Has(P + "minder.told") && !told.Has("trickster.secret.mielarah_oskel"),
            "Trk_Mielarah_Minder: the truth does not post him.");
        check(lied.Has(P + "primed.minder") && lied.Has(P + "minder.lied") && lied.Has("trickster.secret.mielarah_oskel"),
            "Trk_Mielarah_Minder: the lie is not a Ledger secret.");

        // Trk_Mielarah_Raid: the curse takes the man on the rope; without the bosun, canon fate stands.
        var hanged = World(story, 4, "trickster.ever", "mielarah.dead", P + "primed.pattern", P + "primed.minder", P + "minder.told");
        check(!Rules.Available(story, rope, hanged) && Rules.Available(story, rope, Later(story, hanged, 25)) == Rules.Available(story, rope, Later(story, hanged, 25)),
            "Trk_Mielarah_Raid: delay check.");
        check(Rules.Available(story, rope, World(story, 4, "trickster.ever", "mielarah.dead", "mielarah.dead.latched", P + "primed.minder", P + "minder.told")),
            "Trk_Mielarah_Raid: the hanging's payoff is shut.");
        var alive = After(rope, World(story, 4, "trickster.ever", "mielarah.dead", "mielarah.dead.latched", P + "primed.minder", P + "minder.told"), "oskel", 0).First();
        check(alive.Has(P + "returned") && alive.Has(P + "cost.oskel") && alive.Has(P + "cost.noticed"),
            "Trk_Mielarah_Raid: the return does not cost the bosun, or the Gravedragger does not notice.");
        check(After(rope, World(story, 4, "trickster.ever", "mielarah.dead", "mielarah.dead.latched", P + "primed.minder", P + "minder.lied"), "lied", 0)
                  .All(r => r.Has("trickster.secret.mielarah_oskel.known.mielarah")),
            "Trk_Mielarah_Raid: she does not work out the lie.");
        check(Choice(rope, "raid", 1).Alignment?.Direction == "Evil", "The unrepentant raid is not an evil answer.");
        var unprepared = World(story, 4, "trickster.ever", "mielarah.dead", "mielarah.dead.latched", P + "primed.pattern");
        check(!Rules.Available(story, rope, unprepared) && !Reaches(Later(story, unprepared, 100, 5), "mielarah.committed"),
            "Trk_Mielarah_LateAfterDeath: a hanging without the bosun at her elbow is defied.");
        check(Rules.Available(story, rock, Later(story, alive, 49)), "Trk_Mielarah_Rock: the eleven on the rock never come up.");
        check(Reaches(Later(story, alive, 10, 5), "mielarah.committed"), "Trk_Mielarah_Raid: no road to the commit.");

        // Trk_Mielarah_Storm: her curse spares her; word left in the aeronauts' taverns brings her back.
        var storm = World(story, 4, "trickster.ever", "mielarah.storm_crash", "mielarah.storm_crash.latched", "mielarah.told_curse", P + "primed.minder", P + "minder.told", P + "primed.pattern");
        check(Rules.Available(story, word, Later(story, storm, 1)), "Trk_Mielarah_Storm: the word is shut.");
        var sent = After(word, storm, "known", 0).First();
        check(sent.Has(P + "primed.word") && Rules.Available(story, survivor, Later(story, sent, 48)), "Trk_Mielarah_Storm: the survivor does not follow the word.");
        var survived = After(survivor, Later(story, sent, 48), "hatch", 0).First();
        check(survived.Has(P + "returned") && survived.Has(P + "cost.ship_lost") && survived.Has(P + "cost.oskel"), "Trk_Mielarah_Storm: the return costs nothing.");
        check(Reaches(Later(story, survived, 10, 5), "mielarah.committed"), "Trk_Mielarah_Storm: no road to the commit.");
        var unread = World(story, 4, "trickster.ever", "mielarah.storm_crash", "mielarah.storm_crash.latched", "mielarah.told_curse");
        check(After(word, unread, "unknown", 1).Any(r => r.Has(P + "primed.word") && r.Has(P + "cost.late")) && Choice(word, "unknown", 1).Crusade?.Resource == "Finances",
            "Trk_Mielarah_PreparedStorm: the unread storm has no late road.");

        // Trk_Mielarah_Arrived: the landfall at Colyphyr, or her letter if the Commander left without a word.
        var arrived = World(story, 4, "trickster.ever", "trickster", "mielarah.arrived", P + "primed.pattern");
        check(Rules.Available(story, landfall, arrived), "Trk_Mielarah_Arrived: the landfall is shut.");
        var invited = After(landfall, arrived, "close", 0).First();
        check(invited.Has(P + "landfall") && invited.Has(P + "contact"), "Trk_Mielarah_Arrived: the invitation does not bring her north.");
        check(Rules.Available(story, landfallLetter, Later(story, arrived, 73)), "Trk_Mielarah_Arrived: the missed landfall has no letter.");
        check(Reaches(Later(story, invited, 10, 5), "mielarah.committed"), "Trk_Mielarah_Arrived: no road to the commit.");

        // Trk_Mielarah_Charter: another captain; the charter at her table or her letter in Chapter 5.
        var charterTable = World(story, 4, "trickster", P + "primed.pattern");
        check(Rules.Available(story, charter, charterTable), "Trk_Mielarah_Charter: the charter is shut.");
        var chartered = After(charter, charterTable, "code", 0).First();
        var kerz = Later(story, chartered, 10, 5);
        kerz.Flags.Add("captain.kerz");
        Rules.Complete(story, kerz);
        check(kerz.Has(P + "contact") && Reaches(kerz, "mielarah.committed"), "Trk_Mielarah_Charter: no road to the commit.");
        check(Rules.Available(story, charterLetter, World(story, 5, "trickster.ever", P + "primed.pattern", "captain.nocticula")),
            "Trk_Mielarah_Charter: the charter letter is shut.");

        // Trk_Mielarah_KilledAtColyphyr: canon fate stands.
        var killed = World(story, 5, "trickster.ever", "mielarah.arrived", "mielarah.killed_at_colyphyr", P + "landfall");
        check(own.All(s => !Rules.Available(story, s, killed)) && !story.Presences["mielarah.presence"].Forbids.Contains("x")
              && story.Presences["mielarah.presence"].Forbids.Contains("mielarah.killed_at_colyphyr"),
            "Trk_Mielarah_KilledAtColyphyr: a scene or her presence survives the Commander's own kill.");

        // Trk_Mielarah_Commit: in flight she lets go of the wheel; holding the course is the yes, turning for home her soft no.
        var ready = World(story, 5, "trickster.ever", P + "landfall", "mielarah.started", D + "docked", D + "reckoned", D + "flown", D + "corrected", D + "market");
        check(Rules.Available(story, wheel, ready), "Trk_Mielarah_Commit: the wheel is shut.");
        var held = After(wheel, ready, "letgo", 0).First();
        check(held.Has("mielarah.committed"), "Trk_Mielarah_Commit: holding the course does not commit.");
        var home = After(wheel, ready, "letgo", 1).First();
        check(home.Has(P + "declined") && !home.Has("mielarah.committed") && !home.Has("mielarah.closed"),
            "Trk_Mielarah_Declined: turning for home is not her soft no.");
        check(!Rules.Available(story, wheel, Later(story, home, 100)), "Her soft no is asked again (no second ask).");
        check(After(wheel, ready, "kiss_first", 0).Any(r => r.Has(D + "quarterdeck")), "The quarterdeck does not follow the commit.");
        check(!Rules.Available(story, quarterdeck, Later(story, ready, 100)) && Rules.Available(story, quarterdeck, Later(story, held, 13)),
            "The quarterdeck is not gated on the commit.");
        var night = After(wheel, ready, "kiss_first", 0).First(r => r.Has(D + "quarterdeck"));
        check(Rules.Available(story, morning, Later(story, night, 7)), "The morning does not follow the night.");
        var dawn = After(morning, Later(story, night, 7), "shield", 0).First();
        check(dawn.Has(P + "cost.noticed") && dawn.Has(D + "morning"), "Trk_Mielarah_Morning: the Gravedragger does not notice.");
        check(Rules.Available(story, dream, Later(story, dawn, 25)), "The spade dream never comes.");

        // Every Chapter 5 beat opens once its own gates are held.
        foreach (var s in deck.Where(s => !s.Id.EndsWith(".arcade", StringComparison.Ordinal)))
        {
            var needs = s.Requires.Where(k => k != P + "contact").ToArray();
            var extra = new List<string> { "trickster.ever", P + "landfall", "mielarah.started" };
            if (needs.Contains(P + "cost.ship_lost") || needs.Contains(P + "cost.oskel")) extra.Add(P + "returned");
            if (needs.Contains(D + "declined") || s.Id == D + "after_no") extra.Add(P + "declined");
            if (needs.Contains("mielarah.trickster.charter")) { extra.Remove(P + "landfall"); extra.Add("captain.kerz"); extra.Add("captain.kerz"); }
            if (s.Id == D + "other_voyage") { extra.Remove(P + "landfall"); extra.Add("captain.kerz"); }
            if (s.Id == D + "fourth") extra.Add(P + "storm.owned");
            var w = World(story, 5, extra.Concat(needs).Distinct().ToArray());
            check(Rules.Available(story, s, Later(story, w, s.DelayHours + 1)), "A Chapter 5 beat never opens: " + s.Id);
        }

        // Reactions and pages.
        check(reactions.Length == 3 && reactions.All(r => r.Nodes.Count == 1)
              && reactions.Where(r => r.Owner == "Lann").All(r => r.Forbids.Contains("lann.dead") && r.Forbids.Contains("lann.kicked_out"))
              && reactions.Where(r => r.Owner == "Woljif").All(r => r.Forbids.Contains("woljif.dead") && r.Forbids.Contains("woljif.kicked_out"))
              && reactions.Select(r => r.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Lann", "Woljif" }),
            "The reactions are not exactly Lann and Woljif behind their guards.");
        check(pages.Length == 2 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null))),
            "The epilogue pages carry effects or are missing.");
        check(story.Derived[P + "late_committed"].Single().SequenceEqual(new[] { "trickster.ever", D + "flown" })
              && story.Derived["mielarah.harem.eligible"].Count == 2, "The late commit or the harem eligibility is not declared.");
        Console.WriteLine("PASS: Mielarah Trickster (Trk_Mielarah_*): the rule read, the bosun, the hanging, the storm, the landfall, the charter, "
                          + deck.Length / 2 + " Chapter 5 beats and the wheel.");
    }
}
