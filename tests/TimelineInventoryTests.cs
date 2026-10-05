using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E-Q7-18: concrete Anevia producer histories, and timestamp/OR clock mutations.
internal static class TimelineInventoryTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Snapshot Native(bool killed = false)
        {
            var state = new Snapshot { Chapter = 5, Area = Drezen, Hour = 0,
                CrusadeResources = new Dictionary<string, int> { ["Favors"] = 1000, ["Finances"] = 1000, ["Materials"] = 1000 } };
            foreach (var f in new[] { "trickster", "irabeth_dead", "anevia_gone", "coronation.after", "closets.known" })
            {
                check(story.Etudes.ContainsKey(f) || story.SeenCues.ContainsKey(f) || story.SelectedAnswers.ContainsKey(f),
                    "Timeline native fixture has no binding: " + f);
                state.Flags.Add(f); state.Times[f] = 0;
            }
            if (killed) { state.Flags.Add("anevia.irabeth_killed_by_commander"); state.Times["anevia.irabeth_killed_by_commander"] = 0; }
            foreach (var unit in new[] { "b5e867e13503c6f41bb1316705efb4a2", "280d4712dceb37f4a88e98f1f4c6e64f" })
                state.AvailableContacts.Add(unit);
            Complete(state);
            return state;
        }
        void Complete(Snapshot state)
        {
            // eng-final: a new native observation recomputes live readers;
            // unavailability from before the paid return is not a save latch.
            state.Flags.ExceptWith(story.Derived.Keys);
            var pending = Rules.PendingLatches(story, state).ToArray();
            Rules.Complete(story, state);
            foreach (var flag in pending) state.Times[flag] = state.Hour;
        }
        Snapshot Play(string id, Snapshot initial, Func<Snapshot, bool> wanted)
        {
            var scene = S(id);
            var state = Program.Copy(initial);
            for (int waited = 0; !Rules.Available(story, scene, state) && waited <= 600; waited++) state.Hour++;
            check(Rules.Available(story, scene, state), "Timeline scene unavailable: " + id);
            Snapshot? Walk(string nodeId, Snapshot at, HashSet<string> visited)
            {
                if (!visited.Add(nodeId)) return null;
                var node = scene.Nodes.Single(n => n.Id == nodeId);
                foreach (var choice in node.Choices.Where(c => Rules.ChoiceAvailable(c, at)))
                {
                    var next = Program.Copy(at);
                    if (choice.Crusade != null) next.CrusadeResources![choice.Crusade.Resource] += choice.Crusade.Amount;
                    foreach (var flag in choice.Set)
                        if (next.Flags.Add(flag)) next.Times[flag] = next.Hour;
                    Complete(next);
                    var targets = Rules.NextNodes(choice).ToArray();
                    foreach (var target in targets)
                    {
                        var found = Walk(target, next, new HashSet<string>(visited));
                        if (found != null) return found;
                    }
                    if (targets.Length == 0 && !choice.Abort)
                    {
                        next.Flags.Add(id); next.Times[id] = next.Hour; Complete(next);
                        if (wanted(next)) return next;
                    }
                }
                return null;
            }
            var result = Walk(scene.Nodes[0].Id, state, new HashSet<string>());
            check(result != null, "Timeline producer has no chosen outcome: " + id);
            return result!;
        }

        // The original widow keeps her mourning interval; no new outcome gate.
        var widow = Play("anevia.trickster.gone.setup", Native(), s => s.Has("anevia.trickster.primed"));
        widow = Play("anevia.trickster.gone.wardrobe", widow, s => s.Has("anevia.trickster.returned"));
        widow = Play("anevia.trickster.gone.gate", widow, s => s.Has("anevia.trickster.gate_seen"));
        widow = Play("anevia.trickster.gone.commit", widow, s => s.Has("anevia.committed"));
        check(widow.Hour == 168, "Widow commitment violates the 168-hour mourning minimum: " + widow.Hour);

        foreach (bool killed in new[] { false, true })
        {
            var state = Native(killed);
            if (killed)
            {
                state = Play("irabeth.trickster.killed.late_step", state, s => s.Has("irabeth.trickster.raised_on_record"));
                state = Play("irabeth.trickster.killed.blow_missed", state,
                    s => s.Has("irabeth.trickster.returned") && s.Has("irabeth.trickster.cost.under_orders"));
            }
            else
            {
                state = Play("irabeth.trickster.dead.late_order", state, s => s.Has("irabeth.trickster.primed"));
                // The late order already folds the paid chapel list; do not
                // replay the retired second delivery or inject its cost flag.
                if (!state.Has("irabeth.trickster.cost.vell"))
                    state = Play("irabeth.trickster.dead.raise_list", state, s => s.Has("irabeth.trickster.cost.vell"));
                state = Play("irabeth.trickster.dead.relieved_not_dismissed", state, s => s.Has("irabeth.trickster.returned"));
            }
            check(state.Hour == 48, "Irabeth return producer is mistimed: " + state.Hour);
            state = Play("anevia.trickster.gone.fetched", state, s => s.Has("anevia.trickster.returned"));
            state = Play("anevia.trickster.gone.fetched_gate", state, s => s.Has("anevia.trickster.gate_seen"));
            state = Play("anevia.trickster.gone.fetched_commit", state, s => s.Has("anevia.trickster.declined"));
            state = Play("anevia.trickster.gone.fetched_second_ask", state, s => s.Has("anevia.committed"));
            check(state.Hour <= 168 && state.Has("anevia.trickster.cost.her_key"),
                "Post-Coronation cap or second-ask price failed: " + state.Hour);
            Console.WriteLine("E-Q7-18 " + (killed ? "raised" : "called") + ": return 48 -> letters 144 -> gate 156 -> refusal 162 -> paid yes " + state.Hour);
        }

        // eng-final: both sides of the new presence guard on one history.
        var observation = Native();
        check(observation.Has("crossroute.irabeth.unavailable"), "Unreturned death loses its presence veto");
        observation.Flags.Add("irabeth.trickster.returned");
        Complete(observation);
        check(!observation.Has("crossroute.irabeth.unavailable"), "Paid return keeps a stale absence veto");
        observation.Flags.Add("irabeth_gone");
        Complete(observation);
        check(observation.Has("crossroute.irabeth.unavailable"), "Later departure keeps stale living eligibility");

        // A 204h itinerary cannot pass by appealing to the 504h campaign cap.
        bool Age(int hour, int at, int minimum, int? maximum) => at >= 0 && at <= hour
            && hour - at >= minimum && (maximum == null || hour - at <= maximum.Value);
        check(!Age(204, 0, 0, 168) && !Age(78, 0, 168, null), "Audited timing mutations escaped their separate contracts");
        var window = new ContactWindow { Flag = "origin", MinAgeHours = 168 };
        var timing = new Snapshot { Hour = 168, Flags = new HashSet<string> { "origin" } };
        check(!Rules.ContactWindowsAvailable(new[] { window }, timing), "Missing origin timestamp accepted");
        timing.Times["origin"] = 169;
        check(!Rules.ContactWindowsAvailable(new[] { window }, timing), "Future origin timestamp accepted");
        timing.Times["origin"] = 0;
        check(Rules.ContactWindowsAvailable(new[] { window }, timing), "Exact mourning boundary withheld");

        var fixture = TricksterLatchTests.Fixture();
        var callback = new Scene { Id = "clock", Owner = "Irabeth", Relationship = "irabeth", DelayHours = 24,
            Requires = new[] { "origin" }, RequiresAnyGroups = new[] { new[] { "paid", "found" } } };
        foreach (string producer in new[] { "paid", "found" })
        {
            var at = new Snapshot { Chapter = 5, Hour = 95,
                Flags = new HashSet<string> { "origin", producer }, Times = new Dictionary<string, int> { ["origin"] = 0, [producer] = 72 } };
            check(!Rules.Available(fixture, callback, at), "OR producer opens before its own delay");
            at.Hour = 96;
            check(Rules.Available(fixture, callback, at), "OR producer cannot open at its boundary");
            at.Flags.UnionWith(new[] { "paid", "found" }); at.Times["found"] = 90;
            check(!Rules.Available(fixture, callback, at), "Later held OR producer omitted from clock");
        }
    }
}
