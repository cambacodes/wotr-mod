using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Melazmera, Trickster (Writer/handoffs/trickster/melazmera.md; binding plan 11-ROSTER-PLAN-2 §2, Melazmera block and build
// sheet, R5): "Salt the hoard". One block per rules test (Trk_Melazmera_*): the plan on the Fulsome Queen's list, the salt
// (Thievery twins, the grey fingers), the hunt on Colyphyr or found in the Abyss, the kill that stands, the message (Greybor
// paid in advance, or the stone through the shutter), her hunger and its secret, the commit (a theft she allows), the crown
// and the shared hunt, the heap and its morning, the reactors, the letters in stone and the night visits, and the pages.
internal static class MelazmeraTricksterTests
{
    private const string P = "melazmera.trickster.";
    private const string Committed = "melazmera.committed";
    private const string Closed = "melazmera.closed";
    private const string Started = "melazmera.started";
    private const string Dead = "melazmera.dead.latched";
    private const string Colyphyr = "c876d5303f4a19f4a80b0cc9b313db6f";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string QueenList = "5c08af90f48f60b42b9f14ab0e0e3220";
    private const string QueenHub = "a39dd7d45c635304f9e8404c78a340c3";
    private const string GreyborList = "174d6c94b6725f44aad1d2a76993a926";
    private const string Told = "melazmera.hoard_told";
    private const string Lifted = "melazmera.illusion_lifted";
    private const string Plan = P + "plan";
    private const string Salted = P + "salted";
    private const string Seal = P + "cost.seal_given";
    private const string GreyHand = P + "cost.grey_hand";
    private const string Returned = P + "returned";
    private const string Carried = P + "greybor_carried";
    private const string Message = P + "message";
    private const string Fed = P + "fed";
    private const string Secret = "trickster.secret.melazmera_cultists";
    private const string Declined = P + "declined";
    private const string Hunted = P + "hunted";
    private const string Lashed = P + "cost.lashed";
    private const string StoneKept = P + "stone_kept";
    private const string LeftFree = P + "left_free";
    private const string Mistake = P + "mistake";
    private const string Heap = P + "heap_seen";
    private const string Wary = P + "greybor_wary";
    private const string Ch5 = "melazmera.ch5.latched";

    private static Snapshot World(Story story, int chapter, string area, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = area };
        state.Flags.UnionWith(flags);
        // These positive predicate fixtures represent an already accepted route.
        // Coarse-key negatives are independent in PayoffDepartureRulesTests.
        foreach (var rel in story.Relationships)
            if (flags.Contains(rel.Value.CommittedFlag) && story.Derived.ContainsKey(rel.Key + ".payoff.ordinary"))
                HouseholdTests.Earn(story, state, rel.Key + ".payoff.ordinary");
        // Native ending/Last Call checkpoint flags expand to their actual sources.
        foreach (var context in flags.Where(story.Derived.ContainsKey))
            HouseholdTests.Earn(story, state, context);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 300;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, string? area = null, int? chapter = null)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        if (area != null) later.Area = area;
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
        // Every outcome of a scene with the exact edges taken to reach it (only choices whose gates hold; a check branches
        // to both outcomes).
        List<(Snapshot state, List<(string node, int index)> path)> Paths(Scene scene, Snapshot initial)
        {
            var outcomes = new List<(Snapshot, List<(string, int)>)>();
            void Visit(string id, Snapshot state, List<(string, int)> path)
            {
                var node = scene.Nodes.Single(n => n.Id == id);
                for (int i = 0; i < node.Choices.Count; i++)
                {
                    var choice = node.Choices[i];
                    if (!Rules.Match(choice.Requires, choice.Forbids, state)) continue;
                    var next = Program.Copy(state);
                    foreach (var effect in choice.Set)
                        if (next.Flags.Add(effect)) next.Times[effect] = next.Hour;
                    var edge = new List<(string, int)>(path) { (id, i) };
                    if (choice.Next != null || choice.Check != null)
                        foreach (var target in Rules.NextNodes(choice)) Visit(target, Program.Copy(next), edge);
                    else
                    {
                        if (!choice.Abort) { next.Flags.Add(scene.Id); next.Times[scene.Id] = next.Hour; }
                        outcomes.Add((next, edge));
                    }
                }
            }
            Visit(scene.Nodes[0].Id, initial, new List<(string, int)>());
            return outcomes;
        }
        Snapshot Take(Scene scene, Snapshot w, string node, int index, params string[] also)
        {
            check(Avail(scene, w), "Not available before taking " + scene.Id + "/" + node + "[" + index + "]");
            var hit = Paths(scene, w).Where(o => o.path.Contains((node, index))).Select(o => o.state).FirstOrDefault(r => also.All(r.Has));
            check(hit != null, "No outcome of " + scene.Id + " through " + node + "[" + index + "] with " + string.Join(", ", also));
            if (hit == null) return w;
            Rules.Complete(story, hit);
            return hit;
        }

        var rel = story.Relationships["melazmera"];
        var own = story.Scenes.Where(s => s.Relationship == "melazmera" && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var pages = story.Scenes.Where(s => s.Relationship == "melazmera" && s.Owner == "MelazmeraEpilogue").ToArray();
        var plan = S(P + "ch4.plan");
        var salt = S(P + "ch4.salt");
        var hunt = S(P + "ch4.hunt");
        var found = S(P + "ch4.hunt_found");
        var queenAfter = S(P + "ch4.queen_after");
        var oldHoard = S(P + "ch4.old_hoard");
        var first = S(P + "stone.first");
        var second = S(P + "stone.second");
        var msgA = S(P + "ch5.message");
        var msgB = S(P + "ch5.message_b");
        var read = S(P + "ch5.message_read");
        var letter = S(P + "ch5.message_letter");
        var hunger = S(P + "ch5.hunger");
        var commit = S(P + "commit.stone");
        var shared = S(P + "hunt.shared");
        var heap = S(P + "visit.heap");
        var after = S(P + "react.greybor_after");
        var coly = S(P + "react.greybor_colyphyr");
        var nenio = S(P + "react.nenio_specimen");

        // Trk_Melazmera_Bindings: the build sheet's keys, bound as listed (tools/verify-game-bindings.py resolves every GUID).
        check(rel.StartedFlag == "melazmera.started" && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.SequenceEqual(new[] { Dead, P + "left_free" }) && rel.UnavailableOverrides.Count == 0
              && rel.TricksterAccess.Keys.SequenceEqual(new[] { "alive" }) && rel.TricksterAccess["alive"].Device == P + "ch4.salt",
            "Melazmera's relationship does not match the plan (the kill stands; one device, the salt).");
        check(story.SeenCues[Told].OrderBy(g => g).SequenceEqual(new[] { "87aeec42d8aa3544093e3ff144a12e06", "ee90b60ecefa31f44aeb8a58c1e5ebab" })
              && story.UnlockableFlags[Lifted] == "47359cb2a981461db0c138fdc153bc9f"
              && story.UnlockableFlags["melazmera.illusion_lifted_b"] == "3b2bba05723d42058469f9ecce3c22d0"
              && story.SelectedAnswers["melazmera.harpooned"] == "f35d182506d00494293206a940bb5229"
              && story.SeenCues["melazmera.ate_sailors"].SequenceEqual(new[] { "04805628b9eeb914cb7c5aeea4751596" })
              && story.Etudes["melazmera_dead"] == "fee0f0cf006c96f4f90f895ba8d73d97"
              && story.Latches[Dead].SequenceEqual(new[] { "melazmera_dead" })
              && story.Etudes["melazmera.ch5"] == "5b01aa690202e584888dfc600a4aac0a" && story.Latches[Ch5].SequenceEqual(new[] { "melazmera.ch5" })
              && story.SeenCues["greybor.declined_queen"].SequenceEqual(new[] { "8a7d6895c1e22ac4992e1aa2b47be518" }),
            "Trk_Melazmera_Bindings: a native key is not bound as the build sheet lists it.");
        check(story.Derived["melazmera.harem.eligible"].Select(g => string.Join("+", g)).SequenceEqual(new[] { "melazmera.payoff.ordinary" }),
            "Her household eligibility is not her real commitment alone (no late or transactional key).");
        check(story.Scenes.Where(s => s.Relationship == "melazmera").All(s => !s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g))
                  .Any(f => f.StartsWith("hepzamirah.", StringComparison.Ordinal))),
            "A Melazmera scene gates on Hepzamirah (node variants only).");
        check(!own.Any(s => s.Nodes.Any(n => n.Choices.Any(c => c.Set.Any(f => f.StartsWith("trickster.wmt.use.", StringComparison.Ordinal))))),
            "Melazmera's device spends a Word Made True.");
        check(own.Concat(pages).All(s => s.Requires.Contains("trickster") || s.Requires.Contains("trickster.ever")),
            "Path fit (v1, all T): a Melazmera scene is not Trickster-gated.");
        check(own.Where(s => Rules.IsRemote(s)).All(s => s.Kind != null) && salt.Kind == "event" && first.Kind == "letter" && hunger.Kind == "visit",
            "A remote Melazmera scene does not declare what it is (event, letter, visit).");

        // Trk_Melazmera_Salt: the plan on the Queen's list, the salt at a Colyphyr rest, the hunt at the next.
        var q = World(story, 4, Colyphyr, "trickster", "trickster.ever", Told, "melazmera.queen_contract_offered");
        check(Avail(plan, q) && plan.AnswerLists.SequenceEqual(new[] { QueenList }) && plan.ReturnToList && plan.NativeReturnCue == null
              && plan.EntryMythic == "PlayerIsTrickster" && Ch(plan, "start", 2).Abort && !Avail(plan, World(story, 4, Colyphyr, "trickster", "trickster.ever")),
            "Trk_Melazmera_Salt: the plan is not inline on the Queen's contract list once the hoard's trick is known, with a silent abort.");
        var planned = Take(plan, q, "crown", 0, Plan, P + "queen_promised");
        check(Avail(salt, planned) && !Avail(salt, Later(story, planned, 1, Drezen)) && !Avail(salt, World(story, 4, Colyphyr, "trickster", "trickster.ever"))
              && salt.TricksterDevice && salt.TricksterState == "alive" && salt.Areas.SequenceEqual(new[] { Colyphyr }),
            "Trk_Melazmera_Salt: the salt is not a Colyphyr rest page on the live path, after the plan or the lifted illusion.");
        check(Avail(salt, World(story, 4, Colyphyr, "trickster", "trickster.ever", Lifted)),
            "Trk_Melazmera_Salt: seeing through the illusion alone does not open the salt.");
        var place = salt.Nodes.Single(n => n.Id == "heap").Choices.Where(c => c.Check != null).ToList();
        check(place.Count == 2 && place.All(c => c.Check!.Skill == "SkillThievery" && c.Check.Success == "set" && c.Check.Failure == "brush")
              && place[0].Check!.DC == 22 && place[0].Requires.Contains("melazmera.illusion_seen") && place[1].Check!.DC == 26
              && place[1].Forbids.Contains("melazmera.illusion_seen") && Ch(salt, "heap", 2).Abort
              && salt.Nodes.All(n => n.Choices.All(c => c.Mythic == null)),
            "Trk_Melazmera_Salt: the salt is not Thievery DC 26 (22 once seen through), by hand, with a replayable back-out.");
        var salted = Take(salt, planned, "out", 0, Salted, Seal);
        var grey = Take(salt, planned, "drain", 0, Salted, Seal, GreyHand);
        check(!salted.Has(GreyHand) && Take(salt, planned, "fist", 0, Salted, Seal, GreyHand).Has(P + "fist_closed"),
            "Trk_Melazmera_Salt: the seal is not given on both outcomes, or the failure does not cost the grey fingers.");
        var rest2 = Later(story, salted, 10);
        check(Avail(hunt, rest2) && !Avail(hunt, Later(story, salted, 10, Drezen)) && !Avail(found, rest2),
            "Trk_Melazmera_Salt: the hunt does not come at the next Colyphyr rest.");
        var met = Take(hunt, rest2, "leaves", 0, Returned, Started);
        check(!met.Has(Committed) && Take(hunt, rest2, "name", 3, Returned).Has(P + "terms.rent")
              && Take(hunt, Later(story, grey, 10), "arrive_known", 0, Returned).Has(GreyHand),
            "Trk_Melazmera_Salt: the hunt does not end in her return (owed or rent), whatever the salt cost.");
        // The crew is acknowledged on every native arrival branch.
        var nameNode = hunt.Nodes.Single(n => n.Id == "name");
        check(nameNode.Choices[0].Requires.Contains("melazmera.ate_sailors")
              && nameNode.Choices[1].Requires.Contains("melazmera.harpooned") && nameNode.Choices[1].Forbids.Contains("melazmera.ate_sailors")
              && nameNode.Choices[2].Forbids.Contains("melazmera.ate_sailors") && nameNode.Choices[2].Forbids.Contains("melazmera.harpooned")
              && Take(hunt, Later(story, World(story, 4, Colyphyr, "trickster", "trickster.ever", Salted, Seal, "melazmera.ate_sailors"), 10), "name", 0, Returned).Has(P + "terms.owed")
              && Take(hunt, Later(story, World(story, 4, Colyphyr, "trickster", "trickster.ever", Salted, Seal, "melazmera.harpooned"), 10), "name", 1, Returned).Has(P + "terms.owed")
              && Take(hunt, rest2, "name", 2, Returned).Has(P + "terms.owed"),
            "Trk_Melazmera_Salt: an arrival branch (she ate the crew, the harpoon, the ship got away) has no way through the hunt.");

        // The failed salt is remembered as it happened: the ring held out, or the fist she opened herself.
        var fistSalt = Take(salt, planned, "fist", 0, Salted, Seal, GreyHand, P + "fist_closed");
        check(Take(hunt, Later(story, fistSalt, 10), "arrive_fist", 0, Returned).Has(Returned)
              && !Paths(hunt, Later(story, fistSalt, 10)).Any(o => o.path.Contains(("arrive_known", 0)))
              && !Paths(hunt, Later(story, grey, 10)).Any(o => o.path.Contains(("arrive_fist", 0)))
              && new[] { found, S(P + "ch5.hunt_window") }.All(s => s.Nodes.Any(n => n.Id == "arrive_fist")),
            "The hunt remembers the failed salt wrongly (the offered ring against the closed fist).");
        // The harpy's news tells the Queen's six native outcomes apart.
        var queenBeat = S(P + "beat.queen");
        Snapshot QW(string f) => World(story, 5, Drezen, "trickster", "trickster.ever", Returned, Message, "melazmera.queen_contract_offered", f);
        bool Reaches(string f, string node) => Paths(queenBeat, QW(f)).Any(o => o.path.Any(e => e.node == node));
        check(Reaches("melazmera.fq_betrayed", "turned") && !Reaches("melazmera.fq_retreated", "turned") && Reaches("melazmera.fq_retreated", "withdrew")
              && Reaches("melazmera.fq_sulked", "withdrew") && Reaches("melazmera.fq_attacked", "fought") && Reaches("melazmera.fq_refused", "fought")
              && Reaches("melazmera.fq_disobeyed", "fought") && !Reaches("melazmera.fq_attacked", "turned"),
            "The harpy's news overwrites the Queen's native outcome (betrayal, fight or retreat).");

        // Trk_Melazmera_Found: salted and gone from Colyphyr: she finds the camp in the Abyss after 36 hours.
        var away = Later(story, salted, 12, Drezen);
        // eng7-l12: off-island fallback is read at the Nexus, never on Colyphyr.
        check(!Avail(found, away) && Avail(found, Later(story, salted, 40, "7847c3e3537104f4694167af0b9fcd0e")) && !Avail(found, Later(story, salted, 40, "7847c3e3537104f4694167af0b9fcd0e", 5))
              && Take(found, Later(story, salted, 40, "7847c3e3537104f4694167af0b9fcd0e"), "leaves", 0, Returned).Has(Started)
              && !found.Nodes.Any(n => n.Choices.Any(c => c.Requires.Contains("hepzamirah.dead"))),
            "Trk_Melazmera_Found: the hunt does not find a Commander who left Colyphyr (Chapter 4, off the island's etudes).");

        // Trk_Melazmera_Window: salted in Chapter 4 and never met there: she comes to the window in Drezen in Chapter 5.
        var window = S(P + "ch5.hunt_window");
        var ch5salted = World(story, 5, Drezen, "trickster", "trickster.ever", Salted, Seal, Ch5);
        ch5salted.Times[Ch5] = ch5salted.Hour;
        check(!Avail(window, ch5salted) && Avail(window, Later(story, ch5salted, 40)) && !Avail(window, Later(story, ch5salted, 40, "abyss"))
              && Take(window, Later(story, ch5salted, 40), "leaves", 0, Returned).Has(Started),
            "Trk_Melazmera_Window: a salted Commander who reaches Chapter 5 unmet is not found at the window in Drezen.");
        var afterWindow = Take(window, Later(story, ch5salted, 40), "leaves", 0, Returned);
        var viaWindow = Take(msgB, Later(story, World(story, 5, Drezen, "trickster", "trickster.ever", Returned, "greybor.in_party", Ch5), 1), "start", 0, Carried);
        check(afterWindow.Has(Returned) && viaWindow.Has(Carried),
            "Trk_Melazmera_Window: the window meeting does not lead into her Chapter 5 message.");
        // Chapter 5 night visits stage the citadel: never at a rest outside Drezen.
        check(own.Where(s => s.Chapters.SequenceEqual(new[] { 5 }) && Rules.IsRemote(s) && s.Id != P + "ch5.message_read")
                  .All(s => s.Areas.SequenceEqual(new[] { Drezen })),
            "A Chapter 5 visit or window stone can arrive at a rest outside Drezen.");

        // Trk_Melazmera_KillStands: the canon kill (latched on Colyphyr) closes everything. The kill is the player's own
        // choice at the lair (11 §5 ruling #2, §5.1; matrix user_decision killed_at_colyphyr), not a fate to defy.
        var killed = World(story, 4, Colyphyr, "trickster", "trickster.ever", Told, "melazmera_dead");
        check(killed.Has(Dead) && !own.Any(s => Avail(s, killed))
              && !own.Any(s => Avail(s, World(story, 5, Drezen, "trickster", "trickster.ever", Returned, Message, Fed, Dead)))
              && !pages.Any(s => Avail(s, World(story, 6, Drezen, "trickster", "trickster.ever", Returned, Committed, Dead))),
            "Trk_Melazmera_KillStands: a scene or page survives the canon kill.");
        var mistaken = Take(hunt, rest2, "mistake", 0, Mistake, Closed);
        check(!own.Any(s => Avail(s, Later(story, mistaken, 200, Drezen, 5)))
              && pages.Where(s => Avail(s, Later(story, mistaken, 200, Drezen, 6))).Select(s => s.Id).SequenceEqual(new[] { P + "epilogue.closed" }),
            "Trk_Melazmera_KillStands: [It was a mistake] does not close the route onto its own page.");

        // Chapter 4 after the hunt: the Queen asks, the old cave, the stones through the roof.
        check(Avail(queenAfter, World(story, 4, Colyphyr, "trickster", "trickster.ever", Salted, P + "queen_promised")) && queenAfter.AnswerLists.SequenceEqual(new[] { QueenHub })
              && queenAfter.ReturnToList && !Avail(queenAfter, World(story, 4, Colyphyr, "trickster", "trickster.ever", Salted, "melazmera.fq_betrayed"))
              && Take(queenAfter, World(story, 4, Colyphyr, "trickster", "trickster.ever", Salted, P + "queen_promised"), "shining", 0).Has(P + "queen_crowned"),
            "The Queen's follow-up is not on her hub, or asks after she has turned on the Commander.");
        check(Avail(oldHoard, Later(story, met, 10)) && !Avail(oldHoard, Later(story, met, 10, Drezen)),
            "The old cave by daylight is not a Colyphyr rest visit after the hunt.");
        var st1 = Later(story, met, 30, "abyss");
        check(Avail(first, st1) && !Avail(first, Later(story, met, 10, "abyss")) && first.Chapters.SequenceEqual(new[] { 4 }),
            "The first stone does not come through the roof a day after the hunt, in Chapter 4.");
        var read1 = Take(first, st1, "reply", 2, P + "stone.first_read", P + "stone.reply_question");
        check(!Avail(second, Later(story, read1, 10)) && Take(second, Later(story, read1, 50), "tail", 0).Has(P + "stone.second_read"),
            "The second stone does not answer the first two days later.");

        // Trk_Melazmera_Message: Greybor paid in advance, or a stone through the shutter; both open her hunger.
        var c5 = World(story, 5, Drezen, "trickster", "trickster.ever", Returned, Seal, Salted, "greybor.in_party", Ch5);
        check(Avail(msgB, c5) && !Avail(msgA, c5) && msgB.AnswerLists.SequenceEqual(new[] { GreyborList }) && msgB.Reaction
              && Avail(msgA, World(story, 5, Drezen, "trickster", "trickster.ever", Returned, "greybor.in_party", "greybor.declined_queen", Ch5))
              && !Avail(msgB, World(story, 5, Drezen, "trickster", "trickster.ever", Returned, "greybor.in_party", "greybor.declined_queen", Ch5)),
            "Trk_Melazmera_Message: Greybor does not carry her stone in Chapter 5 (the swamp queen remembered where he turned her down).");
        var carried = Take(msgB, c5, "start", 0, Carried);
        check(Avail(read, carried) && !Avail(letter, Later(story, carried, 100)) && Take(read, carried, "words", 0).Has(Message)
              && !Avail(msgB, Later(story, carried, 1)),
            "Trk_Melazmera_Message: the carried stone is not read at the next rest, once, instead of the window twin.");
        var noGrey = World(story, 5, Drezen, "trickster", "trickster.ever", Returned, Seal, "greybor.dead", Ch5);
        noGrey.Times[Ch5] = noGrey.Hour;
        check(!Avail(msgA, noGrey) && !Avail(msgB, noGrey) && !Avail(letter, noGrey) && !Avail(letter, Later(story, noGrey, 50))
              && Avail(letter, Later(story, noGrey, 80)) && Take(letter, Later(story, noGrey, 80), "words", 0).Has(Message)
              && !Avail(letter, Later(story, World(story, 5, Drezen, "trickster", "trickster.ever", Returned, Seal, "greybor.dead"), 80)),
            "Trk_Melazmera_NoGreybor: without Greybor, the stone through the shutter does not carry her message 72 hours into Chapter 5.");

        // Trk_Melazmera_Secret: her hunger; only the cultists set the Ledger secret; the herd costs Favors.
        var told = Take(read, carried, "words", 0, Message);
        var h = Later(story, told, 50);
        check(Avail(hunger, h) && !Avail(hunger, Later(story, told, 20)),
            "Trk_Melazmera_Secret: her hunger does not come two days after her message.");
        var cult = Take(hunger, h, "cultists_after", 0, Fed, P + "fed.cultists");
        var dem = Take(hunger, h, "demons_after", 0, Fed, P + "fed.demons");
        var herd = Take(hunger, h, "forbid_after", 0, Fed, P + "fed.herd");
        check(cult.Has(Secret) && !dem.Has(Secret) && !herd.Has(Secret)
              && Ch(hunger, "ask", 0).Alignment?.Direction == "Evil" && Ch(hunger, "forbid_after", 0).Crusade?.Resource == "Favors"
              && Ch(hunger, "forbid_after", 0).Crusade?.Amount == -50 && !new[] { cult, dem, herd }.Any(s => s.Has(Closed)),
            "Trk_Melazmera_Secret: the secret is not set only by feeding her the cultists, or the herd does not cost Favors, or a choice closes her.");
        check(story.Scenes.Where(s => s.Relationship == "melazmera").SelectMany(s => s.Nodes).SelectMany(n => n.Choices)
                  .Where(c => c.Set.Contains(Secret)).Count() == 1,
            "Trk_Melazmera_Secret: another choice sets her Ledger secret.");

        // Trk_Melazmera_Commit: a theft she allows. The stone is the yes; the crown and nothing are the player's no.
        var ready = Later(story, dem, 50);
        check(Avail(commit, ready) && !Avail(commit, Later(story, dem, 20)),
            "Trk_Melazmera_Commit: the commit does not come two days after her hunger.");
        var yes = Take(commit, ready, "home", 0, Committed, StoneKept);
        var crown = Take(commit, ready, "crown2", 0, Declined);
        var none = Take(commit, ready, "nothing2", 0, LeftFree, Closed);
        check(!crown.Has(Closed) && !crown.Has(Committed) && Ch(commit, "open", 0).Requires.Contains(Salted),
            "Trk_Melazmera_Commit: the crown closes the route, or the stone does not need the salt.");
        // Trk_Melazmera_Recover: the crown, then the shared hunt (either outcome), then the stone.
        check(!Avail(shared, Later(story, crown, 10)) && Avail(shared, Later(story, crown, 30)),
            "Trk_Melazmera_Recover: the shared hunt does not come a day after the crown.");
        var hunt2 = shared.Nodes.Single(n => n.Id == "wound").Choices[0].Check;
        check(hunt2 != null && hunt2.Skill == "SkillPerception" && hunt2.DC == 24 && hunt2.Success == "spotted" && hunt2.Failure == "missed",
            "Trk_Melazmera_Recover: the shared hunt is not Perception DC 24.");
        var won = Take(shared, Later(story, crown, 30), "stone2", 0, Committed, StoneKept, Hunted);
        var lashed = Take(shared, Later(story, crown, 30), "missed2", 0, Committed, StoneKept, Hunted, Lashed);
        check(!won.Has(Lashed) && Take(shared, Later(story, crown, 30), "leave", 0).Has(LeftFree)
              && Take(shared, Later(story, crown, 30), "bed", 0).Has(Closed),
            "Trk_Melazmera_Recover: a failed hunt costs the chance, or a success costs the lash, or there is no way to walk away.");

        // The heap: the intimacy, the morning, the dogs or Greybor.
        var night = Later(story, yes, 30);
        check(Avail(heap, night) && !Avail(heap, Later(story, yes, 10)) && !Avail(heap, Later(story, crown, 30)),
            "The heap does not follow the commit by a day.");
        var greyIn = Program.Copy(night);
        greyIn.Flags.Add("greybor.in_party");
        var morning = Take(heap, greyIn, "home", 1, Heap);
        check(!Avail(heap, Later(story, morning, 30)) && Avail(after, morning) && Take(after, morning, "start", 0).Has(Wary)
              && after.AnswerLists.SequenceEqual(new[] { GreyborList }),
            "Greybor does not react after the heap (and set his refusal of her coin), once.");
        var dogsWorld = Program.Copy(night);
        dogsWorld.Flags.Add("greybor.dead");
        Rules.Complete(story, dogsWorld);
        check(Take(heap, dogsWorld, "dogs", 0, Heap).Has(Heap) && !Avail(after, Take(heap, dogsWorld, "dogs", 0, Heap)),
            "Without Greybor the stable dogs do not carry the reaction, or his reaction plays anyway.");
        var cut = heap.Nodes.Single(n => n.Id == "cut");

        // Reactors: Greybor on Colyphyr (he turned the contract down), Nenio on the specimen.
        check(Avail(coly, World(story, 4, Colyphyr, "trickster", "trickster.ever", Returned, "greybor.in_party", "greybor.declined_queen"))
              && !Avail(coly, World(story, 4, Colyphyr, "trickster", "trickster.ever", Returned, "greybor.in_party"))
              && !Avail(coly, World(story, 4, Colyphyr, "trickster", "trickster.ever", Returned, "greybor.in_party", "greybor.declined_queen", "greybor.dead")),
            "Greybor's Colyphyr reaction does not need him there when the Queen's contract was offered, alive.");
        check(Avail(nenio, World(story, 5, Drezen, "trickster", "trickster.ever", Fed)) && !Avail(nenio, World(story, 5, Drezen, "trickster", "trickster.ever", Fed, "nenio.dead"))
              && Avail(nenio, World(story, 5, Drezen, "trickster", "trickster.ever", Fed, "nenio.dead", "nenio.trickster.returned", "nenio.trickster.cost.recreated")), // eng8-q8a: existing paid vessel fixture
            "Nenio's reaction is not guarded by her own death and return.");

        // The night visits: after her message, never while she is tired of the Commander (the crown) unless committed after.
        var beats = own.Where(s => s.Id.StartsWith(P + "beat.", StringComparison.Ordinal)).ToArray();
        check(beats.Length >= 12 && beats.All(b => b.Optional && b.Forbids.Contains(Declined) && b.ForbidOverrides[Declined] == Committed
                  && b.Forbids.Contains(LeftFree) && b.Requires.Contains(Message)),
            "A night visit is not optional, or comes after the crown without a commit, or before her message.");
        var busy = Later(story, yes, 60);
        check(beats.Count(b => Avail(b, busy)) >= 1 && !beats.Any(b => Avail(b, Later(story, crown, 60)))
              && beats.Any(b => Avail(b, Later(story, won, 60))),
            "The night visits do not follow the commit (or the recovered commit), or play while she is tired.");

        // Recollections never run ahead of play: the war visit remembers the heap only after it; the seal visit never does.
        check(S(P + "beat.war").Requires.Contains(Heap),
            "A night visit recalls an encounter the player may not have had, or the joke's punchline is not written.");
        // The together page does not assume the Wound closed (Epilogues/Cue_0571): one opening paragraph per ending.
        var together = S(P + "epilogue.together").Nodes[0].Paragraphs;
        check(together.Count(pg => pg.Requires.Contains("ending.wound_closed")) == 1 && together.Count(pg => pg.Forbids.Contains("ending.wound_closed")) == 1,
            "The together page states the Wound's fate unconditionally.");

        // The crew's payment names Greybor only where he carried her stone; the copper is recorded and read.
        var crew = S(P + "beat.crew");
        Snapshot CW(params string[] f) => World(story, 5, Drezen, new[] { "trickster", "trickster.ever", Returned, Message, "melazmera.ate_sailors" }.Concat(f).ToArray());
        var viaGrey = Paths(crew, CW(Carried)).Where(o => o.path.Contains(("ate", 0))).ToList();
        var viaStone = Paths(crew, CW("greybor.dead")).Where(o => o.path.Contains(("ate", 1))).ToList();
        check(viaGrey.Count > 0 && viaGrey.All(o => o.state.Has(P + "beat.crew_paid")) && viaStone.Count > 0 && viaStone.All(o => o.state.Has(P + "beat.crew_paid"))
              && !Paths(crew, CW("greybor.dead")).Any(o => o.path.Contains(("ate", 0))),
            "The crew's payment recalls Greybor's fee in a world where he never carried her stone.");
        check(S(P + "beat.putting_down").Requires.Contains(Heap)
              && S(P + "epilogue.together").Nodes[0].Paragraphs.Any(pg => pg.Requires.Contains(P + "beat.copper_kept")),
            "The kept copper is not read by the ending, or the ending settles how she shares.");

        // No authoring notation reaches the player; aftermaths and recollections follow the branch taken.
        check(story.Scenes.Where(s => s.Relationship == "melazmera").SelectMany(s => s.Nodes)
                  .All(n => !n.Text.Contains("*") && n.Choices.All(c => !c.Text.Contains("*")) && n.Paragraphs.All(pg => !pg.Text.Contains("*"))),
            "Markdown emphasis survives in Melazmera's text.");
        var ill = S(P + "beat.illusion");
        check(ill.Nodes.Single(n => n.Id == "stay").Choices.All(c => c.Next == "after_held"),
            "The illusion's aftermath shows damage from a branch the player did not take.");
        check(Paths(shared, Later(story, crown, 30)).Where(o => o.path.Any(e => e.node == "challenge")).Count() == 0
              && Paths(shared, Later(story, Take(commit, ready, "crown3", 0, Declined), 30)).Any(o => o.path.Any(e => e.node == "challenge")),
            "The shared hunt assigns the Commander an experimental motive the player never gave.");
        check(Reaches(P + "queen_crowned", "crowned") && Reaches(P + "queen_refused_crown", "denied")
              && !Paths(queenBeat, World(story, 5, Drezen, "trickster", "trickster.ever", Returned, Message, "melazmera.queen_contract_offered", P + "queen_promised", P + "queen_crowned"))
                    .Any(o => o.path.Any(e => e.node == "promised")),
            "The harpy's news forgets how the crown was settled.");

        // Pages: one per outcome.
        string[] Shown(params string[] flags) => pages.Where(s => Avail(s, World(story, 6, Drezen, flags))).Select(s => s.Id).ToArray();
        check(Shown("trickster.ever", Returned, Committed, StoneKept, Seal).SequenceEqual(new[] { P + "epilogue.together" })
              // eng7-l13: offering the new late promise needs current Trickster power.
              && Shown("trickster", "trickster.ever", Returned, Fed).SequenceEqual(new[] { P + "epilogue.commit" })
              && !Shown("trickster.ever", Returned, Fed).Contains(P + "epilogue.commit")
              && Shown("trickster.ever", Returned, Declined).SequenceEqual(new[] { P + "epilogue.declined" })
              && Shown("trickster.ever", Returned, LeftFree, Closed).SequenceEqual(new[] { P + "epilogue.left_free" })
              && Shown("trickster.ever", Returned, Committed, Declined, Hunted).SequenceEqual(new[] { P + "epilogue.together" })
              && Shown("trickster.ever", Returned, Committed, "sacrifice").SequenceEqual(new[] { P + "epilogue.mourned" })
              && Shown("trickster.ever", Returned, Committed, "sacrifice", "trickster.commander_back").SequenceEqual(new[] { P + "epilogue.together" })
              && Shown("trickster.ever").Length == 0,
            "Trk_Melazmera_Pages: the pages do not follow her outcome one to one.");
        check(pages.All(pg => pg.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Mythic == null && c.Alignment == null && c.Crusade == null))),
            "An epilogue page carries effects.");

        // Polish C9: commitment alone never earns the heap's promise in mourning.
        var promise = S(P + "epilogue.mourned").Nodes[0].Paragraphs.Single(pg => pg.Requires.Contains(Heap));
        var mournedWithoutHeap = World(story, 6, Drezen, "trickster.ever", Returned, Committed, Seal, "sacrifice");
        var mournedAfterHeap = Program.Copy(mournedWithoutHeap);
        mournedAfterHeap.Flags.Add(Heap);
        check(Avail(S(P + "epilogue.mourned"), mournedWithoutHeap)
              && !Rules.ParagraphVisible(promise, mournedWithoutHeap)
              && Rules.ParagraphVisible(promise, mournedAfterHeap),
            "Mourning recalls the heap promise before the Commander heard it, or loses it afterwards.");

        // Polish C5: the crown gift is not evidence that the Queen survived a later fight.
        foreach (var pageId in new[] { "together", "commit", "declined", "left_free" })
        {
            var crownMemory = S(P + "epilogue." + pageId).Nodes[0].Paragraphs.Single(pg => pg.Requires.Contains(P + "queen_crowned"));
            Snapshot CrownHistory(params string[] extra) => World(story, 6, Drezen,
                new[] { "trickster.ever", P + "queen_crowned" }.Concat(extra).ToArray());
            check(!Rules.ParagraphVisible(crownMemory, World(story, 6, Drezen, "trickster.ever"))
                  && Rules.ParagraphVisible(crownMemory, CrownHistory()),
                "The Queen's crown paragraph lost its earned gift in " + pageId + ".");
            foreach (var combat in new[] { "melazmera.fq_betrayed", "melazmera.fq_attacked", "melazmera.fq_disobeyed", "melazmera.fq_refused" })
                check(!Rules.ParagraphVisible(crownMemory, CrownHistory(combat)),
                    "The Queen's crown paragraph promises survival after " + combat + " in " + pageId + ".");
        }

        // Last Call: her coda reads the real commitment only.
        var coda = story.Scenes.SingleOrDefault(s => s.Id == "melazmera.lastcall.page");
        check(coda != null && coda.Requires.Contains(Committed) && coda.RequiresAnyGroups.All(g => !g.Contains(P + "late_committed")),
            "Her Last Call coda is missing or reads something other than her commitment.");
        var call = story.Scenes.SingleOrDefault(s => s.Id == "melazmera.lastcall.call");
        check(call != null && call.RequiresAnyGroups.Length == 1 && call.RequiresAnyGroups[0].SequenceEqual(new[] { StoneKept })
              && !call.RequiresAnyGroups[0].Contains(Seal),
            "Her Last Call call-in (the sapphire held up) is offered without the stone: seal-only, declined or closed worlds must not see it.");
        var leftFree = S(P + "epilogue.left_free").Nodes[0];
        check(leftFree.Paragraphs.Count(pg => pg.Requires.Contains("ending.wound_closed")) == 1
              && leftFree.Paragraphs.Count(pg => pg.Forbids.Contains("ending.wound_closed")) == 1,
            "The left_free page states the Wound's fate unconditionally.");
    }
}
