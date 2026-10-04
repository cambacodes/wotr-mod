using System;
using System.Linq;
using System.Text.Json;
using Tirabade;

// E-Q7-30: unsupported retrospective actions are retired; the existing native interruption is retained.
internal static class WenduagNativeMomentInventoryTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string W = "wenduag.trickster.";
        const string E = Rules.WenduagEchoPrefix;
        // Serialized native evidence for the existing adapter's one reviewed dispatch.
        // This verifies the hook contract offline; it does not execute Unity's Kill/custody actions.
        const string dialog = "World/Dialogs/Companions/CompanionQuests/Lann/Q2BadBlood/MongrelsDefeated/";
        const string cutscene = "World/Cutscenes/AlushinyrraHigherCity/LannQ2_WenduagAttackAndDie/";
        var cue = PresencePlacementManifestTests.NativeRecord(dialog + "Cue_0001.jbp");
        var action = PresencePlacementManifestTests.NativeRecord(cutscene + "CommandAction.jbp");
        var sequence = PresencePlacementManifestTests.NativeRecord(cutscene + "LannQ2_WenduagAttackAndDie.jbp");
        check(cue.GetProperty("AssetId").GetString() == "c3ca34383f9ee3a4e9908ce68a2e828b"
            && cue.GetProperty("Data").GetProperty("OnStop").GetProperty("Actions").GetArrayLength() == 1
            && cue.GetProperty("Data").GetProperty("OnStop").GetProperty("Actions")[0].GetProperty("m_Cutscene").GetString()
                == "!bp_1199b669674bce842db3e128c938d00a",
            "E-Q7-30: reviewed native dispatch no longer plays the verified death sequence");
        var actions = action.GetProperty("Data").GetProperty("Action").GetProperty("Actions");
        check(action.GetProperty("AssetId").GetString() == "e25887bed0b17944f76b1f87c9f60abb"
            && actions.EnumerateArray().Select(a => a.GetProperty("$type").GetString()!.Split(", ").Last())
                .SequenceEqual(new[] { "DetachBuff", "SwitchFaction", "Kill" })
            && actions[2].GetProperty("Target").GetProperty("m_Companion").GetString() == "!bp_ae766624c03058440a036de90a7f2009"
            && actions[2].GetProperty("Killer").GetProperty("m_Companion").GetString() == "!bp_cb29621d99b902e4da6f5d232352fbda"
            && actions[2].GetProperty("RemoveExp").GetBoolean(),
            "E-Q7-30: original native Kill target/killer/action order differs");
        var tracks = sequence.GetProperty("Data").GetProperty("m_Tracks");
        check(tracks.GetArrayLength() == 3 && tracks[2].GetProperty("m_Commands").EnumerateArray().Select(c => c.GetString())
            .SequenceEqual(new[] { "!bp_791c6e19471770249833ca4dbc68aadf", "!bp_e25887bed0b17944f76b1f87c9f60abb" }),
            "E-Q7-30: reviewed native attack/death track differs");
        foreach (var pair in new[] { ("abyss.fall", 4), ("street.fall", 5) })
        {
            var scene = story.Scenes.Single(s => s.Id == W + pair.Item1);
            check(scene.Requires.Contains("trickster.ever") && scene.Forbids.Contains("trickster.ever"),
                "E-Q7-30: unsupported fall replay was not retired: " + scene.Id);
            foreach (bool prepared in new[] { false, true })
            foreach (bool page in new[] { false, true })
            foreach (string path in new[] { "trickster", "legend", "angel" })
            {
                var state = new Snapshot { Chapter = pair.Item2, Hour = 10000, Area = Rules.NurahCapital };
                state.Flags.UnionWith(scene.Requires.Concat(scene.RequiresAnyGroups.Select(g => g[0])));
                state.Flags.Add(path);
                if (path != "trickster") state.Flags.Remove("trickster.now");
                if (prepared) state.Flags.UnionWith(new[] { W + "fall_agreed", W + "primed", W + "bought" });
                else state.Flags.Remove(W + "fall_agreed");
                if (page) state.Flags.Add("trickster.foresight.accepted");
                Rules.Complete(story, state);
                foreach (string flag in state.Flags) state.Times[flag] = 0;
                check(!Rules.Available(story, scene, state), "E-Q7-30: completed encounter can be rescued retrospectively");
                var reload = JsonSerializer.Deserialize<Snapshot>(JsonSerializer.Serialize(state,
                    new JsonSerializerOptions { IncludeFields = true }), new JsonSerializerOptions { IncludeFields = true })!;
                check(!Rules.Available(story, scene, reload), "E-Q7-30: reload reopened retired replay");
            }
            // Mutation control: the otherwise legitimate historical fixture must expose the defect if retirement is removed.
            var gate = scene.Forbids;
            var witness = new Snapshot { Chapter = pair.Item2, Hour = 10000, Area = Rules.NurahCapital };
            witness.Flags.UnionWith(scene.Requires.Concat(scene.RequiresAnyGroups.Select(g => g[0])));
            witness.Flags.Add("trickster");
            Rules.Complete(story, witness);
            foreach (string flag in witness.Flags) witness.Times[flag] = 0;
            try {
                scene.Forbids = gate.Where(f => f != "trickster.ever").ToArray();
                check(Rules.Available(story, scene, witness), "E-Q7-30: negative fixture cannot detect removed retirement gate");
            } finally { scene.Forbids = gate; }
        }
        var pickup = story.Scenes.Single(s => s.Id == E + "pickup");
        var preparation = story.Scenes.Single(s => s.Id == E + "prepare");
        check(!Rules.IsRemote(pickup) && pickup.DelayHours == 0 && pickup.ContactUnit == "ae766624c03058440a036de90a7f2009"
            && pickup.Requires.Contains(E + "casualty_available") && pickup.Requires.Contains(E + "ready"),
            "E-Q7-30: immediate pickup lost current original/casualty/preparation evidence");
        check(preparation.Requires.Contains(E + "adapter_available") && preparation.Requires.Contains("foresight.page_taken"),
            "E-Q7-30: preparation no longer requires its existing adapter/page contract");
        check(story.SelectedAnswers[E + "journey"] == "ddbcf384507535043a1ad5ad8ad8ea15",
            "E-Q7-30: custody journey is not the actual native departure answer");
        var stateWithoutIntervention = new Snapshot { Chapter = 4, Hour = 10000 };
        stateWithoutIntervention.Flags.UnionWith(new[] { "trickster", "wenduag.dead_any", "wenduag.abyss_fell", E + "ready", "trickster.foresight.accepted" });
        Rules.Complete(story, stateWithoutIntervention);
        check(!Rules.Available(story, pickup, stateWithoutIntervention), "E-Q7-30: preparation/page alone fabricated a casualty");
        Console.WriteLine("PASS: E-Q7-30 both fall replays retired across preparation/page/path/reload histories; retirement mutation detected.");
    }
}
