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
        var state = new Snapshot { Chapter = chapter, Area = chapter == 4 ? "" : Wintersun, Hour = 5000 };
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
        check(!Rules.Available(story, bearA, World(story, 3, "trickster.ever", "camellia.claimed_soana_a")),
            "The handover joke is a new trick and needs the live path.");

        // Trk_Soana_Killed: Camellia bled her; the knot read the other way.
        var killed = World(story, 3, "trickster", "trickster.ever", "soana.dead", "soana.killed_by_camellia", "soana.forest_dead");
        check(Rules.Available(story, knot, killed) && !Any(killed, crooked, lateLuck, dice) && !Any(killed, handovers),
            "Trk_Soana_Killed: the knot is unavailable, or a living-Soana scene opens.");
        check(knot.Nodes.Single(n => n.Id == "read").Choices.Count == 3, "The knot's choices changed shape.");
        var raised = Pick(knot, killed, P + "returned", P + "cost.guardian_paid");
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
        var back = World(story, 5, "trickster.ever", "soana.dead", P + "returned");
        check(Rules.Available(story, graveyard, back) && !Rules.Available(story, terms, back),
            "Trk_Soana_Graveyard: the grave is closed, or the terms skip it.");
        var awayFromCave = Program.Copy(back); awayFromCave.Area = Drezen;
        check(!Rules.Available(story, graveyard, awayFromCave), "The grave test happens away from her cave.");
        var dug = Pick(graveyard, back, P + "graveyard_kept", P + "cost.grave_dug");
        var bought = Pick(graveyard, back, P + "graveyard_kept", P + "cost.grave_bought");
        check(graveyard.Nodes.SelectMany(n => n.Choices).Any(c => c.Crusade?.Resource == "Finances" && c.Crusade.Amount == -100
              && c.Set.Contains(P + "cost.grave_bought")), "The diggers cost nothing.");
        check(Rules.Available(story, terms, Later(story, dug, 72)) && !Rules.Available(story, terms, Later(story, dug, 71))
              && Rules.Available(story, terms, Later(story, bought, 72)),
            "Trk_Soana_Graveyard: the terms ignore their three days.");
        var walked = Pick(graveyard, back, "soana.closed", P + "cost.left_the_grave");
        var gravePages = new HashSet<string>();
        var graveEnds = Program.Walk(graveyard, back, (id, _) => gravePages.Add(id));
        check(gravePages.Contains("decide") && graveEnds.Any(r => r.Has(P + "graveyard_kept") && r.Has("soana.closed")),
            "The grave has no word of hers on what the Commander wants, or no way to leave after digging.");
        check(!Reaches(walked, "soana.committed"), "Walking away from the grave still commits.");

        // Trk_Soana_Terms: her terms, the commit, the night and the morning.
        var atTerms = Later(story, dug, 72);
        var bound = Pick(terms, atTerms, "soana.committed", P + "cost.knot_bearer");
        var visited = new HashSet<string>();
        foreach (var r in Program.Walk(terms, atTerms, (id, _) => visited.Add(id))) { }
        check(visited.IsSupersetOf(new[] { "start", "dug", "price", "bind", "no", "fool", "night", "morning" }),
            "Trk_Soana_Terms: a page of the terms is unreachable.");
        var boughtPages = new HashSet<string>();
        foreach (var r in Program.Walk(terms, Later(story, bought, 72), (id, _) => boughtPages.Add(id))) { }
        check(boughtPages.Contains("bought") && !boughtPages.Contains("dug"), "The terms misremember who dug.");

        // Trk_Soana_TermsRefused: her soft no, then the one priced second ask.
        var refused = Pick(terms, atTerms, P + "declined");
        check(!refused.Has("soana.committed") && !refused.Has("soana.closed"), "Trk_Soana_TermsRefused: her no closes or commits.");
        check(Rules.Available(story, secondAsk, Later(story, refused, 96)) && !Rules.Available(story, secondAsk, Later(story, refused, 95))
              && !Rules.Available(story, terms, Later(story, refused, 96)),
            "Trk_Soana_TermsRefused: the second ask ignores its days, or the terms repeat.");
        var paid = Pick(secondAsk, Later(story, refused, 96), "soana.committed", P + "cost.second_ask");
        check(secondAsk.Nodes.SelectMany(n => n.Choices).Any(c => c.Crusade?.Resource == "Materials" && c.Crusade.Amount == -150
              && c.Set.Contains("soana.committed")), "The second ask costs nothing.");
        check(Play(secondAsk, Later(story, refused, 96)).Any(r => r.Has("soana.closed") && !r.Has("soana.committed")),
            "The Commander cannot refuse her raised price.");
        var fooled = Pick(terms, atTerms, "soana.closed");
        check(!fooled.Has("soana.committed"), "The Commander's hard no commits.");

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
        check(crooked.Nodes.SelectMany(n => n.Choices).Any(c => c.Crusade?.Resource == "Materials" && c.Crusade.Amount == -100
              && c.Set.Contains(P + "luck_kept")), "Trk_Soana_Missed: the salt and meat are free.");
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
        check(bowlAsk.Nodes.SelectMany(n => n.Choices).Any(c => c.Crusade?.Resource == "Favors" && c.Crusade.Amount == -150
              && c.Set.Contains("soana.committed")), "The woods are sealed for free.");
        check(!Rules.Available(story, sheBear, World(story, 5, "trickster.ever", "soana.after_quest", "soana.old_defender", "soana.progression_kept")),
            "The missed courtship opens for a Commander who kept the registered visits.");

        // Trk_Soana_MissedLate: no die was planted; it is thrown now, dearer.
        var noDie = World(story, 5, "trickster", "trickster.ever", "soana.after_quest", "soana.bear_dead");
        check(Rules.Available(story, lateLuck, noDie) && !Rules.Available(story, crooked, noDie),
            "Trk_Soana_MissedLate: the late throw is unavailable, or the payoff opens without a die.");
        var thrown = Pick(lateLuck, noDie, P + "primed_dice", P + "cost.late", P + "luck_kept");
        check(lateLuck.Nodes.SelectMany(n => n.Choices).Any(c => c.Crusade?.Resource == "Materials" && c.Crusade.Amount == -200),
            "Trk_Soana_MissedLate: the late throw is no dearer.");
        check(!Rules.Available(story, crooked, thrown) && !Rules.Available(story, lateLuck, thrown), "The luck is sold twice.");
        check(Reaches(thrown, "soana.committed"), "Trk_Soana_MissedLate: no road to the commit.");

        // Trk_Soana_MissedAfterFailure: no die and no live trick.
        check(!Any(World(story, 5, "trickster.ever", "trickster.failed", "soana.after_quest", "soana.old_defender"), crooked, lateLuck),
            "Trk_Soana_MissedAfterFailure: a lost path still throws the die.");
        check(Rules.Available(story, crooked, World(story, 5, "trickster.ever", "trickster.failed", "soana.after_quest", "soana.old_defender",
              P + "primed_dice")), "A die planted as a Trickster stops paying out after a lost path (ledger 18).");

        // Epilogue pages: one Soana page per history; the loss pages belong to a Soana who stayed dead.
        Snapshot End(Snapshot s) { var e = Program.Copy(s); e.Chapter = 6; Rules.Complete(story, e); return e; }
        string[] Endings(Snapshot s) => pages.Where(p => Rules.Available(story, p, End(s))).Select(p => p.Id).ToArray();
        var knotEnd = Endings(bound);
        check(knotEnd.SequenceEqual(new[] { epKnot.Id }), "The knot's commit ends on the wrong pages: " + string.Join(",", knotEnd));
        var luckEnd = Endings(Pick(bowl, Later(story, tested0, 72), "soana.committed"));
        check(luckEnd.SequenceEqual(new[] { epLuck.Id }), "The bowl's commit ends on the wrong pages: " + string.Join(",", luckEnd));
        check(Endings(refused).SequenceEqual(new[] { epDeclined.Id }), "Her refusal ends on the wrong pages.");
        var lateBack = Pick(graveyard, back, P + "graveyard_kept");
        check(Endings(lateBack).SequenceEqual(new[] { epCommit.Id }), "A return never committed has no late page.");
        check(Endings(Pick(sheBear, Later(story, lucky, 48), P + "luck_tested")).SequenceEqual(new[] { epCommit.Id }),
            "A luck never committed has no late page.");
        check(Endings(walked).Length == 0, "Walking away from the grave still ends on a Soana page.");
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
        check(reactions.Length == 6 && reactions.Select(r => r.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Camellia", "Ember", "Ulbrig" }),
            "The reactors are not exactly Camellia, Ember and Ulbrig.");
        foreach (var r in reactions.Where(r => r.Owner == "Ulbrig"))
            check(r.Requires.Contains("ulbrig.talked") && r.Forbids.Contains("ulbrig.dead") && r.Forbids.Contains("ulbrig.kicked_out"),
                "Ulbrig speaks without his dialog or after he is gone: " + r.Id);
        foreach (var r in reactions.Where(r => r.Owner == "Ember"))
            check(r.Forbids.Contains("ember_dead") && r.Forbids.Contains("ember_gone"), "Ember speaks after she is gone: " + r.Id);
        foreach (var r in reactions.Where(r => r.Owner == "Camellia"))
            check(r.Forbids.Contains("camellia.dead") && r.Forbids.Contains("camellia.killed") && r.Forbids.Contains("camellia.kicked_out"),
                "Camellia speaks after she is gone: " + r.Id);
        check(Rules.Available(story, S(P + "react.camellia_knot"), Later(story, World(story, 3, "trickster.ever",
              "soana.killed_by_camellia", "soana.dead", P + "returned"), 24)), "Camellia never hears the woman she bled is walking.");
        Console.WriteLine("PASS: Soana Trickster (Trk_Soana_*): portion, knot, grave, terms, crooked luck and its courtship.");
    }
}
