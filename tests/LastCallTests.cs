using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Last Call (Writer/handoffs/04-TRICKSTER-EXTENDED-ENDING.md §8), re-scoped by 07/08: the bottle, the ledger at the rift, the
// last joke, the four Block A pages and Block C, the partner codas, and the Trickster's Ledger (E15). Plus the user's rules:
// no page is an exit, "apart" only on a failure flag, nothing reads another route's closed/death/return flag (G5), and every
// mourning page yields to a Commander who walked out of the rift (L6).
internal static class LastCallTests
{
    private const string Taken = "trickster.lastcall.taken", Open = "trickster.lastcall.open", Primed = "trickster.lastcall.primed.bottle";
    private const string Bottle = "trickster.lastcall.pillar.bottle", Creditors = "trickster.lastcall.pillar.creditors";
    private const string Heroic = "trickster.lastcall.heroic", Bottled = "trickster.lastcall.cost.bottled", Due = "trickster.lastcall.cost.creditors_due";
    private const string Late = "trickster.lastcall.cost.late", Active = "lastcall.active";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 20000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 500;
        return state;
    }

    private static Snapshot Done(Story story, Snapshot state)
    {
        var next = Program.Copy(state);
        Rules.Complete(story, next);
        return next;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Sc(string id) => story.Scenes.Single(s => s.Id == id);
        bool Av(Scene s, Snapshot w) => Rules.Available(story, s, w);
        var threshold = Sc("trickster.lastcall.threshold");
        var joke = Sc("trickster.lastcall.last_joke");
        var jokeAreelu = Sc("trickster.lastcall.last_joke.areelu");
        var king = Sc("trickster.lastcall.bottle.king");
        var alone = Sc("trickster.lastcall.bottle.alone");
        var a1 = Sc("trickster.lastcall.page.interrupted");
        var a1h2 = Sc("trickster.lastcall.page.heroic");
        var a2 = Sc("trickster.lastcall.page.bottle");
        var a3 = Sc("trickster.lastcall.page.collectors");
        var lastWord = Sc("trickster.lastcall.page.last_word");
        var framework = story.Scenes.Where(s => s.Relationship == "lastcall").ToArray();
        var pages = framework.Where(s => s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var codas = pages.Where(s => s.Id.EndsWith(".lastcall.page", StringComparison.Ordinal)).ToArray();
        var calls = framework.Where(s => s.Id.EndsWith(".lastcall.call", StringComparison.Ordinal)).ToArray();

        // 1. LastCall_Offer_Vessel: on every final list; an unprimed vessel fills late at the rift; both pillars close the scene.
        var vessel = World(story, 6, "trickster", "trickster.ever", "lastcall.flask_taken", "lastcall.flask_held");
        check(Av(threshold, vessel) && threshold.AnswerLists.Length == 5 && threshold.ReturnToList,
            "LastCall_Offer_Vessel: [Call last orders] is not an E14b line on all five final lists.");
        var opened = Done(story, Program.Walk(threshold, vessel).Single(r => r.Has(Open)));
        check(opened.Has(Bottle) && opened.Has(Late) && opened.Has("trickster.lastcall.joke.funeral") && !Av(threshold, opened),
            "LastCall_Offer_Vessel: the late vessel does not fill at the rift, or the opener stays offered.");
        var told = Program.Walk(joke, opened).Where(r => r.Has(Taken)).ToList();
        check(told.Any(r => r.Has(Bottled) && !r.Has(Heroic)) && told.Any(r => r.Has(Heroic) && r.Has("trickster.lastcall.cost.mortal")),
            "LastCall_Offer_Vessel: the last joke lacks the bottle or the heroic answer beside a self-sacrifice.");
        check(!Program.Walk(jokeAreelu, opened).Any(r => r.Has(Heroic)) && jokeAreelu.AnswerLists.Intersect(joke.AnswerLists).Count() == 0,
            "LastCall_Offer_Vessel: the heroic answer is offered on an Areelu-punchline list, which has no self-sacrifice.");
        var afterJoke = Done(story, told.First(r => !r.Has(Heroic)));
        check(!Av(joke, afterJoke) && !Av(jokeAreelu, afterJoke) && afterJoke.Has(Taken), "LastCall_Offer_Vessel: the last joke can be told twice.");

        // 2. LastCall_Offer_Creditors: no vessel; a partner's power debt keeps the Commander alive.
        var creditorsWorld = World(story, 6, "trickster", "trickster.ever", "anevia.committed", "anevia.trickster.cost.socoth_listening");
        check(Av(threshold, creditorsWorld), "LastCall_Offer_Creditors: a power debt does not open last orders.");
        var counted = Done(story, Program.Walk(threshold, creditorsWorld).Single(r => r.Has(Open)));
        var anevia = Sc("anevia.lastcall.call");
        check(!counted.Has(Bottle) && Av(anevia, counted), "LastCall_Offer_Creditors: Anevia's call-in is not offered once last orders are called.");
        var calledIn = Done(story, Program.Walk(anevia, counted).Single(r => r.Has("anevia.lastcall.called")));
        check(calledIn.Has(Creditors) && !Av(anevia, calledIn), "LastCall_Offer_Creditors: the live Socothbenoth does not hold the Commander up.");
        check(Program.Walk(joke, calledIn).Any(r => r.Has(Taken) && r.Has(Due)), "LastCall_Offer_Creditors: the creditors' punchline is missing.");

        // 3. LastCall_OutlivedOnly: an outlived creditor keeps nobody alive, so its ledger never opens (no soft-lock: every
        // opened ledger reaches a last joke); a live creditor beside an outlived one still opens it.
        var outlived = World(story, 6, "trickster", "trickster.ever", "anevia.committed", "anevia.trickster.cost.socoth_listening", "socot.gone");
        check(!Program.Walk(threshold, outlived).Any(r => r.Has(Open)), "LastCall_OutlivedOnly: an outlived-only ledger opens and cannot close.");
        var shadowOnly = World(story, 6, "trickster", "trickster.ever", "noct.complete", "nocticula.trickster.cost.shade_paid", "noct.dead");
        check(!Program.Walk(threshold, shadowOnly).Any(r => r.Has(Open)), "LastCall_OutlivedOnly: a shadow's debt alone opens the ledger.");
        var mixed = World(story, 6, "trickster", "trickster.ever", "anevia.committed", "anevia.trickster.cost.socoth_listening", "socot.gone",
                          "noct.complete", "nocticula.trickster.cost.shade_paid");
        var mixedOpen = Program.Walk(threshold, mixed).Where(r => r.Has(Open)).ToList();
        check(mixedOpen.Count == 1, "LastCall_OutlivedOnly: a live Nocticula beside an outlived Socothbenoth does not open exactly one way.");
        var mixedNoct = Done(story, Program.Walk(Sc("nocticula.lastcall.call"), Done(story, mixedOpen[0])).Single(r => r.Has("nocticula.lastcall.called")));
        var mixedCalled = Done(story, Program.Walk(anevia, mixedNoct).Single(r => r.Has("anevia.lastcall.called")));
        check(Program.Walk(joke, mixedCalled).Any(r => r.Has(Taken) && r.Has(Due)), "LastCall_OutlivedOnly: the live creditor cannot close the opened ledger.");
        // Every world that opens the ledger by creditors alone can reach a last joke (the soft-lock check).
        foreach (var debt in new[] { "arsinoe.trickster.cost.lien", "nurah.trickster.cost.ramisa_fee", "soana.trickster.cost.guardian_paid" })
        {
            var rel = debt.Split('.')[0];
            var commit = story.Relationships[rel].CommittedFlag;
            var w = World(story, 6, "trickster", "trickster.ever", commit, debt);
            var o = Program.Walk(threshold, w).Where(r => r.Has(Open)).Select(r => Done(story, r)).ToList();
            var called = o.SelectMany(r => Program.Walk(Sc(rel + ".lastcall.call"), r)).Where(r => r.Has(rel + ".lastcall.called")).Select(r => Done(story, r)).ToList();
            check(o.Count == 1 && called.Any(r => Program.Walk(joke, r).Any(x => x.Has(Taken))), "Soft-lock: a creditor-only ledger cannot reach its last joke: " + debt);
        }

        // 4-5. No vessel and no debt; a failed path.
        check(!Av(threshold, World(story, 6, "trickster", "trickster.ever")), "LastCall_NoVesselNoDebt: last orders without a vessel or a debt.");
        check(!Av(threshold, World(story, 6, "trickster.ever", "trickster.failed", "lastcall.flask_taken", "lastcall.flask_held")),
            "LastCall_PathFailed: last orders on a failed Trickster path.");

        // 6. LastCall_Bottle_King / _Alone: exclusive by the King's crown; each primes the bottle once.
        var withKing = World(story, 5, "trickster", "trickster.ever", "lastcall.flask_taken", "lastcall.flask_held", "fool_king.crowned");
        check(Av(king, withKing) && !Av(alone, withKing), "LastCall_Bottle_King: the King's table and the lonely night are not exclusive.");
        var kingOut = Program.Walk(king, withKing).Where(r => r.Has(Primed)).ToList();
        check(kingOut.Count == 6 && kingOut.All(r => r.Has("trickster.lastcall.king_blessed") && r.Has("trickster.lastcall.started"))
              && kingOut.Count(r => r.Has("trickster.lastcall.cost.royal_round")) == 3 && king.Nodes.SelectMany(n => n.Choices).Count(c => c.Crusade != null) == 3,
            "LastCall_Bottle_King: three jokes by round or tab, the round paid in Finances.");
        var noKing = World(story, 5, "trickster", "trickster.ever", "lastcall.flask_taken", "lastcall.flask_held");
        check(!Av(king, noKing) && Av(alone, noKing) && Rules.IsRemote(alone)
              && Program.Walk(alone, noKing).Where(r => r.Has(Primed)).All(r => r.Has("trickster.lastcall.cost.bled_alone")),
            "LastCall_Bottle_Alone: the lonely night is not the letter fallback.");
        check(!Av(king, Done(story, kingOut[0])), "LastCall_Bottle_King: the flask is filled twice.");

        // 7. LastCall_Epilogue_Matrix: each Block A page appears exactly in its world; H2 never without the bottle.
        var endings = new[] { "ending.trickster", "ending.trickster_full", "ending.trickster_allplanes", "ending.trickster_allplanes_fw", "ending.wound_closed", "ending.not_my_business" };
        foreach (var ending in endings)
        foreach (bool sacrifice in new[] { false, true })
        foreach (bool taken in new[] { false, true })
        foreach (string pillar in new[] { Bottle, Creditors })
        {
            var flags = new List<string> { "trickster.ever", pillar };
            check(story.Etudes.ContainsKey(ending) || ending == "ending.not_my_business", "LastCall_Epilogue_Matrix: an ending etude is not bound: " + ending);
            if (story.Etudes.ContainsKey(ending)) flags.Add(ending);
            if (sacrifice) flags.Add("sacrifice");
            if (taken) flags.Add(Taken);
            var w = World(story, 6, flags.ToArray());
            bool h1 = taken && ending.StartsWith("ending.trickster", StringComparison.Ordinal) && story.Etudes.ContainsKey(ending);
            bool h2 = taken && ending == "ending.wound_closed" && sacrifice && pillar == Bottle;
            bool active = h1 || h2;
            check(Av(a1, w) == h1 && Av(a1h2, w) == h2 && Av(a2, w) == (active && pillar == Bottle) && Av(a3, w) == (active && pillar == Creditors)
                  && Av(lastWord, w) == active,
                "LastCall_Epilogue_Matrix: a Block A/C page is shown out of its world (" + ending + ", sacrifice " + sacrifice + ", taken " + taken + ", " + pillar + ").");
        }

        // 8. LastCall_AllCommitted: one coda per committed partner; the canon pair plays instead of Anevia's and Irabeth's own.
        var commits = new[] { "anevia.committed", "irabeth.committed", "committed", "arsinoe.committed", "jerribeth.committed", "konomi.committed",
            "noct.complete", "vellexia.committed", "nurah.complete", "kiana.committed", "minachiv.complete", "soana.committed", "aranka.extension_kept",
            "gesmerha.committed", "seelah.committed", "targona.committed", "dorgelinda.committed", "hepzamirah.committed", "eritrice.committed",
            "areelu.committed", "chadali.committed" };
        var all = World(story, 6, new[] { "trickster.ever", Taken, "ending.trickster", "sacrifice", Bottle }.Concat(commits).ToArray());
        var shown = codas.Where(s => Av(s, all)).Select(s => s.Id).ToList();
        check(codas.Length == 21 && shown.Count == 19 && !shown.Contains("anevia.lastcall.page") && !shown.Contains("irabeth.lastcall.page")
              && shown.Contains("tirabade.lastcall.page"),
            "LastCall_AllCommitted: expected 19 codas with the pair page replacing Anevia's and Irabeth's (got " + shown.Count + ").");
        foreach (var coda in codas)
        {
            var own = World(story, 6, "trickster.ever", Taken, "ending.trickster", Bottle, coda.Requires.Last());
            check(Av(coda, own), "LastCall_AllCommitted: a coda does not play for its committed partner alone: " + coda.Id);
            var uncommitted = World(story, 6, "trickster.ever", Taken, "ending.trickster", Bottle);
            check(!Av(coda, uncommitted), "LastCall_AllCommitted: a coda plays without her commit: " + coda.Id);
        }

        // 9. LastCall_Paragraphs_Nonempty: every page has unconditional text.
        foreach (var page in pages)
            check(page.Nodes.All(n => !string.IsNullOrWhiteSpace(n.Text)), "LastCall_Paragraphs_Nonempty: an empty page: " + page.Id);

        // 11. L6 LastCall_MourningSuppressed: no epilogue that Requires sacrifice plays beside an active Last Call.
        foreach (var mourning in story.Scenes.Where(s => s.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && s.Requires.Contains("sacrifice")))
            check(mourning.Forbids.Contains(Active), "LastCall_MourningSuppressed (L6): a mourning page ignores Last Call: " + mourning.Id);
        check(Sc("nocticula.trickster.defeated.epilogue.favour").Forbids.Contains(Active), "Nocticula's favour page is not called in on her Last Call page.");

        // 12. LastCall_Fallback: never taken, nothing of Last Call plays.
        var fallback = World(story, 6, new[] { "ending.trickster", "sacrifice", "trickster.ever", Bottle }.Concat(commits).ToArray());
        check(!pages.Any(s => Av(s, fallback)), "LastCall_Fallback: a Last Call page plays although the last joke was never told.");

        // The user's rulings. No page or call-in closes, kills or returns anyone; every page is effect-free.
        var closers = story.Relationships.Values.Select(r => r.ClosedFlag).Where(f => !string.IsNullOrEmpty(f)).ToHashSet();
        var deaths = story.Relationships.Values.SelectMany(r => r.UnavailableFlags).Concat(story.Relationships.Values.SelectMany(r => r.UnavailableOverrides.Values)).ToHashSet();
        foreach (var s in framework)
        {
            var reads = s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g))
                .Concat(s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids)))
                .Concat(s.Nodes.SelectMany(n => n.Paragraphs).SelectMany(p => p.Requires.Concat(p.Forbids).Concat(p.AnyGroups.SelectMany(g => g))));
            check(!reads.Any(k => closers.Contains(k) && k != "trickster.lastcall.closed"), "G5: Last Call reads another route's closed flag: " + s.Id);
            check(s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Set).All(f => f.StartsWith("trickster.lastcall.", StringComparison.Ordinal) || f.EndsWith(".lastcall.called", StringComparison.Ordinal)
                                                                                     || f.EndsWith(".lastcall.resolved", StringComparison.Ordinal)),
                "Last Call writes a flag outside its own namespace: " + s.Id);
            if (s.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
                check(s.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0 && c.Crusade == null && c.Mythic == null && c.Alignment == null),
                    "An epilogue page carries an effect: " + s.Id);
        }
        // "At the table, apart" is a price for a concrete failure: every coda paragraph that seats her apart reads a cost flag.
        foreach (var coda in codas)
        foreach (var para in coda.Nodes.SelectMany(n => n.Paragraphs).Where(p => p.Text.Contains("far end") || p.Text.Contains("other side") || p.Text.Contains("apart")))
            check(para.Requires.Concat(para.AnyGroups.SelectMany(g => g)).Any(k => k.Contains(".cost.")), "An 'apart' paragraph is not keyed to a failure: " + coda.Id);
        // Every call-in needs her commit and a deal she made; no call-in is offered before last orders or after the joke.
        foreach (var call in calls)
            check(call.Requires.Contains(Open) && call.Forbids.Contains(Taken) && call.RequiresAnyGroups.Length == 1 && call.AnswerLists.Length == 5
                  && call.Forbids.Any(f => f.EndsWith(".lastcall.resolved", StringComparison.Ordinal))
                  && call.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Any(f => f.EndsWith(".lastcall.resolved", StringComparison.Ordinal))),
                "A call-in is not a ledger line of the open ledger, or one of its answers leaves the debt unresolved: " + call.Id);
        // Sequencing: the last joke waits until every open debt's call-in is resolved.
        var many = Done(story, World(story, 6, "trickster", "trickster.ever", Open, Primed, Bottle, "lastcall.flask_taken", "lastcall.flask_held",
                                    "arsinoe.trickster.cost.lien", "seelah.trickster.cost.keeps_it"));
        check(!Av(joke, many), "Sequencing: the last joke is offered with two debts still open.");
        var oneDone = Done(story, Program.Walk(Sc("arsinoe.lastcall.call"), many).Single(r => r.Has("arsinoe.lastcall.called")));
        check(!Av(joke, oneDone), "Sequencing: the last joke is offered with one debt still open.");
        var allDone = Done(story, Program.Walk(Sc("seelah.lastcall.call"), oneDone).Single(r => r.Has("seelah.lastcall.called")));
        check(Av(joke, allDone), "Sequencing: the last joke stays closed after every debt is resolved.");
        // A mortal creditor collects but keeps nobody alive: Sunhammer alone never opens the creditors branch.
        var mortalOnly = World(story, 6, "trickster", "trickster.ever", "kiana.committed", "kiana.trickster.cost.sunhammer_favour");
        check(!Program.Walk(threshold, mortalOnly).Any(r => r.Has(Open)), "A mortal jeweller's debt holds back the Wound.");
        // Targona: keeping the promise is a real choice; breaking it is the failure that seats her apart.
        var targona = Sc("targona.lastcall.call");
        var sealedWorld = Done(story, World(story, 6, "trickster", "trickster.ever", Open, "targona.committed", "targona.trickster.cost.light_sealed"));
        var targonaOut = Program.Walk(targona, sealedWorld);
        check(targonaOut.Count == 2 && targonaOut.Count(r => r.Has("targona.lastcall.called")) == 1, "Targona's promise is not a choice at the rift.");

        // E15, the Ledger: debts open when made, settle when called in or at the end; the journal step is give-then-complete.
        var ledger = story.Relationships["lastcall"];
        check(ledger.JournalEntries.Count >= 20 && ledger.Title == "The Trickster's Ledger", "The Trickster's Ledger has no Debts lines.");
        var socoth = ledger.JournalEntries.Single(e => e.Id == "debt.socoth");
        var none = World(story, 5, "trickster.ever");
        var owed = World(story, 5, "trickster.ever", "anevia.trickster.cost.socoth_listening");
        var paid = World(story, 6, "trickster.ever", "anevia.trickster.cost.socoth_listening", "anevia.lastcall.called");
        check(Rules.JournalStep(socoth, false, false, none) == null && Rules.JournalStep(socoth, false, false, owed) == "give"
              && Rules.JournalStep(socoth, true, true, owed) == null && Rules.JournalStep(socoth, true, true, paid) == "complete"
              && Rules.JournalStep(socoth, true, false, paid) == null,
            "E15: a Ledger line is not given when the debt appears and completed when it is called in.");
        var authored = story.Scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).ToHashSet();
        foreach (var entry in ledger.JournalEntries)
            check(entry.OpenWhen.SelectMany(g => g).All(authored.Contains), "A Ledger line opens on a flag nothing sets: " + entry.Id);
    }
}
