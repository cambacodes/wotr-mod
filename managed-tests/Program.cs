using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;
using System.Text;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Quests;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.Localization;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Tirabade;
using UnityModManagerNet;

internal static class Program
{
    private static int profiledChecks;
    private static double profiledSeconds;
    private static readonly List<object> suiteTimings = new List<object>();
    private static void RunSuite(string name, Action run)
    {
        int before = checks;
        var timer = System.Diagnostics.Stopwatch.StartNew();
        try { run(); }
        finally
        {
            timer.Stop();
            profiledChecks += checks - before;
            profiledSeconds += timer.Elapsed.TotalSeconds;
            suiteTimings.Add(new { suite = name, seconds = timer.Elapsed.TotalSeconds, assertions = checks - before });
            string? output = Environment.GetEnvironmentVariable("RRT_MANAGED_TIMINGS");
            if (!string.IsNullOrEmpty(output)) File.WriteAllText(output, JsonConvert.SerializeObject(suiteTimings));
        }
    }
    private static int checks;
    private const BindingFlags PrivateStatic = BindingFlags.NonPublic | BindingFlags.Static;

    private static void Check(bool condition, string message)
    {
        checks++;
        if (!condition) throw new InvalidOperationException(message);
    }

    private static BlueprintGuid Id(string name)
    {
        using (var sha = SHA256.Create())
            return BlueprintGuid.Parse(string.Concat(sha.ComputeHash(Encoding.UTF8.GetBytes("RanRomance.Tirabade.v1/" + name)).Take(16).Select(b => b.ToString("x2"))));
    }

    private static T Reference<T>(string guid) where T : BlueprintReferenceBase, new()
    {
        var reference = new T();
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!
            .SetValue(reference, BlueprintGuid.Parse(guid));
        return reference;
    }

    private static T Seed<T>(string guid) where T : SimpleBlueprint, new()
    {
        var id = BlueprintGuid.Parse(guid);
        var prior = ResourcesLibrary.TryGetBlueprint(id);
        if (prior != null) return (T)prior;
        var blueprint = new T { AssetGuid = id, name = "NativeFixture_" + guid };
        ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(id, blueprint);
        return blueprint;
    }

    private static Dictionary<string, JObject> ReadNative(string path, IEnumerable<string> ids)
    {
        string script = Path.Combine(Bootstrap.RepositoryRoot, "managed-tests", "read-native.py");
        var start = new System.Diagnostics.ProcessStartInfo(Environment.GetEnvironmentVariable("RRT_PYTHON") ?? "python")
        {
            Arguments = "\"" + script + "\" \"" + path + "\"",
            UseShellExecute = false, CreateNoWindow = true, RedirectStandardInput = true, RedirectStandardOutput = true
        };
        using (var process = System.Diagnostics.Process.Start(start)!)
        {
            process.StandardInput.Write(JsonConvert.SerializeObject(ids.Distinct()));
            process.StandardInput.Close();
            string output = process.StandardOutput.ReadToEnd();
            process.WaitForExit();
            Check(process.ExitCode == 0, "Native blueprint extraction failed");
            return JsonConvert.DeserializeObject<Dictionary<string, JObject>>(output)!;
        }
    }

    private static string[] NativeReferences(JObject data, string field) =>
        ((JArray?)data[field] ?? new JArray()).Select(value => ((string)value!).Replace("!bp_", "")).ToArray();

    private static void SeedNativeFields(SimpleBlueprint target, JObject data, params string[] names)
    {
        foreach (string name in names)
        {
            var field = target.GetType().GetField(name)!;
            field.SetValue(target, data[name]!.ToObject(field.FieldType));
        }
    }

    private static string Hash(string path)
    {
        using (var sha = SHA256.Create())
        using (var file = File.OpenRead(path))
            return BitConverter.ToString(sha.ComputeHash(file)).Replace("-", "");
    }

    [MethodImpl(MethodImplOptions.NoInlining)]
    public static int Run(string game, string storyPath, string modDirectory)
    {
        var timer = System.Diagnostics.Stopwatch.StartNew();
        try { return RunConstruction(game, storyPath, modDirectory); }
        finally
        {
            string? output = Environment.GetEnvironmentVariable("RRT_MANAGED_TIMINGS");
            if (!string.IsNullOrEmpty(output))
            {
                suiteTimings.Add(new { suite = "ManagedConstructionAndNativeInline", seconds = timer.Elapsed.TotalSeconds - profiledSeconds,
                    assertions = checks - profiledChecks });
                File.WriteAllText(output, JsonConvert.SerializeObject(suiteTimings));
            }
        }
    }

