using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Items;
using Kingmaker.Blueprints.Quests;
using Newtonsoft.Json.Linq;
using Tirabade;

// E10 + ER-5: the read-only native readers resolve the right archive types and read real game state containers.
internal static class NativeReaderManagedTests
{
    private const string Flag = "23cacf7a07480da459b3a59d0fd6da82";      // WenduagRomance_VelexiaConflict_flag
    private const string Item = "d66b1fdc9d313784ca51712640e210c7";      // EmptySyphon
    private const string Quest = "5a5a533c9ce630a48b877f9a194840cb";     // WeightOfMySword_SeelahQ3_quest
    private const string Objective = "3fb92b54fc950714799b3444672d39e6"; // C3_FoolKing/Obj_025_ReadyForCrowning
    private const BindingFlags PrivateStatic = BindingFlags.NonPublic | BindingFlags.Static;

    public static IEnumerable<string> NativeIds(Story story) => new[] { Flag, Item, Quest, Objective }
        .Concat(story.UnlockableFlags.Values).Concat(story.InventoryItems.Values).Concat(story.PartyItems.Values).Concat(story.StartedQuests.Values).Concat(story.MainCharacterFacts.Values)
        .Concat(story.QuestObjectives.Values.Select(v => v[0]));

    private static T Seed<T>(string guid) where T : SimpleBlueprint, new()
    {
        var id = BlueprintGuid.Parse(guid);
        if (ResourcesLibrary.TryGetBlueprint(id) is T prior) return prior;
        var blueprint = new T { AssetGuid = id, name = "NativeFixture_" + guid };
        ResourcesLibrary.BlueprintsCache.AddCachedBlueprint(id, blueprint);
        return blueprint;
    }

