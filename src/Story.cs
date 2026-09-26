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
        public string[] PermanentEtudes = Array.Empty<string>();
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
    }

    public sealed class Scene
    {
        public string Id = "";
        public string Title = "";
        public string Entry = "";
        public string Owner = "Anevia";
        public string Relationship = "tirabade";
        public string[] AnswerLists = Array.Empty<string>();
        public string[] Areas = Array.Empty<string>();
        public int[] Chapters = Array.Empty<int>();
        public bool Remote;
        public bool ManualOnly;
        public string? Recovery;
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
        public static readonly string[] CheckSkills = { "SkillAthletics", "SkillMobility", "SkillStealth", "SkillThievery", "SkillKnowledgeArcana", "SkillKnowledgeWorld", "SkillLoreNature", "SkillLoreReligion", "SkillPerception", "SkillUseMagicDevice", "CheckDiplomacy", "CheckBluff", "CheckIntimidate" };

        public static IEnumerable<string> NextNodes(Choice choice) => choice.Check != null
            ? new[] { choice.Check.Success, choice.Check.Failure }
            : choice.Next == null ? Array.Empty<string>() : new[] { choice.Next };

        public static bool Match(IEnumerable<string> requires, IEnumerable<string> forbids, Snapshot state) =>
            requires.All(state.Has) && !forbids.Any(state.Has);

        public static bool Available(Story story, Scene scene, Snapshot state)
        {
            if (state.Chapter < scene.MinChapter || state.Chapter > scene.MaxChapter || state.Has(scene.Id)) return false;
            if (scene.Chapters.Length > 0 && !scene.Chapters.Contains(state.Chapter)) return false;
            if (scene.Areas.Length > 0 && !scene.Areas.Contains(state.Area)) return false;
            if (!scene.Requires.All(state.Has) || scene.Forbids.Any(flag => state.Has(flag)
                && (!scene.ForbidOverrides.TryGetValue(flag, out var overrideFlag) || !state.Has(overrideFlag)))) return false;
            if (scene.RequiresAny.Length > 0 && !scene.RequiresAny.Any(state.Has)) return false;
            if (!scene.RequiresAnyGroups.All(group => group.Any(state.Has))) return false;
            if (!ContactAvailable(story, scene, state)) return false;
            if (scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)) return true;
            var relationship = story.Relationships[scene.Relationship];
            var recovery = scene.Recovery == null ? null : story.Revivals[scene.Recovery];
            if (recovery != null && !state.Has("revive." + scene.Recovery + ".available")) return false;
            if (state.Has(relationship.ClosedFlag) || relationship.UnavailableFlags.Any(flag => flag != recovery?.DeathFlag && state.Has(flag))) return false;
            if (scene.Relationship == "tirabade")
            {
                if (!IsRemote(scene) && state.Chapter == 4) return false;
                if (scene.Owner == "Together" && state.Chapter >= 5 && (state.Has("irabeth_away") || state.Has("anevia_away"))) return false;
            }
            int last = scene.Requires.Concat(scene.RequiresAnyGroups.SelectMany(group => group).Where(state.Has))
                .Where(state.Times.ContainsKey).Select(k => state.Times[k]).DefaultIfEmpty(state.Hour - scene.DelayHours).Max();
            return state.Hour - last >= scene.DelayHours;
        }

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
                && !scene.Forbids.Any(flag => IsNativeFlag(story, flag) && state.Has(flag))
                && !story.Relationships[scene.Relationship].UnavailableFlags.Any(flag => flag != recovery?.DeathFlag && state.Has(flag))
                && (recovery == null || state.Has("revive." + scene.Recovery + ".available"))
                && (scene.RequiresAny.Length == 0 || scene.RequiresAny.Any(state.Has))
                && scene.RequiresAnyGroups.All(group => group.Any(state.Has));
        }

        private static bool IsNativeFlag(Story story, string flag) => story.Etudes.ContainsKey(flag)
            || story.CompletedEtudes.ContainsKey(flag) || story.CompletedQuests.ContainsKey(flag)
            || story.SeenCues.ContainsKey(flag) || story.SelectedAnswers.ContainsKey(flag)
            || story.StartedDialogs.ContainsKey(flag)
            || flag == "inhuman" || flag == "ascended" || flag == "chapter_one" || flag == "chapter_later"
            || flag == "konomi.missed_contact_available" || flag == "konomi.missed_contact_invalidated";

        public static bool IsRemote(Scene scene) => scene.Remote || scene.Owner == "Memory";

        public static Scene? NextRemote(Story story, Snapshot state) => story.Scenes
            .FirstOrDefault(scene => IsRemote(scene) && !scene.ManualOnly && Available(story, scene, state));

        public static string[] EntryTargets(Scene scene)
        {
            if (IsRemote(scene) || scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)) return Array.Empty<string>();
            if (scene.AnswerLists.Length > 0) return scene.AnswerLists;
            if (scene.Relationship == "tirabade")
            {
                if (scene.Owner == "Anevia") return new[] { "33960c7f7af40cd43b7f801a76c87a0b" };
                if (scene.Owner == "Irabeth") return new[] { "871af36f2ab2b1f40b5de77976c54276" };
                if (scene.Owner == "Together") return new[] { "33960c7f7af40cd43b7f801a76c87a0b", "871af36f2ab2b1f40b5de77976c54276" };
            }
            throw new InvalidOperationException("No dialogue attachment points for " + scene.Id + " (" + scene.Owner + ").");
        }

        public static void Validate(Story story)
        {
            if (story.Scenes.Count == 0) throw new InvalidOperationException("The route has no scenes.");
            foreach (var pair in story.CompletedQuests)
                if (string.IsNullOrWhiteSpace(pair.Key) || story.Etudes.ContainsKey(pair.Key) || !Guid.TryParseExact(pair.Value, "N", out _))
                    throw new InvalidOperationException("Invalid completed quest binding: " + pair.Key);
            var relationshipFlags = new HashSet<string>();
            foreach (var pair in story.Revivals)
                if (string.IsNullOrWhiteSpace(pair.Key) || !Guid.TryParseExact(pair.Value.Unit, "N", out _)
                    || !story.Relationships.ContainsKey(pair.Value.Relationship) || !story.Etudes.ContainsKey(pair.Value.DeathFlag)
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
                "konomi.missed_contact_available", "konomi.missed_contact_invalidated" }
                .Concat(story.Revivals.Keys.Select(key => "revive." + key + ".available")));
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
            foreach (var key in story.PermanentEtudes)
                if (!story.Etudes.ContainsKey(key)) throw new InvalidOperationException("Unknown permanent etude: " + key);
            var ids = new HashSet<string>();
            foreach (var scene in story.Scenes)
            {
                if (scene.ManualOnly && !IsRemote(scene))
                    throw new InvalidOperationException("Manual-only delivery requires a remote scene: " + scene.Id);
                foreach (var pair in scene.ForbidOverrides)
                    if (!scene.Forbids.Contains(pair.Key) || !authoredFlags.Contains(pair.Key)
                        || !authoredFlags.Contains(pair.Value) || pair.Key == pair.Value
                        || story.Relationships.Values.Any(r => r.ClosedFlag == pair.Key)
                        || story.Etudes.ContainsKey(pair.Key) || story.CompletedQuests.ContainsKey(pair.Key)
                        || story.SeenCues.ContainsKey(pair.Key) || story.SelectedAnswers.ContainsKey(pair.Key)
                        || story.CompletedEtudes.ContainsKey(pair.Key) || story.StartedDialogs.ContainsKey(pair.Key) || derivedFlags.Contains(pair.Key))
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
                        if (choice.Set.Any(flag => flag == "konomi.missed_contact_available" || flag == "konomi.missed_contact_invalidated"))
                            throw new InvalidOperationException("Native contact observation cannot be authored: " + scene.Id);
                        if (choice.Next != null && !nodes.Contains(choice.Next)) throw new InvalidOperationException("Missing node: " + scene.Id + "/" + choice.Next);
                        if (choice.Check != null && (choice.Next != null || choice.Abort || choice.Revive != null
                            || scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                            || !CheckSkills.Contains(choice.Check.Skill) || choice.Check.DC <= 0
                            || choice.Check.Success == choice.Check.Failure
                            || !nodes.Contains(choice.Check.Success) || !nodes.Contains(choice.Check.Failure)))
                            throw new InvalidOperationException("Invalid skill check: " + scene.Id + "/" + node.Id);
                        if (choice.Revive != null && (choice.Revive != scene.Recovery || choice.Next != null || choice.Abort))
                            throw new InvalidOperationException("Revival must be a terminal recovery choice: " + scene.Id);
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
        }
    }
}
