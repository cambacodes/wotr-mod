using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Shyka's page (Writer/handoffs/12-TRICKSTER-FORESIGHT.md §4 acceptance tests 1-14, §7, and §2.4a, the echoes): the Council
// bargain Shyka may refuse, the price (one memory, or two, or the counteroffer), the memory page and its Chapter 5 fallback,
// the east-gate misstep in one scene on two native lists, the Chapter 5 line, the witnesses, Last Call's paragraphs and the Ledger's
// journal lines; injected echoes are optional, appended and neutral. Allocated existing pilots retain their authored chains.
// Every allocated echo counts in the budget: one per route, two per chapter, Trickster-only.
// Nothing outside the listed scenes reads trickster.foresight.*; registered consumers read the public page key.
internal static class ForesightTests
{
#if FORESIGHT_ACCEPTANCE
    // Compile with StartupObject=ForesightTests for a focused gate; normal RulesTests keeps its existing entry point.
    private static void Main(string[] args)
    {
        var story = System.Text.Json.JsonSerializer.Deserialize<Story>(System.IO.File.ReadAllText(args.Single()),
            new System.Text.Json.JsonSerializerOptions { IncludeFields = true })!;
        Run(story, (passed, message) => { if (!passed) throw new Exception(message); });
    }
#endif

