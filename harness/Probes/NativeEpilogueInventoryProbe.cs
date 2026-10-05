// BEGIN eng7-f5: harness-only slide selection. No native etudes, route gates or save IDs are changed.
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using HarmonyLib;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.Controllers.Dialog;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.UI.MVVM._VM.Dialog.BookEvent;
using Newtonsoft.Json;

namespace RRT.TestHarness
{
    public sealed class NativeSlideCase
    {
        public string Id = "", Target = "", Dialog = "", Page = "", ExpectedCandidate = "";
        public int Chapter = 6;
        public bool UseSaveState;
        public List<string> Flags = new List<string>(), NativeEligible = new List<string>();
        public List<string> ExpectShown = new List<string>(), ExpectHidden = new List<string>();
        public List<string> AnswerPath = new List<string>();
    }
    public sealed class NativeSlideCases
    {
        public int Schema;
        public string Evidence = "";
        public List<NativeSlideCase> Cases = new List<NativeSlideCase>();
        public static NativeSlideCases Parse(string json)
        {
            var data = JsonConvert.DeserializeObject<NativeSlideCases>(json,
                new JsonSerializerSettings { MissingMemberHandling = MissingMemberHandling.Error }) ?? throw new FormatException("Empty slide cases");
            if (data.Schema != 1 || data.Cases.Count == 0 || data.Cases.Any(c => string.IsNullOrWhiteSpace(c.Id))
                || data.Cases.Select(c => c.Id).Distinct().Count() != data.Cases.Count)
                throw new FormatException("Slide cases need schema 1, unique IDs and at least one case");
            return data;
        }
    }
    public sealed class NativeSlideRow
    {
        public string Kind = "", Target = "", Scene = "", Cue = "", Relationship = "", Parent = "";
        public bool Expected, CanShow, Attached;
        public List<string> Continue = new List<string>(), OnShow = new List<string>(), OnStop = new List<string>();
        public string Speaker = "", ImagePolicy = "";
        public string Page = "";
        public string TextKey = "", Text = "";
    }
    public sealed class NativeSlideObservation
    {
        public string Event = "", Cue = "", Name = "";
        public List<string> Actions = new List<string>();
        public string Picture = "", ExpectedPicture = "";
    }
    public sealed class NativeSlideResult
    {
        public string Case = "", Evidence = "", Dialog = "", Entry = "", Result = "running";
        public bool Forced, Passed;
        public SnapshotData? State;
        public List<NativeSlideRow> Inventory = new List<NativeSlideRow>();
        public List<NativeSlideObservation> Observations = new List<NativeSlideObservation>();
        public List<string> Findings = new List<string>(), Warnings = new List<string>(), Degraded = new List<string>();
        public List<string> Screenshots = new List<string>();
        public bool RanEpiloguePatched;
        public Dictionary<string, List<string>> LoadedSequences = new Dictionary<string, List<string>>();
        public Dictionary<string, bool> ForcedNativeChecks = new Dictionary<string, bool>();
    }

