using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class NocticulaContinuationTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var scenes = story.Scenes.Where(s => s.Relationship == "nocticula").ToArray();
        var visits = scenes.Where(s => !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var endings = scenes.Except(visits).ToArray();
        check(visits.Length == 16 && endings.Length == 8, "Nocticula campaign or ending coverage changed; review the test scope.");
        var reached = visits.ToDictionary(s => s.Id, _ => new HashSet<string>());
        var native = story.Etudes.Keys.Concat(story.SeenCues.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.CompletedEtudes.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();
        var finalChoices = new[] { "noct.chosen_company", "noct.chosen_alliance", "noct.chosen_limit" };
        var finalWitnesses = new Dictionary<string, Snapshot>();

        IEnumerable<string> Reads(Scene scene) => scene.Requires.Concat(scene.Forbids).Concat(scene.RequiresAny)
            .Concat(scene.RequiresAnyGroups.SelectMany(g => g))
            .Concat(scene.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids)));

        // Parent acceptance is an explicit starting fixture. This does not play its acquisition in Unity.
        string[] optionalHistory = { "trickster", "noct.parent_laulieh", "noct.parent_laulieh_departure",
            "noct.parent_ambition_heard", "noct.socoth_plan_exposed" };
        for (int mask = 0; mask < 1 << optionalHistory.Length; mask++)
        {
            var initial = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            initial.Flags.UnionWith(new[] { "noct.parent_active", "noct.parent_agreement_seen", "noct.gift",
                "seelah.committed", "arueshalae.committed", "minachiv.complete" });
            for (int bit = 0; bit < optionalHistory.Length; bit++)
                if ((mask & (1 << bit)) != 0) initial.Flags.Add(optionalHistory[bit]);
            var nativeBefore = initial.Flags.Where(native.Contains).ToHashSet();
            var states = new List<Snapshot> { initial };
            for (int index = 0; index < visits.Length; index++)
            {
                var scene = visits[index];
                var next = new List<Snapshot>();
                foreach (var before in states)
                {
                    var ready = Program.Copy(before);
                    if (index > 0 && scene.DelayHours > 0)
                    {
                        check(!Rules.Available(story, scene, ready), "Nocticula skips the interval: " + scene.Id);
                        ready.Hour += scene.DelayHours;
                    }
                    check(Rules.Available(story, scene, ready), "Played Nocticula history cannot enter " + scene.Id);
                    foreach (var result in Program.Walk(scene, ready, (node, partial) =>
                    {
                        reached[scene.Id].Add(node);
                        check(Rules.ContactAvailable(story, scene, partial), "Nocticula loses earned dream contact within " + scene.Id);
                        foreach (string evidence in new[] { "noct.parent_active", "noct.parent_agreement_seen", "noct.gift" })
                        {
                            var lost = Program.Copy(partial); lost.Flags.Remove(evidence);
                            check(!Rules.ContactAvailable(story, scene, lost), "Nocticula ignores lost parent evidence: " + evidence);
                        }
                        var dead = Program.Copy(partial); dead.Flags.Add("noct.dead");
                        check(!Rules.ContactAvailable(story, scene, dead), "Nocticula death leaves dream contact available.");
                    }))
                    {
                        check(result.Flags.Where(native.Contains).ToHashSet().SetEquals(nativeBefore), "Nocticula changes native or parent history.");
                        check(initial.Flags.IsSubsetOf(result.Flags), "Nocticula deletes an existing relationship or history.");
                        check(result.AvailableContacts.Count == 0, "A dream manufactures a physical contact.");
                        if (!result.Has(scene.Id)) continue;
                        check(!Rules.Available(story, scene, result), "Completed Nocticula visit repeats.");
                        next.Add(result);
                    }
                }
                // Merge only states indistinguishable to every later predicate, retaining a real played witness.
                var future = scenes.SkipWhile(s => s.Id != scene.Id).Skip(1).SelectMany(Reads)
                    .Concat(finalChoices).Concat(native).Concat(initial.Flags).ToHashSet();
                states = next.GroupBy(s => string.Join("|", s.Flags.Where(future.Contains).OrderBy(f => f)))
                    .Select(g => g.First()).ToList();
                check(states.Count > 0, "No continuing Nocticula outcome after " + scene.Id);
            }
            foreach (var state in states)
            {
                check(state.Has("noct.complete") && finalChoices.Count(state.Has) == 1, "Nocticula lacks one earned final decision.");
                string choice = finalChoices.Single(state.Has);
                if (!finalWitnesses.ContainsKey(choice)) finalWitnesses.Add(choice, state);
            }
        }
        check(finalWitnesses.Count == 3, "Not every Nocticula final relationship decision is playable.");
        foreach (var scene in visits)
        {
            check(reached[scene.Id].SetEquals(scene.Nodes.Select(n => n.Id)), "Unreached Nocticula branch: " + scene.Id);
            check(Rules.IsRemote(scene) && scene.ContactUnit == null && scene.AdditionalContactUnits.Length == 0,
                "Dream continuation claims an unverified physical actor.");
            check(scene.Nodes.SelectMany(n => n.Choices).All(c => c.Revive == null && c.Set.All(f => !native.Contains(f))),
                "Nocticula continuation rewrites parent state or revives an actor.");
            var ready = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            ready.Flags.UnionWith(scene.Requires);
            check(Rules.Available(story, scene, ready), "Nocticula baseline eligibility is inconsistent.");
            foreach (string prerequisite in scene.Requires)
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(prerequisite);
                check(!Rules.Available(story, scene, missing), "Nocticula bypasses " + prerequisite);
            }
            foreach (string blocker in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(blocker);
                check(!Rules.Available(story, scene, blocked), "Nocticula ignores " + blocker);
            }
            var elsewhere = Program.Copy(ready); elsewhere.Area = "";
            check(!Rules.Available(story, scene, elsewhere), "Nocticula ignores the authored dream setting.");
        }
        foreach (var witness in finalWitnesses.Values)
        for (int mask = 0; mask < 16; mask++)
        {
            var ending = Program.Copy(witness);
            string[] outcomes = { "noct.dead", "inhuman", "ascended", "sacrifice" };
            for (int bit = 0; bit < outcomes.Length; bit++)
                if ((mask & (1 << bit)) != 0) ending.Flags.Add(outcomes[bit]);
            var available = endings.Where(s => s.Owner == "Epilogue" && Rules.Available(story, s, ending)).ToArray();
            check(available.Length == 1, "Nocticula recollections overlap or disappear for outcome mask " + mask);
            string expected = ending.Has("noct.dead") ? "death" : ending.Has("inhuman") ? "changed"
                : ending.Has("ascended") ? "ascent" : ending.Has("sacrifice") ? "sacrifice"
                : ending.Has("noct.chosen_company") ? "company" : ending.Has("noct.chosen_alliance") ? "alliance" : "limit";
            check(available[0].Id == "noct.ending_" + expected, "Nocticula recollection contradicts outcome precedence.");
            check(endings.Count(s => s.Owner == "AeonEpilogue" && Rules.Available(story, s, ending)) == 1,
                "Nocticula lacks a distinct altered-history recollection.");
            ending.Flags.Remove("noct.complete");
            check(!endings.Any(s => Rules.Available(story, s, ending)), "An unfinished undertaking grants a completed recollection.");
        }
    }
}
