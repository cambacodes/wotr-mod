using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Reviewed polish: decisive positives are played answers, with native campaign
// observations supplied as fixtures. Losses and interruptions are negatives.
internal static class ArsinoePolishTests
{
    private const string Prefix = "arsinoe.trickster.";
    private const string Accepted = Prefix + "late_accepted";
    private const string Declined = Prefix + "late_declined";
    private const string Known = Prefix + "after_war.konomi_known";
    private const string Night = Prefix + "collection_night_shared";
    private const string Grace = Prefix + "cost.rent_grace";
    private const string Called = "arsinoe.lastcall.called";

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        void Refresh(Snapshot s) => LateAcceptanceInventory2Tests.Refresh(story, s);
        Snapshot World(params string[] flags) => LateAcceptanceInventory2Tests.World(story, 3, flags);
        Snapshot Earn(string id, Snapshot before, string receipt, params string[] absent)
            => LateAcceptanceInventory2Tests.Earn(story, check, id, before, receipt, absent);
        Snapshot Changed(Snapshot before, params string[] flags)
        {
            var s = Program.Copy(before); s.Flags.UnionWith(flags); Refresh(s); return s;
        }
        string Text(string id, string node, Snapshot state)
        {
            var n = S(id).Nodes.Single(n => n.Id == node);
            return n.Text + " " + string.Join(" ", Rules.VisibleParagraphs(n, state).Select(p => p.Text));
        }
        Snapshot End(Snapshot before, bool burst, bool closed, string life)
        {
            var s = Program.Copy(before); s.Chapter = 6;
            if (burst) s.Flags.Add("siphon.burst_council");
            if (closed) s.Flags.Add("ending.wound_closed");
            if (life != "alive") s.Flags.Add("sacrifice");
            if (life == "back") s.Flags.Add("ending.trickster");
            Refresh(s); return s;
        }
        var city = Earn("arsinoe_city_on_paper", World("arsinoe.capital"), "arsinoe.picture_invitation");
        var printer = Earn("arsinoe_printers_view", city, "arsinoe.printer_met");
        var roof = Earn("arsinoe_roofs", printer, "arsinoe.courting");
        Snapshot ThroughRepair(Snapshot beginning)
        {
            var state = Program.Copy(beginning);
            foreach (var id in new[] { "arsinoe_first_impression", "arsinoe_hours_of_her_own", "arsinoe_your_hours",
                "arsinoe_borrowed_court", "arsinoe_price_of_an_evening", "arsinoe_courtyard_company", "arsinoe_another_hour",
                "arsinoe_the_unprofitable_hour", "arsinoe_after_rain", "arsinoe_two_doors", "arsinoe_a_stone_in_hand", "arsinoe_the_first_cart" })
                state = Earn(id, state, id);
            return state;
        }
        var beforeTerms = ThroughRepair(roof);
        var open = Earn("arsinoe_what_she_asks", beforeTerms, "arsinoe.open_future", "arsinoe.committed");
        var committed = Earn("arsinoe_what_she_asks", beforeTerms, "arsinoe.committed");
        var friend = Earn("arsinoe_what_she_asks", ThroughRepair(Earn("arsinoe_roofs", printer, "arsinoe.friendship")), "arsinoe.campaign_friend");
        var slow = Earn("arsinoe_what_she_asks", ThroughRepair(Earn("arsinoe_roofs", printer, "arsinoe.slow")), "arsinoe.campaign_slow");
        var parted = Earn("arsinoe_what_she_asks", beforeTerms, "arsinoe.parted");
        check(open.Has("arsinoe.campaign_lover") && !open.Has("arsinoe.committed"), "Ordinary open love gains an extra promise requirement");

        Snapshot ReturnedOffice(Snapshot before)
        {
            // Native dismissal is a fixture; the road and the return are played.
            var gone = Changed(before, "konomi.dismissed", "konomi.office_completed");
            gone.Chapter = 5; Refresh(gone);
            var road = Earn("konomi.trickster.dismissed.late", gone, "konomi.trickster.back_from_the_road");
            var back = Earn("konomi.trickster.dismissed.recess", road, "konomi.trickster.recessed");
            check(back.CrusadeResources!["Finances"] == gone.CrusadeResources!["Finances"] - 150,
                "Returned-office fixture skips the driver's actual price");
            check(!back.Has("konomi.trickster.returned"), "Dismissal return was replaced with another device's receipt");
            // Observe her restored office after the actual physical return.
            return Changed(back, "konomi.in_office");
        }

