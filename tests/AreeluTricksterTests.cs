using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Areelu Vorlesh, Trickster (Writer/handoffs/trickster/areelu-vorlesh.md): the Architect's wager (F20, the epilogue rewrite).
// One block per spec rules test (Trk_Areelu_*), plus the Chapter 4 file, the lens correspondence, the Chapter 6 beats,
// the report chain and the reactions.
internal static class AreeluTricksterTests
{
    private const string P = "areelu.trickster.";
    private const string Primed = P + "primed";
    private const string Bet = P + "bet_offered";
    private const string Lens = P + "rivalry.lens";
    private const string Struck = P + "wager_struck";
    private const string Declined = P + "declined";
    private const string StakeOnly = P + "stake_only";
    private const string Noticed = P + "noticed";
    private const string LensHeld = P + "lens_held";
    private const string LensAsked = P + "lens.asked";
    private const string Late = P + "cost.late";
    private const string WitchBet = P + "cost.bet_with_the_witch";
    private const string Named = P + "stake_named";
    private const string WoundCeded = P + "cost.wound_ceded";
    private const string Drawn = P + "graft_drawn";
    private const string Committed = "areelu.committed";
    private const string Started = "areelu.started";
    private const string Closed = "areelu.closed";
    private const string FinalList = "f56a69dc64a48b14096a557697f43f2a";
    private const string Siphon = "areelu.siphon.council";
    private const string Unprimed = P + "cost.unprimed";
    private const string LifeTerm = P + "term.life";
    private const string Dagger = "areelu.dagger_held";

