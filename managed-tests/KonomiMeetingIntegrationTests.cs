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

internal static class KonomiMeetingIntegrationTests
{
    private const BindingFlags Members = BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;
    private static readonly Type Main = typeof(Tirabade.Main);
    private static readonly Type Meeting = Main.Assembly.GetType("Tirabade.KonomiMeeting", true)!;
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
        foreach (bool visible in new[] { false, true })
        {
            var bp = Seed<BlueprintEtude>(Constant(visible ? "Office" : "Hidden"));
            if (bp.ComponentsArray.OfType<EtudePlayTrigger>().Any()) continue;
            bp.Priority = visible ? -20 : -100;
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
        var instance = Main.GetField("konomiMeeting", Members)!.GetValue(null)!;
        check(instance != null, "Actual Main.Build did not construct the personal meeting helper");
        var blueprint = (BlueprintEtude)Meeting.GetField("Blueprint", Members)!.GetValue(instance)!;
        var registered = (List<SimpleBlueprint>)Main.GetField("registered", Members)!.GetValue(null)!;
        check(registered.Contains(blueprint) && ReferenceEquals(ResourcesLibrary.TryGetBlueprint(blueprint.AssetGuid), blueprint),
            "Authored meeting is not registered before save restoration");
        check(blueprint.name == "RRT_etude.konomi.personal_return" && blueprint.Priority == -90, "Wrong authored meeting identity/priority");
        check(blueprint.ActivationCondition.Conditions.Single().Owner == blueprint
            && blueprint.CompletionCondition.Conditions.Single().Owner == blueprint,
            "Actual Main.Build omitted meeting condition owners");
        check(blueprint.ComponentsArray.Single().OwnerBlueprint == blueprint, "Actual OnEnable omitted placement component owner");
        var office = (BlueprintEtude)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(Constant("Office")));
        var nativeActions = office.ComponentsArray.OfType<EtudePlayTrigger>().Single().Actions.Actions;
        check(nativeActions.All(a => ReferenceEquals(a.Owner, office)), "Main initialization reparented native placement actions");
        var flags = (Dictionary<string, BlueprintUnlockableFlag>)Main.GetField("flags", Members)!.GetValue(null)!;
        string retryKey = (string)Main.GetField("KonomiMeetingRetry", Members)!.GetRawConstantValue()!;
        check(flags.TryGetValue(retryKey, out var retry) && registered.Contains(retry)
            && ReferenceEquals(ResourcesLibrary.TryGetBlueprint(retry.AssetGuid), retry), "Retry counter lacks native saved flag identity");

