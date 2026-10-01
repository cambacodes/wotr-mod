using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Newtonsoft.Json.Linq;
using Tirabade;

// E18: the reviewed native gates match blueprints.zip, attach once to exactly the reviewed checkers, and read false only
// while the earned state holds (canon otherwise, including when the gate's relationship is degraded).
internal static class NativeGateManagedTests
{
    public static IEnumerable<string> NativeIds => NativeGate.Reviewed.Values;

    private static T Seed<T>(string guid) where T : SimpleBlueprint, new()
    {
        var id = BlueprintGuid.Parse(guid);
        if (ResourcesLibrary.TryGetBlueprint(id) is T prior) return prior;
        var blueprint = new T { AssetGuid = id, name = "NativeFixture_" + guid };
        ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(id, blueprint);
        return blueprint;
    }

    private static string Type(JToken token) => ((string)token["$type"]!).Split(new[] { ", " }, StringSplitOptions.None).Last();

    private static EntityReference Entity(JToken token) => new EntityReference
    {
        EntityNameInEditor = (string)token["EntityNameInEditor"]!, UniqueId = (string)token["_entity_id"]!, SceneAssetGuid = (string)token["SceneAssetGuid"]!
    };

    private static EtudeStatus Status(JToken token)
    {
        var status = new EtudeStatus { Not = (bool)token["Not"]!, NotStarted = (bool)token["NotStarted"]!, Started = (bool)token["Started"]!,
            Playing = (bool)token["Playing"]!, CompletionInProgress = (bool)token["CompletionInProgress"]!, Completed = (bool)token["Completed"]! };
        var reference = new BlueprintEtudeReference();
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!
            .SetValue(reference, BlueprintGuid.Parse(((string)token["m_Etude"]!).Replace("!bp_", "")));
        typeof(EtudeStatus).GetField("m_Etude", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!.SetValue(status, reference);
        return status;
    }

    // Archive-shaped fixtures: every EtudePlayTrigger of the etude with its spawn-related actions (Conditional, Spawn,
    // SpawnByUnitGroup); other native actions are not modeled. Asserts the archive still holds the reviewed shape.
    public static void Seed(Dictionary<string, JObject> native, Action<bool, string> check)
    {
        var data = native[NativeGate.SanctumEtude];
        check(Type(data) == "BlueprintEtude", "IvorySanctum_MainEtude is not a BlueprintEtude");
        GameAction? Map(JToken action)
        {
            switch (Type(action))
            {
                case "Spawn":
                    return new Spawn { Spawners = action["Spawners"]!.Select(Entity).ToArray(), ActionsOnSpawn = new ActionList { Actions = Array.Empty<GameAction>() } };
                case "SpawnByUnitGroup":
                    return new SpawnByUnitGroup { Group = Entity(action["m_Group"]!), ActionsOnSpawn = new ActionList { Actions = Array.Empty<GameAction>() } };
                case "Conditional":
                    var conditions = action["ConditionsChecker"]!["Conditions"]!.Select(c => Type(c) == "EtudeStatus" ? (Condition)Status(c) : null).ToArray();
                    if (conditions.Any(c => c == null)) return null;
                    return new Conditional
                    {
                        ConditionsChecker = new ConditionsChecker { Operation = (Operation)Enum.Parse(typeof(Operation), (string)action["ConditionsChecker"]!["Operation"]!), Conditions = conditions! },
                        IfTrue = new ActionList { Actions = action["IfTrue"]!["Actions"]!.Select(Map).Where(a => a != null).ToArray()! },
                        IfFalse = new ActionList { Actions = action["IfFalse"]!["Actions"]!.Select(Map).Where(a => a != null).ToArray()! }
                    };
                default: return null;
            }
        }
        var etude = Seed<BlueprintEtude>(NativeGate.SanctumEtude);
        var triggers = new List<BlueprintComponent>();
        foreach (var component in (JArray)data["Components"]!)
        {
            if (Type(component) != "EtudePlayTrigger") continue;
            var trigger = new EtudePlayTrigger { Actions = new ActionList { Actions = component["Actions"]!["Actions"]!.Select(Map).Where(a => a != null).ToArray()! },
                Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() } };
            trigger.name = (string)component["name"]!;
            triggers.Add(trigger);
        }
        etude.ComponentsArray = triggers.ToArray();
        var branches = triggers.OfType<EtudePlayTrigger>().SelectMany(t => t.Actions.Actions).OfType<Conditional>().Where(NativeGateIsSpawnBranch).ToArray();
        check(branches.Length == 2, "IvorySanctum_MainEtude no longer has exactly two RedDragon_CR20 spawn branches (" + branches.Length + ")");
        var cueData = native[NativeGate.GolemsCue];
        check(Type(cueData) == "BlueprintCue", "Golems_DragonEggs/Cue_0001 is not a BlueprintCue");
        var cue = Seed<BlueprintCue>(NativeGate.GolemsCue);
        cue.Conditions = new ConditionsChecker { Operation = (Operation)Enum.Parse(typeof(Operation), (string)cueData["Conditions"]!["Operation"]!),
            Conditions = cueData["Conditions"]!["Conditions"]!.Select(c => (Condition)Status(c)).ToArray() };
    }

