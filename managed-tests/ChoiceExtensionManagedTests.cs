using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
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
    private const BindingFlags PrivateStatic = BindingFlags.NonPublic | BindingFlags.Static;

    public static IEnumerable<string> NativeIds => Rules.MythicAchievementFlags.Values
        .Concat(new[] { NativeTricksterAnswer, NocticulaCue, StorytellerCue });

    public static void Run(Dictionary<string, JObject> native, Func<string, BlueprintUnlockableFlag> seedFlag,
        Func<string, BlueprintCue> seedCue, Func<string, BlueprintGuid> id, Action<bool, string> check)
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
                new Tirabade.Node { Id = "more", Speaker = "Narrator", Text = "fixture", Choices = new List<Choice> { new Choice { Mythic = "TricksterUnlocked" } } }
            }
        };
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
        Console.WriteLine("PASS: E5 choice extensions built with the real assemblies (Mythic, NativeNext, Alignment) and matched Answer_0214.");
    }
}