    // Every node path through a scene (Sol HOW: sequence checks, not only per-page availability).
    private static List<List<string>> Paths(Scene scene, Snapshot state)
    {
        var all = new List<List<string>>();
        void Go(string id, List<string> path)
        {
            var here = new List<string>(path) { id };
            var node = scene.Nodes.Single(n => n.Id == id);
            var next = node.Choices.Where(c => Rules.Match(c.Requires, c.Forbids, state)).SelectMany(c => c.Next == null ? new string[0] : Rules.NextNodes(c)).ToList();
            if (next.Count == 0 || node.Choices.Any(c => c.Next == null && Rules.Match(c.Requires, c.Forbids, state))) all.Add(here);
            foreach (var n in next) Go(n, here);
        }
        Go(scene.Nodes[0].Id, new List<string>());
        return all;
    }
    private const string TricksterPage = "fb42f8bd123bf1f40a448f6dbc66cbbe";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = "2570015799edf594daf2f076f2f975d8", Hour = 5000 };
        state.Flags.UnionWith(flags);
        if (chapter > 1) state.Flags.Add("chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 1000;
        return state;
    }

    private static Snapshot With(Story story, Snapshot state, params string[] flags)
    {
        var next = Program.Copy(state);
        foreach (var flag in flags) if (next.Flags.Add(flag)) next.Times[flag] = next.Hour;
        next.Hour += 200;
        Rules.Complete(story, next);
        return next;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        bool Available(Scene s, Snapshot w) => Rules.Available(story, s, w);
        var audience = S(P + "audience.notes");
        var izBet = S(P + "rivalry.iz_bet");
        var lens = S(P + "rivalry.lens");
        var watched = S(P + "lens.watched");
        var struck = S(P + "wager.struck");
        var welcome = S(P + "threshold.welcome");
        var desk = S(P + "truth.the_desk");
        var rift = S(P + "rift.odds");
        var clause = S(P + "witch.the_clause");
        var late = S(P + "wager.at_threshold");
        var raised = S(P + "wager.raised");
        var lastWords = S(P + "wager.last_words");
        var collect = S(P + "wager.collect");
        var rewrite = S(P + "finale.rewrite");
        var after = S(P + "finale.after");
        var survived = S(P + "finale.survived");
        var unnamed = S(P + "finale.unnamed");
        var stakeOnlyPage = S(P + "finale.stake_only");
        var stands = S(P + "finale.report_stands");
        var ascended = S(P + "finale.ascended");
        var report = new[] { "rooms", "hunters", "grey", "graft", "sarkoris", "participation", "wound", "crossroads", "prison",
                             "cult", "incursion", "dagger", "lady", "visitors", "name", "promise", "afterword" }
            .Select(id => S(P + "report." + id)).ToArray();
        var nenio = S(P + "react.nenio_two_drafts");
        var ember = S(P + "react.ember_regret");
        var ours = story.Scenes.Where(s => s.Relationship == "areelu").ToList();
        var pages = ours.Where(s => s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToList();

        // Relationship, hooks and shape.
        var rel = story.Relationships["areelu"];
        check(rel.StartedFlag == Started && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed && rel.UnavailableFlags.Length == 0,
            "Areelu relationship flags drifted.");
        check(izBet.AnswerLists.SequenceEqual(new[] { "09b8d5eb5dae3634d9dc3d8c7bdd6e9d" }) && izBet.NativeReturnCue == "c000ae3d47250b943953b1bd25333f30"
              && izBet.EntryMythic == "PlayerIsTrickster", "The Iz bet left AreeluIntro/AnswersList_0002.");
        check(izBet.Nodes.SelectMany(n => n.Choices).Where(c => c.NativeNext != null).All(c => c.NativeNext == "f4eee511a0c0f9e4cace9e0ced47bfba"),
            "The Iz bet does not hand back to her warning (Cue_0014).");
        check(struck.AnswerLists.SequenceEqual(new[] { "74989c07fc5fd8a42b18b333dc40acc1" }) && struck.NativeReturnCue == "3d63aae9686620845acc8be95e490c26"
              && struck.Nodes.SelectMany(n => n.Choices).Where(c => c.NativeNext != null).All(c => c.NativeNext == "13e9433101b3586488df88c296d91ed2"),
            "The wager left her cell (AnswersList_0003, Cue_0035, Cue_0038).");
        check(audience.AnswerLists.SequenceEqual(new[] { "199a940b97b11664aace4101733cd963" }) && audience.EntryMythic == "PlayerIsTrickster"
              && audience.Chapters.SequenceEqual(new[] { 4 }), "The file left the Alushinyrra audience.");
        check(new[] { late, raised }.All(s => s.ReturnToList && s.AnswerLists.SequenceEqual(new[] { FinalList }) && s.NativeReturnCue == null)
              && lastWords.ReturnToList && lastWords.AnswerLists.SequenceEqual(new[] { "b6bc1d5fb28e115499b8bcbbc0d541f9" }),
            "The Threshold beats are not E14b return-to-list scenes on GrandFinal.");
        check(new[] { lens, watched }.All(s => Rules.IsRemote(s) && s.Chapters.SequenceEqual(new[] { 5 })),
            "The lens is not a Chapter 5 letter.");
        // letters_max.5 = 1: the lens is the only Areelu letter on either path (the late primer or the glass after the bet).
        check(ours.Count(s => Rules.IsRemote(s)) == 2 && lens.Forbids.Contains(Primed) && watched.Requires.Contains(Bet),
            "Areelu has more than one Chapter 5 letter on a path.");
        check(rewrite.EpilogueSequence == "PlayerFinalChoice" && rewrite.EpilogueAfter == TricksterPage, "The rewrite is not after BookPage_0147.");
        var chain = new[] { rewrite, after, unnamed, survived }.Concat(report).ToArray();
        for (int i = 1; i < chain.Length; i++)
            check(chain[i].EpilogueSequence == "PlayerFinalChoice" && chain[i].EpilogueAfter == "scene:" + chain[i - 1].Id,
                "The report chain is out of order at " + chain[i].Id);
        check(pages.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).All(c => c.Set.Length == 0 && c.Mythic == null && c.Alignment == null),
            "An epilogue page sets a flag or carries a native effect (R2-0e).");
        var stake = struck.Nodes.SelectMany(n => n.Choices).Where(c => c.Text.StartsWith("[Name your stake]", StringComparison.Ordinal)).ToList();
        check(stake.Count > 0 && stake.All(c => c.Mythic == "PlayerIsTrickster" && c.Alignment?.Direction == "Chaotic" && c.Alignment.Value == 1),
            "The stake lost its [Trickster] mark or its Chaotic shift.");

        // Not on Trickster: nothing opens (other paths keep canon fate).
        var notTrickster = World(story, 5, "areelu.met", "areelu.one_must_burn", "areelu.notes_told");
        check(!ours.Where(s => !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).Any(s => Available(s, notTrickster)),
            "An Areelu scene opens off the Trickster path.");

        // Chapter 4: the file (optional primer, a variant read only).
        // Chapter 4 physical scenes are blocked only for the Tirabade route (Rules.Available: `if (scene.Relationship ==
        // "tirabade") { if (!IsRemote(scene) && state.Chapter == 4) return false; }`); Areelu's file is physical in Chapter 4.
        var palace = World(story, 4, "trickster", "trickster.ever", "areelu.notes_told");
        check(audience.Relationship == "areelu" && !Rules.IsRemote(audience) && palace.Chapter == 4 && Available(audience, palace),
            "The Chapter 4 file is not reachable as a physical scene in the Alushinyrra audience.");
        check(Available(audience, palace) && !Available(audience, World(story, 4, "trickster", "trickster.ever")), "The file is not gated on her notes.");
        var filed = Program.Walk(audience, palace).Where(r => r.Has(audience.Id)).ToList();
        check(filed.Count > 0 && filed.All(r => r.Has(Noticed) && !r.Has(Started)), "The file starts the relationship or loses its note.");

        // Trk_Areelu_Rivalry.
        var iz = World(story, 5, "trickster", "trickster.ever", "areelu.met");
        check(Available(izBet, iz) && !Available(izBet, World(story, 5, "trickster.ever", "areelu.met")), "Trk_Areelu_Rivalry: availability.");
        var bet = Program.Walk(izBet, iz).Where(r => r.Has(izBet.Id)).ToList();
        check(bet.Count > 0 && bet.All(r => r.Has(Primed) && r.Has(Bet)), "Trk_Areelu_Rivalry: flags.");
        check(!Available(lens, bet[0]) && Available(watched, With(story, bet[0])), "Trk_Areelu_Rivalry: the lens follows the bet wrongly.");
        var noticedIz = Program.Walk(izBet, With(story, iz, Noticed));
        var izPages = new HashSet<string>();
        Program.Walk(izBet, With(story, iz, Noticed), (page, _) => izPages.Add(page));
        check(izPages.Contains("observed") && noticedIz.Any(r => r.Has(Bet)), "The Iz bet does not remember the file.");

        // Trk_Areelu_Lens (late primer) and the correspondence on both paths.
        check(Available(lens, iz), "Trk_Areelu_Lens: the lens is unavailable without the bet.");
        var kept = Program.Walk(lens, iz).Where(r => r.Has(lens.Id)).ToList();
        check(kept.Count > 0 && kept.All(r => r.Has(Primed) && r.Has(Lens) && r.Has(Late) && r.Has(LensHeld)), "Trk_Areelu_Lens: flags.");
        check(lens.Nodes.SelectMany(n => n.Choices).Any(c => c.Mythic == "PlayerIsTrickster"), "The knock on the lens is not a [Trickster] answer.");
        // The same letter carries her three questions and where she was; both lens letters share that night.
        foreach (var (letter, world) in new[] { (lens, iz), (watched, With(story, bet[0])) })
        {
            var nights = new HashSet<string>();
            var ends = Program.Walk(letter, With(story, world, "fool_king.ever_crowned"), (node, _) => nights.Add(node)).Where(r => r.Has(letter.Id)).ToList();
            check(ends.Count > 0 && ends.All(r => r.Has(LensHeld)) && ends.Any(r => r.Has(LensAsked)) && ends.Any(r => !r.Has(LensAsked))
                  && new[] { "first", "second", "third", "accounts", "fool_king", "bait" }.All(nights.Contains),
                "The lens night (questions, where she was) is not in the letter: " + letter.Id);
        }

        // Trk_Areelu_Wager.
        var cell = World(story, 5, "trickster", "trickster.ever", "areelu.met", "areelu.one_must_burn", Primed, Bet);
        check(Available(struck, cell) && !Available(struck, World(story, 5, "trickster", "trickster.ever", Primed, Bet)),
            "Trk_Areelu_Wager: the wager does not wait for 'One of us must burn'.");
        var wagers = Program.Walk(struck, cell).Where(r => r.Has(struck.Id)).ToList();
        check(wagers.Any(r => r.Has(Struck) && r.Has(Started) && r.Has(WitchBet)) && wagers.Any(r => r.Has(Closed) && !r.Has(Struck)),
            "Trk_Areelu_Wager: the stake or the refusal is missing.");
        check(wagers.Any(r => r.Has(Struck) && r.Has(Named)) && wagers.Any(r => r.Has(Struck) && !r.Has(Named)),
            "The cell does not offer (without forcing) the joke that names the stake.");
        var cellPages = new HashSet<string>();
        Program.Walk(struck, With(story, cell, "areelu.crib.rage"), (page, _) => cellPages.Add(page));
        check(cellPages.Contains("crib_rage") && !cellPages.Contains("crib_sadness"), "The wager does not read her crib question.");
        check(Available(nenio, wagers.First(r => r.Has(Struck))) && Available(ember, bet[0]) && !Available(ember, kept[0]),
            "Reactions: Nenio after the wager, Ember after the bet.");
        check(!Available(nenio, With(story, wagers.First(r => r.Has(Struck)), "nenio.dead")) && !Available(ember, With(story, bet[0], "ember_gone")),
            "Reactions are not guarded.");
        // Seelah objects on her own hub once the Commander commits; G6: her return lifts her death/departure guard.
        var seelah = S(P + "react.seelah_objects");
        var courted = World(story, 6, "trickster.ever", Struck, Bet, Committed);
        check(seelah.Reaction && !Available(seelah, courted) && seelah.Forbids.Contains("trickster.ever"),
            "Seelah's reaction is not retired (the ledger allocates Areelu exactly Nenio and Ember).");

        // Chapter 6 beats after the wager.
        var ch6 = World(story, 6, "trickster", "trickster.ever", Primed, Bet, Struck, Started);
        check(new[] { welcome, desk, rift, clause, raised, lastWords }.All(s => Available(s, ch6)) && !Available(late, ch6),
            "The Chapter 6 beats do not follow the wager.");
        check(!new[] { welcome, desk, rift, clause, raised }.Any(s => Available(s, With(story, ch6, Closed))), "A closed wager still opens Chapter 6 beats.");

        // Trk_Areelu_Raised / _RaisedRefused / stake only.
        var raisedOut = Program.Walk(raised, ch6).Where(r => r.Has(raised.Id)).ToList();
        check(raisedOut.Any(r => r.Has(Committed)) && raisedOut.Any(r => r.Has(Declined) && !r.Has(Committed))
              && raisedOut.Any(r => r.Has(StakeOnly) && !r.Has(Committed)), "Trk_Areelu_Raised: her yes, her no or the stake only is missing.");
        check(raisedOut.Any(r => r.Has(Committed) && r.Has(Named) && r.Has(WoundCeded)) && raisedOut.Any(r => r.Has(Committed) && !r.Has(Named)),
            "The priced term (notes for her life, the wound as the price) or its refusal is missing at Threshold.");
        var producer = raised.Nodes.Single(n => n.Id == "her_choice").Choices[0];
        check(producer.Set.SequenceEqual(new[] { Committed }) && producer.Requires.Length == 0, "The CommittedFlag producer moved (her_choice, choice 0).");
        check(!Available(raised, raisedOut.First(r => r.Has(Committed))), "The raised wager can be raised twice.");

        // Trk_Areelu_LateThreshold.
        var lateWorld = World(story, 6, "trickster", "trickster.ever", Primed, Lens, Late);
        check(Available(late, lateWorld), "Trk_Areelu_LateThreshold: unavailable.");
        var lateOut = Program.Walk(late, lateWorld).Where(r => r.Has(late.Id)).ToList();
        check(lateOut.Any(r => r.Has(Struck) && r.Has(Late) && r.Has(Named)) && lateOut.Any(r => r.Has(Closed)), "Trk_Areelu_LateThreshold: flags.");
        var latePages = new HashSet<string>();
        Program.Walk(raised, lateOut.First(r => r.Has(Struck)), (page, _) => latePages.Add(page));
        check(Available(raised, lateOut.First(r => r.Has(Struck))) && latePages.Contains("late_raise"), "The raised wager forgets the late terms.");

        // Finale pages: Trk_Areelu_Rewrite / _Survived / _NoWager / _Declined, the stake only and the late commit.
        // The stake collected on screen: the soul cauldron takes the graft before the final choice.
        var cauldronWorld = World(story, 6, "trickster", "trickster.ever", Siphon, Primed, Bet, Struck, Committed, Named, WoundCeded);
        check(collect.ReturnToList && Available(collect, cauldronWorld) && !Available(collect, World(story, 6, "trickster.ever", Primed, Bet, Struck, Committed, Named, WoundCeded))
              && !Available(collect, World(story, 6, "trickster.ever", Siphon, Primed, Bet, Struck, Committed, WoundCeded)),
            "The collection does not need both a siphon in hand and the named stake.");
        // Sol INT (r1): the native Trickster finale (GrandFinal/Answer_0055) needs a filled siphon; an empty one cannot be collected into.
        check(!Available(collect, World(story, 6, "trickster", "trickster.ever", "areelu.siphon.empty", Primed, Bet, Struck, Committed, Named, WoundCeded)),
            "The graft can be collected into the empty siphon.");
        // Sol INT: the historical hand-over is not possession (Shyka_Offer/Cue_0031 takes the filled siphon back).
        check(!Available(collect, World(story, 6, "trickster.ever", "council.cauldron_given", Primed, Bet, Struck, Committed, Named, WoundCeded)),
            "The collection reads the Council's hand-over instead of the siphon in the inventory.");
        // Sol TRK: the substitution is paid for before it is collected, and never after "Your life. Nothing less."
        check(!Available(collect, World(story, 6, "trickster.ever", Siphon, Primed, Bet, Struck, Named)),
            "The graft can be collected before the wound is ceded.");
        check(!Available(collect, With(story, cauldronWorld, LifeTerm)), "The life-only term still receives the work substitution.");
        var cellNamed = World(story, 6, "trickster", "trickster.ever", Siphon, Primed, Bet, Struck, Started, Named);
        var raisedLife = Program.Walk(raised, cellNamed).Where(r => r.Has(Committed) && !r.Has(WoundCeded)).ToList();
        check(raisedLife.Count > 0 && raisedLife.All(r => !Available(collect, r)), "A commit without the wound price reaches the collection.");
        var raisedPaid = Program.Walk(raised, cellNamed).Where(r => r.Has(Committed) && r.Has(WoundCeded)).ToList();
        check(raisedPaid.Count > 0 && raisedPaid.All(r => Available(collect, r)), "The paid commit does not reach the collection.");
        check(collect.Nodes.Any(n => n.Id == "full") && Program.Walk(collect, With(story, cauldronWorld)).Where(r => r.Has(collect.Id)).All(r => r.Has(Drawn)),
            "The collection does not settle a filled siphon's contents.");
        var collected = Program.Walk(collect, cauldronWorld).Where(r => r.Has(collect.Id)).ToList();
        check(collected.Count == 1 && collected[0].Has(Drawn) && collect.Nodes.SelectMany(n => n.Choices).Any(ch => ch.Mythic == "PlayerIsTrickster") && collect.Nodes.Any(n => n.Id == "contest"),
            "The collection does not draw the graft with a [Trickster] act.");
        var rewriteWorld = World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", "ending.trickster", Struck, Bet, Committed, Named, Drawn);
        check(Available(rewrite, rewriteWorld) && Available(after, rewriteWorld) && !Available(survived, rewriteWorld), "Trk_Areelu_Rewrite failed.");
        check(Available(report.Single(s => s.Id.EndsWith(".grey")), rewriteWorld) && !Available(report.Single(s => s.Id.EndsWith(".graft")), rewriteWorld)
              && !Available(report.Single(s => s.Id.EndsWith(".lady")), rewriteWorld), "The rewrite path shows the witch's pages.");
        var punchline = World(story, 6, "trickster.ever", "sacrifice", "ending.trickster", Struck, Bet, Committed);
        check(punchline.Has("trickster.cheated_death") && Available(survived, punchline) && !Available(rewrite, punchline) && !Available(after, punchline),
            "Trk_Areelu_Survived failed.");
        check(Available(report.Single(s => s.Id.EndsWith(".graft")), punchline) && !Available(report.Single(s => s.Id.EndsWith(".grey")), punchline)
              && Available(report.Single(s => s.Id.EndsWith(".lady")), punchline), "The punchline path shows the mortal's pages.");
        // Only the Trickster finale is rewritten, and only on the collected stake; every other death keeps canon fate.
        foreach (var fate in new[] { "areelu.dead_fight", "areelu.incinerated", "areelu.sacrifice_wound", "areelu.sacrifice_before" })
        {
            var other = World(story, 6, "trickster.ever", fate, Struck, Bet, Committed, Named, Drawn);
            check(!Available(rewrite, other) && Available(unnamed, other) && !report.Any(s => Available(s, other)), "Another fate is rewritten: " + fate);
        }
        check(!Available(rewrite, World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", "ending.trickster", Struck, Bet, Committed, Named))
              && Available(unnamed, World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", "ending.trickster", Struck, Bet, Committed, Named)),
            "A named but uncollected stake is rewritten.");
        // The failure path: the stake was never named, so there is nothing to collect in place of her life.
        var unnamedWorld = World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", "ending.trickster", Struck, Bet, Committed);
        check(Available(unnamed, unnamedWorld) && !Available(rewrite, unnamedWorld) && !Available(after, unnamedWorld)
              && !report.Any(s => Available(s, unnamedWorld)) && !Available(unnamed, rewriteWorld), "The unnamed stake does not keep her canon fate.");
        var noWager = World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", "ending.trickster");
        check(!pages.Any(s => Available(s, noWager)), "Trk_Areelu_NoWager: a page plays without the wager.");
        var declined = World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", "ending.trickster", Struck, Bet, Declined);
        check(Available(stands, declined) && !Available(rewrite, declined) && !report.Any(s => Available(s, declined)), "Trk_Areelu_Declined failed.");
        var stakeOnly = World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", Struck, Bet, StakeOnly);
        check(Available(stakeOnlyPage, stakeOnly) && !Available(rewrite, stakeOnly), "The stake-only page failed.");
        var lateCommit = World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", "ending.trickster", Struck, Bet, Named, Drawn);
        check(lateCommit.Has(P + "late_committed") && Available(rewrite, lateCommit), "The late commit (R2-6) does not reach the rewrite.");
        check(Available(ascended, World(story, 6, "trickster.ever", "areelu.ascended", Struck, Bet, Committed)), "The ascended page failed.");

        // Sol INT: the missed-entry world (no Iz bet, no lens) has its own Threshold wager, at her harshest terms.
        var unprimedScene = S(P + "wager.unprimed");
        var cold = World(story, 6, "trickster", "trickster.ever");
        check(unprimedScene.ReturnToList && unprimedScene.AnswerLists.SequenceEqual(new[] { FinalList }) && Available(unprimedScene, cold)
              && !Available(late, cold) && !Available(unprimedScene, World(story, 6, "trickster.ever"))
              && !Available(unprimedScene, With(story, cold, Primed)), "The unprimed Threshold entry is missing or misgated.");
        var coldOut = Program.Walk(unprimedScene, cold).Where(r => r.Has(unprimedScene.Id)).ToList();
        check(coldOut.Any(r => r.Has(Primed) && r.Has(Late) && r.Has(Struck) && r.Has(WoundCeded) && r.Has(Named) && r.Has(Unprimed))
              && coldOut.Any(r => r.Has(Closed) && !r.Has(Struck)), "The unprimed wager does not produce its flags through the choices.");
        var coldStruck = With(story, coldOut.First(r => r.Has(Struck)));
        var coldRaised = Program.Walk(raised, coldStruck).Where(r => r.Has(Committed)).ToList();
        check(Available(raised, coldStruck) && coldRaised.Count > 0 && coldStruck.Has(P + "wager_on_screen"),
            "The unprimed wager cannot be raised to the commit.");
        var coldFinale = World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", "ending.trickster", Struck, Unprimed, Committed, Named, WoundCeded, Drawn);
        check(Available(rewrite, coldFinale) && Available(report[0], coldFinale), "The unprimed commit does not reach the rewrite and the report.");

        // Sol INT: the punchline after the graft was drawn: she lives, and the body follows the extraction.
        var drawnPunchline = With(story, punchline, Named, WoundCeded, Drawn);
        check(Available(survived, drawnPunchline) && Available(report.Single(s => s.Id.EndsWith(".grey")), drawnPunchline)
              && !Available(report.Single(s => s.Id.EndsWith(".graft")), drawnPunchline), "The drawn punchline restores the graft.");
        var drawnNight = new HashSet<string>();
        Program.Walk(report.Single(s => s.Id.EndsWith(".participation")), drawnPunchline, (node, _) => drawnNight.Add(node));
        check(drawnNight.Contains("in_mortal_2") && !drawnNight.Contains("in_witch_2"), "The drawn punchline night shows the Abyss.");
        // A punchline over her native death in the fight revives nobody.
        check(!report.Any(s => Available(s, With(story, punchline, "areelu.dead_fight"))), "The punchline revives an Areelu who died.");

        // Sol COX (r1): Areelu's page and the Last Call page agree about Shyka (H1: the Commander came back one person).
        var fw = World(story, 6, "trickster.ever", "sacrifice", "ending.trickster_allplanes_fw", Struck, Bet, Committed);
        var fwH1 = With(story, fw, "trickster.lastcall.taken");
        string ShykaLine(Snapshot w) => string.Join("|", Rules.VisibleParagraphs(survived.Nodes[0], w).Select(pp => pp.Text).Where(tx => tx.Contains("Shyka")));
        check(Available(survived, fw) && fwH1.Has("lastcall.h1") && ShykaLine(fw).Contains("initialled twice") && !ShykaLine(fw).Contains("bottle")
              && ShykaLine(fwH1).Contains("bottle") && !ShykaLine(fwH1).Contains("initialled twice"),
            "The Shyka paragraph contradicts the Last Call H1 page.");
        // Sol INT (r1): a returned Nenio (G6(b)) is at breakfast exactly once; a dissolved one never.
        var nenioBack = With(story, rewriteWorld, "nenio.dead", "nenio.trickster.returned");
        int Breakfast(Snapshot w) => Rules.VisibleParagraphs(report.Single(s => s.Id.EndsWith(".participation")).Nodes.Single(n => n.Id == "morning"), w).Count(pp => pp.Text.StartsWith("Nenio arrived at breakfast"));
        check(Breakfast(rewriteWorld) == 1 && Breakfast(nenioBack) == 1 && Breakfast(With(story, rewriteWorld, "nenio.dead")) == 0
              && Breakfast(With(story, nenioBack, "nenio.dissolved")) == 0, "A returned Nenio misses breakfast, or appears twice.");
        // Sol COX (r1): no companion outside the allocation visits the report.
        check(report.Single(s => s.Id.EndsWith(".visitors")).Nodes.Single(n => n.Id == "start").Choices.Where(ch => ch.Next == "daeran").All(ch => ch.Forbids.Contains("trickster.ever")),
            "Daeran still visits the report.");

        // Sol r2 (CAN): the lens invents no deaths; the Crossroads shows no fighting hosts (Epilogues/Cue_0175 turns them to ale).
        check(lens.Nodes.Single(n => n.Id == "died").Text.IndexOf("twice", StringComparison.Ordinal) < 0
              && report.Single(s => s.Id.EndsWith(".crossroads")).Nodes.All(n => !n.Text.Contains("killing") && !n.Text.Contains("fought") && !n.Text.Contains("still fighting")),
            "The lens counts deaths that never happened, or the Crossroads is still a battlefield.");
        // Every other native death keeps canon fate, and the page says whose choice it was.
        foreach (var fate in new[] { "areelu.incinerated", "areelu.sacrifice_wound", "areelu.sacrifice_before", "areelu.dead_fight" })
        {
            var w = World(story, 6, "trickster.ever", fate, Struck, Bet, Committed, Named, Drawn);
            check(Rules.VisibleParagraphs(unnamed.Nodes[0], w).Length >= 2, "The uncollected page does not explain " + fate);
        }

        // Sol BEL: the breakup ends the report; the afterword lives only in the branches that continue.
        var promise = report.Single(s => s.Id.EndsWith(".promise"));
        check(!Available(report.Single(s => s.Id.EndsWith(".afterword")), rewriteWorld) && !Available(report.Single(s => s.Id.EndsWith(".afterword")), punchline),
            "The separate afterword page still plays.");
        foreach (var world in new[] { rewriteWorld, punchline })
        {
            var paths = Paths(promise, world);
            check(paths.Where(pth => pth.Contains("burned")).All(pth => !pth.Contains("afterword"))
                  && paths.Any(pth => pth.Contains("kept") && pth.Contains("aw_line")) && paths.Any(pth => pth.Contains("filed") && pth.Contains("afterword")),
                "The promise page's endings are inconsistent.");
        }

        // Sol CAN: the dagger is narrated only where the inventory holds it.
        var daggerPage = report.Single(s => s.Id.EndsWith(".dagger"));
        var noDagger = new HashSet<string>();
        Program.Walk(daggerPage, rewriteWorld, (node, _) => noDagger.Add(node));
        var withDagger = new HashSet<string>();
        Program.Walk(daggerPage, With(story, rewriteWorld, Dagger), (node, _) => withDagger.Add(node));
        check(noDagger.Contains("gone") && !noDagger.Contains("give") && withDagger.Contains("give") && !withDagger.Contains("gone"),
            "The dagger page narrates a dagger the Commander does not hold.");
        // Trk_Areelu_PriorLien (ledger row 16): the Commander burned closing the Wound; only the prior-lien page plays.
        // Iomedae's form of this world (iomedae.appointment_kept, now produced by her route) has its own page, not_burned; a
        // committed Areelu (a struck wager is at least late-committed) gets her night there (Sol PP8 r1, BEL cap).
        var notBurned = S(P + "finale.not_burned");
        var keptWorld = World(story, 6, "trickster.ever", "iomedae.appointment_kept", Struck, Bet, Committed, Named);
        var keptPages = new HashSet<string>();
        Program.Walk(notBurned, keptWorld, (page, _) => keptPages.Add(page));
        check(Available(notBurned, keptWorld) && keptPages.Contains("nb_across") && keptPages.Contains("nb_morning") && keptPages.Contains("nb_stopped"),
            "The appointment-kept page does not give a committed Areelu her night.");
        // Sol PP8 r2 (INT/BEL): her refusal or the stake alone settles the page; no night follows either.
        foreach (var refusal in new[] { Declined, StakeOnly })
        {
            var refusedPages = new HashSet<string>();
            var refusedOut = Program.Walk(notBurned, World(story, 6, "trickster.ever", "iomedae.appointment_kept", Struck, Bet, Named, refusal), (page, _) => refusedPages.Add(page));
            check(refusedOut.Count > 0 && !refusedPages.Contains("nb_across") && !refusedPages.Contains("nb_morning"),
                "The appointment-kept page gives a night after " + refusal + ".");
        }
        // Sol PP8 r1 (CAN): a stake named only at Threshold is never recalled as named in her cell.
        var lateRaise = new HashSet<string>();
        Program.Walk(raised, lateOut.First(r => r.Has(Struck) && r.Has(Named)), (page, _) => lateRaise.Add(page));
        check(!lateRaise.Contains("priced_known"), "The raised wager recalls a cell naming that never happened.");
        var priorLien = S(P + "finale.prior_lien");
        var burned = World(story, 6, "trickster.ever", "sacrifice", "ending.wound_closed", Struck, Bet, Committed, Named, Drawn);
        check(burned.Has(P + "commander_burned") && !burned.Has("trickster.cheated_death") && Available(priorLien, burned)
              && !Available(survived, burned) && !report.Any(s => Available(s, burned)), "Trk_Areelu_PriorLien failed.");
        check(!Available(priorLien, punchline) && !Available(priorLien, rewriteWorld), "The prior-lien page plays when the Commander lived.");
        // Sol r3 COX: Last Call H2 returns the Commander from the Wound-closed sacrifice; the permanent-loss page yields.
        var bottled = World(story, 6, "trickster.ever", "sacrifice", "ending.wound_closed", "trickster.lastcall.taken", "trickster.lastcall.pillar.bottle",
            Struck, Bet, Committed, Named, Drawn);
        var lienBottled = S(P + "finale.lien_bottled");
        check(bottled.Has("trickster.commander_back") && !Available(priorLien, bottled) && Available(lienBottled, bottled) && !Available(lienBottled, burned),
            "Sol r3 COX: Areelu's prior lien ignores Last Call H2 (or the H2 page plays in a permanent loss).");
        var h2Nodes = new HashSet<string>();
        Program.Walk(lienBottled, bottled, (node, _) => h2Nodes.Add(node));
        check(h2Nodes.Contains("across") && h2Nodes.Contains("morning") && h2Nodes.Contains("stopped")
              && !lienBottled.Nodes.SelectMany(n => new[] { n.Text }.Concat(n.Paragraphs.Select(pp => pp.Text))).Any(t => t.Contains("empty flask")),
            "Sol r4 BEL/COX: the H2 romance has no night, or the flask leaves the Commander.");
        // Sol r3 INT: the native Trickster sacrifice also starts Ending_AreeluDead (areelu.dead_fight); the collected
        // rewrite lifts both, and the report (with its intimate beat) continues. A bare combat death stays canon.
        var fullRewrite = With(story, rewriteWorld, "areelu.dead_fight");
        check(Available(report.Single(s => s.Id.EndsWith(".rooms")), fullRewrite) && Available(report.Single(s => s.Id.EndsWith(".participation")), fullRewrite)
              && !Available(report.Single(s => s.Id.EndsWith(".rooms")), World(story, 6, "trickster.ever", "areelu.dead_fight", "ending.trickster", Struck, Bet, Committed, Named, Drawn)),
            "Sol r3 INT: the native sacrifice's general death key blocks the rewritten report.");
        // Sol r3 CAN: the Crossroads of Worlds is the all-planes outcome only.
        var crossroads = report.Single(s => s.Id.EndsWith(".crossroads"));
        check(!Available(crossroads, rewriteWorld) && !Available(crossroads, punchline)
              && Available(crossroads, World(story, 6, "trickster.ever", "sacrifice", "ending.trickster_allplanes", Struck, Bet, Committed)),
            "Sol r3 CAN: the Crossroads page plays on the Nirvana-only ending.");
        check(!Available(report.Single(s => s.Id.EndsWith(".wound")), World(story, 6, "trickster.ever", "areelu.sacrifice_wound", Struck, Bet, Committed, Named)),
            "The wound page plays after the Wound was closed.");

        // The intimate beat and its refusal are reachable on both survivals; the morning after follows the yes.
        var participation = report.Single(s => s.Id.EndsWith(".participation"));
        foreach (var world in new[] { rewriteWorld, With(story, rewriteWorld, "areelu.dead_fight"), punchline, lateCommit })
        {
            var visited = new HashSet<string>();
            var ends = Program.Walk(participation, world, (node, _) => visited.Add(node));
            check(ends.Count > 0 && visited.Contains("morning") && visited.Contains("morning_after") && visited.Contains("closed")
                  && (ReferenceEquals(world, punchline) ? visited.Contains("in_witch_2") : visited.Contains("in_mortal_2")),
                "The night, its morning after or its refusal is unreachable.");
        }
        // Every page of the report walks to the end on both survivals without a dead end.
        foreach (var world in new[] { rewriteWorld, punchline })
            foreach (var page in pages.Where(s => Available(s, world)))
                check(Program.Walk(page, world).Count > 0, "A report page has no ending: " + page.Id);

        Console.WriteLine("PASS: Areelu Trickster (Trk_Areelu_*): the file, the bet, the lens, the wager, Threshold, the rewrite and the report.");
    }
}