    private static bool NativeGateIsSpawnBranch(Conditional conditional) => (bool)typeof(NativeGate)
        .GetMethod("IsSpawnBranch", BindingFlags.Static | BindingFlags.NonPublic)!.Invoke(null, new object[] { conditional })!;

    private static Func<bool> Holds(Condition condition) => (Func<bool>)typeof(NativeGate.Guard)
        .GetField("Holds", BindingFlags.Instance | BindingFlags.NonPublic)!.GetValue(condition)!;

    private static ConditionsChecker Original(Condition condition) => (ConditionsChecker)typeof(NativeGate.Guard)
        .GetField("Original", BindingFlags.Instance | BindingFlags.NonPublic)!.GetValue(condition)!;

    // After Main.Build: each reviewed checker carries one guard around the native checker, and the guard is false only
    // while the earned state holds.
    public static void Run(Story story, Action<bool, string> check)
    {
        var etude = (BlueprintEtude)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(NativeGate.SanctumEtude))!;
        var cue = (BlueprintCue)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(NativeGate.GolemsCue))!;
        var spawnBranches = etude.ComponentsArray.OfType<EtudePlayTrigger>().SelectMany(t => t.Actions.Actions).OfType<Conditional>()
            .Where(c => c.IfTrue.Actions.OfType<Spawn>().Any(s => s.Spawners.Any(e => e.UniqueId == NativeGate.DragonSpawner))).ToArray();
        bool gated = story.NativeGates.ContainsKey(NativeGate.SanctumSpawn);
        check(spawnBranches.Length == 2, "The dragon spawn branches changed shape");
        foreach (var branch in spawnBranches)
        {
            var guard = branch.ConditionsChecker.Conditions.SingleOrDefault() as NativeGate.Guard;
            check(gated == (guard != null), "RedDragon_CR20 spawn branch gate attachment does not match Story.NativeGates");
            if (guard == null) continue;
            check(ReferenceEquals(guard.Owner, etude) && etude.ElementsArray.Contains(guard), "Spawn gate is not owned by its etude");
            var original = Original(guard);
            check(original.Conditions.Length == 1 && original.Conditions[0] is EtudeStatus, "Spawn gate lost the native RedDragonDead condition");
            check(branch.IfTrue.Actions.Single() is Spawn && branch.IfFalse.Actions.Single() is SpawnByUnitGroup, "Spawn gate changed the native branches");
        }
        var cueGuard = cue.Conditions.Conditions.SingleOrDefault() as NativeGate.Guard;
        check(story.NativeGates.ContainsKey(NativeGate.GolemsOverBody) == (cueGuard != null), "Golem carcass cue gate attachment does not match Story.NativeGates");
        if (cueGuard != null)
            check(Original(cueGuard).Conditions.Single() is EtudeStatus status && status.Not && status.Started, "Golem cue gate lost its native condition");
        // Evaluation: a fixture checker whose native part is the empty AND (the host cannot run Owlcat's etude reporting).
        var fixture = new BlueprintCue { name = "NativeGateFixture" };
        var checker = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() };
        bool holds = false;
        NativeGate.Attach(fixture, checker, () => holds);
        NativeGate.Attach(fixture, checker, () => holds);
        check(checker.Conditions.Length == 1 && fixture.ElementsArray.OfType<NativeGate.Guard>().Count() == 1, "A second attach nests or duplicates the guard");
        check(checker.Conditions.All(c => c.Check()), "Without the earned state the native branch must play");
        holds = true;
        check(!checker.Conditions.All(c => c.Check()), "With the earned state the native branch must be gated off");
        NativeGate.Attach(fixture, checker, () => throw new InvalidOperationException("observation failure"));
        check(checker.Conditions.All(c => c.Check()), "An observation failure must fall back to canon");
        // Rules: a degraded relationship never gates, and the gate reads only its When groups.
        if (gated)
        {
            var spec = story.NativeGates[NativeGate.SanctumSpawn];
            var state = new Snapshot();
            check(!Rules.NativeGateHolds(story, NativeGate.SanctumSpawn, state), "The spawn gate holds in an empty world");
            foreach (var flag in spec.When[0]) state.Flags.Add(flag);
            check(Rules.NativeGateHolds(story, NativeGate.SanctumSpawn, state), "The spawn gate does not hold in its earned world");
            state.Flags.Add(Rules.DegradedPrefix + spec.Relationship);
            check(!Rules.NativeGateHolds(story, NativeGate.SanctumSpawn, state), "A degraded relationship still gates native content");
        }
        if (gated) check(Holds(spawnBranches[0].ConditionsChecker.Conditions[0]) != null, "Spawn gate has no observation");
        Console.WriteLine("PASS: E18 reviewed native gates match blueprints.zip, attach once, and fall back to canon unless earned.");
    }
}
