using System;
using System.Collections.Generic;
using System.Linq;

namespace Tirabade
{
    public sealed class Story
    {
        public List<Scene> Scenes = new List<Scene>();
        public Dictionary<string, string> Etudes = new Dictionary<string, string>();
        public Dictionary<string, string> CompletedQuests = new Dictionary<string, string>();
        public Dictionary<string, string[]> SeenCues = new Dictionary<string, string[]>();
        public Dictionary<string, string> SelectedAnswers = new Dictionary<string, string>();
        public Dictionary<string, string> StartedDialogs = new Dictionary<string, string>();
        public Dictionary<string, string> CompletedEtudes = new Dictionary<string, string>();
        public Dictionary<string, Revival> Revivals = new Dictionary<string, Revival>();
        public Dictionary<string, ParentEndingEdit> ParentEpilogueEdits = new Dictionary<string, ParentEndingEdit>();
        public List<ParentEndingLossRule> ParentEpilogueLossRules = new List<ParentEndingLossRule>();
        public string[] PermanentEtudes = Array.Empty<string>();
        // E1: authored flags recorded forever the first time any native/derived source key is observed (TT-02).
        public Dictionary<string, string[]> Latches = new Dictionary<string, string[]>();
        // E4: data-driven composite flags, an OR of AND-groups over any known flag, computed in State() after latches.
        public Dictionary<string, string[][]> Derived = new Dictionary<string, string[][]>();
        public Dictionary<string, Relationship> Relationships = new Dictionary<string, Relationship>
        {
            ["tirabade"] = new Relationship
            {
                Title = "Three at the Table",
                Description = "There is room for more than military reports in my conversations with Anevia and Irabeth. What we make of that time is another matter.",
                Objective = "Make time for Anevia and Irabeth",
                Guidance = "Speak to each woman at headquarters. Private conversations develop over the campaign, with time between meetings. In the Abyss, there may be time to write during a quiet rest.",
                StartedFlag = "started", ClosedFlag = "closed", CommittedFlag = "committed",
                UnavailableFlags = new[] { "anevia_dead", "irabeth_dead", "anevia_gone", "irabeth_gone", "swarm", "true_lich" },
                FailureFlags = new[] { "loss", "inhuman" }
            }
        };
    }

    public class ParentEndingText
    {
        public string LocalizedKey = "";
        public string? Text;
    }

    public sealed class ParentEndingEdit : ParentEndingText
    {
        public string ParentKey = "";
        public string Owner = "";
        public string[] Requires = Array.Empty<string>();
        public string[] Forbids = Array.Empty<string>();
    }

    public sealed class ParentEndingLossRule
    {
        public string Id = "";
        public string Owner = "";
        public string[] Requires = Array.Empty<string>();
        public string[] Forbids = Array.Empty<string>();
        public string[] ReplacementScenes = Array.Empty<string>();
        public string[] SuppressPages = Array.Empty<string>();
        public string[] SuppressCues = Array.Empty<string>();
        public Dictionary<string, ParentEndingText> SurvivorAlternates = new Dictionary<string, ParentEndingText>();
    }

    public enum ParentEndingSelection { Original, Suppress, Ordinary, Survivor }

    public sealed class Revival
    {
        public string Relationship = "";
        public string Unit = "";
        public string DeathFlag = "";
    }

    public sealed class Relationship
    {
        public string Title = "";
        public string Description = "";
        public string Objective = "";
        public string Guidance = "";
        public string StartedFlag = "";
        public string ClosedFlag = "";
        public string CommittedFlag = "";
        public string[] UnavailableFlags = Array.Empty<string>();
        public string[] FailureFlags = Array.Empty<string>();
        // E2: an UnavailableFlag stops blocking once its authored return flag is held (Trickster returns).
        public Dictionary<string, string> UnavailableOverrides = new Dictionary<string, string>();
    }

    public sealed class Scene
    {
        public string Id = "";
        public string Title = "";
        public string Entry = "";
        public string Owner = "Anevia";
        public string Relationship = "tirabade";
        public string[] AnswerLists = Array.Empty<string>();
        public string? NativeReturnCue;
        public string[] Areas = Array.Empty<string>();
        public int[] Chapters = Array.Empty<int>();
        public bool Remote;
        public bool ManualOnly;
        public string? InteractionHub;
        public string? Recovery;
        public string? AfterRecovery;
        public string? AfterDeparture;
        public string? ContactUnit;
        public string[] AdditionalContactUnits = Array.Empty<string>();
        public int MinChapter = 1;
        public int MaxChapter = 5;
        public int DelayHours;
        public bool Optional;
        public string[] Requires = Array.Empty<string>();
        public string[] RequiresAny = Array.Empty<string>();
        public string[][] RequiresAnyGroups = Array.Empty<string[]>();
        public string[] Forbids = Array.Empty<string>();
        public Dictionary<string, string> ForbidOverrides = new Dictionary<string, string>();
        public List<Node> Nodes = new List<Node>();
    }

    public sealed class Node
    {
        public string Id = "";
        public string Speaker = "Narrator";
        public string Portrait = "";
        public string Text = "";
        public List<Choice> Choices = new List<Choice>();
    }

    public sealed class Choice
    {
        public string Text = "Continue";
        public string? Next;
        public bool Abort;
        public string? Revive;
        public SkillCheck? Check;
        public string[] Set = Array.Empty<string>();
        public string[] Requires = Array.Empty<string>();
        public string[] Forbids = Array.Empty<string>();
        // E5 native answer effects. Mythic: a Kingmaker.DialogSystem.Blueprints.Mythic name (MythicRequirement plus the
        // native mythic-choice achievement counter). NativeNext: a native BlueprintCue of the same dialog, for a terminal
        // choice of an inline (NativeReturnCue) scene. Alignment: a native AlignmentShift applied on select.
        public string? Mythic;
        public string? NativeNext;
        public AlignmentChoice? Alignment;
    }

    public sealed class AlignmentChoice
    {
        public string Direction = "";
        public int Value;
    }

    public sealed class SkillCheck
    {
        public string Skill = "";
        public int DC;
        public string Success = "";
        public string Failure = "";
        public bool CommanderOnly = true;
    }

    public sealed class Snapshot
    {
        public int Chapter;
        public int Hour;
        public string Area = "";
        public HashSet<string> Flags = new HashSet<string>(StringComparer.Ordinal);
        public HashSet<string> AvailableContacts = new HashSet<string>(StringComparer.Ordinal);
        public Dictionary<string, int> Times = new Dictionary<string, int>();
        public bool Has(string flag) => Flags.Contains(flag);
    }

