using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Hepzamirah, Trickster (Writer/handoffs/trickster/hepzamirah.md; F06): "Who said a trick is less impressive the second time?"
// One block per spec rules test (Trk_Hepzamirah_*), the shape of each hook, and the courtship by the forge
// (hepzamirah_flesh): every beat reachable on its own path, the commit only after the courier and the pick, the nights
// only after the commit, and the Directive 12 cut on the threshold.
internal static class HepzamirahTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Labyrinth = "3538511f16d45f44f8249ff710777e2d";
    private const string Body = "bd2a925967b5f5f489f6da0b03236d03";
    private const string Ghost = "78549b805f0a63e41805cfe3e02e2ea8";
    private const string GhostList = "f457c8326a05b674c83a1c836636f99d";
    private const string ColyList = "995aaa29e772b594a966a2f133be702c";
    private const string Pick = "3b8021631cd1b7d4eb749601047a7bda";
    private const string P = "hepzamirah.trickster.";
    private const string F = "hepzamirah.trickster.flesh.";
    private const string B = "hepzamirah.trickster.bond.";

    private static Snapshot World(Story story, int chapter, params string[] flags) => WorldIn(story, Drezen, chapter, flags);

    private static Snapshot WorldIn(Story story, string area, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = area, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Body);
        state.AvailableContacts.Add(Ghost);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var offer = S(P + "colyphyr.offer");
        var second = S(P + "ghost.second_time");
        var first = S(P + "ghost.first_time");
        var late = S(P + "ghost.late_gather");
        var body = S(P + "ghost.body");
        var hounds = S(P + "body.hounds");
        var terms = S(P + "body.terms");
        var morning = S(F + "first_morning");
        var pick = S(F + "the_pick");
        var pages = story.Scenes.Where(s => s.Relationship == "hepzamirah" && s.Owner == "HepzamirahEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "hepzamirah" && s.Reaction).ToArray();
        var yard = story.Scenes.Where(s => s.Relationship == "hepzamirah" && s.InteractionHub == "hepzamirah.presence").ToArray();
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));
        List<Snapshot> Play(Scene scene, Snapshot w) => Program.Walk(scene, w).Where(r => r.Has(scene.Id)).ToList();
        Choice Choice(Scene scene, string node, int index) => scene.Nodes.Single(n => n.Id == node).Choices[index];
        // The outcomes of a walk that took the named choice of the named node.
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            var chosen = Choice(scene, node, index);
            var hits = new List<Snapshot>();
            foreach (var r in Program.Walk(scene, w))
                if (chosen.Set.All(r.Has) && (chosen.Set.Length > 0 || r.Has(scene.Id))) hits.Add(r);
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        // Plays every available Hepzamirah scene forward and reports whether a flag is ever held.
        var own = story.Scenes.Where(s => s.Relationship == "hepzamirah" && !s.Reaction && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        bool Reaches(Snapshot start, string flag)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 10 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    if (from.Has(flag)) return true;
                    var w = Later(story, from, 100);
                    w.Area = Drezen;   // after the Labyrinth, the courtship is in Drezen
                    w.AvailableContacts.Add(Body);
                    foreach (var scene in own.Where(s => Rules.Available(story, s, w)))
                        foreach (var r in Program.Walk(scene, w).Take(4))
                        {
                            if (r.Has(flag)) return true;
                            if (seen.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                        }
                }
                frontier = next.Take(40).ToList();
            }
            return false;
        }

        // Shape and hooks.
        var rel = story.Relationships["hepzamirah"];
        check(rel.StartedFlag == "hepzamirah.started" && rel.ClosedFlag == "hepzamirah.closed" && rel.CommittedFlag == "hepzamirah.committed"
              && rel.UnavailableFlags.Length == 0 && rel.UnavailableOverrides.Count == 0
              && rel.TricksterAccess.Keys.SequenceEqual(new[] { "ghost" }) && rel.TricksterAccess["ghost"].Device == P + "ghost.body",
            "Hepzamirah's relationship does not match the spec.");
        check(offer.AnswerLists.SequenceEqual(new[] { ColyList }) && offer.NativeReturnCue == "b03aa7395540e8040a55a62309caaa1a"
              && offer.Chapters.SequenceEqual(new[] { 4 }) && offer.EntryMythic == "PlayerIsTrickster" && offer.Forbids.Contains("hepzamirah.dead"),
            "The Colyphyr offer is not an inline Trickster answer on her living list, before her death.");
        foreach (var setup in new[] { second, first })
            check(setup.AnswerLists.SequenceEqual(new[] { GhostList }) && setup.NativeReturnCue == "001f33d929abf1440945839ace51891a"
                  && setup.EntryMythic == "PlayerIsTrickster" && setup.EntryAlignment?.Direction == "Chaotic" && setup.TricksterDevice
                  && Choice(setup, "sneer", 0).NativeNext == "a4011b00473994b4dadc6aed381cf504",
                "A setup is not an inline Trickster answer on her ghost's list that continues into Cue_0016: " + setup.Id);
        check(late.ContactUnit == Ghost && late.Areas.SequenceEqual(new[] { Labyrinth }) && late.NativeReturnCue == null
              && Choice(late, "demand", 0).Alignment?.Value == 2 && Choice(late, "demand", 0).Mythic == "PlayerIsTrickster",
            "The late fallback is not the physical, dearer steal in the Labyrinth.");
        check(Rules.IsRemote(body) && Rules.IsRemote(hounds) && body.DelayHours == 48 && hounds.DelayHours == 48,
            "The body and the courier are not the two Chapter 5 letters.");
        check(Choice(body, "terms", 1).Crusade?.Resource == "Finances" && Choice(body, "terms", 1).Crusade!.Amount == -1000
              && Choice(body, "terms", 2).Alignment?.Direction == "Evil",
            "Mutasafen's coin and threat cost nothing.");
        check(Choice(body, "rename", 0).Set.Contains(P + "returned"), "The rename does not return her.");
        // The answers retain their authored presentation; ENGINE-Q5 puts the live requirement on the producer scene.
        check(body.Nodes.SelectMany(n => n.Choices).All(c => c.Mythic == null),
            "The lodger's answers acquired an unnecessary mythic bracket.");
        foreach (var s in yard)
            check(s.ContactUnit == Body && s.Areas.SequenceEqual(new[] { Drezen }) && !Rules.IsRemote(s) && s.Chapters.SequenceEqual(new[] { 5 })
                  && s.Forbids.Contains("hepzamirah.closed"),
                "A yard scene is not by the forge in Drezen, Chapter 5: " + s.Id);
        check(story.Presences["hepzamirah.presence"].Dialog == "hub" && story.Presences["hepzamirah.presence"].At?.NearUnit == "15f754455d1d87c42a4e14df456d5415"
              && story.Presences["hepzamirah.presence.ghost"].Mode == "reuse-native",
            "Her presences are not the forge-yard hub and the Labyrinth ghost.");
        foreach (var s in story.Scenes.Where(s => s.Relationship == "hepzamirah"))
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)))
                check(!(key.EndsWith(".dead", StringComparison.Ordinal) || key.EndsWith("_dead", StringComparison.Ordinal) || key.EndsWith(".closed", StringComparison.Ordinal))
                      || key == "hepzamirah.dead" || key == "hepzamirah.closed" || key == "horzalah.dead",
                    "Hepzamirah needs someone else dead or closed: " + s.Id + " " + key);
        var giveBack = Choice(pick, "smith", 2);
        check(giveBack.RemoveItem == Pick && giveBack.Requires.Contains("hepzamirah.pick_held") && story.RemovableItems.Contains(Pick)
              && story.InventoryItems["hepzamirah.pick_held"] == Pick,
            "Dreadful Onslaught cannot be given back, or is removed without being held.");
        // PP9 (15b T2): Woljif answers the Moon reckoning, one reaction per answer he got, behind his own guards.
        check(reactions.Length == 4 && reactions.All(r => r.Nodes.Count == 1)
              && reactions.Any(r => r.Owner == "Greybor" && r.Forbids.Contains("greybor.dead"))
              && reactions.Any(r => r.Owner == "Ember" && r.Requires.Contains("ember.present") && r.Forbids.Contains("ember_dead"))
              && reactions.Count(r => r.Owner == "Woljif" && r.Forbids.Contains("woljif.dead") && r.Forbids.Contains("woljif.kicked_out")) == 2,
            "The reactions are not exactly Greybor, Ember and Woljif's two Moon answers behind their guards.");
        check(pages.Length == 4 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null))),
            "The epilogue pages carry effects or are missing.");
        check(story.Derived["hepzamirah.trickster.late_committed"].Single().SequenceEqual(new[] { "trickster.ever", P + "courier_seen" }),
            "The late commit is not derived from the courier.");

        // Trk_Hepzamirah_Colyphyr: the standing offer, before she dies; read later as a variant only.
        var colyphyr = World(story, 4, "trickster");
        check(Rules.Available(story, offer, colyphyr) && !Rules.Available(story, offer, World(story, 4, "trickster", "hepzamirah.dead")),
            "Trk_Hepzamirah_Colyphyr: the offer is shut, or survives her death.");
        check(After(offer, colyphyr, "shelf", 0).All(r => r.Has(P + "colyphyr_offer") && !r.Has("hepzamirah.started")),
            "Trk_Hepzamirah_Colyphyr: the offer starts the relationship.");

        // Trk_Hepzamirah_SecondTime.
        var leavable = World(story, 5, "trickster", "trickster.ever", "hepzamirah.dead", "alderpash.leavable");
        check(Rules.Available(story, second, leavable) && !Any(leavable, first, late),
            "Trk_Hepzamirah_SecondTime: the second-time steal is shut, or another setup opens.");
        var primed = After(second, leavable, "sneer", 0).First();
        check(primed.Has(P + "primed") && primed.Has(P + "cost.baphomet_grudge") && primed.Has("hepzamirah.started"),
            "Trk_Hepzamirah_SecondTime: 'After you' does not prime her.");
        check(Rules.Available(story, body, Later(story, primed, 48)) && !Rules.Available(story, body, Later(story, primed, 24)),
            "Trk_Hepzamirah_SecondTime: the body does not follow two days later.");
        check(Reaches(primed, "hepzamirah.committed"), "Trk_Hepzamirah_SecondTime: no road to the commit.");

        // Trk_Hepzamirah_NoAlderpash.
        var plain = World(story, 5, "trickster", "trickster.ever", "hepzamirah.dead");
        check(Rules.Available(story, first, plain) && !Rules.Available(story, second, plain), "Trk_Hepzamirah_NoAlderpash: the wrong setup opens.");

        // Trk_Hepzamirah_Dispersed: the late steal, aloud, dearer.
        var dispersed = WorldIn(story, Labyrinth, 5, "trickster", "trickster.ever", "hepzamirah.dead", "hepzamirah.ghost_dispersed");
        check(Rules.Available(story, late, dispersed) && !Any(dispersed, second, first),
            "Trk_Hepzamirah_Dispersed: the late steal is shut, or a setup survives the dispersal.");
        var loud = After(late, dispersed, "demand", 0).First();
        check(loud.Has(P + "primed") && loud.Has(P + "cost.late"), "Trk_Hepzamirah_Dispersed: the late steal does not cost the late terms.");
        check(Reaches(loud, "hepzamirah.committed"), "Trk_Hepzamirah_Dispersed: no road to the commit.");

        // Trk_Hepzamirah_Deed: the Commander left the Labyrinth without either steal; his horned mark cut into the Commander's own arm on his altar, priced.
        var deed = S(P + "ghost.deed_by_fire");
        var walkedPast = World(story, 5, "trickster", "trickster.ever", "hepzamirah.dead", "baphomet.parley.latched");
        check(Rules.IsRemote(deed) && deed.TricksterDevice && deed.DelayHours == 72 && deed.Requires.Contains("trickster"),
            "Trk_Hepzamirah_Deed: the post-Labyrinth fallback is not a live-path Trickster device, three days later.");
        check(Rules.Available(story, deed, walkedPast), "Trk_Hepzamirah_Deed: the deed does not open after the Labyrinth.");
        var burned = After(deed, walkedPast, "deed", 0).First();
        check(burned.Has(P + "primed") && burned.Has(P + "cost.altar") && burned.Has(P + "cost.late") && burned.Has(P + "cost.horned_scar")
              && Choice(deed, "deed", 0).Crusade?.Resource == "Favors" && Choice(deed, "deed", 0).Alignment?.Value == 2,
            "Trk_Hepzamirah_Deed: the blood mark costs nothing, leaves no scar, or does not prime her.");
        check(!Choice(deed, "deed", 0).Text.Contains("Signed") && Choice(deed, "deed", 0).Text.Contains("blood"),
            "Trk_Hepzamirah_Deed: the altar is reached by paperwork again instead of by the Commander's own blood.");
        check(After(deed, walkedPast, "deed", 1).All(r => r.Has("hepzamirah.closed") && !r.Has(P + "primed")),
            "Trk_Hepzamirah_Deed: breaking the altar is not the hard no.");
        check(!Rules.Available(story, deed, World(story, 5, "trickster.ever", "trickster.failed", "hepzamirah.dead", "baphomet.parley.latched")),
            "Trk_Hepzamirah_Deed: the deed opens without the live path.");
        check(Rules.Available(story, body, Later(story, burned, 48)) && Reaches(burned, "hepzamirah.committed"),
            "Trk_Hepzamirah_Deed: no road from the altar to the commit.");

        // Trk_Hepzamirah_LeftToRot: the Commander's hard no.
        var rot = After(second, leavable, "sneer", 1).First();
        check(rot.Has("hepzamirah.closed") && !rot.Has(P + "primed") && !Any(Later(story, rot, 100), body, first, second),
            "Trk_Hepzamirah_LeftToRot: leaving her to rot does not close the route.");

        // Trk_Hepzamirah_Deal*: Mutasafen's three prices; the foresight is only a variant.
        var ghost = World(story, 5, "trickster", "trickster.ever", P + "primed");
        check(Rules.Available(story, body, ghost), "Trk_Hepzamirah_NoForesight: the body needs the letter or the boast.");
        check(After(body, ghost, "terms", 0).All(r => r.Has(P + "cost.blood_sample") && r.Has(P + "returned")),
            "Trk_Hepzamirah_DealBlood: the blood does not buy the body.");
        check(After(body, ghost, "terms", 1).All(r => r.Has(P + "cost.lab_funded") && r.Has(P + "returned")),
            "Trk_Hepzamirah_DealCoin: the coin does not buy the body.");
        check(After(body, ghost, "terms", 2).All(r => r.Has(P + "cost.mutasafen_grudge") && r.Has(P + "returned")),
            "Trk_Hepzamirah_DealThreat: the threat does not buy the body.");
        check(Rules.Available(story, body, World(story, 5, "trickster", "trickster.ever", P + "primed", "hepzamirah.mutasafen_letter", "hepzamirah.mutasafen_secret")),
            "The foresight gates the body instead of colouring it.");
        check(Play(body, ghost).All(r => !r.Has("hepzamirah.committed")), "The return scene commits.");

        // The courtship by the forge: the first morning, then the pick; the commit needs both and the courier.
        var back = World(story, 5, "trickster", "trickster.ever", P + "primed", P + "returned");
        check(Rules.Available(story, morning, Later(story, back, 12)) && !Rules.Available(story, pick, Later(story, back, 12))
              && !Rules.Available(story, terms, Later(story, back, 200)),
            "The first morning does not open the courtship, or the pick or the terms skip it.");
        check(hounds.DelayHours == 48 && Rules.Available(story, hounds, Later(story, back, 48)),
            "The courier does not follow the return two days later.");

        // Trk_Hepzamirah_Courier: her test of the Commander.
        var fed = World(story, 5, "trickster", "trickster.ever", P + "primed", P + "returned", F + "first_morning", F + "the_pick", P + "armed");
        check(Rules.Available(story, hounds, fed) && !Rules.Available(story, terms, fed),
            "Trk_Hepzamirah_Courier: the courier is shut, or the terms skip it.");
        var tested = After(hounds, fed, "joke", 0).First();
        check(tested.Has(P + "courier_seen") && tested.Has(P + "cost.vial_paid"), "Trk_Hepzamirah_Courier: the vial does not pay the courier.");
        check(Choice(hounds, "joke", 0).Next == "vial" && hounds.Nodes.Single(n => n.Id == "vial").Text.Contains("She draws it herself"),
            "Trk_Hepzamirah_Courier: the blood is paid off-screen instead of drawn from the Commander.");
        check(Rules.Available(story, terms, Later(story, tested, 24)), "Trk_Hepzamirah_Courier: the terms do not follow the courier.");
        check(After(hounds, fed, "joke", 1).All(r => r.Has(P + "cost.courier_killed")) && Choice(hounds, "joke", 1).Alignment?.Direction == "Evil"
              && After(hounds, fed, "joke", 2).All(r => r.Has(P + "cost.vial_forged")),
            "The courier's three answers are not all reachable with their costs.");

        // Trk_Hepzamirah_Commit and her hard no.
        var ready = Later(story, tested, 24);
        var committed = Play(terms, ready).Where(r => r.Has("hepzamirah.committed")).ToList();
        check(committed.Count > 0 && committed.All(r => !r.Has("hepzamirah.closed")), "Trk_Hepzamirah_Commit: the terms do not commit.");
        check(Choice(terms, "sealed", 0).Set.Contains("hepzamirah.committed") && Choice(terms, "sealed", 0).Next == "threshold",
            "The named producer is not terms/sealed[0].");
        check(Play(terms, ready).Any(r => r.Has("hepzamirah.closed") && !r.Has("hepzamirah.committed")),
            "Trk_Hepzamirah_Refused: her hard no is not reachable.");
        var refused = World(story, 6, "trickster", "trickster.ever", P + "primed", P + "returned", P + "courier_seen", "hepzamirah.closed");
        check(!Rules.Available(story, S(P + "epilogue.commit"), refused) && !Rules.Available(story, S(P + "epilogue.leavable"), refused)
              && Rules.Available(story, S(P + "epilogue.refused"), refused),
            "Trk_Hepzamirah_Refused: the refused page does not replace the others.");
        check(!yard.Any(s => Rules.Available(story, s, Later(story, refused, 100))) && !Rules.Available(story, terms, refused),
            "Her refusal leaves a yard scene open.");

        // Trk_Hepzamirah_EmberDead: Ember hosts nothing; she only speaks if she is there.
        var emberDead = World(story, 5, "trickster", "trickster.ever", P + "primed", P + "returned", P + "courier_seen", F + "first_morning", F + "the_pick", "ember_dead");
        check(Rules.Available(story, terms, emberDead) && !Rules.Available(story, S(F + "flowers"), emberDead),
            "Trk_Hepzamirah_EmberDead: the terms depend on Ember, or her flowers come without her.");
        check(Rules.Available(story, S(P + "epilogue.commit"), World(story, 6, "trickster", "trickster.ever", P + "courier_seen")),
            "The epilogue commit does not carry a world where the terms were never heard.");

        // Q8 (Sol COX): a Last Call bottle survivor (commander_back without cheated_death) keeps her ending pages.
        var bottle = World(story, 6, "trickster", "trickster.ever", P + "courier_seen", "sacrifice", "trickster.commander_back");
        check(Rules.Available(story, S(P + "epilogue.commit"), bottle)
              && Rules.Available(story, S(P + "epilogue.leavable"), World(story, 6, "trickster", "trickster.ever", P + "courier_seen", "hepzamirah.committed", "sacrifice", "trickster.commander_back"))
              && !Rules.Available(story, S(P + "epilogue.leavable_on_record"), World(story, 6, "trickster", "trickster.ever", "hepzamirah.committed", "sacrifice", "trickster.commander_back"))
              && Rules.Available(story, S(P + "epilogue.leavable_on_record"), World(story, 6, "trickster", "trickster.ever", "hepzamirah.committed", "sacrifice")),
            "A surviving Commander loses Hepzamirah's ending, or a dead one keeps it.");

        // ENGINE-Q5: stealing the corner and completing the body both require the live path.
        var failed = WorldIn(story, Labyrinth, 5, "trickster.was", "trickster.ever", "trickster.failed", "hepzamirah.dead", "hepzamirah.ghost_dispersed");
        check(!Any(failed, second, first, late), "Trk_Hepzamirah_PathFailed: a steal opens without the live path.");
        check(!Rules.Available(story, body, World(story, 5, "trickster.ever", "trickster.failed", P + "primed")),
            "A new body completes after the path failed.");

        // The nights: only after the commit, and the cut lands at the start of the act (Directive 12).
        var lovers = World(story, 5, "trickster", "trickster.ever", P + "primed", P + "returned", P + "courier_seen", F + "first_morning", F + "the_pick", "hepzamirah.committed");
        var dawn = S(B + "morning");
        check(Rules.Available(story, dawn, Later(story, lovers, 6)) && !Rules.Available(story, dawn, fed), "The morning after comes before the night.");
        var threshold = terms.Nodes.Single(n => n.Id == "threshold");
        check(threshold.Text.Contains("shoves you back against it") && threshold.Text.Contains("a bite that forgot to finish")
              && threshold.Choices.Count == 1 && threshold.Choices[0].Next == null,
            "The terms fade before the approach, or the cut does not land on the threshold.");
        var crooked = S(B + "crooked");
        var down = crooked.Nodes.Single(n => n.Id == "down");
        check(down.Choices.Count == 1 && down.Choices[0].Next == null && crooked.Nodes.Single(n => n.Id == "pull").Text.Contains("bears you down"),
            "The second night does not stage the approach, or runs past the cut.");
        foreach (var banned in new[] { "thrust", "inside her", "inside you", "climax", "moan", "naked" })
            check(new[] { terms, crooked }.All(s => s.Nodes.All(n => !n.Text.Contains(banned, StringComparison.OrdinalIgnoreCase))),
                "Her nights narrate past the cut: " + banned);

        // Every courtship beat is reachable on its own path, in order.
        var armed = World(story, 5, "trickster", "trickster.ever", P + "primed", P + "returned", F + "first_morning", F + "the_pick", P + "armed", "ember.present");
        foreach (var id in new[] { "chaplains", "mirror_open", "rent", "sister", "the_corner", "drill", "the_market", "the_nexus", "flowers" })
        {
            if (id == "mirror_open") continue;
            check(Rules.Available(story, S(F + id), Later(story, armed, 24)), "A courtship beat does not open after the pick: " + id);
        }
        // Q8 (Sol INT): the garrison's cot verse waits for the cot.
        check(!Rules.Available(story, S(F + "the_song"), Later(story, armed, 24)) && S(F + "the_song").Requires.Contains(B + "morning"),
            "The barracks sing about the lovers' cot before there is one.");
        // Q8 (Sol INT): three nights in the cells are enforced; the yard waits for the release at 72 h.
        var chap = S(F + "chaplains");
        var jailed = Play(chap, Later(story, armed, 24)).First(r => r.Has(P + "cost.confined"));
        var release = S(F + "released");
        foreach (var h in new[] { 0, 36, 71 })
            check(!yard.Where(s => s != release).Any(s => Rules.Available(story, s, Later(story, jailed, h))) && !Rules.Available(story, release, Later(story, jailed, h)),
                "A yard beat opens while she is in the cells (hour " + h + ").");
        var freed = Later(story, jailed, 72);
        check(Rules.Available(story, release, freed), "Her release does not come at 72 hours.");
        var out72 = Play(release, freed).First();
        check(out72.Has(F + "released") && Rules.Available(story, pick, Later(story, out72, 24)) == false
              && Rules.Available(story, S(F + "the_market"), Later(story, out72, 24)),
            "The yard does not reopen after her release.");
        var mirrored = Later(story, armed, 24);
        mirrored.Flags.Add(F + "mirror");
        check(Rules.Available(story, S(F + "the_horn"), Later(story, mirrored, 24)) && Rules.Available(story, S(F + "unsent"), Later(story, mirrored, 24)),
            "The horn and the letter do not follow the mirror.");
        var woljifGone = Later(story, armed, 24);
        woljifGone.Flags.Add("woljif.dead");
        check(!Rules.Available(story, S(F + "bloodline"), woljifGone) && Rules.Available(story, S(F + "bloodline"), Later(story, armed, 24)),
            "Woljif's bloodline scene ignores whether he lives.");
        var nights = Later(story, lovers, 6);
        nights.Flags.Add(B + "morning");
        foreach (var id in new[] { "the_call", "the_hunt", "sortie", "names", "her_room", "gift", "map_table" })
            check(Rules.Available(story, S(B + id), Later(story, nights, 48)), "A post-commit beat does not open after the morning: " + id);
        var hunted = Later(story, nights, 48);
        hunted.Flags.Add(B + "the_hunt");
        hunted.Times[B + "the_hunt"] = hunted.Hour;
        // Q8 (Sol BEL): two days out, two days back, the work between; she comes home on the fifth day.
        check(S(B + "the_eye").DelayHours == 120 && Rules.Available(story, S(B + "the_eye"), Later(story, hunted, 120))
              && !Rules.Available(story, S(B + "the_eye"), Later(story, hunted, 119))
              && !Rules.Available(story, S(B + "the_eye"), Later(story, nights, 48)),
            "What she brings back does not wait for the hunt.");
        var eye = Play(S(B + "the_eye"), Later(story, hunted, 120));
        check(eye.Any(r => r.Has(P + "eye_kept")) && eye.Any(r => r.Has(P + "eye_burned")), "The eye cannot be kept or burned.");
        check(Rules.Available(story, S(B + "eve"), Later(story, eye.First(), 24)), "The eve does not follow the eye.");
        var hunt = S(B + "the_hunt");
        check(Choice(hunt, "where", 1).Check?.Skill == "SkillStealth" && Play(hunt, Later(story, nights, 48)).Any(r => r.Has(P + "cost.followed")),
            "Following her against her term costs nothing.");

        // Every hunt terminal withholds the same physical contact, even when the snapshot retains the old body.
        var terminals = Play(hunt, Later(story, nights, 48));
        check(terminals.Count == 4, "Hunt fixture must walk all four terminals.");
        foreach (var terminal in terminals)
        {
            var visits = yard.Where(s => s.Id != hunt.Id && Rules.Available(story, s, Later(story, terminal, 121))).ToArray();
            check(visits.Length > 0, "Hunt fixture has no ordinary visits to check.");
            foreach (int hours in new[] { 0, 24, 119, 120, 121 })
            {
                var at = Later(story, terminal, hours);
                check(Rules.PresenceWanted(story.Presences["hepzamirah.presence"], at) == (hours >= 120), "Hunt presence interval: " + hours);
                foreach (var visit in visits)
                    check(Rules.ContactAvailable(story, visit, at) == (hours >= 120)
                        && Rules.Available(story, visit, at) == (hours >= 120), "Stale hunt contact: " + visit.Id + "/" + hours);
            }
        }

        // No other route's flag is required, closed or forbidden by her scenes; her closure touches nobody else.
        foreach (var s in story.Scenes.Where(s => s.Relationship != "hepzamirah"))
            check(!s.Requires.Contains("hepzamirah.closed") && !s.Forbids.Contains("hepzamirah.closed"), "Another route reads Hepzamirah's closure: " + s.Id);
        foreach (var s in yard)
            foreach (var node in s.Nodes.Where(n => n.Speaker == "Hepzamirah"))
                check(!node.Text.Contains("you say") && !node.Text.Contains("you tell her"),
                    "The Commander speaks inside her node: " + s.Id + "/" + node.Id);
        Console.WriteLine("PASS: Hepzamirah Trickster (Trk_Hepzamirah_*): Colyphyr, the Leavable steal, the lodger, the Apprentice, the terms and the courtship by the forge.");
    }
}
