using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Reviewed Galfrey operations, payments and completed reservations. These use
// production Rules and the real walker; receipts start at the action's hour.
internal static class GalfreyPolishTests
{
    private const string P = "galfrey.trickster.";
    private const string Committed = "galfrey.committed";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string suffix) => story.Scenes.Single(s => s.Id == P + suffix);
        Snapshot World(int chapter, params string[] flags)
        {
            var w = new Snapshot { Chapter = chapter, Hour = 0, Area = Drezen,
                CrusadeResources = new Dictionary<string, int> { ["Finances"] = 1000, ["Materials"] = 1000, ["Favors"] = 1000 } };
            w.Flags.UnionWith(new[] { "chapter_later", "trickster", "trickster.ever" });
            w.Flags.UnionWith(flags);
            w.AvailableContacts.Add("a8b7f6fd39ff2974f8b5fbf944a7f735");
            w.AvailableContacts.Add("8a23e71893cf8ab428e7ebd64b10ad27");
            Rules.Complete(story, w);
            foreach (var f in w.Flags) w.Times[f] = 0;
            return w;
        }
        Snapshot Wait(Snapshot w, int hours)
        {
            var next = Program.Copy(w); next.Hour += hours; Rules.Complete(story, next); return next;
        }
        Snapshot Play(string suffix, Snapshot w, string result)
        {
            var s = S(suffix);
            check(Rules.Available(story, s, w), "Galfrey polish contact unavailable: " + suffix);
            var ends = Program.Walk(s, w).Where(x => x.Has(result)).ToArray();
            check(ends.Length > 0, "Galfrey polish outcome missing: " + suffix + " -> " + result);
            return ends[0];
        }
        Choice C(string suffix, string node, int index) => S(suffix).Nodes.Single(n => n.Id == node).Choices[index];
        void Select(Choice c, Snapshot w)
        {
            check(Rules.ChoiceAvailable(c, w), "Galfrey polish answer unavailable: " + c.Text);
            if (c.Crusade != null) w.CrusadeResources![c.Crusade.Resource] += c.Crusade.Amount;
            foreach (var f in c.Set) { w.Flags.Add(f); w.Times[f] = w.Hour; }
            Rules.Complete(story, w);
        }

        var standing = S("ch3.standing_orders");
        var poor = World(3, "galfrey.early.kitrane.mooted"); poor.Hour = 24; poor.CrusadeResources!["Finances"] = 99;
        check(Rules.Available(story, standing, poor) && !Rules.ChoiceAvailable(C("ch3.standing_orders", "why", 0), poor),
            "Galfrey preparation spends unavailable funds.");
        var free = Play("ch3.standing_orders", poor, P + "crows_briefed");
        check(free.CrusadeResources!["Finances"] == 99 && !free.Has(P + "standing_orders.paid"), "Galfrey free supplies became a fee.");
        var funded = Program.Copy(poor); funded.CrusadeResources!["Finances"] = 100;
        var paid = Play("ch3.standing_orders", funded, P + "standing_orders.paid");
        check(paid.CrusadeResources!["Finances"] == 0 && paid.Has(P + "crows_briefed"), "Galfrey preparation debit/receipt mismatch.");

        foreach (var twin in new[] { "", "_stall" })
        {
            var hanged = World(5, "galfrey.dead", P + "returned", P + "first_morning", P + "ride.hanged", P + "ride.refused_order");
            if (twin != "") { hanged.Flags.Add("galfrey.presence.failed"); hanged.Times["galfrey.presence.failed"] = 0; }
            hanged = Wait(hanged, 24); hanged.CrusadeResources!["Finances"] = 49;
            check(!Rules.ChoiceAvailable(C("kitrane.ford_after" + twin, "agreed", 0), hanged)
                  && Program.Walk(S("kitrane.ford_after" + twin), hanged).All(x => !x.Has(P + "ride.answered")),
                "Galfrey hanging repaired without the grave money: " + twin);
            hanged.CrusadeResources["Finances"] = 50;
            var repaired = Play("kitrane.ford_after" + twin, hanged, P + "ride.answered");
            check(repaired.CrusadeResources!["Finances"] == 0, "Galfrey grave debit mismatch: " + twin);
            var beforeVisit = Program.Copy(hanged); Select(C("kitrane.ford_after" + twin, "agreed", 0), beforeVisit);
            check(!beforeVisit.Has(P + "ride.answered"), "Galfrey purse alone repairs the hanging.");

            foreach (var origin in new[] { "commit.answer", "commit.release" })
            {
                var w = World(5, "galfrey.dead", P + "returned", P + "first_morning",
                    P + (origin == "commit.answer" ? "oath_postponed" : "sworn"));
                if (twin != "") { w.Flags.Add("galfrey.presence.failed"); w.Times["galfrey.presence.failed"] = 0; }
                w = Wait(w, 48);
                // Existing direct yes survives; reservation is an additional completed result.
                Play(origin + twin, w, Committed);
                var reserved = Play(origin + twin, w, P + "answer_reserved");
                check(!reserved.Has(Committed) && !reserved.Has("galfrey.closed")
                      && !Rules.Available(story, S(origin + twin), Wait(reserved, 100)), "Galfrey reservation repeats or commits.");
                check(!Rules.Available(story, S("commit.answer_report" + twin), Wait(reserved, 23)), "Galfrey muster arrives before 24 hours.");
                var reported = Play("commit.answer_report" + twin, Wait(reserved, 24), P + "answer_reported");
                check(!Rules.Available(story, S("commit.answer_again" + twin), Wait(reported, 47)), "Galfrey second answer arrives before 48 hours.");
                var decision = Wait(reported, 48);
                Play("commit.answer_again" + twin, decision, Committed);
                foreach (var outcome in new[] { "answer_ally", "answer_refused" })
                {
                    var no = Play("commit.answer_again" + twin, decision, P + outcome);
                    check(!no.Has(Committed) && !no.Has(P + "partner") && !no.Has("galfrey.closed")
                        && !Rules.Available(story, S("visit.tent" + twin), Wait(no, 100))
                        && !Rules.Available(story, S("commit.answer_again" + twin), Wait(no, 100))
                        && !Rules.Available(story, S("commit.release" + twin), Wait(no, 100)), "Galfrey completed no leaks romance: " + outcome);
                }
                if (origin == "commit.release")
                    Play(origin + twin, w, P + "release_order_refused");
                var breached = Program.Copy(reserved); breached.Flags.Add(P + "ride.hanged"); breached.Times[P + "ride.hanged"] = breached.Hour;
                check(!Rules.Available(story, S("commit.answer_report" + twin), Wait(breached, 24)), "Galfrey follow-up ignores hanging.");
                breached.Flags.Add(P + "ride.answered"); breached.Times[P + "ride.answered"] = breached.Hour;
                check(Rules.Available(story, S("commit.answer_report" + twin), Wait(breached, 24)), "Galfrey existing remedy fails on follow-up.");
            }
        }

        // A real elapsed trace from the living contact, with both native histories.
        // Its inherited header waits remain visible; the pacing owner must resolve
        // the cumulative budget rather than certify it with pre-aged receipts.
        foreach (var refused in new[] { false, true })
        {
            var w = World(5, "galfrey.final");
            if (refused) { w.Flags.Add("galfrey.native_refused"); w.Times["galfrey.native_refused"] = 0; }
            var evening = Play("alive.kitrane", w, P + "alive.plan_told");
            var dispatched = Play("alive.plan", Wait(evening, S("alive.plan").DelayHours), P + "alive.plan_dispatched");
            check(!dispatched.Has(P + "alive.plan_kept") && dispatched.CrusadeResources!["Materials"] == 850
                && !Rules.Available(story, S("alive.trial"), Wait(dispatched, 100)), "Galfrey dispatch buys immediate success.");
            check(!Rules.Available(story, S("alive.plan_report"), Wait(dispatched, 23)), "Galfrey plan report early.");
            var planKept = Play("alive.plan_report", Wait(dispatched, 24), P + "alive.plan_kept");
            check(planKept.CrusadeResources!["Materials"] == 850, "Galfrey report charges the wagons twice.");
            var started = Play("alive.trial", Wait(planKept, S("alive.trial").DelayHours), P + "alive.trial_started");
            check(!started.Has(P + "alive.trial_kept") && started.CrusadeResources!["Finances"] == 900,
                "Galfrey escort does not start a paid trial.");
            check(!Rules.Available(story, S("alive.trial_report"), Wait(started, 95))
                && !Rules.Available(story, S("alive.oath"), Wait(started, 96)), "Galfrey judgment bypasses four days or report completion.");
            var visits = new HashSet<string>();
            Program.Walk(S("alive.trial_report"), Wait(started, 96), (id, _) => visits.Add(id));
            check(visits.Contains(refused ? "judgment" : "judgment_never") && !visits.Contains(refused ? "judgment_never" : "judgment"),
                "Galfrey report invents or forgets native refusal.");
            var kept = Play("alive.trial_report", Wait(started, 96), P + "alive.trial_kept");
            var oathAt = Wait(kept, S("alive.oath").DelayHours);
            Play("alive.oath", oathAt, Committed);
            var reserved = Play("alive.oath", oathAt, P + "alive.oath_reserved");
            check(!reserved.Has(Committed) && !Rules.Available(story, S("alive.oath"), Wait(reserved, 100))
                && !Rules.Available(story, S("alive.after_no"), Wait(reserved, 47)), "Galfrey living reservation repeats or comes early.");
            Play("alive.after_no", Wait(reserved, 48), Committed);
            foreach (var outcome in new[] { "alive.reserved_ally", "alive.reserved_refused" })
            {
                var no = Play("alive.after_no", Wait(reserved, 48), P + outcome);
                check(!no.Has(Committed) && !no.Has(P + "partner") && !no.Has(P + "alive.committed") && !no.Has("galfrey.closed")
                    && !Rules.Available(story, S("alive.after_no"), Wait(no, 100)), "Galfrey living completed no repeats or earns a bed.");
            }
        }

        // An accepted order is knowledge and collateral; merely being at the
        // sickbed or withdrawing the offer is neither.
        foreach (var atBed in new[] { false, true })
        {
            var bed = World(5, "galfrey.dying_seen");
            if (atBed) { bed.Flags.Add("galfrey.seelah_at_bed"); bed.Times["galfrey.seelah_at_bed"] = 0; }
            var accepted = Program.Walk(S("iz.offer"), bed).Where(w => w.Has(P + "kitrane_taken")).ToArray();
            check(accepted.Length > 0 && accepted.All(w => w.Has(P + "cost.coffin")
                && w.Has("trickster.secret.galfrey_eulogy.known.seelah") == atBed), "Galfrey direct order loses coffin or invents Seelah knowledge.");
            var withdrawn = Program.Walk(S("iz.offer"), bed).Where(w => w.Has(P + "let_die")).ToArray();
            check(withdrawn.Length > 0 && withdrawn.All(w => w.Has(P + "offer_withdrawn") && w.Has("galfrey.closed")
                && !w.Has(P + "cost.coffin") && !w.Has(P + "returned") && !w.Has("trickster.secret.galfrey_eulogy.known.seelah")),
                "Galfrey deliberate withdrawal receives rescue collateral or knowledge.");
        }
        var crows = World(5, P + "carried.crows");
        check(!crows.Has("trickster.secret.galfrey_eulogy.known.irabeth"), "Crows carrying invents Irabeth knowledge.");
        var irabeth = World(5, P + "carried.irabeth");
        check(irabeth.Has("trickster.secret.galfrey_eulogy.known.irabeth"), "Irabeth loses her firsthand knowledge.");
        foreach (var receipt in new[] { "react.irabeth.learned", "react.irabeth.after_death", "react.irabeth.chapel" })
            check(World(5, P + receipt).Has("trickster.secret.galfrey_eulogy.known.irabeth"), "Irabeth discovery has no Ledger receipt.");
        var secret = story.Books["trickster.ledger"].Entries.Single(e => e.Id == "secret.galfrey_eulogy");
        check(secret.Lines.Where(p => Rules.ParagraphVisible(p, irabeth)).All(p => !p.Text.Contains("Irabeth", StringComparison.Ordinal))
            && secret.Lines.Any(p => Rules.ParagraphVisible(p, crows) && p.Text.Contains("Irabeth", StringComparison.Ordinal)),
            "Galfrey Ledger displays the wrong unknown witness.");
        foreach (var twin in new[] { "", "_stall" })
        {
            var recognition = World(5, "galfrey.dead", P + "returned", P + "first_morning");
            if (twin != "") { recognition.Flags.Add("galfrey.presence.failed"); recognition.Times["galfrey.presence.failed"] = 0; }
            recognition = Wait(recognition, 24);
            Play("kitrane.seelah" + twin, recognition, "trickster.secret.galfrey_eulogy.known.seelah");
            recognition.Flags.Add("seelah_dead"); Rules.Complete(story, recognition);
            check(Program.Walk(S("kitrane.seelah" + twin), recognition).All(w => !w.Has("trickster.secret.galfrey_eulogy.known.seelah")),
                "Absent Seelah receives a recognition receipt.");
        }
        foreach (var page in new[] { "epilogue.kitrane", "epilogue.sworn", "epilogue.late" })
        {
            var uncommitted = World(6, P + "cost.found_late");
            var node = S(page).Nodes.Single(n => n.Id == "page");
            check(Rules.VisibleParagraphs(node, uncommitted).All(p => !p.Text.Contains("stirred beside her", StringComparison.Ordinal))
                && Rules.VisibleParagraphs(node, uncommitted).Any(p => p.Text.Contains("chapel alone", StringComparison.Ordinal)),
                "Galfrey uncommitted anniversary invents a shared bed.");
            HouseholdTests.Earn(story, uncommitted, "galfrey.payoff.ordinary");
            Rules.Complete(story, uncommitted);
            check(Rules.VisibleParagraphs(node, uncommitted).Any(p => p.Text.Contains("stirred beside her", StringComparison.Ordinal)),
                "Galfrey earned partner anniversary lost.");
        }
        var unseen = World(5);
        check(Rules.ChoiceAvailable(C("iz.cortege", "surgeon", 3), unseen) && !Rules.ChoiceAvailable(C("iz.cortege", "surgeon", 0), unseen),
            "Unmet Galfrey has no truthful Diplomacy answer.");
        unseen.Flags.Add("galfrey.incognito_met"); Rules.Complete(story, unseen);
        check(!Rules.ChoiceAvailable(C("iz.cortege", "surgeon", 3), unseen) && Rules.ChoiceAvailable(C("iz.cortege", "surgeon", 0), unseen),
            "Met Galfrey Diplomacy variants overlap.");
        Console.WriteLine("PASS: Galfrey reviewed polish: paid/free, 49/50, both hubs, real report clocks, yes/ally/refused, knowledge and withdrawals.");
    }
}
