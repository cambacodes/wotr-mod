using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class HouseholdEngineTests
{
    internal static void Run(Story exported, Action<bool, string> check)
    {
        var story = new Story { Relationships = exported.Relationships, Derived = exported.Derived,
            DerivedOpenRoutes = exported.DerivedOpenRoutes, DerivedForbids = exported.DerivedForbids,
            DepartureEpochs = exported.DepartureEpochs, Latches = exported.Latches,
            RestAllowances = exported.RestAllowances, SeatWomen = new Dictionary<string, SeatWoman>(exported.SeatWomen) };
        Scene Entry(string id, string? allowance = "household.pair") => new Scene {
            Id = id, Owner = "Seelah", Relationship = "household", MinChapter = 3, MaxChapter = 5,
            InteractionHub = Rules.TableHub, RestAllowance = allowance,
            Participants = new[] { "seelah", "wenduag" }, Pair = new[] { "seelah", "wenduag" }
        };
        Snapshot State() {
            var state = new Snapshot { Chapter = 5, Hour = 1000 };
            state.Flags.UnionWith(new[] { "trickster", "trickster.ever", "trickster.foresight.accepted",
                exported.Relationships["seelah"].CommittedFlag, exported.Relationships["wenduag"].CommittedFlag });
            HouseholdTests.Earn(story, state, "seelah.payoff.ordinary");
            HouseholdTests.Earn(story, state, "wenduag.payoff.ordinary");
            Rules.Complete(story, state);
            return state;
        }
        story.Counts["household.cap.ch5.arcs"] = new CountSpec { Of = new[] { "test.started" }, Min = 1, Chapters = new[] { 5 } };
        var capState = new Snapshot { Chapter = 5 }; capState.Flags.Add("test.started"); Rules.Complete(story, capState);
        check(capState.Has("household.cap.ch5.arcs"), "H3: a chapter cap was not evaluated on the current snapshot.");
        capState = new Snapshot { Chapter = 3 }; capState.Flags.Add("test.started"); Rules.Complete(story, capState);
        check(!capState.Has("household.cap.ch5.arcs"), "H3: Ch5 cap leaked into another chapter.");
        var a = Entry("test.a"); var b = Entry("test.b");
        var p = Entry("test.p", "household.protected"); var q = Entry("test.q", "household.protected");
        var r = Entry("test.r", "household.protected"); var free = Entry("test.free", null);
        q.Chapters = new[] { 5 }; q.MaxChapter = 6; // Its last allowed chapter, rather than the broad bound, is the deadline.
        story.Scenes.AddRange(new[] { a, b, p, q, r, free });
        var state = State();
        check(Rules.TableEntries(story, state).Select(s => s.Id).SequenceEqual(new[] { p.Id, q.Id, r.Id, a.Id, b.Id, free.Id }),
            "Protected Table entries do not precede optional entries in authored order.");
        check(Rules.Available(story, a, state) && Rules.Available(story, b, state), "T1/T8: first visit has no allowance.");
        a.Nodes.Add(new Node { Id = "start", Text = "Test", Choices = new List<Choice> { new Choice { Abort = true } } });
        var aborted = Program.Walk(a, state).Single();
        check(aborted.RestSpent.Count == 0 && !aborted.Has(a.Id) && Rules.Available(story, b, aborted), "T5: abort spent the allowance.");
        var before = Program.Copy(state);
        check(Rules.SpendRestAllowance(story, a, state), "T1: completion did not spend.");
        state.Flags.Add(a.Id);
        check(!Rules.SpendRestAllowance(story, a, state) && state.RestSpent["household.pair"] == 1, "T3: completion spent twice.");
        check(!Rules.Available(story, b, state) && Rules.Available(story, free, state), "T1/T6: incorrect withdrawal.");
        var options = new JsonSerializerOptions { IncludeFields = true };
        var reload = JsonSerializer.Deserialize<Snapshot>(JsonSerializer.Serialize(state, options), options)!;
        check(!Rules.Available(story, b, reload) && Rules.Available(story, b, before), "T3: reload refunded or polluted an earlier save.");
        Rules.RestFinished(state, false);
        check(!Rules.Available(story, b, state), "T2: interrupted rest refunded allowance.");
        check(Rules.SpendRestAllowance(story, p, state) && Rules.SpendRestAllowance(story, q, state)
            && !Rules.Available(story, r, state), "T4: protected allowance does not allow exactly two alongside a pair.");
        b.DelayHours = 48; b.Requires = new[] { "test.witness" };
        state.Flags.Add("test.witness"); state.Times["test.witness"] = state.Hour - 48;
        check(!Rules.Available(story, b, state), "T7: elapsed delay bypassed allowance.");
        Rules.RestFinished(state, true);
        state.Times["test.witness"] = state.Hour;
        check(!Rules.Available(story, b, state), "T7: rest bypassed delay.");
        state.Hour += 48;
        check(Rules.Available(story, b, state), "T1/T7: successful rest and elapsed delay did not restore access.");
        foreach (var participant in a.Participants)
        {
            var rel = story.Relationships[participant];
            foreach (var loss in rel.UnavailableFlags.Concat(new[] { rel.ClosedFlag }))
            {
                var absent = State(); absent.Flags.Add(loss); Rules.Complete(story, absent);
                check(!Rules.Available(story, a, absent), "A1: participant still staged with " + loss);
                if (rel.UnavailableOverrides.TryGetValue(loss, out var back))
                {
                    // The legacy paid execution copy answers that execution;
                    // a historical return alone cannot answer arbitrary dead_any.
                    if (participant == "wenduag" && loss == "wenduag.dead_any") absent.Flags.Add("wenduag.killed");
                    HouseholdTests.Earn(story, absent, back); Rules.Complete(story, absent);
                    check(Rules.Available(story, a, absent), "A2: earned return failed for " + loss);
                    absent.Flags.Add(rel.ClosedFlag); Rules.Complete(story, absent);
                    check(!Rules.Available(story, a, absent), "A2: return bypassed deliberate closure.");
                }
            }
        }
        state = State(); state.Flags.Add("seelah.harem.stance.own_house");
        check(Rules.Available(story, a, state), "A3: own-house partner lost Table access.");
        var noCommit = new Snapshot { Chapter = 5, Hour = 1000 };
        noCommit.Flags.UnionWith(new[] { "trickster", "seelah.committed" }); Rules.Complete(story, noCommit);
        check(!Rules.Available(story, a, noCommit), "A1: ineligible participant was staged.");
        var noEligibility = Entry("test.friendship", null); noEligibility.Pair = Array.Empty<string>();
        noEligibility.Participants = new[] { "ember" };
        check(!Rules.Available(story, noEligibility, State()), "A1: a route without harem eligibility was staged.");
        var realSolo = Entry("test.minagho", null); realSolo.Pair = Array.Empty<string>();
        realSolo.Participants = new[] { "minagho_chivarro" }; realSolo.ParticipantWomen = new[] { "minagho" };
        var separated = State(); separated.Flags.UnionWith(new[] { "minachiv.complete", "minagho_chivarro.trickster.minagho_in",
            "minagho_chivarro.trickster.chivarro_in", "minachiv.before_the_last_road", "minachiv.future_two", "chivarro.dead" }); Rules.Complete(story, separated);
        check(Rules.Available(story, realSolo, separated), "A4: native Chivarro death withdrew a Minagho-only scene.");
        realSolo.ParticipantWomen = new[] { "chivarro" };
        check(!Rules.Available(story, realSolo, separated), "A4: native-dead Chivarro appeared without a return.");
        separated.Flags.Add("minagho_chivarro.trickster.returned_chivarro");
        // eng7-l05: current readers are recomputed in a fresh runtime observation after an earned return.
        separated.Flags.ExceptWith(story.Derived.Keys); Rules.Complete(story, separated);
        check(Rules.Available(story, realSolo, separated), "A4: Chivarro's native-death return did not restore her visit.");
        story.SeatWomen["minagho"] = new SeatWoman { Relationship = "minagho_chivarro", UnavailableFlags = new[] { "minagho.absent" } };
        story.SeatWomen["chivarro"] = new SeatWoman { Relationship = "minagho_chivarro", UnavailableFlags = new[] { "chivarro.absent" },
            UnavailableOverrides = new Dictionary<string, string> { ["chivarro.absent"] = "chivarro.returned" } };
        var solo = Entry("test.solo", null); solo.Pair = Array.Empty<string>();
        solo.Participants = new[] { "minagho_chivarro" }; solo.ParticipantWomen = new[] { "minagho" };
        state = State(); HouseholdTests.Earn(story, state, "minagho_chivarro.payoff.ordinary"); state.Flags.Add("chivarro.absent"); Rules.Complete(story, state);
        check(Rules.Available(story, solo, state), "A4: absent Chivarro withdrew Minagho-only scene.");
        solo.ParticipantWomen = new[] { "chivarro" };
        check(!Rules.Available(story, solo, state), "A4: unavailable seat woman was staged.");
        state.Flags.Add("chivarro.returned");
        check(Rules.Available(story, solo, state), "A4: seat woman's earned return failed.");
        var visit = Entry("test.visit", null); visit.Remote = true; visit.Kind = "visit";
        check(!Rules.IsTableScene(visit), "Unsanctioned remote scene entered Table.");
        visit.TableHosted = true; story.Scenes.Add(visit);
        check(Rules.IsTableScene(visit) && Rules.TableEntries(story, State()).Contains(visit)
            && !Rules.IsMailbagLetter(visit) && !Rules.NextRemoteBag(story, State(), new Dictionary<string, int>(), 3).Contains(visit),
            "TableHosted visit did not remain exclusively selectable at Table.");
        var offer = exported.Scenes.Single(s => s.Id == "household.table.offered");
        state = new Snapshot { Chapter = 3, Hour = 1000 }; state.Flags.UnionWith(new[] { "trickster", "seelah.committed" }); Rules.Complete(story, state);
        check(!state.Has("household.stance_eligible") && !Rules.Available(story, offer, state), "Harem opened without Shyka's page.");
        state.Flags.Add("trickster.foresight.accepted"); HouseholdTests.Earn(story, state, "seelah.payoff.ordinary"); Rules.Complete(story, state);
        check(state.Has("household.stance_eligible") && Rules.Available(story, offer, state), "Page did not open stance eligibility.");
        state = new Snapshot { Chapter = 3, Hour = 1000 }; state.Flags.UnionWith(new[] { "trickster.foresight.accepted", "seelah.committed" }); Rules.Complete(story, state);
        check(!state.Has("household.stance_eligible"), "Page opened household off current Trickster path.");
    }
}
