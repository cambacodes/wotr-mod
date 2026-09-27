using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

// E5: Choice.Mythic / NativeNext / Alignment are whitelisted native answer effects.
internal static class ChoiceExtensionTests
{
    private const string NocticulaCue = "77216dc2c3770794f93b010659f4aa64"; // c6 NocticulaThreshold/Cue_0056
    private const string ReturnCue = "ca71b79bc9a45b741bcc6599ef017fe7";    // StoryTeller_MainDialogue/Cue_0785 (fixture use)

    private static Story Fixture()
    {
        var story = new Story();
        story.Relationships["nocticula"] = new Relationship { Title = "Nocticula", StartedFlag = "noct.started",
            ClosedFlag = "noct.closed", CommittedFlag = "noct.committed" };
        story.Etudes["trickster"] = "9f486a9c0c9abfc4a952bb22e88a7e96";
        story.Scenes.Add(new Scene
        {
            Id = "noct.trickster.threshold.setup", Title = "setup", Owner = "Nocticula", Relationship = "nocticula",
            AnswerLists = new[] { "871af36f2ab2b1f40b5de77976c54276" }, NativeReturnCue = ReturnCue, MinChapter = 5,
            Requires = new[] { "trickster" },
            Nodes = new List<Node> { new Node { Id = "start", Speaker = "Nocticula", Text = "x", Choices = new List<Choice> {
                new Choice { Text = "Trick", Next = "more", Mythic = "PlayerIsTrickster", Alignment = new AlignmentChoice { Direction = "Chaotic", Value = 1 } },
                new Choice { Text = "Leave it to the native scene", NativeNext = NocticulaCue, Set = new[] { "noct.trickster.primed" } } } },
                new Node { Id = "more", Speaker = "Nocticula", Text = "y", Choices = new List<Choice> { new Choice { Mythic = "TricksterUnlocked" } } } }
        });
        story.Scenes.Add(new Scene
        {
            Id = "noct.trickster.threshold.letter", Title = "letter", Owner = "Memory", Relationship = "nocticula", Remote = true, MinChapter = 5,
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> {
                new Choice { Mythic = "PlayerIsAeon", Alignment = new AlignmentChoice { Direction = "LawfulGood", Value = 2 } } } } }
        });
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        var story = Fixture();
        Rules.Validate(story);
        // Round trip through the same serializer family as Story.json keeps the new fields.
        var json = JsonSerializer.Serialize(story, new JsonSerializerOptions { IncludeFields = true });
        var reloaded = JsonSerializer.Deserialize<Story>(json, new JsonSerializerOptions { IncludeFields = true })!;
        var choice = reloaded.Scenes[0].Nodes[0].Choices[0];
        check(choice.Mythic == "PlayerIsTrickster" && choice.Alignment?.Direction == "Chaotic" && choice.Alignment.Value == 1
            && reloaded.Scenes[0].Nodes[0].Choices[1].NativeNext == NocticulaCue, "Choice extensions lost in a Story.json round trip.");
        Rules.Validate(reloaded);
        // Absent fields stay null, so existing stories are unchanged.
        check(new Choice().Mythic == null && new Choice().NativeNext == null && new Choice().Alignment == null, "Choice extension defaults are not null.");
        check(Rules.MythicNames.Length == 20 && Rules.MythicNames.All(name => Rules.MythicAchievementFlags.ContainsKey(Rules.MythicPath(name))),
            "Every mythic requirement needs its verified achievement counter.");
        check(Rules.MythicPath("PlayerIsTrickster") == "Trickster" && Rules.MythicPath("TricksterUnlocked") == "Trickster", "Mythic path mapping.");

        void Invalid(string what, Action<Story> mutate)
        {
            var bad = Fixture();
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid choice extension accepted: " + what);
        }
        Choice First(Story s) => s.Scenes[0].Nodes[0].Choices[0];
        Choice Native(Story s) => s.Scenes[0].Nodes[0].Choices[1];
        Invalid("unknown mythic", s => First(s).Mythic = "Trickster");
        Invalid("mythic None", s => First(s).Mythic = "None");
        Invalid("mythic on an epilogue", s => { s.Scenes[1].Owner = "Epilogue"; s.Scenes[1].Remote = false; });
        Invalid("unknown alignment", s => First(s).Alignment = new AlignmentChoice { Direction = "Chaos", Value = 1 });
        Invalid("zero alignment", s => First(s).Alignment = new AlignmentChoice { Direction = "Chaotic", Value = 0 });
        Invalid("negative alignment", s => First(s).Alignment = new AlignmentChoice { Direction = "Chaotic", Value = -1 });
        Invalid("native_next bad guid", s => Native(s).NativeNext = "not-a-guid");
        Invalid("native_next empty guid", s => Native(s).NativeNext = "00000000000000000000000000000000");
        Invalid("native_next with next", s => Native(s).Next = "more");
        Invalid("native_next with abort", s => Native(s).Abort = true);
        Invalid("native_next equals the return cue", s => Native(s).NativeNext = ReturnCue);
        Invalid("native_next outside an inline scene", s => s.Scenes[1].Nodes[0].Choices[0].NativeNext = NocticulaCue);
        Invalid("native_next with a check", s =>
        {
            Native(s).Check = new SkillCheck { Skill = "CheckBluff", DC = 10, Success = "more", Failure = "start" };
        });
    }
}
