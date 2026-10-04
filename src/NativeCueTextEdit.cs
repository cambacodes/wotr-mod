using System;
using System.Collections.Generic;
using HarmonyLib;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.Localization;

namespace Tirabade
{
    // eng7-f6b: the existing native-edit selector supplies presentation only.
    // Original cue IDs, CueSeen, sequence positions, actions and answers stay native.
    public static class NativeCueTextEdit
    {
        private static readonly Dictionary<BlueprintCue, Func<string?>> edits = new Dictionary<BlueprintCue, Func<string?>>();
        public static void Clear() => edits.Clear();
        public static void Attach(BlueprintCue cue, Func<string?> text)
        {
            if (!NativeEpilogueEdit.IsTextOnly(cue.AssetGuid.ToString()))
                throw new InvalidOperationException("Cue has no reviewed text-only native policy");
            edits[cue] = text;
        }
        private static string? Replacement(BlueprintCue cue)
        {
            try { return edits.TryGetValue(cue, out var edit) ? edit() : null; }
            catch { return null; }
        }
        public static string Display(BlueprintCue cue, string original) => Replacement(cue) ?? original;
        public static bool SuppressVoice(BlueprintCue cue) => Replacement(cue) != null;
        [HarmonyPatch(typeof(BlueprintCue), "get_DisplayText")]
        private static class DisplayPatch
        {
            [HarmonyPostfix]
            private static void Postfix(BlueprintCue __instance, ref string __result)
                => __result = Display(__instance, __result);
        }
        // The old spoken line would contradict the replacement subtitle. Null is
        // the installed LocalizedString.PlayCueVoiceOver result for unvoiced text.
        // Disabled, unpaid or failed observation retains the original voice-over.
        [HarmonyPatch(typeof(BlueprintCue), "PlayVoiceOver")]
        private static class VoicePatch
        {
            [HarmonyPrefix]
            private static bool Prefix(BlueprintCue __instance, ref VoiceOverStatus __result)
            {
                if (!SuppressVoice(__instance)) return true;
                __result = null!;
                return false;
            }
        }
    }
    // eng7-f6b end
}
