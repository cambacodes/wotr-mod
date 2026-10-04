using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using HarmonyLib;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.Localization;

namespace Tirabade
{
    // eng7-f1: text-only, reviewed answer replacements. The native answer itself is selected,
    // so its GUID, history, availability, actions and continuation remain native on every path.
    public static class NativeAnswerEdit
    {
        private static readonly Dictionary<BlueprintAnswer, (Func<string> Text, Func<bool> Holds)> edits
            = new Dictionary<BlueprintAnswer, (Func<string>, Func<bool>)>();

        public static string? Check(string target, NativeAnswerEditSpec spec, Func<string, SimpleBlueprint?> resolve)
        {
            if (!Rules.ReviewedNativeAnswers.TryGetValue(target, out var policy)
                || spec.AnswerList != policy.AnswerList || spec.Key != policy.Key)
                return "not a reviewed native answer";
            if (!(resolve(target) is BlueprintAnswer answer) || !(resolve(spec.AnswerList) is BlueprintAnswersList list)
                || list.Answers.Count(r => r.Guid == answer.AssetGuid) != 1)
                return "answer missing or not exactly once on its reviewed list";
            var shown = answer.ShowConditions;
            bool empty = policy.SeenCue.Length == 0;
            bool show = shown != null && shown.Operation == Operation.And && shown.Conditions != null
                && (empty ? shown.Conditions.Length == 0 : shown.Conditions.Length == 1
                    && shown.Conditions[0] is CueSeen seen && !seen.Not && !seen.CurrentDialog
                    && ((BlueprintCueBaseReference?)typeof(CueSeen).GetField("m_Cue", BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.Public)!
                        .GetValue(seen))?.Guid == BlueprintGuid.Parse(policy.SeenCue));
            if (NativeEpilogueEdit.TextKey(answer.Text) != policy.Key || !show
                || answer.ComponentsArray.Length != 0 || answer.ShowOnce || answer.ShowOnceCurrentDialog || answer.DebugMode
                || answer.MythicRequirement != default || answer.AlignmentRequirement != default
                || answer.Experience != DialogExperience.NoExperience || answer.RequireValidCue || !answer.AddToHistory
                || answer.ShowCheck.Type.ToString() != "Unknown" || answer.ShowCheck.DC != 0 || answer.FakeChecks.Length != 0
                || answer.CharacterSelection.SelectionType.ToString() != "Clear" || answer.CharacterSelection.ComparisonStats.Length != 0
                || answer.AlignmentShift.Value != 0 || answer.AlignmentShift.Direction.ToString() != "TrueNeutral"
                || answer.SelectConditions?.Operation != Operation.And || answer.SelectConditions.Conditions?.Length != 0
                || answer.OnSelect?.Actions?.Length != 0 || answer.NextCue?.Strategy != Kingmaker.DialogSystem.Strategy.First
                || answer.NextCue.Cues?.Count != 1 || answer.NextCue.Cues[0].Guid != BlueprintGuid.Parse(policy.NextCue))
                return "answer behavior differs from the reviewed policy";
            return null;
        }

        public static void Attach(BlueprintAnswer answer, LocalizedString text, Func<bool> holds)
            => Attach(answer, () => text.ToString(), holds);

        public static void Attach(BlueprintAnswer answer, Func<string> text, Func<bool> holds)
            => edits[answer] = (text, holds);

        // Also callable by the offline managed contract test. Observation or localization failure keeps native text.
        public static string Display(BlueprintAnswer answer, string original)
        {
            try { return edits.TryGetValue(answer, out var edit) && edit.Holds() ? edit.Text() : original; }
            catch { return original; }
        }

        [HarmonyPatch(typeof(BlueprintAnswer), "get_DisplayText")]
        private static class DisplayPatch
        {
            [HarmonyPostfix]
            private static void Postfix(BlueprintAnswer __instance, ref string __result)
                => __result = Display(__instance, __result);
        }
    }
    // end eng7-f1
}
