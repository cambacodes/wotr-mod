using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Newtonsoft.Json.Linq;
using Tirabade;

internal static partial class NativeEpilogueEditManagedTests
{
    private sealed class CountStop : GameAction
    {
        internal int Calls;
        public override string GetCaption() => "Count selected cue stop";
        public override void RunAction() => Calls++;
    }

    public static void RunQ4(Dictionary<string, JObject> native, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        const string terendelev = "ca71b79bc9a45b741bcc6599ef017fe7";
        var terEvidence = NativeEpilogueEdit.Reviewed[terendelev];
        var terSpec = new NativeEpilogueEditSpec { Parent = terEvidence.Parent!, Dialog = terEvidence.Dialog!, Key = terEvidence.Key,
            Replacement = "terendelev.q4.fixture", When = new[] { new[] { "trickster.now", "terendelev.trickster.returned" } } };
        Dictionary<string, SimpleBlueprint> TerWorld()
        {
            var cue = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(terendelev), name = "Q4_Terendelev" };
            LoadArchiveShape(cue, native[terendelev], check);
            cue.Conditions = new ConditionsChecker { Conditions = Array.Empty<Condition>() };
            var parent = new BlueprintAnswer { AssetGuid = BlueprintGuid.Parse(terSpec.Parent),
                NextCue = new CueSelection { Strategy = Strategy.First, Cues = new List<BlueprintCueBaseReference> { Ref(terendelev) } } };
            var dialog = new BlueprintDialog { AssetGuid = BlueprintGuid.Parse(terSpec.Dialog) };
            return new Dictionary<string, SimpleBlueprint> { [terendelev] = cue, [terSpec.Parent] = parent, [terSpec.Dialog] = dialog };
        }
        var terWorld = TerWorld();
        SimpleBlueprint? ResolveTer(string guid) => terWorld.TryGetValue(guid, out var bp) ? bp : null;
        check(NativeEpilogueEdit.Check(terendelev, terSpec, ResolveTer, null) == null, "Terendelev Cue_0785 archive refused");
        var terOriginal = (BlueprintCue)terWorld[terendelev];
        var terReplacement = new BlueprintCue { AssetGuid = id("q4.terendelev.replacement") };
        Snapshot? current = null;
        var terGroup = new NativeEpilogueEdit.Group(terSpec, () => current);
        var terPlan = NativeEpilogueEdit.PrepareInDialog(terendelev, terSpec, terOriginal, terWorld[terSpec.Parent], terReplacement,
            () => terGroup.Selected() == 0);
        NativeEpilogueEdit.AttachGroup(terGroup, new[] { terPlan }, _ => Ref(terReplacement.AssetGuid.ToString()));
        check(terReplacement.Answers.Select(r => r.Guid).SequenceEqual(terOriginal.Answers.Select(r => r.Guid))
            && ((BlueprintAnswer)terWorld[terSpec.Parent]).NextCue.Cues.Select(r => r.Guid)
                .SequenceEqual(new[] { terReplacement.AssetGuid, terOriginal.AssetGuid }), "Terendelev lost her native answer list or parent order");
        foreach (bool returned in new[] { false, true })
        foreach (bool trickster in new[] { false, true })
        {
            current = new Snapshot();
            if (returned) current.Flags.Add("terendelev.trickster.returned");
            if (trickster) current.Flags.Add("trickster.now");
            check((terGroup.Selected() == 0) == (returned && trickster), "Terendelev unearned/off-path edit selected");
        }
        foreach (var change in new Action<Dictionary<string, SimpleBlueprint>>[] {
            w => ((BlueprintCue)w[terendelev]).ShowOnce = true,
            w => ((BlueprintCue)w[terendelev]).Answers.Clear(),
            w => ((BlueprintAnswer)w[terSpec.Parent]).NextCue.Cues.Clear(),
            w => typeof(Kingmaker.Localization.LocalizedString).GetField("m_Key", BindingFlags.Instance | BindingFlags.NonPublic)!
                .SetValue(((BlueprintCue)w[terendelev]).Text, "drifted") })
        {
            var drift = TerWorld(); change(drift);
            check(NativeEpilogueEdit.Check(terendelev, terSpec, g => drift.TryGetValue(g, out var bp) ? bp : null, null) != null
                && !NativeEpilogueEdit.DegradesOnRefusal(terendelev), "Terendelev drift accepted or degraded the route");
        }