        // Knowledge is an actual office exchange, independent of eligibility.
        var ask = S(Prefix + "late.ask");
        foreach (var officeCase in new[] { "present", "returned", "absent", "dead", "dismissed", "closed", "return_then_dead", "recess_then_dead", "unloaded_dead", "recess_then_unloaded" })
        {
            var s = Program.Copy(roof); s.Chapter = 5;
            if (officeCase is "returned" or "recess_then_dead" or "recess_then_unloaded") s = ReturnedOffice(s);
            if (officeCase != "absent") s.Flags.Add("konomi.in_office");
            if (officeCase is "dead" or "return_then_dead" or "recess_then_dead" or "unloaded_dead" or "recess_then_unloaded") s.Flags.Add("konomi.retained_dead");
            if (officeCase == "return_then_dead") s.Flags.Add("konomi.trickster.returned"); // stale history, negative only
            if (officeCase == "dismissed") s.Flags.Add("konomi.dismissed");
            if (officeCase == "closed") s.Flags.Add("konomi.closed");
            Refresh(s);
            if (officeCase is "unloaded_dead" or "recess_then_unloaded")
            {
                s.Flags.Remove("konomi.retained_dead"); Refresh(s);
                check(s.Has("konomi.dead.unreturned"), "Native body unloading erased its observed death");
            }
            var yes = Earn(ask.Id, s, Accepted);
            var no = Earn(ask.Id, s, Declined);
            check(yes.Has(Known) == (officeCase is "present" or "returned") && !no.Has(Known), "Unwitnessed Konomi knowledge: " + officeCase);
            check(!Rules.Available(story, ask, yes) && !Rules.Available(story, ask, no), "Late ask replays");
            var pending = Program.Copy(s);
            check(!pending.Has(Accepted) && !pending.Has(Known), "Pending ask invents acceptance/knowledge");
            var postwar = End(yes, false, false, "alive");
            var business = End(no, false, false, "alive");
            var pages = Program.Walk(S(Prefix + "late.commit"), postwar);
            check(pages.Count == 2, "Accepted page lost the night or deferred appointment");
            foreach (var node in new[] { "morning", "table" })
            {
                var t = Text(Prefix + "late.commit", node, postwar);
                check(t.Contains("letters of credit") == (officeCase is "present" or "returned"), "Postwar Konomi note ignores current post: " + officeCase);
                var lost = Changed(postwar, "konomi.retained_dead");
                check(!Text(Prefix + "late.commit", node, lost).Contains("letters of credit"), "Known Konomi writes after a later death");
                lost.Flags.Remove("konomi.retained_dead"); Refresh(lost);
                check(lost.Has("konomi.dead.unreturned")
                    && !Text(Prefix + "late.commit", node, lost).Contains("letters of credit"),
                    "An unloaded body lets historical Konomi knowledge write a new letter");
                var dismissed = Changed(postwar, "konomi.dismissed");
                if (officeCase != "returned")
                    check(!Text(Prefix + "late.commit", node, dismissed).Contains("letters of credit"), "Known Konomi writes after leaving her office");
                var closedOffice = Changed(postwar, "konomi.closed");
                check(!Text(Prefix + "late.commit", node, closedOffice).Contains("letters of credit"), "Known Konomi writes after closure");
            }
            check(Rules.Available(story, S(Prefix + "late.commit"), business), "Recorded decline lacks its business-only memory");
            var seen = new HashSet<string>();
            Program.Walk(S(Prefix + "late.commit"), business, (n, _) => seen.Add(n));
            check(seen.SetEquals(new[] { "offer", "business" }), "A recorded decline gets a late night");
            // Before the affirmative terminal, the office knowledge is absent.
            if (officeCase is "present" or "returned")
                check(ask.Nodes.Single(n => n.Id == "yes_known").Choices[0].Set.Contains(Known)
                    && ask.Nodes[0].Choices.All(c => !c.Set.Contains(Known)), "Knowledge precedes the witnessed exchange");
        }

