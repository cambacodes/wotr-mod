using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class TargonaOpeningTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        string[] ids = { "unasked_question", "second_margin", "the_folded_room", "an_unpromised_future", "the_unscheduled_door", "what_she_keeps" };
        var scenes = ids.Select(id => story.Scenes.Single(s => s.Id == "targona." + id)).ToArray();
        var focused = new Story { Scenes = scenes.ToList(), Relationships = story.Relationships };
        var seen = scenes.ToDictionary(s => s.Id, _ => new HashSet<string>());
        var native = story.Etudes.Keys.Concat(story.CompletedQuests.Keys).Concat(story.CompletedEtudes.Keys)
            .Concat(story.SelectedAnswers.Keys).Concat(story.SeenCues.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();
        string[] modes = { "none", "angel", "azata", "aeon", "trickster" };
        string[][] alternatives = {
            new[] { "targona.account_public", "targona.account_private" },
            new[] { "targona.fold_found", "targona.fold_failed", "targona.fold_cut" },
            new[] { "targona.story_leaving", "targona.story_receiving" },
            new[] { "targona.extra_ending", "targona.ordinary_ending" }
        };
        check(story.CompletedQuests["targona.ran_treatment_completed"] == "6ec03ce2f763460c8ac89f4c2064c5ad",
            "Targona continuation does not require the real parent treatment quest.");
        check(story.SeenCues["targona.ran_final_seen"].ToHashSet().SetEquals(new[] {
            "ad655c40be31401386b85287483b3841", "cfc5f3cb2cf94672a96cab742e62225d",
            "62c24328ae744ee98fabd219dbe74c92", "ec76729da60441a1b2028f340743c0a8" }),
            "Targona finale memory uses a start marker or wrong endpoint.");

        foreach (string mode in modes)
        foreach (bool parentRomance in new[] { false, true })
        foreach (bool wardCommitted in new[] { false, true })   // polish (INT): the Trickster ward's earned commitment
        foreach (string currentPath in mode == "none" ? new[] { "angel", "trickster" } : new[] { mode })
        {
            if (wardCommitted && currentPath != "trickster") continue;
            bool romance = parentRomance || wardCommitted;
            var initial = new Snapshot { Chapter = 5, Area = scenes[0].Areas.Single(), Hour = 1000 };
            initial.Flags.UnionWith(new[] { "targona.free", "targona.ran_treatment_completed", "targona.ran_final_seen",
                "targona.ran_" + mode, currentPath, "seelah.committed", "arueshalae.committed" });
            if (parentRomance) initial.Flags.Add("targona.ran_romance");
            if (wardCommitted) initial.Flags.Add("targona.committed");
            Rules.Complete(story, initial);
            check(initial.Has("targona.correspondence_romanced") == romance, "Targona correspondence misreads the earned romance history.");
            var states = new List<Snapshot> { initial };
            for (int index = 0; index < scenes.Length; index++)
            {
                var scene = scenes[index];
                var next = new List<Snapshot>();
                check(scene.ManualOnly && Rules.IsRemote(scene) && scene.ContactUnit == null,
                    "Targona correspondence fabricates a native physical-contact requirement.");
                foreach (var prior in states)
                {
                    var ready = Program.Copy(prior);
                    if (index > 0)
                    {
                        check(!Rules.Available(story, scene, ready), "Targona reply ignores the predecessor delay.");
                        ready.Hour += scene.DelayHours;
                    }
                    check(Rules.Available(story, scene, ready), "Attainable parent history cannot enter " + scene.Id);
                    check(Rules.NextRemote(focused, ready) == null, "Targona private correspondence hijacks the rest queue.");
                    foreach (var result in Program.Walk(scene, ready, (node, partial) =>
                    {
                        seen[scene.Id].Add(node);
                        check(partial.Flags.SetEquals(ready.Flags), "Targona records an unacknowledged intermediate outcome.");
                        // Q6 r5 (CAN): Anograt appears, in any node, only in the histories whose treatment created her.
                        if (scene.Nodes.Single(x => x.Id == node).Text.Contains("Anograt", StringComparison.Ordinal))
                            check(mode == "aeon" || mode == "trickster", "Targona names Anograt in a history without her: " + scene.Id + "/" + node);
                        if (node == "anograt" || node == "two")
                            check(mode == "aeon" || mode == "trickster", "Targona invents Anograt for a different transformation history.");
                        if (node == "lover" || node == "romance")
                            check(romance, "Targona duplicates a romance after the parent friendship decision.");
                        if (node == "friend")
                            check(!romance, "Targona addresses an earned lover as a friend.");
                    }))
                    {
                        check(ready.Flags.IsSubsetOf(result.Flags), "Targona removes established history.");
                        check(native.All(f => result.Has(f) == ready.Has(f)), "Targona writes native or parent romance state.");
                        check(result.Has("seelah.committed") && result.Has("arueshalae.committed"), "Targona interferes with another romance.");
                        check(result.Has("targona.committed") == ready.Has("targona.committed"), "Correspondence silently awards or drops a full commitment.");
                        check(result.Has("targona.ran_romance") == ready.Has("targona.ran_romance"), "Correspondence rewrites the parent romance history.");
                        check(!result.Has("targona.extra_ending") || currentPath == "trickster", "A non-Trickster uses the authored fate trick.");
                        check(result.AvailableContacts.Count == 0, "A letter invents a loaded Targona actor.");
                        foreach (var group in alternatives)
                            check(group.Count(result.Has) <= 1, "Targona mixes opposing correspondence outcomes.");
                        if (result.Has(scene.Id)) next.Add(result);
                        else check(result.Flags.SetEquals(ready.Flags), "Postponing correspondence records progress.");
                    }
                }
                states = next.GroupBy(s => string.Join("|", s.Flags.OrderBy(f => f))).Select(g => g.First()).ToList();
                check(states.Count > 0, "Targona loses every continuing history.");
            }
            check(states.All(s => s.Has("targona.extension_opening_kept")), "Targona correspondence lacks a played conclusion.");
            check(states.Any(s => s.Has("targona.ordinary_ending")), "Targona forces a supernatural intervention.");
            if (currentPath == "trickster") check(states.Any(s => s.Has("targona.extra_ending")), "Trickster's bespoke continuation is unreachable.");
        }

        foreach (var scene in scenes)
        {
            check(scene.Nodes.All(n => n.Portrait == "TargonaCorrespondence"),
                "Targona correspondence falls back to unrelated speaker or Tirabade artwork.");
            check(seen[scene.Id].SetEquals(scene.Nodes.Select(n => n.Id)), "Targona has unreachable prose: " + scene.Id);
            var ready = new Snapshot { Chapter = 5, Area = scene.Areas.Single(), Hour = 1000 };
            ready.Flags.UnionWith(scene.Requires); ready.Flags.Add("targona.ran_trickster"); ready.Flags.Add("trickster");
            check(Rules.Available(story, scene, ready), "Targona gate baseline invalid.");
            foreach (string flag in scene.Requires)
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(flag);
                check(!Rules.Available(story, scene, missing), "Targona bypasses parent/native prerequisite " + flag);
            }
            foreach (string flag in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag);
                check(!Rules.Available(story, scene, blocked), "Targona rewrites excluded identity/path/death history " + flag);
            }
            var wrong = Program.Copy(ready); wrong.Flags.Remove("targona.ran_trickster");
            check(!Rules.Available(story, scene, wrong), "Trickster alone fabricates parent treatment progress.");
            wrong = Program.Copy(ready); wrong.Flags.Remove("targona.ran_final_seen"); wrong.Flags.Add("targona.ran_dialog_started");
            check(!Rules.Available(story, scene, wrong), "Starting a dialogue substitutes for the parent finale.");
            wrong = Program.Copy(ready); wrong.Chapter = 3;
            check(!Rules.Available(story, scene, wrong), "Targona extension begins before its chapter-five finale.");
            wrong = Program.Copy(ready); wrong.Area = "outside_drezen";
            check(!Rules.Available(story, scene, wrong), "Drezen correspondence invents delivery elsewhere.");
        }

        // Polish (INT): the visit and its answer open after the parent romance or the ward's commitment, never after neither.
        foreach (var id in new[] { "targona.the_open_threshold", "targona.the_key_remains_hers" })
        {
            var later = story.Scenes.Single(s => s.Id == id);
            foreach (var history in new[] { new string[0], new[] { "targona.ran_romance" }, new[] { "targona.committed" },
                                            new[] { "targona.ran_romance", "targona.committed" } })
            {
                var ready = new Snapshot { Chapter = 5, Area = later.Areas.Single(), Hour = 100000 };
                ready.Flags.UnionWith(later.Requires.Where(f => f != "targona.correspondence_romanced"));
                ready.Flags.UnionWith(history); ready.Flags.Add("targona.ran_angel");
                Rules.Complete(story, ready);
                check(Rules.Available(story, later, ready) == (history.Length > 0), "Targona visit gate misreads the earned history: " + id);
            }
        }

        var paper = scenes[2];
        var skill = paper.Nodes.SelectMany(n => n.Choices).Single(c => c.Check != null);
        check(skill.Check!.Skill == "SkillPerception" && skill.Check.DC == 25 && skill.Check.CommanderOnly
            && skill.Check.Success == "found" && skill.Check.Failure == "creased" && skill.Set.Length == 0,
            "Targona paper inspection changes its outcome/actor contract.");
        var seed = new Snapshot { Chapter = 5, Area = paper.Areas.Single(), Hour = 1000 };
        seed.Flags.UnionWith(paper.Requires); seed.Flags.Add("targona.ran_trickster");
        Program.Walk(paper, seed, (page, partial) =>
        {
            if (page != "found" && page != "creased") return;
            check(!alternatives[1].Any(partial.Has), "Targona commits an unacknowledged roll outcome.");
            var replay = Program.Copy(partial);
            check(Rules.Available(story, paper, replay), "An interrupted paper inspection cannot reopen.");
            var cut = Program.Walk(paper, replay).Where(s => s.Has("targona.fold_cut")).ToArray();
            check(cut.Length > 0 && cut.All(s => alternatives[1].Count(s.Has) == 1), "Targona failed roll contaminates non-roll replay.");
        });
    }
}
