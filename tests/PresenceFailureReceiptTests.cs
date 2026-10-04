using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class PresenceFailureReceiptTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        if (!story.PresenceFailureReceipts.ContainsKey("gesmerha.presence")) return;
        const string name = "gesmerha.presence";
        var receipt = story.PresenceFailureReceipts[name];
        var present = story.Presences[name];
        var failure = new PresenceObservation { AreaLoaded = true, AnchorResolved = false };
        var unpaid = PresenceBootstrapInventoryTests.Fresh(story, 3, "gesmerha.dead");
        check(!Rules.RecordPresenceFailure(story, name, unpaid, failure), "Unpaid receipt recorded");
        // Execute the paid return, then actually attempt placement beside the absent smith.
        var initial = PresenceBootstrapInventoryTests.Fresh(story, 3, "gesmerha.feared_hands");
        initial = PresenceBootstrapInventoryTests.Play(story, "gesmerha.trickster.dead.commission", initial, "gesmerha.trickster.primed", check);
        initial.Flags.Add("gesmerha.dead"); // actual native ambush outcome, after the commission
        PresenceBootstrapInventoryTests.Recompute(story, initial);
        initial = PresenceBootstrapInventoryTests.Later(story, initial);
        var state = PresenceBootstrapInventoryTests.Play(story, "gesmerha.trickster.dead.unfinished_work", initial, "gesmerha.trickster.returned", check);
        check(Rules.PresenceWanted(present, state), "Gesmerha earned return not wanted");
        check(Rules.PlanPresence(present, true, failure).Contains(PresenceStep.Blocked), "Missing smith placement not attempted");
        check(Rules.RecordPresenceFailure(story, name, state, failure), "Observed eligible failure not recorded");
        check(!Rules.RecordPresenceFailure(story, name, state, new PresenceObservation()), "Unloaded receipt recorded");
        check(!Rules.RecordPresenceFailure(story, name, state, new PresenceObservation { AreaLoaded = true, AnchorResolved = true }), "Success records failure");
        var closed = Program.Copy(state); closed.Flags.Add("gesmerha.closed"); Rules.Complete(story, closed);
        check(!Rules.RecordPresenceFailure(story, name, closed, failure), "Closed receipt recorded");
        // Save exactly the runtime SettingsList receipt value, travel, reload into a fresh native snapshot.
        string saveKey = Rules.PresenceFailureSaveKey(name);
        var saved = new Dictionary<string, string> { [saveKey] = "1" };
        string save = JsonSerializer.Serialize(saved);
        foreach (bool mourned in new[] { false, true })
        {
            var finale = new Snapshot { Chapter = 6, Hour = state.Hour + 2000, Area = "threshold", Flags = new HashSet<string>(state.Flags) };
            finale.Flags.ExceptWith(story.Derived.Keys);
            finale.Flags.Remove(Rules.PresenceFailedFlag(name));
            if (mourned) finale.Flags.Add("sacrifice");
            var loaded = JsonSerializer.Deserialize<Dictionary<string, string>>(save)!;
            if (loaded.TryGetValue(saveKey, out var value) && value == "1") finale.Flags.Add(receipt.Flag);
            Rules.Complete(story, finale);
            check(finale.Has("gesmerha.trickster.late_committed"), "Receipt commitment lost on travel/load");
            string ending = "gesmerha.trickster.epilogue." + (mourned ? "commit_mourned" : "commit");
            check(Rules.Available(story, story.Scenes.Single(s => s.Id == ending), finale), "Receipt finale withheld: " + ending);
            foreach (var scene in story.Scenes.Where(s => s.Id.StartsWith("gesmerha.trickster.epilogue.unvisited", StringComparison.Ordinal)))
                check(!Rules.Available(story, scene, finale), "Observed failure selects neglected visit: " + scene.Id);
            Console.WriteLine("eng7-l06 rendered after failure/travel/reload " + ending + ": " + story.Scenes.Single(s => s.Id == ending).Nodes[0].Text);
            foreach (string lost in new[] { "gesmerha.closed", "gesmerha.trickster.declined" })
            {
                var refused = Program.Copy(finale); refused.Flags.Add(lost); Rules.Complete(story, refused);
                check(!Rules.Available(story, story.Scenes.Single(s => s.Id == ending), refused), "Receipt overrides refusal " + lost);
            }
            var unattempted = Program.Copy(finale); unattempted.Flags.Remove(receipt.Flag); PresenceBootstrapInventoryTests.Recompute(story, unattempted);
            check(!Rules.Available(story, story.Scenes.Single(s => s.Id == ending), unattempted), "Never-visited finale receives failure outcome");
        }
    }
}
