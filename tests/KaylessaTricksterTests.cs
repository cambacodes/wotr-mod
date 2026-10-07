using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Kaylessa, Trickster (Writer/handoffs/trickster/kaylessa.md; binding plan 11-ROSTER-PLAN-2 §2): "No lamb to the slaughter".
// One block per rules test (Trk_Kaylessa_*): Shyka's timeline trade in the dead worlds, the amulet swap in the living one,
// the spine after her return (rules, the clock, the pivot in the cells, the dagger), her proposal with no test, the knife
// put down on a table after the Commander's no, the pages, the three allocated reactors, Camellia's oath branch that her
// return closes, and the courtship around it (kaylessa_wasps before the knife, kaylessa_clearing after).
internal static class KaylessaTricksterTests
{
    private const string Unit = "a1569a0739314d04cb8af1d47dcffbe0";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Tailor = "253cdb8f434e5a6469b75e18428316e3";
    private const string PleaList = "07bc8bac6a8c8074183e6abb6ce56847";
    private const string PleaCue = "58f994154e180a147a4ab18381f9bc8c";
    private const string Goodbye = "0585a80d0b70442409f30afad8207e9d";
    private const string ShykaList = "e7236a1fe9273ba498b96b9616b3f379";
    private const string ShykaBack = "cd2b35a474db55544a63f59a67ac67bf";
    private const string P = "kaylessa.trickster.";
    private const string W = "kaylessa.wasps.";
    private const string N = "kaylessa.clearing.";
    private const string Dead = "kaylessa.dead";
    private const string Begged = "kaylessa.begged_death";
    private const string Returned = P + "returned";
    private const string Committed = "kaylessa.committed";
    private const string Closed = "kaylessa.closed";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        // eng-final E-Q8-10: fund the positive fixture; the walker enforces every debit.
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
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
        var own = story.Scenes.Where(s => s.Relationship == "kaylessa" && !s.Reaction && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        using var reachability = new ReachabilityCache();
        bool Reaches(Snapshot start, string flag, int chapter = 5, Func<Snapshot, bool>? keep = null)
            => keep == null
                ? reachability.Reaches(start, flag, chapter, () => Explore(Program.Copy(start), chapter, null))
                : Explore(Program.Copy(start), chapter, keep).Any(s => s.Has(flag));
        IEnumerable<Snapshot> Explore(Snapshot start, int chapter, Func<Snapshot, bool>? keep)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 20 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    yield return from;
                    var w = Later(story, from, 100, chapter);
                    foreach (var scene in own.Where(s => Avail(s, w)))
                        foreach (var r in Program.Walk(scene, w))
                        {
                            yield return r;
                            if (keep != null && !keep(r)) continue;
                            if (seen.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                        }
                }
                frontier = next.Take(300).ToList();
            }
        }

        var rel = story.Relationships["kaylessa"];
        var promise = S(P + "reveal.promise");
        var borrow = S(P + "dead.borrow");
        var soldier = S(P + "dead.soldier");
        var hunter = S(P + "alive.hunter");
        var warning = S(P + "alive.warning");
        var swap = S(P + "alive.amulet_swap");
        var rules = S(P + "after.rules");
        var clock = S(P + "after.dark_fate");
        var beast = S(P + "after.the_beast");
        var knife = S(P + "after.the_knife");
        var commit = S(P + "commit");
        var table = S(P + "after.knife_on_table");
        var pages = story.Scenes.Where(s => s.Relationship == "kaylessa" && s.Owner == "KaylessaEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "kaylessa" && s.Reaction).ToArray();

        // Shape and hooks.
        check(rel.StartedFlag == "kaylessa.started" && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.SequenceEqual(new[] { Dead, "inhuman", P + "left_free", "kaylessa.early_player_killed" })
              && rel.UnavailableOverrides.Single().Key == Dead && rel.UnavailableOverrides.Single().Value == Returned
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "alive", "dead" }),
            "Kaylessa's relationship does not match the spec: unavailable=" + string.Join(",", rel.UnavailableFlags) + "; overrides=" + string.Join(",", rel.UnavailableOverrides.Select(p => p.Key + "=" + p.Value)) + "; access=" + string.Join(",", rel.TricksterAccess.Keys));
        check(promise.AnswerLists.SequenceEqual(new[] { PleaList }) && promise.NativeReturnCue == PleaCue && promise.Nodes.Count == 1
              && promise.EntryMythic == "PlayerIsTrickster" && Ch(promise, "start", 0).NativeNext == Goodbye
              && Ch(promise, "start", 0).Set.SequenceEqual(new[] { P + "promised" }),
            "The promise is not the one-node inline primer at her plea that continues into the native death.");
        check(borrow.AnswerLists.SequenceEqual(new[] { ShykaList }) && borrow.NativeReturnCue == ShykaBack && borrow.ContactUnit == null
              && borrow.Chapters.SequenceEqual(new[] { 3, 5 }) && borrow.EntryMythic == "PlayerIsTrickster"
              && borrow.TricksterDevice && borrow.TricksterState == "dead"
              && new[] { "shyka.gone", "council.fought", "council.fought_nocta_allied" }.All(borrow.Forbids.Contains),
            "The borrow is not Shyka's own inline hub device, closed by every outlived Council key.");
        check(new[] { hunter, warning, swap }.All(s => Rules.IsRemote(s) && s.MinChapter == 5)
              && new[] { hunter, swap }.All(s => s.TricksterDevice && s.TricksterState == "alive"),
            "The living world's device is not a Chapter 5 chain of Trickster device visits.");
        var presence = story.Presences["kaylessa.presence"];
        check(presence.Unit == Unit && presence.Dialog == "hub" && presence.At?.NearUnit == Tailor && presence.At!.Side == "left"
              && presence.At.Distance >= 2.0 && presence.MinChapter == 3 && presence.MaxChapter == 5,
            "Her presence is not the talkable copy beside the tailor's awning.");
        foreach (var hub in own.Where(s => !Rules.IsRemote(s) && s.InteractionHub == "kaylessa.presence"))
            check(hub.ContactUnit == Unit && hub.Areas.SequenceEqual(new[] { Drezen }) && hub.Forbids.Contains(Closed)
                  && hub.Requires.Contains("trickster.ever"),
                "A presence scene is not a Trickster-path hub scene behind her closure: " + hub.Id);
        check(!own.Any(s => s.AnswerLists.Contains("0f12118177d102f428a3b30b15b132eb") || s.AnswerLists.Contains("a380d926e92f70e429681eb9654478f9")),
            "A Kaylessa scene hangs on a crowded hub.");

        // Trk_Kaylessa_DeadEarly: every voluntary attack permanently closes all roads.
        foreach (var attack in new[] { "kaylessa.attack_kenabres_masked", "kaylessa.attack_kenabres_drow", "kaylessa.attack_camp" })
            foreach (var council in new[] { "", "shyka.gone", "council.fought", "council.fought_nocta_allied" })
            {
                var killed = World(story, 5, "trickster", "trickster.ever", Dead, attack, council,
                    P + "primed", Returned, Committed, P + "told_borrowed", P + "knife_shown", "kaylessa.wasps.in_the_dark");
                check(killed.Has("kaylessa.early_player_killed") && !Rules.RouteOpen(rel, killed)
                      && !killed.Has("kaylessa.harem.eligible") && !Avail(borrow, killed)
                      && !Avail(S(P + "dead.borrow_sending"), killed) && !Avail(soldier, killed)
                      && !Avail(commit, killed), "Trk_Kaylessa_DeadEarly: route reopened after " + attack + "/" + council);
            }
        // Positive payment, arrival and romance coverage belongs to plot-imposed Reveal deaths.
        var early = World(story, 3, "trickster", "trickster.ever", Dead, Begged);
        check(Avail(borrow, early) && !Avail(hunter, World(story, 5, "trickster", "trickster.ever", Dead)) && !Avail(soldier, early),
            "Trk_Kaylessa_Reveal: the borrow is not the only door.");
        check(Ch(borrow, "which", 1).Requires.Contains(Begged) && Ch(borrow, "which", 2).Forbids.Contains(Begged)
              && Ch(borrow, "trade", 3).Requires.Contains(Begged),
            "Trk_Kaylessa_Reveal: her plea's lines show without her plea.");
        var primed = Take(borrow, early, "trade", 0, P + "primed", P + "cost.shyka_price");
        check(Ch(borrow, "trade", 0).Alignment?.Direction == "Chaotic", "Trk_Kaylessa_Reveal: the trade is not a Chaotic act.");
        check(Avail(soldier, Later(story, primed, 12)) && !Avail(soldier, Later(story, primed, 6)),
            "Trk_Kaylessa_Reveal: she does not arrive twelve hours after the trade.");
        var back = Take(soldier, Later(story, primed, 12), "speak", 0, Returned, P + "cost.dark_fate_stalled");
        check(Reaches(back, Committed, 5), "Trk_Kaylessa_Reveal: no road to the commit.");
        check(Reaches(primed, Committed, 3), "Trk_Kaylessa_Reveal: no road from the trade to the commit.");

        // Trk_Kaylessa_Reveal_Raised (the failed haggle).
        var raised = Take(borrow, World(story, 5, "trickster", "trickster.ever", Dead, Begged), "raised", 0, P + "cost.shyka_raised");
        check(raised.Has(P + "primed") && Ch(borrow, "raised", 1).Abort, "Trk_Kaylessa_Raised: the raised price cannot be paid or refused.");
        check(Ch(borrow, "trade", 2).Check?.Skill == "CheckDiplomacy" && Ch(borrow, "trade", 2).Check!.Failure == "raised",
            "Trk_Kaylessa_Raised: the haggle is not a Diplomacy check whose failure raises the price.");

        // Trk_Kaylessa_Outlived: without Shyka there is no holder who can deliver; canon fate stands.
        foreach (var gone in new[] { "council.fought_nocta_allied", "council.fought", "shyka.gone" })
            check(!Avail(borrow, World(story, 5, "trickster", "trickster.ever", Dead, gone)) && !Avail(hunter, World(story, 5, "trickster", "trickster.ever", Dead, gone)),
                "Trk_Kaylessa_Outlived: a device opens after " + gone);

        // Trk_Kaylessa_Reveal and its pivotal decline.
        var reveal = World(story, 3, "trickster", "trickster.ever", Dead, Begged, P + "promised", "kaylessa.camellia_killed");
        check(Avail(borrow, reveal), "Trk_Kaylessa_Reveal: the borrow does not open after her plea.");
        var kept = Take(borrow, reveal, "trade", 3, P + "ending_kept", Closed);
        check(!kept.Has(P + "primed") && !Avail(borrow, Later(story, kept, 48)) && !Avail(soldier, Later(story, kept, 48)),
            "Trk_Kaylessa_Reveal_Decline: letting her keep her ending still opens the route.");
        var revealBack = Take(soldier, Later(story, Take(borrow, reveal, "trade", 0, P + "primed"), 12), "speak", 1, P + "lied_about_price", Returned);
        check(Reaches(revealBack, Committed, 5), "Trk_Kaylessa_Reveal: a lie about the price shuts the road.");

        // Trk_Kaylessa_Promise.
        var plea = World(story, 3, "trickster", "trickster.ever");
        check(Avail(promise, plea) && !Avail(promise, World(story, 3, "trickster.ever", "trickster.failed")), "Trk_Kaylessa_Promise: the promise is not a live-Trickster answer.");

        // Trk_Kaylessa_PathFailed.
        var failed = World(story, 5, "trickster.was", "trickster.ever", "trickster.failed", Dead);
        check(!Avail(borrow, failed) && !Avail(hunter, World(story, 5, "trickster.was", "trickster.ever", "trickster.failed")),
            "Trk_Kaylessa_PathFailed: a device opens after the path is lost.");

        // Trk_Kaylessa_Alive: Forn's courtesy, the plan, the swap.
        var alive = World(story, 5, "trickster", "trickster.ever", "kaylessa.met");
        check(Avail(hunter, alive) && !Avail(borrow, alive) && !Avail(hunter, World(story, 3, "trickster", "trickster.ever")),
            "Trk_Kaylessa_Alive: Forn does not come in Chapter 5 only, or the borrow opens without a death.");
        check(Ch(hunter, "ask", 2).Abort && Ch(hunter, "ask", 1).Check?.Skill == "SkillPerception",
            "Trk_Kaylessa_Alive: Forn cannot be refused, or his bandage cannot be studied.");
        var played = Take(hunter, alive, "seen", 0, P + "primed", P + "alive.wound_seen");
        check(Avail(warning, Later(story, played, 12)) && !Avail(swap, Later(story, played, 48)), "Trk_Kaylessa_Alive: the warning does not come first.");
        var planned = Take(warning, Later(story, played, 12), "terms", 1, P + "alive.planned", P + "alive.shield_sworn");
        var ready = Later(story, planned, 24);
        check(Avail(swap, ready), "Trk_Kaylessa_Alive: the ambush does not come.");
        var ridge = swap.Nodes.Single(n => n.Id == "ridge").Choices;
        check(ridge.Count == 3 && ridge.All(c => c.Check?.Skill == "SkillThievery") && ridge[0].Requires.Contains("trickster.trickery_tier1")
              && ridge[1].Requires.Contains(P + "alive.wound_seen") && ridge[2].Requires.Length == 0
              && ridge[0].Check!.DC < ridge[2].Check!.DC && ridge[1].Check!.DC < ridge[2].Check!.DC,
            "Trk_Kaylessa_Alive: the swap is not a Trickery check that the chosen trick or the spotted wound makes easier.");
        var clean = Take(swap, ready, "end", 0, Returned, P + "cost.amulet_burnt", P + "alive.swap_clean");
        var fumbled = Program.Walk(swap, ready).Where(r => r.Has(P + "alive.swap_fumbled")).ToList();
        check(fumbled.Count > 0 && fumbled.All(r => r.Has(Returned) && r.Has(P + "cost.council_knows") && r.Has(P + "cost.amulet_burnt")
                                                   && r.Has(P + "cost.arrow_taken")),
            "Trk_Kaylessa_Alive: a failed swap does not still return her, at the cost of an arrow and a Council that knows.");
        check(Reaches(clean, Committed) && Reaches(fumbled[0], Committed), "Trk_Kaylessa_Alive: no road from the ravine to the commit.");
        var unshielded = Take(warning, Later(story, played, 12), "terms", 0, P + "alive.planned");
        check(Program.Walk(swap, Later(story, unshielded, 24)).Where(r => r.Has(P + "alive.swap_fumbled")).All(r => r.Has(P + "cost.her_collarbone") && !r.Has(P + "cost.arrow_taken")),
            "Trk_Kaylessa_Alive: without the Commander's oath, the arrow is not hers.");

        // Trk_Kaylessa_Spine: rules, the clock, the pivot, the dagger.
        var home = World(story, 5, "trickster", "trickster.ever", Returned, "kaylessa.started", P + "alive.swap_clean", P + "cost.amulet_burnt", W + "in_the_dark");
        check(Avail(rules, home) && !Avail(clock, home) && !Avail(commit, home), "Trk_Kaylessa_Spine: the rules are not first.");
        var ruled = Later(story, Take(rules, home, "rules", 0), 24);
        check(Avail(clock, ruled), "Trk_Kaylessa_Spine: the clock does not follow the rules.");
        var clocked = Later(story, Take(clock, ruled, "what", 0, P + "clock_named"), 48);
        check(Avail(beast, clocked), "Trk_Kaylessa_Spine: the cells do not follow the clock.");
        var key = beast.Nodes.Single(n => n.Id == "key").Choices;
        check(key[0].Alignment?.Direction == "Evil" && key[1].Alignment == null && key[2].Check?.Skill == "CheckDiplomacy",
            "Trk_Kaylessa_Pivot: the cell is not the pivotal moral node (Evil to feed it, a plain no, a harder third way).");
        var fed = Later(story, Take(beast, clocked, "key", 0, P + "cost.beast_fed"), 24);
        var sent = Later(story, Take(beast, clocked, "witness_after", 0, P + "wasp_sent_home"), 24);
        check(Avail(knife, fed) && Avail(knife, sent), "Trk_Kaylessa_Spine: the dagger does not follow the cells.");

        // Trk_Kaylessa_Commit: she proposes; no test; two yeses; the Commander's no; the road.
        var shown = Later(story, Take(knife, sent, "why", 0, P + "knife_shown"), 24);
        check(Avail(commit, shown), "Trk_Kaylessa_Commit: the knife is not offered after the dagger.");
        var ask = commit.Nodes.Single(n => n.Id == "ask").Choices;
        check(ask[0].Set.Contains(Committed) && ask[1].Set.Contains(Committed) && ask[1].Set.Contains(P + "knife_handed_back")
              && ask[2].Set.Contains(P + "declined") && !ask[2].Set.Contains(Closed) && ask[3].Set.Contains(Closed)
              && ask[4].Set.Contains(Committed) && ask[4].Requires.Contains(P + "cost.beast_fed"),
            "Trk_Kaylessa_Commit: the hilt is not two yeses, a no that keeps a yes, and the road.");
        check(Through(commit, shown, "ask", 0).All(r => r.Has(Committed)) && Through(commit, shown, "ask", 1).All(r => r.Has(Committed)),
            "Trk_Kaylessa_Commit: taking the knife or handing it back does not commit.");
        var fedShown = Later(story, Take(knife, fed, "why", 0, P + "knife_shown"), 24);
        check(Through(commit, fedShown, "ask", 4).All(r => r.Has(Committed) && r.Has(P + "knife_held")),
            "Trk_Kaylessa_Commit: after the cells she cannot be handed her own death back.");
        var no = Take(commit, shown, "ask", 2, P + "declined");
        check(!Avail(commit, Later(story, no, 96)) && Avail(table, Later(story, no, 72)), "Trk_Kaylessa_Declined: the knife is not put down later.");
        check(Through(table, Later(story, no, 72), "knife", 0).All(r => r.Has(Committed)) && Take(table, Later(story, no, 72), "knife", 2, Closed).Has(P + "left_free"),
            "Trk_Kaylessa_Declined: the knife on the table is not a yes (picked up) or a parting (left).");
        var liar = World(story, 5, "trickster", "trickster.ever", Returned, Dead, P + "lied_about_price", P + "knife_shown", P + "beast_met", W + "in_the_dark");
        // Rule three (Sol quality pass, VOI): an unconfessed lie postpones her proposal, exactly as it ends the knife on the table;
        // the confession or the table's scratched answer still reaches a yes, so the refusal is never final.
        var liarWalks = Program.Walk(commit, liar).ToList();
        check(Avail(commit, liar) && liarWalks.Where(r => r.Has(Committed)).All(r => r.Has(P + "confessed_price"))
              && liarWalks.Any(r => r.Has(Committed)) && liarWalks.Any(r => r.Has(P + "declined") && !r.Has(Committed) && !r.Has(Closed)),
            "Trk_Kaylessa_Lie: she hands her death to a Commander still lying to her, or the lie closes her for good.");
        var liarNo = Later(story, liarWalks.First(r => r.Has(P + "declined") && !r.Has(P + "confessed_price")), 72);
        check(Avail(table, liarNo) && Program.Walk(table, liarNo).Any(r => r.Has(Committed) && r.Has(P + "confessed_price")),
            "Trk_Kaylessa_Lie: the postponed proposal has no road back through the truth.");
        // The late page needs the dagger's disclosure (the last beat before her proposal); the clock alone is an ally's ending.
        var epAlly = pages.Single(p => p.Id == P + "epilogue.ally");
        check(Avail(pages.Single(p => p.Id == P + "epilogue.commit"), World(story, 6, "trickster", "trickster.ever", P + "clock_named", P + "knife_shown", W + "in_the_dark", P + "alive.swap_clean"))
              && !Avail(pages.Single(p => p.Id == P + "epilogue.commit"), World(story, 6, "trickster", "trickster.ever", P + "clock_named"))
              && Avail(epAlly, World(story, 6, "trickster", "trickster.ever", P + "clock_named"))
              && !Avail(epAlly, World(story, 6, "trickster", "trickster.ever", P + "clock_named", P + "knife_shown", W + "in_the_dark", P + "alive.swap_clean"))
              && Avail(epAlly, World(story, 6, "trickster", "trickster.ever", P + "clock_named", P + "knife_shown"))
              && !Avail(pages.Single(p => p.Id == P + "epilogue.commit"), World(story, 6, "trickster", "trickster.ever", P + "clock_named", P + "knife_shown")),
            "Trk_Kaylessa_Late: the war's end commits a mere acquaintance, or leaves the knife's disclosure without a late yes.");
        check(!World(story, 6, "trickster", "trickster.ever", P + "clock_named").Has(P + "late_committed"), "The clock alone makes her a household partner.");

        // Location (Sol quality pass, CAN): every visit in Drezen needs the rest taken in Drezen.
        foreach (var v in own.Where(s => Rules.IsRemote(s) && Rules.KindOf(s) == "visit"))
            check(v.Areas.SequenceEqual(new[] { Drezen }), "A Drezen visit can arrive after a rest elsewhere: " + v.Id);
        var outside = Program.Copy(alive); outside.Area = "ffffffffffffffffffffffffffffffff";
        check(!Avail(hunter, outside) && Avail(hunter, alive), "Forn's antechamber visit arrives in the wilderness.");
        // Histories the text must not invent: the living world never died; never-met is not greeted as an old meeting; the promise.
        var lastWords = S(W + "last_words");
        var wantScene = S(W + "what_i_want");
        var wantBase = World(story, 5, "trickster", "trickster.ever", Returned, "kaylessa.started", P + "alive.swap_clean", W + "in_the_dark", P + "knife_shown");
        var wantPages = new HashSet<string>();
        Program.Walk(wantScene, wantBase, (page, _) => wantPages.Add(page));
        var wantMet = Program.Copy(wantBase); wantMet.Flags.Add("kaylessa.first_words_seen");
        var metPages = new HashSet<string>();
        Program.Walk(wantScene, wantMet, (page, _) => metPages.Add(page));
        check(wantPages.Contains("start_fresh") && !wantPages.Contains("start") && !wantPages.Contains("know")
              && metPages.Contains("start") && !metPages.Contains("start_fresh"),
            "Her first words are recalled for a Commander who never heard them.");
        // Round 4 (BEL): the proposal follows one played exchange of attraction (the kiss after curfew); without it, no proposal.
        check(commit.Requires.Contains(W + "in_the_dark") && !Avail(commit, World(story, 5, "trickster", "trickster.ever", Returned, P + "knife_shown")),
            "The proposal comes before any played attraction.");
        // Round 4 (INT): Shyka gone from the Council still answers a sending, on worse terms, in Chapter 5.
        var sending = S(P + "dead.borrow_sending");
        var goneWorld = World(story, 5, "trickster", "trickster.ever", Dead, "shyka.gone");
        check(Avail(sending, goneWorld) && !Avail(borrow, goneWorld) && Rules.KindOf(sending) == "sending"
              && !Avail(sending, World(story, 5, "trickster.ever", "trickster.failed", Dead, "shyka.gone")), "Shyka's departure shuts the dead worlds.");
        // Round 6 (INT): the Council fights do not end Shyka (Shyka_Offer/Cue_0002): the sending answers after either fight too.
        foreach (var fight in new[] { "council.fought", "council.fought_nocta_allied" })
        {
            var fought = World(story, 5, "trickster", "trickster.ever", Dead, fight);
            check(Avail(sending, fought) && !Avail(borrow, fought), "A Council fight shuts the dead worlds: " + fight);
            check(Reaches(Take(sending, fought, "answer", 0, P + "primed"), Committed), "No road from the sending after " + fight);
        }
        // Round 6 (INT): her recollection of being believed follows the native warning answers.
        var hunted = Later(story, played, 12);
        var metPagesW = new HashSet<string>(); var warnedPagesW = new HashSet<string>();
        Program.Walk(warning, hunted, (page, _) => metPagesW.Add(page));
        var warnedWorld = Program.Copy(hunted); warnedWorld.Flags.Add("kaylessa.warned_camp"); Rules.Complete(story, warnedWorld);
        Program.Walk(warning, warnedWorld, (page, _) => warnedPagesW.Add(page));
        check(metPagesW.Contains("met_doubted") && !metPagesW.Contains("met") && warnedPagesW.Contains("met") && !warnedPagesW.Contains("met_doubted"),
            "She credits the Commander with a trust the native answers never gave.");
        var sent2 = Take(sending, goneWorld, "answer", 0, P + "primed", P + "cost.shyka_raised");
        check(Avail(soldier, Later(story, sent2, 12)) && Reaches(sent2, Committed), "The sending does not bring her back.");
        // Round 4 (CAN): Forn is the Winter Council's hunter, never a darkhunter.

        // Round 5 (INT): rule three reaches the late page too; an unconfessed liar gets the ally's ending, not the romance.
        var lateLiar = World(story, 6, "trickster", "trickster.ever", Dead, Returned, P + "clock_named", P + "knife_shown", W + "in_the_dark", P + "lied_about_price");
        check(!lateLiar.Has(P + "late_committed") && !Avail(pages.Single(p => p.Id == P + "epilogue.commit"), lateLiar)
              && Avail(pages.Single(p => p.Id == P + "epilogue.ally"), lateLiar) && !lateLiar.Has("kaylessa.harem.eligible"),
            "An unconfessed liar gets the late romance.");
        var lateConfessed = Program.Copy(lateLiar); lateConfessed.Flags.Add(P + "confessed_price"); Rules.Complete(story, lateConfessed);
        check(lateConfessed.Has(P + "late_committed") && Avail(pages.Single(p => p.Id == P + "epilogue.commit"), lateConfessed),
            "A confessed lie still blocks the late page.");

        // Round 5 (CAN/COX): no narration decides the Commander's night sight; Avennara's reply comes at the awning.
        foreach (var x in own.Concat(pages))
            foreach (var n in x.Nodes.Where(n => n.Speaker == "Narrator"))
        check(Rules.IsPresenceHubScene(S(N + "avennara")), "Avennara's reply is a second Chapter 5 letter.");
        var nightScene = S(N + "where_i_was_meant_to_die");
        var desireNode = nightScene.Nodes.Single(n => n.Id == "desire");
        check(desireNode.Choices.Single(c => c.Next == "like_met").Requires.Contains("kaylessa.first_words_seen")
              && desireNode.Choices.Single(c => c.Next == "like_stranger").Forbids.Contains("kaylessa.first_words_seen"),
            "The night recalls first words that a started dialogue does not prove.");
        var commitPage = pages.Single(p => p.Id == P + "epilogue.commit");
        check(commitPage.Nodes[0].Paragraphs.Single(q => q.Requires.Contains(P + "cost.dark_fate_stalled") && !q.Requires.Contains(P + "cost.beast_fed")).Forbids.Contains(P + "cost.beast_fed")
              && commitPage.Nodes[0].Paragraphs.Any(q => q.Requires.Contains(P + "cost.beast_fed")), "The late page forgets the fed beast.");
        var hunterParas = pages.Single(p => p.Id == P + "epilogue.no_lamb").Nodes[0].Paragraphs.Where(q => q.Requires.Contains(P + "cost.council_knows")).ToList();
        check(hunterParas.Count == 2 && hunterParas.Single(q => SurfaceIds.Has(SurfaceIds.Of(story, q), "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/7]")).Forbids.Contains(N + "hunter_turned_back")
              && hunterParas.Any(q => q.AnyGroups.Any(g => g.Contains(N + "hunter_turned_back") && g.Contains(N + "hunter_hers"))),
            "The page replaces the played hunter with an unplayed killing.");
        var nameScene = S(N + "once_when_it_counts");
        var namePages = new HashSet<string>();
        Program.Walk(nameScene, World(story, 5, "trickster", "trickster.ever", Committed, P + "knife_held", N + "grey_light"), (page, _) => namePages.Add(page));
        check(namePages.Contains("name_fresh") && !namePages.Contains("name"), "She keeps a promise from a conversation that never happened.");

        PolishHistories(story, check);

        // Pages: effect-free Chapter 6 pages; no exclusivity stated as fact is linted by the house rules.
        check(pages.Length == 5 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null && c.Mythic == null))),
            "The pages are not five effect-free Chapter 6 pages.");
        check(Avail(pages.Single(p => p.Id == P + "epilogue.no_lamb"), World(story, 6, "trickster", "trickster.ever", Committed))
              && !Avail(pages.Single(p => p.Id == P + "epilogue.commit"), World(story, 6, "trickster", "trickster.ever", Committed, P + "clock_named")),
            "The committed page is not the committed ending.");

        // Reactions: exactly the allocated reactors (Anevia, Woljif, Shyka), each behind its guard.
        check(reactions.All(r => r.Nodes.Count == 1) && reactions.Select(r => r.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Anevia", "Shyka", "Woljif" })
              && reactions.Where(r => r.Owner == "Anevia").All(r => r.Forbids.Contains("anevia_gone") && r.ForbidOverrides["anevia_gone"] == "anevia.trickster.returned")
              && reactions.Where(r => r.Owner == "Woljif").All(r => r.Forbids.Contains("woljif.dead") && r.Forbids.Contains("woljif.kicked_out"))
              && reactions.Where(r => r.Owner == "Shyka").All(r => Rules.IsRemote(r) && r.Forbids.Contains("shyka.gone")),
            "The reactions are not exactly Anevia, Woljif and Shyka behind their guards.");

        // Sol quality pass (CAN/INT/COX/BEL): the successor, the native outcome of the ravine, bottle survival, the morning seen.
        const string FornIsDead = "7a6f0ef4dd004418aa613693dd9d280a";
        check(story.Etudes["kaylessa.forn_dead"] == FornIsDead && story.StartableEtudes.Contains(FornIsDead),
            "E17: FornIsDead is not both read and startable.");
        // The original Forn: every ravine outcome starts FornIsDead (native Forn_Ambush/Cue_0040 would have), which removes his
        // DrezenCapital spawner (Forn_m_spawnConditions requires it not playing) and hides him (DrezenCapital_DefaultMechanic).
        var ravineEnds = swap.Nodes.SelectMany(n => n.Choices).Where(c => c.Next == null && c.Check == null && !c.Abort).ToList();
        check(ravineEnds.Where(c => c.Forbids.Contains(P + "alive.successor")).All(c => c.StartEtude == FornIsDead)
              && ravineEnds.Where(c => c.Requires.Contains(P + "alive.successor")).All(c => c.StartEtude == null)
              && ravineEnds.Count(c => c.StartEtude == FornIsDead) == 3 && ravineEnds.Count(c => c.Requires.Contains(P + "alive.successor")) == 3,
            "The ravine does not start FornIsDead for the original Forn only.");
        var origPages = new HashSet<string>();
        Program.Walk(swap, ready, (page, _) => origPages.Add(page));
        check(origPages.Contains("forn") && origPages.Contains("volley") && !origPages.Contains("forn_s") && !origPages.Contains("volley_s"),
            "The original ravine plays the successor's pages.");
        // After the ravine the native etude plays: the later scenes must still remember the original Forn, not a successor.
        var afterRavine = Program.Copy(clean); afterRavine.Flags.Add("kaylessa.forn_dead"); afterRavine.Times["kaylessa.forn_dead"] = afterRavine.Hour;
        var cleanRuled = Later(story, Take(rules, Later(story, afterRavine, 24), "rules", 0), 24);
        var clockPages = new HashSet<string>();
        Program.Walk(clock, cleanRuled, (page, _) => clockPages.Add(page));
        check(clockPages.Contains("clean") && !clockPages.Contains("clean_s"), "FornIsDead turns the original Forn into his successor afterwards.");
        // Forn died in canon: a nameless successor, named nowhere as Forn, with Forn's face nowhere on the page.
        var heirWorld = World(story, 5, "trickster", "trickster.ever", "kaylessa.met", "kaylessa.forn_dead");
        var heirPages = new HashSet<string>();
        Program.Walk(hunter, heirWorld, (page, _) => heirPages.Add(page));
        check(heirPages.Contains("second") && heirPages.Contains("ask_s") && !heirPages.Contains("named") && !heirPages.Contains("ask"),
            "The successor is introduced as Forn.");
        var heirPlayed = Take(hunter, heirWorld, "seen_s", 0, P + "primed", P + "alive.successor");
        var heirPlanned = Later(story, Take(warning, Later(story, heirPlayed, 12), "terms", 0, P + "alive.planned"), 24);
        var heirWarnPages = new HashSet<string>(); var heirSwapPages = new HashSet<string>();
        Program.Walk(warning, Later(story, heirPlayed, 12), (page, _) => heirWarnPages.Add(page));
        Program.Walk(swap, heirPlanned, (page, _) => heirSwapPages.Add(page));
        check(heirWarnPages.Contains("amulet_s") && !heirWarnPages.Contains("amulet") && heirSwapPages.Contains("forn_s")
              && heirSwapPages.Contains("volley_s") && !heirSwapPages.Contains("forn") && !heirSwapPages.Contains("volley"),
            "The successor's ambush plays Forn's pages.");
        foreach (var id in heirSwapPages.Concat(heirPages).Distinct())
        {
            var node = swap.Nodes.Concat(hunter.Nodes).First(n => n.Id == id && (heirSwapPages.Contains(id) ? swap.Nodes.Contains(n) : hunter.Nodes.Contains(n)));
            check(node.Speaker != "Forn" && node.Portrait != "Forn", "The successor speaks with Forn's name or face: " + id);
        }
        var heirClean = Take(swap, heirPlanned, "end", 1, Returned, P + "alive.swap_clean");
        check(Program.Walk(swap, heirPlanned).All(r => !r.Has(Returned) || r.Has(P + "alive.successor")), "The successor's ravine forgets whose it was.");
        var heirClock = new HashSet<string>();
        Program.Walk(clock, Later(story, Take(rules, Later(story, heirClean, 24), "rules", 0), 24), (page, _) => heirClock.Add(page));
        check(heirClock.Contains("clean_s") && !heirClock.Contains("clean"), "The clock remembers Forn going down in the successor's ravine.");
        var noLamb = pages.Single(p => p.Id == P + "epilogue.no_lamb");
        var swapPara = noLamb.Nodes[0].Paragraphs.Where(p => p.Requires.Contains(P + "alive.swap_clean")).ToList();
        check(swapPara.Count == 2 && SurfaceIds.Has(SurfaceIds.Of(story, swapPara.Single(p => p.Forbids.Contains(P + "alive.successor"))), "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/4][kaylessa.trickster.epilogue.no_lamb/page/paragraph/5]")
              && SurfaceIds.Has(SurfaceIds.Of(story, swapPara.Single(p => p.Requires.Contains(P + "alive.successor"))), "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/5]"), "The page names the wrong dead hunter.");
        // The living clock: no unprepared reversal, no promised long life; the knots continue.
        var morning = S(N + "grey_light");
        check(noLamb.Nodes[0].Paragraphs.Any(p => p.AnyGroups.Any(g => g.Contains(P + "alive.swap_clean") && g.Contains(P + "alive.swap_fumbled"))),
            "The living world's curse is reversed or outlived without a cause.");
        // Last Call: a Commander who came back from the sacrifice (bottle or not) keeps the ending; an unsurvived one does not.
        foreach (var page in pages.Where(p => p.Forbids.Contains("sacrifice")))
            check(page.ForbidOverrides["sacrifice"] == "trickster.commander_back", "A page ignores the Commander's return: " + page.Id);
        check(Avail(noLamb, World(story, 6, "trickster", "trickster.ever", Committed, "sacrifice", "ending.trickster"))
              && !Avail(noLamb, World(story, 6, "trickster", "trickster.ever", Committed, "sacrifice")), "Bottle-backed survival loses her ending.");
        // Directive 12: the morning after, seen by Woljif.
        var wMorning = S(P + "react.woljif_morning");
        check(wMorning.Owner == "Woljif" && wMorning.Requires.Contains(N + "grey_light") && !Avail(wMorning, World(story, 5, "trickster", "trickster.ever", Committed))
              && Avail(wMorning, World(story, 5, "trickster", "trickster.ever", Committed, N + "grey_light", "woljif.in_party"))
              && !Avail(wMorning, World(story, 5, "trickster", "trickster.ever", Committed, N + "grey_light"))
              && !Avail(wMorning, World(story, 5, "trickster", "trickster.ever", Committed, N + "grey_light", "woljif.in_party", "woljif.plot_absent")),
            "The morning witness ignores Woljif's recruitment or plot absence.");

        // Camellia's oath: her kill that didn't take, now that this route returns her (ledger 05 row 12).
        var oathCamp = S("camellia.trickster.kills_answered.oath_camp");
        var kWorld = World(story, 5, "trickster", "trickster.ever", Returned, "kaylessa.camellia_killed");
        kWorld.AvailableContacts.Add("397b090721c41044ea3220445300e1b8");   // Camellia's own unit: her oath is a physical scene at her camp
        var route = oathCamp.Nodes.Single(n => n.Id == "start").Choices.Where(c => Rules.Match(c.Requires, c.Forbids, kWorld)).ToList();
        check(Rules.Available(story, oathCamp, kWorld) && route.Count == 1 && route[0].Next == "kaylessa",
            "Trk_Kaylessa_CamelliaOath: Camellia's oath does not answer the Kaylessa kill that didn't take.");

        // The courtship: every beat of kaylessa_wasps and kaylessa_clearing reachable in some world, the night only after the knife.
        var courtship = own.Where(s => s.Id.StartsWith(W, StringComparison.Ordinal) || s.Id.StartsWith(N, StringComparison.Ordinal)).ToArray();
        check(courtship.Length >= 18 && courtship.All(s => s.Optional && s.Requires.Contains("trickster.ever")),
            "The courtship is missing beats, or a beat is not an optional Trickster-path scene.");
        check(courtship.Where(s => s.Id.StartsWith(N, StringComparison.Ordinal)).All(s => s.Requires.Contains(Committed)),
            "An after-the-knife beat opens before the commit.");
        var night = S(N + "where_i_was_meant_to_die");
        check(night.Nodes.Any(n => n.Id == "cut") && night.Nodes.Single(n => n.Id == "down").Choices.Single().Set.Contains(N + "night"),
            "The night does not reach its threshold and cut.");
        var worlds = new[]
        {
            World(story, 5, "trickster", "trickster.ever", Returned, Dead, "kaylessa.started", P + "cost.dark_fate_stalled", P + "cost.shyka_price", P + "cost.shyka_raised",
                  Begged, "kaylessa.tomb", "kaylessa.camellia_killed", "kaylessa.anevia_caught", "kaylessa.unmasked", "kaylessa.ember_met",
                  "iz.done", "kaylessa.anemora_told", "kaylessa.met", "kaylessa.trickster.react.shyka_note"),
            World(story, 5, "trickster", "trickster.ever", Returned, Dead, "kaylessa.started", P + "cost.dark_fate_stalled", P + "cost.shyka_price", "kaylessa.note_held",
                  "kaylessa.healed_by_force", "iz.anemora_dead", "kaylessa.trickster.react.shyka_note"),
            World(story, 5, "trickster", "trickster.ever", Returned, "kaylessa.started", "kaylessa.met", P + "alive.swap_fumbled", P + "cost.amulet_burnt",
                  P + "cost.council_knows", P + "cost.arrow_taken", "iz.done"),
            // Deep in the courtship: the spine up to the dagger and the walk in the dark already behind her.
            World(story, 5, "trickster", "trickster.ever", Returned, "kaylessa.started", P + "alive.swap_clean", P + "cost.amulet_burnt",
                  P + "after.rules", P + "clock_named", P + "after.dark_fate", P + "beast_met", P + "after.the_beast", P + "knife_shown",
                  P + "after.the_knife", W + "the_wasp", W + "soldier", W + "in_the_dark"),
        };
        foreach (var beat in courtship)
            check(worlds.Any(w => Reaches(w, beat.Id)), "Courtship beat unreachable in every test world: " + beat.Id);
        Console.WriteLine("PASS: Kaylessa Trickster (Trk_Kaylessa_*): the promise, Shyka's trade, Forn's courtesy and the amulet swap, the rules, the clock, the cells, the dagger, the hilt, the knife on the table, the pages, the oath, and "
                          + courtship.Length + " courtship beats.");
    }

    private static void PolishHistories(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Node Node(string id, string node) => S(id).Nodes.Single(n => n.Id == node);
        Choice[] Choices(string id, string node, Snapshot w) => Node(id, node).Choices
            .Where(c => Rules.Match(c.Requires, c.Forbids, w)).ToArray();
        string[] Visible(string id, Snapshot w) => Rules.VisibleParagraphs(Node(id, "page"), w).Select(p => SurfaceIds.Of(story, p)).ToArray();
        var kept = P + "epilogue.no_lamb";
        var late = P + "epilogue.commit";
        const string raised = P + "cost.shyka_raised";
        const string sending = P + "dead.borrow_sending";
        const string stalled = P + "cost.dark_fate_stalled";
        const string fed = P + "cost.beast_fed";

        // Payment history dispatches accurate speech; declining to disclose remains possible.
        foreach (var history in new[] { "direct", "amused", "raised", "sending" })
        {
            var w = World(story, 5, "trickster", "trickster.ever", Returned, Dead, Begged, stalled,
                P + "cost.shyka_price", P + "after.rules");
            if (history == "amused") w.Flags.Add(P + "shyka_amused");
            if (history == "raised" || history == "sending") w.Flags.Add(raised);
            if (history == "sending") w.Flags.Add(sending);
            string target = history == "sending" ? "shyka_sending" : history == "raised" ? "shyka_raised" : "shyka_yes";
            var choices = Choices(P + "dead.soldier", "price", w);
            check(choices.Length == 2 && choices.Any(c => c.Next == "mine") && choices.Any(c => c.Next == target),
                "Polish Kaylessa: wrong price disclosure/refusal in " + history);
            foreach (var node in new[] { "how", "better" })
            {
                var reports = Choices(W + "the_other_you", node, w);
                var expected = target == "shyka_yes" ? "shyka" : target;
                check(reports.Length == 1 && reports[0].Next == expected,
                    "Polish Kaylessa: wrong Shyka report from " + node + " in " + history);
                check(Node(W + "the_other_you", expected).Choices.Single().Next == "branch",
                    "Polish Kaylessa: price report lost the bounded memory continuation.");
            }
            var price = Visible(kept, w).Where(text => SurfaceIds.Has(text, "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/1][kaylessa.trickster.epilogue.no_lamb/page/paragraph/17]") || SurfaceIds.Has(text, "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/0]")).ToArray();
            check(price.Length == 1 && (history != "sending" || SurfaceIds.Has(price[0], "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/17]"))
                && (history != "raised" || SurfaceIds.Has(price[0], "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/1]")),
                "Polish Kaylessa: ending mixes price methods in " + history);
        }
        var unpaid = World(story, 5, "trickster", "trickster.ever", Dead, "shyka.gone");
        foreach (var outcome in Program.Walk(S(sending), unpaid))
            check(outcome.Has(P + "primed") == outcome.Has(sending), "Polish Kaylessa: unpaid sending acquired paid history.");
        check(Node(P + "react.woljif_haggled", "start").Choices.Count == 1,
            "Polish Kaylessa: Woljif invents a negotiation or gained a dispatcher.");

        // Neither hunter identity nor arrow allocation turns a failed swap into a clean kill.
        foreach (var outcome in new[] { "swap_clean", "swap_fumbled" })
        foreach (var successor in new[] { false, true })
        foreach (var shield in new[] { false, true })
        {
            var w = World(story, 5, "trickster", "trickster.ever", Returned, P + "cost.amulet_burnt", P + "alive." + outcome);
            if (successor) w.Flags.Add(P + "alive.successor");
            if (outcome == "swap_fumbled") w.Flags.Add(P + (shield ? "cost.arrow_taken" : "cost.her_collarbone"));
            var choices = Choices(W + "last_words", "start", w);
            string target = outcome == "swap_clean" ? "alive" : "alive_fumbled";
            check(choices.Length == 1 && choices[0].Next == target, "Polish Kaylessa: wrong swap recollection.");
            var memory = Node(W + "last_words", target);
            check(memory.Choices.Select(c => c.Next).SequenceEqual(new[] { "alive_write", "alive_say" }),
                "Polish Kaylessa: successor named Forn or writing answers lost.");
            check(!Visible(kept, w).Any(text => SurfaceIds.Has(text, "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/1][kaylessa.trickster.epilogue.no_lamb/page/paragraph/17]")), "Polish Kaylessa: living swap acquired a Shyka price.");
        }

        // Curse consequences and the single dagger retain each earned history.
        foreach (var device in new[] { stalled, P + "alive.swap_clean", P + "alive.swap_fumbled" })
        foreach (var fedBeast in new[] { false, true })
        foreach (var holder in new[] { P + "knife_held", P + "knife_handed_back" })
        {
            var w = World(story, 6, "trickster", "trickster.ever", Returned, Committed, device, holder);
            if (fedBeast) w.Flags.Add(fed);
            foreach (var id in new[] { kept, late })
            {
                var text = Visible(id, w);
                var consequences = text.Where(t => SurfaceIds.Has(t, "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/3][kaylessa.trickster.epilogue.no_lamb/page/paragraph/18][kaylessa.trickster.epilogue.commit/page/paragraph/1][kaylessa.trickster.epilogue.commit/page/paragraph/5]")).ToArray();
                check(consequences.Length == (fedBeast ? 1 : 0), "Polish Kaylessa: fed consequence missing/doubled in " + id);
                if (fedBeast)
                    check(SurfaceIds.Has(consequences[0], "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/3][kaylessa.trickster.epilogue.commit/page/paragraph/1]") == (device == stalled), "Polish Kaylessa: living curse acquired stasis.");
            }
            var knife = Visible(kept, w).Where(t => SurfaceIds.Has(t, "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/12][kaylessa.trickster.epilogue.no_lamb/page/paragraph/13]")).ToArray();
            check(knife.Length == 1 && SurfaceIds.Has(knife[0], holder.EndsWith("knife_held") ? "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/12]" : "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/13]"),
                "Polish Kaylessa: ending moved or duplicated the chosen dagger.");
        }

        // A kiss without the knife disclosure stays an ally; unresolved truth with the knife never acquires a free yes.
        foreach (var kissed in new[] { false, true })
        foreach (var truth in new[] { "honest", "lied", "confessed" })
        {
            var w = World(story, 6, "trickster", "trickster.ever", Returned, P + "clock_named", stalled);
            if (kissed) w.Flags.Add(W + "in_the_dark");
            if (truth != "honest") w.Flags.Add(P + "lied_about_price");
            if (truth == "confessed") w.Flags.Add(P + "confessed_price");
            if (truth == "honest") w.Flags.Add(P + "told_borrowed");
            foreach (var knifeShown in truth == "lied" ? new[] { false, true } : new[] { false })
            {
                var ally = Program.Copy(w);
                if (knifeShown) ally.Flags.Add(P + "knife_shown");
                Rules.Complete(story, ally);
                check(Rules.Available(story, S(P + "epilogue.ally"), ally) && !Rules.Available(story, S(late), ally),
                    "Polish Kaylessa: kiss-only or unresolved truth acquired late commitment.");
                var history = Visible(P + "epilogue.ally", ally);
                check(history.Length == 1 && !SurfaceIds.Has(history[0], "[kaylessa.trickster.epilogue.ally/page/paragraph/3]") == kissed,
                    "Polish Kaylessa: ally denied a played kiss or invented a proposal.");
                if (kissed && truth == "lied") check(SurfaceIds.Has(history[0], "[kaylessa.trickster.epilogue.no_lamb/page/paragraph/6][kaylessa.trickster.epilogue.ally/page/paragraph/0]"), "Polish Kaylessa: ally forgave unresolved price.");
                if (kissed && truth == "confessed") check(SurfaceIds.Has(history[0], "[kaylessa.trickster.epilogue.ally/page/paragraph/2]"), "Polish Kaylessa: ally lost confession.");
            }
        }
        Console.WriteLine("PASS: Kaylessa polish histories (price, sending abort, swaps, curse, knife and ally).");
    }
}
