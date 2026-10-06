using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// eng7-l13: execute existing refusal/repair answers, then recompute readers.
// Native loss/path inputs are observations; no desired composite is injected.
internal static class EarnedOutcomeInventoryTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        void Refresh(Snapshot state)
        {
            // Main.State rebuilds composites from saved facts on every observation.
            state.Flags.ExceptWith(story.Derived.Keys);
            state.Flags.ExceptWith(story.Counts.Keys);
            Rules.Complete(story, state);
        }
        Snapshot World(params string[] flags)
        {
            var state = new Snapshot { Chapter = 6, Hour = 10000,
                CrusadeResources = new Dictionary<string, int> { ["Finances"] = 200 } };
            state.Flags.UnionWith(new[] { "chapter_later", "trickster" });
            state.Flags.UnionWith(flags);
            Refresh(state);
            return state;
        }
        void Select(string scene, string node, int index, Snapshot state)
        {
            var choice = S(scene).Nodes.Single(n => n.Id == node).Choices[index];
            check(Rules.ChoiceAvailable(choice, state), "Inventory answer blocked: " + scene + "/" + node + "[" + index + "]");
            if (choice.Crusade != null) state.CrusadeResources![choice.Crusade.Resource] += choice.Crusade.Amount;
            foreach (var flag in choice.Set) { state.Flags.Add(flag); state.Times[flag] = state.Hour; }
            Refresh(state);
        }
        Choice Incoming(string scene, string node) => S(scene).Nodes.SelectMany(n => n.Choices).First(c => c.Next == node);

        var devarra = World("devarra.trickster.tested");
        check(devarra.Has("devarra.trickster.late_committed"), "Earned Devarra late road lost.");
        // Main.State supplies this built-in aggregate from the native path.
        devarra.Flags.UnionWith(new[] { "swarm", "inhuman" }); Refresh(devarra);
        check(!devarra.Has("devarra.trickster.late_committed"), "Swarm retains Devarra's late road.");
        devarra.Flags.ExceptWith(new[] { "swarm", "inhuman" }); devarra.Flags.Add("devarra.dead_lair"); Refresh(devarra);
        check(!devarra.Has("devarra.trickster.late_committed"), "Unreturned death retains late entitlement.");
        devarra.Flags.Add("devarra.trickster.returned"); Refresh(devarra);
        check(devarra.Has("devarra.trickster.late_committed"), "Matching earned Devarra return over-blocked.");

        var kaylessa = World("kaylessa.trickster.knife_shown", "kaylessa.wasps.in_the_dark", "kaylessa.trickster.told_borrowed");
        check(kaylessa.Has("kaylessa.trickster.late_committed"), "Prepared Kaylessa late road lost.");
        Select("kaylessa.trickster.commit", "ask", 2, kaylessa);
        check(!kaylessa.Has("kaylessa.trickster.late_committed") && !kaylessa.Has("kaylessa.harem.eligible"), "Kaylessa refusal leaves a household entitlement.");
        Select("kaylessa.trickster.after.knife_on_table", "knife", 0, kaylessa);
        check(kaylessa.Has("kaylessa.trickster.late_committed") && kaylessa.Has("kaylessa.harem.eligible"), "Existing Kaylessa second offer cannot repair refusal.");

        const string MC = "minagho_chivarro.trickster.";
        var pair = World(MC + "tprev.house", MC + "reunited");
        check(pair.Has("minagho_chivarro.outcome.eligible"), "Earned pair road lost.");
        Select(MC + "after.the_price_of_her_name", "walk", 0, pair);
        check(!pair.Has("minagho_chivarro.outcome.eligible"), "Walked-out Chivarro retains pair entitlement.");
        check(!Rules.ChoiceAvailable(Incoming(MC + "epilogue.commit", "went"), pair), "Pair intimacy bypasses won_back.");
        Select(MC + "after.won_back", "start", 0, pair);
        Select(MC + "after.won_back", "answer", 0, pair);
        Select(MC + "after.won_back", "hand", 0, pair);
        Select(MC + "after.won_back", "house_too", 0, pair);
        check(pair.CrusadeResources!["Finances"] == 0, "Won-back fixture bypassed its actual silk payment.");
        check(pair.Has("minagho_chivarro.outcome.eligible") && Rules.ChoiceAvailable(Incoming(MC + "epilogue.commit", "went"), pair), "Existing won_back cannot restore pair intimacy.");
        pair.Flags.Add("minagho.dead"); Refresh(pair);
        check(!Rules.ChoiceAvailable(Incoming(MC + "epilogue.commit", "went"), pair), "Pair intimacy brings unreturned dead Minagho.");
        var solo = World(MC + "chivarro_waiting", MC + "chivarro_in", "minagho.dead");
        check(Rules.ChoiceAvailable(Incoming(MC + "epilogue.commit", "went_alone"), solo), "Legitimate Chivarro-only late invitation was over-blocked.");
        solo.Flags.Add(MC + "chivarro_walked"); Refresh(solo);
        check(!Rules.Available(story, S(MC + "epilogue.commit"), solo), "Solo Chivarro invitation brings her back without won_back.");
        // pair contains the actual paid WON_BACK producer trace above.
        check(Rules.Available(story, S(MC + "epilogue.commit"), pair)
            && Rules.ChoiceAvailable(Incoming(MC + "epilogue.commit", "went_alone"), pair), "Paid Chivarro return loses her solo road after Minagho dies.");

        foreach (var refusal in new[] { ("no_lie", 0, 0, true), ("bout_again", 2, 1, false),
            ("you_first", 2, 2, false), ("her_first", 1, 3, false),
            ("bout_again", 2, 0, true), ("you_first", 2, 0, true), ("her_first", 1, 0, true) })
        {
            var jannah = World();
            if (refusal.Item4) Select("jannah.trickster.challenge", "lie", 1, jannah);
            Select("jannah.trickster.challenge", refusal.Item1, refusal.Item2, jannah);
            foreach (var entry in new[] { ("blade", "flirt"), ("the_watch", "mine"), ("anything_but_wings", "stay"), ("your_part", "not_you_want") })
                check(!Rules.ChoiceAvailable(Incoming("jannah.circle." + entry.Item1, entry.Item2), jannah), "Unrepaired Jannah refusal bypasses " + entry.Item1);
            Select("jannah.trickster.chalk_circle", "open", refusal.Item3, jannah);
            foreach (var entry in new[] { ("blade", "flirt"), ("the_watch", "mine"), ("anything_but_wings", "stay"), ("your_part", "not_you_want") })
                check(Rules.ChoiceAvailable(Incoming("jannah.circle." + entry.Item1, entry.Item2), jannah), "Earned Jannah repair loses " + entry.Item1);
        }

        foreach (var suffix in new[] { "", "_visitor", "_arcade" })
        {
            var nenio = World("nenio.trickster.scribe", "nenio.trickster.margin");
            Select("nenio.trickster.commit.hypothesis" + suffix, "conditions", 0, nenio);
            var pulse = S("nenio.folio.pulse" + suffix);
            var result = S("nenio.trickster.commit.result" + suffix);
            var clean = Program.Copy(nenio);
            Select(result.Id, "variable", 0, clean);
            check(clean.Has("nenio.committed"), "Clean earned Nenio result lost: " + suffix);
            var kisses = pulse.Nodes.Single(n => n.Id == "result").Choices;
            int index = kisses.FindIndex(c => c.Set.Contains("nenio.trickster.tampered"));
            Select(pulse.Id, "result", index, nenio);
            var cleanEntry = result.Nodes[0].Choices.Single(c => c.Next == "clean");
            check(!Rules.ChoiceAvailable(cleanEntry, nenio), "Pulse kiss still earns a clean result: " + suffix);
            check(Rules.ChoiceAvailable(result.Nodes[0].Choices.Single(c => c.Next == "void"), nenio), "Pulse contamination has no void outcome: " + suffix);
        }
        foreach (var sid in new[] { "mielarah.deck.market", "mielarah.deck.market.arcade" })
        {
            var mielarah = World("mielarah.trickster.minder.lied", "mielarah.trickster.landfall");
            Select(sid, "crowd", 1, mielarah);
            Select(sid, "prisoner", 0, mielarah);
            Select(sid, "worked_out", 0, mielarah);
            var wheel = S("mielarah.deck.wheel");
            mielarah.Chapter = 5; mielarah.Hour += 200;
            mielarah.Area = wheel.Areas[0]; mielarah.AvailableContacts.Add(wheel.ContactUnit!);
            check(!Rules.Available(story, wheel, mielarah), "Discovered sacrifice bypasses Oskel settlement: " + sid);
            var settlement = story.Scenes.SelectMany(s => s.Nodes.SelectMany(n => n.Choices.Select((c, i) => (s, n, c, i))))
                .First(t => t.c.Set.Contains("mielarah.deck.oskel_spoke") && Rules.ChoiceAvailable(t.c, mielarah));
            Select(settlement.s.Id, settlement.n.Id, settlement.i, mielarah);
            check(Rules.Available(story, wheel, mielarah)
                && Rules.ChoiceAvailable(wheel.Nodes.Single(n => n.Id == "letgo").Choices[0], mielarah), "Existing Oskel settlement cannot earn commitment.");
        }

        foreach (var route in new[] { "anevia", "nenio" })
        {
            var late = World();
            if (route == "anevia") Select("anevia.trickster.gone.gate", "beth_widow", 0, late);
            else Select("nenio.trickster.taken.riddle", "filed", 0, late);
            // Last Call is a paid existing framework outcome, not a commitment.
            late.Flags.Add("trickster.lastcall.taken"); late.Flags.Add("ending.trickster"); Refresh(late);
            // eng8-q8h: Nenio's riddle buys continued company, not pursuit.
            check(!late.Has(route + ".committed") && Rules.Available(story, S(route + ".lastcall.page"), late) == (route != "nenio"), "Late readiness mistaken for acceptance: " + route);
            late.Flags.Add(story.Relationships[route].ClosedFlag); Refresh(late);
            check(!Rules.Available(story, S(route + ".lastcall.page"), late), "Closed late fallback leaks coda: " + route);
        }
        var name = World();
        Select("nenio.trickster.taken.riddle", "filed", 0, name);
        check(!name.Has("nenio.trickster.name_gone") && !name.Has("nenio.lastcall.callable"),
            "Unfiled Nenio stake grants name loss or Last Call eligibility.");
        name.Flags.Add("trickster.lastcall.open"); Refresh(name);
        check(!Rules.Available(story, S("nenio.lastcall.call"), name), "Unfiled Nenio stake can select the call.");
        name.Flags.Add("nenio.enigma_resolved"); Refresh(name);
        name = Program.Walk(S("nenio.trickster.after_enigma"), name)
            .First(o => o.Has("nenio.trickster.cost.name_filed"));
        Refresh(name);
        check(name.Has("nenio.trickster.cost.name_filed") && name.Has("nenio.trickster.name_gone")
            && name.Has("nenio.lastcall.callable"), "Completed Nenio filing loses the paid name stake.");
        name.Flags.Add("trickster.lastcall.open"); Refresh(name);
        check(Rules.Available(story, S("nenio.lastcall.call"), name), "Actual name stake cannot select the call.");
        Select("nenio.lastcall.call", "call", 0, name);
        check(Rules.VisibleParagraphs(S("nenio.lastcall.page").Nodes[0], name)
            .Any(p => p.Requires.Contains("nenio.trickster.name_gone")), "Actual name stake misses its coda paragraph.");
        check(Rules.BookVisible(story.Books["trickster.ledger"], name).Any(e => e.Id == "owed.nenio"), "Paid name absent from Ledger.");
        check(Rules.JournalEntryOpen(story.Relationships["lastcall"].JournalEntries.Single(e => e.Id == "owed.nenio"), name), "Paid name absent from journal.");
        var cairn = World("wenduag.trickster.cairn_built");
        check(!cairn.Has("wenduag.lastcall.callable"), "Built cairn alone grants a partner call.");
        cairn.Flags.Add("wenduag.committed"); Refresh(cairn);
        check(cairn.Has("wenduag.lastcall.callable"), "Earned Wenduag partner cannot call.");
        cairn.Flags.Add("wenduag.dead_any"); Refresh(cairn);
        check(!cairn.Has("wenduag.lastcall.callable"), "Unreturned Wenduag retains call.");
        Console.WriteLine("PASS: eng7-l13 late entitlements, mandatory consequences and Last Call consumer parity.");
    }
}