    public static void Run(Story story, Dictionary<string, JObject> native, Action<bool, string> check)
    {
        bool Is(string guid, string type) => ((string)native[guid]["$type"]!).EndsWith(", " + type, StringComparison.Ordinal);
        bool IsItem(string guid) => ((string)native[guid]["$type"]!).Split(new[] { ", " }, StringSplitOptions.None).Last().StartsWith("BlueprintItem", StringComparison.Ordinal);
        check(Is(Flag, "BlueprintUnlockableFlag") && IsItem(Item) && Is(Quest, "BlueprintQuest") && Is(Objective, "BlueprintQuestObjective"),
            "Reader fixture GUIDs have unexpected archive types.");
        foreach (var guid in story.UnlockableFlags.Values) check(Is(guid, "BlueprintUnlockableFlag"), "UnlockableFlags binding is not a BlueprintUnlockableFlag: " + guid);
        foreach (var guid in story.InventoryItems.Values) check(IsItem(guid), "InventoryItems binding is not a BlueprintItem: " + guid);
        foreach (var guid in story.PartyItems.Values) check(IsItem(guid), "PartyItems binding is not a BlueprintItem: " + guid);
        foreach (var guid in story.StartedQuests.Values) check(Is(guid, "BlueprintQuest"), "StartedQuests binding is not a BlueprintQuest: " + guid);
        foreach (var guid in story.MainCharacterFacts.Values) check(Is(guid, "BlueprintFeature"), "MainCharacterFacts binding is not a BlueprintFeature: " + guid);
        foreach (var value in story.QuestObjectives.Values) check(Is(value[0], "BlueprintQuestObjective"), "QuestObjectives binding is not an objective: " + value[0]);

        // Main.ReadNativeProgress over real containers: UnlockableFlagsManager values, a fresh QuestBook, an item predicate.
        var flag = Seed<BlueprintUnlockableFlag>(Flag);
        var item = Seed<BlueprintItem>(Item);
        var quest = Seed<BlueprintQuest>(Quest);
        var objective = Seed<BlueprintQuestObjective>(Objective);
        var questRef = new BlueprintQuestReference();
        typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!
            .SetValue(questRef, quest.AssetGuid);
        typeof(BlueprintQuestObjective).GetField("m_Quest", BindingFlags.Instance | BindingFlags.NonPublic)!.SetValue(objective, questRef);
        var main = typeof(Main);
        var flags = (Dictionary<string, BlueprintUnlockableFlag>)main.GetField("nativeFlags", PrivateStatic)!.GetValue(null)!;
        var items = (Dictionary<string, BlueprintItem>)main.GetField("nativeItems", PrivateStatic)!.GetValue(null)!;
        var quests = (Dictionary<string, BlueprintQuest>)main.GetField("startedQuests", PrivateStatic)!.GetValue(null)!;
        var objectives = (Dictionary<string, KeyValuePair<BlueprintQuestObjective, QuestObjectiveState>>)main.GetField("nativeObjectives", PrivateStatic)!.GetValue(null)!;
        var saved = (flags.ToArray(), items.ToArray(), quests.ToArray(), objectives.ToArray());
        try
        {
            flags["e10.flag"] = flag;
            items["e10.item"] = item;
            quests["e10.quest"] = quest;
            objectives["e10.objective_none"] = new KeyValuePair<BlueprintQuestObjective, QuestObjectiveState>(objective, QuestObjectiveState.None);
            objectives["e10.objective_done"] = new KeyValuePair<BlueprintQuestObjective, QuestObjectiveState>(objective, QuestObjectiveState.Completed);
            var read = main.GetMethod("ReadNativeProgress", PrivateStatic)!;
            var manager = new UnlockableFlagsManager();
            var book = new QuestBook();
            bool held = false;
            Snapshot Read()
            {
                var state = new Snapshot();
                read.Invoke(null, new object[] { manager, book, new Func<BlueprintItem, bool>(bp => held && ReferenceEquals(bp, item)), state });
                return state;
            }
            var before = Read();
            check(!before.Has("e10.flag") && !before.Has("e10.item") && !before.Has("e10.quest") && !before.Has("e10.objective_done")
                && before.Has("e10.objective_none"), "Native readers report state that was never set.");
            manager.UnlockedFlags.Add(flag, 0);
            check(!Read().Has("e10.flag"), "An unlocked flag with value 0 reads as true.");
            manager.UnlockedFlags[flag] = 2;
            held = true;
            var after = Read();
            check(after.Has("e10.flag") && after.Has("e10.item"), "Flag value > 0 or held item not read.");
            check(manager.GetFlagValue(flag) == 2 && manager.UnlockedFlags.Count == 1, "Reading native flags changed them.");
        }
        finally
        {
            flags.Clear(); foreach (var p in saved.Item1) flags.Add(p.Key, p.Value);
            items.Clear(); foreach (var p in saved.Item2) items.Add(p.Key, p.Value);
            quests.Clear(); foreach (var p in saved.Item3) quests.Add(p.Key, p.Value);
            objectives.Clear(); foreach (var p in saved.Item4) objectives.Add(p.Key, p.Value);
        }
        // E10 (party-only): every PartyItems binding is resolved by Build, and ReadPartyItems reports only what the party predicate
        // holds (Main passes Player.Inventory alone, never the shared stash: an item only in the stash reads as not held).
        var party = (Dictionary<string, BlueprintItem>)main.GetField("partyItems", PrivateStatic)!.GetValue(null)!;
        check(story.PartyItems.Keys.All(party.ContainsKey), "A PartyItems binding was not resolved by Build.");
        var readParty = main.GetMethod("ReadPartyItems", PrivateStatic)!;
        foreach (bool inParty in new[] { false, true })
        {
            var state = new Snapshot();
            readParty.Invoke(null, new object[] { new Func<BlueprintItem, bool>(_ => inParty), state });
            check(story.PartyItems.Keys.All(k => state.Has(k) == inParty), "The party-only item reader misreports: " + inParty);
        }
        var throwing = new Snapshot();
        readParty.Invoke(null, new object[] { new Func<BlueprintItem, bool>(_ => throw new InvalidOperationException("fixture")), throwing });
        check(!story.PartyItems.Keys.Any(throwing.Has), "A throwing party read reports the item as held.");
        var mainSource = System.IO.File.ReadAllText(System.IO.Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "..", "..", "..", "..", "src", "Main.cs"));
        check(mainSource.Contains("ReadPartyItems(item => player.Inventory.Contains(item), state);"),
            "Main.BuildState no longer reads PartyItems from the party inventory alone.");
        // MainCharacterFacts: every bound fact is resolved by Build, and the reader reports exactly what the unit holds.
        var facts = (System.Collections.IDictionary)main.GetField("mainCharacterFacts", PrivateStatic)!.GetValue(null)!;
        check(story.MainCharacterFacts.Keys.All(facts.Contains), "A MainCharacterFacts binding was not resolved by Build.");
        var readFacts = main.GetMethod("ReadMainCharacterFacts", BindingFlags.NonPublic | BindingFlags.Static)!;
        foreach (bool holdsFact in new[] { false, true })
        {
            var state = new Snapshot();
            readFacts.Invoke(null, new object[] { new Func<Kingmaker.Blueprints.Facts.BlueprintUnitFact, bool>(_ => holdsFact), state });
            check(story.MainCharacterFacts.Keys.All(k => state.Has(k) == holdsFact), "The main-character fact reader misreports: " + holdsFact);
        }
        Console.WriteLine("PASS: E10 native readers (UnlockableFlags, QuestObjectives, InventoryItems, StartedQuests, MainCharacterFacts) resolve archive types and read real containers.");
    }
}