        // The ordinary morning and collection morning each earn their receipt.
        Snapshot ReturnHome(Snapshot lover)
        {
            var travel = Earn("arsinoe_before_the_road", lover, "arsinoe.departure_kept");
            travel.Chapter = 4; Refresh(travel);
            travel = Earn("arsinoe_one_dull_thing", travel, "arsinoe.dull_thing_kept");
            travel.Chapter = 5; Refresh(travel);
            var home = Earn("arsinoe_where_she_stays", travel, "arsinoe.staying_chosen");
            return home;
        }
        var home = ReturnHome(open);
        var ordinary = Earn("arsinoe_the_window_opens", home, "arsinoe.night_shared");
        var near = Earn("arsinoe_the_window_opens", home, "arsinoe.last_evening_kept", "arsinoe.night_shared");
        var afterHours = S(Prefix + "after_hours.react_konomi");
        foreach (var basis in new[] { ordinary, near, friend, slow, roof })
        {
            var s = Changed(basis, "konomi.in_office");
            check(Rules.Available(story, afterHours, s) == basis.Has("arsinoe.night_shared"), "Aftermath opens without an actual night");
        }
        var returnedIntimacy = ReturnedOffice(ordinary);
        check(Rules.Available(story, afterHours, returnedIntimacy)
            && Rules.Available(story, S(Prefix + "cauldron_seen.react_konomi"), Changed(returnedIntimacy, Prefix + "cost.lien")),
            "Actual office return leaves an allocated Konomi occasion unavailable");
        check(!Rules.Available(story, afterHours, Changed(returnedIntimacy, "konomi.retained_dead")),
            "Actual office return overrides Konomi's later death");
        var unloadedLoss = Changed(returnedIntimacy, "konomi.retained_dead");
        unloadedLoss.Flags.Remove("konomi.retained_dead"); Refresh(unloadedLoss);
        check(!Rules.Available(story, afterHours, unloadedLoss)
            && !Rules.Available(story, S(Prefix + "cauldron_seen.react_konomi"), Changed(unloadedLoss, Prefix + "cost.lien")),
            "An unloaded body lets an old return revive a Konomi occasion");
        var reacted = Earn(afterHours.Id, Changed(ordinary, "konomi.in_office"), afterHours.Id);
        check(!Rules.Available(story, afterHours, reacted), "Intimacy aftermath replays");
        foreach (var loss in new[] { "konomi.retained_dead", "konomi.dismissed", "konomi.closed" })
            check(!Rules.Available(story, afterHours, Changed(ordinary, "konomi.in_office", loss)), "Unavailable Konomi reacts: " + loss);
        check(!Rules.Available(story, afterHours, ordinary), "Konomi reacts outside her office");

        var askReady = Program.Copy(roof); askReady.Chapter = 5; Refresh(askReady);
        var lateYes = Earn(ask.Id, askReady, Accepted);
        var lateNo = Earn(ask.Id, askReady, Declined);
        // A historical late refusal does not close the ordinary courtship.
        var beforeDecline = Program.Copy(beforeTerms); beforeDecline.Chapter = 5; Refresh(beforeDecline);
        var refusedThenOrdinary = Earn(ask.Id, beforeDecline, Declined);
        refusedThenOrdinary = Earn("arsinoe_what_she_asks", refusedThenOrdinary, "arsinoe.open_future", "arsinoe.committed");

        // Cross played lease, haggle and pledge producers with native outcomes.
        foreach (bool grace in new[] { false, true })
        foreach (string pledge in new[] { "collateral_word", "collateral_still", "collateral_worldwound" })
        foreach (var relationship in new[] { roof, open, committed, lateYes, lateNo, refusedThenOrdinary })
        {
            var ready = Changed(relationship, "council.cauldron_given", "fool_king.crowned"); ready.Chapter = 5; Refresh(ready);
            var lease = Earn(Prefix + "cauldron.lease", ready, Prefix + "primed",
                grace ? Prefix + "cost.rent_raised" : Grace);
            // Earn() prefers the unhaggled result in the no-grace case; success
            // is selected explicitly from the check's real success path.
            if (grace)
                lease = LateAcceptanceInventory2Tests.PaidPaths(story, S(Prefix + "cauldron.lease"), ready)
                    .First(s => s.Has(Prefix + "primed") && s.Has(Grace));
            Refresh(lease);
            var collected = Earn(Prefix + "cauldron.collection", lease, Prefix + "cost." + pledge);
            // Native inventory evidence unlocks the existing bottle preparation.
            var bottled = Changed(collected, "lastcall.flask_taken", "lastcall.flask_held");
            var bottleScene = S("trickster.lastcall.bottle.king");
            foreach (var input in bottleScene.Requires.Where(k => story.InventoryItems.ContainsKey(k))) bottled.Flags.Add(input);
            Refresh(bottled);
            bottled = Earn(bottleScene.Id, bottled, "trickster.lastcall.primed.bottle");
            bottled.Chapter = 6; Refresh(bottled);
            var opened = Earn("trickster.lastcall.threshold", bottled, "trickster.lastcall.open");
            var called = Earn("arsinoe.lastcall.call", opened, Called);
            called = Earn("trickster.lastcall.last_joke", called, "trickster.lastcall.taken");
            // Negative fixture: removing the lease's call receipt must leave
            // its account unpaid even beside an otherwise completed Last Call.
            var active = Program.Copy(called); active.Flags.Remove(Called); Refresh(active);
            foreach (var history in new[] { collected, active, called })
            foreach (bool burst in new[] { false, true })
            foreach (bool closed in new[] { false, true })
            foreach (string life in new[] { "alive", "back", "dead" })
            {
                var state = End(history, burst, closed, life);
                var id = Prefix + "epilogue." + (burst ? "bill_to_threshold" : "pot_returned");
                bool alive = !state.Has("sacrifice") || state.Has("trickster.commander_back");
                check(Rules.Available(story, S(id), state) == alive, "Fate page leaks an unreturned Commander");
                if (!alive) continue;
                var t = Text(id, "end", state);
                bool love = relationship.Has("arsinoe.campaign_lover") || relationship.Has(Accepted);
                bool settled = !burst || history.Has(Called);
                check(t.Contains("invitation on temple vellum") == (pledge == "collateral_word" && love && settled),
                    "Invitation substitutes for a debt, acceptance or formal commitment");
                check(t.Contains("kept her hand") == (burst && history.Has(Called) && love), "Commercial return forces affection");
                check(!t.Contains("reopened it") && !t.Contains("no excuses accepted") && !t.Contains("never once suggested"), "Retired account coercion survived");
                check(t.Contains("waived") == grace, "Rent forgets the negotiated grace");
                if (pledge == "collateral_word")
                {
                    var paragraphs = Rules.VisibleParagraphs(S(id).Nodes[0], state).Where(p => p.Requires.Contains(Prefix + "cost.collateral_word") && !p.Text.Contains("invitation on temple vellum")).ToArray();
                    check(paragraphs.Length == 1, "Pledged word has multiple security dispositions");
                    check(paragraphs[0].Text.Contains("Released", StringComparison.OrdinalIgnoreCase) == settled, "Word security contradicts settlement");
                }
                if (pledge == "collateral_still")
                    check(t.Contains("lien on the Fool King's still") == settled && t.Contains("While the loss account remained unpaid") == !settled, "Still security contradicts settlement");
                if (pledge == "collateral_worldwound" && !closed)
                {
                    var lien = S(Prefix + "epilogue.foreclosure").Nodes[0];
                    var visible = Rules.VisibleParagraphs(lien, state).ToArray();
                    check(visible.Length == 1, "Wound lien has multiple dispositions");
                    check((visible[0].Text.Contains("released", StringComparison.OrdinalIgnoreCase)) == settled, "Intact Wound security remains open");
                }
                var shut = Changed(state, "arsinoe.closed", "arsinoe.parted");
                check(!Text(id, "end", shut).Contains("invitation on temple vellum"), "A closed relationship gets a personal invitation");
            }
        }

