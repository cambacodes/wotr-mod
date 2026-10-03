using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.ResourceLinks;

namespace Tirabade
{
    // E14d: a reviewed native epilogue cue is replaced by an RRT epilogue scene's text when an earned condition holds.
    // The original keeps its native checker, wrapped by ParentEndingGuard (shown only when no replacement applies);
    // each replacement is a registered RRT cue inserted right before it, shown only when it is the selected variant AND the
    // original's own checker passes. All read the same per-frame snapshot, so exactly one of them plays. When the mod is
    // disabled or uninitialized every replacement is hidden and the native cue plays.
    //
    // E14d extension (Cue_0311): one native cue may carry several ordered variants (the first attached variant whose When
    // holds is selected), a reviewed OnShow ChangeBookEventImage that a variant may keep, and a page outside
    // CueSequence_Companions. A refusal of a cue marked DegradeOnRefusal = false only skips the edit (the native cue plays);
    // it never disables a relationship.
    //
    // Why not ParentEndingAlternate: its selection is refreshed only inside ParentEndingIntegration's scoped page evaluation
    // (Harmony hooks on the parent's RanRomAdd pages). These native cues are ShowOnce false, have no answers or continuation,
    // so complementary conditions give the same one-of-N selection without new patches.
    public static class NativeEpilogueEdit
    {
        public readonly struct Evidence
        {
            public readonly string Page, Sequence, Key;
            public readonly string? Image;            // the reviewed OnShow ChangeBookEventImage asset, or null for no OnShow
            public readonly bool DegradeOnRefusal;     // false: a refusal skips the edit and warns, the native cue plays
            internal Evidence(string page, string sequence, string key, string? image = null, bool degradeOnRefusal = true)
            { Page = page; Sequence = sequence; Key = key; Image = image; DegradeOnRefusal = degradeOnRefusal; }
        }

        // Whitelist, verified in blueprints.zip: ShowOnce false, cues without OnStop, answers, continuation or components,
        // and OnShow empty or exactly the reviewed image action. Before adding a cue, check that the RanRomance parent never
        // mutates it (reference/canon-review/aranka-*.cs and the parent DLL's UTF-16 strings): Cue_0461 failed live because
        // the parent sets its Continue.
        public const string Companions = "fec3b6f28610c8a48a239f148ed3ed60";
        public const string Special = "f8d7f50e3bb88c143834d234c0b24474";   // CueSequence_Special (the Tirabade pair page)
        public static readonly Dictionary<string, Evidence> Reviewed = new Dictionary<string, Evidence>
        {
            ["86bf0569a9029ae4b8c9d300a41e5739"] = new Evidence("223fd069ee25c784db2df011adbf10f8", Companions, "0dfe0435-8149-466d-bf0c-88d648651c3a"), // Wenduag Cue_0409
            ["36a07840d25540eeac6b1c6631196bcc"] = new Evidence("503164ff04ac64543ba42561ea9f970f", Companions, "af56e46e-7e82-4e22-9951-8ddc37dd015f"), // Camellia Cue_38_master
            ["78ae1bdc3b0824b4ca2ed618782f1faa"] = new Evidence("e83fff8e997db8e439bf12e09225696a", Companions, "411ef2f1-5168-455f-99b0-ca33960678c5"), // Arueshalae Cue_0461
            ["f76713034f4087a4f80495971c47ca7b"] = new Evidence("e83fff8e997db8e439bf12e09225696a", Companions, "fa1468ba-9679-4805-9dd4-c71997aa4e7f"), // Arueshalae Cue_0462 (NM1)
            // Tirabade BookPage_0307 Cue_0311 (IrabethDead + AneviaGone Playing): "No one ever saw her again." Its OnShow swaps
            // the pair picture for f96ad5fa, as the other departure cue (Cue_0310) does. The parent never names the cue, its
            // page or CueSequence_Special.
            ["3a3e561c6b05a284d93eb3bff7b712a6"] = new Evidence("ae1f824fe248d9f4aac7d39ec2e12140", Special, "4c278ba4-5217-4fae-afec-47c6f6597e00",
                image: "f96ad5fa9c59d7549adff4c90f0703ab", degradeOnRefusal: false),
        };

        public static bool DegradesOnRefusal(string cueId) => !Reviewed.TryGetValue(cueId, out var evidence) || evidence.DegradeOnRefusal;

        public sealed class Plan
        {
            internal string CueId = "";
            internal NativeEpilogueEditSpec Spec = null!;
            internal int Variant;
            internal BlueprintCue Original = null!;
            internal BlueprintBookPage Page = null!;
            internal BlueprintCue Replacement = null!;
            public ConditionsChecker OriginalChecker = null!;
        }

        // The ordered variants of one native cue. The group selects nothing until Enable() (every variant attached), so a
        // partial attachment never hides the native cue or lets a later fallback variant stand in for an earlier one.
        public sealed class Group
        {
            private readonly NativeEpilogueVariant[] variants;
            private readonly Func<Snapshot?> observe;
            private bool enabled;
            public Group(NativeEpilogueEditSpec spec, Func<Snapshot?> observe)
            {
                variants = Rules.EditVariants(spec);
                this.observe = observe;
            }
            public int Count => variants.Length;
            public bool Enabled => enabled;
            public void Enable() => enabled = true;
            public int Selected()
            {
                if (!enabled) return -1;
                var state = observe();
                return state == null ? -1 : Rules.SelectNativeEditVariant(variants, state);
            }
        }

        private static readonly FieldInfo? ImageField = typeof(ChangeBookEventImage).GetField("m_Image",
            BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.Public);

