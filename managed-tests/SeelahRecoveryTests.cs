using System;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using Kingmaker.Blueprints;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic;
using Kingmaker.UnitLogic.Parts;
using Newtonsoft.Json.Linq;
using Tirabade;

// Seelah_FinallyDead_ReviveAvailable (Writer/handoffs/trickster/seelah.md, SEE-01): the Trickster pickpocket Requires
// seelah.finally_dead, a Derived key over the runtime revive.seelah.available that Main.BuildState adds when
// Fate.CanRevive(Seelah_Companion) holds. This checks that chain on a fixture of the exact state the game is in:
// her companion unit held in the cross-scene state, roster InParty (the native SeelahNotInParty_Dead is
// CompanionInParty with MatchWhenDead only), and finally dead.
internal static class SeelahRecoveryTests
{
    private const string Companion = "54be53f0b35bf3c4592a97ae335fe765";
    private const string DeadEtude = "26ae0f50130942b4bb8dfe658e77b1c6";

    internal static void Run(Story story, JObject deadEtude, Action<bool, string> check)
    {
        const BindingFlags instance = BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance;
        const BindingFlags statics = BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static;
        void Set(object value, Type type, string field, object data) => type.GetField(field, instance)!.SetValue(value, data);
        var fate = typeof(Main).Assembly.GetType("Tirabade.Fate", true)!;
        bool Retained(bool faction, bool crossScene, CompanionState? state)
            => (bool)fate.GetMethod("IsRetained", statics)!.Invoke(null, new object?[] { faction, crossScene, state })!;
        RecoveryStatus Status(UnitEntityData unit, CompanionState state)
            => (RecoveryStatus)fate.GetMethod("Status", statics)!.Invoke(null, new object[] { unit, state })!;

        // The native etude that the pickpocket's death detect reads: active only while her companion is in the party and dead.
        var condition = (JArray)deadEtude["ActivationCondition"]!["Conditions"]!;
        var inParty = condition.Single();
        check(((string)inParty["$type"]!).EndsWith(", CompanionInParty", StringComparison.Ordinal)
              && (string)inParty["m_companion"]! == "!bp_" + Companion && (bool)inParty["MatchWhenDead"]!
              && !(bool)inParty["MatchWhenActive"]! && !(bool)inParty["MatchWhenRemote"]! && !(bool)inParty["MatchWhenDetached"]!
              && !(bool)inParty["MatchWhenEx"]! && !(bool)inParty["Not"]!,
            "SeelahNotInParty_Dead is no longer 'her companion unit, in the party, dead'.");

        // A companion who dies in the party keeps roster InParty in the cross-scene state: retained.
        check(Retained(true, true, CompanionState.InParty), "An in-party dead companion is not retained.");
        check(Retained(true, true, CompanionState.Remote), "A remote companion is not retained.");
        check(!Retained(true, true, CompanionState.None) && !Retained(true, true, CompanionState.ExCompanion)
              && !Retained(true, true, CompanionState.InPartyDetached)
              && !Retained(false, true, CompanionState.InParty) && !Retained(true, false, CompanionState.InParty),
            "A dismissed, departed, hostile or scene-bound unit became a recoverable Seelah.");

        // Her finally-dead unit reads as a recoverable death; a living one does not.
        UnitEntityData Unit(UnitLifeState life, bool finallyDead)
        {
            var unit = (UnitEntityData)FormatterServices.GetUninitializedObject(typeof(UnitEntityData));
            var descriptor = (UnitDescriptor)FormatterServices.GetUninitializedObject(typeof(UnitDescriptor));
            var state = (UnitState)FormatterServices.GetUninitializedObject(typeof(UnitState));
            Set(unit, typeof(EntityDataBase), "<UniqueId>k__BackingField", "seelah-fixture");
            Set(unit, typeof(UnitEntityData), "<Descriptor>k__BackingField", descriptor);
            Set(descriptor, typeof(UnitDescriptor), "<Unit>k__BackingField", unit);
            Set(descriptor, typeof(UnitDescriptor), "<Blueprint>k__BackingField", new BlueprintUnit { AssetGuid = BlueprintGuid.Parse(Companion) });
            Set(descriptor, typeof(UnitDescriptor), "State", state);
            Set(state, typeof(UnitState), "<LifeState>k__BackingField", life);
            Set(state, typeof(UnitState), "<IsFinallyDead>k__BackingField", finallyDead);
            return unit;
        }
        var dead = Status(Unit(UnitLifeState.Dead, true), CompanionState.InParty);
        check(dead.Eligible && dead.Dead && !dead.Conscious && dead.Roster == (int)CompanionState.InParty,
            "A finally-dead retained Seelah does not read as a recoverable death.");
        var alive = Status(Unit(UnitLifeState.Conscious, false), CompanionState.InParty);
        check(!alive.Dead && alive.Conscious, "A living Seelah reads as recoverable.");

        // The story side: the revival binds her companion unit to seelah_dead, and the pickpocket reaches it through
        // revive.seelah.available -> seelah.finally_dead with a terminal revive choice.
        check(story.Revivals.TryGetValue("seelah", out var revival) && revival.Unit == Companion && revival.DeathFlag == "seelah_dead"
              && story.Etudes["seelah_dead"] == DeadEtude, "Seelah's revival binding changed.");
        var pick = story.Scenes.Single(s => s.Id == "seelah.trickster.dead.pickpocket");
        check(pick.Recovery == "seelah" && pick.Requires.Contains("seelah.finally_dead")
              && story.Derived["seelah.finally_dead"].Length == 1 && story.Derived["seelah.finally_dead"][0].SequenceEqual(new[] { "revive.seelah.available" })
              && pick.Nodes.SelectMany(n => n.Choices).Count(c => c.Revive == "seelah" && c.Next == null) == 2,
            "The pickpocket no longer reaches the retained revive.");
        Snapshot World(bool retainedDead)
        {
            var world = new Snapshot { Chapter = 3, Area = pick.Areas[0], Hour = 5000 };
            world.Flags.UnionWith(new[] { "trickster", "trickster.was", "seelah_dead", "seelah.diamond_held" });
            if (retainedDead) world.Flags.Add("revive.seelah.available");   // Main.BuildState: Fate.CanRevive(Seelah_Companion)
            Rules.Complete(story, world);
            foreach (var latch in story.Latches.Keys.Where(world.Has)) world.Times[latch] = world.Hour - 48;
            return world;
        }
        var retained = World(true);
        check(retained.Has("seelah.finally_dead") && Rules.Available(story, pick, retained),
            "Seelah_FinallyDead_ReviveAvailable: the runtime key does not open the pickpocket.");
        var lost = World(false);
        check(!lost.Has("seelah.finally_dead") && !Rules.Available(story, pick, lost),
            "The pickpocket opens without a retained dead unit.");
    }
}
