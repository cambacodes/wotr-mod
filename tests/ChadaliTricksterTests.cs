using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Chadali, Trickster (Writer/handoffs/trickster/chadali.md; F21): "The lucky charm".
// One block per spec rules test (Trk_Chadali_*), the shape of each hook, and the wagers that make the coin a courtship
// (chadali_wagers, chadali_fortunes, chadali_sessions): every sitting reachable, the question only after the real wager,
// the honey night only after the commit, and her sealed-hall worlds served by letters and the late epilogue page.
internal static class ChadaliTricksterTests
{
    private const string List = "e649f211c6b002a49a0c633061877927";
    private const string Cookie = "ed7a31d6f063e0c4aa4ec4e08fab57c0";
    private const string P = "chadali.trickster.";
    private const string W = "chadali.wagers.";
    private const string F = "chadali.fortunes.";
    private const string S = "chadali.sessions.";
    private const string H = "chadali.hours.";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        // eng-final E-Q8-10: fund the positive fixture; the walker enforces every debit.
        var state = new Snapshot { Chapter = chapter, Hour = 5000,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        // These positive predicate fixtures represent an already accepted route.
        // Coarse-key negatives are independent in PayoffDepartureRulesTests.
        foreach (var rel in story.Relationships)
            if (flags.Contains(rel.Value.CommittedFlag) && story.Derived.ContainsKey(rel.Key + ".payoff.ordinary"))
                HouseholdTests.Earn(story, state, rel.Key + ".payoff.ordinary");
        foreach (var context in flags.Where(story.Derived.ContainsKey))
            HouseholdTests.Earn(story, state, context);
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
        Scene Sc(string id) => story.Scenes.Single(s => s.Id == id);
        var coin = Sc(P + "council.coin");
        var orange = Sc(P + "council.orange");
        var second = Sc(P + "council.second_cookie");
        var tree = Sc(P + "after.orange_tree");
        var letter = Sc(P + "council.orange_letter");
        var lucky = Sc(P + "fought.lucky");
        var pageCommit = Sc(P + "epilogue.commit");
        var pageDeclined = Sc(P + "epilogue.declined");
        var pageNight = Sc(P + "epilogue.lucky_night");
        var wager = Sc(W + "the_real_wager");
        var night = Sc(F + "honey");
        var pages = story.Scenes.Where(s => s.Relationship == "chadali" && s.Owner == "ChadaliEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "chadali" && s.Reaction).ToArray();
        var own = story.Scenes.Where(s => s.Relationship == "chadali" && !s.Reaction && s.Owner == "Chadali").ToArray();
        var sittings = own.Where(s => s.Id.StartsWith(W, StringComparison.Ordinal) || s.Id.StartsWith(F, StringComparison.Ordinal)
                                      || s.Id.StartsWith(S, StringComparison.Ordinal) || s.Id.StartsWith(H, StringComparison.Ordinal)).ToArray();
        Choice Choice(Scene scene, string node, int index) => scene.Nodes.Single(n => n.Id == node).Choices[index];
        // The outcomes of a walk that took the named choice of the named node.
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            var hits = Program.WalkVia(scene, w, node, index);
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        Snapshot First(Scene scene, Snapshot w, string node, int index) => After(scene, w, node, index).FirstOrDefault() ?? w;
        // Plays every available Chadali scene forward and reports whether a flag is ever held.
        using var reachability = new ReachabilityCache();
        bool Reaches(Snapshot start, string flag, int chapter = 5)
            => reachability.Reaches(start, flag, chapter, () => Explore(Program.Copy(start), chapter));
        IEnumerable<Snapshot> Explore(Snapshot start, int chapter)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 16 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    yield return from;
                    var w = Later(story, from, 100, chapter);
                    foreach (var scene in own.Where(s => Rules.Available(story, s, w)))
                        foreach (var r in Program.Walk(scene, w))
                        {
                            yield return r;
                            if (seen.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                        }
                }
                frontier = next.Take(400).ToList();
            }
        }

