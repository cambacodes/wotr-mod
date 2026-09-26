using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KianaFurtherTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "kiana." + id);
        var scenes = new[] { "borrowed_name", "yard_evening", "unborrowed_evening" }.Select(Find).ToArray();
        var capstone = Find("a_place_afterward");
        var offer = Find("later_incident");
        var farewell = Find("farewell");
        var route = new Story { Scenes = story.Scenes.Where(s => s.Relationship == "kiana").ToList(), Relationships = story.Relationships };
        var protectedFlags = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys)
            .Concat(new[] { "seelah.committed", "arueshalae.committed", "kiana.separated", "kiana.bereaved", "kiana.affair", "kiana.waited",
                "kiana.committed", "kiana.future_open", "kiana.future_settled", "kiana.farewell", "kiana.farewell_kept" }).Distinct().ToArray();
        var groups = new[]
        {
            new[] { "further_plain", "further_stiff", "further_private" },
            new[] { "further_offer", "further_withdraw" },
            new[] { "further_spoke", "further_listened" },
            new[] { "further_wait_voice", "further_answer_abuse" },
            new[] { "further_private_evening", "further_private_walk" }
        }.Select(g => g.Select(f => "kiana." + f).ToArray()).ToArray();
        var seen = new HashSet<string>();
        var replay = new Dictionary<string, (Scene Scene, Snapshot State)>();
        string[] Endings(Snapshot state) => story.Scenes.Where(s => s.Relationship == "kiana" && s.Owner == "Epilogue" && Rules.Available(story, s, state)).Select(s => s.Id).ToArray();
        Snapshot Play(string id, Snapshot input, Func<Snapshot, bool>? select = null)
        {
            var scene = Find(id); var ready = Program.Copy(input); ready.Hour += scene.DelayHours;
            check(Rules.Available(story, scene, ready), "Kiana actual predecessor unavailable: " + id);
            return Program.Walk(scene, ready).First(s => s.Has(scene.Id) && !s.Has("kiana.closed") && (select == null || select(s)));
        }
        void Preserve(Snapshot before, Snapshot after)
        {
            foreach (string flag in protectedFlags) check(before.Has(flag) == after.Has(flag), "Kiana further rewrites existing history: " + flag);
            foreach (string flag in new[] { "kiana.farewell", "kiana.farewell_kept", "kiana.future_settled" })
                if (before.Times.TryGetValue(flag, out int hour)) check(after.Times.TryGetValue(flag, out int afterHour) && hour == afterHour, "Kiana further retimes old history.");
            check(before.AvailableContacts.SetEquals(after.AvailableContacts), "Kiana further manufactures native actors.");
        }
        check(capstone.Requires.Contains("kiana.further_kept"), "Fresh Kiana capstone bypasses the new played consequence.");
        check(offer.ManualOnly && Rules.IsRemote(offer), "Older Kiana opt-in must remain manual.");
        foreach (string history in new[] { "waited", "affair", "widow" })
        foreach (bool committed in new[] { false, true })
        {
            var initial = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            initial.Flags.UnionWith(new[] { "seelah.souls_returned", "kiana.aftermath_seen", "seelah.committed", "arueshalae.committed" });
            if (history == "widow") initial.Flags.Add("seelah.elan_dead");
            var state = Play("invitation", initial);
            state = Play("rehearsal", state); state = Play("stagecraft", state);
            if (history == "widow") state = Play("widow", state);
            else { state = Play("marriage", state, s => s.Has("kiana." + history)); state = Play("answer", state); }
            state = Play("date", state); state = Play("morning", state, s => s.Has("kiana.committed") == committed);
            state = Play("seelah", state);
            foreach (string id in new[] { "guest_table", "market_weather", "lenna_door", "blue_room", "bakery_stairs", "last_page", "first_readers", "ink_after", "working_room", "kept_evening" }) state = Play(id, state);
            var fullBefore = Program.Copy(state);
            foreach (string age in new[] { "fresh", "old_decision", "old_farewell", "old_early_farewell" })
            {
                state = Program.Copy(fullBefore);
                if (age == "old_early_farewell")
                {
                    state.Flags.UnionWith(new[] { "kiana.farewell", "kiana.farewell_kept", "kiana.catchup_requested" });
                    state.Times["kiana.farewell"] = 500;
                }
                bool developedOld = age == "old_decision" || age == "old_farewell";
                if (developedOld)
                {
                    // Play the previously released capstone graph to reconstruct an older save.
                    // Current entry correctly requires the new milestone, so it is not used here.
                    state = Program.Walk(capstone, state).First(s => s.Has(capstone.Id) && !s.Has("kiana.closed") && s.Has("kiana.committed") == committed);
                    if (age == "old_farewell") state = Play("farewell", state);
                    var endings = Endings(state);
                    state.Hour += 10000;
                    check(!Rules.Available(story, scenes[0], state), "An older developed save silently opts into new Kiana scenes.");
                    check(Rules.Available(story, offer, state), "Older Kiana save lacks explicit opt-in.");
                    var answers = Program.Walk(offer, state);
                    var deferred = answers.Single(s => !s.Has(offer.Id));
                    check(deferred.Flags.SetEquals(state.Flags), "Deferring Kiana opt-in changes history.");
                    state = answers.Single(s => s.Has(offer.Id));
                    check(state.Has("kiana.further_requested") && state.Has("kiana.catchup_requested"), "Kiana opt-in fails to permit her later incident.");
                    check(Endings(state).SequenceEqual(endings), "Kiana opt-in rewrites an older developed ending.");
                }
                else check(!Rules.Available(story, offer, state), "Fresh Kiana route receives an older-developed opt-in.");
                var states = new List<Snapshot> { state };
                foreach (var scene in scenes)
                {
                    var next = new Dictionary<string, Snapshot>();
                    foreach (var input in states)
                    {
                        var ready = Program.Copy(input); ready.Hour += scene.DelayHours;
                        check(Rules.Available(story, scene, ready), "Kiana further chain cannot enter " + scene.Id + "/" + age);
                        if (!developedOld)
                        {
                            check(!Rules.Available(story, capstone, ready) && !Rules.Available(story, farewell, ready), "Kiana capstone or farewell bypasses the incident.");
                            check(Rules.NextRemote(route, ready)?.Id == scene.Id, "Kiana automatic queue skips required further scene.");
                        }
                        foreach (var result in Program.Walk(scene, ready, (node, partial) =>
                        {
                            seen.Add(scene.Id + "/" + node);
                            string key = scene.Id + "/" + node + "/" + history + "/" + string.Join(",", groups.SelectMany(g => g).Where(partial.Has));
                            replay.TryAdd(key, (scene, Program.Copy(partial)));
                            if (node == "widow" || node == "bereaved") check(partial.Has("seelah.elan_dead") && !partial.Has("kiana.separated"), "Kiana invents widowhood.");
                            if (node == "separated" || node == "waited" || node == "affair") check(partial.Has("kiana.separated") && !partial.Has("seelah.elan_dead"), "Kiana invents a living separated Elan.");
                        }))
                        {
                            Preserve(ready, result);
                            foreach (var group in groups) check(group.Count(result.Has) <= 1, "Kiana further records opposing outcomes.");
                            if (!result.Has(scene.Id))
                            {
                                check(result.Flags.SetEquals(ready.Flags), "Kiana further deferral changes progress.");
                                check(result.Times.Count == ready.Times.Count, "Kiana further deferral changes timestamps.");
                                continue;
                            }
                            check(!Rules.Available(story, scene, result), "Kiana further repeats completed scene.");
                            next[string.Join("|", result.Flags.OrderBy(f => f))] = result;
                        }
                    }
                    check(next.Count > 0, "Kiana further has no completed path.");
                    states = next.Values.ToList();
                }
                foreach (var result in states)
                {
                    check(result.Has("kiana.further_kept"), "Kiana finishes without a genuine completion milestone.");
                    check(result.Has("kiana.further_private_evening") != result.Has("kiana.further_private_walk"), "Kiana loses the selected final evening.");
                    var later = Program.Copy(result); later.Hour += capstone.DelayHours;
                    check(Rules.Available(story, capstone, later) == !developedOld, "Kiana new capstone gate replays old decisions or blocks fresh ones.");
                    check(!Rules.Available(story, offer, later), "Completed Kiana incident offers another old-save invitation.");
                }
            }
        }
        foreach (var example in replay.Values)
        {
            var input = Program.Copy(example.State); input.Hour += 1000;
            foreach (var result in Program.Walk(example.Scene, input))
            {
                Preserve(input, result);
                foreach (var group in groups) check(group.Count(result.Has) <= 1, "Interrupted Kiana replay accumulates incompatible choices: " + example.Scene.Id);
            }
        }
        foreach (var scene in scenes.Append(offer))
        {
            // The reconciliation suite separately walks changed native histories.
            if (scene != offer) foreach (var node in scene.Nodes.Where(n => !n.Id.EndsWith("_former_grief") && !n.Id.EndsWith("_uncertain"))) check(seen.Contains(scene.Id + "/" + node.Id), "Kiana further page not visited: " + scene.Id + "/" + node.Id);
            var ready = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            ready.Flags.UnionWith(scene.Requires); ready.Flags.Add("kiana.separated");
            check(Rules.Available(story, scene, ready), "Kiana further gate baseline invalid.");
            foreach (string flag in new[] { "kiana.closed", "inhuman" })
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag); blocked.Flags.UnionWith(new[] { "kiana.catchup_requested", "kiana.further_requested" });
                check(!Rules.Available(story, scene, blocked), "Kiana old-save exception overrides " + flag);
            }
            foreach (string flag in scene.Requires)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Remove(flag);
                check(!Rules.Available(story, scene, blocked), "Kiana further skips prerequisite " + flag);
            }
            var wrong = Program.Copy(ready); wrong.Chapter = 4;
            check(!Rules.Available(story, scene, wrong), "Kiana further appears in the Abyss.");
            wrong = Program.Copy(ready); wrong.Area = "another-area";
            check(!Rules.Available(story, scene, wrong), "Kiana further appears outside Drezen.");
            if (scene.DelayHours > 0)
            {
                ready.Times[scene.Requires.Last()] = ready.Hour;
                ready.Hour += scene.DelayHours - 1; check(!Rules.Available(story, scene, ready), "Kiana further skips delay.");
                ready.Hour++; check(Rules.Available(story, scene, ready), "Kiana further misses exact delay boundary.");
            }
        }
    }
}
