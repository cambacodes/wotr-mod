using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using Kingmaker;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Area;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.Controllers.Dialog;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.DialogSystem.State;
using Kingmaker.GameModes;
using Newtonsoft.Json;

internal static class IrabethMeetingIntegrationTests
{
    private const BindingFlags Members = BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;
    private static readonly Type Main = typeof(Tirabade.Main);
    private static readonly Type Meeting = Main.Assembly.GetType("Tirabade.IrabethMeeting", true)!;
    private static FieldInfo Field(Type type, string name)
    {
        for (Type? current = type; current != null; current = current.BaseType)
        {
            var field = current.GetField(name, Members | BindingFlags.DeclaredOnly);
            if (field != null) return field;
        }
        throw new InvalidOperationException("Missing native fixture field: " + name);
    }
    private static void Set(object value, string name, object? data) => Field(value.GetType(), name).SetValue(value, data);
    private static string Constant(string name) => (string)Meeting.GetField(name, Members)!.GetRawConstantValue()!;
    private static T Seed<T>(string guid) where T : SimpleBlueprint, new()
    {
        var id = BlueprintGuid.Parse(guid);
        var prior = ResourcesLibrary.TryGetBlueprint(id);
        if (prior != null) return (T)prior;
        var blueprint = new T { AssetGuid = id, name = "NativeMeetingFixture_" + guid };
        ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(id, blueprint);
        return blueprint;
    }
    private static T Reference<T>(SimpleBlueprint blueprint) where T : BlueprintReferenceBase, new()
    {
        var result = new T();
        Set(result, "deserializedGuid", blueprint.AssetGuid);
        Set(result, "<Cached>k__BackingField", blueprint);
        return result;
    }

    // Detached native fixtures with the audited placement shape, seeded before actual Main.Build.
    internal static void PrepareNativePlacement()
    {
        var group = Seed<BlueprintEtudeConflictingGroup>(Constant("Group"));
        Seed<BlueprintArea>(Constant("Capital"));
        Seed<BlueprintEtude>(Constant("Expedition"));
        Seed<BlueprintEtude>(Constant("Death"));
        Seed<BlueprintEtude>(Constant("Gone"));
        foreach (string name in new[] { "Hidden", "Throne", "Departure" })
        {
            bool visible = name == "Throne";
            var bp = Seed<BlueprintEtude>(Constant(name));
            bp.Priority = visible ? -50 : name == "Departure" ? 99 : -100;
            Set(bp, "m_Parent", new BlueprintEtudeReference());
            Set(bp, "m_ConflictingGroups", new List<BlueprintEtudeConflictingGroupReference> { Reference<BlueprintEtudeConflictingGroupReference>(group) });
            EntityReference Entity(string id) => new EntityReference { UniqueId = id, SceneAssetGuid = Constant("SceneAsset") };
            var unit = new UnitFromSpawner { Spawner = Entity(Constant("Spawner")), Owner = bp };
            var actions = new List<GameAction> { new HideUnit { Target = unit, Unhide = visible, Owner = bp } };
            if (visible)
            {
                var move = new TranslocateUnit { Unit = unit, Owner = bp,
                    translocatePositionEvaluator = new LocatorPosition { Locator = Entity(Constant("Locator")), Owner = bp },
                    translocateOrientationEvaluator = new LocatorOrientation { Locator = Entity(Constant("Locator")), Owner = bp } };
                Set(move, "m_CopyRotation", true);
                actions.Add(move);
            }
            bp.ComponentsArray = new BlueprintComponent[] { new EtudePlayTrigger { name = "NativeMeetingFixturePlacement",
                Conditions = new ConditionsChecker { Conditions = Array.Empty<Condition>() },
                Actions = new ActionList { Actions = actions.ToArray() } } };
        }
    }

    internal static void Run(Action<bool, string> check)
    {
        if (!MonoNativeBoundary.Enabled) { RunFixture(check); return; }
        using (var boundary = new MonoNativeBoundary(HarmonyLib.AccessTools.PropertyGetter(
            typeof(Kingmaker.EntitySystem.Persistence.LoadingProcess), "Instance"), nameof(IrabethMeetingIntegrationTests)))
        {
            RunFixture(check);
            check(boundary.Calls == 1, "Meeting Tick skipped or replayed its native loading boundary");
        }
    }

