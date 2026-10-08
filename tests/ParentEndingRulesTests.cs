using System;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class ParentEndingRulesTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var json = new JsonSerializerOptions { IncludeFields = true };
        Story Copy() => JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(story, json), json)!;
        Snapshot State(params string[] flags)
        {
            var state = new Snapshot { Chapter = 5, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(flags);
            return state;
        }
        const string owner = "Epilogue";
        const string page = "951e4432cf844a36a8a222b27589fb43";
        const string pairedPage = "5c95d8e3fa4f3b44896914987cb04b0b";
        const string invitation = "minachiv.invitation_kept";
        const string arrival = "minachiv.arrival_kept";
        const string minagho = "minagho.dead";
        const string chivarro = "chivarro.dead";
        check(story.ParentEpilogueEdits.Count == 35 && story.ParentEpilogueLossRules.Count == 3,
            "Test candidate does not contain the reviewed 35-cue/3-loss contract.");
        Rules.Validate(story);
        var roundTrip = Copy();
        Rules.Validate(roundTrip);
        check(JsonSerializer.Serialize(story.ParentEpilogueEdits, json) == JsonSerializer.Serialize(roundTrip.ParentEpilogueEdits, json)
            && JsonSerializer.Serialize(story.ParentEpilogueLossRules, json) == JsonSerializer.Serialize(roundTrip.ParentEpilogueLossRules, json),
            "Typed parent metadata lost information on JSON round trip.");

        foreach (var pair in story.ParentEpilogueEdits)
        {
            var unplayed = State();
            check(Rules.ParentEndingCue(story, page, pair.Key, owner, unplayed, out var text) == ParentEndingSelection.Original && text == null,
                "Parent-only save acquired an alternate.");
            var invited = State("trickster", invitation);
            var expected = pair.Value.Requires.Contains(arrival) ? ParentEndingSelection.Original
                : pair.Value.Text == null ? ParentEndingSelection.Suppress : ParentEndingSelection.Ordinary;
            check(Rules.ParentEndingCue(story, page, pair.Key, owner, invited, out text) == expected,
                "Invitation was confused with played arrival: " + pair.Key);
            var arrived = State("trickster", invitation, arrival);
            expected = pair.Value.Text == null ? ParentEndingSelection.Suppress : ParentEndingSelection.Ordinary;
            check(Rules.ParentEndingCue(story, page, pair.Key, owner, arrived, out text) == expected
                && (expected == ParentEndingSelection.Suppress ? text == null : ReferenceEquals(text, pair.Value)),
                "Earned cue policy lost exact private text or suppression: " + pair.Key);
            check(Rules.ParentEndingCue(story, page, pair.Key, "AeonEpilogue", arrived, out text) == ParentEndingSelection.Original && text == null,
                "Ordinary edit leaked into erased history.");
            foreach (string path in new[] { "none", "trickster.failed", "dragon", "legend", "swarm" })
            {
                var offPath = State(invitation, arrival, "trickster.ever");
                if (path == "none") offPath.Flags.Remove("trickster");
                else offPath.Flags.UnionWith(new[] { path, "trickster.failed" });
                check(Rules.ParentEndingCue(story, page, pair.Key, owner, offPath, out text) == ParentEndingSelection.Original && text == null,
                    "Ordinary edit leaked off the live Trickster path: " + path + "/" + pair.Key);
            }
            check(arrived.Flags.SetEquals(new[] { "trickster", invitation, arrival }), "Policy wrote progress or native history.");
        }

        foreach (var rule in story.ParentEpilogueLossRules)
        foreach (bool completed in new[] { false, true })
        {
            string replacement = rule.ReplacementScenes.Single(id => id.EndsWith("_completed", StringComparison.Ordinal) == completed);
            var state = State(rule.Requires);
            if (state.Has(chivarro)) state.Flags.Add("chivarro.exile_objective_done");
            if (completed) HouseholdTests.Earn(story, state, "minagho_chivarro.payoff.ordinary");
            Rules.Complete(story, state);
            check(ReferenceEquals(Rules.ParentEndingLoss(story, owner, state), rule), "Available loss replacement failed to earn arbitration.");
            check(Rules.ParentEndingLoss(story, "AeonEpilogue", state) == null, "Ordinary death erased Aeon history.");
            foreach (string target in rule.SuppressPages)
                check(Rules.ParentEndingPageSuppressed(story, target, owner, state), "Earned page suppression was lost.");
            foreach (string target in rule.SuppressCues)
            {
                var selection = Rules.ParentEndingCue(story, page, target, owner, state, out var alternate);
                bool survivor = rule.SurvivorAlternates.TryGetValue(target, out var expected);
                check(selection == (survivor ? ParentEndingSelection.Survivor : ParentEndingSelection.Suppress)
                    && (survivor ? ReferenceEquals(alternate, expected) : alternate == null), "Survivor/suppression precedence failed: " + target);
            }
            // A selected loss page must precede any constituent cue alternative.
            foreach (var target in rule.SurvivorAlternates.Keys)
                check(Rules.ParentEndingCue(story, pairedPage, target, owner, state, out var text) == ParentEndingSelection.Suppress && text == null,
                    "Survivor bypassed a suppressed containing page.");
            foreach (string path in new[] { "none", "trickster.failed", "dragon", "legend", "swarm" })
            foreach (bool seen in new[] { false, true })
            {
                var offPath = State(state.Flags.ToArray());
                offPath.Flags.Add("trickster.ever");
                if (path == "none") offPath.Flags.Remove("trickster");
                else offPath.Flags.UnionWith(new[] { path, "trickster.failed" });
                if (seen) offPath.Flags.Add(replacement);
                check(Rules.ParentEndingLoss(story, owner, offPath) == null,
                    "Loss rule leaked off the live Trickster path: " + path + "/" + rule.Id + "/" + seen);
                foreach (string target in rule.SuppressPages)
                    check(!Rules.ParentEndingPageSuppressed(story, target, owner, offPath), "Off-path loss suppressed a parent page: " + target);
                foreach (string target in rule.SuppressCues)
                    check(Rules.ParentEndingCue(story, page, target, owner, offPath, out var text) == ParentEndingSelection.Original && text == null,
                        "Off-path loss changed a parent cue: " + target);
            }
            state.Flags.Add("minachiv.closed");
            check(Rules.ParentEndingLoss(story, owner, state) == null, "Unavailable and unseen replacement removed parent output.");
            state.Flags.Add(replacement);
            check(ReferenceEquals(Rules.ParentEndingLoss(story, owner, state), rule), "Already played replacement was forgotten.");
            foreach (string death in rule.Requires.Where(flag => flag == minagho || flag == chivarro))
            {
                state.Flags.Remove(death);
                check(Rules.ParentEndingLoss(story, owner, state) == null, "Seen loss scene substituted for current death: " + death);
                state.Flags.Add(death);
            }
            state.Flags.Remove(invitation);
            check(Rules.ParentEndingLoss(story, owner, state) == null, "Seen loss scene substituted for earned invitation.");
        }
        var sacrifice = State(invitation, "sacrifice");
        check(Rules.ParentEndingLoss(story, owner, sacrifice) == null && !Rules.ParentEndingPageSuppressed(story, page, owner, sacrifice),
            "Commander sacrifice was mistaken for either woman's death.");
        var noReplacement = Copy();
        noReplacement.Scenes.RemoveAll(scene => story.ParentEpilogueLossRules.SelectMany(rule => rule.ReplacementScenes).Contains(scene.Id));
        var missing = State(invitation, minagho, chivarro, "minachiv.ending_both_lost");
        check(Rules.ParentEndingLoss(noReplacement, owner, missing) == null, "Absent replacement was trusted because its name was saved.");
        var legacy = Copy();
        legacy.ParentEpilogueEdits.Clear(); legacy.ParentEpilogueLossRules.Clear();
        Rules.Validate(legacy);
        check(Rules.ParentEndingCue(legacy, page, story.ParentEpilogueEdits.Keys.First(), owner, missing, out _) == ParentEndingSelection.Original
            && !Rules.ParentEndingPageSuppressed(legacy, page, owner, missing), "Absent metadata changed legacy behavior.");

        void Reject(Action<Story> change, string reason)
        {
            var invalid = Copy(); change(invalid); bool rejected = false;
            try { Rules.Validate(invalid); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, reason);
        }
        Reject(s => { var edit = s.ParentEpilogueEdits.First(); s.ParentEpilogueEdits.Remove(edit.Key); s.ParentEpilogueEdits.Add("minagho.alias", edit.Value); }, "Non-GUID cue alias accepted.");
        Reject(s => s.ParentEpilogueLossRules[0].SuppressPages[0] = Guid.Empty.ToString("N"), "Empty native page identity accepted.");
        Reject(s => s.ParentEpilogueLossRules[0].SuppressCues = new[] { "bad-guid" }, "Malformed suppression identity accepted.");
        Reject(s => s.ParentEpilogueEdits.Values.First().Requires = new[] { "trickster", "minachiv.made_up" }, "Unknown gate alias accepted.");
        Reject(s => { s.ParentEpilogueEdits.Values.First(edit => edit.Requires.Contains(invitation)).Requires = new[] { "trickster", invitation, "minagho.ran_conscience" };
            s.Etudes["minagho.ran_conscience"] = "bad-guid"; }, "Referenced native alias with malformed GUID accepted.");
        Reject(s => s.Etudes[invitation] = "3b8c0801d5e9a694b848ee13564d2ad7", "Native alias manufactured authored invitation.");
        foreach (string earned in new[] { invitation, arrival })
            Reject(s => {
                foreach (var choice in s.Scenes.SelectMany(scene => scene.Nodes).SelectMany(node => node.Choices))
                    choice.Set = choice.Set.Where(flag => flag != earned).ToArray();
                s.Etudes[earned] = "3b8c0801d5e9a694b848ee13564d2ad7";
            }, "Native alias replaced removed authored evidence: " + earned);
        Reject(s => s.Etudes[minagho] = s.Etudes["sacrifice"], "Commander sacrifice aliased to Minagho death.");
        Reject(s => s.ParentEpilogueEdits.Values.First().Owner = "AeonEpilogue", "Ordinary edit entered Aeon scope.");
        Reject(s => s.ParentEpilogueEdits["c47829fba057400c8e0279990be3d25e"].Requires = new[] { "trickster", invitation }, "Reunion rewrite accepted invitation without arrival.");
        Reject(s => s.ParentEpilogueEdits.Values.First().Forbids = new[] { minagho, "trickster.failed", "dragon", "legend", "swarm" }, "Ordinary replacement omitted Chivarro's death.");
        Reject(s => s.ParentEpilogueEdits.Values.Last().LocalizedKey = s.ParentEpilogueEdits.Values.First().LocalizedKey, "Duplicate private key accepted.");
        Reject(s => s.ParentEpilogueEdits.Values.First().LocalizedKey = s.ParentEpilogueEdits.Values.First().ParentKey, "Original localization mutation accepted.");
        Reject(s => s.ParentEpilogueLossRules[0].ReplacementScenes = new[] { "minachiv.missing" }, "Missing replacement scene accepted.");
        Reject(s => s.Scenes.Single(scene => scene.Id == s.ParentEpilogueLossRules[0].ReplacementScenes[0]).Owner = "AeonEpilogue", "Wrong-owner loss replacement accepted.");
        Reject(s => s.Scenes.Single(scene => scene.Id == s.ParentEpilogueLossRules[0].ReplacementScenes[0]).Requires = new[] { "trickster", invitation }, "Loss replacement omitted current death evidence.");
        Reject(s => s.ParentEpilogueLossRules[0].Requires = new[] { "trickster", invitation, "sacrifice" }, "Sacrifice-only loss rule accepted.");
        Reject(s => s.ParentEpilogueLossRules[0].Id = s.ParentEpilogueLossRules[1].Id, "Duplicate loss rule identity accepted.");
        Reject(s => s.ParentEpilogueLossRules.Add(new ParentEndingLossRule {
            Id = "overlap", Owner = owner, Requires = s.ParentEpilogueLossRules[0].Requires,
            Forbids = s.ParentEpilogueLossRules[0].Forbids,
            ReplacementScenes = s.ParentEpilogueLossRules[0].ReplacementScenes, SuppressPages = new[] { page } }), "Ambiguous co-applicable loss rules accepted.");
        Reject(s => s.ParentEpilogueLossRules[2].SuppressCues = Array.Empty<string>(), "Survivor target outside suppression set accepted.");
        Reject(s => s.ParentEpilogueLossRules[2].SurvivorAlternates.Values.First().Text = null, "Survivor suppression masqueraded as replacement prose.");
        Reject(s => s.ParentEpilogueLossRules[2].SurvivorAlternates.Values.First().Text = " ", "Empty survivor text accepted.");
        Reject(s => s.ParentEpilogueLossRules[2].Requires = new[] { "trickster", invitation, chivarro, minagho }, "Contradictory survivor death scope accepted.");
    }
}