        public static string? ImageOf(GameAction? action) => action is ChangeBookEventImage change
            ? (ImageField?.GetValue(change) as WeakResourceLink)?.AssetId : null;

        // Phase 1: the native evidence must match exactly, or the edit is refused (the caller degrades the relationships only
        // when the evidence says so; otherwise the native cue plays).
        public static string? Check(string cueId, NativeEpilogueEditSpec spec, Func<string, SimpleBlueprint?> resolve, BlueprintCueSequence? aeon)
        {
            if (!Reviewed.TryGetValue(cueId, out var evidence) || evidence.Page != spec.Page || evidence.Sequence != spec.Sequence || evidence.Key != spec.Key)
                return "not a reviewed native cue";
            if (evidence.Image == null && Rules.EditVariants(spec).Any(variant => variant.KeepNativeImage))
                return "a variant keeps a native image the reviewed cue does not have";
            if (!(resolve(cueId) is BlueprintCue cue)) return "cue missing";
            if (!(resolve(spec.Page) is BlueprintBookPage page)) return "page missing";
            if (!(resolve(spec.Sequence) is BlueprintCueSequence sequence)) return "sequence missing";
            if (cue.Text?.Key != spec.Key) return "cue text key changed (patch drift)";
            var onShow = cue.OnShow?.Actions;
            bool onShowReviewed = evidence.Image == null ? onShow?.Length == 0
                : onShow?.Length == 1 && ImageOf(onShow[0]) == evidence.Image;
            if (cue.ShowOnce || cue.ShowOnceCurrentDialog || cue.Conditions == null || cue.ComponentsArray.Length != 0
                || !onShowReviewed || cue.OnStop?.Actions?.Length != 0 || cue.Continue?.Cues?.Count != 0 || cue.Answers?.Count != 0)
                return "cue behavior differs from the reviewed policy";
            if (page.Cues.Count(reference => reference.Guid == cue.AssetGuid) != 1) return "cue is not exactly once on its page";
            if (sequence.Cues.Count(reference => reference.Guid == page.AssetGuid) != 1) return "page is not exactly once in its sequence";
            if (aeon != null && aeon.Cues.Any(reference => reference.Guid == page.AssetGuid)) return "page is in the Aeon sequence";
            return null;
        }

        // Phase 2 (registration): the replacement cue carries the native cue's presentation and a combined checker. A variant
        // that keeps the native image runs the native cue's own reviewed OnShow actions; any other shows the page's picture.
        public static Plan Prepare(string cueId, NativeEpilogueEditSpec spec, BlueprintCue original, BlueprintBookPage page, BlueprintCue replacement,
            Func<bool> replacementApplies, int variant = 0)
        {
            var variants = Rules.EditVariants(spec);
            replacement.Speaker = original.Speaker;
            replacement.TurnSpeaker = original.TurnSpeaker;
            replacement.ShowOnce = false;
            replacement.ShowOnceCurrentDialog = false;
            replacement.OnShow = variants[variant].KeepNativeImage && original.OnShow?.Actions != null
                ? new ActionList { Actions = original.OnShow.Actions.ToArray() }
                : new ActionList { Actions = Array.Empty<GameAction>() };
            replacement.OnStop = new ActionList { Actions = Array.Empty<GameAction>() };
            replacement.Continue = new Kingmaker.DialogSystem.CueSelection { Cues = new List<BlueprintCueBaseReference>() };
            replacement.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = new Condition[] {
                new Applies { Original = original.Conditions, ReplacementApplies = replacementApplies } } };
            return new Plan { CueId = cueId, Spec = spec, Variant = variant, Original = original, Page = page, Replacement = replacement,
                OriginalChecker = original.Conditions };
        }

        // Phase 3: insert the replacement before the original and guard the original. Refuses if the page moved meanwhile.
        public static void Attach(Plan plan, BlueprintCueBaseReference replacementReference, Func<bool> replacementApplies)
        {
            Insert(plan, replacementReference);
            ParentEndingGuard.Attach(plan.Original, replacementApplies);
        }

        // Phase 3 for a variant group: each variant goes in right before the original, in variant order, so the page reads
        // v0, v1, ..., original. The original is then guarded once (Guard) by "some attached variant is selected".
        public static void Insert(Plan plan, BlueprintCueBaseReference replacementReference)
        {
            int index = plan.Page.Cues.FindIndex(reference => reference.Guid == plan.Original.AssetGuid);
            if (index < 0 || plan.Page.Cues.Any(reference => reference.Guid == plan.Replacement.AssetGuid))
                throw new InvalidOperationException("Native epilogue page changed before attachment: " + plan.CueId);
            plan.Page.Cues.Insert(index, replacementReference);
        }

        public static void Guard(BlueprintCue original, Func<bool> anySelected) => ParentEndingGuard.Attach(original, anySelected);

        // Phase 3 for one cue's variants (plans in variant order, all of them): guard the original by "a variant is selected"
        // (false while the group is disabled), insert every variant right before it, then enable the group. If an insert
        // throws, the group stays disabled: every inserted variant stays hidden and the native cue plays.
        public static void AttachGroup(Group group, IReadOnlyList<Plan> plans, Func<Plan, BlueprintCueBaseReference> reference)
        {
            if (plans.Count != group.Count || plans.Select((plan, i) => plan.Variant != i).Any(wrong => wrong))
                throw new InvalidOperationException("Native epilogue edit variants are incomplete or out of order: " + plans.FirstOrDefault()?.CueId);
            Guard(plans[0].Original, () => group.Selected() >= 0);
            foreach (var plan in plans) Insert(plan, reference(plan));
            group.Enable();
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
