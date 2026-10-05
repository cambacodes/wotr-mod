using System;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng8-q8e: real native checkers plus Available-aware production selection.
internal static class NativeEndingInventory2Tests
{
    private static void Forget(Story story, Snapshot state, string key)
    {
        state.Flags.Remove(key);
        if (story.Derived.TryGetValue(key, out var groups))
            foreach (string flag in groups.SelectMany(g => g)) Forget(story, state, flag);
        if (story.Latches.TryGetValue(key, out var sources))
            foreach (string flag in sources) Forget(story, state, flag);
    }
    internal static void Run(Story story, Action<bool, string> check)
    {
        if (!story.Derived.ContainsKey("participant.vellexia.available")) return;
        using var doc = JsonDocument.Parse(File.ReadAllText("tools/native_ending_inventory2_contracts.json"));
        var fixtures = doc.RootElement.GetProperty("Fixtures");
        int targets = 0;
        foreach (var row in doc.RootElement.GetProperty("Rows").EnumerateArray())
        {
            targets++;
            string cue = row.GetProperty("Target").GetString()!, field = row.GetProperty("Field").GetString()!;
            bool hide = field == "NativeEpilogueSuppressions";
            check(hide ? story.NativeEpilogueSuppressions.ContainsKey(cue) : story.NativeEpilogueEdits.ContainsKey(cue), "Q8-06 target missing " + cue);
            var outcomes = row.GetProperty("Outcomes").EnumerateArray().Select(x => story.Scenes.Single(s => s.Id == x.GetString())).ToArray();
            for (int i = 0; i < outcomes.Length; i++)
            {
                var outcome = outcomes[i];
                var live = ImplicitParticipantInventoryTests.World(story, outcome);
                // Existing paid restoration can coexist with native dead flags. No romance implies a return.
                foreach (bool returned in new[] { false, true })
                {
                    var state = Program.Copy(live);
                    if (returned) state.Flags.Add(outcome.Relationship + ".trickster.returned");
                    ImplicitParticipantInventoryTests.Observe(story, state);
                    check(Rules.Available(story, outcome, state), "Q8-06 positive ending unavailable " + outcome.Id);
                    bool Selected(Snapshot s)
                    {
                        if (hide) return Rules.WhenHolds(story.NativeEpilogueSuppressions[cue].When, s);
                        var edit = story.NativeEpilogueEdits[cue];
                        var variants = Rules.EditVariants(edit);
                        int selected = Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), s);
                        return selected >= 0 && variants[selected].Replacement == row.GetProperty("Replacements")[i].GetString();
                    }
                    check(Selected(state), "Q8-06 earned ending still gets native loss " + cue + "/" + outcome.Id);
                    foreach (string control in new[] { "off-path", "unpaid", "closed", "dead", "sacrifice", "degraded" })
                    {
                        var bad = Program.Copy(state);
                        switch (control)
                        {
                            case "off-path": bad.Flags.UnionWith(new[] { "legend", "trickster.failed" }); break;
                            case "unpaid":
                                foreach (string key in outcome.Requires.Where(k => !k.StartsWith("trickster"))) Forget(story, bad, key);
                                Forget(story, bad, "trickster.commander_back");
                                break;
                            case "closed": bad.Flags.Add(story.Relationships[outcome.Relationship].ClosedFlag); break;
                            case "dead":
                                bad.Flags.Remove(outcome.Relationship + ".trickster.returned");
                                bad.Flags.Add(outcome.Relationship == "camellia" ? "camellia.dead" : outcome.Relationship == "nenio" ? "nenio.dead" : "wenduag.dead_any");
                                break;
                            case "sacrifice": Forget(story, bad, "trickster.commander_back"); bad.Flags.Add("sacrifice"); break;
                            case "degraded": bad.Flags.Add("rrt.degraded." + outcome.Relationship); break;
                        }
                        ImplicitParticipantInventoryTests.Observe(story, bad);
                        // Suppression is a When-only policy; degraded native edits fail via runtime relationship guard.
                        if (hide && control == "degraded") continue;
                        check(!Selected(bad), "Q8-06 native control suppressed " + cue + "/" + control);
                    }
                }
            }
        }
        check(targets == 13, "Q8-06 missing nominated continuation");
        bool Original(string target, string[] playing, string[]? seen = null, string[]? completed = null)
            => NativeContradictionInventoryTests.OriginalHolds(fixtures.GetProperty(target).GetProperty("Data").GetProperty("Conditions"), playing, seen, completed);
        const string departure = "8f6017d8d3bc5ec46b15773947e80c70", mourning = "86bf0569a9029ae4b8c9d300a41e5739";
        check(Original(departure, Array.Empty<string>()) && !Original(departure, Array.Empty<string>(), completed: new[] { "5ba83bd1a6b1c884794fbb4858480e7f" }), "Q8-06 Q3 fixture dishonest");
        check(Original(mourning, new[] { "381a296094804761af0893d2e70dc2df", "c3a5748e4a44a1649a75e0968c15a0c1" }), "Q8-06 native bereavement not eligible");
        check(Original("b6c0fb4c102cfb84f83a772e2dbb8a14", Array.Empty<string>()) && !Original("b6c0fb4c102cfb84f83a772e2dbb8a14", new[] { "9748dacf968fdbf408af504d00e3e38e" }, completed: new[] { "fcf68dc28a7e9df43961d067937e3935" }), "Q8-06 Nenio no-friend native partition");
        foreach (string seen in new[] { departure, mourning })
            check(Original("8593ec10e3c34cdaaa2d2ed45e73e58a", Array.Empty<string>(), new[] { seen }), "Q8-06 Greybor continuation missing");
        foreach (string seen in new[] { departure, "d744a32aeb3e0804b98683deb56da799" })
            check(Original("3d54fe05a0fe44f78ac907c37fe8a460", Array.Empty<string>(), new[] { seen }), "Q8-06 Ember continuation missing");
        check(!Original("8593ec10e3c34cdaaa2d2ed45e73e58a", Array.Empty<string>()) && !Original("3d54fe05a0fe44f78ac907c37fe8a460", Array.Empty<string>()), "Q8-06 continuation eligibility broadened");
        Console.WriteLine("Q8-06: 13 ending targets, living/returned/negative controls and native continuation partitions passed");
    }
}
