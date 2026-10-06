using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class VellexiaOpeningTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var ids = new[] { "unfinished_likeness", "second_painter", "price_of_novelty", "two_observers", "unadvertised_hour", "a_question_kept" };
        var scenes = ids.Select(id => story.Scenes.Single(s => s.Id == "vellexia." + id)).ToArray();
        const string contact = "a32a07903e428d34cb0e98a804d40569";
        var reached = new HashSet<string>();
        var results = new HashSet<string>();
        var protectedFlags = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys)
            .Concat(new[] { "vellexia.introduced", "jerribeth.committed", "jerribeth.warned", "arueshalae.committed", "wenduag.committed" }).Distinct().ToArray();
        var groups = new[]
        {
            new[] { "panel_found", "panel_missed", "panel_asked" },
            new[] { "kept_picture", "returned_picture" },
            new[] { "private_hour", "candid_hour" },
            new[] { "courting", "slow", "company" },
            new[] { "first_kiss", "held_close" }
        }.Select(g => g.Select(f => "vellexia." + f).ToArray()).ToArray();
        foreach (bool introduced in new[] { false, true })
        foreach (bool trickster in new[] { false, true })
        {
            var initial = new Snapshot { Chapter = 4, Hour = 1000, Area = scenes[0].Areas.Single() };
            initial.Flags.UnionWith(new[] { "vellexia.greeted", "jerribeth.committed", "arueshalae.committed", "wenduag.committed" });
            if (introduced) initial.Flags.UnionWith(new[] { "vellexia.introduced", "jerribeth.warned" });
            if (trickster) initial.Flags.Add("trickster");
            initial.AvailableContacts.Add(contact);
            var states = new List<Snapshot> { initial };
            foreach (var scene in scenes)
            {
                var continuing = new Dictionary<string, Snapshot>();
                foreach (var input in states)
                {
                    check(Program.CurrentAvailable(story, scene, input), "Vellexia actual preceding history cannot continue: " + scene.Id);
                    foreach (var result in Program.Walk(scene, input, (page, partial) =>
                    {
                        reached.Add(scene.Id + "/" + page);
                        check(partial.Flags.SetEquals(input.Flags), "Vellexia interruption records an unplayed outcome.");
                        check(partial.Times.OrderBy(p => p.Key).SequenceEqual(input.Times.OrderBy(p => p.Key)), "Vellexia intermediate page changes timestamps.");
                        check(Rules.ContactAvailable(story, scene, partial), "Vellexia valid local contact rejected.");
                        var vanished = Program.Copy(partial); vanished.AvailableContacts.Clear();
                        check(!Rules.ContactAvailable(story, scene, vanished), "Vellexia vanished actor can continue.");
                        if (page == "jerribeth") check(introduced, "Vellexia invents Jerribeth's advice.");
                    }))
                    {
                        foreach (var flag in protectedFlags) check(input.Has(flag) == result.Has(flag), "Vellexia opening changes native or existing relationship history: " + flag);
                        check(result.AvailableContacts.SetEquals(input.AvailableContacts), "Vellexia opening manufactures a native actor.");
                        foreach (var group in groups) check(group.Count(result.Has) <= 1, "Vellexia incompatible outcomes overlap.");
                        check(!result.Has("vellexia.committed"), "Vellexia opening grants full commitment.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(input.Flags), "Vellexia deferral changes history.");
                            continue;
                        }
                        check(!Program.CurrentAvailable(story, scene, result), "Vellexia completed book can repeat.");
                        if (scene == scenes.Last())
                        {
                            check(result.Has("vellexia.opening_kept"), "Vellexia opening lacks final milestone.");
                            check(!result.Has("vellexia.first_kiss") || result.Has("vellexia.courting"), "Vellexia unchosen romance receives a kiss.");
                            check(!result.Has("vellexia.held_close") || result.Has("vellexia.courting"), "Vellexia company or slow route assumes intimate contact.");
                            results.UnionWith(result.Flags);
                        }
                        continuing[string.Join("|", result.Flags.OrderBy(f => f))] = result;
                    }
                    // Every intermediate state equals input, so restarting any interrupted page
                    // produces this same reachable book, without opposing durable outcomes.
                    foreach (var transition in new[] { "vellexia.arena_invited", "vellexia.native_finished" })
                    {
                        var paused = Program.Copy(input); paused.Flags.Add(transition);
                        check(!Program.CurrentAvailable(story, scene, paused), "Vellexia initial-window interlude escapes native transition.");
                        check(input.Flags.All(paused.Has) && !paused.Has("vellexia.closed"), "Native invitation wipes or closes authored progress.");
                    }
                }
                states = continuing.Values.ToList();
                check(states.Count > 0, "Vellexia opening has no continuing history.");
            }
        }
        foreach (var scene in scenes)
        {
            check(scene.ContactUnit == contact && !scene.Remote, "Vellexia opening loses original living-contact contract.");
            check(scene.DelayHours == 0, "Vellexia initial window requires daylong return visits.");
            check(scene.AnswerLists.SequenceEqual(new[] { "7f394dd6cd32c44408a59bd08eb1512a" }), "Vellexia opening patches the wrong native answer list.");
            foreach (var node in scene.Nodes) check(reached.Contains(scene.Id + "/" + node.Id), "Unvisited Vellexia opening page: " + scene.Id + "/" + node.Id);
            var ready = new Snapshot { Chapter = 4, Hour = 1000, Area = scene.Areas.Single() };
            ready.Flags.UnionWith(scene.Requires);
            ready.AvailableContacts.Add(contact);
            check(Program.CurrentAvailable(story, scene, ready), "Vellexia independent gate baseline invalid.");
            foreach (var flag in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag);
                check(!Program.CurrentAvailable(story, scene, blocked), "Vellexia ignores entry blocker: " + flag);
                if (story.SeenCues.ContainsKey(flag) || story.CompletedQuests.ContainsKey(flag))
                    check(!Rules.ContactAvailable(story, scene, blocked), "Vellexia continues after native departure history changes: " + flag);
            }
            foreach (var flag in scene.Requires.Where(requiredKey => !requiredKey.EndsWith(".present_now", StringComparison.Ordinal) && !requiredKey.EndsWith(".reachable_by_letter", StringComparison.Ordinal)))
            {
                var blocked = Program.Copy(ready); blocked.Flags.Remove(flag);
                check(!Program.CurrentAvailable(story, scene, blocked) && !Rules.ContactAvailable(story, scene, blocked), "Vellexia ignores missing prerequisite: " + flag);
            }
            foreach (var flag in story.Relationships["vellexia"].UnavailableFlags)
            {
                var unavailable = Program.Copy(ready); unavailable.Flags.Add(flag);
                check(!Rules.ContactAvailable(story, scene, unavailable), "Vellexia dead/hostile history continues: " + flag);
            }
            foreach (int chapter in new[] { 3, 5 })
            {
                var wrong = Program.Copy(ready); wrong.Chapter = chapter;
                check(!Program.CurrentAvailable(story, scene, wrong), "Vellexia initial interlude escapes Chapter 4.");
            }
            var elsewhere = Program.Copy(ready); elsewhere.Area = "other";
            check(!Program.CurrentAvailable(story, scene, elsewhere) && !Rules.ContactAvailable(story, scene, elsewhere), "Vellexia appears outside loaded Upper City.");
        }
        foreach (string suffix in new[] { "panel_found", "panel_missed", "panel_asked", "kept_picture", "returned_picture", "private_hour", "candid_hour", "first_kiss", "held_close", "slow", "company" })
            check(results.Contains("vellexia." + suffix), "Vellexia traversal missed authored consequence: " + suffix);
        var roll = scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Single(c => c.Check != null).Check!;
        check(roll.Skill == "SkillKnowledgeArcana" && roll.DC == 28 && roll.CommanderOnly, "Vellexia actual arcane examination check changed.");
    }
}
