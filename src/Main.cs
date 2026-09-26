using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Text.RegularExpressions;
using System.Diagnostics;
using HarmonyLib;
using Kingmaker;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Area;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Blueprints.Quests;
using Kingmaker.Controllers.Dialog;
using Kingmaker.Controllers.Rest;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.DialogSystem.State;
using Kingmaker.ElementsSystem;
using Kingmaker.GameModes;
using Kingmaker.Localization;
using Kingmaker.UI.MVVM._VM.Dialog.BookEvent;
using Newtonsoft.Json;
using UnityEngine;
using UnityModManagerNet;

namespace Tirabade
{
    public sealed class Settings : UnityModManager.ModSettings
    {
        public bool Narration = true;
        public override void Save(UnityModManager.ModEntry entry) => Save(this, entry);
    }

    public static class Main
    {
        private static UnityModManager.ModEntry entry = null!;
        private static Story story = null!;
        private static Settings settings = null!;
        private static bool initialized;
        private static bool enabled;
        private static string? error;
        private static Scene? pending;
        private static object? pendingPlayer;
        private static object? narrationPlayer;
        private static int pendingFrame;
        private static readonly Dictionary<string, BlueprintUnlockableFlag> flags = new Dictionary<string, BlueprintUnlockableFlag>();
        private static readonly Dictionary<string, BlueprintDialog> dialogs = new Dictionary<string, BlueprintDialog>();
        private static readonly Dictionary<string, Node> pages = new Dictionary<string, Node>();
        private static readonly Dictionary<string, Sprite> portraits = new Dictionary<string, Sprite>();
        private static readonly Dictionary<string, BlueprintEtude> etudes = new Dictionary<string, BlueprintEtude>();
        private static readonly Dictionary<string, BlueprintQuest> completedQuests = new Dictionary<string, BlueprintQuest>();
        private static readonly Dictionary<string, BlueprintCue[]> seenCues = new Dictionary<string, BlueprintCue[]>();
        private static readonly Dictionary<string, BlueprintAnswer> selectedAnswers = new Dictionary<string, BlueprintAnswer>();
        private static readonly Dictionary<string, BlueprintDialog> startedDialogs = new Dictionary<string, BlueprintDialog>();
        private static readonly Dictionary<string, BlueprintEtude> completedEtudes = new Dictionary<string, BlueprintEtude>();
        private static readonly Dictionary<string, BlueprintUnit> revivalUnits = new Dictionary<string, BlueprintUnit>();
        private static readonly Dictionary<string, BlueprintUnit> contactUnits = new Dictionary<string, BlueprintUnit>();
        private static string? recoveryMessage;
        private static object? recoveryPlayer;
        private static readonly List<SimpleBlueprint> registered = new List<SimpleBlueprint>();
        private static readonly Dictionary<string, BlueprintQuestObjective> objectives = new Dictionary<string, BlueprintQuestObjective>();
        private static Process? narrator;
        private static float pollAt;
        private static bool restPending;

        public static bool Load(UnityModManager.ModEntry mod)
        {
            entry = mod;
            try
            {
                story = JsonConvert.DeserializeObject<Story>(File.ReadAllText(Path.Combine(mod.Path, "Story.json"))) ?? throw new InvalidOperationException("Story.json is empty.");
                Rules.Validate(story);
                settings = UnityModManager.ModSettings.Load<Settings>(mod);
                mod.OnToggle = (_, value) =>
                {
                    if (!value && Game.Instance?.DialogController?.Dialog?.name.StartsWith("RRT_", StringComparison.Ordinal) == true)
                    {
                        mod.Logger.Log("Finish the current route conversation before disabling the extension.");
                        return false;
                    }
                    enabled = value;
                    if (!value) CancelPending();
                    return true;
                };
                mod.OnGUI = OnGUI;
                mod.OnSaveGUI = m => settings.Save(m);
                mod.OnUpdate = (_, dt) => Update();
                enabled = true;
                new Harmony(mod.Info.Id).PatchAll(typeof(Main).Assembly);
                mod.Logger.Log("Three at the Table loaded. Waiting for the blueprint cache.");
                return true;
            }
            catch (Exception ex) { mod.Logger.LogException(ex); return false; }
        }

