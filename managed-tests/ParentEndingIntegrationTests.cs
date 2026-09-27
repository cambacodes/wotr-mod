using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Reflection.Emit;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using HarmonyLib;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.Controllers.Dialog;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.DialogSystem.State;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.EntitySystem;
using Kingmaker.Localization;
using Newtonsoft.Json.Linq;
using Tirabade;

internal static class ParentEndingIntegrationTests
{
    private const BindingFlags Members = BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static | BindingFlags.Instance;
    private static readonly Type Service = typeof(Tirabade.Main).Assembly.GetType("Tirabade.ParentEndingIntegration", true)!;
    private static readonly Dictionary<BlueprintCueBase, ConditionsChecker> originalConditions = new Dictionary<BlueprintCueBase, ConditionsChecker>();
    private static readonly Dictionary<BlueprintBookPage, BlueprintCueBaseReference[]> originalCues = new Dictionary<BlueprintBookPage, BlueprintCueBaseReference[]>();
    private static readonly Dictionary<BlueprintBookPage, ActionList> originalActions = new Dictionary<BlueprintBookPage, ActionList>();
    private static readonly Dictionary<BlueprintCue, LocalizedString> originalTexts = new Dictionary<BlueprintCue, LocalizedString>();
    private static readonly Dictionary<Element, SimpleBlueprint> originalOwners = new Dictionary<Element, SimpleBlueprint>();
    private static Action? during;
    private sealed class Effect : GameAction
    {
        internal Action Apply = null!;
        public override string GetCaption() => "Controlled native page effect";
        public override void RunAction() => Apply();
    }
    private static T Seed<T>(string guid) where T : SimpleBlueprint, new()
    {
        var id = BlueprintGuid.Parse(guid);
        var prior = ResourcesLibrary.TryGetBlueprint(id);
        if (prior != null) return (T)prior;
        var result = new T { AssetGuid = id, name = "ReviewedParentFixture_" + guid };
        ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(id, result);
        return result;
    }
    private static BlueprintCueBaseReference Ref(BlueprintCueBase cue)
    {
        var result = new BlueprintCueBaseReference();
        AccessTools.Field(typeof(BlueprintReferenceBase), "deserializedGuid").SetValue(result, cue.AssetGuid);
        return result;
    }
    private static LocalizedString Text(string key)
    {
        var result = new LocalizedString(); AccessTools.Field(typeof(LocalizedString), "m_Key").SetValue(result, key); return result;
    }

    private static void OwnConditions(BlueprintCueBase cue, ConditionsChecker checker)
    {
        foreach (var condition in checker.Conditions)
        {
            condition.Owner = cue;
            if (!cue.ElementsArray.Contains(condition)) cue.ElementsArray.Add(condition);
            var nested = condition.GetType().GetField("ConditionsChecker", Members)?.GetValue(condition) as ConditionsChecker;
            if (nested != null) OwnConditions(cue, nested);
        }
    }