    private static void RunFixture(Action<bool, string> check)
    {
        var goneFact = (Etude)FormatterServices.GetUninitializedObject(typeof(Etude));
        var hideFact = (Etude)FormatterServices.GetUninitializedObject(typeof(Etude));
        var history = Meeting.GetMethod("DepartureHistoryPermits", Members)!;
        bool History() => (bool)history.Invoke(null, new object?[] { goneFact, hideFact })!;
        check(!History(), "Started-only Gone incorrectly witnesses actual departure");
        Set(goneFact, "<IsActive>k__BackingField", true);
        check(History() && !hideFact.IsPlaying, "Living post-coronation departure incorrectly requires its dormant hide child to play");
        Set(hideFact, "m_CompletionInProgress", true);
        check(!History(), "Completing hide history allowed correspondence");
        Set(hideFact, "m_CompletionInProgress", false);
        Set(hideFact, "m_IsCompleted", true);
        check(!History(), "Completed hide history allowed correspondence");
        Set(hideFact, "m_IsCompleted", false);
        Set(goneFact, "m_CompletionInProgress", true);
        check(!History(), "Completing Gone history allowed correspondence");
        Set(goneFact, "m_CompletionInProgress", false);
        Set(goneFact, "m_IsCompleted", true);
        check(!History(), "Completed Gone history allowed correspondence");
        check(!(bool)history.Invoke(null, new object?[] { null, hideFact })!
            && !(bool)history.Invoke(null, new object?[] { goneFact, null })!, "Missing native producer history allowed correspondence");
        var instance = Main.GetField("irabethMeeting", Members)!.GetValue(null)!;
        check(instance != null, "Actual Main.Build did not construct the personal meeting helper");
        var blueprint = (BlueprintEtude)Meeting.GetField("Blueprint", Members)!.GetValue(instance)!;
        var registered = (List<SimpleBlueprint>)Main.GetField("registered", Members)!.GetValue(null)!;
        check(registered.Contains(blueprint) && ReferenceEquals(ResourcesLibrary.TryGetBlueprint(blueprint.AssetGuid), blueprint),
            "Authored meeting is not registered before save restoration");
        check(blueprint.name == "RRT_etude.irabeth.personal_return" && blueprint.Priority == 100, "Wrong authored meeting identity/priority");
        check(blueprint.ActivationCondition.Conditions.Single().Owner == blueprint
            && blueprint.CompletionCondition.Conditions.Single().Owner == blueprint,
            "Actual Main.Build omitted meeting condition owners");
        check(blueprint.ComponentsArray.Single().OwnerBlueprint == blueprint, "Actual OnEnable omitted placement component owner");
        var throne = (BlueprintEtude)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(Constant("Throne")));
        var nativeActions = throne.ComponentsArray.OfType<EtudePlayTrigger>().Single().Actions.Actions;
        check(nativeActions.All(a => ReferenceEquals(a.Owner, throne)), "Main initialization reparented native placement actions");
        var flags = (Dictionary<string, BlueprintUnlockableFlag>)Main.GetField("flags", Members)!.GetValue(null)!;
        string retryKey = (string)Main.GetField("IrabethMeetingRetry", Members)!.GetRawConstantValue()!;
        check(flags.TryGetValue(retryKey, out var retry) && registered.Contains(retry)
            && ReferenceEquals(ResourcesLibrary.TryGetBlueprint(retry.AssetGuid), retry), "Retry counter lacks native saved flag identity");