    public static class Rules
    {
        public const string NurahCapital = "2570015799edf594daf2f076f2f975d8";
        public const string NurahContact = "f999fc37ddb225640b7f98c0a05d6948";
        public static readonly string[] CheckSkills = { "SkillAthletics", "SkillMobility", "SkillStealth", "SkillThievery", "SkillKnowledgeArcana", "SkillKnowledgeWorld", "SkillLoreNature", "SkillLoreReligion", "SkillPerception", "SkillUseMagicDevice", "CheckDiplomacy", "CheckBluff", "CheckIntimidate" };

        // Kingmaker.DialogSystem.Blueprints.Mythic (Assembly-CSharp), minus None.
        public static readonly string[] MythicNames = { "PlayerIsAeon", "PlayerIsAngel", "PlayerIsAzata", "PlayerIsDemon", "PlayerIsDevil",
            "PlayerIsDragon", "PlayerIsLegend", "PlayerIsLich", "PlayerIsLocust", "PlayerIsTrickster", "AeonUnlocked", "AngelUnlocked",
            "AzataUnlocked", "DemonUnlocked", "DevilUnlocked", "DragonUnlocked", "LegendUnlocked", "LocustUnlocked", "LichUnlocked", "TricksterUnlocked" };

        // Kingmaker.UnitLogic.Alignments.AlignmentShiftDirection.
        public static readonly string[] AlignmentDirections = { "LawfulGood", "NeutralGood", "ChaoticGood", "LawfulNeutral", "TrueNeutral",
            "ChaoticNeutral", "LawfulEvil", "NeutralEvil", "ChaoticEvil", "Good", "Evil", "Lawful", "Chaotic" };

        // MythicChoices_<path>_Achievement BlueprintUnlockableFlags (blueprints.zip, GameAchievements_Flag). Native answers with
        // MythicRequirement PlayerIs<path> or <path>Unlocked add IncrementFlagValue(flag, IntConstant 1, UnlockIfNot) on select
        // (e.g. Goddesses_Summit/Answer_0214); verified for every path, including the one Lich-path answer that counts for Devil.
        public static readonly Dictionary<string, string> MythicAchievementFlags = new Dictionary<string, string>
        {
            ["Aeon"] = "7715151721f747eebf0ab22fe14ff190", ["Angel"] = "c1691692455b46228ba19ad9eb1d3b3d",
            ["Azata"] = "04aa3a7e7fc14101b4453f7fd7d83d88", ["Demon"] = "1604aba2aae245a5bcb481a99b8bdaeb",
            ["Devil"] = "5c2c056854a44ec4904d258505e03eea", ["Dragon"] = "1711d42130814faebc6f2bb5b0a5b514",
            ["Legend"] = "deb42e87a7a54194bac798a8f98f8beb", ["Lich"] = "b7f5fe87397b446aadc6f061de76f109",
            ["Locust"] = "271b28c9b5b7441c809a825885f00d29", ["Trickster"] = "611b65da018c4922b3f0656055fd0553",
        };

        public static string MythicPath(string mythic) => mythic.StartsWith("PlayerIs", StringComparison.Ordinal)
            ? mythic.Substring("PlayerIs".Length) : mythic.Substring(0, mythic.Length - "Unlocked".Length);

        public static IEnumerable<string> NextNodes(Choice choice) => choice.Check != null
            ? new[] { choice.Check.Success, choice.Check.Failure }
            : choice.Next == null ? Array.Empty<string>() : new[] { choice.Next };

        public static bool Match(IEnumerable<string> requires, IEnumerable<string> forbids, Snapshot state) =>
            requires.All(state.Has) && !forbids.Any(state.Has);

        // These gates add earned story policy; the native page and cue checkers still decide eligibility.
        public static ParentEndingLossRule? ParentEndingLoss(Story story, string owner, Snapshot state) =>
            story.ParentEpilogueLossRules.Where(rule => rule.Owner == owner && Match(rule.Requires, rule.Forbids, state)
                && rule.ReplacementScenes.Any(id => story.Scenes.Any(scene => scene.Id == id && scene.Owner == owner
                    && (state.Has(id) || Available(story, scene, state))))).SingleOrDefault();

        public static bool ParentEndingPageSuppressed(Story story, string page, string owner, Snapshot state) =>
            ParentEndingLoss(story, owner, state)?.SuppressPages.Contains(page) == true;

        public static ParentEndingSelection ParentEndingCue(Story story, string page, string cue, string owner,
            Snapshot state, out ParentEndingText? alternate)
        {
            alternate = null;
            var loss = ParentEndingLoss(story, owner, state);
            if (loss != null)
            {
                if (loss.SuppressPages.Contains(page)) return ParentEndingSelection.Suppress;
                if (loss.SurvivorAlternates.TryGetValue(cue, out alternate)) return ParentEndingSelection.Survivor;
                if (loss.SuppressCues.Contains(cue)) return ParentEndingSelection.Suppress;
            }
            if (!story.ParentEpilogueEdits.TryGetValue(cue, out var edit) || edit.Owner != owner
                || !Match(edit.Requires, edit.Forbids, state)) return ParentEndingSelection.Original;
            if (edit.Text == null) return ParentEndingSelection.Suppress;
            alternate = edit;
            return ParentEndingSelection.Ordinary;
        }

        // Set by Main.Build when a relationship's native dependencies are missing; never authored.
        public const string DegradedPrefix = "rrt.degraded.";

