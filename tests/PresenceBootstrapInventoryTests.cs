using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// eng7-l06: actual exported producer choices, affordability, placement and contact precede reconciliation.
internal static class PresenceBootstrapInventoryTests
{
    internal static Snapshot Fresh(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8",
            CrusadeResources = Rules.CrusadeResources.ToDictionary(k => k, k => 5000) };
        state.Flags.UnionWith(flags.Concat(new[] { "trickster", Rules.ChapterFlag(chapter)! }));
        Rules.Complete(story, state);
        return state;
    }

    internal static Snapshot Later(Story story, Snapshot original, int hours = 300)
    {
        var state = Program.Copy(original);
        state.Hour += hours;
        Recompute(story, state);
        return state;
    }

    internal static void Recompute(Story story, Snapshot state)
    {
        // Main creates a new snapshot on each tick; retain historical/native inputs, reread composites.
        state.Flags.ExceptWith(story.Derived.Keys);
        state.Flags.ExceptWith(story.Counts.Keys);
        Rules.Complete(story, state);
    }

    // Play only selectable answers, execute their resource costs, and record terminal completion.
    // Native input witnesses are supplied before this walk; outputs and composites are never seeded.
    internal static Snapshot Play(Story story, string id, Snapshot initial, string output, Action<bool, string> check, params string[] without)
    {
        var scene = story.Scenes.Single(s => s.Id == id);
        check(Program.CurrentAvailable(story, scene, initial), "Producer not available: " + id);
        Snapshot? result = null;
        var trace = new List<string>();
        bool Visit(string nodeId, Snapshot state, HashSet<string> path, List<string> selected)
        {
            if (!path.Add(nodeId)) return false;
            var node = scene.Nodes.Single(n => n.Id == nodeId);
            foreach (var choice in node.Choices.Where(c => Rules.ChoiceAvailable(c, state)))
            {
                var next = Program.Copy(state);
                if (choice.Crusade != null) next.CrusadeResources![choice.Crusade.Resource] += choice.Crusade.Amount;
                foreach (var flag in choice.Set)
                    if (next.Flags.Add(flag)) next.Times[flag] = next.Hour;
                var route = new List<string>(selected) { node.Id + "[" + node.Choices.IndexOf(choice) + "]: " + SurfaceIds.Of(story, choice) };
                foreach (var target in Rules.NextNodes(choice))
                    if (Visit(target, next, new HashSet<string>(path), route)) return true;
                if (choice.Next == null && choice.Check == null && !choice.Abort && next.Has(output) && !without.Any(next.Has))
                {
                    next.Flags.Add(scene.Id); next.Times[scene.Id] = next.Hour;
                    Rules.Complete(story, next);
                    result = next; trace = route;
                    Console.WriteLine("eng7-l06 rendered " + id + ": " + node.Text);
                    return true;
                }
            }
            return false;
        }
        Visit(scene.Nodes[0].Id, initial, new HashSet<string>(), new List<string>());
        check(result != null, "No selectable producer path to " + output + ": " + id);
        Console.WriteLine("eng7-l06 producer " + id + " -> " + output + ": " + string.Join(" -> ", trace));
        return result!;
    }

    internal static void Contact(Story story, string name, Snapshot state, Action<bool, string> check)
    {
        var presence = story.Presences[name];
        check(Rules.PresenceWanted(presence, state), "Earned bootstrap is unwanted: " + name);
        var before = new PresenceObservation { AreaLoaded = true, AnchorResolved = true,
            NativeAlive = presence.Mode == "reuse-native", NativeHidden = presence.Mode == "reuse-native" };
        var plan = Rules.PlanPresence(presence, true, before);
        check(plan.Contains(presence.Mode == "spawn-copy" ? PresenceStep.Spawn : PresenceStep.Unhide), "No placement: " + name);
        // Observe the usable actor produced by that plan (rather than granting contact at setup).
        var actors = new[] { new { Unit = presence.Unit, Usable = true } };
        var contact = Rules.SingleUsable(actors, a => a.Usable, a => !a.Usable);
        check(contact != null, "Placement did not yield one usable actor: " + name);
        state.AvailableContacts.Add(contact!.Unit);
        Console.WriteLine("eng7-l06 placement " + name + ": " + string.Join("+", plan) + " -> observed contact " + contact.Unit);
    }

    internal static void MissingAnchor(Story story, string name, Snapshot state, string fallback, Action<bool, string> check)
    {
        var failed = Program.Copy(state); failed.AvailableContacts.Clear();
        var presence = story.Presences[name];
        var seen = new PresenceObservation { AreaLoaded = true, AnchorResolved = false };
        check(Rules.PresenceFailed(presence, Rules.PresenceWanted(presence, failed), seen), "Missing anchor is unwanted: " + name);
        failed.Flags.Add(Rules.PresenceFailedFlag(name));
        Rules.Complete(story, failed);
        check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == fallback), failed), "Failed placement cannot deliver " + fallback);
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        if (!story.Derived.ContainsKey(Rules.TricksterNow)) return;
        // Both existing coffin ritual histories use their actual choices, including the blood bargain.
        foreach (bool bargained in new[] { false, true })
        {
            var state = Fresh(story, 3, "camellia.killed", "camellia.dead", "camellia.trickster.primed");
            if (bargained) state.Flags.Add("camellia.trickster.spirits_bargained");
            state = Play(story, "camellia.trickster.killed.third_night", state, "camellia.trickster.raised", check);
            state = Later(story, state);
            check(!Rules.RouteOpen(story.Relationships["camellia"], state), "Bootstrap grants Camellia's relationship");
            Contact(story, "camellia.presence", state, check);
            check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "camellia.trickster.killed.performance"), state), "Camellia reckoning blocked");
            MissingAnchor(story, "camellia.presence", state, "camellia.trickster.killed.performance_letter", check);
        }
        foreach (bool late in new[] { false, true })
        {
            var state = Fresh(story, 5, "irabeth_dead", "coronation.seen");
            if (!late) state.Flags.Add("irabeth.trickster.primed");
            state = Play(story, late ? "irabeth.trickster.dead.late_order" : "irabeth.trickster.dead.raise_list", state, "irabeth.trickster.cost.vell", check);
            state = Later(story, state);
            check(!state.Has("irabeth.trickster.returned"), "Irabeth pre-return seeded");
            Contact(story, "irabeth.presence", state, check);
            check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "irabeth.trickster.dead.relieved_not_dismissed"), state), "Irabeth reporting blocked");
        }
        {
            var state = Fresh(story, 5, "irabeth_dead", "coronation.seen", "anevia.irabeth_killed_by_commander", "irabeth.trickster.drilled");
            state = Play(story, "irabeth.trickster.killed.dig", state, "irabeth.trickster.cost.dug_out", check);
            state = Later(story, state); Contact(story, "irabeth.presence", state, check);
            check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "irabeth.trickster.killed.blow_missed"), state), "Irabeth dug-out reckoning blocked");
            var unpaid = Fresh(story, 5, "irabeth_dead", "coronation.seen", "irabeth.trickster.primed");
            unpaid.CrusadeResources!["Favors"] = 0; unpaid.CrusadeResources["Finances"] = 0;
            check(!Rules.PresenceWanted(story.Presences["irabeth.presence"], unpaid), "Unpaid Irabeth bootstrap");
            check(story.Scenes.Single(s => s.Id == "irabeth.trickster.dead.raise_list").Nodes.SelectMany(n => n.Choices)
                .Where(c => c.Crusade != null).All(c => !Rules.ChoiceAvailable(c, unpaid)), "Unaffordable resurrection selectable");
        }
        {
            var state = Fresh(story, 5, "irabeth_dead", "coronation.seen", "anevia.irabeth_killed_by_commander");
            state = Play(story, "irabeth.trickster.killed.late_step", state, "irabeth.trickster.raised_on_record", check);
            state = Later(story, state); Contact(story, "irabeth.presence", state, check);
            check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "irabeth.trickster.killed.blow_missed"), state), "Irabeth paid-record reckoning blocked");
        }
        foreach (bool sending in new[] { false, true })
        {
            var state = Fresh(story, sending ? 5 : 3, "kaylessa.dead");
            if (sending) { state.Flags.Add("shyka.gone"); Recompute(story, state); }
            state = Play(story, sending ? "kaylessa.trickster.dead.borrow_sending" : "kaylessa.trickster.dead.borrow", state, "kaylessa.trickster.primed", check);
            state = Later(story, state); Contact(story, "kaylessa.presence", state, check);
            check(!state.Has("kaylessa.trickster.returned") && Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "kaylessa.trickster.dead.soldier"), state), "Kaylessa arrival blocked");
        }
        {
            var state = Fresh(story, 5, "minagho.dead", "chivarro.dead", "chivarro.exile_objective_done");
            state = Play(story, "minagho_chivarro.trickster.react.baphomet", state, "minagho_chivarro.trickster.collateral_delivered", check);
            state = Later(story, state); Contact(story, "minagho_chivarro.presence.minagho", state, check);
            check(!Rules.RouteOpen(story.Relationships["minagho_chivarro"], state), "Solo bootstrap grants pair route");
            check(!Rules.PresenceWanted(story.Presences["minagho_chivarro.presence.chivarro"], state), "Minagho bootstrap grants unreturned Chivarro");
            check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "minagho_chivarro.trickster.minagho_dead.brand"), state), "Paid Minagho brand blocked");
            MissingAnchor(story, "minagho_chivarro.presence.minagho", state, "minagho_chivarro.trickster.minagho_dead.brand_letter", check);
            state = Play(story, "minagho_chivarro.trickster.minagho_dead.brand", state, "minagho_chivarro.trickster.returned_minagho", check);
            state = Later(story, state);
            check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "minagho_chivarro.trickster.debt.collectors"), state), "Returned solo debt consequence blocked");
            check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "minagho_chivarro.trickster.alone.minagho"), state), "Returned solo invitation blocked");
            MissingAnchor(story, "minagho_chivarro.presence.minagho", state, "minagho_chivarro.trickster.alone.minagho_letter", check);
        }
        {
            var state = Fresh(story, 4, "herrax.asked_kill_chivarro");
            state = Play(story, "minagho_chivarro.trickster.chivarro_dead.deposit", state, "minagho_chivarro.trickster.chivarro_deposit", check);
            state.Chapter = 5; state.Flags.UnionWith(new[] { "chivarro.dead", "chivarro.exile_objective_done", "minagho.dead" });
            Recompute(story, state); state = Later(story, state);
            state = Play(story, "minagho_chivarro.trickster.chivarro_dead.bought", state, "minagho_chivarro.trickster.chivarro_owned", check);
            state = Later(story, state); Contact(story, "minagho_chivarro.presence.chivarro", state, check);
            check(!Rules.RouteOpen(story.Relationships["minagho_chivarro"], state), "Chivarro solo contact grants pair availability");
            check(!Rules.PresenceWanted(story.Presences["minagho_chivarro.presence.minagho"], state), "Chivarro solo grants unreturned Minagho");
            check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "minagho_chivarro.trickster.chivarro_dead.the_bill"), state), "Solo bill blocked by dead Minagho");
            MissingAnchor(story, "minagho_chivarro.presence.chivarro", state, "minagho_chivarro.trickster.chivarro_dead.the_bill_letter", check);
        }
        {
            var state = Fresh(story, 5, "chivarro.dead", "chivarro.exile_objective_done", "minagho.spared_c4");
            state = Later(story, state); Contact(story, "minagho_chivarro.presence.minagho_spared", state, check);
            check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "minagho_chivarro.trickster.spared.brand"), state), "Living Minagho blocked by dead Chivarro");
            MissingAnchor(story, "minagho_chivarro.presence.minagho_spared", state, "minagho_chivarro.trickster.spared.brand_letter", check);
            state = Play(story, "minagho_chivarro.trickster.spared.brand", state, "minagho_chivarro.trickster.minagho_in", check);
            state = Later(story, state);
            check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "minagho_chivarro.trickster.debt.collectors_spared"), state), "Solo debt consequence blocked");
            check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "minagho_chivarro.trickster.alone.minagho_spared"), state), "Living solo invitation blocked");
            MissingAnchor(story, "minagho_chivarro.presence.minagho_spared", state, "minagho_chivarro.trickster.alone.minagho_letter", check);
        }
        foreach (bool recruited in new[] { false, true })
        {
            var state = Fresh(story, 5, "nurah.prison");
            if (recruited) state.Flags.Add("nurah.trickster_recruited");
            Contact(story, "nurah.presence.cell", state, check);
            state = Play(story, "nurah.trickster.prison.pardon_late", state, "nurah.trickster.cost.ledger_lie", check);
            state = Later(story, state);
            check(!state.Has("nurah.trickster.released"), "Cell grants release before night out");
            state = Play(story, "nurah.trickster.prison.night_out_late", state, "nurah.trickster.released", check);
        }
        {
            var state = Fresh(story, 3, "nurah.prison");
            state = Play(story, "nurah.trickster.prison.pardon", state, "nurah.trickster.cost.ledger_lie", check);
            state.Chapter = 5; state = Later(story, state);
            Contact(story, "nurah.presence.cell", state, check);
            state = Play(story, "nurah.trickster.prison.night_out_late", state, "nurah.trickster.released", check);
        }
        // eng8-q8d: the living sergeant hosts the vigil and the earned return.
        foreach (var scene in story.Scenes.Where(s => s.Id == "galfrey.trickster.iz.eulogy" || s.Id.StartsWith("galfrey.trickster.return.kitrane", StringComparison.Ordinal)))
            check(scene.ContactUnit == "8a23e71893cf8ab428e7ebd64b10ad27" && !Rules.IsRemote(scene), "Missing Galfrey sergeant delivery: " + scene.Id);
        foreach (bool scarred in new[] { false, true })
        {
            var state = Fresh(story, 5, "galfrey.dying_seen", "coronation.seen");
            state = Play(story, "galfrey.trickster.iz.offer", state,
                scarred ? "galfrey.trickster.cost.rent_scar" : "galfrey.trickster.kitrane_taken", check,
                scarred ? "galfrey.closed" : "galfrey.trickster.cost.rent_scar");
            state.Flags.Add("galfrey.dead"); Recompute(story, state); state = Later(story, state);
            check(!Rules.PresenceWanted(story.Presences["galfrey.presence"], state), "Unreturned Galfrey staged for vigil");
            Contact(story, "galfrey.presence.sergeant", state, check);
            state = Play(story, "galfrey.trickster.iz.eulogy", state, "galfrey.trickster.cost.eulogy", check);
            state = Later(story, state);
            state = Play(story, scarred ? "galfrey.trickster.return.kitrane_scarred" : "galfrey.trickster.return.kitrane",
                state, "galfrey.trickster.returned", check);
            state = Later(story, state); Contact(story, "galfrey.presence", state, check);
        }
        // eng7-f4: walk both existing thefts, then place Seelah before she has reconciled.
        foreach (bool late in new[] { false, true })
        {
            var state = Fresh(story, 3);
            if (late) { state.Flags.Add("seelah_gone"); Recompute(story, state); state = Later(story, state); }
            state = Play(story, late ? "seelah.trickster.dismissed.late" : "seelah.trickster.dismissed.setup",
                state, "seelah.trickster.primed", check);
            state.Flags.Add("seelah_gone"); Recompute(story, state); state = Later(story, state);
            check(!state.Has("seelah.trickster.returned") && !Rules.RouteOpen(story.Relationships["seelah"], state),
                "Stolen papers grant reconciliation before her answer");
            Contact(story, "seelah.presence", state, check);
            check(Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "seelah.trickster.dismissed.back_for_the_papers"), state),
                "Seelah cannot demand her stolen papers");
            MissingAnchor(story, "seelah.presence", state, "seelah.trickster.dismissed.back_for_the_papers_letter", check);
            foreach (var blocker in new[] { "seelah.closed", "seelah_dead", "trickster.failed" })
            {
                var blocked = Program.Copy(state); blocked.Flags.Add(blocker); Recompute(story, blocked);
                if (blocker == "trickster.failed")
                    check(!Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "seelah.trickster.dismissed.back_for_the_papers"), blocked),
                        "Seelah's new return act fires after leaving Trickster");
                else
                    check(!Rules.PresenceWanted(story.Presences["seelah.presence"], blocked), "Papers lift unrelated loss: " + blocker);
            }
            state = Play(story, "seelah.trickster.dismissed.back_for_the_papers", state, "seelah.trickster.returned", check);
            state = Later(story, state);
            check(Rules.RouteOpen(story.Relationships["seelah"], state), "Her answer does not complete the earned return");
        }
        {
            var unpaid = Fresh(story, 3, "seelah_gone");
            check(!Rules.PresenceWanted(story.Presences["seelah.presence"], unpaid), "Seelah returns without stolen papers");
            var otherPath = Program.Copy(unpaid); otherPath.Flags.Remove("trickster"); Recompute(story, otherPath);
            check(!Program.CurrentAvailable(story, story.Scenes.Single(s => s.Id == "seelah.trickster.dismissed.late"), otherPath),
                "Papers theft changes canon off-Trickster");
        }
        // eng7-f4 end
        foreach (var name in new[] { "camellia.presence", "irabeth.presence", "kaylessa.presence", "nurah.presence.cell", "minagho_chivarro.presence.minagho" })
        {
            var p = story.Presences[name]; string rel = Rules.PresenceRelationship(name)!;
            var closed = Fresh(story, p.MinChapter, story.Relationships[rel].ClosedFlag);
            check(!Rules.PresenceWanted(p, closed), "Closed bootstrap present: " + name);
            var unpaid = Fresh(story, p.MinChapter);
            check(!Rules.PresenceWanted(p, unpaid), "Unattempted bootstrap present: " + name);
        }
    }
}
