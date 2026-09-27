using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Items;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.UnitLogic.Alignments;
using Newtonsoft.Json.Linq;
using Tirabade;

// E5: construct Mythic / NativeNext / Alignment answers with the real game assemblies (Main.BuildScene) and compare
// them with the native Trickster answer they imitate (Goddesses_Summit/Answer_0214) from blueprints.zip.
internal static class ChoiceExtensionManagedTests
{
    private const string NativeTricksterAnswer = "e328123e766e3d1429de966a1728f70c"; // c5 Goddesses_Summit/Answer_0214
    private const string NocticulaCue = "77216dc2c3770794f93b010659f4aa64";          // c6 NocticulaThreshold/Cue_0056
    private const string StorytellerCue = "ca71b79bc9a45b741bcc6599ef017fe7";        // StoryTeller_MainDialogue/Cue_0785
    private const string NativeCrusadeCue = "7005d12127f06b94995a262a0e6bd675";      // c3 KTC_ReactivityReinforcements/Cue_0028 (AddCrusadeResources)
    private const string NativeRemovalCue = "6603e3274d42438faa38af673024a832";      // c0 RadianceFound/Cue_0002 (RemoveItemFromPlayer)
    private const string Scale = "816f244523b5455a85ae06db452d4330";                 // TerendelevScaleItem
    private const BindingFlags PrivateStatic = BindingFlags.NonPublic | BindingFlags.Static;

    public static IEnumerable<string> NativeIds => Rules.MythicAchievementFlags.Values
        .Concat(new[] { NativeTricksterAnswer, NocticulaCue, StorytellerCue, NativeCrusadeCue, NativeRemovalCue, Scale });

    private static bool IsItem(Dictionary<string, JObject> native, string guid) =>
        ((string)native[guid]["$type"]!).Split(new[] { ", " }, StringSplitOptions.None).Last().StartsWith("BlueprintItem", StringComparison.Ordinal);

