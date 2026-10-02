using System;
using System.Collections.Generic;
using System.Linq;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;

namespace Tirabade
{
    // E14d: a reviewed native companion-epilogue cue is replaced by an RRT epilogue scene's text when an earned condition holds.
    // The original keeps its native checker, wrapped by ParentEndingGuard (shown only when the replacement does not apply);
    // the replacement is a registered RRT cue inserted right before it, shown only when the replacement applies AND the
    // original's own checker passes. Both read the same per-frame snapshot, so exactly one of them plays. When the mod is
    // disabled or uninitialized the replacement is hidden and the native cue plays.
    //
    // Why not ParentEndingAlternate: its selection is refreshed only inside ParentEndingIntegration's scoped page evaluation
    // (Harmony hooks on the parent's RanRomAdd pages). These native cues are ShowOnce false, have no actions, answers or
    // continuation, so two complementary conditions give the same one-of-two selection without new patches.
    public static class NativeEpilogueEdit
    {
        public readonly struct Evidence
        {
            public readonly string Page, Sequence, Key;
            internal Evidence(string page, string sequence, string key) { Page = page; Sequence = sequence; Key = key; }
        }

        // v1 whitelist, verified in blueprints.zip: companion pages in CueSequence_Companions, ShowOnce false, cues without
        // actions, answers, continuation or components.
        public const string Companions = "fec3b6f28610c8a48a239f148ed3ed60";
        public static readonly Dictionary<string, Evidence> Reviewed = new Dictionary<string, Evidence>
        {
            ["86bf0569a9029ae4b8c9d300a41e5739"] = new Evidence("223fd069ee25c784db2df011adbf10f8", Companions, "0dfe0435-8149-466d-bf0c-88d648651c3a"), // Wenduag Cue_0409
            ["36a07840d25540eeac6b1c6631196bcc"] = new Evidence("503164ff04ac64543ba42561ea9f970f", Companions, "af56e46e-7e82-4e22-9951-8ddc37dd015f"), // Camellia Cue_38_master
            ["78ae1bdc3b0824b4ca2ed618782f1faa"] = new Evidence("e83fff8e997db8e439bf12e09225696a", Companions, "411ef2f1-5168-455f-99b0-ca33960678c5"), // Arueshalae Cue_0461
            ["f76713034f4087a4f80495971c47ca7b"] = new Evidence("e83fff8e997db8e439bf12e09225696a", Companions, "fa1468ba-9679-4805-9dd4-c71997aa4e7f"), // Arueshalae Cue_0462 (NM1)
        };

        public sealed class Plan
        {
            internal string CueId = "";
            internal NativeEpilogueEditSpec Spec = null!;
            internal BlueprintCue Original = null!;
            internal BlueprintBookPage Page = null!;
            internal BlueprintCue Replacement = null!;
            public ConditionsChecker OriginalChecker = null!;
        }

        // Phase 1: the native evidence must match exactly, or the edit is refused (the caller degrades its relationship).
        public static string? Check(string cueId, NativeEpilogueEditSpec spec, Func<string, SimpleBlueprint?> resolve, BlueprintCueSequence? aeon)
        {
            if (!Reviewed.TryGetValue(cueId, out var evidence) || evidence.Page != spec.Page || evidence.Sequence != spec.Sequence || evidence.Key != spec.Key)
                return "not a reviewed native cue";
            if (!(resolve(cueId) is BlueprintCue cue)) return "cue missing";
            if (!(resolve(spec.Page) is BlueprintBookPage page)) return "page missing";
            if (!(resolve(spec.Sequence) is BlueprintCueSequence sequence)) return "sequence missing";
            if (cue.Text?.Key != spec.Key) return "cue text key changed (patch drift)";
            if (cue.ShowOnce || cue.ShowOnceCurrentDialog || cue.Conditions == null || cue.ComponentsArray.Length != 0
                || cue.OnShow?.Actions?.Length != 0 || cue.OnStop?.Actions?.Length != 0 || cue.Continue?.Cues?.Count != 0 || cue.Answers?.Count != 0)
                return "cue behavior differs from the reviewed policy";
            if (page.Cues.Count(reference => reference.Guid == cue.AssetGuid) != 1) return "cue is not exactly once on its page";
            if (sequence.Cues.Count(reference => reference.Guid == page.AssetGuid) != 1) return "page is not exactly once in its sequence";
            if (aeon != null && aeon.Cues.Any(reference => reference.Guid == page.AssetGuid)) return "page is in the Aeon sequence";
            return null;
        }

        // Phase 2 (registration): the replacement cue carries the native cue's presentation and a combined checker.
        public static Plan Prepare(string cueId, NativeEpilogueEditSpec spec, BlueprintCue original, BlueprintBookPage page, BlueprintCue replacement,
            Func<bool> replacementApplies)
        {
            replacement.Speaker = original.Speaker;
            replacement.TurnSpeaker = original.TurnSpeaker;
            replacement.ShowOnce = false;
            replacement.ShowOnceCurrentDialog = false;
            replacement.OnShow = new ActionList { Actions = Array.Empty<GameAction>() };
            replacement.OnStop = new ActionList { Actions = Array.Empty<GameAction>() };
            replacement.Continue = new Kingmaker.DialogSystem.CueSelection { Cues = new List<BlueprintCueBaseReference>() };
            replacement.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = new Condition[] {
                new Applies { Original = original.Conditions, ReplacementApplies = replacementApplies } } };
            return new Plan { CueId = cueId, Spec = spec, Original = original, Page = page, Replacement = replacement, OriginalChecker = original.Conditions };
        }

        // Phase 3: insert the replacement before the original and guard the original. Refuses if the page moved meanwhile.
        public static void Attach(Plan plan, BlueprintCueBaseReference replacementReference, Func<bool> replacementApplies)
        {
            int index = plan.Page.Cues.FindIndex(reference => reference.Guid == plan.Original.AssetGuid);
            if (index < 0 || plan.Page.Cues.Any(reference => reference.Guid == plan.Replacement.AssetGuid))
                throw new InvalidOperationException("Native epilogue page changed before attachment: " + plan.CueId);
            plan.Page.Cues.Insert(index, replacementReference);
            ParentEndingGuard.Attach(plan.Original, replacementApplies);
        }

        public sealed class Applies : Condition
        {
            internal ConditionsChecker? Original;
            internal Func<bool> ReplacementApplies = null!;
            internal Exception? LastObservationError { get; private set; }
            protected override string GetConditionCaption() => "Earned replacement of a native epilogue cue";
            protected override bool CheckCondition()
            {
                bool applies = false;
                LastObservationError = null;
                try { applies = ReplacementApplies(); }
                catch (Exception ex) { LastObservationError = ex; }
                return applies && (Original?.Check() ?? true);
            }
        }
    }
}
