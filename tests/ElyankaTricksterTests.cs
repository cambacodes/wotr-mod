using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Elyanka Camilary, Trickster (Writer/handoffs/trickster/elyanka-camilary.md; binding plan 11-ROSTER-PLAN-2 §2, Elyanka block
// and build sheet, R5): "Mourner at your own wake". One block per rules test (Trk_Elyanka_*): the funeral door and its
// delay, the executor's Bluff (and its twin), the bare-faced sale, the Iz dead (the evil pivot), the exchange of claims and
// her move, the hearse and its morning, the courtship beats, the reactors, the pages for every ending of the debt, Last
// Call's coda and creditor, and the household's eligibility.
internal static class ElyankaTricksterTests
{
    private const string P = "elyanka.trickster.";
    private const string Committed = "elyanka.committed";
    private const string Closed = "elyanka.closed";
    private const string Started = "elyanka.started";
    private const string Latch = P + "funeral.latched";
    private const string Owned = P + "owned";
    private const string Bequeathed = P + "cost.corpse_bequeathed";
    private const string Tested = P + "tested";
    private const string Declined = P + "declined";
    private const string LeftFree = P + "left_free";
    private const string Bier = P + "bier_seen";
    private const string Active = "lastcall.active";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = "2570015799edf594daf2f076f2f975d8" };
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

        var rel = story.Relationships["elyanka"];
        var mine = story.Scenes.Where(s => s.Relationship == "elyanka").ToArray();
        var own = mine.Where(s => !s.Reaction && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var pages = mine.Where(s => s.Owner == "ElyankaEpilogue").ToArray();
        var reactions = mine.Where(s => s.Reaction).ToArray();
        var door = S(P + "door.hearse");
        var haggle = S(P + "executor.haggle");
        var straight = S(P + "straight.offer");
        var dead = S(P + "test.the_dead");
        var claims = S(P + "commit.claims");
        var move = S(P + "commit.her_move");
        var hearse = S(P + "visit.hearse");

        // Trk_Elyanka_Bindings: the relationship and the funeral reads; no Lich key, no presence, no crowded hub.
        check(rel.StartedFlag == Started && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.SequenceEqual(new[] { P + "left_free" }),
            "Elyanka's relationship does not match the plan (no fate to defy: no UnavailableFlags).");
        check(story.SeenCues["elyanka.funeral.king"].SequenceEqual(new[] { "d1c14400d70bf0d4b947283f16f65009" })
              && story.SeenCues["elyanka.funeral.partisans_a"].SequenceEqual(new[] { "59ac2148b08ee7a47912253362ab0b27" })
              && story.SeenCues["elyanka.funeral.partisans_b"].SequenceEqual(new[] { "04923e59ebb21f943b7a2a330a6a8820" })
              && story.SeenCues["elyanka.funeral.fye"].SequenceEqual(new[] { "c76a1e617bcba114c9c726ba2363c98f" })
              && story.Latches[Latch].OrderBy(k => k).SequenceEqual(new[] { "elyanka.funeral.fye", "elyanka.funeral.king", "elyanka.funeral.partisans_a", "elyanka.funeral.partisans_b", "iz.done" })
              && story.CompletedQuests["iz.done"] == "95ff7d975689fcf44b085d10907e711d",
            "Trk_Elyanka_Bindings: the funeral is not read from its four canon tellings with the Iz fallback.");
        check(!mine.Any(s => s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g))
                  .Concat(s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids)))
                  .Any(f => f.IndexOf("lich", StringComparison.OrdinalIgnoreCase) >= 0)),
            "Trk_Elyanka_Door: an Elyanka scene reads a Lich key (the funeral is her only door).");
        check(!story.Presences.Keys.Any(k => k.StartsWith("elyanka", StringComparison.Ordinal))
              && own.All(s => s.Remote && s.AnswerLists.Length == 0) && own.All(s => s.Kind != null),
            "Elyanka has a presence or an inline entry (every beat is a rest-delivered visit), or a page has no kind.");
        check(mine.All(s => !s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g))
                  .Any(f => f.EndsWith(".started") || f.EndsWith(".closed") || f.EndsWith(".committed")) || s.Requires.Concat(s.Forbids)
                  .Concat(s.RequiresAnyGroups.SelectMany(g => g)).Where(f => f.EndsWith(".started") || f.EndsWith(".closed") || f.EndsWith(".committed"))
                  .All(f => f.StartsWith("elyanka.", StringComparison.Ordinal))),
            "Coexistence: an Elyanka scene gates on another relationship's lifecycle flag.");
        check(!mine.Any(s => s.Nodes.Any(n => n.Choices.Any(c => c.Set.Any(f => f.StartsWith("trickster.wmt.use.", StringComparison.Ordinal))))),
            "Elyanka's route spends a Word Made True (the device is a con).");
        check(mine.All(s => s.Requires.Contains("trickster") || s.Requires.Contains("trickster.ever")),
            "Path fit (v1): an Elyanka scene is not Trickster-gated (every scene is T).");

        // Runtime Complete expands transitive derived inputs; a suffix-only scan cannot establish independence.
        foreach (var funeral in new[] { "king", "partisans_a", "partisans_b", "fye" })
        {
            var lostWitnesses = World(story, 5, "trickster", "trickster.ever", "iz.done",
                "elyanka.funeral." + funeral, "anevia_gone", "irabeth_dead");
            check(Avail(door, lostWitnesses), "Trk_Elyanka_Coexistence: historical funeral " + funeral + " needs live witnesses.");
        }
        foreach (var seelah in new[] { new string[0], new[] { "seelah.in_party" }, new[] { "seelah_dead" } })
        {
            var independentTest = World(story, 5, new[] { "trickster.ever", Owned, "iomedae.closed" }.Concat(seelah).ToArray());
            check(Avail(dead, independentTest), "Trk_Elyanka_Coexistence: the corpse test needs Iomedae's romance open.");
        }

        // Trk_Elyanka_Door: 72 hours after the first funeral telling (latched), after Iz, on the live Trickster path.
        var heard = World(story, 5, "trickster", "trickster.ever", "elyanka.funeral.partisans_a", "iz.done");
        foreach (var native in new[] { "trickster", "trickster.ever", "elyanka.funeral.partisans_a", "iz.done", "chapter_later", "elyanka.present_now" }) heard.Times.Remove(native);
        heard.Times[Latch] = 4000;
        check(heard.Has(Latch) && !Avail(door, Later(heard, -929)) && Avail(door, Later(heard, -928)) && door.DelayHours == 72
              && door.Chapters.SequenceEqual(new[] { 5 }) && door.MaxChapter == 5,
            "Trk_Elyanka_Door: the hearse does not arrive exactly 72 hours after the funeral is latched (Chapter 5 only).");
        check(!Avail(door, World(story, 5, "trickster", "trickster.ever")) && !Avail(door, World(story, 5, "trickster", "trickster.ever", "elyanka.funeral.partisans_a"))
              && Avail(door, World(story, 5, "trickster", "trickster.ever", "iz.done"))
              && !Avail(door, World(story, 5, "trickster.ever", "trickster.failed", "iz.done", "elyanka.funeral.king"))
              && !Avail(door, World(story, 6, "trickster", "trickster.ever", "iz.done")),
            "Trk_Elyanka_Door: the door opens without the funeral, before Iz, off the live path, or after Chapter 5.");
        var tower = Take(door, World(story, 5, "trickster", "trickster.ever", "iz.done", "fool_king.crowned"), "tower", 0, P + "executor", P + "mourners");
        check(tower.Has(P + "executor") && tower.Has(P + "door_seen") && Ch(door, "choice", 1).Mythic == "PlayerIsTrickster"
              && Ch(door, "mourners", 0).Crusade?.Resource == "Finances" && Ch(door, "mourners", 0).Crusade?.Amount == -50
              && Ch(door, "plan", 0).Requires.Contains("fool_king.available"),
            "Trk_Elyanka_Door: the executor's plan (with the King's paid mourners where he reigns) is not reachable.");
        var escorted = Take(door, World(story, 5, "trickster", "trickster.ever", "iz.done"), "choice", 3, Closed);
        check(escorted.Has(Closed) && !escorted.Has(Started), "Trk_Elyanka_Door: the escort is not the Commander's own no.");

        // Trk_Elyanka_Executor: CheckBluff DC 26 (22 with the mourners); success names her purpose; failure sells bare-faced.
        var twins = haggle.Nodes.Single(n => n.Id == "why").Choices.Where(c => c.Check != null).ToList();
        check(twins.Count == 2 && twins.All(c => c.Check!.Skill == "CheckBluff" && c.Check.CommanderOnly && c.Check.Success == "named" && c.Check.Failure == "pulse")
              && twins[0].Check!.DC == 22 && twins[0].Requires.Contains(P + "mourners") && twins[1].Check!.DC == 26 && twins[1].Forbids.Contains(P + "mourners"),
            "Trk_Elyanka_Executor: the executor's lie is not CheckBluff DC 26 (22 with the King's court weeping).");
        var ex = World(story, 5, "trickster.ever", P + "executor");
        var sold = Take(haggle, ex, "sold", 0, Owned);
        check(sold.Has(Owned) && sold.Has(Bequeathed) && sold.Has(Started) && sold.Has(P + "bluffed") && !sold.Has(P + "exposed")
              && Ch(haggle, "sold", 0).Alignment?.Direction == "Evil" && Ch(haggle, "sold", 0).Alignment?.Value == 1,
            "Trk_Elyanka_Executor: the con's sale does not set owned + the bequest (Evil 1).");
        var bare = Take(haggle, ex, "bare_sold", 0, Owned);
        check(bare.Has(P + "exposed") && bare.Has(Bequeathed) && !bare.Has(P + "bluffed"),
            "Trk_Elyanka_Executor: a failed Bluff does not sell bare-faced with exposed.");
        check(Take(haggle, ex, "seen_out", 0, Closed).Has(Closed) && Take(haggle, ex, "refuse", 0, Closed).Has(Closed)
              && Take(haggle, ex, "refuse_veiled", 0, Closed).Has(Closed),
            "Trk_Elyanka_Executor: the Commander's refusals do not close the route.");
        var fresh = World(story, 5, "trickster.ever", P + "executor");
        fresh.Times[P + "executor"] = fresh.Hour - 23;
        check(!Avail(haggle, fresh) && haggle.DelayHours == 24, "Trk_Elyanka_Executor: the wake plays before a day has passed.");

        // Trk_Elyanka_Straight: the corpse comes to supper.
        var st = World(story, 5, "trickster.ever", P + "straight");
        check(Take(straight, st, "sold", 0, Owned).Has(Bequeathed) && Take(straight, st, "refuse", 0, Closed).Has(Closed)
              && Ch(straight, "sold", 0).Alignment?.Direction == "Evil",
            "Trk_Elyanka_Straight: the bare-faced sale or its refusal is missing.");

        // Trk_Elyanka_TheDead: the evil pivot. Every answer passes to the claims; the gift is Evil 2 and a Ledger secret.
        var ow = World(story, 5, "trickster.ever", Owned, Bequeathed, Started);
        var gave = Take(dead, ow, "give", 0, Tested);
        var carrion = Take(dead, ow, "carrion", 0, Tested);
        var kept = Take(dead, ow, "refuse", 0, Tested);
        check(gave.Has(P + "gave_dead") && gave.Has("trickster.secret.elyanka_siege_dead") && Ch(dead, "ask", 0).Alignment?.Value == 2
              && carrion.Has(P + "gave_carrion") && kept.Has(P + "refused_dead") && !kept.Has("trickster.secret.elyanka_siege_dead")
              && new[] { gave, carrion, kept }.All(r => !r.Has(Closed)),
            "Trk_Elyanka_TheDead: the pivot does not branch (give Evil 2 + secret / carrion / refuse), or it closes the route.");
        check(dead.DelayHours == 48, "Trk_Elyanka_TheDead: the test does not wait two days after the sale.");

        // Trk_Elyanka_Claims: the exchange of claims (her proposal), the soft no, her move 48 hours later with no price.
        // eng7-l13: positive claims and second-offer commitments use current power.
        var t = World(story, 5, "trickster", "trickster.ever", Owned, Bequeathed, Started, Tested, P + "gave_carrion", P + "beat.whisper");
        var yes = Take(claims, t, "rites", 0, Committed);
        check(yes.Has(Committed) && yes.Has("trickster.secret.elyanka_rites") && Take(claims, t, "yes_kiss", 0, Committed).Has(Committed),
            "Trk_Elyanka_Claims: taking her claim does not commit (with her rites kept secret).");
        var no = Take(claims, t, "buyer", 0, Declined);
        check(no.Has(Declined) && !no.Has(Committed) && !no.Has(Closed), "Trk_Elyanka_Claims: the buyer's question is not her soft no.");
        var nw = World(story, 5, "trickster", "trickster.ever", Owned, Bequeathed, Started, Tested, Declined);
        check(move.DelayHours == 48 && Take(move, nw, "take_rites", 0, Committed).Has(P + "lock_taken")
              && Take(move, nw, "home", 0, LeftFree).Has(Closed)
              && move.Nodes.SelectMany(n => n.Choices).All(c => c.Crusade == null && c.Alignment == null),
            "Trk_Elyanka_HerMove: her move is not 48 hours later, priceless, with the lock of hair or her dismissal (left_free closes).");
        check(!Avail(move, World(story, 5, "trickster.ever", Owned, Tested, Declined, Committed)) && !Avail(claims, nw),
            "Trk_Elyanka_HerMove: a settled claim is asked again.");

        // Trk_Elyanka_Hearse: the intimacy, the cut and the morning; the horses startle at the carriage door.
        var c5 = World(story, 5, "trickster.ever", Owned, Tested, Committed, Started);
        check(Avail(hearse, c5) && Take(hearse, c5, "last_night", 0, Bier).Has(Bier)
              && Take(hearse, World(story, 5, "trickster.ever", Owned, Tested, Committed, Started, "daeran.dead"), "horses2", 0, Bier).Has(P + "horses_balked"),
            "Trk_Elyanka_Hearse: the night in the hearse (cut at the first motion) or its horse variant is missing.");

        // Trk_Elyanka_Reactions: Daeran (twice), Seelah and Regill (twice), each guarded against death or departure.
        var after = S(P + "react.daeran_after");
        check(after.AnswerLists.SequenceEqual(new[] { "4d978cbd2aa780d46874255282039f3f" }) && after.Forbids.Contains("daeran.dead") && after.Forbids.Contains("daeran.kicked_out")
              && after.Nodes[0].Choices[0].Set.Contains(P + "daeran_ally") && Avail(after, World(story, 5, "trickster.ever", Bier))
              && !Avail(after, World(story, 5, "trickster.ever", Bier, "daeran.dead")),
            "Trk_Elyanka_Reactions: Daeran's hearse reaction is not on his hub, guarded, and setting daeran_ally.");
        check(reactions.All(r => r.Forbids.Any(f => f.EndsWith(".dead") || f.EndsWith("_dead"))) && reactions.Length == 5,
            "Trk_Elyanka_Reactions: a reactor is not guarded against death, or a reactor is missing.");
        check(S(P + "react.seelah_rows").Requires.Contains("seelah.in_party") && S(P + "react.regill_writ").RequiresAnyGroups.Length == 1
              && S(P + "react.regill_writ").RequiresAnyGroups[0].Length == 2 && S(P + "react.regill_lie").Requires.Contains(P + "writ.lied"),
            "Trk_Elyanka_Reactions: Seelah's or Regill's reaction reads the wrong state (any-of must be one group).");

        // Trk_Elyanka_Beats: the courtship spreads over Chapter 5 (and one Chapter 6 visit), optional, after the sale.
        var beats = own.Where(s => s.Id.StartsWith(P + "beat.", StringComparison.Ordinal)).ToArray();
        var ch6 = S(P + "ch6.collateral");
        var finalCamp = World(story, 6, "trickster.ever", Owned);
        finalCamp.Area = "10c4b0e2af186ba46ab4d238d00a40a8";
        var insideThreshold = Program.Copy(finalCamp);
        insideThreshold.Area = "22c6a99913fe5bb46b2e6011aaf93368";
        check(!Avail(ch6, insideThreshold), "Trk_Elyanka_Camp: collateral delivery escaped ThresholdOutdoor.");
        check(beats.Length >= 18 && beats.Where(b => b.Id != P + "beat.whisper").All(b => b.Optional && b.Remote && b.Requires.Contains(Bier) || b.Requires.Contains(P + "daeran_ally"))
              && !S(P + "beat.whisper").Optional && S(P + "beat.whisper").Requires.Contains(Tested) && claims.Requires.Contains(P + "beat.whisper")
              && ch6.Chapters.SequenceEqual(new[] { 6 }) && Avail(ch6, finalCamp),
            "Trk_Elyanka_Beats: a courtship beat is not optional, not after the sale, or the Chapter 6 visit is missing.");
        check(Avail(S(P + "beat.king_bill"), World(story, 5, "trickster.ever", Owned, Bier, P + "mourners", "fool_king.crowned"))
              && !Avail(S(P + "beat.king_bill"), World(story, 5, "trickster.ever", Owned, Bier)),
            "Trk_Elyanka_Beats: the King's bill plays without his weeping court.");

        // Trk_Elyanka_Pages: a page for every ending of the debt.
        Scene Pg(string id) => S(P + "epilogue." + id);
        var lived = World(story, 6, "trickster.ever", Owned, Bequeathed, Started, Tested, Committed, Bier);
        var eaten = World(story, 6, "trickster.ever", Owned, Bequeathed, Started, Tested, Committed, "sacrifice");
        var debtOnly = World(story, 6, "trickster.ever", Owned, Bequeathed, Started, Tested);
        var freed = World(story, 6, "trickster.ever", Owned, Bequeathed, Started, Tested, Declined, LeftFree, Closed);
        check(Avail(Pg("claim"), lived) && !Avail(Pg("eaten"), lived) && !Avail(Pg("debt"), lived)
              && Avail(Pg("eaten"), eaten) && !Avail(Pg("claim"), eaten)
              && Avail(Pg("debt"), debtOnly) && !Avail(Pg("claim"), debtOnly)
              && Avail(Pg("left_free"), freed) && !Avail(Pg("claim"), freed) && !Avail(Pg("lock"), freed)
              && Avail(Pg("lock"), World(story, 6, "trickster.ever", Owned, Tested, Declined)),
            "Trk_Elyanka_Pages: a page shows in the wrong world (claim / eaten / debt / left_free / lock).");
        check(Avail(Pg("claim"), World(story, 6, "trickster.ever", Owned, Committed, "sacrifice", "ending.trickster", "trickster.commander_back"))
              && pages.All(pg => pg.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0))),
            "Trk_Elyanka_Pages: the claim page does not wait for a Commander who came back, or a page has effects.");
        var unpaid = Pg("claim").Nodes[0].Paragraphs.Where(pp => SurfaceIds.Has(SurfaceIds.Of(story, pp), "[elyanka.trickster.epilogue.claim/page/paragraph/26][elyanka.trickster.epilogue.claim/page/paragraph/27]")).ToList();
        check(unpaid.Count == 2 && unpaid.All(pp => pp.Forbids.Contains(Active)),
            "Trk_Elyanka_LastCall: without the bottle the claim does not stand unpaid on her page.");

        // Trk_Elyanka_Continuity: the rendered ending of a dismissal carries no later visit or shared journey; the whisper only
        // remembers a wake the Commander actually attended; the Drezen encounters end with Chapter 5.
        bool Shows(Paragraph pp, Snapshot w) => pp.Requires.All(w.Has) && !pp.Forbids.Any(w.Has) && pp.AnyGroups.All(g => g.Any(w.Has));
        var parted = World(story, 6, "trickster.ever", Owned, Bequeathed, Started, Tested, Declined, LeftFree, Closed, P + "grave.stone_kept",
            P + "ustalav.promised", P + "night.woke", P + "daeran_ally", P + "bluffed");
        var partedText = string.Join(" ", Pg("left_free").Nodes[0].Paragraphs.Where(pp => Shows(pp, parted)).Select(pp => SurfaceIds.Of(story, pp)));
        check(Avail(Pg("left_free"), parted) && partedText.Length > 0,
            "Trk_Elyanka_Continuity: the dismissal page renders a later visit or a shared journey.");
        var whisper = S(P + "beat.whisper");
        check(Ch(whisper, "again", 1).Requires.Contains(P + "bluffed") && Ch(whisper, "again", 2).Requires.Contains(P + "exposed")
              && Ch(whisper, "again", 3).Requires.Contains(P + "straight")
              && Paths(whisper, World(story, 5, "trickster.ever", Owned, P + "straight")).All(o => !o.path.Contains(("again", 1)))
              && Paths(whisper, World(story, 5, "trickster.ever", Owned, P + "bluffed")).Any(o => o.path.Contains(("again", 1))),
            "Trk_Elyanka_Continuity: the whisper remembers a veiled wake in a world that never had one.");
        var late6 = World(story, 6, "trickster.ever", Owned, Tested, Committed, Started, Declined);
        check(new[] { dead, claims, move, hearse, S(P + "beat.night") }.All(x => x.MaxChapter == 5 && !Avail(x, late6)),
            "Trk_Elyanka_Continuity: a Drezen encounter plays in Chapter 6.");

        // Sequential walks (audit r2): commit, then straight into Chapter 6 without the hearse night: the collateral visit never
        // recalls a measuring; dismissal, then the creditor called: the Collectors paragraph does not bring her back in person;
        // the dead given without Seelah at the rows: no Seelah in the ending.
        var yesFirst = Take(claims, t, "rites", 0, Committed);
        var marched = Program.Copy(yesFirst);
        marched.Chapter = 6;
        marched.Area = "10c4b0e2af186ba46ab4d238d00a40a8";
        marched.Hour += 30;
        Rules.Complete(story, marched);
        var coll = S(P + "ch6.collateral");
        check(!Avail(hearse, marched) && Avail(coll, marched) && Paths(coll, marched).All(o => !o.path.Contains(("start", 0)))
              && Paths(coll, marched).Any(o => o.path.Contains(("start", 1))),
            "Trk_Elyanka_Continuity: committed and marched before the hearse, the Chapter 6 visit still recalls the measuring.");
        var sentHome = Take(move, nw, "home", 0, LeftFree);
        var collectors = story.Scenes.Single(s => s.Id == "trickster.lastcall.page.collectors").Nodes[0].Paragraphs
            .Where(pp => pp.Requires.Contains("lastcall.debt.whispering_way") && !pp.Requires.Contains("iomedae.appointment_kept")).ToList();   // the Appointment variant is Iomedae's (ledger row 6)
        check(sentHome.Has(Closed) && collectors.Count == 3 && collectors.All(pp => pp.AnyGroups.Length == 1 && pp.AnyGroups[0].Contains("elyanka.lastcall.called") && !pp.Requires.Contains("elyanka.present_now")),
            "Trk_Elyanka_Continuity: after a dismissal the creditor's collection reverses it (she presents the claim in person).");
        var noSeelah = Take(dead, ow, "give", 0, Tested);
        var withSeelah = Take(dead, World(story, 5, "trickster.ever", Owned, Bequeathed, Started, "seelah.in_party"), "give", 0, Tested);
        var seelahPara = Pg("claim").Nodes[0].Paragraphs.Single(pp => SurfaceIds.Has(SurfaceIds.Of(story, pp), "[elyanka.trickster.epilogue.claim/page/paragraph/5]"));
        check(!noSeelah.Has(P + "seelah_prayed") && withSeelah.Has(P + "seelah_prayed") && seelahPara.Requires.Contains(P + "seelah_prayed")
              && Pg("claim").Nodes[0].Paragraphs.Where(pp => SurfaceIds.Has(SurfaceIds.Of(story, pp), "[elyanka.trickster.epilogue.claim/page/paragraph/5][elyanka.trickster.epilogue.claim/page/paragraph/16][elyanka.trickster.epilogue.claim/page/paragraph/17][elyanka.trickster.epilogue.claim/page/paragraph/18]")).All(pp => pp.Requires.Contains(P + "seelah_prayed") || pp.Requires.Any(f => f.StartsWith(P + "inquiry.", StringComparison.Ordinal)))
              && S(P + "react.seelah_rows").Requires.Contains(P + "seelah_prayed") && S(P + "beat.inquiry").Requires.Contains(P + "react.seelah_rows"),
            "Trk_Elyanka_Continuity: the ending names Seelah at rows she never saw.");
        var cord = story.Scenes.Single(s => s.Id == "elyanka.lastcall.page").Nodes[0];
        check(cord.Paragraphs.Where(pp => SurfaceIds.Has(SurfaceIds.Of(story, pp), "[elyanka.lastcall.page/page/paragraph/7]")).All(pp => pp.Requires.Contains(Bier)),
            "Trk_Elyanka_Continuity: the coda's measuring cord does not wait for the hearse night.");

        // Trk_Elyanka_Spine (audit r3): the required chain walked in order with advancing time, from the door to the hearse,
        // at rests in Drezen; nothing of it plays at a rest elsewhere.
        var spine = World(story, 5, "trickster", "trickster.ever", "iz.done");
        foreach (var native in new[] { "trickster", "trickster.ever", "iz.done", "chapter_later" }) spine.Times.Remove(native);
        spine.Times[Latch] = spine.Hour - 72;
        var s1 = Take(door, spine, "plan", 1, P + "executor");
        check(!Avail(haggle, Later(s1, 23)), "Trk_Elyanka_Spine: the wake does not wait a day after the door.");
        var s2 = Take(haggle, Later(s1, 24), "sold", 0, Owned);
        check(!Avail(dead, Later(s2, 47)), "Trk_Elyanka_Spine: the dead do not wait two days after the sale.");
        var s3 = Take(dead, Later(s2, 48), "refuse", 0, Tested);
        var s3w = Take(S(P + "beat.whisper"), Later(s3, 24), "hers", 0, P + "beat.whisper");
        check(!Avail(claims, Later(s3w, 23)), "Trk_Elyanka_Spine: the claims do not wait a day after the whisper.");
        var s4 = Take(claims, Later(s3w, 24), "rites", 0, Committed);
        var s5 = Take(hearse, Later(s4, 24), "last_night", 0, Bier);
        var abroad = Later(s4, 24);
        abroad.Area = "00000000000000000000000000000000";
        check(s5.Has(Bier) && !Avail(hearse, abroad) && hearse.Areas.SequenceEqual(new[] { "2570015799edf594daf2f076f2f975d8" })
              && own.Where(x => x.Id != P + "beat.courier" && x.Id != P + "ch6.collateral").All(x => x.Areas.SequenceEqual(new[] { "2570015799edf594daf2f076f2f975d8" }))
              && S(P + "beat.courier").Areas.Length == 0 && S(P + "ch6.collateral").Areas.SequenceEqual(new[] { "10c4b0e2af186ba46ab4d238d00a40a8" }),
            "Trk_Elyanka_Spine: the chain does not run in order, or a Drezen encounter plays at a rest outside Drezen.");

        // Rendered endings (audit r3): exactly one unpaid line per surviving ending; the claim page never promises collection
        // where the bottle cheats it; the coda places her in one spot; the Ledger names no witness who was not there.
        string Render(Scene page, Snapshot w) => string.Join(" ", page.Nodes[0].Paragraphs.Where(pp => Shows(pp, w)).Select(pp => SurfaceIds.Of(story, pp)));
        var codaScene = story.Scenes.Single(x => x.Id == "elyanka.lastcall.page");
        var ordinary = World(story, 6, "trickster.ever", Owned, Committed, Bier);
        var returned = World(story, 6, "trickster.ever", Owned, Committed, Bier, "sacrifice", "ending.trickster", "trickster.commander_back");
        var h1 = World(story, 6, "trickster.ever", Owned, Committed, Bier, "trickster.lastcall.taken", "ending.trickster", "trickster.lastcall.pillar.bottle");
        var h2 = World(story, 6, "trickster.ever", Owned, Committed, Bier, "trickster.lastcall.taken", "ending.wound_closed", "sacrifice",
            "trickster.lastcall.pillar.bottle", "elyanka.lastcall.called", P + "collateral.in_drezen");
        int Unpaid(Snapshot w) => Pg("claim").Nodes[0].Paragraphs.Count(pp => SurfaceIds.Has(SurfaceIds.Of(story, pp), "[elyanka.trickster.epilogue.claim/page/paragraph/26][elyanka.trickster.epilogue.claim/page/paragraph/27]") && Shows(pp, w));
        check(Unpaid(ordinary) == 1 && Unpaid(returned) == 1 && Unpaid(h1) == 0 && h1.Has(Active) && h2.Has(Active),
            "Trk_Elyanka_Rendered: a surviving ending renders no unpaid line, or two.");
        check(SurfaceIds.Has(Render(Pg("claim"), ordinary), "[elyanka.trickster.epilogue.claim/page/paragraph/0]") && !SurfaceIds.Has(Render(Pg("claim"), h1), "[elyanka.trickster.epilogue.claim/page/paragraph/0]")
              && SurfaceIds.Has(Render(Pg("claim"), h1), "[elyanka.trickster.epilogue.claim/page/paragraph/1]") && SurfaceIds.Has(Render(codaScene, h1), "[elyanka.lastcall.page/page/paragraph/5]"),
            "Trk_Elyanka_Rendered: the claim page promises a collection the bottle has cheated.");
        var codaH2 = Render(codaScene, h2);
        check(SurfaceIds.Has(codaH2, "[elyanka.lastcall.page/page/paragraph/3]") && !SurfaceIds.Has(codaH2, "[elyanka.lastcall.page/page/paragraph/2]") && SurfaceIds.Has(codaH2, "[elyanka.lastcall.page/page/paragraph/4]"),
            "Trk_Elyanka_Rendered: the coda places her at the rift and in Drezen on the same night.");
        var secretDead = story.Books["trickster.ledger"].Entries.Single(x => x.Id == "secret.elyanka_siege_dead");
        check(secretDead.Requires.SequenceEqual(new[] { "trickster.secret.elyanka_siege_dead" }),
            "Trk_Elyanka_Rendered: the Ledger's secret names a witness at the rows who may never have been there.");

        // Trk_Elyanka_Recall (audit r4): no scene or ending recalls an event the world never had. Every node reachable in each
        // history (bare-faced / veiled / caught; with or without the hearse night and the hunt; kept, stationed, dismissed) is
        // read against the facts it could remember.
        IEnumerable<string> Reachable(Scene scene, Snapshot initial)
        {
            var seen = new HashSet<string>();
            var stack = new Stack<(string, Snapshot)>();
            stack.Push((scene.Nodes[0].Id, initial));
            while (stack.Count > 0)
            {
                var (id, st) = stack.Pop();
                if (!seen.Add(id)) continue;
                foreach (var choice in scene.Nodes.Single(nn => nn.Id == id).Choices.Where(ch => Rules.Match(ch.Requires, ch.Forbids, st)))
                {
                    var next = Program.Copy(st);
                    foreach (var f in choice.Set) next.Flags.Add(f);
                    foreach (var target in Rules.NextNodes(choice)) stack.Push((target, next));
                }
            }
            return seen.Select(id => SurfaceIds.Of(story, scene.Nodes.Single(nn => nn.Id == id)));
        }
        foreach (var where in new[] { new string[0], new[] { P + "collateral.at_rift" }, new[] { P + "collateral.in_drezen" }, new[] { Declined, LeftFree, Closed } })
        {
            var gone = World(story, 6, new[] { "trickster.ever", Owned, Bequeathed, Started, Tested, "sacrifice", P + "straight" }.Concat(where).ToArray());
            int places = Pg("eaten").Nodes[0].Paragraphs.Take(4).Count(p => Rules.ParagraphVisible(p, gone));
            var ending = where.Contains(LeftFree) ? Pg("left_free_mourned") : Pg("eaten");
            check(Avail(ending, gone) && (where.Contains(LeftFree)
                  ? (ending.Nodes[0].Text + string.Join(" ", ending.Nodes[0].Paragraphs.Where(pp => Shows(pp, gone)).Select(pp => pp.Text))).Contains("in Ustalav, months late") && ending.Nodes[0].Text.Contains("no flesh to fetch")
                    && !Avail(Pg("eaten"), gone)
                  : places == 1),
                "Trk_Elyanka_Recall: the Wound's news does not resolve the claim at her actual location: " + string.Join("+", where));
        }
        foreach (var how in new[] { P + "straight", P + "bluffed", P + "exposed" })
        {
            var h1w = World(story, 6, "trickster.ever", Owned, Committed, how, "trickster.lastcall.taken", "ending.trickster");
            var coda1 = Render(story.Scenes.Single(x => x.Id == "elyanka.lastcall.page"), h1w);
            check(!SurfaceIds.Has(coda1, "[elyanka.lastcall.page/page/paragraph/7]"),
                "Trk_Elyanka_Recall: the Last Call coda recalls the wake, a veil or the cord in the " + how + " history without the hearse night.");
        }

        // Audit r7: her reason for the claims answers the whisper as it was (a lie is owed, not praised).
        var liar = World(story, 5, "trickster.ever", Owned, Bequeathed, Started, Tested, P + "gave_dead", P + "beat.whisper", P + "whisper.lie");
        var honest = World(story, 5, "trickster.ever", Owned, Bequeathed, Started, Tested, P + "gave_dead", P + "beat.whisper", P + "whisper.fear");
        check(Reachable(claims, liar).Any(x => SurfaceIds.Has(x, "[elyanka.trickster.commit.claims/lied_secret]")) && !Reachable(claims, liar).Any(x => SurfaceIds.Has(x, "[elyanka.trickster.commit.claims/true_secret]"))
              && Reachable(claims, honest).Any(x => SurfaceIds.Has(x, "[elyanka.trickster.commit.claims/true_secret]")) && !Reachable(claims, honest).Any(x => SurfaceIds.Has(x, "[elyanka.trickster.commit.claims/lied_secret]")),
            "Trk_Elyanka_Claims: her proposal praises a truth the Commander lied about, or the reverse.");

        // Audit r8: the inquiry needs Seelah present; a threat to Lastwall is not a letter sent; each rejection page tells its own.
        var rowsSeen = World(story, 5, "trickster.ever", Owned, Tested, Committed, Bier, P + "gave_dead", P + "seelah_prayed", "seelah.in_party", P + "react.seelah_rows");
        var inquiry = S(P + "beat.inquiry");
        check(Avail(inquiry, rowsSeen) && !Avail(inquiry, World(story, 5, "trickster.ever", Owned, Tested, Committed, Bier, P + "gave_dead", P + "seelah_prayed", P + "react.seelah_rows", "seelah_gone"))
              && !Avail(inquiry, World(story, 5, "trickster.ever", Owned, Tested, Committed, Bier, P + "gave_dead", P + "seelah_prayed", "seelah.in_party", P + "react.seelah_rows", "seelah_dead"))
              && Avail(S(P + "beat.hunt"), World(story, 5, "trickster.ever", Owned, Tested, Committed, Bier, "seelah_gone")),
            "Trk_Elyanka_Inquiry: Seelah investigates while gone or dead, or her absence stalls Elyanka.");
        var tyrant = S(P + "beat.tyrant");
        check(tyrant.Nodes.Single(n => n.Id == "told").Choices.All(ch => !ch.Set.Contains(P + "tyrant.lastwall_warned"))
              && tyrant.Nodes.Single(n => n.Id == "warned2").Choices.All(ch => ch.Set.Contains(P + "tyrant.lastwall_warned")),
            "Trk_Elyanka_Tyrant: a spoken threat sets the Lastwall letter.");
        foreach (var (scene0, node, index, marker) in new[] { (haggle, "refuse_veiled", 0, 1), (haggle, "refuse", 0, 2),
                                                               (haggle, "seen_out", 0, 3), (straight, "refuse", 0, 4) })
        {
            var w0 = World(story, 5, "trickster.ever", scene0 == straight ? P + "straight" : P + "executor", P + "door_seen");
            var refusedW = Take(scene0, w0, node, index, Closed);
            refusedW.Chapter = 6;
            check(Avail(Pg("turned_away"), refusedW) && Rules.ParagraphVisible(Pg("turned_away").Nodes[0].Paragraphs[marker], refusedW)
                  && Pg("turned_away").Nodes[0].Paragraphs.Take(5).Count(p => Rules.ParagraphVisible(p, refusedW)) == 1,
                "Trk_Elyanka_Rejections: the page after " + scene0.Id + "/" + node + " tells another branch's refusal.");
        }

        // Trk_Elyanka_LastCall: her coda needs the real commit; the bequest is a debt to a live power; it never keeps anyone alive.
        var coda = story.Scenes.Single(s => s.Id == "elyanka.lastcall.page");
        var call = story.Scenes.Single(s => s.Id == "elyanka.lastcall.call");
        check(coda.Requires.Contains(Committed) && coda.Requires.Contains(Active) && coda.Forbids.Contains(Declined)
              && coda.ForbidOverrides[Declined] == Committed
              && call.RequiresAnyGroups.Length == 1 && call.RequiresAnyGroups[0].SequenceEqual(new[] { Bequeathed })
              && story.Derived["lastcall.debt.whispering_way"].Single().SequenceEqual(new[] { Bequeathed })
              && call.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Contains("elyanka.lastcall.called") && c.Set.Contains("trickster.lastcall.creditors_called")),
            "Trk_Elyanka_LastCall: the coda, the call-in or the Whispering Way's debt is not wired as the plan says.");
        check(!mine.Concat(new[] { coda, call }).Any(s => s.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Any(f => f.StartsWith("trickster.lastcall.", StringComparison.Ordinal) && f != "trickster.lastcall.creditors_called")))
              && !mine.Any(s => s.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains("trickster.commander_back"))),
            "Trk_Elyanka_LastCall: the bequest sets a survival key (it never makes survival possible).");

        // Trk_Elyanka_Household: eligible only by a yes she actually gave.
        check(story.Derived["elyanka.harem.eligible"].Any(g => g.Length == 1 && g[0] == "elyanka.payoff.ordinary")
        // eng7-l13: preparation also requires the live outcome contract.
              && story.Derived[P + "late_committed"].Single().SequenceEqual(new[] { "trickster.ever", "elyanka.payoff.ordinary", "elyanka.outcome.route_open" })
              && !World(story, 6, "trickster.ever", Owned, Tested, Declined, LeftFree, Closed).Has("elyanka.harem.eligible")
              && !World(story, 6, "trickster.ever", Owned, Tested).Has("elyanka.harem.eligible")
              && World(story, 5, "trickster.ever", Committed).Has("elyanka.harem.eligible"),
            "Trk_Elyanka_Household: eligibility follows something other than her commit (a debt is not a romance).");
        Console.WriteLine("PASS: Elyanka Trickster (Trk_Elyanka_*): the funeral door and its delay, the executor's Bluff and the bare-faced sale, the Iz dead, the claims and her move, the hearse, " + beats.Length + " courtship beats, " + reactions.Length + " reactions, " + pages.Length + " pages, Last Call's coda and creditor, eligibility.");
    }
}
