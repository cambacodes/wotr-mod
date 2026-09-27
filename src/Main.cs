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
using Kingmaker.EntitySystem.Persistence;
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
        // E8: letters per rest; 0 uses Story.PostBagSize.
        public int PostBagSize;
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
        // E10 read-only readers (never written).
        private static readonly Dictionary<string, BlueprintUnlockableFlag> nativeFlags = new Dictionary<string, BlueprintUnlockableFlag>();
        private static readonly Dictionary<string, KeyValuePair<BlueprintQuestObjective, QuestObjectiveState>> nativeObjectives =
            new Dictionary<string, KeyValuePair<BlueprintQuestObjective, QuestObjectiveState>>();
        private static readonly Dictionary<string, Kingmaker.Blueprints.Items.BlueprintItem> nativeItems = new Dictionary<string, Kingmaker.Blueprints.Items.BlueprintItem>();
        private static readonly Dictionary<string, BlueprintQuest> startedQuests = new Dictionary<string, BlueprintQuest>();
        // E12 returned presences, and the last status line logged for each.
        private static readonly List<GuestPresence> presences = new List<GuestPresence>();
        private static readonly List<NativeEpilogueEdit.Plan> nativeEditPlans = new List<NativeEpilogueEdit.Plan>();
        private static readonly Dictionary<string, string> presenceStatus = new Dictionary<string, string>(StringComparer.Ordinal);
        private static readonly Dictionary<string, BlueprintUnit> revivalUnits = new Dictionary<string, BlueprintUnit>();
        private static readonly Dictionary<string, BlueprintUnit> contactUnits = new Dictionary<string, BlueprintUnit>();
        private static string? recoveryMessage;
        private static object? recoveryPlayer;
        private static readonly List<SimpleBlueprint> registered = new List<SimpleBlueprint>();
        private static readonly Dictionary<string, BlueprintQuestObjective> objectives = new Dictionary<string, BlueprintQuestObjective>();
        private static Process? narrator;
        private static float pollAt;
        private static bool restPending;
        private static readonly PostBag postBag = new PostBag();
        private static object? postBagPlayer;
        private static int BagSize() => settings.PostBagSize > 0 ? settings.PostBagSize : story.PostBagSize;
        private static KonomiMeeting? konomiMeeting;
        private static IrabethMeeting? irabethMeeting;
        private static NurahMeeting? nurahMeeting;
        private static NurahInteraction? nurahInteraction;
        private static BlueprintDialog? nurahHub;
        private static ParentEndingIntegration? parentEndings;
        // Relationships whose native dependencies failed to resolve. Their blueprints stay registered for save safety,
        // but they offer no entries, letters or endings until the dependency is available again.
        private static readonly HashSet<string> degraded = new HashSet<string>(StringComparer.Ordinal);
        private static readonly List<string> warnings = new List<string>();
        internal const string KonomiMeetingRetry = "konomi.return_meeting_retry";
        internal const string IrabethMeetingRetry = "irabeth.return_meeting_retry";
        internal const string NurahMeetingRetry = "nurah.private_meeting_retry";

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
                    konomiMeeting?.Tick();
                    irabethMeeting?.Tick();
                    nurahMeeting?.Tick();
                    nurahInteraction?.Tick();
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
        // Phase 1 resolves native references without throwing and records what is missing.
        // Phase 2 always registers every blueprint a save can reference (flags, quests, cues, pages, answers, dialogs, etudes).
        // Phase 3 attaches to native content per relationship; a missing dependency degrades only its own relationship.
        private static void Build()
        {
            if (initialized || error != null) return;
            try
            {
                // ---------- Phase 1: resolve native references (never throws for a missing binding) ----------
                var missingKeys = new HashSet<string>(StringComparer.Ordinal);
                T? Resolve<T>(string guid, string what) where T : SimpleBlueprint
                {
                    try { return Get<T>(guid); }
                    catch (Exception ex) { warnings.Add(what + ": " + ex.Message); return null; }
                }
                void Degrade(string relationship, string reason)
                {
                    if (degraded.Add(relationship)) warnings.Add("Relationship '" + relationship + "' disabled: " + reason);
                }
                var targets = new Dictionary<string, BlueprintAnswersList>();
                foreach (var id in story.Scenes.SelectMany(Rules.EntryTargets).Distinct())
                {
                    var list = Resolve<BlueprintAnswersList>(id, "Dialogue attachment " + id);
                    if (list != null) targets.Add(id, list);
                }
                foreach (var scene in story.Scenes)
                    foreach (var id in Rules.EntryTargets(scene).Where(id => !targets.ContainsKey(id)))
                        Degrade(scene.Relationship, "dialogue attachment " + id + " is missing (scene " + scene.Id + ")");
                foreach (var scene in story.Scenes.Where(s => s.NativeReturnCue != null))
                {
                    var nativeReturn = Resolve<BlueprintCue>(scene.NativeReturnCue!, "Native audience return " + scene.Id);
                    if (nativeReturn == null || !targets.TryGetValue(scene.AnswerLists.Single(), out var returnList))
                    {
                        Degrade(scene.Relationship, "native audience return for " + scene.Id + " is missing");
                        continue;
                    }
                    if (nativeReturn.ShowOnce || nativeReturn.ShowOnceCurrentDialog || nativeReturn.Conditions.Conditions.Length != 0
                        || nativeReturn.OnShow.Actions.Length != 0 || nativeReturn.OnStop.Actions.Length != 0
                        || nativeReturn.Continue.Cues.Count != 0 || nativeReturn.Experience != DialogExperience.NoExperience
                        || nativeReturn.AlignmentShift.Value != 0 || returnList.ShowOnce || returnList.Conditions.Conditions.Length != 0
                        || returnList.MythicRequirement != default || returnList.AlignmentRequirement != default
                        || nativeReturn.Answers.Count != 1 || !ReferenceEquals(nativeReturn.Answers[0].Get(), returnList))
                        Degrade(scene.Relationship, "Native audience return must reopen its answer list without replaying actions: " + scene.Id);
                }
                // E14e: every parent must be a native cue whose Continue(First) holds the anchor cue, or the scene's relationship is disabled.
                var continueParents = new Dictionary<Scene, BlueprintCue[]>();
                foreach (var scene in story.Scenes.Where(s => s.ContinueBefore != null))
                {
                    var spec = scene.ContinueBefore!;
                    var parents = spec.Parents.Select(id => Resolve<BlueprintCue>(id, "Continue parent " + scene.Id)).ToArray();
                    var anchor = BlueprintGuid.Parse(spec.Cue);
                    if (parents.Any(parent => parent == null || parent.Continue?.Cues == null || parent.Continue.Strategy != Strategy.First
                        || parent.Continue.Cues.Count(reference => reference.Guid == anchor) != 1))
                        Degrade(scene.Relationship, "continue-before parents of " + scene.Id + " are missing or no longer continue First into " + spec.Cue);
                    else continueParents.Add(scene, parents!);
                }
                // E14d: native epilogue edits need their exact reviewed evidence, or their replacement relationship is disabled.
                var nativeEditSources = new Dictionary<string, (BlueprintCue Cue, BlueprintBookPage Page)>();
                foreach (var pair in story.NativeEpilogueEdits)
                {
                    var owner = story.Scenes.First(s => s.Id == pair.Value.Replacement).Relationship;
                    string? refusal;
                    try { refusal = NativeEpilogueEdit.Check(pair.Key, pair.Value, id => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(id)),
                        ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse("ced82f299d246f448b48afa0b630dd70")) as BlueprintCueSequence); }
                    catch (Exception ex) { refusal = ex.Message; }
                    if (refusal != null) Degrade(owner, "native epilogue edit " + pair.Key + ": " + refusal);
                    else nativeEditSources[pair.Key] = ((BlueprintCue)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(pair.Key))!,
                        (BlueprintBookPage)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(pair.Value.Page))!);
                }
                // E12: a presence needs its native unit, area and host lists, or its relationship is disabled.
                foreach (var pair in story.Presences)
                {
                    string relationship = pair.Key.Substring(0, pair.Key.Length - ".presence".Length);
                    var unit = Resolve<BlueprintUnit>(pair.Value.Unit, "Presence unit " + pair.Key);
                    // E12b: a NearUnit anchor must be a native unit; a wrong one disables only this presence.
                    if (pair.Value.At?.NearUnit != null && Resolve<BlueprintUnit>(pair.Value.At.NearUnit, "Presence anchor " + pair.Key) == null)
                    {
                        warnings.Add("Presence " + pair.Key + " disabled: its anchor unit " + pair.Value.At.NearUnit + " is not a BlueprintUnit.");
                        continue;
                    }
                    var area = Resolve<BlueprintArea>(pair.Value.Area, "Presence area " + pair.Key);
                    var hosts = pair.Value.AnswerLists.Select(id => Resolve<BlueprintAnswersList>(id, "Presence answer list " + pair.Key)).ToArray();
                    if (unit == null || area == null || hosts.Any(list => list == null)) Degrade(relationship, "presence " + pair.Key + " is missing native data");
                    else presences.Add(new GuestPresence(pair.Key, pair.Value, unit));
                }
                // E11: a whitelisted removable item must resolve, or the relationships that remove it are disabled.
                foreach (string guid in story.RemovableItems)
                    if (Resolve<Kingmaker.Blueprints.Items.BlueprintItem>(guid, "Removable item " + guid) == null)
                        foreach (var scene in story.Scenes.Where(s => s.Nodes.SelectMany(n => n.Choices).Any(c => c.RemoveItem == guid)))
                            Degrade(scene.Relationship, "removable item " + guid + " for " + scene.Id + " is missing");
                // E5: a native continuation must resolve to a BlueprintCue, or its relationship is disabled.
                foreach (var scene in story.Scenes)
                    foreach (var guid in scene.Nodes.SelectMany(n => n.Choices).Select(c => c.NativeNext).OfType<string>().Distinct())
                        if (Resolve<BlueprintCue>(guid, "Native continuation " + scene.Id) == null)
                            Degrade(scene.Relationship, "native continuation " + guid + " for " + scene.Id + " is missing or not a cue");
                var epilogue = Resolve<BlueprintCueSequence>("ed4baeaf69394754902344f0598d7e5a", "Parent epilogue sequence (RanRomance)");
                var aeon = Resolve<BlueprintCueSequence>("ced82f299d246f448b48afa0b630dd70", "Native Aeon epilogue sequence");
                var expanded = ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse("2b9424b1b93e4d0896b0958db79d2339"));
                if (expanded != null && !(expanded is BlueprintCueSequence))
                    warnings.Add("Optional parent epilogue has the wrong type: 2b9424b1b93e4d0896b0958db79d2339; it is ignored.");
                var expandedEpilogue = expanded as BlueprintCueSequence;
                // E14a: native sequence targets. A missing sequence or anchor disables only the relationships that use it.
                var nativeSequences = new Dictionary<string, BlueprintCueSequence>();
                foreach (var scene in story.Scenes.Where(s => s.EpilogueSequence != null))
                {
                    string name = scene.EpilogueSequence!;
                    if (!nativeSequences.TryGetValue(name, out var target))
                    {
                        target = Resolve<BlueprintCueSequence>(Rules.PlayerFinalChoice, "Native epilogue sequence " + name)!;
                        if (target != null) nativeSequences.Add(name, target);
                    }
                    if (target == null || !scene.EpilogueAfter!.StartsWith("scene:", StringComparison.Ordinal)
                        && !target.Cues.Any(reference => reference.Guid == BlueprintGuid.Parse(scene.EpilogueAfter)))
                        Degrade(scene.Relationship, "native epilogue anchor " + scene.EpilogueAfter + " for " + scene.Id + " is missing from " + name);
                }
                if (nativeSequences.Count > 0 && Harmony.HasAnyPatches("RanEpilogue"))
                    warnings.Add("RanEpilogue is installed and patches epilogues; pages placed in PlayerFinalChoice may interleave with its changes.");
                foreach (var pair in story.Etudes)
                    if (Resolve<BlueprintEtude>(pair.Value, "Etude " + pair.Key) is BlueprintEtude e) etudes.Add(pair.Key, e); else missingKeys.Add(pair.Key);
                foreach (var pair in story.CompletedQuests)
                    if (Resolve<BlueprintQuest>(pair.Value, "Quest " + pair.Key) is BlueprintQuest q) completedQuests.Add(pair.Key, q); else missingKeys.Add(pair.Key);
                foreach (var pair in story.SeenCues)
                {
                    var cues = pair.Value.Select(id => Resolve<BlueprintCue>(id, "Seen cue " + pair.Key)).ToArray();
                    if (cues.All(c => c != null)) seenCues.Add(pair.Key, cues!); else missingKeys.Add(pair.Key);
                }
                foreach (var pair in story.SelectedAnswers)
                    if (Resolve<BlueprintAnswer>(pair.Value, "Selected answer " + pair.Key) is BlueprintAnswer a) selectedAnswers.Add(pair.Key, a); else missingKeys.Add(pair.Key);
                foreach (var pair in story.StartedDialogs)
                    if (Resolve<BlueprintDialog>(pair.Value, "Started dialog " + pair.Key) is BlueprintDialog d) startedDialogs.Add(pair.Key, d); else missingKeys.Add(pair.Key);
                foreach (var pair in story.CompletedEtudes)
                    if (Resolve<BlueprintEtude>(pair.Value, "Completed etude " + pair.Key) is BlueprintEtude c) completedEtudes.Add(pair.Key, c); else missingKeys.Add(pair.Key);
                foreach (var pair in story.UnlockableFlags)
                    if (Resolve<BlueprintUnlockableFlag>(pair.Value, "Native flag " + pair.Key) is BlueprintUnlockableFlag nf) nativeFlags.Add(pair.Key, nf); else missingKeys.Add(pair.Key);
                foreach (var pair in story.QuestObjectives)
                    if (Resolve<BlueprintQuestObjective>(pair.Value[0], "Quest objective " + pair.Key) is BlueprintQuestObjective qo)
                        nativeObjectives.Add(pair.Key, new KeyValuePair<BlueprintQuestObjective, QuestObjectiveState>(qo,
                            (QuestObjectiveState)Enum.Parse(typeof(QuestObjectiveState), pair.Value[1])));
                    else missingKeys.Add(pair.Key);
                foreach (var pair in story.InventoryItems)
                    if (Resolve<Kingmaker.Blueprints.Items.BlueprintItem>(pair.Value, "Inventory item " + pair.Key) is Kingmaker.Blueprints.Items.BlueprintItem it) nativeItems.Add(pair.Key, it);
                    else missingKeys.Add(pair.Key);
                foreach (var pair in story.StartedQuests)
                    if (Resolve<BlueprintQuest>(pair.Value, "Started quest " + pair.Key) is BlueprintQuest sq) startedQuests.Add(pair.Key, sq); else missingKeys.Add(pair.Key);
                foreach (var pair in story.Revivals)
                    if (Resolve<BlueprintUnit>(pair.Value.Unit, "Revival unit " + pair.Key) is BlueprintUnit u) revivalUnits.Add(pair.Key, u);
                    else Degrade(pair.Value.Relationship, "revival unit for " + pair.Key + " is missing");
                foreach (var guid in story.Scenes.Where(s => s.ContactUnit != null).SelectMany(s => new[] { s.ContactUnit! }.Concat(s.AdditionalContactUnits)).Distinct())
                    if (Resolve<BlueprintUnit>(guid, "Contact unit " + guid) is BlueprintUnit u) contactUnits.Add(guid, u);
                foreach (var scene in story.Scenes.Where(s => s.ContactUnit != null))
                    if (new[] { scene.ContactUnit! }.Concat(scene.AdditionalContactUnits).Any(guid => !contactUnits.ContainsKey(guid)))
                        Degrade(scene.Relationship, "contact unit for " + scene.Id + " is missing");
                // Derived flags inherit a missing input: a missing death etude must not read as "alive".
                if (new[] { "irabeth_dead", "anevia_dead", "irabeth_gone", "anevia_gone", "sacrifice" }.Any(missingKeys.Contains)) missingKeys.Add("loss");
                if (new[] { "ascend_all", "ascend_alone", "ascend_areelu", "ascend_companions" }.Any(missingKeys.Contains)) missingKeys.Add("ascended");
                if (missingKeys.Contains("swarm") || missingKeys.Contains("true_lich")) missingKeys.Add("inhuman");
                Rules.PropagateMissing(story, missingKeys);
                if (missingKeys.Count > 0)
                {
                    foreach (var scene in story.Scenes)
                    {
                        var uses = scene.Requires.Concat(scene.RequiresAny).Concat(scene.RequiresAnyGroups.SelectMany(g => g)).Concat(scene.Forbids)
                            .Concat(scene.ForbidOverrides.Values).Concat(scene.Nodes.SelectMany(n => n.Choices).SelectMany(ch => ch.Requires.Concat(ch.Forbids)));
                        var hit = uses.FirstOrDefault(missingKeys.Contains);
                        if (hit != null) Degrade(scene.Relationship, "native state '" + hit + "' is unavailable (scene " + scene.Id + ")");
                    }
                    foreach (var pair in story.Relationships)
                    {
                        var hit = pair.Value.UnavailableFlags.Concat(pair.Value.FailureFlags).FirstOrDefault(missingKeys.Contains);
                        if (hit != null) Degrade(pair.Key, "native state '" + hit + "' is unavailable");
                    }
                }

                // ---------- Phase 2: register every save-referenced blueprint, unconditionally ----------
                var effects = story.Scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).Distinct().ToArray();
                var keys = story.Scenes.Select(s => s.Id).Concat(story.Scenes.Select(s => "hour." + s.Id))
                    .Concat(effects).Concat(effects.Select(key => "hour." + key))
                    .Concat(story.Relationships.Values.SelectMany(r => new[] { r.StartedFlag, r.ClosedFlag, r.CommittedFlag })).Distinct();
                foreach (var key in keys) flags.Add(key, New<BlueprintUnlockableFlag>("flag." + key));
                foreach (string key in new[] { KonomiMeetingRetry, IrabethMeetingRetry, "irabeth.return_meeting_accepted", "hour.irabeth.return_meeting_accepted",
                    "irabeth.return_meeting_declined", "irabeth.return_reply", "irabeth.return_first_words", NurahMeetingRetry })
                    if (!flags.ContainsKey(key)) flags.Add(key, New<BlueprintUnlockableFlag>("flag." + key));
                foreach (string key in story.Relationships.Keys.Select(key => Rules.ServedPrefix + key))
                    if (!flags.ContainsKey(key)) flags.Add(key, New<BlueprintUnlockableFlag>("flag." + key));
                // E1: each latch is an ordinary authored flag (with its hour) recorded by Update().
                foreach (string key in story.Latches.Keys.SelectMany(key => new[] { key, "hour." + key }))
                    if (!flags.ContainsKey(key)) flags.Add(key, New<BlueprintUnlockableFlag>("flag." + key));
                var konomiEtude = New<BlueprintEtude>("etude.konomi.personal_return");
                var irabethEtude = New<BlueprintEtude>("etude.irabeth.personal_return");
                var nurahEtude = New<BlueprintEtude>("etude.nurah.private_meeting");
                foreach (var relationship in story.Relationships) BuildJournal(relationship.Key, relationship.Value);
                foreach (var scene in story.Scenes)
                    if (scene.ReturnToList) BuildReturnToList(scene);
                    else if (scene.ContinueBefore != null) BuildContinueBefore(scene);
                    else BuildScene(scene);
                foreach (var scene in story.Scenes)
                {
                    // Entry answers are recorded in dialogue history, so they exist even when their relationship is degraded.
                    if (scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal) || Rules.IsRemote(scene) || scene.InteractionHub != null
                        || scene.ReturnToList || scene.ContinueBefore != null) continue;
                    var answer = New<BlueprintAnswer>("entry." + scene.Id);
                    InitializeAnswer(answer);
                    answer.Text = Text("entry." + scene.Id, scene.Entry);
                    answer.ShowConditions = Conditions(new RouteCondition { Scene = scene });
                    // SelectConditions are also checked when ToyBox displays unavailable answers.
                    answer.SelectConditions = Conditions(new RouteCondition { Scene = scene });
                    if (scene.NativeReturnCue != null)
                        answer.NextCue = Cues(Get<BlueprintCue>(GuidFor("cue." + scene.Id + "." + scene.Nodes[0].Id).ToString()));
                    else
                        answer.OnSelect = Actions(new RouteAction { Start = scene });
                    // E13: the entry itself can be a native [Trickster] answer or shift alignment (same shape as E5 choices).
                    if (scene.EntryMythic != null || scene.EntryAlignment != null)
                        ConfigureNativeEffects(answer, new Choice { Mythic = scene.EntryMythic, Alignment = scene.EntryAlignment }, warnings.Add);
                }
                if (story.Scenes.Any(Rules.IsNurahHubScene)) nurahHub = BuildNurahHub();
                // E14d: every replacement cue is registered (save names); only verified edits get their native presentation.
                foreach (var pair in story.NativeEpilogueEdits)
                {
                    var scene = story.Scenes.First(s => s.Id == pair.Value.Replacement);
                    var replacement = New<BlueprintCue>("native-edit." + pair.Key);
                    replacement.Text = Text("native-edit." + pair.Key, scene.Nodes[0].Text);
                    var when = pair.Value.When;
                    Func<bool> applies = () => enabled && initialized && Game.Instance?.Player != null && Rules.WhenHolds(when, State());
                    if (nativeEditSources.TryGetValue(pair.Key, out var source))
                        nativeEditPlans.Add(NativeEpilogueEdit.Prepare(pair.Key, pair.Value, source.Cue, source.Page, replacement, applies));
                    else
                    {
                        replacement.Conditions = Conditions();
                        replacement.OnShow = Actions();
                        replacement.OnStop = Actions();
                        replacement.Continue = Cues();
                    }
                }

                // ---------- Phase 3: optional helpers and native attachment, each isolated ----------
                T? Optional<T>(string what, Func<T?> create) where T : class
                {
                    try { return create(); }
                    catch (Exception ex) { warnings.Add(what + " unavailable: " + ex.Message); entry.Logger.LogException(ex); return null; }
                }
                konomiMeeting = Optional("Konomi meeting", () => new KonomiMeeting(konomiEtude, CurrentKonomiVisit, Get<SimpleBlueprint>));
                irabethMeeting = Optional("Irabeth meeting", () => new IrabethMeeting(irabethEtude, CurrentIrabethVisit, Get<SimpleBlueprint>));
                nurahMeeting = Optional("Nurah meeting", () => new NurahMeeting(nurahEtude, CurrentNurahVisit, Get<SimpleBlueprint>));
                if (nurahHub != null && nurahMeeting != null)
                    nurahInteraction = Optional("Nurah hub", () => new NurahInteraction(nurahMeeting, nurahHub, CanOpenNurahHub));
                // Relationships whose endings are rewritten through the parent's epilogue; without the integration
                // their own pages are withheld so they cannot contradict the parent's unmodified slides.
                var parentOwned = new HashSet<string>(story.ParentEpilogueLossRules.SelectMany(r => r.ReplacementScenes)
                    .Select(id => story.Scenes.FirstOrDefault(s => s.Id == id)?.Relationship).OfType<string>(), StringComparer.Ordinal);
                if (epilogue != null && aeon != null && (story.ParentEpilogueEdits.Count > 0 || story.ParentEpilogueLossRules.Count > 0))
                    parentEndings = Optional("Parent ending integration", () => ParentEndingIntegration.Prepare(story, epilogue, aeon, Get<SimpleBlueprint>,
                        id => New<BlueprintCue>(id), () => initialized && enabled ? State() : null));
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
                bool parentAttached = parentEndings != null
                    && Optional<object>("Parent ending attachment", () => { parentEndings!.Attach(); return new object(); }) != null;
                if (!parentAttached) parentEndings = null;
                foreach (var scene in story.Scenes)
                {
                    if (degraded.Contains(scene.Relationship)) continue;
                    if (scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
                    {
                        if (Rules.IsNativeReplacement(story, scene)) continue;   // E14d: shown only in place of its native cue
                        var sequence = scene.EpilogueSequence != null ? nativeSequences.TryGetValue(scene.EpilogueSequence, out var native) ? native : null
                            : scene.Owner == "AeonEpilogue" ? aeon : epilogue;
                        if (sequence == null || !parentAttached && parentOwned.Contains(scene.Relationship)) continue;
                        var page = Ref<BlueprintCueBaseReference>(Get<BlueprintBookPage>(GuidFor("page." + scene.Id + "." + scene.Nodes[0].Id).ToString()));
                        string? after = Rules.EpilogueAnchor(story, scene.EpilogueAfter, name => GuidFor(name).ToString());
                        if (!InsertEpiloguePage(sequence.Cues, page, after))
                            warnings.Add("Epilogue anchor " + scene.EpilogueAfter + " is not in the sequence; " + scene.Id + " was appended.");
                        if (scene.Owner != "AeonEpilogue" && scene.EpilogueSequence == null && expandedEpilogue != null)
                            InsertEpiloguePage(expandedEpilogue.Cues, page, after);
                        continue;
                    }
                    if (Rules.IsRemote(scene) || scene.InteractionHub != null) continue;
                    foreach (var id in Rules.EntryTargets(scene))
                    {
                        var answer = Get<BlueprintAnswer>(GuidFor(scene.ReturnToList ? "entry." + scene.Id + "." + id : "entry." + scene.Id).ToString());
                        targets[id].Answers.Insert(Math.Max(0, targets[id].Answers.Count - 1), Ref<BlueprintAnswerBaseReference>(answer));
                    }
                }
                foreach (var pair in continueParents)
                {
                    if (degraded.Contains(pair.Key.Relationship)) continue;
                    var line = Ref<BlueprintCueBaseReference>(Get<BlueprintCue>(GuidFor("cue." + pair.Key.Id + ".continue").ToString()));
                    var anchor = BlueprintGuid.Parse(pair.Key.ContinueBefore!.Cue);
                    foreach (var parent in pair.Value) InsertContinueBefore(parent, line, anchor);
                }
                foreach (var plan in nativeEditPlans)
                {
                    var relationship = story.Scenes.First(s => s.Id == plan.Spec.Replacement).Relationship;
                    if (degraded.Contains(relationship)) continue;
                    var when = plan.Spec.When;
                    Optional<object>("Native epilogue edit " + plan.CueId, () =>
                    {
                        NativeEpilogueEdit.Attach(plan, Ref<BlueprintCueBaseReference>(plan.Replacement),
                            () => enabled && initialized && Game.Instance?.Player != null && Rules.WhenHolds(when, State()));
                        return new object();
                    });
                }
                if (epilogue == null) warnings.Add("Epilogue pages are not shown: the RanRomance parent epilogue is missing.");
                initialized = true;
                entry.Logger.Log("Registered " + story.Scenes.Count + " scenes. Existing dialogue answers and finish actions preserved."
                    + (warnings.Count == 0 ? "" : " " + warnings.Count + " integration warning(s); disabled relationships: "
                        + (degraded.Count == 0 ? "none" : string.Join(", ", degraded.OrderBy(r => r))) + "."));
                foreach (var warning in warnings) entry.Logger.Log("Integration warning: " + warning);
            }
            catch (Exception ex) { error = ex.Message; entry.Logger.LogException(ex); }
        }

        // ER-3: pages anchored after a native page follow it (and the RRT pages already placed after it, keeping authored order).
        private static readonly HashSet<BlueprintCueBaseReference> anchoredPages = new HashSet<BlueprintCueBaseReference>();

        internal static bool InsertEpiloguePage(List<BlueprintCueBaseReference> cues, BlueprintCueBaseReference page, string? after)
        {
            int at = after == null ? -1 : cues.FindIndex(reference => reference.Guid == BlueprintGuid.Parse(after));
            if (at < 0)
            {
                cues.Add(page);
                return after == null;
            }
            int index = at + 1;
            while (index < cues.Count && anchoredPages.Contains(cues[index])) index++;
            cues.Insert(index, page);
            anchoredPages.Add(page);
            return true;
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
            var local = new Dictionary<string, BlueprintCueBase>();
            bool inline = scene.NativeReturnCue != null;
            var nativeReturn = inline ? ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(scene.NativeReturnCue!)) as BlueprintCue : null;
            foreach (var node in scene.Nodes)
            {
                string id = scene.Id + "." + node.Id;
                var cue = New<BlueprintCue>("cue." + id);
                cue.Conditions = Conditions();
                cue.OnShow = Actions();
                cue.OnStop = Actions();
                cue.Speaker = inline ? InlineSpeaker(node, nativeReturn != null && node.Speaker == scene.Owner ? nativeReturn.Speaker : null)
                    : new DialogSpeaker { NoSpeaker = true, MoveCamera = false };
                cue.TurnSpeaker = false;
                cue.Continue = Cues();
                cue.Text = Text("cue." + id, node.Text);
                if (inline)
                {
                    cue.ShowOnce = false;
                    local.Add(node.Id, cue);
                    continue;
                }
                var page = New<BlueprintBookPage>("page." + id);
                page.ShowOnce = scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal);
                page.Conditions = scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal) ? Conditions(new RouteCondition { Scene = scene }) : Conditions();
                page.OnShow = Actions();
                page.Title = Text("title." + id, scene.Title);
                // E14c: a textless paragraph node keeps its (registered) base cue off the page.
                if (!string.IsNullOrWhiteSpace(node.Text)) page.Cues.Add(Ref<BlueprintCueBaseReference>(cue));
                for (int p = 0; p < node.Paragraphs.Count; p++)
                {
                    var paragraph = New<BlueprintCue>("cue." + id + ".p" + p);
                    paragraph.Conditions = Conditions(new ParagraphCondition { Paragraph = node.Paragraphs[p] });
                    paragraph.OnShow = Actions();
                    paragraph.OnStop = Actions();
                    paragraph.Speaker = new DialogSpeaker { NoSpeaker = true, MoveCamera = false };
                    paragraph.TurnSpeaker = false;
                    paragraph.Continue = Cues();
                    paragraph.Text = Text("cue." + id + ".p" + p, node.Paragraphs[p].Text);
                    page.Cues.Add(Ref<BlueprintCueBaseReference>(paragraph));
                }
                local.Add(node.Id, page);
                pages.Add(page.AssetGuid.ToString(), node);
            }
            foreach (var node in scene.Nodes)
            {
                var page = local[node.Id];
                var answers = page is BlueprintBookPage book ? book.Answers : ((BlueprintCue)page).Answers;
                bool ending = scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal);
                var continuation = !ending && (scene.ContactUnit != null || Rules.IsRemote(scene)) ? scene : null;
                // Preserve saved terminal answer IDs while building authored ending branches normally.
                if (ending && node.Choices.Count == 1 && node.Choices[0].Next == null && node.Choices[0].Check == null
                    && node.Choices[0].Requires.Length == 0 && node.Choices[0].Forbids.Length == 0
                    && node.Choices[0].Set.Length == 0 && node.Choices[0].Text == "Continue"
                    && !node.Choices[0].Abort && node.Choices[0].Revive == null)
                {
                    var next = New<BlueprintAnswer>("answer." + scene.Id + "." + node.Id + ".continue");
                    InitializeAnswer(next);
                    next.Text = Text(next.name, "Continue");
                    answers.Add(Ref<BlueprintAnswerBaseReference>(next));
                    continue;
                }
                for (int i = 0; i < node.Choices.Count; i++)
                {
                    var choice = node.Choices[i];
                    var answer = New<BlueprintAnswer>("answer." + scene.Id + "." + node.Id + "." + i);
                    InitializeAnswer(answer);
                    answer.Text = Text(answer.name, choice.Text);
                    answer.ShowConditions = Conditions(new RouteCondition { Choice = choice, Continuation = continuation });
                    answer.SelectConditions = Conditions(new RouteCondition { Choice = choice, Continuation = continuation });
                    answer.OnSelect = Actions(new RouteAction { Choice = choice, Continuation = continuation, Complete = !ending && choice.Next == null && choice.Check == null && !choice.Abort ? scene : null });
                    if (choice.Next != null) answer.NextCue = Cues(local[choice.Next]);
                    else if (choice.NativeNext != null && choice.Check == null)
                        // A missing target degraded the relationship in phase 1; keep the saved answer resolvable.
                        answer.NextCue = ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(choice.NativeNext)) is BlueprintCue next
                            ? Cues(next) : nativeReturn != null ? Cues(nativeReturn) : Cues();
                    else if (nativeReturn != null && choice.Check == null) answer.NextCue = Cues(nativeReturn);
                    ConfigureNativeEffects(answer, choice, warnings.Add);
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
                    answers.Add(Ref<BlueprintAnswerBaseReference>(answer));
                }
                if (continuation != null)
                {
                    var leave = New<BlueprintAnswer>("answer." + scene.Id + "." + node.Id + ".contact_lost");
                    InitializeAnswer(leave);
                    leave.Text = Text(leave.name, "[The conversation can no longer continue. Leave.]");
                    leave.ShowConditions = Conditions(new RouteCondition { Continuation = scene, ContactLost = true });
                    answers.Add(Ref<BlueprintAnswerBaseReference>(leave));
                }
            }
            if (inline) return;
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

        // E5: whitelisted native effects on an injected answer, shaped exactly like native answers
        // (MythicRequirement + IncrementFlagValue MythicChoices_<path>_Achievement; AlignmentShift on select).
        internal static void ConfigureNativeEffects(BlueprintAnswer answer, Choice choice, Action<string> warn)
        {
            if (choice.Mythic != null)
            {
                answer.MythicRequirement = (Kingmaker.DialogSystem.Blueprints.Mythic)Enum.Parse(typeof(Kingmaker.DialogSystem.Blueprints.Mythic), choice.Mythic);
                string path = Rules.MythicPath(choice.Mythic);
                if (Rules.MythicAchievementFlags.TryGetValue(path, out var guid)
                    && ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(guid)) is BlueprintUnlockableFlag counter)
                {
                    var value = new Kingmaker.Designers.EventConditionActionSystem.Evaluators.IntConstant { Value = 1 };
                    value.Owner = answer;
                    value.name = "$IntConstant$" + System.Guid.NewGuid();
                    answer.AddToElementsList(value);
                    var increment = new Kingmaker.Designers.EventConditionActionSystem.Actions.IncrementFlagValue { Value = value, UnlockIfNot = true };
                    Field(increment, "m_Flag", Ref<BlueprintUnlockableFlagReference>(counter));
                    answer.OnSelect = Actions((answer.OnSelect?.Actions ?? Array.Empty<GameAction>()).Concat(new GameAction[] { increment }).ToArray());
                }
                else warn("Mythic-choice achievement counter unavailable for " + choice.Mythic + "; the requirement is kept without it.");
            }
            if (choice.Crusade != null)
            {
                int amount = Math.Abs(choice.Crusade.Amount);
                var resources = choice.Crusade.Resource == "Finances" ? Kingmaker.Kingdom.KingdomResourcesAmount.FromFinances(amount)
                    : choice.Crusade.Resource == "Materials" ? Kingmaker.Kingdom.KingdomResourcesAmount.FromMaterials(amount)
                    : Kingmaker.Kingdom.KingdomResourcesAmount.FromFavors(amount);
                GameAction change;
                if (choice.Crusade.Amount > 0)
                {
                    change = new Kingmaker.Kingdom.Blueprints.AddCrusadeResources();
                    Field(change, "_resourcesAmount", resources);
                }
                else
                {
                    change = new Kingmaker.Kingdom.Blueprints.RemoveCrusadeResources();
                    Field(change, "m_ResourcesAmount", resources);
                }
                answer.OnSelect = Actions((answer.OnSelect?.Actions ?? Array.Empty<GameAction>()).Concat(new[] { change }).ToArray());
            }
            if (choice.RemoveItem != null)
            {
                if (ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(choice.RemoveItem)) is Kingmaker.Blueprints.Items.BlueprintItem item)
                {
                    var remove = new Kingmaker.Designers.EventConditionActionSystem.Actions.RemoveItemFromPlayer { Quantity = 1 };
                    Field(remove, "m_ItemToRemove", Ref<BlueprintItemReference>(item));
                    answer.OnSelect = Actions((answer.OnSelect?.Actions ?? Array.Empty<GameAction>()).Concat(new GameAction[] { remove }).ToArray());
                }
                else warn("Removable item " + choice.RemoveItem + " is missing; the choice removes nothing.");
            }
            if (choice.Alignment != null)
                answer.AlignmentShift = new Kingmaker.UnitLogic.Alignments.AlignmentShift
                {
                    Direction = (Kingmaker.UnitLogic.Alignments.AlignmentShiftDirection)Enum.Parse(
                        typeof(Kingmaker.UnitLogic.Alignments.AlignmentShiftDirection), choice.Alignment.Direction),
                    Value = choice.Alignment.Value,
                    Description = EmptyText()
                };
        }

        private static LocalizedString EmptyText()
        {
            var text = new LocalizedString();
            Field(text, "m_Key", "");
            return text;
        }

        // E14b: one inline cue graph per native list; terminal and abort answers go to an authored return cue whose only answer
        // is that list, so the native menu reappears. Completion is recorded on the terminal choice, so the entry then hides.
        private static void BuildReturnToList(Scene scene)
        {
            foreach (string list in scene.AnswerLists)
            {
                string prefix = scene.Id + "." + list;
                CueSetup(out var returnCue, "cue." + prefix + ".return", scene.ReturnText ?? "{n}The moment passes. The conversation resumes.{/n}");
                var listReference = new BlueprintAnswerBaseReference();
                Field(listReference, "deserializedGuid", BlueprintGuid.Parse(list));
                returnCue.Answers.Add(listReference);
                var local = new Dictionary<string, BlueprintCue>();
                foreach (var node in scene.Nodes)
                {
                    CueSetup(out var cue, "cue." + prefix + "." + node.Id, node.Text);
                    cue.Speaker = InlineSpeaker(node, null);
                    local.Add(node.Id, cue);
                }
                foreach (var node in scene.Nodes)
                    for (int i = 0; i < node.Choices.Count; i++)
                    {
                        var choice = node.Choices[i];
                        var answer = New<BlueprintAnswer>("answer." + prefix + "." + node.Id + "." + i);
                        InitializeAnswer(answer);
                        answer.Text = Text(answer.name, choice.Text);
                        answer.ShowConditions = Conditions(new RouteCondition { Choice = choice });
                        answer.SelectConditions = Conditions(new RouteCondition { Choice = choice });
                        answer.OnSelect = Actions(new RouteAction { Choice = choice, Complete = choice.Next == null && !choice.Abort ? scene : null });
                        answer.NextCue = Cues(choice.Next != null ? local[choice.Next] : returnCue);
                        ConfigureNativeEffects(answer, choice, warnings.Add);
                        local[node.Id].Answers.Add(Ref<BlueprintAnswerBaseReference>(answer));
                    }
                var entryAnswer = New<BlueprintAnswer>("entry." + prefix);
                InitializeAnswer(entryAnswer);
                entryAnswer.Text = Text("entry." + prefix, scene.Entry);
                entryAnswer.ShowConditions = Conditions(new RouteCondition { Scene = scene });
                entryAnswer.SelectConditions = Conditions(new RouteCondition { Scene = scene });
                entryAnswer.NextCue = Cues(local[scene.Nodes[0].Id]);
                if (scene.EntryMythic != null || scene.EntryAlignment != null)
                    ConfigureNativeEffects(entryAnswer, new Choice { Mythic = scene.EntryMythic, Alignment = scene.EntryAlignment }, warnings.Add);
            }
        }

        internal static void InsertContinueBefore(BlueprintCue parent, BlueprintCueBaseReference line, BlueprintGuid anchor)
        {
            if (parent.Continue.Cues.Any(reference => reference.Guid == line.Guid)) return;
            int index = parent.Continue.Cues.FindIndex(reference => reference.Guid == anchor);
            if (index < 0) throw new InvalidOperationException("Continue anchor " + anchor + " left " + parent.AssetGuid);
            parent.Continue.Cues.Insert(index, line);
        }

        // E14e: the line is one registered cue; showing it records the scene's single choice (flags and completion).
        private static void BuildContinueBefore(Scene scene)
        {
            var node = scene.Nodes[0];
            CueSetup(out var cue, "cue." + scene.Id + ".continue", node.Text);
            cue.Speaker = InlineSpeaker(node, new DialogSpeaker { NoSpeaker = false, MoveCamera = false });
            cue.Conditions = Conditions(new RouteCondition { Scene = scene });
            cue.OnShow = Actions(new RouteAction { Choice = node.Choices[0], Complete = scene });
        }

        // E14f: a named unit (its portrait/name, camera untouched), the dialog's conversant, or the scene's default.
        // A unit that does not resolve falls back to the default rather than show a wrong portrait.
        internal static DialogSpeaker InlineSpeaker(Node node, DialogSpeaker? fallback)
        {
            if (node.SpeakerUnit != null)
            {
                if (ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(node.SpeakerUnit)) is BlueprintUnit unit)
                {
                    var speaker = new DialogSpeaker { NoSpeaker = false, MoveCamera = false };
                    Field(speaker, "m_Blueprint", Ref<BlueprintUnitReference>(unit));
                    return speaker;
                }
                warnings.Add("Speaker unit " + node.SpeakerUnit + " is missing; node " + node.Id + " is narrated.");
            }
            else if (node.Speaker == "conversant") return new DialogSpeaker { NoSpeaker = false, MoveCamera = false };
            return fallback ?? new DialogSpeaker { NoSpeaker = true, MoveCamera = false };
        }

        private static void CueSetup(out BlueprintCue cue, string name, string text)
        {
            cue = New<BlueprintCue>(name);
            cue.Conditions = Conditions();
            cue.OnShow = Actions();
            cue.OnStop = Actions();
            cue.Speaker = new DialogSpeaker { NoSpeaker = true, MoveCamera = false };
            cue.TurnSpeaker = false;
            cue.Continue = Cues();
            cue.ShowOnce = false;
            cue.Text = Text(name.Substring("cue.".Length), text);
        }

        private static BlueprintDialog BuildNurahHub()
        {
            var scenes = story.Scenes.Where(Rules.IsNurahHubScene).ToArray();
            if (scenes.Length == 0) throw new InvalidOperationException("Nurah arrival hub has no authored physical scenes.");
            var page = New<BlueprintBookPage>("page.nurah.arrival_hub");
            page.ShowOnce = false;
            page.Conditions = Conditions();
            page.OnShow = Actions();
            page.Title = Text("title.nurah.arrival_hub", "A private appointment");
            var cue = New<BlueprintCue>("cue.nurah.arrival_hub");
            cue.Conditions = Conditions();
            cue.OnShow = Actions();
            cue.OnStop = Actions();
            cue.Speaker = new DialogSpeaker { NoSpeaker = true, MoveCamera = false };
            cue.TurnSpeaker = false;
            cue.Continue = Cues();
            const string greeting = "Nurah closes the door behind her and lays the open proofs aside. \"I have brought the work, the questions it caused, and enough time to hear what you actually came to say. Choose what deserves our attention. Or leave me to finish the page.\"";
            cue.Text = Text("cue.nurah.arrival_hub", greeting);
            page.Cues.Add(Ref<BlueprintCueBaseReference>(cue));
            pages.Add(page.AssetGuid.ToString(), new Node { Id = "arrival_hub", Speaker = "Nurah", Portrait = "Nurah", Text = greeting });
            foreach (var scene in scenes)
            {
                var answer = New<BlueprintAnswer>("answer.nurah.arrival_hub." + scene.Id);
                InitializeAnswer(answer);
                answer.Text = Text(answer.name, scene.Title);
                answer.ShowConditions = Conditions(new RouteCondition { Scene = scene });
                answer.SelectConditions = Conditions(new RouteCondition { Scene = scene });
                answer.OnSelect = Actions(new RouteAction { Start = scene });
                page.Answers.Add(Ref<BlueprintAnswerBaseReference>(answer));
            }
            var leave = New<BlueprintAnswer>("answer.nurah.arrival_hub.leave");
            InitializeAnswer(leave);
            leave.Text = Text(leave.name, "Leave the proofs for another time.");
            page.Answers.Add(Ref<BlueprintAnswerBaseReference>(leave));

            var dialog = New<BlueprintDialog>("dialog.nurah.arrival_hub");
            dialog.Type = DialogType.Book;
            dialog.Conditions = Conditions();
            dialog.FirstCue = Cues(page);
            dialog.TurnPlayer = false;
            dialog.TurnFirstSpeaker = false;
            dialog.StartActions = Actions();
            dialog.FinishActions = Actions(new RouteAction { StopSpeech = true });
            return dialog;
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

        // One snapshot per frame (GLOBAL-11): opening a native list with ~60 RRT entries used to rebuild it ~120 times.
        // Invalidated by every RRT flag write; a native change in the same frame is picked up on the next frame.
        private static Snapshot? cachedState;
        private static int cachedFrame = -1;
        private static object? cachedPlayer;
        internal static int StateBuilds;

        [System.Runtime.CompilerServices.MethodImpl(System.Runtime.CompilerServices.MethodImplOptions.NoInlining)]
        private static int UnityFrame() => Time.frameCount;

        private static int CurrentFrame()
        {
            try { return UnityFrame(); }
            catch { return -1; } // outside Unity (managed tests): never cache
        }

        internal static void InvalidateState() => cachedState = null;

        internal static Snapshot State()
        {
            int frame = CurrentFrame();
            var owner = Game.Instance?.Player;
            if (frame >= 0 && cachedState != null && cachedFrame == frame && ReferenceEquals(cachedPlayer, owner)) return cachedState;
            var built = BuildState();
            if (frame >= 0) { cachedState = built; cachedFrame = frame; cachedPlayer = owner; }
            return built;
        }

        private static Snapshot BuildState()
        {
            StateBuilds++;
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
            ReadNativeProgress(player.UnlockableFlags, player.QuestBook,
                item => player.Inventory.Contains(item) || player.SharedStash?.Contains(item) == true, state);
            if (flags.ContainsKey("konomi.missed_letter_sent") && etudes.TryGetValue("konomi.present", out var office))
            {
                // A dormant office is still an appointment, not a missed introduction.
                bool officeActive = player.EtudesSystem.Etudes.GetFact(office) != null
                    && !player.EtudesSystem.EtudeIsCompleted(office);
                var contact = KonomiContactObservation.Observe(officeActive || state.Has("konomi.present"));
                if (contact.Available) state.Flags.Add("konomi.missed_contact_available");
                if (contact.Invalidated && (state.Has("konomi.missed_letter_sent") || state.Has("konomi.missed_private_access")))
                    state.Flags.Add("konomi.missed_contact_invalidated");
            }
            foreach (var contact in contactUnits)
                if (NativeContact.IsAvailable(contact.Value)) state.AvailableContacts.Add(contact.Key);
            if (IrabethCorrespondenceAvailable()) state.Flags.Add("irabeth.return_correspondence_available");
            foreach (var presence in presences)
                if (presence.AnchorFailed) state.Flags.Add(Rules.PresenceFailedFlag(presence.Key));
            if (irabethMeeting?.Arrived() == true) state.Flags.Add("irabeth.return_meeting_arrived");
            if (nurahMeeting?.CorrespondenceAvailable() == true) state.Flags.Add("nurah.correspondence_available");
            if (nurahMeeting?.ArrivedActor() != null)
            {
                state.Flags.Add("nurah.meeting_arrived");
                state.AvailableContacts.Add(NurahMeeting.Unit);
            }
            foreach (var revival in revivalUnits)
                if (revival.Key == "konomi")
                {
                    if (KonomiRecovery.CanRequest()) state.Flags.Add("revive.konomi.available");
                    if (KonomiRecovery.RetainedDead()) state.Flags.Add("konomi.retained_dead");
                    else if (KonomiRecovery.RetainedHostile()) state.Flags.Add("konomi.retained_hostile");
                    if (konomiMeeting?.ContactAvailable() == true) state.Flags.Add("konomi.return_contact_available");
                    if (KonomiRecovery.ReturnCorrespondenceAvailable()) state.Flags.Add("konomi.return_correspondence_available");
                }
                else if (Fate.CanRevive(revival.Value)) state.Flags.Add("revive." + revival.Key + ".available");
            if (new[] { "ascend_all", "ascend_alone", "ascend_areelu", "ascend_companions" }.Any(state.Has)) state.Flags.Add("ascended");
            if (state.Has("swarm") || state.Has("true_lich")) state.Flags.Add("inhuman");
            state.Flags.Add(player.Chapter == 1 ? "chapter_one" : "chapter_later");
            // Latches and data-driven composites read the completed native picture.
            Rules.Complete(story, state);
            foreach (var relationship in degraded) state.Flags.Add(Rules.DegradedPrefix + relationship);
            return state;
        }

        // E10: read-only native progress. Items: the party inventory (which holds every party member's equipped items, as the
        // native ItemsEnough condition reads it) or the shared stash; never the vendor or loot collections.
        internal static void ReadNativeProgress(Kingmaker.AreaLogic.QuestSystem.UnlockableFlagsManager unlockable, QuestBook quests,
            Func<Kingmaker.Blueprints.Items.BlueprintItem, bool> holds, Snapshot state)
        {
            // A native container that throws (e.g. a quest whose objective list changed in a patch) reads as "not held".
            void Read(string key, Func<bool> observe)
            {
                try { if (observe()) state.Flags.Add(key); }
                catch (Exception ex) { if (readerWarnings.Add(key)) entry?.Logger.Log("Native reader '" + key + "' unavailable: " + ex.Message); }
            }
            foreach (var pair in nativeFlags) Read(pair.Key, () => unlockable.GetFlagValue(pair.Value) > 0);
            foreach (var pair in nativeObjectives) Read(pair.Key, () => quests.GetObjectiveState(pair.Value.Key) == pair.Value.Value);
            foreach (var pair in startedQuests)
                Read(pair.Key, () => quests.GetQuestState(pair.Value) is QuestState questState
                    && (questState == QuestState.Started || questState == QuestState.Completed));
            foreach (var pair in nativeItems) Read(pair.Key, () => holds(pair.Value));
        }

        private static readonly HashSet<string> readerWarnings = new HashSet<string>(StringComparer.Ordinal);

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

        private static void Set(string key, int value = 1)
        {
            Game.Instance.Player.UnlockableFlags.SetFlagValue(flags[key], value);
            InvalidateState();
        }

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
                if (choice != null && choice.Set.Contains(relationship.StartedFlag)
                    && !state.Has(relationship.ClosedFlag) && !state.Has(relationship.CommittedFlag)
                    && Game.Instance.Player.QuestBook.GetObjectiveState(pair.Value) == QuestObjectiveState.None)
                    Game.Instance.Player.QuestBook.GiveObjective(pair.Value);
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
                    if (pair.Key == "konomi")
                    {
                        var request = KonomiRecovery.RequestedAction();
                        if (request == null) continue;
                        var match = story.Scenes.Where(s => s.Recovery == "konomi")
                            .SelectMany(s => s.Nodes.SelectMany(n => n.Choices).Where(c => c.Revive == "konomi")
                                .Select(c => new { Scene = s, Choice = c }))
                            .SingleOrDefault(item => KonomiRequestIdentity(item.Scene, item.Choice) == request);
                        if (match == null) throw new InvalidOperationException("The saved Konomi return no longer matches its authored choice.");
                        if (Game.Instance.Player.UnlockableFlags.GetFlagValue(flags[match.Scene.Id]) > 0) continue;
                        // The saved exact choice witnesses the earlier authorized action. Verification consumes no new mythic power.
                        if (KonomiRecovery.Poll(true, out var message) == KonomiRecovery.Outcome.Confirmed)
                            RecordProgress(match.Choice, match.Scene);
                        messages.Add(message);
                        continue;
                    }
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

        private static string KonomiRequestIdentity(Scene scene, Choice choice) =>
            JsonConvert.SerializeObject(new object[] { scene.Id, choice });

        private static bool Idle() => Game.Instance?.Player != null && Game.Instance.DialogController?.Dialog == null
            && Game.Instance.Player.Dialog.Scheduled == null && !Game.Instance.Player.IsInCombat
            && Game.Instance.CurrentMode == GameModeType.Default;

        // Raw saved consent only. Never call State here: its contact observer calls the meeting helper.
        internal static string? KonomiVisitRequest(Func<string, int> read, int hour)
        {
            if (read("konomi.retained_return_confirmed") <= 0 || read("konomi.return_visit_declined") > 0
                || read("konomi.return_second_visit") > 0) return null;
            int restored = read("hour.konomi.retained_return_confirmed");
            int retry = read(KonomiMeetingRetry);
            if (restored <= 0 || (long)hour - (restored - 1L) < 12 || retry < 0) return null;
            bool firstDone = read("konomi.return_first_words") > 0;
            if (firstDone)
            {
                int invited = read("hour.konomi.return_followup_invited");
                if (read("konomi.return_followup_invited") <= 0 || invited <= 0 || (long)hour - (invited - 1L) < 48) return null;
            }
            else if (read("konomi.return_meeting_accepted") <= 0) return null;
            return (firstDone ? "konomi.return.followup/" : "konomi.return.first/")
                + retry.ToString(System.Globalization.CultureInfo.InvariantCulture);
        }

        internal static string? NurahVisitRequest(Func<string, int> read, int hour)
        {
            int accepted = read("hour.nurah.meeting_accepted");
            int retry = read(NurahMeetingRetry);
            if (read("nurah.meeting_accepted") <= 0 || read("nurah.meeting_declined") > 0
                || read("nurah.meeting_withdrawn") > 0 || read("nurah.closed") > 0
                || read("nurah.complete") > 0 || read("closed") > 0 || read("inhuman") > 0
                || accepted <= 0 || retry < 0 || (long)hour - (accepted - 1L) < 12) return null;
            return "nurah.private/" + retry.ToString(System.Globalization.CultureInfo.InvariantCulture);
        }

        private static string? CurrentNurahVisit()
        {
            try
            {
                if (!initialized || !enabled) return null;
                var game = Game.Instance;
                if (game?.Player == null || game.IsLoadingSave || game.IsUnloading
                    || LoadingProcess.Instance.IsLoadingInProcess || game.Player.Chapter != 5
                    || game.Player.IsInCombat || game.CurrentlyLoadedArea?.AssetGuid.ToString() != NurahMeeting.Capital
                    || !NurahVisitWindow()) return null;
                int Read(string key) => flags.TryGetValue(key, out var flag) ? game.Player.UnlockableFlags.GetFlagValue(flag) : 0;
                var request = NurahVisitRequest(Read, (int)game.Player.GameTime.TotalHours);
                return request != null && nurahMeeting?.CorrespondenceAvailable() == true ? request : null;
            }
            catch { return null; }
        }

        private static bool NurahVisitWindow()
        {
            var game = Game.Instance;
            bool ownDialog = nurahHub != null && ReferenceEquals(game.DialogController?.Dialog, nurahHub)
                || story.Scenes.Where(Rules.IsNurahHubScene).Any(scene => dialogs.TryGetValue(scene.Id, out var dialog)
                    && ReferenceEquals(game.DialogController?.Dialog, dialog));
            return game.Player.Dialog.Scheduled == null && !game.Player.IsInCombat
                && (Idle() || ownDialog && game.CurrentMode == GameModeType.Dialog);
        }

        private static bool CanOpenNurahHub()
        {
            if (!initialized || !enabled || nurahMeeting?.ArrivedActor() == null || !Idle()) return false;
            var state = State();
            return story.Scenes.Where(Rules.IsNurahHubScene).Any(scene => Rules.Available(story, scene, state));
        }

        private static bool CanRetryNurahVisit()
        {
            try
            {
                return initialized && enabled && Idle() && nurahMeeting?.CurrentRequest != null
                    && nurahMeeting.SavedFailed && Game.Instance.Player.UnlockableFlags.GetFlagValue(flags[NurahMeetingRetry]) < int.MaxValue;
            }
            catch { return false; }
        }

        private static void RetryNurahVisit()
        {
            if (!CanRetryNurahVisit()) return;
            int prior = Game.Instance.Player.UnlockableFlags.GetFlagValue(flags[NurahMeetingRetry]);
            if (prior < 0 || prior == int.MaxValue) return;
            Set(NurahMeetingRetry, checked(prior + 1));
            nurahMeeting!.Tick();
        }

        private static string? CurrentKonomiVisit()
        {
            if (!initialized || !enabled) return null;
            var game = Game.Instance;
            if (game?.Player == null || game.IsLoadingSave || game.IsUnloading
                || LoadingProcess.Instance.IsLoadingInProcess || game.Player.IsInCombat
                || (game.Player.Chapter != 3 && game.Player.Chapter != 5)) return null;
            var player = game.Player;
            foreach (string key in new[] { "swarm", "true_lich" })
                if (etudes.TryGetValue(key, out var mythic) && (player.EtudesSystem.Etudes.GetFact(mythic)?.IsPlaying == true
                    || (key == "true_lich" || story.PermanentEtudes.Contains(key)) && player.EtudesSystem.EtudeIsCompleted(mythic))) return null;
            int Read(string key) => flags.TryGetValue(key, out var flag) ? player.UnlockableFlags.GetFlagValue(flag) : 0;
            string? request = KonomiVisitRequest(Read, (int)player.GameTime.TotalHours);
            if (request == null || !KonomiRecovery.ReturnCorrespondenceAvailable()) return null;
            string scene = Read("konomi.return_first_words") > 0 ? "konomi.return_second_visit" : "konomi.return_first_words";
            return KonomiVisitWindow(scene) ? request : null;
        }

        private static bool KonomiVisitWindow(string scene)
        {
            var game = Game.Instance;
            // Keep the actor through her own visit; unrelated dialogue/events withdraw the temporary claim.
            bool ownDialog = dialogs.TryGetValue(scene, out var dialog) && ReferenceEquals(game.DialogController?.Dialog, dialog);
            return !game.Player.IsInCombat && game.Player.Dialog.Scheduled == null
                && (Idle() || ownDialog && game.CurrentMode == GameModeType.Dialog);
        }

        private static bool CanRetryKonomiVisit()
        {
            try
            {
                return initialized && enabled && Idle() && konomiMeeting?.CurrentRequest != null
                    && konomiMeeting.SavedFailed && KonomiRecovery.ReturnCorrespondenceAvailable()
                    && Game.Instance.Player.UnlockableFlags.GetFlagValue(flags[KonomiMeetingRetry]) < int.MaxValue;
            }
            catch { return false; }
        }

        internal static string? IrabethVisitRequest(Func<string, int> read, int hour)
        {
            int accepted = read("hour.irabeth.return_meeting_accepted");
            int retry = read(IrabethMeetingRetry);
            if (read("irabeth.return_meeting_accepted") <= 0 || read("irabeth.return_reply") <= 0
                || read("irabeth.return_meeting_declined") > 0
                || read("irabeth.return_first_words") > 0 || read("irabeth.closed") > 0 || read("closed") > 0
                || accepted <= 0 || retry < 0
                || (long)hour - (accepted - 1L) < 12) return null;
            return "irabeth.return.first/" + retry.ToString(System.Globalization.CultureInfo.InvariantCulture);
        }

        private static bool IrabethCorrespondenceAvailable()
        {
            try
            {
                if (!initialized || !enabled) return false;
                var game = Game.Instance;
                if (game?.Player == null || game.IsLoadingSave || game.IsUnloading || LoadingProcess.Instance.IsLoadingInProcess
                    || game.Player.Chapter != 5 || game.CurrentlyLoadedArea?.AssetGuid.ToString() != IrabethMeeting.Capital
                    || !etudes.TryGetValue("trickster", out var trickster)
                    || game.Player.EtudesSystem.Etudes.GetFact(trickster)?.IsPlaying != true) return false;
                foreach (string key in new[] { "swarm", "true_lich" })
                    if (etudes.TryGetValue(key, out var path) && (game.Player.EtudesSystem.Etudes.GetFact(path)?.IsPlaying == true
                        || key == "true_lich" && game.Player.EtudesSystem.EtudeIsCompleted(path))) return false;
                return irabethMeeting?.CorrespondenceAvailable() == true;
            }
            catch { return false; }
        }

        // Raw saved request plus current native evidence; never call State from this callback.
        private static string? CurrentIrabethVisit()
        {
            if (!IrabethCorrespondenceAvailable()) return null;
            var game = Game.Instance;
            int Read(string key) => flags.TryGetValue(key, out var flag) ? game.Player.UnlockableFlags.GetFlagValue(flag) : 0;
            string? request = IrabethVisitRequest(Read, (int)game.Player.GameTime.TotalHours);
            return request != null && IrabethVisitWindow() ? request : null;
        }

        private static bool IrabethVisitWindow()
        {
            var game = Game.Instance;
            bool ownDialog = dialogs.TryGetValue("irabeth.return_first_words", out var dialog)
                && ReferenceEquals(game.DialogController?.Dialog, dialog);
            return game.Player.Dialog.Scheduled == null && !game.Player.IsInCombat
                && (Idle() || ownDialog && game.CurrentMode == GameModeType.Dialog);
        }

        private static bool CanRetryIrabethVisit()
        {
            try
            {
                return initialized && enabled && Idle() && irabethMeeting?.CurrentRequest != null
                    && irabethMeeting.SavedFailed && IrabethCorrespondenceAvailable()
                    && Game.Instance.Player.UnlockableFlags.GetFlagValue(flags[IrabethMeetingRetry]) < int.MaxValue;
            }
            catch { return false; }
        }

        private static void RetryIrabethVisit()
        {
            if (!CanRetryIrabethVisit()) return;
            int prior = Game.Instance.Player.UnlockableFlags.GetFlagValue(flags[IrabethMeetingRetry]);
            if (prior < 0 || prior == int.MaxValue) return;
            Set(IrabethMeetingRetry, checked(prior + 1));
            irabethMeeting!.Tick();
        }

        private static void RetryKonomiVisit()
        {
            if (!CanRetryKonomiVisit()) return;
            int prior = Game.Instance.Player.UnlockableFlags.GetFlagValue(flags[KonomiMeetingRetry]);
            if (prior < 0 || prior == int.MaxValue) return;
            Set(KonomiMeetingRetry, checked(prior + 1));
            konomiMeeting!.Tick();
        }

        private static void Update()
        {
            if (Input.GetKey(KeyCode.LeftControl) && Input.GetKeyDown(KeyCode.S)) StopNarration();
            if (!initialized || Time.realtimeSinceStartup < pollAt) return;
            pollAt = Time.realtimeSinceStartup + 0.3f;
            // Disabled, combat and other-event states must still withdraw an existing meeting claim.
            konomiMeeting?.Tick();
            irabethMeeting?.Tick();
            nurahMeeting?.Tick();
            nurahInteraction?.Tick();
            if (!enabled) return;
            if (narrationPlayer != null && !ReferenceEquals(narrationPlayer, Game.Instance?.Player)) StopNarration();
            if (pendingPlayer != null && !ReferenceEquals(pendingPlayer, Game.Instance?.Player)) CancelPending();
            // Undelivered letters belong to the save that rested; loading another save drops them.
            if (postBag.Queue.Count > 0 && !ReferenceEquals(postBagPlayer, Game.Instance?.Player)) postBag.Clear();
            if (recoveryPlayer != null && !ReferenceEquals(recoveryPlayer, Game.Instance?.Player))
            {
                recoveryMessage = null;
                recoveryPlayer = null;
            }
            if (!Idle() || Game.Instance?.Player == null || Game.Instance.IsLoadingSave || Game.Instance.IsUnloading
                || LoadingProcess.Instance.IsLoadingInProcess) return;
            ReconcileRecoveries();
            RecordLatches();
            var state = State();
            TickPresences(state);
            foreach (var pair in objectives)
            {
                if (Game.Instance.Player.QuestBook.GetObjectiveState(pair.Value) == QuestObjectiveState.Started
                    && Rules.Failed(story.Relationships[pair.Key], state)) Game.Instance.Player.QuestBook.FailObjective(pair.Value);
            }
            if (restPending)
            {
                restPending = false;
                var served = story.Relationships.Keys.ToDictionary(key => key, key =>
                    flags.TryGetValue(Rules.ServedPrefix + key, out var flag) ? Game.Instance.Player.UnlockableFlags.GetFlagValue(flag) - 1 : -1);
                int added = postBag.Fill(story, state, served, BagSize());
                postBagPlayer = Game.Instance.Player;
                if (added > 0) entry.Logger.Log("Post bag: " + added + " letter(s) after rest; " + postBag.Queue.Count + " waiting.");
            }
            // E8: whenever no dialog is open, the next undelivered letter follows (a finished letter chains into the next).
            if (pending == null && postBag.Queue.Count > 0 && postBag.Next(story, state) is Scene next)
            {
                pending = next;
                pendingPlayer = Game.Instance.Player;
                pendingFrame = Time.frameCount + 2;
            }
            if (pending == null || Time.frameCount < pendingFrame) return;
            var scene = pending;
            pending = null;
            pendingPlayer = null;
            if (!Rules.Available(story, scene, State()) || Game.Instance?.Player == null) return;
            Set(story.Relationships[scene.Relationship].StartedFlag);
            var objective = objectives[scene.Relationship];
            if (Game.Instance.Player.QuestBook.GetObjectiveState(objective) == QuestObjectiveState.None) Game.Instance.Player.QuestBook.GiveObjective(objective);
            // Remember when each relationship last received a letter so the next rest serves someone else first.
            if (flags.ContainsKey(Rules.ServedPrefix + scene.Relationship))
                Set(Rules.ServedPrefix + scene.Relationship, Math.Max(1, (int)Game.Instance.Player.GameTime.TotalHours + 1));
            Game.Instance.DialogController.StartDialogWithoutTarget(dialogs[scene.Id], null);
        }

        // E12: place, unhide, spawn or remove returned presences for the loaded area. Idle only; each change is logged once.
        private static void TickPresences(Snapshot state)
        {
            if (presences.Count == 0) return;
            foreach (var presence in presences)
            {
                bool wanted = !degraded.Contains(presence.Key.Substring(0, presence.Key.Length - ".presence".Length))
                    && Rules.PresenceWanted(presence.Spec, state);
                presence.Tick(wanted);
                string line = presence.Report(wanted);
                if (!presenceStatus.TryGetValue(presence.Key, out var last) || last != line)
                {
                    presenceStatus[presence.Key] = line;
                    entry.Logger.Log("Presence " + line);
                }
            }
            InvalidateState();
        }

        // Harness hook (GLOBAL-20): one line per presence, "<key> [mode] wanted|not wanted; <status>".
        internal static string[] PresenceReport() => presences.Select(presence =>
            presenceStatus.TryGetValue(presence.Key, out var line) ? line : presence.Key + " [" + presence.Spec.Mode + "] not observed").ToArray();

        // E1: persist every latch the current snapshot observes. Idle-only, so native state is settled.
        private static void RecordLatches()
        {
            if (story.Latches.Count == 0) return;
            var state = State();
            int hour = (int)Game.Instance.Player.GameTime.TotalHours;
            foreach (var key in story.Latches.Keys)
            {
                if (!state.Has(key) || !flags.TryGetValue(key, out var flag)
                    || Game.Instance.Player.UnlockableFlags.GetFlagValue(flag) > 0) continue;
                Set("hour." + key, hour + 1);
                Set(key);
                entry.Logger.Log("Recorded latch: " + key);
            }
        }

        private static void CancelPending()
        {
            pending = null;
            pendingPlayer = null;
            restPending = false;
            postBag.Clear();
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
            GUILayout.BeginHorizontal();
            GUILayout.Label("Letters delivered per rest: " + BagSize() + (settings.PostBagSize > 0 ? "" : " (story default)"));
            if (GUILayout.Button("-", GUILayout.Width(30))) settings.PostBagSize = Math.Max(1, BagSize() - 1);
            if (GUILayout.Button("+", GUILayout.Width(30))) settings.PostBagSize = Math.Min(10, BagSize() + 1);
            if (settings.PostBagSize > 0 && GUILayout.Button("Default", GUILayout.Width(70))) settings.PostBagSize = 0;
            GUILayout.EndHorizontal();
            GUILayout.Label("Windows narration is synthetic, not the original actors. Existing AI Voiceover lines are untouched.");
            if (error != null) { GUILayout.Label("Route initialization failed: " + error); return; }
            if (degraded.Count > 0) GUILayout.Label("Unavailable in this installation (missing game or RanRomance content): " + string.Join(", ", degraded.OrderBy(r => r)) + ". Other relationships are unaffected; details are in the mod log.");
            if (!initialized || Game.Instance?.Player == null) { GUILayout.Label("Load a main-campaign save after restarting the application once."); return; }
            var state = State();
            if (CanRetryKonomiVisit() && GUILayout.Button("Arrange Konomi's visit again")) RetryKonomiVisit();
            if (CanRetryIrabethVisit() && GUILayout.Button("Arrange Irabeth's visit again")) RetryIrabethVisit();
            if (CanRetryNurahVisit() && GUILayout.Button("Retry Nurah's private appointment")) RetryNurahVisit();
            if (state.Has("nurah.meeting_arrived")
                && story.Scenes.Where(Rules.IsNurahHubScene).Any(scene => Rules.Available(story, scene, state)))
                GUILayout.Label("Nurah is waiting by the private chambers. Click her to choose what you discuss.");
            foreach (var pair in story.Relationships)
            {
                GUILayout.Label(pair.Value.Title);
                foreach (var scene in story.Scenes.Where(s => s.Relationship == pair.Key && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && Rules.Available(story, s, state)))
                {
                    GUILayout.Label(scene.Title + (scene.ManualOnly ? " | choose Read below" : Rules.IsRemote(scene) ? " | available at your next rest" : " | speak to " + (scene.Owner == "Together" ? "Anevia or Irabeth" : scene.Owner)));
                    if (Rules.IsRemote(scene) && Idle() && GUILayout.Button("Read: " + scene.Title)) Queue(scene);
                }
                if (state.Has(pair.Value.ClosedFlag)) GUILayout.Label(pair.Key == "nocticula" ? "The harbor undertaking has ended." : "This relationship has ended.");
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

        // E14c: one conditional paragraph of an epilogue page.
        public sealed class ParagraphCondition : Condition
        {
            public Paragraph? Paragraph;
            protected override string GetConditionCaption() => "Three at the Table epilogue paragraph";
            protected override bool CheckCondition() => enabled && initialized && Game.Instance?.Player != null && Paragraph != null
                && Rules.ParagraphVisible(Paragraph, State());
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
                        string message;
                        bool restored = Choice.Revive == "konomi"
                            ? KonomiRecovery.Request(KonomiRequestIdentity(Complete, Choice), true, out message) == KonomiRecovery.Outcome.Confirmed
                            : Fate.TryRevive(Choice.Revive, revivalUnits[Choice.Revive], Complete, Choice, out message);
                        ReportRecovery(message);
                        if (!restored) return;
                    }
                }
                RecordProgress(Choice, Complete);
                if (Choice?.Revive != null && Choice.Revive != "konomi") Fate.Clear(Choice.Revive);
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
