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
    public static IEnumerable<string> NativeIds => NativeGate.Reviewed.Values.Concat(Rules.ReviewedNativeObjectives.Values);

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
        // Engine queue 8a: VendorArsinoe/Answer_0025 as the archive has it (two QuestStatus, one EtudeStatus; NextCue Cue_0026).
        var answerData = native[NativeGate.ArsinoeAnswer];
        check(Type(answerData) == "BlueprintAnswer", "VendorArsinoe/Answer_0025 is not a BlueprintAnswer");
        var answer = Seed<BlueprintAnswer>(NativeGate.ArsinoeAnswer);
        answer.ShowConditions = new ConditionsChecker { Operation = (Operation)Enum.Parse(typeof(Operation), (string)answerData["ShowConditions"]!["Operation"]!),
            Conditions = answerData["ShowConditions"]!["Conditions"]!.Select(c => Type(c) == "QuestStatus" ? (Condition)Quest(c) : Status(c)).ToArray() };
        answer.NextCue = new Kingmaker.DialogSystem.CueSelection { Cues = ((JArray)answerData["NextCue"]!["Cues"]!)
            .Select(v => CueRef(((string)v!).Replace("!bp_", ""))).ToList() };
        answer.OnSelect = new ActionList { Actions = Array.Empty<GameAction>() };
        // Engine queue 9c: DragonEggs_Dialogue's own condition as the archive has it (FlagUnlocked EnableEggDialog).
        string dialogId = Rules.ReviewedNativeGates[NativeGate.DragonEggsDialog];
        var dialogData = native[dialogId];
        check(Type(dialogData) == "BlueprintDialog", "DragonEggs_Dialogue is not a BlueprintDialog");
        var dialog = Seed<BlueprintDialog>(dialogId);
        dialog.Conditions = new ConditionsChecker { Operation = (Operation)Enum.Parse(typeof(Operation), (string)dialogData["Conditions"]!["Operation"]!),
            Conditions = dialogData["Conditions"]!["Conditions"]!.Select(c => (Condition)Flag(c, check)).ToArray() };
        // E19: the reviewed objectives load as the game loads them.
        foreach (string objective in Rules.ReviewedNativeObjectives.Values)
        {
            check(Type(native[objective]) == "BlueprintQuestObjective", "Reviewed settlement target is not a BlueprintQuestObjective: " + objective);
            Seed<Kingmaker.Blueprints.Quests.BlueprintQuestObjective>(objective);
        }
    }

    private static FlagUnlocked Flag(JToken token, Action<bool, string> check)
    {
        check(Type(token) == "FlagUnlocked", "DragonEggs_Dialogue condition is not FlagUnlocked");
        var flag = new FlagUnlocked { Not = (bool)token["Not"]!, ExceptSpecifiedValues = (bool)token["ExceptSpecifiedValues"]! };
        var reference = new BlueprintUnlockableFlagReference();
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!
            .SetValue(reference, BlueprintGuid.Parse(((string)token["m_ConditionFlag"]!).Replace("!bp_", "")));
        typeof(FlagUnlocked).GetField("m_ConditionFlag", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!.SetValue(flag, reference);
        return flag;
    }

    // After Main.Build (engine queue 9b/9c): the egg dialog carries one guard around FlagUnlocked, warning-only, and both the gate and
    // the Obj5A settlement hold only after her return (clutch collected) / in the flight world past the egg chamber, on the Trickster path.
    public static void RunDevarra(Story story, Action<bool, string> check)
    {
        var dialog = (BlueprintDialog)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(Rules.ReviewedNativeGates[NativeGate.DragonEggsDialog]))!;
        var guard = dialog.Conditions.Conditions.Length == 1 ? dialog.Conditions.Conditions[0] as NativeGate.Guard : null;
        check(story.NativeGates.ContainsKey(NativeGate.DragonEggsDialog) == (guard != null), "The egg dialog gate attachment does not match Story.NativeGates.");
        if (guard != null)
            check(Original(guard).Conditions.Single() is FlagUnlocked flag && !flag.Not && ReferenceEquals(guard.Owner, dialog),
                "The egg dialog gate lost FlagUnlocked EnableEggDialog or is not owned by the dialog.");
        check(Rules.WarningOnlyNativeGates.Contains(NativeGate.DragonEggsDialog), "The egg dialog gate would degrade Devarra on refusal.");
        // Drift: an extra condition is refused.
        var drifted = new BlueprintDialog { AssetGuid = dialog.AssetGuid, name = "EggDialogDrift" };
        drifted.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = new Condition[] { new FlagUnlocked { Not = true }, new FlagUnlocked() } };
        check(NativeGate.Check(NativeGate.DragonEggsDialog, story.NativeGates[NativeGate.DragonEggsDialog], g => drifted, out _, out _) != null,
            "A drifted egg dialog condition is accepted.");
        const string T = "devarra.trickster.";
        foreach (var (what, flags, gated, settled) in new (string, string[], bool, bool)[]
        {
            ("flight, before the chamber", new[] { "trickster.ever", T + "flight.pact", "devarra.escaped" }, false, false),
            ("flight, golems met", new[] { "trickster.ever", T + "flight.pact", "devarra.escaped", "devarra.golems_met.latched" }, false, true),
            ("flight, clutch collected", new[] { "trickster.ever", T + "flight.pact", "devarra.escaped", "devarra.golems_met.latched", T + "clutch_collected" }, true, true),
            ("killed in the lair", new[] { "trickster.ever", "devarra.golems_met.latched" }, false, false),
            ("off the Trickster path", new[] { T + "flight.pact", "devarra.escaped", "devarra.golems_met.latched", T + "clutch_collected" }, false, false),
            ("collected, degraded", new[] { "trickster.ever", T + "flight.pact", "devarra.escaped", "devarra.golems_met.latched", T + "clutch_collected",
                Rules.DegradedPrefix + "devarra" }, false, false),
        })
        {
            var state = new Snapshot { Chapter = 3 };
            state.Flags.UnionWith(flags);
            Rules.Complete(story, state);
            check(Rules.NativeGateHolds(story, NativeGate.DragonEggsDialog, state) == gated, "Egg dialog gate, " + what);
            check(Rules.NativeObjectiveSettles(story, "greybor.dragon_hunt.sanctum", state) == settled, "Obj5A settlement, " + what);
        }
        Console.WriteLine("PASS: E18 egg dialog shut after Devarra takes her clutch; E19 Greybor's Obj5A failed in the flight world (Trickster only).");
    }

    private static QuestStatus Quest(JToken token)
    {
        var status = new QuestStatus { Not = (bool)token["Not"]!,
            State = (Kingmaker.AreaLogic.QuestSystem.QuestState)Enum.Parse(typeof(Kingmaker.AreaLogic.QuestSystem.QuestState), (string)token["State"]!) };
        var reference = new BlueprintQuestReference();
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!
            .SetValue(reference, BlueprintGuid.Parse(((string)token["m_Quest"]!).Replace("!bp_", "")));
        typeof(QuestStatus).GetField("m_Quest", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!.SetValue(status, reference);
        return status;
    }

    private static BlueprintCueBaseReference CueRef(string guid)
    {
        var reference = new BlueprintCueBaseReference();
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!
            .SetValue(reference, BlueprintGuid.Parse(guid));
        return reference;
    }

    // Engine queue 8a: after Build, Arsinoe's "any news" answer is gated exactly while the guests were ransomed or bought back.
    public static void RunArsinoe(Story story, Action<bool, string> check)
    {
        var answer = (BlueprintAnswer)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(NativeGate.ArsinoeAnswer))!;
        var guard = answer.ShowConditions.Conditions.Length == 1 ? answer.ShowConditions.Conditions[0] as NativeGate.Guard : null;
        check(story.NativeGates.ContainsKey(NativeGate.ArsinoeSouls) == (guard != null), "Arsinoe's answer gate attachment does not match Story.NativeGates.");
        if (guard == null) return;
        check(Original(guard).Conditions.Length == 3 && Original(guard).Conditions.Take(2).All(c => c is QuestStatus), "The Arsinoe gate lost the native conditions.");
        check(Rules.WarningOnlyNativeGates.Contains(NativeGate.ArsinoeSouls), "The Arsinoe gate would degrade Kiana on refusal.");
        foreach (var (what, flags, gated) in new (string, string[], bool)[]
        {
            ("nothing done", new[] { "trickster" }, false),
            ("ransomed", new[] { "trickster", "kiana.trickster.guests_ransomed" }, true),
            ("bought back", new[] { "trickster", "kiana.trickster.guests_bought_back" }, true),
            ("former Trickster", new[] { "trickster.ever", "kiana.trickster.guests_ransomed" }, false),
            ("ransomed, degraded", new[] { "trickster", "kiana.trickster.guests_ransomed", Rules.DegradedPrefix + "kiana" }, false),
        })
        {
            var state = new Snapshot { Chapter = 4 };
            state.Flags.UnionWith(flags);
            Rules.Complete(story, state);
            check(Rules.NativeGateHolds(story, NativeGate.ArsinoeSouls, state) == gated, "Arsinoe gate, " + what);
        }
        Console.WriteLine("PASS: E18 Arsinoe's 'any news' answer (VendorArsinoe/Answer_0025) gated after a ransom or buy-back.");
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