        var collectionReady = Changed(home, "council.cauldron_given", "fool_king.crowned");
        var signed = Earn(Prefix + "cauldron.lease", collectionReady, Prefix + "primed");
        var collectionNight = Earn(Prefix + "cauldron.collection", signed, Night);
        var businessOnly = Earn(Prefix + "cauldron.collection", signed, Prefix + "collection_closed", Night);
        check(!businessOnly.Has(Night), "Business collection claims a night");
        check(S(Prefix + "cauldron.collection").Nodes.SelectMany(n => n.Choices).Count(c => c.Set.Contains(Night)) == 1,
            "Collection receipt has a non-morning producer");
        check(S(Prefix + "cauldron.collection").Nodes.Single(n => n.Id == "morning").Choices[0].Set.Contains(Night),
            "Collection morning lost its terminal receipt");
        var twoNights = Earn("arsinoe_the_window_opens", collectionNight, "arsinoe.night_shared");
        var reverseSigned = Earn(Prefix + "cauldron.lease", Changed(ordinary, "council.cauldron_given", "fool_king.crowned"), Prefix + "primed");
        var reverseNights = Earn(Prefix + "cauldron.collection", reverseSigned, Night);
        foreach (var both in new[] { twoNights, reverseNights })
        {
            check(both.Has(Night) && both.Has("arsinoe.night_shared"), "Two-night ordering loses a receipt");
            var office = Changed(both, "konomi.in_office");
            var lienReaction = S(Prefix + "cauldron_seen.react_konomi");
            var lienFirst = Earn(lienReaction.Id, office, lienReaction.Id);
            check(Rules.Available(story, afterHours, lienFirst), "Lien reaction consumes intimacy aftermath");
            var intimacyFirst = Earn(afterHours.Id, office, afterHours.Id);
            check(Rules.Available(story, lienReaction, intimacyFirst), "Intimacy aftermath consumes lien reaction");
            var bothSeen = Earn(lienReaction.Id, intimacyFirst, lienReaction.Id);
            check(!Rules.Available(story, afterHours, bothSeen) && !Rules.Available(story, lienReaction, bothSeen), "A second occasion replays either reaction");
        }
        check(!Rules.Available(story, S(Prefix + "late.ask"), Changed(roof, "trickster.failed")), "New late acceptance fires off path");
        check(!Rules.Available(story, S(Prefix + "late.commit"), End(parted, false, false, "alive")), "Parting is reopened");
    }
}
