using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Jannah, Trickster (Writer/handoffs/trickster/jannah.md; binding plan 11-ROSTER-PLAN-2 §2 with the coordinator's correction):
// "First blood". One block per rules test (Trk_Jannah_*): the Aldori forms at the Molten Scar cage before the native blow, the
// unclaimed yield in her Drezen cell, blood and tale in the living worlds (the catch, the false catch, the lost tale and the
// wagon), the spine (the forms, Houndheart, the wall), her public challenge (two yeses, the Commander's public yield, her
// thrown bout), the chalk circle after her no, the night and the morning, the pages, the two allocated reactors, the Ledger
// secret, and Seelah's own word on her after Q3.
internal static class JannahTricksterTests
{
    private const string Unit = "4880d0b16ca74fa46a167914e2b44bcc";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Locator = "e595a2a6-e8ca-4d13-9010-f482088a4a27";
    private const string CageList = "170fd7a11f66c88428bc27bfba3a569f";
    private const string FirstList = "b2b77a591c8808f409aa2083bd1b318a";
    private const string FirstCue = "8c909dc650b9dff408a0d144da24b920";
    private const string IrabethHub = "871af36f2ab2b1f40b5de77976c54276";
    private const string KingC5 = "6dccfd39947ef4242a8afbe36b21a46c";
    private const string SeelahHub = "417fa384f3250634bb71859fbc913453";
    private const string P = "jannah.trickster.";
    private const string C = "jannah.circle.";
    private const string Dead = "jannah.dead";
    private const string DeadKnown = "jannah.dead_known";
    private const string Primed = P + "primed";
    private const string Returned = P + "returned";
    private const string Committed = "jannah.committed";
    private const string Closed = "jannah.closed";
    private const string FirstLoss = P + "cost.first_loss";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Unit);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 300;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, int? chapter = null)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        if (chapter != null) later.Chapter = chapter.Value;
        Rules.Complete(story, later);
        foreach (var flag in later.Flags.Where(f => !later.Times.ContainsKey(f)).ToList()) later.Times[flag] = state.Hour;
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        bool Avail(Scene s, Snapshot w) => Rules.Available(story, s, w);
        Choice Ch(Scene s, string node, int index) => s.Nodes.Single(n => n.Id == node).Choices[index];
        List<Snapshot> Through(Scene scene, Snapshot w, string node, int index)
        {
            var chosen = Ch(scene, node, index);
            var hits = new List<Snapshot>();
            foreach (var r in Program.Walk(scene, w))
                if (chosen.Set.All(r.Has) && (chosen.Set.Length > 0 || r.Has(scene.Id))
                    && chosen.Forbids.All(f => !r.Has(f) || chosen.Set.Contains(f))) hits.Add(r);
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        Snapshot Take(Scene scene, Snapshot w, string node, int index, params string[] also)
        {
            var hit = Through(scene, w, node, index).FirstOrDefault(r => also.All(r.Has));
            check(hit != null, "No outcome of " + scene.Id + " through " + node + "[" + index + "] with " + string.Join(", ", also));
            return hit ?? w;
        }
        var own = story.Scenes.Where(s => s.Relationship == "jannah" && !s.Reaction && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        bool Reaches(Snapshot start, string flag, int chapter = 5, Func<Snapshot, bool>? keep = null)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 20 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    if (from.Has(flag)) return true;
                    var w = Later(story, from, 160, chapter);
                    foreach (var scene in own.Where(s => Avail(s, w)))
                        foreach (var r in Program.Walk(scene, w))
                        {
                            if (r.Has(flag)) return true;
                            if (keep != null && !keep(r)) continue;
                            if (seen.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                        }
                }
                frontier = next.Take(300).ToList();
            }
            return false;
        }

        var rel = story.Relationships["jannah"];
        var named = S(P + "cage.forms");
        var terms = S(P + "cage.terms");
        var ash = S(P + "cage.ash");
        var yield = S(P + "killed.yield");
        var letter = S(P + "alive.letter");
        var stories = S(P + "alive.stories");
        var wagon = S(P + "alive.wagon");
        var forms = S(C + "forms");
        var houndheart = S(C + "houndheart");
        var walls = S(C + "walls");
        var challenge = S(P + "challenge");
        var night = S(P + "circle_night");
        var morning = S(P + "morning");
        var chalk = S(P + "chalk_circle");
        var pages = story.Scenes.Where(s => s.Relationship == "jannah" && s.Owner == "JannahEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "jannah" && s.Reaction).ToArray();

        // Shape and hooks.
        check(rel.StartedFlag == "jannah.started" && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.SequenceEqual(new[] { Dead, DeadKnown })
              && rel.UnavailableOverrides[Dead] == Returned && rel.UnavailableOverrides[DeadKnown] == Returned
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "alive", "killed", "killed_known" }),
            "Jannah's relationship does not match the plan (killed/killed_known/alive access; the return lifts both deaths).");
        check(named.AnswerLists.SequenceEqual(new[] { FirstList }) && named.NativeReturnCue == FirstCue && named.EntryMythic == "PlayerIsTrickster"
              && named.Chapters.SequenceEqual(new[] { 3 }) && named.Requires.SequenceEqual(new[] { "trickster" }) && named.TricksterDevice
              && Ch(named, "start", 0).Check?.Skill == "SkillKnowledgeWorld" && Ch(named, "start", 1).Abort
              && Ch(named, "named_her", 0).Set.SequenceEqual(new[] { P + "primed.forms_named" }) && Ch(named, "named_her", 1).Set.SequenceEqual(new[] { P + "primed.forms_named" })
              && Ch(named, "garbled_her", 0).Set.SequenceEqual(new[] { P + "cage.botched" }),
            "The forms are not the inline Knowledge (World) primer on her first list, returning to a clean native cue.");
        check(terms.AnswerLists.SequenceEqual(new[] { CageList }) && terms.ReturnToList && terms.NativeReturnCue == null && terms.EntryMythic == "PlayerIsTrickster"
              && terms.Requires.SequenceEqual(new[] { "trickster", P + "primed.forms_named" }) && terms.Forbids.Contains(Primed) && terms.TricksterDevice
              && Ch(terms, "guard", 0).Set.SequenceEqual(new[] { Primed }) && Ch(terms, "guard", 1).Abort && Ch(terms, "accept", 1).Abort
              && terms.Nodes.All(n => n.Choices.All(c => c.NativeNext == null && c.Check == null)),
            "The challenge is not the return-to-list scene on the sentence list, made before the native [Attack] and after the forms were named.");
        check(!story.Scenes.Any(s => s.Nodes.Any(n => n.Choices.Any(c => c.Set.Any(f => f.StartsWith("trickster.wmt.use.", StringComparison.Ordinal))))
                                  && s.Relationship == "jannah"),
            "Jannah's device spends a Word Made True (the budget is full: duel law, not a word made true).");

        var presence = story.Presences["jannah.presence"];
        check(presence.Unit == Unit && presence.Mode == "spawn-copy" && presence.Dialog == "hub" && presence.At?.Locator == Locator
              && presence.MinChapter == 5 && presence.MaxChapter == 5 && presence.Requires.Contains(P + "presence_on")
              && story.Derived[P + "presence_on"].Any(g => g.Contains("jannah.dead.latched") && g.Contains(Primed))
              && story.Derived[P + "presence_on"].Any(g => g.Length == 1 && g[0] == Returned),
            "Her presence is not the Chapter 5 copy at her canon cell locator, on in the kept-forms and returned worlds only.");
        check(!story.Presences.Any(p => !p.Key.StartsWith("jannah.presence", StringComparison.Ordinal) && p.Value.At?.Locator == Locator),
            "Another presence stands on her cell locator.");
        // Q6 follow-up (INT/COX): the cell before her return and the cell after the wagon are her own presences on the same
        // locator, never wanted together with each other or with the returned one.
        var jp = story.Presences.Where(p => p.Key.StartsWith("jannah.presence", StringComparison.Ordinal)).ToList();
        check(jp.Count == 3 && jp.All(p => p.Value.At?.Locator == Locator && p.Value.Dialog == "hub")
              && jp.All(a => jp.All(b => a.Key == b.Key || Rules.PresencesExclusive(a.Value, b.Value))),
            "Her cell presences are not three exclusive hubs on her cell locator.");
        foreach (var hub in own.Where(s => !Rules.IsRemote(s) && s.InteractionHub != null && s.InteractionHub.StartsWith("jannah.presence", StringComparison.Ordinal)))
            check(hub.ContactUnit == Unit && hub.Areas.SequenceEqual(new[] { Drezen }) && hub.Forbids.Contains(Closed)
                  && hub.Requires.Contains("trickster.ever") && hub.Chapters.SequenceEqual(new[] { 5 }),
                "A cell scene is not a Chapter 5 Trickster-path hub scene behind her closure: " + hub.Id);
        check(!own.Any(s => s.AnswerLists.Contains("0f12118177d102f428a3b30b15b132eb") || s.AnswerLists.Contains("a380d926e92f70e429681eb9654478f9")
                            || s.AnswerLists.Contains("15f754455d1d87c42a4e14df456d5415")),
            "A Jannah scene hangs on a crowded hub (Fye, the yard, the smith).");
        check(own.All(s => !s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g))
                           .Any(f => f == "seelah_dead" || f == "seelah_gone" || f == "seelah.closed" || f == "seelah.trickster.returned")),
            "A Jannah scene gates on Seelah's fate (coexistence: node-level reads only).");

        // Trk_Jannah_Cage (quality pass Q6 r3): the cage primers are retired by gating until an engine substitution of the native
        // [Attack] outcome exists (Cue_0027 + KillJanna run a real Kill). The cage is then the Commander's own choice of a
        // non-partner's death, and canon stands (11-ROSTER-PLAN-2 section 5 ruling #2). Ids, nodes and indices are kept.
        foreach (var w in new[] { World(story, 3, "trickster", "trickster.ever"), World(story, 3, "trickster", "trickster.ever", P + "primed.forms_named") })
            check(!Avail(named, w) && !Avail(terms, w), "Trk_Jannah_Cage: a retired cage primer still opens.");
        check(named.Forbids.Contains("chapter_later") && terms.Forbids.Contains("chapter_later")
              && !own.Where(s => s.MinChapter <= 3).Where(s => Avail(s, World(story, 3, "trickster", "trickster.ever")))
                     .SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Any(c => c.Set.Contains(Primed)),
            "Trk_Jannah_Cage: something still primes the staged survival.");
        check(!rel.Guidance.Contains("know the Aldori forms first", StringComparison.Ordinal), "The journal still promises the cage device.");

        // The killed-world scenes below are dormant (nothing sets `primed`); their unit checks stay for the day the substitution lands.
        // Trk_Jannah_Killed: the kill after the forms; the ash; the unclaimed yield in her cell.
        var killed3 = World(story, 3, "trickster", "trickster.ever", Dead, Primed);
        check(Avail(ash, Later(story, killed3, 6)) && ash.TricksterDevice && Rules.IsRemote(ash) && ash.Optional,
            "Trk_Jannah_Killed: the ash is not the optional memory of the blow.");
        var killed5 = World(story, 5, "trickster.ever", Dead, Primed);
        check(Avail(yield, killed5) && yield.TricksterDevice && !Avail(letter, World(story, 5, "trickster", "trickster.ever", Dead, "coronation.seen")),
            "Trk_Jannah_Killed: the yield does not wait in her cell, or the living world's letter opens over her death.");
        var claim = yield.Nodes.Single(n => n.Id == "claim").Choices;
        check(claim.Count == 4 && claim.Take(3).All(c => c.Set.Contains(Returned) && c.Set.Contains(FirstLoss) && c.Set.Contains(P + "cost.temple_scar"))
              && claim[2].Alignment?.Direction == "Evil" && claim[3].Set.Contains(Closed) && !claim[3].Set.Contains(Returned),
            "Trk_Jannah_Killed: the claim is not three returns (one Evil) that cost her record and scar, and a dismissal.");
        var back = Take(yield, killed5, "claim", 0, Returned);
        check(Reaches(back, Committed), "Trk_Jannah_Killed: no road from the yield to the commit.");
        check(Take(ash, Later(story, killed3, 6), "fall", 1, P + "ash.said_sentence").Has(P + "cost.left_in_ash"), "Trk_Jannah_Killed: the ash costs nothing.");
        check(Through(yield, World(story, 5, "trickster.ever", Dead, Primed, P + "ash.said_sentence"), "claim", 1).Any(), "Trk_Jannah_Killed: the spoken sentence closes the yield.");
        check(Avail(yield, World(story, 5, "trickster.ever", DeadKnown, Primed)) && Reaches(Take(yield, World(story, 5, "trickster.ever", DeadKnown, Primed), "claim", 1, Returned), Committed),
            "Trk_Jannah_KilledKnown: Seelah's knowing closes the road.");

        // Trk_Jannah_KilledUnprimed / PathFailed: canon fate stands.
        check(!own.Any(s => Avail(s, World(story, 5, "trickster", "trickster.ever", Dead, "coronation.seen"))),
            "Trk_Jannah_KilledUnprimed: a scene opens over an unprimed kill (canon stands for a player-chosen kill).");
        check(!own.Any(s => Avail(s, World(story, 5, "trickster.was", "trickster.ever", "trickster.failed", Dead))),
            "Trk_Jannah_PathFailed: a scene opens after the path is lost.");

        // Trk_Jannah_Alive: every living world reaches the letter, blood and tale, and the commit.
        var worlds = new (string name, string[] flags)[]
        {
            ("joined", new[] { "jannah.joined", "jannah.condemned", "seelah.q3_started", "seelah.souls_returned" }),
            ("refused", new[] { "jannah.refused_q3", "jannah.free", "seelah.q3_started" }),
            ("condemned", new[] { "jannah.condemned", "coronation.seen" }),
            ("prison", new[] { "jannah.prison", "coronation.seen" }),
            ("free", new[] { "jannah.free", "coronation.seen" }),
            ("unmet", new[] { "coronation.seen" }),
        };
        foreach (var (name, flags) in worlds)
        {
            var w = World(story, 5, new[] { "trickster", "trickster.ever", "seelah.houndheart_seen" }.Concat(flags).ToArray());
            check(Avail(letter, w) && !Avail(yield, w), "Trk_Jannah_Alive_" + name + ": the letter from the cells does not come.");
            var node = letter.Nodes.Single(n => n.Id == "open").Choices.Where(c => Rules.Match(c.Requires, c.Forbids, w)).Select(c => c.Next).ToList();
            check(node.Count == 1 && node[0] == name, "Trk_Jannah_Alive_" + name + ": the letter speaks from the wrong world (" + string.Join(",", node) + ").");
            var cells = Take(letter, w, "sign", 0, P + "alive.in_cells");
            check(Avail(stories, Later(story, cells, 12)) && stories.TricksterDevice && stories.TricksterState == "alive",
                "Trk_Jannah_Alive_" + name + ": blood and tale does not follow the letter.");
            check(Reaches(cells, Committed), "Trk_Jannah_Alive_" + name + ": no road from the cells to the commit.");
        }
        var q3open = World(story, 5, "trickster", "trickster.ever", "jannah.condemned", "coronation.seen", "seelah.q3_started");
        check(!Avail(letter, q3open), "Trk_Jannah_Q3: she writes from the cells in the middle of Seelah's Q3.");
        var inCells = Later(story, Take(letter, World(story, 5, "trickster", "trickster.ever", "jannah.free", "coronation.seen", "seelah.houndheart_seen"), "sign", 0, P + "alive.in_cells"), 12);
        // Q6 r5 (CAN): the duel of stories tells Houndheart, so it needs the Commander there (KnightCamp Cue_0011/Cue_0012).
        // Q6 follow-up (INT): without it she plays the visitors' way (each tells her own bout); the route goes on, by the catch
        // or by the wagon, and only letting her go closes it.
        var noHH = Later(story, Take(letter, World(story, 5, "trickster", "trickster.ever", "coronation.seen"), "sign", 0, P + "alive.in_cells"), 12);
        var noHHPaths = Program.Walk(stories, noHH).ToList();
        HashSet<string> Pages(Scene s, Snapshot w) { var seen = new HashSet<string>(); Program.Walk(s, w, (page, _) => seen.Add(page)); return seen; }
        check(story.SeenCues["seelah.houndheart_seen"].Contains("2100f41ae724734418dc74b15719543e")
              && Ch(stories, "choose", 0).Requires.Contains("seelah.houndheart_seen") && Ch(stories, "choose", 2).Forbids.Contains("seelah.houndheart_seen")
              && !Pages(stories, noHH).Contains("rules") && !Pages(stories, noHH).Contains("your_tale") && Pages(stories, noHH).Contains("own_tale")
              && Pages(stories, inCells).Contains("rules") && !Pages(stories, inCells).Contains("own_tale"),
            "The duel of stories recalls a Houndheart the Commander never saw, or the visitors' way opens for one who saw it.");
        check(noHHPaths.Any(r => r.Has(Returned) && r.Has(P + "alive.caught_her") && r.Has(P + "alive.visitors_way"))
              && noHHPaths.Any(r => r.Has(P + "alive.posted") && !r.Has(Closed))
              && noHHPaths.Where(r => r.Has(Closed)).All(r => r.Has(P + "gone") && !r.Has(P + "alive.posted"))
              && Reaches(noHH, Committed),
            "Trk_Jannah_NoHoundheart: a Commander who was never at Houndheart cannot win her out of the cell, lose to the wagon, or reach the commit.");
        check(Ch(stories, "caught", 0).Requires.Contains("jannah.quasit_seen") && Ch(stories, "caught", 1).Forbids.Contains("jannah.quasit_seen")
              && story.SeenCues["jannah.quasit_seen"].SequenceEqual(new[] { "da671fced713af6419502ca50bdeb94c" }),
            "The shared catch remembers a quasit attempt the Commander may not have seen (KnightCamp Cue_0017).");
        var visitorWorld = World(story, 5, "trickster.ever", Returned, P + "alive.caught_her", P + "alive.visitors_way", C + "forms");
        check(Pages(houndheart, visitorWorld).Contains("told_visitor") && !Pages(houndheart, visitorWorld).Contains("told"),
            "Houndheart tells a visitor that the two of them told the camp together.");
        // Q6 r5 (CAN): no invented Houndheart weather, wagons or fire anywhere in the living route.
        foreach (var s in own.Where(x => !x.Forbids.Contains("chapter_later")))
            foreach (var n in s.Nodes)
                check(!new[] { "barricade", "wagon tongue", "second wave", "rained at Houndheart", "into the rain" }.Any(t => n.Text.Contains(t, StringComparison.Ordinal)),
                    "Invented Houndheart detail in " + s.Id + "/" + n.Id);
        var caught = Take(stories, inCells, "yield", 0, P + "alive.caught_her", Returned, FirstLoss);
        check(Ch(stories, "her_tale", 0).Check?.Skill == "SkillPerception" && Ch(stories, "missed", 0).Check?.Skill == "CheckBluff",
            "Trk_Jannah_Stories: the catch is not Perception, or the false catch not a Bluff.");
        Take(stories, inCells, "stay_false", 0, P + "alive.false_blood", "trickster.secret.jannah_false_blood", Returned, FirstLoss);
        var lost = Program.Walk(stories, inCells).Where(r => r.Has(P + "alive.posted")).ToList();
        check(lost.Count > 0 && lost.All(r => !r.Has(Returned) && !r.Has(Closed)), "Trk_Jannah_Stories: a lost tale closes her, or returns her.");
        check(Program.Walk(stories, inCells).Where(r => r.Has(Closed)).All(r => r.Has(P + "gone")),
            "Trk_Jannah_Stories: the only close is letting her go without a bout.");
        var posted = lost[0];
        check(!Avail(wagon, Later(story, posted, 35)) && Avail(wagon, Later(story, posted, 36)) && wagon.TricksterDevice,
            "Trk_Jannah_Wagon: she does not come back from the posting.");
        var home = Take(wagon, Later(story, posted, 36), "said", 0, Returned, P + "cost.story_lost", P + "cost.posting");
        check(!home.Has(FirstLoss) && Reaches(home, Committed), "Trk_Jannah_Wagon: no road from the wagon to the commit, or she lost her record in a tale she won.");

        // Trk_Jannah_Spine: the forms, Houndheart, the wall; the challenge only after the wall.
        var spine = Later(story, caught, 24);
        check(Avail(forms, spine) && !Avail(houndheart, spine) && !Avail(challenge, spine), "Trk_Jannah_Spine: the forms are not first.");
        var formed = Later(story, Take(forms, spine, "grip_her", 0), 24);
        check(Avail(houndheart, formed), "Trk_Jannah_Spine: Houndheart does not follow the forms.");
        var blame = houndheart.Nodes.Single(n => n.Id == "blame").Choices;
        check(blame.Count == 4 && blame[0].Set.Contains(C + "hh.honest") && blame[1].Set.Contains(C + "hh.lucky") && blame[2].Set.Contains(C + "hh.stand"),
            "Trk_Jannah_Houndheart: her shame does not meet three distinct answers and a lie she catches.");
        var hh = Later(story, Take(houndheart, formed, "blame", 0, C + "hh.honest"), 48);
        check(Avail(walls, hh) && !Rules.IsRemote(walls) && walls.InteractionHub == "jannah.presence" && !string.IsNullOrWhiteSpace(walls.Entry),
            "Trk_Jannah_Spine: the wall does not follow Houndheart on her cell hub.");
        var freeze = walls.Nodes.Single(n => n.Id == "freeze").Choices;
        check(freeze.Count == 3 && freeze.All(c => c.Set.Length == 1), "Trk_Jannah_Wall: the pivot is not three answers, each recorded.");
        var walled = Later(story, Take(walls, hh, "freeze", 2, C + "walls.watched"), 24);
        check(Avail(challenge, walled) && Avail(pages.Single(p => p.Id == P + "epilogue.commit"), World(story, 6, "trickster.ever", C + "walls")),
            "Trk_Jannah_Spine: the challenge does not follow the wall, or the war's end has no late yes.");

        // Trk_Jannah_Commit: her public rematch decides only her record; afterwards she chooses; the Commander's public yield.
        var bout = challenge.Nodes.Single(n => n.Id == "bout").Choices;
        check(bout[0].Check?.Skill == "SkillMobility" && bout[1].Check?.Skill == "SkillAthletics" && bout[2].Next == "no_gift"
              && challenge.Nodes.Single(n => n.Id == "no_gift").Choices.Single().Next == "bout_again"
              && challenge.Nodes.Single(n => n.Id == "bout_again").Choices[2].Set.Contains(P + "threw_the_bout"),
            "Trk_Jannah_Commit: the bout is not Mobility or Athletics, or a thrown line is not refused once and then her no.");
        check(!challenge.Nodes.Any(n => n.Text.Contains("you're mine")) && challenge.Nodes.Where(n => n.Id != "yes").All(n => n.Choices.All(c => !c.Set.Contains(Committed)))
              && challenge.Nodes.Single(n => n.Id == "yes").Choices.Take(2).All(c => c.Set.Contains(Committed)),
            "Trk_Jannah_Commit: somebody is won by the bout (the yes is not hers, after it).");
        var paths = Program.Walk(challenge, walled).ToList();
        var won = paths.Where(r => r.Has(P + "bout.commander_first") && r.Has(Committed)).ToList();
        var lostBout = paths.Where(r => r.Has(P + "bout.her_first") && r.Has(Committed)).ToList();
        check(won.Count > 0 && won.All(r => r.Has(FirstLoss)) && lostBout.Count > 0 && lostBout.All(r => r.Has(P + "cost.public_yield")),
            "Trk_Jannah_Commit: her yes does not follow either outcome, or her win does not lay the Commander down in public.");
        foreach (var cause in new[] { P + "threw_the_bout", P + "shamed_her", P + "refused_the_yield" })
            check(paths.Any(r => r.Has(cause)) && paths.Where(r => r.Has(cause)).All(r => r.Has(P + "declined") && !r.Has(Committed) && !r.Has(Closed)),
                "Trk_Jannah_Commit: the Commander's failure " + cause + " is not her no (with a later yes kept).");
        check(paths.Where(r => r.Has(Closed)).All(r => r.Has(P + "gone") && !r.Has(Committed)), "Trk_Jannah_Commit: a close other than the Commander's refusal.");
        check(Avail(night, Later(story, won[0], 8)) && night.Nodes.Any(n => n.Id == "cut") && !Rules.IsRemote(night) && night.InteractionHub == "jannah.presence",
            "Trk_Jannah_Night: the chalked circle does not follow the commit, or has no cut.");
        var nighted = Later(story, Program.Walk(night, Later(story, won[0], 8)).First(r => r.Has(night.Id)), 6);
        check(Avail(morning, nighted), "Trk_Jannah_Morning: the morning does not follow the night.");

        // Trk_Jannah_Lie: the false catch named at the challenge; kept, she fights and then says no; the circle in the yard after.
        var liar = World(story, 5, "trickster.ever", Returned, "jannah.started", FirstLoss, P + "alive.false_blood",
                         "trickster.secret.jannah_false_blood", C + "forms", C + "houndheart", C + "walls");
        check(Avail(challenge, liar) && Program.Walk(challenge, liar).Any(r => r.Has(P + "confessed") && r.Has(Committed)),
            "Trk_Jannah_Lie: confessing does not lead to the bout and her yes.");
        var kept = Program.Walk(challenge, liar).Where(r => r.Has(P + "held_the_lie")).ToList();
        check(kept.Count > 0 && kept.All(r => !r.Has(Committed) && !r.Has(Closed) && r.Has("trickster.secret.jannah_false_blood.known.jannah"))
              && kept.Any(r => r.Has(P + "declined") && (r.Has(P + "bout.commander_first") || r.Has(P + "bout.her_first"))),
            "Trk_Jannah_Lie: a kept lie does not end in her no after a fought bout, with the secret known.");
        var no = kept.First(r => r.Has(P + "declined"));
        check(!Avail(chalk, Later(story, no, 48)) && Avail(chalk, Later(story, no, 72)),
            "Trk_Jannah_Lie: the chalk circle is not left in the yard.");
        var circle = chalk.Nodes.Single(n => n.Id == "open").Choices;
        check(circle.Count == 5 && circle[0].Requires.Contains(P + "held_the_lie") && circle[1].Requires.Contains(P + "threw_the_bout")
              && circle[2].Requires.Contains(P + "shamed_her") && circle[3].Requires.Contains(P + "refused_the_yield")
              && circle.Take(4).All(c => c.Set.Contains(Committed) && c.Crusade == null) && circle[4].Set.Contains(Closed),
            "Trk_Jannah_Circle: the circle is not one unpriced answer per failure, and a parting.");
        check(Through(chalk, Later(story, no, 72), "open", 0).All(r => r.Has(Committed) && r.Has(P + "confessed"))
              && Take(chalk, Later(story, no, 72), "open", 4, Closed).Has(P + "gone"),
            "Trk_Jannah_Lie: the circle is not a yes (walked into with the truth) or a parting (left).");
        foreach (var (cause, index) in new[] { (P + "threw_the_bout", 1), (P + "shamed_her", 2), (P + "refused_the_yield", 3) })
        {
            var failed = World(story, 5, "trickster.ever", Returned, P + "declined", cause, C + "walls");
            check(Avail(chalk, failed) && Through(chalk, failed, "open", index).All(r => r.Has(Committed)),
                "Trk_Jannah_Circle: no later yes after " + cause);
        }
        check(Avail(night, Later(story, Take(chalk, Later(story, no, 72), "open", 0, Committed), 8)),
            "Trk_Jannah_Lie: the late yes has no night.");

        // Pages: effect-free Chapter 6 pages.
        check(pages.Length == 4 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null && c.Mythic == null))),
            "The pages are not four effect-free Chapter 6 pages.");
        check(Avail(pages.Single(p => p.Id == P + "epilogue.first_blood"), World(story, 6, "trickster.ever", Committed))
              && !Avail(pages.Single(p => p.Id == P + "epilogue.commit"), World(story, 6, "trickster.ever", Committed, C + "walls"))
              && Avail(pages.Single(p => p.Id == P + "epilogue.declined"), World(story, 6, "trickster.ever", P + "declined"))
              && Avail(pages.Single(p => p.Id == P + "epilogue.gone"), World(story, 6, "trickster.ever", P + "gone", Closed)),
            "The pages do not follow the commit, the late yes, her no and her leaving.");

        // Reactions: Irabeth and the King (the allocated pair), and Seelah (a named stake), each behind its guard.
        check(reactions.Length == 12 && reactions.All(r => r.Nodes.Count == 1)
              && reactions.Select(r => r.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Irabeth", "Seelah", "Thaberdine" })
              && reactions.Where(r => r.Owner == "Irabeth").All(r => r.AnswerLists.SequenceEqual(new[] { IrabethHub })
                                                                     && r.Forbids.Contains("irabeth_dead") && r.ForbidOverrides["irabeth_dead"] == "irabeth.trickster.returned")
              && reactions.Where(r => r.Owner == "Seelah").All(r => r.AnswerLists.SequenceEqual(new[] { SeelahHub })
                                                                    && r.Forbids.Contains("seelah_dead") && r.ForbidOverrides["seelah_dead"] == "seelah.trickster.returned"
                                                                    && r.Forbids.Contains("seelah_gone") && r.ForbidOverrides["seelah_gone"] == "seelah.trickster.returned")
              && reactions.Where(r => r.Owner == "Thaberdine").All(r => r.AnswerLists.SequenceEqual(new[] { KingC5 }) && r.NativeReturnCue != null
                                                                        && r.Forbids.Contains("fool_king.gone") && r.Requires.Contains("fool_king.available")),
            "The reactions are not exactly Irabeth, Seelah and the King behind their guards.");
        // Q6 r5 (CAN): Irabeth's appeal account is the Condemned history only (ktc_DeserterJoins/Cue_0013-0014).
        check(S(P + "react.irabeth_wagon").Requires.Contains("jannah.condemned") && S(P + "react.irabeth_wagon_free").Forbids.Contains("jannah.condemned"),
            "Irabeth recalls an appeal Jannah never made.");
        var seelahKnown = World(story, 5, "trickster.ever", Returned, DeadKnown, C + "seelah.herself");
        check(Avail(S(P + "react.seelah_known"), seelahKnown) && !Avail(S(P + "react.seelah_unknown"), seelahKnown)
              && !Avail(S(P + "react.seelah_known"), World(story, 5, "trickster.ever", Returned, DeadKnown, C + "seelah.kept"))
              && !Avail(S(P + "react.seelah_known"), World(story, 5, "trickster.ever", Returned, DeadKnown, C + "seelah.herself", "seelah_dead"))
              && Avail(S(P + "react.seelah_known"), World(story, 5, "trickster.ever", Returned, DeadKnown, C + "seelah.herself", "seelah_dead", "seelah.trickster.returned")),
            "Seelah speaks before Jannah faced her, over her own death, or not after her own return.");

        // The Ledger secret: the false catch, unknown to her until she names it.
        var ledger = story.Books["trickster.ledger"];
        var secret = ledger.Entries.SingleOrDefault(e => e.Id == "secret.jannah_false_blood");
        check(secret != null && secret.Section == "Secrets" && secret.Requires.SequenceEqual(new[] { "trickster.secret.jannah_false_blood" })
              && secret.Lines.Single().Forbids.SequenceEqual(new[] { "trickster.secret.jannah_false_blood.known.jannah" }),
            "The false catch is not a Ledger secret unknown to Jannah until she names it.");

        // Seelah's own word on her, after the Q3 that returned her (additive: the last choice of an existing node, gated).
        var souls = S("seelah.souls");
        var grief = souls.Nodes.Single(n => n.Id == "grief").Choices;
        check(grief.Count == 3 && grief[0].Next == "elan" && grief[1].Next == "survived" && grief[2].Next == "jannah"
              && grief[2].Requires.SequenceEqual(new[] { "jannah.joined" }) && souls.Nodes.Any(n => n.Id == "jannah"),
            "Seelah's Q3 aftermath does not acknowledge Jannah, or the addition is not appended and gated.");

        // The courtship: every optional beat reachable in some world.
        var courtship = own.Where(s => s.Id.StartsWith(C, StringComparison.Ordinal) && s.Optional).ToArray();
        check(courtship.Length >= 27 && courtship.All(s => s.Requires.Contains("trickster.ever")),
            "The courtship is missing beats, or a beat is not a Trickster-path scene.");
        var deep = new[]
        {
            World(story, 5, "trickster.ever", Returned, "jannah.started", Dead, "jannah.dead.latched", Primed, P + "cost.temple_scar", FirstLoss, C + "forms", C + "houndheart", C + "walls",
                  C + "mivon", C + "mivon.truth"),
            World(story, 5, "trickster.ever", Returned, "jannah.started", "jannah.joined", "jannah.condemned", P + "alive.caught_her", FirstLoss, C + "forms", C + "houndheart", C + "walls"),
            World(story, 5, "trickster.ever", Returned, "jannah.started", P + "alive.posted", P + "cost.story_lost", P + "cost.posting", C + "forms"),
            World(story, 5, "trickster.ever", Returned, "jannah.started", P + "alive.caught_her", FirstLoss, C + "forms", C + "houndheart", C + "walls",
                  Committed, P + "bout.commander_first", P + "circle_night"),
            World(story, 5, "trickster.ever", Returned, "jannah.started", Dead, "jannah.dead.latched", Primed, P + "cost.temple_scar", FirstLoss, C + "forms", C + "houndheart", C + "walls",
                  Committed, P + "bout.her_first", P + "cost.public_yield", P + "circle_night"),
        };
        foreach (var beat in courtship)
            check(deep.Any(w => Reaches(w, beat.Id)), "Courtship beat unreachable in every test world: " + beat.Id);

        // Quality pass Q6 (INT): joining Q3 is not finishing it. The joined letter waits for the souls to come home.
        var joinedOpen = World(story, 5, "trickster", "trickster.ever", "jannah.joined", "jannah.condemned", "seelah.q3_started");
        check(!Avail(letter, joinedOpen) && Avail(letter, World(story, 5, "trickster", "trickster.ever", "jannah.joined", "jannah.condemned", "seelah.q3_started", "seelah.souls_returned")),
            "The joined letter arrives while Q3 is unfinished.");
        check(!letter.Nodes.Single(n => n.Id == "joined").Text.Contains("parole", StringComparison.Ordinal),
            "The joined letter invents a parole term.");
        // Quality pass Q6 (BEL): the night names a lost record only if she lost one.
        var nightLost = World(story, 5, "trickster.ever", Returned, "jannah.started", Committed, P + "bout.commander_first", FirstLoss);
        var nightKept = World(story, 5, "trickster.ever", Returned, "jannah.started", Committed, P + "bout.her_first", P + "cost.public_yield");
        HashSet<string> NightPages(Snapshot w) { var seen = new HashSet<string>(); Program.Walk(night, w, (page, _) => seen.Add(page)); return seen; }
        check(Avail(night, nightLost) && NightPages(nightLost).Contains("record_lost") && !NightPages(nightLost).Contains("record_kept")
              && Avail(night, nightKept) && NightPages(nightKept).Contains("record_kept") && !NightPages(nightKept).Contains("record_lost")
              && !night.Nodes.Single(n => n.Id == "close").Text.Contains("any more", StringComparison.Ordinal),
            "The night tells an undefeated Jannah that she lost her record.");
        // Quality pass Q6 (BEL): her answer to Irabeth counts the muster only after it.
        var answer = S(C + "the_answer");
        check(answer.Requires.Contains(P + "challenge"), "Her answer counts a muster she has not fought.");
        // Quality pass Q6 (COX): the romance pages survive a Last Call return that is not a cheated death.
        var fb = pages.Single(p => p.Id == P + "epilogue.first_blood");
        var ec = pages.Single(p => p.Id == P + "epilogue.commit");
        check(fb.ForbidOverrides["sacrifice"] == "trickster.commander_back" && ec.ForbidOverrides["sacrifice"] == "trickster.commander_back",
            "A romance page keys survival on the retired cheated_death.");
        check(!fb.Nodes.SelectMany(n => n.Paragraphs).Any(q => q.Text.Contains("accident", StringComparison.Ordinal)),
            "The yearly bouts are thrown in secret.");
        // Quality pass Q6 (BEL): the declined page names only the refusal that happened.
        var dec = pages.Single(p => p.Id == P + "epilogue.declined");
        check(!dec.Nodes[0].Text.Contains(" lie", StringComparison.Ordinal)
              && new[] { P + "held_the_lie", P + "threw_the_bout", P + "shamed_her", P + "refused_the_yield" }
                  .All(f => dec.Nodes[0].Paragraphs.Count(q => q.Requires.SequenceEqual(new[] { f })) == 1),
            "The declined page blames a lie that may not have been told.");
        // Q6 follow-up (INT/COX): no progression scene is a mod-menu read; her letter is her one Chapter 5 rest delivery (tier A),
        // and the device's other pages are met in person in her cell.
        var rest5 = story.Scenes.Where(s => s.Relationship == "jannah" && Rules.IsMailbagLetter(s) && s.Chapters.Contains(5)).Select(s => s.Id).OrderBy(x => x, StringComparer.Ordinal).ToArray();
        check(rest5.Contains(P + "alive.letter") && rest5.All(id => id == P + "alive.letter" || id == P + "killed.yield")
              && letter.Forbids.Contains(Dead) && letter.Forbids.Contains(DeadKnown),
            "Tier A: Jannah has more than one Chapter 5 rest delivery in a world (" + string.Join(", ", rest5) + ").");
        foreach (var (scene, hubKey) in new[] { (stories, "jannah.presence.cells"), (wagon, "jannah.presence.back"), (walls, "jannah.presence"),
                                                (night, "jannah.presence"), (chalk, "jannah.presence"), (challenge, "jannah.presence") })
            check(!Rules.IsRemote(scene) && !scene.ManualOnly && scene.InteractionHub == hubKey && !string.IsNullOrWhiteSpace(scene.Entry),
                "A progression scene is not met in person on her hub: " + scene.Id);
        var cellsP = story.Presences["jannah.presence.cells"];
        var backP = story.Presences["jannah.presence.back"];
        var mainP = story.Presences["jannah.presence"];
        var justIn = Take(letter, World(story, 5, "trickster", "trickster.ever", "jannah.free", "coronation.seen", "seelah.houndheart_seen"), "sign", 0, P + "alive.in_cells");
        check(!Rules.PresenceWanted(cellsP, Later(story, justIn, 11)) && Rules.PresenceWanted(cellsP, inCells) && !Rules.PresenceWanted(mainP, inCells)
              && !Rules.PresenceWanted(backP, inCells),
            "Her cell presence does not wait for her letter's twelve hours, or another of her presences stands with it.");
        check(!Rules.PresenceWanted(cellsP, Later(story, posted, 1)) && !Rules.PresenceWanted(backP, Later(story, posted, 35))
              && Rules.PresenceWanted(backP, Later(story, posted, 36)) && !Rules.PresenceWanted(mainP, Later(story, posted, 36))
              && Rules.PresenceWanted(mainP, Later(story, home, 1)) && !Rules.PresenceWanted(backP, Later(story, home, 1)),
            "She stands in her cell while the wagon has her, or is not back in it when the wagon returns.");

        // Q6 follow-up (COX, hard): the Last Call coda Requires her real committed flag. A woman refused at the muster, gone from
        // the yard, or killed at the cage has no coda; reaching the wall (late_committed) is not a romance.
        var coda = S("jannah.lastcall.page");
        check(coda.Requires.Contains(Committed) && coda.RequiresAnyGroups.Length == 0 && coda.Forbids.Contains(P + "gone"),
            "Her Last Call coda does not Require her committed flag.");
        check(Avail(coda, World(story, 6, "trickster.ever", "lastcall.active", Committed, C + "walls")),
            "Her Last Call coda does not play for a committed Jannah.");
        foreach (var (why, flags) in new (string, string[])[]
        {
            ("refused at the muster", new[] { C + "walls", Closed, P + "gone" }),
            ("gone from the chalk circle", new[] { C + "walls", P + "declined", P + "threw_the_bout", Closed, P + "gone" }),
            ("left to the wagon", new[] { Closed, P + "gone" }),
            ("killed at the cage", new[] { Dead, "jannah.dead.latched" }),
            ("killed at the cage, Seelah told", new[] { DeadKnown, "jannah.dead.latched" }),
            ("unfinished after the wall", new[] { C + "walls" }),
        })
            check(!Avail(coda, World(story, 6, new[] { "trickster.ever", "lastcall.active" }.Concat(flags).ToArray())),
                "Her Last Call coda plays although she is " + why + ".");
        // Played through: each muster refusal, then its chalk-circle yes, then Chapter 6 with Last Call (declined stays set).
        foreach (var (cause, index) in new[] { (P + "held_the_lie", 0), (P + "threw_the_bout", 1), (P + "shamed_her", 2), (P + "refused_the_yield", 3) })
        {
            var before = cause == P + "held_the_lie" ? Later(story, no, 72) : World(story, 5, "trickster.ever", Returned, P + "declined", cause, C + "walls");
            foreach (var reconciled in Through(chalk, before, "open", index))
            {
                var end = World(story, 6, reconciled.Flags.Where(f => f != "chapter_later").Concat(new[] { "lastcall.active" }).ToArray());
                check(end.Has(Committed) && end.Has(P + "declined") && !end.Has(Closed) && !end.Has(P + "gone") && Avail(coda, end),
                    "Her Last Call coda is lost after the chalk-circle yes that answered " + cause + ".");
            }
        }
        var codaParas = coda.Nodes[0].Paragraphs;
        check(codaParas.Where(q => q.Text.Contains("north wall", StringComparison.Ordinal)).All(q => q.Requires.Contains(C + "walls.saluted"))
              && codaParas.Count(q => q.Requires.Contains("jannah.lastcall.called")) == 2
              && !S("jannah.lastcall.call").Nodes.Any(n => n.Text.Contains(" a wall", StringComparison.Ordinal) || n.Text.Contains("north wall", StringComparison.Ordinal) || n.Text.Contains("Mivon words", StringComparison.Ordinal)),
            "The Last Call call or coda recalls a wall salute the Commander never called.");

        Console.WriteLine("PASS: Jannah Trickster (Trk_Jannah_*): the forms at the cage, the ash, the unclaimed yield, blood and tale in six living worlds, the false catch and the wagon, "
                          + "the forms, Houndheart, the wall, her challenge, the chalk circle, the night, the pages, the reactors, the secret, Seelah's word, and "
                          + courtship.Length + " courtship beats.");
    }
}
