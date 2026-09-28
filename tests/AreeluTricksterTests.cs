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
    private const string Committed = "areelu.committed";
    private const string Started = "areelu.started";
    private const string Closed = "areelu.closed";
    private const string FinalList = "f56a69dc64a48b14096a557697f43f2a";
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
        var questions = S(P + "lens.questions");
        var accounts = S(P + "lens.accounts");
        var struck = S(P + "wager.struck");
        var welcome = S(P + "threshold.welcome");
        var desk = S(P + "truth.the_desk");
        var rift = S(P + "rift.odds");
        var clause = S(P + "witch.the_clause");
        var late = S(P + "wager.at_threshold");
        var raised = S(P + "wager.raised");
        var lastWords = S(P + "wager.last_words");
        var rewrite = S(P + "finale.rewrite");
        var after = S(P + "finale.after");
        var survived = S(P + "finale.survived");
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
        check(new[] { lens, watched, questions, accounts }.All(s => Rules.IsRemote(s) && s.Chapters.SequenceEqual(new[] { 5 })),
            "The lens correspondence is not Chapter 5 letters.");
        check(rewrite.EpilogueSequence == "PlayerFinalChoice" && rewrite.EpilogueAfter == TricksterPage, "The rewrite is not after BookPage_0147.");
        var chain = new[] { rewrite, after, survived }.Concat(report).ToArray();
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
        var palace = World(story, 4, "trickster", "trickster.ever", "areelu.notes_told");
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
        var asked = Program.Walk(questions, With(story, kept[0])).Where(r => r.Has(questions.Id)).ToList();
        check(Available(questions, With(story, kept[0])) && asked.Count > 0 && asked.All(r => r.Has(LensAsked)), "The three questions do not follow the lens.");
        check(Available(accounts, With(story, asked[0])), "Where she was does not follow the questions.");
        var betHeld = Program.Walk(watched, With(story, bet[0])).Where(r => r.Has(watched.Id)).ToList();
        check(betHeld.Count > 0 && betHeld.All(r => r.Has(LensHeld)) && Available(questions, With(story, betHeld[0])),
            "The bet path never gets the lens.");
        var foolPages = new HashSet<string>();
        Program.Walk(accounts, With(story, asked[0], "fool_king.ever_crowned"), (page, _) => foolPages.Add(page));
        check(foolPages.Contains("fool_king"), "The lens never mentions the Fool King.");

        // Trk_Areelu_Wager.
        var cell = World(story, 5, "trickster", "trickster.ever", "areelu.met", "areelu.one_must_burn", Primed, Bet);
        check(Available(struck, cell) && !Available(struck, World(story, 5, "trickster", "trickster.ever", Primed, Bet)),
            "Trk_Areelu_Wager: the wager does not wait for 'One of us must burn'.");
        var wagers = Program.Walk(struck, cell).Where(r => r.Has(struck.Id)).ToList();
        check(wagers.Any(r => r.Has(Struck) && r.Has(Started) && r.Has(WitchBet)) && wagers.Any(r => r.Has(Closed) && !r.Has(Struck)),
            "Trk_Areelu_Wager: the stake or the refusal is missing.");
        var cellPages = new HashSet<string>();
        Program.Walk(struck, With(story, cell, "areelu.crib.rage"), (page, _) => cellPages.Add(page));
        check(cellPages.Contains("crib_rage") && !cellPages.Contains("crib_sadness"), "The wager does not read her crib question.");
        check(Available(nenio, wagers.First(r => r.Has(Struck))) && Available(ember, bet[0]) && !Available(ember, kept[0]),
            "Reactions: Nenio after the wager, Ember after the bet.");
        check(!Available(nenio, With(story, wagers.First(r => r.Has(Struck)), "nenio.dead")) && !Available(ember, With(story, bet[0], "ember_gone")),
            "Reactions are not guarded.");

        // Chapter 6 beats after the wager.
        var ch6 = World(story, 6, "trickster", "trickster.ever", Primed, Bet, Struck, Started);
        check(new[] { welcome, desk, rift, clause, raised, lastWords }.All(s => Available(s, ch6)) && !Available(late, ch6),
            "The Chapter 6 beats do not follow the wager.");
        check(!new[] { welcome, desk, rift, clause, raised }.Any(s => Available(s, With(story, ch6, Closed))), "A closed wager still opens Chapter 6 beats.");

        // Trk_Areelu_Raised / _RaisedRefused / stake only.
        var raisedOut = Program.Walk(raised, ch6).Where(r => r.Has(raised.Id)).ToList();
        check(raisedOut.Any(r => r.Has(Committed)) && raisedOut.Any(r => r.Has(Declined) && !r.Has(Committed))
              && raisedOut.Any(r => r.Has(StakeOnly) && !r.Has(Committed)), "Trk_Areelu_Raised: her yes, her no or the stake only is missing.");
        var producer = raised.Nodes.Single(n => n.Id == "her_choice").Choices[0];
        check(producer.Set.SequenceEqual(new[] { Committed }) && producer.Requires.Length == 0, "The CommittedFlag producer moved (her_choice, choice 0).");
        check(!Available(raised, raisedOut.First(r => r.Has(Committed))), "The raised wager can be raised twice.");

        // Trk_Areelu_LateThreshold.
        var lateWorld = World(story, 6, "trickster", "trickster.ever", Primed, Lens, Late);
        check(Available(late, lateWorld), "Trk_Areelu_LateThreshold: unavailable.");
        var lateOut = Program.Walk(late, lateWorld).Where(r => r.Has(late.Id)).ToList();
        check(lateOut.Any(r => r.Has(Struck) && r.Has(Late)) && lateOut.Any(r => r.Has(Closed)), "Trk_Areelu_LateThreshold: flags.");
        var latePages = new HashSet<string>();
        Program.Walk(raised, lateOut.First(r => r.Has(Struck)), (page, _) => latePages.Add(page));
        check(Available(raised, lateOut.First(r => r.Has(Struck))) && latePages.Contains("late_raise"), "The raised wager forgets the late terms.");

        // Finale pages: Trk_Areelu_Rewrite / _Survived / _NoWager / _Declined, the stake only and the late commit.
        var rewriteWorld = World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", "ending.trickster", Struck, Bet, Committed);
        check(Available(rewrite, rewriteWorld) && Available(after, rewriteWorld) && !Available(survived, rewriteWorld), "Trk_Areelu_Rewrite failed.");
        check(Available(report.Single(s => s.Id.EndsWith(".grey")), rewriteWorld) && !Available(report.Single(s => s.Id.EndsWith(".graft")), rewriteWorld)
              && !Available(report.Single(s => s.Id.EndsWith(".lady")), rewriteWorld), "The rewrite path shows the witch's pages.");
        var punchline = World(story, 6, "trickster.ever", "sacrifice", "ending.trickster", Struck, Bet, Committed);
        check(punchline.Has("trickster.cheated_death") && Available(survived, punchline) && !Available(rewrite, punchline) && !Available(after, punchline),
            "Trk_Areelu_Survived failed.");
        check(Available(report.Single(s => s.Id.EndsWith(".graft")), punchline) && !Available(report.Single(s => s.Id.EndsWith(".grey")), punchline)
              && Available(report.Single(s => s.Id.EndsWith(".lady")), punchline), "The punchline path shows the mortal's pages.");
        foreach (var fate in new[] { "areelu.dead_fight", "areelu.incinerated", "areelu.sacrifice_wound", "areelu.sacrifice_before" })
            check(Available(rewrite, World(story, 6, "trickster.ever", fate, Struck, Bet, Committed)), "The rewrite ignores the fate " + fate);
        var noWager = World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", "ending.trickster");
        check(!pages.Any(s => Available(s, noWager)), "Trk_Areelu_NoWager: a page plays without the wager.");
        var declined = World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", "ending.trickster", Struck, Bet, Declined);
        check(Available(stands, declined) && !Available(rewrite, declined) && !report.Any(s => Available(s, declined)), "Trk_Areelu_Declined failed.");
        var stakeOnly = World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", Struck, Bet, StakeOnly);
        check(Available(stakeOnlyPage, stakeOnly) && !Available(rewrite, stakeOnly), "The stake-only page failed.");
        var lateCommit = World(story, 6, "trickster.ever", "areelu.sacrifice_trickster", "ending.trickster", Struck, Bet);
        check(lateCommit.Has(P + "late_committed") && Available(rewrite, lateCommit), "The late commit (R2-6) does not reach the rewrite.");
        check(Available(ascended, World(story, 6, "trickster.ever", "areelu.ascended", Struck, Bet, Committed)), "The ascended page failed.");
        check(!Available(report.Single(s => s.Id.EndsWith(".wound")), World(story, 6, "trickster.ever", "areelu.sacrifice_wound", Struck, Bet, Committed)),
            "The wound page plays after the Wound was closed.");

        // Every page of the report walks to the end on both survivals without a dead end.
        foreach (var world in new[] { rewriteWorld, punchline })
            foreach (var page in pages.Where(s => Available(s, world)))
                check(Program.Walk(page, world).Count > 0, "A report page has no ending: " + page.Id);

        Console.WriteLine("PASS: Areelu Trickster (Trk_Areelu_*): the file, the bet, the lens, the wager, Threshold, the rewrite and the report.");
    }
}
