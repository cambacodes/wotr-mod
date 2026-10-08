using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Anevia, Trickster (Writer/handoffs/trickster/anevia.md): the wardrobe in Kenabres (F01), her return through Irabeth,
// the confession, the gate, the commit and her no. One block per spec rules test (Trk_Anevia_*), plus the Irabeth
// items that waited on her return, the shared table (Trk_Tirabade_TableAgain) and the one-page epilogue arbitration.
internal static class AneviaTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Contact = "b5e867e13503c6f41bb1316705efb4a2";
    private const string IrabethContact = "280d4712dceb37f4a88e98f1f4c6e64f";
    private const string Returned = "anevia.trickster.returned";
    private const string Primed = "anevia.trickster.primed";
    private const string IrabethReturned = "irabeth.trickster.returned";
    private const string Killed = "anevia.irabeth_killed_by_commander";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000,
            // eng-final / E-Q8-10: fund these positive histories; the walker enforces every debit.
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        foreach (var context in flags.Where(story.Derived.ContainsKey))
            HouseholdTests.Earn(story, state, context);
        state.AvailableContacts.Add(Contact);
        state.AvailableContacts.Add(IrabethContact);
        Rules.Complete(story, state);
        foreach (var latch in story.Latches.Keys.Where(state.Has)) state.Times[latch] = state.Hour - 24;
        if (state.Has("trickster.ever")) state.Times["trickster.ever"] = state.Hour - 1000;   // the path was taken long before
        // Authored flags in a fixture were set long ago unless a test says otherwise.
        foreach (var flag in flags.Where(f => !state.Times.ContainsKey(f))) state.Times[flag] = state.Hour - 1000;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours)
    {
        var later = Program.Copy(state); later.Hour += hours; Rules.Complete(story, later); return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var setup = S("anevia.trickster.gone.setup");
        var wardrobe = S("anevia.trickster.gone.wardrobe");
        var fetched = S("anevia.trickster.gone.fetched");
        var confession = S("anevia.trickster.gone.confession");
        var gate = S("anevia.trickster.gone.gate");
        var commit = S("anevia.trickster.gone.commit");
        var letterTwin = S("anevia.trickster.gone.commit_letter");
        var second = S("anevia.trickster.gone.second_ask");
        var returns = new[] { wardrobe, fetched, confession };
        var grief = new[] { S("anevia.a_grief_with_a_name"), S("anevia.ending_grief_unanswered"), S("anevia.ending_wife_killed") };
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));

        // Hooks: the devices are delivered at rest (her room in Kenabres has no engine area); their kind is checked below.
        // The gate beats are on her own hub.
        check(new[] { setup, wardrobe, fetched, confession, letterTwin }.All(s => s.Remote), "An Anevia rest-delivered device became physical.");
        check(new[] { setup, wardrobe, fetched, confession }.All(s => s.TricksterDevice && s.TricksterState == "gone"), "Device states mislabelled.");
        check(new[] { gate, commit, second }.All(s => s.AnswerLists.SequenceEqual(new[] { "33960c7f7af40cd43b7f801a76c87a0b" })
              && s.ContactUnit == Contact && !s.TricksterDevice), "Gate beats left her own hub.");
        var rel = story.Relationships["anevia"];
        check(rel.UnavailableOverrides.TryGetValue("anevia_gone", out var over) && over == Returned
              && rel.TricksterAccess.Count == 1 && rel.TricksterAccess["gone"].Device == setup.Id, "Anevia relationship patch missing.");
        check(story.Presences.TryGetValue("anevia.presence", out var presence) && presence.Unit == Contact && presence.Mode == "reuse-native"
              && presence.At?.NearUnit == "15f754455d1d87c42a4e14df456d5415" && presence.Requires.Contains(Returned),
            "Anevia presence is not anchored at the smith by the gate.");
        // Polish b6b: Gesmerha and Hepzamirah stand at the smith's sides (2.5); Anevia keeps her own spot out on the road.
        check(presence!.At!.Side == "front" && presence.At.Distance >= 6f && presence.At.Distance <= 10f
              && story.Presences.Where(kv => kv.Key != "anevia.presence" && kv.Value.At?.NearUnit == presence.At.NearUnit)
                   .All(kv => {
                       var a = Rules.AnchorOffset(presence.At, 0);
                       var b = Rules.AnchorOffset(kv.Value.At!, 0);
                       return Math.Sqrt(Math.Pow(a.Dx - b.Dx, 2) + Math.Pow(a.Dz - b.Dz, 2)) >= 4;
                   }),
            "Anevia is crowded back into the smith's corner.");
        var tirabade = story.Relationships["tirabade"];
        check(tirabade.UnavailableOverrides["irabeth_dead"] == IrabethReturned && tirabade.UnavailableOverrides["anevia_gone"] == Returned,
            "Tirabade relationship does not come back with both women.");

        // Trk_Anevia_Gone_Wardrobe: the paid knock, then the wardrobe a day later; fetched stays shut.
        var known = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", "closets.known");
        check(Rules.Available(story, setup, known) && !Any(known, fetched, confession, wardrobe), "Trk_Anevia_Gone_Wardrobe: wrong device.");
        var knocks = Program.Walk(setup, known);
        var paid = knocks.Single(r => r.Has("anevia.trickster.cost.socoth_listening"));
        var pay = setup.Nodes.Single(n => n.Id == "socoth").Choices[0];
        check(paid.Has(Primed) && pay.Alignment?.Direction == "Chaotic" && pay.Alignment.Value == 1 && pay.Mythic == "PlayerIsTrickster",
            "The paid knock is free.");
        check(knocks.Any(r => r.Has("anevia.trickster.cost.wrong_door")) && knocks.Any(r => !r.Has(setup.Id) && !r.Has(Primed)),
            "Haggle or the abort is missing.");
        check(!knocks.Any(r => r.Has("anevia.trickster.cost.stolen_door") || r.Has("anevia.trickster.cost.crated")),
            "The kept closet or the crate is offered while Socothbenoth answers.");
        check(!Rules.Available(story, wardrobe, Later(story, paid, 23)) && Rules.Available(story, wardrobe, Later(story, paid, 24))
              && !Rules.Available(story, fetched, Later(story, paid, 24)), "Wardrobe mistimed, or fetched survives the setup.");
        check(!Rules.Available(story, setup, World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead")),
            "Setup opens with no closet doctrine and no expired Council.");

        // Trk_Anevia_Gone_KeptCloset: the treasure closet, kept not spent, at a Favors price.
        var kept = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", "closets.known", "socot.gone");
        check(Rules.Available(story, setup, kept), "Trk_Anevia_Gone_KeptCloset: setup unavailable.");
        var closet = Program.Walk(setup, kept).Where(r => r.Has(Primed)).ToList();
        check(closet.Count == 1 && closet[0].Has("anevia.trickster.cost.stolen_door"), "Trk_Anevia_Gone_KeptCloset: wrong door.");
        var open = setup.Nodes.Single(n => n.Id == "door").Choices.Single();
        check(open.Crusade?.Resource == "Favors" && open.Crusade.Amount == -100 && open.Requires.Contains("trickster"), "Kept closet is free.");

        // Trk_Anevia_Gone_Crate: no demon, no door; posted south at a Materials price.
        var crateWorld = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", "council.fought");
        check(Rules.Available(story, setup, crateWorld), "Trk_Anevia_Gone_Crate: setup unavailable.");
        var crated = Program.Walk(setup, crateWorld).Where(r => r.Has(Primed)).ToList();
        check(crated.Count == 1 && crated[0].Has("anevia.trickster.cost.crated"), "Trk_Anevia_Gone_Crate: wrong route.");
        var crate = setup.Nodes.Single(n => n.Id == "crate").Choices.Single();
        check(crate.Crusade?.Resource == "Materials" && crate.Crusade.Amount == -100, "The crate is free.");

        // Trk_Anevia_Gone_Return and the wardrobe variants.
        var primed = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", Primed);
        check(Rules.Available(story, wardrobe, primed) && !Any(primed, fetched, confession, gate), "Trk_Anevia_Gone_Return: wrong scenes.");
        foreach (var cost in new[] { "", "anevia.trickster.cost.wrong_door", "anevia.trickster.cost.stolen_door", "anevia.trickster.cost.crated",
                                     "anevia.trickster.cost.socoth_listening" })
        foreach (var beth in new[] { "", IrabethReturned, "irabeth.trickster.declined" })
        {
            var start = Program.Copy(primed);
            if (cost != "") start.Flags.Add(cost);
            if (beth != "") start.Flags.Add(beth);
            var pages = new HashSet<string>();
            var back = Program.Walk(wardrobe, start, (page, _) => pages.Add(page));
            check(back.Count == 1 && back[0].Has(Returned) && back[0].Has("anevia.trickster.cost.wardrobe_nailed") && back[0].Has("anevia.started"),
                "Trk_Anevia_Gone_Return: the wardrobe does not return her.");
            check(back[0].Has("anevia.trickster.cost.thrown_out") == cost.EndsWith("socoth_listening"), "The listener is not thrown out.");
            check(pages.Contains("wimple") == cost.EndsWith("wrong_door") && pages.Contains("stolen") == cost.EndsWith("stolen_door")
                  && pages.Contains("lid") == cost.EndsWith("crated") && pages.Contains("beth_back") == (beth == IrabethReturned)
                  && pages.Contains("rest") == (beth == "irabeth.trickster.declined"), "Wardrobe variants ignore the route or Beth.");
            var after = Later(story, back[0], 47);
            check(!Any(after, returns) && !Rules.Available(story, gate, after) && Rules.Available(story, gate, Later(story, after, 1))
                  && !Rules.Available(story, commit, Later(story, after, 1)), "Gate mistimed, or a second return opened.");
            check(!Rules.Failed(rel, back[0]), "Journal still fails after her return.");
        }

        // The Commander's own blow at Iz, not undone: she faces her wife's killer, and says so.
        foreach (bool owned in new[] { false, true })
        {
            var killer = Program.Copy(primed); killer.Flags.Add(Killed);
            if (owned) killer.Flags.Add("irabeth.trickster.declined");
            var pages = new HashSet<string>();
            var back = Program.Walk(wardrobe, killer, (page, _) => pages.Add(page));
            check(back.Count == 1 && back[0].Has(Returned) && pages.Contains("killer") && !pages.Contains("beth_dead")
                  && pages.Contains("owned") == owned, "The wardrobe forgets who killed Beth.");
            var ask = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", Killed, Returned, "anevia.trickster.gate_seen");
            ask.Times["anevia.trickster.gate_seen"] = ask.Hour - 96;
            var commitPages = new HashSet<string>();
            Program.Walk(commit, ask, (page, _) => commitPages.Add(page));
            var killerOutcomes = Program.Walk(commit, ask, (page, _) => commitPages.Add(page));
            check(commitPages.Contains("widow_killed") && commitPages.Contains("said") && !commitPages.Contains("widow"), "The commit forgets whose sword it was.");
            check(killerOutcomes.All(r => !r.Has("anevia.committed")), "The killer reaches the commitment before the muster.");
        }

        // Both Tirabades left at the Coronation (IrabethGone, Beth alive): no beat speaks of Beth as dead.
        {
            var bothLeft = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_gone", "closets.known", "socot.gone");
            check(Rules.Available(story, setup, bothLeft), "Both left: the wardrobe setup is unavailable.");
            var leftPrimed = Program.Walk(setup, bothLeft).Single(r => r.Has(Primed));
            var leftPages = new HashSet<string>();
            var leftBack = Program.Walk(wardrobe, Later(story, leftPrimed, 24), (page, _) => leftPages.Add(page));
            check(leftBack.Count == 1 && leftBack[0].Has(Returned) && leftPages.Contains("beth_left")
                  && !leftPages.Contains("beth_dead") && !leftPages.Contains("killer") && !leftPages.Contains("beth_back"),
                "Both left: the wardrobe treats a living, departed Beth as dead or returned.");
            var leftGateWorld = Later(story, leftBack[0], 48);
            check(Rules.Available(story, gate, leftGateWorld), "Both left: the gate is unavailable.");
            var gatePages = new HashSet<string>();
            var leftGate = Program.Walk(gate, leftGateWorld, (page, _) => gatePages.Add(page));
            check(gatePages.Contains("beth_left") && gatePages.Contains("told_left") && !gatePages.Contains("beth_widow")
                  && !gatePages.Contains("told") && !gatePages.Contains("beth_back"),
                "Both left: the gate treats a living, departed Beth as dead.");
            var handTaken = leftGate.Single(r => r.Has("anevia.trickster.hand_taken"));
            var commitWorld = Later(story, handTaken, 96);
            check(Rules.Available(story, commit, commitWorld), "Both left: the commit is unavailable.");
            var commitLeftPages = new HashSet<string>();
            var leftCommit = Program.Walk(commit, commitWorld, (page, _) => commitLeftPages.Add(page));
            check(commitLeftPages.Contains("left") && commitLeftPages.Contains("morning_left") && !commitLeftPages.Contains("widow")
                  && !commitLeftPages.Contains("morning") && leftCommit.Any(r => r.Has("anevia.committed")),
                "Both left: the commit treats a living, departed Beth as dead, or cannot commit.");
            check(leftCommit.Any(r => r.Has("anevia.partner_stance.share") && r.Has("anevia.committed") && !r.Has("anevia.closed")),
                "Both left: sharing loses the absent wife's letter.");
            check(leftCommit.Any(r => r.Has("anevia.partner_stance.exclusive") && r.Has("anevia.closed") && !r.Has("anevia.committed")),
                "Both left: exclusivity bypasses the refusal.");
            check(leftCommit.Any(r => r.Has("anevia.partner_stance.secret") && r.Has("anevia.partner_lie_exposed") && r.Has("anevia.closed")),
                "Both left: the careless affair loses discovery.");
        }

        // Trk_Anevia_Coexistence_*: at most one return; Irabeth's state never gates the wardrobe.
        var withBeth = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", IrabethReturned, Primed);
        check(Rules.Available(story, wardrobe, withBeth) && !Any(withBeth, fetched, confession), "Trk_Anevia_Coexistence_Primed failed.");
        var bethClosed = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", "irabeth.closed", Primed);
        check(Rules.Available(story, wardrobe, bethClosed) && !Any(bethClosed, fetched, confession), "Trk_Anevia_Coexistence_Closed failed.");
        var both = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", IrabethReturned, "irabeth.trickster.blow_rewritten",
                         Killed, Returned, "anevia.lover");
        check(Rules.Available(story, gate, both) && !Any(both, returns) && !Any(both, grief), "Trk_Anevia_Coexistence_Returned failed.");

        // Trk_Anevia_GriefGuard: no grief over a wife who has come back.
        var guard = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", "anevia_gone", IrabethReturned, Returned, "anevia.lover");
        check(!Any(guard, grief) && !Any(World(story, 6, "trickster", "trickster.ever", "irabeth_dead", "anevia_gone", IrabethReturned, Returned, "anevia.lover"), grief),
            "Trk_Anevia_GriefGuard: a grief page for a living wife.");

        // Trk_Anevia_Fetched: Irabeth rides south for her; the bargain is told.
        var fetch = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", IrabethReturned, "irabeth.trickster.cost.under_orders");
        check(Rules.Available(story, fetched, fetch) && !Any(fetch, wardrobe, confession), "Trk_Anevia_Fetched: wrong device.");
        var fetchPages = new HashSet<string>();
        var brought = Program.Walk(fetched, fetch, (page, _) => fetchPages.Add(page));
        check(brought.Count == 2 && brought.All(r => r.Has(Returned) && r.Has("anevia.trickster.cost.knows_the_bargain")) && fetchPages.Contains("bargain"),
            "Trk_Anevia_Fetched: the letters do not return her, or the bargain is untold.");
        check(Rules.Available(story, gate, Later(story, brought[0], 48)), "Gate unreachable after the fetch.");
        var joked = brought.Single(r => r.Has("anevia.trickster.told_the_joke"));
        var jokePages = new HashSet<string>();
        Program.Walk(gate, Later(story, joked, 48), (page, _) => jokePages.Add(page));
        check(jokePages.Contains("joke") && jokePages.Contains("beth_back") && jokePages.Contains("beth_terms"), "Gate forgets the joke or Beth.");
        check(Program.Walk(gate, Later(story, joked, 48)).All(r => r.Has("anevia.trickster.shares_beth")), "Anevia's terms for Beth are not recorded.");
        check(Program.Walk(gate, Later(story, brought.Single(r => !r.Has("anevia.trickster.told_the_joke")), 48)).All(r => r.Has("anevia.trickster.shares_beth")),
            "Anevia's terms for Beth depend on the joke.");

        // Trk_Anevia_Confession / _Lie: after the rewritten blow she wants the version that hurts.
        var rewritten = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", Killed, IrabethReturned, "irabeth.trickster.blow_rewritten");
        check(Rules.Available(story, confession, rewritten) && !Any(rewritten, fetched, wardrobe), "Trk_Anevia_Confession: wrong device.");
        var told = Program.Walk(confession, rewritten);
        check(told.Count == 1 && told[0].Has(Returned) && told[0].Has("anevia.trickster.cost.accounting") && !told[0].Has("anevia.trickster.cost.lie_exposed"),
            "Trk_Anevia_Confession: the truth does not return her, or the lie is offered to an honest Commander.");
        var lied = Program.Copy(rewritten); lied.Flags.Add("irabeth.trickster.cost.accounting_lied");
        var exposed = Program.Walk(confession, lied).Where(r => r.Has("anevia.trickster.cost.lie_exposed")).ToList();
        check(exposed.Count == 1 && exposed[0].Has(Returned), "Trk_Anevia_Confession_Lie: the lie is not exposed.");

        // Trk_Anevia_Gone_Commit / Trk_Anevia_Gone_Refusal: Beth first, her terms, her no.
        foreach (int beth in new[] { 0, 1, 2 })   // 0 widow, 1 Beth back and has not asked, 2 Beth back and asked Anevia herself
        foreach (bool listening in new[] { false, true })
        {
            bool bethBack = beth > 0, bethAsked = beth == 2;
            var ask = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", Returned, "anevia.trickster.gate_seen");
            if (bethBack) ask.Flags.Add(IrabethReturned);
            if (bethAsked) ask.Flags.Add("irabeth.trickster.asked_nevi");
            if (listening) ask.Flags.Add("anevia.trickster.cost.socoth_listening");
            ask.Times["anevia.trickster.gate_seen"] = ask.Hour - 96;
            check(Rules.Available(story, commit, ask) && !Rules.Available(story, second, ask), "Trk_Anevia_Gone_Commit: commit unavailable.");
            check(!Rules.Available(story, commit, Later(story, ask, -1)), "Commit ignores the delay after the gate.");
            var pages = new HashSet<string>();
            var outcomes = Program.Walk(commit, ask, (page, _) => pages.Add(page));
            // Two openings ([Ask her to stay] / [Say nothing and wait]) lead to the same terms.
            if (!bethBack)
                check(outcomes.Count(r => r.Has("anevia.committed")) == 2
                      && outcomes.All(r => !r.Has("anevia.partner_stance.share") && !r.Has("anevia.partner_stance.exclusive") && !r.Has("anevia.partner_stance.secret")),
                    "Widow commitment invents a living-wife stance.");
            else
            {
                check(outcomes.Any(r => r.Has("anevia.committed") && r.Has("anevia.partner_stance.share") && !r.Has("anevia.closed")),
                    "A living wife prevents negotiated sharing.");
                check(outcomes.Any(r => r.Has("anevia.partner_stance.exclusive") && r.Has("anevia.closed") && !r.Has("anevia.committed")),
                    "An exclusive demand overrides Anevia's refusal.");
                check(outcomes.Any(r => r.Has("anevia.partner_stance.secret") && r.Has("anevia.committed") && r.Has("anevia.partner_lie_exposed") && r.Has("anevia.closed")),
                    "The discovered affair loses its commitment or its consequence.");
                check(outcomes.Where(r => r.Has("anevia.closed")).All(r => !r.Has("irabeth.closed") && !r.Has("tirabade.group_closed")),
                    "Anevia's stance closes another relationship.");
            }
            check(pages.Contains("threshold") && pages.Contains(bethAsked ? "morning_back" : bethBack ? "morning_quiet" : "morning")
                  && pages.Contains("coats") == listening
                  && pages.Contains(bethAsked ? "share" : bethBack ? "share_quiet" : "widow"), "Commit skips the intimate beat or a variant.");
            // Sol COX: Anevia never reports Beth's ask, or promises Beth's night, unless Beth has asked her herself.
            check(bethAsked || !pages.Contains("share") && !pages.Contains("morning_back"), "Anevia answers for her wife.");
            var no = outcomes.Where(r => r.Has("anevia.trickster.declined")).ToList();
            check(no.Count == 4 && no.All(r => !r.Has("anevia.committed") && !r.Has("irabeth.closed") && !r.Has("tirabade.group_closed")),
                "Trk_Anevia_Gone_Refusal: her no is missing from a branch, or it touches another route.");
            check(!Rules.Available(story, commit, no[0]) && !Rules.Available(story, second, Later(story, no[0], 95))
                  && Rules.Available(story, second, Later(story, no[0], 96)), "The priced second ask is mistimed.");
            var asked = new HashSet<string>();
            var finals = Program.Walk(second, Later(story, no[0], 96), (page, _) => asked.Add(page));
            check(finals.Any(r => r.Has("anevia.committed") && r.Has("anevia.trickster.cost.her_key")) && finals.Any(r => r.Has("anevia.closed") && !r.Has("anevia.committed"))
                  && asked.Contains("night"), "Second ask: no key, no hard no, or no night.");
        }
        check(!Rules.Available(story, letterTwin, World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", Returned)),
            "The letter twin opens while the gate presence can be placed.");
        var failedAnchor = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", Returned, "anevia.presence.failed");
        var byPost = Program.Walk(letterTwin, Later(story, failedAnchor, 96));
        check(byPost.Count > 0 && byPost.All(r => !r.Has("anevia.committed") && r.Has("anevia.trickster.gate_seen")),
            "The letter twin commits by post instead of leaving it for a real door.");

        // Trk_Anevia_PathFailed: canon fate stands.
        var failed = World(story, 5, "trickster.was", "trickster.ever", "trickster.failed", "anevia_gone", "irabeth_dead", "closets.known");
        check(!Any(failed, setup, wardrobe), "Trk_Anevia_PathFailed: a device survives the lost path.");

        // Trk_Tirabade_TableAgain: both back, three chairs; the shared route commits on its own flag.
        var table = S("tirabade.trickster.table_again");
        var chairs = S("tirabade.trickster.third_chair");
        var reunited = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", "anevia_gone", IrabethReturned, Returned);
        check(Rules.Available(story, table, reunited), "Trk_Tirabade_TableAgain: table unavailable.");
        var third = Program.Walk(table, reunited).Single(r => r.Has("tirabade.trickster.third_chair"));
        var dealt = Program.Walk(chairs, Later(story, third, 72));
        check(dealt.Any(r => r.Has("committed")) && dealt.Any(r => r.Has("tirabade.trickster.declined") && !r.Has("committed")),
            "The third chair does not commit the shared route, or has no soft no.");
        check(!Rules.Available(story, chairs, Later(story, third, 71)), "Third chair mistimed.");
        var accounting = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", "anevia_gone", IrabethReturned, Returned, Killed, "irabeth.trickster.blow_rewritten");
        var accountingPages = new HashSet<string>();
        var accounted = Program.Walk(table, accounting, (page, _) => accountingPages.Add(page));
        check(accountingPages.Contains("accounting") && accounted.Where(r => r.Has("tirabade.trickster.third_chair")).All(r => r.Has("anevia.trickster.cost.accounting")),
            "The third chair is offered before Anevia hears the accounting.");
        // Epilogue arbitration: exactly one Anevia page for every returned history, with her paragraphs.
        foreach (bool lover in new[] { false, true })
        foreach (string outcome in new[] { "", "anevia.committed", "anevia.trickster.declined", "anevia.closed", "anevia.trickster.friends", "anevia.trickster.gate_seen" })
        foreach (string beth in new[] { "", IrabethReturned, Killed })
        {
            var end = World(story, 6, "trickster", "trickster.ever", "irabeth_dead", "anevia_gone", Returned, "anevia.trickster.cost.wardrobe_nailed");
            if (lover) end.Flags.Add("anevia.lover");
            if (outcome != "") end.Flags.Add(outcome);
            if (beth != "") end.Flags.Add(beth);
            Rules.Complete(story, end);
            var pages = story.Scenes.Where(s => s.Relationship == "anevia" && s.Owner == "Epilogue" && Rules.Available(story, s, end)).ToList();
            // Coarse commitment can retain a nonromantic fate recap, but cannot acquire the lovers' payoff.
            int expected = outcome == "anevia.committed" && !end.Has("anevia.payoff.ordinary") && lover ? 0 : 1;
            check((outcome == "anevia.committed" && !end.Has("anevia.payoff.ordinary")) ? pages.Count <= 1 && pages.All(p => !p.Requires.Any(k => k.Contains(".payoff."))) : pages.Count == expected, "Anevia epilogue: " + pages.Count + " pages for lover=" + lover + " outcome=" + outcome + " beth=" + beth
                                    + " (" + string.Join(",", pages.Select(s => s.Id)) + ")");
            if (pages.Count == 1)
                check(Rules.VisibleParagraphs(pages[0].Nodes.Last(), end).Length >= 1, "Returned Anevia's page has none of her paragraphs: " + pages[0].Id);
        }
        // Sol INT: the Commander killed Beth, Anevia came back and chose the Commander anyway; the closure page does not deny it.
        var unforgiven = World(story, 6, "trickster", "trickster.ever", "irabeth_dead", "anevia_gone", Returned, Killed, "anevia.lover", "anevia.committed",
                               "anevia.trickster.terms_kept", "anevia.trickster.said_it", "anevia.trickster.cost.muster_confession");
        var unforgivenPages = story.Scenes.Where(s => s.Relationship == "anevia" && s.Owner == "Epilogue" && Rules.Available(story, s, unforgiven)).ToList();
        check(unforgivenPages.Count == 1 && unforgivenPages[0].Id == "anevia.trickster.epilogue.nailed_wardrobe_unforgiven"
              && Rules.VisibleParagraphs(unforgivenPages[0].Nodes.Last(), unforgiven).Contains(unforgivenPages[0].Nodes.Last().Paragraphs[11]),
            "The recommitted Anevia gets the ending that denies her night: " + string.Join(",", unforgivenPages.Select(s => s.Id)));
        // Sol r1 INT: the renewed widow (Beth dead, not by the Commander) keeps her night too.
        var widowRenewed = World(story, 6, "trickster", "trickster.ever", "irabeth_dead", "anevia_gone", Returned, "anevia.lover", "anevia.committed",
                                 "anevia.trickster.terms_kept", "anevia.trickster.gate_seen");
        var widowPages = story.Scenes.Where(s => s.Relationship == "anevia" && s.Owner == "Epilogue" && Rules.Available(story, s, widowRenewed)).ToList();
        check(widowPages.Count == 1 && widowPages[0].Id == "anevia.trickster.epilogue.nailed_wardrobe_widow",
            "The renewed widow gets a page that denies her night: " + string.Join(",", widowPages.Select(s => s.Id)));
        // Sol r1 BEL: after the Commander killed Beth, the door has a price paid in public, and the second ask cannot skip it.
        var penanceWorld = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", Killed, Returned, "anevia.trickster.gate_seen",
                                 "anevia.lover");
        penanceWorld.Times["anevia.trickster.gate_seen"] = penanceWorld.Hour - 96;
        var penancePages = new HashSet<string>();
        var penanceOut = Program.Walk(commit, penanceWorld, (page, _) => penancePages.Add(page));
        check(penancePages.Contains("penance") && penancePages.Contains("promise") && penanceOut.All(r => !r.Has("anevia.committed")),
            "She commits to her wife's killer before the muster.");
        var promised = penanceOut.Single(r => r.Has("anevia.trickster.said_it"));
        var muster = S("anevia.trickster.gone.muster");
        check(!Rules.Available(story, muster, Later(story, promised, 11)) && Rules.Available(story, muster, Later(story, promised, 12)), "The muster is mistimed.");
        var musterPages = new HashSet<string>();
        var mustered = Program.Walk(muster, Later(story, promised, 12), (page, _) => musterPages.Add(page));
        check(musterPages.Contains("yard") && mustered.All(r => !r.Has("anevia.committed"))
              && mustered.Any(r => r.Has("anevia.trickster.cost.muster_confession") && r.Has("anevia.trickster.declined")),
            "The public confession is not played, or it buys the door at once.");
        // Sol r4 BEL: the muster buys the gate; her own later decision (the second ask) opens the door.
        var afterMuster = mustered.First(r => r.Has("anevia.trickster.cost.muster_confession"));
        var laterPages = new HashSet<string>();
        var later = Program.Walk(second, Later(story, afterMuster, 96), (page, _) => laterPages.Add(page));
        check(later.Any(r => r.Has("anevia.committed")) && !laterPages.Contains("say_it"), "After the muster the second ask cannot open the door.");
        // Sol r4 INT: a Trickster commitment does not restart the registered courtship from its first scenes.
        var committedAtGate = World(story, 5, "trickster", "trickster.ever", "anevia_gone", "irabeth_dead", Returned, IrabethReturned, "anevia.committed",
                                    "anevia.trickster.terms_kept", "anevia_away");
        check(!Rules.Available(story, S("anevia.unborrowed_hour"), Later(story, committedAtGate, 500))
              && !Rules.Available(story, S("anevia.a_question_at_home"), Later(story, committedAtGate, 500)),
            "The gate commitment reopens the courtship's first scenes.");
        var killedNo = penanceOut.First(r => r.Has("anevia.trickster.declined") && !r.Has("anevia.trickster.said_it"));
        var sayPages = new HashSet<string>();
        var sayOut = Program.Walk(second, Later(story, killedNo, 96), (page, _) => sayPages.Add(page));
        check(sayPages.Contains("say_it") && sayOut.All(r => !r.Has("anevia.committed")), "The second ask trades the murder for an unrelated secret.");
        // Sol r5 INT: the promise leaves the second ask open; muster, then the second ask, reaches the door.
        var promisedAgain = sayOut.First(r => r.Has("anevia.trickster.said_it") && !r.Has(second.Id));
        check(Rules.Available(story, second, promisedAgain), "The promise closes the second ask.");
        var waitPages = new HashSet<string>();
        check(Program.Walk(second, promisedAgain, (page, _) => waitPages.Add(page)).All(r => !r.Has("anevia.committed")) && waitPages.Contains("wait_muster"),
            "Coming back before muster opens the door, or has no answer.");
        check(Rules.Available(story, muster, Later(story, promisedAgain, 12)), "The muster does not follow the second-ask promise.");
        var penancePaid = Program.Walk(muster, Later(story, promisedAgain, 12)).First(r => r.Has("anevia.trickster.cost.muster_confession"));
        check(Rules.Available(story, second, penancePaid) && Program.Walk(second, penancePaid).Any(r => r.Has("anevia.committed")),
            "After the muster the second ask cannot open the door.");
        // A Commander who was never her lover and killed her wife gets no door (the stranger branch).
        var stranger = Program.Copy(penanceWorld); stranger.Flags.Remove("anevia.lover");
        var strangerPages = new HashSet<string>();
        var strangerOut = Program.Walk(commit, stranger, (page, _) => strangerPages.Add(page));
        check(strangerPages.Contains("stranger") && !strangerPages.Contains("penance") && strangerOut.All(r => !r.Has("anevia.committed")),
            "A stranger who killed her wife is offered her door.");
        var closure = World(story, 6, "irabeth_dead", Killed, "anevia.lover");
        check(Rules.Available(story, S("anevia.ending_wife_killed"), closure), "The closure page is gone for a lover who never came back.");
        // Sol pol INT: the rendered "wife killed" ending says where each played history left her, never "gone" after a soft no.
        string EndingText(Snapshot history, out int pageCount)
        {
            var end = Program.Copy(history); end.Chapter = 6; Rules.Complete(story, end);
            var pages = story.Scenes.Where(s => s.Relationship == "anevia" && s.Owner == "Epilogue" && Rules.Available(story, s, end)).ToList();
            pageCount = pages.Count(s => s.Id == "anevia.ending_wife_killed") == 1 ? pages.Count : -pages.Count;
            if (pages.Count != 1 || pages[0].Id != "anevia.ending_wife_killed") return "";
            var node = pages[0].Nodes.Last();
            return string.Join("\n", new[] { SurfaceIds.Of(story, node) }.Concat(Rules.VisibleParagraphs(node, end).Select(x => SurfaceIds.Of(story, x))));
        }
        int VariantCount(string visible) => SurfaceIds.Count(visible, "[anevia.ending_wife_killed/end/paragraph/0][anevia.ending_wife_killed/end/paragraph/1][anevia.ending_wife_killed/end/paragraph/2][anevia.ending_wife_killed/end/paragraph/3]");
        // Refused at the penance (private admission only): the unpaid soft no and her letters, nothing closed or paid.
        var refusedText = EndingText(killedNo, out var refusedPages);
        check(refusedPages == 1 && SurfaceIds.Has(refusedText, "[anevia.ending_wife_killed/end/paragraph/1]") && SurfaceIds.Has(refusedText, "[anevia.ending_wife_killed/end/paragraph/18]") && VariantCount(refusedText) == 1
              && !SurfaceIds.Has(refusedText, "[anevia.ending_wife_killed/end/paragraph/17]") && !killedNo.Has("anevia.trickster.cost.muster_confession"),
            "Wife-killed ending after her soft no: " + refusedText);
        // Promised again at the second ask but never said at muster: still unpaid.
        var promisedText = EndingText(promisedAgain, out var promisedPages);
        check(promisedPages == 1 && SurfaceIds.Has(promisedText, "[anevia.ending_wife_killed/end/paragraph/1]") && SurfaceIds.Has(promisedText, "[anevia.ending_wife_killed/end/paragraph/18]") && VariantCount(promisedText) == 1
              && !SurfaceIds.Has(promisedText, "[anevia.ending_wife_killed/end/paragraph/17]"), "Wife-killed ending after an unkept promise: " + promisedText);
        // Said at muster, walked back to the road, never asked again: paid for the gate, not the door.
        var paidText = EndingText(afterMuster, out var paidPages);
        check(afterMuster.Has("anevia.trickster.declined") && !afterMuster.Has("anevia.committed") && paidPages == 1
              && SurfaceIds.Has(paidText, "[anevia.ending_wife_killed/end/paragraph/2]") && SurfaceIds.Has(paidText, "[anevia.ending_wife_killed/end/paragraph/17]") && VariantCount(paidText) == 1,
            "Wife-killed ending after the paid muster: " + paidText);
        // Never came back: the permanent closure stands alone. Came back without a soft no: the neutral line.
        var closureText = EndingText(closure, out var closurePages);
        check(closurePages == 1 && SurfaceIds.Has(closureText, "[anevia.ending_wife_killed/end/paragraph/0]") && VariantCount(closureText) == 1, "Closure page lost its closure: " + closureText);
        foreach (var extra in new[] { "", "anevia.trickster.gate_seen", "anevia.trickster.friends" })
        {
            var back = World(story, 5, "trickster", "trickster.ever", "irabeth_dead", "anevia_gone", Killed, "anevia.lover", Returned);
            if (extra == "anevia.trickster.gate_seen") { back.Flags.Add(extra); back.Flags.Add("anevia.trickster.hand_taken"); }
            else if (extra != "") back.Flags.Add(extra);
            var backText = EndingText(back, out var backPages);
            check(backPages == 1 && SurfaceIds.Has(backText, "[anevia.ending_wife_killed/end/paragraph/3]") && VariantCount(backText) == 1,
                "Wife-killed ending for a returned Anevia without a soft no (" + extra + "): " + backText);
        }
        // Presentation: the setup and the wardrobe are encounters delivered at rest, not correspondence.
        check(Rules.KindOf(setup) == "visit" && Rules.KindOf(wardrobe) == "visit" && Rules.KindOf(confession) == "visit"
              && Rules.KindOf(fetched) == "letter" && Rules.KindOf(letterTwin) == "letter",
            "Anevia's devices are presented as the wrong kind (setup/wardrobe/confession visits; fetched and the twin letters).");
        // The kept closet opens onto her room once: setup finds the room and does not open it.
        var stayed = World(story, 6, "anevia.lover", "anevia.committed", "anevia.developed");
        var stayedParagraphs = Rules.VisibleParagraphs(S("anevia.ending_kept").Nodes.Last(), stayed);
        check(stayedParagraphs.Length == 1 && stayedParagraphs.All(p => !p.Requires.Contains(Returned)),
            "The stayed ending loses its current wife state or leaks a Trickster return paragraph.");
        var widowed = World(story, 6, "irabeth_dead", "anevia_gone", "anevia.lover");
        check(Rules.Available(story, S("anevia.ending_gone"), widowed)
              && !Rules.Available(story, S("anevia.ending_gone"), World(story, 6, "irabeth_dead", "anevia_gone", "anevia.lover", Returned)),
            "Canon departure page lost, or shown for a returned Anevia.");

        // Reactions: Konomi and Woljif only, never closing anything.
        var reactions = story.Scenes.Where(s => s.Relationship == "anevia" && s.Reaction).ToArray();
        check(reactions.Length == 8 && reactions.All(r => r.Owner == "Konomi" || r.Owner == "Woljif"), "Anevia reactions changed.");
    }
}