        public static bool Available(Story story, Scene scene, Snapshot state)
        {
            if (state.Has(DegradedPrefix + scene.Relationship)) return false;
            if (state.Chapter < scene.MinChapter || state.Chapter > scene.MaxChapter || state.Has(scene.Id)) return false;
            if (scene.Chapters.Length > 0 && !scene.Chapters.Contains(state.Chapter)) return false;
            if (scene.Areas.Length > 0 && !scene.Areas.Contains(state.Area)) return false;
            if (!scene.Requires.All(state.Has) || scene.Forbids.Any(flag => ForbidHolds(scene, flag, state))) return false;
            if (scene.RequiresAny.Length > 0 && !scene.RequiresAny.Any(state.Has)) return false;
            if (!scene.RequiresAnyGroups.All(group => group.Any(state.Has))) return false;
            if (!ContactAvailable(story, scene, state)) return false;
            if (scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)) return true;
            var relationship = story.Relationships[scene.Relationship];
            var recovery = scene.Recovery == null ? null : story.Revivals[scene.Recovery];
            if (recovery != null && !state.Has("revive." + scene.Recovery + ".available")) return false;
            if (state.Has(relationship.ClosedFlag) && scene.Recovery != "konomi" && scene.AfterRecovery == null
                || relationship.UnavailableFlags.Any(flag => flag != recovery?.DeathFlag
                    && !(scene.AfterDeparture == "irabeth" && flag == "irabeth_gone") && Blocks(relationship, flag, state, scene))) return false;
            if (scene.Relationship == "tirabade")
            {
                if (!IsRemote(scene) && state.Chapter == 4) return false;
                if (scene.Owner == "Together" && state.Chapter >= 5 && (state.Has("irabeth_away") || state.Has("anevia_away"))) return false;
            }
            if (scene.AfterDeparture == "irabeth")
            {
                string? waitedFor = scene.Id == "irabeth.return_reply" ? "irabeth.return_request_sent"
                    : scene.Id == "irabeth.return_first_words" ? "irabeth.return_meeting_accepted" : null;
                if (waitedFor != null && (!state.Times.TryGetValue(waitedFor, out int requestedAt)
                    || requestedAt < 0 || (long)state.Hour - requestedAt < scene.DelayHours)) return false;
            }
            int last = scene.Requires.Concat(scene.RequiresAnyGroups.SelectMany(group => group).Where(state.Has))
                .Where(state.Times.ContainsKey).Select(k => state.Times[k]).DefaultIfEmpty(state.Hour - scene.DelayHours).Max();
            return state.Hour - last >= scene.DelayHours;
        }

        // A held Forbid blocks unless the scene's authored ForbidOverride for it is also held (E3: native keys too).
        public static bool ForbidHolds(Scene scene, string flag, Snapshot state) => state.Has(flag)
            && (!scene.ForbidOverrides.TryGetValue(flag, out var overrideFlag) || !state.Has(overrideFlag));

        // E2: a held UnavailableFlag blocks unless the relationship's authored return flag overrides it.
        // The device scene that performs the return necessarily Requires the overridable state itself; that
        // explicit requirement is the only other exemption, and only for flags the relationship declares overridable.
        public static bool Blocks(Relationship relationship, string flag, Snapshot state, Scene? scene = null) => state.Has(flag)
            && !(relationship.UnavailableOverrides.TryGetValue(flag, out var returned)
                && (state.Has(returned) || scene != null && scene.Requires.Contains(flag)));

        // Journal failure follows the same return: an overridden unavailable flag no longer fails the objective.
        public static bool Failed(Relationship relationship, Snapshot state) =>
            relationship.FailureFlags.Any(flag => Blocks(relationship, flag, state));

