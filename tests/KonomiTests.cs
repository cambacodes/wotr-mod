using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KonomiTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        // The Trickster route (konomi.trickster.*) meets her outside the office by design: KonomiTricksterTests.
        var scenes = story.Scenes.Where(s => s.Relationship == "konomi" && !s.Id.StartsWith("konomi.trickster.", StringComparison.Ordinal)).ToArray();
        if (scenes.Length == 0) return;
        var drezen = scenes.Single(s => s.Id == "konomi.margin").Areas.Single();
        Scene Find(string id) => scenes.Single(s => s.Id == "konomi." + id);
        var ordinaryVisits = new HashSet<string>(new[] { "a_useful_supper", "the_upper_passage", "two_bad_prices", "the_trial_day", "a_name_beside_hers", "the_evening_she_kept" }.Select(id => "konomi." + id));

        void Play(Scene scene, Snapshot state, bool publicly, bool quiet, bool nearlyDenied = false)
        {
            check(Program.CurrentAvailable(story, scene, state), "Konomi campaign cannot open " + scene.Id);
            var node = scene.Nodes[0];
            var visited = new HashSet<string>();
            while (true)
            {
                check(visited.Add(node.Id), "Konomi campaign loop: " + scene.Id);
                var choices = node.Choices.Where(c => Rules.Match(c.Requires, c.Forbids, state)).ToArray();
                check(choices.Length > 0, "Konomi campaign dead end: " + scene.Id + "/" + node.Id);
                string? preferred = null;
                if (scene.Id == "konomi.leak" && node.Id == "start") preferred = nearlyDenied ? "lie" : publicly ? "public" : "discreet";
                if (scene.Id == "konomi.evening" && node.Id == "supper")
                    preferred = state.Has("inhuman") ? "changed" : quiet ? "quiet" : "stay";
                var choice = preferred == null ? choices[0] : choices.Single(c => c.Next == preferred);
                foreach (var flag in choice.Set)
                    if (state.Flags.Add(flag)) state.Times[flag] = state.Hour;
                var next = choice.Check?.Success ?? choice.Next;
                if (next != null)
                {
                    node = scene.Nodes.Single(n => n.Id == next);
                    continue;
                }
                check(!choice.Abort, "Konomi campaign unexpectedly aborted " + scene.Id);
                state.Flags.Add(scene.Id);
                state.Times[scene.Id] = state.Hour;
                check(!state.Has("konomi.closed"), "Konomi continuing choices closed the romance.");
                return;
            }
        }

        foreach (var startChapter in new[] { 3, 5 })
        foreach (var path in new[] { "angel", "azata", "aeon", "demon", "devil", "dragon", "legend", "trickster", "true_lich", "swarm" })
        foreach (var publicly in new[] { false, true })
        foreach (var quiet in new[] { false, true })
        {
            var state = new Snapshot { Chapter = startChapter, Hour = 1000, Area = drezen };
            state.AvailableContacts.Add("ca2d58c5c65723945857e04fb85d30ce");
            state.Flags.Add("konomi.present");
            state.Flags.Add(path);
            if (path == "true_lich" || path == "swarm") state.Flags.Add("inhuman");
            // A different relationship ending must not close this one.
            state.Flags.Add("closed");
            state.Flags.Add("seelah.closed");
            foreach (var chapter in Enumerable.Range(startChapter, 6 - startChapter))
            {
                state.Chapter = chapter;
                if (chapter == 4)
                {
                    state.Area = "7847c3e3537104f4694167af0b9fcd0e";
                    state.Hour += 72;
                    Play(Find("unsent"), state, publicly, quiet);
                    continue;
                }
                state.Area = drezen;
                for (int attempt = 0; attempt < scenes.Length; attempt++)
                {
                    state.Hour += Math.Max(72, scenes.Max(s => s.DelayHours));
                    var scene = scenes.FirstOrDefault(s => (!s.Optional || ordinaryVisits.Contains(s.Id)) && !s.Owner.EndsWith("Epilogue") && Program.CurrentAvailable(story, s, state));
                    if (scene == null) break;
                    Play(scene, state, publicly, quiet);
                }
            }
            check(state.Has("konomi.farewell_kept"), "Konomi campaign never reached farewell: " + startChapter + "/" + path);
            check(state.Has("konomi.petition_resolved") && state.Has("konomi.scandal_answered"), "Konomi campaign skipped political consequences.");
            check(state.Has("konomi.public_cost") == publicly && state.Has("konomi.traced_leak") != publicly, "Konomi publicity outcome does not match the player's decision.");
            check(state.Has("konomi.wrote") == (startChapter == 3), "Konomi late-start campaign invented an Abyss letter.");
            check(state.Has("konomi.fate_terms") == (path == "trickster"), "Konomi Trickster response selection is wrong.");
            var ending = scenes.Where(s => s.Owner == "Epilogue" && Program.CurrentAvailable(story, s, state)).Single();
            var expected = state.Has("inhuman") ? "changed" : publicly ? "public" : "private";
            check(ending.Id == "konomi.ending_" + expected, "Konomi selected the wrong ending.");
            state.Flags.Remove("konomi.present");
            check(Program.CurrentAvailable(story, ending, state), "Konomi ending incorrectly requires her capital actor.");
            state.Flags.Add("konomi.present");
            state.Flags.Add("ascended");
            check(scenes.Single(s => s.Owner == "Epilogue" && Program.CurrentAvailable(story, s, state)).Id == "konomi.ending_ascended", "Konomi ascension conflicts with another ending.");
            state.Flags.Add("konomi.closed");
            check(scenes.Single(s => s.Owner == "Epilogue" && Program.CurrentAvailable(story, s, state)).Id == "konomi.ending_apart", "Konomi separation conflicts with another ending.");
            check(!scenes.Any(s => !s.Owner.EndsWith("Epilogue") && Program.CurrentAvailable(story, s, state)), "Konomi continues after separation.");
        }

        var repairing = new Snapshot { Chapter = 5, Hour = 1000, Area = drezen };
        repairing.AvailableContacts.Add("ca2d58c5c65723945857e04fb85d30ce");
        repairing.Flags.Add("konomi.present");
        foreach (var id in new[] { "margin", "reception", "letter", "evening", "disagreement", "leak", "reckoning" })
        {
            repairing.Hour += 72;
            Play(Find(id), repairing, false, true, nearlyDenied: true);
        }
        check(repairing.Has("konomi.almost_denied") && repairing.Has("konomi.apologized"), "Konomi's attempted denial has no repair conversation.");
        check(repairing.Has("konomi.scandal_answered") && !repairing.Has("konomi.closed"), "Konomi cannot continue after an accepted apology.");

        var waiting = new Snapshot { Chapter = 4, Hour = 1000 };
        waiting.Flags.Add("konomi.letter");
        check(!Program.CurrentAvailable(story, Find("unsent"), waiting), "Abyss plant callback precedes the gardening conversation.");
        waiting.Flags.Add("konomi.evening");
        waiting.Times["konomi.evening"] = waiting.Hour;
        check(!Program.CurrentAvailable(story, Find("unsent"), waiting), "Abyss letter ignores its delay.");
        waiting.Hour += 24;
        check(Program.CurrentAvailable(story, Find("unsent"), waiting), "Abyss letter remains blocked after the evening and delay.");
        var elsewhere = new Snapshot { Chapter = 3, Hour = 1000 };
        check(!Program.CurrentAvailable(story, Find("margin"), elsewhere), "Konomi appears outside Drezen.");
        elsewhere.Area = drezen;
        check(!Program.CurrentAvailable(story, Find("margin"), elsewhere), "Konomi begins without native capital presence.");
        elsewhere.Flags.Add("konomi.present");
        elsewhere.AvailableContacts.Add("ca2d58c5c65723945857e04fb85d30ce");
        check(Program.CurrentAvailable(story, Find("margin"), elsewhere), "Konomi cannot begin in Drezen.");
        foreach (var scene in scenes.Where(s => !s.Remote && !s.Owner.EndsWith("Epilogue")))
        {
            var absent = new Snapshot { Chapter = scene.Chapters.Last(), Hour = 1000, Area = drezen };
            foreach (var requirement in scene.Requires.Where(r => r != "konomi.present")) absent.Flags.Add(requirement);
            if (scene.RequiresAny.Length > 0) absent.Flags.Add(scene.RequiresAny[0]);
            check(!Program.CurrentAvailable(story, scene, absent), "Konomi meeting ignores lost contact: " + scene.Id);
            absent.Flags.Add("trickster");
            check(!Program.CurrentAvailable(story, scene, absent), "Trickster title alone invents Konomi contact: " + scene.Id);
            absent.Flags.Add("konomi.present");
            if (scene.ContactUnit != null)
            {
                check(!Program.CurrentAvailable(story, scene, absent), "Office state alone invents the physical Konomi actor: " + scene.Id);
                absent.AvailableContacts.Add(scene.ContactUnit);
            }
            check(Program.CurrentAvailable(story, scene, absent), "Native Konomi contact does not restore meeting: " + scene.Id);
            absent.Flags.Remove("konomi.present");
            check(!Program.CurrentAvailable(story, scene, absent), "Lost Konomi contact remains cached: " + scene.Id);
        }
    }
}
