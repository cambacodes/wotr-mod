using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng7-l09 / E-Q7-19: actual affordability, node entry, abort, re-entry and resource deltas.
internal static class TransactionExitInventoryTests
{
    private const string Lease = "arsinoe.trickster.cauldron.lease";
    private const string Paid = "arsinoe.trickster.cost.rent_paid";
    private const string Raised = "arsinoe.trickster.cost.rent_raised";
    private const string Settled = "arsinoe.trickster.cost.rent_surcharge_paid";

    private static Snapshot World(Story story, int finances)
    {
        var state = new Snapshot { Chapter = 5, Hour = 5000, Area = "2570015799edf594daf2f076f2f975d8",
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = finances } };
        state.Flags.UnionWith(new[] { "trickster", "arsinoe.capital", "council.cauldron_given" });
        state.AvailableContacts.Add("a609ed9b2205d034bb3bb04d2a255681");
        Rules.Complete(story, state);
        return state;
    }

    private static string? Take(Story story, Scene scene, string nodeId, Snapshot state, Func<Choice, bool> select,
        Action<bool, string> check, bool success = true)
    {
        var node = scene.Nodes.Single(n => n.Id == nodeId);
        Rules.EnterNode(node, state);
        var choices = node.Choices.Where(c => Rules.ChoiceAvailable(c, state) && select(c)).ToArray();
        check(choices.Length > 0, "Transaction has no selected affordable answer: " + nodeId);
        var choice = choices[0];
        if (choice.Crusade != null)
        {
            var cost = choice.Crusade;
            check(Rules.ApplyCrusadeChange(cost, () => state.CrusadeResources![cost.Resource],
                () => state.CrusadeResources![cost.Resource] += cost.Amount,
                warning => throw new InvalidOperationException(warning)), "Payment did not change the real fixture balance");
        }
        foreach (string flag in choice.Set)
            if (state.Flags.Add(flag)) state.Times[flag] = state.Hour;
        Rules.Complete(story, state);
        if (choice.Check != null) return success ? choice.Check.Success : choice.Check.Failure;
        if (choice.Next == null && !choice.Abort)
        {
            state.Flags.Add(scene.Id);
            state.Times[scene.Id] = state.Hour;
        }
        return choice.Next;
    }

    private static void Sign(Story story, Scene scene, Snapshot state, string node, Action<bool, string> check)
    {
        for (int steps = 0; steps < 12; steps++)
        {
            string? next = Take(story, scene, node, state, c => true, check);
            if (next == null)
            {
                check(state.Has(Lease) && state.Has("arsinoe.trickster.primed"), "Lease did not sign");
                return;
            }
            node = next;
        }

    }

    private static void FailedExit(Story story, Action<bool, string> check)
    {
        var scene = story.Scenes.Single(s => s.Id == Lease);
        var state = World(story, 500);
        check(Rules.Available(story, scene, state), "Exactly-500 lease unavailable");
        string node = Take(story, scene, "start", state, c => true, check)!;
        node = Take(story, scene, node, state, c => c.Crusade != null, check)!;
        check(state.CrusadeResources!["Finances"] == 0 && state.Has(Paid), "Initial 500 not paid/recorded");
        node = Take(story, scene, node, state, c => c.Check != null, check, success: false)!;
        var failed = scene.Nodes.Single(n => n.Id == node);
        Rules.EnterNode(failed, state);
        check(state.Has(Raised), "Failed haggle not persisted before generated Leave");
        check(Rules.PaymentExitAvailable(failed, state), "Exactly-zero history lacks generated payment exit");
        check(!state.Has(Lease) && !state.Has(Settled), "Generated abort signs or settles lease");
        // Main.AddPaymentExit has no OnSelect effects: the same snapshot is re-entered.
        for (int retry = 0; retry < 2; retry++)
        {
            state.Hour++;
            Rules.Complete(story, state);
            check(Rules.Available(story, scene, state), "Unpaid failure cannot reopen");
            node = Take(story, scene, "start", state, c => true, check)!;
            check(node == "raised", "Reopening bypasses surcharge or offers another roll");
            Rules.EnterNode(failed, state);
            check(Rules.PaymentExitAvailable(failed, state) && state.Has(Raised), "Repeated abort erased liability");
        }
        check(scene.Nodes.Single(n => n.Id == "rent").Choices.All(c => !Rules.ChoiceAvailable(c, state)),
              "Agreed or reroll remains selectable after recorded failure");
        state.CrusadeResources!["Finances"] = 200;
        node = Take(story, scene, "start", state, c => true, check)!;
        check(!Rules.PaymentExitAvailable(failed, state), "Payment exit hides affordable settlement");
        Sign(story, scene, state, node, check);
        check(state.CrusadeResources["Finances"] == 0 && state.Has(Settled), "Original negotiated 700 total changed");
        check(!Rules.Available(story, scene, state), "Settled signed lease replays");
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        if (!story.Scenes.Any(s => s.Id == Lease)) return;
        FailedExit(story, check);
        var scene = story.Scenes.Single(s => s.Id == Lease);
        foreach (string outcome in new[] { "agreed", "success", "failure" })
        {
            int initial = outcome == "failure" ? 700 : 500;
            var state = World(story, initial);
            var node = Take(story, scene, "start", state, c => true, check)!;
            node = Take(story, scene, node, state, c => c.Crusade != null, check)!;
            node = Take(story, scene, node, state, c => outcome == "agreed" ? c.Check == null : c.Check != null,
                        check, success: outcome != "failure")!;
            Sign(story, scene, state, node, check);
            check(state.CrusadeResources!["Finances"] == 0, "Wrong actual transaction delta: " + outcome);
            check(state.Has(Raised) == (outcome == "failure"), "Success/agreement acquires failure liability");
        }
        var poor = World(story, 499);
        var terms = scene.Nodes.Single(n => n.Id == "terms");
        check(!Rules.ChoiceAvailable(terms.Choices[0], poor) && !poor.Has(Paid), "Unaffordable initial payment records debt");
        check(!Rules.PaymentExitAvailable(terms, poor), "Payment exit offered while refusal/postponement remains selectable");
        Take(story, scene, "terms", poor, c => c.Abort, check);
        check(!poor.Has(Lease) && !poor.Has(Raised), "Postponement creates failed-haggle liability");
        poor.CrusadeResources!["Finances"] = 500;
        check(Rules.Available(story, scene, poor), "Initial postponement cannot return");
        var refusal = World(story, 500);
        Take(story, scene, "terms", refusal, c => c.Next == "refused", check);
        Take(story, scene, "refused", refusal, c => true, check);
        check(refusal.CrusadeResources!["Finances"] == 500 && !refusal.Has(Lease), "Refusal changes resource balance");

        foreach (string mutation in new[] { "entry", "redirect", "reroll" })
        {
            var options = new JsonSerializerOptions { IncludeFields = true };
            var changed = JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(story, options), options)!;
            var host = changed.Scenes.Single(s => s.Id == Lease);
            if (mutation == "entry") host.Nodes.Single(n => n.Id == "raised").EnterSet = Array.Empty<string>();
            if (mutation == "redirect") host.Nodes[0].Choices.RemoveAll(c => c.Requires.Contains(Raised));
            if (mutation == "reroll") foreach (var c in host.Nodes.Single(n => n.Id == "rent").Choices) c.Forbids = Array.Empty<string>();
            bool rejected = false;
            try { FailedExit(changed, (ok, message) => { if (!ok) throw new InvalidOperationException(message); }); }
            catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Transaction mutation escaped acceptance: " + mutation);
        }
        Console.WriteLine("eng7-l09 transaction: exact-500 fail/Leave/reopen/settle, agreement, success, funded failure, insufficient funds, refusal; 3 mutations rejected");
    }
}
