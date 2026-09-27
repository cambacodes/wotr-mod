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
        // E10 read-only native readers: a BlueprintUnlockableFlag with value > 0; a quest objective in the named state
        // ([guid, "Started"|"Completed"|"Failed"]); an item in the party inventory or the shared stash; ER-5: a quest
        // that is Started or Completed.
        public Dictionary<string, string> UnlockableFlags = new Dictionary<string, string>();
        public Dictionary<string, string[]> QuestObjectives = new Dictionary<string, string[]>();
        public Dictionary<string, string> InventoryItems = new Dictionary<string, string>();
        public Dictionary<string, string> StartedQuests = new Dictionary<string, string>();
        public Dictionary<string, Revival> Revivals = new Dictionary<string, Revival>();
        public Dictionary<string, ParentEndingEdit> ParentEpilogueEdits = new Dictionary<string, ParentEndingEdit>();
        public List<ParentEndingLossRule> ParentEpilogueLossRules = new List<ParentEndingLossRule>();
        public string[] PermanentEtudes = Array.Empty<string>();
        // E12 (GLOBAL-07-lite): returned presences, keyed "<relationship>.presence".
        public Dictionary<string, Presence> Presences = new Dictionary<string, Presence>();
        // E14d: reviewed native epilogue cues replaced by an RRT epilogue scene's text when an earned condition holds.
        public Dictionary<string, NativeEpilogueEditSpec> NativeEpilogueEdits = new Dictionary<string, NativeEpilogueEditSpec>();
        // E11: the only items a choice may remove (Choice.RemoveItem), each a native BlueprintItem GUID.
        public string[] RemovableItems = Array.Empty<string>();
        // E1: authored flags recorded forever the first time any native/derived source key is observed (TT-02).
        public Dictionary<string, string[]> Latches = new Dictionary<string, string[]>();
        // E4: data-driven composite flags, an OR of AND-groups over any known flag, computed in State() after latches.
        public Dictionary<string, string[][]> Derived = new Dictionary<string, string[][]>();
        // E8 (TT-09, ER-4): a successful rest delivers up to PostBagSize letters, at most one per rotation key, and a
        // relationship never holds more than QueueCapPerRelationship undelivered letters.
        public int PostBagSize = 3;
        public int QueueCapPerRelationship = 2;
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
        // E7: authoring metadata for the verifier (TT-20). Opaque to the runtime; only its shape is validated.
        public Dictionary<string, TricksterAccess> TricksterAccess = new Dictionary<string, TricksterAccess>();
        // ER-4: relationships sharing a rotation key (e.g. nocticula and nocticula.acquisition) share one post-bag slot.
        public string? RotationKey;
    }

    // E12: a character made present in an area while Requires hold and no Forbid holds. "reuse-native" unhides and
    // (optionally) moves the existing native unit when it exists alive and friendly; "spawn-copy" spawns one copy of the
    // native blueprint at Position when no live unit of that blueprint is in the area, and removes it when unwanted.
    public sealed class Presence
    {
        public string Unit = "";
        public string Area = "";
        public string Mode = "reuse-native";
        public string[] Requires = Array.Empty<string>();
        public string[] Forbids = Array.Empty<string>();
        public int MinChapter = 1;
        public int MaxChapter = 6;
        public PresencePosition? Position;
        public string[] AnswerLists = Array.Empty<string>();
    }

    public sealed class PresencePosition
    {
        public float X, Y, Z;
        public float Orientation;
    }

    public enum PresenceStep { None, Unhide, Move, Hide, Spawn, Remove, Forget, Blocked }

    // What the runtime observed for one presence in the loaded area (pure input to Rules.PlanPresence).
    public sealed class PresenceObservation
    {
        public bool AreaLoaded;
        public bool NativeAlive;       // a live, friendly unit of the blueprint that is not our copy
        public bool NativeHidden;      // that unit is out of game (hidden by native state)
        public bool NativeAtPosition = true;
        public bool CopyFound;         // our recorded copy is in the area state
        public bool CopyAlive;
        public bool Recorded;          // a saved presence record exists
        public bool RecordedUnhide;    // the record says we unhid the native unit
        public bool Submitted;         // the record says a copy was spawned
    }

    public sealed class NativeEpilogueEditSpec
    {
        public string Page = "";
        public string Sequence = "";
        public string Key = "";
        public string Replacement = "";
        public string[][] When = Array.Empty<string[]>();
    }

    public sealed class TricksterAccess
    {
        public string[] Detect = Array.Empty<string>();
        public string? Device;
        public string? Returned;
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
        // E6: a one-node companion/NPC reaction to a Trickster device (story_format.reaction).
        public bool Reaction;
        // ER-2: a Trickster device scene is reachable while its relationship's detected unavailable state still holds
        // (before the return is recorded). TricksterState names the relationship's TricksterAccess entry; when omitted,
        // the entry whose Device is this scene is used, else every entry of the relationship.
        public bool TricksterDevice;
        public string? TricksterState;
        // ER-3: an epilogue page placed right after this native page or cue of its sequence (authored order among pages
        // sharing an anchor); appended as before when the anchor is not a member of the sequence.
        public string? EpilogueAfter;
        // E14a: an epilogue page placed in a native sequence instead of the RanRomance one ("PlayerFinalChoice").
        public string? EpilogueSequence;
        // E14b: an inline scene inside a native dialog whose list has no clean return cue. For each AnswerList the runtime builds
        // its own cue graph ending in an authored return cue (ReturnText) that shows that list again.
        public bool ReturnToList;
        public string? ReturnText;
        // E13: native effects on the scene's entry answer (the one injected into a native answer list), as E5 does for choices.
        public string? EntryMythic;
        public AlignmentChoice? EntryAlignment;
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
        // E14c: epilogue pages only. Conditional paragraphs appended after the node text, in order (the native BookPage idiom).
        public List<Paragraph> Paragraphs = new List<Paragraph>();
    }

    public sealed class Paragraph
    {
        public string Text = "";
        public string[] Requires = Array.Empty<string>();
        public string[] Forbids = Array.Empty<string>();
        public string[][] AnyGroups = Array.Empty<string[]>();
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
        // E11 native costs: a crusade resource change (native AddCrusadeResources / RemoveCrusadeResources) and the removal
        // of one whitelisted item (native RemoveItemFromPlayer, quantity 1).
        public CrusadeChoice? Crusade;
        public string? RemoveItem;
    }

    public sealed class CrusadeChoice
    {
        public string Resource = "";
        public int Amount;
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

    // E8: the undelivered letters of successive rests. Main starts the next one whenever no dialog is open, so a
    // finished RRT letter chains into the next (after the 2-frame UI delay in Main.Queue).
    public sealed class PostBag
    {
        public readonly List<Scene> Queue = new List<Scene>();

        public int Fill(Story story, Snapshot state, IReadOnlyDictionary<string, int> lastServedHour, int size)
        {
            var bag = Rules.NextRemoteBag(story, state, lastServedHour, size, Queue, Math.Max(1, story.QueueCapPerRelationship));
            Queue.AddRange(bag);
            return bag.Count;
        }

        // The next letter still deliverable now; letters that stopped being available are dropped.
        public Scene? Next(Story story, Snapshot state)
        {
            while (Queue.Count > 0)
            {
                var scene = Queue[0];
                Queue.RemoveAt(0);
                if (Rules.Available(story, scene, state)) return scene;
            }
            return null;
        }

        public void Clear() => Queue.Clear();
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

        // Kingmaker.Kingdom.KingdomResource minus None; KingdomResourcesAmount has m_Finances, m_Materials, m_Favors.
        public static readonly string[] CrusadeResources = { "Finances", "Materials", "Favors" };

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
        // ER-2: a TricksterDevice scene also ignores the unavailable flags its TricksterAccess state detects, and nothing else.
        public static bool Blocks(Relationship relationship, string flag, Snapshot state, Scene? scene = null) => state.Has(flag)
            && !(relationship.UnavailableOverrides.TryGetValue(flag, out var returned) && state.Has(returned))
            && !(scene != null && scene.TricksterDevice && DeviceDetects(relationship, scene).Contains(flag));

        // The unavailable flags a device scene is built to serve: its TricksterAccess state's detect keys ("!" = absent, ignored).
        public static IEnumerable<string> DeviceDetects(Relationship relationship, Scene scene)
        {
            IEnumerable<TricksterAccess> entries;
            if (scene.TricksterState != null)
                entries = relationship.TricksterAccess.TryGetValue(scene.TricksterState, out var named) ? new[] { named } : Array.Empty<TricksterAccess>();
            else
            {
                var own = relationship.TricksterAccess.Values.Where(entry => entry.Device == scene.Id).ToArray();
                entries = own.Length > 0 ? own : relationship.TricksterAccess.Values;
            }
            return entries.SelectMany(entry => entry.Detect).Where(key => !key.StartsWith("!", StringComparison.Ordinal))
                .Intersect(relationship.UnavailableFlags);
        }

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
            .Concat(story.StartedDialogs.Keys).Concat(ReaderKeys(story));

        // E10 reader kinds.
        public static IEnumerable<string> ReaderKeys(Story story) => story.UnlockableFlags.Keys.Concat(story.QuestObjectives.Keys)
            .Concat(story.InventoryItems.Keys).Concat(story.StartedQuests.Keys);

        public static readonly string[] ObjectiveStates = { "Started", "Completed", "Failed" };

        private static bool IsReservedKey(string key) => key.StartsWith(DegradedPrefix, StringComparison.Ordinal)
            || key.StartsWith(ServedPrefix, StringComparison.Ordinal) || key.StartsWith("hour.", StringComparison.Ordinal)
            || key.StartsWith("revive.", StringComparison.Ordinal);

        private static bool IsNativeFlag(Story story, string flag) => story.Etudes.ContainsKey(flag)
            || story.CompletedEtudes.ContainsKey(flag) || story.CompletedQuests.ContainsKey(flag)
            || story.SeenCues.ContainsKey(flag) || story.SelectedAnswers.ContainsKey(flag)
            || story.StartedDialogs.ContainsKey(flag) || story.UnlockableFlags.ContainsKey(flag) || story.QuestObjectives.ContainsKey(flag)
            || story.InventoryItems.ContainsKey(flag) || story.StartedQuests.ContainsKey(flag)
            || flag == "inhuman" || flag == "ascended" || flag == "chapter_one" || flag == "chapter_later"
            || flag == "konomi.missed_contact_available" || flag == "konomi.missed_contact_invalidated"
            || flag == "konomi.retained_dead" || flag == "konomi.retained_hostile" || flag == "konomi.return_contact_available"
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

        // E12: the presence is wanted in this snapshot (area, chapter window, Requires, Forbids).
        public static bool PresenceWanted(Presence presence, Snapshot state) => state.Area == presence.Area
            && state.Chapter >= presence.MinChapter && state.Chapter <= presence.MaxChapter
            && presence.Requires.All(state.Has) && !presence.Forbids.Any(state.Has);

        // E12: the steps the runtime takes for one presence. A spawned copy is never created twice for one record.
        public static PresenceStep[] PlanPresence(Presence presence, bool wanted, PresenceObservation seen)
        {
            if (!seen.AreaLoaded) return Array.Empty<PresenceStep>();
            var steps = new List<PresenceStep>();
            if (presence.Mode == "reuse-native")
            {
                if (wanted && seen.NativeAlive)
                {
                    if (seen.NativeHidden) steps.Add(PresenceStep.Unhide);
                    if (presence.Position != null && !seen.NativeAtPosition) steps.Add(PresenceStep.Move);
                }
                else if (!wanted && seen.RecordedUnhide && seen.NativeAlive && !seen.NativeHidden) steps.Add(PresenceStep.Hide);
                else if (!wanted && seen.Recorded) steps.Add(PresenceStep.Forget);
                return steps.ToArray();
            }
            if (wanted)
            {
                if (seen.CopyFound) { if (!seen.CopyAlive) steps.Add(PresenceStep.Blocked); }
                else if (seen.NativeAlive) { if (seen.Recorded) steps.Add(PresenceStep.Forget); }
                else if (seen.Submitted) steps.Add(PresenceStep.Blocked);
                else steps.Add(PresenceStep.Spawn);
            }
            else if (seen.CopyFound) steps.Add(PresenceStep.Remove);
            else if (seen.Recorded) steps.Add(PresenceStep.Forget);
            return steps.ToArray();
        }

        // E14a: native epilogue sequences a page may target, with the anchors (member pages) it may follow.
        public const string PlayerFinalChoice = "a3096e5b145badb448827a7336d86d02";
        public static readonly Dictionary<string, string[]> NativeEpilogueSequences = new Dictionary<string, string[]>
        {
            // CueSequence_PlayerFinalChoice: after BookPage_0147 (Trickster ending) or BookPage_0115 (Wound closed).
            ["PlayerFinalChoice"] = new[] { "fb42f8bd123bf1f40a448f6dbc66cbbe", "8f234537d0e0e504ba7fa281f02a3601" },
        };

        // E14c: a paragraph shows when its requires hold, no forbid holds and every any-group has a member.
        public static bool ParagraphVisible(Paragraph paragraph, Snapshot state) => paragraph.Requires.All(state.Has)
            && !paragraph.Forbids.Any(state.Has) && paragraph.AnyGroups.All(group => group.Any(state.Has));

        public static Paragraph[] VisibleParagraphs(Node node, Snapshot state) => node.Paragraphs.Where(p => ParagraphVisible(p, state)).ToArray();

        // A paragraph that every world satisfying the scene's own Requires shows (guards against an empty page).
        public static bool ParagraphAlwaysShown(Scene scene, Paragraph paragraph) => paragraph.Requires.All(scene.Requires.Contains)
            && !paragraph.Forbids.Any() && paragraph.AnyGroups.All(group => group.Any(scene.Requires.Contains));

        // E14d: an OR of AND-groups over the snapshot.
        public static bool WhenHolds(string[][] when, Snapshot state) => when.Any(group => group.All(state.Has));

        // E14d: scenes used as native-cue replacements are never attached as pages of their own.
        public static bool IsNativeReplacement(Story story, Scene scene) => story.NativeEpilogueEdits.Values.Any(edit => edit.Replacement == scene.Id);

        public static string RotationKey(Story story, string relationship) =>
            story.Relationships.TryGetValue(relationship, out var r) && !string.IsNullOrWhiteSpace(r.RotationKey) ? r.RotationKey! : relationship;

        // E8: one rest's post bag. Groups the deliverable letters by rotation key, takes the most urgent keys first (soonest
        // closing chapter window, then least recently served), one letter per key (its first in authored order), skips a
        // relationship that already holds `cap` undelivered letters, and returns the bag in story list order.
        public static List<Scene> NextRemoteBag(Story story, Snapshot state, IReadOnlyDictionary<string, int> lastServedHour,
            int size, IReadOnlyCollection<Scene>? queued = null, int cap = int.MaxValue)
        {
            queued ??= Array.Empty<Scene>();
            int Served(string relationship) => lastServedHour.TryGetValue(relationship, out int hour) ? hour : int.MinValue;
            var order = story.Scenes.Select((scene, index) => (scene, index)).ToDictionary(pair => pair.scene, pair => pair.index);
            return story.Scenes
                .Where(scene => IsRemote(scene) && !scene.ManualOnly && !scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                    && !queued.Contains(scene) && queued.Count(other => other.Relationship == scene.Relationship) < cap
                    && Available(story, scene, state))
                .GroupBy(scene => RotationKey(story, scene.Relationship))
                .OrderBy(group => group.Min(scene => scene.MaxChapter))
                .ThenBy(group => group.Max(scene => Served(scene.Relationship)))
                .Take(Math.Max(0, size))
                .Select(group => group.First())
                .OrderBy(scene => order[scene]).ToList();
        }


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
            if (story.UnlockableFlags == null || story.QuestObjectives == null || story.InventoryItems == null || story.StartedQuests == null)
                throw new InvalidOperationException("Native reader collections cannot be null.");
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
                "konomi.missed_contact_available", "konomi.missed_contact_invalidated", "konomi.retained_dead", "konomi.retained_hostile", "konomi.return_contact_available", "konomi.return_correspondence_available",
                "irabeth.return_correspondence_available", "irabeth.return_meeting_arrived",
                "nurah.correspondence_available", "nurah.meeting_arrived" }
                .Concat(story.Revivals.Keys.Select(key => "revive." + key + ".available")));
            var contactEvidence = new HashSet<string>(new[] { "konomi.missed_contact_available", "konomi.missed_contact_invalidated",
                "konomi.retained_dead", "konomi.retained_hostile", "konomi.return_contact_available", "konomi.return_correspondence_available",
                "irabeth.return_correspondence_available", "irabeth.return_meeting_arrived",
                "nurah.correspondence_available", "nurah.meeting_arrived" });
            if (authoredFlags.Concat(story.Etudes.Keys).Concat(story.CompletedQuests.Keys).Concat(story.SeenCues.Keys)
                .Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).Concat(story.CompletedEtudes.Keys).Concat(ReaderKeys(story))
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
            // E10: reader keys are new names, each bound once, to a well-formed GUID (and objective state).
            var others = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys).Concat(story.SeenCues.Keys)
                .Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).ToList();
            var readers = ReaderKeys(story).ToList();
            foreach (var key in readers)
            {
                string? guid = story.UnlockableFlags.TryGetValue(key, out var f) ? f : story.InventoryItems.TryGetValue(key, out var i) ? i
                    : story.StartedQuests.TryGetValue(key, out var q) ? q : story.QuestObjectives.TryGetValue(key, out var o) && o?.Length == 2
                        && ObjectiveStates.Contains(o[1]) ? o[0] : null;
                if (string.IsNullOrWhiteSpace(key) || guid == null || !Guid.TryParseExact(guid, "N", out var parsed) || parsed == Guid.Empty
                    || readers.Count(other => other == key) != 1 || others.Contains(key) || authoredFlags.Contains(key)
                    || derivedFlags.Contains(key) || contactEvidence.Contains(key) || IsReservedKey(key))
                    throw new InvalidOperationException("Invalid native reader binding: " + key);
            }
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
                    // ER-1: the value is an authored flag, a latch or a Story.Derived composite; never native or runtime-owned.
                    if (!pair.Value.UnavailableFlags.Contains(entry.Key) || string.IsNullOrWhiteSpace(entry.Value) || entry.Key == entry.Value
                        || !authoredFlags.Contains(entry.Value) && !story.Derived.ContainsKey(entry.Value) || nativeKeys.Contains(entry.Value)
                        || derivedFlags.Contains(entry.Value) || IsReservedKey(entry.Value) || pair.Value.UnavailableFlags.Contains(entry.Value)
                        || story.Relationships.Values.Any(r => r.ClosedFlag == entry.Value))
                        throw new InvalidOperationException("Invalid unavailable override (key must be one of the relationship's UnavailableFlags, value an authored return flag): "
                            + pair.Key + "/" + entry.Key);
            }
            foreach (var pair in story.Relationships)
                if (pair.Value.TricksterAccess == null || pair.Value.TricksterAccess.Any(access => string.IsNullOrWhiteSpace(access.Key)
                    || access.Value == null || access.Value.Detect == null || access.Value.Detect.Any(string.IsNullOrWhiteSpace)))
                    throw new InvalidOperationException("Malformed TricksterAccess metadata: " + pair.Key);
            if (story.PostBagSize < 1 || story.PostBagSize > 10 || story.QueueCapPerRelationship < 1
                || story.Relationships.Values.Any(r => r.RotationKey != null && string.IsNullOrWhiteSpace(r.RotationKey)))
                throw new InvalidOperationException("Invalid post-bag settings (PostBagSize 1-10, QueueCapPerRelationship >= 1, non-blank RotationKey).");
            ValidatePresences(story, authoredFlags, nativeKeys, derivedFlags);
            ValidateNativeEpilogueEdits(story, authoredFlags, nativeKeys, derivedFlags);
            if (story.RemovableItems == null || story.RemovableItems.Any(guid => !Guid.TryParseExact(guid, "N", out var item) || item == Guid.Empty)
                || story.RemovableItems.Distinct().Count() != story.RemovableItems.Length)
                throw new InvalidOperationException("RemovableItems must be distinct native item GUIDs.");
            foreach (var key in story.PermanentEtudes)
                if (!story.Etudes.ContainsKey(key)) throw new InvalidOperationException("Unknown permanent etude: " + key);
            var ids = new HashSet<string>();
            foreach (var scene in story.Scenes)
            {
                if (scene.InteractionHub != null && !IsNurahHubScene(scene))
                    throw new InvalidOperationException("Invalid authored Nurah interaction-hub contract: " + scene.Id);
                // E13: a Trickster device may meet Nurah physically on explicit native lists (prison, pardon, Camellia).
                if (scene.Relationship == "nurah" && !IsRemote(scene) && !IsNurahHubScene(scene)
                    && !(scene.TricksterDevice && scene.InteractionHub == null && scene.AnswerLists.Length > 0))
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
                        || !authoredFlags.Contains(pair.Value) && !story.Derived.ContainsKey(pair.Value) || IsReservedKey(pair.Value) || pair.Key == pair.Value
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
                if (scene.Reaction) ValidateReaction(story, scene);
                if (scene.TricksterDevice || scene.TricksterState != null) ValidateDevice(story, scene);
                if ((scene.EntryMythic != null || scene.EntryAlignment != null) && (IsRemote(scene) || scene.InteractionHub != null
                    || scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                    || scene.EntryMythic != null && !MythicNames.Contains(scene.EntryMythic)
                    || scene.EntryAlignment != null && (!AlignmentDirections.Contains(scene.EntryAlignment.Direction)
                        || scene.EntryAlignment.Value <= 0 || scene.EntryAlignment.Value > 100)))
                    throw new InvalidOperationException("Invalid entry mythic/alignment (physical entry answers only; Mythic and AlignmentShiftDirection names): " + scene.Id);
                if (scene.ReturnToList && (scene.NativeReturnCue != null || IsRemote(scene) || scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                    || scene.ContactUnit != null || scene.InteractionHub != null || scene.Recovery != null || scene.AnswerLists.Length == 0
                    || scene.AnswerLists.Distinct().Count() != scene.AnswerLists.Length
                    || (scene.ReturnText ?? "").Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries).Length > 25
                    || scene.Nodes.SelectMany(node => node.Choices).Any(choice => choice.Check != null || choice.NativeNext != null || choice.Revive != null))
                    || !scene.ReturnToList && scene.ReturnText != null)
                    throw new InvalidOperationException("Invalid return-to-list scene (physical, explicit AnswerLists, no NativeReturnCue/ContactUnit/"
                        + "hub, ReturnText <= 25 words, no check/native_next/revive choices): " + scene.Id);
                if (scene.EpilogueSequence != null && (!NativeEpilogueSequences.TryGetValue(scene.EpilogueSequence, out var anchors)
                    || !scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal) || scene.Owner == "AeonEpilogue"
                    || scene.EpilogueAfter == null || !anchors.Contains(scene.EpilogueAfter)))
                    throw new InvalidOperationException("Invalid native epilogue sequence (PlayerFinalChoice, non-Aeon epilogue page, anchored after "
                        + "BookPage_0147 or BookPage_0115): " + scene.Id);
                if (scene.EpilogueAfter != null && (!scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                    || !Guid.TryParseExact(scene.EpilogueAfter, "N", out var anchor) || anchor == Guid.Empty))
                    throw new InvalidOperationException("EpilogueAfter needs an epilogue page and a native page or cue GUID: " + scene.Id);
                foreach (var target in EntryTargets(scene))
                    if (!Guid.TryParseExact(target, "N", out _)) throw new InvalidOperationException("Invalid dialogue attachment: " + scene.Id + "/" + target);
                foreach (var area in scene.Areas)
                    if (!Guid.TryParseExact(area, "N", out _)) throw new InvalidOperationException("Invalid scene area: " + scene.Id + "/" + area);
                if (scene.Chapters.Any(c => c < scene.MinChapter || c > scene.MaxChapter) || scene.Chapters.Distinct().Count() != scene.Chapters.Length || scene.DelayHours < 0)
                    throw new InvalidOperationException("Invalid chapter or timing constraints: " + scene.Id);
                if (scene.Nodes.Count == 0 || scene.MinChapter > scene.MaxChapter) throw new InvalidOperationException("Invalid scene: " + scene.Id);
                var nodes = new HashSet<string>();
                foreach (var node in scene.Nodes)
                {
                    if (node.Paragraphs == null) throw new InvalidOperationException("Paragraphs cannot be null: " + scene.Id + "/" + node.Id);
                    bool paragraphs = node.Paragraphs.Count > 0;
                    if (paragraphs && (!scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                        || node.Paragraphs.Any(p => p == null || string.IsNullOrWhiteSpace(p.Text) || p.Requires == null || p.Forbids == null
                            || p.AnyGroups == null || p.AnyGroups.Any(g => g == null || g.Length == 0))
                        || string.IsNullOrWhiteSpace(node.Text) && !node.Paragraphs.Any(p => ParagraphAlwaysShown(scene, p))))
                        throw new InvalidOperationException("Invalid paragraphs (epilogue pages only; a textless node needs a paragraph its scene's Requires always show): "
                            + scene.Id + "/" + node.Id);
                    if (!nodes.Add(node.Id) || string.IsNullOrWhiteSpace(node.Text) && !paragraphs || node.Choices.Count == 0)
                        throw new InvalidOperationException("Invalid node: " + scene.Id + "/" + node.Id);
                }
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
                        ValidateNativeEffects(story, scene, node, choice);
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

        // E12: presences name a relationship, a native unit and area, a mode, known gates and (for copies) a position.
        private static void ValidatePresences(Story story, HashSet<string> authored, HashSet<string> native, HashSet<string> runtime)
        {
            if (story.Presences == null) throw new InvalidOperationException("Presences cannot be null.");
            bool Known(string flag) => authored.Contains(flag) || native.Contains(flag) || runtime.Contains(flag) || story.Derived.ContainsKey(flag);
            bool GuidOk(string? value) => value != null && Guid.TryParseExact(value, "N", out var guid) && guid != Guid.Empty;
            foreach (var pair in story.Presences)
            {
                var p = pair.Value;
                string relationship = pair.Key.EndsWith(".presence", StringComparison.Ordinal) ? pair.Key.Substring(0, pair.Key.Length - ".presence".Length) : "";
                if (p == null || !story.Relationships.ContainsKey(relationship) || !GuidOk(p.Unit) || !GuidOk(p.Area)
                    || p.Mode != "reuse-native" && p.Mode != "spawn-copy" || p.Requires == null || p.Forbids == null || p.AnswerLists == null
                    || p.Mode == "spawn-copy" && (p.Position == null || p.Requires.Length == 0)
                    || p.MinChapter < 1 || p.MaxChapter > 6 || p.MinChapter > p.MaxChapter
                    || p.Requires.Concat(p.Forbids).Any(flag => !Known(flag)) || p.Requires.Intersect(p.Forbids).Any()
                    || p.AnswerLists.Any(id => !GuidOk(id))
                    || story.Presences.Any(other => other.Key != pair.Key && other.Value?.Unit == p.Unit && other.Value.Area == p.Area))
                    throw new InvalidOperationException("Invalid presence (\"<relationship>.presence\", unit and area GUIDs, reuse-native|spawn-copy, "
                        + "known gates, spawn-copy needs Position and Requires): " + pair.Key);
            }
        }

        // E14d: each edit names a whitelisted cue with its exact evidence, a 1-node epilogue replacement scene, and When groups
        // that each require the replacement relationship's CommittedFlag.
        private static void ValidateNativeEpilogueEdits(Story story, HashSet<string> authored, HashSet<string> native, HashSet<string> runtime)
        {
            if (story.NativeEpilogueEdits == null) throw new InvalidOperationException("NativeEpilogueEdits cannot be null.");
            bool Known(string flag) => authored.Contains(flag) || native.Contains(flag) || runtime.Contains(flag) || story.Derived.ContainsKey(flag);
            foreach (var pair in story.NativeEpilogueEdits)
            {
                var edit = pair.Value;
                var scene = story.Scenes.FirstOrDefault(s => s.Id == edit?.Replacement);
                if (edit == null || !Guid.TryParseExact(pair.Key, "N", out _) || scene == null
                    || !scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal) || scene.Owner == "AeonEpilogue" || scene.Nodes.Count != 1
                    || string.IsNullOrWhiteSpace(scene.Nodes[0].Text) || scene.Nodes[0].Paragraphs.Count != 0 || scene.EpilogueSequence != null
                    || edit.When == null || edit.When.Length == 0 || edit.When.Any(g => g == null || g.Length == 0 || g.Any(f => !Known(f))
                        || !g.Contains(story.Relationships[scene.Relationship].CommittedFlag))
                    || story.NativeEpilogueEdits.Count(other => other.Value?.Replacement == edit.Replacement) != 1)
                    throw new InvalidOperationException("Invalid native epilogue edit (1-node epilogue replacement, known When groups that each "
                        + "require its relationship's CommittedFlag): " + pair.Key);
            }
        }

        // E6: a reaction is one node of terminal choices; it never closes, and never touches another relationship's state.
        private static void ValidateReaction(Story story, Scene scene)
        {
            var own = story.Relationships[scene.Relationship];
            var others = story.Relationships.Where(pair => pair.Key != scene.Relationship)
                .SelectMany(pair => new[] { pair.Value.StartedFlag, pair.Value.ClosedFlag, pair.Value.CommittedFlag }).ToArray();
            var choices = scene.Nodes.SelectMany(node => node.Choices).ToArray();
            if (scene.Nodes.Count != 1 || scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal) || scene.Recovery != null
                || scene.AfterRecovery != null || scene.AfterDeparture != null || scene.InteractionHub != null
                || !Rules.IsRemote(scene) && scene.AnswerLists.Length == 0
                || choices.Any(choice => choice.Next != null || choice.Check != null || choice.Revive != null || choice.NativeNext != null)
                || choices.SelectMany(choice => choice.Set).Any(flag => flag == own.ClosedFlag || others.Contains(flag))
                || scene.Forbids.Concat(choices.SelectMany(choice => choice.Forbids)).Any(others.Contains))
                throw new InvalidOperationException("Invalid reaction (one node; never closes or touches another relationship): " + scene.Id);
        }

        // ER-2: a device scene needs the Trickster power (live for setups, latched for payoffs), declared access, and a
        // choice that records the device (the return, a primer or a cost).
        private static void ValidateDevice(Story story, Scene scene)
        {
            var relationship = story.Relationships[scene.Relationship];
            var records = new HashSet<string>(relationship.TricksterAccess.Values.Select(entry => entry.Returned).OfType<string>()
                .Concat(relationship.UnavailableOverrides.Values));
            bool Records(string flag) => records.Contains(flag) || flag.Contains(".trickster.primed")
                || flag.Contains(".trickster.returned") || flag.Contains(".trickster.cost.");
            if (!scene.TricksterDevice || relationship.TricksterAccess.Count == 0 || scene.Reaction
                || scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                || scene.TricksterState != null && !relationship.TricksterAccess.ContainsKey(scene.TricksterState)
                || !scene.Requires.Contains("trickster") && !scene.Requires.Contains("trickster.ever")
                || !scene.Nodes.SelectMany(node => node.Choices).SelectMany(choice => choice.Set).Any(Records))
                throw new InvalidOperationException("Invalid Trickster device (needs TricksterAccess, trickster or trickster.ever, "
                    + "and a choice setting the return, primed or cost flag): " + scene.Id);
        }

        // E5: native answer effects are whitelisted and shaped like their native counterparts.
        private static void ValidateNativeEffects(Story story, Scene scene, Node node, Choice choice)
        {
            // The crusade (KingdomState) exists from Chapter 3; a removal must be gated on holding that exact item.
            if (choice.Crusade != null && (scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal) || scene.MinChapter < 3
                || !CrusadeResources.Contains(choice.Crusade.Resource) || choice.Crusade.Amount == 0 || Math.Abs(choice.Crusade.Amount) > 100000))
                throw new InvalidOperationException("Invalid crusade cost (Finances/Materials/Favors, non-zero, Chapter 3+): " + scene.Id + "/" + node.Id);
            if (choice.RemoveItem != null && (scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                || !story.RemovableItems.Contains(choice.RemoveItem)
                || !choice.Requires.Concat(scene.Requires).Any(key => story.InventoryItems.TryGetValue(key, out var held) && held == choice.RemoveItem)))
                throw new InvalidOperationException("Invalid item removal (whitelisted in RemovableItems and gated on an InventoryItems key for it): "
                    + scene.Id + "/" + node.Id);
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
