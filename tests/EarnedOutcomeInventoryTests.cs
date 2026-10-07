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
            state.Flags.UnionWith(new[] { "chapter_later", "chapter.six", "trickster", "trickster.ever" });
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
            Rules.RecordAvailabilityEvents(story, state, choice.Set);
            Refresh(state);
        }
        Choice Incoming(string scene, string node)
        {
            // Heated inserts keep an effect-free continuation. Test the
            // original gated approach, rather than that interior edge.
            var target = node;
            var seen = new HashSet<string>();
            while (seen.Add(target))
            {
                var edge = S(scene).Nodes.SelectMany(n => n.Choices.Select(c => (node: n, choice: c)))
                    .First(e => e.choice.Next == target);
                if (!edge.node.Id.Contains(".explicit.", StringComparison.Ordinal)) return edge.choice;
                target = edge.node.Id;
            }
            throw new InvalidOperationException("Insert cycle in " + scene + "/" + node);
        }

        Snapshot AcceptedDevarra()
        {
            var state = World("devarra.trickster.tested", "devarra.trickster.returned");
            check(!state.Has("devarra.trickster.late_committed"), "A submitted story supplies Devarra's unplayed late yes.");
            state.Chapter = 5; Refresh(state);
            check(Rules.Available(story, S("devarra.trickster.after.late_proposal"), state), "Devarra's campaign proposal is unavailable.");
            Select("devarra.trickster.after.late_proposal", "offer", 0, state);
            state.Chapter = 6; Refresh(state);
            return state;
        }
        var devarra = AcceptedDevarra();
        check(devarra.Has("devarra.trickster.late_committed"), "Earned Devarra late road lost.");
        // Main.State supplies this built-in aggregate from the native path.
        devarra.Flags.UnionWith(new[] { "swarm", "inhuman" }); Refresh(devarra);
        check(!devarra.Has("devarra.trickster.late_committed"), "Swarm retains Devarra's late road.");
        // A separate native history tests death; removing Swarm from its
        // old snapshot must never erase a witnessed conversion epoch.
        devarra = AcceptedDevarra();
        devarra.Flags.Remove("devarra.trickster.returned");
        devarra.Flags.Add("devarra.dead_lair"); Refresh(devarra);
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
            // Round two defers the repair until her personal yes; walking
            // into the circle alone no longer awards that receipt.
            var nextRepair = S("jannah.trickster.chalk_circle").Nodes.Single(n => n.Id == "open")
                .Choices[refusal.Item3].Next;
            for (int step = 0; nextRepair != null && step < 10; step++)
            {
                var answers = S("jannah.trickster.chalk_circle").Nodes.Single(n => n.Id == nextRepair).Choices;
                int index = answers.FindIndex(c => c.Next != "left" && Rules.ChoiceAvailable(c, jannah));
                check(index >= 0, "No earned Jannah repair continuation: " + nextRepair);
                var next = answers[index].Next;
                Select("jannah.trickster.chalk_circle", nextRepair, index, jannah);
                nextRepair = next;
            }
            check(jannah.Has("jannah.trickster.chalk_circle.walked_in"), "Repair fixture omitted Jannah's personal acceptance.");
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
            // eng3-ab: neither the taken hand nor the riddle records the
            // route-specific acceptance needed for a romantic Last Call payoff.
            check(!late.Has(route + ".committed") && !Rules.Available(story, S(route + ".lastcall.page"), late), "Late readiness mistaken for acceptance: " + route);
            late.Flags.Add(story.Relationships[route].ClosedFlag); Refresh(late);
            check(!Rules.Available(story, S(route + ".lastcall.page"), late), "Closed late fallback leaks coda: " + route);
        }
        var name = World("nenio.enigma_resolved");
        Select("nenio.trickster.taken.riddle", "filed", 0, name);
        name.Flags.Add("trickster.lastcall.open"); Refresh(name);
        check(!name.Has("nenio.trickster.name_gone") && !name.Has("nenio.lastcall.callable")
            && !Rules.Available(story, S("nenio.lastcall.call"), name), "Unfiled name stake grants name loss or Last Call eligibility.");
        // Her native farewell still uses the name; after_enigma completes the filing.
        name.Chapter = 5; name.Hour += 13;
        var filing = S("nenio.trickster.after_enigma");
        name.AvailableContacts.Add(filing.ContactUnit!);
        check(Rules.Available(story, filing, name), "Earned name filing is unavailable after the native farewell.");
        Select(filing.Id, "open", 0, name);
        Select(filing.Id, "missing", 0, name);
        Select(filing.Id, "thanked", 0, name);
        Select(filing.Id, "law", 2, name);
        check(name.Has("nenio.trickster.name_gone") && name.Has("nenio.lastcall.callable"), "Completed name filing loses name loss or Last Call eligibility.");
        name.Chapter = 6;
        check(Rules.Available(story, S("nenio.lastcall.call"), name), "Actual name stake cannot select the call.");
        Select("nenio.lastcall.call", "call", 0, name);
        check(Rules.VisibleParagraphs(S("nenio.lastcall.page").Nodes[0], name)
            .Any(p => p.Requires.Contains("nenio.trickster.name_gone")), "Actual name stake misses its coda paragraph.");
        check(Rules.BookVisible(story.Books["trickster.ledger"], name).Any(e => e.Id == "owed.nenio"), "Paid name absent from Ledger.");
        check(Rules.JournalEntryOpen(story.Relationships["lastcall"].JournalEntries.Single(e => e.Id == "owed.nenio"), name), "Paid name absent from journal.");
        var cairn = World("wenduag.trickster.cairn_built");
        check(!cairn.Has("wenduag.lastcall.callable"), "Built cairn alone grants a partner call.");
        cairn.Flags.Add("wenduag.committed"); Refresh(cairn);
        check(!cairn.Has("wenduag.lastcall.callable"), "Coarse Wenduag commitment and cairn grant a partner call.");
        cairn.Flags.UnionWith(new[] { "wenduag.trickster.proved", "wenduag.trickster.gate_seen", "wenduag.trickster.claim.given" });
        Refresh(cairn);
        check(cairn.Has("wenduag.lastcall.callable"), "Earned Wenduag partner cannot call.");
        cairn.Flags.Add("wenduag.dead_any"); Refresh(cairn);
        check(!cairn.Has("wenduag.lastcall.callable"), "Unreturned Wenduag retains call.");
        Console.WriteLine("PASS: eng7-l13 late entitlements, mandatory consequences and Last Call consumer parity.");
    }
}
