using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text.Json;
using Tirabade;

// eng8-q8h: all yes/refusal facts below come from selectable producer histories.
internal static class LateAcceptanceInventory2Tests
{
    internal static void Refresh(Story story, Snapshot state)
    {
        state.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
        Rules.Complete(story, state);
    }
    internal static Snapshot World(Story story, int chapter, params string[] natives)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 10000, Area = Rules.NurahCapital,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000 } };
        state.Flags.UnionWith(new[] { "chapter_later", "trickster", "trickster.ever" });
        state.Flags.UnionWith(natives);
        Refresh(story, state);
        foreach (var flag in state.Flags) state.Times[flag] = 0;
        return state;
    }
    internal static Snapshot Earn(Story story, Action<bool, string> check, string id, Snapshot before,
        string receipt, params string[] absent)
    {
        var s = story.Scenes.Single(s => s.Id == id);
        var state = Program.Copy(before);
        state.SceneContacts.UnionWith(before.SceneContacts);
        state.Hour += 200;
        // Resolve the contact used by this host, as the native/presence adapter does.
        if (s.ContactUnit != null) state.AvailableContacts.Add(s.ContactUnit);
        Refresh(story, state);
        check(Rules.Available(story, s, state), "eng8-q8h producer unavailable: " + id);
        var result = PaidPaths(story, s, state).FirstOrDefault(r => r.Has(receipt) && absent.All(f => !r.Has(f)));
        check(result != null, "eng8-q8h no actual producer path: " + id + " -> " + receipt);
        Refresh(story, result!);
        return result!;
    }
    // Replay selectable graph paths, including the actual existing resource costs.
    // Program.Walk intentionally does not debit resources in its generic prose oracle.
    internal static List<Snapshot> PaidPaths(Story story, Scene scene, Snapshot initial)
    {
        var outcomes = new List<Snapshot>();
        void Visit(string id, Snapshot current, HashSet<string> visited)
        {
            if (!visited.Add(id)) throw new Exception("Inventory cycle: " + scene.Id + "/" + id);
            Refresh(story, current);
            var node = scene.Nodes.Single(n => n.Id == id);
            Rules.EnterNode(node, current);
            foreach (var choice in node.Choices.Where(c => Rules.ChoiceAvailable(c, current)))
            {
                var next = Program.Copy(current);
                next.SceneContacts.UnionWith(current.SceneContacts);
                if (choice.Crusade != null) next.CrusadeResources![choice.Crusade.Resource] += choice.Crusade.Amount;
                foreach (string flag in choice.Set) { next.Flags.Add(flag); next.Times[flag] = next.Hour; }
                if (choice.Next != null || choice.Check != null)
                    foreach (var target in Rules.NextNodes(choice)) Visit(target, Program.Copy(next), new HashSet<string>(visited));
                else
                {
                    if (!choice.Abort) { next.Flags.Add(scene.Id); next.Times[scene.Id] = next.Hour; }
                    Refresh(story, next);
                    outcomes.Add(next);
                }
            }
        }
        Visit(scene.Nodes[0].Id, Program.Copy(initial), new HashSet<string>());
        return outcomes;
    }
    internal static void Run(Story story, Action<bool, string> check)
    {
        using var inventory = JsonDocument.Parse(File.ReadAllText("tools/late_acceptance_inventory2_contracts.json"));
        check(inventory.RootElement.GetProperty("finding_ids").GetArrayLength() == 13, "Late acceptance mapped inventory incomplete");
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        bool Guest(string route, Snapshot s) => Rules.BookVisible(story.Books["trickster.ledger"], s).Any(e => e.Id == "guest." + route);
        Snapshot End(Snapshot before) { var s = Program.Copy(before); s.Chapter = 6; s.Flags.UnionWith(new[] { "trickster.lastcall.taken", "ending.trickster" }); Refresh(story, s); return s; }

        var city = Earn(story, check, "arsinoe_city_on_paper", World(story, 5, "arsinoe.capital"), "arsinoe.picture_invitation");
        var printer = Earn(story, check, "arsinoe_printers_view", city, "arsinoe.printer_met");
        var roof = Earn(story, check, "arsinoe_roofs", printer, "arsinoe.courting");
        check(roof.Has("arsinoe.trickster.late_ready") && !roof.Has("arsinoe.harem.eligible") && !Guest("arsinoe", roof), "Roof pending counts as yes");
        var yes = Earn(story, check, "arsinoe.trickster.late.ask", roof, "arsinoe.trickster.late_accepted");
        var no = Earn(story, check, "arsinoe.trickster.late.ask", roof, "arsinoe.trickster.late_declined");
        check(yes.Has("arsinoe.harem.eligible") && Guest("arsinoe", yes) && !no.Has("arsinoe.harem.eligible") && !Guest("arsinoe", no), "Physical yes/refusal not distinguished");
        check(Rules.Available(story, S("arsinoe.lastcall.page"), End(yes)) && !Rules.Available(story, S("arsinoe.lastcall.page"), End(no)), "Arsinoe late coda mismatch");
        foreach (var blocker in new[] { "arsinoe.closed", "arsinoe.parted", "arsinoe.unavailable" })
        {
            if (blocker != "arsinoe.closed" && !story.Relationships["arsinoe"].UnavailableFlags.Contains(blocker)) continue;
            var closed = End(yes); closed.Flags.Add(blocker); Refresh(story, closed);
            check(!Guest("arsinoe", closed) && !Rules.Available(story, S("arsinoe.lastcall.page"), closed), "Closed late acceptance leaks");
        }
        var acceptedEnding = End(yes);
        var remembered = S("arsinoe.trickster.late.commit");
        check(Rules.Available(story, remembered, acceptedEnding)
            && Program.Walk(remembered, acceptedEnding).Count >= 2, "Arsinoe accepted ending has no selectable memory paths");
        check(S("arsinoe.trickster.late.commit").Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0), "Arsinoe epilogue writes acceptance");
        var lease = Earn(story, check, "arsinoe.trickster.cauldron.lease", World(story, 5, "arsinoe.capital", "council.cauldron_given"), "arsinoe.trickster.primed");
        var flirt = Earn(story, check, "arsinoe.trickster.cauldron.collection", lease, "arsinoe.trickster.stays_to_collect");
        check(flirt.Has("arsinoe.trickster.late_ready") && !Guest("arsinoe", flirt), "Flirt-only grants household acceptance");
        var flirtNo = Earn(story, check, "arsinoe.trickster.late.ask", flirt, "arsinoe.trickster.late_declined");
        var flirtYes = Earn(story, check, "arsinoe.trickster.late.ask", flirt, "arsinoe.trickster.late_accepted");
        check(!Guest("arsinoe", flirtNo) && Guest("arsinoe", flirtYes), "Flirt-road answers conflate readiness and yes");

        var scribe = Earn(story, check, "nenio.folio.dictation", World(story, 5), "nenio.trickster.scribe");
        check(!scribe.Has("nenio.harem.eligible") && !Guest("nenio", scribe) && !Rules.Available(story, S("nenio.trickster.epilogue.commit"), End(scribe)), "Dictation creates romance");
        check(Rules.Available(story, S("nenio.trickster.epilogue.scholar"), End(scribe)), "Employment-only scholarship ending missing");
        var boughtBack = Earn(story, check, "nenio.trickster.dead.the_price", World(story, 5, "nenio.dead", "revive.nenio.available"), "nenio.trickster.returned");
        var report = Earn(story, check, "nenio.trickster.away.field_report", World(story, 5, "nenio.kicked_out"), "nenio.trickster.primed_away");
        var probation = Earn(story, check, "nenio.trickster.away.correction_visitor", report, "nenio.trickster.returned");
        foreach (var employment in new[] { boughtBack, probation })
            check(!Guest("nenio", employment) && !employment.Has("nenio.trickster.late_committed")
                && !Rules.Available(story, S("nenio.trickster.epilogue.commit"), End(employment)), "Paid return/probation creates romance without pursuit");
        var margin = Earn(story, check, "nenio.folio.demons", scribe, "nenio.folio.demons");
        var pursued = Earn(story, check, "nenio.trickster.commit.hypothesis", margin, "nenio.trickster.test_running", "nenio.trickster.tampered");
        check(Guest("nenio", pursued) && Rules.Available(story, S("nenio.trickster.epilogue.commit"), End(pursued)), "Actual romantic hypothesis misses readers");
        var contaminated = Earn(story, check, "nenio.trickster.commit.hypothesis", margin, "nenio.trickster.tampered");
        check(!Guest("nenio", contaminated), "Contaminated hypothesis bypasses L13 control");

        var met = Earn(story, check, "kiana.trickster.aftermath.letter_waited", World(story, 5, "seelah.souls_returned"), "kiana.trickster.met");
        var marriage = Earn(story, check, "kiana.marriage", met, "kiana.attracted", "kiana.closed");
        var separated = Earn(story, check, "kiana.answer", marriage, "kiana.available");
        var lovers = Earn(story, check, "kiana.date", separated, "kiana.lovers");
        var unanswered = End(lovers);
        var ep = S("kiana.trickster.epilogue.commit");
        check(Rules.Available(story, ep, unanswered), "Actual unanswered courtship cannot reach question");
        // Round 2a: saved answers 3/4 are retired for a separated Kiana; 5/6 record her exclusive stance.
        check(!Rules.ChoiceAvailable(ep.Nodes[0].Choices[3], unanswered) && !Rules.ChoiceAvailable(ep.Nodes[0].Choices[4], unanswered), "Separated Kiana bypasses stance at old late answers");
        foreach (int index in new[] { 2, 5, 6 })
        {
            check(Rules.ChoiceAvailable(ep.Nodes[0].Choices[index], unanswered), "Advertised answer impossible: " + index);
            var result = Program.WalkVia(ep, unanswered, "start", index).Single();
            Refresh(story, result);
            check(result.Has("kiana.partner_stance.exclusive") == (index != 2), "Late acceptance loses Kiana stance");
            check(result.Has("kiana.trickster.late_committed") == (index != 2) && !result.Has("kiana.committed"), "Affirmative consumer invalidated by joint commitment");
            check(Rules.Available(story, S("kiana.lastcall.page"), result) == (index != 2), "Actual late yes/no misses coda");
        }

        const string T = "terendelev.trickster.";
        var back = Earn(story, check, T + "bones.restitution", World(story, 5, "iz.terendelev_battle"), T + "returned");
        foreach (var suffix in new[] { "", "_awning" })
        {
            var place = Program.Copy(back);
            if (suffix.Length > 0) place.Flags.Add("terendelev.presence.failed");
            var free = Earn(story, check, T + "after.first_night" + suffix, place, T + "debt_free");
            var debt = Earn(story, check, T + "after.first_night" + suffix, place, T + "owed");
            var commit = S(T + "commit" + suffix);
            check(!Rules.Available(story, commit, free) && !Guest("terendelev", free) && !Rules.Available(story, S(T + "epilogue.late"), End(free)), "Rescue/breakfast grants permanence");
            var proof = Earn(story, check, T + "watch.proof" + suffix, free, T + "watch.proof_seen");
            check(!Rules.Available(story, commit, proof) && !Guest("terendelev", proof), "Proof-only grants permanence");
            var personalOnly = Earn(story, check, T + "watch.wings" + suffix, free, T + "watch.wings_tried");
            check(!Rules.Available(story, commit, personalOnly), "Personal-only bypasses proof");
            var developed = Earn(story, check, T + "watch.wings" + suffix, proof, T + "watch.wings_tried");
            check(Guest("terendelev", developed) && Rules.Available(story, S(T + "epilogue.late"), End(developed)), "Documented earned late road lost");
            Earn(story, check, T + "commit" + suffix, developed, "terendelev.committed");
            var debtProof = Earn(story, check, T + "watch.proof" + suffix, debt, T + "watch.proof_seen");
            var debtPersonal = Earn(story, check, T + "watch.wings" + suffix, debtProof, T + "watch.wings_tried");
            check(!Guest("terendelev", debtPersonal) && !Rules.Available(story, S(T + "epilogue.late"), End(debtPersonal)), "Held debt grants late permanence");
            var declined = Earn(story, check, T + "commit" + suffix, debtPersonal, T + "declined", "terendelev.committed");
            check(!Guest("terendelev", declined), "Declined debt grants household");
            var released = Earn(story, check, T + "commit.release" + suffix, declined, "terendelev.committed");
            check(released.Has(T + "debt_free") && Guest("terendelev", released), "Actual release misses commitment");
        }
        Console.WriteLine("PASS: eng8-q8h actual late readiness, acceptance/refusal, proof/personal/debt producers and readers.");
    }
}
