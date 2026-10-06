using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class MinaghoChivarroStanceTests
{
    private const string P = "minagho_chivarro.trickster.";
    private const string S = "minagho_chivarro.partner_stance.";

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Find(string id) => story.Scenes.Single(s => s.Id == id);
        Snapshot World(params string[] flags)
        {
            var w = new Snapshot { Chapter = 5, Hour = 5000, Area = "2570015799edf594daf2f076f2f975d8",
                CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000 } };
            w.Flags.UnionWith(new[] { "chapter_later", "trickster", "trickster.ever", "minachiv.started" });
            w.Flags.UnionWith(flags);
            w.AvailableContacts.UnionWith(new[] { "b7e819e2a9bb0804abcbffe8e7d91ba6", "565ccab37e2475742b043ec912a750fa" });
            Rules.Complete(story, w);
            foreach (var flag in w.Flags) w.Times[flag] = 0;
            return w;
        }
        var road = Find(P + "after.before_the_last_road");
        var ready = World(P + "minagho_in", P + "chivarro_in", P + "reunited", P + "tprev.house",
                          P + "primed", P + "cost.baphomet_debtor", "minagho.spared.latched");
        check(Rules.Available(story, road, ready), "Stance fixture bypasses commitment eligibility.");
        var shared = Program.WalkVia(road, ready, "terms", 0).Where(w => w.Has("minachiv.complete")).ToArray();
        check(shared.Length == 1 && shared[0].Has(S + "share") && shared[0].Has(P + "night.pair")
              && !shared[0].Has(S + "secret") && !shared[0].Has(S + "exclusive"), "Original commitment lost negotiated sharing or its night.");
        foreach (var (woman, demandIndex, affairIndex, morning) in new[] {
            ("minagho", 4, 5, "alone.minagho_spared_morning"),
            ("chivarro", 6, 7, "alone.chivarro_morning") })
        {
            var demands = Program.WalkVia(road, ready, "terms", demandIndex);
            check(demands.Any(w => w.Has(S + "exclusive") && w.Has(S + "cooled") && w.Has("minachiv.closed")
                                  && !w.Has("minachiv.complete")), "Exclusive demand grants a commitment: " + woman);
            check(demands.Any(w => w.Has(S + "share") && w.Has("minachiv.complete") && !w.Has(S + "exclusive")),
                  "Exclusive refusal has no honest backdown: " + woman);
            var affair = Program.WalkVia(road, ready, "terms", affairIndex).Single(w => w.Has(S + "secret"));
            check(affair.Has("minachiv.future_" + woman) && affair.Has(P + "night." + woman)
                  && !affair.Has("minachiv.future_two") && !affair.Has(S + "share"), "Affair grants the unchosen pair: " + woman);
            affair.Hour += 200;
            var dawn = Find(P + morning);
            check(Rules.Available(story, dawn, affair), "Secret has no existing morning: " + woman);
            var exposed = Program.Walk(dawn, affair);
            check(exposed.Count > 0 && exposed.All(w => w.Has(S + "exposed") && w.Has(S + "cooled") && w.Has("minachiv.closed") && w.Has(P + "cost.morning_after")),
                  "Discovery is avoidable or forgiven without fallout: " + woman);
            check(exposed.All(w => Rules.Available(story, Find(P + "epilogue.partner_refused"), w)
                                  && !Rules.Available(story, Find(P + "epilogue." + woman), w)), "Discovery retains the romance ending: " + woman);
        }
        // The letter twin must not show a shared dawn before an affair's
        // discovery. Its original morning remains on the honest contract.
        var letter = Find(P + "after.before_the_last_road_letter");
        var letterReady = World(P + "minagho_in", P + "chivarro_in", P + "reunited", P + "tprev.house",
                                P + "primed", P + "cost.baphomet_debtor", "minagho.spared.latched",
                                "minagho_chivarro.presence.chivarro.failed");
        check(Rules.Available(story, letter, letterReady), "Letter stance fixture bypasses the existing fallback gate.");
        var secretPages = new HashSet<string>();
        var letterOutcomes = Program.Walk(letter, letterReady, (id, w) => { if (w.Has(S + "secret")) secretPages.Add(id); });
        check(secretPages.Contains("stance_morning_route") && !secretPages.Contains("morning")
              && letterOutcomes.Where(w => w.Has(S + "secret")).All(w => w.Has(S + "exposed") && w.Has(S + "cooled") && w.Has(P + "cost.morning_after")),
              "Secret letter commit gets a shared morning before discovery or escapes its fallout.");
        // Late invitations record the same moves without granting the earlier
        // commitment, its payoff, or a call-in before the already-ended rift.
        var late = Find(P + "epilogue.commit");
        check(Rules.Available(story, late, ready), "Late stance fixture bypasses the invitation gate.");
        var lateShare = Program.WalkVia(late, ready, "pair", 0);
        check(lateShare.Count == 1 && lateShare[0].Has(S + "share") && !lateShare[0].Has("minachiv.complete"),
              "Late sharing lacks a recorded stance or grants the earlier commitment.");
        foreach (var (demand, affair) in new[] { (3, 4), (5, 6) })
        {
            var refusedLate = Program.WalkVia(late, ready, "pair", demand);
            check(refusedLate.Count == 1 && refusedLate[0].Has(S + "exclusive") && refusedLate[0].Has(S + "cooled")
                  && refusedLate[0].Has("minachiv.closed") && !refusedLate[0].Has("minachiv.complete"),
                  "Late exclusive demand switches the lover instead of recording her refusal.");
            var exposedLate = Program.WalkVia(late, ready, "pair", affair);
            check(exposedLate.Count == 1 && exposedLate[0].Has(S + "secret") && exposedLate[0].Has(S + "exposed")
                  && exposedLate[0].Has(S + "cooled") && exposedLate[0].Has("minachiv.closed")
                  && !exposedLate[0].Has("minachiv.complete"), "Late affair loses its recorded discovery and consequence.");
        }
        // The paid double died; the captive partner is living, but absent.
        var captive = World(P + "minagho_in", "minagho.spared.latched", "chivarro.dead", "chivarro.exile_objective_done",
                            P + "chivarro_deposit", P + "primed", P + "cost.baphomet_debtor");
        var captiveSolo = Find(P + "alone.minagho_spared");
        check(Rules.Available(story, captiveSolo, captive), "Cellar fixture bypasses the solo gate.");
        var captiveShare = Program.WalkVia(captiveSolo, captive, "terms", 0);
        check(captiveShare.Count == 1 && captiveShare[0].Has(S + "share") && !captiveShare[0].Has(P + "chivarro_in"),
              "Captive partner strands provisional sharing or returns for free.");
        var captiveSecret = Program.WalkVia(captiveSolo, captive, "terms", 4);
        check(captiveSecret.Any(w => w.Has(S + "secret") && !w.Has(S + "exposed") && !w.Has(P + "chivarro_in")),
              "Living captive partner is treated as dead, or discovers the affair bodily.");
        // Her existing waiting road leaves a real partner's whereabouts
        // unresolved. No reply or body may be invented to settle the demand.
        var uncertainSolo = Find(P + "alone.chivarro");
        var uncertain = World(P + "chivarro_in", P + "chivarro_waiting", P + "cost.baphomet_debtor");
        check(Rules.Available(story, uncertainSolo, uncertain), "Unknown-partner fixture bypasses the existing solo gate.");
        var unanswered = new HashSet<string>();
        Program.Walk(uncertainSolo, uncertain, (id, _) => unanswered.Add(id));
        var unknownDemand = Program.WalkVia(uncertainSolo, uncertain, "terms", 4);
        check(unanswered.Contains("stance_0_exclusive_chivarro_unknown")
              && !unanswered.Contains("stance_0_exclusive_chivarro_letter")
              && unknownDemand.Any(w => w.Has(S + "exclusive") && w.Has(S + "cooled")),
              "Unknown partner is treated as dead or supplies a free reply.");
        var unknownAffair = Program.WalkVia(uncertainSolo, uncertain, "terms", 5).Single(w => w.Has(S + "secret"));
        check(!unknownAffair.Has(S + "exposed") && !unknownAffair.Has(P + "minagho_in"),
              "Unknown partner cannot remain a secret without returning for free.");
        var unknownMorning = Program.Walk(Find(P + "alone.chivarro_morning"), unknownAffair);
        check(unknownMorning.Count > 0 && unknownMorning.All(w => !w.Has(S + "exposed") && !w.Has(P + "minagho_in")),
              "Unknown morning invents discovery or a body.");
        var lateWaiting = World(P + "chivarro_in", P + "chivarro_waiting");
        check(Rules.Available(story, late, lateWaiting), "Unknown late-partner fixture bypasses the waiting invitation.");
        var waitingRefusal = Program.WalkVia(late, lateWaiting, "waiting", 2);
        check(waitingRefusal.Count == 1 && waitingRefusal[0].Has(S + "exclusive")
              && waitingRefusal[0].Has(S + "cooled") && !waitingRefusal[0].Has("minachiv.complete"),
              "Late unknown-partner demand grants an exclusive lover or an earlier commitment.");
        var waitingSecret = Program.WalkVia(late, lateWaiting, "waiting", 3);
        check(waitingSecret.Count == 1 && waitingSecret[0].Has(S + "secret")
              && !waitingSecret[0].Has(S + "exposed") && !waitingSecret[0].Has(P + "minagho_in")
              && !waitingSecret[0].Has("minachiv.complete"), "Late unknown partner appears or knows the affair for free.");
        // An absent lover can answer by letter; her existing, earned arrival
        // can also expose the affair. Discovery grants no body of its own.
        var solo = Find(P + "alone.minagho_spared");
        var distant = World(P + "minagho_in", "minagho.spared.latched", P + "chivarro_declined", "chivarro.exiled",
                            P + "primed", P + "cost.baphomet_debtor", "closets.known");
        check(Rules.Available(story, solo, distant), "Distant-partner fixture bypasses the solo gate.");
        var held = Program.Walk(solo, distant).Single(w => w.Has(S + "secret"));
        check(!held.Has(S + "discovery_due") && !held.Has(S + "exposed"), "Distant partner appears to expose the affair.");
        var letterWitness = new HashSet<string>();
        var letterFallout = Program.Walk(Find(P + "alone.minagho_spared_morning"), held, (id, _) => letterWitness.Add(id));
        check(letterWitness.Contains("stance_discovery_letter") && !letterWitness.Contains("stance_discovery")
              && letterFallout.All(w => w.Has(S + "exposed") && w.Has("minachiv.closed") && !w.Has(P + "chivarro_in")),
              "Distant discovery is unreachable or brings the partner back for free.");
        var wardrobe = Find(P + "reunion.wardrobe");
        check(Rules.Available(story, wardrobe, held), "Existing arrival cannot discover the affair.");
        var returned = Program.Walk(wardrobe, held).Where(w => w.Has(P + "reunited")).ToArray();
        check(returned.Length > 0 && returned.All(w => w.Has(P + "chivarro_in") && w.Has(S + "exposed") && w.Has("minachiv.closed")),
              "Arrival fails to preserve the earned body or discovery fallout.");
        var sharedSolo = Program.WalkVia(solo, distant, "terms", 0).Single(w => w.Has(S + "share"));
        var witnessed = new HashSet<string>();
        var sharedReturn = Program.Walk(wardrobe, sharedSolo, (id, _) => witnessed.Add(id));
        check(witnessed.Contains("stance_share_return") && sharedReturn.Any(w => w.Has(P + "reunited") && !w.Has(S + "cooled"))
              && sharedReturn.Any(w => w.Has(P + "reunited") && w.Has(S + "cooled") && w.Has("minachiv.closed")),
              "Returned partner does not answer sharing, or her terms cannot be refused.");
        check(Find("minachiv.lastcall.page").Forbids.Contains(S + "cooled")
              && !Find("minachiv.lastcall.page").ForbidOverrides.ContainsKey(S + "cooled"),
              "Last Call restores a withdrawn welcome.");
        // Adultery must not rewrite the existing service contract.
        var native = Find("minachiv.before_the_last_road");
        var serviceWorld = World("minagho.ran_complete", "minagho.book_three_finished", "chivarro.searching",
                                 "minachiv.chivarro_future_spoken", "minagho.ran_demon", "minachiv.chivarro_lasting");
        check(Rules.Available(story, native, serviceWorld), "Service stance fixture bypasses the original native commitment.");
        var serviceAffair = Program.WalkVia(native, serviceWorld, "service", 4).Where(w => w.Has(S + "secret")).ToArray();
        check(serviceAffair.Length == 1 && serviceAffair[0].Has("minachiv.future_chivarro_service")
              && !serviceAffair[0].Has("minachiv.future_chivarro") && serviceAffair[0].Has(S + "cooled"),
              "Secret service drops the original contract or escapes its discovery.");
        // New canonical changes are invisible to a former Trickster.
        var former = World(P + "minagho_in", P + "chivarro_in", P + "reunited", P + "tprev.house");
        former.Flags.Remove("trickster"); former.Flags.Remove(Rules.TricksterNow);
        check(road.Nodes.Single(n => n.Id == "terms").Choices.Skip(4).Take(4).All(a => !Rules.ChoiceAvailable(a, former)),
              "Partner changes can be initiated off the Trickster path.");
    }
}