        var saved = new UnlockableFlagsManager();
        void Write(string key, int value) => saved.UnlockedFlags[flags[key]] = value;
        int Read(string key) => flags.TryGetValue(key, out var flag) ? saved.GetFlagValue(flag) : 0;
        var requestMethod = Main.GetMethod("KonomiVisitRequest", Members)!;
        string? Request(int hour) => (string?)requestMethod.Invoke(null, new object[] { new Func<string, int>(Read), hour });
        check(Request(112) == null, "Missing saved consent created a request");
        Write("konomi.retained_return_confirmed", 1); Write("hour.konomi.retained_return_confirmed", 101);
        check(Request(112) == null, "Recovery alone created visit consent");
        Write("konomi.return_meeting_accepted", 1);
        check(Request(111) == null && Request(112) == "konomi.return.first/0", "First request ignored exact 12-hour recovery boundary");
        string first = Request(112)!;
        check(Request(10000) == first && Request(112) == first, "Ordinary observation invents retry episodes");
        Write("konomi.closed", 1); Write("konomi.farewell", 1); Write("konomi.private_parted", 1);
        check(Request(112) == first, "Old romantic closure revoked separately accepted friendly aftercare");
        Write("konomi.return_visit_declined", 1);
        check(Request(112) == null, "Declined visit still authorized");
        Write("konomi.return_visit_declined", 0); Write("konomi.return_meeting_accepted", 0);
        check(Request(112) == null, "Removed acceptance still authorized");
        Write("konomi.return_meeting_accepted", 1); Write(retryKey, 1);
        check(Request(112) == "konomi.return.first/1", "Explicit saved retry did not create a distinct stable episode");
        Write(retryKey, -1); check(Request(112) == null, "Corrupt negative retry counter accepted");
        Write(retryKey, int.MaxValue); check(Request(112) == "konomi.return.first/2147483647", "Final representable episode cannot be observed");
        Write(retryKey, 1); Write("konomi.return_first_words", 1);
        check(Request(500) == null, "Completed first visit continued without followup invitation");
        Write("konomi.return_followup_invited", 1); Write("hour.konomi.return_followup_invited", 121);
        Write("konomi.return_meeting_accepted", 0);
        check(Request(167) == null && Request(168) == "konomi.return.followup/1", "Legacy first completion lost followup or bypassed 48-hour interval");
        Write("hour.konomi.return_followup_invited", 0); check(Request(168) == null, "Missing saved invitation time invented elapsed time");
        Write("hour.konomi.return_followup_invited", 121);
        Write("konomi.return_second_visit", 1); check(Request(500) == null, "Completed followup retained meeting authorization");
        Write("konomi.return_second_visit", 0);
        var serialized = JsonConvert.SerializeObject(saved.UnlockedFlags.ToDictionary(p => p.Key.AssetGuid.ToString(), p => p.Value));
        var copied = JsonConvert.DeserializeObject<Dictionary<string, int>>(serialized)!;
        var restored = new UnlockableFlagsManager();
        foreach (var pair in copied) restored.UnlockedFlags[(BlueprintUnlockableFlag)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(pair.Key))] = pair.Value;
        check(restored.GetFlagValue(retry!) == 1 && restored.GetFlagValue(flags["hour.konomi.return_followup_invited"]) == 121,
            "Stable registered flag identities did not retain retry/time values through serialized fixture reconstruction");

        var contact = Meeting.GetMethod("ContactPermitted", Members)!;
        int arrivalChecks = 0, contactChecks = 0;
        bool arrived = false, present = true;
        bool Contact(BlueprintEtude? holder) => (bool)contact.Invoke(null, new object?[] { holder, blueprint, office,
            new Func<bool>(() => { arrivalChecks++; return arrived; }), new Func<bool>(() => { contactChecks++; return present; }) })!;
        check(!Contact(blueprint) && arrivalChecks == 1 && contactChecks == 0, "Partial unhide bypassed required helper arrival");
        arrived = true; check(Contact(blueprint), "Verified temporary arrival rejected");
        int prior = arrivalChecks;
        check(Contact(office) && arrivalChecks == prior && contactChecks == 1, "Ordinary office contact unnecessarily requires temporary arrival");
        present = false; check(!Contact(office), "Office claim without actual contact accepted");
        present = true;
        check(!Contact(new BlueprintEtude { Priority = 0 }) && !Contact(new BlueprintEtude { Priority = -95 }) && !Contact(null),
            "Rank-up, unknown holder or absent claim bypassed physical contact policy");

        var oldEnabled = Main.GetField("enabled", Members)!.GetValue(null);
        var oldGame = Field(typeof(Game), "s_Instance").GetValue(null);
        var oldRequest = Field(Meeting, "acceptedRequest").GetValue(instance);
        try
        {
            Main.GetField("enabled", Members)!.SetValue(null, false);
            check(Main.GetMethod("CurrentKonomiVisit", Members)!.Invoke(null, null) == null, "Disabled addon still supplies consent to native activation");
            check(!(bool)Main.GetMethod("CanRetryKonomiVisit", Members)!.Invoke(null, null)!, "Disabled addon offers a retry");
            var game = (Game)FormatterServices.GetUninitializedObject(typeof(Game));
            var player = (Player)FormatterServices.GetUninitializedObject(typeof(Player));
            var state = (PersistentState)FormatterServices.GetUninitializedObject(typeof(PersistentState));
            Set(state, "PlayerState", player); Set(game, "State", state);
            Field(typeof(Game), "s_Instance").SetValue(null, game);
            Main.GetField("enabled", Members)!.SetValue(null, true);
            game.IsUnloading = true;
            check(Main.GetMethod("CurrentKonomiVisit", Members)!.Invoke(null, null) == null, "Unload supplied an active visit");
            Meeting.GetMethod("Tick", Members)!.Invoke(instance, null);
            check(Meeting.GetProperty("LastError", Members)!.GetValue(instance) == null, "Unload Tick touched incomplete native state");
            game.IsUnloading = false;
            Set(game, "<LoadingSave>k__BackingField", FormatterServices.GetUninitializedObject(typeof(Kingmaker.EntitySystem.Persistence.SaveInfo)));
            check(Main.GetMethod("CurrentKonomiVisit", Members)!.Invoke(null, null) == null, "Save restoration supplied an active visit");
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
            bool Window(string scene) => (bool)Main.GetMethod("KonomiVisitWindow", Members)!.Invoke(null, new object[] { scene })!;
            var dialogs = (Dictionary<string, BlueprintDialog>)Main.GetField("dialogs", Members)!.GetValue(null)!;
            Mode(GameModeType.Default);
            check(Window("konomi.return_first_words"), "Idle native context rejected accepted visit window");
            Mode(GameModeType.Dialog); controller.Dialog = dialogs["konomi.return_first_words"];
            check(Window("konomi.return_first_words") && !Window("konomi.return_second_visit"), "Exact own dialog exemption lost episode identity");
            controller.Dialog = new BlueprintDialog { name = dialogs["konomi.return_first_words"].name };
            check(!Window("konomi.return_first_words"), "An unrelated same-name dialog preserved the temporary claim");
            controller.Dialog = dialogs["konomi.return_second_visit"];
            check(Window("konomi.return_second_visit"), "Followup dialog withdrew its own actor");
            Set(player, "<IsInCombat>k__BackingField", true);
            check(!Window("konomi.return_second_visit"), "Combat retained a temporary meeting window");
            Set(player, "<IsInCombat>k__BackingField", false);
            Mode(GameModeType.Rest);
            check(!Window("konomi.return_second_visit"), "Another event mode preserved the temporary meeting");
            controller.Dialog = null; Mode(GameModeType.Default);
            player.Dialog.Scheduled = new StartDialogData();
            check(!Window("konomi.return_first_words"), "Scheduled native dialog did not defer personal visit");
            player.Dialog.Scheduled = null;

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
            Set(data, "Request", "konomi.return.first/0"); Set(data, "ActorId", "retained-actor"); Set(data, "Failed", true);
            Set(runtime, "m_Data", data);
            string? episode = "konomi.return.first/0";
            Field(Meeting, "acceptedRequest").SetValue(instance, new Func<string?>(() => episode));
            bool Failed() => (bool)Meeting.GetProperty("SavedFailed", Members)!.GetValue(instance)!;
            check(Failed() && Meeting.GetProperty("LastError", Members)!.GetValue(instance) == null, "Nonthrowing saved placement failure was invisible to retry status");
            check((string?)Meeting.GetProperty("CurrentRequest", Members)!.GetValue(instance) == episode,
                "Read-only status does not expose current accepted episode");
            episode = "konomi.return.followup/0";
            check(!Failed(), "Prior episode failure became a new episode retry");
            episode = null; check(!Failed(), "Withdrawn request still offers failure retry");
            episode = "konomi.return.first/0";
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
            if (!system.ConditionsDirty) Console.WriteLine("Konomi meeting Tick boundary: native LoadingProcess.Instance requires Unity; withdrawal scheduling not executed headlessly.");
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
