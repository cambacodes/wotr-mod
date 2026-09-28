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
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
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

        // Hooks: the devices are letters (her room in Kenabres has no engine area); the gate beats are on her own hub.
        check(new[] { setup, wardrobe, fetched, confession, letterTwin }.All(s => s.Remote), "An Anevia letter became physical.");
        check(new[] { setup, wardrobe, fetched, confession }.All(s => s.TricksterDevice && s.TricksterState == "gone"), "Device states mislabelled.");
        check(new[] { gate, commit, second }.All(s => s.AnswerLists.SequenceEqual(new[] { "33960c7f7af40cd43b7f801a76c87a0b" })
              && s.ContactUnit == Contact && !s.TricksterDevice), "Gate beats left her own hub.");
        var rel = story.Relationships["anevia"];
        check(rel.UnavailableOverrides.TryGetValue("anevia_gone", out var over) && over == Returned
              && rel.TricksterAccess.Count == 1 && rel.TricksterAccess["gone"].Device == setup.Id, "Anevia relationship patch missing.");
        check(story.Presences.TryGetValue("anevia.presence", out var presence) && presence.Unit == Contact && presence.Mode == "reuse-native"
              && presence.At?.NearUnit == "15f754455d1d87c42a4e14df456d5415" && presence.Requires.Contains(Returned),
            "Anevia presence is not anchored at the smith by the gate.");
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
        var primed = World(story, 5, "trickster.ever", "anevia_gone", "irabeth_dead", Primed);
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

        // Trk_Anevia_Coexistence_*: at most one return; Irabeth's state never gates the wardrobe.
        var withBeth = World(story, 5, "trickster.ever", "anevia_gone", "irabeth_dead", IrabethReturned, Primed);
        check(Rules.Available(story, wardrobe, withBeth) && !Any(withBeth, fetched, confession), "Trk_Anevia_Coexistence_Primed failed.");
        var bethClosed = World(story, 5, "trickster.ever", "anevia_gone", "irabeth_dead", "irabeth.closed", Primed);
        check(Rules.Available(story, wardrobe, bethClosed) && !Any(bethClosed, fetched, confession), "Trk_Anevia_Coexistence_Closed failed.");
        var both = World(story, 5, "trickster.ever", "anevia_gone", "irabeth_dead", IrabethReturned, "irabeth.trickster.blow_rewritten",
                         Killed, Returned, "anevia.lover");
        check(Rules.Available(story, gate, both) && !Any(both, returns) && !Any(both, grief), "Trk_Anevia_Coexistence_Returned failed.");

        // Trk_Anevia_GriefGuard: no grief over a wife who has come back.
        var guard = World(story, 5, "trickster.ever", "irabeth_dead", "anevia_gone", IrabethReturned, Returned, "anevia.lover");
        check(!Any(guard, grief) && !Any(World(story, 6, "trickster.ever", "irabeth_dead", "anevia_gone", IrabethReturned, Returned, "anevia.lover"), grief),
            "Trk_Anevia_GriefGuard: a grief page for a living wife.");

        // Trk_Anevia_Fetched: Irabeth rides south for her; the bargain is told.
        var fetch = World(story, 5, "trickster.ever", "anevia_gone", "irabeth_dead", IrabethReturned, "irabeth.trickster.cost.under_orders");
        check(Rules.Available(story, fetched, fetch) && !Any(fetch, wardrobe, confession), "Trk_Anevia_Fetched: wrong device.");
        var fetchPages = new HashSet<string>();
        var brought = Program.Walk(fetched, fetch, (page, _) => fetchPages.Add(page));
        check(brought.Count == 2 && brought.All(r => r.Has(Returned) && r.Has("anevia.trickster.cost.knows_the_bargain")) && fetchPages.Contains("bargain"),
            "Trk_Anevia_Fetched: the letters do not return her, or the bargain is untold.");
        check(Rules.Available(story, gate, Later(story, brought[0], 48)), "Gate unreachable after the fetch.");
        var joked = brought.Single(r => r.Has("anevia.trickster.told_the_joke"));
        var jokePages = new HashSet<string>();
        Program.Walk(gate, Later(story, joked, 48), (page, _) => jokePages.Add(page));
        check(jokePages.Contains("joke") && jokePages.Contains("beth_back"), "Gate forgets the joke or Beth.");

        // Trk_Anevia_Confession / _Lie: after the rewritten blow she wants the version that hurts.
        var rewritten = World(story, 5, "trickster.ever", "anevia_gone", "irabeth_dead", Killed, IrabethReturned, "irabeth.trickster.blow_rewritten");
        check(Rules.Available(story, confession, rewritten) && !Any(rewritten, fetched, wardrobe), "Trk_Anevia_Confession: wrong device.");
        var told = Program.Walk(confession, rewritten);
        check(told.Count == 1 && told[0].Has(Returned) && told[0].Has("anevia.trickster.cost.accounting") && !told[0].Has("anevia.trickster.cost.lie_exposed"),
            "Trk_Anevia_Confession: the truth does not return her, or the lie is offered to an honest Commander.");
        var lied = Program.Copy(rewritten); lied.Flags.Add("irabeth.trickster.cost.accounting_lied");
        var exposed = Program.Walk(confession, lied).Where(r => r.Has("anevia.trickster.cost.lie_exposed")).ToList();
        check(exposed.Count == 1 && exposed[0].Has(Returned), "Trk_Anevia_Confession_Lie: the lie is not exposed.");

        // Trk_Anevia_Gone_Commit / Trk_Anevia_Gone_Refusal: Beth first, her terms, her no.
        foreach (bool bethBack in new[] { false, true })
        foreach (bool listening in new[] { false, true })
        {
            var ask = World(story, 5, "trickster.ever", "anevia_gone", "irabeth_dead", Returned, "anevia.trickster.gate_seen");
            if (bethBack) ask.Flags.Add(IrabethReturned);
            if (listening) ask.Flags.Add("anevia.trickster.cost.socoth_listening");
            ask.Times["anevia.trickster.gate_seen"] = ask.Hour - 96;
            check(Rules.Available(story, commit, ask) && !Rules.Available(story, second, ask), "Trk_Anevia_Gone_Commit: commit unavailable.");
            check(!Rules.Available(story, commit, Later(story, ask, -1)), "Commit ignores the delay after the gate.");
            var pages = new HashSet<string>();
            var outcomes = Program.Walk(commit, ask, (page, _) => pages.Add(page));
            // Two openings ([Ask her to stay] / [Say nothing and wait]) lead to the same terms.
            check(outcomes.Count(r => r.Has("anevia.committed")) == (bethBack ? 4 : 2), "The kiss is offered in the widow world, or missing after Beth's return.");
            check(pages.Contains("threshold") && pages.Contains(bethBack ? "morning_back" : "morning") && pages.Contains("coats") == listening
                  && pages.Contains(bethBack ? "share" : "widow"), "Commit skips the intimate beat or a variant.");
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
        check(!Rules.Available(story, letterTwin, World(story, 5, "trickster.ever", "anevia_gone", "irabeth_dead", Returned)),
            "The letter twin opens while the gate presence can be placed.");

        // Trk_Anevia_PathFailed: canon fate stands.
        var failed = World(story, 5, "trickster.was", "trickster.ever", "trickster.failed", "anevia_gone", "irabeth_dead", "closets.known");
        check(!Any(failed, setup, wardrobe), "Trk_Anevia_PathFailed: a device survives the lost path.");

        // Trk_Tirabade_TableAgain: both back, three chairs; the shared route commits on its own flag.
        var table = S("tirabade.trickster.table_again");
        var chairs = S("tirabade.trickster.third_chair");
        var reunited = World(story, 5, "trickster.ever", "irabeth_dead", "anevia_gone", IrabethReturned, Returned);
        check(Rules.Available(story, table, reunited), "Trk_Tirabade_TableAgain: table unavailable.");
        var third = Program.Walk(table, reunited).Single(r => r.Has("tirabade.trickster.third_chair"));
        var dealt = Program.Walk(chairs, Later(story, third, 72));
        check(dealt.Any(r => r.Has("committed")) && dealt.Any(r => r.Has("tirabade.trickster.declined") && !r.Has("committed")),
            "The third chair does not commit the shared route, or has no soft no.");
        check(!Rules.Available(story, chairs, Later(story, third, 71)), "Third chair mistimed.");
        var accounting = World(story, 5, "trickster.ever", "irabeth_dead", "anevia_gone", IrabethReturned, Returned, Killed, "irabeth.trickster.blow_rewritten");
        var accountingPages = new HashSet<string>();
        var accounted = Program.Walk(table, accounting, (page, _) => accountingPages.Add(page));
        check(accountingPages.Contains("accounting") && accounted.Where(r => r.Has("tirabade.trickster.third_chair")).All(r => r.Has("anevia.trickster.cost.accounting")),
            "The third chair is offered before Anevia hears the accounting.");
        // Epilogue arbitration: exactly one Anevia page for every returned history, with her paragraphs.
        foreach (bool lover in new[] { false, true })
        foreach (string outcome in new[] { "", "anevia.committed", "anevia.trickster.declined", "anevia.closed", "anevia.trickster.friends", "anevia.trickster.gate_seen" })
        foreach (string beth in new[] { "", IrabethReturned, Killed })
        {
            var end = World(story, 6, "trickster.ever", "irabeth_dead", "anevia_gone", Returned, "anevia.trickster.cost.wardrobe_nailed");
            if (lover) end.Flags.Add("anevia.lover");
            if (outcome != "") end.Flags.Add(outcome);
            if (beth != "") end.Flags.Add(beth);
            Rules.Complete(story, end);
            var pages = story.Scenes.Where(s => s.Relationship == "anevia" && s.Owner == "Epilogue" && Rules.Available(story, s, end)).ToList();
            check(pages.Count == 1, "Anevia epilogue: " + pages.Count + " pages for lover=" + lover + " outcome=" + outcome + " beth=" + beth
                                    + " (" + string.Join(",", pages.Select(s => s.Id)) + ")");
            if (pages.Count == 1)
                check(Rules.VisibleParagraphs(pages[0].Nodes.Last(), end).Length >= 1, "Returned Anevia's page has none of her paragraphs: " + pages[0].Id);
        }
        var stayed = World(story, 6, "anevia.lover", "anevia.committed", "anevia.developed");
        check(Rules.VisibleParagraphs(S("anevia.ending_kept").Nodes.Last(), stayed).Length == 0, "Trickster paragraphs leak onto an Anevia who stayed.");
        var widowed = World(story, 6, "irabeth_dead", "anevia_gone", "anevia.lover");
        check(Rules.Available(story, S("anevia.ending_gone"), widowed)
              && !Rules.Available(story, S("anevia.ending_gone"), World(story, 6, "irabeth_dead", "anevia_gone", "anevia.lover", Returned)),
            "Canon departure page lost, or shown for a returned Anevia.");

        // Reactions: Konomi and Woljif only, never closing anything.
        var reactions = story.Scenes.Where(s => s.Relationship == "anevia" && s.Reaction).ToArray();
        check(reactions.Length == 8 && reactions.All(r => r.Owner == "Konomi" || r.Owner == "Woljif"), "Anevia reactions changed.");
    }
}