        private static BlueprintGuid GuidFor(string name)
        {
            using (var hash = SHA256.Create())
                return BlueprintGuid.Parse(string.Concat(hash.ComputeHash(Encoding.UTF8.GetBytes("RanRomance.Tirabade.v1/" + name)).Take(16).Select(b => b.ToString("x2"))));
        }

        private static T New<T>(string id) where T : SimpleBlueprint, new()
        {
            var guid = GuidFor(id);
            if (ResourcesLibrary.TryGetBlueprint(guid) != null) throw new InvalidOperationException("Blueprint collision: " + id);
            var bp = new T { name = "RRT_" + id, AssetGuid = guid };
            ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(guid, bp);
            registered.Add(bp);
            return bp;
        }

        private static T Get<T>(string guid) where T : SimpleBlueprint =>
            ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(guid)) as T ?? throw new InvalidOperationException("Required blueprint missing: " + guid);

        private static T Ref<T>(SimpleBlueprint bp) where T : BlueprintReferenceBase, new()
        {
            var reference = new T();
            Field(reference, "deserializedGuid", bp.AssetGuid);
            return reference;
        }
        private static void Field(object obj, string name, object value) => AccessTools.Field(obj.GetType(), name).SetValue(obj, value);
        private static ConditionsChecker Conditions(params Condition[] conditions) => new ConditionsChecker { Conditions = conditions };
        private static ActionList Actions(params GameAction[] actions) => new ActionList { Actions = actions };
        private static CueSelection Cues(params BlueprintCueBase[] cues) => new CueSelection { Cues = cues.Select(Ref<BlueprintCueBaseReference>).ToList() };
        private static LocalizedString Text(string id, string value)
        {
            string key = "RRT." + id;
            LocalizationManager.CurrentPack.PutString(key, value);
            var result = new LocalizedString();
            Field(result, "m_Key", key);
            return result;
        }

        // Register all save references before any saved game is deserialized.
        private static void Build()
        {
            if (initialized || error != null) return;
            try
            {
                // Check integration points before creating or attaching anything.
                var targets = story.Scenes.SelectMany(Rules.EntryTargets).Distinct().ToDictionary(id => id, Get<BlueprintAnswersList>);
                var epilogue = Get<BlueprintCueSequence>("ed4baeaf69394754902344f0598d7e5a");
                var aeon = Get<BlueprintCueSequence>("ced82f299d246f448b48afa0b630dd70");
                foreach (var pair in story.Etudes) etudes.Add(pair.Key, Get<BlueprintEtude>(pair.Value));
                foreach (var pair in story.CompletedQuests) completedQuests.Add(pair.Key, Get<BlueprintQuest>(pair.Value));
                foreach (var pair in story.SeenCues) seenCues.Add(pair.Key, pair.Value.Select(Get<BlueprintCue>).ToArray());
                foreach (var pair in story.SelectedAnswers) selectedAnswers.Add(pair.Key, Get<BlueprintAnswer>(pair.Value));
                foreach (var pair in story.StartedDialogs) startedDialogs.Add(pair.Key, Get<BlueprintDialog>(pair.Value));
                foreach (var pair in story.CompletedEtudes) completedEtudes.Add(pair.Key, Get<BlueprintEtude>(pair.Value));
                foreach (var pair in story.Revivals) revivalUnits.Add(pair.Key, Get<BlueprintUnit>(pair.Value.Unit));
                foreach (var guid in story.Scenes.Where(s => s.ContactUnit != null).Select(s => s.ContactUnit!).Distinct())
                    contactUnits.Add(guid, Get<BlueprintUnit>(guid));
                var effects = story.Scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).Distinct().ToArray();
                var keys = story.Scenes.Select(s => s.Id).Concat(story.Scenes.Select(s => "hour." + s.Id))
                    .Concat(effects).Concat(effects.Select(key => "hour." + key))
                    .Concat(story.Relationships.Values.SelectMany(r => new[] { r.StartedFlag, r.ClosedFlag, r.CommittedFlag })).Distinct();
                foreach (var key in keys) flags.Add(key, New<BlueprintUnlockableFlag>("flag." + key));
                foreach (var relationship in story.Relationships) BuildJournal(relationship.Key, relationship.Value);
                foreach (var scene in story.Scenes) BuildScene(scene);
                foreach (var scene in story.Scenes)
                {
                    if (scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
                    {
                        var sequence = scene.Owner == "AeonEpilogue" ? aeon : epilogue;
                        sequence.Cues.Add(Ref<BlueprintCueBaseReference>(Get<BlueprintBookPage>(GuidFor("page." + scene.Id + "." + scene.Nodes[0].Id).ToString())));
                        continue;
                    }
                    if (Rules.IsRemote(scene)) continue;
                    var answer = New<BlueprintAnswer>("entry." + scene.Id);
                    InitializeAnswer(answer);
                    answer.Text = Text("entry." + scene.Id, scene.Entry);
                    answer.ShowConditions = Conditions(new RouteCondition { Scene = scene });
                    // SelectConditions are also checked when ToyBox displays unavailable answers.
                    answer.SelectConditions = Conditions(new RouteCondition { Scene = scene });
                    answer.OnSelect = Actions(new RouteAction { Start = scene });
                    foreach (var id in Rules.EntryTargets(scene))
                        targets[id].Answers.Insert(Math.Max(0, targets[id].Answers.Count - 1), Ref<BlueprintAnswerBaseReference>(answer));
                }
                foreach (var blueprint in registered)
                {
                    foreach (var field in blueprint.GetType().GetFields())
                    {
                        var value = field.GetValue(blueprint);
                        IEnumerable<Element> elements = value is ConditionsChecker checker ? (checker.Conditions ?? Array.Empty<Condition>()).Cast<Element>()
                            : value is ActionList actions ? actions.Actions.Cast<Element>() : Enumerable.Empty<Element>();
                        foreach (var element in elements)
                        {
                            element.Owner = blueprint;
                            element.name = "$" + element.GetType().Name + "$" + System.Guid.NewGuid();
                            blueprint.AddToElementsList(element);
                        }
                    }
                    blueprint.OnEnable();
                }
                initialized = true;
                entry.Logger.Log("Registered " + story.Scenes.Count + " scenes. Existing dialogue answers and finish actions preserved.");
            }
            catch (Exception ex) { error = ex.Message; entry.Logger.LogException(ex); }
        }

