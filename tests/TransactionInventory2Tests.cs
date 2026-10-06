using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng8-q8c / E-Q8-09: real resource changes, OnShow, exit and reopening.
internal static class TransactionInventory2Tests
{
    private const string Lease = "arsinoe.trickster.cauldron.lease";
    private const string Collection = "arsinoe.trickster.cauldron.collection";
    private const string Late = "horzalah.trickster.late.at_night";
    private const string Paid = "arsinoe.trickster.cost.rent_paid";
    private const string Grace = "arsinoe.trickster.cost.rent_grace";
    private const string Raised = "arsinoe.trickster.cost.rent_raised";
    private const string Settled = "arsinoe.trickster.cost.rent_surcharge_paid";
    private const string Primed = "horzalah.trickster.primed";
    private static readonly string[] Pledges = { "arsinoe.trickster.cost.collateral_still",
        "arsinoe.trickster.cost.collateral_worldwound", "arsinoe.trickster.cost.collateral_word" };
    private static readonly string[] Injury = { "horzalah.trickster.cost.ear", "horzalah.trickster.cost.late" };

    private static Snapshot World(Story story, Scene scene, int funds = 700)
    {
        var state = new Snapshot { Chapter = 5, Hour = 5000, Area = "2570015799edf594daf2f076f2f975d8",
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = funds, ["Favors"] = funds } };
        foreach (var key in scene.Requires.Concat(new[] { "trickster", "fool_king.available" })) HouseholdTests.Earn(story, state, key);
        foreach (var group in scene.RequiresAnyGroups) state.Flags.Add(group[0]);
        if (scene.ContactUnit != null) state.AvailableContacts.Add(scene.ContactUnit);
        foreach (var flag in state.Flags) state.Times[flag] = state.Hour - 1000;
        Rules.Complete(story, state);
        return state;
    }

    private static Node Enter(Scene scene, string id, Snapshot state)
    {
        var node = scene.Nodes.Single(n => n.Id == id);
        Rules.EnterNode(node, state);
        return node;
    }

    private static string? Take(Story story, Scene scene, string id, Snapshot state, int index,
        Action<bool, string> check, bool success = true)
    {
        var node = Enter(scene, id, state);
        var choice = node.Choices[index];
        check(Rules.ChoiceAvailable(choice, state), scene.Id + "/" + id + ": answer unavailable " + index);
        if (!Rules.ChoiceAvailable(choice, state)) throw new InvalidOperationException("Unavailable fixture answer");
        if (choice.Crusade != null)
        {
            var cost = choice.Crusade;
            check(Rules.ApplyCrusadeChange(cost, () => state.CrusadeResources![cost.Resource],
                () => state.CrusadeResources![cost.Resource] += cost.Amount,
                warning => throw new InvalidOperationException(warning)), "Real balance change failed");
        }
        foreach (var flag in choice.Set)
            if (state.Flags.Add(flag)) state.Times[flag] = state.Hour;
        Rules.Complete(story, state);
        string? target = choice.Check != null ? (success ? choice.Check.Success : choice.Check.Failure) : choice.Next;
        if (target != null) Enter(scene, target, state); // Runtime OnShow immediately follows the answer.
        else if (!choice.Abort) { state.Flags.Add(scene.Id); state.Times[scene.Id] = state.Hour; }
        return target;
    }

    private static string Resume(Story story, Scene scene, Snapshot state, Action<bool, string> check)
    {
        state.Hour++;
        Rules.Complete(story, state);
        check(Rules.Available(story, scene, state), "Interrupted scene cannot reopen: " + scene.Id);
        var node = Enter(scene, scene.Nodes[0].Id, state);
        var offered = node.Choices.Select((c, i) => (c, i)).Where(x => Rules.ChoiceAvailable(x.c, state)).ToArray();
        check(offered.Length == 1, "Re-entry must offer one recorded outcome: " + scene.Id);
        return Take(story, scene, node.Id, state, offered[0].i, check)!;
    }

    private static void Finish(Story story, Scene scene, string first, Snapshot state, Action<bool, string> check)
    {
        string? node = first;
        for (int step = 0; node != null && step < 30; step++)
        {
            var shown = Enter(scene, node, state);
            int index = shown.Choices.FindIndex(c => Rules.ChoiceAvailable(c, state) && !c.Abort);
            check(index >= 0, "No selectable continuation: " + scene.Id + "/" + node);
            node = Take(story, scene, node, state, index, check);
        }
        check(node == null && state.Has(scene.Id), "Transaction did not finish: " + scene.Id);
    }

    private static void Exclusive(Story story, Action<bool, string> check)
    {
        var scene = story.Scenes.Single(s => s.Id == Collection);
        for (int selected = 0; selected < 3; selected++)
        {
            var state = World(story, scene);
            var entry = Enter(scene, "start", state).Choices.FindIndex(c => Rules.ChoiceAvailable(c, state));
            var node = Take(story, scene, "start", state, entry, check)!;
            check(node == "pledge", "Fresh collection did not reach pledges");
            check(Enter(scene, node, state).Choices.Skip(3).All(c => !Rules.ChoiceAvailable(c, state)),
                "Fresh collection offers a resume without a recorded pledge");
            node = Take(story, scene, node, state, selected, check)!;
            check(state.Has(Pledges[selected]) && !state.Has(scene.Id), "Selection not persistent before interruption");
            // Simulated interruption immediately after selection, then each old alternative.
            for (int attempt = 0; attempt < 2; attempt++)
            {
                node = Resume(story, scene, state, check);
                var pledge = Enter(scene, node, state);
                foreach (var original in pledge.Choices.Take(3))
                    check(!Rules.ChoiceAvailable(original, state), "Reopened pledge offers a new collateral selection");
                check(Pledges.Count(state.Has) == 1, "Interrupted collateral accumulated");
                var offers = pledge.Choices.Select((c, i) => (c, i)).Where(x => Rules.ChoiceAvailable(x.c, state)).ToArray();
                check(offers.Length == 1 && offers[0].c.Next == new[] { "still", "wound", "word" }[selected],
                    "Recorded pledge cannot resume disjointly");
                node = Take(story, scene, node, state, offers[0].i, check)!;
            }
            // An earned pledge does not depend on the still being available now.
            state.Flags.Remove("fool_king.available"); state.Flags.Add("fool_king.gone");
            node = Resume(story, scene, state, check);
            var resume = Enter(scene, node, state).Choices.FindIndex(c => Rules.ChoiceAvailable(c, state));
            node = Take(story, scene, node, state, resume, check)!;
            Finish(story, scene, node, state, check);
            check(Pledges.Count(state.Has) == 1, "Finished collateral lost exclusivity");
            check(!Rules.Available(story, scene, state), "Completed collection replays");
        }
    }

    private static void Haggle(Story story, Action<bool, string> check)
    {
        var scene = story.Scenes.Single(s => s.Id == Lease);
        foreach (bool success in new[] { true, false })
        foreach (bool interrupted in new[] { true, false })
        {
            var state = World(story, scene, 500);
            var entry = Enter(scene, "start", state).Choices.FindIndex(c => Rules.ChoiceAvailable(c, state));
            var node = Take(story, scene, "start", state, entry, check)!;
            node = Take(story, scene, node, state, 0, check)!; // Existing initial 500.
            node = Take(story, scene, node, state, 1, check, success)!;
            check(state.Has(Paid) && state.Has(Grace) == success && state.Has(Raised) != success,
                "Check outcome not recorded at entry before interruption");
            check(scene.Nodes.Single(n => n.Id == "rent").Choices.All(c => !Rules.ChoiceAvailable(c, state)),
                "Recorded check can be rerolled/agreed away");
            if (interrupted)
                for (int repeat = 0; repeat < 2; repeat++)
                {
                    node = Resume(story, scene, state, check);
                    check(node == (success ? "discount" : "raised"), "Interrupted check changed its result");
                }
            if (!success)
            {
                check(Rules.PaymentExitAvailable(Enter(scene, node, state), state), "Underfunded surcharge has no Leave");
                check(!state.Has(Settled), "Abort settled surcharge");
                state.CrusadeResources!["Finances"] = 200;
            }
            Finish(story, scene, node, state, check);
            check(state.CrusadeResources!["Finances"] == 0 && state.Has(Grace) == success && state.Has(Raised) != success,
                "Paid lease changed negotiated outcome or cost");
            foreach (string id in new[] { "arsinoe.trickster.epilogue.bill_to_threshold", "arsinoe.trickster.epilogue.pot_returned" })
            {
                var page = story.Scenes.Single(s => s.Id == id).Nodes[0];
                var grace = page.Paragraphs.Where(p => p.Requires.Contains(Grace)).ToArray();
                check(grace.Length > 0 && grace.Any(p => Rules.ParagraphVisible(p, state)) == success,
                    "Settlement does not recognize earned grace: " + id);
                check(grace.Any(p => p.Text.Contains("three seasonal renewals")), "Grace changed the promised duration");
                check(!success || Rules.VisibleParagraphs(page, state).All(p => !p.Text.Contains("never once suggested a discount")),
                    "Settlement contradicts the earned concession");
            }
        }
    }

    private static void Irreversible(Story story, Action<bool, string> check)
    {
        var scene = story.Scenes.Single(s => s.Id == Late);
        foreach (int funds in new[] { 0, 99, 100 })
        {
            var state = World(story, scene, funds);
            string node = scene.Nodes[0].Id;
            int cuts = 0;
            while (node != "no_priest")
            {
                var shown = Enter(scene, node, state);
                int index = shown.Choices.FindIndex(c => Rules.ChoiceAvailable(c, state) && c.Next != "guard");
                node = Take(story, scene, node, state, index, check)!;
                if (node == "cut") cuts++;
            }
            check(Injury.All(state.Has) && !state.Has(Primed) && !state.Has("horzalah.started"),
                "Cut failed to persist injury or advanced the paid romance outcome");
            var pay = Enter(scene, node, state);
            check(Rules.ChoiceAvailable(pay.Choices[0], state) == (funds >= 100), "Payment ignores actual Favors");
            check(Rules.PaymentExitAvailable(pay, state) == (funds < 100), "Underfunded irreversible act cannot Leave");
            // Leave/forced interruption has no OnSelect effects. Reopening must never cut again.
            for (int repeat = 0; repeat < 2; repeat++)
            {
                node = Resume(story, scene, state, check);
                check(node == "no_priest" && Injury.All(state.Has) && !state.Has(Primed), "Injury re-entry repeats act or settles for free");
                check(state.CrusadeResources!["Favors"] == funds, "Exit or re-entry charged Favors");
            }
            state.CrusadeResources!["Favors"] = 100;
            Finish(story, scene, node, state, check);
            check(cuts == 1 && state.Has(Primed) && state.Has("horzalah.started") && Injury.All(state.Has) && state.CrusadeResources!["Favors"] == 0,
                "Later settlement changed irreversible paid outcome");
            check(!Rules.Available(story, scene, state), "Paid injury repeats");
        }
        var refusal = World(story, scene, 100);
        string next = Take(story, scene, "start", refusal, 3, check)!;
        next = Take(story, scene, next, refusal, 0, check)!;
        next = Take(story, scene, next, refusal, 2, check)!;
        Finish(story, scene, next, refusal, check);
        check(!Injury.Any(refusal.Has) && !refusal.Has(Primed) && refusal.CrusadeResources!["Favors"] == 100,
            "Calling guards grants injury or spends Favors");
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        var inventory = JsonDocument.Parse(File.ReadAllText(Path.Combine("tools", "transaction_inventory2_contracts.json")));
        var contracts = inventory.RootElement.GetProperty("eng8-q8c").GetProperty("contracts");
        check(contracts.GetArrayLength() == 3 && contracts.EnumerateArray().SelectMany(c => c.GetProperty("findings").EnumerateArray())
              .Select(f => f.GetString()).Distinct().Count() == 5, "E-Q8-09 registry lost a mapped finding");
        Exclusive(story, check); Haggle(story, check); Irreversible(story, check);
        var options = new JsonSerializerOptions { IncludeFields = true };
        int mutations = 0;
        for (int i = 0; i < 3; i++)
        foreach (string defect in new[] { "receipt", "exclusion", "resume" })
        {
            var changed = JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(story, options), options)!;
            var node = changed.Scenes.Single(s => s.Id == Collection).Nodes.Single(n => n.Id == "pledge");
            if (defect == "receipt") node.Choices[i].Set = Array.Empty<string>();
            if (defect == "exclusion") node.Choices[i].Forbids = Array.Empty<string>();
            if (defect == "resume") node.Choices[3 + i].Requires = Array.Empty<string>();
            Reject(() => Exclusive(changed, Throw), "pledge " + i + " " + defect); mutations++;
        }
        foreach (string defect in new[] { "grace", "raised", "reroll", "resume", "consumer", "injury", "injury-resume", "payment", "paid-receipt" })
        {
            var changed = JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(story, options), options)!;
            var lease = changed.Scenes.Single(s => s.Id == Lease);
            var late = changed.Scenes.Single(s => s.Id == Late);
            if (defect == "grace" || defect == "raised") lease.Nodes.Single(n => n.Id == (defect == "grace" ? "discount" : "raised")).EnterSet = Array.Empty<string>();
            if (defect == "reroll") lease.Nodes.Single(n => n.Id == "rent").Choices[1].Forbids = Array.Empty<string>();
            if (defect == "resume") lease.Nodes[0].Choices.RemoveAll(c => c.Requires.Contains(Grace));
            if (defect == "consumer") changed.Scenes.Single(s => s.Id == "arsinoe.trickster.epilogue.pot_returned").Nodes[0].Paragraphs.RemoveAll(p => p.Requires.Contains(Grace));
            if (defect == "injury") late.Nodes.Single(n => n.Id == "cut").EnterSet = Array.Empty<string>();
            if (defect == "injury-resume") late.Nodes[0].Choices.RemoveAll(c => c.Requires.Contains(Injury[0]));
            if (defect == "payment") late.Nodes.Single(n => n.Id == "no_priest").Choices[0].Crusade = null;
            if (defect == "paid-receipt") late.Nodes.Single(n => n.Id == "no_priest").Choices[0].Set = Array.Empty<string>();
            Reject(() => { if (defect.StartsWith("injury") || defect.StartsWith("paid") || defect == "payment") Irreversible(changed, Throw);
                           else Haggle(changed, Throw); }, defect); mutations++;
        }
        void Throw(bool ok, string message) { if (!ok) throw new InvalidOperationException(message); }
        void Reject(Action run, string defect)
        {
            bool rejected = false;
            try { run(); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "E-Q8-09 mutation escaped acceptance: " + defect);
        }
        Console.WriteLine("eng8-q8c: interrupted pledges, success/failure, irreversible payment/exit/re-entry; " + mutations + " mutations rejected");
    }
}
