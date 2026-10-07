using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class HaremS36Tests
{
    internal static void Run(Story exported, Action<bool, string> check)
    {
        const string p = "household.pair.melazmera_hepzamirah.";
        var scenes = exported.Scenes.Where(s => s.Id.StartsWith(p, StringComparison.Ordinal)).ToArray();
        // The coordinator has to attach this allow-listed module in expansion.py.
        // A baseline export has no S36; the candidate gate must use its assembled payload.
        check(scenes.Length == 3, "S36 must have exactly preparation, primary and one retry.");
        var story = new Story { Scenes = scenes.ToList(), Relationships = exported.Relationships,
            RestAllowances = exported.RestAllowances };
        Snapshot Ready(Scene scene)
        {
            var state = new Snapshot { Chapter = 5, Hour = 1000, Area = scene.Areas.Single(),
                CrusadeResources = new Dictionary<string, int> { ["Finances"] = 1000 } };
            state.Flags.UnionWith(scene.Requires);
            return state;
        }
        var open = scenes.Single(s => s.Id == p + "open");
        var diversion = scenes.Single(s => s.Id == p + "diversion");
        var replacement = scenes.Single(s => s.Id == p + "replacement");
        foreach (var scene in scenes)
        {
            var state = Ready(scene);
            check(Rules.Available(story, scene, state), "S36 ready visit unavailable: " + scene.Id);
            foreach (var gate in scene.Requires)
            {
                var skipped = Program.Copy(state); skipped.Flags.Remove(gate);
                skipped.Flags.UnionWith(new[] { "trickster.ever", "trickster.foresight.met" });
                check(!Rules.Available(story, scene, skipped), "S36 skipped gate: " + gate);
            }
            foreach (var woman in scene.Participants)
            {
                var rel = story.Relationships[woman];
                foreach (var loss in rel.UnavailableFlags.Append(rel.ClosedFlag))
                {
                    var absent = Program.Copy(state); absent.Flags.Add(loss);
                    check(!Rules.Available(story, scene, absent), "S36 absent woman staged: " + loss);
                }
            }
            // Production progression walker traverses every selectable answer and
            // both check results, including the runtime insufficient-funds exit.
            foreach (int funds in new[] { 0, 299, 300, 399, 400, 1000 })
            {
                state.CrusadeResources!["Finances"] = funds;
                var histories = Program.Walk(scene, state);
                check(histories.Count > 0, "S36 no terminal history: " + scene.Id);
                check(histories.All(h => scene.Participants.All(w => !h.Has(story.Relationships[w].ClosedFlag))),
                    "S36 household choice closed a romance.");
                check(histories.All(h => !h.Has(p + "resolved") || h.Has(p + "diversion.held") || h.Has(p + "replacement.held")),
                    "S36 resolution without a completed deed.");
            }
        }
        var remedy = Ready(replacement);
        remedy.Flags.UnionWith(new[] { "hepzamirah.harem.enmity.melazmera", "melazmera.harem.enmity.hepzamirah",
            "hepzamirah.harem.enmity.delamere" });
        remedy.Times[p + "diversion.failed"] = 953;
        check(!Rules.Available(story, replacement, remedy), "S36 remedy before 48 hours.");
        remedy.Hour++;
        check(Rules.Available(story, replacement, remedy), "S36 separate remedy blocked by enmity.");
        var paid = Program.Walk(replacement, remedy).Single(h => h.Has(p + "replacement.held"));
        check(paid.CrusadeResources!["Finances"] == 600 && paid.Has("hepzamirah.harem.enmity.delamere"),
            "S36 remedy debit or existing target changed.");
        var options = new JsonSerializerOptions { IncludeFields = true };
        var loaded = JsonSerializer.Deserialize<Snapshot>(JsonSerializer.Serialize(paid, options), options)!;
        check(!Rules.Available(story, replacement, loaded), "S36 reload replayed the remedy.");
        var blocked = Ready(open); blocked.Flags.Add("hepzamirah.harem.enmity.melazmera");
        check(!Rules.Available(story, open, blocked), "S36 direct exchange ignored enmity.");
        blocked.Flags.Add("hepzamirah.harem.reconciled.melazmera");
        check(Rules.Available(story, open, blocked), "S36 reconciliation override failed.");
    }
}
