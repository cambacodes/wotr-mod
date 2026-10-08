using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class GesmerhaOpeningTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var ids = new[] { "unbought_work", "along_the_grain", "whose_mark", "the_first_game", "the_unclaimed_hour", "against_the_current" };
        var scenes = ids.Select(id => story.Scenes.Single(s => s.Id == "gesmerha." + id)).ToArray();
        const string contact = "3ba3a0ff8575be8419159221177c1411";
        var reached = new HashSet<string>();
        var results = new HashSet<string>();
        foreach (var illusion in new[] { "truth", "illusions", "both" })
        foreach (bool marhevok in new[] { false, true })
        foreach (bool trickster in new[] { false, true })
        {
            var initial = new Snapshot { Chapter = 3, Hour = 1000, Area = scenes[0].Areas.Single() };
            initial.Flags.UnionWith(new[] { "gesmerha.wintersun_resolved", "seelah.committed", "jerribeth.committed" });
            if (illusion != "illusions") initial.Flags.Add("gesmerha.truth");
            if (illusion != "truth") initial.Flags.Add("gesmerha.illusions");
            if (marhevok) initial.Flags.Add("gesmerha.marhevok_rules");
            if (trickster) initial.Flags.Add("trickster");
            initial.AvailableContacts.Add(contact);
            var states = new List<Snapshot> { initial };
            foreach (var scene in scenes)
            {
                var continuing = new List<Snapshot>();
                foreach (var input in states)
                {
                    var ready = Program.Copy(input);
                    ready.Hour += scene.DelayHours;
                    check(Program.CurrentAvailable(story, scene, ready), "Gesmerha earned chain cannot continue: " + scene.Id);
                    foreach (var outcome in Program.Walk(scene, ready, (page, state) =>
                    {
                        reached.Add(scene.Id + "/" + page);
                        check(Rules.ContactAvailable(story, scene, state), "Gesmerha valid continuation lost contact.");
                        var interrupted = Program.Copy(state);
                        interrupted.AvailableContacts.Clear();
                        check(!Rules.ContactAvailable(story, scene, interrupted), "Gesmerha continuation ignores vanished actor.");
                        if (page == "trick") check(trickster, "Non-Trickster reaches fate experiment.");
                        if (page == "chief") check(!marhevok, "Gesmerha replaces living chief in text.");
                        if (page == "carver") check(marhevok, "Gesmerha invents Marhevok leadership.");
                        if (page == "illusion") check(illusion == "illusions", "Gesmerha retained-illusion branch overrides truth.");
                        // Every outcome is committed only after its last narrative page.
                        check(state.Flags.SetEquals(ready.Flags), "Gesmerha partial page writes an unplayed outcome.");
                    }))
                    {
                        foreach (var flag in initial.Flags)
                            check(outcome.Has(flag), "Gesmerha resets native history or another romance: " + flag);
                        check(!outcome.Has("gesmerha.committed"), "Gesmerha opening claims full commitment.");
                        if (!outcome.Has(scene.Id))
                        {
                            check(outcome.Flags.SetEquals(ready.Flags), "Gesmerha defer records progress.");
                            check(outcome.Times.OrderBy(x => x.Key).SequenceEqual(ready.Times.OrderBy(x => x.Key)), "Gesmerha defer changes timestamps.");
                            continue;
                        }
                        check(!Program.CurrentAvailable(story, scene, outcome), "Gesmerha completed scene repeats.");
                        if (scene.Id == "gesmerha.against_the_current")
                        {
                            check(new[] { "courting", "slow", "friendship" }.Count(x => outcome.Has("gesmerha." + x)) == 1, "Gesmerha relationship intentions overlap.");
                            check(!outcome.Has("gesmerha.first_kiss") || outcome.Has("gesmerha.courting"), "Gesmerha friendship or slow path receives kiss.");
                            check(!(outcome.Has("gesmerha.first_kiss") && outcome.Has("gesmerha.held_close")), "Gesmerha mutually exclusive affection outcomes overlap.");
                            check(outcome.Has("gesmerha.opening_kept"), "Gesmerha final visit lacks completion.");
                            results.UnionWith(outcome.Flags);
                        }
                        continuing.Add(outcome);
                    }
                }
                states = continuing.GroupBy(s => string.Join("|", s.Flags.OrderBy(x => x))).Select(g => g.First()).ToList();
                check(states.Count > 0, "Gesmerha has no completed scene path.");
            }
        }
        foreach (var scene in scenes)
        {
            check(scene.ContactUnit == contact && !scene.Remote, "Gesmerha loses living local contact contract.");
            foreach (var page in scene.Nodes) check(reached.Contains(scene.Id + "/" + page.Id), "Unplayed Gesmerha page: " + scene.Id + "/" + page.Id);
            var ready = new Snapshot { Chapter = 3, Hour = 1000, Area = scene.Areas.Single() };
            ready.Flags.UnionWith(scene.Requires);
            ready.Flags.Add("gesmerha.truth");
            ready.AvailableContacts.Add(contact);
            check(Program.CurrentAvailable(story, scene, ready), "Gesmerha gate baseline invalid.");
            foreach (var flag in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag);
                check(!Program.CurrentAvailable(story, scene, blocked), "Gesmerha ignores blocker: " + flag);
            }
            foreach (var flag in scene.Requires.Concat(new[] { "gesmerha.truth" }).Where(key => !key.EndsWith(".present_now", StringComparison.Ordinal) && !key.EndsWith(".reachable_by_letter", StringComparison.Ordinal)))
            {
                var blocked = Program.Copy(ready); blocked.Flags.Remove(flag);
                check(!Program.CurrentAvailable(story, scene, blocked), "Gesmerha ignores missing prerequisite: " + flag);
                check(!Rules.ContactAvailable(story, scene, blocked), "Gesmerha continuation ignores missing prerequisite: " + flag);
            }
            var dead = Program.Copy(ready); dead.Flags.Add("gesmerha.dead");
            check(!Rules.ContactAvailable(story, scene, dead), "Gesmerha dead actor continues dialog.");
            var elsewhere = Program.Copy(ready); elsewhere.Area = "elsewhere";
            check(!Program.CurrentAvailable(story, scene, elsewhere) && !Rules.ContactAvailable(story, scene, elsewhere), "Gesmerha visit ignores location.");
            foreach (int chapter in new[] { 2, 4, 5 })
            {
                var wrong = Program.Copy(ready); wrong.Chapter = chapter;
                check(!Program.CurrentAvailable(story, scene, wrong), "Gesmerha opening escapes Chapter 3.");
            }
            if (scene.DelayHours > 0)
            {
                ready.Times[scene.Requires.Last()] = ready.Hour;
                ready.Hour += scene.DelayHours - 1;
                check(!Program.CurrentAvailable(story, scene, ready), "Gesmerha skips visit delay.");
                ready.Hour++;
                check(Program.CurrentAvailable(story, scene, ready), "Gesmerha misses delay boundary.");
            }
        }
        foreach (var flag in new[] { "grain_found", "grain_missed", "grain_cut", "own_mark", "introduced", "finished_rule", "changed_rule", "first_kiss", "held_close", "slow", "friendship" })
            check(results.Contains("gesmerha." + flag), "Gesmerha traversal missed consequence: " + flag);
        var roll = scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Single(c => c.Check != null).Check!;
        check(roll.Skill == "SkillLoreNature" && roll.DC == 23 && roll.CommanderOnly, "Gesmerha native wood examination check changed.");
    }
}