    private const string P = "trickster.foresight.";
    private const string Accepted = P + "accepted", Raised = P + "raised", GateFire = P + "gate_fire", GateWatch = P + "gate_watch";
    private const string Promise = P + "cost.promise", Square = P + "cost.square", Caves = P + "cost.caves";
    private const string Wager = P + "wager", Counter = P + "counter", Told = P + "memory_told", Essence = P + "shyka_essence";
    private const string PageTaken = "foresight.page_taken", GateBelieved = "foresight.gate_believed";
    private const string GoneSquare = "foresight.memory_gone.square_morning", GoneCaves = "foresight.memory_gone.caves";
    private const string ShykaList = "e7236a1fe9273ba498b96b9616b3f379", ShykaBack = "cd2b35a474db55544a63f59a67ac67bf";
    private const string OfferList = "d3d0efb4dfcc1964c923d7b2d6e0dc77", OfferBack = "5d6810f1e0eb8204fa4c3211fc603769";
    private const string KingC3 = "1a17d8053a3be7f47a7908eb6706f2fe", KingC5 = "6dccfd39947ef4242a8afbe36b21a46c";
    private static readonly string[] Costs = { Promise, Square, Caves };
    private static readonly string[] Readers = { P + "page", P + "memory", P + "fire_watch", P + "offer_line", P + "noticed.anevia",
        P + "noticed.seelah", P + "noticed.king", "trickster.lastcall.page.interrupted", "trickster.lastcall.page.heroic" };

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000,
            // eng-final / E-Q8-10: fund these positive histories; the walker enforces every debit.
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 500;
        return state;
    }

    private static bool Shown(Paragraph line, Snapshot s) =>
        line.Requires.All(s.Has) && !line.Forbids.Any(s.Has) && line.AnyGroups.All(g => g.Any(s.Has));

    private static IEnumerable<string> Reads(Scene s) =>
        s.Requires.Concat(s.Forbids).Concat(s.RequiresAny).Concat(s.RequiresAnyGroups.SelectMany(g => g)).Concat(s.ForbidOverrides.Keys).Concat(s.ForbidOverrides.Values)
            .Concat(s.Nodes.SelectMany(n => n.Choices.SelectMany(c => c.Requires.Concat(c.Forbids))))
            .Concat(s.Nodes.SelectMany(n => n.Paragraphs.SelectMany(p => p.Requires.Concat(p.Forbids).Concat(p.AnyGroups.SelectMany(g => g)))));

    private static string Key(Snapshot s, IEnumerable<string> ignore) =>
        string.Join(",", s.Flags.Where(f => !ignore.Contains(f) && !f.StartsWith(P, StringComparison.Ordinal)
                                             && !f.StartsWith("foresight.", StringComparison.Ordinal)).OrderBy(f => f, StringComparer.Ordinal));

    private static IEnumerable<string> SceneReads(Scene s) =>
        s.Requires.Concat(s.Forbids).Concat(s.RequiresAny).Concat(s.RequiresAnyGroups.SelectMany(g => g))
            .Concat(s.ForbidOverrides.Keys).Concat(s.ForbidOverrides.Values);

    private static IEnumerable<string> ParagraphReads(Paragraph p) =>
        p.Requires.Concat(p.Forbids).Concat(p.AnyGroups.SelectMany(g => g));

    private static bool PublicKey(string key) => key.StartsWith("foresight.", StringComparison.Ordinal);

    private static void GateContract(Story story, IReadOnlyDictionary<string, string> consumers, Action<bool, string> check)
    {
        foreach (var s in story.Scenes.Where(s => !Readers.Contains(s.Id)))
        {
            check(!Reads(s).Any(k => k.StartsWith(P, StringComparison.Ordinal)),
                "Foresight_GateContract: " + s.Id + " reads trickster.foresight.*.");
            var publicReads = SceneReads(s).Concat(s.Nodes.SelectMany(n => n.Paragraphs.SelectMany(ParagraphReads)))
                .Where(PublicKey).Distinct().ToArray();
            check(publicReads.All(k => consumers.TryGetValue(s.Id, out var registered) && registered == k),
                "Foresight_GateContract: unregistered scene or paragraph consumer: " + s.Id);
            foreach (var node in s.Nodes)
                foreach (var c in node.Choices.Where(c => c.Requires.Any(PublicKey)))
                    check(consumers.TryGetValue(s.Id, out var registered) && c.Requires.Where(PublicKey).All(k => k == registered)
                          || c.Next != null && (c.Next.StartsWith("echo.", StringComparison.Ordinal) || c.Next.StartsWith("gap.", StringComparison.Ordinal)),
                        "Foresight_GateContract: " + s.Id + "/" + node.Id + " reads the page in an unlisted choice.");
        }
        foreach (var pair in consumers)
        {
            var consumer = story.Scenes.SingleOrDefault(s => s.Id == pair.Key);
            check(consumer != null && pair.Value == PageTaken,
                "Foresight_GateContract: missing consumer or unsupported public gate: " + pair.Key);
            if (consumer == null || pair.Value != PageTaken) continue;
            bool sceneGate = SceneReads(consumer).Contains(pair.Value);
            var paragraphs = consumer.Nodes.SelectMany(n => n.Paragraphs).Where(p => ParagraphReads(p).Contains(pair.Value)).ToArray();
            check(sceneGate || paragraphs.Length > 0, "Foresight_GateContract: registered consumer has no gate: " + pair.Key);
            foreach (var paragraph in paragraphs.Cast<Paragraph?>().DefaultIfEmpty(null))
            {
                var requires = consumer.Requires.Concat(consumer.RequiresAny)
                    .Concat(consumer.RequiresAnyGroups.Select(g => g[0]))
                    .Concat(paragraph?.Requires ?? Array.Empty<string>())
                    .Concat(paragraph?.AnyGroups.Select(g => g[0]) ?? Enumerable.Empty<string>());
                var held = World(story, consumer.MinChapter, requires.Where(k => !story.Derived.ContainsKey(k))
                    .Concat(new[] { "trickster", Accepted, Promise, GateFire, "seelah.committed" }).ToArray());
                held.Area = consumer.Areas.FirstOrDefault() ?? "";
                held.Flags.ExceptWith(consumer.Forbids.Concat(paragraph?.Forbids ?? Array.Empty<string>()));
                held.AvailableContacts.UnionWith(consumer.Participants.SelectMany(r =>
                    story.Scenes.Where(sc => sc.Relationship == r && sc.ContactUnit != null).Select(sc => sc.ContactUnit!)));
                if (consumer.ContactUnit != null) { held.AvailableContacts.Add(consumer.ContactUnit); held.SceneContacts.Add(consumer.Id); }
                // Fill independent earned requirements before changing only the paid page and current path.
                held.Flags.UnionWith(requires.Where(k => k != pair.Value && k != "household.stance_eligible"));
                foreach (var f in held.Flags) held.Times[f] = 0;
                Rules.Complete(story, held);
                var bare = Program.Copy(held);
                bare.Flags.Remove(Accepted);
                bare.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
                Rules.Complete(story, bare);
                check(Rules.Match(consumer.Requires.Where(k => k != pair.Value && k != "household.stance_eligible"), consumer.Forbids, bare),
                    "Foresight_GateContract: page-free control lost an independent prerequisite: " + pair.Key);
                check(Rules.Available(story, consumer, held) && (paragraph == null || Shown(paragraph, held))
                      && (sceneGate ? !Rules.Available(story, consumer, bare) : paragraph != null && !Shown(paragraph, bare)),
                    "Foresight_GateContract: consumer unavailable with page or available without it: " + pair.Key);
                foreach (var path in new[] { "legend", "dragon", "swarm", "trickster.failed" })
                {
                    var former = Program.Copy(held);
                    former.Flags.Add("trickster.was");
                    former.Flags.Add(path);
                    former.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
                    Rules.Complete(story, former);
                    check(!Rules.Available(story, consumer, former) || !sceneGate && paragraph != null && !Shown(paragraph, former),
                        "Foresight_PathChanged: consumer remains available on " + path + ": " + pair.Key);
                }
            }
        }
    }

    private static void GateContractFixtures(Story story, Dictionary<string, string> consumers, Action<bool, string> check)
    {
        var fixtures = new[]
        {
            new Scene { Id = "acceptance.fate.preparation", Relationship = "foresight", MinChapter = 3,
                Requires = new[] { "trickster.now", PageTaken, "acceptance.prepared" }, Optional = true },
            new Scene { Id = "acceptance.fate.ending", Relationship = "foresight", MinChapter = 6, MaxChapter = 6, EpilogueSequence = "PlayerFinalChoice",
                Nodes = new List<Node> { new Node { Id = "start", Paragraphs = new List<Paragraph> {
                    new Paragraph { Text = "Paid ending.", Requires = new[] { "trickster.now", PageTaken, "acceptance.prepared" } } } } } }
        };
        story.Scenes.AddRange(fixtures);
        try
        {
            foreach (var fixture in fixtures) consumers.Add(fixture.Id, PageTaken);
            GateContract(story, consumers, check);
            foreach (var fixture in fixtures)
            {
                consumers.Remove(fixture.Id);
                var errors = new List<string>();
                GateContract(story, consumers, (passed, message) => { if (!passed) errors.Add(message); });
                check(errors.Count == 1 && errors[0].Contains("unregistered scene or paragraph consumer: " + fixture.Id),
                    "Foresight_GateContract: an unregistered consumer was accepted: " + fixture.Id);
                consumers.Add(fixture.Id, PageTaken);
            }
        }
        finally
        {
            foreach (var fixture in fixtures) { story.Scenes.Remove(fixture); consumers.Remove(fixture.Id); }
        }
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Node N(Scene scene, string node) => scene.Nodes.Single(n => n.Id == node);
        bool Avail(Scene s, Snapshot w) => Rules.Available(story, s, w);
        // eng7-l13: exact authored effects exclude freshly recomputed Derived/Counts readers.
        HashSet<string> New(Snapshot from, Snapshot to) => new HashSet<string>(to.Flags.Where(f => !from.Has(f)
            && !story.Derived.ContainsKey(f) && !story.Counts.ContainsKey(f)));
        Snapshot Later(Snapshot w, int hours, int? chapter = null, params string[] add)
        {
            var later = Program.Copy(w);
            later.Hour += hours;
            if (chapter != null) later.Chapter = chapter.Value;
            foreach (var f in add) { later.Flags.Add(f); later.Times[f] = w.Hour; }
            Rules.Complete(story, later);
            return later;
        }

        var page = S(P + "page");
        var memory = S(P + "memory");
        var watch = S(P + "fire_watch");
        var offer = S(P + "offer_line");
        var interrupted = S("trickster.lastcall.page.interrupted");
        var heroic = S("trickster.lastcall.page.heroic");
        var rel = story.Relationships["foresight"];
        var ours = story.Scenes.Where(s => s.Relationship == "foresight").ToArray();

        // Shape: a framework, never a romance; Shyka is an ally, not a partner (12 §2.8).
        check(rel.Title == "Shyka's page" && rel.StartedFlag == Accepted && rel.CommittedFlag == GateFire && !story.Relationships.ContainsKey("shyka")
              && !story.Derived.ContainsKey("foresight.harem.eligible")
              && ours.All(s => s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Set).All(f => f.StartsWith(P, StringComparison.Ordinal))),
            "Foresight_Ally: the page is not a framework relationship, or it sets something outside trickster.foresight.* (Shyka is no romance).");
        check(ours.Length == 7 && ours.All(s => s.Requires.Contains("trickster") || s.Requires.Contains("trickster.ever") || s.Requires.Contains("trickster.now")),
            "Foresight_TricksterOnly: a foresight scene is not gated on the Trickster.");
        check(page.AnswerLists.SequenceEqual(new[] { ShykaList }) && page.NativeReturnCue == ShykaBack && page.EntryMythic == "PlayerIsTrickster"
              && Rules.MythicNames.Contains(page.EntryMythic) && page.Chapters.SequenceEqual(new[] { 3, 5 }) && page.MaxChapter == 5,
            "Foresight_Hook: the page is not inline on Council_Shyka AnswersList_0003 (Cue_0002 return, PlayerIsTrickster, Chapters 3 and 5).");
        var start = N(page, "start");
        check(start.Choices.Count == 3 && start.Choices[0].Check?.Skill == "CheckDiplomacy" && start.Choices[0].Check?.DC == 26
              && start.Choices[1].Check?.Skill == "SkillKnowledgeArcana" && start.Choices[1].Check?.DC == 30 && start.Choices[2].Abort
              && start.Choices.All(c => c.Set.Length == 0),
            "Foresight_Checks: the pitch is not Diplomacy 26 / Arcana 30 / leave, or a pitch sets a flag before acceptance.");

        // 4. Chapters (the fallback window, 2026-10-03): Chapters 3 and 5 while Shyka is present; never in the Abyss (Chapter 4,
        // no Council), after the Council is gone, off-Trickster or twice. Still paid in Chapter 5.
        var ch3 = World(story, 3, "trickster", "trickster.ever");
        var ch5 = World(story, 5, "trickster", "trickster.ever");
        check(Avail(page, ch3) && Avail(page, ch5) && !Avail(page, World(story, 4, "trickster", "trickster.ever"))
              && Program.WalkVia(page, ch5, "m1_pick", 1).All(o => o.Has(Square) && o.Has(Accepted))
              && !Avail(page, World(story, 3, "trickster", "trickster.ever", "shyka.gone"))
              && !Avail(page, World(story, 3, "trickster", "trickster.ever", "council.fought"))
              && !Avail(page, World(story, 3, "trickster", "trickster.ever", Accepted))
              && !Avail(page, World(story, 3)) && !Avail(page, World(story, 5, "trickster", "trickster.ever", "shyka.gone")),
            "Foresight_Chapters: the page is not offered in Chapters 3 and 5 with Shyka present, or is offered elsewhere.");

        // 1. Decline: every abort sets nothing and leaves the entry for the next visit.
        var outcomes = Program.Walk(page, ch3);
        var declined = outcomes.Where(o => !o.Has(page.Id)).ToList();
        check(declined.Count >= 4 && declined.All(o => New(ch3, o).Count == 0) && declined.All(o => Avail(page, o)),
            "Foresight_Decline: declining (or leaving) sets a flag, or closes the entry.");
        check(N(page, "offer1").Choices.Last().Abort && N(page, "offer1w").Choices.Last().Abort && N(page, "offer2").Choices.Last().Abort,
            "Foresight_Decline: an offer has no decline before a memory is taken.");

        // 2. Success: pitch_ok, accept, the promise: exactly accepted, cost.promise, gate_fire; the glimpses in order.
        var success = Program.WalkVia(page, ch3, "m1_pick", 0);
        check(success.Count > 0 && success.All(o => New(ch3, o).SetEquals(new[] { Accepted, Promise, GateFire, page.Id })),
            "Foresight_Success: accepting the promise does not set exactly accepted, cost.promise and gate_fire.");
        check(N(page, "g_punchline").Choices.Single().Next == "g_shyka" && N(page, "g_shyka").Choices.Single().Next == "g_funeral"
              && N(page, "g_funeral").Choices.Single().Next == "g_gate" && N(page, "g_gate").Choices.Single().Set.SequenceEqual(new[] { GateFire })
              && new[] { "read_p", "read_s", "read_c", "read_ps", "read_pc", "read_sc" }.All(r => N(page, r).Choices.Single().Next == "g_punchline"),
            "Foresight_Glimpses: the page does not play punchline, Shyka, funeral, gate after every reading.");
        var wagered = Program.WalkVia(page, ch3, "offer1w", 0);
        check(wagered.Count == 3 && wagered.All(o => o.Has(Wager) && o.Has(Accepted) && !o.Has(Raised) && Costs.Count(o.Has) == 1),
            "Foresight_Wager: the won wager does not take the base price with the wager on record.");

        // 3 + 11 + 12. Failure: offer2; two distinct memories; no way back once the first is taken; the counteroffer.
        var raised = Program.WalkVia(page, ch3, "offer2", 0);
        check(raised.Count == 12 && raised.All(o => o.Has(Accepted) && o.Has(Raised) && Costs.Count(o.Has) == 2 && !o.Has(Counter))
              && raised.Select(o => string.Join(",", Costs.Where(o.Has))).Distinct().Count() == 3,
            "Foresight_Fail: the raised price does not set accepted, raised and exactly two distinct costs.");
        foreach (var (node, own) in new[] { ("m2_second_p", Promise), ("m2_second_s", Square), ("m2_second_c", Caves) })
            check(N(page, node).Choices.Count == 2 && N(page, node).Choices.All(c => c.Set.Contains(own) && c.Set.Count(Costs.Contains) == 2),
                "Foresight_NoDuplicate: " + node + " offers a memory already taken.");
        var reach = new HashSet<string>();
        void Mark(string id) { if (!reach.Add(id)) return; foreach (var c in N(page, id).Choices) foreach (var t in Rules.NextNodes(c)) Mark(t); }
        Mark("m2_first");
        check(N(page, "m2_first").Choices.All(c => c.Set.Length == 0)
              && reach.SelectMany(id => N(page, id).Choices).All(c => !c.Abort && (c.Next != null || c.Set.Contains(GateFire))),
            "Foresight_Commit: after the first memory is taken there is a way out without the page.");
        var counter = Program.WalkVia(page, ch3, "offer2", 1);
        check(counter.Count == 6 && counter.All(o => o.Has(Counter) && o.Has(Accepted) && !o.Has(Raised) && Costs.Count(o.Has) == 1),
            "Foresight_Counteroffer (§7.2): one memory plus the unsettled wager is not offered at the raised price.");
        check(N(page, "offer1").Text.Contains("belongs to a Drezen that is not yours") && N(page, "offer2").Text.Contains("You will not know which"),
            "Foresight_Legible: the page's unreliability is not said before acceptance.");

        // 5. The memory: a remote memory page, at the next rest (>= 1 h after acceptance), for the chosen cost only.
        var paid = Later(ch3, 0, null, Accepted, Promise, GateFire, page.Id);
        check(memory.Remote && memory.Kind == "memory" && memory.DelayHours == 1 && !Avail(memory, paid) && Avail(memory, Later(paid, 1)),
            "Foresight_Memory: the memory page is not a remote memory delivered one hour after the bargain.");
        var visited = new List<string>();
        Program.Walk(memory, Later(paid, 1), (id, _) => visited.Add(id));
        check(visited.SequenceEqual(new[] { "start", "r_p" }), "Foresight_Memory: the memory page does not show the promise's receipt alone.");
        var pair = World(story, 5, "trickster", "trickster.ever", Accepted, Raised, Square, Caves, GateFire);
        visited.Clear();
        Program.Walk(memory, pair, (id, _) => visited.Add(id));
        check(visited.SequenceEqual(new[] { "start", "r_sc" }), "Foresight_Memory: the raised price does not show both receipts.");

        // §7.3: no rest before the Chapter 5 payoff: the line reads the receipt first, and the memory page then stays quiet.
        visited.Clear();
        var unrested = World(story, 5, "trickster", "trickster.ever", Accepted, Square, GateFire);
        check(Avail(offer, unrested), "Foresight_OfferLine: the Chapter 5 line is not offered with the page accepted.");
        var offerOut = Program.Walk(offer, unrested, (id, _) => visited.Add(id));
        check(visited.Contains("lr_s") && offerOut.All(o => o.Has(Told)) && offerOut.All(o => !Avail(memory, Later(o, 48))),
            "Foresight_NoRest: without a rest the Chapter 5 line does not read the receipt, or the memory page plays after it.");
        visited.Clear();
        Program.Walk(offer, World(story, 5, "trickster", "trickster.ever", Accepted, Square, GateFire, memory.Id), (id, _) => visited.Add(id));
        check(!visited.Any(v => v.StartsWith("lr_", StringComparison.Ordinal)) && visited.Contains("cost_s") && visited.Contains("gate"),
            "Foresight_OfferLine: a rested Commander hears the receipt twice, or the line skips the false gate or the cost.");

        // 9 + 14. The Chapter 5 line: only inline on AnswersList_0011 with a clean return; no other Chapter 5 surface.
        check(offer.AnswerLists.SequenceEqual(new[] { OfferList }) && offer.NativeReturnCue == OfferBack && !offer.Remote
              && !Avail(offer, World(story, 5, "trickster", "trickster.ever")) && !Avail(offer, World(story, 3, "trickster", "trickster.ever", Accepted, Square)),
            "Foresight_OfferLine: the line is not exactly an inline answer on Shyka_Offer AnswersList_0011 in Chapter 5 with the page.");
        visited.Clear();
        Program.Walk(offer, World(story, 5, "trickster", "trickster.ever", Accepted, Promise, GateFire, GateWatch, Counter, memory.Id), (id, _) => visited.Add(id));
        check(visited.Contains("gate_watched") && visited.Contains("won_ours") && !visited.Contains("won_yours"),
            "Foresight_OfferLine: the believed gate or Shyka's won wager is not named.");
        visited.Clear();
        Program.Walk(offer, World(story, 5, "trickster", "trickster.ever", Accepted, Promise, GateFire, Wager, memory.Id), (id, _) => visited.Add(id));
        check(visited.Contains("won_yours") && !visited.Contains("gate_watched") && !visited.Contains("count"),
            "Foresight_OfferLine: the Commander's wager is not settled, or Kaylessa's count shows without her trade.");
        check(offer.Nodes.SelectMany(n => n.Choices).All(c => c.Set.All(f => f == Told)),
            "Foresight_OfferLine: the Chapter 5 line has an effect beyond reading the receipt.");

        // 8 + §7.4. The misstep: one scene on two native lists, Chapters 3 and 5; Favors -50.
        var setters = story.Scenes.Where(s => s.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains(GateWatch))).ToArray();
        check(setters.Length == 1 && setters[0] == watch && watch.AnswerLists.OrderBy(x => x).SequenceEqual(new[] { KingC3, KingC5 }.OrderBy(x => x))
              && watch.ReturnToList && watch.InteractionHub == null && watch.MinChapter == 3 && watch.MaxChapter == 5 && watch.Chapters.SequenceEqual(new[] { 3, 5 }),
            "Foresight_Gate: the fire watch is not one scene on both of the King's lists in Chapters 3 and 5.");
        foreach (var ch in new[] { 3, 5 })
        {
            check(Avail(watch, World(story, ch, "trickster", "trickster.ever", Accepted, Promise, GateFire)), "Foresight_Gate: no fire watch in Chapter " + ch + " with gate_fire.");
            check(!Avail(watch, World(story, ch, "trickster", "trickster.ever", Accepted, Promise)), "Foresight_Gate: a fire watch without gate_fire in Chapter " + ch + ".");
            check(!Avail(watch, World(story, ch, "trickster", "trickster.ever", Accepted, Promise, GateFire, "fool_king.gone")), "Foresight_Gate: a fire watch with no King in Chapter " + ch + ".");
        }
        check(!Avail(watch, World(story, 4, "trickster", "trickster.ever", Accepted, Promise, GateFire)), "Foresight_Gate: a fire watch in Chapter 4.");
        var post = N(watch, "ask").Choices[0];
        check(post.Crusade?.Resource == "Favors" && post.Crusade?.Amount == -50 && N(watch, "ask").Choices[1].Abort,
            "Foresight_Gate: posting the watch is not Favors -50, or [Never mind] does not abort.");
        foreach (var ch in new[] { 3, 5 })
        {
            var before = World(story, ch, "trickster", "trickster.ever", Accepted, Promise, GateFire);
            var posted = Program.Walk(watch, before);
            check(posted.Count(o => o.Has(GateWatch)) == 1
                  && posted.Count(o => !o.Has(watch.Id) && !o.Has(GateWatch) && New(before, o).Count == 0) == 1
                  && posted.Where(o => o.Has(GateWatch)).All(o => New(before, o).SetEquals(new[] { GateWatch, watch.Id })
                      && !Avail(watch, o) && !Avail(watch, Later(o, 0, ch == 3 ? 5 : 3))),
                "Foresight_Gate: Chapter " + ch + " does not produce one watch outcome shared by both visits, or [Never mind] sets something.");
        }

        // 10. Last Call: exactly one report paragraph per paid combination on each Block A page; none without the page.
        string[][] combos = { new[] { Promise }, new[] { Square }, new[] { Caves }, new[] { Raised, Promise, Square }, new[] { Raised, Promise, Caves }, new[] { Raised, Square, Caves } };
        var reports = new[] { interrupted, heroic }.Select(pg => pg.Nodes[0].Paragraphs.Where(p => p.Requires.Contains(Accepted) && !p.Requires.Contains(Essence) && !p.Forbids.Contains(memory.Id)).ToArray()).ToArray();
        var unread = new[] { interrupted, heroic }.Select(pg => pg.Nodes[0].Paragraphs.Where(p => p.Requires.Contains(Accepted) && p.Forbids.Contains(memory.Id) && p.Forbids.Contains(Told)).ToArray()).ToArray();
        // §7.3 at Threshold: a Commander who never rested and never heard the Chapter 5 line gets the unread receipt, once, first.
        foreach (var pg in new[] { interrupted, heroic })
        {
            var ps = pg.Nodes[0].Paragraphs;
            int firstUnread = ps.FindIndex(p => p.Forbids.Contains(memory.Id));
            int firstReport = ps.FindIndex(p => p.Requires.Contains(Accepted) && !p.Forbids.Contains(memory.Id));
            check(firstUnread >= 0 && firstUnread < firstReport, "Foresight_NoRest: the unread receipt is not placed before the report on " + pg.Id);
        }
        check(reports.All(r => r.Length == 6), "Foresight_LastCall: a Block A page lacks the six report variants.");
        foreach (var combo in combos)
        {
            var world = World(story, 6, new[] { "trickster", "trickster.ever", Accepted, GateFire }.Concat(combo).ToArray());
            check(reports.All(r => r.Count(p => Shown(p, world)) == 1), "Foresight_LastCall: not exactly one report variant for " + string.Join("+", combo));
            check(unread.All(r => r.Count(p => Shown(p, world)) == 1), "Foresight_NoRest: not exactly one unread receipt for " + string.Join("+", combo));
            var rested = World(story, 6, new[] { "trickster", "trickster.ever", Accepted, GateFire, memory.Id }.Concat(combo).ToArray());
            var told = World(story, 6, new[] { "trickster", "trickster.ever", Accepted, GateFire, Told }.Concat(combo).ToArray());
            check(unread.All(r => r.All(p => !Shown(p, rested) && !Shown(p, told))), "Foresight_NoRest: a delivered receipt is read again at Threshold.");
        }
        var noPage = World(story, 6, "trickster", "trickster.ever", Promise);
        check(reports.All(r => r.All(p => !Shown(p, noPage))), "Foresight_LastCall: a report variant shows without the page.");
        check(story.Latches.TryGetValue(Essence, out var essence) && essence.SequenceEqual(new[] { "areelu.siphon.council_shyka" })
              && interrupted.Nodes[0].Paragraphs.Any(p => p.Requires.Contains(Essence) && p.Requires.Contains(Accepted)),
            "Foresight_LastCall: Shyka's recital at the table does not follow the latched Shyka siphon.");

        // 13. The Ledger: "What I no longer remember", one line per memory, opened by the payment, never settled.
        var ledger = story.Relationships["lastcall"].JournalEntries.Where(e => e.Id.StartsWith("foresight.forgot.", StringComparison.Ordinal)).ToList();
        var lp = World(story, 3, "trickster", "trickster.ever", Accepted, Promise);
        check(ledger.Count == 3 && ledger.All(e => e.Title == "What I no longer remember" && e.SettledWhen.Length == 0)
              && Rules.JournalStep(ledger.Single(e => e.Id.EndsWith(".p", StringComparison.Ordinal)), false, false, lp) == "give"
              && Rules.JournalStep(ledger.Single(e => e.Id.EndsWith(".s", StringComparison.Ordinal)), false, false, lp) == null
              && Rules.JournalStep(ledger.Single(e => e.Id.EndsWith(".p", StringComparison.Ordinal)), true, true, World(story, 6, "trickster.ever", Accepted, Promise, "lastcall.active")) == null,
            "Foresight_Journal: the lost memory is not a Ledger line given on payment and never settled.");

        // The witnesses (§2.3): Anevia and Seelah for the caves, Thaberdine's lie for any cost; reactions only.
        var anevia = S(P + "noticed.anevia");
        var seelah = S(P + "noticed.seelah");
        var king = S(P + "noticed.king");
        var cavesFound = World(story, 3, "trickster", "trickster.ever", Accepted, Caves, GateFire, memory.Id);
        var squareFound = World(story, 3, "trickster", "trickster.ever", Accepted, Square, GateFire, memory.Id);
        check(new[] { anevia, seelah, king }.All(s => s.Reaction && s.Nodes.Count == 1)
              && Avail(anevia, cavesFound) && Avail(seelah, cavesFound) && Avail(king, cavesFound) && Avail(king, squareFound)
              && !Avail(anevia, squareFound) && !Avail(seelah, squareFound)
              && !Avail(anevia, World(story, 3, "trickster", "trickster.ever", Accepted, Caves, GateFire))
              && king.AnswerLists.OrderBy(x => x).SequenceEqual(new[] { KingC3, KingC5 }.OrderBy(x => x)),
            "Foresight_Witnesses: the caves' witnesses, or Thaberdine's toast, do not follow the lost memory.");

        // 7. Kaylessa's trade is a different transaction: no shared flag; the page reads her price for one line only.
        var kaylessa = story.Scenes.Where(s => s.Relationship == "kaylessa").ToArray();
        check(kaylessa.All(s => !Reads(s).Any(k => k.StartsWith(P, StringComparison.Ordinal)))
              && kaylessa.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).All(f => !f.StartsWith(P, StringComparison.Ordinal))
              && ours.SelectMany(Reads).Where(k => k.StartsWith("kaylessa.", StringComparison.Ordinal)).Distinct().SequenceEqual(new[] { "kaylessa.trickster.cost.shyka_price" })
              && page.Entry != S("kaylessa.trickster.dead.borrow").Entry,
            "Foresight_KaylessaDistinct: the page and Kaylessa's trade share a flag or an entry.");

        // Exported acceptance metadata comes directly from foresight.CONSUMERS; the runtime ignores it.
        using (var export = System.Text.Json.JsonDocument.Parse(System.IO.File.ReadAllText(Environment.GetCommandLineArgs().Last())))
        {
            var consumers = export.RootElement.GetProperty("ForesightConsumers").EnumerateObject()
                .ToDictionary(item => item.Name, item => item.Value.GetString()!);
            GateContract(story, consumers, check);
            GateContractFixtures(story, consumers, check);
        }
        check(story.Derived.Where(d => d.Value.SelectMany(g => g).Any(k => k.StartsWith(P, StringComparison.Ordinal))).Select(d => d.Key).OrderBy(k => k)
                  .SequenceEqual(new[] { GateBelieved, GoneCaves, GoneSquare, PageTaken }.OrderBy(k => k))
              && new[] { PageTaken, GateBelieved }.All(k => story.Derived[k].All(g => g.Contains("trickster.now")))
              && new[] { GoneSquare, GoneCaves }.All(k => story.Derived[k].All(g => g.Contains("trickster.ever") && !g.Contains("trickster.now"))),
            "Foresight_GateContract: a Derived key outside the public four reads the page, or a public key holds off-Trickster.");
        // With and without, for every gated consumer: the page's own gated scenes, then each echo and gap choice.
        var withPage = World(story, 5, "trickster", "trickster.ever", Accepted, Promise, GateFire, memory.Id);
        var noPageCh5 = World(story, 5, "trickster", "trickster.ever", memory.Id);
        check(Avail(offer, withPage) && !Avail(offer, noPageCh5) && Avail(watch, withPage) && !Avail(watch, noPageCh5)
              && Avail(S(P + "noticed.king"), withPage) && !Avail(S(P + "noticed.king"), noPageCh5)
              && withPage.Has(PageTaken) && !noPageCh5.Has(PageTaken),
            "Foresight_GateContract: a page-gated scene opens without the page, or stays shut with it.");
        foreach (var s in story.Scenes)
            foreach (var node in s.Nodes)
                foreach (var c in node.Choices.Where(c => c.Requires.Any(k => k.StartsWith("foresight.", StringComparison.Ordinal))))
                {
                    var keys = c.Requires.Concat(c.Forbids).Where(k => k != "trickster.ever" && !k.StartsWith("foresight.", StringComparison.Ordinal)).ToArray();
                    var held = new Snapshot();
                    held.Flags.UnionWith(c.Requires);
                    var bare = new Snapshot();
                    bare.Flags.UnionWith(c.Requires.Where(k => !k.StartsWith("foresight.", StringComparison.Ordinal)));
                    check(Rules.Match(c.Requires, c.Forbids, held) && !Rules.Match(c.Requires, c.Forbids, bare),
                        "Foresight_GateContract: " + s.Id + "/" + node.Id + " is selectable without the page, or never with it.");
                }

        // New-save sequence: take the page, post the watch, then leave the path.
        var watched = Program.WalkVia(watch, Later(success.First(), 12), "ask", 0).First();
        var purchased = Later(watched, 0, 4, Essence);
        var cavePurchase = Later(Program.WalkVia(page, ch3, "m1_pick", 2).First(), 0, 4);
        var pilot = S(Rules.WenduagEchoPrefix + "prepare");
        purchased = Later(purchased, 0, null, "lann.in_party", Rules.WenduagEchoPrefix + "adapter_available");
        check(purchased.Has(PageTaken) && purchased.Has(GateBelieved) && purchased.Has(GoneSquare) && Avail(pilot, purchased),
            "Foresight_PathChanged: continuing Chapter 4 Trickster control lost page/history.");
        foreach (var path in new[] { "legend", "dragon", "swarm", "trickster.failed" })
        {
            var formerCaves = Program.Copy(cavePurchase);
            formerCaves.Flags.Remove("trickster");
            formerCaves.Flags.Add("trickster.was");
            formerCaves.Flags.Add(path);
            formerCaves.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
            Rules.Complete(story, formerCaves);
            check(formerCaves.Has(GoneCaves) && !formerCaves.Has(PageTaken)
                  && formerCaves.Times[Caves] == cavePurchase.Times[Caves],
                "Foresight_PathChanged: caves payment/history vanishes after " + path);
            var former = Program.Copy(purchased);
            former.Flags.Remove("trickster");
            former.Flags.Add("trickster.was");
            former.Flags.Add(path);
            former.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
            Rules.Complete(story, former);
            check(former.Has("trickster.ever") && former.Has(Accepted) && former.Has(Promise) && former.Has(GateWatch)
                  && former.Times[Accepted] == purchased.Times[Accepted] && former.Times[Promise] == purchased.Times[Promise]
                  && former.Has(GoneSquare) && !former.Has(PageTaken) && !former.Has(GateBelieved)
                  && !Avail(pilot, former) && !Avail(page, Later(former, 0, 3)) && !Avail(watch, Later(former, 0, 5)) && !Avail(offer, Later(former, 0, 5)),
                "Foresight_PathChanged: new outcomes survive path loss or historical payment/timestamps vanish: " + path);
            var ending = Later(former, 0, 6);
            check(interrupted.Nodes[0].Paragraphs.Where(p => p.Requires.Contains(Essence)).All(p => !Shown(p, ending))
                  && reports.All(r => r.Count(p => Shown(p, ending)) == 1),
                "Foresight_PathChanged: Shyka visits off-path or the historical report disappears: " + path);
            foreach (var scene in story.Scenes)
                foreach (var choice in scene.Nodes.SelectMany(n => n.Choices).Where(c => c.Requires.Contains(PageTaken)))
                {
                    var echoFormer = Program.Copy(former);
                    echoFormer.Flags.UnionWith(choice.Requires.Where(k => k != PageTaken && k != "trickster.now"));
                    check(!Rules.Match(choice.Requires, choice.Forbids, echoFormer),
                        "Foresight_PathChanged: echo selectable after path loss: " + scene.Id);
                }
        }

        // Never-Trickster control: unearned page flags derive no public keys.
        var off = World(story, 5, Accepted, Promise, Square, Caves, Raised, GateFire, GateWatch, memory.Id);
        check(!off.Has(PageTaken) && !off.Has(GateBelieved) && !off.Has(GoneSquare) && !off.Has(GoneCaves)
              && ours.All(s => !Avail(s, off) && !Avail(s, Later(off, 0, 3)))
              && reports.All(r => r.All(p => !Shown(p, World(story, 6, Accepted, Promise)))),
            "Foresight_OffTrickster: a foresight scene, key or paragraph shows off the Trickster path.");

        // The echoes (§2.4a): optional, appended last, neutral, Trickster-only, at most one per route per chapter, distinct.
        var hosts = story.Scenes.Where(s => s.Nodes.Any(n => n.Id.StartsWith("echo.", StringComparison.Ordinal))).ToArray();
        // Only coordinator-allocated echoes are exported (foresight.ALLOCATED, 06 "Echo slots"); tests/test_foresight_echo.py
        // exercises the API with allocations. Every exported echo is checked here.
        // 12 §2.9 budget: at most 8 route echoes mod-wide, 1 per route, 2 per chapter across the roster.
        var budgetHosts = hosts.Concat(new[] { pilot }).ToArray();
        var perChapter = budgetHosts.SelectMany(h => (h.Chapters.Length > 0 ? h.Chapters : Enumerable.Range(h.MinChapter, h.MaxChapter - h.MinChapter + 1)).Select(ch => ch));
        check(budgetHosts.Length <= 8 && budgetHosts.GroupBy(h => h.Relationship).All(g => g.Count() <= 1) && perChapter.GroupBy(x => x).All(g => g.Count() <= 2),
            "Foresight_EchoBudget: more than 8 route echoes, more than one for a route, or more than two in a chapter.");
        var entries = new List<string>();
        foreach (var host in hosts)
        {
            var echoNodes = host.Nodes.Where(n => n.Id.StartsWith("echo.", StringComparison.Ordinal)).ToList();
            var hostNode = host.Nodes.Single(n => n.Choices.Any(c => c.Next == echoNodes[0].Id));
            var echoChoices = hostNode.Choices.Where(c => c.Next != null && c.Next.StartsWith("echo.", StringComparison.Ordinal)).ToList();
            var own = hostNode.Choices.Take(hostNode.Choices.Count - echoChoices.Count).ToList();
            entries.Add(echoChoices[0].Text);
            check(hostNode.Choices.Skip(own.Count).All(echoChoices.Contains) && echoChoices.All(c => c.Set.Length == 0 && !c.Abort && c.Check == null
                      && c.Requires.Contains(PageTaken) && c.Requires.Contains("trickster.now") && c.Crusade != null && c.Crusade.Amount < 0),
                "Foresight_Echo: an echo in " + host.Id + " is not appended last, costs nothing, or sets, checks or skips anything.");
            string Sig(Choice c) => string.Join("|", c.Text, c.Next, c.Abort, string.Join(",", c.Set), string.Join(",", c.Requires), string.Join(",", c.Forbids),
                c.Check == null ? "" : c.Check.Skill + c.Check.DC + c.Check.Success + c.Check.Failure, c.NativeNext, c.Mythic, c.Crusade?.Amount);
            check(echoNodes.All(e => e.Choices.Select(Sig).SequenceEqual(own.Select(Sig))) && echoNodes.All(e => e.Text.Length < 1200 && e.Text.Contains("Shyka's page")),
                "Foresight_Echo: an echo in " + host.Id + " does not continue with the host node's own choices, or runs long.");
            var keys = echoChoices.SelectMany(c => c.Requires.Concat(c.Forbids)).Where(k => k != PageTaken && k != "trickster.now").Distinct().ToArray();
            for (int mask = 0; mask < 1 << keys.Length; mask++)
            {
                var held = new Snapshot();
                held.Flags.Add(PageTaken); held.Flags.Add("trickster.now");
                for (int i = 0; i < keys.Length; i++) if ((mask & (1 << i)) != 0) held.Flags.Add(keys[i]);
                check(echoChoices.Count(c => Rules.Match(c.Requires, c.Forbids, held)) == 1, "Foresight_Echo: echo variants in " + host.Id + " overlap or leave a gap.");
            }
            // Neutral: the scene's outcomes with the page taken are exactly its outcomes without it.
            var baseFlags = host.Requires.Where(f => !f.StartsWith("!", StringComparison.Ordinal)).Concat(new[] { "trickster", "trickster.ever" }).ToArray();
            var without = World(story, host.MinChapter, baseFlags);
            var with = World(story, host.MinChapter, baseFlags.Concat(new[] { Accepted, Caves, Square, Raised, GateFire, GateWatch }).ToArray());
            var a = new HashSet<string>(Program.Walk(host, without).Select(o => Key(o, without.Flags)));
            var b = new HashSet<string>(Program.Walk(host, with).Select(o => Key(o, with.Flags)));
            check(a.SetEquals(b), "Foresight_EchoNeutral: " + host.Id + " has different outcomes with the page.");
        }
        check(entries.Distinct().Count() == entries.Count && entries.All(e => !e.Contains("Shyka")), "Foresight_Echo: echo entries repeat or name the page.");

        // The memory gap: the Commander who sold the square knows it as told; the original answers are gated off, not removed.
        var square = S("terendelev.trickster.memory.square");
        var gapNode = N(square, "gap.square");
        check(gapNode.Choices.All(c => c.Next == "promise" && c.Set.Length == 0)
              && N(square, "scale").Choices[0].Forbids.Contains(GoneSquare) && N(square, "no_scale").Choices[0].Forbids.Contains(GoneSquare)
              && N(square, "scale").Choices.Last().Next == "gap.square" && N(square, "scale").Choices.Last().Requires.Contains(GoneSquare),
            "Foresight_Gap: Terendelev's memory page does not route a sold morning through the gap and back to her promise.");
        var sqBase = World(story, 3, "trickster", "trickster.ever", "terendelev.scale_held");
        var sqPaid = World(story, 3, "trickster", "trickster.ever", "terendelev.scale_held", Accepted, Promise, GateFire);
        visited.Clear();
        var paidOut = Program.Walk(square, sqPaid, (id, _) => visited.Add(id));
        check(visited.Contains("gap.square") && !visited.Contains("square")
              && new HashSet<string>(Program.Walk(square, sqBase).Select(o => Key(o, sqBase.Flags))).SetEquals(paidOut.Select(o => Key(o, sqPaid.Flags))),
            "Foresight_GapNeutral: the sold morning still plays as remembered, or changes the memory page's outcomes.");

        foreach (string suffix in new[] { "", "_awning" })
            foreach (string? sold in new string?[] { null, Promise, Square, Caves })
                foreach (string beat in new[] { "watch.proof", "after.first_night", "watch.market" })
                {
                    var flags = new List<string> { "trickster", "terendelev.trickster.returned" };
                    if (beat != "after.first_night") flags.Add("terendelev.trickster.first_night_seen");
                    if (sold != null) flags.AddRange(new[] { Accepted, sold });
                    var world = World(story, 5, flags.ToArray());
                    var host = S("terendelev.trickster." + beat + suffix);
                    var seen = new List<string>();
                    var result = Program.Walk(host, world, (id, _) => seen.Add(id));
                    var targets = beat == "watch.proof" ? new[] { "try" }
                        : beat == "watch.market" ? new[] { "ice" } : new[] { "turnips", "nothing", "breakfast" };
                    foreach (var target in targets)
                    {
                        bool gap = sold == Promise || sold == Square;
                        check(seen.Contains(gap ? "gap." + target : target) && !seen.Contains(gap ? target : "gap." + target),
                            "Foresight_GapWatch: sold memory selected the wrong wording: " + host.Id + "/" + target);
                    }
                    var bare = World(story, 5, flags.Where(f => f != Accepted && f != sold).ToArray());
                    check(new HashSet<string>(result.Select(o => Key(o, world.Flags)))
                              .SetEquals(Program.Walk(host, bare).Select(o => Key(o, bare.Flags))),
                        "Foresight_GapWatch: memory wording changed outcomes: " + host.Id);
                }

        // Earned gates remain legitimate; the page itself stays optional.
        check(ours.Where(s => !s.Reaction).All(s => s.Optional), "Foresight_Optional: a foresight scene is not optional.");
        Console.WriteLine("PASS: Shyka's page (12): the bargain and its prices, the memory and its fallback, the misstep, the Chapter 5 line, the witnesses, Last Call, the Ledger, the gate contract, off-Trickster, the echo budget and the gap.");
    }
}
