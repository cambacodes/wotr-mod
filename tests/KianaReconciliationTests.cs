using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KianaReconciliationTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "kiana." + id);
        var touched = new[] { "guest_table", "market_weather", "blue_room", "bakery_stairs", "a_place_afterward", "yard_evening", "unborrowed_evening" };
        var seen = new HashSet<string>();
        var replay = new Dictionary<string, (Scene Scene, Snapshot State)>();
        Snapshot Play(string id, Snapshot input, Func<Snapshot, bool>? choose = null)
        {
            var scene = Find(id);
            var ready = Program.Copy(input);
            ready.Hour += scene.DelayHours;
            check(Rules.Available(story, scene, ready), "Kiana reconciliation actual chain unavailable: " + id);
            var outcomes = Program.Walk(scene, ready, (node, partial) =>
            {
                if (!touched.Contains(id)) return;
                seen.Add(id + "/" + node);
                if (node.EndsWith("_former_grief") || node.EndsWith("_uncertain"))
                {
                    check(node.EndsWith("_former_grief") == partial.Has("kiana.separated"), "Kiana selects the wrong reconciled history.");
                    replay.TryAdd(id + "/" + node + "/" + input.Has("kiana.affair"), (scene, Program.Copy(partial)));
                }
            });
            var completed = outcomes.Where(s => s.Has(scene.Id) && !s.Has("kiana.closed")).ToArray();
            check(completed.Length > 0, "Kiana reconciliation has no continuing outcome: " + id);
            foreach (var result in completed.Where(_ => touched.Contains(id)))
            foreach (var flag in new[] { "kiana.separated", "kiana.bereaved", "seelah.elan_dead", "kiana.waited", "kiana.affair", "seelah.committed", "arueshalae.committed" })
                check(result.Has(flag) == ready.Has(flag), "Kiana reconciliation rewrites existing history: " + flag);
            return completed.First(s => choose == null || choose(s));
        }
        foreach (string history in new[] { "waited", "affair", "bereaved" })
        foreach (bool changed in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(new[] { "seelah.souls_returned", "kiana.aftermath_seen", "seelah.committed", "arueshalae.committed" });
            if (history == "bereaved") state.Flags.Add("seelah.elan_dead");
            state = Play("invitation", state);
            state = Play("rehearsal", state);
            state = Play("stagecraft", state);
            if (history == "bereaved") state = Play("widow", state);
            else
            {
                state = Play("marriage", state, s => s.Has("kiana." + history));
                state = Play("answer", state);
            }
            state = Play("date", state);
            state = Play("morning", state, s => s.Has("kiana.committed"));
            state = Play("seelah", state);
            // Simulate a later native snapshot, not a mutation authored by the route.
            if (changed)
            {
                if (history == "bereaved") state.Flags.Remove("seelah.elan_dead");
                else state.Flags.Add("seelah.elan_dead");
            }
            var initial = Program.Copy(state);
            foreach (var id in new[] { "guest_table", "market_weather", "lenna_door", "blue_room", "bakery_stairs", "last_page", "first_readers", "ink_after", "working_room", "kept_evening", "borrowed_name", "yard_evening", "unborrowed_evening", "a_place_afterward" })
                state = Play(id, state);
            check(state.Has("kiana.future_settled"), "Reconciled Kiana cannot complete the developed capstone.");
            var correspondence = Find(history == "bereaved" ? "uncertain_reports" : "former_grief");
            check(correspondence.ManualOnly && Rules.IsRemote(correspondence), "Reconciliation letter must remain explicitly requested.");
            check(Rules.Available(story, correspondence, state) == changed, "Kiana reconciliation letter has the wrong native-history gate.");
            if (changed)
            {
                state.Flags.UnionWith(new[] { "kiana.farewell", "kiana.farewell_kept" });
                state.Times["kiana.farewell"] = 200;
                check(Rules.Available(story, correspondence, state), "Old completed Kiana history cannot request correspondence.");
                foreach (var result in Program.Walk(correspondence, state, (node, partial) =>
                    replay.TryAdd(correspondence.Id + "/" + node, (correspondence, Program.Copy(partial)))))
                {
                    foreach (var flag in state.Flags) check(result.Has(flag), "Kiana correspondence removed an existing flag.");
                    check(result.Times["kiana.farewell"] == 200, "Kiana correspondence retimes an old farewell.");
                    check(result.AvailableContacts.SetEquals(state.AvailableContacts), "Kiana correspondence manufactures an actor.");
                    if (!result.Has(correspondence.Id)) check(result.Flags.SetEquals(state.Flags), "Deferring reconciliation mutates history.");
                }
            }
            check(initial.Has("kiana.separated") == state.Has("kiana.separated") && initial.Has("kiana.bereaved") == state.Has("kiana.bereaved"), "Kiana original marital history was rewritten.");
        }
        foreach (var id in touched)
        foreach (var node in Find(id).Nodes.Where(n => n.Id.EndsWith("_former_grief") || n.Id.EndsWith("_uncertain")))
            check(seen.Contains(id + "/" + node.Id), "Unvisited Kiana reconciliation branch: " + id + "/" + node.Id);
        foreach (var pair in replay.Values)
            check(Program.Walk(pair.Scene, pair.State).Any(s => s.Has(pair.Scene.Id)), "Interrupted Kiana reconciliation cannot resume its book.");
    }
}
