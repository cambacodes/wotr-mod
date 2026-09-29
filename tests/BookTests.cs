using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E15: the RRT book. Paged views (mailbag v2, the letter archive, data books such as the Ledger): visibility and order,
// pagination, the cursor, the read-only replay graph, and the contract checks on books and glossary entries.
internal static class BookTests
{
    private static Scene Letter(string id, string owner, int chapter = 3, params Node[] nodes) => new Scene
    {
        Id = id, Title = "Title " + id, Owner = owner, Relationship = "konomi", Remote = true, MinChapter = chapter, MaxChapter = 6,
        Nodes = nodes.Length > 0 ? nodes.ToList() : new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } }
    };

    internal static void Run(Story built, Action<bool, string> check)
    {
        // E15c: every rest-delivered scene of the built story says what it is; kinds are the five allowed values, only on
        // remote scenes, and a framework page (the Commander alone) is an event, never correspondence.
        var remote = built.Scenes.Where(s => Rules.IsRemote(s) && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToList();
        check(remote.Count > 0 && remote.All(s => s.Kind != null && Rules.SceneKinds.Contains(s.Kind)),
            "E15c remote scene without a valid Kind: " + string.Join(", ", remote.Where(s => s.Kind == null || !Rules.SceneKinds.Contains(s.Kind)).Select(s => s.Id).Take(5)));
        check(built.Scenes.All(s => s.Kind == null || Rules.IsRemote(s)), "E15c Kind on an in-person scene.");
        check(remote.Where(s => s.Relationship == "lastcall").All(s => s.Kind == "event"), "E15c a Last Call framework page is not an event.");
        check(remote.Where(s => s.Kind != "event").All(s => !string.IsNullOrEmpty(Rules.SenderOf(s)) && Rules.SenderOf(s) != "Memory"),
            "E15c a remote scene has no real sender (a presentation owner leaked into its header).");

        // The archive lists letters already read, the most recently read first; unread, manual and epilogue pages never.
        var story = new Story();
        var a = Letter("l.a", "Konomi");
        var b = Letter("l.b", "Seelah");
        var c = Letter("l.c", "Nurah");
        var manual = Letter("l.manual", "Konomi");
        manual.ManualOnly = true;
        var page = Letter("l.page", "KonomiEpilogue");
        story.Scenes.AddRange(new[] { a, b, c, manual, page });
        var state = new Snapshot { Chapter = 3, Hour = 100 };
        foreach (var (scene, hour) in new[] { (a, 10), (c, 30), (manual, 40), (page, 50) })
        {
            state.Flags.Add(scene.Id);
            state.Times[scene.Id] = hour;
        }
        var archive = Rules.ArchiveLetters(story, state).Select(s => s.Id).ToList();
        check(archive.SequenceEqual(new[] { "l.c", "l.a" }), "The archive is not the read letters, newest first: " + string.Join(",", archive));

        // Pagination: eight to a page, 0-based, and an empty list still has one page.
        var twenty = Enumerable.Range(0, 20).Select(i => "k" + i).ToList();
        check(Rules.PageCount(0, 8) == 1 && Rules.PageCount(8, 8) == 1 && Rules.PageCount(9, 8) == 2 && Rules.PageCount(20, 8) == 3,
            "Page counts are wrong.");
        check(Rules.PageSlice(twenty, 2, 8).SequenceEqual(new[] { "k16", "k17", "k18", "k19" }) && Rules.PageSlice(twenty, 3, 8).Count == 0
            && Rules.PageSlice(twenty, 0, 8).First() == "k0", "Page slices are wrong.");

        // The cursor steps and wraps; a key that left the list (a letter just read) restarts at the first.
        var keys = new List<string> { "x", "y", "z" };
        check(Rules.Step(keys, "x", 1) == "y" && Rules.Step(keys, "z", 1) == "x" && Rules.Step(keys, "x", -1) == "z"
            && Rules.Step(keys, "gone", 1) == "x" && Rules.Step(keys, null, 1) == "x" && Rules.Step(new List<string>(), "x", 1) == null,
            "The book cursor does not step, wrap or restart correctly.");

        // Read-only replay: each choice leads to its next node, or a check's success node; everything else ends the
        // replay. Only labels travel: the edge carries no flag, cost, check, revival or native effect.
        var replay = Letter("l.replay", "Konomi", 3,
            new Node { Id = "start", Text = "Dear Commander", Choices = new List<Choice> {
                new Choice { Text = "Answer warmly", Next = "warm", Set = new[] { "konomi.warm" } },
                new Choice { Text = "Try your luck", Check = new SkillCheck { Skill = "SkillPersuasion", DC = 20, Success = "won", Failure = "lost" } },
                new Choice { Text = "Burn it", Set = new[] { "konomi.closed" } },
                new Choice { Text = "Answer warmly", Next = "warm" } } },
            new Node { Id = "warm", Text = "She smiles", Choices = new List<Choice> { new Choice { Text = "Seal it", Next = "missing" } } },
            new Node { Id = "won", Text = "Won", Choices = new List<Choice> { new Choice() } },
            new Node { Id = "lost", Text = "Lost", Choices = new List<Choice> { new Choice() } });
        var edges = Rules.ReplayEdges(replay, replay.Nodes[0]);
        check(edges.Count == 3 && edges[0] == ("Answer warmly", "warm") && edges[1] == ("Try your luck", "won") && edges[2] == ("Burn it", null),
            "Replay edges are wrong: " + string.Join(";", edges));
        check(Rules.ReplayEdges(replay, replay.Nodes[1]).Single() == ("Seal it", null), "A replay edge to a missing node does not end the replay.");
        var before = new HashSet<string>(state.Flags);
        foreach (var node in replay.Nodes) Rules.ReplayEdges(replay, node);
        check(state.Flags.SetEquals(before), "Replaying a letter changed the state.");

        // Data books: visible entries in section order, then authored order; conditions and lines are read-only reads.
        var book = new BookSpec { Title = "Ledger", Sections = new[] { "Debts", "Secrets" }, Entries = new List<BookEntry> {
            new BookEntry { Id = "s1", Section = "Secrets", Title = "S1", Text = "t" },
            new BookEntry { Id = "d1", Section = "Debts", Title = "D1", Text = "t" },
            new BookEntry { Id = "d2", Section = "Debts", Title = "D2", Text = "t", Requires = new[] { "debt.two" } },
            new BookEntry { Id = "d3", Section = "Debts", Title = "D3", Text = "t", Forbids = new[] { "debt.paid" } },
            new BookEntry { Id = "d4", Section = "Debts", Title = "D4", Text = "t", AnyGroups = new[] { new[] { "x", "y" } } } } };
        var ledger = new Snapshot();
        check(Rules.BookVisible(book, ledger).Select(e => e.Id).SequenceEqual(new[] { "d1", "d3", "s1" }), "Book visibility or order is wrong (empty state).");
        ledger.Flags.UnionWith(new[] { "debt.two", "debt.paid", "y" });
        check(Rules.BookVisible(book, ledger).Select(e => e.Id).SequenceEqual(new[] { "d1", "d2", "d4", "s1" }), "Book visibility or order is wrong (flags set).");

        // Contract checks: glossary keys RRT_<word> with a name and a description; entries need a unique id, a declared
        // section, a title and text; tooltips and {g|RRT_...} links must name a known glossary entry.
        var contract = new Story();
        contract.Scenes.Add(a);
        contract.Glossary["RRT_Debt"] = new GlossaryText { Name = "Debt", Description = "d" };
        contract.Books["ledger"] = new BookSpec { Title = "Ledger", Sections = new[] { "Debts" }, Entries = new List<BookEntry> {
            new BookEntry { Id = "d1", Section = "Debts", Title = "D1", Text = "A {g|RRT_Debt}debt{/g}.", Tooltip = "RRT_Debt" } } };
        Rules.ValidateBooks(contract);
        void Rejects(Action<Story> spoil, string what)
        {
            var copy = new Story();
            copy.Glossary = contract.Glossary.ToDictionary(p => p.Key, p => new GlossaryText { Name = p.Value.Name, Description = p.Value.Description });
            copy.Books["ledger"] = new BookSpec { Title = "Ledger", Sections = new[] { "Debts" }, Entries = new List<BookEntry> {
                new BookEntry { Id = "d1", Section = "Debts", Title = "D1", Text = "A {g|RRT_Debt}debt{/g}.", Tooltip = "RRT_Debt" } } };
            spoil(copy);
            bool threw = false;
            try { Rules.ValidateBooks(copy); } catch (InvalidOperationException) { threw = true; }
            check(threw, "The book contract accepts " + what + ".");
        }
        Rejects(s => s.Glossary["Debt"] = new GlossaryText { Name = "n", Description = "d" }, "a glossary key without the RRT_ prefix");
        Rejects(s => s.Glossary["RRT_Blank"] = new GlossaryText { Name = "n", Description = "" }, "a glossary entry without a description");
        Rejects(s => s.Books["ledger"].Entries.Add(new BookEntry { Id = "d1", Section = "Debts", Title = "x", Text = "x" }), "a duplicate entry id");
        Rejects(s => s.Books["ledger"].Entries[0].Section = "Secrets", "an undeclared section");
        Rejects(s => s.Books["ledger"].Entries[0].Tooltip = "RRT_Missing", "an unknown tooltip");
        Rejects(s => s.Books["ledger"].Entries[0].Text = "{g|RRT_Missing}x{/g}", "a link to an unknown glossary key");
        Rejects(s => s.Books["ledger"].Sections = new[] { "Debts", "Debts" }, "duplicate sections");

        // The shipped story: every book and glossary entry is valid (Validate runs it), and the guide demonstrates the contract.
        check(built.Glossary.Count >= 9 && new[] { "RRT_Mailbag", "RRT_LettersKept", "RRT_Ledger", "RRT_Debt", "RRT_Secret", "RRT_SecretRisk",
                "RRT_WordMadeTrue", "RRT_Tolerated", "RRT_AtTheTableApart" }.All(built.Glossary.ContainsKey),
            "The shipped glossary does not explain every new mechanic.");
        check(built.Books.TryGetValue("rrt.guide", out var guide) && guide.Entries.Count >= 3 && guide.Entries.All(e => e.Tooltip.Length > 0)
            && guide.Entries.Any(e => e.Requires.Length > 0) && guide.Entries.Any(e => e.Lines.Count > 0),
            "The guide book does not demonstrate sections, conditions, lines and tooltips.");
        Rules.ValidateBooks(built);
        Console.WriteLine("PASS: E15 book (archive order, pagination, cursor, read-only replay edges, book visibility, book and glossary contract).");
    }
}
