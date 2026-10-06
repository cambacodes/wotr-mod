using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Soana, Trickster (Writer/handoffs/trickster/soana.md): the spirits' portion (handover, F17), the knot never checked
// (killed, F17) and crooked luck (missed Chapter 3 window, F13). One block per spec rules test (Trk_Soana_*), plus the
// missed branch's own courtship, the epilogue pages and the registered-route edits.
internal static class SoanaTricksterTests
{
    private const string Unit = "64805abb52739e44280a758f850b300c";
    private const string Wintersun = "0a5654e7dc18f074d9356009d55eb51b";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string HerList = "2b1776f3e398685479ff6b16290b4cc2";
    private const string HerReturn = "e9feb6b2946c77641875f2bc731ede1e";
    private const string Medallion = "4d78ec5dd1d1d5d41b9f2d8f2c8b5d53";
    private const string P = "soana.trickster.";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = chapter == 4 ? "" : Wintersun, Hour = 5000,
            // eng-final / E-Q8-10: fund these positive histories; the walker enforces every debit.
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        if (chapter != 4) state.AvailableContacts.Add(Unit);
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
        var afterQuest = S(P + "handover.after_quest");
        var bearA = S(P + "handover.after_bear_a");
        var bearB = S(P + "handover.after_bear_b");
        var knot = S(P + "killed.knot");
        var graveyard = S(P + "returned.graveyard");
        var terms = S(P + "returned.terms");
        var secondAsk = S(P + "returned.second_ask");
        var accounting = S(P + "returned.accounting");
        var dice = S(P + "missed.dice_bowl");
        var crooked = S(P + "missed.crooked_luck");
        var lateLuck = S(P + "missed.late_luck");
        var sheBear = S(P + "missed.she_bear");
        var bowl = S(P + "missed.bowl");
        var bowlAsk = S(P + "missed.second_ask");
        var epKnot = S(P + "epilogue.knot");
        var epLuck = S(P + "epilogue.luck");
        var epCommit = S(P + "epilogue.commit");
        var epDeclined = S(P + "epilogue.declined");
        var handovers = new[] { afterQuest, bearA, bearB };
        var own = story.Scenes.Where(s => s.Relationship == "soana" && s.Id.StartsWith(P, StringComparison.Ordinal) && !s.Reaction
                                          && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var pages = story.Scenes.Where(s => s.Relationship == "soana" && s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));
        List<Snapshot> Play(Scene scene, Snapshot w) => Program.Walk(scene, w).Where(r => r.Has(scene.Id)).ToList();
        Snapshot Pick(Scene scene, Snapshot w, params string[] flags)
        {
            // Prefer an outcome that keeps the relationship open unless the closing flag is the one asked for.
            var hit = Play(scene, w).Where(r => flags.All(r.Has))
                .OrderBy(r => !flags.Contains("soana.closed") && r.Has("soana.closed") ? 1 : 0).FirstOrDefault();
            check(hit != null, "No outcome of " + scene.Id + " sets " + string.Join(", ", flags));
            return hit ?? w;
        }

        // Polish r4: a save that returned her after the Commander's own kill, before the ruling that such a kill stands.
        Snapshot Legacy(Snapshot w)
        {
            var e = Program.Copy(w);
            foreach (var f in new[] { P + "returned", P + "cost.guardian_paid", P + "cost.leash_held" }) { e.Flags.Add(f); e.Times[f] = e.Hour; }
            Rules.Complete(story, e);
            return e;
        }

