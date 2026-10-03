using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// The household (08-TRICKSTER-HOUSEHOLD.md, 10-HAREM-RESIDENCE.md P1): the Table's door on Thaberdine's list (the offer and
// the native openers), the Table menu's entries, <rel>.harem.eligible, the Ledger's Guest List / Seating Notes / Secrets
// visibility, the Word Made True counter, and the invitation kind. System only: no pair scene exists yet.
internal static class HouseholdTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string KingC3 = "1a17d8053a3be7f47a7908eb6706f2fe";
    private const string KingC5 = "6dccfd39947ef4242a8afbe36b21a46c";
    private const string Kept = "household.table.kept";

    private static Snapshot State(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 1000 };
        foreach (var flag in flags) state.Flags.Add(flag);
        Rules.Complete(story, state);
        return state;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        string Committed(string rel) => story.Relationships[rel].CommittedFlag;

        // Eligibility: one Derived key per romance route, from its committed state (or its late commitment); the friendship
        // routes and the frameworks have none. any_eligible opens the King's offer.
        var partners = story.Derived.Keys.Where(k => k.EndsWith(".harem.eligible", StringComparison.Ordinal))
            .Select(k => k.Substring(0, k.Length - ".harem.eligible".Length)).ToList();
        check(partners.Count == 41 && !partners.Contains("ember") && !partners.Contains("aivu") && !partners.Contains("lastcall")
            && !partners.Contains("household"), "Household eligibility is not exactly the 41 romance routes: " + string.Join(",", partners));
        check(partners.All(rel => story.Derived[rel + ".harem.eligible"].Any(g => g.Length == 1 && g[0] == Committed(rel))),
            "A partner's eligibility does not follow her committed flag.");
        var none = State(story, 3, "trickster");
        check(!none.Has("household.any_eligible") && partners.All(rel => !none.Has(rel + ".harem.eligible")), "Eligibility holds with nobody committed.");
        var seelah = State(story, 3, "trickster", Committed("seelah"));
        check(seelah.Has("seelah.harem.eligible") && seelah.Has("household.any_eligible") && !seelah.Has("camellia.harem.eligible"),
            "Seelah's commitment does not make her (alone) eligible.");
        check(State(story, 3, "noct.acq.renewed_agreement").Has("nocticula.harem.eligible"), "Nocticula's acquired harbour is not eligible.");
        check(State(story, 3, "minachiv.complete").Has("minagho_chivarro.harem.eligible"), "The canon pair is not eligible from minachiv.complete.");
        check(State(story, 3, "committed").Has("tirabade.harem.eligible"), "Anevia and Irabeth together are not eligible from 'committed'.");
        if (story.Derived.ContainsKey("aranka.trickster.late_committed"))
            check(story.Derived["aranka.harem.eligible"].Any(g => g.Length == 1 && g[0] == "aranka.trickster.late_committed"),
                "Aranka's late commitment does not make her eligible.");
        // Closed routes leave the household (E4b, Story.DerivedOpenRoutes): eligibility also needs her route open, read from her
        // own relationship data. Her ClosedFlag (a refusal, a breakup, a parting) or one of her UnavailableFlags (death,
        // dismissal, departure) withdraws it; a Trickster return in her UnavailableOverrides restores it.
        check(partners.All(rel => story.DerivedOpenRoutes.TryGetValue(rel + ".harem.eligible", out var routes) && routes.SequenceEqual(new[] { rel })),
            "A partner's eligibility is not guarded by her own route.");
        var stillOpen = partners.Where(rel => State(story, 3, "trickster", Committed(rel), story.Relationships[rel].ClosedFlag).Has(rel + ".harem.eligible")).ToList();
        check(stillOpen.Count == 0, "A partner whose route is closed is still eligible: " + string.Join(",", stillOpen));
        var badReturn = partners.Where(rel => !story.Relationships[rel].UnavailableFlags.All(flag =>
                !State(story, 3, "trickster", Committed(rel), flag).Has(rel + ".harem.eligible")
                && (!story.Relationships[rel].UnavailableOverrides.TryGetValue(flag, out var back)
                    || State(story, 3, "trickster", Committed(rel), flag, back).Has(rel + ".harem.eligible")))).ToList();
        check(badReturn.Count == 0, "An unavailable state does not withdraw eligibility, or its return does not restore it: " + string.Join(",", badReturn));
        // Arsinoe: the yes, then the goodbye (the Arsinoe polish finding).
        var arsinoeYes = State(story, 3, "trickster", "trickster.ever", "arsinoe.committed");
        var arsinoeBye = State(story, 3, "trickster", "trickster.ever", "arsinoe.committed", "arsinoe.closed", "arsinoe.parted", "arsinoe.future_spoken");
        check(arsinoeYes.Has("arsinoe.harem.eligible") && !arsinoeBye.Has("arsinoe.harem.eligible") && !arsinoeBye.Has("household.any_eligible"),
            "Arsinoe stays a household partner after saying goodbye.");
        if (story.Derived.ContainsKey("arsinoe.trickster.late_committed"))
        {
            var late = story.Derived["arsinoe.trickster.late_committed"].First();
            check(State(story, 3, late.Concat(new[] { "trickster" }).ToArray()).Has("arsinoe.harem.eligible")
                && !State(story, 3, late.Concat(new[] { "trickster", "arsinoe.closed", "arsinoe.parted" }).ToArray()).Has("arsinoe.harem.eligible"),
                "Arsinoe's late yes survives her closed route.");
        }
        // Seelah: parted (seelah.parted beside seelah.closed) leaves; dead or gone leaves; her Trickster return restores her.
        check(!State(story, 3, "trickster", "seelah.committed", "seelah.closed", "seelah.parted").Has("seelah.harem.eligible")
            && !State(story, 3, "trickster", "seelah.committed", "seelah_dead").Has("seelah.harem.eligible")
            && State(story, 3, "trickster", "seelah.committed", "seelah_dead", "seelah.trickster.returned").Has("seelah.harem.eligible")
            && !State(story, 3, "trickster", "seelah.committed", "seelah_gone").Has("seelah.harem.eligible")
            && State(story, 3, "trickster", "seelah.committed", "seelah_gone", "seelah.trickster.returned").Has("seelah.harem.eligible"),
            "Seelah's parting, death or return does not move her household eligibility.");
        // Anevia: a refusal closes her; gone leaves her until the Trickster brings her back; dead (no return) stays out.
        check(!State(story, 3, "trickster", "anevia.committed", "anevia.closed", "anevia.local_declined").Has("anevia.harem.eligible")
            && !State(story, 3, "trickster", "anevia.committed", "anevia_gone").Has("anevia.harem.eligible")
            && State(story, 3, "trickster", "anevia.committed", "anevia_gone", "anevia.trickster.returned").Has("anevia.harem.eligible")
            && !State(story, 3, "trickster", "anevia.committed", "anevia_dead", "anevia.trickster.returned").Has("anevia.harem.eligible"),
            "Anevia's refusal, departure or return does not move her household eligibility.");
        // Soana (a return device): dead leaves, returned restores; returned but refused (soana.closed) leaves again.
        check(!State(story, 3, "trickster", "soana.committed", "soana.dead").Has("soana.harem.eligible")
            && State(story, 3, "trickster", "soana.committed", "soana.dead", "soana.trickster.returned").Has("soana.harem.eligible")
            && State(story, 3, "trickster", "trickster.ever", "soana.dead", "soana.trickster.returned").Has("soana.harem.eligible")
            && !State(story, 3, "trickster", "trickster.ever", "soana.dead", "soana.trickster.returned", "soana.closed", "soana.trickster.refused").Has("soana.harem.eligible"),
            "Soana's death, return or refusal does not move her household eligibility.");
        // Terendelev (a return device): her commitment holds; sending her home (terendelev.closed) ends it.
        check(State(story, 3, "trickster", "terendelev.committed").Has("terendelev.harem.eligible")
            && !State(story, 3, "trickster", "terendelev.committed", "terendelev.closed", "terendelev.trickster.guardian").Has("terendelev.harem.eligible"),
            "Terendelev stays a household partner after her route closes.");
        // The Guest List follows: a parted woman has no chair.
        var seelahParted = State(story, 3, "trickster", "seelah.committed", "seelah.closed", "seelah.parted");
        check(!Rules.BookVisible(story.Books["trickster.ledger"], seelahParted).Any(e => e.Id == "guest.seelah"), "A parted partner keeps her Guest List chair.");
        bool Guest(string rel, params string[] flags) =>
            Rules.BookVisible(story.Books["trickster.ledger"], State(story, 3, new[] { "trickster", "trickster.ever" }.Concat(flags).ToArray())).Any(e => e.Id == "guest." + rel);
        // Every guest entry reads the guarded key, so the open-route guard reaches the Guest List for every partner.
        check(story.Books["trickster.ledger"].Entries.Where(e => e.Section == "Guest List").All(e => e.Requires.SequenceEqual(new[] { e.Id.Substring(6) + ".harem.eligible" })),
            "A Guest List entry is not gated by its partner's guarded eligibility.");
        // Shamira (COX audit): closed hides, killed hides, her earned return shows her again.
        check(Guest("shamira", "shamira.committed") && !Guest("shamira", "shamira.committed", "shamira.closed")
            && !Guest("shamira", "shamira.committed", "shamira.killed") && Guest("shamira", "shamira.committed", "shamira.killed", "shamira.trickster.returned")
            && !Guest("shamira", "shamira.committed", "shamira.killed", "shamira.trickster.returned", "shamira.closed", "shamira.trickster.cost.kept_captive"),
            "Shamira's Guest List chair ignores her closed route, her death or her return.");
        // Nenio (COX audit): closed hides, dead hides, returned shows; dissolved has no return and stays hidden.
        check(Guest("nenio", "nenio.committed") && !Guest("nenio", "nenio.committed", "nenio.closed")
            && !Guest("nenio", "nenio.committed", "nenio.dead") && Guest("nenio", "nenio.committed", "nenio.dead", "nenio.trickster.returned")
            && !Guest("nenio", "nenio.committed", "nenio.dissolved", "nenio.trickster.returned"),
            "Nenio's Guest List chair ignores her closed route, her death or her return.");
        // Engine contract (E4b): a guard only withholds; a Derived closure input settles first; a missing input propagates.
        var guarded = new Story();
        guarded.Relationships["r"] = new Relationship { ClosedFlag = "r.closed", CommittedFlag = "r.c", UnavailableFlags = new[] { "r.dead" },
            UnavailableOverrides = new Dictionary<string, string> { ["r.dead"] = "r.back" } };
        guarded.Derived["r.ok"] = new[] { new[] { "r.c" } };
        guarded.Derived["r.dead"] = new[] { new[] { "r.killed" } };
        guarded.DerivedOpenRoutes["r.ok"] = new[] { "r" };
        check(!State(guarded, 3).Has("r.ok") && State(guarded, 3, "r.c").Has("r.ok") && !State(guarded, 3, "r.c", "r.killed").Has("r.ok")
            && State(guarded, 3, "r.c", "r.killed", "r.back").Has("r.ok") && !State(guarded, 3, "r.c", "r.closed").Has("r.ok"),
            "DerivedOpenRoutes does not withhold a key on a closed or blocked route, or does not honour the return.");
        var missing = new HashSet<string> { "r.killed" };
        Rules.PropagateMissing(guarded, missing);
        check(missing.Contains("r.ok"), "A guarded key does not inherit a missing closure input.");

        // Stance, enmity and joined-late flags are reserved: nothing in this pass sets them.
        var setters = story.Scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).ToList();
        check(!setters.Any(f => f.Contains(".harem.stance.") || f.Contains(".harem.enmity.") || f.EndsWith(".harem.joined_late", StringComparison.Ordinal)),
            "A reserved stance flag is set by a scene.");

        // The offer: Thaberdine, inline on his own Chapter 3 / Chapter 5 list, once someone is eligible, until it is kept.
        var offered = story.Scenes.Single(s => s.Id == "household.table.offered");
        var offeredC5 = story.Scenes.Single(s => s.Id == "household.table.offered_c5");
        check(offered.AnswerLists.SequenceEqual(new[] { KingC3 }) && offeredC5.AnswerLists.SequenceEqual(new[] { KingC5 })
            && offered.NativeReturnCue != null && offeredC5.NativeReturnCue != null && offered.ContactUnit == null
            && offered.Nodes.All(n => n.Speaker == "conversant"), "The table offer is not Thaberdine's, inline on his tavern lists.");
        check(Rules.EntryTargets(offered).SequenceEqual(new[] { KingC3 }), "The Chapter 3 offer does not attach to AnswersList_0009.");
        check(!Rules.Available(story, offered, none), "The table is offered with nobody eligible.");
        check(Rules.Available(story, offered, seelah), "The table is not offered once a partner is eligible.");
        check(!Rules.Available(story, offered, State(story, 3, "trickster", Committed("seelah"), Kept)), "The table is offered again once kept.");
        check(!Rules.Available(story, offered, State(story, 3, Committed("seelah"))), "The table is offered off the Trickster path.");
        check(!Rules.Available(story, offeredC5, State(story, 3, "trickster", Committed("seelah"))), "The Chapter 5 offer shows in Chapter 3.");
        check(Rules.Available(story, offeredC5, State(story, 5, "trickster", Committed("seelah"))), "The Chapter 5 offer is missing.");
        check(!Rules.Available(story, offeredC5, State(story, 5, "trickster", Committed("seelah"), "fool_king.gone")), "The offer outlives the King.");
        check(offered.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains(Kept)), "Accepting the table does not keep it.");

        // The door: "[The corner table]" on both tavern states, once kept, in its own chapters.
        var openers = story.Openers.Where(o => o.Relationship == "household").ToList();
        check(openers.Count == 2 && openers.All(o => o.Text == "[The corner table]" && o.View == "table")
            && openers.Select(o => o.AnswerList).OrderBy(x => x).SequenceEqual(new[] { KingC3, KingC5 }.OrderBy(x => x)),
            "The Table's openers are not '[The corner table]' on AnswersList_0009 and AnswersList_0054.");
        var c3 = openers.Single(o => o.AnswerList == KingC3);
        var c5 = openers.Single(o => o.AnswerList == KingC5);
        check(!Rules.OpenerShown(c3, seelah), "The corner table shows before the table is kept.");
        check(Rules.OpenerShown(c3, State(story, 3, "trickster", Kept)) && !Rules.OpenerShown(c5, State(story, 3, "trickster", Kept)),
            "The Chapter 3 door is wrong.");
        check(Rules.OpenerShown(c5, State(story, 5, "trickster", Kept)) && !Rules.OpenerShown(c3, State(story, 5, "trickster", Kept)),
            "The Chapter 5 door is wrong.");
        check(!Rules.OpenerShown(c3, State(story, 3, Kept)), "The corner table shows off the Trickster path.");

        // The menu: table scenes only (physical, no unit, no list), those available now, in authored order, six to a page.
        check(Rules.TablePerPage == 6 && Rules.TableHub == "household.table", "The Table menu contract changed.");
        check(story.Scenes.Where(s => s.InteractionHub == Rules.TableHub).All(Rules.IsTableScene), "A built Table scene is malformed.");
        var menu = new Story { Relationships = story.Relationships, Derived = story.Derived };
        Scene Entry(string id, params string[] requires) => new Scene
        {
            Id = id, Title = id, Owner = "Seelah", Relationship = "household", Entry = "[" + id + "]", InteractionHub = Rules.TableHub,
            MinChapter = 3, MaxChapter = 5, Chapters = new[] { 3, 5 }, Areas = new[] { Drezen }, Requires = requires,
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } }
        };
        for (int i = 0; i < 8; i++) menu.Scenes.Add(Entry("t" + i, "trickster", Kept, "trigger." + i));
        var remote = Entry("t.remote", "trickster");
        remote.Remote = true;
        var unit = Entry("t.unit", "trickster");
        unit.ContactUnit = "b803d86a3c2483f44b20c0ecc81893f4";
        menu.Scenes.AddRange(new[] { remote, unit });
        check(!Rules.IsTableScene(remote) && !Rules.IsTableScene(unit), "A remote or unit scene counts as a Table scene.");
        var all = Enumerable.Range(0, 8).Select(i => "trigger." + i).Concat(new[] { "trickster", Kept }).ToArray();
        var entries = Rules.TableEntries(menu, State(menu, 3, all)).Select(s => s.Id).ToList();
        check(entries.SequenceEqual(Enumerable.Range(0, 8).Select(i => "t" + i)), "The Table menu is not the ready entries in order: " + string.Join(",", entries));
        check(Rules.PageCount(entries.Count, Rules.TablePerPage) == 2 && Rules.PageSlice(entries, 1, Rules.TablePerPage).SequenceEqual(new[] { "t6", "t7" }),
            "The Table menu does not page six at a time.");
        check(Rules.TableEntries(menu, State(menu, 3, "trickster", Kept, "trigger.2")).Select(s => s.Id).SequenceEqual(new[] { "t2" }),
            "The Table menu lists an entry whose trigger has not fired.");
        var played = State(menu, 3, all.Concat(new[] { "t0" }).ToArray());
        check(!Rules.TableEntries(menu, played).Any(s => s.Id == "t0"), "A played Table scene is offered again.");
        var elsewhere = State(menu, 3, all);
        elsewhere.Area = "somewhere";
        check(Rules.TableEntries(menu, elsewhere).Count == 0 && Rules.TableEntries(menu, State(menu, 4, all)).Count == 0,
            "The Table menu lists entries outside the tavern's chapters or the capital.");

        // The Ledger: Guest List (a line per stance), Seating Notes (both women eligible), Secrets (only with the flag).
        var ledger = story.Books["trickster.ledger"];
        check(new[] { "Guest List", "Seating Notes", "Secrets" }.All(ledger.Sections.Contains), "The Ledger lacks a household section.");
        List<string> Lines(string id, Snapshot state) =>
            ledger.Entries.Single(e => e.Id == id).Lines.Where(p => Rules.ParagraphVisible(p, state)).Select(p => p.Text).ToList();
        bool Visible(string id, Snapshot state) => Rules.BookVisible(ledger, state).Any(e => e.Id == id);
        check(ledger.Entries.Count(e => e.Section == "Guest List") == 41, "The Guest List does not have one entry per partner.");
        check(!Visible("guest.seelah", none) && Visible("guest.seelah", seelah), "A Guest List entry does not follow eligibility.");
        check(Lines("guest.seelah", seelah).SequenceEqual(new[] { "{n}Not yet at the table.{/n}" }), "An unstanced guest is not 'not yet at the table'.");
        check(Lines("guest.seelah", State(story, 3, Committed("seelah"), "seelah.harem.stance.joined")).SequenceEqual(new[] { "{n}At the table.{/n}" }),
            "A joined guest is not 'at the table'.");
        check(Lines("guest.seelah", State(story, 3, Committed("seelah"), "seelah.harem.stance.joined", "seelah.harem.joined_late")).Single().Contains("late"),
            "A late joiner is not marked late.");
        var apart = Lines("guest.seelah", State(story, 3, Committed("seelah"), "seelah.harem.stance.tolerated", "seelah.harem.enmity.camellia"));
        check(apart.Count == 2 && apart[0].Contains("RRT_AtTheTableApart") && apart[1].Contains("Camellia"),
            "A tolerated guest is not 'at the table, apart' from the one woman she will not speak to.");
        var both = State(story, 3, "committed", Committed("anevia"));
        check(Visible("guest.tirabade", both) && !Visible("guest.anevia", both), "Anevia is listed apart from Anevia and Irabeth together.");
        var pair = Lines("guest.minagho_chivarro", State(story, 3, "minachiv.complete", "minagho_chivarro.harem.stance.minagho.joined"));
        check(pair.Contains("{n}Minagho: at the table.{/n}") && pair.Contains("{n}Chivarro: not yet at the table.{/n}"), "The canon pair does not have a seat each.");
        var seating = ledger.Entries.Where(e => e.Section == "Seating Notes" && e.Id != "seating.word_made_true").ToList();
        check(seating.Count == 5 && seating.All(e => e.Requires.Length == 2 && e.Requires.All(r => r.EndsWith(".harem.eligible", StringComparison.Ordinal))),
            "The Seating Notes are not the seeded frictions, each shown only when both women are eligible.");
        check(!Visible("seating.seelah.camellia", seelah) && Visible("seating.seelah.camellia", State(story, 3, Committed("seelah"), Committed("camellia"))),
            "A Seating Note shows before both women are eligible.");
        check(Lines("seating.seelah.areelu", State(story, 3, Committed("seelah"), Committed("areelu"))).Any(t => t.Contains("No word of mine")),
            "An atrocity friction does not say the Word cannot settle it.");
        check(ledger.Entries.Where(e => e.Section == "Secrets").All(e => e.Requires.Length == 1 && e.Requires[0].StartsWith("trickster.secret.", StringComparison.Ordinal)),
            "A Secrets entry shows without its trickster.secret flag.");

        // Word Made True: three uses per campaign, counted from trickster.wmt.use.*; the Ledger line reads the count.
        var fresh = State(story, 3, "trickster", Kept);
        check(Rules.WordMadeTrueMax == 3 && fresh.Has("trickster.wmt.left.3") && fresh.Has("trickster.wmt.available"), "A fresh campaign does not have three Words.");
        var two = State(story, 3, "trickster", Kept, "trickster.wmt.use.a", "trickster.wmt.use.b");
        check(two.Has("trickster.wmt.left.1") && !two.Has("trickster.wmt.left.3") && two.Has("trickster.wmt.available"), "Two Words spent do not leave one.");
        var spent = State(story, 3, "trickster", Kept, "trickster.wmt.use.a", "trickster.wmt.use.b", "trickster.wmt.use.c", "trickster.wmt.use.d");
        check(spent.Has("trickster.wmt.left.0") && !spent.Has("trickster.wmt.available") && Rules.WordMadeTrueLeft(spent) == 0,
            "A spent Word is still available.");
        Rules.Complete(story, spent);
        check(spent.Flags.Count(f => f.StartsWith("trickster.wmt.left.", StringComparison.Ordinal)) == 1, "The Word counter keeps a stale count.");
        check(Lines("seating.word_made_true", two).SingleOrDefault()?.Contains("One word") == true, "The Ledger does not show the Words left.");
        check(story.Scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Where(c => c.Set.Any(f => f.StartsWith("trickster.wmt.use.", StringComparison.Ordinal)))
            .All(c => c.Requires.Contains("trickster.wmt.available")), "A Word Made True choice does not require a Word left.");

        // The invitation kind: authored only, never inferred, on a remote scene.
        var invitation = new Scene { Id = "i", Owner = "Seelah", Relationship = "household", Remote = true, Kind = "invitation" };
        check(Rules.SceneKinds.Contains("invitation") && Rules.KindOf(invitation) == "invitation", "The invitation kind is not recognized.");
        check(story.Glossary.ContainsKey("RRT_Table") && story.Glossary.ContainsKey("RRT_GuestList") && story.Glossary.ContainsKey("RRT_SeatingNotes")
            && story.Glossary.ContainsKey("RRT_WordMadeTrueUses") && story.Glossary.ContainsKey("RRT_AtTheTableApart"), "A household tooltip is missing.");
    }
}
