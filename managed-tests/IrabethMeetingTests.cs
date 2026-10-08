using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using Kingmaker;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Area;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem;
using Newtonsoft.Json;

internal static class IrabethMeetingTests
{
    private const BindingFlags Members = BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;
    private static FieldInfo Field(Type type, string name)
    {
        for (Type? current = type; current != null; current = current.BaseType)
        {
            var field = current.GetField(name, Members | BindingFlags.DeclaredOnly);
            if (field != null) return field;
        }
        throw new Exception("Missing native fixture field: " + name);
    }
    private static void Set(object item, string name, object value) => Field(item.GetType(), name).SetValue(item, value);
    private static object Bare(Type type) => FormatterServices.GetUninitializedObject(type);
    private static T Reference<T>(SimpleBlueprint blueprint) where T : BlueprintReferenceBase, new()
    {
        var result = new T();
        Set(result, "deserializedGuid", blueprint.AssetGuid);
        Set(result, "<Cached>k__BackingField", blueprint);
        return result;
    }

    internal static void Run(Action<bool, string> check)
    {
        var service = typeof(Tirabade.Main).Assembly.GetType("Tirabade.IrabethMeeting", true)!;
        string Constant(string name) => (string)service.GetField(name, Members)!.GetRawConstantValue()!;
        var group = new BlueprintEtudeConflictingGroup { AssetGuid = BlueprintGuid.Parse(Constant("Group")) };
        var map = new Dictionary<string, SimpleBlueprint>();
        EntityReference Entity(string id)
        {
            var value = new EntityReference();
            value.UniqueId = id;
            value.SceneAssetGuid = Constant("SceneAsset");
            return value;
        }
        BlueprintEtude Blueprint(string id, int priority)
        {
            var value = new BlueprintEtude { AssetGuid = BlueprintGuid.Parse(id), name = "fixture_" + id, Priority = priority,
                ActivationCondition = new ConditionsChecker { Conditions = Array.Empty<Condition>() },
                CompletionCondition = new ConditionsChecker { Conditions = Array.Empty<Condition>() },
                ComponentsArray = Array.Empty<BlueprintComponent>() };
            Set(value, "m_ConflictingGroups", new List<BlueprintEtudeConflictingGroupReference> { Reference<BlueprintEtudeConflictingGroupReference>(group) });
            Set(value, "m_Parent", new BlueprintEtudeReference());
            map[id] = value;
            return value;
        }
        BlueprintEtude Background(string name, int priority, bool visible)
        {
            var value = Blueprint(Constant(name), priority);
            var unit = new UnitFromSpawner { Spawner = Entity(Constant("Spawner")) };
            var actions = new List<GameAction> { new HideUnit { Target = unit, Unhide = visible } };
            if (visible)
            {
                var move = new TranslocateUnit { Unit = unit,
                    translocatePositionEvaluator = new LocatorPosition { Locator = Entity(Constant("Locator")) },
                    translocateOrientationEvaluator = new LocatorOrientation { Locator = Entity(Constant("Locator")) } };
                Set(move, "m_CopyRotation", true);
                actions.Add(move);
            }
            value.ComponentsArray = new BlueprintComponent[] { new EtudePlayTrigger {
                Conditions = new ConditionsChecker { Conditions = Array.Empty<Condition>() },
                Actions = new ActionList { Actions = actions.ToArray() } } };
            return value;
        }
        var hidden = Background("Hidden", -100, false);
        var throne = Background("Throne", -50, true);
        var departure = Background("Departure", 99, false);
        var expedition = Blueprint(Constant("Expedition"), 400);
        Blueprint(Constant("Death"), 0);
        Blueprint(Constant("Gone"), 0);
        map[Constant("Group")] = group;
        map[Constant("Capital")] = new BlueprintArea { AssetGuid = BlueprintGuid.Parse(Constant("Capital")) };
        var meeting = Blueprint("67d14f48c926473dbf0389f6583209e8", 0);
        Func<string?> request = () => "fixture.request/0";
        var nativeBefore = throne.ComponentsArray[0];
        var instance = Activator.CreateInstance(service, Members, null,
            new object[] { meeting, request, new Func<string, SimpleBlueprint>(id => map[id]) }, null)!;
        check(meeting.Priority == 100 && meeting.ConflictingGroups.Single().Get() == group, "Meeting owns exactly the reviewed Irabeth group at 100.");
        check(meeting.Parent.IsEmpty() && !meeting.StartsParent && !meeting.CompletesParent, "Meeting cannot start or complete native parents.");
        check(meeting.LinkedAreaPart.AssetGuid.ToString() == Constant("Capital"), "Meeting links only the capital.");
        check(meeting.ComponentsArray.Length == 1 && meeting.ComponentsArray[0].GetType().Name == "Placement", "Production native bracket component is attached.");
        check(ReferenceEquals(nativeBefore, throne.ComponentsArray[0]) && throne.Priority == -50 && departure.Priority == 99, "Construction preserves native placement objects and priorities.");
        check(meeting.ActivationCondition.Conditions.Single().GetType().Name == "Eligibility", "Production eligibility condition is installed.");
        check(meeting.CompletionCondition.Conditions.Single().GetType().Name == "NeverComplete", "Temporary meeting has no completion condition with native effects.");
        var dataType = service.GetNestedType("MeetingData", Members)!;
        var data = Activator.CreateInstance(dataType)!;
        Set(data, "ActorId", "retained-actor-A");
        Set(data, "Placed", true);
        string serialized = JsonConvert.SerializeObject(data);
        var loaded = JsonConvert.DeserializeObject(serialized, dataType)!;
        check((string)Field(dataType, "ActorId").GetValue(loaded)! == "retained-actor-A", "Saved component data retains the actual actor identity.");
        check(!(bool)Field(dataType, "Placed").GetValue(loaded)!, "Arrival is not restored from serialized certainty.");
        var runtime = ((IRuntimeEntityFactComponentProvider)meeting.ComponentsArray[0]).CreateRuntimeFactComponent();
        runtime.Setup(meeting.ComponentsArray[0]);
        check(runtime.GetType().Name == "EtudeBracketRuntime", "Production component creates the native bracket runtime.");

        // Detached native facts isolate claim arbitration. No scene, view or player save is loaded.
        var system = (EtudesSystem)Bare(typeof(EtudesSystem));
        Set(system, "m_HeldConflictingGroups", new Dictionary<BlueprintEtudeConflictingGroup, BlueprintEtude>());
        var manager = new EntityFactsManager(system);
        Set(system, "Facts", manager);
        var tree = manager.EnsureFactProcessor<EtudesTree>();
        Set(system, "<Etudes>k__BackingField", tree);
        var rawFacts = (IList)Field(typeof(EntityFactsManager), "m_Facts").GetValue(manager)!;
        Etude Fact(BlueprintEtude bp)
        {
            var fact = (Etude)Bare(typeof(Etude));
            Set(fact, "<Blueprint>k__BackingField", bp);
            rawFacts.Add(fact);
            return fact;
        }
        var meetingFact = Fact(meeting);
        var departureFact = Fact(departure);
        var lower = Fact(Blueprint("866d1c41365f48ee8d74c0a6b552f18d", -10));
        var equal = Fact(Blueprint("21a04e38a5d645f4b2c7208e49b1e3c8", 100));
        var queen = Fact(expedition);
        var claims = service.GetMethod("ClaimsPermit", Members)!;
        var eligible = new HashSet<Etude>();
        bool Permitted() => (bool)claims.Invoke(null, new object[] { system, meeting, group, new Func<Etude, bool>(eligible.Contains) })!;
        // Register actual facts with the native processor; adding only manager storage is insufficient.
        check(tree.RawFacts.Count() > 0, "Native facts processor exposes fixture facts.");
        system.SetConflictingGroupTask(group, departureFact);
        check(Permitted(), "Reviewed ordinary departure permits a candidate request.");
        eligible.Add(lower);
        check(!Permitted(), "Pending lower-priority native event blocks meeting acquisition.");
        eligible.Clear(); eligible.Add(equal);
        check(!Permitted(), "Pending equal-priority native event blocks meeting acquisition.");
        eligible.Clear();
        system.SetConflictingGroupTask(group, lower);
        check(!Permitted(), "Unknown lower-priority holder is never background.");
        system.SetConflictingGroupTask(group, queen);
        check(!Permitted(), "Queen expedition remains a native location commitment.");
        system.SetConflictingGroupTask(group, meetingFact);
        eligible.Add(lower);
        check(!Permitted(), "Already-held meeting withdraws for a newly eligible low-priority event.");
        eligible.Clear();
        check(Permitted(), "Same meeting may become eligible again when the competing event no longer qualifies.");
        check(!meetingFact.IsCompleted && !departureFact.IsCompleted, "Policy never completes native or authored histories.");
        Lifecycle(check, system, manager, meetingFact, group, runtime);
        var parent = Fact(Blueprint("d9cd169eb75749f2929549c90d7f92bc", 0));
        var child = Fact(Blueprint("2dd3df2fb0d24e11922668685c571124", -10));
        Set(child.Blueprint, "m_Parent", Reference<BlueprintEtudeReference>(parent.Blueprint));
        child.ChangeParent(parent);
        var nativeEligible = service.GetMethod("ReadyUnderPlayingParents", Members)!;
        check(!(bool)nativeEligible.Invoke(null, new object?[] { child, null, null })!,
            "A pending child beneath a non-playing parent cannot block the meeting merely because predicates pass.");
    }

