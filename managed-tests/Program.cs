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
        string script = Path.GetFullPath(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "../../../read-native.py"));
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

    private static string Hash(string path)
    {
        using (var sha = SHA256.Create())
        using (var file = File.OpenRead(path))
            return BitConverter.ToString(sha.ComputeHash(file)).Replace("-", "");
    }

    [MethodImpl(MethodImplOptions.NoInlining)]
    public static int Run(string game, string storyPath, string modDirectory)
    {
        var story = JsonConvert.DeserializeObject<Story>(File.ReadAllText(storyPath))!;
        Rules.Validate(story);
        TerendelevDeliveryBlueprintTests.Run(Check);
        NativeContactStorageTests.Run(Check);
        JerribethRecoveryObservationTests.Run(Check);
        TirabadeRecoveryObservationTests.Run(Check);
        KonomiContactObservationTests.Run(Check);
        KonomiRecoveryTests.Run(Check);
        KonomiMeetingTests.Run(Check);
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
        var sequenceIds = new[] { "ed4baeaf69394754902344f0598d7e5a", "ced82f299d246f448b48afa0b630dd70" };
        var unitIds = story.Revivals.Values.Select(r => r.Unit).Concat(story.Scenes.Where(s => s.ContactUnit != null).SelectMany(s => new[] { s.ContactUnit! }.Concat(s.AdditionalContactUnits))).Distinct().ToArray();
        var native = ReadNative(Path.Combine(game, "blueprints.zip"), targetIds.Concat(sequenceIds.Skip(1)).Concat(story.Etudes.Values).Concat(story.CompletedEtudes.Values).Concat(story.SelectedAnswers.Values).Concat(story.StartedDialogs.Values).Concat(story.CompletedQuests.Values).Concat(story.SeenCues.Values.SelectMany(ids => ids)).Concat(unitIds));
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
            foreach (string answer in NativeReferences(native[guid], "Answers")) list.Answers.Add(Reference<BlueprintAnswerBaseReference>(answer));
            answerLists.Add(guid, list);
            originalAnswers.Add(guid, list.Answers.ToArray());
        }
        var sequences = new Dictionary<string, BlueprintCueSequence>();
        var originalCues = new Dictionary<string, BlueprintCueBaseReference[]>();
        foreach (string guid in sequenceIds)
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintCueSequence", StringComparison.Ordinal), "Wrong native sequence type: " + guid);
            var sequence = Seed<BlueprintCueSequence>(guid);
            foreach (string cue in NativeReferences(native[guid], "Cues")) sequence.Cues.Add(Reference<BlueprintCueBaseReference>(cue));
            sequences.Add(guid, sequence);
            originalCues.Add(guid, sequence.Cues.ToArray());
        }
        foreach (string guid in story.Etudes.Values.Concat(story.CompletedEtudes.Values).Distinct())
        {
            Check(((string)native[guid]["$type"]!).EndsWith(", BlueprintEtude", StringComparison.Ordinal), "Wrong native etude type: " + guid);
            Seed<BlueprintEtude>(guid);
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
            string contractPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory,
                "../../../fixtures/parent-ending-source/verified-contract.json");
            ParentEndingIntegrationTests.PrepareSourceFixtures(JObject.Parse(File.ReadAllText(contractPath)),
                ParentEndingSourceFixtures.Build(), ParentEndingSourceFixtures.PageActions());
            ParentEndingIntegrationTests.CheckPreflight(story, Check);
            foreach (var pair in sequences) originalCues[pair.Key] = pair.Value.Cues.ToArray();
        }
        var entry = new UnityModManager.ModEntry(new UnityModManager.ModInfo { Id = "ManagedBuildTests", Version = "1.0.0", ManagerVersion = "0.27.11" }, modDirectory);
        Type main = typeof(Tirabade.Main);
        main.GetField("entry", PrivateStatic)!.SetValue(null, entry);
        main.GetField("story", PrivateStatic)!.SetValue(null, story);
        MethodInfo build = main.GetMethod("Build", PrivateStatic)!;
        KonomiMeetingIntegrationTests.PrepareNativePlacement();
        build.Invoke(null, null);
        KonomiMeetingIntegrationTests.Run(Check);
        Check((bool)main.GetField("initialized", PrivateStatic)!.GetValue(null)!, "Build did not initialize: " + main.GetField("error", PrivateStatic)!.GetValue(null));
        Check(main.GetField("error", PrivateStatic)!.GetValue(null) == null, "Build reported an error");
        if (hasParentEndingRules) ParentEndingIntegrationTests.Run(story, Check);
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
                var added = pair.Value.Answers.Single(reference => reference.Guid == Id("entry." + scene.Id));
                expected.Insert(Math.Max(0, expected.Count - 1), added);
            }
            Check(pair.Value.Answers.SequenceEqual(expected), "Native answers changed or inserted out of order: " + pair.Key);
        }
        foreach (var pair in sequences)
        {
            var expected = originalCues[pair.Key].Select(reference => reference.Guid).ToList();
            expected.AddRange(story.Scenes.Where(s => s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                && (s.Owner == "AeonEpilogue" ? sequenceIds[1] : sequenceIds[0]) == pair.Key)
                .Select(s => Id("page." + s.Id + "." + s.Nodes[0].Id)));
            Check(pair.Value.Cues.Select(reference => reference.Guid).SequenceEqual(expected), "Native epilogue references changed: " + pair.Key);
            Check(pair.Value.Cues.Take(originalCues[pair.Key].Length).SequenceEqual(originalCues[pair.Key]), "Native epilogue reference instances replaced");
        }
        foreach (var scene in story.Scenes)
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
                Check(page!.Cues.Count == 1 && page.Cues[0].Get() is BlueprintCue, "Missing page cue: " + nodeId);
                bool ending = scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal);
                var continuation = !ending && (scene.ContactUnit != null || Rules.IsRemote(scene)) ? scene : null;
                bool plainEnding = ending && node.Choices.Count == 1 && node.Choices[0].Next == null && node.Choices[0].Check == null
                    && node.Choices[0].Requires.Length == 0 && node.Choices[0].Forbids.Length == 0
                    && node.Choices[0].Set.Length == 0 && node.Choices[0].Text == "Continue"
                    && !node.Choices[0].Abort && node.Choices[0].Revive == null;
                Check(page.Answers.Count == (plainEnding ? 1 : node.Choices.Count + (continuation == null ? 0 : 1)), "Wrong choice count: " + nodeId);
                foreach (var reference in page.Answers) Check(reference.Get() is BlueprintAnswer, "Unresolved generated answer: " + nodeId);
                if (plainEnding)
                {
                    var leave = (BlueprintAnswer)page.Answers.Single().Get();
                    Check(leave.AssetGuid == Id("answer." + nodeId + ".continue"), "Legacy ending exit identity changed: " + nodeId);
                    Check(leave.OnSelect.Actions.Length == 0 && leave.NextCue.Cues.Count == 0, "Plain ending mutates progress or continues: " + nodeId);
                    continue;
                }
                if (continuation != null)
                {
                    var leave = (BlueprintAnswer)page.Answers.Last().Get();
                    Check(leave.AssetGuid == Id("answer." + nodeId + ".contact_lost"), "Contact exit changes stable answer identities: " + nodeId);
                    Check(leave.ShowConditions.Conditions.Single() is Tirabade.Main.RouteCondition lost && lost.ContactLost && ReferenceEquals(lost.Continuation, scene), "Missing contact-loss exit guard: " + nodeId);
                    Check(leave.SelectConditions.Conditions.Length == 0 && leave.OnSelect.Actions.Length == 0 && leave.NextCue.Cues.Count == 0, "Contact exit can block, mutate progress or continue: " + nodeId);
                }
                for (int i = 0; i < node.Choices.Count; i++)
                {
                    var choice = node.Choices[i];
                    var answer = (BlueprintAnswer)page.Answers[i].Get();
                    Check(answer.ShowConditions.Conditions.Single() is Tirabade.Main.RouteCondition shown && ReferenceEquals(shown.Choice, choice) && ReferenceEquals(shown.Owner, answer), "Choice lost its visibility guard or owner: " + nodeId);
                    Check(answer.SelectConditions.Conditions.Single() is Tirabade.Main.RouteCondition selected && ReferenceEquals(selected.Choice, choice) && ReferenceEquals(selected.Owner, answer), "Choice lost its selection guard or owner: " + nodeId);
                    var action = answer.OnSelect.Actions.Single() as Tirabade.Main.RouteAction;
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
        build.Invoke(null, null);
        Check(registered.SequenceEqual(registeredBefore), "Second Build creates duplicate blueprints");
        Check(answerLists.All(pair => pair.Value.Answers.SequenceEqual(answersBefore[pair.Key])), "Second Build duplicates answers");
        Check(sequences.All(pair => pair.Value.Cues.SequenceEqual(cuesBefore[pair.Key])), "Second Build duplicates epilogues");
        Console.WriteLine($"PASS: {checks} assertions; real Main.Build, {story.Scenes.Count} scenes, {registered.Count} generated blueprints, {targetIds.Length} native answer lists, 1 native Aeon sequence and 1 parent-mod sentinel sequence, idempotence.");
        Console.WriteLine("DLL SHA256 " + Hash(typeof(Tirabade.Main).Assembly.Location));
        Console.WriteLine("Story SHA256 " + Hash(storyPath));
        Console.WriteLine("Scope: real managed blueprint construction; native answer and Aeon reference lists extracted from blueprints.zip; parent-mod sequence has preservation sentinels. No parent-mod initialization, Unity runtime, condition evaluation, portraits, ToyBox execution or game save round trip.");
        return 0;
    }
}
