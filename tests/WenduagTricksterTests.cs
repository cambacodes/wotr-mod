using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Wenduag, Trickster (Writer/handoffs/trickster/wenduag.md, R6 build sheet; 11-ROSTER-PLAN-2 §2, Wenduag block): "The
// Mongrel cairn". One block per rules test (Trk_Wenduag_*): the bindings and the relationship; the staged blow on Lann's kill
// list and its cairn; her return; a Commander-chosen kill closing the route; the outbid (traitor hub, exile lists, the late
// bid, the crystal); the falls in Savamelekh's house and in the street, bought and unbought; Lann's price; the native romance
// owning her; the courtship chain to the commit and the cairn; the pages; Last Call's coda and the household.
internal static class WenduagTricksterTests
{
    private const string P = "wenduag.trickster.";
    private const string Committed = "wenduag.committed";
    private const string Closed = "wenduag.closed";
    private const string Started = "wenduag.started";
    private const string Killed = "wenduag.killed";
    private const string Dead = "wenduag.dead_any";
    private const string Kicked = "wenduag.kicked_out";
    private const string Returned = P + "returned";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = Drezen };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 300;
        return state;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        bool Avail(Scene s, Snapshot w) => Rules.Available(story, s, w);
        Choice Ch(Scene s, string node, int index) => s.Nodes.Single(n => n.Id == node).Choices[index];
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
                        Rules.Complete(story, next);
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
            return hit ?? w;
        }
        Snapshot Later(Snapshot state, int hours)
        {
            var later = Program.Copy(state);
            later.Hour += hours;
            return later;
        }
        Snapshot At(Snapshot state, int chapter)
        {
            var moved = Program.Copy(state);
            moved.Chapter = chapter;
            Rules.Complete(story, moved);
            return moved;
        }

        var rel = story.Relationships["wenduag"];
        var mine = story.Scenes.Where(s => s.Relationship == "wenduag").ToArray();
        var pages = mine.Where(s => s.Owner == "WenduagEpilogue").ToArray();
        var stage = S(P + "killed.stage");
        var cairn = S(P + "killed.cairn");
        var back = S(P + "killed.back");
        var stone = S(P + "ch4.stone");
        var bid = S(P + "traitor.bid");
        var exile = S(P + "exile.bid_hub");
        var exileL = S(P + "exile.bid_traitor");
        var champion = S(P + "exile.champion");
        var lateBid = S(P + "exile.late_bid");
        var crystal = S(P + "crystal.bid");
        var abyssFall = S(P + "abyss.fall");
        var abyssBack = S(P + "abyss.back");
        var streetFall = S(P + "street.fall");
        var streetBack = S(P + "street.back");
        var truth = S(P + "lann.truth");
        var foundOut = S(P + "lann.found_out");
        var trial = S(P + "court.trial");
        var gate = S(P + "court.gate");
        var claim = S(P + "court.claim");
        var bed = S(P + "court.cairn");
        var morning = S(P + "court.morning");

        // Trk_Wenduag_Bindings: the relationship, its overrides and access, and the native reads.
        check(rel.StartedFlag == Started && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.OrderBy(f => f).SequenceEqual(new[] { Dead, Killed, Kicked, "wenduag.hello_attacked", "wenduag.hello_sent_away", "wenduag.q3_killed", "wenduag.q3_sent_away" }.OrderBy(f => f))
              && rel.UnavailableOverrides[Killed] == Returned && rel.UnavailableOverrides[Dead] == Returned && rel.UnavailableOverrides[Kicked] == Returned
              && !rel.UnavailableOverrides.ContainsKey("wenduag.q3_killed") && !rel.UnavailableOverrides.ContainsKey("wenduag.hello_attacked"),
            "Trk_Wenduag_Bindings: the relationship does not match the build sheet (three overridden losses, four closures of the Commander's own).");
        check(story.Etudes[Killed] == "85ee36dae8f3317448fa5b950543b3ad" && story.Etudes[Dead] == "1129a007a909f5c4f860cd0909cd10e0"
              && story.Etudes[Kicked] == "9b1902a20e98aa94094741ef9c91d962" && story.Etudes["wenduag.romance_active"] == "33c4c2f66f2461e4993df21566252079"
              && story.Etudes["wenduag.romance_finished"] == "c3a5748e4a44a1649a75e0968c15a0c1"
              && story.Etudes["wenduag.redeemed"] == "52576309e24d8024fbc08c2ff7016c2f" && story.Etudes["wenduag.traitor"] == "653968fb2e671d1458cc95f66e66860a"
              && story.SeenCues["wenduag.heard_savamelekh"].SequenceEqual(new[] { "b97fe0d7003556b4d806c3db9bc15ecf" })
              && story.SeenCues["wenduag.abyss_fell"].SequenceEqual(new[] { "c3ca34383f9ee3a4e9908ce68a2e828b" })
              && story.SeenCues["wenduag.street_confronted"].SequenceEqual(new[] { "eeea5c1c81a03ba4f83abe1ab0a70df0" })
              && story.SeenCues["wenduag.q3_killed"].SequenceEqual(new[] { "94f483f833d6c9243b539112dbf707d2" })
              && story.CompletedQuests["savamelekh.dead.w"] == "5ba83bd1a6b1c884794fbb4858480e7f"
              && story.CompletedQuests["savamelekh.dead.l"] == "df19bef39c8aa6a4b9dcaf40450b94dc"
              && story.Latches["wenduag.romance_finished.latched"].SequenceEqual(new[] { "wenduag.romance_finished" }),
            "Trk_Wenduag_Bindings: a native read is not bound to its verified GUID.");
        check(!mine.Any(s => s.Nodes.Any(n => n.Choices.Any(c => c.StartEtude != null || c.Set.Any(f => f.StartsWith("trickster.wmt.use.", StringComparison.Ordinal)))))
              && !mine.Any(s => s.Nodes.Any(n => n.Choices.Any(c => c.Revive != null))),
            "Trk_Wenduag_Bindings: the route starts an etude, spends a Word Made True or raises the dead (she was never dead).");
        check(mine.Where(s => s.Id.StartsWith(P + "early.", StringComparison.Ordinal)).All(s => !s.Requires.Contains("trickster") && !s.Requires.Contains("trickster.ever"))
              && mine.Where(s => !s.Id.StartsWith(P + "early.", StringComparison.Ordinal) && !s.Id.StartsWith("wenduag.lastcall", StringComparison.Ordinal))
                  .All(s => s.Requires.Contains("trickster") || s.Requires.Contains("trickster.ever")),
            "Path fit (v1): the early beats must be N-all and everything else Trickster-gated.");
        check(!story.Presences.Keys.Any(k => k.StartsWith("wenduag", StringComparison.Ordinal)),
            "Wenduag has a presence (every Drezen beat is a rest-delivered visit in the capital).");

        // Trk_Wenduag_Early: the N-all hub beats (Chapters 1, 2, 3), with no Trickster gate.
        var w1 = World(story, 1);
        check(Avail(S(P + "early.teeth"), w1) && !Avail(S(P + "early.walls"), w1) && Avail(S(P + "early.walls"), World(story, 2))
              && Avail(S(P + "early.gate"), World(story, 3)) && S(P + "early.gate").Areas.SequenceEqual(new[] { Drezen }),
            "Trk_Wenduag_Early: the hub beats do not play in their chapters without the Trickster.");
        var yan = World(story, 3, "yaniel.killed");
        check(Avail(S(P + "early.yaniel"), yan) && !Avail(S(P + "early.yaniel"), World(story, 3))
              && !Avail(S(P + "early.yaniel"), World(story, 3, "yaniel.killed", "wenduag.yaniel_death")),
            "Trk_Wenduag_Early: the Yaniel beat plays without her Fane outcome, or after the native romance's own question.");

        // Trk_Wenduag_Stage: the Commander's own blow at Lann's Q1, pulled (Mobility), before Cue_0049.
        check(stage.AnswerLists.SequenceEqual(new[] { "71ec232384eb5d349aff0b7d60f092ed" }) && stage.NativeReturnCue == "1d3ea8f8fe724a841b509dcab0961436"
              && stage.EntryMythic == "PlayerIsTrickster" && stage.TricksterDevice && stage.TricksterState == "killed"
              && Ch(stage, "start", 0).Check?.Skill == "SkillMobility" && Ch(stage, "start", 0).Check?.DC == 24 && Ch(stage, "start", 1).Abort
              && Ch(stage, "clean", 0).NativeNext == "fbf606cbf933aa04691bc7cfbe23292a" && Ch(stage, "deep", 0).NativeNext == "fbf606cbf933aa04691bc7cfbe23292a",
            "Trk_Wenduag_Stage: the staged blow is not hosted on the kill list, or does not continue into Cue_0049 (her request, Lann's eulogy, the blow).");
        var w3 = World(story, 3, "trickster", "trickster.ever");
        check(Avail(stage, w3) && !Avail(stage, World(story, 3, "trickster.ever")) && !Avail(stage, World(story, 5, "trickster", "trickster.ever")),
            "Trk_Wenduag_Stage: the staged blow is offered off the live Trickster path, or outside Chapter 3.");
        var staged = Take(stage, w3, "clean", 0, P + "staged", P + "primed", P + "stroke_clean");
        var stagedDeep = Take(stage, w3, "deep", 0, P + "staged", P + "cost.stroke_deep");
        check(!staged.Has(Killed) && !staged.Has(Returned), "Trk_Wenduag_Stage: the blow itself changes native state or returns her.");

        // Trk_Wenduag_Cairn: the burial, taken alone (Lore/Knowledge, then Bluff vs Lann); her knife in her right hand.
        var afterBlow = World(story, 3, "trickster", "trickster.ever", Killed, P + "staged", P + "stroke_clean");
        check(Avail(cairn, afterBlow) && !Avail(cairn, World(story, 3, "trickster", "trickster.ever", Killed))
              && cairn.Remote && cairn.Kind == "event" && cairn.TricksterDevice && cairn.TricksterState == "killed",
            "Trk_Wenduag_Cairn: the cairn plays without the staged blow, or is not a device page.");
        check(Ch(cairn, "read", 0).Check?.Skill == "SkillLoreNature" && Ch(cairn, "read", 1).Check?.Skill == "SkillKnowledgeWorld"
              && Ch(cairn, "lann_custom", 0).Check?.Skill == "CheckBluff" && Ch(cairn, "lann_custom", 0).Check?.DC == 18
              && Ch(cairn, "lann_guess", 0).Check?.DC == 24,
            "Trk_Wenduag_Cairn: the custom and the Bluff against Lann are not the build sheet's checks.");
        var buried = Take(cairn, afterBlow, "build", 0, P + "cairn_built", P + "cost.lied_to_lann", "trickster.secret.wenduag_cairn", P + "lann.alone", P + "cairn.bare");
        var buriedWatched = Take(cairn, afterBlow, "build_watched", 1, P + "cairn_built", P + "lann.watching", P + "cairn.water");
        check(!buried.Has(Returned) && !buried.Has(Started), "Trk_Wenduag_Cairn: the cairn returns her before she digs.");
        // Overlapping native losses: WenduagNotInParty_Dead may hold beside WenduagKilled; the killed world still plays through.
        var killedAndDead = World(story, 3, "trickster", "trickster.ever", Killed, Dead, P + "staged", P + "stroke_clean");
        check(Avail(stage, World(story, 3, "trickster", "trickster.ever", Dead)) && Avail(cairn, killedAndDead),
            "Trk_Wenduag_Cairn: the killed world stalls when WenduagNotInParty_Dead also holds.");
        var buriedDead = Take(cairn, killedAndDead, "build", 2, P + "cairn_built", P + "cairn.mark");
        var homeDead = Take(back, Later(buriedDead, 72), "lann", 1, Returned);
        check(Avail(trial, At(Later(homeDead, 24), 5)), "Trk_Wenduag_Cairn: the courtship does not open after a return over overlapping losses.");

        // Trk_Wenduag_Back: she digs, and comes to Drezen (72 h); the Commander's no closes.
        check(!Avail(back, Later(buried, 71)) && Avail(back, Later(buried, 72)) && back.Areas.SequenceEqual(new[] { Drezen })
              && back.Chapters.SequenceEqual(new[] { 3, 5 }) && back.TricksterDevice,
            "Trk_Wenduag_Back: the return does not wait 72 hours for a rest in Drezen (Chapters 3 and 5).");
        var home = Take(back, Later(buried, 72), "lann", 0, Returned, Started);
        check(home.Has(Returned) && !home.Has(Committed), "Trk_Wenduag_Back: her return commits her.");
        var stayed = Take(back, Later(buried, 72), "stay_dead", 0, Closed);
        check(stayed.Has(Closed) && !stayed.Has(Returned), "Trk_Wenduag_Back: the Commander's 'stay dead' is not a closure.");
        check(Avail(stone, Later(At(buried, 4), 24)) && !Avail(stone, Later(At(buried, 5), 24)), "Trk_Wenduag_Stone: the Chapter 4 beat does not play for a buried Wenduag in Chapter 4 only.");

        // Trk_Wenduag_PlayerKill: a native [Kill] answer, with no staged blow, is canon and closes the route.
        var killedPlain = World(story, 3, "trickster", "trickster.ever", Killed);
        // The staged blow itself stays listed: it is inline on the kill list, which never shows again once she is dead.
        check(!mine.Where(s => s.Owner != "WenduagEpilogue" && s != stage).Any(s => Avail(s, killedPlain) || Avail(s, Later(At(killedPlain, 5), 500))),
            "Trk_Wenduag_PlayerKill: a scene is offered after a kill the Commander chose (canon stands).");
        var q3Killed = World(story, 5, "trickster", "trickster.ever", "wenduag.in_party", "wenduag.q3_killed", P + "bought", Dead);
        check(!Avail(trial, q3Killed) && !Avail(claim, q3Killed), "Trk_Wenduag_PlayerKill: the courtship survives the Commander's kill at Savamelekh's end.");

        // Trk_Wenduag_TraitorBid: the outbid on the L path's traitor hub; failure is the late path, never a retry.
        var traitorW = World(story, 3, "trickster", "trickster.ever", "wenduag.traitor", "wenduag.in_party");
        check(bid.AnswerLists.SequenceEqual(new[] { "9bad7ea452d30254997b153473954cc1" }) && bid.NativeReturnCue == "daeb0e0796521c042bdd6baebbce7ade"
              && Avail(bid, traitorW) && !Avail(bid, World(story, 3, "trickster.ever", "wenduag.traitor"))
              && Ch(bid, "offer", 0).Check?.DC == 26 && Ch(bid, "offer", 1).Check?.Skill == "CheckIntimidate",
            "Trk_Wenduag_TraitorBid: the outbid is not on the traitor hub, or its checks are wrong.");
        var bought = Take(bid, traitorW, "after", 0, P + "bought", P + "primed");
        var failedBid = Take(bid, traitorW, "no", 0, P + "bid_failed");
        check(!Avail(bid, bought) && !Avail(bid, failedBid), "Trk_Wenduag_TraitorBid: the bid can be retried.");

        // Trk_Wenduag_Abyss: she falls in his house (Lann's blow); bought, the Commander claims her from Lann; she follows his smell home.
        var fellBought = World(story, 4, "trickster", "trickster.ever", Dead, "wenduag.abyss_fell", P + "bought");
        check(Avail(abyssFall, fellBought) && abyssFall.TricksterDevice && abyssFall.TricksterState == "abyss"
              && !Avail(abyssFall, World(story, 4, "trickster", "trickster.ever", Dead)),
            "Trk_Wenduag_Abyss: the fall in Savamelekh's house does not play on MongrelsDefeated/Cue_0001.");
        var abyssCairn = Take(abyssFall, fellBought, "cairn", 0, P + "abyss_cairn", P + "lann.alone", P + "cost.lied_to_lann", "trickster.secret.wenduag_cairn");
        var abyssKnown = Take(abyssFall, fellBought, "cairn_known", 0, P + "abyss_cairn", P + "lann.knows");
        check(!abyssKnown.Has(P + "cost.lied_to_lann"), "Trk_Wenduag_Abyss: a Lann who saw her breathing is recorded as lied to.");
        var fellUnbought = World(story, 4, "trickster", "trickster.ever", Dead, "wenduag.abyss_fell");
        var abyssLate = Take(abyssFall, fellUnbought, "cairn", 0, P + "abyss_cairn", P + "cost.late");
        var inDrezen = At(Later(abyssCairn, 48), 5);
        check(!Avail(abyssBack, At(Later(abyssCairn, 47), 5)) && Avail(abyssBack, inDrezen) && !Avail(abyssBack, Later(abyssCairn, 48)),
            "Trk_Wenduag_Abyss: the return does not wait 48 hours and Chapter 5.");
        var abyssHome = Take(abyssBack, inDrezen, "dug", 0, Returned, Started);

        // Trk_Wenduag_Exile: the dismissal made a bid (both lists); the champion's report; the late bid.
        var inParty = World(story, 3, "trickster", "trickster.ever", "wenduag.in_party");
        check(exile.AnswerLists.SequenceEqual(new[] { "0f4612672dd4d3e4d84575b23ffdddb3" }) && exile.NativeReturnCue == "f436e2adfafcc6541849a828790416ca"
              && Ch(exile, "yes", 0).NativeNext == "fa010a1b9f738964782d313580c1c0d1" && Ch(exile, "no", 0).NativeNext == "fa010a1b9f738964782d313580c1c0d1"
              && exileL.AnswerLists.SequenceEqual(new[] { "25a503735f9dd5448b84649add442029" }) && Ch(exileL, "yes", 0).NativeNext == "d07647bcdf0e2dc47b9534a3ca4cb048"
              && Ch(exile, "plan", 0).Check?.DC == 22 && Ch(exile, "plan", 1).Abort,
            "Trk_Wenduag_Exile: the bid is not on the exile answers, or does not continue into the native exile.");
        var sent = Take(exile, inParty, "yes", 0, P + "bought");
        var exiled = World(story, 4, "trickster", "trickster.ever", Kicked, P + "bought");
        check(Avail(champion, exiled) && champion.TricksterState == "exiled" && !Avail(champion, World(story, 4, "trickster", "trickster.ever", Kicked)),
            "Trk_Wenduag_Exile: the champion's report plays without the bid.");
        var scorned = World(story, 4, "trickster", "trickster.ever", Kicked, "wenduag.kicked_out.latched", P + "exile_scorned");
        check(Avail(lateBid, scorned) && !Avail(lateBid, exiled) && !Avail(lateBid, World(story, 5, "trickster", "trickster.ever", Kicked, "wenduag.kicked_out.latched")),
            "Trk_Wenduag_Exile: the late bid is not Chapter 4's fallback for an unbought exile.");
        var lateBought = Take(lateBid, scorned, "deal", 0, P + "bought", P + "cost.late");

        // Trk_Wenduag_Street: she falls in the street in Chapter 5; Brask; the catacombs; she digs.
        var street = World(story, 5, "trickster", "trickster.ever", Kicked, Dead, "wenduag.street_confronted", P + "bought");
        check(Avail(streetFall, street) && streetFall.TricksterState == "street" && !Avail(streetFall, World(story, 5, "trickster", "trickster.ever", Kicked, Dead)),
            "Trk_Wenduag_Street: the street fall does not play on the street's Cue_0025.");
        var streetCairn = Take(streetFall, street, "catacomb", 0, P + "street_cairn", "trickster.secret.wenduag_cairn");
        var streetLann = Take(streetFall, World(story, 5, "trickster", "trickster.ever", Kicked, Dead, "wenduag.street_confronted", P + "bought", "lann.in_party"),
            "catacomb_lann", 0, P + "street_cairn", P + "cost.lied_to_lann");
        var streetUnbought = World(story, 5, "trickster", "trickster.ever", Kicked, Dead, "wenduag.street_confronted");
        var brask = Take(streetFall, streetUnbought, "pull_rank_hard", 0, P + "brask_knows", P + "cost.watch", P + "cost.late");
        check(Ch(streetFall, "pull_rank_hard", 0).Crusade?.Resource == "Favors" && Ch(streetFall, "pull_rank_hard", 0).Crusade?.Amount == -150
              && Ch(streetFall, "pull_rank", 0).Crusade?.Amount == -100,
            "Trk_Wenduag_Street: the watch's bill is not the build sheet's Favors cost.");
        var streetHome = Take(streetBack, Later(streetCairn, 48), "dug", 0, Returned, Started);

        // Trk_Wenduag_Crystal: the W path's outbid after Savamelekh's crystal; the native romance owns her.
        var heard = World(story, 4, "trickster", "trickster.ever", "wenduag.in_party", "wenduag.heard_savamelekh");
        check(Avail(crystal, heard) && !Avail(crystal, World(story, 4, "trickster", "trickster.ever", "wenduag.in_party", "wenduag.heard_savamelekh", "wenduag.romance_active")),
            "Trk_Wenduag_Crystal: the bid after the crystal ignores the native romance.");
        var kept = Take(crystal, heard, "yes", 0, P + "bought", P + "crystal_done");
        var both = Take(crystal, heard, "both", 0, P + "crystal_both");
        check(!both.Has(P + "bought"), "Trk_Wenduag_Crystal: keeping both bids open buys her.");

        // Trk_Wenduag_Native: where the native romance lives or has finished, no courtship scene plays.
        var nativeLive = World(story, 5, "trickster", "trickster.ever", "wenduag.in_party", P + "bought", "wenduag.romance_active");
        var nativeDone = World(story, 5, "trickster", "trickster.ever", "wenduag.in_party", P + "bought", "wenduag.romance_finished.latched");
        check(!Avail(trial, nativeLive) && !Avail(trial, nativeDone) && Avail(trial, World(story, 5, "trickster", "trickster.ever", "wenduag.in_party", P + "bought")),
            "Trk_Wenduag_Native: the courtship double-romances a native romance (or never plays for a bought Wenduag).");
        check(!Avail(trial, World(story, 3, "trickster", "trickster.ever", "wenduag.in_party", P + "bought"))
              && !Avail(trial, World(story, 4, "trickster", "trickster.ever", "wenduag.in_party", P + "bought")),
            "Trk_Wenduag_Native: the courtship plays in Chapters 3-4 (the native window).");

        // Trk_Wenduag_Chain: trial -> gate -> claim (COMMIT) -> cairn -> morning, in Drezen, Chapter 5.
        var ch5 = At(Later(home, 24), 5);
        var proved = Take(trial, ch5, "stain", 0, P + "proved", P + "trial.tricked", Started);
        var bledOut = Take(trial, ch5, "lost", 0, P + "proved", P + "cost.bled");
        check(Ch(trial, "which", 2).Mythic == "PlayerIsTrickster" && Ch(trial, "which", 0).Check?.Skill == "SkillAthletics" && Ch(trial, "which", 0).Check?.DC == 26,
            "Trk_Wenduag_Chain: the trial's checks or its kept misdirection are wrong.");
        var gated = Take(gate, Later(proved, 24), "after_struck", 0, P + "gate_seen", P + "gate.struck");
        check(!Avail(claim, Later(proved, 48)) && Avail(claim, Later(gated, 24)), "Trk_Wenduag_Chain: the claim plays before the gate.");
        var yes = Take(claim, Later(gated, 24), "after_given", 0, Committed, P + "claim.given");
        var yesKnelt = Take(claim, Later(gated, 24), "after_knelt", 0, Committed, P + "claim.knelt");
        var yesStruck = Take(claim, Later(gated, 24), "after_struck", 0, Committed, P + "claim.struck");
        var no = Take(claim, Later(gated, 24), "no", 0, Closed);
        check(!no.Has(Committed) && Ch(claim, "want", 0).Alignment?.Direction == "Evil",
            "Trk_Wenduag_Chain: the Commander's no commits her, or [He's yours] carries no Evil shift.");
        check(!Avail(trial, no) && !Avail(bed, no), "Trk_Wenduag_Chain: the courtship survives the Commander's no.");
        var night = Take(bed, Later(yes, 24), "cut", 0, P + "court.cairn");
        var after = Take(morning, Later(night, 8), "end", 0, P + "morning.stone");

        // Trk_Wenduag_Kept: the chain also runs for a Wenduag kept at the Commander's side (bought, loyal, spared, redeemed).
        foreach (var way in new[] { P + "bought", "wenduag.q3_turned_on_him", "wenduag.q3_spared", "wenduag.redeemed" })
            check(Avail(trial, World(story, 5, "trickster", "trickster.ever", "wenduag.in_party", way)), "Trk_Wenduag_Kept: the courtship does not open for " + way);
        check(!Avail(trial, World(story, 5, "trickster", "trickster.ever", "wenduag.in_party")), "Trk_Wenduag_Kept: the courtship opens for a Wenduag nobody earned.");

        // Trk_Wenduag_Kept: a kept companion's trial says nothing of stones; her claim is played in person on her own list.
        var keptW = World(story, 5, "trickster", "trickster.ever", "wenduag.in_party", P + "bought");
        var keptProved = Take(trial, keptW, "stain_her", 0, P + "proved");
        check(Paths(trial, keptW).All(o => !o.path.Contains(("which_back", 0))), "Trk_Wenduag_Kept: a kept Wenduag remembers a burial she never had.");
        var claimHub = S(P + "court.claim_in_person");
        var keptGated = Take(gate, Later(keptProved, 24), "after_hers", 0, P + "gate_seen");
        check(claimHub.ReturnToList && claimHub.AnswerLists.Length == 3 && !claimHub.Remote && Avail(claimHub, Later(keptGated, 24))
              && !Avail(claim, Later(keptGated, 24)),
            "Trk_Wenduag_Kept: the kept claim is not in person on her native lists, or the remote claim also plays.");
        Take(claimHub, Later(keptGated, 24), "after_knelt", 0, Committed);

        // Trk_Wenduag_PathFailed: an unprepared rescue is a live Trickster act; a bought fall still pays off after the path fails.
        check(!Avail(abyssFall, World(story, 4, "trickster.ever", Dead, "wenduag.abyss_fell"))
              && Avail(abyssFall, World(story, 4, "trickster.ever", Dead, "wenduag.abyss_fell", P + "bought"))
              && !Avail(streetFall, World(story, 5, "trickster.ever", Kicked, Dead, "wenduag.street_confronted")),
            "Trk_Wenduag_PathFailed: an unprepared rescue appears after the Trickster path failed.");
        check(Ch(abyssFall, "price", 0).Crusade?.Amount == -100 && Ch(streetFall, "yields_late", 0).Crusade?.Amount == -50,
            "Trk_Wenduag_PathFailed: an unprepared rescue costs nothing.");

        // Trk_Wenduag_Vellexia: the hunt is offered only while Vellexia walks Drezen in her own body.
        var vel = S(P + "court.vellexia");
        check(vel.Requires.Contains("vellexia.trickster.in_person") && !Avail(vel, World(story, 5, "trickster", "trickster.ever", Returned, P + "gate_seen", "wenduag.vellexia_conflict")),
            "Trk_Wenduag_Vellexia: the hunt is offered while Vellexia is a mirror or absent.");

        // Trk_Wenduag_Lann: the cost, paid first or named by him.
        var lannWorld = World(story, 5, "trickster", "trickster.ever", Killed, P + "cairn_built", P + "cost.lied_to_lann", Returned, "lann.in_party");
        check(Avail(truth, lannWorld) && truth.ReturnToList && truth.AnswerLists.SequenceEqual(new[] { "66385ad77fa743e4bb1234078dbd804c" })
              && !Avail(truth, World(story, 5, "trickster", "trickster.ever", Killed, P + "cost.lied_to_lann", Returned, "lann.in_party", "lann.dead")),
            "Trk_Wenduag_Lann: the truth is not offered on Lann's list while he is with the Commander.");
        var paid = Take(truth, lannWorld, "owed", 0, P + "lann.paid");
        check(!Avail(foundOut, Later(paid, 100)), "Trk_Wenduag_Lann: Lann finds out after he was told.");
        var lannWorldLater = Later(World(story, 5, "trickster", "trickster.ever", Killed, P + "cairn_built", P + "cost.lied_to_lann", Returned, "lann.in_party"), 0);
        lannWorldLater.Times[Returned] = lannWorldLater.Hour - 71;
        check(!Avail(foundOut, lannWorldLater), "Trk_Wenduag_Lann: Lann finds out before 72 hours.");
        lannWorldLater.Times[Returned] = lannWorldLater.Hour - 72;
        check(Avail(foundOut, lannWorldLater), "Trk_Wenduag_Lann: Lann never finds out.");
        Take(foundOut, lannWorldLater, "truth", 0, P + "lann.paid_late");
        Take(foundOut, lannWorldLater, "refuse", 0, P + "lann.owed");
        var lied = Take(foundOut, lannWorldLater, "lie", 0, P + "lann.lied_again");
        check(Ch(foundOut, "price", 2).Alignment?.Direction == "Evil" && !lied.Has(Closed),
            "Trk_Wenduag_Lann: lying to Lann a second time is not an Evil shift, or it closes her route.");

        // Trk_Wenduag_Pages: one page per ending; no page for a live native romance.
        var ep = World(story, 6, "trickster.ever", Committed, P + "claim.given", P + "lann.paid");
        check(pages.Count(pg => Avail(pg, ep)) == 1 && Avail(S(P + "epilogue.pack"), ep),
            "Trk_Wenduag_Pages: the committed ending does not show exactly its own page.");
        check(Avail(S(P + "epilogue.dead"), World(story, 6, "trickster.ever", Closed, P + "cairn_built"))
              && Avail(S(P + "epilogue.unclaimed"), World(story, 6, "trickster.ever", Started))
              && !pages.Any(pg => Avail(pg, World(story, 6, "trickster.ever", "wenduag.romance_finished.latched"))),
            "Trk_Wenduag_Pages: a stayed-dead or unclaimed Wenduag has no page, or the native romance gets an RRT page.");

        // Trk_Wenduag_Household: the Last Call coda and household eligibility (committed, or her native romance kept to the end).
        var coda = story.Scenes.Single(s => s.Id == "wenduag.lastcall.page");
        check(coda.Requires.Contains(P + "partner") && story.Derived[P + "partner"].Any(g => g.SequenceEqual(new[] { Committed }))
              && story.Derived[P + "partner"].Any(g => g.SequenceEqual(new[] { "wenduag.romance_finished.latched" }))
              && story.Derived["wenduag.harem.eligible"].Any(g => g.SequenceEqual(new[] { "wenduag.romance_finished.latched" }))
              && story.Derived["wenduag.harem.eligible"].Any(g => g.SequenceEqual(new[] { Committed })),
            "Trk_Wenduag_Household: Last Call or the household does not count her commit and her native romance.");

        // Trk_Wenduag_Optional: her evil demand (the culling) is a real choice, and the optional beats never gate the commit.
        var neathers = S(P + "court.neathers");
        check(Ch(neathers, "ask", 0).Alignment?.Direction == "Evil" && Ch(neathers, "ask", 2).Alignment?.Direction == "Good" && neathers.Optional
              && !claim.Requires.Any(r => r.Contains("neathers") || r.Contains("hunt") || r.Contains("stinger")),
            "Trk_Wenduag_Optional: the culling is not a moral pivot, or an optional beat gates the claim.");
        Console.WriteLine("PASS: Wenduag Trickster (Trk_Wenduag_*): the staged blow and the cairn, the return and the closing no, the Commander's kills that stand, "
            + "the outbid on the traitor hub, the exile answers and the late bid, the falls in Savamelekh's house and the street (bought and unbought), "
            + "Lann's price, the native romance first, the chain to the claim and the cairn, " + pages.Length + " pages, Last Call and the household.");
    }
}
