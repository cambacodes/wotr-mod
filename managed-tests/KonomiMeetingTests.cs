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

internal static class KonomiMeetingTests
{
    private const BindingFlags Members = BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic;
    private static FieldInfo Field(Type type, string name)
    {
        for (Type? current = type; current != null; current = current.BaseType)
        {
            var field = current.GetField(name, Members | BindingFlags.DeclaredOnly);
            if (field != null) return field;
        }
        throw new Exception("Missing fixture field: " + name);
    }
    private static void Set(object value, string name, object? data) => Field(value.GetType(), name).SetValue(value, data);
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
        var service = typeof(Tirabade.Main).Assembly.GetType("Tirabade.KonomiMeeting", true)!;
        string Constant(string name) => (string)service.GetField(name, Members)!.GetRawConstantValue()!;
        var group = new BlueprintEtudeConflictingGroup { AssetGuid = BlueprintGuid.Parse(Constant("Group")) };
        var map = new Dictionary<string, SimpleBlueprint> { [Constant("Group")] = group,
            [Constant("Capital")] = new BlueprintArea { AssetGuid = BlueprintGuid.Parse(Constant("Capital")) } };
        BlueprintEtude Blueprint(string id, int priority)
        {
            var bp = new BlueprintEtude { AssetGuid = BlueprintGuid.Parse(id), name = "fixture_" + id, Priority = priority,
                ActivationCondition = new ConditionsChecker { Conditions = Array.Empty<Condition>() },
                CompletionCondition = new ConditionsChecker { Conditions = Array.Empty<Condition>() },
                ComponentsArray = Array.Empty<BlueprintComponent>() };
            Set(bp, "m_Parent", new BlueprintEtudeReference());
            Set(bp, "m_ConflictingGroups", new List<BlueprintEtudeConflictingGroupReference> { Reference<BlueprintEtudeConflictingGroupReference>(group) });
            map[id] = bp;
            return bp;
        }
        EntityReference Entity(string id) => new EntityReference { UniqueId = id, SceneAssetGuid = Constant("SceneAsset") };
        BlueprintEtude Placement(string name, int priority, bool visible)
        {
            var bp = Blueprint(Constant(name), priority);
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
            bp.ComponentsArray = new BlueprintComponent[] { new EtudePlayTrigger {
                Conditions = new ConditionsChecker { Conditions = Array.Empty<Condition>() },
                Actions = new ActionList { Actions = actions.ToArray() } } };
            return bp;
        }
        var hidden = Placement("Hidden", -100, false);
        var office = Placement("Office", -20, true);
        var nativeActions = ((EtudePlayTrigger)office.ComponentsArray[0]).Actions.Actions;
        var meeting = Blueprint("18e6d3ec663b4f2e88a1eb14db892cba", 0);
        string? request = null;
        bool badConsent = false;
        var instance = Activator.CreateInstance(service, Members, null,
            new object[] { meeting, new Func<string?>(() => badConsent ? throw new InvalidOperationException("Unavailable consent observation") : request), new Func<string, SimpleBlueprint>(id => map[id]) }, null)!;
        check(meeting.Priority == -90 && meeting.ConflictingGroups.Single().Get() == group, "Meeting must own only Konomi actor group at -90");
        check(meeting.Parent.IsEmpty() && !meeting.StartsParent && !meeting.CompletesParent, "Meeting cannot rewrite native parent history");
        check(meeting.LinkedAreaPart.AssetGuid.ToString() == Constant("Capital"), "Meeting must link capital");
        check(ReferenceEquals(nativeActions, ((EtudePlayTrigger)office.ComponentsArray[0]).Actions.Actions)
            && office.Priority == -20 && hidden.Priority == -100, "Construction changed native placement");
        check(meeting.ComponentsArray.Single().GetType().Name == "Placement", "Native bracket placement missing");
        check(meeting.ActivationCondition.Conditions.Single().GetType().Name == "Eligibility"
            && !meeting.CompletionCondition.Conditions.Single().Check(), "Authored lifecycle guards missing");
        check(!(bool)service.GetMethod("Eligible", Members)!.Invoke(instance, null)!, "No accepted request became eligible");
        var dataType = service.GetNestedType("MeetingData", Members)!;
        var data = Activator.CreateInstance(dataType)!;
        Set(data, "ActorId", "original-actor");
        Set(data, "Request", "first-visit");
        Set(data, "Placed", true);
        var permits = service.GetMethod("RequestAllows", Members)!;
        bool RequestAllows(string? current, string actor = "original-actor")
            => (bool)permits.Invoke(null, new object?[] { data, current, actor })!;
        check(RequestAllows("first-visit"), "Valid accepted request rejected");
        check(!RequestAllows(null), "Withdrawn consent remains authorized");
        check(!RequestAllows("first-visit", "different-actor"), "Request transferred to another actor");
        check(!(bool)service.GetMethod("Place", Members)!.Invoke(instance, new[] { data })!
            && !(bool)Field(dataType, "Failed").GetValue(data)!, "Normal deferred placement became permanent failure");
        check(RequestAllows("first-visit"), "Deferred request cannot resume without replaying invitation");
        badConsent = true;
        check(!(bool)service.GetMethod("Eligible", Members)!.Invoke(instance, null)!
            && service.GetProperty("LastError", Members)!.GetValue(instance) is InvalidOperationException,
            "Failed consent observation granted eligibility or lost diagnostics");
        badConsent = false;
        var attempt = service.GetMethod("AttemptPlacement", Members)!;
        bool Attempt(Func<bool> action) => (bool)attempt.Invoke(null, new object[] { data, action })!;
        check(!Attempt(() => false) && !RequestAllows("first-visit"),
            "Nonthrowing post-unhide failure must block automatic same-episode replay");
        check(RequestAllows("explicit-retry"), "Partial mutation failure lost explicit retry path");
        check(Attempt(() => RequestAllows("first-visit")) && RequestAllows("first-visit"),
            "Successful retry self-invalidated during its own arrival checks");
        try { Attempt(() => throw new InvalidOperationException("Native mutation failed")); check(false, "Mutation exception disappeared"); }
        catch (TargetInvocationException ex) { check(ex.InnerException is InvalidOperationException && !RequestAllows("first-visit"),
            "Throwing partial mutation failed to retain retry protection"); }
        Set(data, "Failed", true);
        check(!RequestAllows("first-visit"), "Failed partial placement replays the same request");
        check(RequestAllows("explicit-retry") && RequestAllows("second-visit"), "New authorized episode cannot recover failed placement");
        string json = JsonConvert.SerializeObject(data);
        var restored = JsonConvert.DeserializeObject(json, dataType)!;
        check((string)Field(dataType, "ActorId").GetValue(restored)! == "original-actor"
            && (string)Field(dataType, "Request").GetValue(restored)! == "first-visit"
            && (bool)Field(dataType, "Failed").GetValue(restored)!, "Saved failure and identity checkpoint lost");
        check(!(bool)Field(dataType, "Placed").GetValue(restored)!, "Save/load trusted stale arrival proof");
        var validate = service.GetMethod("ValidatePlacement", Members)!;
        var target = ((UnitFromSpawner)((HideUnit)nativeActions[0]).Target).Spawner;
        target.SceneAssetGuid = "wrong-scene";
        try { validate.Invoke(null, new object[] { office, Constant("Office"), -20, true }); check(false, "Wrong native scene accepted"); }
        catch (TargetInvocationException ex) { check(ex.InnerException is InvalidOperationException, "Wrong scene did not fail closed"); }
        target.SceneAssetGuid = Constant("SceneAsset");
        var runtime = ((IRuntimeEntityFactComponentProvider)meeting.ComponentsArray.Single()).CreateRuntimeFactComponent();
        runtime.Setup(meeting.ComponentsArray.Single());
        check(runtime.GetType().Name == "EtudeBracketRuntime", "Production component did not create native bracket runtime");
        var system = (EtudesSystem)Bare(typeof(EtudesSystem));
        Set(system, "m_HeldConflictingGroups", new Dictionary<BlueprintEtudeConflictingGroup, BlueprintEtude>());
        var manager = new EntityFactsManager(system);
        Set(system, "Facts", manager);
        var tree = manager.EnsureFactProcessor<EtudesTree>();
        Set(system, "<Etudes>k__BackingField", tree);
        var raw = (IList)Field(typeof(EntityFactsManager), "m_Facts").GetValue(manager)!;
        Etude Fact(BlueprintEtude bp)
        {
            var fact = (Etude)Bare(typeof(Etude));
            Set(fact, "<Blueprint>k__BackingField", bp);
            raw.Add(fact);
            return fact;
        }
        var meetingFact = Fact(meeting);
        var fallbackFact = Fact(hidden);
        var officeFact = Fact(office);
        var rank = Fact(Blueprint("e513ab6862e999644acde5a994911f5a", 0));
        var unknown = Fact(Blueprint("ae71e805e19445b39c755f8702b173a6", -95));
        var eligible = new HashSet<Etude>();
        var claims = service.GetMethod("ClaimsPermit", Members)!;
        bool Permitted() => (bool)claims.Invoke(null, new object[] { system, meeting, hidden, group, new Func<Etude, bool>(eligible.Contains) })!;
        system.SetConflictingGroupTask(group, fallbackFact);
        check(Permitted(), "Audited fallback disallows personal meeting");
        system.SetConflictingGroupTask(group, officeFact);
        check(!Permitted(), "Meeting steals active native office");
        system.SetConflictingGroupTask(group, rank);
        check(!Permitted(), "Meeting steals native rank-up");
        system.SetConflictingGroupTask(group, unknown);
        check(!Permitted(), "Unknown lower-priority holder treated as fallback");
        system.SetConflictingGroupTask(group, meetingFact);
        eligible.Add(rank);
        check(!Permitted(), "Already-held meeting does not yield to eligible rank-up");
        eligible.Clear(); eligible.Add(unknown);
        check(!Permitted(), "Pending unknown lower event starved");
        eligible.Clear();
        check(Permitted() && RequestAllows("second-visit"), "Native preemption cannot resume under retained consent");
        check(!officeFact.IsCompleted && !fallbackFact.IsCompleted && !rank.IsCompleted, "Policy completed native history");
        Lifecycle(check, system, manager, meetingFact, group, runtime);
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
            var tree = system.Etudes;
            var starts = (HashSet<Etude>)Field(typeof(EtudesTree), "m_StartingSet").GetValue(tree)!;
            var stops = (HashSet<Etude>)Field(typeof(EtudesTree), "m_StoppingSet").GetValue(tree)!;
            var filter = typeof(EtudesTree).GetMethod("FilterOnActors", Members)!;
            var fallback = tree.RawFacts.Single(item => item.Blueprint.Priority == -100);
            var officer = tree.RawFacts.Single(item => item.Blueprint.Priority == -20);
            var rank = tree.RawFacts.Single(item => item.Blueprint.AssetGuid.ToString() == "e513ab6862e999644acde5a994911f5a");
            void Prepare(Etude held, params Etude[] pending)
            {
                starts.Clear(); stops.Clear(); system.SetConflictingGroupTask(group, held);
                foreach (var candidate in pending) starts.Add(candidate);
            }
            Prepare(fallback, fact); filter.Invoke(tree, null);
            check(starts.Contains(fact) && stops.Contains(fallback), "Actual selector does not select meeting over fallback");
            Prepare(officer, fact); filter.Invoke(tree, null);
            check(!starts.Contains(fact) && !stops.Contains(officer), "Actual selector lets meeting override office");
            Prepare(fact, rank); filter.Invoke(tree, null);
            check(starts.Contains(rank) && stops.Contains(fact), "Actual eligible rank-up cannot preempt held meeting");
            tree.RemoveFromPlaying(fact); starts.Clear(); stops.Clear(); starts.Add(fallback); filter.Invoke(tree, null);
            check(starts.Contains(fallback) && !fallback.IsCompleted, "Native fallback cannot resume after claim release");
            Prepare(officer); tree.RemoveFromPlaying(fact);
            check(ReferenceEquals(system.GetConflictingGroupTask(group), officer.Blueprint), "Stale release removed new native owner");
            // Exercise the exact shared parent-readiness helper used by Konomi eligibility.
            var parentBlueprint = new BlueprintEtude { AssetGuid = BlueprintGuid.Parse("fbca0c5fe2cb4f528708554c681890e2"),
                ActivationCondition = new ConditionsChecker { Conditions = Array.Empty<Condition>() },
                ComponentsArray = Array.Empty<BlueprintComponent>() };
            Set(parentBlueprint, "m_Parent", new BlueprintEtudeReference());
            Set(parentBlueprint, "m_ConflictingGroups", new List<BlueprintEtudeConflictingGroupReference>());
            var parent = (Etude)Bare(typeof(Etude));
            Set(parent, "<Blueprint>k__BackingField", parentBlueprint);
            Set(parent, "<Manager>k__BackingField", manager);
            Set(parent, "Children", new List<Etude>());
            Set(parent, "Components", new List<EntityFactComponent>());
            var childBlueprint = new BlueprintEtude { AssetGuid = BlueprintGuid.Parse("5839ca670b5f4e65acf18fd408796f44"),
                ActivationCondition = new ConditionsChecker { Conditions = Array.Empty<Condition>() } };
            Set(childBlueprint, "m_Parent", Reference<BlueprintEtudeReference>(parentBlueprint));
            var child = (Etude)Bare(typeof(Etude));
            Set(child, "<Blueprint>k__BackingField", childBlueprint);
            child.ChangeParent(parent);
            var readiness = typeof(Tirabade.Main).Assembly.GetType("Tirabade.IrabethMeeting", true)!
                .GetMethod("ReadyUnderPlayingParents", Members)!;
            bool Ready() => (bool)readiness.Invoke(null, new object?[] { child, null, null })!;
            check(!Ready(), "Non-playing parent made its child eligible");
            parent.Activate();
            check(Ready(), "Playing parent did not enable otherwise eligible native child");
            parent.Deactivate();
            check(!Ready() && !parent.IsCompleted, "Parent withdrawal did not defer child without history completion");
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
}
