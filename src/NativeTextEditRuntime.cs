using System;
using System.Collections.Generic;
using HarmonyLib;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Quests;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.Localization;

namespace Tirabade
{
    // Same instance-scoped LoadString interception as WenduagEcho. No localized pack or native blueprint is mutated.
    public static class NativeTextEditRuntime
    {
        private static readonly Dictionary<LocalizedString, NativeTextEdit> fields = new Dictionary<LocalizedString, NativeTextEdit>();
        private static Func<Snapshot?> observe = () => null;

        public static LocalizedString? Field(SimpleBlueprint? blueprint, string field) => blueprint switch
        {
            BlueprintCue cue when field == "Text" => cue.Text,
            BlueprintAnswer answer when field == "Text" => answer.Text,
            BlueprintQuest quest when field == "Description" => quest.Description,
            BlueprintQuest quest when field == "CompletionText" => quest.CompletionText,
            BlueprintQuestObjective objective when field == "Title" => objective.Title,
            BlueprintQuestObjective objective when field == "Description" => objective.Description,
            _ => null,
        };

        public static string? Check(string id, NativeTextEdit edit, SimpleBlueprint? blueprint)
        {
            if (!Rules.ReviewedNativeTexts.TryGetValue(id, out var contract) || contract != edit.Type + ":" + edit.Key)
                return "unreviewed text field";
            var parts = id.Split('/');
            if (blueprint == null || blueprint.AssetGuid.ToString() != parts[0] || blueprint.GetType().Name != edit.Type
                || NativeEpilogueEdit.TextKey(Field(blueprint, parts[1])) != edit.Key)
                return "native text evidence changed";
            return null;
        }

        public static void Install(Story story, Func<Snapshot?> read, Func<string, SimpleBlueprint?> resolve, Action<string> warn)
        {
            fields.Clear();
            observe = read;
            foreach (var pair in story.NativeTextEdits)
            {
                var parts = pair.Key.Split('/');
                var blueprint = resolve(parts[0]);
                var refusal = Check(pair.Key, pair.Value, blueprint);
                if (refusal != null) { warn("Native text " + pair.Key + ": " + refusal); continue; }
                fields[Field(blueprint, parts[1])!] = pair.Value;
            }
        }

        public static string? Replacement(LocalizedString field)
        {
            if (!fields.TryGetValue(field, out var edit)) return null;
            try
            {
                var state = observe();
                return state == null ? null : Rules.NativeText(edit, state);
            }
            catch { return null; } // Observation failure leaves the installed game's text available.
        }

        [HarmonyPatch(typeof(BlueprintCue), "PlayVoiceOver")]
        private static class VoicePatch
        {
            private static bool Prefix(BlueprintCue __instance, ref VoiceOverStatus __result)
            {
                if (Replacement(__instance.Text) == null) return true;
                __result = null!;
                return false;
            }
        }

        [HarmonyPatch(typeof(LocalizedString), "LoadString")]
        private static class TextPatch
        {
            private static bool Prefix(LocalizedString __instance, ref string __result)
            {
                var text = Replacement(__instance);
                if (text == null) return true;
                __result = text;
                return false;
            }
        }
    }
}