        // Shape and hooks.
        var rel = story.Relationships["chadali"];
        check(rel.StartedFlag == "chadali.started" && rel.ClosedFlag == "chadali.closed" && rel.CommittedFlag == "chadali.committed"
              && rel.UnavailableFlags.SequenceEqual(new[] { "chadali.lost_at_council" })
              && rel.UnavailableOverrides.Single().Key == "chadali.lost_at_council" && rel.UnavailableOverrides.Single().Value == P + "returned"
              && rel.TricksterAccess.Keys.SequenceEqual(new[] { "chadali.lost_at_council" }),
            "Chadali's relationship does not match the spec.");
        foreach (var inline in new[] { coin, orange })
            check(inline.AnswerLists.SequenceEqual(new[] { List }) && inline.NativeReturnCue == Cookie && inline.ContactUnit == null
                  && inline.Areas.Length == 0 && inline.Chapters.SequenceEqual(new[] { 3, 5 }),
                "Not an inline scene on her private list with the clean return cue: " + inline.Id);
        check(Choice(coin, "start", 0).Mythic == "PlayerIsTrickster" && Choice(coin, "start", 0).Alignment?.Direction == "Chaotic"
              && Choice(coin, "start", 0).Alignment!.Value == 1 && Choice(coin, "start", 1).Abort,
            "The coin is not a Trickster answer (Chaotic 1) with a way back.");
        check(orange.Nodes.Single(n => n.Id == "open").Choices.Count == 3
              && Choice(orange, "open", 0).Requires.Contains("council.orange_called") && Choice(orange, "open", 0).Next == "start_orange"
              && Choice(orange, "open", 1).Forbids.Contains("council.orange_called")
              && Choice(orange, "open", 2).Requires.Contains("council.orange_called") && Choice(orange, "open", 2).Next == "start_edge",
            "The payoff does not let the Commander plant the orange on the page (Council_5-1/Cue_0020), or leave the bag alone.");
        foreach (var hall in own.Where(s => !Rules.IsRemote(s) && s.InteractionHub != "chadali.presence.market"))
            check(hall.AnswerLists.SequenceEqual(new[] { List }) && hall.ContactUnit == null
                  && hall.Chapters.All(c => c >= 3 && c <= 5) && hall.Forbids.Contains("chadali.lost_at_council"),
                "A hall scene is not on her private list in Chapters 3-5 behind the sealed-hall guard: " + hall.Id);
        foreach (var remote in new[] { letter, lucky })
            check(Rules.IsRemote(remote) && remote.MinChapter == 5 && remote.MaxChapter == 5, "A sealed-hall letter is not a Chapter 5 letter: " + remote.Id);
        check(own.Count(Rules.IsRemote) == 4, "Chadali has correspondence beyond three branch letters and the single failed-anchor market visit.");
        check(lucky.TricksterDevice && lucky.TricksterState == "chadali.lost_at_council" && lucky.Requires.Contains("trickster")
              && lucky.Requires.Contains("chadali.lost_at_council.latched"),
            "'Lucky you' is not the ER-2 device of the lost-at-council state.");
        check(second.Requires.Contains("chadali.started") && second.Requires.Contains(W + "the_real_wager") && second.NativeReturnCue == null,
            "The second cookie is not a physical entry that waits for the real wager.");
        check(pages.Length == 4 && pages.All(p => p.MinChapter == 6 && p.EpilogueAfter == null
                                                   && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null && c.Mythic == null))),
            "The epilogue pages are not four effect-free, unanchored Chapter 6 pages (appended in authored order, as Eritrice, Nocticula and Dorgelinda).");
        check(story.Derived[P + "late_committed"].Length == 2, "The late-commit derived key is missing.");
        check(pageCommit.Nodes[0].Choices.Select(c => c.Next).SequenceEqual(new[] { P + "epilogue.commit.explicit.1", "half", "coin", "penny", "friend" }),
            "The late-commit page does not let the Commander answer her (stay, half the orange, the coin, or the posted penny; PP6).");

        // Trk_Chadali_Coin.
        var council = World(story, 3, "trickster", "trickster.ever", "chadali.chance_asked");
        check(Rules.Available(story, coin, council) && !Rules.Available(story, orange, council) && !Rules.Available(story, second, council),
            "Trk_Chadali_Coin: the coin is not the only door.");
        var primed = First(coin, council, "start", 0);
        check(primed.Has(P + "primed") && primed.Has(P + "cost.luck_lent"), "Trk_Chadali_Coin: the coin does not prime and lend.");
        check(Rules.Available(story, orange, Later(story, primed, 24)) && !Rules.Available(story, orange, Later(story, primed, 12)),
            "Trk_Chadali_Coin: the orange does not open a day later.");
        check(Reaches(primed, "chadali.committed", 3), "Trk_Chadali_Coin: no road to the commit.");

        // Trk_Chadali_Payoff.
        var paying = World(story, 5, "trickster", "trickster.ever", P + "primed", "council.cauldron_given", "council.orange_called");
        check(Rules.Available(story, orange, paying), "Trk_Chadali_Payoff: the orange is not available.");
        var started = First(orange, paying, "confession", 0);
        check(started.Has("chadali.started") && started.Has(P + "courted"), "Trk_Chadali_Payoff: keeping the luck does not start the relationship.");
        check(First(orange, paying, "confession", 1).Has(P + "cost.luck_owed"), "Trk_Chadali_Payoff: the luck cannot be asked back.");
        check(!Rules.Available(story, second, Later(story, started, 72)) && Rules.Available(story, Sc(W + "the_recipe"), Later(story, started, 24)),
            "Trk_Chadali_Payoff: the question opens before the wagers have begun.");
        check(Reaches(started, W + "the_real_wager") && Reaches(started, "chadali.committed"), "Trk_Chadali_Payoff: no road through the real wager to the commit.");

        // Trk_Chadali_Commit.
        // eng7-l13: positive new commitment walks observe current power.
        var ready = World(story, 5, "trickster", "trickster.ever", "chadali.started", W + "the_real_wager", W + "bet_her");
        // Sol HOW (2026-09-30): postponing the wager does not consume it, and the question needs the bet itself.
        var unbet = World(story, 5, "trickster", "trickster.ever", "chadali.started", W + "so_gloomy", W + "a_free_space");
        check(Choice(wager, "not_tonight", 0).Abort && Rules.Available(story, wager, unbet)
              && !Rules.Available(story, second, Later(story, World(story, 5, "trickster.ever", "chadali.started", W + "the_real_wager"), 72)),
            "Trk_Chadali_Commit: refusing to bet consumes the wager or still opens the question.");
        check(After(wager, unbet, "bet", 0).All(r => r.Has(W + "bet_her")), "Trk_Chadali_Commit: staking does not record the bet.");
        check(Rules.Available(story, second, ready) && !Rules.Available(story, tree, ready), "Trk_Chadali_Commit: the second cookie is not available.");
        check(After(second, ready, "her_test", 0).All(r => r.Has("chadali.committed")), "Trk_Chadali_Commit: asking her does not commit.");

        // Trk_Chadali_Declined.
        var declined = First(second, ready, "refused", 0);
        check(declined.Has(P + "declined") && !declined.Has("chadali.committed"), "Trk_Chadali_Declined: her refusal is not the soft no.");
        check(First(second, ready, "luck", 0).Has(P + "declined"), "Trk_Chadali_Declined: flattery does not lead to her no.");
        check(Program.Walk(second, ready).All(r => !r.Has("chadali.closed")), "Trk_Chadali_Declined: the second cookie closes the relationship.");
        var afterNo = Later(story, declined, 72);
        check(Rules.Available(story, tree, afterNo) && !Rules.Available(story, second, afterNo), "Trk_Chadali_Declined: no seed after her no.");
        check(Choice(tree, "start", 0).Crusade?.Resource == "Materials" && Choice(tree, "start", 0).Crusade!.Amount == -100
              && Choice(tree, "start", 0).Set.Contains("chadali.committed") && Choice(tree, "start", 1).Set.Contains("chadali.closed"),
            "Trk_Chadali_Declined: the seed is not the priced second ask with a hard no.");
        check(Reaches(declined, "chadali.committed"), "Trk_Chadali_Declined: no road to the commit after her no.");
        check(Reaches(declined, W + "a_coin_lying_flat"), "Her soft no has no sitting of its own.");

        // Trk_Chadali_LateOrange.
        var sealedHall = World(story, 5, "trickster", "trickster.ever", P + "primed", "council.debrief_motion");
        check(Rules.Available(story, letter, sealedHall) && !Rules.Available(story, coin, sealedHall), "Trk_Chadali_LateOrange: the orange does not arrive.");
        var uneatenIntent = First(letter, sealedHall, "letter", 0);
        check(!Rules.Available(story, pageCommit, Later(story, uneatenIntent, 100, 6)), "Eating the late orange alone grants a romance.");
        var lateStart = First(letter, sealedHall, "letter", 1);
        check(lateStart.Has("chadali.started") && lateStart.Has(P + "cost.late"), "Trk_Chadali_LateOrange: eating the orange does not start her.");
        check(Rules.Available(story, pageCommit, Later(story, lateStart, 100, 6)), "Trk_Chadali_LateOrange: the late commit page is not reachable.");

        // Trk_Chadali_Fought.
        var fought = World(story, 5, "trickster", "trickster.ever", "council.fought_nocta_allied", "chadali.lost_at_council.latched");
        check(Rules.Available(story, lucky, fought) && !Rules.Available(story, coin, fought) && !Rules.Available(story, second, fought)
              && !sittings.Any(s => Rules.Available(story, s, fought)),
            "Trk_Chadali_Fought: the sealed hall still opens, or her letter does not come.");
        check(Choice(lucky, "hurt", 0).Mythic == "PlayerIsTrickster" && Choice(lucky, "hurt", 0).Alignment?.Direction == "Chaotic",
            "Trk_Chadali_Fought: the bet on her luck is not a Trickster answer (Chaotic 1).");
        var apology = First(lucky, fought, "refusal", 0);
        check(apology.Has(P + "returned") && apology.Has(P + "cost.grudge") && apology.Has(P + "cost.apologised")
              && Choice(lucky, "refusal", 0).Crusade?.Resource == "Favors" && Choice(lucky, "refusal", 0).Crusade!.Amount == -200,
            "Trk_Chadali_Fought: the public apology is not paid for.");
        check(First(lucky, fought, "refusal", 1).Has(P + "cost.needle_owed"), "Trk_Chadali_Fought: the needle cannot be promised.");

        // Trk_Chadali_Fought_Refused.
        var hostile = World(story, 5, "trickster", "trickster.ever", "council.fought", "chadali.lost_at_council.latched");
        var refused = First(lucky, hostile, "refusal", 2);
        check(refused.Has("chadali.closed") && !refused.Has(P + "returned"), "Trk_Chadali_Fought_Refused: refusing her terms is not her hard no.");

        // Trk_Chadali_Fought_Epilogue.
        // eng7-l13: new late yes fixtures observe current Trickster power.
        var market = Sc(P + "after.market_wager");
        var renewed = World(story, 5, "trickster", "trickster.ever", "council.fought", P + "returned");
        var unreadyEnding = Later(story, renewed, 100, 6);
        check(!Rules.ChoiceAvailable(Choice(pageCommit, "page", 0), unreadyEnding)
              && Rules.ChoiceAvailable(Choice(pageCommit, "page", 4), unreadyEnding),
            "Reconciliation alone offers intimacy, or withholds friendship.");
        var invited = First(market, renewed, "carried", 0);
        check(invited.Has(P + "return_test.ready") && invited.Has(P + "late_romantic_intent"),
            "The actual market invitation did not earn late courtship.");
        var ending = Later(story, invited, 100, 6);
        check(Rules.Available(story, pageCommit, ending) && !Rules.Available(story, pageDeclined, ending),
            "Trk_Chadali_Fought_Epilogue: the late commit page is not the only page.");
        check(Rules.Available(story, pageNight, World(story, 6, "trickster.ever", "chadali.committed", W + "bet_her"))
              && !Rules.Available(story, pageCommit, World(story, 6, "trickster.ever", "chadali.committed", W + "bet_her")),
            "The committed ending page is not the lucky night page.");
        check(Rules.Available(story, pageDeclined, World(story, 6, "trickster.ever", P + "declined"))
              && Rules.Available(story, pageNight, World(story, 6, "trickster.ever", P + "declined", "chadali.committed", P + "cost.orange_tree")),
            "The refusal page or the declined-then-committed override is wrong.");
        check(pageNight.Nodes[0].Paragraphs.Count >= 20, "The committed page is missing the courtship's consequences.");
        // Sol INT (2026-09-30): the lucky night reads the real commit only, so the late page never overlaps it before an answer.
        var lateOnly = World(story, 6, "trickster", "trickster.ever", "chadali.started", P + "cost.late", P + "courted");
        check(Rules.Available(story, pageCommit, lateOnly) && !Rules.Available(story, pageNight, lateOnly),
            "The committed page shows beside the late page before the Commander has answered.");
        // Ledger row 16: a Commander back from the sacrifice (the Last Call bottle) keeps her pages; a dead one does not.
        var bottle = new[] { "sacrifice", "ending.wound_closed", "trickster.lastcall.taken", "trickster.lastcall.pillar.bottle" };
        check(Rules.Available(story, pageNight, World(story, 6, new[] { "trickster.ever", "chadali.committed" }.Concat(bottle).ToArray()))
              && Rules.Available(story, pageCommit, World(story, 6, new[] { "trickster", "trickster.ever", "chadali.started", P + "courted" }.Concat(bottle).ToArray()))
              && !Rules.Available(story, pageNight, World(story, 6, "trickster.ever", "chadali.committed", "sacrifice", "ending.wound_closed")),
            "The romance pages do not follow trickster.commander_back.");
        // Sol BEL: the curse lifted by her own hand shows only the restored-luck paragraph.
        var cursed = pageNight.Nodes[0].Paragraphs.Single(p => p.Requires.Contains(W + "cobblehoof_left_cursed"));
        check(cursed.Forbids.Contains(S + "cobblehoof_freed_by_her")
              && pageNight.Nodes[0].Paragraphs.Any(p => p.Requires.Contains(S + "cobblehoof_freed_by_her")),
            "The permanent curse paragraph prints after she lifted it.");
        // Sol BEL: the sealed-hall yes is staged to its threshold, with a morning after.
        // Sol CAN: the Chapter 3 knucklebones recall no Abyss expedition.
        // Sol r2. CAN: no invented Shyka testimony, no Abyss in the future tense; INT: no rescue asserted before any extraction.
        // INT: the kept promise is recalled only by the Commander who made it.
        var needles = Sc(F + "sharp_needles");
        check(Choice(needles, "start", 2).Next == "sorry" && Choice(needles, "start", 2).Requires.Contains(F + "promised_no_force"),
            "The needle's apology recalls a promise never made.");
        // BEL: the feint is a proposal the Commander signs or refuses on the page.
        var feint = Sc(S + "you_bet_with_people");
        check(feint.Nodes.Single(n => n.Id == "start").Choices.Count == 5 && Choice(feint, "start", 3).Next == "refuse",
            "The feint is an atrocity the player never chose.");
        // BEL/COX: the committed page agrees with a called Last Call (the coin fell once) and with a loan paid back in the hall.
        var paras = pageNight.Nodes[0].Paragraphs;
        check(paras.Any(p => p.Requires.Contains("chadali.lastcall.luck_returned")) && paras.Where(p => p.Requires.Contains(P + "cost.luck_owed")).Count() == 2 && paras.Single(p => p.Requires.Contains(P + "cost.luck_owed") && !p.Requires.Contains(F + "loan_returned")).Forbids.Contains(F + "loan_returned") && pageCommit.Nodes[0].Paragraphs.Any(p => p.Requires.Contains("chadali.lastcall.luck_returned")),
            "The romance pages contradict the Last Call call-in or the repaid loan.");
        // R1:chadali:004: dispatch completes the sitting without personal delivery credit.
        // WalkVia records the chosen answer, rather than inferring it from the final flags.
        var shrine = Sc(S + "a_parcel_for_the_shrine");
        var shrineWorld = World(story, 3, "trickster", "trickster.ever", "chadali.started", W + "her_worshippers");
        check(Rules.Available(story, shrine, shrineWorld), "The earned shrine sitting is unavailable.");
        var personalPlaque = paras[29];
        check(personalPlaque.Requires.Contains(S + "carried_the_parcel"), "The shrine plaque lost its personal-delivery condition.");
        foreach (var branch in new[] { (node: "start", index: 0), (node: "what", index: 0), (node: "what", index: 1) })
        {
            var deliveries = Program.WalkVia(shrine, shrineWorld, branch.node, branch.index);
            bool personal = branch.index == 0;
            check(deliveries.Count == 1 && deliveries.All(r => r.Has(shrine.Id) && r.Has(S + "carried_the_parcel") == personal),
                "The selected shrine deliverer disagrees with completion or credit: " + branch);
            foreach (var delivery in deliveries)
            {
                var epilogue = Later(story, delivery, 100, 6);
                epilogue.Flags.Add("chadali.committed");
                Rules.Complete(story, epilogue);
                check(Rules.Available(story, pageNight, epilogue)
                      && Rules.VisibleParagraphs(pageNight.Nodes[0], epilogue).Contains(personalPlaque) == personal,
                    "The selected shrine deliverer receives the wrong plaque: " + branch);
                check(!Rules.Available(story, shrine, Later(story, delivery, 100)), "The dispatched parcel can be replayed.");
            }
        }
        var dispatch = Choice(shrine, "runner", 0);
        check(dispatch.Next == null && !dispatch.Abort && !dispatch.Set.Contains(S + "carried_the_parcel") && dispatch.Set.Contains(S + "cache_allocated"),
            "The runner does not complete dispatch without personal delivery.");

        // Sol r3 INT: a live, unprimed Trickster whose hall closed in peace is reached by a priced wager by post; a soft no whose hall
        // sealed before the seed keeps its later ask on the late page (no extra letter, Sol r3 COX).
        var lateWager = Sc(P + "council.late_wager");
        var peaceful = World(story, 5, "trickster", "trickster.ever", "council.debrief_motion");
        var wagerOut = After(lateWager, peaceful, "reply", 0);
        check(Rules.IsRemote(lateWager) && Rules.Available(story, lateWager, peaceful) && wagerOut.All(r => r.Has("chadali.started"))
              && Choice(lateWager, "start", 0).Crusade?.Amount == -100 && !Rules.Available(story, lateWager, World(story, 5, "trickster", "trickster.ever", "council.debrief_motion", P + "primed"))
              && Rules.Available(story, pageCommit, Later(story, wagerOut[0], 100, 6)),
            "A peaceful, unprimed sealed hall has no way in.");
        var declinedSealed = World(story, 6, "trickster", "trickster.ever", "chadali.started", P + "declined", P + "courted", "council.debrief_motion");
        check(Rules.Available(story, pageCommit, declinedSealed) && !Rules.Available(story, pageDeclined, declinedSealed)
              && pageCommit.Nodes[0].Paragraphs.Any(p => p.Requires.Contains(P + "declined"))
              && !story.Scenes.Any(s => s.Id == P + "after.orange_tree_letter"),
            "A soft no is locked out when the hall seals before the seed.");
        // Sol r3 BEL: the rigging is the Commander's own secret answer to the prayer; the needle is renegotiated, not paid with a pin.
        var rigged = Sc(F + "rigged");
        check(rigged.Requires.Contains(W + "prayer_answered") && rigged.Forbids.Contains(W + "prayer_credited"), "Chadali accuses the Commander of an act never chosen, or a pin pays the needle.");
        // Sol r3 CAN: the Lexicon recollection waits for the native discovery.
        check(Sc(S + "an_interesting_way").Requires.Contains("chadali.lexicon_found")
              && story.SeenCues["chadali.lexicon_found"].Contains("805e49b56b678a145891d30f5a5b30f6"), "The Lexicon is recalled before it is found.");
        // Sol r4: the promise against force is recorded only when kept; she can be reminded she asked for the rigging; the shared
        // remembering belongs to the ceased-Council ending.
        var hurtScene = Sc(F + "will_it_hurt");
        check(!Choice(hurtScene, "start", 0).Set.Contains(F + "promised_no_force") && Choice(hurtScene, "promise", 0).Set.Contains(F + "promised_no_force")
              && !Choice(hurtScene, "promise", 1).Set.Contains(F + "promised_no_force")
              && rigged.Nodes.Single(n => n.Id == "start").Choices.Any(c => c.Next == "asked")
              && pageNight.Nodes[0].Paragraphs.Where(p => p.Requires.Contains(H + "promised_to_remember")).All(p => p.Requires.Contains("council.epilogue_ceased")),
            "A revised promise, a requested rigging or the shared remembering contradicts its history.");
        // Sol r2 CAN/BEL: no Chapter 5 essence debate in a Chapter 3 sitting; the burnt-cookie secret is recalled only after it was told.
        check(Choice(Sc(F + "worthless"), "frightened", 0).Requires.Contains(F + "burnt_edges") && Choice(Sc(F + "worthless"), "frightened", 2).Next == "forgive_early",
            "A sitting recalls an event or a secret the player has not reached.");

        // The courtship: every sitting reachable, the question only after the wager, the night only after the commit.
        foreach (var sitting in sittings)
            check(sitting.Optional && sitting.Requires.Contains("trickster.ever"), "A sitting is not an optional Trickster-path beat: " + sitting.Id);
        check(sittings.Length >= 44, "The wagers are missing sittings.");
        check(wager.Requires.Contains(W + "so_gloomy") && wager.Requires.Contains(W + "a_free_space"), "The real wager does not wait for the gloom and the dream.");
        check(night.Requires.Contains("chadali.committed") && !Rules.Available(story, night, Later(story, ready, 24)),
            "The honey night opens before the commit.");
        check(night.Nodes.Any(n => n.Id == "cut") && night.Nodes.Single(n => n.Id == "look").Choices.Single().Set.Contains(F + "night"),
            "The night does not reach its threshold and cut.");
        // Sol r2 HOW: no Chapter 4 key proposal in a Chapter 3 fixture.
        var courting3 = World(story, 3, "trickster", "trickster.ever", "chadali.started", "chadali.called_babbling", "chadali.cobblehoof_stopped", "chadali.lexicon_found");
        foreach (var id in new[] { W + "the_recipe", W + "born_lucky", W + "her_worshippers", W + "a_lucky_charm", W + "the_old_fellow",
                                   W + "just_joking", W + "odious_questions", W + "knucklebones", W + "a_free_space", W + "so_gloomy",
                                   W + "the_real_wager", S + "what_you_said", S + "a_dull_future", S + "an_interesting_way",
                                   S + "a_drinking_song", S + "a_parcel_for_the_shrine", S + "two_patrons", H + "make_some_stronger",
                                   H + "an_unlucky_day", H + "our_new_friend", H + "who_brought_you", H + "a_cookie_for_the_enemy",
                                   H + "not_today", H + "a_lucky_number" })
            check(Reaches(courting3, id, 3), "Sitting unreachable in Chapter 3: " + id);
        check(Reaches(courting3, W + "loaded_dice", 3), "The hidden cheat is never caught.");
        var old = Sc(W + "the_old_fellow");
        check(old.Nodes.Single(n => n.Id == "stopped").Choices.Any(c => c.Alignment?.Direction == "Evil")
              && old.Nodes.Single(n => n.Id == "stopped").Choices.Any(c => c.Alignment == null),
            "The old fellow's pivotal split has no evil option, or its mending is shifted.");
        var chapterFive = World(story, 5, "trickster", "trickster.ever", "chadali.started", "council.cauldron_given", "chadali.fair_proposed",
            "chadali.bows_for_nocticula", "chadali.worthless_essence", "chadali.needle_hurt", "chadali.pressed_on_essence");
        foreach (var id in new[] { F + "will_it_hurt", F + "a_great_big_fair", F + "matching_ribbons", F + "worthless",
                                   F + "sharp_needles", S + "we_are_friends_right", H + "pretend_we_never_met" })
            check(Reaches(chapterFive, id), "Sitting unreachable in Chapter 5: " + id);
        var committed5 = World(story, 5, "trickster.ever", "chadali.started", "chadali.committed", W + "the_real_wager", W + "cobblehoof_left_cursed", W + "prayer_answered");
        foreach (var id in new[] { F + "honey", F + "burnt_edges", F + "rigged", F + "the_meadows", F + "a_yellow_ribbon", F + "sharing",
                                   F + "paid_back", S + "what_chance_wishes", S + "you_bet_with_people", S + "the_old_fellow_again",
                                   S + "the_last_evening", H + "for_luck", H + "the_seat_beside_her" })
            check(Reaches(committed5, id), "Post-commit sitting unreachable: " + id);

        // Reactions: exactly Eritrice and Ember, behind their guards; Eritrice's own Chadali reaction honours her return.
        check(reactions.Length == 4 && reactions.All(r => r.Nodes.Count == 1)
              && reactions.Where(r => r.Owner == "Eritrice").All(r => r.Forbids.Contains("eritrice.lost_at_council"))
              && reactions.Where(r => r.Owner == "Ember").All(r => r.Forbids.Contains("ember_dead") && r.Forbids.Contains("ember_gone")),
            "The reactions are not exactly Eritrice and Ember behind their guards.");
        // Eritrice's Chadali reaction is a hall scene: both women's loss keys derive from the same two fight etudes, so it
        // stays behind the sealed-hall guard (a derived key takes no ForbidOverride; the Eritrice backlog item is moot).
        var motion = Sc("eritrice.trickster.react.chadali_motion");
        check(motion.Forbids.Contains("chadali.lost_at_council") && motion.AnswerLists.SequenceEqual(new[] { List }),
            "Eritrice's Chadali reaction is not a hall scene behind Chadali's sealed-hall guard.");
        check(letter.Nodes.Any(n => n.Id == "postscript"), "Eritrice's postscript is missing from the orange letter.");
        // PP6 (pacing): her book on Cobblehoof's errand, in the hall the night of the Chapter 4 session (Council_Lexicon2/Cue_0033),
        // settled by the bag in Chapter 5 (will_it_hurt gains three answers after its own three); the Lexicon sitting may open that
        // night too ([3, 5] -> [3, 4, 5]), where its key branch answers the session.
        var fetch = Sc(F + "what_he_went_for");
        check(story.SeenCues["chadali.cobblehoof_errand"].SequenceEqual(new[] { "507a2a7cccb1c26449838fbf28f2e3af" })
              && fetch.Chapters.SequenceEqual(new[] { 4 }) && fetch.MinChapter == 4 && fetch.MaxChapter == 4 && !Rules.IsRemote(fetch)
              && fetch.AnswerLists.SequenceEqual(new[] { List }) && fetch.Forbids.Contains("chadali.lost_at_council")
              && fetch.Requires.Contains("chadali.started") && fetch.Requires.Contains("chadali.cobblehoof_errand"),
            "The bag bet lost its shape (a Chapter 4 hall sitting after Cobblehoof's errand).");
        var errand4 = World(story, 4, "trickster.ever", "chadali.started", "chadali.cobblehoof_errand");
        check(Rules.Available(story, fetch, errand4), "The bag bet does not open the night of the session.");
        check(!Rules.Available(story, fetch, World(story, 4, "trickster.ever", "chadali.started")), "The bag bet opens before Cobblehoof's errand.");
        foreach (int ch in new[] { 3, 5 })
            check(!Rules.Available(story, fetch, World(story, ch, "trickster.ever", "chadali.started", "chadali.cobblehoof_errand")),
                "The bag bet opens outside Chapter 4: " + ch);
        check(!Rules.Available(story, fetch, World(story, 4, "trickster.ever", "chadali.started", "chadali.cobblehoof_errand", "chadali.lost_at_council")),
            "The bag bet ignores the sealed hall.");
        string[] betWays = { F + "bag_bet_against", F + "bag_bet_partners", F + "bag_bet_declined" };
        string[] betPages = { "bet_won", "bet_lost", "bet_declined" };
        var bets = Program.Walk(fetch, errand4).Where(r => r.Has(fetch.Id)).ToList();
        check(bets.Count == 3 && betWays.All(f => bets.Count(r => r.Has(f)) == 1) && bets.All(r => !Rules.Available(story, fetch, Later(story, r, 48))),
            "The bag bet cannot go three ways, or is made twice.");
        var hurtOpen = Sc(F + "will_it_hurt").Nodes.Single(n => n.Id == "start").Choices;
        check(hurtOpen.Count == 6 && hurtOpen[0].Next == "promise" && hurtOpen[1].Next == "truth" && hurtOpen[2].Next == "looking"
              && hurtOpen.Skip(3).Select(c => c.Requires.Single()).SequenceEqual(betWays), "The bet's settlement was not appended to will_it_hurt.");
        foreach (var r in bets)
        {
            var home = Later(story, r, 0, 5); home.Flags.Add("council.cauldron_given"); Rules.Complete(story, home);
            check(Rules.Available(story, Sc(F + "will_it_hurt"), home), "Will it hurt does not follow the bag bet.");
            var pagesSeen = new HashSet<string>();
            var outcomes = Program.Walk(Sc(F + "will_it_hurt"), home, (page, _) => pagesSeen.Add(page));
            string want = betPages[Array.FindIndex(betWays, r.Has)];
            check(pagesSeen.Contains(want) && betPages.Count(pagesSeen.Contains) == 1 && outcomes.Any(o => o.Has(F + "told_it_would_hurt"))
                  && outcomes.Any(o => o.Has(F + "promised_no_force")), "Will it hurt settles the wrong bet, or loses its own answers: " + want);
        }
        var noBetPages = new HashSet<string>();
        Program.Walk(Sc(F + "will_it_hurt"), World(story, 5, "trickster.ever", "chadali.started", "council.cauldron_given"), (page, _) => noBetPages.Add(page));
        check(!betPages.Any(noBetPages.Contains), "A bet is settled that was never made.");
        var lexicon = Sc(S + "an_interesting_way");
        var lexPages = new HashSet<string>();
        Program.Walk(lexicon, World(story, 4, "trickster.ever", "chadali.started", "chadali.lexicon_found", "eritrice.proposed_key"), (page, _) => lexPages.Add(page));
        check(lexicon.Chapters.SequenceEqual(new[] { 3, 4, 5 }) && lexPages.Contains("key") && !lexPages.Contains("how"),
            "The Lexicon sitting does not answer the key the night of the session.");
        check(own.Where(s => !Rules.IsRemote(s) && s.Chapters.Contains(4)).Select(s => s.Id).OrderBy(x => x)
                  .SequenceEqual(new[] { fetch.Id, lexicon.Id }.OrderBy(x => x)), "Chapter 4 holds more of the hall than the session's own night.");
        // PP6 Sol r1. CAN: the feast forgot the Commander (Epilogues/Cue_0569); Socothbenoth's favours stop where he vanishes
        // (SocotGone, Cue_0570). INT: the unprimed refusal returns no coin it never gave.
        var nightParas = pageNight.Nodes[0].Paragraphs;
        check(nightParas.Where(p => p.Requires.Contains("council.epilogue_feast")).All(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[chadali.trickster.epilogue.lucky_night/page/paragraph/2]")),
            "The victory feast seats the Commander that Cue_0569 forgot.");
        check(story.SeenCues["chadali.socoth_never_seen"].SequenceEqual(new[] { "fb1347793c15a9342af9eaf03060056d" }), "Cue_0570 is not bound.");
        check(nightParas.Where(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[chadali.trickster.epilogue.lucky_night/page/paragraph/40][chadali.trickster.epilogue.lucky_night/page/paragraph/41][chadali.trickster.epilogue.lucky_night/page/paragraph/44][chadali.trickster.epilogue.lucky_night/page/paragraph/45]") && (SurfaceIds.Has(SurfaceIds.Of(story, p), "[chadali.trickster.epilogue.lucky_night/page/paragraph/40]") || SurfaceIds.Has(SurfaceIds.Of(story, p), "[chadali.trickster.epilogue.lucky_night/page/paragraph/26][chadali.trickster.epilogue.lucky_night/page/paragraph/41]")))
                  .All(p => p.Forbids.Contains("socot.gone") && p.Forbids.Contains("chadali.socoth_never_seen")),
            "Socothbenoth keeps sending favours after he vanished.");
        check(nightParas.Count(p => p.AnyGroups.Any(g => g.Contains("socot.gone") && g.Contains("chadali.socoth_never_seen"))) == 2,
            "Socothbenoth's absence has no paragraph: " + nightParas.Count(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[chadali.trickster.epilogue.lucky_night/page/paragraph/40][chadali.trickster.epilogue.lucky_night/page/paragraph/41][chadali.trickster.epilogue.lucky_night/page/paragraph/44][chadali.trickster.epilogue.lucky_night/page/paragraph/45]")));
        var shut = lucky.Nodes.Single(n => n.Id == "shut");
        check(shut.Choices[0].Requires.Contains(P + "primed") && shut.Choices[0].Next == "shut_coin" && shut.Choices[1].Forbids.Contains(P + "primed") && shut.Choices[1].Next == null,
            "The refusal returns a coin the unprimed Commander never gave her.");
        // PP6 Sol r2. INT: a Commander committed before the Council fight gets the lucky night only after her reconciliation; the
        // late page's keepsake is the coin only if it was called, the penny only if it was posted. CAN: the odious questions recall
        // only the one Cue_0017 guarantees; the hall is reached by the chamber closet.
        foreach (var fight in new[] { "council.fought", "council.fought_nocta_allied" })
        {
            check(!Rules.Available(story, pageNight, World(story, 6, "trickster.ever", "chadali.committed", fight)), "The lucky night ignores an unreconciled fight: " + fight);
            check(Rules.Available(story, pageNight, World(story, 6, "trickster.ever", "chadali.committed", fight, P + "returned")), "The lucky night stays shut after her price: " + fight);
        }
        check(Rules.Available(story, pageNight, World(story, 6, "trickster.ever", "chadali.committed", W + "bet_her")), "The lucky night is lost for a Commander who never fought her.");
        var lateOpen = pageCommit.Nodes.Single(n => n.Id == "page").Choices;
        check(lateOpen.Count == 5 && lateOpen[2].Next == "coin" && lateOpen[2].Requires.Contains(P + "primed")
              && lateOpen[3].Next == "penny" && lateOpen[3].Requires.Contains(P + "cost.late_wager") && lateOpen[3].Forbids.Contains(P + "primed"),
            "The late page hands back a keepsake the Commander never gave her.");
        Console.WriteLine("PASS: Chadali Trickster (Trk_Chadali_*): coin, orange, second cookie, the seed, the sealed hall's letters, 'Lucky you' and the wagers.");
    }
}