        // Remote conversations need live-state guards too, without reapplying authored closure or delays.
        public static bool ContactAvailable(Story story, Scene scene, Snapshot state)
        {
            if (scene.ContactUnit == null && (!IsRemote(scene) || scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal))) return true;
            var recovery = scene.Recovery == null ? null : story.Revivals[scene.Recovery];
            return (scene.ContactUnit == null || state.AvailableContacts.Contains(scene.ContactUnit))
                && scene.AdditionalContactUnits.All(state.AvailableContacts.Contains)
                && state.Chapter >= scene.MinChapter && state.Chapter <= scene.MaxChapter
                && (scene.Chapters.Length == 0 || scene.Chapters.Contains(state.Chapter))
                && (scene.Areas.Length == 0 || scene.Areas.Contains(state.Area))
                && scene.Requires.All(state.Has)
                && !scene.Forbids.Any(flag => IsNativeFlag(story, flag) && ForbidHolds(scene, flag, state))
                && !story.Relationships[scene.Relationship].UnavailableFlags.Any(flag => flag != recovery?.DeathFlag
                    && !(scene.AfterDeparture == "irabeth" && flag == "irabeth_gone") && Blocks(story.Relationships[scene.Relationship], flag, state, scene))
                && (scene.AfterDeparture == null || !state.Has(story.Relationships[scene.Relationship].ClosedFlag)
                    && !scene.Forbids.Any(state.Has))
                && (recovery == null || state.Has("revive." + scene.Recovery + ".available"))
                && (scene.RequiresAny.Length == 0 || scene.RequiresAny.Any(state.Has))
                && scene.RequiresAnyGroups.All(group => group.Any(state.Has));
        }

        public static IEnumerable<string> NativeKeys(Story story) => story.Etudes.Keys.Concat(story.CompletedEtudes.Keys)
            .Concat(story.CompletedQuests.Keys).Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys)
            .Concat(story.StartedDialogs.Keys);

        private static bool IsReservedKey(string key) => key.StartsWith(DegradedPrefix, StringComparison.Ordinal)
            || key.StartsWith(ServedPrefix, StringComparison.Ordinal) || key.StartsWith("hour.", StringComparison.Ordinal)
            || key.StartsWith("revive.", StringComparison.Ordinal);

        private static bool IsNativeFlag(Story story, string flag) => story.Etudes.ContainsKey(flag)
            || story.CompletedEtudes.ContainsKey(flag) || story.CompletedQuests.ContainsKey(flag)
            || story.SeenCues.ContainsKey(flag) || story.SelectedAnswers.ContainsKey(flag)
            || story.StartedDialogs.ContainsKey(flag)
            || flag == "inhuman" || flag == "ascended" || flag == "chapter_one" || flag == "chapter_later"
            || flag == "konomi.missed_contact_available" || flag == "konomi.missed_contact_invalidated"
            || flag == "konomi.retained_dead" || flag == "konomi.return_contact_available"
            || flag == "konomi.return_correspondence_available"
            || flag == "irabeth.return_correspondence_available" || flag == "irabeth.return_meeting_arrived"
            || flag == "nurah.correspondence_available" || flag == "nurah.meeting_arrived";

        // E1: latch keys whose source is observed in this snapshot but which are not recorded yet.
        public static string[] PendingLatches(Story story, Snapshot state) => story.Latches
            .Where(pair => !state.Has(pair.Key) && pair.Value.Any(state.Has)).Select(pair => pair.Key).ToArray();

        // Latches (then Story.Derived composites) complete a snapshot after every native reader has run.
        public static void Complete(Story story, Snapshot state)
        {
            foreach (var key in PendingLatches(story, state)) state.Flags.Add(key);
            // Validate guarantees an acyclic graph, so this reaches its fixed point in at most Derived.Count passes.
            for (bool changed = story.Derived.Count > 0; changed;)
            {
                changed = false;
                foreach (var pair in story.Derived)
                    if (!state.Has(pair.Key) && pair.Value.Any(group => group.All(state.Has)))
                    {
                        state.Flags.Add(pair.Key);
                        changed = true;
                    }
            }
        }

        // Build: a missing native input makes dependent composites unavailable too (like "loss").
        // A latch is only lost when every source is missing: one surviving source can still record it.
        public static void PropagateMissing(Story story, HashSet<string> missing)
        {
            foreach (var pair in story.Latches)
                if (pair.Value.All(missing.Contains)) missing.Add(pair.Key);
            for (bool changed = true; changed;)
            {
                changed = false;
                foreach (var pair in story.Derived)
                    if (!missing.Contains(pair.Key) && pair.Value.SelectMany(group => group).Any(missing.Contains))
                    {
                        missing.Add(pair.Key);
                        changed = true;
                    }
            }
        }

        public static bool IsRemote(Scene scene) => scene.Remote || scene.Owner == "Memory";

        public static Scene? NextRemote(Story story, Snapshot state) => story.Scenes
            .FirstOrDefault(scene => IsRemote(scene) && !scene.ManualOnly
                && !scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && Available(story, scene, state));

        // Fair rest delivery (GLOBAL-03): the relationship served least recently goes first, then the one whose
        // chapter window closes soonest; within a relationship, authored order is kept.
        public static Scene? NextRemote(Story story, Snapshot state, IReadOnlyDictionary<string, int> lastServedHour) => story.Scenes
            .Where(scene => IsRemote(scene) && !scene.ManualOnly
                && !scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && Available(story, scene, state))
            .GroupBy(scene => scene.Relationship)
            .OrderBy(group => lastServedHour.TryGetValue(group.Key, out int hour) ? hour : int.MinValue)
            .ThenBy(group => group.Min(scene => scene.MaxChapter))
            .Select(group => group.First()).FirstOrDefault();

        public const string ServedPrefix = "served.";


        public static string[] EntryTargets(Scene scene)
        {
            if (IsRemote(scene) || scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)) return Array.Empty<string>();
            if (scene.InteractionHub != null)
            {
                if (IsNurahHubScene(scene)) return Array.Empty<string>();
                throw new InvalidOperationException("Unrecognized authored interaction hub: " + scene.Id + "/" + scene.InteractionHub);
            }
            if (scene.AnswerLists.Length > 0) return scene.AnswerLists;
            if (scene.Relationship == "tirabade")
            {
                if (scene.Owner == "Anevia") return new[] { "33960c7f7af40cd43b7f801a76c87a0b" };
                if (scene.Owner == "Irabeth") return new[] { "871af36f2ab2b1f40b5de77976c54276" };
                if (scene.Owner == "Together") return new[] { "33960c7f7af40cd43b7f801a76c87a0b", "871af36f2ab2b1f40b5de77976c54276" };
            }
            throw new InvalidOperationException("No dialogue attachment points for " + scene.Id + " (" + scene.Owner + ").");
        }

        public static bool IsNurahHubScene(Scene scene) => scene.InteractionHub == "nurah.arrival"
            && scene.Relationship == "nurah" && scene.Owner == "Nurah" && !IsRemote(scene)
            && scene.ContactUnit == NurahContact && scene.AnswerLists.Length == 0
            && scene.Areas.SequenceEqual(new[] { NurahCapital })
            && scene.Chapters.SequenceEqual(new[] { 5 })
            && scene.Requires.Contains("nurah.meeting_accepted") && scene.Requires.Contains("nurah.meeting_arrived");

        public static void Validate(Story story)
        {
            if (story.Scenes.Count == 0) throw new InvalidOperationException("The route has no scenes.");
            foreach (var pair in story.CompletedQuests)
                if (string.IsNullOrWhiteSpace(pair.Key) || story.Etudes.ContainsKey(pair.Key) || !Guid.TryParseExact(pair.Value, "N", out _))
                    throw new InvalidOperationException("Invalid completed quest binding: " + pair.Key);
            var relationshipFlags = new HashSet<string>();
            foreach (var pair in story.Revivals)
                if (string.IsNullOrWhiteSpace(pair.Key) || !Guid.TryParseExact(pair.Value.Unit, "N", out _)
                    || !story.Relationships.ContainsKey(pair.Value.Relationship)
                    || (pair.Key == "konomi" ? pair.Value.Relationship != "konomi"
                        || pair.Value.Unit != "ca2d58c5c65723945857e04fb85d30ce" || pair.Value.DeathFlag != "konomi.retained_dead"
                        : !story.Etudes.ContainsKey(pair.Value.DeathFlag))
                    || !story.Relationships[pair.Value.Relationship].UnavailableFlags.Contains(pair.Value.DeathFlag))
                    throw new InvalidOperationException("Invalid revival binding: " + pair.Key);
            foreach (var pair in story.SeenCues)
                if (string.IsNullOrWhiteSpace(pair.Key) || story.Etudes.ContainsKey(pair.Key) || story.CompletedQuests.ContainsKey(pair.Key)
                    || pair.Value.Length == 0 || pair.Value.Any(id => !Guid.TryParseExact(id, "N", out _)))
                    throw new InvalidOperationException("Invalid seen-cue binding: " + pair.Key);
            foreach (var pair in story.Relationships)
            {
                if (string.IsNullOrWhiteSpace(pair.Key) || string.IsNullOrWhiteSpace(pair.Value.Title)) throw new InvalidOperationException("Unnamed relationship.");
                foreach (var flag in new[] { pair.Value.StartedFlag, pair.Value.ClosedFlag, pair.Value.CommittedFlag })
                    if (string.IsNullOrWhiteSpace(flag) || !relationshipFlags.Add(flag)) throw new InvalidOperationException("Empty or shared relationship state: " + pair.Key + "/" + flag);
            }
            var authoredFlags = new HashSet<string>(story.Scenes.Select(s => s.Id)
                .Concat(story.Scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set))
                .Concat(relationshipFlags));
            var derivedFlags = new HashSet<string>(new[] { "loss", "ascended", "inhuman", "chapter_one", "chapter_later",
                "konomi.missed_contact_available", "konomi.missed_contact_invalidated", "konomi.retained_dead", "konomi.return_contact_available", "konomi.return_correspondence_available",
                "irabeth.return_correspondence_available", "irabeth.return_meeting_arrived",
                "nurah.correspondence_available", "nurah.meeting_arrived" }
                .Concat(story.Revivals.Keys.Select(key => "revive." + key + ".available")));
            var contactEvidence = new HashSet<string>(new[] { "konomi.missed_contact_available", "konomi.missed_contact_invalidated",
                "konomi.retained_dead", "konomi.return_contact_available", "konomi.return_correspondence_available",
                "irabeth.return_correspondence_available", "irabeth.return_meeting_arrived",
                "nurah.correspondence_available", "nurah.meeting_arrived" });
            if (authoredFlags.Concat(story.Etudes.Keys).Concat(story.CompletedQuests.Keys).Concat(story.SeenCues.Keys)
                .Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).Concat(story.CompletedEtudes.Keys)
                .Any(flag => flag.StartsWith(DegradedPrefix, StringComparison.Ordinal) || flag.StartsWith(ServedPrefix, StringComparison.Ordinal)))
                throw new InvalidOperationException("The " + DegradedPrefix + " and " + ServedPrefix + " prefixes are reserved for runtime state.");
            if (authoredFlags.Any(contactEvidence.Contains)
                || story.Scenes.Any(scene => scene.Id == "konomi.retained_return_confirmed")
                || relationshipFlags.Contains("konomi.retained_return_confirmed")
                || story.Etudes.Keys.Concat(story.CompletedQuests.Keys).Concat(story.SeenCues.Keys)
                    .Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).Concat(story.CompletedEtudes.Keys)
                    .Any(key => contactEvidence.Contains(key) || key == "konomi.retained_return_confirmed"))
                throw new InvalidOperationException("Authored state or native aliases cannot manufacture contact evidence.");
            var nativeKeys = new HashSet<string>(NativeKeys(story));
            if (story.Latches == null) throw new InvalidOperationException("Latches cannot be null.");
            foreach (var pair in story.Latches)
                if (string.IsNullOrWhiteSpace(pair.Key) || authoredFlags.Contains(pair.Key) || nativeKeys.Contains(pair.Key)
                    || derivedFlags.Contains(pair.Key) || contactEvidence.Contains(pair.Key) || IsReservedKey(pair.Key)
                    || pair.Value == null || pair.Value.Length == 0 || pair.Value.Distinct().Count() != pair.Value.Length
                    || pair.Value.Any(source => !nativeKeys.Contains(source) && !derivedFlags.Contains(source)))
                    throw new InvalidOperationException("Invalid latch (sources must be native or runtime-derived keys; the key must be new): " + pair.Key);
            // A latch is an ordinary authored flag once recorded.
            authoredFlags.UnionWith(story.Latches.Keys);
            ValidateDerived(story, authoredFlags, nativeKeys, derivedFlags, contactEvidence);
            foreach (var pair in story.StartedDialogs)
                if (string.IsNullOrWhiteSpace(pair.Key) || !Guid.TryParseExact(pair.Value, "N", out _)
                    || story.Etudes.ContainsKey(pair.Key) || story.CompletedQuests.ContainsKey(pair.Key)
                    || story.SeenCues.ContainsKey(pair.Key) || story.SelectedAnswers.ContainsKey(pair.Key)
                    || story.CompletedEtudes.ContainsKey(pair.Key) || authoredFlags.Contains(pair.Key)
                    || derivedFlags.Contains(pair.Key) || pair.Key.StartsWith("hour.", StringComparison.Ordinal))
                    throw new InvalidOperationException("Invalid started-dialog binding: " + pair.Key);
            foreach (var pair in story.SelectedAnswers)
                if (string.IsNullOrWhiteSpace(pair.Key) || !Guid.TryParseExact(pair.Value, "N", out _)
                    || story.Etudes.ContainsKey(pair.Key) || story.CompletedQuests.ContainsKey(pair.Key)
                    || story.SeenCues.ContainsKey(pair.Key) || story.CompletedEtudes.ContainsKey(pair.Key)
                    || pair.Key.StartsWith("hour.", StringComparison.Ordinal) || authoredFlags.Contains(pair.Key) || derivedFlags.Contains(pair.Key))
                    throw new InvalidOperationException("Invalid selected-answer binding: " + pair.Key);
            foreach (var pair in story.CompletedEtudes)
                if (string.IsNullOrWhiteSpace(pair.Key) || !Guid.TryParseExact(pair.Value, "N", out _)
                    || story.Etudes.ContainsKey(pair.Key) || story.CompletedQuests.ContainsKey(pair.Key)
                    || story.SeenCues.ContainsKey(pair.Key) || pair.Key.StartsWith("hour.", StringComparison.Ordinal)
                    || authoredFlags.Contains(pair.Key) || derivedFlags.Contains(pair.Key))
                    throw new InvalidOperationException("Invalid completed-etude binding: " + pair.Key);
            foreach (var pair in story.Relationships)
            {
                if (pair.Value.UnavailableOverrides == null) throw new InvalidOperationException("UnavailableOverrides cannot be null: " + pair.Key);
                foreach (var entry in pair.Value.UnavailableOverrides)
                    if (!pair.Value.UnavailableFlags.Contains(entry.Key) || string.IsNullOrWhiteSpace(entry.Value) || entry.Key == entry.Value
                        || !authoredFlags.Contains(entry.Value) || story.Latches.ContainsKey(entry.Value) || nativeKeys.Contains(entry.Value)
                        || derivedFlags.Contains(entry.Value) || pair.Value.UnavailableFlags.Contains(entry.Value)
                        || story.Relationships.Values.Any(r => r.ClosedFlag == entry.Value))
                        throw new InvalidOperationException("Invalid unavailable override (key must be one of the relationship's UnavailableFlags, value an authored return flag): "
                            + pair.Key + "/" + entry.Key);
            }
            foreach (var key in story.PermanentEtudes)
                if (!story.Etudes.ContainsKey(key)) throw new InvalidOperationException("Unknown permanent etude: " + key);
            var ids = new HashSet<string>();
            foreach (var scene in story.Scenes)
            {
                if (scene.InteractionHub != null && !IsNurahHubScene(scene))
                    throw new InvalidOperationException("Invalid authored Nurah interaction-hub contract: " + scene.Id);
                if (scene.Relationship == "nurah" && !IsRemote(scene) && !IsNurahHubScene(scene))
                    throw new InvalidOperationException("Physical Nurah scenes require the authored arrival hub: " + scene.Id);
                if (scene.ManualOnly && !IsRemote(scene))
                    throw new InvalidOperationException("Manual-only delivery requires a remote scene: " + scene.Id);
                if (scene.NativeReturnCue != null && (!Guid.TryParseExact(scene.NativeReturnCue, "N", out _)
                    || IsRemote(scene) || scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                    || scene.ContactUnit != null || scene.InteractionHub != null || scene.AnswerLists.Length != 1
                    || scene.Nodes.SelectMany(node => node.Choices).Any(choice => choice.Revive != null)))
                    throw new InvalidOperationException("Invalid native audience return: " + scene.Id);
                // E3: the overridden key may be an authored flag or a native binding (never both, never runtime-derived
                // or a closure). The override value must be authored: never native, runtime-derived or a closure.
                foreach (var pair in scene.ForbidOverrides)
                    if (!scene.Forbids.Contains(pair.Key) || authoredFlags.Contains(pair.Key) == nativeKeys.Contains(pair.Key)
                        || !authoredFlags.Contains(pair.Value) && !story.Derived.ContainsKey(pair.Value) || pair.Key == pair.Value
                        || story.Relationships.Values.Any(r => r.ClosedFlag == pair.Key || r.ClosedFlag == pair.Value)
                        || nativeKeys.Contains(pair.Value) || derivedFlags.Contains(pair.Key) || derivedFlags.Contains(pair.Value))
                        throw new InvalidOperationException("Invalid authored forbid override: " + scene.Id + "/" + pair.Key);
                if (string.IsNullOrWhiteSpace(scene.Id) || !ids.Add(scene.Id)) throw new InvalidOperationException("Duplicate or empty scene: " + scene.Id);
                if (!story.Relationships.ContainsKey(scene.Relationship)) throw new InvalidOperationException("Unknown relationship: " + scene.Relationship);
                if (scene.ContactUnit != null && !Guid.TryParseExact(scene.ContactUnit, "N", out _))
                    throw new InvalidOperationException("Invalid native contact unit: " + scene.Id);
                if (scene.AdditionalContactUnits == null || scene.AdditionalContactUnits.Any(id => !Guid.TryParseExact(id, "N", out _))
                    || (scene.AdditionalContactUnits.Length > 0 && scene.ContactUnit == null)
                    || scene.AdditionalContactUnits.Concat(scene.ContactUnit == null ? Array.Empty<string>() : new[] { scene.ContactUnit })
                        .Distinct(StringComparer.OrdinalIgnoreCase).Count() != scene.AdditionalContactUnits.Length + (scene.ContactUnit == null ? 0 : 1))
                    throw new InvalidOperationException("Invalid additional native contact units: " + scene.Id);
                if (scene.RequiresAny.Any(string.IsNullOrWhiteSpace) || scene.RequiresAny.Distinct().Count() != scene.RequiresAny.Length)
                    throw new InvalidOperationException("Invalid alternative prerequisites: " + scene.Id);
                if (scene.RequiresAnyGroups == null || scene.RequiresAnyGroups.Any(group => group == null
                    || group.Length == 0 || group.Any(string.IsNullOrWhiteSpace) || group.Distinct().Count() != group.Length))
                    throw new InvalidOperationException("Invalid prerequisite groups: " + scene.Id);
                if (scene.Recovery != null && (!story.Revivals.TryGetValue(scene.Recovery, out var revival)
                    || revival.Relationship != scene.Relationship || !IsRemote(scene)))
                    throw new InvalidOperationException("Invalid recovery scene: " + scene.Id);
                if (scene.Recovery == "konomi" && (!scene.Requires.Contains("trickster") || !scene.Requires.Contains("konomi.retained_dead")))
                    throw new InvalidOperationException("Konomi's retained return requires Trickster power and current retained death: " + scene.Id);
                if (scene.Recovery == "konomi" && scene.Nodes.SelectMany(node => node.Choices).Count(choice => choice.Revive == "konomi") > 1)
                    throw new InvalidOperationException("Konomi's retained return requires one unambiguous terminal request per scene: " + scene.Id);
                if (scene.AfterRecovery != null && (scene.AfterRecovery != "konomi" || scene.Recovery != null
                    || !story.Revivals.ContainsKey("konomi") || scene.Relationship != "konomi"
                    || !scene.Requires.Contains("konomi.retained_return_confirmed")
                    || (scene.ContactUnit == null
                        ? !IsRemote(scene) || !scene.Requires.Contains("konomi.return_correspondence_available")
                        : scene.ContactUnit != "ca2d58c5c65723945857e04fb85d30ce" || !scene.Requires.Contains("konomi.return_contact_available"))))
                    throw new InvalidOperationException("Invalid retained-return aftermath: " + scene.Id);
                if (scene.AfterDeparture != null) ValidateDepartureVisit(story, scene);
                foreach (var target in EntryTargets(scene))
                    if (!Guid.TryParseExact(target, "N", out _)) throw new InvalidOperationException("Invalid dialogue attachment: " + scene.Id + "/" + target);
                foreach (var area in scene.Areas)
                    if (!Guid.TryParseExact(area, "N", out _)) throw new InvalidOperationException("Invalid scene area: " + scene.Id + "/" + area);
                if (scene.Chapters.Any(c => c < scene.MinChapter || c > scene.MaxChapter) || scene.Chapters.Distinct().Count() != scene.Chapters.Length || scene.DelayHours < 0)
                    throw new InvalidOperationException("Invalid chapter or timing constraints: " + scene.Id);
                if (scene.Nodes.Count == 0 || scene.MinChapter > scene.MaxChapter) throw new InvalidOperationException("Invalid scene: " + scene.Id);
                var nodes = new HashSet<string>();
                foreach (var node in scene.Nodes)
                    if (!nodes.Add(node.Id) || string.IsNullOrWhiteSpace(node.Text) || node.Choices.Count == 0) throw new InvalidOperationException("Invalid node: " + scene.Id + "/" + node.Id);
                foreach (var node in scene.Nodes)
                    foreach (var choice in node.Choices)
                    {
                        if (choice.Set.Any(contactEvidence.Contains))
                            throw new InvalidOperationException("Native contact observation cannot be authored: " + scene.Id);
                        if (choice.Revive == "konomi" && !choice.Set.SequenceEqual(new[] { "konomi.retained_return_confirmed" })
                            || choice.Set.Contains("konomi.retained_return_confirmed") && choice.Revive != "konomi")
                            throw new InvalidOperationException("Konomi restoration records only verified return, not relationship access: " + scene.Id);
                        if (choice.Next != null && !nodes.Contains(choice.Next)) throw new InvalidOperationException("Missing node: " + scene.Id + "/" + choice.Next);
                        if (choice.Check != null && (choice.Next != null || choice.Abort || choice.Revive != null
                            || scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                            || !CheckSkills.Contains(choice.Check.Skill) || choice.Check.DC <= 0
                            || choice.Check.Success == choice.Check.Failure
                            || !nodes.Contains(choice.Check.Success) || !nodes.Contains(choice.Check.Failure)))
                            throw new InvalidOperationException("Invalid skill check: " + scene.Id + "/" + node.Id);
                        if (choice.Revive != null && (choice.Revive != scene.Recovery || choice.Next != null || choice.Abort))
                            throw new InvalidOperationException("Revival must be a terminal recovery choice: " + scene.Id);
                        ValidateNativeEffects(scene, node, choice);
                    }
                var reached = new HashSet<string>();
                var pending = new Stack<string>();
                pending.Push(scene.Nodes[0].Id);
                while (pending.Count > 0)
                {
                    var id = pending.Pop();
                    if (!reached.Add(id)) continue;
                    foreach (var choice in scene.Nodes.Single(n => n.Id == id).Choices)
                        foreach (var next in NextNodes(choice)) pending.Push(next);
                }
                if (reached.Count != nodes.Count) throw new InvalidOperationException("Unreachable node in " + scene.Id);
            }
            ValidateParentEndings(story, authoredFlags, derivedFlags);
        }

        // E5: native answer effects are whitelisted and shaped like their native counterparts.
        private static void ValidateNativeEffects(Scene scene, Node node, Choice choice)
        {
            bool ending = scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal);
            if (choice.Mythic != null && (ending || !MythicNames.Contains(choice.Mythic)))
                throw new InvalidOperationException("Invalid mythic requirement: " + scene.Id + "/" + node.Id + " (" + choice.Mythic + ")");
            if (choice.Alignment != null && (ending || !AlignmentDirections.Contains(choice.Alignment.Direction)
                || choice.Alignment.Value <= 0 || choice.Alignment.Value > 100))
                throw new InvalidOperationException("Invalid alignment shift: " + scene.Id + "/" + node.Id);
            // Only an inline scene runs inside the native dialog, so only it can continue into that dialog's own cue.
            if (choice.NativeNext != null && (!Guid.TryParseExact(choice.NativeNext, "N", out var cue) || cue == Guid.Empty
                || scene.NativeReturnCue == null || choice.Next != null || choice.Check != null || choice.Abort || choice.Revive != null
                || string.Equals(choice.NativeNext, scene.NativeReturnCue, StringComparison.OrdinalIgnoreCase)))
                throw new InvalidOperationException("Invalid native continuation (terminal choice of an inline scene only): " + scene.Id + "/" + node.Id);
        }

        // E4: composite keys are new names over known flags, without cycles.
        private static void ValidateDerived(Story story, HashSet<string> authored, HashSet<string> native, HashSet<string> runtime, HashSet<string> evidence)
        {
            if (story.Derived == null) throw new InvalidOperationException("Derived cannot be null.");
            foreach (var pair in story.Derived)
            {
                if (string.IsNullOrWhiteSpace(pair.Key) || authored.Contains(pair.Key) || native.Contains(pair.Key) || runtime.Contains(pair.Key)
                    || evidence.Contains(pair.Key) || IsReservedKey(pair.Key))
                    throw new InvalidOperationException("Derived key collides with an authored, native or reserved key: " + pair.Key);
                if (pair.Value == null || pair.Value.Length == 0 || pair.Value.Any(group => group == null || group.Length == 0
                    || group.Any(string.IsNullOrWhiteSpace) || group.Distinct().Count() != group.Length))
                    throw new InvalidOperationException("Derived key needs non-empty AND-groups: " + pair.Key);
                foreach (var source in pair.Value.SelectMany(group => group))
                    if (!authored.Contains(source) && !native.Contains(source) && !runtime.Contains(source) && !story.Derived.ContainsKey(source))
                        throw new InvalidOperationException("Derived key reads an unknown flag: " + pair.Key + "/" + source);
            }
            var state = new Dictionary<string, int>();
            void Visit(string key, int depth)
            {
                if (state.TryGetValue(key, out int mark))
                {
                    if (mark == 1) throw new InvalidOperationException("Derived keys form a cycle through: " + key);
                    return;
                }
                state[key] = 1;
                foreach (var source in story.Derived[key].SelectMany(group => group).Where(story.Derived.ContainsKey)) Visit(source, depth + 1);
                state[key] = 2;
            }
            foreach (var key in story.Derived.Keys) Visit(key, 0);
        }

        // A personal visit does not reverse departure or reopen the ordinary relationship.
        private static void ValidateDepartureVisit(Story story, Scene scene)
        {
            bool first = scene.Id == "irabeth.return_first_words";
            bool reply = scene.Id == "irabeth.return_reply";
            if (scene.AfterDeparture != "irabeth" || (!first && !reply && scene.Id != "irabeth.return_request")
                || scene.Relationship != "irabeth" || scene.Owner != "Irabeth"
                || scene.Recovery != null || scene.AfterRecovery != null
                || scene.MinChapter != 5 || scene.MaxChapter != 5
                || !scene.Areas.SequenceEqual(new[] { "2570015799edf594daf2f076f2f975d8" })
                || !new[] { "trickster", "irabeth_gone" }.All(scene.Requires.Contains)
                || !new[] { "closed", "irabeth.closed", "irabeth.return_meeting_declined", "irabeth_dead", "inhuman", "swarm", "true_lich" }.All(scene.Forbids.Contains)
                || scene.ForbidOverrides.Count != 0 || scene.AdditionalContactUnits.Length != 0
                || scene.Nodes.SelectMany(node => node.Choices).SelectMany(choice => choice.Set)
                    .Any(flag => !flag.StartsWith("irabeth.return_", StringComparison.Ordinal) || IsNativeFlag(story, flag))
                || (first
                    ? IsRemote(scene) || scene.ContactUnit != "280d4712dceb37f4a88e98f1f4c6e64f"
                        || !scene.AnswerLists.SequenceEqual(new[] { "871af36f2ab2b1f40b5de77976c54276" })
                        || !new[] { "irabeth.return_reply", "irabeth.return_meeting_accepted", "irabeth.return_meeting_arrived" }.All(scene.Requires.Contains)
                        || scene.DelayHours < 12
                    : !IsRemote(scene) || scene.ContactUnit != null || scene.AnswerLists.Length != 0
                        || !scene.Requires.Contains("irabeth.return_correspondence_available")
                        || (reply && (!new[] { "irabeth.return_request", "irabeth.return_request_sent" }.All(scene.Requires.Contains)
                            || !scene.Forbids.Contains("irabeth.return_meeting_accepted") || scene.DelayHours < 48))))
                throw new InvalidOperationException("Invalid Irabeth departure visit: " + scene.Id);
        }

        private static void ValidateParentEndings(Story story, HashSet<string> authored, HashSet<string> derived)
        {
            if (story.ParentEpilogueEdits == null || story.ParentEpilogueLossRules == null)
                throw new InvalidOperationException("Parent ending collections cannot be null.");
            if (story.ParentEpilogueEdits.Count == 0 && story.ParentEpilogueLossRules.Count == 0) return;
            var deaths = new Dictionary<string, string> {
                ["minagho.dead"] = "3b8c0801d5e9a694b848ee13564d2ad7", ["chivarro.dead"] = "fd2ab9b67ce3e284184b1894c82c6c5d" };
            var nativeKeys = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
                .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).ToArray();
            var nativeBindings = story.Etudes.Concat(story.CompletedEtudes).Concat(story.CompletedQuests)
                .Concat(story.SelectedAnswers).Concat(story.StartedDialogs)
                .Concat(story.SeenCues.SelectMany(pair => pair.Value.Select(id => new KeyValuePair<string, string>(pair.Key, id))))
                .ToLookup(pair => pair.Key, pair => pair.Value);
            var known = new HashSet<string>(authored.Concat(derived).Concat(nativeKeys));
            foreach (string earned in new[] { "minachiv.invitation_kept", "minachiv.arrival_kept" })
                if (!authored.Contains(earned) || nativeKeys.Contains(earned) || derived.Contains(earned))
                    throw new InvalidOperationException("Parent endings require authored relationship evidence: " + earned);
            bool GuidValid(string value) => Guid.TryParseExact(value, "N", out var guid) && guid != Guid.Empty && value == guid.ToString("N");
            bool NamesValid(string[]? values) => values != null && !values.Any(string.IsNullOrWhiteSpace)
                && values.Distinct(StringComparer.Ordinal).Count() == values.Length;
            bool TargetsValid(string[]? values) => NamesValid(values) && values!.All(GuidValid);
            foreach (var death in deaths)
                if (!story.Etudes.TryGetValue(death.Key, out var guid) || guid != death.Value || authored.Contains(death.Key)
                    || nativeKeys.Count(key => key == death.Key) != 1)
                    throw new InvalidOperationException("Parent endings require the exact native death observation: " + death.Key);
            void Gate(string owner, string[] requires, string[] forbids)
            {
                if (owner != "Epilogue" || !NamesValid(requires) || !NamesValid(forbids)
                    || requires.Intersect(forbids).Any() || requires.Concat(forbids).Any(flag => !known.Contains(flag)
                        || nativeBindings[flag].Any(id => !GuidValid(id)) || nativeKeys.Count(key => key == flag) > 1
                        || authored.Contains(flag) && nativeKeys.Contains(flag)))
                    throw new InvalidOperationException("Invalid parent ending owner or flag aliases.");
            }
            var privateKeys = new HashSet<string>(StringComparer.Ordinal);
            var parentKeys = new HashSet<string>(story.ParentEpilogueEdits.Values.Where(edit => edit != null).Select(edit => edit.ParentKey));
            void Text(ParentEndingText value, string expectedKey, bool suppressible)
            {
                if (value == null || value.LocalizedKey != expectedKey || parentKeys.Contains(value.LocalizedKey)
                    || !privateKeys.Add(value.LocalizedKey) || (value.Text == null ? !suppressible : string.IsNullOrWhiteSpace(value.Text)))
                    throw new InvalidOperationException("Parent ending alternate needs unique private localization and valid text.");
            }
            var reunions = new[] { "c47829fba057400c8e0279990be3d25e", "8399dbc5987b462594b2b4168764e269", "5787f92575364c1459df8f075676c2db" };
            foreach (var pair in story.ParentEpilogueEdits)
            {
                var edit = pair.Value;
                if (!GuidValid(pair.Key) || edit == null || string.IsNullOrWhiteSpace(edit.ParentKey))
                    throw new InvalidOperationException("Invalid parent cue identity or original text key.");
                Gate(edit.Owner, edit.Requires, edit.Forbids);
                if (!deaths.Keys.All(edit.Forbids.Contains)
                    || !edit.Requires.Contains(reunions.Contains(pair.Key) ? "minachiv.arrival_kept" : "minachiv.invitation_kept"))
                    throw new InvalidOperationException("Ordinary parent edit lacks earned living-history scope: " + pair.Key);
                Text(edit, "Tirabade.Minachiv.ParentEnding." + pair.Key, true);
            }
            var ids = new HashSet<string>(StringComparer.Ordinal);
            foreach (var rule in story.ParentEpilogueLossRules)
            {
                if (rule == null || string.IsNullOrWhiteSpace(rule.Id) || !ids.Add(rule.Id))
                    throw new InvalidOperationException("Empty or duplicate parent loss rule.");
                Gate(rule.Owner, rule.Requires, rule.Forbids);
                if (!rule.Requires.Contains("minachiv.invitation_kept") || !deaths.Keys.Any(rule.Requires.Contains)
                    || !deaths.Keys.All(flag => rule.Requires.Contains(flag) || rule.Forbids.Contains(flag))
                    || !NamesValid(rule.ReplacementScenes) || rule.ReplacementScenes.Length == 0
                    || !TargetsValid(rule.SuppressPages) || !TargetsValid(rule.SuppressCues)
                    || rule.SuppressPages.Intersect(rule.SuppressCues).Any() || rule.SuppressPages.Length + rule.SuppressCues.Length == 0
                    || rule.SurvivorAlternates == null)
                    throw new InvalidOperationException("Invalid parent loss evidence or suppression targets: " + rule.Id);
                foreach (string id in rule.ReplacementScenes)
                {
                    var scene = story.Scenes.SingleOrDefault(item => item.Id == id);
                    if (scene == null || scene.Owner != rule.Owner || scene.Relationship != "minagho_chivarro"
                        || !deaths.Keys.Where(rule.Requires.Contains).All(scene.Requires.Contains)
                        || !deaths.Keys.Where(rule.Forbids.Contains).All(scene.Forbids.Contains))
                        throw new InvalidOperationException("Missing or incompatible parent loss replacement: " + id);
                }
                foreach (var pair in rule.SurvivorAlternates)
                {
                    if (!GuidValid(pair.Key) || !rule.SuppressCues.Contains(pair.Key) || deaths.Keys.Count(rule.Requires.Contains) != 1)
                        throw new InvalidOperationException("Survivor alternate must replace a suppressed cue with one living woman: " + pair.Key);
                    Text(pair.Value, "Tirabade.Minachiv.Survivor." + pair.Key, false);
                }
            }
            for (int i = 0; i < story.ParentEpilogueLossRules.Count; i++)
                foreach (var other in story.ParentEpilogueLossRules.Skip(i + 1))
                {
                    var rule = story.ParentEpilogueLossRules[i];
                    if (rule.Owner == other.Owner && !rule.Requires.Intersect(other.Forbids).Any() && !other.Requires.Intersect(rule.Forbids).Any())
                        throw new InvalidOperationException("Overlapping parent loss rules: " + rule.Id + "/" + other.Id);
                }
        }
    }
}