    private static int RunConstruction(string game, string storyPath, string modDirectory)
    {
        var story = JsonConvert.DeserializeObject<Story>(File.ReadAllText(storyPath))!;
        Rules.Validate(story);
        RunSuite("TerendelevDeliveryBlueprintTests", () => TerendelevDeliveryBlueprintTests.Run(Check));
        RunSuite("NativeContactStorageTests", () => NativeContactStorageTests.Run(Check));
        RunSuite("JerribethRecoveryObservationTests", () => JerribethRecoveryObservationTests.Run(Check));
        RunSuite("TirabadeRecoveryObservationTests", () => TirabadeRecoveryObservationTests.Run(Check));
        RunSuite("KonomiContactObservationTests", () => KonomiContactObservationTests.Run(Check));
        RunSuite("KonomiRecoveryTests", () => KonomiRecoveryTests.Run(Check));
        RunSuite("KonomiMeetingTests", () => KonomiMeetingTests.Run(Check));
        RunSuite("IrabethMeetingTests", () => IrabethMeetingTests.Run(Check));
        RunSuite("NurahMeetingTests", () => NurahMeetingTests.Run(Check));
        RunSuite("NurahInteractionTests", () => NurahInteractionTests.Run(Check));
        RunSuite("NurahHubTests", () => NurahHubTests.Run(story, Check));
        var savedSettings = typeof(Kingmaker.Player).GetMember("SettingsList").Single();
        Check(savedSettings.GetCustomAttributes(typeof(JsonPropertyAttribute), true).Length == 1,
            "Player checkpoint container is not included in native JSON serialization");
        var checkpoint = new RecoveryAttempt { UnitId = "checkpoint-fixture", Roster = 2,
            SceneId = "seelah.fate_life", ChoiceJson = "recorded-choice" };
        var settingsCopy = JsonConvert.DeserializeObject<Dictionary<string, object>>(JsonConvert.SerializeObject(
            new Dictionary<string, object> { ["RanRomance.Tirabade.Revival.seelah"] = JsonConvert.SerializeObject(checkpoint) }))!;
        Check(settingsCopy["RanRomance.Tirabade.Revival.seelah"] is string, "Checkpoint JSON lost its string representation");
        var restoredCheckpoint = JsonConvert.DeserializeObject<RecoveryAttempt>((string)settingsCopy["RanRomance.Tirabade.Revival.seelah"])!;
        Check(restoredCheckpoint.UnitId == checkpoint.UnitId && restoredCheckpoint.Roster == checkpoint.Roster
            && restoredCheckpoint.SceneId == checkpoint.SceneId && restoredCheckpoint.ChoiceJson == checkpoint.ChoiceJson,
            "Native Newtonsoft JSON checkpoint encoding lost recovery identity or action");
        var targetIds = story.Scenes.SelectMany(Rules.EntryTargets).Distinct().ToArray();
        var nativeReturnIds = story.Scenes.Where(s => s.NativeReturnCue != null).Select(s => s.NativeReturnCue!).Distinct().ToArray();
        // E5 native continuations (c(native_next=...)) are real cues of the same dialog; seed them as the game would load them.
        var nativeNextIds = story.Scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Select(c => c.NativeNext).OfType<string>()
            .Distinct().Except(nativeReturnIds).Except(story.SeenCues.Values.SelectMany(ids => ids)).ToArray();
        var sequenceIds = new[] { "ed4baeaf69394754902344f0598d7e5a", "ced82f299d246f448b48afa0b630dd70" };
        // E12b anchors are native units the game loads like any other; a presence whose anchor does not resolve is skipped.
        var unitIds = story.Revivals.Values.Select(r => r.Unit).Concat(story.Scenes.Where(s => s.ContactUnit != null).SelectMany(s => new[] { s.ContactUnit! }.Concat(s.AdditionalContactUnits)))
            .Concat(story.Presences.Values.Where(p => p.At?.NearUnit != null).Select(p => p.At!.NearUnit!))
            .Concat(story.Presences.Values.Select(p => p.Unit))
            // E14f speaker units: the game resolves them from the archive like any unit, so seed every node's SpeakerUnit.
            .Concat(story.Scenes.SelectMany(s => s.Nodes).Select(n => n.SpeakerUnit).OfType<string>()).Distinct().ToArray();
        var nurahNativeBindings = NurahMeetingTests.NativeBlueprintBindings();
        var native = ReadNative(Path.Combine(game, "blueprints.zip"), targetIds.Concat(nativeReturnIds).Concat(nativeNextIds).Concat(sequenceIds.Skip(1)).Concat(story.Etudes.Values).Concat(story.CompletedEtudes.Values).Concat(story.SelectedAnswers.Values).Concat(story.StartedDialogs.Values).Concat(story.CompletedQuests.Values).Concat(story.SeenCues.Values.SelectMany(ids => ids)).Concat(unitIds).Concat(nurahNativeBindings.Keys).Concat(ChoiceExtensionManagedTests.NativeIds).Concat(NativeReaderManagedTests.NativeIds(story)).Concat(PresenceManagedTests.NativeIds(story)).Concat(NativeEpilogueManagedTests.NativeIds).Concat(ContinueBeforeManagedTests.NativeIds).Concat(SpeakerManagedTests.NativeIds).Concat(NativeEpilogueEditManagedTests.NativeIds).Concat(NativeGateManagedTests.NativeIds).Concat(NativeQ3Recovery.NativeIds).Concat(ReturnToListManagedTests.NativeIds).Concat(WenduagEchoManagedTests.NativeIds).Concat(story.RemovableItems).Concat(story.PortraitFallbacks.Values.Where(v => v.Length == 32)).Distinct());
        // SEE-01: the retained finally-dead Seelah reaches the Trickster pickpocket through revive.seelah.available.
        if (story.Scenes.Any(s => s.Id == "seelah.trickster.dead.pickpocket"))
            RunSuite("SeelahRecoveryTests", () => SeelahRecoveryTests.Run(story, native["26ae0f50130942b4bb8dfe658e77b1c6"], Check));
        // Book-picture fallbacks: every native target is a BlueprintPortrait in the archive, and every alias names another key.
        foreach (var fallback in story.PortraitFallbacks)
            Check(fallback.Value.Length == 32
                ? ((string)native[fallback.Value]["$type"]!).EndsWith(", BlueprintPortrait", StringComparison.Ordinal)
                : fallback.Value.Length > 0 && fallback.Value != fallback.Key,
                "Portrait fallback is not a native BlueprintPortrait or a key alias: " + fallback.Key);
        foreach (var binding in nurahNativeBindings)
            Check(((string)native[binding.Key]["$type"]!).EndsWith(", " + binding.Value, StringComparison.Ordinal),
                "Nurah native binding has the wrong archive type: " + binding.Key);
        // RanRomance creates the first sequence; it is absent from the base-game archive.
        // Sentinels verify preservation without pretending to execute the parent mod.
        native[sequenceIds[0]] = new JObject
        {
            ["$type"] = "fixture, BlueprintCueSequence",
            ["Cues"] = new JArray("!bp_" + Id("fixture.parent.first"), "!bp_" + Id("fixture.parent.last"))
        };
        var answerLists = new Dictionary<string, BlueprintAnswersList>();
        var originalAnswers = new Dictionary<string, BlueprintAnswerBaseReference[]>();
        foreach (string guid in targetIds)
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintAnswersList", StringComparison.Ordinal), "Wrong native target type: " + guid);
            var list = Seed<BlueprintAnswersList>(guid);
            if (nativeReturnIds.Any(id => NativeReferences(native[id], "Answers").Contains(guid)))
                SeedNativeFields(list, native[guid], "ShowOnce", "Conditions", "MythicRequirement", "AlignmentRequirement");
            foreach (string answer in NativeReferences(native[guid], "Answers")) list.Answers.Add(Reference<BlueprintAnswerBaseReference>(answer));
            answerLists.Add(guid, list);
            originalAnswers.Add(guid, list.Answers.ToArray());
        }
        var sequences = new Dictionary<string, BlueprintCueSequence>();
        var originalCues = new Dictionary<string, BlueprintCueBaseReference[]>();
        // E14a: a page that targets PlayerFinalChoice needs the native sequence (with its members) loaded like the game does.
        var e14aSequences = story.Scenes.Any(s => s.EpilogueSequence != null) ? new[] { Rules.PlayerFinalChoice } : Array.Empty<string>();
        foreach (string guid in sequenceIds.Concat(e14aSequences))
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintCueSequence", StringComparison.Ordinal), "Wrong native sequence type: " + guid);
            var sequence = Seed<BlueprintCueSequence>(guid);
            foreach (string cue in NativeReferences(native[guid], "Cues")) sequence.Cues.Add(Reference<BlueprintCueBaseReference>(cue));
            sequences.Add(guid, sequence);
            originalCues.Add(guid, sequence.Cues.ToArray());
        }
        // NM1: the E14d native epilogue edits the story ships load their reviewed cue, page and sequence as the game does. The
        // host cannot run Owlcat's element reporting, so each cue's checker is the empty AND (NativeEpilogueEditManagedTests).
        // E14d extension: suppressed cues (NativeEpilogueSuppressions) load the same way.
        foreach (var target in story.NativeEpilogueEdits.Where(p => string.IsNullOrEmpty(p.Value.Parent)).Select(p => (Cue: p.Key, p.Value.Page, p.Value.Sequence))
            .Concat(story.NativeEpilogueSuppressions.Select(p => (Cue: p.Key, p.Value.Page, p.Value.Sequence))))
        {
            var editSequence = string.IsNullOrEmpty(target.Sequence) ? null : Seed<BlueprintCueSequence>(target.Sequence);
            // CueSequence_Special also holds the parent's native pair page, which ParentEndingIntegrationTests seeds as a fixture;
            // there only the edit's own page is loaded, so that page stays exactly once in the sequence.
            if (target.Sequence == NativeEpilogueEdit.Special)
            {
                if (!editSequence!.Cues.Any(r => r.Guid == BlueprintGuid.Parse(target.Page)))
                    editSequence.Cues.Add(Reference<BlueprintCueBaseReference>(target.Page));
            }
            else if (editSequence != null && editSequence.Cues.Count == 0)
                foreach (string cue in NativeReferences(native[target.Sequence], "Cues")) editSequence.Cues.Add(Reference<BlueprintCueBaseReference>(cue));
            var editPage = Seed<BlueprintBookPage>(target.Page);
            if (editPage.Cues.Count == 0)
                foreach (string cue in NativeReferences(native[target.Page], "Cues")) editPage.Cues.Add(Reference<BlueprintCueBaseReference>(cue));
            var editCue = Seed<BlueprintCue>(target.Cue);
            editCue.Conditions = new Kingmaker.ElementsSystem.ConditionsChecker { Operation = Kingmaker.ElementsSystem.Operation.And, Conditions = Array.Empty<Kingmaker.ElementsSystem.Condition>() };
            // The archive's reviewed OnShow image action, continuation and text key (own or shared), as the game loads them.
            NativeEpilogueEditManagedTests.LoadArchiveShape(editCue, native[target.Cue], Check);
        }
        // E14i: a common-dialog edit loads its dialog (FirstCue), its parent cue (Continue as the archive has it) and the cue.
        foreach (var pair in story.NativeEpilogueEdits.Where(p => !string.IsNullOrEmpty(p.Value.Parent)))
        {
            var dialog = Seed<BlueprintDialog>(pair.Value.Dialog);
            if (dialog.FirstCue == null || dialog.FirstCue.Cues.Count == 0)
                dialog.FirstCue = new Kingmaker.DialogSystem.CueSelection { Cues = NativeReferences((JObject)native[pair.Value.Dialog]["FirstCue"]!, "Cues")
                    .Select(Reference<BlueprintCueBaseReference>).ToList() };
            string parentType = ((string)native[pair.Value.Parent]["$type"]!).Split(new[] { ", " }, StringSplitOptions.None).Last();
            if (parentType == "BlueprintCue")
            {
                var parent = Seed<BlueprintCue>(pair.Value.Parent);
                if (parent.Continue == null || parent.Continue.Cues.Count == 0)
                {
                    parent.Conditions = new Kingmaker.ElementsSystem.ConditionsChecker { Operation = Kingmaker.ElementsSystem.Operation.And, Conditions = Array.Empty<Kingmaker.ElementsSystem.Condition>() };
                    NativeEpilogueEditManagedTests.LoadArchiveShape(parent, native[pair.Value.Parent], Check);
                }
            }
            else if (parentType == "BlueprintAnswer")   // E14i: an answer's NextCue lists the cue (Devarra's DragonEggs/Answer_0004)
            {
                var answer = Seed<BlueprintAnswer>(pair.Value.Parent);
                if (answer.NextCue == null || answer.NextCue.Cues.Count == 0)
                    answer.NextCue = new Kingmaker.DialogSystem.CueSelection { Cues = NativeReferences((JObject)native[pair.Value.Parent]["NextCue"]!, "Cues")
                        .Select(Reference<BlueprintCueBaseReference>).ToList() };
            }
            else if (parentType == "BlueprintCueSequence")   // eng7-f6b: a text-only edit whose parent is a cue sequence (Cues lists the cue)
            {
                var parentSequence = Seed<Kingmaker.DialogSystem.Blueprints.BlueprintCueSequence>(pair.Value.Parent);
                if (parentSequence.Cues.Count == 0)
                    foreach (string cue in NativeReferences(native[pair.Value.Parent], "Cues")) parentSequence.Cues.Add(Reference<BlueprintCueBaseReference>(cue));
            }
            else if (parentType == "BlueprintSequenceExit")   // eng7-f6b: a text-only edit whose parent is a sequence exit (Continue lists the cue)
            {
                var exit = Seed<Kingmaker.DialogSystem.Blueprints.BlueprintSequenceExit>(pair.Value.Parent);
                if (exit.Continue == null || exit.Continue.Cues.Count == 0)
                    exit.Continue = new Kingmaker.DialogSystem.CueSelection { Cues = NativeReferences((JObject)native[pair.Value.Parent]["Continue"]!, "Cues")
                        .Select(Reference<BlueprintCueBaseReference>).ToList() };
            }
            else Check(parentType == "BlueprintDialog" && pair.Value.Parent == pair.Value.Dialog, "Unexpected E14i parent type: " + parentType);
            // E14i: further parents of a mid-dialog cue (Kiana's JewelerFinal/Cue_0051: Cue_0049, Cue_0050) load like the parent.
            foreach (string also in NativeEpilogueEdit.AlsoParentsOf(pair.Key))
            {
                string alsoType = ((string)native[also]["$type"]!).Split(new[] { ", " }, StringSplitOptions.None).Last();
                if (alsoType == "BlueprintSequenceExit")   // eng7-f6b: a further parent that is a sequence exit (Continue lists the cue)
                {
                    var alsoExit = Seed<Kingmaker.DialogSystem.Blueprints.BlueprintSequenceExit>(also);
                    if (alsoExit.Continue == null || alsoExit.Continue.Cues.Count == 0)
                        alsoExit.Continue = new Kingmaker.DialogSystem.CueSelection { Cues = NativeReferences((JObject)native[also]["Continue"]!, "Cues")
                            .Select(Reference<BlueprintCueBaseReference>).ToList() };
                    continue;
                }
                if (alsoType == "BlueprintCueSequence")
                {
                    var alsoSequence = Seed<Kingmaker.DialogSystem.Blueprints.BlueprintCueSequence>(also);
                    if (alsoSequence.Cues.Count == 0)
                        foreach (string cue in NativeReferences(native[also], "Cues")) alsoSequence.Cues.Add(Reference<BlueprintCueBaseReference>(cue));
                    continue;
                }
                var alsoParent = Seed<BlueprintCue>(also);
                if (alsoParent.Continue == null || alsoParent.Continue.Cues.Count == 0)
                {
                    alsoParent.Conditions = new Kingmaker.ElementsSystem.ConditionsChecker { Operation = Kingmaker.ElementsSystem.Operation.And, Conditions = Array.Empty<Kingmaker.ElementsSystem.Condition>() };
                    NativeEpilogueEditManagedTests.LoadArchiveShape(alsoParent, native[also], Check);
                }
            }
            var editCue = Seed<BlueprintCue>(pair.Key);
            editCue.Conditions = new Kingmaker.ElementsSystem.ConditionsChecker { Operation = Kingmaker.ElementsSystem.Operation.And, Conditions = Array.Empty<Kingmaker.ElementsSystem.Condition>() };
            NativeEpilogueEditManagedTests.LoadArchiveShape(editCue, native[pair.Key], Check);
        }
        foreach (string guid in story.Etudes.Values.Concat(story.CompletedEtudes.Values).Distinct())
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintEtude", StringComparison.Ordinal), "Wrong native etude type: " + guid);
            Seed<BlueprintEtude>(guid);
        }
        // Native unlockable flags a scene reads (e.g. KyadoDead) must exist before Build, like the etudes above.
        foreach (string guid in story.UnlockableFlags.Values.Distinct())
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintUnlockableFlag", StringComparison.Ordinal), "Wrong native flag type: " + guid);
            Seed<BlueprintUnlockableFlag>(guid);
        }
        // E10 quest-objective bindings (a native objective a scene reads) must resolve before Build, like the flags above.
        foreach (var value in story.QuestObjectives.Values)
        {
            Check(((string)native[value[0]]["$type"]!).EndsWith(", BlueprintQuestObjective", StringComparison.Ordinal), "Wrong native objective type: " + value[0]);
            Seed<Kingmaker.Blueprints.Quests.BlueprintQuestObjective>(value[0]);
        }
        // E10 main-character facts (a chosen mythic trick) must resolve before Build, or the scenes that read them degrade.
        foreach (string guid in story.MainCharacterFacts.Values.Distinct())
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintFeature", StringComparison.Ordinal), "Wrong native fact type: " + guid);
            Seed<Kingmaker.Blueprints.Classes.BlueprintFeature>(guid);
        }
        // E14e: a story line inserted ahead of a native cue needs its native parents (Continue First) loaded like the game does.
        var continueParents = story.Scenes.Where(s => s.ContinueBefore != null).SelectMany(s => s.ContinueBefore!.Parents).Distinct().ToArray();
        foreach (string guid in continueParents)
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintCue", StringComparison.Ordinal), "Wrong native continue parent type: " + guid);
            var parent = Seed<BlueprintCue>(guid);
            parent.Continue = new Kingmaker.DialogSystem.CueSelection { Strategy = (Kingmaker.DialogSystem.Strategy)Enum.Parse(typeof(Kingmaker.DialogSystem.Strategy), (string)native[guid]["Continue"]!["Strategy"]!),
                Cues = NativeReferences((JObject)native[guid]["Continue"]!, "Cues").Select(Reference<BlueprintCueBaseReference>).ToList() };
        }
        foreach (string guid in unitIds)
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintUnit", StringComparison.Ordinal), "Wrong native unit type: " + guid);
            Seed<BlueprintUnit>(guid);
        }
        LocalizationManager.CurrentPack = new LocalizationPack();
        foreach (string guid in story.SeenCues.Values.SelectMany(ids => ids).Distinct())
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintCue", StringComparison.Ordinal), "Wrong native seen-cue type: " + guid);
            Seed<BlueprintCue>(guid);
        }
        foreach (string guid in nativeNextIds)
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintCue", StringComparison.Ordinal), "Wrong native continuation type: " + guid);
            Seed<BlueprintCue>(guid);
        }
        foreach (string guid in nativeReturnIds)
        {
            var data = native[guid];
            Check(((string)data["$type"]!).EndsWith(", BlueprintCue", StringComparison.Ordinal), "Wrong native return-cue type: " + guid);
            // Preserve archive fields used by BuildScene's safety guard and native speaker selection.
            // This graph fixture does not execute Unity's camera or dialogue controller.
            var cue = Seed<BlueprintCue>(guid);
            cue.ShowOnce = (bool)data["ShowOnce"]!;
            cue.ShowOnceCurrentDialog = (bool)data["ShowOnceCurrentDialog"]!;
            cue.Conditions = data["Conditions"]!.ToObject<Kingmaker.ElementsSystem.ConditionsChecker>()!;
            cue.OnShow = data["OnShow"]!.ToObject<Kingmaker.ElementsSystem.ActionList>()!;
            cue.OnStop = data["OnStop"]!.ToObject<Kingmaker.ElementsSystem.ActionList>()!;
            cue.Speaker = data["Speaker"]!.ToObject<Kingmaker.DialogSystem.DialogSpeaker>()!;
            SeedNativeFields(cue, data, "Experience", "AlignmentShift");
            cue.Continue = data["Continue"]!.ToObject<Kingmaker.DialogSystem.CueSelection>()!;
            cue.Answers.Clear();
            cue.Answers.AddRange(NativeReferences(data, "Answers").Select(Reference<BlueprintAnswerBaseReference>));
        }
        // E11: a whitelisted removable item must resolve before Build, or the relationships that remove it degrade.
        foreach (string guid in story.RemovableItems.Distinct())
        {
            Check(((string)native[guid]["$type"]!).Split(new[] { ", " }, StringSplitOptions.None).Last().StartsWith("BlueprintItem", StringComparison.Ordinal),
                "Removable item is not a BlueprintItem: " + guid);
            Seed<Kingmaker.Blueprints.Items.BlueprintItem>(guid);
        }
        // E10: an InventoryItems binding resolves from the archive like any item (the game loads it), so seed it before Build,
        // or the relationships that read it degrade. Removable items are seeded above.
        foreach (string guid in story.InventoryItems.Values.Concat(story.PartyItems.Values).Distinct().Except(story.RemovableItems))
        {
            Check(((string)native[guid]["$type"]!).Split(new[] { ", " }, StringSplitOptions.None).Last().StartsWith("BlueprintItem", StringComparison.Ordinal),
                "Inventory item binding is not a BlueprintItem: " + guid);
            Seed<Kingmaker.Blueprints.Items.BlueprintItem>(guid);
        }
        // E12 presence areas outside the capital are native areas the game loads; seed them like the capital fixture.
        foreach (string guid in story.Presences.Values.Select(p => p.Area).Distinct())
        {
            Check(((string)native[guid]["$type"]!).Split(new[] { ", " }, StringSplitOptions.None).Last().StartsWith("BlueprintArea", StringComparison.Ordinal),
                "Presence area is not a BlueprintArea: " + guid);
            Seed<Kingmaker.Blueprints.Area.BlueprintArea>(guid);
        }
        foreach (string guid in story.CompletedQuests.Values.Distinct())
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintQuest", StringComparison.Ordinal), "Wrong native completed quest type: " + guid);
            Seed<BlueprintQuest>(guid);
        }
        foreach (string guid in story.SelectedAnswers.Values.Distinct())
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintAnswer", StringComparison.Ordinal), "Wrong native selected-answer type: " + guid);
            Seed<BlueprintAnswer>(guid);
        }
        foreach (string guid in story.StartedDialogs.Values.Distinct())
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintDialog", StringComparison.Ordinal), "Wrong native started-dialog type: " + guid);
            Seed<BlueprintDialog>(guid);
        }
        bool hasParentEndingRules = story.ParentEpilogueEdits.Count > 0 || story.ParentEpilogueLossRules.Count > 0;
        if (hasParentEndingRules)
        {
            string contractPath = Path.Combine(Bootstrap.RepositoryRoot,
                "managed-tests/fixtures/parent-ending-source/verified-contract.json");
            ParentEndingIntegrationTests.PrepareSourceFixtures(JObject.Parse(File.ReadAllText(contractPath)),
                ParentEndingSourceFixtures.Build(), ParentEndingSourceFixtures.PageActions());
            ParentEndingIntegrationTests.CheckPreflight(story, Check);
            foreach (var pair in sequences) originalCues[pair.Key] = pair.Value.Cues.ToArray();
        }
        BlueprintCueSequence? expandedEpilogue = null;
        BlueprintCueBaseReference[] expandedOriginal = Array.Empty<BlueprintCueBaseReference>();
        bool invalidExpandedEpilogue = Environment.GetEnvironmentVariable("RRT_TEST_EXPANDED_EPILOGUE") == "wrong-type";
        if (invalidExpandedEpilogue) Seed<BlueprintCue>("2b9424b1b93e4d0896b0958db79d2339");
        if (Environment.GetEnvironmentVariable("RRT_TEST_EXPANDED_EPILOGUE") == "1")
        {
            // The reviewed parent creates this optional sequence from the same page references.
            // Its plugin-owned caller graph is not installed and is not simulated here.
            expandedEpilogue = Seed<BlueprintCueSequence>("2b9424b1b93e4d0896b0958db79d2339");
            expandedOriginal = sequences[sequenceIds[0]].Cues.ToArray();
            expandedEpilogue.Cues.AddRange(expandedOriginal);
        }
        if (story.Scenes.Any(Rules.IsWenduagEchoHub)) WenduagEchoManagedTests.Seed(native, Check);
        var entry = new UnityModManager.ModEntry(new UnityModManager.ModInfo { Id = "ManagedBuildTests", Version = "1.0.0", ManagerVersion = "0.27.11" }, modDirectory);
        string? invalidReturnKind = Environment.GetEnvironmentVariable("RRT_TEST_NATIVE_RETURN");
        bool invalidNativeReturn = !string.IsNullOrEmpty(invalidReturnKind);
        if (invalidNativeReturn)
        {
            Check(nativeReturnIds.Length > 0, "Native return rejection test needs an inline scene.");
            var unsafeCue = Seed<BlueprintCue>(nativeReturnIds[0]);
            switch (invalidReturnKind)
            {
                case "show-once": unsafeCue.ShowOnceCurrentDialog = true; break;
                case "list-show-once": ((BlueprintAnswersList)unsafeCue.Answers.Single().Get()).ShowOnce = true; break;
                case "experience": unsafeCue.Experience = (Kingmaker.DialogSystem.DialogExperience)1; break;
                case "alignment": unsafeCue.AlignmentShift.Value = 1; break;
                case "extra-list": unsafeCue.Answers.Add(unsafeCue.Answers.Single()); break;
                default: throw new InvalidOperationException("Unknown native return rejection fixture: " + invalidReturnKind);
            }
        }
        // E18: the reviewed native gate targets, shaped like the archive, loaded before Build as the game would load them.
        NativeGateManagedTests.Seed(native, Check);
        TerendelevNativeManagedTests.Seed(native, Check); // eng7-f6d
        NativeQ3RecoveryManagedTests.Seed(native, Check);
        Type main = typeof(Tirabade.Main);
        main.GetField("entry", PrivateStatic)!.SetValue(null, entry);
        main.GetField("story", PrivateStatic)!.SetValue(null, story);
        MethodInfo build = main.GetMethod("Build", PrivateStatic)!;
        KonomiMeetingIntegrationTests.PrepareNativePlacement();
        IrabethMeetingIntegrationTests.PrepareNativePlacement();
        NurahMeetingTests.PrepareNativePlacement();
        // RRT_TEST_MISSING_ETUDE=<key> simulates a game or parent-mod update that removed a native binding.
        string? missingEtude = Environment.GetEnvironmentVariable("RRT_TEST_MISSING_ETUDE");
        if (missingEtude != null)
        {
            Check(story.Etudes.ContainsKey(missingEtude), "Unknown etude key for the missing-binding fixture: " + missingEtude);
            story.Etudes[missingEtude] = "0123456789abcdef0123456789abcdef";
        }
        build.Invoke(null, null);
        HashSet<string> Degraded() => (HashSet<string>)main.GetField("degraded", PrivateStatic)!.GetValue(null)!;
        List<string> Warnings() => (List<string>)main.GetField("warnings", PrivateStatic)!.GetValue(null)!;
        bool Initialized() => (bool)main.GetField("initialized", PrivateStatic)!.GetValue(null)!;
        if (invalidNativeReturn)
        {
            // Save-safe contract: an unsafe native return disables only its own relationship. Every blueprint a save
            // can reference is still registered, and no entry of that relationship is attached to any native list.
            var unsafeScene = story.Scenes.First(s => s.NativeReturnCue == nativeReturnIds[0]);
            Check(Initialized(), "Unsafe native return disabled the whole addon instead of its relationship.");
            Check(Degraded().SetEquals(new[] { unsafeScene.Relationship }), "Unsafe native return degraded the wrong relationships: " + string.Join(",", Degraded()));
            Check(Warnings().Any(w => w.Contains("Native audience return must reopen")), "Unsafe native return was not reported.");
            foreach (var scene in story.Scenes.Where(s => s.Relationship == unsafeScene.Relationship))
                Check(ResourcesLibrary.TryGetBlueprint(Id("flag." + scene.Id)) is BlueprintUnlockableFlag, "Degraded relationship lost a save flag: " + scene.Id);
            var degradedEntries = new HashSet<BlueprintGuid>(story.Scenes.Where(s => s.Relationship == unsafeScene.Relationship).Select(s => Id("entry." + s.Id)));
            Check(answerLists.Values.All(list => !list.Answers.Any(reference => degradedEntries.Contains(reference.Guid))), "Degraded relationship was attached to a native list.");
            Check(answerLists.All(pair => originalAnswers[pair.Key].All(pair.Value.Answers.Contains)), "Failed return preflight removed native answers.");
            var probe = new Snapshot { Chapter = unsafeScene.MinChapter, Hour = 100000 };
            probe.Flags.Add(Rules.DegradedPrefix + unsafeScene.Relationship);
            Check(!Rules.Available(story, unsafeScene, probe), "Degraded relationship remains available to the rules.");
            Console.WriteLine($"PASS: {checks} assertions; unsafe native return degraded only '{unsafeScene.Relationship}', saves stay resolvable.");
            return 0;
        }
        if (missingEtude != null)
        {
            // Runtime-derived flags, latches and data-driven composites inherit the missing input.
            var lost = new HashSet<string> { missingEtude };
            if (new[] { "irabeth_dead", "anevia_dead", "irabeth_gone", "anevia_gone", "sacrifice" }.Contains(missingEtude)) lost.Add("loss");
            if (missingEtude == "swarm" || missingEtude == "true_lich") lost.Add("inhuman");
            Rules.PropagateMissing(story, lost);
            var dependent = new HashSet<string>(story.Scenes.Where(sc => sc.Requires.Concat(sc.RequiresAny).Concat(sc.RequiresAnyGroups.SelectMany(g => g))
                    .Concat(sc.Forbids).Concat(sc.ForbidOverrides.Values).Concat(sc.Nodes.SelectMany(n => n.Choices).SelectMany(ch => ch.Requires.Concat(ch.Forbids)))
                    .Any(lost.Contains))
                .Select(sc => sc.Relationship)
                .Concat(story.Relationships.Where(r => r.Value.UnavailableFlags.Concat(r.Value.FailureFlags).Any(lost.Contains)).Select(r => r.Key)));
            Check(Initialized(), "A missing native etude disabled the whole addon.");
            Check(dependent.Count > 0, "Missing-binding fixture chose an etude no relationship uses.");
            Check(Degraded().SetEquals(dependent), "Missing etude degraded the wrong set. Expected " + string.Join(",", dependent.OrderBy(x => x))
                + " got " + string.Join(",", Degraded().OrderBy(x => x)));
            foreach (var scene in story.Scenes)
                Check(ResourcesLibrary.TryGetBlueprint(Id("flag." + scene.Id)) is BlueprintUnlockableFlag, "Save flag missing after partial integration: " + scene.Id);
            foreach (var key in story.Relationships.Keys)
                Check(ResourcesLibrary.TryGetBlueprint(Id(key == "tirabade" ? "quest" : "quest." + key)) is BlueprintQuest, "Journal quest missing after partial integration: " + key);
            // E14b: a return-to-list scene has one entry answer per list it joins.
            IEnumerable<BlueprintGuid> Entries(Tirabade.Scene sc) => sc.ReturnToList
                ? Rules.EntryTargets(sc).Select(list => Id("entry." + sc.Id + "." + list)) : new[] { Id("entry." + sc.Id) };
            var degradedEntries = new HashSet<BlueprintGuid>(story.Scenes.Where(sc => dependent.Contains(sc.Relationship)).SelectMany(Entries));
            var liveEntries = new HashSet<BlueprintGuid>(story.Scenes.Where(sc => !dependent.Contains(sc.Relationship) && Rules.EntryTargets(sc).Length > 0 && sc.NativeReturnCue == null).SelectMany(Entries));
            Check(answerLists.Values.All(list => !list.Answers.Any(r => degradedEntries.Contains(r.Guid))), "A degraded relationship was attached to a native list.");
            Check(liveEntries.All(guid => answerLists.Values.Any(list => list.Answers.Any(r => r.Guid == guid))), "An unaffected relationship lost its native entries.");
            Console.WriteLine($"PASS: {checks} assertions; missing etude '{missingEtude}' degraded only [{string.Join(", ", dependent.OrderBy(x => x))}]; "
                + $"{story.Scenes.Count} scene flags and {story.Relationships.Count} journal quests stay registered.");
            return 0;
        }
        if (invalidExpandedEpilogue)
        {
            var wrong = (BlueprintCue)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse("2b9424b1b93e4d0896b0958db79d2339"))!;
            Check(Initialized(), "Invalid optional epilogue disabled the whole addon.");
            Check(Degraded().Count == 0, "Invalid optional epilogue degraded a relationship.");
            Check(Warnings().Any(w => w.Contains("Optional parent epilogue has the wrong type")), "Invalid optional epilogue was not reported.");
            Check(sequences.All(pair => originalCues.TryGetValue(pair.Key, out var before) ? before.All(pair.Value.Cues.Contains) : true), "Invalid optional epilogue removed native sequence pages.");
            Console.WriteLine($"PASS: {checks} assertions; wrong-type optional epilogue ignored with a warning; addon initialized.");
            return 0;
        }
        Check(Degraded().Count == 0, "Blueprint construction disabled relationships: " + string.Join(",", Degraded().OrderBy(x => x)));
        RunSuite("KonomiMeetingIntegrationTests", () => KonomiMeetingIntegrationTests.Run(Check));
        RunSuite("IrabethMeetingIntegrationTests", () => IrabethMeetingIntegrationTests.Run(Check));
        RunSuite("NurahHubIntegrationTests", () => NurahHubIntegrationTests.Run(story, Check));
        Check((bool)main.GetField("initialized", PrivateStatic)!.GetValue(null)!, "Build did not initialize: " + main.GetField("error", PrivateStatic)!.GetValue(null));
        Check(main.GetField("error", PrivateStatic)!.GetValue(null) == null, "Build reported an error");
        // E14d: every shipped native epilogue edit passed its evidence check on the archive-shaped cue and attached all of its
        // variants, in order, right before the native cue; none was skipped or degraded a relationship.
        foreach (var pair in story.NativeEpilogueEdits)
        {
            var variantNames = Rules.EditVariants(pair.Value).Select((v, i) => Id(Rules.NativeEditCueName(pair.Key, pair.Value, i))).ToArray();
            // eng7-f6b: a text-only edit never touches membership; the parent lists the native cue once and no replacement cue.
            if (NativeEpilogueEdit.IsTextOnly(pair.Key))
            {
                // eng8-q8e: a book-page text edit keeps its original page membership too.
                foreach (string parentId in new[] { string.IsNullOrEmpty(pair.Value.Parent) ? pair.Value.Page : pair.Value.Parent }.Concat(NativeEpilogueEdit.AlsoParentsOf(pair.Key)))
                {
                    var parent = ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(parentId));
                    var textParent = (parent is BlueprintBookPage textPage ? textPage.Cues : NativeEpilogueEdit.TextParentCues(parent))?.Select(r => r.Guid).ToList();
                    Check(textParent != null && textParent.Count(g => g == BlueprintGuid.Parse(pair.Key)) == 1 && !textParent.Any(variantNames.Contains),
                        "E14d text-only edit changed its parent's membership: " + pair.Key + " / " + parentId);
                }
                Check(!Warnings().Any(w => w.Contains(pair.Key)), "E14d text-only edit warned or degraded: " + string.Join(" | ", Warnings().Where(w => w.Contains(pair.Key))));
                continue;
            }
            // E14i: a dialog edit's variants sit in its parent cue's Continue, right before the native cue.
            var editPageCues = (string.IsNullOrEmpty(pair.Value.Parent)
                ? ((BlueprintBookPage)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(pair.Value.Page))!).Cues
                : NativeEpilogueEdit.ParentSelection(ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(pair.Value.Parent)))!.Cues).Select(r => r.Guid).ToList();
            int nativeAt = editPageCues.IndexOf(BlueprintGuid.Parse(pair.Key));
            Check(nativeAt >= variantNames.Length && editPageCues.Skip(nativeAt - variantNames.Length).Take(variantNames.Length).SequenceEqual(variantNames),
                "E14d variants not attached in order right before their native cue: " + pair.Key);
            Check(!Warnings().Any(w => w.Contains(pair.Key)), "E14d edit warned or degraded: " + string.Join(" | ", Warnings().Where(w => w.Contains(pair.Key))));
            foreach (string also in NativeEpilogueEdit.AlsoParentsOf(pair.Key))
            {
                var alsoCues = NativeEpilogueEdit.ParentSelection(ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(also)))!.Cues.Select(r => r.Guid).ToList();
                int alsoAt = alsoCues.IndexOf(BlueprintGuid.Parse(pair.Key));
                Check(alsoAt >= variantNames.Length && alsoCues.Skip(alsoAt - variantNames.Length).Take(variantNames.Length).SequenceEqual(variantNames),
                    "E14i variants not attached right before their native cue in a further parent: " + pair.Key + " / " + also);
            }
        }
        // E14d extension: every shipped suppression passed its evidence check and guarded its native cue exactly once.
        foreach (var pair in story.NativeEpilogueSuppressions)
        {
            var suppressed = (BlueprintCue)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(pair.Key))!;
            Check(suppressed.Conditions.Conditions.Length == 1 && suppressed.Conditions.Conditions[0].GetType().Name == "Guard",
                "E14d suppression did not guard its native cue: " + pair.Key);
            Check(!Warnings().Any(w => w.Contains(pair.Key)), "E14d suppression warned: " + string.Join(" | ", Warnings().Where(w => w.Contains(pair.Key))));
        }
        foreach (var latch in story.Latches.Keys)
            Check(ResourcesLibrary.TryGetBlueprint(Id("flag." + latch)) is BlueprintUnlockableFlag
                && ResourcesLibrary.TryGetBlueprint(Id("flag.hour." + latch)) is BlueprintUnlockableFlag, "Latch flag not registered: " + latch);
        RunSuite("NativeAudienceTests", () => NativeAudienceTests.Run(story, Check));
        foreach (var scene in story.Scenes.Where(s => s.ContinueBefore != null))
        {
            var line = ResourcesLibrary.TryGetBlueprint(Id("cue." + scene.Id + ".continue"));
            foreach (string guid in scene.ContinueBefore!.Parents)
            {
                var cues = ((BlueprintCue)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(guid))!).Continue.Cues.Select(r => r.Guid).ToList();
                int at = cues.IndexOf(BlueprintGuid.Parse(scene.ContinueBefore.Cue));
                Check(line != null && at > 0 && cues[at - 1] == line.AssetGuid && cues.Count(g => g == line.AssetGuid) == 1,
                    "Continue-before line is not inserted once, right before its anchor: " + scene.Id + " in " + guid);
            }
        }
        if (hasParentEndingRules) RunSuite("ParentEndingIntegrationTests", () => ParentEndingIntegrationTests.Run(story, Check));
        RunSuite("EndingDeliveryTests", () => EndingDeliveryTests.Run(story, Id, Check));
        if (expandedEpilogue != null)
        {
            Check(expandedEpilogue.Cues.Take(expandedOriginal.Length).SequenceEqual(expandedOriginal),
                "Optional epilogue changes existing parent page references.");
            Check(expandedEpilogue.Cues.Select(reference => reference.Guid).SequenceEqual(sequences[sequenceIds[0]].Cues.Select(reference => reference.Guid)),
                "Optional epilogue omits or reorders addon endings.");
        }
        var contacts = (Dictionary<string, BlueprintUnit>)main.GetField("contactUnits", PrivateStatic)!.GetValue(null)!;
        var expectedContacts = story.Scenes.Where(s => s.ContactUnit != null)
            .SelectMany(s => new[] { s.ContactUnit! }.Concat(s.AdditionalContactUnits)).Distinct().ToArray();
        Check(new HashSet<string>(contacts.Keys).SetEquals(expectedContacts), "Build omitted or added native contact observers.");
        foreach (string guid in expectedContacts)
            Check(contacts[guid].AssetGuid == BlueprintGuid.Parse(guid), "Contact observer uses the wrong unit: " + guid);
        var readHistory = main.GetMethod("ReadDialogHistory", PrivateStatic)!;
        foreach (var binding in story.StartedDialogs)
        {
            var history = new Kingmaker.DialogSystem.State.DialogState();
            Snapshot ReadStarted()
            {
                var result = new Snapshot();
                readHistory.Invoke(null, new object[] { history, result });
                return result;
            }
            Check(!ReadStarted().Has(binding.Key), "Unstarted dialog appears in history");
            var unrelated = Seed<BlueprintDialog>(Id("fixture.unrelated.dialog").ToString());
            history.ShownDialogs.Add(unrelated);
            Check(!ReadStarted().Has(binding.Key), "Unrelated dialog satisfies started history");
            var dialog = (BlueprintDialog)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(binding.Value));
            history.ShownDialogs.Add(dialog);
            Check(ReadStarted().Has(binding.Key), "Started dialog requires an unproven completion event");
            Check(history.ShownDialogs.Count == 2 && history.ShownDialogs.Contains(unrelated)
                && history.ShownCues.Count == 0 && history.SelectedAnswers.Count == 0,
                "Reading started dialogs changes native dialog history");
            history.ShownDialogs.Remove(dialog);
            Check(!ReadStarted().Has(binding.Key), "Started dialog leaks across snapshots");
        }
        foreach (var binding in story.SelectedAnswers)
        {
            var history = new Kingmaker.DialogSystem.State.DialogState();
            Snapshot ReadHistory()
            {
                var result = new Snapshot();
                readHistory.Invoke(null, new object[] { history, result });
                return result;
            }
            Check(!ReadHistory().Has(binding.Key), "An unselected answer appears in native history");
            var unrelated = Seed<BlueprintAnswer>(Id("fixture.unrelated.answer").ToString());
            history.SelectedAnswers.Add(unrelated);
            Check(!ReadHistory().Has(binding.Key), "Unrelated answer satisfies native choice history");
            var answer = (BlueprintAnswer)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(binding.Value));
            history.SelectedAnswers.Add(answer);
            Check(ReadHistory().Has(binding.Key), "Actual native selected-answer collection is not read");
            Check(history.SelectedAnswers.Count == 2 && history.SelectedAnswers.Contains(unrelated), "Reading answer history changed native choices");
            history.SelectedAnswers.Remove(answer);
            Check(!ReadHistory().Has(binding.Key), "Selected-answer truth leaks into a fresh snapshot");
        }
        var registered = (List<SimpleBlueprint>)main.GetField("registered", PrivateStatic)!.GetValue(null)!;
        Check(registered.Select(bp => bp.AssetGuid).Distinct().Count() == registered.Count, "Duplicate generated GUIDs");
        foreach (string effect in story.Scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).Distinct())
            Check(ResourcesLibrary.TryGetBlueprint(Id("flag.hour." + effect)) is BlueprintUnlockableFlag, "Choice timestamp cannot survive a save: " + effect);
        foreach (var pair in answerLists)
        {
            var expected = originalAnswers[pair.Key].ToList();
            foreach (var scene in story.Scenes.Where(s => Rules.EntryTargets(s).Contains(pair.Key)))
            {
                // E14b: a return-to-list scene has one entry answer per list it joins.
                var added = pair.Value.Answers.Single(reference => reference.Guid == Id(scene.ReturnToList ? "entry." + scene.Id + "." + pair.Key : "entry." + scene.Id));
                expected.Insert(Math.Max(0, expected.Count - 1), added);
            }
            // E16: native openers follow the scene entries, each before the list's last native answer too.
            foreach (var opener in story.Openers.Where(o => o.AnswerList == pair.Key))
                expected.Insert(Math.Max(0, expected.Count - 1), pair.Value.Answers.Single(reference => reference.Guid == Id("opener." + opener.Id)));
            Check(pair.Value.Answers.SequenceEqual(expected), "Native answers changed or inserted out of order: " + pair.Key);
        }
        foreach (var pair in sequences)
        {
            var expected = originalCues[pair.Key].Select(reference => reference.Guid).ToList();
            if (pair.Key == Rules.PlayerFinalChoice)
            {
                // E14a/E14h: scene anchors are installed before their dependants. Native members retain their order.
                var anchored = new HashSet<BlueprintGuid>();
                foreach (var s in Rules.EpilogueInsertionOrder(story).Where(s => s.EpilogueSequence == "PlayerFinalChoice"))
                {
                    var page = Id("page." + s.Id + "." + s.Nodes[0].Id);
                    int at = expected.IndexOf(BlueprintGuid.Parse(Rules.EpilogueAnchor(story, s.EpilogueAfter, name => Id(name).ToString())!));
                    int index = at < 0 ? expected.Count : at + 1;
                    while (index < expected.Count && anchored.Contains(expected[index])) index++;
                    expected.Insert(index, page);
                    if (at >= 0) anchored.Add(page);   // runtime's missing-anchor fallback appends without an anchor marker
                }
                Check(pair.Value.Cues.Select(reference => reference.Guid).SequenceEqual(expected), "E14a pages misplaced in PlayerFinalChoice.");
                Check(pair.Value.Cues.Where(c => originalCues[pair.Key].Contains(c)).SequenceEqual(originalCues[pair.Key]),
                    "PlayerFinalChoice native members moved or replaced");
                continue;
            }
            // A native epilogue edit's replacement (E14d) is swapped in for its native cue on the native page, never appended.
            var addedPages = new HashSet<BlueprintGuid>();
            foreach (var s in Rules.EpilogueInsertionOrder(story).Where(s => s.EpilogueSequence == null
                && (s.Owner == "AeonEpilogue" ? sequenceIds[1] : sequenceIds[0]) == pair.Key))
            {
                var page = Id("page." + s.Id + "." + s.Nodes[0].Id);
                string? after = Rules.EpilogueAnchor(story, s.EpilogueAfter, name => Id(name).ToString());
                int at = after == null ? -1 : expected.IndexOf(BlueprintGuid.Parse(after));
                int index = at < 0 ? expected.Count : at + 1;
                while (index < expected.Count && addedPages.Contains(expected[index])) index++;
                expected.Insert(index, page);
                if (at >= 0) addedPages.Add(page);
            }
            Check(pair.Value.Cues.Select(reference => reference.Guid).SequenceEqual(expected), "Native epilogue references changed: " + pair.Key);
            Check(pair.Value.Cues.Where(c => originalCues[pair.Key].Contains(c)).SequenceEqual(originalCues[pair.Key]), "Native epilogue reference instances replaced");
        }
        var genericEndingExits = new HashSet<string>(JsonConvert.DeserializeObject<string[]>(File.ReadAllText(Path.Combine(
            Environment.GetEnvironmentVariable("RRT_TEST_REPO_ROOT") ?? Directory.GetCurrentDirectory(),
            "tools", "generic_ending_exit_contracts.json")))!);
        // Polish appended an ascent night: the original refusal remains answer zero, with no effects.
        var ascentExit = story.Scenes.Single(s => s.Id == "areelu.trickster.finale.ascended").Nodes.Single(n => n.Id == "end");
        Check(ascentExit.Choices.Count == 2 && ascentExit.Choices[0].Next == null
            && ascentExit.Choices[0].Set.Length == 0 && ascentExit.Choices[0].Requires.Length == 0
            && ascentExit.Choices[0].Forbids.Length == 0 && !ascentExit.Choices[0].Abort
            && ascentExit.Choices[0].Check == null && ascentExit.Choices[0].Revive == null
            && ascentExit.Choices[1].Next == "asc_night", "Expanded ascent ending changed the saved refusal or appended night index");
        // Appending a branch must also keep the old generic terminal blueprint resolvable.
        var legacyAscentExit = ResourcesLibrary.TryGetBlueprint(Id("answer.areelu.trickster.finale.ascended.end.continue")) as BlueprintAnswer;
        Check(legacyAscentExit != null, "Legacy ascent ending exit identity disappeared: answer.areelu.trickster.finale.ascended.end.continue");
        Check(legacyAscentExit!.OnSelect.Actions.Length == 0 && legacyAscentExit.NextCue.Cues.Count == 0,
            "Legacy ascent ending exit mutates progress or continues");
        var ascentPage = (BlueprintBookPage)ResourcesLibrary.TryGetBlueprint(Id("page.areelu.trickster.finale.ascended.end"));
        Check(ReferenceEquals(ascentPage.Answers[0].Get(), legacyAscentExit), "Saved ascent exit is not the displayed first answer");
        Check(ascentPage.Answers[1].Guid == Id("answer.areelu.trickster.finale.ascended.end.1")
            && ((BlueprintAnswer)ascentPage.Answers[1].Get()).NextCue.Cues.Single().Guid == Id("page.areelu.trickster.finale.ascended.asc_night"),
            "Appended ascent night lost its positional identity or destination");
        foreach (var scene in story.Scenes.Where(s => s.NativeReturnCue == null && !s.ReturnToList && s.ContinueBefore == null))
        {
            var dialog = ResourcesLibrary.TryGetBlueprint(Id("dialog." + scene.Id)) as BlueprintDialog;
            Check(dialog != null, "Missing dialog: " + scene.Id);
            Check(dialog!.FirstCue.Cues.Single().Guid == Id("page." + scene.Id + "." + scene.Nodes[0].Id), "Wrong first page: " + scene.Id);
            if (Rules.EntryTargets(scene).Length > 0)
            {
                var entryAnswer = (BlueprintAnswer)ResourcesLibrary.TryGetBlueprint(Id("entry." + scene.Id));
                Check(entryAnswer.ShowConditions.Conditions.Single() is Tirabade.Main.RouteCondition shown && ReferenceEquals(shown.Scene, scene) && ReferenceEquals(shown.Owner, entryAnswer), "Entry lost its visibility guard or owner: " + scene.Id);
                Check(entryAnswer.SelectConditions.Conditions.Single() is Tirabade.Main.RouteCondition selected && ReferenceEquals(selected.Scene, scene) && ReferenceEquals(selected.Owner, entryAnswer), "Entry lost its selection guard or owner: " + scene.Id);
                Check(entryAnswer.OnSelect.Actions.Single() is Tirabade.Main.RouteAction start && ReferenceEquals(start.Start, scene) && ReferenceEquals(start.Owner, entryAnswer), "Entry starts the wrong scene: " + scene.Id);
            }
            foreach (var node in scene.Nodes)
            {
                string nodeId = scene.Id + "." + node.Id;
                var page = ResourcesLibrary.TryGetBlueprint(Id("page." + nodeId)) as BlueprintBookPage;
                Check(page != null, "Missing page: " + nodeId);
                // E15c: a letter, sending or memory opens its first page with one kind line ("Letter from Seelah").
                int kindLine = ReferenceEquals(node, scene.Nodes[0]) && Rules.IsRemote(scene) && !scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                    && (Rules.KindOf(scene) == "letter" || Rules.KindOf(scene) == "sending" || Rules.KindOf(scene) == "memory") ? 1 : 0;
                Check(page!.Cues.Count == kindLine + (string.IsNullOrWhiteSpace(node.Text) ? 0 : 1) + node.Paragraphs.Count && page.Cues.All(c => c.Get() is BlueprintCue), "Missing page cue: " + nodeId);
                bool ending = scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal);
                Check(page.ShowOnce == ending && !page.ShowOnceCurrentDialog, "Wrong native page history policy: " + nodeId);
                var continuation = !ending && (scene.ContactUnit != null || Rules.IsRemote(scene) || scene.Participants.Length > 0) ? scene : null;
                // The frozen contracts cover old exits; new inert one-answer pages use the same runtime rule.
                var sole = node.Choices.Count == 1 ? node.Choices[0] : null;
                bool legacyEnding = genericEndingExits.Contains(nodeId);
                bool plainEnding = ending && sole != null
                    && sole.Id == null && sole.Text == "Continue" && sole.Next == null && sole.Check == null
                    && sole.Requires.Length == 0 && sole.Forbids.Length == 0 && sole.Set.Length == 0
                    && !sole.Abort && sole.Revive == null;
                if (legacyEnding || plainEnding)
                    Check(ending && node.Choices.Count >= 1 && node.Choices[0].Next == null && node.Choices[0].Check == null
                        && node.Choices[0].Requires.Length == 0 && node.Choices[0].Forbids.Length == 0
                        && node.Choices[0].Set.Length == 0 && !node.Choices[0].Abort && node.Choices[0].Revive == null
                        && node.Choices[0].NativeNext == null && node.Choices[0].Mythic == null
                        && node.Choices[0].Alignment == null && node.Choices[0].Crusade == null
                        && node.Choices[0].RemoveItem == null && node.Choices[0].StartEtude == null,
                        "Legacy ending exit mechanics changed: " + nodeId);
                Check(page.Answers.Count == (plainEnding ? 1 : node.Choices.Count + (continuation == null ? 0 : 1) + (node.Choices.Any(choice => choice.Crusade?.Amount < 0) ? 1 : 0)), "Wrong choice count: " + nodeId);
                foreach (var reference in page.Answers) Check(reference.Get() is BlueprintAnswer, "Unresolved generated answer: " + nodeId);
                if (legacyEnding || plainEnding)
                {
                    var leave = (BlueprintAnswer)page.Answers[0].Get();
                    Check(leave.AssetGuid == Id("answer." + nodeId + ".continue"), "Legacy ending exit identity changed: " + nodeId);
                    Check(leave.OnSelect.Actions.Length == 0 && leave.NextCue.Cues.Count == 0, "Plain ending mutates progress or continues: " + nodeId);
                    if (plainEnding) continue;
                }
                if (node.Choices.Any(choice => choice.Crusade?.Amount < 0))
                {
                    var paymentExit = (BlueprintAnswer)page.Answers.Last().Get();
                    Check(paymentExit.AssetGuid == Id("answer." + nodeId + ".payment_unavailable")
                        && paymentExit.ShowConditions.Conditions.Single() is Tirabade.Main.RouteCondition fallback
                        && ReferenceEquals(fallback.PaymentNode, node) && paymentExit.OnSelect.Actions.Length == 0
                        && paymentExit.SelectConditions.Conditions.Length == 0 && paymentExit.NextCue.Cues.Count == 0,
                        "Paid-only page has no unconditional, mutation-free exit: " + nodeId);
                }
                if (continuation != null)
                {
                    var leave = (BlueprintAnswer)page.Answers[node.Choices.Count].Get();
                    Check(leave.AssetGuid == Id("answer." + nodeId + ".contact_lost"), "Contact exit changes stable answer identities: " + nodeId);
                    Check(leave.ShowConditions.Conditions.Single() is Tirabade.Main.RouteCondition lost && lost.ContactLost && ReferenceEquals(lost.Continuation, scene), "Missing contact-loss exit guard: " + nodeId);
                    Check(leave.SelectConditions.Conditions.Length == 0 && leave.OnSelect.Actions.Length == 0 && leave.NextCue.Cues.Count == 0, "Contact exit can block, mutate progress or continue: " + nodeId);
                }
                for (int i = 0; i < node.Choices.Count; i++)
                {
                    var choice = node.Choices[i];
                    var answer = (BlueprintAnswer)page.Answers[i].Get();
                    Check(answer.AssetGuid == Id("answer." + nodeId + "." + (choice.Id ?? i.ToString())), "Choice identity changed: " + nodeId);
                    if (ending && choice.Id == "continue")
                    {
                        Check(answer.ShowConditions.Conditions.Length == 0 && answer.SelectConditions.Conditions.Length == 0
                            && answer.OnSelect.Actions.Length == 0 && answer.NextCue.Cues.Count == 0,
                            "Preserved ending exit gained gates, effects or a continuation: " + nodeId);
                        continue;
                    }
                    Check(answer.ShowConditions.Conditions.Single() is Tirabade.Main.RouteCondition shown && ReferenceEquals(shown.Choice, choice) && ReferenceEquals(shown.Owner, answer), "Choice lost its visibility guard or owner: " + nodeId);
                    Check(answer.SelectConditions.Conditions.Single() is Tirabade.Main.RouteCondition selected && ReferenceEquals(selected.Choice, choice) && ReferenceEquals(selected.Owner, answer), "Choice lost its selection guard or owner: " + nodeId);
                    var action = answer.OnSelect.Actions.OfType<Tirabade.Main.RouteAction>().Single();
                    int nativeEffects = (choice.Crusade?.Amount > 0 && !scene.Id.StartsWith(Rules.WenduagEchoPrefix, StringComparison.Ordinal) ? 1 : 0) + (choice.RemoveItem != null ? 1 : 0) + (choice.StartEtude != null ? 1 : 0);
                    Check(answer.OnSelect.Actions.Length - 1 - nativeEffects is 0 or 1 && (choice.Mythic != null || answer.OnSelect.Actions.Length == 1 + nativeEffects)
                        && answer.OnSelect.Actions[choice.Crusade?.Amount > 0 && !scene.Id.StartsWith(Rules.WenduagEchoPrefix, StringComparison.Ordinal) ? 1 : 0] is Tirabade.Main.RouteAction, "Choice carries unexpected native actions: " + nodeId);
                    if (choice.Crusade?.Amount > 0 && !scene.Id.StartsWith(Rules.WenduagEchoPrefix, StringComparison.Ordinal))
                    {
                        var payment = answer.OnSelect.Actions[0] is Tirabade.Main.GuardedRemoveCrusadeResources remove ? remove.Payment
                            : ((Tirabade.Main.GuardedAddCrusadeResources)answer.OnSelect.Actions[0]).Payment;
                        Check(payment != null && ReferenceEquals(payment, action.Payment) && ReferenceEquals(payment.Cost, choice.Crusade),
                            "Paid progress has no resource-action witness: " + nodeId);
                    }
                    if (choice.Crusade?.Amount < 0)
                    {
                        Check(action.Payment != null && ReferenceEquals(action.Payment.Cost, choice.Crusade)
                            && ReferenceEquals(action.Payment.Scene, scene)
                            && ((Tirabade.Main.RouteCondition)answer.ShowConditions.Conditions.Single()).PaidScene == scene
                            && ((Tirabade.Main.RouteCondition)answer.SelectConditions.Conditions.Single()).PaidScene == scene
                            && !answer.OnSelect.Actions.OfType<Kingmaker.Kingdom.Blueprints.RemoveCrusadeResources>().Any(),
                            "Negative payment is not owned by its story transaction: " + nodeId);
                        Check(ResourcesLibrary.TryGetBlueprint(Id("flag." + Rules.PaymentKey(scene, choice))) is BlueprintUnlockableFlag,
                            "Negative payment lacks a saved replay receipt: " + nodeId);
                    }
                    Check((answer.MythicRequirement.ToString() == (choice.Mythic ?? "None")) && (answer.AlignmentShift?.Value ?? 0) == (choice.Alignment?.Value ?? 0), "Choice native mythic/alignment drifted: " + nodeId);
                    Check(action != null && ReferenceEquals(action.Choice, choice) && ReferenceEquals(action.Owner, answer), "Choice lost its effects or action owner: " + nodeId);
                    Check(ReferenceEquals(((Tirabade.Main.RouteCondition)answer.ShowConditions.Conditions.Single()).Continuation, continuation)
                        && ReferenceEquals(((Tirabade.Main.RouteCondition)answer.SelectConditions.Conditions.Single()).Continuation, continuation)
                        && ReferenceEquals(action!.Continuation, continuation), "Contact continuation is not guarded at visibility, selection and mutation: " + nodeId);
                    Check(ReferenceEquals(action!.Complete, !ending && choice.Next == null && choice.Check == null && !choice.Abort ? scene : null), "Choice completes at the wrong point: " + nodeId);
                    var expected = choice.Check != null ? new[] { Id("check." + nodeId + "." + i) }
                        : choice.Next == null ? Array.Empty<BlueprintGuid>() : new[] { Id("page." + scene.Id + "." + choice.Next) };
                    Check(answer.NextCue.Cues.Select(reference => reference.Guid).SequenceEqual(expected), "Wrong next page: " + nodeId);
                    if (choice.Check != null)
                    {
                        var roll = answer.NextCue.Cues.Single().Get() as BlueprintCheck;
                        Check(roll != null && roll.Type.ToString() == choice.Check.Skill && roll.DC == choice.Check.DC, "Native check has wrong stat or difficulty: " + nodeId);
                        Check(roll!.Success.AssetGuid == Id("page." + scene.Id + "." + choice.Check.Success)
                            && roll.Fail.AssetGuid == Id("page." + scene.Id + "." + choice.Check.Failure), "Native check has wrong outcome pages: " + nodeId);
                        Check(continuation == null ? roll.Conditions.Conditions.Length == 0
                            : roll.Conditions.Conditions.Single() is Tirabade.Main.RouteCondition guard
                                && ReferenceEquals(guard.Continuation, scene) && guard.Choice == null && !guard.ContactLost,
                            "Native check can roll after contact loss: " + nodeId);
                        Check(!roll.Hidden && roll.Experience == Kingmaker.DialogSystem.DialogExperience.NoExperience, "Courtship check visibility or XP differs from declared policy: " + nodeId);
                        var evaluator = typeof(BlueprintCheck).GetField("m_UnitEvaluator", BindingFlags.Instance | BindingFlags.NonPublic)!.GetValue(roll);
                        Check(roll.BanPartyCheckInCamp == choice.Check.CommanderOnly
                            && (choice.Check.CommanderOnly ? evaluator is Kingmaker.Designers.EventConditionActionSystem.Evaluators.PlayerCharacter : evaluator == null), "Check uses the wrong actor policy: " + nodeId);
                    }
                    else Check(answer.NextCue.Cues.All(reference => reference.Get() is BlueprintBookPage), "Unresolved next page: " + nodeId);
                }
            }
        }
        var registeredBefore = registered.ToArray();
        var answersBefore = answerLists.ToDictionary(pair => pair.Key, pair => pair.Value.Answers.ToArray());
        var cuesBefore = sequences.ToDictionary(pair => pair.Key, pair => pair.Value.Cues.ToArray());
        var expandedBefore = expandedEpilogue?.Cues.ToArray();
        build.Invoke(null, null);
        Check(registered.SequenceEqual(registeredBefore), "Second Build creates duplicate blueprints");
        Check(answerLists.All(pair => pair.Value.Answers.SequenceEqual(answersBefore[pair.Key])), "Second Build duplicates answers");
        Check(sequences.All(pair => pair.Value.Cues.SequenceEqual(cuesBefore[pair.Key])), "Second Build duplicates epilogues");
        if (expandedEpilogue != null) Check(expandedEpilogue.Cues.SequenceEqual(expandedBefore!), "Second Build duplicates optional epilogue pages.");
        Console.WriteLine("Optional Expanded Epilogue fixture: " + (expandedEpilogue == null ? "absent" : "present; parent reference preservation and attachment checked, external caller graph not executed"));
        // RRT_DUMP_REGISTERED=<path> writes every generated blueprint name and GUID for the save-reference ledger (tools/save_ledger.py).
        string? dump = Environment.GetEnvironmentVariable("RRT_DUMP_REGISTERED");
        if (!string.IsNullOrEmpty(dump))
            File.WriteAllLines(dump, registered.Select(bp => bp.name + "	" + bp.AssetGuid + "	" + bp.GetType().Name).OrderBy(line => line, StringComparer.Ordinal));
        Console.WriteLine($"PASS: {checks} assertions; real Main.Build, {story.Scenes.Count} scenes, {registered.Count} generated blueprints, {targetIds.Length} native answer lists, 1 native Aeon sequence and 1 parent-mod sentinel sequence, idempotence.");
        Console.WriteLine("DLL SHA256 " + Hash(typeof(Tirabade.Main).Assembly.Location));
        Console.WriteLine("Story SHA256 " + Hash(storyPath));
        RunSuite("ChoiceExtensionManagedTests", () => ChoiceExtensionManagedTests.Run(native, Seed<BlueprintUnlockableFlag>, Seed<BlueprintCue>, Seed<Kingmaker.Blueprints.Items.BlueprintItem>, Id, Check));
        RunSuite("NativeReaderManagedTests", () => NativeReaderManagedTests.Run(story, native, Check));
        RunSuite("EpilogueAfterManagedTests", () => EpilogueAfterManagedTests.Run(Id, Check));
        RunSuite("PresenceManagedTests", () => PresenceManagedTests.Run(story, native, Check));
        RunSuite("NativeEpilogueManagedTests", () => NativeEpilogueManagedTests.Run(native, Id, Check));
        RunSuite("ReturnToListManagedTests", () => ReturnToListManagedTests.Run(native, Id, Check));
        RunSuite("ParagraphManagedTests", () => ParagraphManagedTests.Run(Id, Check));
        RunSuite("NativeEpilogueEditManagedTests", () => NativeEpilogueEditManagedTests.Run(native, Id, Check));
        RunSuite("NativeEpilogueEditManagedTests.RunQ4", () => NativeEpilogueEditManagedTests.RunQ4(native, Id, Check));
        if (story.NativeEpilogueEdits.ContainsKey("3a3e561c6b05a284d93eb3bff7b712a6")) RunSuite("NativeEpilogueEditManagedTests.RunTirabade", () => NativeEpilogueEditManagedTests.RunTirabade(story, native, Id, Check));
        if (story.NativeEpilogueEdits.ContainsKey("4ed8e9723359441dae10ad3068d3f2c7")) RunSuite("NativeEpilogueEditManagedTests.RunCamellia", () => NativeEpilogueEditManagedTests.RunCamellia(story, native, Id, Check));
        if (story.NativeEpilogueEdits.ContainsKey("825786e8c5db4511ae30950bb286f0e9")) RunSuite("NativeEpilogueEditManagedTests.RunAfterlogue", () => NativeEpilogueEditManagedTests.RunAfterlogue(story, native, Id, Check));
        RunSuite("NativeEpilogueEditManagedTests.RunKianaSiblings", () => NativeEpilogueEditManagedTests.RunKianaSiblings(story, native, Id, Check));
        RunSuite("NativeQ3RecoveryManagedTests", () => NativeQ3RecoveryManagedTests.Run(story, Id, Check));
        RunSuite("NativeEpilogueEditManagedTests.RunDelivery", () => NativeEpilogueEditManagedTests.RunDelivery(story, Check));
        RunSuite("NativeEpilogueEditManagedTests.RunDreamPage", () => NativeEpilogueEditManagedTests.RunDreamPage(story, native, Id, Check));
        RunSuite("NativeEpilogueEditManagedTests.RunJewelerBowl", () => NativeEpilogueEditManagedTests.RunJewelerBowl(story, native, Id, Check));
        // eng8-q8e: EE follow-ons retain actual native history receipts.
        RunSuite("NativeEpilogueEditManagedTests.RunEndingIdentity", () => NativeEpilogueEditManagedTests.RunEndingIdentity(story, native, Check));
        RunSuite("NativeGateManagedTests", () => NativeGateManagedTests.Run(story, Check));
        RunSuite("TerendelevNativeManagedTests", () => TerendelevNativeManagedTests.Run(story, native, Check)); // eng7-f6d
        if (story.Scenes.Any(Rules.IsWenduagEchoHub)) RunSuite("WenduagEchoManagedTests", () => WenduagEchoManagedTests.Run(Check));
        RunSuite("NativeGateManagedTests.RunArsinoe", () => NativeGateManagedTests.RunArsinoe(story, Check));
        RunSuite("NativeGateManagedTests.RunDevarra", () => NativeGateManagedTests.RunDevarra(story, Check));
        RunSuite("SpeakerManagedTests", () => SpeakerManagedTests.Run(native, Check));
        RunSuite("ContinueBeforeManagedTests", () => ContinueBeforeManagedTests.Run(native, Id, Check));
        RunSuite("PresenceHubManagedTests", () => PresenceHubManagedTests.Run(Id, Check));
        RunSuite("MailbagManagedTests", () => MailbagManagedTests.Run(story, Id, Check));
        RunSuite("BookManagedTests", () => BookManagedTests.Run(story, Id, Path.GetFullPath(Path.Combine(Path.GetDirectoryName(Path.GetFullPath(storyPath))!, "..", "art", "CustomNpcPortraits", "RanRomance-Tirabade", "Scenes")), Check));
        RunSuite("BookPolishManagedTests", () => BookPolishManagedTests.Run(story, Id, Check));
        RunSuite("HouseholdManagedTests", () => HouseholdManagedTests.Run(story, Id, Check));
        // __E14_MANAGED__
        Console.WriteLine("Scope: real managed blueprint construction and native ending seen-state checks; native answer and Aeon reference lists extracted from blueprints.zip; parent-mod sequence has preservation sentinels. Ending probes bypass route eligibility, Unity page rendering and debug logging. No parent-mod initialization, full campaign condition evaluation, portraits, ToyBox execution or game save round trip.");
        return 0;
    }
}
