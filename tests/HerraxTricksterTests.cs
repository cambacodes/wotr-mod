using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Herrax, Trickster (Writer/handoffs/trickster/herrax.md; binding plan 11-ROSTER-PLAN-2 §2, Herrax block and build sheet, R3):
// "The coup on her schedule". One block per rules test (Trk_Herrax_*): her night set on her hub after Rokhorn's own
// confession, the sale on Rokhorn's list (a Bluff, twin DC for his clients), the con and the blown con, the night (the pivotal
// knife), her proposal at closing, her refusal after a stayed hand and the knife returned hilt-first, the Chapter 5 fallbacks
// (never started, ended mid-chain), the one discovery about Chivarro, the pages, the reactors, and the courtship beats.
internal static class HerraxTricksterTests
{
    private const string Hub = "43f93812d6216c94db356622859397f1";
    private const string HubReturn = "1af69c65d15cc8949a4fe47a45c4f85d";
    private const string RokList = "571f316720b8d164b819495959222919";
    private const string RokReturn = "e7d43c3ec7ab16444be9759414f48436";
    private const string Coin = "1d5570f0d0d2b7b4ba805d48f492a749";
    private const string P = "herrax.trickster.";
    private const string Committed = "herrax.committed";
    private const string Closed = "herrax.closed";
    private const string Started = "herrax.started";
    private const string Primed = P + "primed";
    private const string Bait = P + "bait_taken";
    private const string Blown = P + "cost.con_blown";
    private const string Lesson = P + "lesson_given";
    private const string Declined = P + "declined";
    private const string Restored = P + "knife_restored";
    private const string Promised = P + "promised";
    private static readonly string[] Base = { "trickster", "trickster.ever", "herrax.madam", "herrax.met", "herrax.rokhorn_confessed", "herrax.coin_held" };

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        // eng-final E-Q8-10: fund the positive fixture; the walker enforces every debit.
        var state = new Snapshot { Chapter = chapter, Hour = 5000,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
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
            var hits = Program.WalkVia(scene, w, node, index);
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        Snapshot Take(Scene scene, Snapshot w, string node, int index, params string[] also)
        {
            var hit = Through(scene, w, node, index).FirstOrDefault(r => also.All(r.Has));
            check(hit != null, "No outcome of " + scene.Id + " through " + node + "[" + index + "] with " + string.Join(", ", also));
            return hit ?? w;
        }
        var own = story.Scenes.Where(s => s.Relationship == "herrax" && !s.Reaction && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var rel = story.Relationships["herrax"];
        var schedule = S(P + "madam.schedule");
        var sell = S(P + "madam.sell_the_night");
        var night = S(P + "madam.the_night");
        var reachable = S(P + "madam.reachable");
        var hilt = S(P + "madam.hilt_first");
        var restored = S(P + "madam.reachable_restored");
        var nextMove = S(P + "late.next_move");
        var owed = S(P + "owed.night");
        var seen = S(P + "chivarro_seen");
        var pages = story.Scenes.Where(s => s.Relationship == "herrax" && s.Owner == "HerraxEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "herrax" && s.Reaction).ToArray();
        var beats = own.Where(s => s.Id.StartsWith("herrax.house.", StringComparison.Ordinal)).ToArray();
        var letters = own.Where(s => s.Id.StartsWith("herrax.letters.", StringComparison.Ordinal)).ToArray();

        // Shape and hooks.
        check(rel.StartedFlag == Started && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed && rel.UnavailableFlags.Length == 0
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "madam", "not_started" }),
            "Herrax's relationship does not match the plan (no unavailability; madam and not-started access).");
        check(story.InventoryItems["herrax.coin_held"] == Coin && story.RemovableItems.Contains(Coin)
              && story.SelectedAnswers["herrax.rokhorn_confessed"] == "c60613dca14bf0943a428246cf51bb3a"
              && story.SelectedAnswers["herrax.rokhorn_client"] == "33447e2dcba529f4ba678688db744411",
            "The coin, Rokhorn's confession or his client answer is not bound as the build sheet says.");
        var removals = own.SelectMany(s => s.Nodes.SelectMany(n => n.Choices).Where(c => c.RemoveItem != null).Select(c => (s, c))).ToList();
        check(removals.Count == 2 && removals.All(x => x.c.RemoveItem == Coin && (x.c.Requires.Contains("herrax.coin_held") || x.s.Requires.Contains("herrax.coin_held"))),
            "Every coin removal must require the coin held (the sale, and the coin handed back before the house).");
        foreach (var hall in own.Where(s => s.AnswerLists.Contains(Hub)))
            check(hall.NativeReturnCue == HubReturn && hall.ContactUnit == null && hall.MinChapter == 4 && hall.MaxChapter == 4
                  && hall.Requires.Contains("herrax.madam") && hall.Requires.Contains("herrax.met") && hall.Forbids.Contains(Closed),
                "A hall scene is not inline on her hub, Chapter 4, behind her madamship and her closure: " + hall.Id);
        foreach (var rok in own.Where(s => s.AnswerLists.Contains(RokList)))
            check(rok.NativeReturnCue == RokReturn && rok.MinChapter == 4 && rok.MaxChapter == 4
                  && rok.Nodes.Where(n => n.Speaker == "Rokhorn").All(n => n.SpeakerUnit == "25ad116e1f5008e488b13f9b968596d4"),
                "A Rokhorn scene is not inline on his list, returning to Cue_0159, with his own portrait: " + rok.Id);
        check(own.All(s => s.Id == seen.Id || s.Id == seen.Id + "_stall" || !s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g))
                           .Any(f => f.StartsWith("minagho_chivarro.", StringComparison.Ordinal) || f == "chivarro.dead" || f.StartsWith("minachiv.", StringComparison.Ordinal))),
            "A Herrax scene other than the one discovery gates on Minagho or Chivarro (node-level reads only).");
        check(!own.Any(s => s.AnswerLists.Contains("0f12118177d102f428a3b30b15b132eb") || s.AnswerLists.Contains("a380d926e92f70e429681eb9654478f9")
                            || s.AnswerLists.Contains("15f754455d1d87c42a4e14df456d5415"))
              && story.Presences.Keys.Where(k => k.StartsWith("herrax", StringComparison.Ordinal)).OrderBy(k => k).SequenceEqual(new[] { "herrax.presence.rokhorn", "herrax.presence.rokhorn_stall" }),
            "A Herrax scene hangs on a crowded hub, or the presences are not Rokhorn's two (she has none of her own in Drezen).");
        check(!own.Any(s => s.Nodes.Any(n => n.Choices.Any(c => c.Set.Any(f => f.StartsWith("trickster.wmt.use.", StringComparison.Ordinal))))),
            "Herrax's device spends a Word Made True (the budget is full: a con, not a word made true).");

        // Trk_Herrax_Con: her night set, sold, cut, and her proposal.
        var w = World(story, 4, Base);
        check(Avail(schedule, w) && schedule.TricksterDevice && Ch(schedule, "start", 0).Mythic == "PlayerIsTrickster"
              && !Avail(schedule, World(story, 4, Base.Where(f => f != "herrax.rokhorn_confessed").ToArray()))
              && !Avail(schedule, World(story, 4, Base.Where(f => f != "herrax.coin_held").ToArray()))
              && !Avail(schedule, World(story, 4, Base.Where(f => f != "trickster").ToArray())),
            "Trk_Herrax_Con: her night is not set on the live path after Rokhorn's confession, with her coin in hand.");
        check(Program.Walk(schedule, w).Where(r => r.Has(schedule.Id)).All(r => r.Has(Primed) && r.Has(Started))
              && Ch(schedule, "quietly", 0).Abort,
            "Trk_Herrax_Con: the quiet offer is not her 'My house. My knife.' abort.");
        var primed = Take(schedule, w, "plan", 0, Primed, Started);
        check(Avail(sell, primed) && !Avail(sell, w), "Trk_Herrax_Con: the sale does not follow the set night.");
        var pitch = sell.Nodes.Single(n => n.Id == "wary").Choices;
        check(pitch[0].Check?.Skill == "CheckBluff" && pitch[0].Check?.DC == 28 && pitch[0].Forbids.Contains("herrax.rokhorn_client")
              && pitch[1].Check?.Skill == "CheckBluff" && pitch[1].Check?.DC == 23 && pitch[1].Requires.Contains("herrax.rokhorn_client")
              && pitch[0].Check?.Success == "bait" && pitch[0].Check?.Failure == "blown",
            "Trk_Herrax_Con: the sale is not a Bluff DC 28 (23 for his clients) with the con and the blown con.");
        check(Ch(sell, "bait_end", 0).RemoveItem == Coin && Ch(sell, "bait_end", 0).Requires.Contains("herrax.coin_held"),
            "Trk_Herrax_Con: the coin does not leave with the sale.");
        var sold = Take(sell, primed, "bait_end", 0, Bait, P + "cost.coin_lost");
        check(!Avail(night, Later(story, sold, 12)) && Avail(night, Later(story, sold, 24)), "Trk_Herrax_Con: the night does not come a day after the sale.");
        var knife = night.Nodes.Single(n => n.Id == "knife").Choices;
        check(knife.Count == 3 && knife[0].Alignment?.Direction == "Evil" && knife[0].Alignment?.Value == 1 && knife[0].Set.Contains(P + "knife_taken")
              && knife[1].Alignment == null && knife[1].Set.Contains(P + "knife_handed_back")
              && knife[2].Alignment?.Direction == "Good" && knife[2].Set.Contains(Declined) && knife.All(c => c.Set.Contains(Lesson)),
            "Trk_Herrax_Con: the night is not the pivot (cut him yourself, Evil; hand it back; stay her hand, Good).");
        var cut = Take(night, Later(story, sold, 24), "knife", 0, Lesson, P + "knife_taken");
        check(!Avail(reachable, Later(story, cut, 12)) && Avail(reachable, Later(story, cut, 24)), "Trk_Herrax_Con: her proposal does not come at the next closing.");
        var yes = Take(reachable, Later(story, cut, 24), "offer", 0, Committed, P + "morning_served");
        check(yes.Has(Committed) && Take(reachable, Later(story, cut, 24), "offer", 1, Closed).Has(Closed),
            "Trk_Herrax_Con: yes is not the commit, or no is not the Commander's own close.");
        // eng7-l13: live eligibility is required; no new test or price is allowed.
        check(!reachable.Nodes.Any(n => n.Id == "offer" && n.Choices.Any(c => c.Check != null || c.Crusade != null || c.Requires.Any(k => k != "trickster.now" && k != "herrax.outcome.route_open"))),
            "Trk_Herrax_Con: her proposal carries a test, a price or a gate.");

        // Trk_Herrax_ConBlown: the failure plays out in public, and still reaches the yes.
        var blown = Take(sell, primed, "loud", 0, Blown, P + "cost.clawed_cheek");
        check(!blown.Has(P + "cost.coin_lost") && Avail(night, Later(story, blown, 24)), "Trk_Herrax_ConBlown: the blown sale takes the coin, or skips the night.");
        check(Ch(night, "hall_coin", 0).RemoveItem == Coin && Ch(night, "hall_coin", 0).Requires.Contains("herrax.coin_held")
              && Ch(night, "hall_coin", 1).Forbids.Contains("herrax.coin_held"),
            "Trk_Herrax_ConBlown: the coin is not handed back before the house (or no road without it).");
        var handed = Take(night, Later(story, blown, 24), "knife", 1, Lesson, P + "knife_handed_back", P + "coin_handed_back");
        check(Take(reachable, Later(story, handed, 24), "offer", 0, Committed).Has(Committed), "Trk_Herrax_ConBlown: no yes after the blown con.");
        var noCoin = World(story, 4, Base.Where(f => f != "herrax.coin_held").Concat(new[] { Primed, Blown }).ToArray());
        check(Avail(night, noCoin) && Through(night, noCoin, "knife", 1).Any(), "Trk_Herrax_ConBlown: a lost coin strands the night.");

        // Trk_Herrax_StayedHand_WithChivarro: her refusal, the knife hilt-first, and the yes; Chivarro's route untouched.
        var withChiv = World(story, 4, Base.Concat(new[] { "minagho_chivarro.trickster.reunited", "minagho_chivarro.committed", Primed, Bait }).ToArray());
        var stayed = Take(night, Later(story, withChiv, 24), "knife", 2, Declined, Lesson);
        check(!Avail(reachable, Later(story, stayed, 24)) && Avail(hilt, Later(story, stayed, 24)), "Trk_Herrax_StayedHand: her refusal does not hold, or the knife cannot go back.");
        var back = Take(hilt, Later(story, stayed, 24), "start", 0, Restored);
        // Sol INT: the closing follows the punishment the Commander watched, a day later (never the same evening).
        var lateNight = S("herrax.house.a_night_late");
        check(!Avail(restored, Later(story, back, 24)) && Avail(lateNight, Later(story, back, 13)), "Trk_Herrax_StayedHand: the closing comes before the punishment it recalls.");
        var punished = Take(lateNight, Later(story, back, 13), "said", 0);
        check(!Avail(restored, Later(story, punished, 1)) && Avail(restored, Later(story, punished, 24)), "Trk_Herrax_StayedHand: the closing does not wait a day after the punishment.");
        var yesAgain = Take(restored, Later(story, punished, 24), "offer", 0, Committed);
        check(yesAgain.Has(Committed) && yesAgain.Has("minagho_chivarro.trickster.reunited") && yesAgain.Has("minagho_chivarro.committed")
              && !own.Any(s => s.Nodes.Any(n => n.Choices.Any(c => c.Set.Any(f => f.StartsWith("minagho_chivarro.", StringComparison.Ordinal))))),
            "Trk_Herrax_StayedHand_WithChivarro: no yes after the knife, or her route touches Minagho and Chivarro's flags.");

        // Trk_Herrax_NoMadam: never started in Chapter 4 (never met, or never told); the letter, and the page after the Threshold.
        var unmet = World(story, 5, "trickster", "trickster.ever", "herrax.madam");
        // Sol CAN: where Chivarro was never removed, Herrax is not the madam, and no courier of hers comes.
        // Sol COX: where Chivarro never fell, Herrax is a senior girl of the house, not the madam: her courier still comes,
        // with her own rooms at stake, and the page after the Threshold reads her place (Minagho/Chivarro untouched).
        var neverFell = World(story, 5, "trickster", "trickster.ever", "minagho_chivarro.committed");
        var nfNodes = new HashSet<string>(); Program.Walk(S(P + "late.next_move"), neverFell, (id, _) => nfNodes.Add(id));
        check(Avail(S(P + "late.next_move"), neverFell) && nfNodes.Contains("stranger_house") && !nfNodes.Contains("stranger")
              && Program.Walk(S(P + "late.next_move"), neverFell).Where(r => r.Has(P + "promised")).All(r => r.Flags.Where(f => f.StartsWith("minagho_chivarro.", StringComparison.Ordinal) && !story.Derived.ContainsKey(f)).SequenceEqual(new[] { "minagho_chivarro.committed" })),
            "Trk_Herrax_NeverMadam: no courier where Chivarro never fell, or the courier treats her as the madam.");
        check(Avail(nextMove, unmet) && nextMove.TricksterDevice && nextMove.TricksterState == "not_started" && !Avail(owed, unmet),
            "Trk_Herrax_NoMadam: her courier does not find a Commander who never started.");
        var met5 = World(story, 5, "trickster", "trickster.ever", "herrax.met", "herrax.madam");
        var route = nextMove.Nodes.Single(n => n.Id == "start").Choices;
        check(route.Single(c => Rules.Match(c.Requires, c.Forbids, unmet)).Next == "stranger" && route.Single(c => Rules.Match(c.Requires, c.Forbids, met5)).Next == "met",
            "Trk_Herrax_NoMadam: the courier does not speak to the met and unmet worlds.");
        var promise = Take(nextMove, unmet, "door", 0, Primed, Promised, Started);
        var late = pages.Single(s => s.Id == P + "epilogue.after_hours");
        check(Avail(late, World(story, 6, promise.Flags.ToArray())) && !Avail(pages.Single(s => s.Id == P + "epilogue.reachable"), World(story, 6, "trickster.ever", Promised)),
            "Trk_Herrax_NoMadam: the page after the Threshold does not answer her letter.");
        check(story.Derived[P + "late_committed"].Any(g => g.Contains(Promised)) && story.Derived["herrax.harem.eligible"].Any(g => g.Length == 1 && g[0] == P + "late_committed"),
            "Trk_Herrax_NoMadam: the late commit is not the R2-6 late_committed key, or eligibility ignores it.");
        check(!Avail(nextMove, World(story, 5, "trickster.ever", "trickster.was")), "Trk_Herrax_NoMadam: the courier comes after the path is lost.");

        // Trk_Herrax_Owed: Chapter 4 ended mid-chain; one letter, every state, and a reachable yes.
        var states = new (string node, string[] flags)[]
        {
            ("unsold", new[] { Primed }), ("sold", new[] { Primed, Bait }), ("blown", new[] { Primed, Blown }),
            ("lesson", new[] { Primed, Bait, Lesson, P + "knife_taken" }), ("knife", new[] { Primed, Bait, Lesson, Declined }),
            ("restored", new[] { Primed, Bait, Lesson, Declined, Restored }),
            ("restored_watched", new[] { Primed, Bait, Lesson, Declined, Restored, "herrax.house.a_night_late" }),
        };
        foreach (var (node, flags) in states)
        {
            var ow = World(story, 5, new[] { "trickster", "trickster.ever" }.Concat(flags).ToArray());
            check(Avail(owed, ow) && !Avail(nextMove, ow), "Trk_Herrax_Owed_" + node + ": the owed letter does not come, or both letters do.");
            var next = owed.Nodes.Single(n => n.Id == "start").Choices.Where(c => Rules.Match(c.Requires, c.Forbids, ow)).Select(c => c.Next).ToList();
            check(next.Count == 1 && next[0] == node, "Trk_Herrax_Owed_" + node + ": the letter speaks from the wrong state (" + string.Join(",", next) + ").");
            var promised = Take(owed, ow, "ask", 0, Promised);
            check(Avail(late, World(story, 6, promised.Flags.ToArray())), "Trk_Herrax_Owed_" + node + ": no page after the Threshold.");
        }
        check(!Avail(owed, World(story, 5, "trickster.ever", Primed, Bait, Lesson, Committed)), "Trk_Herrax_Owed: the owed letter comes after the commit.");

        // Trk_Herrax_ChivarroSeen: the one discovery (ledger 05 row 13).
        Snapshot InDrezen(Snapshot s) { var t = Program.Copy(s); t.Area = "2570015799edf594daf2f076f2f975d8"; t.AvailableContacts.Add("25ad116e1f5008e488b13f9b968596d4"); return t; }
        // eng8-q8e: historical reunion alone is not current physical presence.
        Snapshot ChivarroAtSide(params string[] flags) => InDrezen(World(story, 5, flags.Concat(new[] { "minagho_chivarro.trickster.chivarro_in" }).ToArray()));
        var chiv = ChivarroAtSide("trickster.ever", Started, "herrax.asked_kill_chivarro", "minagho_chivarro.trickster.reunited", "herrax.letters.the_courier");
        check(Avail(seen, chiv) && Avail(seen, ChivarroAtSide("trickster.ever", Started, "herrax.asked_kill_chivarro", "minagho_chivarro.trickster.returned_chivarro", P + "owed.night"))
              && !Avail(seen, ChivarroAtSide("trickster.ever", Started, "herrax.asked_kill_chivarro", "minagho_chivarro.trickster.returned_chivarro", "minagho_chivarro.trickster.chivarro_deposit", "minagho_chivarro.trickster.cost.herrax_favor", "herrax.letters.the_courier"))
              && !Avail(seen, ChivarroAtSide("trickster.ever", Started, "minagho_chivarro.trickster.reunited", "herrax.letters.the_courier"))
              && !Avail(seen, ChivarroAtSide("trickster.ever", Started, "herrax.asked_kill_chivarro", "minagho_chivarro.trickster.reunited"))
              && !Avail(seen, ChivarroAtSide("trickster.ever", Started, "herrax.asked_kill_chivarro", "minagho_chivarro.trickster.reunited", "herrax.letters.the_courier", "minagho_chivarro.trickster.chivarro_sent_back"))
              && !Avail(seen, ChivarroAtSide("trickster.ever", Started, "herrax.asked_kill_chivarro", "minagho_chivarro.trickster.reunited", "herrax.letters.the_courier", "minachiv.closed"))
              && !Rules.IsRemote(seen) && seen.InteractionHub == "herrax.presence.rokhorn",
            "Trk_Herrax_ChivarroSeen: the discovery does not follow her request and Chivarro alive at the Commander's side, or fires over a sale.");
        var kept = Take(seen, chiv, "start", 0, P + "cost.contract_unfinished", P + "contract.kept_out");
        check(!kept.Flags.Any(f => f.StartsWith("minagho_chivarro.", StringComparison.Ordinal) && !chiv.Has(f)) && !kept.Has(Closed),
            "Trk_Herrax_ChivarroSeen: the discovery sets Minagho and Chivarro's flags, or closes Herrax.");

        // Trk_Herrax_PathFailed: nothing new opens off the path, but the chain in progress is honoured.
        check(!Avail(schedule, World(story, 4, Base.Where(f => f != "trickster").Concat(new[] { "trickster.was" }).ToArray()))
              && Avail(night, Later(story, World(story, 4, "trickster.ever", "trickster.was", "herrax.madam", "herrax.met", Primed, Bait), 24)),
            "Trk_Herrax_PathFailed: the night is set off the path, or a sold night is lost with it.");

        // Pages.
        check(pages.Length == 4 && pages.All(s => s.MinChapter == 6 && s.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.RemoveItem == null))),
            "Herrax's pages are not four effect-free Chapter 6 pages.");
        check(Avail(pages.Single(s => s.Id == P + "epilogue.reachable"), World(story, 6, "trickster.ever", Committed))
              && Avail(pages.Single(s => s.Id == P + "epilogue.knife"), World(story, 6, "trickster.ever", Declined))
              && !Avail(pages.Single(s => s.Id == P + "epilogue.knife"), World(story, 6, "trickster.ever", Declined, Restored)),
            "Herrax's pages do not follow the yes, or the knife kept.");

        // Reactors: Arueshalae, Regill and Woljif (ledger 05 §3.1 row 20), on their own hubs.
        check(reactions.Length == 7 && reactions.Select(s => s.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Arueshalae", "Regill", "Woljif" })
              && reactions.All(s => s.AnswerLists.Length == 1 && s.Forbids.Length > 0),
            "Herrax's reactions are not the three allocated reactors on their hubs, each with its guard.");

        // Courtship: every beat is reachable on some road; Chapter 5 carries one letter (the packet), after the yes. The six
        // later letters of the first build are folded into it and retired by gating on the packet (never deleted).
        var courier = letters.Single(s => s.Id == "herrax.letters.the_courier");
        var retired = letters.Where(s => s != courier).ToArray();
        check(beats.Length >= 18 && letters.Length == 7 && letters.All(s => Rules.IsRemote(s) && s.Chapters.SequenceEqual(new[] { 5 }))
              && courier.Requires.Contains(Committed) && retired.All(s => s.Forbids.Contains("herrax.letters.bundle"))
              && courier.Nodes[0].Choices.All(c => c.Set.Contains("herrax.letters.bundle")),
            "Herrax's courtship is not the Chapter 4 beats and the one Chapter 5 packet after the yes (the folded letters retired).");
        // A greedy playthrough per road: every available scene is played through its first completing outcome that keeps her open.
        var reachedIds = new HashSet<string>();
        void Play(Snapshot start, int chapter, int rounds, params string[] avoid)
        {
            var state = start;
            for (int i = 0; i < rounds; i++)
            {
                state = Later(story, state, 48, chapter);
                foreach (var scene in own.OrderBy(s => s.Id.StartsWith("herrax.house.", StringComparison.Ordinal) ? 0 : 1).Where(s => Avail(s, state)).ToList())
                {
                    if (!Avail(scene, state)) continue;
                    var outcome = Program.Walk(scene, state).FirstOrDefault(r => r.Has(scene.Id) && !r.Has(Closed) && !avoid.Any(r.Has));
                    if (outcome == null) continue;
                    reachedIds.Add(scene.Id);
                    state = outcome;
                }
            }
        }
        Play(World(story, 4, Base.Concat(new[] { "herrax.haggled", "herrax.asked_kill_chivarro" }).ToArray()), 4, 16, Declined, Blown);
        Play(World(story, 4, Base.Concat(new[] { Primed, Bait, Lesson, Declined }).ToArray()), 4, 3, Restored);
        Play(World(story, 4, Base.Concat(new[] { Primed, Bait, Lesson, Declined, Restored }).ToArray()), 4, 3);
        Play(World(story, 5, "trickster", "trickster.ever", "herrax.met", Primed, Bait, Lesson, P + "knife_taken", Committed, P + "cost.clawed_cheek"), 5, 12);
        foreach (var scene in beats.Concat(new[] { courier }))
            check(reachedIds.Contains(scene.Id), "Herrax: the beat " + scene.Id + " is never reachable.");
        foreach (var scene in retired)
            check(!reachedIds.Contains(scene.Id), "Herrax: the folded letter " + scene.Id + " is still delivered after the packet.");

        // Sol INT/HOW: the coin demonstration is about a coin the Commander still holds; it closes once the coin is sold
        // (RemoveItem clears the inventory observation), handed back before the house, or lost elsewhere.
        var coinBeat = S("herrax.house.the_coin");
        var coinWorld = World(story, 4, Base.Concat(new[] { "herrax.house.first_price" }).ToArray());
        check(Avail(coinBeat, coinWorld), "Trk_Herrax_Coin: the coin demonstration does not open while the coin is held.");
        var soldWorld = Take(sell, Program.Copy(primed), "bait_end", 0, Bait);
        soldWorld.Flags.Add("herrax.house.first_price");
        check(!soldWorld.Has("herrax.coin_held") && !Avail(coinBeat, Later(story, soldWorld, 48)),
            "Trk_Herrax_Coin: the coin demonstration survives the sale of the coin.");
        var handedBack = Take(night, Later(story, blown, 24), "hall_coin", 0, P + "coin_handed_back");
        handedBack.Flags.Add("herrax.house.first_price");
        check(!handedBack.Has("herrax.coin_held") && !Avail(coinBeat, Later(story, handedBack, 48)),
            "Trk_Herrax_Coin: the coin demonstration survives the coin handed back before the house.");
        check(!Avail(coinBeat, World(story, 4, Base.Where(f => f != "herrax.coin_held").Concat(new[] { "herrax.house.first_price" }).ToArray())),
            "Trk_Herrax_Coin: the coin demonstration opens with the coin lost elsewhere.");

        // Sol INT: every living history reaches its page; a Last Call bottle survival (sacrifice + commander_back, without the
        // native punchline key) is alive, and a real death is not.
        var reachablePage = pages.Single(s => s.Id == P + "epilogue.reachable");
        foreach (var page in new[] { reachablePage, late })
        {
            var basis = page == late ? promise.Flags.ToArray() : new[] { "trickster.ever", Committed };
            check(Avail(page, World(story, 6, basis))
                  && Avail(page, World(story, 6, basis.Concat(new[] { "sacrifice", "trickster.commander_back" }).ToArray()))
                  && !Avail(page, World(story, 6, basis.Concat(new[] { "sacrifice" }).ToArray())),
                "Trk_Herrax_Survival: " + page.Id + " does not follow the Commander's survival (commander_back), or plays over a death.");
        }

        // Sol TRK (R2-2): the late road is a present, priced act. Her letter is an innocent invitation (the plan is under the
        // coin in her seal); the promise is set only after the doorstep con, and always with its cost.
        var lateOutcomes = Program.Walk(nextMove, unmet).Where(r => r.Has(Promised)).ToList();
        check(lateOutcomes.Count > 0 && lateOutcomes.All(r => r.Has(P + "cost.late") && r.Has(Primed) && r.Has(Started)),
            "Trk_Herrax_LateCon: the late promise is set without the doorstep con's cost.");
        var earnest = nextMove.Nodes.Single(n => n.Id == "earnest").Choices[0];
        var doubted = nextMove.Nodes.Single(n => n.Id == "earnest_doubted").Choices[0];
        check(earnest.Check?.Skill == "CheckBluff" && earnest.Check?.Success == "earnest_taken" && earnest.Check?.Failure == "earnest_doubted"
              && doubted.Crusade?.Resource == "Finances" && doubted.Crusade?.Amount == -500
              && nextMove.Nodes.Where(n => n.Id == "door" || n.Id == "why").All(n => n.Choices.All(c => !c.Set.Contains(Promised))),
            "Trk_Herrax_LateCon: the doorstep con is not a Bluff with a paid fallback, or the promise is still a bare answer.");

        // Sol COX (05 §4.2): one Herrax letter in Chapter 5 on the worst branch, discovery included, through actual delivery.
        int Ch5Letters(Snapshot start)
        {
            var state = start; int delivered = 0;
            for (int rest = 0; rest < 30; rest++)
            {
                state = Later(story, state, 24, 5);
                var arrived = Rules.MailbagArrivals(story, state).Where(s => s.Relationship == "herrax").ToList();
                foreach (var letter in arrived)
                {
                    var outcome = Program.Walk(letter, state).Where(r => r.Has(letter.Id) && !r.Has(Closed)).OrderByDescending(r => r.Flags.Count).FirstOrDefault();
                    if (outcome == null) continue;
                    delivered++; state = outcome;
                }
            }
            return delivered;
        }
        var chivWorlds = new[] { "herrax.asked_kill_chivarro", "minagho_chivarro.trickster.reunited", "minagho_chivarro.trickster.chivarro_in" };
        foreach (var (name, flags) in new (string, string[])[] {
            ("committed", new[] { "trickster", "trickster.ever", "herrax.madam", "herrax.met", Started, Primed, Bait, Lesson, P + "knife_taken", Committed }),
            ("owed", new[] { "trickster", "trickster.ever", "herrax.met", Started, Primed }),
            ("late", new[] { "trickster", "trickster.ever", "herrax.met", "herrax.madam" }) })
        {
            var count = Ch5Letters(World(story, 5, flags.Concat(chivWorlds).ToArray()));
            check(count == 1, "Trk_Herrax_OneCh5Letter_" + name + ": " + count + " Herrax letters delivered in Chapter 5 (cap 1, discovery included).");
        }
        var packetWalk = Program.Walk(courier, World(story, 5, "trickster.ever", Committed, Primed, Bait, Lesson, P + "knife_taken", Started, "herrax.asked_kill_chivarro", "minagho_chivarro.trickster.reunited", "minagho_chivarro.trickster.chivarro_in"));
        check(packetWalk.Any(r => r.Has(P + "contract.kept_out")) && packetWalk.Any(r => r.Has(P + "contract.stood_by_her")),
            "Trk_Herrax_Discovery_Folded: the packet does not carry the one discovery.");

        // Sol INT: Chivarro back after the packet was read: the discovery is not lost; Rokhorn waited in Drezen for it, and it
        // is the only Herrax scene then, and physical (the one-letter cap holds).
        var packetFirst = Program.Walk(courier, World(story, 5, "trickster", "trickster.ever", "herrax.madam", "herrax.met", Started, Primed, Bait, Lesson, P + "knife_taken", Committed, "herrax.asked_kill_chivarro"))
            .First(r => r.Has(courier.Id) && !r.Has(Closed));
        check(!packetFirst.Has(P + "cost.contract_unfinished"), "Trk_Herrax_LateReturn: the packet settles a discovery before Chivarro is back.");
        var backLater = InDrezen(Later(story, packetFirst, 48));
        backLater.Flags.Add("minagho_chivarro.trickster.reunited");
        backLater.Flags.Add("minagho_chivarro.trickster.chivarro_in");
        ImplicitParticipantInventoryTests.Observe(story, backLater);
        check(Avail(seen, backLater) && Rules.MailbagArrivals(story, backLater).All(s => s.Relationship != "herrax"),
            "Trk_Herrax_LateReturn: Chivarro returning after the packet has no discovery, or it arrives as a second letter.");
        check(Take(seen, backLater, "start", 1, P + "contract.stood_by_her").Has(P + "cost.contract_unfinished"), "Trk_Herrax_LateReturn: no answer to carry home.");
        var stall = S(P + "chivarro_seen_stall");
        var kingGone = Program.Copy(backLater); kingGone.Flags.Add("fool_king.gone");
        check(story.Presences["herrax.presence.rokhorn"].Forbids.Contains("fool_king.gone") && Avail(stall, kingGone) && stall.Forbids.Contains(seen.Id) && seen.Forbids.Contains(stall.Id),
            "Trk_Herrax_LateReturn: Rokhorn has no place to wait when the King is gone.");

        // Sol CAN: the white room holds Dyunk's girls only if the Commander sent them there (Answer_0039); watching Herrax
        // haggle is not a sale.
        var laby = S("herrax.house.labyrinth");
        var labyWorld = World(story, 4, Base.Concat(new[] { "herrax.house.first_price", "herrax.haggled" }).ToArray());
        var labyNodes = new HashSet<string>();
        Program.Walk(laby, Later(story, labyWorld, 24), (id, _) => labyNodes.Add(id));
        check(labyNodes.Contains("asset_empty") && !labyNodes.Contains("asset_yours") && !labyNodes.Contains("asset"),
            "Trk_Herrax_WhiteRoom: witnessing the haggle puts the girls in her house, or remembers a sale.");
        var sentNodes = new HashSet<string>();
        var sentWorld = World(story, 4, Base.Concat(new[] { "herrax.house.first_price", "herrax.aasimars_sent" }).ToArray());
        Program.Walk(laby, Later(story, sentWorld, 24), (id, _) => sentNodes.Add(id));
        check(sentNodes.Contains("asset_yours") && !sentNodes.Contains("asset_empty") && story.SelectedAnswers["herrax.aasimars_sent"] == "2bfaec7837a9a4a40a43e73f06b3cf51",
            "Trk_Herrax_WhiteRoom: sending the girls to the Delights is not what fills the room.");

        // Sol INT: Arueshalae recalls her sermon in the hall only if the Commander heard it.
        var heardMorning = S(P + "react.arueshalae_morning");
        var unheardMorning = S(P + "react.arueshalae_morning_unheard");
        var morningWorld = World(story, 4, "trickster.ever", "arueshalae.in_party", P + "morning_served"); // eng7-l05: current reactor recruitment.
        check(!Avail(heardMorning, morningWorld) && Avail(unheardMorning, morningWorld)
              && Avail(heardMorning, World(story, 4, "trickster.ever", "arueshalae.in_party", P + "morning_served", "herrax.sermon_heard"))
              && !Avail(unheardMorning, World(story, 4, "trickster.ever", "arueshalae.in_party", P + "morning_served", "herrax.sermon_heard")),
            "Trk_Herrax_Sermon: Arueshalae recalls a warning the Commander never heard.");

        // Sol INT: telling Herrax about Rokhorn's offer has her answer in the packet.
        var toldNodes = new HashSet<string>();
        Program.Walk(courier, World(story, 5, "trickster.ever", Committed, Lesson, P + "knife_taken"), (id, _) => toldNodes.Add(id));
        check(toldNodes.Contains("b_told_answer") && Program.WalkVia(courier, World(story, 5, "trickster.ever", Committed, Lesson, P + "knife_taken"), "b_offer2", 2).All(r => r.Has("herrax.letters.offer.told_her")),
            "Trk_Herrax_OfferTold: the reported offer has no answer.");

        // Sol INT: Rokhorn's stitches remember the history the player made (trusted and robbed, or scratched and still cut).
        var stitched = S("herrax.house.rokhorn.stitched");
        foreach (var (hist, node) in new (string, string)[] { (Bait, "read"), (Blown, "read_blown") })
        {
            var sn = new HashSet<string>();
            Program.Walk(stitched, World(story, 4, Base.Concat(new[] { Primed, hist, Lesson, P + "knife_taken" }).ToArray()), (id, _) => sn.Add(id));
            check(sn.Contains(node) && sn.Count(x => x.StartsWith("read", StringComparison.Ordinal)) == 1, "Trk_Herrax_Stitched: Rokhorn misremembers the " + node + " history.");
        }
        // Sol BEL: the lost bet is collected in the packet.
        var nightOut = S("herrax.house.a_night_out");
        var lost = Take(nightOut, World(story, 4, Base.Concat(new[] { Committed }).ToArray()), "bet", 1, "herrax.house.arena.bet_lost");
        var debtPaths = Program.Walk(courier, World(story, 5, lost.Flags.Where(f => f != "trickster").ToArray()));
        check(debtPaths.All(r => r.Has("herrax.letters.arena.bet_collected")) && Take(nightOut, World(story, 4, Base.Concat(new[] { Committed }).ToArray()), "bet", 0).Flags.All(f => f != "herrax.house.arena.bet_lost"),
            "Trk_Herrax_Bet: the lost bet is never collected, or a won bet is owed.");

        // Sol COX (ledger 05 row 2): after the Council the Lady is in hiding; the packet's court letter says so.
        var hidingSeen = new HashSet<string>();
        Program.Walk(courier, World(story, 5, "trickster.ever", Committed, Lesson, P + "knife_taken", "noct.defeated_not_dead"), (id, _) => hidingSeen.Add(id));
        var courtSeen = new HashSet<string>();
        Program.Walk(courier, World(story, 5, "trickster.ever", Committed, Lesson, P + "knife_taken"), (id, _) => courtSeen.Add(id));
        check(hidingSeen.Contains("b_lady_hiding") && !hidingSeen.Contains("b_lady") && courtSeen.Contains("b_lady") && !courtSeen.Contains("b_lady_hiding"),
            "Trk_Herrax_LadyHiding: the Lady's people act for her while she is in hiding (ledger 05 row 2).");
        Console.WriteLine("PASS: Herrax Trickster (Trk_Herrax_*): her night set, the sale and the blown sale, the knife, her proposal, the stayed hand and the hilt, "
                          + "the courier in both fallbacks, the one discovery, the pages, the reactors, " + beats.Length + " courtship beats, the packet, the coin, survival, the late con and the Chapter 5 cap.");
    }
}