        private static void InitializeAnswer(BlueprintAnswer answer)
        {
            answer.NextCue = Cues();
            answer.ShowConditions = Conditions();
            answer.SelectConditions = Conditions();
            answer.OnSelect = Actions();
            answer.CharacterSelection = new CharacterSelection();
            answer.ShowCheck = new ShowCheck();
        }

        private static void BuildScene(Scene scene)
        {
            var local = new Dictionary<string, BlueprintBookPage>();
            foreach (var node in scene.Nodes)
            {
                string id = scene.Id + "." + node.Id;
                var page = New<BlueprintBookPage>("page." + id);
                page.Conditions = scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal) ? Conditions(new RouteCondition { Scene = scene }) : Conditions();
                page.OnShow = Actions();
                page.Title = Text("title." + id, scene.Title);
                var cue = New<BlueprintCue>("cue." + id);
                cue.Conditions = Conditions();
                cue.OnShow = Actions();
                cue.OnStop = Actions();
                cue.Speaker = new DialogSpeaker { NoSpeaker = true, MoveCamera = false };
                cue.TurnSpeaker = false;
                cue.Continue = Cues();
                cue.Text = Text("cue." + id, node.Text);
                page.Cues.Add(Ref<BlueprintCueBaseReference>(cue));
                local.Add(node.Id, page);
                pages.Add(page.AssetGuid.ToString(), node);
            }
            foreach (var node in scene.Nodes)
            {
                var page = local[node.Id];
                bool ending = scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal);
                // Preserve saved terminal answer IDs while building authored ending branches normally.
                if (ending && node.Choices.Count == 1 && node.Choices[0].Next == null && node.Choices[0].Check == null
                    && node.Choices[0].Requires.Length == 0 && node.Choices[0].Forbids.Length == 0
                    && node.Choices[0].Set.Length == 0 && node.Choices[0].Text == "Continue"
                    && !node.Choices[0].Abort && node.Choices[0].Revive == null)
                {
                    var next = New<BlueprintAnswer>("answer." + scene.Id + "." + node.Id + ".continue");
                    InitializeAnswer(next);
                    next.Text = Text(next.name, "Continue");
                    page.Answers.Add(Ref<BlueprintAnswerBaseReference>(next));
                    continue;
                }
                for (int i = 0; i < node.Choices.Count; i++)
                {
                    var choice = node.Choices[i];
                    var answer = New<BlueprintAnswer>("answer." + scene.Id + "." + node.Id + "." + i);
                    InitializeAnswer(answer);
                    answer.Text = Text(answer.name, choice.Text);
                    var continuation = scene.ContactUnit == null ? null : scene;
                    answer.ShowConditions = Conditions(new RouteCondition { Choice = choice, Continuation = continuation });
                    answer.SelectConditions = Conditions(new RouteCondition { Choice = choice, Continuation = continuation });
                    answer.OnSelect = Actions(new RouteAction { Choice = choice, Continuation = continuation, Complete = !ending && choice.Next == null && choice.Check == null && !choice.Abort ? scene : null });
                    if (choice.Next != null) answer.NextCue = Cues(local[choice.Next]);
                    if (choice.Check != null)
                    {
                        var specification = choice.Check;
                        var roll = New<BlueprintCheck>("check." + scene.Id + "." + node.Id + "." + i);
                        roll.Conditions = continuation == null ? Conditions() : Conditions(new RouteCondition { Continuation = continuation });
                        roll.Type = (Kingmaker.EntitySystem.Stats.StatType)Enum.Parse(typeof(Kingmaker.EntitySystem.Stats.StatType), specification.Skill);
                        roll.DC = specification.DC;
                        roll.Hidden = false;
                        roll.BanPartyCheckInCamp = specification.CommanderOnly;
                        roll.Experience = DialogExperience.NoExperience;
                        Field(roll, "m_Success", Ref<BlueprintCueBaseReference>(local[specification.Success]));
                        Field(roll, "m_Fail", Ref<BlueprintCueBaseReference>(local[specification.Failure]));
                        if (specification.CommanderOnly)
                        {
                            var actor = new Kingmaker.Designers.EventConditionActionSystem.Evaluators.PlayerCharacter();
                            actor.Owner = roll;
                            Field(roll, "m_UnitEvaluator", actor);
                        }
                        answer.NextCue = Cues(roll);
                    }
                    page.Answers.Add(Ref<BlueprintAnswerBaseReference>(answer));
                }
                if (scene.ContactUnit != null)
                {
                    var leave = New<BlueprintAnswer>("answer." + scene.Id + "." + node.Id + ".contact_lost");
                    InitializeAnswer(leave);
                    leave.Text = Text(leave.name, "[The conversation can no longer continue. Leave.]");
                    leave.ShowConditions = Conditions(new RouteCondition { Continuation = scene, ContactLost = true });
                    page.Answers.Add(Ref<BlueprintAnswerBaseReference>(leave));
                }
            }
            var dialog = New<BlueprintDialog>("dialog." + scene.Id);
            dialog.Type = DialogType.Book;
            dialog.Conditions = Conditions();
            dialog.FirstCue = Cues(local[scene.Nodes[0].Id]);
            dialog.TurnPlayer = false;
            dialog.TurnFirstSpeaker = false;
            dialog.StartActions = Actions();
            dialog.FinishActions = Actions(new RouteAction { StopSpeech = true });
            dialogs.Add(scene.Id, dialog);
        }

        private static void BuildJournal(string id, Relationship relationship)
        {
            // Existing quest and objective GUIDs are already embedded in users' saves.
            string suffix = id == "tirabade" ? "" : "." + id;
            var quest = New<BlueprintQuest>("quest" + suffix);
            quest.Title = Text("quest" + suffix + ".title", relationship.Title);
            quest.Description = Text("quest" + suffix + ".description", relationship.Description);
            quest.CompletionText = Text("quest" + suffix + ".complete", "We have made our choice about the life we can share. The war will not make keeping that choice easy.");
            quest.OnSetAutoKingdom = Actions();
            Field(quest, "m_LastChapter", 6);
            // Use the Relations and Romances journal group registered by the parent mod.
            Field(quest, "m_Group", (Kingmaker.Enums.QuestGroupId)18);
            var objective = New<BlueprintQuestObjective>("objective" + suffix);
            objective.Title = Text("objective" + suffix + ".title", relationship.Objective);
            objective.Description = Text("objective" + suffix + ".description", relationship.Guidance);
            Field(objective, "m_Quest", Ref<BlueprintQuestReference>(quest));
            Field(objective, "m_FinishParent", true);
            Field(quest, "m_Objectives", new List<BlueprintQuestObjectiveReference> { Ref<BlueprintQuestObjectiveReference>(objective) });
            objectives.Add(id, objective);
        }

        internal static Snapshot State()
        {
            var player = Game.Instance.Player;
            var state = new Snapshot { Chapter = player.Chapter, Hour = (int)player.GameTime.TotalHours,
                Area = Game.Instance.CurrentlyLoadedArea?.AssetGuid.ToString() ?? "" };
            foreach (var flag in flags)
            {
                int value = player.UnlockableFlags.GetFlagValue(flag.Value);
                if (value > 0) state.Flags.Add(flag.Key);
                if (flag.Key.StartsWith("hour.", StringComparison.Ordinal) && value > 0) state.Times[flag.Key.Substring(5)] = value - 1;
            }
            foreach (var etude in etudes)
            {
                bool permanent = story.PermanentEtudes.Contains(etude.Key) || etude.Key.EndsWith("_dead", StringComparison.Ordinal) || etude.Key.EndsWith("_gone", StringComparison.Ordinal)
                    || etude.Key.StartsWith("ascend_", StringComparison.Ordinal) || etude.Key == "sacrifice" || etude.Key == "true_lich";
                // Started etudes can be dormant until their activation conditions pass.
                if (player.EtudesSystem.Etudes.GetFact(etude.Value)?.IsPlaying == true
                    || permanent && player.EtudesSystem.EtudeIsCompleted(etude.Value)) state.Flags.Add(etude.Key);
            }
            if (new[] { "irabeth_dead", "anevia_dead", "irabeth_gone", "anevia_gone", "sacrifice" }.Any(state.Has)) state.Flags.Add("loss");
            foreach (var quest in completedQuests)
                if (player.QuestBook.GetQuestState(quest.Value) == QuestState.Completed) state.Flags.Add(quest.Key);
            foreach (var etude in completedEtudes)
                if (player.EtudesSystem.EtudeIsCompleted(etude.Value)) state.Flags.Add(etude.Key);
            ReadDialogHistory(player.Dialog, state);
            foreach (var contact in contactUnits)
                if (NativeContact.IsAvailable(contact.Value)) state.AvailableContacts.Add(contact.Key);
            foreach (var revival in revivalUnits)
                if (Fate.CanRevive(revival.Value)) state.Flags.Add("revive." + revival.Key + ".available");
            if (new[] { "ascend_all", "ascend_alone", "ascend_areelu", "ascend_companions" }.Any(state.Has)) state.Flags.Add("ascended");
            if (state.Has("swarm") || state.Has("true_lich")) state.Flags.Add("inhuman");
            state.Flags.Add(player.Chapter == 1 ? "chapter_one" : "chapter_later");
            return state;
        }

        private static void ReadDialogHistory(DialogState dialog, Snapshot state)
        {
            foreach (var cue in seenCues)
                if (cue.Value.Any(dialog.ShownCues.Contains)) state.Flags.Add(cue.Key);
            foreach (var answer in selectedAnswers)
                if (dialog.SelectedAnswers.Contains(answer.Value)) state.Flags.Add(answer.Key);
            // Native ShownDialogs records start, not successful completion.
            foreach (var started in startedDialogs)
                if (dialog.ShownDialogs.Contains(started.Value)) state.Flags.Add(started.Key);
        }

        private static void Set(string key, int value = 1) => Game.Instance.Player.UnlockableFlags.SetFlagValue(flags[key], value);

        private static void ReportRecovery(string message)
        {
            if (recoveryMessage != message) entry.Logger.Log(message);
            recoveryMessage = message;
            recoveryPlayer = Game.Instance?.Player;
        }

        private static void RecordProgress(Choice? choice, Scene? complete)
        {
            foreach (var key in (choice?.Set ?? Array.Empty<string>()).Concat(complete == null ? Array.Empty<string>() : new[] { complete.Id }))
            {
                if (Game.Instance.Player.UnlockableFlags.GetFlagValue(flags[key]) > 0) continue;
                Set("hour." + key, (int)Game.Instance.Player.GameTime.TotalHours + 1);
                Set(key);
            }
            if (complete != null) entry.Logger.Log("Completed scene: " + complete.Id);
            var state = State();
            foreach (var pair in objectives)
            {
                var relationship = story.Relationships[pair.Key];
                if ((state.Has(relationship.ClosedFlag) || state.Has(relationship.CommittedFlag))
                    && Game.Instance.Player.QuestBook.GetObjectiveState(pair.Value) == QuestObjectiveState.Started)
                    Game.Instance.Player.QuestBook.CompleteObjective(pair.Value);
            }
        }

        private static void ReconcileRecoveries()
        {
            var messages = new List<string>();
            foreach (var pair in revivalUnits)
            {
                try
                {
                    var attempt = Fate.Pending(pair.Key);
                    if (attempt == null) continue;
                    var status = Fate.Inspect(pair.Value);
                    if (!attempt.IsRestored(status))
                    {
                        messages.Add(pair.Key + ": " + attempt.PendingReason(status));
                        continue;
                    }
                    var scene = story.Scenes.SingleOrDefault(s => s.Id == attempt.SceneId && s.Recovery == pair.Key);
                    var choice = scene?.Nodes.SelectMany(n => n.Choices).SingleOrDefault(c => c.Revive == pair.Key
                        && JsonConvert.SerializeObject(c) == attempt.ChoiceJson);
                    if (scene == null || choice == null)
                        throw new InvalidOperationException("The saved recovery action no longer matches the story: " + pair.Key);
                    RecordProgress(choice, scene);
                    Fate.Clear(pair.Key);
                    messages.Add("Verified the original companion's recovery and recorded the pending scene. Resurrection was not repeated.");
                }
                catch (Exception ex) { messages.Add("Recovery verification remains pending: " + ex.Message); }
            }
            if (messages.Count > 0) ReportRecovery(string.Join(Environment.NewLine, messages));
        }

        private static bool Idle() => Game.Instance?.Player != null && Game.Instance.DialogController?.Dialog == null
            && Game.Instance.Player.Dialog.Scheduled == null && !Game.Instance.Player.IsInCombat
            && Game.Instance.CurrentMode == GameModeType.Default;

        private static void Update()
        {
            if (Input.GetKey(KeyCode.LeftControl) && Input.GetKeyDown(KeyCode.S)) StopNarration();
            if (!initialized || !enabled || Time.realtimeSinceStartup < pollAt) return;
            pollAt = Time.realtimeSinceStartup + 0.3f;
            if (narrationPlayer != null && !ReferenceEquals(narrationPlayer, Game.Instance?.Player)) StopNarration();
            if (pendingPlayer != null && !ReferenceEquals(pendingPlayer, Game.Instance?.Player)) CancelPending();
            if (recoveryPlayer != null && !ReferenceEquals(recoveryPlayer, Game.Instance?.Player))
            {
                recoveryMessage = null;
                recoveryPlayer = null;
            }
            if (!Idle() || Game.Instance?.Player == null) return;
            ReconcileRecoveries();
            var state = State();
            foreach (var pair in objectives)
            {
                if (Game.Instance.Player.QuestBook.GetObjectiveState(pair.Value) == QuestObjectiveState.Started
                    && story.Relationships[pair.Key].FailureFlags.Any(state.Has)) Game.Instance.Player.QuestBook.FailObjective(pair.Value);
            }
            if (restPending && pending == null)
            {
                restPending = false;
                pending = Rules.NextRemote(story, state);
            }
            if (pending == null || Time.frameCount < pendingFrame) return;
            var scene = pending;
            pending = null;
            pendingPlayer = null;
            if (!Rules.Available(story, scene, State()) || Game.Instance?.Player == null) return;
            Set(story.Relationships[scene.Relationship].StartedFlag);
            var objective = objectives[scene.Relationship];
            if (Game.Instance.Player.QuestBook.GetObjectiveState(objective) == QuestObjectiveState.None) Game.Instance.Player.QuestBook.GiveObjective(objective);
            Game.Instance.DialogController.StartDialogWithoutTarget(dialogs[scene.Id], null);
        }

        private static void CancelPending()
        {
            pending = null;
            pendingPlayer = null;
            restPending = false;
            StopNarration();
        }

        private static void OnGUI(UnityModManager.ModEntry mod)
        {
            GUILayout.Label("Relations and Romances | Additional relationships");
            if (recoveryMessage != null && ReferenceEquals(recoveryPlayer, Game.Instance?.Player)) GUILayout.Label(recoveryMessage);
            bool narration = GUILayout.Toggle(settings.Narration, "Read new scenes aloud with the installed Windows voice");
            if (settings.Narration && !narration) StopNarration();
            settings.Narration = narration;
            if (GUILayout.Button("Stop narration")) StopNarration();
            GUILayout.Label("Windows narration is synthetic, not the original actors. Existing AI Voiceover lines are untouched.");
            if (error != null) { GUILayout.Label("Route initialization failed: " + error); return; }
            if (!initialized || Game.Instance?.Player == null) { GUILayout.Label("Load a main-campaign save after restarting the application once."); return; }
            var state = State();
            foreach (var pair in story.Relationships)
            {
                GUILayout.Label(pair.Value.Title);
                foreach (var scene in story.Scenes.Where(s => s.Relationship == pair.Key && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && Rules.Available(story, s, state)))
                {
                    GUILayout.Label(scene.Title + (scene.ManualOnly ? " | choose Read below" : Rules.IsRemote(scene) ? " | available at your next rest" : " | speak to " + (scene.Owner == "Together" ? "Anevia or Irabeth" : scene.Owner)));
                    if (Rules.IsRemote(scene) && Idle() && GUILayout.Button("Read: " + scene.Title)) Queue(scene);
                }
                if (state.Has(pair.Value.ClosedFlag)) GUILayout.Label("This relationship has ended.");
                else if (state.Has(pair.Value.CommittedFlag)) GUILayout.Label("You have chosen a relationship. Later meetings follow campaign progress.");
            }
            GUILayout.Label("If no meeting is listed, continue the campaign or allow a day or two between conversations.");
        }

        private static Sprite? Portrait(string key)
        {
            if (portraits.TryGetValue(key, out var sprite)) return sprite;
            string folder = Path.GetFullPath(Path.Combine(entry.Path, "..", "CustomNpcPortraits", "RanRomance-Tirabade"));
            string path = Path.Combine(folder, "Scenes", key + ".png");
            if (!File.Exists(path)) return null;
            var texture = new Texture2D(2, 2, TextureFormat.RGBA32, false);
            if (!ImageConversion.LoadImage(texture, File.ReadAllBytes(path))) { UnityEngine.Object.Destroy(texture); return null; }
            sprite = Sprite.Create(texture, new Rect(0, 0, texture.width, texture.height), new Vector2(0.5f, 0.5f));
            portraits.Add(key, sprite);
            return sprite;
        }

        private static void StopNarration()
        {
            narrationPlayer = null;
            try { if (narrator != null && !narrator.HasExited) narrator.StandardInput.WriteLine("STOP"); }
            catch (Exception ex) { entry.Logger.Log("Narrator stopped: " + ex.Message); }
        }

        // The Windows .NET helper owns SAPI. Unity's Mono does not reliably support COM speech.
        private static void Narrate(Node node)
        {
            try
            {
                StopNarration();
                if (!settings.Narration || !enabled) return;
                if (narrator == null || narrator.HasExited)
                {
                    narrator?.Dispose();
                    narrator = Process.Start(new ProcessStartInfo(Path.Combine(entry.Path, "Tirabade.Narrator.exe"))
                    { UseShellExecute = false, CreateNoWindow = true, WindowStyle = ProcessWindowStyle.Hidden, RedirectStandardInput = true });
                    if (narrator == null) throw new InvalidOperationException("Cannot start Windows narration helper.");
                    narrator.StandardInput.AutoFlush = true;
                }
                string text = Regex.Replace(node.Text, @"\{[^}]*\}|<[^>]*>", "");
                narrator.StandardInput.WriteLine((node.Speaker == "Irabeth" ? "-1" : "0") + " " + Convert.ToBase64String(Encoding.UTF8.GetBytes(text)));
                narrationPlayer = Game.Instance?.Player;
            }
            catch (Exception ex)
            {
                entry.Logger.Log("Narration unavailable: " + ex.Message);
                settings.Narration = false;
                narrator?.Dispose();
                narrator = null;
            }
        }

        public sealed class RouteCondition : Condition
        {
            public Scene? Scene;
            public Choice? Choice;
            public Scene? Continuation;
            public bool ContactLost;
            protected override string GetConditionCaption() => "Three at the Table availability";
            protected override bool CheckCondition() => enabled && initialized && Game.Instance?.Player != null
                && (Scene != null ? Rules.Available(story, Scene, State())
                    : ContactLost ? Continuation != null && !Rules.ContactAvailable(story, Continuation, State())
                    : Choice == null && Continuation != null ? Rules.ContactAvailable(story, Continuation, State())
                    : Choice != null && (Continuation == null || Rules.ContactAvailable(story, Continuation, State()))
                        && Rules.Match(Choice.Requires, Choice.Forbids, State()));
        }

        private static void Queue(Scene scene)
        {
            pending = scene;
            pendingPlayer = Game.Instance.Player;
            // StopDialog schedules UI disposal; wait until that old dialogue has finished closing.
            pendingFrame = Time.frameCount + 2;
        }

        public sealed class RouteAction : GameAction
        {
            public Scene? Start;
            public Scene? Complete;
            public Scene? Continuation;
            public Choice? Choice;
            public bool StopSpeech;
            public override string GetCaption() => "Three at the Table story action";
            public override void RunAction()
            {
                if (StopSpeech) { StopNarration(); return; }
                if (!enabled || !initialized) return;
                if (Start != null)
                {
                    if (Rules.Available(story, Start, State())) Queue(Start);
                    return;
                }
                if (Choice != null)
                {
                    if (Continuation != null && !Rules.ContactAvailable(story, Continuation, State())) return;
                    if (!Rules.Match(Choice.Requires, Choice.Forbids, State())) return;
                    if (Choice.Revive != null)
                    {
                        if (Complete == null || !Rules.Available(story, Complete, State())) return;
                        bool restored = Fate.TryRevive(Choice.Revive, revivalUnits[Choice.Revive], Complete, Choice, out var message);
                        ReportRecovery(message);
                        if (!restored) return;
                    }
                }
                RecordProgress(Choice, Complete);
                if (Choice?.Revive != null) Fate.Clear(Choice.Revive);
            }
        }

        [HarmonyPatch(typeof(BlueprintsCache), nameof(BlueprintsCache.Init))]
        private static class CachePatch
        {
            [HarmonyPostfix, HarmonyPriority(Priority.Last), HarmonyAfter("RanRomance")]
            private static void Postfix() => Build();
        }

        [HarmonyPatch(typeof(BookEventVM), "SetPage")]
        private static class BookPatch
        {
            [HarmonyPostfix]
            private static void Postfix(BookEventVM __instance, BlueprintBookPage page)
            {
                if (!pages.TryGetValue(page.AssetGuid.ToString(), out var node)) return;
                var portrait = Portrait(node.Portrait.Length > 0 ? node.Portrait : node.Speaker == "Narrator" ? "Together" : node.Speaker);
                if (portrait != null) __instance.EventPicture.Value = portrait;
                Narrate(node);
            }
        }

        [HarmonyPatch(typeof(DialogController), nameof(DialogController.StopDialog))]
        private static class StopPatch
        {
            [HarmonyPrefix]
            private static void Prefix(DialogController __instance)
            {
                if (__instance.Dialog?.name.StartsWith("RRT_", StringComparison.Ordinal) == true) StopNarration();
            }
        }

        [HarmonyPatch(typeof(RestController), nameof(RestController.Stop))]
        private static class RestPatch
        {
            [HarmonyPrefix]
            private static void Prefix(RestController __instance)
            {
                if (!initialized || !enabled || !__instance.Status.RestSucceeded || Game.Instance?.Player == null) return;
                restPending = true;
                pendingPlayer = Game.Instance.Player;
            }
        }
    }
}