        var saved = new UnlockableFlagsManager();
        void Write(string key, int value) => saved.UnlockedFlags[flags[key]] = value;
        int Read(string key) => flags.TryGetValue(key, out var flag) ? saved.GetFlagValue(flag) : 0;
        var requestMethod = Main.GetMethod("IrabethVisitRequest", Members)!;
        string? Request(int hour) => (string?)requestMethod.Invoke(null, new object[] { new Func<string, int>(Read), hour });
        check(Request(112) == null, "Missing saved consent created an Irabeth request");
        Write("irabeth.return_meeting_accepted", 1);
        check(Request(112) == null, "Acceptance without its saved timestamp invented elapsed time");
        Write("hour.irabeth.return_meeting_accepted", 101);
        check(Request(112) == null, "Accepted but unfinished reply created an unusable physical visit");
        Write("irabeth.return_reply", 1);
        check(Request(111) == null && Request(112) == "irabeth.return.first/0", "Visit ignored the 12-hour acceptance boundary");
        string first = Request(112)!;
        check(Request(10000) == first && Request(112) == first, "Observation invents retry episodes");
        foreach (string closure in new[] { "irabeth.closed", "closed" })
        {
            Write(closure, 1); check(Request(112) == null, "Closed route retained an unusable meeting claim");
            Write(closure, 0);
        }
        Write("irabeth.return_meeting_declined", 1);
        check(Request(112) == null, "Decline lost precedence over acceptance");
        Write("irabeth.return_meeting_declined", 0); Write("irabeth.return_meeting_accepted", 0);
        check(Request(112) == null, "Removed acceptance still authorized");
        Write("irabeth.return_meeting_accepted", 1); Write(retryKey, 1);
        check(Request(112) == "irabeth.return.first/1", "Explicit saved retry did not create a distinct stable episode");
        Write(retryKey, -1); check(Request(112) == null, "Negative retry counter accepted");
        Write(retryKey, int.MaxValue); check(Request(112) == "irabeth.return.first/2147483647", "Final representable episode cannot be observed");
        Write(retryKey, 1); Write("irabeth.return_first_words", 1);
        check(Request(500) == null, "Completed meeting retains authorization");
        Write("irabeth.return_first_words", 0);
        var serialized = JsonConvert.SerializeObject(saved.UnlockedFlags.ToDictionary(p => p.Key.AssetGuid.ToString(), p => p.Value));
        var copied = JsonConvert.DeserializeObject<Dictionary<string, int>>(serialized)!;
        var restored = new UnlockableFlagsManager();
        foreach (var pair in copied) restored.UnlockedFlags[(BlueprintUnlockableFlag)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(pair.Key))] = pair.Value;
        check(restored.GetFlagValue(retry!) == 1 && restored.GetFlagValue(flags["hour.irabeth.return_meeting_accepted"]) == 101,
            "Registered flags lost saved retry/time through JSON fixture reconstruction");

        var requestAllows = Meeting.GetMethod("RequestAllows", Members)!;
        var attempt = Meeting.GetMethod("AttemptPlacement", Members)!;
        var savedType = Meeting.GetNestedType("MeetingData", Members)!;
        var failedData = Activator.CreateInstance(savedType)!;
        Set(failedData, "ActorId", "actor-A"); Set(failedData, "Request", first);
        bool Allowed(string? request, string actor) => (bool)requestAllows.Invoke(null, new object?[] { failedData, request, actor })!;
        check(Allowed(first, "actor-A") && !Allowed(first, "actor-B") && !Allowed(null, "actor-A"), "Request accepted another actor or no consent");
        check(!(bool)attempt.Invoke(null, new object[] { failedData, new Func<bool>(() => false) })!, "Unverified placement became arrival");
        check(!Allowed(first, "actor-A") && Allowed("irabeth.return.first/1", "actor-A"), "Saved failure did not require explicit new episode");
        check((bool)attempt.Invoke(null, new object[] { failedData, new Func<bool>(() => true) })! && Allowed(first, "actor-A"), "Verified placement did not clear failure");
        try { attempt.Invoke(null, new object[] { failedData, new Func<bool>(() => throw new InvalidOperationException("placement fault")) }); }
        catch (TargetInvocationException ex) when (ex.InnerException is InvalidOperationException) { }
        check(!Allowed(first, "actor-A"), "Throwing placement lost its saved failure");

        var oldEnabled = Main.GetField("enabled", Members)!.GetValue(null);
        var oldGame = Field(typeof(Game), "s_Instance").GetValue(null);
        var oldRequest = Field(Meeting, "acceptedRequest").GetValue(instance);
        try
        {
            Main.GetField("enabled", Members)!.SetValue(null, false);
            check(Main.GetMethod("CurrentIrabethVisit", Members)!.Invoke(null, null) == null, "Disabled addon still supplies consent to native activation");
            check(!(bool)Main.GetMethod("CanRetryIrabethVisit", Members)!.Invoke(null, null)!, "Disabled addon offers a retry");
            var game = (Game)FormatterServices.GetUninitializedObject(typeof(Game));
            var player = (Player)FormatterServices.GetUninitializedObject(typeof(Player));
            var state = (PersistentState)FormatterServices.GetUninitializedObject(typeof(PersistentState));
            Set(state, "PlayerState", player); Set(game, "State", state);
            Field(typeof(Game), "s_Instance").SetValue(null, game);
            Main.GetField("enabled", Members)!.SetValue(null, true);
            game.IsUnloading = true;
            check(Main.GetMethod("CurrentIrabethVisit", Members)!.Invoke(null, null) == null, "Unload supplied an active visit");
            Meeting.GetMethod("Tick", Members)!.Invoke(instance, null);
            check(Meeting.GetProperty("LastError", Members)!.GetValue(instance) == null, "Unload Tick touched incomplete native state");
            game.IsUnloading = false;
            Set(game, "<LoadingSave>k__BackingField", FormatterServices.GetUninitializedObject(typeof(Kingmaker.EntitySystem.Persistence.SaveInfo)));
            check(Main.GetMethod("CurrentIrabethVisit", Members)!.Invoke(null, null) == null, "Save restoration supplied an active visit");
            Meeting.GetMethod("Tick", Members)!.Invoke(instance, null);
            check(Meeting.GetProperty("LastError", Members)!.GetValue(instance) == null, "Save-loading Tick mutated incomplete native state");
            Set(game, "<LoadingSave>k__BackingField", null);
            Set(player, "m_Dialog", new DialogState());
            var controller = (DialogController)FormatterServices.GetUninitializedObject(typeof(DialogController));
            Set(game, "DialogController", controller);
            var modes = new Stack<GameMode>();
            Set(game, "m_GameModes", modes);
            void Mode(GameModeType value)
            {
                modes.Clear();
                var mode = (GameMode)FormatterServices.GetUninitializedObject(typeof(GameMode));
                Set(mode, "Type", value); modes.Push(mode);
            }
            bool Window() => (bool)Main.GetMethod("IrabethVisitWindow", Members)!.Invoke(null, null)!;
            var dialogs = (Dictionary<string, BlueprintDialog>)Main.GetField("dialogs", Members)!.GetValue(null)!;
            bool hadScene = dialogs.TryGetValue("irabeth.return_first_words", out var priorDialog);
            try
            {
                // The narrative producer is separate; this fixture isolates the exact registered-dialog exemption.
                var ownDialog = new BlueprintDialog { name = "RRT_dialog.irabeth.return_first_words" };
                dialogs["irabeth.return_first_words"] = ownDialog;
                Mode(GameModeType.Default);
                check(Window(), "Idle native context rejected accepted visit window");
                Mode(GameModeType.Dialog); controller.Dialog = ownDialog;
                check(Window(), "Exact own dialog withdrew its actor");
                controller.Dialog = new BlueprintDialog { name = ownDialog.name };
                check(!Window(), "Unrelated same-name dialog retained the meeting");
                Set(player, "<IsInCombat>k__BackingField", true); controller.Dialog = ownDialog;
                check(!Window(), "Combat retained the temporary meeting");
                Set(player, "<IsInCombat>k__BackingField", false);
                Mode(GameModeType.Rest); check(!Window(), "Another event mode retained the meeting");
                controller.Dialog = null; Mode(GameModeType.Default);
            }
            finally
            {
                if (hadScene) dialogs["irabeth.return_first_words"] = priorDialog!;
                else dialogs.Remove("irabeth.return_first_words");
            }
            var system = (EtudesSystem)FormatterServices.GetUninitializedObject(typeof(EtudesSystem));
            var manager = new EntityFactsManager(system);
            Set(system, "Facts", manager);
            var tree = manager.EnsureFactProcessor<EtudesTree>();
            Set(system, "<Etudes>k__BackingField", tree); Set(player, "EtudesSystem", system);
            var fact = (Etude)FormatterServices.GetUninitializedObject(typeof(Etude));
            Set(fact, "<Blueprint>k__BackingField", blueprint);
            ((IList)Field(typeof(EntityFactsManager), "m_Facts").GetValue(manager)!).Add(fact);
            var runtime = ((IRuntimeEntityFactComponentProvider)blueprint.ComponentsArray.Single()).CreateRuntimeFactComponent();
            runtime.Setup(blueprint.ComponentsArray.Single()); Set(runtime, "<Fact>k__BackingField", fact);
            Set(fact, "Components", new List<EntityFactComponent> { runtime });
            var dataType = Meeting.GetNestedType("MeetingData", Members)!;
            var data = Activator.CreateInstance(dataType)!;
            Set(data, "Request", "irabeth.return.first/0"); Set(data, "ActorId", "retained-actor"); Set(data, "Failed", true);
            Set(runtime, "m_Data", data);
            string? episode = "irabeth.return.first/0";
            Field(Meeting, "acceptedRequest").SetValue(instance, new Func<string?>(() => episode));
            bool Failed() => (bool)Meeting.GetProperty("SavedFailed", Members)!.GetValue(instance)!;
            check(Failed() && Meeting.GetProperty("LastError", Members)!.GetValue(instance) == null, "Nonthrowing saved placement failure was invisible to retry status");
            check((string?)Meeting.GetProperty("CurrentRequest", Members)!.GetValue(instance) == episode,
                "Read-only status does not expose current accepted episode");
            episode = "irabeth.return.first/1";
            check(!Failed(), "Prior episode failure became a new episode retry");
            episode = null; check(!Failed(), "Withdrawn request still offers failure retry");
            episode = "irabeth.return.first/0";
            var reloaded = JsonConvert.DeserializeObject(JsonConvert.SerializeObject(data), dataType)!;
            Set(runtime, "m_Data", reloaded);
            check(Failed(), "Read-only failure status lost saved failed episode after JSON restoration");
            Set(reloaded, "Failed", false); check(!Failed(), "Deferred attempt was displayed as a failed retry");

            // Actual Tick must mark an existing fact dirty even though its callback now returns no request.
            Field(Meeting, "acceptedRequest").SetValue(instance, oldRequest);
            Main.GetField("enabled", Members)!.SetValue(null, false);
            system.ClearConditionsDirty();
            Meeting.GetMethod("Tick", Members)!.Invoke(instance, null);
            var tickError = Meeting.GetProperty("LastError", Members)!.GetValue(instance);
            check(system.ConditionsDirty || tickError is System.Security.SecurityException,
                "Disabled Tick neither requested native reevaluation nor reached the documented Unity loading boundary: " + tickError);
            if (!system.ConditionsDirty) Console.WriteLine("Irabeth meeting Tick boundary: native LoadingProcess.Instance requires Unity; withdrawal scheduling not executed headlessly.");
            system.ClearConditionsDirty(); game.IsUnloading = true;
            Meeting.GetMethod("Tick", Members)!.Invoke(instance, null);
            check(!system.ConditionsDirty, "Unload Tick mutated native condition state");
            game.IsUnloading = false;
            Set(game, "<LoadingSave>k__BackingField", FormatterServices.GetUninitializedObject(typeof(SaveInfo)));
            Meeting.GetMethod("Tick", Members)!.Invoke(instance, null);
            check(!system.ConditionsDirty, "Save-loading Tick mutated native condition state");
        }
        finally
        {
            Main.GetField("enabled", Members)!.SetValue(null, oldEnabled);
            Field(Meeting, "acceptedRequest").SetValue(instance, oldRequest);
            Field(typeof(Game), "s_Instance").SetValue(null, oldGame);
        }
    }
}