    internal sealed class NativeEpilogueInventoryProbe : IDisposable
    {
        internal const string EpilogueDialog = "ae58532cb72b28b4eaaccb82eb78eaea";
        internal const string AfterlogueDialog = "57e18f5158904030a84a772fb361ceb4";
        const string ParentSequence = "ed4baeaf69394754902344f0598d7e5a";
        const BindingFlags Static = BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;
        static NativeEpilogueInventoryProbe? active;
        readonly Harmony patches = new Harmony("RRT.TestHarness.eng7-f5.slides");
        readonly Dictionary<ConditionsChecker, bool> nativeChecks = new Dictionary<ConditionsChecker, bool>();
        readonly Dictionary<ActionList, List<(string Cue, string Event)>> actionLists = new Dictionary<ActionList, List<(string, string)>>();
        readonly RrtBridge bridge;
        readonly NativeSlideResult result;
        readonly object snapshot;
        readonly BlueprintDialog dialog;
        readonly CueSelection firstCue;
        bool disposed;
        // Keep autosaves blocked during reloads and pending native actions as well as during the active case.
        internal static IDisposable PreventSaves() => new SaveBlock();
        sealed class SaveBlock : IDisposable
        {
            readonly Harmony guard = new Harmony("RRT.TestHarness.eng7-f5.slide-session-saves");
            internal SaveBlock()
            {
                try
                {
                    foreach (var method in AccessTools.GetDeclaredMethods(typeof(Game)).Where(m => m.Name == "SaveGame"))
                        guard.Patch(method, prefix: new HarmonyMethod(typeof(SaveBlock), nameof(NoSave)));
                }
                catch { guard.UnpatchAll(guard.Id); throw; }
            }
            static bool NoSave() => false;
            public void Dispose() => guard.UnpatchAll(guard.Id);
        }
        static object? Field(object o, string name) => o.GetType().GetField(name)?.GetValue(o);
        static string Str(object o, string name) => (string?)Field(o, name) ?? "";
        static SimpleBlueprint? Resolve(string id) => string.IsNullOrEmpty(id) ? null : ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(id));
        static BlueprintCueBaseReference Ref(BlueprintCueBase cue) => cue.ToReference<BlueprintCueBaseReference>();
        static IEnumerable<object> Items(object? o) => (o as IEnumerable)?.Cast<object>() ?? Enumerable.Empty<object>();

        internal NativeEpilogueInventoryProbe(RrtBridge bridge, NativeSlideCase scenario, bool force, NativeSlideResult result)
        {
            this.bridge = bridge; this.result = result;
            if (active != null) throw new InvalidOperationException("Another slide probe is active");
            snapshot = force ? Activator.CreateInstance(bridge.Assembly.GetType("Tirabade.Snapshot", true)!)! : bridge.State();
            if (force)
            {
                snapshot.GetType().GetField("Chapter")!.SetValue(snapshot, scenario.Chapter);
                snapshot.GetType().GetField("Flags")!.SetValue(snapshot, new HashSet<string>(scenario.Flags, StringComparer.Ordinal));
            }
            result.State = RrtBridge.ToData(snapshot);
            result.Forced = force;
            result.RanEpiloguePatched = Harmony.HasAnyPatches("RanEpilogue");
            result.Evidence = force ? "synthetic final snapshot and native eligibility; campaign earning unproved" : "loaded save; native checkers and RRT snapshot unchanged";
            var edits = (IDictionary)Field(bridge.Story!, "NativeEpilogueEdits")!;
            object? spec = edits.Contains(scenario.Target) ? edits[scenario.Target] : null;
            string dialogId = string.IsNullOrEmpty(scenario.Dialog) ? EpilogueDialog : scenario.Dialog;
            dialog = Resolve(dialogId) as BlueprintDialog ?? throw new InvalidOperationException("Actual native dialog missing: " + dialogId);
            firstCue = dialog.FirstCue;
            result.Dialog = dialogId + " " + dialog.name;
            try
            {
                active = this;
                Patch(bridge.Assembly.GetType("Tirabade.Main", true)!.GetMethod("Update", Static)!, nameof(BlockUpdate));
                if (force) Patch(bridge.Assembly.GetType("Tirabade.Main", true)!.GetMethod("State", Static)!, nameof(State));
                foreach (var method in AccessTools.GetDeclaredMethods(typeof(Game)).Where(m => m.Name == "SaveGame")) Patch(method, nameof(BlockSave));
                // CanShow calls Check(debugContext), while Applies calls Check(). Both paths must retain the
                // RRT wrapper and reach the same forced native checker.
                foreach (var method in AccessTools.GetDeclaredMethods(typeof(ConditionsChecker)).Where(m => m.Name == "Check")) Patch(method, nameof(Check));
                Patch(AccessTools.Method(typeof(DialogController), "PlayCue"), nameof(Entering));
                Patch(AccessTools.Method(typeof(DialogController), "PlayBasicCue"), nameof(Shown));
                patches.Patch(typeof(ActionList).GetMethod("Run")!, postfix: new HarmonyMethod(typeof(NativeEpilogueInventoryProbe), nameof(RanActions)));
                patches.Patch(AccessTools.Method(typeof(BookEventVM), "SetPage"), postfix:
                    new HarmonyMethod(typeof(NativeEpilogueInventoryProbe), nameof(Presented)) { after = new[] { "RanRomanceTirabade" }, priority = Priority.Last });
                if (force)
                {
                    // Enter the actual loaded sequence/selection, including the parent's and RRT's inserted pages.
                    // The dialog's entry is restored in Dispose. Conditions on unrelated native pages remain intact.
                    if (spec != null && !string.IsNullOrEmpty(Str(spec, "Page")))
                    {
                        var sequence = Resolve(Str(spec, "Sequence")) as BlueprintCueBase;
                        var page = Resolve(Str(spec, "Page")) as BlueprintBookPage ?? throw new InvalidOperationException("Native page missing");
                        Enter(sequence ?? page);
                        ForceChecker(page, scenario.NativeEligible.Count > 0);
                        foreach (var cue in page.Cues.Select(r => r.Get()).OfType<BlueprintCue>())
                            if (!cue.name.StartsWith("RRT_", StringComparison.Ordinal)) ForceChecker(cue, scenario.NativeEligible.Contains(cue.AssetGuid.ToString()));
                    }
                    else if (spec != null)
                    {
                        var parent = Resolve(Str(spec, "Parent"));
                        var selection = parent is BlueprintCue pc ? pc.Continue : parent is BlueprintAnswer pa ? pa.NextCue : (parent as BlueprintDialog)?.FirstCue;
                        if (selection == null) throw new InvalidOperationException("Native dialog parent missing");
                        // Keep the live selection list; it contains the real registered replacements in their real order.
                        dialog.FirstCue = selection;
                        result.Entry = "native parent selection " + Str(spec, "Parent");
                        foreach (var cue in selection.Cues.Select(r => r.Get()).OfType<BlueprintCue>())
                            if (!cue.name.StartsWith("RRT_", StringComparison.Ordinal)) ForceChecker(cue, scenario.NativeEligible.Contains(cue.AssetGuid.ToString()));
                    }
                    else
                    {
                        var scene = bridge.Scenes.Cast<object>().Single(s => Str(s, "Id") == scenario.ExpectedCandidate);
                        string sequenceId = SequenceOf(scene);
                        Enter(Resolve(sequenceId) as BlueprintCueBase ?? throw new InvalidOperationException("Loaded epilogue sequence missing: " + sequenceId));
                    }
                    if (spec != null && Resolve(scenario.Target) is BlueprintCue target)
                    {
                        ForceChecker(target, scenario.NativeEligible.Contains(scenario.Target));
                        // Native/parent continuation cues use their native eligibility in a natural run. In forced cases
                        // explicitly exercise the registered continuation without starting or completing its etudes.
                        foreach (var continued in target.Continue.Cues.Select(r => r.Get()).OfType<BlueprintCue>()) ForceChecker(continued, true);
                    }
                }
                BuildInventory(edits);
            }
            catch { Dispose(); throw; }
        }

