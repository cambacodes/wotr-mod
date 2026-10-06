using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class ArsinoeOpeningTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var openingIds = new HashSet<string> { "arsinoe_city_on_paper", "arsinoe_printers_view", "arsinoe_roofs", "arsinoe_first_impression", "arsinoe_hours_of_her_own" };
        var scenes = story.Scenes.Where(s => openingIds.Contains(s.Id)).ToArray();
        var outcomes = new HashSet<string>();
        var evening = scenes.Single(s => s.Id == "arsinoe_hours_of_her_own");
        var eveningReady = new Snapshot { Chapter = 3, Area = evening.Areas.Single(), Hour = 1000 };
        eveningReady.Flags.UnionWith(evening.Requires);
        eveningReady.Flags.UnionWith(new[] { "arsinoe.courting", "arsinoe.next_walk" });
        eveningReady.AvailableContacts.Add(evening.ContactUnit!);
        Program.Walk(evening, eveningReady, (id, state) =>
        {
            if (id != "kiss") return;
            var interruptedKiss = Program.Copy(state);
            interruptedKiss.AvailableContacts.Clear();
            check(!Rules.ContactAvailable(story, evening, interruptedKiss), "Kiss scene retains lost contact.");
            check(!interruptedKiss.Has("arsinoe.first_kiss"), "Arsinoe kiss recorded before its page is acknowledged.");
            interruptedKiss.AvailableContacts.Add(evening.ContactUnit!);
            bool tookHand = false;
            Program.Walk(evening, interruptedKiss, (replayId, replay) =>
            {
                if (replayId != "hand") return;
                tookHand = true;
                check(!replay.Has("arsinoe.first_kiss"), "Interrupted kiss leaks into hand-only replay.");
            });
            check(tookHand, "Interrupted kiss cannot choose the hand-only replay.");
        });
        var printer = scenes.Single(s => s.Id == "arsinoe_printers_view");
        var printerReady = new Snapshot { Chapter = 3, Area = printer.Areas.Single(), Hour = 1000 };
        printerReady.Flags.UnionWith(printer.Requires);
        printerReady.AvailableContacts.Add(printer.ContactUnit!);
        var interruptedOrders = new List<Snapshot>();
        Program.Walk(printer, printerReady, (id, state) =>
        {
            if (id == "fantasy" || id == "street") interruptedOrders.Add(Program.Copy(state));
        });
        foreach (var partial in interruptedOrders)
        {
            partial.AvailableContacts.Clear();
            check(!Rules.ContactAvailable(story, printer, partial), "Interrupted printer scene retains contact.");
            partial.AvailableContacts.Add(printer.ContactUnit!);
            check(Program.CurrentAvailable(story, printer, partial), "Interrupted printer scene cannot resume.");
            foreach (var replay in Program.Walk(printer, partial).Where(s => s.Has(printer.Id)))
                check(new[] { "arsinoe.print_fantasy", "arsinoe.print_street" }.Count(replay.Has) == 1,
                    "Interrupted printer replay records contradictory commissions.");
        }
        var roof = scenes.Single(s => s.Nodes.Any(n => n.Id == "touch"));
        var roofReady = new Snapshot { Chapter = 3, Area = roof.Areas.Single(), Hour = 1000 };
        roofReady.Flags.UnionWith(roof.Requires);
        roofReady.AvailableContacts.Add(roof.ContactUnit!);
        var interrupted = new List<Snapshot>();
        Program.Walk(roof, roofReady, (id, state) =>
        {
            if (id == "touch" || id == "slow" || id == "friend") interrupted.Add(Program.Copy(state));
        });
        foreach (var partial in interrupted)
        {
            partial.AvailableContacts.Clear();
            check(!Rules.ContactAvailable(story, roof, partial), "Interrupted roof scene retains contact.");
            check(!partial.Has(roof.Id), "Partial roof conversation is marked complete.");
            partial.AvailableContacts.Add(roof.ContactUnit!);
            check(Program.CurrentAvailable(story, roof, partial), "Restored roof conversation cannot be replayed.");
            foreach (var replay in Program.Walk(roof, partial).Where(s => s.Has(roof.Id)))
                check(new[] { "arsinoe.courting", "arsinoe.slow", "arsinoe.friendship" }.Count(replay.Has) == 1,
                    "Interrupted Arsinoe roof replay accumulates conflicting relationship choices.");
        }
        foreach (int chapter in new[] { 3, 5 })
        {
            var initial = new Snapshot { Chapter = chapter, Area = scenes[0].Areas.Single(), Hour = 1000 };
            initial.Flags.UnionWith(new[] { "arsinoe.capital", "seelah.committed", "konomi.committed" });
            initial.AvailableContacts.Add(scenes[0].ContactUnit!);
            var states = new List<Snapshot> { initial };
            foreach (var scene in scenes)
            {
                var next = new List<Snapshot>();
                foreach (var input in states)
                {
                    var ready = Program.Copy(input);
                    ready.Hour += scene.DelayHours;
                    check(Program.CurrentAvailable(story, scene, ready), "Arsinoe cannot continue played history: " + scene.Id);
                    foreach (var result in Program.Walk(scene, ready))
                    {
                        check(result.Has("seelah.committed") && result.Has("konomi.committed"), "Arsinoe changes another romance.");
                        check(!result.Has("arsinoe.committed"), "Arsinoe opening awards full commitment.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags), "Arsinoe deferral writes progress.");
                            continue;
                        }
                        check(!Program.CurrentAvailable(story, scene, result), "Arsinoe repeats completed scene.");
                        check(!result.Has("arsinoe.first_kiss") || result.Has("arsinoe.courting"), "Arsinoe kisses outside courtship.");
                        // Sol r6 INT: accepting her first invitation sets the StartedFlag, so the journal objective opens.
                        check(result.Has(story.Relationships["arsinoe"].StartedFlag), "Accepted Arsinoe invitation does not start her relationship.");
                        foreach (string flag in new[] { "arsinoe.print_source_found", "arsinoe.print_source_uncertain", "arsinoe.print_asked", "arsinoe.print_listened", "arsinoe.first_kiss", "arsinoe.friendship", "arsinoe.slow" })
                            if (result.Has(flag)) outcomes.Add(flag);
                        next.Add(result);
                    }
                }
                check(next.Count > 0, "Arsinoe has no complete continuing path.");
                states = next;
            }
            check(states.All(s => s.Has("arsinoe.opening_kept")), "Arsinoe loses opening completion.");
            check(states.All(s => new[] { "arsinoe.courting", "arsinoe.slow", "arsinoe.friendship" }.Count(s.Has) == 1), "Arsinoe loses chosen relationship pace.");
        }
        check(outcomes.Count == 7, "Arsinoe traversal misses a roll outcome, alternate method or relationship pace.");

        foreach (var scene in scenes)
        {
            var ready = new Snapshot { Chapter = 3, Area = scene.Areas.Single(), Hour = 1000 };
            ready.Flags.UnionWith(scene.Requires);
            ready.AvailableContacts.Add(scene.ContactUnit!);
            check(Program.CurrentAvailable(story, scene, ready), "Arsinoe contact baseline invalid.");
            foreach (string blocker in new[] { "arsinoe.victims_revived", "swarm", "true_lich" })
            {
                var blocked = Program.Copy(ready);
                blocked.Flags.Add(blocker);
                check(!Program.CurrentAvailable(story, scene, blocked), "Arsinoe entry ignores native restriction: " + blocker);
                check(!Rules.ContactAvailable(story, scene, blocked), "Arsinoe continuation ignores native restriction: " + blocker);
                blocked.Flags.Remove(blocker);
                check(Program.CurrentAvailable(story, scene, blocked) == (blocker == "arsinoe.victims_revived"),
                    "Removing a restriction invents a return from the conversion departure.");
            }
            var absent = Program.Copy(ready);
            absent.AvailableContacts.Clear();
            check(!Rules.ContactAvailable(story, scene, absent), "Arsinoe continues without live actor.");
            var moved = Program.Copy(ready);
            moved.Flags.Remove("arsinoe.capital");
            check(!Rules.ContactAvailable(story, scene, moved), "Arsinoe ignores loss of native capital role.");
            foreach (int chapter in new[] { 1, 2, 4, 6 })
            {
                var wrongChapter = Program.Copy(ready); wrongChapter.Chapter = chapter;
                check(!Program.CurrentAvailable(story, scene, wrongChapter), "Arsinoe appears outside authored campaign chapters.");
            }
        }
    }
}
