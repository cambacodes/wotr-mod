using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class EmberCampaignTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        string[] ids = { "the_empty_basket", "the_cold_side", "the_missing_covering", "a_question_at_the_yard",
            "what_did_not_mend", "the_person_in_the_title", "the_words_people_keep", "a_letter_with_no_road",
            "an_answer_from_elsewhere", "where_she_is_needed", "the_afternoon_not_promised" };
        Scene Get(string id) => story.Scenes.Single(s => s.Id == "ember." + id);
        var first = Get("something_you_cannot_do"); var late = Get("a_late_afternoon");
        var chain = ids.Select(Get).ToArray();
        var care = new[] { Get("a_place_to_sit"), Get("the_small_choice"), Get("the_visits_she_can_end") };
        var physical = chain.Concat(care).Append(first).Append(late).ToArray();
        var endings = story.Scenes.Where(s => s.Id.StartsWith("ember.ending_", StringComparison.Ordinal)).ToArray();
        var visited = physical.ToDictionary(s => s.Id, _ => new HashSet<string>());
        var native = story.Etudes.Keys.Concat(story.CompletedQuests.Keys).Concat(story.CompletedEtudes.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();
        check(!physical.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).Any(native.Contains),
            "Ember friendship writes native history.");
        check(physical.All(s => s.ContactUnit == "2779754eecffd044fbd4842dba55312c" && !Rules.IsRemote(s)),
            "New Ember physical visits bypass actual companion contact.");
        check(care.All(s => s.AnswerLists.SequenceEqual(new[] { "fd8276a6302f4d44583eba3f0b9663bf" })
            && s.Requires.Contains("ember.native_q3_complete") && s.Requires.Contains("ember.native_devastated")),
            "Support bypasses the native devastated conclusion or uses its wrong answer list.");
        check(care.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).All(c => c.Revive == null && c.Check == null
            && !c.Set.Contains("ember.trusted_friend") && !c.Set.Contains("ember.campaign_developed")),
            "Care grants a cure, roll-based affection, or ordinary friendship completion.");
        var roll = physical.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Single(c => c.Check != null);
        check(roll.Check!.Skill == "SkillPerception" && roll.Check.DC == 24 && roll.Check.CommanderOnly && roll.Set.Length == 0,
            "Door inspection changes its actual check or records an unplayed result.");

        var normalHistories = new List<Snapshot>();
        Snapshot? playedIntervention = null;
        foreach (bool oldOpening in new[] { true, false })
        foreach (bool trickster in new[] { false, true })
        foreach (string outcome in new[] { "unresolved", "good", "law" })
        {
            var seed = new Snapshot { Chapter = oldOpening ? 3 : 5, Area = first.Areas.Single(), Hour = 1000 };
            seed.Flags.UnionWith(new[] { "ember.present", "konomi.committed", "seelah.committed" });
            seed.AvailableContacts.Add(first.ContactUnit!);
            if (trickster) seed.Flags.Add("trickster");
            if (outcome != "unresolved") seed.Flags.Add("ember.native_q1_complete");
            if (!oldOpening && outcome != "unresolved")
                seed.Flags.UnionWith(new[] { "ember.native_q2_complete", "ember.native_q3_complete", "ember.native_" + outcome });
            List<Snapshot> states;
            if (oldOpening)
            {
                // Released final-afternoon fixture; the original eight-scene suite owns all earlier combinations.
                var predecessor = Get("second_ending");
                seed.Flags.UnionWith(predecessor.Requires);
                seed.Flags.UnionWith(new[] { "ember.started", "ember.player_fox", "ember.revision_laughter" });
                check(Program.CurrentAvailable(story, predecessor, seed), "Released Ember predecessor fixture is unavailable.");
                states = Program.Walk(predecessor, seed).Where(s => s.Has("ember.puppet_afternoons_kept")).ToList();
                foreach (var state in states) check(!Program.CurrentAvailable(story, late, state), "Late entry duplicates a completed opening.");
            }
            else
            {
                check(!Program.CurrentAvailable(story, first, seed), "Fresh chapter five pretends the earlier puppet afternoons happened.");
                states = new List<Snapshot> { seed };
            }
            var ordered = new[] { oldOpening ? first : late }.Concat(chain).ToArray();
            for (int index = 0; index < ordered.Length; index++)
            {
                var scene = ordered[index]; var next = new List<Snapshot>();
                foreach (var state in states)
                {
                    var ready = Program.Copy(state);
                    if (scene.Id == "ember.where_she_is_needed")
                    {
                        ready.Chapter = 5;
                        if (outcome != "unresolved") ready.Flags.UnionWith(new[] { "ember.native_q2_complete", "ember.native_q3_complete", "ember.native_" + outcome });
                    }
                    ready.Hour += scene.DelayHours;
                    check(Program.CurrentAvailable(story, scene, ready), "Played Ember path stranded at " + scene.Id);
                    CheckGuards(scene, ready);
                    foreach (var result in Program.Walk(scene, ready, (page, partial) =>
                    {
                        visited[scene.Id].Add(page);
                        check(partial.Flags.SetEquals(ready.Flags), "New Ember outcome precedes terminal acknowledgement: " + scene.Id + "/" + page);
                        var lost = Program.Copy(partial); lost.AvailableContacts.Clear();
                        check(!Rules.ContactAvailable(story, scene, lost), "Interrupted friendship ignores contact loss.");
                        lost.AvailableContacts.Add(scene.ContactUnit!);
                        check(Program.CurrentAvailable(story, scene, lost), "Interrupted friendship cannot restart after contact returns.");
                        if (scene.Id == "ember.the_words_people_keep" && page == "captivity") check(partial.Has("ember.native_q1_complete"), "Captivity invented.");
                        if (scene.Id == "ember.the_words_people_keep" && page == "nocticula") check(partial.Has("ember.native_q2_complete"), "Nocticula meeting invented.");
                        if (scene.Id == "ember.a_letter_with_no_road" && (page == "road" || page == "road_checked")) check(trickster, "Non-Trickster gets impossible road.");
                        if (scene.Id == "ember.an_answer_from_elsewhere" && page == "reply") check(partial.Has("ember.letter_trickster"), "Unlocated correspondent sends a reply.");
                        if (scene.Id == "ember.an_answer_from_elsewhere" && page == "another_road") check(partial.Has("trickster"), "Former Trickster performs new magic.");
                        if (scene.Id == "ember.where_she_is_needed" && (page == "good" || page == "law"))
                            check(partial.Has("ember.native_q3_complete") && partial.Has("ember.native_" + page), "Native ending is inferred before actual outcome.");
                    }))
                    {
                        check(ready.Flags.IsSubsetOf(result.Flags) && result.Has("konomi.committed") && result.Has("seelah.committed"), "Friendship rewrites history or other relationships.");
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags) && result.Times.Count == ready.Times.Count, "Postponement fabricates progress.");
                            continue;
                        }
                        check(!Program.CurrentAvailable(story, scene, result), "Completed friendship visit repeats.");
                        if (!oldOpening) check(!result.Has("ember.puppet_afternoons_kept") && !result.Has("ember.second_ending"), "Late entry forges the original eight scenes.");
                        check(!result.Has("ember.trusted_friend") || scene.Id == "ember.the_afternoon_not_promised", "Friendship awarded before its played final visit.");
                        if (scene.Id == "ember.a_letter_with_no_road" && result.Has("ember.letter_trickster"))
                            playedIntervention ??= Program.Copy(result);
                        next.Add(result);
                    }
                }
                // Keep complete histories, merging only ones indistinguishable to all remaining authored guards.
                states = DistinctForFuture(next, ordered.Skip(index + 1).Concat(endings));
                check(states.Count > 0, "All Ember paths lost after " + scene.Id);
            }
            foreach (var state in states)
            {
                check(state.Has("ember.trusted_friend") && state.Has("ember.campaign_developed"), "Played ordinary friendship lacks final acknowledgement.");
                check(endings.Count(s => s.Owner == "Epilogue" && Program.CurrentAvailable(story, s, state)) == 1, "Ordinary friendship has conflicting/missing endings.");
                foreach (string exceptional in new[] { "ember_dead", "ember_gone", "ember.absent", "sacrifice", "ascended" })
                {
                    var changed = Program.Copy(state); changed.Flags.Add(exceptional);
                    check(endings.Count(s => s.Owner == "Epilogue" && Program.CurrentAvailable(story, s, changed)) == 1, "Exceptional friendship has conflicting/missing endings: " + exceptional);
                }
                // Native finale receipts drive the shared return reader; never
                // insert commander_back or a friendship conclusion directly.
                var returned = Program.Copy(state);
                returned.Flags.UnionWith(new[] { "trickster", "trickster.ever", "sacrifice", "ending.trickster" });
                Program.CurrentAvailable(story, endings[0], returned);
                check(returned.Has("trickster.commander_back"), "Ember return fixture has no native producer.");
                check(endings.Count(s => s.Owner == "Epilogue" && Program.CurrentAvailable(story, s, returned)) == 1,
                    "Returned ordinary friendship has conflicting/missing endings.");
                normalHistories.Add(state);
            }
        }

        foreach (bool earlierFriendship in new[] { false, true })
        {
            var ready = earlierFriendship ? Program.Copy(normalHistories[0]) : new Snapshot { Chapter = 5, Area = first.Areas.Single(), Hour = 1000 };
            ready.Flags.Remove("ember.native_good"); ready.Flags.Remove("ember.native_law");
            ready.Flags.UnionWith(new[] { "ember.present", "ember.native_devastated", "ember.native_q3_complete" });
            ready.AvailableContacts.Add(first.ContactUnit!);
            if (earlierFriendship)
                foreach (var scene in chain)
                {
                    var witness = Program.Copy(ready);
                    witness.Flags.Remove(scene.Id); witness.Flags.Remove("ember.native_devastated");
                    witness.Hour += scene.DelayHours;
                    check(Program.CurrentAvailable(story, scene, witness), "Devastation guard witness is already unavailable for another reason.");
                    witness.Flags.Add("ember.native_devastated");
                    check(!Program.CurrentAvailable(story, scene, witness) && !Rules.ContactAvailable(story, scene, witness),
                        "Ordinary confident scene continues after native devastation.");
                }
            var unfinishedNative = Program.Copy(ready); unfinishedNative.Flags.Remove("ember.native_q3_complete");
            check(!Program.CurrentAvailable(story, care[0], unfinishedNative), "Support replaces the native quest conclusion.");
            var states = new List<Snapshot> { ready };
            foreach (var scene in care)
            {
                var next = new List<Snapshot>();
                foreach (var prior in states)
                {
                    var current = Program.Copy(prior); current.Hour += scene.DelayHours;
                    check(Program.CurrentAvailable(story, scene, current), "Actual devastated history cannot reach care visit.");
                    CheckGuards(scene, current);
                    foreach (var result in Program.Walk(scene, current, (page, partial) =>
                    {
                        visited[scene.Id].Add(page);
                        check(partial.Flags.SetEquals(current.Flags), "Care records permission before Ember gives it.");
                    }))
                    {
                        check(current.Flags.IsSubsetOf(result.Flags) && result.Has("ember.native_devastated"), "Care erases devastation or existing friendship.");
                        check(result.Has("ember.trusted_friend") == current.Has("ember.trusted_friend"), "Care awards a cure-shaped trust change.");
                        next.Add(result);
                    }
                }
                states = DistinctForFuture(next, care.Concat(endings));
            }
            foreach (var state in states)
                check(state.Has("ember.care_continues") && endings.Count(s => s.Owner == "Epilogue" && Program.CurrentAvailable(story, s, state)) == 1,
                    "Completed care lacks its own ending or overlaps ordinary friendship.");
        }
        foreach (var scene in physical)
            check(visited[scene.Id].SetEquals(scene.Nodes.Select(n => n.Id)), "Unreached new Ember page: " + scene.Id);

        // A real played letter intervention is remembered after changing path; only new magic is unavailable.
        check(playedIntervention != null, "The main walk never played the real Trickster intervention.");
        var changedPath = Program.Copy(playedIntervention!);
        changedPath.Flags.Remove("trickster"); changedPath.Flags.Add("legend");
        changedPath.Chapter = 5;
        var replyScene = Get("an_answer_from_elsewhere");
        changedPath.Hour += replyScene.DelayHours;
        check(Program.CurrentAvailable(story, replyScene, changedPath), "Former Trickster loses the earned correspondent.");
        var replyPages = new HashSet<string>();
        var changedResults = Program.Walk(replyScene, changedPath, (page, _) => replyPages.Add(page));
        check(replyPages.Contains("reply") && replyPages.Contains("paper_road") && !replyPages.Contains("another_road"),
            "Former Trickster cannot keep correspondence without performing new magic.");
        check(changedResults.All(s => s.Has("ember.anet_answered") && s.Has("ember.letter_trickster") && !s.Has("trickster")),
            "A path change erases history or restores old powers.");

        void CheckGuards(Scene scene, Snapshot current)
        {
            foreach (string flag in new[] { "ember.closed", "ember_dead", "ember_gone", "ember.absent" })
            {
                var blocked = Program.Copy(current); blocked.Flags.Add(flag);
                check(!Program.CurrentAvailable(story, scene, blocked), "Ember ignores closure/absence: " + flag);
                if (flag != "ember.closed") check(!Rules.ContactAvailable(story, scene, blocked), "Ember conversation survives native absence.");
            }
            var away = Program.Copy(current); away.Area = "elsewhere";
            check(!Program.CurrentAvailable(story, scene, away), "Ember capital visit starts elsewhere.");
            away.Area = current.Area; away.Chapter = 4;
            check(!Program.CurrentAvailable(story, scene, away), "Capital visit assumes an Abyss actor.");
            foreach (string requirement in scene.Requires.Where(k => !story.Derived.ContainsKey(k)))
            {
                var missing = Program.Copy(current); missing.Flags.Remove(requirement);
                check(!Program.CurrentAvailable(story, scene, missing), "Ember ignores actual prerequisite: " + requirement);
            }
        }
    }

    private static List<Snapshot> DistinctForFuture(IEnumerable<Snapshot> states, IEnumerable<Scene> remaining)
    {
        var flags = remaining.SelectMany(s => s.Requires.Concat(s.Forbids).Concat(s.RequiresAny)
            .Concat(s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids))))
            .Concat(new[] { "ember.trusted_friend", "ember.campaign_developed", "ember.puppet_afternoons_kept", "ember.second_ending" }).ToHashSet();
        return states.GroupBy(s => string.Join("|", s.Flags.Where(flags.Contains).OrderBy(f => f, StringComparer.Ordinal)))
            .Select(g => g.First()).ToList();
    }
}
