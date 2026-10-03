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
            // E14d extension: the reviewed continuation (Strategy First), or null for none. On a book page the continued cue plays
            // right after the original (DialogController.PlayBasicCue); a replacement never continues, so it hides that too.
            public readonly string[]? Continue;
            // E14d extension (Cue_0461): the continuation the parent mod sets at load (RanRomance SlideArue: Aranka's slide), also
            // accepted (Strategy First); a replacement of such a cue keeps whatever continuation the cue has, so the parent's
            // slide still follows it. 252ccf6: refusing that continuation degraded the relationship in game.
            public readonly string[]? ParentContinue;
            // E14i: a cue of a common dialog: Parent lists it in its Continue (Strategy First), Dialog's FirstCue holds Parent.
            // Page and Sequence are then empty.
            public readonly string? Parent, Dialog;
            internal Evidence(string page, string sequence, string key, string? image = null, bool degradeOnRefusal = true, string[]? continueTo = null,
                string? parent = null, string? dialog = null, string[]? parentContinue = null)
            {
                ParentContinue = parentContinue;
                Page = page; Sequence = sequence; Key = key; Image = image; DegradeOnRefusal = degradeOnRefusal; Continue = continueTo;
                Parent = parent; Dialog = dialog;
            }
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
            ["36a07840d25540eeac6b1c6631196bcc"] = new Evidence("503164ff04ac64543ba42561ea9f970f", Companions, "af56e46e-7e82-4e22-9951-8ddc37dd015f",
                degradeOnRefusal: false), // Camellia Cue_38_master (warning-only, with the other Camellia slides below)
            // Arueshalae Cue_0461 (the dream world): RanRomance's SlideArue sets its Continue to Aranka's slide 959237a3 (aranka-SlideArue.cs),
            // which the cue keeps under a replacement. Warning-only.
            ["78ae1bdc3b0824b4ca2ed618782f1faa"] = new Evidence("e83fff8e997db8e439bf12e09225696a", Companions, "411ef2f1-5168-455f-99b0-ca33960678c5",
                degradeOnRefusal: false, parentContinue: new[] { "959237a34dfe436eb8f088b4be259daa" }),
            ["f76713034f4087a4f80495971c47ca7b"] = new Evidence("e83fff8e997db8e439bf12e09225696a", Companions, "fa1468ba-9679-4805-9dd4-c71997aa4e7f"), // Arueshalae Cue_0462 (NM1)
            // Tirabade BookPage_0307 Cue_0311 (IrabethDead + AneviaGone Playing): "No one ever saw her again." Its OnShow swaps
            // the pair picture for f96ad5fa, as the other departure cue (Cue_0310) does. The parent never names the cue, its
            // page or CueSequence_Special.
            ["3a3e561c6b05a284d93eb3bff7b712a6"] = new Evidence("ae1f824fe248d9f4aac7d39ec2e12140", Special, "4c278ba4-5217-4fae-afec-47c6f6597e00",
                image: "f96ad5fa9c59d7549adff4c90f0703ab", degradeOnRefusal: false),
            // Tirabade BookPage_0307 Cue_0310 (IrabethGone + AneviaGone Playing, both left at the Coronation): "...they could
            // never escape their nightmares of the Fifth Crusade." Same image action and page; the parent never names it.
            ["ccd140dbf2603734aa323261c2445bec"] = new Evidence("ae1f824fe248d9f4aac7d39ec2e12140", Special, "cc716238-3702-4913-977d-6189665672b7",
                image: "f96ad5fa9c59d7549adff4c90f0703ab", degradeOnRefusal: false),
            // Camellia, Epilogues/BookPage_0347 (CompanionInParty Camelia_Companion, dead allowed, Ex not): her departure slides.
            // Lead cues (exactly one plays in every native state): Cue_0392 / Cue_0544 (TE with companions, Q3 completed or not),
            // Cue_28 (romance, no sacrifice), Cue_38_master (romance, sacrifice), Cue_0386 (no romance; continues into Cue_0387,
            // the dagger at the Commander's heart). Follow-ons: Cue_16 (Mireya in Varisia, every non-TE state), Cue_0391 (true
            // romance: came back, left again), Cue_0390 (Mireya's lovers; shared text f25c5ed1). The parent mod names none of
            // them, the page or its sequence (aranka-*.cs, RanRomance.dll strings). Every one is warning-only.
            ["84f892d388bba01489145ecd631f23a2"] = new Evidence(CamelliaPage, Companions, "8f73fe38-c791-4d7e-9bd0-553f1f0b07aa",
                image: "df4a5da19a0a64542929dc8409b29bbe", degradeOnRefusal: false),                                             // Cue_0392
            ["c1b1da84c12d3ac448ec65b4342ce77f"] = new Evidence(CamelliaPage, Companions, "d494dcd7-7f4f-4b8b-a8d7-7dcb41998909", degradeOnRefusal: false), // Cue_0544
            ["4ed8e9723359441dae10ad3068d3f2c7"] = new Evidence(CamelliaPage, Companions, "aee7c6bf-fbe1-4288-83e7-3ff3bd4545ad", degradeOnRefusal: false), // Cue_28
            ["5011dfa46fbb0464ab624d78bcfbd483"] = new Evidence(CamelliaPage, Companions, "4dd21f1d-4280-4598-851d-bbc6bbf2f3e4", degradeOnRefusal: false,
                continueTo: new[] { "f23fb3dacf91b3e4b9d3a85937d323bf" }),                                                         // Cue_0386 -> Cue_0387
            ["3617a648c06a45d1807fde65aedafb06"] = new Evidence(CamelliaPage, Companions, "de512bb2-4d4d-4ca2-b20d-9b2d6384c802", degradeOnRefusal: false), // Cue_16
            ["430ce9767d3ede2479ff9d6aee432304"] = new Evidence(CamelliaPage, Companions, "4819461c-331c-4872-a077-49115a7c9ad7", degradeOnRefusal: false), // Cue_0391
            ["e9a183135b8289544a3144dcf8151920"] = new Evidence(CamelliaPage, Companions, "f31377a1-a78e-47f2-bc10-1721eac2f9c1", degradeOnRefusal: false), // Cue_0390
            // E14i: Areelu's afterlogue (World/Dialogs/Epilogues_afterlogues, a Common dialog, not a book page). Cue_0001 lists, Strategy
            // First: Cue_0002, Cue_28, Cue_0003, Cue_0006, Cue_0004, Cue_29, Cue_0005; each continues into Cue_0007 (her account to
            // Pharasma), which a replacement keeps. Cue_0004 (not redeemed, not dead): the cottage. Cue_0005 (the fallback): "my life
            // ended along with it". The parent mod names none of them (aranka-*.cs, RanRomance.dll strings). Warning-only.
            ["825786e8c5db4511ae30950bb286f0e9"] = new Evidence("", "", "cd04e9ab-c34b-49ce-b0a7-25f064571101", degradeOnRefusal: false,
                continueTo: new[] { AfterlogueAccount }, parent: AfterlogueFirst, dialog: AfterlogueDialog),                         // Cue_0004
            ["1b53c189b767412f921b8294b980a51c"] = new Evidence("", "", "102a4671-6e9d-45b6-a801-32d1706c9698", degradeOnRefusal: false,
                continueTo: new[] { AfterlogueAccount }, parent: AfterlogueFirst, dialog: AfterlogueDialog),                         // Cue_0005
        };
        public const string AfterlogueDialog = "57e18f5158904030a84a772fb361ceb4";   // Epilogues_afterlogues_dialogue
        public const string AfterlogueFirst = "5b567bdd747e497cb9f6984b1ca1dfc8";    // Epilogues_afterlogues/Cue_0001
        public const string AfterlogueAccount = "f5e9e257be4241108316b2c0da0dff4b";  // Epilogues_afterlogues/Cue_0007
        public const string CamelliaPage = "503164ff04ac64543ba42561ea9f970f";   // Epilogues/BookPage_0347

        public static bool DegradesOnRefusal(string cueId) => !Reviewed.TryGetValue(cueId, out var evidence) || evidence.DegradeOnRefusal;

        public sealed class Plan
        {
            internal string CueId = "";
            internal NativeEpilogueEditSpec Spec = null!;
            internal int Variant;
            internal BlueprintCue Original = null!;
            internal BlueprintBookPage Page = null!;
            internal BlueprintCue? ParentCue;   // E14i: the dialog cue whose Continue holds the original (Page is then null)
            internal BlueprintCue Replacement = null!;
            public ConditionsChecker OriginalChecker = null!;
        }

        // The ordered variants of one native cue. The group selects nothing until Enable() (every variant attached), so a
        // partial attachment never hides the native cue or lets a later fallback variant stand in for an earlier one.
        public sealed class Group
        {
            private readonly NativeEpilogueVariant[] variants;
            private readonly Func<Snapshot?> observe;
            private readonly Story? story;          // E14d delivery: with the story, a variant also needs its scene available
            private readonly Scene?[] scenes;
            private bool enabled;
            public Group(NativeEpilogueEditSpec spec, Func<Snapshot?> observe, Story? story = null)
            {
                variants = Rules.EditVariants(spec);
                this.observe = observe;
                this.story = story;
                scenes = story == null ? Array.Empty<Scene?>() : Rules.EditScenes(story, variants);
            }
            public int Count => variants.Length;
            public bool Enabled => enabled;
            public void Enable() => enabled = true;
            public int Selected()
            {
                if (!enabled) return -1;
                var state = observe();
                return state == null ? -1 : story == null ? Rules.SelectNativeEditVariant(variants, state)
                    : Rules.SelectNativeEditVariant(story, variants, scenes, state);
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
            if (Reviewed.TryGetValue(cueId, out var reviewed) && reviewed.Image == null && Rules.EditVariants(spec).Any(variant => variant.KeepNativeImage))
                return "a variant keeps a native image the reviewed cue does not have";
            if (!string.IsNullOrEmpty(spec.Parent) || !string.IsNullOrEmpty(spec.Dialog) || reviewed.Parent != null)
                return CheckInDialog(cueId, spec, resolve);
            return CheckEvidence(cueId, spec.Page, spec.Sequence, spec.Key, resolve, aeon);
        }

        // E14i: a common-dialog cue. The parent continues into it exactly once (Strategy First), the dialog opens on the parent,
        // and the cue has the reviewed shape: no OnShow, OnStop, answers or components, and exactly its reviewed continuation.
        private static string? CheckInDialog(string cueId, NativeEpilogueEditSpec spec, Func<string, SimpleBlueprint?> resolve)
        {
            if (!Reviewed.TryGetValue(cueId, out var evidence) || evidence.Parent == null || evidence.Parent != spec.Parent
                || evidence.Dialog != spec.Dialog || evidence.Key != spec.Key || !string.IsNullOrEmpty(spec.Page) || !string.IsNullOrEmpty(spec.Sequence))
                return "not a reviewed native dialog cue";
            if (!(resolve(cueId) is BlueprintCue cue)) return "cue missing";
            if (!(resolve(evidence.Parent) is BlueprintCue parent)) return "parent cue missing";
            if (!(resolve(evidence.Dialog!) is BlueprintDialog dialog)) return "dialog missing";
            if (TextKey(cue.Text) != spec.Key) return "cue text key changed (patch drift)";
            var continued = cue.Continue?.Cues;
            bool continueReviewed = evidence.Continue == null ? continued?.Count == 0
                : continued != null && cue.Continue!.Strategy == Kingmaker.DialogSystem.Strategy.First
                    && continued.Select(reference => reference?.Guid).SequenceEqual(evidence.Continue.Select(id => (BlueprintGuid?)BlueprintGuid.Parse(id)));
            if (cue.ShowOnce || cue.ShowOnceCurrentDialog || cue.Conditions == null || cue.ComponentsArray.Length != 0 || cue.OnShow?.Actions?.Length != 0
                || cue.OnStop?.Actions?.Length != 0 || !continueReviewed || cue.Answers?.Count != 0)
                return "cue behavior differs from the reviewed policy";
            if (parent.Continue?.Cues == null || parent.Continue.Strategy != Kingmaker.DialogSystem.Strategy.First
                || parent.Continue.Cues.Count(reference => reference?.Guid == cue.AssetGuid) != 1)
                return "parent no longer continues First into the cue exactly once";
            if (dialog.FirstCue?.Cues == null || dialog.FirstCue.Cues.Count(reference => reference?.Guid == parent.AssetGuid) != 1)
                return "dialog no longer opens on the parent cue";
            return null;
        }

        // E14d extension: a suppression is checked against the same reviewed evidence (it has no variants).
        public static string? Check(string cueId, NativeEpilogueSuppressionSpec spec, Func<string, SimpleBlueprint?> resolve, BlueprintCueSequence? aeon)
            => CheckEvidence(cueId, spec.Page, spec.Sequence, spec.Key, resolve, aeon);

        // A cue's text key: its own, or (a shared string, e.g. Cue_0390) the shared asset's. LocalizedString.Key is m_Key only.
        public static string? TextKey(Kingmaker.Localization.LocalizedString? text) =>
            text == null ? null : !string.IsNullOrEmpty(text.Key) ? text.Key : text.Shared?.String?.Key;

        private static string? CheckEvidence(string cueId, string pageId, string sequenceId, string key, Func<string, SimpleBlueprint?> resolve,
            BlueprintCueSequence? aeon)
        {
            if (!Reviewed.TryGetValue(cueId, out var evidence) || evidence.Page != pageId || evidence.Sequence != sequenceId || evidence.Key != key)
                return "not a reviewed native cue";
            if (!(resolve(cueId) is BlueprintCue cue)) return "cue missing";
            if (!(resolve(pageId) is BlueprintBookPage page)) return "page missing";
            if (!(resolve(sequenceId) is BlueprintCueSequence sequence)) return "sequence missing";
            if (TextKey(cue.Text) != key) return "cue text key changed (patch drift)";
            var onShow = cue.OnShow?.Actions;
            bool onShowReviewed = evidence.Image == null ? onShow?.Length == 0
                : onShow?.Length == 1 && ImageOf(onShow[0]) == evidence.Image;
            var continued = cue.Continue?.Cues;
            bool continueReviewed = (evidence.Continue == null ? continued?.Count == 0
                : continued != null && cue.Continue!.Strategy == Kingmaker.DialogSystem.Strategy.First
                    && continued.Select(reference => reference?.Guid).SequenceEqual(evidence.Continue.Select(id => (BlueprintGuid?)BlueprintGuid.Parse(id))))
                || evidence.ParentContinue != null && continued != null && cue.Continue!.Strategy == Kingmaker.DialogSystem.Strategy.First
                    && continued.Select(reference => reference?.Guid).SequenceEqual(evidence.ParentContinue.Select(id => (BlueprintGuid?)BlueprintGuid.Parse(id)));
            if (cue.ShowOnce || cue.ShowOnceCurrentDialog || cue.Conditions == null || cue.ComponentsArray.Length != 0
                || !onShowReviewed || cue.OnStop?.Actions?.Length != 0 || !continueReviewed || cue.Answers?.Count != 0)
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
            // A cue the parent mod continues (ParentContinue) keeps its continuation under the replacement; any other never continues.
            replacement.Continue = Reviewed.TryGetValue(cueId, out var reviewed) && reviewed.ParentContinue != null && original.Continue?.Cues != null
                ? new Kingmaker.DialogSystem.CueSelection { Cues = original.Continue.Cues.ToList(), Strategy = original.Continue.Strategy }
                : new Kingmaker.DialogSystem.CueSelection { Cues = new List<BlueprintCueBaseReference>() };
            replacement.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = new Condition[] {
                new Applies { Original = original.Conditions, ReplacementApplies = replacementApplies } } };
            return new Plan { CueId = cueId, Spec = spec, Variant = variant, Original = original, Page = page, Replacement = replacement,
                OriginalChecker = original.Conditions };
        }

        // E14i phase 2: a replacement for a common-dialog cue speaks as the original (speaker, listener, animation) and keeps its
        // reviewed continuation, so the dialog goes on exactly as it would have (Cue_0007 and Pharasma's verdict).
        public static Plan PrepareInDialog(string cueId, NativeEpilogueEditSpec spec, BlueprintCue original, BlueprintCue parent, BlueprintCue replacement,
            Func<bool> replacementApplies, int variant = 0)
        {
            replacement.Speaker = original.Speaker;
            replacement.TurnSpeaker = original.TurnSpeaker;
            replacement.Animation = original.Animation;
            ListenerField?.SetValue(replacement, ListenerField.GetValue(original));
            replacement.ShowOnce = false;
            replacement.ShowOnceCurrentDialog = false;
            replacement.OnShow = new ActionList { Actions = Array.Empty<GameAction>() };
            replacement.OnStop = new ActionList { Actions = Array.Empty<GameAction>() };
            replacement.Continue = new Kingmaker.DialogSystem.CueSelection { Cues = original.Continue.Cues.ToList(), Strategy = original.Continue.Strategy };
            replacement.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = new Condition[] {
                new Applies { Original = original.Conditions, ReplacementApplies = replacementApplies } } };
            return new Plan { CueId = cueId, Spec = spec, Variant = variant, Original = original, Page = null!, ParentCue = parent,
                Replacement = replacement, OriginalChecker = original.Conditions };
        }

        private static readonly FieldInfo? ListenerField = typeof(BlueprintCue).GetField("m_Listener", BindingFlags.Instance | BindingFlags.NonPublic);

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
            if (plan.ParentCue != null)   // E14i: into the parent's Continue, right before the original (Strategy First picks it first)
            {
                var continued = plan.ParentCue.Continue.Cues;
                int at = continued.FindIndex(reference => reference.Guid == plan.Original.AssetGuid);
                if (at < 0 || continued.Any(reference => reference.Guid == plan.Replacement.AssetGuid))
                    throw new InvalidOperationException("Native dialog cue changed before attachment: " + plan.CueId);
                continued.Insert(at, replacementReference);
                return;
            }
            int index = plan.Page.Cues.FindIndex(reference => reference.Guid == plan.Original.AssetGuid);
            if (index < 0 || plan.Page.Cues.Any(reference => reference.Guid == plan.Replacement.AssetGuid))
                throw new InvalidOperationException("Native epilogue page changed before attachment: " + plan.CueId);
            plan.Page.Cues.Insert(index, replacementReference);
        }

        public static void Guard(BlueprintCue original, Func<bool> anySelected) => ParentEndingGuard.Attach(original, anySelected);

        // E14d extension: a suppression only guards the native cue (hidden, with its continuation, while `suppressed` holds).
        public static void Suppress(BlueprintCue original, Func<bool> suppressed) => ParentEndingGuard.Attach(original, suppressed);

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
