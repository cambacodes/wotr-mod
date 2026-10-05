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
    private const string Bottle = "trickster.lastcall.pillar.bottle", Creditors = "trickster.lastcall.creditors_called";
    private const string Heroic = "trickster.lastcall.heroic", Bottled = "trickster.lastcall.cost.bottled";
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
        // Derived keys are recomputed from scratch each time the runtime builds its state (engine-q2: a resolved debt's
        // callable guard must drop, and Complete only adds keys).
        next.Flags.ExceptWith(story.Derived.Keys);
        Rules.Complete(story, next);
        return next;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        // eng8-q8g: production availability, selected history and enacted receipts.
        LastCallHistoryInventoryTests.Run(story, check);
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

        // 2-3. The flask is the only survival device (a prepared countermeasure, never a list of debts). Without a vessel
        // last orders are never offered, whatever is owed; powers only collect.
        foreach (var debtWorld in new[] { new[] { "anevia.committed", "anevia.trickster.cost.socoth_listening" },
                                          new[] { "arsinoe.committed", "arsinoe.trickster.cost.lien" },
                                          new[] { "kiana.committed", "kiana.trickster.cost.sunhammer_favour" } })
            check(!Av(threshold, World(story, 6, new[] { "trickster", "trickster.ever" }.Concat(debtWorld).ToArray())),
                "LastCall_NoShield: a debt without the flask opens last orders: " + debtWorld[1]);
        var owing = Done(story, World(story, 6, "trickster", "trickster.ever", Open, Primed, Bottle, "lastcall.flask_taken", "lastcall.flask_held",
                                      "anevia.committed", "anevia.trickster.cost.socoth_listening"));
        var anevia = Sc("anevia.lastcall.call");
        var calledIn = Done(story, Program.Walk(anevia, owing).Single(r => r.Has("anevia.lastcall.called")));
        check(calledIn.Has(Creditors) && !Av(anevia, calledIn), "LastCall_Collectors: a live Socothbenoth's call-in does not mark the collectors.");
        var gone = Done(story, World(story, 6, "trickster", "trickster.ever", Open, Primed, Bottle, "lastcall.flask_taken", "lastcall.flask_held",
                                     "anevia.committed", "anevia.trickster.cost.socoth_listening", "socot.gone"));
        var goneCalled = Done(story, Program.Walk(anevia, gone).Single(r => r.Has("anevia.lastcall.resolved")));
        check(!goneCalled.Has(Creditors), "LastCall_Collectors: an outlived Socothbenoth still collects.");

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
            var flags = new List<string> { "trickster.ever", Bottle, pillar };
            check(story.Etudes.ContainsKey(ending) || ending == "ending.not_my_business", "LastCall_Epilogue_Matrix: an ending etude is not bound: " + ending);
            if (story.Etudes.ContainsKey(ending)) flags.Add(ending);
            if (sacrifice) flags.Add("sacrifice");
            if (taken) flags.Add(Taken);
            var w = World(story, 6, flags.ToArray());
            bool h1 = taken && ending.StartsWith("ending.trickster", StringComparison.Ordinal) && story.Etudes.ContainsKey(ending);
            bool h2 = taken && ending == "ending.wound_closed" && sacrifice;
            bool active = h1 || h2;
            check(Av(a1, w) == h1 && Av(a1h2, w) == h2 && Av(a2, w) == active && Av(a3, w) == (active && pillar == Creditors)
                  && Av(lastWord, w) == active,
                "LastCall_Epilogue_Matrix: a Block A/C page is shown out of its world (" + ending + ", sacrifice " + sacrifice + ", taken " + taken + ", " + pillar + ").");
        }

        // 8. LastCall_AllCommitted: one coda per committed partner; the canon pair plays instead of Anevia's and Irabeth's own.
        var commits = new[] { "anevia.committed", "irabeth.committed", "committed", "arsinoe.committed", "jerribeth.committed", "konomi.committed",
            "noct.complete", "vellexia.committed", "devarra.committed", "nurah.complete", "nurah.ran_off" /* her coda needs a living Nurah */, "kiana.committed", "minachiv.complete", "soana.committed", "aranka.extension_kept",
            "gesmerha.committed", "seelah.committed", "targona.committed", "dorgelinda.committed", "hepzamirah.committed", "eritrice.committed",
            "areelu.committed", "chadali.committed", "camellia.committed", "arueshalae.committed", "delamere.committed", "nidalynn.committed", "shamira.committed", "jannah.committed", "nenio.committed", "herrax.committed", "terendelev.committed", "eliandra.committed", "galfrey.committed", "horzalah.committed", "elyanka.committed", "melazmera.committed", "yaniel.committed", "wenduag.committed", "iomedae.committed", "mielarah.committed" };
        var all = World(story, 6, new[] { "trickster.ever", Taken, "ending.trickster", "sacrifice", Bottle }.Concat(commits).ToArray());
        var shown = codas.Where(s => Av(s, all)).Select(s => s.Id).ToList();
        check(codas.Length == 40 && shown.Count == 38 && !shown.Contains("anevia.lastcall.page") && !shown.Contains("irabeth.lastcall.page")
              && shown.Contains("tirabade.lastcall.page"),
            "LastCall_AllCommitted: expected 38 shown codas with the pair page replacing Anevia's and Irabeth's (got " + shown.Count + ").");
        foreach (var coda in codas)
        {
            var own = World(story, 6, "trickster.ever", Taken, "ending.trickster", Bottle, coda.RequiresAnyGroups.Length > 0 ? coda.RequiresAnyGroups[0][0] : coda.Requires.Last());
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
            // Exception (coordinator ruling 2026-10-02, Aranka polish item 3): her coda forbids her own closed route explicitly.
            // Engine-q2 item 3: a call-in reads her route's closure only through its own <rel>.lastcall.callable guard
            // (Derived + DerivedOpenRoutes [her route] = Rules.RouteOpen), never a closed, death or return flag directly.
            check(!reads.Any(k => closers.Contains(k) && k != "trickster.lastcall.closed"
                                  && !(s.Id == "aranka.lastcall.page" && k == "aranka.extension_closed")), "G5: Last Call reads another route's closed flag: " + s.Id);
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
        // Every call-in needs a deal she made and her route open; no call-in is offered before last orders or after the joke.
        foreach (var call in calls)
        {
            string rel = call.Id.Substring(0, call.Id.Length - ".lastcall.call".Length), due = rel + ".lastcall.callable";
            // eng7-l13: stakes stay exact; Nenio control and Wenduag partnership are mandatory extra readers.
            string? eligibility = rel == "nenio" ? "nenio.outcome.eligible" : rel == "wenduag" ? "wenduag.trickster.partner" : null;
            check(call.Requires.Contains(due) && story.DerivedOpenRoutes.TryGetValue(due, out var routes) && routes.SequenceEqual(new[] { rel })
                  && story.DerivedForbids.TryGetValue(due, out var settled) && settled.First() == rel + ".lastcall.resolved"
                  && (eligibility == null || story.Derived[due].All(g => g.Contains(eligibility)))
                  && story.Derived[due].Select(g => g.Where(k => k != eligibility).Single()).OrderBy(k => k).SequenceEqual(call.RequiresAnyGroups.Single().OrderBy(k => k))
                  && joke.Forbids.Contains(due) && jokeAreelu.Forbids.Contains(due),
                "Engine-q2: a call-in is not guarded by its partner's open route, or the last joke does not wait on it: " + call.Id);
            check(call.Requires.Contains(Open) && call.Forbids.Contains(Taken) && call.RequiresAnyGroups.Length == 1 && call.AnswerLists.Length == 5
                  && call.Forbids.Any(f => f.EndsWith(".lastcall.resolved", StringComparison.Ordinal))
                  // eng8-q8g: intermediate answers reach the creditor's terms;
                  // every terminal still resolves the spoken or refused debt.
                  && call.Nodes.SelectMany(n => n.Choices).Where(c => c.Next == null).All(c => c.Set.Any(f => f.EndsWith(".lastcall.resolved", StringComparison.Ordinal))),
                "A call-in is not a ledger line of the open ledger, or one of its answers leaves the debt unresolved: " + call.Id);
        }
        // Engine-q2 item 3: a closed or departed partner's call-in is not offered and does not strand the last joke; her
        // Trickster return reopens it; a resolved debt no longer holds the joke.
        var ready = new[] { "trickster", "trickster.ever", Open, Primed, Bottle, "lastcall.flask_taken", "lastcall.flask_held",
                            "anevia.committed", "anevia.trickster.cost.socoth_listening" };
        var aneviaCall = Sc("anevia.lastcall.call");
        foreach (var (what, extra, offered) in new (string, string[], bool)[] {
            ("open", new string[0], true), ("closed", new[] { "anevia.closed" }, false), ("departed", new[] { "anevia_gone" }, false),
            ("departed and returned", new[] { "anevia_gone", "anevia.trickster.returned" }, true), ("dead", new[] { "anevia_dead" }, false),
            ("resolved", new[] { "anevia.lastcall.resolved" }, false) })
        {
            var w = Done(story, World(story, 6, ready.Concat(extra).ToArray()));
            check(Av(aneviaCall, w) == offered, "Engine-q2: Anevia's call-in, " + what + ": offered " + !offered + ".");
            check(Av(joke, w) == !offered, "Engine-q2: the last joke, Anevia " + what + ": " + (offered ? "offered over an open debt" : "stranded by a debt nobody can call in") + ".");
        }
        // Engine-q2 item 3 (scope extension): every Last Call scene that names a partner (a coda or a call-in) carries her
        // central route guard, <rel>.lastcall.route_open or <rel>.lastcall.callable: a Derived key whose DerivedOpenRoutes is
        // exactly her route (Rules.RouteOpen), so her closure, death or departure hides it and her earned return shows it.
        foreach (var s in framework.Where(s => !s.Id.StartsWith("trickster.", StringComparison.Ordinal)))
        {
            var guards = s.Requires.Where(k => k.EndsWith(".lastcall.route_open", StringComparison.Ordinal) || k.EndsWith(".lastcall.callable", StringComparison.Ordinal)).ToArray();
            check(guards.Length == 1 && story.DerivedOpenRoutes.TryGetValue(guards[0], out var guardRoutes) && guardRoutes.Length == 1
                  && story.Relationships.ContainsKey(guardRoutes[0]) && guards[0].StartsWith(guardRoutes[0] + ".lastcall.", StringComparison.Ordinal),
                "Engine-q2: a Last Call scene naming a partner is not gated on her open route: " + s.Id);
        }
        var targonaPage = Sc("targona.lastcall.page");
        foreach (var (what, extra, plays) in new (string, string[], bool)[] {
            ("committed", new string[0], true), ("closed courtship, stale late commitment", new[] { "targona.closed", "targona.trickster.late_committed" }, false),
            ("dead in the laboratory", new[] { "targona.dead_lab" }, false),
            ("dead, then returned", new[] { "targona.dead_lab", "targona.trickster.returned" }, true) })
            check(Av(targonaPage, World(story, 6, new[] { "trickster", "trickster.ever", Active, "targona.committed" }.Concat(extra).ToArray())) == plays,
                "Engine-q2: Targona's Last Call coda, " + what + ": plays " + !plays + ".");
        // Sequencing: the last joke waits until every open debt's call-in is resolved.
        var many = Done(story, World(story, 6, "trickster", "trickster.ever", Open, Primed, Bottle, "lastcall.flask_taken", "lastcall.flask_held",
                                    "arsinoe.trickster.cost.lien", "seelah.trickster.cost.keeps_it"));
        check(!Av(joke, many), "Sequencing: the last joke is offered with two debts still open.");
        var oneDone = Done(story, Program.Walk(Sc("arsinoe.lastcall.call"), many).Single(r => r.Has("arsinoe.lastcall.called")));
        check(!Av(joke, oneDone), "Sequencing: the last joke is offered with one debt still open.");
        var allDone = Done(story, Program.Walk(Sc("seelah.lastcall.call"), oneDone).Single(r => r.Has("seelah.lastcall.called")));
        check(Av(joke, allDone), "Sequencing: the last joke stays closed after every debt is resolved.");
        // A mortal creditor collects but keeps nobody alive: Sunhammer alone never opens the creditors branch.
        // A mortal creditor collects but is no power: Sunhammer's call-in never marks the collectors' page.
        var mortal = Done(story, World(story, 6, "trickster", "trickster.ever", Open, Primed, Bottle, "lastcall.flask_taken", "lastcall.flask_held",
                                       "kiana.committed", "kiana.trickster.cost.sunhammer_favour"));
        check(Program.Walk(Sc("kiana.lastcall.call"), mortal).All(r => !r.Has(Creditors)), "A mortal jeweller is counted among the powers.");
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
        // eng7-l13: NAME_GONE is an earned Derived stake, validated against its live producers.
        authored.UnionWith(story.Derived.Keys);
        foreach (var entry in ledger.JournalEntries)
            check(entry.OpenWhen.SelectMany(g => g).All(authored.Contains), "A Ledger line opens on a flag nothing sets: " + entry.Id);
        CheckNoStranding(story, check); // eng8-q8g: also callable by the focused gate.
        var devarraCall = Sc("devarra.lastcall.call");
        var refusedBill = new Snapshot { Chapter = 6 }; refusedBill.Flags.UnionWith(new[] { "devarra.trickster.cost.egg_withheld", "devarra.trickster.refused" });
        check(devarraCall.Nodes[0].Choices.Count(ch => Rules.Match(ch.Requires, ch.Forbids, refusedBill)) == 1
              && devarraCall.Nodes[0].Choices.Single(ch => Rules.Match(ch.Requires, ch.Forbids, refusedBill)).Set.SequenceEqual(new[] { "devarra.lastcall.resolved" }),
            "Devarra's refused bill still soft-locks the last joke, or her call-in is spoken anyway.");
    }

    // eng8-q8g: every offered call world must have a resolving terminal path.
    internal static void CheckNoStranding(Story story, Action<bool, string> check)
    {
        // NM1 (ideal-run C14): no call-in can strand the last joke. In every combination of the flags its choices read, some
        // choice is selectable and resolves the debt (Devarra's refused bill used to leave none).
        foreach (var callIn in story.Scenes.Where(s => s.Id.EndsWith(".lastcall.call", StringComparison.Ordinal)))
        {
            bool reviewed = new[] { "kiana.lastcall.call", "eliandra.lastcall.call", "wenduag.lastcall.call" }.Contains(callIn.Id);
            var choices = reviewed ? callIn.Nodes.SelectMany(n => n.Choices) : callIn.Nodes[0].Choices;
            var keys = choices.SelectMany(ch => ch.Requires.Concat(ch.Forbids)).Concat(callIn.RequiresAnyGroups.SelectMany(g => g)).Distinct().ToArray();
            check(keys.Length <= 14, "A call-in reads too many flags to enumerate: " + callIn.Id);
            string resolvedFlag = callIn.Id.Replace(".lastcall.call", ".lastcall.resolved");
            int offeredWorlds = 0;
            for (int mask = 0; mask < 1 << keys.Length; mask++)
            {
                var held = new Snapshot { Chapter = 6 };
                for (int i = 0; i < keys.Length; i++) if ((mask & (1 << i)) != 0) held.Flags.Add(keys[i]);
                if (reviewed)
                {
                    // E11's matrix uses real eligibility inputs; producer proof is separate.
                    held.Flags.UnionWith(callIn.Requires.Where(f => !story.Derived.ContainsKey(f)));
                    if (callIn.Id == "wenduag.lastcall.call") held.Flags.Add("wenduag.committed");
                    if (held.Has("kiana.lastcall.guests_recovered")) held.Flags.Add("seelah.souls_returned");
                    held.Flags.ExceptWith(story.Derived.Keys);
                    Rules.Complete(story, held);
                }
                // Only the worlds where the call-in itself is offered (a deal held, nothing it forbids).
                if (!callIn.RequiresAnyGroups.All(g => g.Any(held.Has)) || callIn.Forbids.Any(held.Has) || !callIn.Requires.All(held.Has)) continue;
                // eng8-q8g: follow the real selectable graph, including pardon/refusal.
                offeredWorlds++;
                var ends = Program.Walk(callIn, held);
                check(ends.Count > 0 && ends.All(end => end.Has(resolvedFlag)),
                    "A call-in strands the last joke (no resolving choice) for " + callIn.Id + " with {" + string.Join(", ", held.Flags) + "}");
            }
            if (reviewed) check(offeredWorlds > 0, "No-stranding matrix executed no offered worlds: " + callIn.Id);
        }
    }
    // end eng8-q8g
}