    // The isolated harness reconstructs extracted parent expressions using actual native condition classes.
    // No condition is replaced with a fabricated successful result.
    internal static void PrepareSourceFixtures(JObject evidence, Dictionary<string, ConditionsChecker> conditions, ActionList markParentPages)
    {
        var ordinary = Seed<BlueprintCueSequence>("ed4baeaf69394754902344f0598d7e5a");
        var aeon = Seed<BlueprintCueSequence>("ced82f299d246f448b48afa0b630dd70");
        var filler = Seed<BlueprintCue>("d741e024073740a69d9c730c2a16fa16");
        filler.Conditions = new ConditionsChecker { Conditions = Array.Empty<Condition>() };
        foreach (var group in evidence.Properties().GroupBy(property => (string)property.Value["page"]!))
        {
            var page = Seed<BlueprintBookPage>(group.Key);
            page.ShowOnce = true;
            page.Conditions = conditions[group.Key];
            page.OnShow = (string)group.First().Value["file"]! == "SlideAeon.cs"
                ? new ActionList { Actions = Array.Empty<GameAction>() } : markParentPages;
            page.Cues.Clear();
            foreach (var property in group)
            {
                var cue = Seed<BlueprintCue>(property.Name);
                cue.ShowOnce = true;
                cue.Conditions = conditions[property.Name];
                cue.Text = Text((string)property.Value["key"]!);
                LocalizationManager.CurrentPack.PutString(cue.Text.Key, (string)property.Value["original_text"]!);
                cue.OnShow = new ActionList { Actions = Array.Empty<GameAction>() };
                cue.OnStop = new ActionList { Actions = Array.Empty<GameAction>() };
                cue.Continue = new CueSelection(); cue.Speaker = new DialogSpeaker { NoSpeaker = true };
                page.Cues.Add(Ref(cue));
                originalConditions.Add(cue, cue.Conditions); originalTexts.Add(cue, cue.Text);
            }
            page.Cues.Add(Ref(filler));
            ((string)group.First().Value["file"]! == "SlideAeon.cs" ? aeon : ordinary).Cues.Add(Ref(page));
            originalConditions.Add(page, page.Conditions); originalCues.Add(page, page.Cues.ToArray()); originalActions.Add(page, page.OnShow);
        }
        var pair = Seed<BlueprintBookPage>("5c95d8e3fa4f3b44896914987cb04b0b");
        var pairedCue = Seed<BlueprintCue>("5787f92575364c1459df8f075676c2db");
        pairedCue.Conditions = conditions[pairedCue.AssetGuid.ToString()];
        pairedCue.Text = Text("056942f6-32d0-4480-8ff7-29356b43db19");
        pairedCue.OnShow = new ActionList { Actions = Array.Empty<GameAction>() };
        pairedCue.OnStop = new ActionList { Actions = Array.Empty<GameAction>() };
        pairedCue.Continue = new CueSelection(); pairedCue.Speaker = new DialogSpeaker { NoSpeaker = true };
        pair.Conditions = conditions[pair.AssetGuid.ToString()]; pair.Cues.Add(Ref(pairedCue));
        pair.OnShow = new ActionList { Actions = Array.Empty<GameAction>() };
        Seed<BlueprintCueSequence>("f8d7f50e3bb88c143834d234c0b24474").Cues.Add(Ref(pair));
        originalConditions.Add(pair, pair.Conditions); originalConditions.Add(pairedCue, pairedCue.Conditions);
        originalCues.Add(pair, pair.Cues.ToArray()); originalActions.Add(pair, pair.OnShow); originalTexts.Add(pairedCue, pairedCue.Text);
        foreach (var entry in originalConditions) OwnConditions(entry.Key, entry.Value);
        foreach (var element in originalConditions.Keys.SelectMany(cue => cue.ElementsArray).Distinct()) originalOwners[element] = element.Owner;
    }