    private static void Lifecycle(Action<bool, string> check, EtudesSystem system, EntityFactsManager manager,
        Etude fact, BlueprintEtudeConflictingGroup group, EntityFactComponent runtime)
    {
        var gameField = Field(typeof(Game), "s_Instance");
        var loggerField = Field(typeof(Owlcat.Runtime.Core.Logging.Logger), "s_Instance");
        var rootReference = ResourcesLibrary.RootRef;
        var cachedRoot = Field(rootReference.GetType(), "<Cached>k__BackingField");
        var oldGame = gameField.GetValue(null);
        var oldLogger = loggerField.GetValue(null);
        var oldRoot = cachedRoot.GetValue(rootReference);
        try
        {
            var game = (Game)Bare(typeof(Game));
            var player = (Player)Bare(typeof(Player));
            var state = (PersistentState)Bare(typeof(PersistentState));
            Set(state, "PlayerState", player);
            Set(game, "State", state);
            Set(game, "TimeController", Bare(typeof(Kingmaker.Controllers.TimeController)));
            Set(player, "EtudesSystem", system);
            gameField.SetValue(null, game);
            var root = new Kingmaker.Blueprints.Root.BlueprintRoot();
            var calendar = (CalendarRoot)Bare(typeof(CalendarRoot));
            Set(calendar, "m_Initialized", true);
            Set(calendar, "m_StartDate", new DateTime(2020, 1, 1));
            root.Calendar = calendar;
            cachedRoot.SetValue(rootReference, root);
            var logger = new Owlcat.Runtime.Core.Logging.Logger { Enabled = true };
            loggerField.SetValue(null, logger);
            Set(system, "EtudeChangedEvent", Activator.CreateInstance(Field(typeof(EtudesSystem), "EtudeChangedEvent").FieldType)!);
            Set(fact, "<Manager>k__BackingField", manager);
            Set(fact, "Children", new List<Etude>());
            Set(runtime, "<Fact>k__BackingField", fact);
            Set(fact, "Components", new List<EntityFactComponent> { runtime });
            system.RemoveConflictingGroupTask(group, fact);
            fact.Activate();
            check(fact.IsPlaying && ReferenceEquals(system.GetConflictingGroupTask(group), fact.Blueprint),
                "Actual native activation acquires the meeting claim.");
            fact.Deactivate();
            check(!fact.IsPlaying && system.GetConflictingGroupTask(group) == null && !fact.IsCompleted,
                "Actual native deactivation releases the claim without completing history.");
            fact.Activate();
            check(fact.IsPlaying && ReferenceEquals(system.GetConflictingGroupTask(group), fact.Blueprint) && !fact.IsCompleted,
                "The same native fact reacquires through activation without historical completion.");
            fact.Deactivate();
            ParentScheduling(check, player);
            var messages = (IEnumerable<Owlcat.Runtime.Core.Logging.LogInfo>)Field(logger.GetType(), "m_RecentMessages").GetValue(logger)!;
            var failures = messages.Where(message => message.IsException).ToArray();
            foreach (var failure in failures) Console.WriteLine("NATIVE CALLBACK ERROR: " + failure.Message);
            check(failures.Length == 0, "Native activation/deactivation callbacks completed without swallowed exceptions.");
        }
        finally
        {
            cachedRoot.SetValue(rootReference, oldRoot);
            loggerField.SetValue(null, oldLogger);
            gameField.SetValue(null, oldGame);
        }
    }
    private static void ParentScheduling(Action<bool, string> check, Player player)
    {
        var service = typeof(Tirabade.Main).Assembly.GetType("Tirabade.IrabethMeeting", true)!;
        var readiness = service.GetMethod("ReadyUnderPlayingParents", Members)!;
        var claims = service.GetMethod("ClaimsPermit", Members)!;
        var oldSystem = player.EtudesSystem;
        try
        {
            foreach (var scenario in new[] { "parent-start", "parent-conflict", "parent-sync", "parent-same-group" })
            {
                var system = (EtudesSystem)Bare(typeof(EtudesSystem));
                Set(system, "m_HeldConflictingGroups", new Dictionary<BlueprintEtudeConflictingGroup, BlueprintEtude>());
                Set(system, "EtudeChangedEvent", Activator.CreateInstance(Field(typeof(EtudesSystem), "EtudeChangedEvent").FieldType)!);
                var manager = new EntityFactsManager(system);
                Set(system, "Facts", manager);
                var tree = manager.EnsureFactProcessor<EtudesTree>();
                Set(system, "<Etudes>k__BackingField", tree);
                Set(player, "EtudesSystem", system);
                Set(system, "m_IsUpdateForUnload", new Kingmaker.Utility.CountingGuard());
                Set(system, "m_AreaPartBeingLoaded", new BlueprintArea { AssetGuid = BlueprintGuid.Parse("a4ef01f3cbbf424489d148b31501e47a") });
                var group = new BlueprintEtudeConflictingGroup { AssetGuid = BlueprintGuid.Parse("997d865aa6f17cc48b480bd62ba02841") };
                var otherGroup = new BlueprintEtudeConflictingGroup { AssetGuid = BlueprintGuid.Parse("ef5e38a84537466da4e79369a1e7f963") };
                var roots = (List<Etude>)Field(typeof(EtudesTree), "m_Roots").GetValue(tree)!;
                var raw = (IList)Field(typeof(EntityFactsManager), "m_Facts").GetValue(manager)!;
                Etude Add(string id, BlueprintEtudeConflictingGroup? actorGroup, int priority, Etude? parent = null)
                {
                    var bp = new BlueprintEtude { AssetGuid = BlueprintGuid.Parse(id), name = scenario + "_" + id,
                        Priority = priority, ComponentsArray = Array.Empty<BlueprintComponent>(),
                        ActivationCondition = new ConditionsChecker { Conditions = Array.Empty<Condition>() },
                        CompletionCondition = new ConditionsChecker { Conditions = Array.Empty<Condition>() } };
                    Set(bp, "m_Parent", parent == null ? new BlueprintEtudeReference() : Reference<BlueprintEtudeReference>(parent.Blueprint));
                    Set(bp, "m_ConflictingGroups", actorGroup == null ? new List<BlueprintEtudeConflictingGroupReference>()
                        : new List<BlueprintEtudeConflictingGroupReference> { Reference<BlueprintEtudeConflictingGroupReference>(actorGroup) });
                    var fact = (Etude)Bare(typeof(Etude));
                    Set(fact, "<Blueprint>k__BackingField", bp);
                    Set(fact, "<Manager>k__BackingField", manager);
                    Set(fact, "Children", new List<Etude>());
                    Set(fact, "Components", new List<EntityFactComponent>());
                    fact.ChangeParent(parent!);
                    raw.Add(fact);
                    if (parent == null) roots.Add(fact); else parent.Children.Add(fact);
                    return fact;
                }
                bool Ready(Etude fact) => (bool)readiness.Invoke(null, new object?[] { fact, null, null })!;
                var meeting = Add("31b8ebef339d42b394f76581093fb9d5", group, 100);
                var parent = Add("5901b604251340c7835b26e9c73216bb", scenario == "parent-conflict" ? otherGroup : scenario == "parent-same-group" ? group : null, 0);
                var child = Add("5a566985223f4485ab2f3b271ea36728", group, -10, parent);
                bool Permitted() => (bool)claims.Invoke(null,
                    new object[] { system, meeting.Blueprint, group, new Func<Etude, bool>(Ready) })!;
                void MakeUnavailable(Etude fact)
                {
                    // A fixture-only native area gate represents withdrawal without patching a native method.
                    Set(fact.Blueprint, "m_IncludeAreaParts", false);
                    Set(fact.Blueprint, "m_LinkedAreaPart", Reference<BlueprintAreaPartReference>(
                        new BlueprintArea { AssetGuid = BlueprintGuid.Parse("52af90cf599a4e38863028a7f336592f") }));
                }
                meeting.Activate();
                if (scenario == "parent-start")
                {
                    check(!Ready(child) && Permitted(), "Inactive parent does not prematurely reserve Irabeth for its pending child.");
                    tree.SelectPlayingEtudes();
                    check(parent.IsPlaying && !child.IsPlaying && meeting.IsPlaying,
                        "Native selector starts the parent while the held meeting blocks the lower-priority child.");
                    check(Ready(child) && !Permitted(),
                        "Fresh production readiness and claim policy detect the child immediately after native parent activation.");
                    MakeUnavailable(meeting);
                    tree.SelectPlayingEtudes();
                    check(!meeting.IsPlaying && !meeting.IsCompleted,
                        "Native selector withdraws the fixture meeting through an unavailable condition without completing it.");
                    tree.SelectPlayingEtudes();
                    check(child.IsPlaying && ReferenceEquals(system.GetConflictingGroupTask(group), child.Blueprint),
                        "Native reselection grants the pending child its actual claim after meeting release.");
                    check(!parent.IsCompleted && !child.IsCompleted && !meeting.IsCompleted,
                        "Parent activation and meeting handover do not complete any history.");
                }
                else if (scenario == "parent-conflict")
                {
                    parent.Activate();
                    check(Ready(child) && !Permitted(), "A pending child under a playing parent blocks the meeting before conflict resolution.");
                    var replacement = Add("9a7e9cce82764fcd91d00cf4cf144b43", otherGroup, 10);
                    tree.SelectPlayingEtudes();
                    check(!parent.IsPlaying && replacement.IsPlaying && !child.IsPlaying,
                        "Actual native actor arbitration stops the parent when another event wins its separate group.");
                    check(!Ready(child) && Permitted(),
                        "Post-selector production policy does not let the now-unavailable child reserve Irabeth.");
                    check(!parent.IsCompleted && !child.IsCompleted,
                        "Losing a parent actor claim leaves parent and child histories uncompleted.");
                }
                else if (scenario == "parent-same-group")
                {
                    check(!Ready(child) && !Permitted(),
                        "An inactive parent that itself claims Irabeth independently blocks the meeting despite its unready child.");
                    MakeUnavailable(meeting);
                    tree.SelectPlayingEtudes();
                    tree.SelectPlayingEtudes();
                    check(parent.IsPlaying && ReferenceEquals(system.GetConflictingGroupTask(group), parent.Blueprint),
                        "Native reselection grants the ancestor's own Irabeth claim after meeting withdrawal.");
                    check(!meeting.IsCompleted && !parent.IsCompleted && !child.IsCompleted,
                        "Ancestor claim handover preserves every completion history.");
                }
                else
                {
                    var dependency = Add("6e40c11c2c024d50ba02159121498ab3", null, 0);
                    Set(parent.Blueprint, "m_Synchronized", new List<BlueprintEtudeReference> {
                        Reference<BlueprintEtudeReference>(dependency.Blueprint) });
                    dependency.Activate();
                    parent.Activate();
                    check(Ready(child) && !Permitted(), "Playing synchronized ancestry initially makes its pending child relevant.");
                    MakeUnavailable(dependency);
                    tree.SelectPlayingEtudes();
                    check(!dependency.IsPlaying && !parent.IsPlaying && !child.IsPlaying,
                        "Actual native synchronization stops the parent when its dependency becomes unavailable.");
                    check(!Ready(child) && Permitted(),
                        "Fresh production policy releases the pending child's reservation after synchronized parent stop.");
                    check(!dependency.IsCompleted && !parent.IsCompleted && !child.IsCompleted,
                        "Synchronization withdrawal changes no completion history.");
                }
                foreach (var fact in raw.Cast<Etude>().Where(item => item.IsPlaying).ToArray()) fact.Deactivate();
            }
        }
        finally { Set(player, "EtudesSystem", oldSystem); }
    }

}
