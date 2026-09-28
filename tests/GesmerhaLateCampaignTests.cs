using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class GesmerhaLateCampaignTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string actor = "3ba3a0ff8575be8419159221177c1411";
        const string capital = "2570015799edf594daf2f076f2f975d8";
        var earlyIds = new[] { "unbought_work", "along_the_grain", "whose_mark", "the_first_game", "the_unclaimed_hour", "against_the_current", "a_story_from_elsewhere", "the_unfinished_verse", "the_evening_answer", "what_she_asks" };
        var lateIds = new[] { "the_things_still_here", "the_box_with_two_names", "the_long_way_with_company", "a_lesson_without_her", "the_room_she_chose", "the_work_left_finished" };
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "gesmerha." + id);
        var late = lateIds.Select(Find).ToArray();
        var oldReunion = Find("the_voice_at_court");
        var endings = story.Scenes.Where(s => s.Relationship == "gesmerha" && s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var reached = new HashSet<string>();
        var outputs = new HashSet<string>();
        bool slowFriendWitness = false;
        var final = new List<Snapshot>();
        var partial = new List<Snapshot>();
        var groups = new[] { new[] { "teaching_copies", "family_loan" }, new[] { "crossing_read", "crossing_delayed" }, new[] { "late_lovers", "late_friends", "late_open" }, new[] { "future_lovers", "future_friends", "future_open" } }.Select(g => g.Select(x => "gesmerha." + x).ToArray()).ToArray();
        var bound = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).Distinct().ToArray();
        foreach (bool trickster in new[] { false, true })
        foreach (bool truth in new[] { false, true })
        foreach (bool chiefRemains in new[] { false, true })
        foreach (bool reunion in new[] { false, true })
        {
            if (chiefRemains && reunion) continue; // Native KTC chooses Marhevok, not Gesmerha, in this history.
            var chain = earlyIds.Select(Find).Concat(reunion ? new[] { oldReunion } : Array.Empty<Scene>()).Concat(late).ToArray();
            var initial = new Snapshot { Chapter = 3, Hour = 1000, Area = late[0].Areas.Single() };
            initial.AvailableContacts.Add(actor);
            initial.Flags.UnionWith(new[] { "gesmerha.wintersun_resolved", "seelah.committed", "jerribeth.committed" });
            if (trickster) initial.Flags.Add("trickster");
            initial.Flags.Add(truth ? "gesmerha.truth" : "gesmerha.illusions");
            if (chiefRemains) initial.Flags.Add("gesmerha.marhevok_rules");
            var states = new List<Snapshot> { initial };
            for (int i = 0; i < chain.Length; i++)
            {
                var scene = chain[i]; var next = new List<Snapshot>();
                foreach (var input in states)
                {
                    var ready = Program.Copy(input); ready.Hour += scene.DelayHours + 24;
                    if (scene == oldReunion)
                    {
                        ready.Chapter = 5; ready.Area = capital;
                        ready.Flags.UnionWith(new[] { "gesmerha.capital_guest", "gesmerha.heard_future", truth ? "gesmerha.heard_migration" : "gesmerha.heard_staying" });
                    }
                    if (scene == late[0])
                    {
                        ready.Chapter = 5; ready.Area = late[0].Areas.Single();
                        ready.Flags.Remove("gesmerha.capital_guest");
                        ready.Flags.Add("gesmerha.post_resolution_contact");
                    }
                    check(Rules.Available(story, scene, ready), "Gesmerha earned history cannot enter " + scene.Id);
                    foreach (var result in Program.Walk(scene, ready, (page, state) =>
                    {
                        check(state.Flags.SetEquals(ready.Flags), "Gesmerha interruption records a premature outcome.");
                        if (!late.Contains(scene)) return;
                        reached.Add(scene.Id + "/" + page);
                        if (scene == late[4] && page == "start" && state.Has("gesmerha.evening_as_friends"))
                        {
                            var offered = scene.Nodes[0].Choices.Where(c => Rules.Match(c.Requires, c.Forbids, state)).ToArray();
                            check(offered.Any(c => c.Next == "friends") && offered.All(c => c.Next != "slow" && c.Next != "lover"), "Gesmerha friendship-only evening reopens romance.");
                            if (state.Has("gesmerha.campaign_slow")) slowFriendWitness = true;
                        }
                        check(Rules.ContactAvailable(story, scene, state), "Gesmerha actual local contact rejected.");
                        var wrongChapter = Program.Copy(state); wrongChapter.Chapter = 4;
                        check(!Rules.Available(story, scene, wrongChapter) && !Rules.ContactAvailable(story, scene, wrongChapter), "Gesmerha late local conversation leaks into the Abyss.");
                        foreach (var blocker in new[] { "gesmerha.dead", "inhuman", "demon", "devil", "gesmerha.closed" })
                        {
                            var blocked = Program.Copy(state); blocked.Flags.Add(blocker);
                            check(!Rules.Available(story, scene, blocked), "Gesmerha entry bypasses blocker " + blocker);
                            if (blocker == "gesmerha.dead") check(!Rules.ContactAvailable(story, scene, blocked), "Gesmerha conversation continues after native death.");
                        }
                        var absent = Program.Copy(state); absent.AvailableContacts.Clear();
                        check(!Rules.ContactAvailable(story, scene, absent), "Gesmerha conversation invents a present actor.");
                        var removed = Program.Copy(state); removed.Flags.Remove("gesmerha.post_resolution_contact");
                        check(!Rules.ContactAvailable(story, scene, removed), "Gesmerha continuation outlives native contact owner.");
                        if (page == "chief") check(!chiefRemains, "Gesmerha assumes chief authority under Marhevok.");
                        if (page == "marhevok") check(chiefRemains, "Gesmerha invents retained Marhevok authority.");
                        if (page == "after_court") check(reunion && state.Has("gesmerha.reunion_kept"), "Gesmerha remembers an unplayed private reunion.");
                        if (page == "without_court") check(!state.Has("gesmerha.reunion_kept"), "Gesmerha repeats first private return after actual reunion.");
                        if (scene == late.Last())
                        {
                            if (page == "migration") check(state.Has("gesmerha.heard_migration"), "Gesmerha invents an observed migration report.");
                            if (page == "shelter") check(state.Has("gesmerha.heard_staying") && !state.Has("gesmerha.heard_migration"), "Gesmerha misstates native shelter history.");
                            if (page == "unreported") check(!state.Has("gesmerha.heard_staying") && !state.Has("gesmerha.heard_migration"), "Gesmerha ignores an observed native plan.");
                        }
                    }))
                    {
                        foreach (var flag in bound) check(ready.Has(flag) == result.Has(flag), "Gesmerha writes native state: " + flag);
                        foreach (var flag in ready.Flags) check(result.Has(flag), "Gesmerha erases earlier history: " + flag);
                        check(result.Has("seelah.committed") && result.Has("jerribeth.committed"), "Gesmerha changes other romances.");
                        check(result.AvailableContacts.SetEquals(ready.AvailableContacts), "Gesmerha creates a physical actor.");
                        foreach (var group in groups) check(group.Count(result.Has) <= 1, "Gesmerha incompatible outcomes overlap.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags), "Gesmerha deferral changes progress.");
                            check(result.Times.OrderBy(x => x.Key).SequenceEqual(ready.Times.OrderBy(x => x.Key)), "Gesmerha deferral changes times.");
                            continue;
                        }
                        check(!Rules.Available(story, scene, result), "Gesmerha completed visit repeats.");
                        outputs.UnionWith(result.Flags);
                        if (late.Contains(scene)) partial.Add(Program.Copy(result));
                        if (scene == late.Last()) final.Add(result);
                        if (!result.Has("gesmerha.closed")) next.Add(result);
                    }
                }
                var reads = chain.Skip(i + 1).Concat(endings).SelectMany(s => s.Requires.Concat(s.RequiresAny).Concat(s.Forbids)
                    .Concat(s.Nodes.SelectMany(n => n.Choices.SelectMany(c => c.Requires.Concat(c.Forbids))))).ToHashSet();
                states = next.GroupBy(s => string.Join("|", s.Flags.Where(reads.Contains).OrderBy(f => f))).Select(g => g.First()).ToList();
            }
        }
        // The Trickster catch-up page (a claimed, not kept, Chapter 3) is played by GesmerhaTricksterTests.
        foreach (var scene in late)
        foreach (var page in scene.Nodes.Where(p => !(scene.Id == "gesmerha.the_things_still_here" && p.Id == "catchup")))
            check(reached.Contains(scene.Id + "/" + page.Id), "Gesmerha unplayed page " + scene.Id + "/" + page.Id);
        foreach (var flag in groups.SelectMany(x => x)) check(outputs.Contains(flag), "Gesmerha unearned outcome " + flag);
        check(slowFriendWitness, "Gesmerha slow-to-friend evening was not actually played.");
        IEnumerable<Scene> Ending(Snapshot state) => endings.Where(s => s.Owner == "Epilogue" && Rules.Available(story, s, state));
        foreach (var state in final)
        {
            var result = Ending(state).ToArray();
            var aeon = endings.Where(s => s.Owner == "AeonEpilogue" && Rules.Available(story, s, state)).ToArray();
            check(aeon.Length == 1 && aeon[0].Id == "gesmerha.late_ending_aeon", "Gesmerha late Aeon ending missing or old ending retained.");
            check(result.Length == 1, "Gesmerha earned ending missing or overlapping.");
            var suffix = state.Has("gesmerha.closed") ? "closed" : state.Has("gesmerha.future_lovers") ? "lovers" : state.Has("gesmerha.future_friends") ? "friends" : "open";
            check(result[0].Id == "gesmerha.late_ending_" + suffix, "Gesmerha final ending contradicts chosen relationship.");
            foreach (var (flag, end) in new[] { ("gesmerha.dead", "loss"), ("inhuman", "changed"), ("demon", "demon"), ("devil", "devil"), ("ascended", "ascent"), ("sacrifice", "sacrifice") })
            {
                if (state.Has("gesmerha.closed") && (flag == "ascended" || flag == "sacrifice")) continue;
                var altered = Program.Copy(state); altered.Flags.Add(flag);
                check(Ending(altered).Single().Id == "gesmerha.late_ending_" + end, "Gesmerha special ending is false: " + flag);
                altered.Flags.Add("gesmerha.dead");
                check(Ending(altered).Single().Id == "gesmerha.late_ending_loss", "Gesmerha death loses precedence.");
            }
        }
        foreach (var state in partial.Where(s => !s.Has("gesmerha.closed")))
        {
            check(Ending(state).Count() == 1, "Gesmerha mid-arc living history lacks exactly one ending.");
            var guest = Program.Copy(state); guest.Area = capital;
            guest.Flags.UnionWith(new[] { "gesmerha.capital_guest", "gesmerha.heard_future", "gesmerha.heard_migration" });
            check(!Rules.Available(story, oldReunion, guest), "Gesmerha old first-reunion scene regresses after late return.");
            var dead = Program.Copy(state); dead.Flags.Add("gesmerha.dead");
            check(Ending(dead).Count() == 1, "Gesmerha native death mid-arc lacks an ending.");
        }
        check(late[2].Nodes.Single(n => n.Id == "road").Choices.Any(c => c.Check != null && c.Check.DC == 26 && c.Check.Skill == "SkillLoreNature"), "Gesmerha selected crossing lost its native skill check.");
    }
}