    internal static void CheckPreflight(Story story, Action<bool, string> check)
    {
        SimpleBlueprint Resolve(string id) => ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(id));
        var ordinary = (BlueprintCueSequence)Resolve("ed4baeaf69394754902344f0598d7e5a");
        var aeon = (BlueprintCueSequence)Resolve("ced82f299d246f448b48afa0b630dd70");
        var special = (BlueprintCueSequence)Resolve("f8d7f50e3bb88c143834d234c0b24474");
        var pair = (BlueprintBookPage)Resolve("5c95d8e3fa4f3b44896914987cb04b0b");
        var target = (BlueprintCue)Resolve("a875684118e64d7ab29f70ca3460c365");
        int registrations = 0;
        object? Prepare() => Service.GetMethod("Prepare", Members)!.Invoke(null, new object[] { story, ordinary, aeon,
            new Func<string, SimpleBlueprint>(Resolve), new Func<string, BlueprintCue>(id => { registrations++; return new BlueprintCue { AssetGuid = BlueprintGuid.Parse(Guid.NewGuid().ToString("N")) }; }),
            new Func<Snapshot?>(() => null) });
        void Reject(Action mutate, Action restore, string label)
        {
            bool rejected = false;
            try { mutate(); Prepare(); }
            catch (TargetInvocationException ex) when (ex.InnerException is InvalidOperationException) { rejected = true; }
            finally { restore(); }
            check(rejected && registrations == 0, label + " mutated or registered before rejection.");
        }
        var originalKey = target.Text;
        Reject(() => target.Text = Text("wrong-original-key"), () => target.Text = originalKey, "Changed original localization");
        var specialRefs = special.Cues.ToArray();
        Reject(() => special.Cues.Clear(), () => special.Cues.AddRange(specialRefs), "Missing native Special membership");
        Reject(() => aeon.Cues.Add(Ref(pair)), () => aeon.Cues.RemoveAt(aeon.Cues.Count - 1), "Ordinary page in Aeon");
        var originalActions = target.OnShow;
        Reject(() => target.OnShow = new ActionList { Actions = new GameAction[] { new Effect() } },
            () => target.OnShow = originalActions, "Unexpected original cue action graph");
        var prepared = Prepare();
        check(prepared != null && registrations == 17, "Reviewed preflight could not prepare the expected families.");
        var oldPageChecker = pair.Conditions;
        var oldTargetChecker = target.Conditions;
        target.Text = Text("changed-after-registration");
        bool attachRejected = false;
        try { Service.GetMethod("Attach", Members)!.Invoke(prepared, null); }
        catch (TargetInvocationException ex) when (ex.InnerException is InvalidOperationException) { attachRejected = true; }
        finally { target.Text = originalKey; }
        check(attachRejected && ReferenceEquals(pair.Conditions, oldPageChecker) && ReferenceEquals(target.Conditions, oldTargetChecker),
            "Changed post-registration cue mutated originals before Attach rejection.");
    }

    private static void OptionalPatch() { }

    [MethodImpl(MethodImplOptions.NoInlining)]
    private static void SimulatedPlay(object controller, BlueprintBookPage page)
    {
        page.OnShow.Run();
        during?.Invoke();
    }
    [MethodImpl(MethodImplOptions.NoInlining)]
    private static bool SimulatedPreview(BlueprintBookPage page) { during?.Invoke(); return true; }

    internal static void Run(Story story, Action<bool, string> check)
    {
        var instance = typeof(Tirabade.Main).GetField("parentEndings", Members)!.GetValue(null)!;
        check(instance != null, "Main did not prepare and attach parent endings.");
        var registered = (List<SimpleBlueprint>)typeof(Tirabade.Main).GetField("registered", Members)!.GetValue(null)!;
        var variants = registered.OfType<BlueprintCue>().Where(cue => cue.name.StartsWith("RRT_parent-ending.", StringComparison.Ordinal)).ToArray();
        check(variants.Length == 17, "Wrong reviewed ordinary/survivor variant count.");
        foreach (var pair in originalOwners) check(ReferenceEquals(pair.Key.Owner, pair.Value), "Native nested condition owner changed.");
        foreach (var pair in originalTexts)
            check(ReferenceEquals(pair.Key.Text, pair.Value), "Native localization object was replaced.");
        foreach (var pair in originalActions)
            check(ReferenceEquals(pair.Key.OnShow, pair.Value), "Parent page arbitration actions were replaced.");
        foreach (var pair in originalCues)
        {
            var retained = pair.Key.Cues.Where(reference => !variants.Contains(reference.Get())).ToArray();
            check(retained.SequenceEqual(pair.Value), "Original cue order or reference objects changed.");
        }
        var familyOriginals = new HashSet<BlueprintCue>();
        foreach (var variant in variants)
        {
            var binding = variant.Conditions.Conditions.Single().GetType().GetField("Binding", Members)!.GetValue(variant.Conditions.Conditions.Single())!;
            var original = ((BlueprintCue[])binding.GetType().GetField("Members", Members)!.GetValue(binding)!)[0];
            familyOriginals.Add(original);
            check(ReferenceEquals(original.OnShow, variant.OnShow) && ReferenceEquals(original.OnStop, variant.OnStop)
                && ReferenceEquals(original.Continue, variant.Continue), "Variant lost exact native behavior objects.");
            check(ReferenceEquals(binding.GetType().GetField("Original", Members)!.GetValue(binding), originalConditions[original]), "Original native checker was approximated.");
            check(variant.ElementsArray.Count == 1 && variant.ElementsArray[0].Owner == variant
                && originalConditions[original].Conditions.All(condition => condition == null || condition.Owner != variant), "Owner pass reparented original conditions.");
            check(variant.Text.Key != original.Text.Key && variant.ShowOnce == original.ShowOnce
                && variant.ShowOnceCurrentDialog == original.ShowOnceCurrentDialog, "Variant changed localization or history policy.");
        }
        foreach (var pair in originalConditions.Where(pair => !(pair.Key is BlueprintCue cue) || !familyOriginals.Contains(cue)))
        {
            var current = pair.Key.Conditions.Conditions.FirstOrDefault();
            if (current?.GetType().Name == "Guard") check(ReferenceEquals(current.GetType().GetField("Original", Members)!.GetValue(current), pair.Value), "Suppression changed original checker.");
        }
        int cueCount = originalCues.Keys.Sum(page => page.Cues.Count);
        Service.GetMethod("Attach", Members)!.Invoke(instance, null);
        check(originalCues.Keys.Sum(page => page.Cues.Count) == cueCount, "Repeated attachment duplicated variants.");

        var play = AccessTools.Method(typeof(DialogController), "PlayBookPage");
        var preview = AccessTools.Method(typeof(DialogController), "CanShowAnyCue");
        check(Harmony.GetPatchInfo(play)?.Transpilers.Any(patch => patch.PatchMethod.DeclaringType == Service) == true
            && Harmony.GetPatchInfo(play)!.Finalizers.Any(patch => patch.PatchMethod.DeclaringType == Service)
            && Harmony.GetPatchInfo(preview)?.Prefixes.Any(patch => patch.PatchMethod.DeclaringType == Service) == true,
            "Actual native page hooks were not installed.");
        var originalIl = PatchProcessor.GetOriginalInstructions(play).ToList();
        var transpile = Service.GetMethod("Transpile", Members)!;
        var patched = ((IEnumerable<CodeInstruction>)transpile.Invoke(null, new object[] { originalIl })!).ToList();
        int injection = patched.FindIndex(instruction => instruction.operand is MethodInfo method && method.Name == "AfterPageShow");
        check(injection > 1 && patched[injection - 1].opcode == OpCodes.Ldarg_1
            && patched[injection - 2].Calls(AccessTools.Method(typeof(ActionList), "Run")), "Refresh hook is not after native page actions.");
        var labeled = originalIl.Select(instruction => new CodeInstruction(instruction)).ToList();
        int afterActions = labeled.FindIndex(instruction => instruction.Calls(AccessTools.Method(typeof(ActionList), "Run"))) + 1;
        var label = new DynamicMethod("FixtureLabel", typeof(void), Type.EmptyTypes).GetILGenerator().DefineLabel();
        labeled[afterActions].labels.Add(label);
        var labeledResult = ((IEnumerable<CodeInstruction>)transpile.Invoke(null, new object[] { labeled })!).ToList();
        check(labeledResult[afterActions].labels.Count == 0 && labeledResult[afterActions + 2].labels.Contains(label),
            "Branch target moved onto refresh and changed the original skip-actions path.");
        foreach (var instructions in new[] { new List<CodeInstruction>(), originalIl.Concat(originalIl).ToList() })
        {
            bool rejected = false;
            try { transpile.Invoke(null, new object[] { instructions }); } catch (TargetInvocationException ex) when (ex.InnerException is InvalidOperationException) { rejected = true; }
            check(rejected, "Incompatible hook shape did not fail before mutation.");
        }

        var oldGame = AccessTools.Field(typeof(Game), "s_Instance").GetValue(null);
        var observer = Service.GetField("observe", Members)!;
        var oldObserver = observer.GetValue(instance);
        var target = (BlueprintCue)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse("a875684118e64d7ab29f70ca3460c365"));
        var pageTarget = originalCues.Single(pair => pair.Value.Any(reference => reference.Get() == target)).Key;
        var member = target.Conditions.Conditions.Single();
        var family = member.GetType().GetField("Binding", Members)!.GetValue(member)!;
        int Selected() => (int)family.GetType().GetField("selected", Members)!.GetValue(family)!;
        var pageActions = pageTarget.OnShow;
        var flags = new HashSet<string>();
        int observations = 0;
        var harness = new Harmony("RanRomance.Tirabade.ParentEndingTest");
        try
        {
            var game = (Game)FormatterServices.GetUninitializedObject(typeof(Game));
            var state = (PersistentState)FormatterServices.GetUninitializedObject(typeof(PersistentState));
            var player = (Player)FormatterServices.GetUninitializedObject(typeof(Player));
            AccessTools.Field(typeof(PersistentState), "PlayerState").SetValue(state, player);
            AccessTools.Field(typeof(Game), "State").SetValue(game, state);
            AccessTools.Field(typeof(Player), "m_Dialog").SetValue(player, new DialogState());
            AccessTools.Field(typeof(Game), "s_Instance").SetValue(null, game);
            observer.SetValue(instance, new Func<Snapshot?>(() => { observations++; return new Snapshot {
                Chapter = 5, Flags = new HashSet<string>(flags), Hour = 1000 }; }));
            HarmonyMethod Hook(string name) => new HarmonyMethod(Service.GetMethod(name, Members)!);
            harness.Patch(AccessTools.Method(typeof(ParentEndingIntegrationTests), nameof(SimulatedPlay)),
                prefix: Hook("PlayPrefix"), postfix: Hook("Finished"), finalizer: Hook("Finalized"), transpiler: Hook("Transpile"));
            harness.Patch(AccessTools.Method(typeof(ParentEndingIntegrationTests), nameof(SimulatedPreview)),
                prefix: Hook("PreviewPrefix"), postfix: Hook("Finished"), finalizer: Hook("Finalized"));
            int actions = 0;
            pageTarget.OnShow = new ActionList { Actions = new GameAction[] { new Effect { Owner = pageTarget, Apply = () => {
                actions++; check(observations == 0, "Playback refreshed before page actions."); flags.Add("minachiv.invitation_kept"); } } } };
            during = () =>
            {
                check(Selected() == 1 && observations == 1 && actions == 1, "Page action did not precede earned selection.");
                flags.Add("minagho.dead"); flags.Add("chivarro.dead");
                var callback = during; during = null;
                SimulatedPreview(pageTarget);
                during = callback;
                check(Selected() == 1 && observations == 1, "Nested preview replaced or invalidated playing selection.");
            };
            SimulatedPlay(new object(), pageTarget);
            check(Selected() == 0, "Playback postfix left stale selection.");
            pageTarget.OnShow = new ActionList { Actions = Array.Empty<GameAction>() };
            during = () => { check(Selected() == -1, "New batch ignored current earned deaths."); throw new InvalidOperationException("Controlled page failure"); };
            bool preserved = false;
            try { SimulatedPlay(new object(), pageTarget); } catch (InvalidOperationException ex) { preserved = ex.Message == "Controlled page failure"; }
            check(preserved && Selected() == 0, "Finalizer swallowed native exception or kept stale batch.");
            var optional = new Harmony("RanEpilogue");
            try
            {
                optional.Patch(AccessTools.Method(typeof(ParentEndingIntegrationTests), nameof(OptionalPatch)),
                    prefix: new HarmonyMethod(AccessTools.Method(typeof(ParentEndingIntegrationTests), nameof(OptionalPatch))));
                during = () => check(Selected() == 0, "Unverified alternate delivery topology suppressed original.");
                SimulatedPreview(pageTarget);
                check(Service.GetProperty("LastObservationError", Members)!.GetValue(instance) is InvalidOperationException,
                    "Unsupported topology omitted diagnostic.");
            }
            finally { optional.UnpatchAll(optional.Id); }
            observer.SetValue(instance, new Func<Snapshot?>(() => throw new InvalidOperationException("Observation unavailable")));
            during = () => check(Selected() == 0, "Failed observation suppressed original.");
            SimulatedPreview(pageTarget);
            check(Service.GetProperty("LastObservationError", Members)!.GetValue(instance) is InvalidOperationException, "Observation failure lost diagnostics.");
            int failedReads = 0;
            observer.SetValue(instance, new Func<Snapshot?>(() => { failedReads++; return failedReads == 1 ? null : new Snapshot { Chapter = 5, Flags = new HashSet<string>(flags), Hour = 1000 }; }));
            var plans = (IDictionary)Service.GetField("plans", Members)!.GetValue(instance)!;
            var plan = plans[pageTarget];
            during = () => check(!(bool)Service.GetMethod("PageSuppressed", Members)!.Invoke(instance, new[] { plan })!
                && failedReads == 1, "Null batch snapshot was reread into a contradictory page suppression.");
            SimulatedPreview(pageTarget);
            during = null;
        }
        finally
        {
            during = null; harness.UnpatchAll(harness.Id); pageTarget.OnShow = pageActions;
            observer.SetValue(instance, oldObserver); AccessTools.Field(typeof(Game), "s_Instance").SetValue(null, oldGame);
        }
    }
}