        void Enter(BlueprintCueBase entry)
        {
            dialog.FirstCue = new CueSelection { Strategy = Strategy.First, Cues = new List<BlueprintCueBaseReference> { Ref(entry) } };
            ForceChecker(entry, true);
            result.Entry = entry.AssetGuid + " " + entry.name;
        }
        static string SequenceOf(object scene) => Str(scene, "EpilogueSequence") == "PlayerFinalChoice" ? "a3096e5b145badb448827a7336d86d02"
            : Str(scene, "Owner") == "AeonEpilogue" ? "ced82f299d246f448b48afa0b630dd70" : ParentSequence;
        void ForceChecker(BlueprintCueBase cue, bool holds)
        {
            var checker = cue.Conditions;
            // Never bypass the RRT complementary guard or Applies. Force only the native checker it wraps.
            if (checker?.Conditions?.Length == 1)
            {
                var condition = checker.Conditions[0];
                if (condition.GetType().FullName == "Tirabade.ParentEndingGuard+Guard")
                    checker = (ConditionsChecker?)condition.GetType().GetField("Original", BindingFlags.Instance | BindingFlags.NonPublic)!.GetValue(condition);
            }
            if (checker != null) nativeChecks[checker] = holds;
            if (checker != null) result.ForcedNativeChecks[cue.AssetGuid.ToString()] = holds;
        }
        void Patch(MethodBase? method, string prefix)
        {
            if (method == null) throw new MissingMethodException(prefix + " game API absent");
            patches.Patch(method, prefix: new HarmonyMethod(typeof(NativeEpilogueInventoryProbe), prefix));
        }
        static bool BlockUpdate() => active == null;
        static bool BlockSave() => active == null;
        static bool State(ref object __result) { if (active == null) return true; __result = active.snapshot; return false; }
        static bool Check(ConditionsChecker __instance, ref bool __result)
        {
            if (active == null || !active.nativeChecks.TryGetValue(__instance, out bool holds)) return true;
            __result = holds; return false;
        }
        static void Shown(object[] __args)
        {
            if (active == null) return;
            var cue = __args.OfType<BlueprintCue>().Single();
            active.Observe("shown", cue, Array.Empty<string>());
            active.Track(cue.OnShow, cue, "OnShow"); active.Track(cue.OnStop, cue, "OnStop");
        }
        static void Entering(object[] __args)
        {
            if (active == null) return;
            var cue = __args.OfType<BlueprintCueBase>().Single();
            active.Observe("entered", cue, Array.Empty<string>());
            // PlayCue dispatches OnShow before PlayBasicCue. Tracking only the shown cue would miss image actions.
            if (Field(cue, "OnShow") is ActionList show) active.Track(show, cue, "OnShow");
            if (Field(cue, "OnStop") is ActionList stop) active.Track(stop, cue, "OnStop");
        }
        static void Presented(BookEventVM __instance, BlueprintBookPage page)
        {
            if (active == null) return;
            var sprite = __instance.EventPicture.Value;
            string expected = "";
            var main = active.bridge.Assembly.GetType("Tirabade.Main", true)!;
            var pages = (IDictionary)main.GetField("pages", Static)!.GetValue(null)!;
            if (pages.Contains(page.AssetGuid.ToString()))
            {
                var node = pages[page.AssetGuid.ToString()]!;
                var scenes = (IDictionary)main.GetField("pageScenes", Static)!.GetValue(null)!;
                var kinds = (IDictionary)main.GetField("pageKinds", Static)!.GetValue(null)!;
                var scene = scenes[page.AssetGuid.ToString()];
                string key = Str(node, "Portrait");
                if (key.Length == 0 && Str(node, "Speaker") != "Narrator") key = Str(node, "Speaker");
                if (key.Length == 0)
                    key = scene == null || Str(scene, "Relationship") == "tirabade" || Str(scene, "Owner") == "Together" ? "Together"
                        : (string)active.bridge.Assembly.GetType("Tirabade.Rules", true)!.GetMethod("SenderOf")!.Invoke(null, new[] { scene })!;
                bool eventPage = (string?)kinds[page.AssetGuid.ToString()] == "event" && Str(node, "Portrait").Length == 0;
                if (!eventPage)
                {
                    var portrait = main.GetMethod("Portrait", Static, null, new[] { typeof(string) }, null)!.Invoke(null, new object[] { key }) as UnityEngine.Sprite;
                    expected = portrait?.name ?? "native fallback";
                    if (portrait != null && sprite != portrait) active.result.Findings.Add("Authored portrait differs on " + page.AssetGuid);
                }
                else expected = "native event picture";
            }
            active.result.Observations.Add(new NativeSlideObservation { Event = "presentation", Cue = page.AssetGuid.ToString(), Name = page.name,
                Picture = sprite?.name ?? "none", ExpectedPicture = expected });
        }
        void Track(ActionList list, BlueprintCueBase cue, string stage)
        {
            if (list == null) return;
            if (!actionLists.TryGetValue(list, out var owners)) actionLists[list] = owners = new List<(string, string)>();
            var owner = (cue.AssetGuid.ToString(), stage);
            if (!owners.Contains(owner)) owners.Add(owner);
        }
        static void RanActions(ActionList __instance)
        {
            if (active == null || !active.actionLists.TryGetValue(__instance, out var owners)) return;
            foreach (var owner in owners)
                if (Resolve(owner.Cue) is BlueprintCueBase cue) active.Observe(owner.Event, cue, active.Shapes(__instance));
        }
        void Observe(string stage, BlueprintCueBase cue, IEnumerable<string> actions) => result.Observations.Add(new NativeSlideObservation
        { Event = stage, Cue = cue.AssetGuid.ToString(), Name = cue.name, Actions = actions.ToList() });
        List<string> Shapes(ActionList? actions)
        {
            var policy = bridge.Assembly.GetType("Tirabade.NativeEpilogueEdit", true)!;
            return (actions?.Actions ?? Array.Empty<GameAction>()).Select(a =>
            {
                string shape = (string)policy.GetMethod("ActionShape")!.Invoke(null, new object[] { a })!;
                string? image = (string?)policy.GetMethod("ImageOf")!.Invoke(null, new object[] { a });
                return image == null ? shape : shape + ":image=" + image;
            }).ToList();
        }
        BlueprintCueBase? RegisteredBase(string name)
        {
            var guid = bridge.Assembly.GetType("Tirabade.Main", true)!.GetMethod("GuidFor", Static)!.Invoke(null, new object[] { name });
            return Resolve(guid!.ToString()!) as BlueprintCueBase;
        }
        BlueprintCue? Registered(string name) => RegisteredBase(name) as BlueprintCue;
        void AddRow(string kind, string target, string scene, string relationship, BlueprintCue? cue, bool expected, bool attached, string parent, string image)
        {
            var row = new NativeSlideRow { Kind = kind, Target = target, Scene = scene, Relationship = relationship,
                Cue = cue?.AssetGuid.ToString() ?? "", Expected = expected, Attached = attached, Parent = parent, ImagePolicy = image };
            if (cue != null)
            {
                row.CanShow = cue.CanShow(); row.Continue = cue.Continue.Cues.Select(r => r.Guid.ToString()).ToList();
                row.OnShow = Shapes(cue.OnShow); row.OnStop = Shapes(cue.OnStop); row.Speaker = cue.Speaker?.ToString() ?? "";
                row.TextKey = (string?)bridge.Assembly.GetType("Tirabade.NativeEpilogueEdit", true)!.GetMethod("TextKey")!.Invoke(null, new object[] { cue.Text }) ?? "";
                row.Text = cue.Text?.ToString() ?? "";
            }
            result.Inventory.Add(row);
        }
        void BuildInventory(IDictionary edits)
        {
            var rules = bridge.Assembly.GetType("Tirabade.Rules", true)!;
            var policy = bridge.Assembly.GetType("Tirabade.NativeEpilogueEdit", true)!;
            var reviewed = (IDictionary)policy.GetField("Reviewed")!.GetValue(null)!;
            var selectedMethod = rules.GetMethods().Single(m => m.Name == "SelectNativeEditVariant" && m.GetParameters().Length == 4);
            foreach (DictionaryEntry pair in edits)
            {
                string target = (string)pair.Key;
                var spec = pair.Value;
                var variants = (Array)rules.GetMethod("EditVariants")!.Invoke(null, new[] { spec })!;
                var scenes = rules.GetMethod("EditScenes")!.Invoke(null, new[] { bridge.Story, variants })!;
                int selected = (int)selectedMethod.Invoke(null, new[] { bridge.Story, variants, scenes, snapshot })!;
                var original = Resolve(target) as BlueprintCue;
                var parent = Resolve(Str(spec, "Parent"));
                var members = !string.IsNullOrEmpty(Str(spec, "Page")) ? (Resolve(Str(spec, "Page")) as BlueprintBookPage)?.Cues
                    : parent is BlueprintCue pc ? pc.Continue.Cues : parent is BlueprintAnswer pa ? pa.NextCue.Cues : (parent as BlueprintDialog)?.FirstCue.Cues;
                string parentId = Str(spec, "Page") + Str(spec, "Parent");
                bool originalAttached = original != null && members?.Count(r => r.Guid == original.AssetGuid) == 1;
                AddRow("native", target, "", "", original, selected < 0, originalAttached, parentId, "original");
                if (!originalAttached) result.Findings.Add("Original native cue missing/duplicated: " + target);
                var order = new List<string>();
                for (int i = 0; i < variants.Length; i++)
                {
                    var variant = variants.GetValue(i)!;
                    string sceneId = Str(variant, "Replacement");
                    var scene = bridge.Scenes.Cast<object>().Single(s => Str(s, "Id") == sceneId);
                    string name = (string)rules.GetMethod("NativeEditCueName")!.Invoke(null, new object[] { target, spec, i })!;
                    var cue = Registered(name);
                    if (cue != null) order.Add(cue.AssetGuid.ToString());
                    bool attached = cue != null && members != null && members.Count(r => r.Guid == cue.AssetGuid) == 1;
                    AddRow("replacement", target, sceneId, Str(scene, "Relationship"), cue, selected == i, attached, parentId,
                        (bool)Field(variant, "KeepNativeImage")! ? "native" : "page");
                    if (!attached) result.Findings.Add("Missing replacement attachment: " + sceneId);
                    if (cue != null && original != null && reviewed.Contains(target))
                    {
                        var evidence = reviewed[target]!;
                        bool keep = (bool)Field(variant, "KeepNativeImage")!;
                        bool copyShow = keep || !string.IsNullOrEmpty(Str(spec, "Parent")) && Field(evidence, "OnShow") != null;
                        if (copyShow ? !Shapes(cue.OnShow).SequenceEqual(Shapes(original.OnShow)) : cue.OnShow.Actions.Length != 0)
                            result.Findings.Add("Replacement image action differs: " + sceneId);
                        var expectedStop = Field(evidence, "OnStop") == null ? new List<string>() : Shapes(original.OnStop);
                        if (!Shapes(cue.OnStop).SequenceEqual(expectedStop)) result.Findings.Add("Replacement OnStop differs: " + sceneId);
                        var expectedContinue = Field(evidence, "ParentContinue") != null || !string.IsNullOrEmpty(Str(spec, "Parent"))
                            ? original.Continue.Cues.Select(r => r.Guid.ToString()).ToList() : new List<string>();
                        if (!cue.Continue.Cues.Select(r => r.Guid.ToString()).SequenceEqual(expectedContinue)) result.Findings.Add("Replacement continuation differs: " + sceneId);
                    }
                }
                if (members != null && original != null)
                {
                    var ids = members.Select(r => r.Guid.ToString()).ToList();
                    int at = ids.IndexOf(original.AssetGuid.ToString());
                    if (at < order.Count || !ids.Skip(at - order.Count).Take(order.Count).SequenceEqual(order))
                        result.Findings.Add("Replacement order differs before " + target);
                }
            }
            foreach (var scene in bridge.Scenes.Cast<object>().Where(s => Str(s, "Owner").EndsWith("Epilogue", StringComparison.Ordinal)))
            {
                if ((bool)rules.GetMethod("IsNativeReplacement")!.Invoke(null, new[] { bridge.Story, scene })!) continue;
                var node = Items(Field(scene, "Nodes")).First();
                string prefix = Str(scene, "Id") + "." + Str(node, "Id");
                var page = RegisteredBase("page." + prefix) as BlueprintBookPage;
                bool available = bridge.Available(scene, snapshot);
                if (page == null) { result.Findings.Add("Authored epilogue page missing: " + Str(scene, "Id")); continue; }
                string sequenceId = SequenceOf(scene);
                var sequence = Resolve(sequenceId) as BlueprintCueSequence;
                bool attached = sequence?.Cues.Count(r => r.Guid == page.AssetGuid) == 1;
                if (sequence != null) result.LoadedSequences[sequenceId] = sequence.Cues.Select(r => r.Guid.ToString()).ToList();
                if (!attached) result.Findings.Add("Authored page not once in its sequence: " + Str(scene, "Id"));
                foreach (var cue in page.Cues.Select(r => r.Get()).OfType<BlueprintCue>())
                {
                    AddRow("authored", "", Str(scene, "Id"), Str(scene, "Relationship"), cue,
                        available && cue.CanShow(), attached, page.AssetGuid.ToString(), "portrait=" + Str(node, "Portrait"));
                    result.Inventory.Last().Page = page.AssetGuid.ToString();
                }
            }
            // Suppressions have no replacement text. Inventory their real guards as well.
            foreach (DictionaryEntry pair in (IDictionary)Field(bridge.Story!, "NativeEpilogueSuppressions")!)
                AddRow("suppression", (string)pair.Key, "", Str(pair.Value, "Relationship"), Resolve((string)pair.Key) as BlueprintCue,
                    !(bool)rules.GetMethod("WhenHolds")!.Invoke(null, new[] { Field(pair.Value, "When"), snapshot })!, true, Str(pair.Value, "Page"), "native");
        }
        internal BlueprintDialog Dialog => dialog;
        internal void Evaluate(NativeSlideCase scenario)
        {
            var shown = result.Observations.Where(o => o.Event == "shown").Select(o => o.Cue).ToList();
            foreach (var row in result.Inventory.Where(r => r.Target == scenario.Target && scenario.Target != ""))
            {
                bool eligible = scenario.NativeEligible.Contains(scenario.Target);
                if (result.Forced && (row.Expected && eligible) != shown.Contains(row.Cue))
                    result.Findings.Add("Selection differs for " + row.Scene + " / " + row.Cue);
            }
            foreach (var row in result.Inventory.Where(r => shown.Contains(r.Cue)))
            {
                if (!row.Expected) result.Findings.Add("Unexpected selected slide: " + row.Scene + " / " + row.Cue);
                if (row.OnShow.Count > 0 && !result.Observations.Any(o => o.Cue == row.Cue && o.Event == "OnShow" && o.Actions.SequenceEqual(row.OnShow)))
                    result.Findings.Add("OnShow not observed: " + row.Cue);
                if (row.OnStop.Count > 0 && !result.Observations.Any(o => o.Cue == row.Cue && o.Event == "OnStop" && o.Actions.SequenceEqual(row.OnStop)))
                    result.Findings.Add("OnStop not observed: " + row.Cue);
                // A native Continue is a First selection; alternatives are not all mandatory. In natural states
                // an entirely gated continuation legitimately shows nothing. Forced target cases exercise it.
                if (result.Forced && row.Target == scenario.Target && row.Continue.Count > 0 && !row.Continue.Any(shown.Contains))
                    result.Findings.Add("Continuation not observed: " + row.Cue + " -> " + string.Join(",", row.Continue));
            }
            foreach (string expected in scenario.ExpectShown)
                if (!shown.Contains(expected) && !result.Observations.Any(o => o.Name == expected && o.Event == "shown")) result.Findings.Add("Expected cue absent: " + expected);
            foreach (string hidden in scenario.ExpectHidden)
                if (shown.Contains(hidden) || result.Observations.Any(o => o.Name == hidden && o.Event == "shown")) result.Findings.Add("Forbidden cue shown: " + hidden);
            if (shown.Count == 0) result.Findings.Add("No live basic cue was observed");
            if (result.Forced && scenario.Target == "" && scenario.ExpectedCandidate != ""
                && !result.Inventory.Any(r => r.Scene == scenario.ExpectedCandidate && (!r.Expected || shown.Contains(r.Cue))))
                result.Findings.Add("Available authored page not reached: " + scenario.ExpectedCandidate);
            foreach (var row in result.Inventory.Where(r => r.Kind == "authored" && shown.Contains(r.Cue)))
                if (!result.Observations.Any(o => o.Event == "presentation" && o.Cue == row.Page))
                    result.Findings.Add("Authored page presentation not observed: " + row.Scene);
            result.Degraded = bridge.Degraded; result.Warnings = bridge.Warnings;
            if (result.Degraded.Count > 0) result.Findings.Add("Relationships degraded: " + string.Join(", ", result.Degraded));
            foreach (var warning in result.Warnings.Where(w => w.StartsWith("Native epilogue edit ", StringComparison.Ordinal)
                || w.StartsWith("Native epilogue suppression ", StringComparison.Ordinal))) result.Findings.Add(warning);
            result.Passed = result.Result == "completed" && result.Findings.Count == 0;
        }
        public void Dispose()
        {
            if (disposed) return;
            disposed = true;
            try { dialog.FirstCue = firstCue; patches.UnpatchAll(patches.Id); }
            finally { if (ReferenceEquals(active, this)) active = null; }
        }
    }
}
// END eng7-f5