        // Plays every available Trickster Soana scene forward and reports whether a flag is ever held.
        bool Reaches(Snapshot start, string flag)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 8 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    if (from.Has(flag)) return true;
                    var w = Later(story, from, 100);
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
        foreach (var s in handovers)
            check(s.NativeReturnCue != null && s.ContactUnit == null && !Rules.IsRemote(s) && s.AnswerLists.Length == 1
                  && s.Chapters.SequenceEqual(new[] { 3 }) && s.EntryMythic == "PlayerIsTrickster"
                  && s.EntryAlignment?.Direction == "Chaotic" && s.TricksterDevice && s.TricksterState == "handover",
                "The handover joke is not an inline Trickster answer on the native handover list: " + s.Id);
        check(afterQuest.AnswerLists.SequenceEqual(new[] { HerList }) && afterQuest.NativeReturnCue == HerReturn
              && bearA.AnswerLists.SequenceEqual(new[] { "001686714a5c2384ba09686b45bd033f" })
              && bearB.AnswerLists.SequenceEqual(new[] { "f7b5537dc61ccdc41b0732f0a1b700b2" }),
            "Handover lists or return cues changed.");
        check(afterQuest.Nodes.Last().Choices.Single().NativeNext == "fef727987297e8d4eb34068688fdac27"
              && bearA.Nodes.Last().Choices.Single().NativeNext == "c6b676fa989a5494cb6ce0c981979907"
              && bearB.Nodes.Last().Choices.Single().NativeNext == "74664ddd7bb36744ba825c29aad6f4b3",
            "The portion does not hand back to the native farewell that resolves the quest.");
        check(bearA.Nodes.Single(n => n.Id == "camellia").SpeakerUnit == "397b090721c41044ea3220445300e1b8"
              && afterQuest.Nodes.All(n => n.Speaker == "Soana"),
            "Camellia speaks where she is not on screen, or is silent where she is.");
        check(knot.Remote && knot.Chapters.SequenceEqual(new[] { 3, 5 }) && knot.TricksterDevice && knot.TricksterState == "killed"
              && knot.Requires.Contains("trickster") && knot.RequiresAnyGroups.Length == 1,
            "The knot is not the live Trickster's Chapter 3 or 5 page.");
        foreach (var s in new[] { graveyard, terms, secondAsk })
            check(s.ContactUnit == Unit && s.Areas.SequenceEqual(new[] { Wintersun }) && s.InteractionHub == "soana.presence"
                  && !Rules.IsRemote(s) && s.Chapters.SequenceEqual(new[] { 3, 5 }),
                "The returned Soana is not met in person at her cave: " + s.Id);
        foreach (var s in new[] { dice, crooked, lateLuck, sheBear, bowl, bowlAsk })
            check(s.AnswerLists.SequenceEqual(new[] { HerList }) && s.NativeReturnCue == HerReturn && s.ContactUnit == null,
                "The missed branch leaves her own list: " + s.Id);
        check(dice.EntryMythic == "PlayerIsTrickster" && lateLuck.EntryMythic == "PlayerIsTrickster" && crooked.EntryMythic == null
              && sheBear.EntryMythic == null && bowl.EntryMythic == null,
            "Only the new tricks carry the Trickster answer; a payoff must stay visible after a lost path.");
        var presence = story.Presences["soana.presence"];
        check(presence.Unit == Unit && presence.Area == Wintersun && presence.Mode == "spawn-copy" && presence.Dialog == "hub"
              && presence.At?.Locator == "cf766aaf-a3a9-490b-ae88-27ebcf6976e6" && presence.MinChapter == 3 && presence.MaxChapter == 5,
            "The presence is not her own copy at the spot where Camellia stood.");
        check(story.RemovableItems.Contains(Medallion) && story.InventoryItems["soana.medallion_held"] == Medallion,
            "The medallion is not a gated removable item.");
        var rel = story.Relationships["soana"];
        foreach (var loss in new[] { "soana.dead", "soana.killed_by_camellia", "soana.forest_dead" })
            check(rel.UnavailableOverrides[loss] == P + "returned", "A return does not lift the loss: " + loss);
        foreach (var s in own.Concat(story.Scenes.Where(x => x.Reaction && x.Id.StartsWith(P, StringComparison.Ordinal))))
            foreach (var key in s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g)))
                check(!key.StartsWith("camellia.trickster", StringComparison.Ordinal) && key != "camellia.committed" && key != "camellia.closed",
                    "Soana reads a Camellia fate: " + s.Id + " " + key);

        // Trk_Soana_Handover: Camellia asked at camp; Soana bleeds for the forest first.
        var asked = World(story, 3, "trickster", "trickster.ever", "camellia.asked_for_soana", "soana.after_quest", "soana.old_defender");
        check(Rules.Available(story, afterQuest, asked) && !Rules.Available(story, knot, asked),
            "Trk_Soana_Handover: the portion is not offered, or the knot is.");
        var portioned = Pick(afterQuest, asked, P + "primed", P + "cost.blood_given");
        check(!portioned.Has("soana.killed_by_camellia") && !portioned.Has("soana.dead") && !Rules.Available(story, afterQuest, portioned),
            "Trk_Soana_Handover: the portion kills her or repeats.");
        check(Rules.Available(story, S("soana.threshold"), Later(story, portioned, 24)),
            "Trk_Soana_Handover: the registered courtship does not open after the portion.");
        check(afterQuest.Nodes.SelectMany(n => n.Choices).Where(c => c.Next == null).All(c => c.Alignment == null),
            "The alignment shift is on the entry, not repeated inside.");

        // Trk_Soana_HandoverNoCamellia.
        check(!Any(World(story, 3, "trickster", "soana.after_quest", "soana.old_defender"), handovers),
            "Trk_Soana_HandoverNoCamellia: the joke plays without Camellia's words.");

        // Trk_Soana_HandoverAfterBearA: Camellia has just spoken in the bear dialog.
        var claimed = World(story, 3, "trickster", "trickster.ever", "camellia.claimed_soana_a");
        check(Rules.Available(story, bearA, claimed) && Rules.Available(story, bearB, claimed),
            "Trk_Soana_HandoverAfterBearA: the bear lists do not offer the portion.");
        Pick(bearA, claimed, P + "primed", P + "cost.blood_given");
        check(!Rules.Available(story, bearA, World(story, 3, "trickster.ever", "trickster.failed", "camellia.claimed_soana_a")),
            "The handover joke is a new trick and needs the live path.");

        // Trk_Soana_Killed: Camellia bled her; the knot read the other way.
        var killed = World(story, 3, "trickster", "trickster.ever", "soana.dead", "soana.killed_by_camellia", "soana.forest_dead");
        check(Rules.Available(story, knot, killed) && !Any(killed, crooked, lateLuck, dice) && !Any(killed, handovers),
            "Trk_Soana_Killed: the knot is unavailable, or a living-Soana scene opens.");
        check(knot.Nodes.Single(n => n.Id == "read").Choices.Count == 3, "The knot's choices changed shape.");
        var raised = Pick(knot, killed, P + "returned", P + "cost.guardian_paid", P + "cost.leash_held");
        check(!raised.Has(P + "cost.medallion_spent"), "Trk_Soana_Killed: a medallion spent that was never held.");
        var raisedLater = Later(story, raised, 48);
        check(Rules.Available(story, graveyard, raisedLater) && !Rules.Available(story, graveyard, Later(story, raised, 47))
              && !Rules.Available(story, terms, raisedLater),
            "Trk_Soana_Killed: the grave test ignores its day, or the terms come first.");
        check(Reaches(raised, "soana.committed"), "Trk_Soana_Killed: no road from the knot to the commit.");
        var left = Pick(knot, killed, "soana.closed");
        check(!left.Has(P + "returned"), "Leaving the knot tied still raises her.");

        // Trk_Soana_KilledMedallion: the Commander's own kill; the medallion was looted.
        var own_kill = World(story, 3, "trickster", "trickster.ever", "soana.dead", "soana.forest_dead", "soana.medallion_held");
        check(Rules.Available(story, knot, own_kill), "Trk_Soana_KilledMedallion: the knot is unavailable.");
        var spent = Pick(knot, own_kill, P + "returned", P + "cost.guardian_paid", P + "cost.medallion_spent");
        var medallionChoice = knot.Nodes.Single(n => n.Id == "read").Choices[0];
        check(medallionChoice.RemoveItem == Medallion && medallionChoice.Requires.Contains("soana.medallion_held")
              && medallionChoice.Mythic == "PlayerIsTrickster" && medallionChoice.Alignment?.Direction == "Chaotic",
            "Trk_Soana_KilledMedallion: the medallion is not spent at the brand.");
        check(Play(knot, own_kill).All(r => !r.Has(P + "returned") || r.Has(P + "cost.medallion_spent")),
            "A held medallion is kept while the knot is read aloud instead.");
        check(Reaches(spent, "soana.committed"), "Trk_Soana_KilledMedallion: no road to the commit.");

        // Trk_Soana_KilledAfterFailure: a lost path loses the new trick; canon stands.
        check(!Rules.Available(story, knot, World(story, 5, "trickster.ever", "trickster.failed", "soana.dead")),
            "Trk_Soana_KilledAfterFailure: the knot outlives the path.");

        // Trk_Soana_Graveyard: the test at the grave.
        var back = World(story, 5, "trickster", "trickster.ever", "soana.dead", P + "returned");
        check(Rules.Available(story, graveyard, back) && !Rules.Available(story, terms, back),
            "Trk_Soana_Graveyard: the grave is closed, or the terms skip it.");
        var awayFromCave = Program.Copy(back); awayFromCave.Area = Drezen;
        check(!Rules.Available(story, graveyard, awayFromCave), "The grave test happens away from her cave.");
        var dug = Pick(graveyard, back, P + "graveyard_kept", P + "cost.grave_dug");
        var bought = Pick(graveyard, back, P + "graveyard_kept", P + "cost.grave_bought");
        check(graveyard.Nodes.SelectMany(n => n.Choices).Any(c => c.Crusade?.Resource == "Finances" && c.Crusade.Amount == -100
              && c.Set.Contains(P + "cost.grave_bought")), "The diggers cost nothing.");
        // Polish (Sol BEL): the accounting comes 72 h after the grave; her invitation there opens the terms 72 h later.
        Snapshot Invite(Snapshot w) => Pick(accounting, Later(story, w, 72), P + "accounting_invited");
        check(Rules.Available(story, accounting, Later(story, dug, 72)) && !Rules.Available(story, accounting, Later(story, dug, 71))
              && !Rules.Available(story, terms, Later(story, dug, 300))
              && Rules.Available(story, terms, Later(story, Invite(dug), 72)) && !Rules.Available(story, terms, Later(story, Invite(dug), 71))
              && Rules.Available(story, terms, Later(story, Invite(bought), 72)),
            "Trk_Soana_Graveyard: the terms ignore their three days.");
        var walked = Pick(graveyard, back, "soana.closed", P + "cost.left_the_grave");
        var gravePages = new HashSet<string>();
        var graveEnds = Program.Walk(graveyard, back, (id, _) => gravePages.Add(id));
        check(gravePages.Contains("decide") && graveEnds.Any(r => r.Has(P + "graveyard_kept") && r.Has("soana.closed")),
            "The grave has no word of hers on what the Commander wants, or no way to leave after digging.");
        check(!Reaches(walked, "soana.committed"), "Walking away from the grave still commits.");

        // Trk_Soana_Terms: her terms, the commit, the night and the morning.
        var atTerms = Later(story, Invite(dug), 72);
        var bound = Pick(terms, atTerms, "soana.committed", P + "cost.knot_bearer");
        var visited = new HashSet<string>();
        foreach (var r in Program.Walk(terms, atTerms, (id, _) => visited.Add(id))) { }
        check(visited.IsSupersetOf(new[] { "start", "dug", "price", "bind", "no", "fool", "night", "morning" }),
            "Trk_Soana_Terms: a page of the terms is unreachable.");
        var boughtPages = new HashSet<string>();
        foreach (var r in Program.Walk(terms, Later(story, Invite(bought), 72), (id, _) => boughtPages.Add(id))) { }
        check(boughtPages.Contains("bought") && !boughtPages.Contains("dug"), "The terms misremember who dug.");

        // NM1 (Sol INT): a luck-chain "not yet" (missed.bowl, the shared declined flag), then her death and return: the knot's own
        // first ask still opens after the graveyard, commits, and its own "not yet" leads to the second ask, not to itself.
        var compound = Program.Copy(atTerms);
        foreach (var f in new[] { P + "declined", P + "luck_kept", P + "luck_tested" }) { compound.Flags.Add(f); compound.Times[f] = compound.Hour - 300; }
        Rules.Complete(story, compound);
        check(Rules.Available(story, terms, compound) && Reaches(compound, "soana.committed"),
            "Trk_Soana_CompoundPostponement: a luck postponement bars the knot's first ask after her return.");
        var compoundNo = Program.Walk(terms, compound).First(r => r.Has(terms.Id) && !r.Has("soana.committed") && !r.Has("soana.closed") && !r.Has(P + "friends"));
        check(!Rules.Available(story, terms, Later(story, compoundNo, 200)) && Rules.Available(story, secondAsk, Later(story, compoundNo, 96)),
            "Trk_Soana_CompoundPostponement: the knot's own 'not yet' repeats the first ask, or never reaches the second.");
        // Trk_Soana_TermsRefused: her soft no, then her second ask: the knot tied tighter (a scar, not a fee).
        var refused = Pick(terms, atTerms, P + "declined");
        check(!refused.Has("soana.committed") && !refused.Has("soana.closed"), "Trk_Soana_TermsRefused: her no closes or commits.");
        check(Rules.Available(story, secondAsk, Later(story, refused, 96)) && !Rules.Available(story, secondAsk, Later(story, refused, 95))
              && !Rules.Available(story, terms, Later(story, refused, 96)),
            "Trk_Soana_TermsRefused: the second ask ignores its days, or the terms repeat.");
        // PP6 (Sol INT): a luck-chain postponement carried into a later death and return does not open the knot's second ask.
        check(!Rules.Available(story, secondAsk, Later(story, World(story, 5, "trickster", "trickster.ever", P + "returned", P + "declined"), 200)),
            "The knot's second ask opens before its graveyard and first ask.");
        var paid = Pick(secondAsk, Later(story, refused, 96), "soana.committed", P + "cost.second_ask");
        var askPages = new HashSet<string>();
        Program.Walk(secondAsk, Later(story, refused, 96), (id, _) => askPages.Add(id));
        check(askPages.IsSupersetOf(new[] { "cut", "night", "morning" }) && SurfaceIds.Has(FullText(epKnot, paid), "[soana.trickster.epilogue.knot/start/paragraph/2]") && !SurfaceIds.Has(FullText(epKnot, bound), "[soana.trickster.epilogue.knot/start/paragraph/2]"),
            "The second ask's deeper cut is priced but never shown or remembered.");
        check(secondAsk.Nodes.SelectMany(n => n.Choices).Any(c => c.Crusade == null && c.Set.Contains(P + "cost.second_ask")
              && c.Set.Contains("soana.committed")), "The second ask is a fee, or leaves no scar.");
        check(Play(secondAsk, Later(story, refused, 96)).Any(r => r.Has("soana.closed") && !r.Has("soana.committed")),
            "The Commander cannot refuse her raised price.");
        var fooled = Pick(terms, atTerms, "soana.closed");
        check(!fooled.Has("soana.committed"), "The Commander's hard no commits.");

        // Trk_Soana_WinterPortion: the blood bargain comes due in person, in Chapter 5, and the Commander may pay it.
        var winter = S(P + "handover.winter_portion");
        var bled = World(story, 5, "trickster", "trickster.ever", P + "cost.blood_given", "soana.after_quest");
        check(Rules.Available(story, winter, Later(story, bled, 72)),
            "Trk_Soana_WinterPortion: the portion never comes due.");
        check(!Rules.Available(story, winter, World(story, 5, "trickster", "trickster.ever", "soana.after_quest")),
            "The portion comes due without a bargain.");
        check(Play(winter, Later(story, bled, 72)).Any(r => r.Has(P + "cost.portion_shared")),
            "The Commander cannot pay the portion.");

        // Trk_Soana_DicePrimer: planted in Chapter 3 on her own list.
        var alive3 = World(story, 3, "trickster", "trickster.ever", "soana.after_quest", "soana.old_defender");
        check(Rules.Available(story, dice, alive3), "Trk_Soana_DicePrimer: the die cannot be offered.");
        var diced = Pick(dice, alive3, P + "primed_dice");
        check(!Rules.Available(story, dice, diced), "The die is offered twice.");
        check(!Rules.Available(story, dice, World(story, 3, "trickster", "soana.after_quest", "soana.old_defender", "soana.dead")),
            "A die is offered to a dead woman.");

        // Trk_Soana_Missed: the die paid for in Chapter 5, then her own courtship.
        var missed = World(story, 5, "trickster", "trickster.ever", "soana.after_quest", "soana.old_defender", P + "primed_dice");
        check(Rules.Available(story, crooked, missed) && !Rules.Available(story, lateLuck, missed) && !Rules.Available(story, knot, missed),
            "Trk_Soana_Missed: the payoff is shut, or the late throw or the knot opens beside it.");
        var lucky = Pick(crooked, missed, P + "luck_kept", P + "cost.catchup");
        check(!lucky.Has("soana.progression_kept"), "The luck pretends the registered visits happened.");
        check(crooked.Nodes.SelectMany(n => n.Choices).Any(c => c.Crusade?.Resource == "Materials" && c.Crusade.Amount == -50
              && c.Set.Contains(P + "luck_kept") && c.Set.Contains(P + "cost.luck_fed")),
            "Trk_Soana_Missed: her beasts do not eat the Commander's luck, or the salt is free.");
        check(Play(crooked, missed).Any(r => r.Has(P + "luck_refused") && !r.Has(P + "luck_kept")), "Her price cannot be refused.");
        check(Rules.Available(story, sheBear, Later(story, lucky, 48)) && !Rules.Available(story, sheBear, Later(story, lucky, 47))
              && !Rules.Available(story, bowl, Later(story, lucky, 48)),
            "The she-bear test ignores its days, or the bowl comes first.");
        foreach (string answer in new[] { P + "answered_rest", P + "answered_roll", P + "answered_cheat" })
        {
            var tested = Pick(sheBear, Later(story, lucky, 48), P + "luck_tested", answer);
            var atBowl = Later(story, tested, 72);
            check(Rules.Available(story, bowl, atBowl) && !Rules.Available(story, bowl, Later(story, tested, 71)),
                "The bowl ignores its days after " + answer);
            var bowlPages = new HashSet<string>();
            var outcomes = Program.Walk(bowl, atBowl, (id, _) => bowlPages.Add(id));
            check(bowlPages.Contains(answer.Substring((P + "answered_").Length)), "The bowl forgets the answer: " + answer);
            check(outcomes.Any(r => r.Has("soana.committed") && r.Has(P + "cost.die_in_her_bowl")), "The bowl cannot commit.");
            check(outcomes.Any(r => r.Has(P + "declined") && !r.Has("soana.committed")), "The bowl has no soft no.");
            check(outcomes.Any(r => r.Has("soana.closed") && !r.Has("soana.committed")), "The die cannot be taken back.");
        }
        check(Reaches(lucky, "soana.committed"), "Trk_Soana_Missed: no road from the luck to the commit.");
        var tested0 = Pick(sheBear, Later(story, lucky, 48), P + "luck_tested");
        var bowlNo = Pick(bowl, Later(story, tested0, 72), P + "declined");
        check(Rules.Available(story, bowlAsk, Later(story, bowlNo, 96)) && !Rules.Available(story, bowl, Later(story, bowlNo, 96)),
            "The missed branch has no priced second ask.");
        check(bowlAsk.Nodes.SelectMany(n => n.Choices).Any(c => c.Crusade == null && c.Set.Contains(P + "cost.pair_given")
              && c.Set.Contains("soana.committed")), "The bowl's second ask does not put the Commander's other die in her keeping (a narrative price: no crusade effect, no claim on combat luck).");
        check(!Rules.Available(story, sheBear, World(story, 5, "trickster", "trickster.ever", "soana.after_quest", "soana.old_defender", "soana.progression_kept")),
            "The missed courtship opens for a Commander who kept the registered visits.");

        // Trk_Soana_MissedLate: no die was planted; it is thrown now, dearer.
        var noDie = World(story, 5, "trickster", "trickster.ever", "soana.after_quest", "soana.bear_dead");
        check(Rules.Available(story, lateLuck, noDie) && !Rules.Available(story, crooked, noDie),
            "Trk_Soana_MissedLate: the late throw is unavailable, or the payoff opens without a die.");
        var thrown = Pick(lateLuck, noDie, P + "primed_dice", P + "cost.late", P + "luck_kept");
        check(lateLuck.Nodes.SelectMany(n => n.Choices).Any(c => c.Crusade?.Resource == "Materials" && c.Crusade.Amount == -100
              && c.Set.Contains(P + "cost.luck_fed")), "Trk_Soana_MissedLate: the late throw is no dearer, or costs no luck.");
        check(!Rules.Available(story, crooked, thrown) && !Rules.Available(story, lateLuck, thrown), "The luck is sold twice.");
        check(Reaches(thrown, "soana.committed"), "Trk_Soana_MissedLate: no road to the commit.");

        // Trk_Soana_MissedAfterFailure: no die and no live trick.
        check(!Any(World(story, 5, "trickster.ever", "trickster.failed", "soana.after_quest", "soana.old_defender"), crooked, lateLuck),
            "Trk_Soana_MissedAfterFailure: a lost path still throws the die.");
        check(!Rules.Available(story, crooked, World(story, 5, "trickster.ever", "trickster.failed", "soana.after_quest", "soana.old_defender",
              P + "primed_dice")), "A planted die completes a return after the path failed.");

        // Epilogue pages: one Soana page per history; the loss pages belong to a Soana who stayed dead.
        Snapshot End(Snapshot s) { var e = Program.Copy(s); e.Chapter = 6; Rules.Complete(story, e); return e; }
        string[] Endings(Snapshot s) => pages.Where(p => Rules.Available(story, p, End(s))).Select(p => p.Id).ToArray();
        var knotEnd = Endings(bound);
        check(knotEnd.SequenceEqual(new[] { epKnot.Id }), "The knot's commit ends on the wrong pages: " + string.Join(",", knotEnd));
        var luckEnd = Endings(Pick(bowl, Later(story, tested0, 72), "soana.committed"));
        check(luckEnd.SequenceEqual(new[] { epLuck.Id }), "The bowl's commit ends on the wrong pages: " + string.Join(",", luckEnd));
        check(Endings(refused).SequenceEqual(new[] { epDeclined.Id }), "Her refusal ends on the wrong pages.");
        var lateBack = Pick(graveyard, back, P + "graveyard_kept");
        // Polish r2 (Sol BEL): the late commit continues her invitation (or a failed presence, R2-6); a bare return gets the
        // unfinished page, never a romance.
        var lateFailed = Program.Copy(lateBack); lateFailed.Flags.Add("soana.presence.failed"); Rules.Complete(story, lateFailed);
        check(Endings(lateBack).SequenceEqual(new[] { P + "epilogue.unfinished" }) && Endings(lateFailed).SequenceEqual(new[] { P + "epilogue.unfinished" })
              && Endings(Invite(dug)).SequenceEqual(new[] { epCommit.Id }),
            "A return never courted gets a romance, or a courted one has no late page: " + string.Join(",", Endings(lateBack)));
        // Polish b9c: a living Soana whose luck was paid gets her own late page, never the killed branch's leash and graves.
        check(Endings(Pick(sheBear, Later(story, lucky, 48), P + "luck_tested")).SequenceEqual(new[] { P + "epilogue.luck_late" }),
            "A luck never committed has no late page, or gets the killed branch's.");
        check(Endings(walked).SequenceEqual(new[] { P + "epilogue.unbound" }), "Walking away from the grave leaves the loose spirit unresolved.");
        // NM1 (Sol COX, R2-6): her Last Call coda accepts the late commit of both fallback histories (the return never
        // brought to terms, the luck never answered) beside the in-play commit; never a refusal, a friend or a postponement.
        var coda = S("soana.lastcall.page");
        Snapshot Called(Snapshot s) { var e = End(s); e.Flags.Add("lastcall.active"); Rules.Complete(story, e); return e; }
        var luckLate = Pick(sheBear, Later(story, lucky, 48), P + "luck_tested");
        check(Rules.Available(story, coda, Called(bound)) && Rules.Available(story, coda, Called(Invite(dug))) && !Rules.Available(story, coda, Called(lateBack)) && Rules.Available(story, coda, Called(luckLate))
              && !Rules.Available(story, coda, End(lateBack)),
            "Trk_Soana_LateLastCall: a late commit (resurrection or luck fallback) has no Last Call coda.");
        var friendBack = Pick(terms, atTerms, P + "friends");
        check(!Rules.Available(story, coda, Called(refused)) && !Rules.Available(story, coda, Called(walked)) && !Rules.Available(story, coda, Called(friendBack))
              && walked.Has(P + "refused") && !lateBack.Has(P + "refused"),
            "Trk_Soana_LateLastCall: a refusal, a friend or a postponement plays her Last Call coda.");
        foreach (var closer in story.Scenes.Where(s => s.Id.StartsWith(P, StringComparison.Ordinal)).SelectMany(s => s.Nodes).SelectMany(n => n.Choices)
                     .Where(c => c.Set.Contains("soana.closed")))
            check(closer.Set.Contains(P + "refused"), "A Trickster-route closure does not keep her out of the Last Call coda: " + SurfaceIds.Of(story, closer));
        check(epDeclined.Nodes[0].Paragraphs.Any(x => x.Requires.Contains(P + "returned") && SurfaceIds.Has(SurfaceIds.Of(story, x), "[soana.trickster.epilogue.declined/start/paragraph/0]")),
            "A killed-branch ending leaves the leash in the Commander's hand.");
        foreach (var loss in new[] { "soana.ending_native_loss", "soana.ending_unfinished_loss" })
            check(S(loss).Forbids.Contains(P + "returned"), "A returned Soana is mourned: " + loss);
        foreach (var page in new[] { epKnot, epLuck, epCommit, epDeclined })
            check(page.Nodes.SelectMany(n => n.Choices).All(c => c.Mythic == null && c.Alignment == null && c.Crusade == null && c.Set.Length == 0),
                "An epilogue page carries effects: " + page.Id);
        foreach (var name in new[] { "kept_life", "chosen_visits", "familiar_company", "sacrifice", "beyond_the_forest" })
            check(S("soana.ending_" + name).Nodes.SelectMany(n => n.Paragraphs).Count(p => p.Requires.Contains(P + "cost.blood_given")) == 1,
                "The portion leaves no mark on the registered ending: " + name);

        // Reactions: exactly Camellia, Ember and Ulbrig, each with its availability guard.
        var reactions = story.Scenes.Where(s => s.Reaction && s.Id.StartsWith(P, StringComparison.Ordinal)).ToArray();
        check(reactions.Length == 7 && reactions.Count(r => r.Id.EndsWith(".history_neutral", StringComparison.Ordinal)) == 1 && reactions.Select(r => r.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Camellia", "Ember", "Ulbrig" }),
            "The reactors are not exactly Camellia, Ember and Ulbrig.");
        foreach (var r in reactions.Where(r => r.Owner == "Ulbrig"))
            check(r.Requires.Contains("ulbrig.talked") && r.Forbids.Contains("ulbrig.dead") && r.Forbids.Contains("ulbrig.kicked_out"),
                "Ulbrig speaks without his dialog or after he is gone: " + r.Id);
        foreach (var r in reactions.Where(r => r.Owner == "Ember"))
            check(r.Forbids.Contains("ember_dead") && r.Forbids.Contains("ember_gone"), "Ember speaks after she is gone: " + r.Id);
        foreach (var r in reactions.Where(r => r.Owner == "Camellia"))
            check(r.Forbids.Contains("camellia.dead") && r.Forbids.Contains("camellia.killed") && r.Forbids.Contains("camellia.kicked_out"),
                "Camellia speaks after she is gone: " + r.Id);
        check(Rules.Available(story, S(P + "react.camellia_knot"), Later(story, World(story, 3, "trickster", "trickster.ever",
              "soana.killed_by_camellia", "soana.dead", P + "returned"), 24)), "Camellia never hears the woman she bled is walking.");
        // Q10 (INT): the knot recalls her words only for a Commander who heard them; otherwise her wall tells it.
        HashSet<string> KnotPages(Snapshot w) { var pagesSeen = new HashSet<string>(); Program.Walk(knot, w, (id, _) => pagesSeen.Add(id)); return pagesSeen; }
        var unheard = KnotPages(killed);
        var heard = KnotPages(World(story, 3, "trickster", "trickster.ever", "soana.dead", "soana.killed_by_camellia", "soana.forest_dead",
                                     "soana.heard_link_b"));
        check(unheard.Contains("marks") && !unheard.Contains("read") && heard.Contains("read") && !heard.Contains("marks"),
            "The knot recalls words the Commander never heard, or hides them from one who did.");
        check(Play(knot, killed).Any(r => r.Has(P + "returned")), "An uninformed Commander cannot read the knot.");
        check(knot.Nodes.Single(n => n.Id == "marks").Choices.Select(c => c.Next).SequenceEqual(new string?[] { "wake_clay", "wake_brand", null }),
            "The uninformed knot skips the test or the bargain.");

        // Q10 (BEL): the clay halves exist only when the medallion was spent; otherwise her hair cord.
        var brandTerms = new HashSet<string>();
        Program.Walk(terms, atTerms, (id, _) => brandTerms.Add(id));
        var clayDug = Pick(graveyard, Later(story, spent, 48), P + "graveyard_kept", P + "cost.grave_dug");
        var clayTerms = new HashSet<string>();
        var clayEnds = Program.Walk(terms, Later(story, Invite(clayDug), 72), (id, _) => clayTerms.Add(id));
        check(!brandTerms.Contains("price_clay") && clayTerms.IsSupersetOf(new[] { "price_clay", "bind_clay", "night_clay" })
              && !clayTerms.Contains("price") && clayEnds.Any(r => r.Has("soana.committed")),
            "The terms show clay shards to a Commander who never broke the medallion, or hide them from one who did.");

        // Q10 (BEL): refusing the late throw's terms is shown; she takes the pledge back off the spirits' plate.
        var lateRefusedPages = new HashSet<string>();
        var lateOutcomes = Program.Walk(lateLuck, noDie, (id, _) => lateRefusedPages.Add(id));
        check(lateRefusedPages.Contains("refused") && lateOutcomes.Any(r => r.Has(P + "luck_refused") && !r.Has(P + "primed_dice")),
            "The late throw's refusal skips the confrontation, or keeps the die in her bowl.");

        // Q10 (INT): a Camellia raised from her retained death hears it on her hub; the veiled (killed) Camellia has no companion
        // hub and answers it in her own route at Fye's (camellia.kill_returned.soana).
        var camelliaBack = Later(story, World(story, 3, "trickster", "trickster.ever", "soana.killed_by_camellia", "soana.dead", P + "returned",
                                              "camellia.trickster.returned"), 24);
        foreach (var id in new[] { P + "react.camellia_knot", P + "react.camellia_portion" })
            check(!S(id).ForbidOverrides.ContainsKey("camellia.dead"),
                "A raised Camellia never hears of Soana: " + id);
        check(Rules.Available(story, S(P + "react.camellia_knot"), camelliaBack), "A raised Camellia never hears of the knot.");
        check(story.Scenes.Any(s => s.Relationship == "camellia" && s.Nodes.Any(n => n.Id == "soana")), "The veiled Camellia never answers Soana's return.");

        // Q10 (INT): the sacrifice. Survived (the punchline) keeps the living pages; stayed dead gets the slack strand.
        var slack = S(P + "epilogue.slack");
        string[] Ends(Snapshot s, params string[] extra)
        {
            var e = End(s); e.Flags.UnionWith(extra); Rules.Complete(story, e);
            return pages.Where(p => Rules.Available(story, p, e)).Select(p => p.Id).ToArray();
        }
        check(Ends(bound, "sacrifice").SequenceEqual(new[] { slack.Id }), "A Commander who stayed dead is remembered as alive: knot.");
        check(Ends(bound, "sacrifice", "ending.trickster").SequenceEqual(new[] { epKnot.Id }), "The punchline Commander loses the knot ending.");
        check(Ends(lateBack, "sacrifice").SequenceEqual(new[] { slack.Id }) && Ends(walked, "sacrifice").SequenceEqual(new[] { slack.Id }),
            "A dead Commander still has the leash taken from a living hand.");
        check(slack.Nodes[0].Paragraphs.Count(x => x.Requires.Contains(P + "luck_kept")) == 1, "The slack page forgets the die.");
        var keptLife = S("soana.ending_kept_life");
        check(keptLife.Forbids.Contains("sacrifice") && keptLife.ForbidOverrides["sacrifice"] == "trickster.commander_back"
              && S("soana.ending_sacrifice").Forbids.Contains("trickster.commander_back"),
            "The registered endings mourn a Commander who came back, or deny them the living page.");

        // Q10 (HOW): the missed branch's second ask takes the other die; it costs no crusade resource and the pair is remembered.
        check(!story.Scenes.Any(s => s.Id.StartsWith(P, StringComparison.Ordinal)
                                     && s.Nodes.Any(n => n.Paragraphs.Any(x => x.Requires.Contains(P + "cost.woods_sealed")))),
            "A page still reads the retired sealed-woods cost.");
        var pairEnd = Pick(bowlAsk, Later(story, bowlNo, 96), "soana.committed", P + "cost.pair_given");
        check(Endings(pairEnd).SequenceEqual(new[] { epLuck.Id }) && epLuck.Nodes[0].Paragraphs.Any(x => x.Requires.Contains(P + "cost.pair_given") && SurfaceIds.Has(SurfaceIds.Of(story, x), "[soana.trickster.epilogue.luck/start/paragraph/3]")),
            "The surrendered pair leaves no mark on the ending.");

        // Q10 r2 (INT/HOW): a lover committed in the registered courtship, then handed to Camellia, then raised by the knot,
        // still has to take the knot's second strand; the knot pages read knot_bearer, not the older commitment.
        var rebind = S(P + "returned.rebind");
        var oldLover = World(story, 3, "trickster", "trickster.ever", "soana.committed", "soana.dead", "soana.killed_by_camellia",
                             "soana.forest_dead");
        var oldRaised = Pick(knot, oldLover, P + "returned");
        check(!oldRaised.Has(P + "cost.knot_bearer"), "The old commitment counts as the knot's vow.");
        var oldDug = Pick(graveyard, Later(story, oldRaised, 48), P + "graveyard_kept", P + "cost.grave_dug");
        var atRebind = Later(story, Invite(oldDug), 72);
        check(!Rules.Available(story, terms, atRebind) && Rules.Available(story, rebind, atRebind)
              && !Rules.Available(story, rebind, Later(story, Invite(oldDug), 71)) && !Rules.Available(story, rebind, Later(story, oldDug, 300)), "A committed lover has no road to the knot's vow.");
        check(Reaches(oldRaised, P + "cost.knot_bearer"), "A committed lover cannot reach knot_bearer from the knot.");
        var rebindPages = new HashSet<string>();
        var rebindEnds = Program.Walk(rebind, atRebind, (id, _) => rebindPages.Add(id));
        check(rebindPages.IsSupersetOf(new[] { "start", "camellia", "price", "night", "morning", "refuse" }) && !rebindPages.Contains("own"),
            "The rebinding forgets who killed her, or skips the vow and the night.");
        var vowed = Pick(rebind, atRebind, P + "cost.knot_bearer", P + "rebind");
        var unvowed = Pick(rebind, atRebind, P + "rebind_declined");
        check(!unvowed.Has(P + "cost.knot_bearer") && !Rules.Available(story, rebind, Later(story, unvowed, 200)),
            "Declining the rebinding still binds, or asks forever.");
        check(Endings(vowed).SequenceEqual(new[] { epKnot.Id }), "The rebound lover ends on the wrong pages: " + string.Join(",", Endings(vowed)));
        check(Endings(unvowed).SequenceEqual(new[] { P + "epilogue.unvowed" }) && Endings(oldRaised).SequenceEqual(new[] { P + "epilogue.unvowed" }),
            "A lover who returned her without the vow ends on the knot page, or on none.");
        var ownKill = World(story, 3, "trickster", "trickster.ever", "soana.committed", "soana.dead", "soana.forest_dead", "soana.killed_self_after_quest");
        var ownRebind = Later(story, Invite(Pick(graveyard, Later(story, Legacy(ownKill), 48), P + "graveyard_kept")), 72);
        var ownPages = new HashSet<string>();
        Program.Walk(rebind, ownRebind, (id, _) => ownPages.Add(id));
        check(ownPages.Contains("own") && !ownPages.Contains("camellia"), "The rebinding blames Camellia for the Commander's own kill.");

        // Q10 r2 (INT): the shared portion's paragraphs follow the Commander's fate.
        var portionWorld = World(story, 6, "trickster", "trickster.ever", "soana.late_campaign_kept", "soana.committed", P + "cost.blood_given",
                                 P + "cost.portion_shared");
        string Visible(string sceneId, Snapshot w) => string.Join("|", Rules.VisibleParagraphs(S(sceneId).Nodes.Last(), w).Select(x => SurfaceIds.Of(story, x)));
        var deadWorld = Program.Copy(portionWorld); deadWorld.Flags.Add("sacrifice"); Rules.Complete(story, deadWorld);
        var backWorld = Program.Copy(deadWorld); backWorld.Flags.Add("ending.trickster"); Rules.Complete(story, backWorld);
        check(Rules.Available(story, S("soana.ending_sacrifice"), deadWorld) && SurfaceIds.Has(Visible("soana.ending_sacrifice", deadWorld), "[soana.ending_sacrifice/start/paragraph/3]")
              && !SurfaceIds.Has(Visible("soana.ending_sacrifice", deadWorld), "[soana.ending_sacrifice/start/paragraph/1]"),
            "The mourning ending sends the dead Commander letters, or forgets the shared portion.");
        check(Rules.Available(story, S("soana.ending_kept_life"), backWorld) && !Rules.Available(story, S("soana.ending_sacrifice"), backWorld)
              && SurfaceIds.Has(Visible("soana.ending_kept_life", backWorld), "[soana.ending_kept_life/start/paragraph/1][soana.ending_kept_life/start/paragraph/3]")
              && SurfaceIds.Has(Visible("soana.ending_kept_life", portionWorld), "[soana.ending_kept_life/start/paragraph/1][soana.ending_kept_life/start/paragraph/3]"),
            "A living Commander loses the shared portion, or is mourned.");
        var slackDead = End(bound); slackDead.Flags.Add("sacrifice"); Rules.Complete(story, slackDead);
        check(SurfaceIds.Has(Visible(P + "epilogue.slack", slackDead), "[soana.trickster.epilogue.slack/start/paragraph/0]"),
            "The unreversed sacrifice misreads the knot.");

        // Q10 r2 (BEL/HOW): each graveyard refusal is remembered as it went.
        var boughtWalked = Pick(graveyard, back, P + "cost.grave_bought", "soana.closed");
        var dugWalked = Pick(graveyard, back, P + "cost.grave_dug", "soana.closed");
        foreach (var (w, says, never) in new[] { (walked, 2, 0), (boughtWalked, 1, 0),
                                                  (dugWalked, 0, 2) })
        {
            var e = End(w);
            check(Endings(w).SequenceEqual(new[] { P + "epilogue.unbound" }) && Rules.ParagraphVisible(S(P + "epilogue.unbound").Nodes[0].Paragraphs[says], e)
                  && !Rules.ParagraphVisible(S(P + "epilogue.unbound").Nodes[0].Paragraphs[never], e),
                "The unbound ending misremembers the grave: " + says);
        }

        // Q10 r2 (INT): the creed is recalled only if the Commander heard it (SoanaAfterBear/Cue_0012).
        var sheBearAt = Later(story, lucky, 48);
        var creedPages = new HashSet<string>();
        Program.Walk(sheBear, sheBearAt, (id, _) => creedPages.Add(id));
        var heardWorld = Program.Copy(sheBearAt); heardWorld.Flags.Add("soana.heard_creed");
        var heardPages = new HashSet<string>();
        Program.Walk(sheBear, heardWorld, (id, _) => heardPages.Add(id));
        check(creedPages.Contains("rest_plain") && !creedPages.Contains("rest") && heardPages.Contains("rest") && !heardPages.Contains("rest_plain"),
            "The she-bear recalls a creed the Commander never heard.");
        check(Play(sheBear, sheBearAt).Any(r => r.Has(P + "answered_rest")), "An uninformed Commander cannot answer that she may rest.");

        // Q10 r3 (CAN): the slain and pulverised bears give no living counterparty; the Commander re-cuts the knot first.
        foreach (var (extra, page) in new[] { ("trickster", "carcass"), ("soana.medallion_pulverized", "pelt") })
        {
            var deadBear = World(story, 3, "trickster", "trickster.ever", "soana.dead", "soana.killed_by_camellia", "soana.forest_dead",
                                 "soana.bear_dead", extra, "soana.heard_link_a");
            var seen = KnotPages(deadBear);
            var outcomes = Play(knot, deadBear);
            check(seen.IsSupersetOf(new[] { "spirit", page, "bait" }) && !seen.Contains("read") && !seen.Contains("marks")
                  && !seen.Contains(page == "pelt" ? "carcass" : "pelt"),
                "The dead-bear knot skips the re-cut knot or reads a living spirit: " + page);
            check(outcomes.Any(r => r.Has(P + "returned") && r.Has(P + "cost.knot_recut"))
                  && outcomes.Where(r => r.Has(P + "returned")).All(r => r.Has(P + "cost.knot_recut")),
                "A dead bear's knot is bargained with before it is re-cut: " + page);
        }

        var deadBearMedallion = World(story, 3, "trickster", "trickster.ever", "soana.dead", "soana.forest_dead", "soana.bear_dead",
                                      "soana.medallion_held");
        check(Play(knot, deadBearMedallion).Where(r => r.Has(P + "returned")).All(r => r.Has(P + "cost.medallion_spent")),
            "A held medallion is kept at a re-cut knot.");

        // Q10 r3 (INT): Camellia's knife is remembered only by a Soana who saw her in the cave.
        var sawWorld = Program.Copy(sheBearAt); sawWorld.Flags.Add("camellia.claimed_soana_a"); Rules.Complete(story, sawWorld);
        var sawPages = new HashSet<string>();
        Program.Walk(sheBear, sawWorld, (id, _) => sawPages.Add(id));
        check(creedPages.Contains("roll_plain") && !creedPages.Contains("roll") && sawPages.Contains("roll") && !sawPages.Contains("roll_plain") && Play(sheBear, sheBearAt).Any(r => r.Has(P + "answered_roll")),
            "The she-bear remembers an absent Camellia, or forgets one who was there.");

        // Q10 r3 (BEL): the Commander's pronouns, and the knot ending's token in full.
        string FullText(Scene page, Snapshot w) => SurfaceIds.Of(story, page.Nodes[0]) + "|" + string.Join("|", Rules.VisibleParagraphs(page.Nodes[0], End(w)).Select(x => SurfaceIds.Of(story, x)));
        var cordEnd = FullText(epKnot, bound);
        var clayBound = Pick(terms, Later(story, Invite(clayDug), 72), "soana.committed", P + "cost.knot_bearer");
        var clayEnd = FullText(epKnot, clayBound);
        check(SurfaceIds.Has(cordEnd, "[soana.trickster.epilogue.knot/start/paragraph/1]") && !SurfaceIds.Has(cordEnd, "[soana.trickster.epilogue.knot/start/paragraph/0]") && SurfaceIds.Has(clayEnd, "[soana.trickster.epilogue.knot/start/paragraph/0]")
              && !SurfaceIds.Has(clayEnd, "[soana.trickster.epilogue.knot/start/paragraph/1]"),
            "The knot ending names the wrong token: " + cordEnd);

        // Q10 r4 (CAN/INT/HOW): the pulverised medallion kills Orso though no BearDead etude starts; the return chain reads
        // soana.guardian_dead, so this history never meets a living Orso.
        var pulverized = new Snapshot { Chapter = 3, Area = Wintersun, Hour = 5000 };
        pulverized.Flags.UnionWith(new[] { "trickster", "trickster.ever", "soana.dead", "soana.forest_dead", "soana.medallion_pulverized",
                                           "chapter_later" });
        pulverized.AvailableContacts.Add(Unit);
        Rules.Complete(story, pulverized);
        check(!pulverized.Has("soana.bear_dead") && pulverized.Has("soana.guardian_dead"), "The pulverised history is not a dead guardian.");
        var pulvPages = KnotPages(pulverized);
        var pulvOutcomes = Play(knot, pulverized);
        check(pulvPages.IsSupersetOf(new[] { "spirit", "pelt", "bait", "wake_spirit" }) && !pulvPages.Contains("orso")
              && !pulvPages.Contains("wake_orso") && !pulvPages.Contains("carcass") && !pulvPages.Contains("read") && !pulvPages.Contains("marks"),
            "The pulverised history meets a living Orso: " + string.Join(",", pulvPages));
        check(pulvOutcomes.Any(r => r.Has(P + "returned"))
              && pulvOutcomes.Where(r => r.Has(P + "returned")).All(r => r.Has(P + "cost.knot_recut")),
            "A pulverised knot is bargained with before it is re-cut.");
        var pulvBack = pulvOutcomes.First(r => r.Has(P + "returned"));
        var pulvGrave = new HashSet<string>();
        Program.Walk(graveyard, Later(story, pulvBack, 48), (id, _) => pulvGrave.Add(id));
        check(pulvGrave.Contains("spirit") && !pulvGrave.Contains("orso"), "The graveyard keeps Orso alive after the medallion was pulverised.");

        // Q10 r4 (BEL): Corven is disclosed before any commitment off the registered courtship; friendship is an answer.
        foreach (var (scene, at, node) in new[] { (terms, atTerms, "price"), (terms, Later(story, Invite(clayDug), 72), "price_clay"),
                                                   (bowl, Later(story, tested0, 72), "terms") })
        {
            var friend = Pick(scene, at, P + "friends");
            check(!friend.Has("soana.committed") && !friend.Has("soana.closed") && Endings(friend).SequenceEqual(new[] { P + "epilogue.friends" }),
                "Friendship has no ending of its own: " + scene.Id + " -> " + string.Join(",", Endings(friend)));
        }

        // Q10 close-out (INT): a lover committed before her death who returns her and walks away from her graves has exactly
        // one closing page, with the leash resolved, both straight away and after digging.
        var oldGrave = Later(story, oldRaised, 48);
        foreach (var w in new[] { Pick(graveyard, oldGrave, "soana.closed", P + "cost.left_the_grave"),
                                  Pick(graveyard, oldGrave, "soana.closed", P + "cost.grave_dug") })
        {
            var ends = Endings(w);
            check(ends.SequenceEqual(new[] { P + "epilogue.unbound" }),
                "A committed lover who left her graves ends on the wrong pages: " + string.Join(",", ends));
        }

        // Q10 close-out (CAN): after the medallion was pulverised, the slack strand names no restored clay token.
        var pulvTerms = Later(story, Invite(Pick(graveyard, Later(story, pulvBack, 48), P + "graveyard_kept", P + "cost.grave_dug")), 72);
        var pulvBound = Pick(terms, pulvTerms, P + "cost.knot_bearer");
        var pulvDead = End(pulvBound); pulvDead.Flags.Add("sacrifice"); Rules.Complete(story, pulvDead);
        var pulvSlack = FullText(slack, pulvDead);
        check(Endings(pulvBound).SequenceEqual(new[] { epKnot.Id }) && pages.Where(pg => Rules.Available(story, pg, pulvDead)).Select(pg => pg.Id).SequenceEqual(new[] { slack.Id })
              && SurfaceIds.Has(pulvSlack, "[soana.trickster.epilogue.slack/start/paragraph/0]"),
            "The pulverised history's sacrifice ending restores a clay token: " + pulvSlack);

        // Polish (Sol INT/HOW): who held the leash when the Commander died at the Threshold. The full visible slack text follows
        // the history: a rite already done in play, an offscreen taking-back before the march, or a leash still in the hand.
        const string Struck = "[soana.trickster.epilogue.slack/start/paragraph/1]", Reclaimed = "[soana.trickster.epilogue.slack/start/paragraph/3]",
                     Closed = "[soana.trickster.epilogue.slack/start/paragraph/4]", Postponed = "[soana.trickster.epilogue.slack/start/paragraph/5]", Slackened = "[soana.trickster.epilogue.slack/start/paragraph/0]";
        string SlackText(Snapshot s) { var e = End(s); e.Flags.Add("sacrifice"); Rules.Complete(story, e); return FullText(slack, e); }
        string[] Leash(string text) => new[] { Struck, Reclaimed, Closed, Postponed, Slackened }.Where(slot => SurfaceIds.Has(text, slot)).ToArray();
        var termsFriend = Pick(terms, atTerms, P + "friends", P + "cost.leash_reclaimed");
        var rebindRefused = Pick(rebind, atRebind, P + "rebind_declined", P + "cost.leash_reclaimed");
        var legacyFriend = Program.Copy(termsFriend); legacyFriend.Flags.Remove(P + "cost.leash_reclaimed"); Rules.Complete(story, legacyFriend);
        var legacyRefused = Program.Copy(rebindRefused); legacyRefused.Flags.Remove(P + "cost.leash_reclaimed"); Rules.Complete(story, legacyRefused);
        var compoundLuckOnly = Program.Copy(lateBack);
        foreach (var f in new[] { P + "declined", P + "luck_kept" }) { compoundLuckOnly.Flags.Add(f); compoundLuckOnly.Times[f] = compoundLuckOnly.Hour - 300; }
        Rules.Complete(story, compoundLuckOnly);
        foreach (var (name, w, expect) in new[] {
                     ("terms friendship", termsFriend, Reclaimed), ("legacy terms friendship", legacyFriend, Reclaimed),
                     ("rebinding refused", rebindRefused, Reclaimed), ("legacy rebinding refused", legacyRefused, Reclaimed),
                     ("graveyard closure", walked, Closed), ("dug then closed", dugWalked, Closed), ("old lover left the grave", Pick(graveyard, oldGrave, "soana.closed", P + "cost.left_the_grave"), Closed),
                     ("knot postponed", refused, Postponed), ("untouched return", lateBack, Struck), ("old lover never rebound", oldRaised, Struck),
                     ("stale luck-only not yet", compoundLuckOnly, Struck), ("knot bearer", bound, Slackened), ("rebound lover", vowed, Slackened) })
        {
            var text = SlackText(w);
            var e = End(w); e.Flags.Add("sacrifice"); Rules.Complete(story, e);
            var onPages = pages.Where(pg => Rules.Available(story, pg, e)).Select(pg => pg.Id).ToArray();
            check(onPages.SequenceEqual(new[] { slack.Id }) && Leash(text).SequenceEqual(new[] { expect }),
                "The slack page misremembers the leash (" + name + "): " + string.Join(",", onPages) + " / " + string.Join(",", Leash(text)));
            var back2 = Program.Copy(e); back2.Flags.Add("ending.trickster"); Rules.Complete(story, back2);
            check(!Rules.Available(story, slack, back2), "The slack page outlives a Commander who came back: " + name);
        }
        // A friend with a stale luck-chain "not yet" ends on the friendship alone.
        var friendStale = Program.Copy(termsFriend); friendStale.Flags.Add(P + "declined"); friendStale.Times[P + "declined"] = friendStale.Hour - 300;
        Rules.Complete(story, friendStale);
        check(Endings(friendStale).SequenceEqual(new[] { P + "epilogue.friends" }),
            "A friend with a stale luck postponement gets two pages, or the leash is taken twice: " + string.Join(",", Endings(friendStale)));
        // Ulbrig does not comment on a leash she has already taken back.
        check(S(P + "react.ulbrig_knot").Forbids.Contains(P + "leash_reclaimed_before_threshold"), "Ulbrig sees a leash she has taken back.");
        // Item 3: the paid diggers are ordered at the grave and arrive within the three days the terms enforce.
        check(!Rules.Available(story, accounting, Later(story, bought, 71)) && Rules.Available(story, accounting, Later(story, bought, 72)),
            "The paid graves narrate a delivery the clock does not keep.");
        var boughtWalkedEnd = string.Join("|", Rules.VisibleParagraphs(S(P + "epilogue.unbound").Nodes[0], End(boughtWalked)).Select(x => SurfaceIds.Of(story, x)));
        check(SurfaceIds.Has(boughtWalkedEnd, "[soana.trickster.epilogue.unbound/start/paragraph/1]"),
            "The unbound ending denies the grave visit, or times the diggers.");

        // Polish (Sol BEL/INT/HOW): the accounting. The history decides the accusation; only an answer and the work earn her
        // invitation; the friendship reclaims the leash; a refusal closes the route, and returning her buys nothing.
        HashSet<string> AccPages(Snapshot w) { var seenAcc = new HashSet<string>(); Program.Walk(accounting, Later(story, w, 72), (id, _) => seenAcc.Add(id)); return seenAcc; }
        var camelliaBackW = Pick(graveyard, Later(story, Pick(knot, killed, P + "returned"), 48), P + "graveyard_kept", P + "cost.grave_dug");
        var ownBackW = Pick(graveyard, Later(story, Legacy(World(story, 3, "trickster", "trickster.ever", "soana.dead", "soana.forest_dead",
                                                                   "soana.killed_self_before_bear")), 48), P + "graveyard_kept", P + "cost.grave_bought");
        var oldCamelliaW = oldDug;
        var oldOwnW = Pick(graveyard, Later(story, Legacy(ownKill), 48), P + "graveyard_kept");
        foreach (var (name, w, node) in new[] { ("camellia", camelliaBackW, "camellia"), ("own", ownBackW, "own"), ("unknown", dug, "unknown"),
                                                ("camellia_lover", oldCamelliaW, "camellia_lover"), ("own_lover", oldOwnW, "own_lover") })
        {
            var seenAcc = AccPages(w);
            var others = new[] { "camellia", "own", "unknown", "camellia_lover", "own_lover" }.Where(x => x != node);
            check(seenAcc.Contains(node) && !others.Any(seenAcc.Contains) && seenAcc.IsSupersetOf(new[] { "evasive", "repeat", "answered", "judged", "friend", "dismiss" }),
                "The accounting accuses the wrong history (" + name + "): " + string.Join(",", seenAcc));
            var outs = Play(accounting, Later(story, w, 72));
            check(outs.Where(r => r.Has(P + "accounting_invited")).All(r => r.Has(P + "accounting_answered") && r.Has(P + "cost.stream_cleared") && r.Has(P + "cost.nursery_guarded"))
                  && outs.Any(r => r.Has(P + "accounting_invited")),
                "The invitation comes without an answer or the work (" + name + ").");
            var refusedAcc = outs.Where(r => r.Has(P + "accounting_refused")).ToList();
            check(refusedAcc.Count > 0 && refusedAcc.All(r => r.Has("soana.closed") && r.Has(P + "refused") && !r.Has(P + "accounting_invited"))
                  && refusedAcc.All(r => !Reaches(r, P + "cost.knot_bearer") && !Rules.Available(story, coda, Called(r))),
                "Refusing the accounting leaves the vow or the coda open (" + name + ").");
            var friendAcc = outs.Where(r => r.Has(P + "accounting_friend")).ToList();
            check(friendAcc.Count > 0 && friendAcc.All(r => r.Has(P + "friends") && r.Has(P + "cost.leash_reclaimed") && r.Has(P + "cost.stream_cleared")
                  && Endings(r).SequenceEqual(new[] { P + "epilogue.friends" }) && !Rules.Available(story, coda, Called(r))),
                "The accounting friendship does not resolve the leash or end on the friendship alone (" + name + ").");
            check(!Rules.Available(story, accounting, Later(story, Invite(w), 500)), "The accounting repeats after the invitation (" + name + ").");
        }
        check(AccPages(ownBackW).Contains("diggers") && !AccPages(dug).Contains("diggers") && AccPages(dug).Contains("work"),
            "The paid diggers are shown at the wrong visit.");
        check(oldOwnW.Has("soana.committed") && Play(accounting, Later(story, oldOwnW, 72)).Where(r => r.Has(P + "accounting_friend")).All(r => r.Has("soana.committed")),
            "An old lover's friendship deletes the historical commitment.");
        check(accounting.Nodes.Single(n => n.Id == "evasive").Choices.All(ch => !ch.Set.Contains(P + "accounting_answered")),
            "The evasion is counted as an answer.");
        check(!Rules.Available(story, accounting, Later(story, bound, 200)) && !Rules.Available(story, accounting, Later(story, vowed, 200)),
            "A vow already taken is asked to answer again.");
        // The late fallback carries the reckoning; the unvowed lover's renewed intimacy follows it; the coda knows it.
        var commitLate = FullText(epCommit, lateBack);
        var commitInvited = FullText(epCommit, Invite(dug));
        check(Endings(Invite(dug)).SequenceEqual(new[] { epCommit.Id }) && SurfaceIds.Has(commitLate, "[soana.trickster.epilogue.commit/start/paragraph/2]")
              && !SurfaceIds.Has(commitLate, "[soana.trickster.epilogue.commit/start/paragraph/3]") && SurfaceIds.Has(commitInvited, "[soana.trickster.epilogue.commit/start/paragraph/3]")
              && !SurfaceIds.Has(commitInvited, "[soana.trickster.epilogue.commit/start/paragraph/0][soana.trickster.epilogue.commit/start/paragraph/1][soana.trickster.epilogue.commit/start/paragraph/2]") && SurfaceIds.Has(commitLate, "[soana.trickster.epilogue.commit/start/paragraph/4]"),
            "The late commit skips the reckoning, or repeats one already played: " + commitLate);
        check(SurfaceIds.Has(FullText(epCommit, Pick(graveyard, Later(story, Pick(knot, killed, P + "returned"), 48), P + "graveyard_kept")), "[soana.trickster.epilogue.commit/start/paragraph/0]"),
            "The late commit forgets Camellia.");
        var unvowedOld = FullText(S(P + "epilogue.unvowed"), oldRaised);
        var unvowedRefused = FullText(S(P + "epilogue.unvowed"), unvowed);
        check(SurfaceIds.Has(unvowedOld, "[soana.trickster.epilogue.unvowed/start/paragraph/1]") && !SurfaceIds.Has(unvowedOld, "[soana.trickster.epilogue.unvowed/start/paragraph/0]")
              && SurfaceIds.Has(unvowedRefused, "[soana.trickster.epilogue.unvowed/start/paragraph/0]") && !SurfaceIds.Has(unvowedRefused, "[soana.trickster.epilogue.unvowed/start/paragraph/1]"),
            "The unvowed lover's ending skips or repeats the reckoning.");
        // Polish r1 (Sol INT/BEL/HOW): a luck "not yet", then her death, return, accounting and the knot's friendship: the stale
        // declined flag does not reopen the knot's second ask, and the friendship is the only ending.
        var luckThenFriend = Pick(terms, compound, P + "friends", P + "cost.leash_reclaimed");
        check(compound.Has(P + "accounting_invited") && !Rules.Available(story, secondAsk, Later(story, luckThenFriend, 300))
              && !Reaches(luckThenFriend, P + "cost.knot_bearer") && Endings(luckThenFriend).SequenceEqual(new[] { P + "epilogue.friends" }),
            "A friend with a stale luck postponement is asked for the knot again, or ends on two pages: " + string.Join(",", Endings(luckThenFriend)));
        // Polish r1 (Sol CAN/INT): the pulverised medallion withered Orso without a BearDead etude; every registered living-Orso
        // answer is shut by it, and each split has a dead-Orso answer for it (raw native readers: the registered tests build
        // states without the Derived pass).
        var guardianNodes = story.Scenes.Where(s => s.Relationship == "soana" && !s.Id.StartsWith(P, StringComparison.Ordinal)
                                                    && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
            .SelectMany(s => s.Nodes.Select(n => (s.Id, n))).Where(x => x.n.Choices.Any(ch => ch.Next == "bound")).ToList();
        check(guardianNodes.Count >= 6 && guardianNodes.All(x =>
                  x.n.Choices.Where(ch => ch.Next == "bound").All(ch => ch.Forbids.Contains("soana.bear_dead") && ch.Forbids.Contains("soana.medallion_pulverized"))
                  && x.n.Choices.Any(ch => ch.Next == "dead" && ch.Requires.Contains("soana.medallion_pulverized") && ch.Forbids.Contains("soana.bear_dead"))),
            "A registered living/dead Orso split keeps Orso alive after the medallion was pulverised: "
            + string.Join(",", guardianNodes.Where(x => !x.n.Choices.Any(ch => ch.Requires.Contains("soana.medallion_pulverized"))).Select(x => x.Id)));
        var pulvAlive = World(story, 3, "soana.after_quest", "soana.water_kept", "soana.fox_waited", "soana.old_defender", "soana.medallion_pulverized");
        var gq = S("soana.guardian_question");
        var gqPages = new HashSet<string>();
        if (Rules.Available(story, gq, pulvAlive)) Program.Walk(gq, pulvAlive, (id, _) => gqPages.Add(id));
        check(pulvAlive.Has("soana.guardian_dead") && gqPages.Contains("dead") && !gqPages.Contains("bound"),
            "The pulverised history's guardian question keeps Orso alive: " + string.Join(",", gqPages));
        // Polish r4 (ruling: a player-chosen kill stands): all six native kill answers (two attacks, two kills after the bear,
        // two executions) close her route. No knot, no presence, no living page or coda; the closing page and the two
        // witnesses' reactions instead. A save returned before the ruling keeps the own-kill accusation at the accounting.
        var byHand = S(P + "epilogue.by_your_hand");
        foreach (var key in new[] { "soana.killed_self_before_bear", "soana.killed_self_after_quest", "soana.killed_self_after_bear_a",
                                    "soana.killed_self_after_bear_b", "soana.executed_after_bear_a", "soana.executed_after_bear_b" })
        {
            check(story.SelectedAnswers.ContainsKey(key), "Unbound native kill answer: " + key);
            foreach (var lover in new[] { false, true })
            {
                var flags = new List<string> { "trickster", "trickster.ever", "soana.dead", "soana.forest_dead", key, "soana.medallion_held" };
                if (lover) flags.Add("soana.committed");
                var killer = World(story, 3, flags.ToArray());
                var later = Later(story, killer, 500);
                check(killer.Has("soana.killed_by_commander") && !Rules.Available(story, knot, killer) && !Rules.Available(story, knot, later)
                      && !Reaches(killer, P + "returned") && Endings(killer).SequenceEqual(new[] { byHand.Id })
                      && !Rules.Available(story, coda, Called(killer)) && !Ends(killer, "sacrifice").Any(id => id != byHand.Id),
                    "The Commander's own kill is undone, or ends on a living page: " + key + (lover ? " (lover)" : "") + " -> " + string.Join(",", Endings(killer)));
                var luckKiller = Program.Copy(killer); luckKiller.Flags.Add(P + "luck_kept"); luckKiller.Flags.Add(P + "luck_tested"); Rules.Complete(story, luckKiller);
                check(Endings(luckKiller).SequenceEqual(new[] { byHand.Id }), "A luck lover killed by the Commander gets the wrong page: " + string.Join(",", Endings(luckKiller)));
            }
            var witnessed = FullText(byHand, World(story, 6, "trickster", "trickster.ever", "soana.dead", "soana.forest_dead", key, "ulbrig.talked"));
            check(SurfaceIds.Has(witnessed, "[soana.trickster.epilogue.by_your_hand/start/paragraph/1][soana.trickster.epilogue.by_your_hand/start/paragraph/3]") && SurfaceIds.Has(witnessed, "[soana.trickster.epilogue.by_your_hand/start/paragraph/2]"), "Nobody answers the Commander's own kill: " + key);
            var legacyGrave = Pick(graveyard, Later(story, Legacy(World(story, 3, "trickster", "trickster.ever", "soana.dead", "soana.forest_dead", key)), 48), P + "graveyard_kept");
            var legacyPages = AccPages(legacyGrave);
            check(legacyPages.Contains("own") && !legacyPages.Contains("unknown"), "A legacy own-kill return is accused as unknown: " + key);
        }
        check(!Rules.Available(story, byHand, Legacy(World(story, 6, "trickster", "trickster.ever", "soana.dead", "soana.killed_self_after_quest"))),
            "The own-kill page is missing, or mourns a Soana a legacy save returned.");
        // The return still answers Camellia's kill and an unattributed death.
        check(Rules.Available(story, knot, killed) && Rules.Available(story, knot, World(story, 3, "trickster", "trickster.ever", "soana.dead", "soana.forest_dead")),
            "The knot no longer answers Camellia's kill or an unattributed death.");
        // Polish r3 (Sol CAN/INT/HOW): a luck lover later killed and never returned stays dead: no living page, no coda, her loss
        // page instead; a failed presence alone is no courtship.
        var luckLover = Pick(bowl, Later(story, tested0, 72), "soana.committed");
        var luckKilled = Program.Copy(luckLover);
        foreach (var f in new[] { "soana.dead", "soana.forest_dead", "soana.killed_by_camellia" }) { luckKilled.Flags.Add(f); luckKilled.Times[f] = luckKilled.Hour; }
        Rules.Complete(story, luckKilled);
        var luckKilledLateCall = Called(luckKilled);
        check(Endings(luckKilled).SequenceEqual(new[] { P + "epilogue.luck_lost" }) && !Rules.Available(story, coda, luckKilledLateCall)
              && !Ends(luckKilled, "sacrifice").Contains(slack.Id),
            "A luck lover killed and never returned keeps a living ending or coda: " + string.Join(",", Endings(luckKilled)));
        var luckReturned = Program.Copy(luckKilled); luckReturned.Flags.Add(P + "returned"); Rules.Complete(story, luckReturned);
        check(Rules.Available(story, coda, Called(luckReturned)) && !Endings(luckReturned).Contains(P + "epilogue.luck_lost"),
            "A returned luck lover loses her coda, or is mourned.");
        string Coda(Snapshot s) { var e = Called(s); return string.Join("|", Rules.VisibleParagraphs(coda.Nodes.Last(), e).Select(x => SurfaceIds.Of(story, x))); }
        check(SurfaceIds.Has(Coda(bound), "[soana.lastcall.page/page/paragraph/3]") && !SurfaceIds.Has(Coda(lateBack), "[soana.lastcall.page/page/paragraph/3]"),
            "The Last Call coda misremembers the accounting.");
        // Reviewed polish P01: play the grave visit through the selected answer, then render its unfinished ending.
        var polishGraveAt = Later(story, raised, 48);
        var polishDug = Program.WalkVia(graveyard, polishGraveAt, "dig", 0)
            .Single(w => w.Has(P + "cost.grave_dug") && !w.Has("soana.closed"));
        var polishBought = Program.WalkVia(graveyard, polishGraveAt, "dig", 1)
            .Single(w => w.Has(P + "cost.grave_bought") && !w.Has("soana.closed"));
        check(Program.WalkVia(graveyard, polishGraveAt, "dug", 0).Any(w => w.Has(P + "cost.grave_dug") && !w.Has("soana.closed")),
            "P01: the unfinished-history fixture never reached the dug page.");
        foreach (var w in new[] { raised, polishDug, polishBought, lateFailed })
        {
            var text = FullText(S(P + "epilogue.unfinished"), w);
            check(Endings(w).SequenceEqual(new[] { P + "epilogue.unfinished" }),
                "P01: the unfinished reckoning erases a grave visit or assumes a closed Wound: " + text);
        }

        // P02: each actual request opens its own handover; the recurring warning must precede the paid receipt.
        foreach (var (handover, request, warningNode) in new[] { (afterQuest, "camellia.asked_for_soana", "cost"),
                    (bearA, "camellia.claimed_soana_a", "start"), (bearB, "camellia.claimed_soana_b", "start") })
        {
            var atHandover = World(story, 3, "trickster", "trickster.ever", "soana.after_quest", "soana.old_defender", request);
            check(Rules.Available(story, handover, atHandover), "P02: missing native handover: " + handover.Id);
            var warningBeforePayment = false;
            var outs = Program.Walk(handover, atHandover, (id, w) =>
            {
                if (id == warningNode)
                    warningBeforePayment = !w.Has(P + "cost.blood_given");
            });
            check(warningBeforePayment && outs.All(w => w.Has(P + "cost.blood_given") && !w.Has("soana.committed") && !w.Has(P + "returned")),
                "P02: payment precedes its warning, or the handover grants romance/return: " + handover.Id);
            var atWinter = Later(story, outs.Single(), 72); atWinter.Chapter = 5; Rules.Complete(story, atWinter);
            check(Rules.Available(story, winter, atWinter), "P02: winter invents a warning memory: " + handover.Id);
            foreach (var (index, effect) in new[] { (0, P + "cost.portion_shared"), (1, P + "portion_watched") })
                check(Program.WalkVia(winter, atWinter, "start", index).Single().Has(effect),
                    "P02: winter choice/effect changed: " + index);
        }

        // P03: both tokens permit earnest delay, laughter, hard refusal and friendship without invented laughter history.
        foreach (var (at, priceNode, bindNode) in new[] { (atTerms, "price", "bind"),
                    (Later(story, Invite(clayDug), 72), "price_clay", "bind_clay") })
        {
            foreach (var (node, index, effect) in new[] { (priceNode, 1, P + "declined"),
                        (bindNode, 1, P + "declined"), (priceNode, 2, "soana.closed") })
            {
                var result = Program.WalkVia(terms, at, node, index).Single();
                var destination = terms.Nodes.Single(n => n.Id == terms.Nodes.Single(n => n.Id == node).Choices[index].Next);
                check(result.Has(effect) && !result.Has("soana.committed") && destination.Id == (effect == "soana.closed" ? "fool" : "no"), "P03: terms misremember the chosen refusal: " + node + "/" + index);
                if (effect == P + "declined")
                    check(Rules.Available(story, secondAsk, Later(story, result, 96)), "P03: postponement lost its priced second ask.");
                else
                    check(!Rules.Available(story, secondAsk, Later(story, result, 300)), "P03: hard refusal reopened the second ask.");
            }
            var friend = Program.WalkVia(terms, at, priceNode, 3).Single();
            check(friend.Has(P + "friends") && friend.Has(P + "cost.leash_reclaimed")
                  && !Rules.Available(story, secondAsk, Later(story, friend, 300)), "P03: friendship lost its leash resolution.");
        }

        Console.WriteLine("PASS: Soana Trickster (Trk_Soana_*): portion, knot, grave, terms, crooked luck and its courtship.");
    }
}