    public static void Run(Dictionary<string, JObject> native, Func<string, BlueprintUnlockableFlag> seedFlag,
        Func<string, BlueprintCue> seedCue, Func<string, BlueprintItem> seedItem, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        // Every whitelisted name exists in the shipped enums.
        check(Rules.MythicNames.All(name => Enum.IsDefined(typeof(Mythic), name))
            && Enum.GetNames(typeof(Mythic)).Except(new[] { "None" }).OrderBy(x => x).SequenceEqual(Rules.MythicNames.OrderBy(x => x)),
            "Rules.MythicNames differs from Kingmaker.DialogSystem.Blueprints.Mythic.");
        check(Enum.GetNames(typeof(AlignmentShiftDirection)).OrderBy(x => x).SequenceEqual(Rules.AlignmentDirections.OrderBy(x => x)),
            "Rules.AlignmentDirections differs from AlignmentShiftDirection.");
        foreach (var pair in Rules.MythicAchievementFlags)
        {
            check(((string)native[pair.Value]["$type"]!).EndsWith(", BlueprintUnlockableFlag", StringComparison.Ordinal),
                "Mythic achievement counter is not a BlueprintUnlockableFlag: " + pair.Key);
            seedFlag(pair.Value);
        }
        foreach (string cue in new[] { NocticulaCue, StorytellerCue })
        {
            check(((string)native[cue]["$type"]!).EndsWith(", BlueprintCue", StringComparison.Ordinal), "Native continuation fixture is not a cue: " + cue);
            seedCue(cue);
        }
        // The native shape being imitated.
        var reference = native[NativeTricksterAnswer];
        var nativeIncrement = (JObject)reference["OnSelect"]!["Actions"]![0]!;
        check((string)reference["MythicRequirement"]! == "PlayerIsTrickster"
            && ((string)nativeIncrement["$type"]!).EndsWith(", IncrementFlagValue", StringComparison.Ordinal)
            && (string)nativeIncrement["m_Flag"]! == "!bp_" + Rules.MythicAchievementFlags["Trickster"]
            && ((string)nativeIncrement["Value"]!["$type"]!).EndsWith(", IntConstant", StringComparison.Ordinal)
            && (int)nativeIncrement["Value"]!["Value"]! == 1 && (bool)nativeIncrement["UnlockIfNot"]!,
            "Answer_0214 no longer has the native Trickster answer shape this extension imitates.");

        var scene = new Scene
        {
            Id = "e5.fixture.trickster.setup", Title = "E5 fixture", Owner = "Nocticula", Relationship = "nocticula",
            AnswerLists = new[] { "871af36f2ab2b1f40b5de77976c54276" }, NativeReturnCue = StorytellerCue, MinChapter = 5,
            Nodes = new List<Tirabade.Node>
            {
                new Tirabade.Node { Id = "start", Speaker = "Narrator", Text = "fixture", Choices = new List<Choice> {
                    new Choice { Text = "Trick", Next = "more", Mythic = "PlayerIsTrickster", Alignment = new AlignmentChoice { Direction = "Chaotic", Value = 1 } },
                    new Choice { Text = "Let it happen", NativeNext = NocticulaCue } } },
                new Tirabade.Node { Id = "more", Speaker = "Narrator", Text = "fixture", Choices = new List<Choice> { new Choice { Mythic = "TricksterUnlocked" },
                    new Choice { Text = "Pay", Crusade = new CrusadeChoice { Resource = "Finances", Amount = -500 }, RemoveItem = Scale },
                    new Choice { Text = "Gain", Crusade = new CrusadeChoice { Resource = "Favors", Amount = 3 } } } }
            }
        };
        seedItem(Scale);
        typeof(Main).GetMethod("BuildScene", PrivateStatic)!.Invoke(null, new object[] { scene });
        BlueprintAnswer Answer(string node, int index) =>
            (BlueprintAnswer)ResourcesLibrary.TryGetBlueprint(id("answer." + scene.Id + "." + node + "." + index))!;

        var mythic = Answer("start", 0);
        var increment = mythic.OnSelect.Actions.OfType<IncrementFlagValue>().SingleOrDefault();
        check(mythic.MythicRequirement == Mythic.PlayerIsTrickster, "Mythic answer lacks MythicRequirement.");
        check(mythic.OnSelect.Actions.Length == 2 && mythic.OnSelect.Actions[0] is Main.RouteAction && increment != null,
            "Mythic answer lost its route action or achievement counter.");
        check(increment!.Flag?.AssetGuid == BlueprintGuid.Parse(Rules.MythicAchievementFlags["Trickster"]) && increment.UnlockIfNot
            && increment.Value is IntConstant constant && constant.Value == 1 && ReferenceEquals(constant.Owner, mythic),
            "Achievement counter differs from the native IncrementFlagValue shape.");
        check(mythic.AlignmentShift.Direction == AlignmentShiftDirection.Chaotic && mythic.AlignmentShift.Value == 1
            && mythic.AlignmentShift.Description != null, "Alignment shift not applied to the answer.");
        check(mythic.NextCue.Cues.Single().Guid == id("cue." + scene.Id + ".more"), "Mythic answer lost its authored next cue.");

        var continuation = Answer("start", 1);
        check(continuation.NextCue.Cues.Single().Guid == BlueprintGuid.Parse(NocticulaCue) && continuation.NextCue.Cues.Single().Get() is BlueprintCue,
            "NativeNext does not continue into the native cue.");
        check(continuation.MythicRequirement == Mythic.None && continuation.OnSelect.Actions.Length == 1
            && continuation.OnSelect.Actions[0] is Main.RouteAction route && ReferenceEquals(route.Complete, scene)
            && continuation.AlignmentShift.Value == 0, "A plain native continuation gained native effects or lost scene completion.");

        var unlocked = Answer("more", 0);
        check(unlocked.MythicRequirement == Mythic.TricksterUnlocked && unlocked.OnSelect.Actions.OfType<IncrementFlagValue>().Count() == 1,
            "TricksterUnlocked answer lacks its requirement or counter.");
        check(unlocked.NextCue.Cues.Single().Guid == BlueprintGuid.Parse(StorytellerCue), "Terminal inline answer no longer returns to the native cue.");
        // E11 native costs, compared with the archive's own AddCrusadeResources / RemoveItemFromPlayer shapes.
        var nativeAdd = (JObject)native[NativeCrusadeCue]["OnShow"]!["Actions"]![0]!;
        var nativeRemove = (JObject)native[NativeRemovalCue]["OnShow"]!["Actions"]![0]!;
        check(((string)nativeAdd["$type"]!).EndsWith(", AddCrusadeResources", StringComparison.Ordinal) && nativeAdd["_resourcesAmount"]!["m_Finances"] != null
            && ((string)nativeRemove["$type"]!).EndsWith(", RemoveItemFromPlayer", StringComparison.Ordinal) && (int)nativeRemove["Quantity"]! == 1,
            "Archive cost actions no longer have the shape the E11 extension imitates.");
        check(IsItem(native, Scale), "Removable-item fixture is not a BlueprintItem.");
        var pay = Answer("more", 1);
        var spend = pay.OnSelect.Actions.OfType<Kingmaker.Kingdom.Blueprints.RemoveCrusadeResources>().SingleOrDefault();
        var removal = pay.OnSelect.Actions.OfType<RemoveItemFromPlayer>().SingleOrDefault();
        check(pay.OnSelect.Actions[0] is Main.RouteAction && spend != null && removal != null, "Cost answer lacks its route action or native costs.");
        var spent = (Kingmaker.Kingdom.KingdomResourcesAmount)typeof(Kingmaker.Kingdom.Blueprints.RemoveCrusadeResources)
            .GetField("m_ResourcesAmount", BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.Public)!.GetValue(spend);
        check(spent.Equals(Kingmaker.Kingdom.KingdomResourcesAmount.FromFinances(500)), "Crusade cost has the wrong amount or resource.");
        check(removal!.ItemToRemove?.AssetGuid == BlueprintGuid.Parse(Scale) && removal.Quantity == 1 && !removal.RemoveAll && !removal.Money,
            "Item removal differs from the native RemoveItemFromPlayer shape.");
        var gain = Answer("more", 2).OnSelect.Actions.OfType<Kingmaker.Kingdom.Blueprints.AddCrusadeResources>().SingleOrDefault();
        var gained = (Kingmaker.Kingdom.KingdomResourcesAmount)typeof(Kingmaker.Kingdom.Blueprints.AddCrusadeResources)
            .GetField("_resourcesAmount", BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.Public)!.GetValue(gain);
        check(gain != null && gained.Equals(Kingmaker.Kingdom.KingdomResourcesAmount.FromFavors(3)), "Crusade gain differs from AddCrusadeResources.");
        check(Enum.GetNames(typeof(Kingmaker.Kingdom.KingdomResource)).Except(new[] { "None" }).SequenceEqual(Rules.CrusadeResources),
            "Rules.CrusadeResources differs from Kingmaker.Kingdom.KingdomResource.");
        // E13: Build applies Scene.EntryMythic / EntryAlignment to the entry answer through the same ConfigureNativeEffects.
        var entryAnswer = new BlueprintAnswer();
        entryAnswer.OnSelect = new Kingmaker.ElementsSystem.ActionList { Actions = new Kingmaker.ElementsSystem.GameAction[] { new Main.RouteAction() } };
        typeof(Main).GetMethod("ConfigureNativeEffects", PrivateStatic)!.Invoke(null, new object[] { entryAnswer,
            new Choice { Mythic = "PlayerIsTrickster", Alignment = new AlignmentChoice { Direction = "Chaotic", Value = 1 } }, new Action<string>(_ => { }) });
        check(entryAnswer.MythicRequirement == Mythic.PlayerIsTrickster && entryAnswer.OnSelect.Actions.Length == 2
            && entryAnswer.OnSelect.Actions[1] is IncrementFlagValue && entryAnswer.AlignmentShift.Direction == AlignmentShiftDirection.Chaotic,
            "Entry-answer native effects differ from the E5 choice shape.");
        Console.WriteLine("PASS: E5/E11 choice extensions built with the real assemblies (Mythic, NativeNext, Alignment, Crusade, RemoveItem) and matched native shapes.");
    }
}