        const string mielarah = "dbec675b71e9d5f4d96055f4bb31762e";
        var evidence = NativeEpilogueEdit.Reviewed[mielarah];
        const string prefix = "mielarah.trickster.";
        // These are the route's distinct rescue histories, with no route rewrite in this engine fixture.
        var rescues = new[] { prefix + "primed.minder", prefix + "primed.self", prefix + "raid.cut_down", prefix + "raid.sent_back" };
        var spec = new NativeEpilogueEditSpec { Page = evidence.Page, Key = evidence.Key, Replacement = "mielarah.q4.fixture",
            When = rescues.Select(flag => new[] { "trickster.now", flag }).ToArray() };
        Dictionary<string, SimpleBlueprint> MielWorld()
        {
            var cue = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(mielarah), name = "Q4_Mielarah" };
            LoadArchiveShape(cue, native[mielarah], check);
            cue.Conditions = new ConditionsChecker { Conditions = Array.Empty<Condition>() };
            var page = new BlueprintBookPage { AssetGuid = BlueprintGuid.Parse(spec.Page) };
            page.Cues.AddRange(((JArray)native[spec.Page]["Cues"]!).Select(v => Ref(((string)v!).Replace("!bp_", ""))));
            return new Dictionary<string, SimpleBlueprint> { [mielarah] = cue, [spec.Page] = page };
        }
        var world = MielWorld();
        var nativeGate = (JArray)native[mielarah]["Conditions"]!["Conditions"]!;
        check(nativeGate.Count == 2 && (string)nativeGate[0]["m_Answer"]! == "!bp_1eececde9d7a70c44be526ea668f3ed4"
            && (string)nativeGate[1]["m_Etude"]! == "!bp_8d0fcb697a43a464fa7119e274bf9d7b" && (bool)nativeGate[1]["Playing"]!,
            "Mielarah raid/captain native eligibility drifted");
        var nativeStop = (JArray)native[mielarah]["OnStop"]!["Actions"]!;
        check(nativeStop.Count == 1 && !(bool)nativeStop[0]["Evaluate"]!
            && nativeStop[0]["EtudeEvaluator"]!.Type == JTokenType.Null, "Mielarah native OnStop evaluator/options drifted");
        check(NativeEpilogueEdit.Check(mielarah, spec, g => world.TryGetValue(g, out var bp) ? bp : null, null) == null,
            "Mielarah Cue_0482 archive OnStop refused");
        var original = (BlueprintCue)world[mielarah];
        var page = (BlueprintBookPage)world[spec.Page];
        var replacement = new BlueprintCue { AssetGuid = id("q4.mielarah.replacement") };
        current = null;
        var group = new NativeEpilogueEdit.Group(spec, () => current);
        var plan = NativeEpilogueEdit.Prepare(mielarah, spec, original, page, replacement, () => group.Selected() == 0);
        check(ReferenceEquals(original.OnStop, replacement.OnStop) && replacement.OnStop.Actions.Length == 1
            && NativeEpilogueEdit.ActionShape(replacement.OnStop.Actions[0]) == "StartEtude:90f2e0f1cdc263b41b2e625bf228b226",
            "Mielarah replacement lost the exact native TumberdDead action");
        NativeEpilogueEdit.AttachGroup(group, new[] { plan }, _ => Ref(replacement.AssetGuid.ToString()));
        foreach (var condition in replacement.Conditions.Conditions)
        {
            condition.Owner = replacement;
            condition.name = "$Q4_Applies$";
            replacement.ElementsArray.Add(condition);
        }
        check(page.Cues.FindIndex(r => r.Guid == replacement.AssetGuid) + 1 == page.Cues.FindIndex(r => r.Guid == original.AssetGuid),
            "Mielarah replacement is not immediately before the native cue");
        // Keep the shared action list, replacing its effect with a counter after verifying the real archive action.
        // This exercises OnStop dispatch without mutating game etudes in the fixture process.
        var nativeActions = original.OnStop.Actions;
        var counter = new CountStop { Owner = original, name = "$Q4_CountStop$" };
        original.ElementsArray.Add(counter);
        original.OnStop.Actions = new GameAction[] { counter };
        foreach (string? rescue in rescues.Cast<string?>().Prepend(null))
        foreach (bool trickster in new[] { false, true })
        foreach (bool nativeEligible in new[] { false, true })
        {
            current = new Snapshot();
            if (rescue != null) current.Flags.Add(rescue);
            if (trickster) current.Flags.Add("trickster.now");
            bool edited = rescue != null && trickster;
            check((group.Selected() == 0) == edited, "Mielarah rescue history selection: " + rescue + "/" + trickster);
            // PlayBookPage checks each cue; both variants keep the native AnswerSelected + CaptainMielara predicate.
            var played = new[] { replacement, original }.Where(c => nativeEligible && c.Conditions.Conditions.All(condition => condition.Check())).ToArray();
            check(played.Length == (nativeEligible ? 1 : 0) && (!nativeEligible || played[0] == (edited ? replacement : original)),
                "Mielarah native and replacement both/neither played");
            counter.Calls = 0;
            foreach (var cue in played) cue.OnStop.Run();
            check(counter.Calls == (nativeEligible ? 1 : 0), "TumberdDead stop effect did not run exactly once");
        }
        original.OnStop.Actions = nativeActions;
        foreach (var change in new Action<Dictionary<string, SimpleBlueprint>>[] {
            w => ((BlueprintCue)w[mielarah]).OnStop.Actions = Array.Empty<GameAction>(),
            w => ((BlueprintCue)w[mielarah]).OnStop.Actions = ((BlueprintCue)w[mielarah]).OnStop.Actions.Concat(((BlueprintCue)w[mielarah]).OnStop.Actions).ToArray(),
            w => ((BlueprintCue)w[mielarah]).OnStop = new ActionList { Actions = new GameAction[] { new CountStop() } },
            w => ((BlueprintCue)w[mielarah]).OnStop.Actions[0].GetType().GetField("Evaluate", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!
                .SetValue(((BlueprintCue)w[mielarah]).OnStop.Actions[0], true),
            w => ((BlueprintBookPage)w[spec.Page]).Cues.RemoveAll(r => r.Guid == BlueprintGuid.Parse(mielarah)) })
        {
            var drift = MielWorld(); change(drift);
            check(NativeEpilogueEdit.Check(mielarah, spec, g => drift.TryGetValue(g, out var bp) ? bp : null, null) != null
                && !NativeEpilogueEdit.DegradesOnRefusal(mielarah), "Mielarah drift accepted or degraded the route");
        }
        Console.WriteLine("PASS: engine-q4 Terendelev evidence/drift and Mielarah rescue selection with one preserved native OnStop.");
    }
}
