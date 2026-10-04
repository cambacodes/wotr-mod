using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class Program
{
    private static int checks;
    private static Story story = null!;

    private static void Check(bool result, string message)
    {
        checks++;
        if (!result) throw new Exception(message);
    }

    internal static Snapshot Copy(Snapshot original) => new Snapshot
    {
        Chapter = original.Chapter, Hour = original.Hour, Area = original.Area,
        Flags = new HashSet<string>(original.Flags), Times = new Dictionary<string, int>(original.Times),
        AvailableContacts = new HashSet<string>(original.AvailableContacts)
    };

    // NM1 (storylines/nm1_fold.py): the per-letter view of a story whose later rest deliveries were folded into earlier ones.
    // Each folded host loses its copied guest nodes (`<key>.arrives` and `<key>.*`) and its hooked terminal choices end
    // again, so a suite written per letter keeps judging each letter; the folded deliveries are judged by Nm1BudgetTests.
    internal static Story Unfolded(Story original)
    {
        var options = new JsonSerializerOptions { IncludeFields = true };
        var story = JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(original, options), options)!;
        foreach (var scene in story.Scenes)
        {
            var keys = scene.Nodes.Where(n => n.Id.EndsWith(".arrives", StringComparison.Ordinal)).Select(n => n.Id.Substring(0, n.Id.Length - ".arrives".Length)).ToArray();
            if (keys.Length == 0) continue;
            scene.Nodes.RemoveAll(n => keys.Any(k => n.Id.StartsWith(k + ".", StringComparison.Ordinal)));
            foreach (var choice in scene.Nodes.SelectMany(n => n.Choices).Where(c => c.Next != null && c.Next.EndsWith(".arrives", StringComparison.Ordinal)))
                choice.Next = null;
        }
        return story;
    }

    // A scene's minimal prerequisites: its Requires plus the first flag of each RequiresAnyGroups group (the original path).
    internal static IEnumerable<string> Prerequisites(Scene scene) => scene.Requires.Concat(scene.RequiresAnyGroups.Select(group => group[0]));

    internal static List<Snapshot> Walk(Scene scene, Snapshot initial, Action<string, Snapshot>? visit = null)
        => WalkPaths(scene, initial, visit, null).Select(r => r.state).ToList();

    // The outcomes of the paths that actually take choice [index] of node `nodeId` (not merely end with its flags).
    internal static List<Snapshot> WalkVia(Scene scene, Snapshot initial, string nodeId, int index)
        => WalkPaths(scene, initial, null, (nodeId, index)).Where(r => r.via).Select(r => r.state).ToList();

    private static List<(Snapshot state, bool via)> WalkPaths(Scene scene, Snapshot initial, Action<string, Snapshot>? visit, (string node, int index)? via)
    {
        var outcomes = new List<(Snapshot, bool)>();
        void Visit(string id, Snapshot state, HashSet<string> path, bool passed)
        {
            Check(path.Add(id), "Cycle without a terminal answer: " + scene.Id + "/" + id);
            var node = scene.Nodes.Single(n => n.Id == id);
            visit?.Invoke(id, state);
            var choices = node.Choices.Where(c => Rules.Match(c.Requires, c.Forbids, state)).ToList();
            Check(choices.Count > 0, "Page has no selectable answers: " + scene.Id + "/" + id);
            foreach (var choice in choices)
            {
                bool took = passed || (via != null && via.Value.node == id && node.Choices.IndexOf(choice) == via.Value.index);
                var next = Copy(state);
                foreach (var effect in choice.Set)
                    if (next.Flags.Add(effect)) next.Times[effect] = next.Hour;
                // E11: a removed item is no longer observed in the inventory (Main.BuildState reads InventoryItems live).
                if (choice.RemoveItem != null && story != null)
                    foreach (var held in story.InventoryItems.Concat(story.PartyItems).Where(e => e.Value == choice.RemoveItem).Select(e => e.Key))
                        next.Flags.Remove(held);
                if (choice.Next != null || choice.Check != null)
                    foreach (var target in Rules.NextNodes(choice)) Visit(target, Copy(next), new HashSet<string>(path), took);
                else
                {
                    if (!choice.Abort) { next.Flags.Add(scene.Id); next.Times[scene.Id] = next.Hour; }
                    outcomes.Add((next, took));
                }
            }
        }
        Visit(scene.Nodes[0].Id, initial, new HashSet<string>(), false);
        return outcomes;
    }

    private static Snapshot Complete(Scene scene, Snapshot state)
    {
        var outcomes = Walk(scene, state).Where(s => !s.Has("closed") && s.Has(scene.Id) && LegacyTirabadeOutcome(s)).OrderByDescending(s => s.Flags.Count).ToList();
        Check(outcomes.Count > 0, "No continuing path in " + scene.Id);
        return outcomes[0];
    }

    // These witnesses deliberately play the retained affair campaign; separate suites play the added alternatives.
    internal static bool LegacyTirabadeOutcome(Snapshot state) => !new[] {
        "anevia.closed", "irabeth.closed", "anevia.courtship_requested", "irabeth.courtship_requested", "tirabade.group_closed"
    }.Any(state.Has);

    private static Snapshot Campaign(int startChapter, bool playAbyss)
    {
        var state = new Snapshot { Hour = 1000 };
        for (int chapter = startChapter; chapter <= 5; chapter++)
        {
            state.Chapter = chapter;
            state.Area = chapter == 4 ? "" : "2570015799edf594daf2f076f2f975d8";
            state.AvailableContacts.Clear();
            if (chapter != 4) state.AvailableContacts.UnionWith(new[] { "b5e867e13503c6f41bb1316705efb4a2", "280d4712dceb37f4a88e98f1f4c6e64f" });
            state.Flags.Remove("chapter_one"); state.Flags.Remove("chapter_later");
            state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
            if (chapter == 4 && !playAbyss) continue;
            for (int attempt = 0; attempt < 50; attempt++)
            {
                state.Hour += 72;
                var scene = story.Scenes.FirstOrDefault(s => s.Relationship == "tirabade" && !s.Id.StartsWith("three_", StringComparison.Ordinal)
                    && !s.Optional && !s.Owner.EndsWith("Epilogue") && Rules.Available(story, s, state));
                if (scene == null) break;
                state = Complete(scene, state);
            }
        }
        if (story.Scenes.Any(s => s.Id == "three_choose_days"))
        {
            // The original-only campaign now chooses its shorter farewell explicitly.
            // TirabadeProgressionTests plays the developed continuation separately.
            var decision = story.Scenes.Single(s => s.Id == "three_choose_days");
            state.Area = decision.Areas.Single();
            state.Hour += 72;
            Check(Rules.Available(story, decision, state), "Original campaign cannot choose a shorter farewell");
            state = Walk(decision, state).Single(s => s.Has("three_progression.short_chosen"));
            var watch = story.Scenes.Single(s => s.Id == "last_watch");
            Check(Rules.Available(story, watch, state), "Explicit shorter farewell remains blocked");
            state = Complete(watch, state);
        }
        Check(state.Has("committed"), "Campaign cannot reach commitment from act " + startChapter);
        Check(state.Has("shared_evening"), "Shared night unreachable");
        Check(state.Has("last_words"), "Final farewell unreachable");
        Check(state.Has("abyss_letter") == (startChapter <= 3 && playAbyss), "Abyss letter availability is wrong for a chapter " + startChapter + " install");
        return state;
    }

    private static IEnumerable<Scene> Endings(Snapshot state) => story.Scenes.Where(s => s.Relationship == "tirabade" && s.Owner == "Epilogue" && Rules.Available(story, s, state));

    private static void TargonaContinuation()
    {
        var meeting = story.Scenes.SingleOrDefault(s => s.Id == "targona.the_open_threshold");
        var followup = story.Scenes.SingleOrDefault(s => s.Id == "targona.the_key_remains_hers");
        if (meeting == null || followup == null) return;

        var tricksterHistories = new[] { "targona.extra_ending", "targona.ordinary_ending" };
        foreach (var history in tricksterHistories)
        {
            var state = new Snapshot { Chapter = meeting.MinChapter, Hour = 10000, Area = meeting.Areas.FirstOrDefault() ?? "", Flags = new HashSet<string>(meeting.Requires) };
            state.Flags.UnionWith(new[] { "trickster", "targona.ran_trickster", history });
            if (meeting.RequiresAny.Length > 0) state.Flags.Add(meeting.RequiresAny[0]);
            Check(Rules.Available(story, meeting, state), "Targona Trickster history cannot open the meeting: " + history);
            var outcomes = Walk(meeting, state);
            Check(outcomes.Any(s => s.Has("targona.visit_correspondence")), "Targona Trickster history has no correspondence fallback: " + history);
            Check(outcomes.Any(s => s.Has("targona.visit_tender")), "Targona Trickster history has no tender visit ending: " + history);
            Check(outcomes.Any(s => s.Has("targona.visit_desire")), "Targona Trickster history has no desire visit ending: " + history);
            Check(outcomes.Any(s => s.Has("targona.visit_pause")), "Targona Trickster history has no pause or departure ending: " + history);
        }

        foreach (var history in new[] { "targona.extra_ending", "targona.ordinary_ending" })
        {
            var state = new Snapshot { Chapter = meeting.MinChapter, Hour = 10000, Area = meeting.Areas.FirstOrDefault() ?? "", Flags = new HashSet<string>(meeting.Requires) };
            state.Flags.UnionWith(new[] { "targona.ran_none", history });
            if (meeting.RequiresAny.Length > 0) state.Flags.Add(meeting.RequiresAny[0]);
            Check(Rules.Available(story, meeting, state), "Targona ordinary history cannot open the meeting: " + history);
            var outcomes = Walk(meeting, state);
            Check(outcomes.Any(s => s.Has("targona.visit_correspondence")), "Targona ordinary history has no correspondence fallback: " + history);
        }

        var replies = new[]
        {
            ("targona.visit_desire", "desire"),
            ("targona.visit_tender", "tender"),
            ("targona.visit_pause", "pause"),
            ("targona.visit_correspondence", "correspondence")
        };
        foreach (var reply in replies)
        {
            var state = new Snapshot { Chapter = followup.MinChapter, Hour = 12000, Area = followup.Areas.FirstOrDefault() ?? "", Flags = new HashSet<string>(followup.Requires) };
            state.Flags.Add(reply.Item1);
            if (followup.RequiresAny.Length > 0) state.Flags.Add(followup.RequiresAny[0]);
            Check(Rules.Available(story, followup, state), "Targona follow-up cannot open after its preceding outcome: " + reply.Item1);
            var visited = new HashSet<string>(StringComparer.Ordinal);
            var outcomes = Walk(followup, state, (node, _) => visited.Add(node));
            Check(visited.Contains(reply.Item2), "Targona follow-up cannot reach the matching history page: " + reply.Item1);
            Check(!visited.Any(node => node != "start" && node != reply.Item2), "Targona follow-up exposes another history page: " + reply.Item1);
            Check(outcomes.Count > 0, "Targona follow-up has no terminal response: " + reply.Item1);
        }
    }

    private static void ArankaContinuation()
    {
        var followup = story.Scenes.SingleOrDefault(s => s.Id == "aranka.the_next_verse");
        if (followup == null) return;

        var historyFlags = new[] { "aranka.story_game", "aranka.story_restraint", "aranka.story_left_alone" };
        foreach (var history in historyFlags)
        {
            var state = new Snapshot { Chapter = followup.MinChapter, Hour = 15000, Area = followup.Areas.FirstOrDefault() ?? "", Flags = new HashSet<string>(followup.Requires) };
            state.Flags.Add(history);
            if (followup.RequiresAny.Length > 0) state.Flags.Add(followup.RequiresAny[0]);
            if (followup.ContactUnit != null) state.AvailableContacts.Add(followup.ContactUnit);
            state.AvailableContacts.UnionWith(followup.AdditionalContactUnits);
            Check(Rules.Available(story, followup, state), "Aranka follow-up cannot open after its preceding history: " + history);
            var outcomes = Walk(followup, state);
            Check(outcomes.Any(s => s.Has("aranka.relationship_plan")), "Aranka follow-up history has no concrete-plan branch: " + history);
            Check(outcomes.Any(s => s.Has("aranka.after_story_deferred")), "Aranka follow-up history has no deferral branch: " + history);
        }

        var deferral = story.Scenes.SingleOrDefault(s => s.Id == "aranka.the_deferred_answer");
        if (deferral != null)
        {
            var state = new Snapshot { Chapter = deferral.MinChapter, Hour = 18000, Area = deferral.Areas.FirstOrDefault() ?? "", Flags = new HashSet<string>(deferral.Requires) };
            if (deferral.RequiresAny.Length > 0) state.Flags.Add(deferral.RequiresAny[0]);
            if (deferral.ContactUnit != null) state.AvailableContacts.Add(deferral.ContactUnit);
            state.AvailableContacts.UnionWith(deferral.AdditionalContactUnits);
            Check(Rules.Available(story, deferral, state), "Aranka deferred answer cannot open after its stated retry interval.");
            var outcomes = Walk(deferral, state);
            Check(outcomes.Any(s => s.Has("aranka.relationship_plan")), "Aranka deferred answer has no accepted-plan branch.");
        }
    }

    private static void Main(string[] args)
    {
        story = JsonSerializer.Deserialize<Story>(File.ReadAllText(args.Last()), new JsonSerializerOptions { IncludeFields = true })!;
        Rules.Validate(story);
        NurahContactEvidenceTests.Run(Check);
        if (args.Contains("--iomedae"))
        {
            // One route's suite alone (fast iteration; the full run still calls it below).
            IomedaeTricksterTests.Run(story, Check);
            Console.WriteLine($"PASS: {checks} Iomedae assertions.");
            return;
        }
        if (args.Contains("--nidalynn"))
        {
            // One route's suite alone (polish: her checks run even when an earlier suite fails; the full run still calls it below).
            NidalynnTricksterTests.Run(story, Check);
            Console.WriteLine($"PASS: {checks} Nidalynn assertions.");
            return;
        }
        if (args.Contains("--prerequisite-groups"))
        {
            PrerequisiteGroupsTests.Run(Check);
            Console.WriteLine($"PASS: {checks} prerequisite group assertions.");
            return;
        }
        if (args.Contains("--bindings"))
        {
            var bindings = story.Scenes.SelectMany(s => Rules.EntryTargets(s).Select(guid => new { Guid = guid, ExpectedType = "BlueprintAnswersList", Source = s.Id }))
                .Concat(story.Scenes.Where(s => s.NativeReturnCue != null).Select(s => new { Guid = s.NativeReturnCue!, ExpectedType = "BlueprintCue", Source = s.Id }))
                // E14h "scene:<id>" anchors name another RRT page (Rules.Validate checks them); only native GUIDs are bindings.
                .Concat(story.Scenes.Where(s => s.EpilogueAfter != null && !s.EpilogueAfter.StartsWith("scene:", StringComparison.Ordinal))
                    .Select(s => new { Guid = s.EpilogueAfter!, ExpectedType = "BlueprintCueBase", Source = s.Id + "/epilogue_after" }))
                .Concat(story.Scenes.SelectMany(s => s.Nodes.SelectMany(n => n.Choices).Where(c => c.NativeNext != null)
                    .Select(c => new { Guid = c.NativeNext!, ExpectedType = "BlueprintCue", Source = s.Id + "/native_next" })))
                .Concat(story.Etudes.Select(e => new { Guid = e.Value, ExpectedType = "BlueprintEtude", Source = e.Key }))
                .Concat(story.CompletedQuests.Select(e => new { Guid = e.Value, ExpectedType = "BlueprintQuest", Source = e.Key }))
                .Concat(story.SeenCues.SelectMany(e => e.Value.Select(guid => new { Guid = guid, ExpectedType = "BlueprintCue", Source = e.Key })))
                .Concat(story.SelectedAnswers.Select(e => new { Guid = e.Value, ExpectedType = "BlueprintAnswer", Source = e.Key }))
                .Concat(story.StartedDialogs.Select(e => new { Guid = e.Value, ExpectedType = "BlueprintDialog", Source = e.Key }))
                .Concat(story.CompletedEtudes.Select(e => new { Guid = e.Value, ExpectedType = "BlueprintEtude", Source = e.Key }))
                .Concat(story.UnlockableFlags.Select(e => new { Guid = e.Value, ExpectedType = "BlueprintUnlockableFlag", Source = e.Key }))
                .Concat(story.QuestObjectives.Select(e => new { Guid = e.Value[0], ExpectedType = "BlueprintQuestObjective", Source = e.Key }))
                .Concat(story.InventoryItems.Select(e => new { Guid = e.Value, ExpectedType = "BlueprintItem*", Source = e.Key }))
                .Concat(story.PartyItems.Select(e => new { Guid = e.Value, ExpectedType = "BlueprintItem*", Source = e.Key }))
                .Concat(story.StartedQuests.Select(e => new { Guid = e.Value, ExpectedType = "BlueprintQuest", Source = e.Key }))
                .Concat(story.MainCharacterFacts.Select(e => new { Guid = e.Value, ExpectedType = "BlueprintFeature", Source = e.Key }))
                .Concat(story.RemovableItems.Select(guid => new { Guid = guid, ExpectedType = "BlueprintItem*", Source = "RemovableItems" }))
                .Concat(story.Presences.SelectMany(p => new[] { new { Guid = p.Value.Unit, ExpectedType = "BlueprintUnit", Source = p.Key },
                    new { Guid = p.Value.Area, ExpectedType = "BlueprintArea*", Source = p.Key } }
                    .Concat(p.Value.At?.NearUnit == null ? new[] { new { Guid = p.Value.Unit, ExpectedType = "BlueprintUnit", Source = p.Key } }
                        : new[] { new { Guid = p.Value.At.NearUnit, ExpectedType = "BlueprintUnit", Source = p.Key + ".At" } })
                    .Concat(p.Value.AnswerLists.Select(g => new { Guid = g, ExpectedType = "BlueprintAnswersList", Source = p.Key }))))
                .Concat(story.Revivals.Select(e => new { Guid = e.Value.Unit, ExpectedType = "BlueprintUnit", Source = "revive." + e.Key }))
                .Concat(story.Scenes.Where(s => s.ContactUnit != null).SelectMany(s => new[] { s.ContactUnit! }.Concat(s.AdditionalContactUnits).Select(guid => new { Guid = guid, ExpectedType = "BlueprintUnit", Source = s.Id })))
                .Concat(story.Scenes.SelectMany(s => s.Areas.Select(guid => new { Guid = guid, ExpectedType = "BlueprintArea", Source = s.Id })))
                .Concat(story.ParentEpilogueEdits.Select(e => new { Guid = e.Key, ExpectedType = "BlueprintCue", Source = "parent-ending-edit" }))
                .Concat(story.ParentEpilogueLossRules.SelectMany(r => r.SuppressPages.Select(guid => new { Guid = guid, ExpectedType = "BlueprintBookPage", Source = r.Id })))
                .Concat(story.ParentEpilogueLossRules.SelectMany(r => r.SuppressCues.Concat(r.SurvivorAlternates.Keys).Select(guid => new { Guid = guid, ExpectedType = "BlueprintCue", Source = r.Id })));
            Console.WriteLine(JsonSerializer.Serialize(bindings));
            return;
        }
        if (args.Contains("--tirabade-combined"))
        {
            var baseline = JsonSerializer.Deserialize<Story>(File.ReadAllText(args[args.Length - 2]), new JsonSerializerOptions { IncludeFields = true })!;
            AneviaIndependentTests.Run(story, Check);
            IrabethIndependentTests.Run(story, Check);
            TirabadeIndependentBridgeTests.Run(story, baseline, Check);
            TirabadeCombinedHistoryTests.Run(story, Check);
            Console.WriteLine($"PASS: {checks} combined individual, bridge and played-history assertions. Live delivery remains unverified.");
            return;
        }
        if (args.Contains("--tirabade-bridge"))
        {
            var baseline = JsonSerializer.Deserialize<Story>(File.ReadAllText(args[args.Length - 2]), new JsonSerializerOptions { IncludeFields = true })!;
            TirabadeIndependentBridgeTests.Run(story, baseline, Check);
            Console.WriteLine($"PASS: {checks} focused bridge assertions. Irabeth contract declarations are fixtures, not a played route or release approval.");
            return;
        }
        FairRestTests.Run(Check);
        PostBagTests.Run(Check);
        MailbagTests.Run(Check);
        BookTests.Run(story, Check);
        HouseholdTests.Run(story, Check);
        ArueshalaeBranchTests.Run(story, Check);
        PrerequisiteGroupsTests.Run(Check);
        TargonaContinuation();
        ArankaContinuation();
        foreach (var recovery in story.Scenes.Where(s => s.Recovery != null))
        {
            var revival = story.Revivals[recovery.Recovery!];
            var relationship = story.Relationships[recovery.Relationship];
            var state = new Snapshot { Chapter = recovery.MinChapter, Hour = 10000, Area = recovery.Areas.FirstOrDefault() ?? "" };
            state.Flags.UnionWith(recovery.Requires);
            Check(!Rules.Available(story, recovery, state), "Recovery offered without a recoverable native entity");
            state.Flags.Add("revive." + recovery.Recovery + ".available");
            Check(Rules.Available(story, recovery, state), "Recoverable death cannot reach its recovery scene");
            foreach (string blocker in relationship.UnavailableFlags.Where(f => f != revival.DeathFlag)
                .Concat(recovery.Recovery == "konomi" ? Array.Empty<string>() : new[] { relationship.ClosedFlag }))
            {
                var blocked = Copy(state);
                blocked.Flags.Add(blocker);
                Check(!Rules.Available(story, recovery, blocked), "Recovery bypasses unrelated blocker: " + blocker);
            }
            foreach (var ordinary in story.Scenes.Where(s => s.Relationship == recovery.Relationship && s.Recovery == null && !s.Owner.EndsWith("Epilogue")))
            {
                // G6: a scene that Requires the relationship's declared override of this death (a Trickster return that
                // lifts it, e.g. a Seelah raised far from her body), or an ER-2 device answering the death itself, is not an
                // ordinary conversation. A device answers the death when it Requires it, or when its declared Trickster state
                // detects it (Camellia's killed state co-holds her retained-death etude; the spec lists both in its detect).
                if (relationship.UnavailableOverrides.TryGetValue(revival.DeathFlag, out var lift) && ordinary.Requires.Contains(lift)
                    || ordinary.TricksterDevice && ordinary.Requires.Contains(revival.DeathFlag)
                    || ordinary.TricksterDevice && ordinary.TricksterState != null
                       && relationship.TricksterAccess.TryGetValue(ordinary.TricksterState, out var access)
                       && access.Detect.Contains(revival.DeathFlag)) continue;
                var dead = new Snapshot { Chapter = ordinary.MinChapter, Hour = 10000, Area = ordinary.Areas.FirstOrDefault() ?? "" };
                dead.Flags.UnionWith(ordinary.Requires);
                dead.Flags.Add(revival.DeathFlag);
                Check(!Rules.Available(story, ordinary, dead), "Ordinary conversation offered while dead: " + ordinary.Id);
            }
        }
        var known = new HashSet<string>(story.Scenes.Select(s => s.Id)
            .Concat(story.Relationships.Values.SelectMany(r => new[] { r.StartedFlag, r.ClosedFlag, r.CommittedFlag }))
            .Concat(story.Scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set))
            .Concat(story.Etudes.Keys).Concat(story.CompletedQuests.Keys).Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).Concat(story.CompletedEtudes.Keys).Concat(Rules.ReaderKeys(story)).Concat(story.Latches.Keys).Concat(story.Derived.Keys).Concat(story.Counts.Keys)
            // E12b: the runtime observation an anchored presence exposes for its letter twin (as Rules.Validate derives it).
            .Concat(story.Presences.Where(p => p.Value?.At != null).Select(p => Rules.PresenceFailedFlag(p.Key))).Concat(new[] { "started", "closed", "committed", "chapter_one", "chapter_later", "loss", "ascended", "inhuman", "konomi.missed_contact_available", "konomi.missed_contact_invalidated", "konomi.retained_dead", "konomi.retained_hostile", "konomi.return_contact_available", "konomi.return_correspondence_available", "nurah.correspondence_available", "nurah.meeting_arrived" }));
        foreach (var scene in story.Scenes)
        {
            foreach (var flag in scene.Requires.Concat(scene.RequiresAny).Concat(scene.RequiresAnyGroups.SelectMany(group => group)).Concat(scene.Forbids).Concat(scene.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids))))
                Check(known.Contains(flag) || flag == "irabeth.return_correspondence_available" || flag == "irabeth.return_meeting_arrived",
                    "Unknown condition " + flag + " in " + scene.Id);
            foreach (var node in scene.Nodes)
                Check(node.Text.Count(c => c == '\u2014') == 0, "Em dash in " + scene.Id + "/" + node.Id);
        }
        if (args.Contains("--tirabade-progression") || story.Scenes.Any(s => s.Id == "three_kept_days"))
            TirabadeProgressionTests.Run(story, Check);
        var normal = Campaign(1, true);
        Campaign(1, false);
        Campaign(2, true);
        Campaign(3, true);
        Campaign(4, true);
        Campaign(5, false);
        bool hasTirabadeProgression = story.Scenes.Any(s => s.Id == "three_kept_days");
        Check(Endings(normal).Single().Id == (hasTirabadeProgression ? "ending_promised" : "ending_together"), "Wrong normal ending");
        var partings = Walk(story.Scenes.Single(s => s.Id == "parting"), normal);
        Check(partings.Any(s => s.Has("closed")) && partings.Any(s => !s.Has("closed")), "Parting cannot be confirmed or canceled");
        foreach (var ending in new[] { ("loss", "ending_loss"), ("ascended", "ending_ascend"), ("inhuman", "ending_monster"), ("closed", "ending_apart") })
        {
            var state = Copy(normal);
            state.Flags.Add(ending.Item1);
            if (ending.Item1 == "loss") state.Flags.Add("irabeth_dead");
            if (ending.Item1 == "ascended") state.Flags.Add("ascend_alone");
            if (ending.Item1 == "inhuman") state.Flags.Add("true_lich");
            string expected = hasTirabadeProgression && ending.Item1 == "ascended" ? "ending_ascend_promised" : ending.Item2;
            Check(Endings(state).Single().Id == expected, "Conflicting or absent ending for " + ending.Item1);
        }
        foreach (var blocker in new[] { "closed", "irabeth_dead", "anevia_dead", "irabeth_gone", "anevia_gone", "swarm", "true_lich" })
        {
            var state = new Snapshot { Chapter = 5, Hour = 10000 };
            state.Flags.Add(blocker);
            Check(!story.Scenes.Any(s => s.Relationship == "tirabade" && !s.Owner.EndsWith("Epilogue") && Rules.Available(story, s, state)), "Original relationship starts after " + blocker);
        }
        var waiting = new Snapshot { Chapter = 3, Hour = 100 };
        waiting.Flags.Add("a_cup"); waiting.Times["a_cup"] = 100;
        var errand = story.Scenes.Single(s => s.Id == "a_errand");
        Check(!Rules.Available(story, errand, waiting), "Delay bypassed");
        waiting.Hour = 112;
        Check(Rules.Available(story, errand, waiting), "Delay never expires");
        waiting.Flags.Add("a_errand");
        Check(!Rules.Available(story, errand, waiting), "Completed scene repeats");
        var reunited = Copy(normal); reunited.Flags.Remove("return"); reunited.Flags.Add("irabeth_away");
        Check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "return"), reunited), "Absent Irabeth appears in Drezen");
        reunited.Flags.Remove("irabeth_away");
        Check(Rules.Available(story, story.Scenes.Single(s => s.Id == "return"), reunited), "Returned Irabeth remains blocked");
        // State does not contain gender, game romance counts, or ToyBox jealousy toggles.
        foreach (var path in new[] { "angel", "azata", "aeon", "demon", "devil", "dragon", "legend", "trickster", "lich" })
        {
            var state = Copy(normal); state.Flags.Add(path); state.Flags.Remove("power");
            Check(Complete(story.Scenes.Single(s => s.Id == "power"), state).Has("power_terms"), "Path cannot negotiate boundaries: " + path);
        }
        var json = JsonSerializer.Serialize(normal, new JsonSerializerOptions { IncludeFields = true });
        var reload = JsonSerializer.Deserialize<Snapshot>(json, new JsonSerializerOptions { IncludeFields = true })!;
        Check(normal.Flags.SetEquals(reload.Flags) && normal.Times.OrderBy(x => x.Key).SequenceEqual(reload.Times.OrderBy(x => x.Key)), "Snapshot round trip lost progress");
        ExpansionTests.Run(Check);
        SkillCheckTests.Run(Check);
        ForbidOverrideTests.Run(Check);
        TricksterLatchTests.Run(Check);
        ChapterZeroTests.Run(Check);
        UnavailableOverrideTests.Run(Check);
        NativeForbidOverrideTests.Run(Check);
        DerivedFlagTests.Run(Check);
        ChoiceExtensionTests.Run(Check);
        ReactionTests.Run(Check);
        TricksterAccessTests.Run(Check);
        NativeReaderTests.Run(Check);
        EpilogueAfterTests.Run(Check);
        NativeCostTests.Run(Check);
        EntryEffectTests.Run(Check);
        PresenceTests.Run(Check);
        ContactWindowTests.Run(Check);
        NativeEpilogueTests.Run(Check);
        ReturnToListTests.Run(Check);
        ParagraphTests.Run(Check);
        NativeEpilogueEditTests.Run(Check);
        ContactDisambiguationTests.Run(Check);
        if (story.NativeEpilogueEdits.ContainsKey("164c14743ee768f409a04f93a040e678")) NativeDialogEditTests.Run(story, Check);
        TricksterOnlyNativeTests.Run(story, Check);
        if (story.NativeEpilogueEdits.ContainsKey("4bb3706172f1ed54ca11db96254c4638")) WenduagNativeAscentTests.Run(story, Check);
        SpeakerTests.Run(Check);
        ContinueBeforeTests.Run(Check);
        CountTests.Run(Check);
        SceneAnchorTests.Run(Check);
        PresenceAnchorTests.Run(Check);
        PresenceHubTests.Run(Check);
        // __E14_RULES__
        StartedDialogTests.Run(Check);
        ContactContinuationTests.Run(Check);
        PairedContactTests.Run(Check);
        TerendelevDeliveryTests.Run(Check);
        RecoveryTests.Run(Check);
        RetainedRecoveryRulesTests.Run(Check);
        // These are draft scene checks. Full new-route campaigns need their own
        // ending, transformation and introducer scenarios before release.
        // These continuations have actual predecessor walkthroughs below; a snapshot
        // containing only direct prerequisites cannot represent their earlier choices.
        var playedContinuations = new HashSet<string> {
            // Q6 r4: Targona's killed-state scenes, retired by gating (ruling #2); no longer devices, never openable.
            "targona.trickster.dead.late_light", "targona.trickster.dead.late_crypt", "targona.trickster.dead.one_soul", "targona.trickster.dead.long_sleep",
            "arsinoe_your_hours", "arsinoe_borrowed_court", "arsinoe_price_of_an_evening",
            "arsinoe_courtyard_company", "arsinoe_another_hour", "arsinoe_the_unprofitable_hour",
            "soana.one_account", "soana.watch_line", "soana.price_of_warning",
            "soana.ordinary_feast", "soana.name_between", "soana.lower_bend",
            "kiana.borrowed_name", "kiana.yard_evening", "kiana.unborrowed_evening",
            "targona.unasked_question", "targona.second_margin", "targona.the_folded_room",
            "targona.an_unpromised_future", "targona.the_unscheduled_door", "targona.what_she_keeps",
            "gesmerha.unbought_work", "gesmerha.along_the_grain", "gesmerha.whose_mark",
            "gesmerha.the_first_game", "gesmerha.the_unclaimed_hour", "gesmerha.against_the_current",
            "konomi.a_useful_supper", "konomi.the_upper_passage", "konomi.two_bad_prices",
            "konomi.the_trial_day", "konomi.a_name_beside_hers", "konomi.the_evening_she_kept",
            "vellexia.unfinished_likeness", "vellexia.second_painter", "vellexia.price_of_novelty",
            "vellexia.two_observers", "vellexia.unadvertised_hour", "vellexia.a_question_kept",
            "aivu.a_city_with_wings", "aivu.the_roof_below", "aivu.a_way_for_feet", "aivu.someone_elses_turn",
            "konomi.private_absence", "konomi.private_absence_catchup",
            "soana.the_thing_in_the_sack", "soana.the_dry_offering", "soana.the_inherited_debt",
            "soana.a_voice_in_the_dark", "soana.what_followed_home", "soana.a_promise_still_spoken",
            "soana.the_unwelcome_path", "soana.after_the_last_visitor",
            "soana.when_the_road_returns", "soana.a_track_with_two_ends", "soana.what_the_hollow_costs",
            "soana.where_the_steps_end", "soana.the_days_she_counted", "soana.before_the_far_road",
            "konomi.private_return_terms", "konomi.private_kept_hours", "konomi.private_last_visit",
            "konomi.ending_distance_lived", "konomi.ending_distance_open_lived", "konomi.a_turn_for_herself",
            "aranka.the_wrong_refrain", "aranka.where_the_breath_goes", "aranka.the_name_missing",
            "aranka.an_evening_uncommanded", "aranka.the_song_afterwards", "aranka.no_encore_needed",
            "konomi.the_names_admitted", "konomi.the_answer_on_record"
        };
        if (story.Scenes.Any(s => s.Id == "anevia.the_last_ordinary_thing"))
        {
            AneviaIndependentTests.Run(story, Check);
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "anevia").Select(s => s.Id));
        }
        if (story.Scenes.Any(s => s.Id == "irabeth.the_evening_she_chose"))
        {
            IrabethIndependentTests.Run(story, Check);
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "irabeth" && s.AfterDeparture == null).Select(s => s.Id));
        }
        if (story.Scenes.Any(s => s.AfterDeparture == "irabeth"))
        {
            IrabethDepartureVisitTests.Run(story, Check);
            IrabethDepartureCampaignTests.Run(story, Check);
            playedContinuations.UnionWith(story.Scenes.Where(s => s.AfterDeparture == "irabeth").Select(s => s.Id));
        }
        if (story.Scenes.Any(s => s.Id == "tirabade.negotiated_table")
            && story.Scenes.Any(s => s.Id == "irabeth.the_evening_she_chose"))
            TirabadeCombinedHistoryTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "arsinoe_after_rain"))
        {
            ArsinoeCampaignTests.Run(story, Check);
            ArsinoeAssembledTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "arsinoe.trickster.cauldron.lease")) ArsinoeTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "irabeth.trickster.dead.setup")) IrabethTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "anevia.trickster.gone.setup")) AneviaTricksterTests.Run(story, Check);
            if (story.NativeEpilogueEdits.ContainsKey("3a3e561c6b05a284d93eb3bff7b712a6")) TirabadeNativeSlideTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "jerribeth.trickster.dead.tenant")) JerribethTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "konomi.trickster.dismissed.late")) KonomiTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "nocticula.trickster.defeated.shadow")) NocticulaTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "vellexia.trickster.mirrored.speaks")) VellexiaTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "nurah.trickster.prison.pardon")) NurahTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "kiana.trickster.possessed.fake_gem"))
            {
                KianaTricksterTests.Run(story, Check);
                playedContinuations.UnionWith(story.Scenes.Where(s => s.Id.StartsWith("kiana.trickster.", StringComparison.Ordinal)
                    || s.Id == "kiana.betrothal").Select(s => s.Id));
            }
            if (story.Scenes.Any(s => s.Id == "minagho_chivarro.trickster.reunion.wardrobe")) MinaghoChivarroTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "soana.trickster.killed.knot")) SoanaTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "aranka.trickster.verse.kings_tavern")) ArankaTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "gesmerha.trickster.dead.unfinished_work")) GesmerhaTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "seelah.trickster.dead.pickpocket")) SeelahTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "seelah.early.pack")) PacingPP1Tests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "nocticula.ch4.hoard")) PacingPP4Tests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "dorgelinda.trickster.audit.open")) DorgelindaTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "targona.trickster.dead.setup")) TargonaTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "hepzamirah.trickster.ghost.body")) HepzamirahTricksterTests.Run(story, Check);
            // 18-ETUDE-BINDING-AUDIT: each fixed native binding holds where its scenes are delivered.
            if (story.Scenes.Any(s => s.Id == "terendelev.trickster.late.the_wound_calls")) EtudeBindingTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "camellia.trickster.killed.performance")) CamelliaTricksterTests.Run(story, Check);
            if (story.NativeEpilogueEdits.ContainsKey("4ed8e9723359441dae10ad3068d3f2c7")) CamelliaNativeSlideTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "eritrice.trickster.council.motion")) EritriceTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "areelu.trickster.wager.struck")) AreeluTricksterTests.Run(story, Check);
            if (story.NativeEpilogueEdits.ContainsKey("825786e8c5db4511ae30950bb286f0e9")) AreeluAfterlogueTests.Run(story, Check);
            // Sol quality pass: Areelu's retired scenes (gated off with Forbids trickster.ever; ids kept for saves).
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "areelu" && s.Forbids.Contains("trickster.ever")).Select(s => s.Id));
            if (story.Scenes.Any(s => s.Id == "chadali.trickster.council.coin")) ChadaliTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "arueshalae.trickster.dead.starving")) ArueshalaeTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "devarra.trickster.dead.woken")) DevarraTricksterTests.Run(story, Check);
            // Option A (devarra-device-options.md): the moult device is retired (gated off with Forbids trickster.ever; ids kept for saves).
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "devarra" && s.Forbids.Contains("trickster.ever")).Select(s => s.Id));
            if (story.Scenes.Any(s => s.Id == "delamere.trickster.crypt.stag")) DelamereTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "kaylessa.trickster.dead.borrow")) KaylessaTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "mielarah.trickster.tavern.arithmetic")) MielarahTricksterTests.Run(story, Check);
            // Sol quality pass: Mielarah's retired scenes (gated off with Forbids trickster.ever; ids kept for saves).
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "mielarah" && s.Forbids.Contains("trickster.ever")).Select(s => s.Id));
            if (story.Scenes.Any(s => s.Id == "nidalynn.trickster.eggs.lamp_black")) NidalynnTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "shamira.trickster.killed.voice")) ShamiraTricksterTests.Run(story, Check);
            // PP9: the early threads T2 (Hepzamirah <- Voetiel) and T3 (Shamira <- Telmer), 15b-EARLY-THREADS.md.
            if (story.Scenes.Any(s => s.Id == "hepzamirah.early.moon_message")) EarlyThreadsTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "longcon.tell_them")) LongConTests.Run(story, Check);
            // PP2: Camellia, Kaylessa and Arueshalae early beats, their readers, and the two near-miss fixes.
            if (story.Scenes.Any(s => s.Id == "camellia.early.blood")) PacingPP2Tests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "jannah.trickster.cage.terms")) JannahTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "aranka.early.duet")) PacingPP3Tests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "nenio.trickster.taken.riddle")) NenioTricksterTests.Run(story, Check);
            // Sol quality pass: Nenio's retired scenes (gated off with Forbids trickster.ever; ids kept for saves).
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "nenio" && s.Forbids.Contains("trickster.ever")).Select(s => s.Id));
            if (story.Scenes.Any(s => s.Id == "herrax.trickster.madam.schedule")) HerraxTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "horzalah.trickster.mercy.gift")) HorzalahTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "elyanka.trickster.door.hearse")) ElyankaTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "melazmera.trickster.ch4.salt")) MelazmeraTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "wenduag.trickster.killed.stage")) WenduagTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "iomedae.trickster.dream.banner")) IomedaeTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "terendelev.trickster.bones.restitution")) TerendelevTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "eliandra.trickster.ch5.last_rite")) EliandraTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "galfrey.trickster.iz.offer")) GalfreyTricksterTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "yaniel.trickster.fane.swap")) YanielTricksterTests.Run(story, Check);
            if (story.PartyItems.ContainsKey("yaniel.radiance_party.plus2")) YanielRadianceTests.Run(story, Check);
            if (story.Derived.ContainsKey("chivarro.dead_confirmed")) ChivarroDeathTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "trickster.lastcall.threshold")) LastCallTests.Run(story, Check);
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "arsinoe").Select(s => s.Id));
        }
        if (story.Scenes.Any(s => s.Id == "gesmerha.a_story_from_elsewhere"))
        {
            GesmerhaCampaignTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "gesmerha.the_things_still_here"))
                GesmerhaLateCampaignTests.Run(story, Check);
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "gesmerha").Select(s => s.Id));
        }
        if (story.Scenes.Any(s => s.Id == "ember.something_you_cannot_do"))
        {
            EmberCampaignTests.Run(story, Check);
            EmberAssembledTests.Run(story, Check);
            RemoteContinuationTests.Run(story, Check);
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "ember").Select(s => s.Id));
        }
        if (story.Scenes.Any(s => s.Id == "aivu.a_garden_that_can_go"))
        {
            AivuCampaignTests.Run(story, Check);
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "aivu").Select(s => s.Id));
        }
        if (story.Scenes.Any(s => s.Id == "vellexia.the_unused_reply"))
        {
            VellexiaCampaignTests.Run(story, Check);
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "vellexia").Select(s => s.Id));
        }
        if (story.Relationships.ContainsKey("minagho_chivarro"))
        {
            MinaghoChivarroContinuationTests.Run(story, Check);
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "minagho_chivarro"
                && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).Select(s => s.Id));
        }
        if (story.Relationships.ContainsKey("nocticula"))
        {
            NocticulaContinuationTests.Run(story, Check);
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "nocticula").Select(s => s.Id));
        }
        if (story.Scenes.Any(s => s.Id == "noct.acq.her_hand"))
        {
            NocticulaAcquisitionTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "noct.acq.borrowed_signature"))
                NocticulaConcessionTests.Run(story, Check);
            NocticulaHarborJoinTests.Run(story, Check);
            NocticulaAcquiredHarborTests.Run(story, Check);
            if (story.Scenes.Any(s => s.Id == "noct.acq.epilogue.correspondence")) Nm1BudgetTests.Run(story, Check);
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Id.StartsWith("noct.join.", StringComparison.Ordinal)).Select(s => s.Id));
            playedContinuations.UnionWith(story.Scenes.Where(s => s.Relationship == "nocticula.acquisition"
                && s.Id != "noct.acq.after_the_council").Select(s => s.Id));
        }
        foreach (var scene in story.Scenes.Where(s => s.Relationship != "tirabade"))
        {
            if (playedContinuations.Contains(scene.Id)) continue;
            var state = new Snapshot { Chapter = scene.MinChapter, Hour = 10000, Area = scene.Areas.FirstOrDefault() ?? "", Flags = new HashSet<string>(scene.Requires) };
            if (scene.Recovery != null) state.Flags.Add("revive." + scene.Recovery + ".available");
            if (scene.ContactUnit != null) state.AvailableContacts.Add(scene.ContactUnit);
            state.AvailableContacts.UnionWith(scene.AdditionalContactUnits);
            if (scene.RequiresAny.Length > 0) state.Flags.Add(scene.RequiresAny[0]);
            foreach (var group in scene.RequiresAnyGroups) state.Flags.Add(group[0]);
            if (scene.Relationship == "soana") state.Flags.Add("soana.fox_waited");
            if (scene.Id.StartsWith("jerribeth.counterfeit_", StringComparison.Ordinal))
                state.Flags.UnionWith(new[] { "jerribeth.counter_cache_intact", "jerribeth.counter_clerk_witness", "jerribeth.counter_return_agreement", "jerribeth.counter_public_account" });
            if (scene.Id == "kiana.rehearsal") state.Flags.Add("kiana.moon");
            if (scene.Id == "kiana.seelah") state.Flags.Add("kiana.waited");
            if (scene.Id == "kiana.morning") state.Flags.Add("kiana.separated");
            if (scene.Id == "kiana.a_place_afterward") state.Flags.Add("kiana.separated");
            if (new[] { "kiana.bakery_stairs", "kiana.last_page", "kiana.first_readers", "kiana.ink_after", "kiana.working_room", "kiana.kept_evening" }.Contains(scene.Id))
                state.Flags.UnionWith(new[] { "kiana.separated", "kiana.waited", "kiana.moon", "kiana.follow_audience", "kiana.follow_short_speech", "kiana.follow_guest_role", "kiana.follow_quiet_desk" });
            if (new[] { "kiana.guest_table", "kiana.market_weather", "kiana.lenna_door", "kiana.blue_room" }.Contains(scene.Id))
                state.Flags.UnionWith(new[] { "kiana.separated", "kiana.waited", "kiana.guest_table.listened", "kiana.lenna_door.plain", "kiana.market_weather.public" });
            if (scene.Id == "ember.rain") state.Flags.Add("ember.manyboots");
            if (new[] { "ember.paper_bird", "ember.missing_cloth", "ember.courtyard_play", "ember.after_applause", "ember.second_ending" }.Contains(scene.Id))
                state.Flags.UnionWith(new[] { "ember.manyboots", "ember.player_fox", "ember.stage_road", "ember.play_restitution", "ember.play_company", "ember.revision_laughter" });
            if (scene.Id == "seelah.letter_after") state.Flags.Add("seelah.letter_public");
            if (scene.Id == "seelah.letter_work") state.Flags.UnionWith(new[] { "seelah.letter_public", "seelah.check_person" });
            if (scene.Id == "seelah.borrowed_saw") state.Flags.Add("seelah.frank_terms");
            if (scene.Id == "seelah.platform_finished") state.Flags.Add("seelah.saw_gift");
            if (scene.Id == "seelah.inheritors_corner") state.Flags.Add("seelah.prayer_company");
            if (scene.Id.StartsWith("seelah.late_", StringComparison.Ordinal))
                state.Flags.UnionWith(new[] { "seelah.late_fixed_lessons", "seelah.late_running", "seelah.late_race_lost", "seelah.late_pc_delight" });
            if (scene.Id == "konomi.hearing_after" || scene.Id == "konomi.private_hearing_after") state.Flags.Add("konomi.hearing_buyer_barred");
            // Prerequisite-only fixtures still need real temporal evidence for held contact witnesses.
            var contacts = scene.AdditionalContactUnits.Append(scene.ContactUnit);
            foreach (var window in story.Presences.Values.Where(p => p.Area == state.Area && contacts.Contains(p.Unit))
                .SelectMany(p => p.ContactWindows).Where(w => state.Has(w.Flag)))
                state.Times[window.Flag] = state.Hour - Math.Max(scene.DelayHours, window.MinAgeHours);
            Check(Rules.Available(story, scene, state), "Draft scene prerequisites cannot open " + scene.Id);
            if (scene.Relationship != "nurah" && scene.Id != "targona.the_key_remains_hers" && scene.Id != "aranka.the_next_verse")
                Check(Walk(scene, state).Count > 0, "Draft scene has no terminal choices: " + scene.Id);
        }
        if (story.Scenes.Any(s => s.Id == "seelah.kept")) CheckSeelahOpening();
        if (story.Scenes.Any(s => s.Id == "seelah.door")) CheckSeelahContinuation();
        if (story.Scenes.Any(s => s.Id == "seelah.letter")) CheckSeelahLetters();
        if (story.Scenes.Any(s => s.Id == "seelah.borrowed_saw")) SeelahAftermathTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "seelah.late_course")) SeelahLateCampaignTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "jerribeth.offered_signature")) JerribethConsequencesTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "three_yard")) TirabadeCampaignTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "three_stolen_roads")) TirabadeReckoningTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "three_borrowed_names")) TirabadeAfterRoadsTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.private_history")) KonomiPrivateHearingTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "kiana.guest_table")) KianaConsequencesTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "kiana.invitation")) KianaEntryTests.Run(story, Check);
        if (args.Contains("--kiana-progression") || story.Scenes.Any(s => s.Id == "kiana.a_place_afterward")) KianaProgressionTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "jerribeth.parting"))
        {
            var delivery = new Story {
                Relationships = story.Relationships,
                Scenes = story.Scenes.Where(s => s.Id == "jerribeth.parting" || s.Id == "jerribeth.offered_signature").ToList()
            };
            var visit = delivery.Scenes.Single(s => s.Id == "jerribeth.offered_signature");
            var ready = new Snapshot { Chapter = 5, Area = visit.Areas[0], Hour = 1000 };   // JER-08: offered_signature is a Chapter 4-5 letter
            ready.Flags.UnionWith(visit.Requires);
            ready.Flags.Add("jerribeth.lovers");
            Check(Rules.NextRemote(delivery, ready)?.Id == visit.Id, "Jerribeth repeatable breakup starves the next eligible continuation.");
        }
        if (story.Scenes.Any(s => s.Id == "seelah.future_followup")) SeelahProgressionTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "kiana.bakery_stairs")) KianaFollowthroughTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "ember.paper_bird")) EmberAfternoonsTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "soana.threshold")) SoanaOpeningTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "arsinoe_city_on_paper")) ArsinoeOpeningTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.political_account")) KonomiPoliticalTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "jerribeth.fate_envelope")) JerribethFateTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "arsinoe_your_hours")) ArsinoeContinuationTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "soana.one_account")) SoanaContinuationTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "kiana.borrowed_name")) KianaFurtherTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "targona.unasked_question")) TargonaOpeningTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "gesmerha.unbought_work")) GesmerhaOpeningTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "kiana.former_grief")) KianaReconciliationTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.a_useful_supper")) KonomiOrdinaryExpansionTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "vellexia.unfinished_likeness")) VellexiaOpeningTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "aivu.a_city_with_wings")) AivuOpeningTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.private_absence")) KonomiPrivateAbsenceTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.private_absence_catchup" && s.Nodes.Any(n => n.Id == "absence_career_future")))
            KonomiAbsenceChronologyTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "soana.the_thing_in_the_sack")) SoanaLaterProgressionTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "soana.when_the_road_returns")) SoanaLateCampaignTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "return" && s.Nodes.Any(n => n.Id == "before_the_abyss")))
            TirabadeChronologyTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.private_return_terms")) KonomiPrivateConsequenceTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.the_unintroduced_letter")) KonomiMissedContactTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.retained_inquiry")) KonomiRetainedReturnTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.return_letter")) KonomiReturnInvitationTests.Run(story, Check);
        if (story.ParentEpilogueEdits.Count > 0 || story.ParentEpilogueLossRules.Count > 0) ParentEndingRulesTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.a_turn_for_herself")) KonomiEarlyReciprocityTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "aranka.the_wrong_refrain")) ArankaContinuationTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.margin" && s.ContactUnit != null)) KonomiContactTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.the_names_admitted")) KonomiPoliticalConsequenceTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "jerribeth.counterfeit_guest")) JerribethCounterofferTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "jerribeth.settlement_visit")) JerribethProgressionTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Nodes.Any(n => n.Id == "wonder_reply"))) KonomiLettersTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "three_locks")) CheckTirabadeLocks();
        if (args.Contains("--installed-legacy"))
            Check(story.Scenes.Count == 34 && story.Relationships.Count == 1,
                "Installed-legacy mode is only for the original standalone 34-scene story.");
        CheckTirabadeQuarrel(expanded: !args.Contains("--installed-legacy"));
        // Earned presence (rubric Binding context (3)): after every special mode, so --bindings stdout stays pure JSON.
        EarnedPresenceTests.Run(story, Check);
        // Engine-q2: the current-path reader (trickster.now), fixture and generated story.
        CurrentPathTests.Run(Check);
        CurrentPathTests.RunStory(story, Check);
        // Engine-q2 item 2: a returned, committed partner's Failed objective is restored.
        ObjectiveRestoreTests.Run(Check);
        ObjectiveRestoreTests.RunStory(story, Check);
        // Engine-q2 item 4: Konomi's death latch.
        KonomiDeathLatchTests.Run(story, Check);
        // Engine-q2 item 5: Galfrey's native Queen slides for a returned, re-crowned Queen.
        if (story.Relationships.ContainsKey("galfrey")) GalfreyQueenSlideTests.Run(story, Check);
        KonomiTests.Run(story, Check);
        if (story.Scenes.Any(s => s.Id == "konomi.hearing")) CheckKonomiHearing();
        if (story.Scenes.Any(s => s.Id == "konomi.fate_post")) CheckKonomiPost();
        if (story.Scenes.Any(s => s.Id == "konomi.private_departure")) CheckKonomiPrivateContinuation();
        if (story.Scenes.Any(s => s.Id == "konomi.capital_letter")) CheckKonomiDistance();
        if (story.Scenes.Any(s => s.Id == "konomi.private_future_choice")) CheckKonomiFuture();
        if (story.Scenes.Any(s => s.Id == "konomi.private_history")) CheckKonomiHistory();
        if (story.Scenes.Any(s => s.Id == "jerribeth.invitation")) CheckJerribethCampaign();
        if (story.Scenes.Any(s => s.Id == "kiana.invitation")) CheckKianaCampaign();
        if (story.Scenes.Any(s => s.Id == "ember.drawing")) CheckEmberOpening();
        Console.WriteLine($"PASS: {checks} assertions covering the original campaign, independent-relationship rules, authored expansion campaign scenarios and {story.Scenes.Count(s => s.Relationship != "tirabade")} draft expansion scenes. Unity execution and real save persistence are not covered.");
    }

    private static void CheckKonomiHistory()
    {
        var meeting = story.Scenes.Single(s => s.Id == "konomi.private_meeting");
        var historyScene = story.Scenes.Single(s => s.Id == "konomi.private_history");
        var carriers = story.Scenes.Single(s => s.Id == "konomi.carriers");
        foreach (var chapter in new[] { 3, 5 })
        foreach (var history in new[] { "new", "petition", "public", "discreet", "denial", "apologized", "heard_whole", "heard_covered", "heard_repaired" })
        {
            bool dispute = history != "new";
            bool leak = dispute && history != "petition";
            bool answered = history == "apologized" || history.StartsWith("heard_");
            bool almostDenied = history == "denial" || history == "apologized" || history == "heard_repaired";
            bool heard = history.StartsWith("heard_");
            var initial = new Snapshot { Chapter = chapter, Hour = 1000, Area = meeting.Areas.Single() };
            initial.Flags.UnionWith(meeting.Requires);
            initial.Flags.UnionWith(new[] { "legend", "seelah.committed" });
            if (dispute) initial.Flags.UnionWith(new[] { "konomi.evening", "konomi.lovers", "konomi.disagreement", "konomi.aid_priority" });
            if (leak) initial.Flags.UnionWith(new[] { "konomi.leak", history == "public" ? "konomi.public" : "konomi.discreet" });
            if (almostDenied) initial.Flags.Add("konomi.almost_denied");
            if (answered) initial.Flags.UnionWith(new[] { "konomi.scandal_answered", "konomi.petition_resolved", "konomi.traced_leak" });
            if (history == "apologized") initial.Flags.Add("konomi.apologized");
            if (history == "heard_repaired") initial.Flags.UnionWith(new[] { "konomi.apologized", "konomi.hearing_trust_repaired" });
            if (heard) initial.Flags.UnionWith(new[] { "konomi.hearing_finished", history == "heard_whole" ? "konomi.hearing_buyer_barred" : "konomi.hearing_buyer_unbarred" });
            if (initial.Has("konomi.apologized"))
            {
                var trustChoices = historyScene.Nodes.Single(n => n.Id == "trust").Choices.Where(c => Rules.Match(c.Requires, c.Forbids, initial)).ToArray();
                Check(trustChoices.Length == 1 && trustChoices[0].Next == (history == "heard_repaired" ? "repaired" : "remember"), "Private history forgets whether trust was already repaired.");
            }
            foreach (var visit in Walk(meeting, initial).Where(s => s.Has(meeting.Id)))
            {
                Check(visit.Has("konomi.private_history_ready") == !dispute, "First meeting skips inherited history or invents it for a new courtship.");
                visit.Hour += 24;
                Check(Rules.Available(story, carriers, visit) == !dispute, "Carrier visit bypasses unresolved earlier history.");
                Check(Rules.Available(story, historyScene, visit) == dispute, "History conversation is missing or demands events that never happened.");
                if (!dispute) continue;
                foreach (var outcome in Walk(historyScene, visit))
                {
                    Check(outcome.Has("konomi.dismissed") && outcome.Has("konomi.office_completed") && !outcome.Has("konomi.present"), "Private history restores native office access.");
                    Check(outcome.Has("seelah.committed") && outcome.Has("konomi.lovers"), "Private history erases a relationship history.");
                    Check(outcome.Has("konomi.hearing_finished") == heard, "Private history invents an association hearing.");
                    foreach (var flag in new[] { "konomi.hearing_buyer_barred", "konomi.hearing_buyer_unbarred", "konomi.public", "konomi.discreet" })
                        Check(outcome.Has(flag) == initial.Has(flag), "Private history rewrites a prior decision: " + flag);
                    if (!outcome.Has(historyScene.Id))
                    {
                        Check(outcome.Flags.SetEquals(visit.Flags) && Rules.Available(story, historyScene, outcome), "Postponed history conversation records false progress.");
                        continue;
                    }
                    Check(outcome.Has("konomi.petition_resolved"), "Private history abandons the provisions report.");
                    Check(outcome.Has("konomi.scandal_answered") == leak, "Private history loses the leak response or invents a leak.");
                    if (history == "public") Check(outcome.Has("konomi.public_cost"), "Public leak loses the courier and dinner cost.");
                    if (leak && history != "public") Check(outcome.Has("konomi.traced_leak"), "Discreet leak loses the identified channel.");
                    if (outcome.Has("konomi.closed"))
                    {
                        Check(history == "denial" && !outcome.Has("konomi.apologized") && !outcome.Has("konomi.private_history_ready"), "Refused apology invents repair or readiness.");
                        var endingState = Copy(outcome); endingState.Chapter = 5;
                        Check(story.Scenes.Single(s => s.Relationship == "konomi" && s.Owner == "Epilogue" && Rules.Available(story, s, endingState)).Id == "konomi.ending_distance_apart", "History breakup restores official correspondence in its ending.");
                        Check(!Rules.Available(story, carriers, outcome), "Refused history repair continues into romance.");
                        continue;
                    }
                    Check(outcome.Has("konomi.private_history_ready"), "Acknowledged history cannot continue.");
                    Check(outcome.Has("konomi.apologized") == almostDenied, "History repair invents or omits the necessary apology.");
                    Check(outcome.Has("konomi.private_hearing_needed") == (leak && !heard), "History carryover loses a pending complaint or invents one.");
                    Check(!Rules.Available(story, carriers, outcome), "Carrier visit skips the delay after history repair.");
                    outcome.Hour += 24;
                    Check(Rules.Available(story, carriers, outcome), "Acknowledged history never reaches the carrier visit.");
                    Check(!Rules.Available(story, historyScene, outcome), "History conversation repeats after acknowledgment.");
                }
            }
        }
        var legacy = new Snapshot { Chapter = 5, Hour = 2000, Area = historyScene.Areas.Single() };
        legacy.Flags.UnionWith(new[] { "konomi.dismissed", "konomi.office_completed", "konomi.private_meeting", "konomi.reconnection_open", "seelah.committed" });
        Check(Rules.Available(story, historyScene, legacy), "Earlier private-meeting snapshot cannot recover the new progression permission.");
        foreach (var recovered in Walk(historyScene, legacy).Where(s => s.Has(historyScene.Id)))
        {
            Check(recovered.Has("konomi.private_history_ready"), "Earlier clean courtship remains blocked at carriers.");
            Check(!recovered.Has("konomi.disagreement") && !recovered.Has("konomi.petition_resolved") && !recovered.Has("konomi.scandal_answered") && !recovered.Has("konomi.apologized"), "Clean history recovery fabricates old events.");
            recovered.Hour += 24;
            Check(Rules.Available(story, carriers, recovered), "Recovered clean history cannot reach carriers.");
        }
        var later = Copy(legacy); later.Flags.UnionWith(new[] { "konomi.disagreement", "konomi.carriers", "konomi.carriers_inspected" });
        Check(!Rules.Available(story, historyScene, later), "Older post-carrier snapshot replays a pre-carrier checkpoint.");
        Check(Rules.Available(story, story.Scenes.Single(s => s.Id == "konomi.before_road"), later), "New checkpoint blocks an already advanced private history.");
        var ready = new Snapshot { Chapter = 5, Hour = 1000, Area = historyScene.Areas.Single() };
        ready.Flags.UnionWith(historyScene.Requires);
        foreach (var group in historyScene.RequiresAnyGroups) ready.Flags.Add(group[0]);
        foreach (var requirement in historyScene.Requires)
        {
            var missing = Copy(ready); missing.Flags.Remove(requirement);
            Check(!Rules.Available(story, historyScene, missing), "History carryover ignores " + requirement);
        }
        foreach (var blocker in historyScene.Forbids.Concat(new[] { "konomi.closed" }))
        {
            var blocked = Copy(ready); blocked.Flags.Add(blocker);
            Check(!Rules.Available(story, historyScene, blocked), "History carryover ignores " + blocker);
        }
        ready.Chapter = 4;
        Check(!Rules.Available(story, historyScene, ready), "History courtyard scene appears in the Abyss.");
    }

    private static void CheckKonomiFuture()
    {
        var scenes = new[] { "lease_offer", "chosen_evening", "private_future_choice" }
            .Select(id => story.Scenes.Single(s => s.Id == "konomi." + id)).ToArray();
        void CheckEnding(Snapshot original)
        {
            foreach (var change in new[] { "none", "inhuman", "ascended", "both" })
            {
                var state = Copy(original); state.Chapter = 5;
                if (change == "inhuman" || change == "both") state.Flags.Add("inhuman");
                if (change == "ascended" || change == "both") state.Flags.Add("ascended");
                var endings = story.Scenes.Where(s => s.Relationship == "konomi" && s.Owner == "Epilogue" && Rules.Available(story, s, state)).ToArray();
                Check(endings.Length == 1, "Private future has absent or conflicting endings: " + change);
                string expected = "distance_apart";
                if (!state.Has("konomi.closed"))
                    expected = state.Has("konomi.committed")
                        ? state.Has("ascended") ? "ascended" : state.Has("inhuman") ? "changed" : "distance"
                        : state.Has("ascended") ? "distance_ascended_open" : state.Has("inhuman") ? "distance_changed_open" : "distance_open";
                Check(endings[0].Id == "konomi.ending_" + expected, "Private future selects the wrong ending: " + expected);
            }
            if (original.Has("konomi.committed") && !original.Has("konomi.closed"))
            {
                var aeon = Copy(original); aeon.Chapter = 5;
                Check(story.Scenes.Count(s => s.Relationship == "konomi" && s.Owner == "AeonEpilogue" && Rules.Available(story, s, aeon)) == 1, "Private commitment loses the existing Aeon ending.");
            }
        }
        foreach (var chapter in new[] { 3, 5 })
        foreach (var history in new[] { "new", "lovers", "committed" })
        {
            var initial = new Snapshot { Chapter = chapter, Hour = 1000, Area = scenes[0].Areas.Single() };
            initial.Flags.UnionWith(scenes[0].Requires);
            foreach (var group in scenes[0].RequiresAnyGroups) initial.Flags.Add(group[0]);
            initial.Flags.UnionWith(new[] { "legend", "konomi.attracted", "konomi.private_departed", "seelah.committed" });
            if (history != "new") initial.Flags.Add("konomi.lovers");
            if (history == "committed") initial.Flags.UnionWith(new[] { "konomi.committed", "konomi.public" });
            var recent = Copy(initial); recent.Times["konomi.reunion_kept"] = 1000;
            recent.Hour = 1047;
            Check(!Rules.Available(story, scenes[0], recent), "Lease offer ignores its reunion delay.");
            recent.Hour++;
            Check(Rules.Available(story, scenes[0], recent), "Lease offer misses its 48-hour boundary.");
            var states = new List<Snapshot> { initial };
            foreach (var scene in scenes)
            {
                var continuing = new List<Snapshot>();
                foreach (var state in states)
                {
                    Check(Rules.Available(story, scene, state) && Rules.EntryTargets(scene).Length == 0, "Private future requires an unavailable actor or lost powers.");
                    if (scene.Id == "konomi.chosen_evening")
                    {
                        Check(scene.Nodes[0].Choices.Single(c => !c.Abort && Rules.Match(c.Requires, c.Forbids, state)).Next == (state.Has("konomi.career_accepts_now") ? "now" : "later"), "Evening forgets the chosen career cost.");
                        Check(scene.Nodes.Single(n => n.Id == "friends").Choices.Single(c => Rules.Match(c.Requires, c.Forbids, state)).Next == (history == "new" ? "first_parting" : "old_parting"), "Declined courtship confuses first romance and an existing relationship.");
                    }
                    if (scene.Id == "konomi.private_future_choice")
                        Check(scene.Nodes[0].Choices.Any(c => c.Next == "open" && Rules.Match(c.Requires, c.Forbids, state)) == !state.Has("konomi.committed"), "Private future silently downgrades an existing commitment.");
                    foreach (var outcome in Walk(scene, state))
                    {
                        Check(outcome.Has("konomi.dismissed") && outcome.Has("konomi.office_completed") && !outcome.Has("konomi.present"), "Career offer restores the native officer role.");
                        Check(outcome.Has("seelah.committed"), "Private future erases another relationship.");
                        if (history == "committed") Check(outcome.Has("konomi.committed"), "Private future erases existing commitment history.");
                        if (!outcome.Has(scene.Id))
                        {
                            Check(outcome.Flags.SetEquals(state.Flags) && Rules.Available(story, scene, outcome), "Postponed private future records false progress.");
                            continue;
                        }
                        Check(!Rules.Available(story, scene, outcome), "Private future scene repeats.");
                        if (outcome.Has("konomi.private_future"))
                        {
                            CheckEnding(outcome);
                            Check(outcome.Has("konomi.closed") == outcome.Has("konomi.private_parted"), "Private parting loses its explicit decision.");
                            foreach (var local in scenes)
                            {
                                var unplayed = Copy(outcome); unplayed.Flags.UnionWith(local.Requires); unplayed.Flags.Remove(local.Id);
                                Check(!Rules.Available(story, local, unplayed), "Finished private visit reopens local scenes.");
                            }
                            if (scene.Id == "konomi.chosen_evening")
                                Check(!outcome.Has("konomi.private_evening_kept") && outcome.Has("konomi.lovers") == (history != "new"), "Declined courtship invents a romantic night.");
                            continue;
                        }
                        if (scene.Id == "konomi.lease_offer")
                            Check(outcome.Has("konomi.career_decided") && outcome.Has("konomi.career_accepts_now") != outcome.Has("konomi.career_waits"), "Career choice has conflicting or missing costs.");
                        if (scene.Id == "konomi.chosen_evening")
                        {
                            Check(outcome.Has("konomi.lovers") && outcome.Has("konomi.private_evening_kept"), "Chosen courtship fails to establish relationship progress.");
                            Check(outcome.Has("konomi.private_night_chosen") != outcome.Has("konomi.private_quiet_chosen"), "Evening confuses intimate and quiet choices.");
                            Check(outcome.Has("konomi.committed") == (history == "committed"), "Evening jumps from courtship to commitment.");
                        }
                        var next = scenes[Array.IndexOf(scenes, scene) + 1];
                        Check(!Rules.Available(story, next, outcome), "Private future skips the next scene's delay.");
                        outcome.Hour += next.DelayHours - 1;
                        Check(!Rules.Available(story, next, outcome), "Private future opens before the delay boundary.");
                        outcome.Hour++;
                        continuing.Add(outcome);
                    }
                }
                states = continuing;
                var ready = Copy(initial); ready.Flags.UnionWith(scene.Requires);
                foreach (var prerequisite in scene.Requires)
                {
                    var missing = Copy(ready); missing.Flags.Remove(prerequisite);
                    Check(!Rules.Available(story, scene, missing), "Private future ignores " + prerequisite);
                }
                foreach (var blocker in new[] { "konomi.present", "konomi.closed", "inhuman", "konomi.farewell", "konomi.private_future" })
                {
                    var blocked = Copy(ready); blocked.Flags.Add(blocker);
                    Check(!Rules.Available(story, scene, blocked), "Private future ignores " + blocker);
                }
                ready.Chapter = 4;
                Check(!Rules.Available(story, scene, ready), "Private future appears during Abyss separation.");
                ready.Chapter = chapter; ready.Area = "elsewhere";
                Check(!Rules.Available(story, scene, ready), "Private future appears outside Drezen.");
            }
        }
    }

    private static void CheckKonomiDistance()
    {
        var scenes = new[] { "capital_letter", "return_offer", "private_reunion" }
            .Select(id => story.Scenes.Single(s => s.Id == "konomi." + id)).ToArray();
        foreach (var chapter in new[] { 3, 5 })
        foreach (var history in new[] { "new", "lovers", "committed" })
        foreach (bool alternate in new[] { false, true })
        {
            var initial = new Snapshot { Chapter = chapter, Hour = 1000, Area = scenes[0].Areas.Single() };
            initial.Flags.UnionWith(scenes[0].Requires);
            foreach (var group in scenes[0].RequiresAnyGroups) initial.Flags.Add(group[0]);
            initial.Flags.UnionWith(new[] { "legend", "seelah.committed", "konomi.reconnection_open" });
            initial.Flags.Add(alternate ? "konomi.departure_arguments" : "konomi.departure_plain_letters");
            initial.Flags.Add(alternate ? "konomi.carriers_asked" : "konomi.carriers_measured");
            if (alternate) initial.Flags.Add("konomi.private_other_promises");
            if (history != "new") initial.Flags.Add("konomi.lovers");
            if (history == "committed") initial.Flags.Add("konomi.committed");
            initial.Times["konomi.private_departed"] = 100;
            var early = Copy(initial); early.Hour = 435;
            Check(!Rules.Available(story, scenes[0], early), "Capital letter arrives before its departure delay.");
            early.Hour++;
            Check(Rules.Available(story, scenes[0], early), "Capital letter misses its arrival boundary.");
            var states = new List<Snapshot> { initial };
            foreach (var scene in scenes)
            {
                var continuing = new List<Snapshot>();
                foreach (var state in states)
                {
                    Check(Rules.Available(story, scene, state), "Distance continuation cannot open: " + scene.Id);
                    Check(Rules.EntryTargets(scene).Length == 0, "Distance continuation depends on a native officer actor.");
                    string Destination(string nodeId) => scene.Nodes.Single(n => n.Id == nodeId).Choices
                        .Single(c => Rules.Match(c.Requires, c.Forbids, state)).Next!;
                    if (scene.Id == "konomi.capital_letter")
                    {
                        Check(Destination("arrival") == (alternate ? "arguments" : "refusal"), "Capital letter forgets the requested subject.");
                        Check(Destination("second") == (alternate ? "asked" : "measured"), "Capital letter invents the player's carrier-yard contribution.");
                    }
                    if (scene.Id == "konomi.return_offer")
                        Check(Destination("reply") == (state.Has("konomi.capital_reply_quiet") ? "quiet" : "distraction"), "Return offer ignores the Commander's reply.");
                    if (scene.Id == "konomi.private_reunion")
                    {
                        Check(Destination("parcel") == (state.Has("konomi.return_walk") ? "walk" : "room"), "Reunion forgets the agreed activity.");
                        Check(Destination("schedule") == (alternate ? "others" : "plans"), "Reunion loses the earlier discussion of other partners.");
                    }
                    foreach (var outcome in Walk(scene, state))
                    {
                        Check(outcome.Has("konomi.dismissed") && outcome.Has("konomi.office_completed") && !outcome.Has("konomi.present"), "Distance scenes rewrite the native dismissal.");
                        Check(outcome.Has("konomi.lovers") == (history != "new") && outcome.Has("konomi.committed") == (history == "committed"), "Distance scenes invent or erase romance stages.");
                        Check(outcome.Has("seelah.committed") && !outcome.Has("konomi.closed"), "Distance scenes change another relationship or close this one.");
                        if (!outcome.Has(scene.Id))
                        {
                            Check(outcome.Flags.SetEquals(state.Flags) && Rules.Available(story, scene, outcome), "Postponed correspondence records progress or cannot resume.");
                            continue;
                        }
                        Check(!Rules.Available(story, scene, outcome), "Completed correspondence repeats.");
                        if (scene.Id == "konomi.capital_letter")
                            Check(outcome.Has("konomi.capital_answer_sent") && outcome.Has("konomi.capital_reply_quiet") != outcome.Has("konomi.capital_reply_distraction"), "Capital reply is unsent or has conflicting subjects.");
                        if (scene.Id == "konomi.return_offer")
                            Check(outcome.Has("konomi.return_expected") && outcome.Has("konomi.return_walk") != outcome.Has("konomi.return_private_evening"), "Return plan is absent or has conflicting activities.");
                        if (scene.Id == "konomi.private_reunion")
                        {
                            Check(outcome.Has("konomi.private_returned") && outcome.Has("konomi.reunion_kept"), "Reunion does not record the actual private return.");
                            Check(outcome.Has("konomi.distance_wants_visits") != outcome.Has("konomi.distance_taking_time"), "Reunion loses the chosen relationship pace.");
                            Check(!outcome.Has("konomi.reunion_kissed") || outcome.Has("konomi.distance_wants_visits"), "Slow reunion assumes an unchosen kiss.");
                            var oldVisit = story.Scenes.Single(s => s.Id == "konomi.carriers");
                            var past = Copy(outcome); past.Flags.UnionWith(oldVisit.Requires);
                            Check(!Rules.Available(story, oldVisit, past), "Temporary return replays the earlier carrier-yard visit.");
                        }
                        else
                        {
                            var next = scenes[Array.IndexOf(scenes, scene) + 1];
                            Check(!Rules.Available(story, next, outcome), "Distance continuation skips correspondence or travel time.");
                            outcome.Hour += next.DelayHours - 1;
                            Check(!Rules.Available(story, next, outcome), "Distance continuation opens before its delay boundary.");
                            outcome.Hour++;
                            continuing.Add(outcome);
                        }
                    }
                }
                states = continuing;
                var ready = Copy(initial); ready.Flags.UnionWith(scene.Requires);
                foreach (var required in scene.Requires.Concat(scene.RequiresAnyGroups.Select(group => group[0])))
                {
                    var missing = Copy(ready); missing.Flags.Remove(required);
                    Check(!Rules.Available(story, scene, missing), "Distance continuation ignores " + required);
                }
                foreach (var blockedBy in new[] { "konomi.present", "konomi.closed", "inhuman", "konomi.farewell" })
                {
                    var blocked = Copy(ready); blocked.Flags.Add(blockedBy);
                    Check(!Rules.Available(story, scene, blocked), "Distance continuation ignores " + blockedBy);
                }
                ready.Chapter = 4;
                Check(!Rules.Available(story, scene, ready), "Drezen correspondence appears in the Abyss.");
                ready.Chapter = chapter; ready.Area = "elsewhere";
                Check(!Rules.Available(story, scene, ready), "Drezen correspondence appears elsewhere.");
            }
        }
    }

    private static void CheckKonomiPrivateContinuation()
    {
        var scenes = new[] { "carriers", "before_road", "private_departure" }
            .Select(id => story.Scenes.Single(s => s.Id == "konomi." + id)).ToArray();
        foreach (var chapter in new[] { 3, 5 })
        foreach (var history in new[] { "new", "lovers", "committed" })
        {
            var initial = new Snapshot { Chapter = chapter, Hour = 1000, Area = scenes[0].Areas.Single() };
            initial.Flags.UnionWith(scenes[0].Requires);
            foreach (var group in scenes[0].RequiresAnyGroups) initial.Flags.Add(group[0]);
            initial.Flags.UnionWith(new[] { "legend", "konomi.private_unhurried", "seelah.committed" });
            if (history != "new") initial.Flags.Add("konomi.lovers");
            if (history == "committed") initial.Flags.Add("konomi.committed");
            var recentlyMet = Copy(initial);
            recentlyMet.Times["konomi.private_meeting"] = initial.Hour;
            recentlyMet.Hour += 23;
            Check(!Rules.Available(story, scenes[0], recentlyMet), "Carrier visit begins before a day has passed since the private meeting.");
            recentlyMet.Hour++;
            Check(Rules.Available(story, scenes[0], recentlyMet), "Carrier visit does not open at its 24-hour boundary.");
            var states = new List<Snapshot> { initial };
            foreach (var scene in scenes)
            {
                var continuing = new List<Snapshot>();
                foreach (var state in states)
                {
                    Check(Rules.Available(story, scene, state), "Private continuation cannot open after the preceding scene: " + scene.Id);
                    Check(Rules.EntryTargets(scene).Length == 0, "Private continuation needs the dismissed native actor.");
                    if (scene.Id == "konomi.before_road")
                        Check(scene.Nodes.Single(n => n.Id == "histories").Choices.Single(c => Rules.Match(c.Requires, c.Forbids, state)).Next == (history == "new" ? "new" : "lovers"), "Evening invents or loses intimate history.");
                    if (scene.Id == "konomi.private_departure")
                        Check(scene.Nodes.Single(n => n.Id == "address").Choices.Any(c => c.Next == "kiss" && Rules.Match(c.Requires, c.Forbids, state)) == state.Has("konomi.before_road_hand"), "Departure ignores the chosen physical pace.");
                    foreach (var outcome in Walk(scene, state))
                    {
                        Check(outcome.Has("konomi.dismissed") && outcome.Has("konomi.office_completed") && !outcome.Has("konomi.present"), "Private continuation restores the council appointment.");
                        Check(outcome.Has("konomi.lovers") == (history != "new") && outcome.Has("konomi.committed") == (history == "committed"), "Private continuation silently changes the romance stage.");
                        Check(outcome.Has("seelah.committed") && !outcome.Has("konomi.closed"), "Private continuation alters another romance or closes this one.");
                        if (!outcome.Has(scene.Id))
                        {
                            Check(Rules.Available(story, scene, outcome), "Postponed private scene cannot be resumed.");
                            Check(outcome.Flags.SetEquals(state.Flags), "Postponement records an event that did not happen.");
                            continue;
                        }
                        Check(!Rules.Available(story, scene, outcome), "Completed private continuation repeats.");
                        if (scene.Id == "konomi.private_departure")
                        {
                            Check(outcome.Has("konomi.private_departed") && outcome.Has("konomi.private_address"), "Departure loses the correspondence address.");
                            Check(outcome.Has("konomi.departure_plain_letters") != outcome.Has("konomi.departure_arguments"), "Departure loses the chosen letter subject.");
                            foreach (var earlier in scenes)
                            {
                                var unplayed = Copy(outcome); unplayed.Flags.Remove(earlier.Id);
                                Check(!Rules.Available(story, earlier, unplayed), "Departed Konomi remains available for a local visit.");
                            }
                        }
                        else
                        {
                            var next = scenes[Array.IndexOf(scenes, scene) + 1];
                            Check(!Rules.Available(story, next, outcome), "Private continuation skips its delay.");
                            outcome.Hour += 24;
                            continuing.Add(outcome);
                        }
                    }
                }
                states = continuing;
                var ready = Copy(initial); ready.Flags.UnionWith(scene.Requires);
                foreach (var required in scene.Requires.Concat(scene.RequiresAnyGroups.Select(group => group[0])))
                {
                    var missing = Copy(ready); missing.Flags.Remove(required);
                    Check(!Rules.Available(story, scene, missing), "Private continuation ignores " + required);
                }
                foreach (var blockedBy in new[] { "konomi.present", "konomi.closed", "inhuman", "konomi.farewell", "konomi.private_departed" })
                {
                    var blocked = Copy(ready); blocked.Flags.Add(blockedBy);
                    Check(!Rules.Available(story, scene, blocked), "Private continuation ignores " + blockedBy);
                }
                ready.Chapter = 4;
                Check(!Rules.Available(story, scene, ready), "Private Drezen visit occurs during Abyss separation.");
                ready.Chapter = chapter; ready.Area = "elsewhere";
                Check(!Rules.Available(story, scene, ready), "Private Drezen visit occurs in another area.");
            }
        }
    }

    private static void CheckKonomiPost()
    {
        var post = story.Scenes.Single(s => s.Id == "konomi.fate_post");
        var reply = story.Scenes.Single(s => s.Id == "konomi.fate_reply");
        var meeting = story.Scenes.Single(s => s.Id == "konomi.private_meeting");
        foreach (var chapter in new[] { 3, 5 })
        foreach (var history in new[] { "new", "lovers", "committed" })
        {
            bool lovers = history != "new";
            var initial = new Snapshot { Chapter = chapter, Hour = 1000, Area = post.Areas.Single() };
            initial.Flags.UnionWith(new[] { "trickster", "konomi.dismissed", "konomi.office_completed", "seelah.committed" });
            if (lovers) initial.Flags.Add("konomi.lovers");
            if (history == "committed") initial.Flags.Add("konomi.committed");
            Check(Rules.Available(story, post, initial), "Trickster cannot attempt a personal invitation after completed dismissal.");
            Check(Rules.EntryTargets(post).Length == 0, "Dismissed Konomi invitation depends on her hidden actor.");
            foreach (var needed in new[] { "trickster", "konomi.dismissed", "konomi.office_completed" })
            {
                var missing = Copy(initial); missing.Flags.Remove(needed);
                Check(!Rules.Available(story, post, missing), "Konomi invitation ignores missing " + needed);
            }
            foreach (var blocker in new[] { "konomi.present", "konomi.closed", "inhuman", "konomi.farewell" })
            {
                var blocked = Copy(initial); blocked.Flags.Add(blocker);
                Check(!Rules.Available(story, post, blocked), "Konomi invitation ignores " + blocker);
            }
            var letter = post.Nodes.Single(n => n.Id == "letter");
            Check(letter.Choices.Single(c => Rules.Match(c.Requires, c.Forbids, initial)).Next == (lovers ? "lover" : "first"), "Trickster invitation invents a past intimate relationship.");
            foreach (var result in Walk(post, initial))
            {
                Check(result.Has("konomi.post_sent") == result.Has(post.Id), "Postponed invitation claims it was sent.");
                Check(!result.Has("konomi.present") && result.Has("konomi.committed") == (history == "committed"), "Invitation invents restored contact or alters a commitment.");
                Check(result.Has("konomi.dismissed") && result.Has("konomi.office_completed"), "Invitation erases native political history.");
                Check(result.Has("seelah.committed"), "Invitation alters another relationship.");
                if (result.Has(post.Id))
                {
                    Check(!Rules.Available(story, post, result), "One-off Trickster post repeats.");
                    Check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "konomi.margin"), result), "A sent invitation alone reopens ordinary meetings.");
                    Check(!Rules.Available(story, reply, result), "Konomi replies before the correspondence delay.");
                    result.Hour += 48;
                    Check(Rules.Available(story, reply, result), "Konomi cannot reply to the sent invitation.");
                    var legendReply = Copy(result); legendReply.Flags.Remove("trickster"); legendReply.Flags.Add("legend");
                    Check(Rules.Available(story, reply, legendReply), "Becoming Legend cancels an already sent invitation.");
                    Check(!Rules.Available(story, meeting, result), "Konomi meeting precedes an accepted appointment.");
                    Check(reply.Nodes[0].Choices.Single(c => Rules.Match(c.Requires, c.Forbids, result)).Next == (lovers ? "lover" : "first"), "Konomi reply invents or forgets the earlier romance.");
                    foreach (var response in Walk(reply, result))
                    {
                        if (response.Has("konomi.closed"))
                        {
                            Check(response.Has("konomi.private_declined") && !Rules.Available(story, meeting, response), "Declined invitation still leads to a meeting.");
                            var epilogue = Copy(response); epilogue.Chapter = 5;
                            var endings = story.Scenes.Where(s => s.Relationship == "konomi" && s.Owner == "Epilogue" && Rules.Available(story, s, epilogue)).ToArray();
                            Check(endings.Length == 1 && endings[0].Id == "konomi.ending_dismissed_apart", "Declined private invitation lacks an ending or restores official correspondence after dismissal.");
                            continue;
                        }
                        if (!response.Has(reply.Id))
                        {
                            Check(!response.Has("konomi.private_appointment") && !Rules.Available(story, meeting, response), "Postponed reply claims an appointment.");
                            continue;
                        }
                        Check(!Rules.Available(story, meeting, response), "Private appointment skips its delay.");
                        response.Hour += 24;
                        Check(Rules.Available(story, meeting, response), "Private appointment never becomes reachable.");
                        var legendMeeting = Copy(response); legendMeeting.Flags.Remove("trickster"); legendMeeting.Flags.Add("legend");
                        Check(Rules.Available(story, meeting, legendMeeting), "Private conversation requires powers no longer used.");
                        foreach (var visit in Walk(meeting, response))
                        {
                            Check(visit.Has("konomi.reconnection_open") == visit.Has(meeting.Id), "Postponed meeting claims renewed personal contact.");
                            Check(visit.Has("konomi.dismissed") && visit.Has("konomi.office_completed") && !visit.Has("konomi.present"), "Private meeting reverses the native dismissal.");
                            Check(visit.Has("konomi.lovers") == lovers && visit.Has("konomi.committed") == (history == "committed"), "Private meeting invents or erases intimacy and commitment.");
                            Check(visit.Has("seelah.committed") && !visit.Has("konomi.closed"), "Private meeting closes or alters another relationship.");
                            if (!visit.Has(meeting.Id)) continue;
                            Check(visit.Has("konomi.private_stands_by") != visit.Has("konomi.private_admits_mistake"), "Meeting loses the political disagreement response.");
                            Check(visit.Has("konomi.private_interest") != visit.Has("konomi.private_unhurried"), "Meeting loses the pace chosen for renewed contact.");
                            Check(!Rules.Available(story, meeting, visit), "First private meeting repeats after completion.");
                            Check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "konomi.margin"), visit), "Private visit reopens an official-office scene.");
                        }
                    }
                }
            }
            initial.Chapter = 4;
            Check(!Rules.Available(story, post, initial), "Dismissal invitation ignores Abyss separation.");
            foreach (var scene in new[] { reply, meeting })
            {
                var ready = new Snapshot { Chapter = chapter, Hour = 1000, Area = initial.Area };
                ready.Flags.UnionWith(scene.Requires);
                Check(Rules.EntryTargets(scene).Length == 0 && Rules.Available(story, scene, ready), "Private correspondence relies on an unavailable native actor.");
                foreach (var prerequisite in scene.Requires)
                {
                    var missing = Copy(ready); missing.Flags.Remove(prerequisite);
                    Check(!Rules.Available(story, scene, missing), "Private correspondence ignores " + prerequisite);
                }
                foreach (var blocker in new[] { "konomi.present", "konomi.closed", "inhuman", "konomi.farewell" })
                {
                    var blocked = Copy(ready); blocked.Flags.Add(blocker);
                    Check(!Rules.Available(story, scene, blocked), "Private correspondence ignores " + blocker);
                }
                ready.Chapter = 4;
                Check(!Rules.Available(story, scene, ready), "Private Drezen meeting appears during Abyss separation.");
            }
        }
    }

    private static void CheckKonomiHearing()
    {
        var hearing = story.Scenes.Single(s => s.Id == "konomi.hearing");
        var evening = story.Scenes.Single(s => s.Id == "konomi.hearing_after");
        var letter = story.Scenes.Single(s => s.Id == "konomi.new_letter");
        foreach (var chapter in new[] { 3, 5 })
        foreach (var history in new[] { "public", "discreet", "denial" })
        {
            var initial = new Snapshot { Chapter = chapter, Hour = 1048, Area = hearing.Areas.Single() };
            initial.AvailableContacts.Add("ca2d58c5c65723945857e04fb85d30ce");
            initial.Flags.UnionWith(new[] { "konomi.present", "konomi.lovers", "konomi.scandal_answered", "seelah.committed", "jerribeth.committed" });
            initial.Flags.Add(history == "public" ? "konomi.public" : "konomi.discreet");
            if (history == "denial") initial.Flags.UnionWith(new[] { "konomi.almost_denied", "konomi.apologized" });
            initial.Times["konomi.scandal_answered"] = 1000;
            initial.Hour--;
            Check(!Rules.Available(story, hearing, initial), "Konomi hearing skips its scheduling delay.");
            initial.Hour++;
            Check(Rules.Available(story, hearing, initial), "Konomi hearing cannot follow the scandal.");
            Check(!Rules.Available(story, evening, initial), "Konomi recalls an unheard complaint.");
            var arrival = hearing.Nodes.Single(n => n.Id == "arrival");
            Check(arrival.Choices.Single(c => Rules.Match(c.Requires, c.Forbids, initial)).Next == (history == "public" ? "public" : "discreet"), "Hearing invents a different public disclosure history.");
            var outcomes = Walk(hearing, initial);
            Check(outcomes.Any(s => s.Has("konomi.hearing_withdrew_permission") && s.Has("konomi.hearing_buyer_unbarred")), "Full-letter consent cannot be withdrawn before comparison.");
            Check(outcomes.Any(s => s.Has("konomi.hearing_buyer_barred")), "Full evidence cannot produce its distinct finding.");
            Check(outcomes.Any(s => s.Has("konomi.hearing_covered") && s.Has("konomi.hearing_buyer_unbarred")), "Covered evidence cannot produce its distinct finding.");
            foreach (var result in outcomes)
            {
                if (!result.Has(hearing.Id))
                {
                    Check(!result.Has("konomi.hearing_finished") && !result.Has("konomi.hearing_owned_letter"), "Postponing the hearing claims attendance or testimony.");
                    continue;
                }
                Check(result.Has("konomi.hearing_owned_letter"), "Hearing omits the Commander's acknowledgment.");
                Check(result.Has("konomi.hearing_buyer_barred") != result.Has("konomi.hearing_buyer_unbarred"), "Hearing findings overlap or disappear.");
                Check(!Rules.Available(story, hearing, result), "Completed hearing repeats.");
                Check(!Rules.Available(story, evening, result), "Hearing aftermath opens immediately.");
                result.Hour += 24;
                Check(Rules.Available(story, evening, result), "Hearing aftermath cannot be reached.");
                var start = evening.Nodes[0];
                Check(start.Choices.Single(c => Rules.Match(c.Requires, c.Forbids, result)).Next == (result.Has("konomi.hearing_buyer_barred") ? "whole" : "covered"), "Aftermath uses intended consent rather than the actual finding.");
                foreach (var end in Walk(evening, result))
                {
                    Check(end.Has("konomi.hearing_evening_kept") && !end.Has("konomi.closed"), "An evidence disagreement closes or stalls Konomi's romance.");
                    Check(end.Has("konomi.hearing_trust_repaired") == (history == "denial"), "Hearing repair invents or forgets the earlier denial.");
                    Check(end.Has("seelah.committed") && end.Has("jerribeth.committed"), "Konomi's hearing alters other relationships.");
                    Check(end.Has("konomi.public") == (history == "public"), "A private hearing forces public relationship disclosure.");
                    Check(!Rules.Available(story, evening, end), "Completed hearing aftermath repeats.");
                    Check(!Rules.Available(story, letter, end), "Konomi letter payoff skips its waiting period.");
                    end.Hour += 24;
                    Check(Rules.Available(story, letter, end) == end.Has("konomi.hearing_new_letter"), "Konomi invents or forgets the promised new letter.");
                    if (end.Has("konomi.hearing_new_letter"))
                    {
                        foreach (var outing in Walk(letter, end))
                        {
                            if (!outing.Has(letter.Id))
                            {
                                Check(!outing.Has("konomi.new_letter_outing") && !outing.Has("konomi.new_letter_frank") && !outing.Has("konomi.new_letter_challenge"), "Postponed letter records a delivered invitation or outing.");
                                continue;
                            }
                            Check(outing.Has("konomi.new_letter_outing"), "New letter has no played outing payoff.");
                            Check(outing.Has("konomi.new_letter_frank") != outing.Has("konomi.new_letter_challenge"), "New letter conflates romantic and playful wording.");
                            Check(outing.Has("konomi.rings_bell") != outing.Has("konomi.rings_empty_handed"), "Konomi's ring-toss results overlap or disappear.");
                            Check(outing.Has("konomi.rings_commander_rooster") != outing.Has("konomi.rings_commander_ribbon"), "Commander wins inconsistent prizes.");
                            var keepsakes = new[] { "konomi.keeps_rooster", "konomi.commander_keeps_rooster", "konomi.keeps_ribbon", "konomi.commander_keeps_ribbon" };
                            Check(keepsakes.Count(outing.Has) == 1, "Outing awards a keepsake to conflicting owners.");
                            Check((outing.Has("konomi.keeps_rooster") || outing.Has("konomi.commander_keeps_rooster")) == outing.Has("konomi.rings_commander_rooster"), "Outing gives away an unwon rooster.");
                            Check(!outing.Has("konomi.new_letter_kissed") || outing.Has("konomi.new_letter_frank"), "Playful letter invents a prior kiss invitation.");
                            Check(outing.Has("seelah.committed") && outing.Has("jerribeth.committed") && !outing.Has("konomi.closed"), "Competitive outing changes relationships.");
                            Check(outing.Has("konomi.public") == (history == "public"), "Outing overwrites the earlier disclosure choice.");
                            Check(!Rules.Available(story, letter, outing), "New letter repeats after completion.");
                            var offered = letter.Nodes.Single(n => n.Id == "walk").Choices.Where(c => Rules.Match(c.Requires, c.Forbids, outing)).Select(c => c.Next).ToArray();
                            Check(offered.Contains("challenge_winner") == (outing.Has("konomi.new_letter_challenge") && outing.Has("konomi.rings_bell") && outing.Has("konomi.rings_commander_ribbon")), "Konomi claims a victory that the prizes do not support.");
                            Check(offered.Contains("challenge_reply") == (outing.Has("konomi.new_letter_challenge") && outing.Has("konomi.rings_commander_rooster")), "Commander's victory teasing contradicts the prize.");
                        }
                        var transformed = Copy(end); transformed.Flags.Add("inhuman");
                        Check(!Rules.Available(story, letter, transformed), "Physical outing invents a transformed-body accommodation.");
                    }
                }
            }
            foreach (var scene in new[] { hearing, evening, letter })
            {
                var ready = Copy(initial);
                ready.Flags.UnionWith(scene.Requires);
                foreach (var blocker in new[] { "konomi.closed", "konomi.farewell" })
                {
                    var blocked = Copy(ready); blocked.Flags.Add(blocker);
                    Check(!Rules.Available(story, scene, blocked), "Konomi hearing sequence ignores " + blocker);
                }
                ready.Flags.Remove("konomi.present");
                Check(!Rules.Available(story, scene, ready), "Konomi hearing invents absent contact.");
                ready.Flags.Add("konomi.present");
                ready.Chapter = 4;
                Check(!Rules.Available(story, scene, ready), "Konomi hearing appears in the Abyss.");
            }
        }
    }

    private static void CheckEmberOpening()
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "ember." + id);
        var initial = new Snapshot { Chapter = 3, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
        Check(!Rules.Available(story, Find("drawing"), initial), "Ember friendship opens without native presence.");
        initial.Flags.Add("ember.present");
        foreach (var blocker in new[] { "ember_dead", "ember_gone", "ember.absent", "ember.closed" })
        {
            var blocked = Copy(initial); blocked.Flags.Add(blocker);
            Check(!Rules.Available(story, Find("drawing"), blocked), "Ember drawing ignores " + blocker);
        }
        foreach (var first in Walk(Find("drawing"), initial).Where(s => s.Has("ember.started")))
        {
            Check(!Rules.Available(story, Find("visitor"), first), "Ember loses the delay between afternoons.");
            first.Hour += 24;
            Check(Rules.Available(story, Find("visitor"), first), "Ember second afternoon is unreachable.");
            foreach (var second in Walk(Find("visitor"), first))
            {
                Check(second.Has("ember.ask_first") || second.Has("ember.answer_respected"), "Ember visitor encounter loses its response history.");
                second.Hour += 24;
                Check(Rules.Available(story, Find("rain"), second), "Ember drawing callback is unreachable.");
                Check(Walk(Find("rain"), second).All(s => s.Has("ember.shared_afternoon")), "Ember drawing choice leaves an unfinished callback.");
            }
        }
    }

    private static void CheckKianaCampaign()
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "kiana." + id);
        var missing = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
        missing.Flags.Add("seelah.souls_returned");
        Check(!Rules.Available(story, Find("invitation"), missing), "Kiana starts before her native aftermath encounter.");
        missing.Flags.Remove("seelah.souls_returned");
        missing.Flags.Add("kiana.aftermath_seen");
        Check(!Rules.Available(story, Find("invitation"), missing), "Kiana starts while soul rescue remains unresolved.");
        foreach (string path in new[] { "angel", "azata", "aeon", "demon", "devil", "dragon", "legend", "trickster", "true_lich", "swarm" })
        foreach (string route in new[] { "widow", "wait", "affair" })
        foreach (string letter in new[] { "moon", "guest" })
        {
            bool transformed = path == "true_lich" || path == "swarm";
            if (transformed && route == "affair") continue;
            var state = new Snapshot { Chapter = 5, Hour = 1000, Area = missing.Area };
            state.Flags.UnionWith(new[] { path, "seelah.souls_returned", "kiana.aftermath_seen", "seelah.in_party", "committed", "seelah.committed", "konomi.committed", "jerribeth.committed" });
            if (route == "widow") state.Flags.Add("seelah.elan_dead");
            if (transformed) state.Flags.Add("inhuman");
            void Play(string id, string wanted)
            {
                var next = Find(id);
                Check(Rules.Available(story, next, state), "Kiana progression blocked: " + path + "/" + route + "/" + id);
                Check(Rules.EntryTargets(next).Length == 0, "Kiana relies on exhausted native answers.");
                var outcomes = Walk(next, state);
                Check(outcomes.Any(s => s.Has(wanted) && !s.Has("kiana.closed")), "Kiana outcome unavailable: " + wanted);
                state = outcomes.First(s => s.Has(wanted) && !s.Has("kiana.closed"));
            }
            Play("invitation", "kiana." + letter);
            state.Hour += 48;
            Play("rehearsal", "kiana.company");
            Check(!Rules.Available(story, Find("stagecraft"), state), "Kiana rehearsal follow-up skips its waiting period.");
            Check(!Rules.Available(story, Find(route == "widow" ? "widow" : "marriage"), state), "Kiana skips time after first company.");
            state.Hour += 168;
            Play("stagecraft", "kiana.rehearsed");
            Check(!Rules.Available(story, Find("stagecraft"), state), "Kiana rehearsal follow-up repeats after completion.");
            Play(route == "widow" ? "widow" : "marriage", route == "widow" ? "kiana.available" : route == "affair" ? "kiana.affair" : "kiana.waited");
            if (route != "widow")
            {
                Check(!Rules.Available(story, Find("date"), state), "Kiana offers an established date before addressing her marriage.");
                state.Hour += 120;
                Play("answer", "kiana.available");
                Check(state.Has("kiana.separated"), "Kiana marriage outcome was not recorded.");
                Check(route != "affair" || state.Has("kiana.owned_hurt"), "Kiana affair bypasses its consequence conversation.");
            }
            state.Hour += Find("date").DelayHours - 1;
            Check(!Rules.Available(story, Find("date"), state), "Kiana invitation bypasses her chosen waiting period.");
            state.Hour++;
            Play("date", "kiana.lovers");
            Check(!transformed || !state.Has("kiana.kissed"), "Kiana assumes transformed physical intimacy.");
            state.Hour += 48;
            Play("seelah", "kiana.seelah_spoke");
            Check(route != "affair" || state.Has("kiana.defend_elan"), "Seelah ignores harm from concealment.");
            Play("morning", "kiana.committed");
            state.Hour += 48;
            bool developedRoute = story.Scenes.Any(s => s.Id == "kiana.a_place_afterward");
            if (developedRoute && !transformed)
            {
                Check(!Rules.Available(story, Find("farewell"), state), "Kiana farewell bypasses developed continuation.");
                var chain = new[] { "guest_table", "market_weather", "lenna_door", "blue_room", "bakery_stairs", "last_page", "first_readers", "ink_after", "working_room", "kept_evening" }.AsEnumerable();
                if (story.Scenes.Any(s => s.Id == "kiana.borrowed_name"))
                    chain = chain.Concat(new[] { "borrowed_name", "yard_evening", "unborrowed_evening" });
                foreach (string id in chain.Append("a_place_afterward"))
                {
                    state.Hour += Find(id).DelayHours;
                    Play(id, "kiana." + id);
                }
            }
            Play("farewell", "kiana.farewell_kept");
            string Ending() => story.Scenes.Single(s => s.Relationship == "kiana" && s.Owner == "Epilogue" && Rules.Available(story, s, state)).Id;
            Check(Ending() == (developedRoute && transformed ? "kiana.ending_promised" : route == "widow" ? "kiana.ending_bereaved" : "kiana.ending_together"), "Kiana commitment loses her marital history or has conflicting endings.");
            state.Flags.Add("ascended");
            Check(Ending() == (developedRoute && transformed ? "kiana.ending_promised" : "kiana.ending_ascended"), "Kiana ascension has conflicting endings.");
            state.Flags.Add("kiana.closed");
            Check(Ending() == "kiana.ending_apart", "Kiana closure has conflicting endings.");
        }
    }

    private static void CheckJerribethCampaign()
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == "jerribeth." + id);
        var unmet = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
        Check(!Rules.Available(story, Find("invitation"), unmet), "Jerribeth contacts a Commander who never met her.");
        unmet.Flags.Add("JerribethLovesUsVeryMuch");
        Check(!Rules.Available(story, Find("invitation"), unmet), "Native misleading affection marker starts Jerribeth courtship.");
        unmet.Flags.Add("jerribeth.met");
        Check(Rules.Available(story, Find("invitation"), unmet), "Known living Jerribeth cannot offer correspondence.");
        unmet.Flags.Add("jerribeth.unavailable");
        Check(!Rules.Available(story, Find("invitation"), unmet), "Unavailable Jerribeth offers correspondence without restoration.");

        // Sol r1 (HOW): native observations are completed before every step (so "trickster" latches trickster.ever, as a
        // real Trickster save does), authored prerequisites come only from their producers, and manual reads are omitted.
        foreach (bool trickster in new[] { false, true })
        foreach (int start in new[] { 3, 4, 5 })
        foreach (bool inhuman in new[] { false, true })
        foreach (bool patronLost in new[] { false, true })
        foreach (bool knowledge in new[] { false, true })
        {
            var state = new Snapshot { Chapter = start, Hour = 1000 };
            state.Flags.UnionWith(new[] { "jerribeth.met", "jerribeth.refuge_known", "seelah.closed", "konomi.closed", "closed" });
            if (trickster) state.Flags.Add("trickster");
            var letters = new Dictionary<int, int>();
            if (inhuman) state.Flags.Add("inhuman");
            if (patronLost) state.Flags.Add("jerribeth.patron_lost");
            if (knowledge) state.Flags.UnionWith(new[] { "jerribeth.wintersun_known", "jerribeth.xanthir_known" });
            for (int chapter = start; chapter <= 5; chapter++)
            {
                state.Chapter = chapter;
                state.Area = chapter == 4 ? "7847c3e3537104f4694167af0b9fcd0e" : "2570015799edf594daf2f076f2f975d8";
                for (int attempt = 0; attempt < story.Scenes.Count; attempt++)
                {
                    state.Hour += 48;
                    if (chapter > 1) state.Flags.Add("chapter_later");
                    Rules.Complete(story, state);
                    Check(state.Has("trickster.ever") == trickster, "Jerribeth campaign: trickster.ever is not latched from a native Trickster run.");
                    var next = story.Scenes.FirstOrDefault(s => s.Relationship == "jerribeth" && !s.ManualOnly && !s.Reaction && !s.Id.StartsWith("jerribeth.trickster.") && !s.Owner.EndsWith("Epilogue") && Rules.Available(story, s, state));
                    if (next == null) break;
                    Check(Rules.EntryTargets(next).Length == 0 && Rules.IsRemote(next), "Jerribeth correspondence takes over a native encounter.");
                    Check(next.Nodes[0].Choices.Any(c => Rules.Match(c.Requires, c.Forbids, state)), "A delivered Jerribeth letter opens with no answer: " + next.Id);
                    letters[chapter] = letters.TryGetValue(chapter, out var sent) ? sent + 1 : 1;
                    var outcomes = Walk(next, state).Where(s => s.Has(next.Id) && !s.Has("jerribeth.closed"));
                    // Alternate private and slower paths, and exercise the Trickster option.
                    if (next.Id == "jerribeth.evening") outcomes = outcomes.Where(s => s.Has(inhuman ? "jerribeth.slow_evening" : "jerribeth.private_evening"));
                    state = outcomes.OrderByDescending(s => s.Has("jerribeth.fate_terms")).First();
                }
            }
            Check(state.Has("jerribeth.farewell_kept") && state.Has("jerribeth.committed"), "Jerribeth campaign cannot reach farewell.");
            Check(state.Has("jerribeth.fate_terms") == trickster, "Jerribeth Trickster response is unreachable on a fresh Trickster history, or leaks off it.");
            Check(!trickster || state.Has("jerribeth.trickster.cost.forfeit"), "Jerribeth's fresh Trickster contract has no forfeit.");
            // COX (ledger R2-5, Sol r1): on the path, at most three Jerribeth letters in Chapter 4; the Chapter 3 core is at most eight.
            Check((!trickster || letters.GetValueOrDefault(4) <= 3 && letters.GetValueOrDefault(5) <= 8) && letters.GetValueOrDefault(3) <= 8, "Jerribeth chapter letter limit exceeded: Ch3 "
                  + letters.GetValueOrDefault(3) + ", Ch4 " + letters.GetValueOrDefault(4) + ", Ch5 " + letters.GetValueOrDefault(5) + " (start " + start + ", Trickster " + trickster + ").");
            // COX edit (Trickster spec): the refuge gates on her own evidence; the patron loss is a variant of its text. Both are
            // Chapter 4 letters, so a correspondence begun at the Nexus or later never reaches them.
            Check(state.Has("jerribeth.refuge_acknowledged") == (start == 3), "Jerribeth refuge unreachable on her own evidence, or read outside Chapter 4.");
            Check(state.Has("jerribeth.warned") == (start == 3 && !patronLost), "Jerribeth offers a dead patron's protection.");
            Check(state.Has("jerribeth.collection") == knowledge, "Jerribeth Xanthir topic ignores actual knowledge.");
            Check(!state.Has("jerribeth.condemned_wintersun") || knowledge, "Jerribeth debate invents knowledge of Wintersun.");
            string[] Endings() => story.Scenes.Where(s => s.Relationship == "jerribeth" && s.Owner == "Epilogue" && Rules.Available(story, s, state)).Select(s => s.Id).ToArray();
            Check(Endings().Single() == "jerribeth.ending_together", "Jerribeth ordinary ending conflicts.");
            state.Flags.Add("ascended");
            Check(Endings().Single() == "jerribeth.ending_ascended", "Jerribeth ascended ending conflicts.");
            state.Flags.Add("jerribeth.closed");
            Check(Endings().Single() == "jerribeth.ending_apart", "Jerribeth separation ending conflicts.");
            state.Flags.Add("jerribeth.unavailable");
            Check(Endings().Length == 0, "Jerribeth death is silently treated as living correspondence.");
        }
    }

    private static void CheckSeelahOpening()
    {
        var boots = story.Scenes.Single(s => s.Id == "seelah.boots");
        var wager = story.Scenes.Single(s => s.Id == "seelah.wager");
        var promise = story.Scenes.Single(s => s.Id == "seelah.promise");
        var kept = story.Scenes.Single(s => s.Id == "seelah.kept");
        foreach (var chapter in new[] { 1, 2, 3, 5 })
        {
            var state = new Snapshot { Chapter = chapter, Hour = 1000 };
            Check(Rules.Available(story, boots, state), "Seelah opening unavailable in supported chapter " + chapter);
            state = Complete(boots, state);
            Check(!Rules.Available(story, wager, state), "Second Seelah meeting starts immediately.");
            state.Hour += 24;
            Check(Rules.Available(story, wager, state), "Second Seelah meeting cannot start after a day.");
            state = Complete(wager, state);
            state.Chapter = Math.Max(2, chapter);
            state.Hour += 24;
            Check(Rules.Available(story, promise, state), "Seelah invitation unavailable after prerequisites.");
            var outcomes = Walk(promise, state);
            var postponed = outcomes.Single(s => s.Has("seelah.rescheduled"));
            Check(!postponed.Has("seelah.kissed") && !postponed.Has("seelah.courting"), "Postponing a meeting granted its later romantic outcome.");
            Check(!Rules.Available(story, kept, postponed), "Tomorrow's meeting happened immediately.");
            postponed.Hour += 23;
            Check(!Rules.Available(story, kept, postponed), "Deferred meeting became available too early.");
            postponed.Hour += 1;
            Check(Rules.Available(story, kept, postponed), "Deferred meeting never became available.");
            var resumed = Walk(kept, postponed);
            Check(resumed.Any(s => s.Has("seelah.kissed")) && resumed.Any(s => s.Has("seelah.courting") && !s.Has("seelah.kissed")), "Deferred meeting lost either the kiss or slower courtship branch.");
            var uninterrupted = outcomes.First(s => s.Has("seelah.courting"));
            uninterrupted.Hour += 72;
            Check(!Rules.Available(story, kept, uninterrupted), "The deferred meeting repeated an evening that was never postponed.");
        }
    }

    private static void CheckTirabadeQuarrel(bool expanded)
    {
        var scene = story.Scenes.Single(s => s.Id == "ordinary");
        var state = new Snapshot { Chapter = 3, Hour = 1000 };
        state.Flags.UnionWith(new[] { "table", "trying" });
        var outcomes = Walk(scene, state);
        var repaired = outcomes.Where(s => !s.Has("closed")).ToArray();
        Check(repaired.All(s => s.Has("kept_terms") && s.Has("ordinary")), "Quarrel repair leaves the original continuation locked.");
        Check(repaired.Any(s => !s.Has("ordinary.find_after") && !s.Has("ordinary.release_wait")), "Original repair now forces a newly added preference.");
        // The installed legacy artifact predates these two authored answers; default builds must retain both.
        if (expanded)
        {
            Check(repaired.Any(s => s.Has("ordinary.find_after")), "Commander cannot ask for a shorter later meeting.");
            Check(repaired.Any(s => s.Has("ordinary.release_wait")), "Commander cannot ask to make another plan instead of waiting.");
        }
        Check(repaired.All(s => !(s.Has("ordinary.find_after") && s.Has("ordinary.release_wait"))), "Different waiting preferences overlap.");
        Check(outcomes.Any(s => s.Has("closed") && s.Has("parted_honestly")), "Quarrel revision removes the existing separation outcome.");
    }

    private static void CheckTirabadeLocks()
    {
        var scene = story.Scenes.Single(s => s.Id == "three_locks");
        var outing = story.Scenes.Single(s => s.Id == "three_outing");
        var state = new Snapshot { Chapter = 3, Hour = 1048, Area = scene.Areas.Single() };
        state.Flags.UnionWith(new[] { "ordinary", "kept_terms", "trying", "seelah.committed", "konomi.committed" });
        state.Times["ordinary"] = 1000;
        state.Times["kept_terms"] = 1000;
        Check(Rules.Available(story, scene, state), "Shared lock lesson cannot follow the repaired evening.");
        var outcomes = Walk(scene, state);
        foreach (var end in outcomes.Where(s => s.Has(scene.Id)))
        {
            Check(end.Has("three_locks.planned"), "Shared lesson has no future plan.");
            Check(end.Has("three_locks.anevia_taught") != end.Has("three_locks.irabeth_taught"), "Teaching paths overlap or lose their history.");
            Check(end.Has("three_locks.music") != end.Has("three_locks.meal"), "Shared lesson loses its outing choice.");
            Check(end.Has("seelah.committed") && end.Has("konomi.committed"), "Shared lesson changes another romance.");
            Check(!Rules.Available(story, outing, end), "Shared outing skips its scheduling delay.");
            end.Hour += 48;
            Check(Rules.Available(story, outing, end), "Shared outing cannot follow its recorded plan.");
            foreach (var evening in Walk(outing, end))
            {
                if (!evening.Has(outing.Id))
                {
                    Check(!evening.Has("three_outing.kept"), "Postponed outing records an evening together.");
                    continue;
                }
                Check(evening.Has("three_outing.kept"), "Shared outing has no complete ending.");
                var heardMusic = evening.Has("three_outing.beth_dance") || evening.Has("three_outing.anevia_dance") || evening.Has("three_outing.listened");
                var ateMeal = evening.Has("three_outing.sweets_first") || evening.Has("three_outing.chosen_for_beth");
                Check(heardMusic == end.Has("three_locks.music") && ateMeal == end.Has("three_locks.meal"), "Outing changes the agreed activity.");
                Check(evening.Has("three_outing.long_walk") != evening.Has("three_outing.home"), "Outing loses its return choice.");
                Check(!evening.Has("three_outing.kissed") || evening.Has("three_outing.home"), "Optional kiss occurs on an unrelated ending.");
                Check(evening.Has("seelah.committed") && evening.Has("konomi.committed") && !evening.Has("closed"), "Shared outing alters other commitments or closes the relationship.");
            }
        }
        Check(outcomes.Where(s => !s.Has(scene.Id)).All(s => !s.Has("three_locks.planned")), "Postponing the lesson records an unseen outing plan.");
        foreach (var lost in new[] { "anevia_dead", "irabeth_dead", "anevia_gone", "irabeth_gone", "closed" })
        {
            var unavailable = Copy(state);
            unavailable.Flags.Add(lost);
            Check(!Rules.Available(story, scene, unavailable), "Lock lesson invents an available partner: " + lost);
        }
        state.Chapter = 4;
        Check(!Rules.Available(story, scene, state), "Drezen lock lesson appears during the Abyss chapter.");
        state.Chapter = 5;
        Check(Rules.Available(story, scene, state), "Lock lesson unavailable after both wives return.");
        foreach (var away in new[] { "irabeth_away", "anevia_away" })
        {
            var absent = Copy(state);
            absent.Flags.Add(away);
            Check(!Rules.Available(story, scene, absent), "Lock lesson ignores an absent wife: " + away);
        }
    }

    private static void CheckSeelahLetters()
    {
        var incident = story.Scenes.Single(s => s.Id == "seelah.letter");
        var aftermath = story.Scenes.Single(s => s.Id == "seelah.letter_after");
        var followup = story.Scenes.Single(s => s.Id == "seelah.letter_work");
        var initial = new Snapshot { Chapter = 4, Hour = 1024, Area = incident.Areas.Single() };
        initial.Flags.UnionWith(new[] { "seelah.abyss_together", "seelah.courting", "konomi.committed", "jerribeth.committed" });
        initial.Times["seelah.abyss_together"] = 1000;
        Check(Rules.Available(story, incident, initial), "Seelah city incident cannot follow her Nexus conversation.");
        Check(!Rules.Available(story, aftermath, initial), "Seelah remembers a letter incident that has not happened.");
        foreach (var result in Walk(incident, initial))
        {
            if (!result.Has(incident.Id))
            {
                Check(!result.Has("seelah.letter_unsettled"), "Declining the city trip records an unseen incident.");
                continue;
            }
            Check(result.Has("seelah.letter_public") != result.Has("seelah.letter_burned"), "Letter outcomes overlap or disappear.");
            Check(!Rules.Available(story, aftermath, result), "Seelah's next-day discussion happens immediately.");
            result.Hour += 24;
            Check(Rules.Available(story, aftermath, result), "Letter aftermath unavailable after its waiting period.");
            foreach (var end in Walk(aftermath, result))
            {
                Check(end.Has("seelah.letter_discussed") && !end.Has("seelah.closed"), "Disagreement closes or stalls Seelah's relationship.");
                Check(end.Has("seelah.check_person") == end.Has("seelah.letter_public"), "Public outcome loses its specific response.");
                Check(end.Has("seelah.check_signal") == end.Has("seelah.letter_burned"), "Distraction outcome loses its specific response.");
                Check(end.Has("konomi.committed") && end.Has("jerribeth.committed"), "Seelah's disagreement changes another romance.");
                Check(!Rules.Available(story, followup, end), "Copyist follow-up skips its waiting period.");
                end.Hour += 24;
                Check(Rules.Available(story, followup, end), "Copyist follow-up cannot be reached from the discussion.");
                var visits = Walk(followup, end);
                var kept = visits.Where(s => s.Has(followup.Id)).ToArray();
                Check(kept.Length > 0 && kept.All(s => s.Has("seelah.copyist_followed")), "Copyist visit has no complete outcome.");
                Check(kept.Any(s => s.Has("seelah.stopped_herself")), "Seelah cannot respond independently in the copyist follow-up.");
                Check(kept.Any(s => s.Has("seelah.signal_used")) == end.Has("seelah.check_signal"), "Wrist signal payoff does not match the prior agreement.");
                Check(kept.Any(s => s.Has("seelah.person_seen")) == end.Has("seelah.check_person"), "Attention payoff does not match the prior agreement.");
                Check(visits.Where(s => !s.Has(followup.Id)).All(s => !s.Has("seelah.copyist_followed")), "Declined follow-up records a visit.");
            }
            result.Chapter = 5;
            Check(!Rules.Available(story, aftermath, result), "Abyss letter scene spills into chapter five.");
        }
        foreach (var absent in new[] { "seelah_dead", "seelah_gone", "inhuman" })
        {
            var state = Copy(initial);
            state.Flags.Add(absent);
            Check(!Rules.Available(story, incident, state), "City incident invents suitable Seelah contact: " + absent);
        }
    }

    private static void CheckSeelahContinuation()
    {
        var state = new Snapshot { Chapter = 3, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
        foreach (var id in new[] { "seelah.boots", "seelah.wager", "seelah.promise" })
        {
            var scene = story.Scenes.Single(s => s.Id == id);
            Check(Rules.Available(story, scene, state), "Seelah timing setup cannot reach " + id);
            state = Walk(scene, state).First(s => s.Has(scene.Id) && (id != "seelah.promise" || s.Has("seelah.courting")));
            if (id != "seelah.promise") state.Hour += 24;
        }
        var door = story.Scenes.Single(s => s.Id == "seelah.door");
        Check(!Rules.Available(story, door, state), "Seelah private invitation bypasses its delay after the courtship choice.");
        state.Hour += 24;
        Check(Rules.Available(story, door, state), "Seelah private invitation does not unlock after a day.");

        foreach (int start in new[] { 3, 5 })
        foreach (string mythic in new[] { "angel", "azata", "aeon", "demon", "devil", "dragon", "legend", "trickster", "true_lich", "swarm" })
        {
            state = new Snapshot { Chapter = start, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.Add(mythic);
            if (mythic == "true_lich" || mythic == "swarm") state.Flags.Add("inhuman");
            // This supplies an available Seelah contact; physical restoration is not simulated.
            for (int chapter = start; chapter <= 5; chapter++)
            {
                state.Chapter = chapter;
                state.Area = chapter == 4 ? "7847c3e3537104f4694167af0b9fcd0e" : "2570015799edf594daf2f076f2f975d8";
                for (int attempt = 0; attempt < story.Scenes.Count; attempt++)
                {
                    state.Hour += 48;
                    var next = story.Scenes.FirstOrDefault(s => s.Relationship == "seelah" && (!s.Optional || s.Id == "seelah.watch") && !s.Owner.EndsWith("Epilogue") && Rules.Available(story, s, state));
                    if (next == null) break;
                    state = Walk(next, state).First(s => s.Has(next.Id) && !s.Has("seelah.closed"));
                }
            }
            Check(state.Has("seelah.farewell_kept"), "Seelah continuation cannot reach farewell: " + start + "/" + mythic);
            Check(state.Has("seelah.changed_beginning") == state.Has("inhuman"), "Seelah transformed opening selection is wrong.");
            Check(!state.Has("inhuman") || !state.Has("seelah.private_night") && !state.Has("seelah.kissed"), "Transformed Seelah progression grants physical intimacy.");
            Check(state.Has("seelah.abyss_together") == (start == 3 && !state.Has("inhuman")), "Seelah Abyss meeting is wrong for the start chapter.");
            var aftermath = story.Scenes.Single(s => s.Id == "seelah.souls");
            Check(!Rules.Available(story, aftermath, state), "Seelah reports returned souls before quest completion.");
            string Ending() => story.Scenes.Single(s => s.Relationship == "seelah" && s.Owner == "Epilogue" && Rules.Available(story, s, state)).Id;
            Check(Ending() == (state.Has("inhuman") ? "seelah.ending_changed" : "seelah.ending_unfinished_work"), "Seelah ending invents completed personal quest.");
            state.Flags.Add("seelah.souls_returned");
            Check(Rules.Available(story, aftermath, state), "Seelah soul-rescue aftermath remains blocked after quest completion.");
            var alive = Walk(aftermath, state);
            Check(alive.All(s => s.Has("seelah.aftercare")), "Seelah living-Elan aftermath has no conclusion.");
            state.Flags.Add("seelah.elan_dead");
            Check(Walk(aftermath, state).All(s => s.Has("seelah.aftercare")), "Seelah dead-Elan aftermath has no conclusion.");
            Check(Ending() == (state.Has("inhuman") ? "seelah.ending_changed" : "seelah.ending_together"), "Seelah quest-complete ending is wrong.");
            state.Flags.Add("seelah.ending_moderate");
            Check(Ending() == (state.Has("inhuman") ? "seelah.ending_changed" : "seelah.ending_unsettled"), "Seelah relationship erases the moderate ending.");
            state.Flags.Add("seelah.ending_bad");
            Check(Ending() == (state.Has("inhuman") ? "seelah.ending_changed" : "seelah.ending_grieving"), "Seelah completed quest erases the bad ending.");
            state.Flags.Add("ascended");
            Check(Ending() == "seelah.ending_ascended", "Seelah ascension conflicts with another ending.");
            state.Flags.Add("seelah.closed");
            Check(Ending() == "seelah.ending_apart", "Seelah separation conflicts with another ending.");
        }
    }
}
