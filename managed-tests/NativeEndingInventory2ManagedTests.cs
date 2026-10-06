using System;
using System.Collections.Generic;
using System.Linq;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Newtonsoft.Json.Linq;
using Tirabade;

// eng8-q8e: presenting a kept huntress still records the original native cue.
internal static partial class NativeEpilogueEditManagedTests
{
    public static void RunEndingIdentity(Story story, Dictionary<string, JObject> native, Action<bool, string> check)
    {
        const string departure = "8f6017d8d3bc5ec46b15773947e80c70", mourning = "86bf0569a9029ae4b8c9d300a41e5739";
        const string greybor = "8593ec10e3c34cdaaa2d2ed45e73e58a", ember = "3d54fe05a0fe44f78ac907c37fe8a460";
        foreach (string target in new[] { departure, mourning, greybor, ember })
        {
            check(NativeEpilogueEdit.IsTextOnly(target), "Q8-06 native history identity lost: " + target);
            var spec = story.NativeEpilogueEdits[target];
            var variants = Rules.EditVariants(spec);
            var scenes = Rules.EditScenes(story, variants);
            for (int v = 0; v < variants.Length; v++)
            {
                var state = new Snapshot { Chapter = 6 };
                state.Flags.UnionWith(variants[v].When[0].Where(f => !f.StartsWith("!")));
                // The native text replacement now reads the actual Wenduag
                // courtship acceptance, not merely its coarse committed bit.
                if (state.Has("wenduag.committed"))
                    state.Flags.UnionWith(new[] { "wenduag.trickster.proved", "wenduag.trickster.gate_seen",
                        "wenduag.trickster.claim.given" });
                if (state.Has("wenduag.trickster.native")) state.Flags.Add("wenduag.romance_finished");
                if (state.Has("trickster.commander_back")) state.Flags.UnionWith(new[] { "sacrifice", "ending.trickster" });
                state.Flags.Add("trickster"); Rules.Complete(story, state);
                check(Rules.SelectNativeEditVariant(story, variants, scenes, state) == v, "Q8-06 text variant unavailable: " + target);
                // Isolated cue: never mutate Main.Build's real native objects.
                var cue = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(target), name = "Q8EndingIdentity_" + target,
                    Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = Array.Empty<Condition>() } };
                var conditions = cue.Conditions; var onShow = cue.OnShow; var onStop = cue.OnStop; var continuation = cue.Continue;
                NativeCueTextEdit.Attach(cue, () => {
                    int selected = Rules.SelectNativeEditVariant(story, variants, scenes, state);
                    return selected < 0 ? null : scenes[selected]!.Nodes[0].Text;
                });
                check(NativeCueTextEdit.Display(cue, "native") == scenes[v]!.Nodes[0].Text && NativeCueTextEdit.SuppressVoice(cue),
                    "Q8-06 earned native text/voice not reconciled: " + target);
                check(cue.AssetGuid == BlueprintGuid.Parse(target) && ReferenceEquals(conditions, cue.Conditions)
                    && ReferenceEquals(onShow, cue.OnShow) && ReferenceEquals(onStop, cue.OnStop) && ReferenceEquals(continuation, cue.Continue),
                    "Q8-06 text delivery changed native behavior: " + target);
                if (target == departure || target == mourning)
                {
                    var seen = new HashSet<string> { cue.AssetGuid.ToString() };
                    check(ArchiveChecker((JObject)native[greybor]["Conditions"]!, _ => false, seen.Contains, _ => false, check, greybor)(),
                        "Q8-06 Greybor loses the reconciled native receipt");
                    if (target == departure)
                        check(ArchiveChecker((JObject)native[ember]["Conditions"]!, _ => false, seen.Contains, _ => false, check, ember)(),
                            "Q8-06 Ember's cruelty lost after departure reconciliation");
                    seen.Clear();
                    check(!ArchiveChecker((JObject)native[greybor]["Conditions"]!, _ => false, seen.Contains, _ => false, check, greybor)(),
                        "Q8-06 continuation invented a seen cue");
                }
                state.Flags.Remove("trickster.now"); state.Flags.Add("trickster.failed");
                check(NativeCueTextEdit.Display(cue, "native") == "native" && !NativeCueTextEdit.SuppressVoice(cue),
                    "Q8-06 off-path native text/voice changed: " + target);
            }
        }
        Console.WriteLine("PASS: Q8-06 native IDs, CueSeen continuations, actions, text/voice fallback and variants.");
    }
}
