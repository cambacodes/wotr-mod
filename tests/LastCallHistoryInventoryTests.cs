using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// eng8-q8g: E-Q8-11. Predicate fixtures supply prior/native history; the
// decisive lease, pledge, offering, stone and pardon come from played choices.
internal static class LastCallHistoryInventoryTests
{
    private const string Freed = "trickster.lastcall.kiana_guests_freed";
    private const string Pardon = "trickster.lastcall.kiana_pardon";
    private const string Recovered = "kiana.lastcall.guests_recovered";
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        void Refresh(Snapshot w)
        {
            w.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
            Rules.Complete(story, w);
        }
        Snapshot World(int chapter, params string[] flags)
        {
            var w = new Snapshot { Chapter = chapter, Hour = 20000,
                CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000 } };
            w.Flags.UnionWith(new[] { "trickster", "trickster.ever", "chapter_later" });
            w.Flags.UnionWith(flags);
            foreach (var rel in story.Relationships)
                if (flags.Contains(rel.Value.CommittedFlag) && story.Derived.ContainsKey(rel.Key + ".payoff.ordinary"))
                    HouseholdTests.Earn(story, w, rel.Key + ".payoff.ordinary");
            foreach (var flag in w.Flags) w.Times[flag] = 1;
            Refresh(w);
            return w;
        }
        Snapshot Play(Scene scene, Snapshot initial, string node, int answer)
        {
            // Native contact in these fixtures is an observed available actor.
            if (scene.ContactUnit != null) initial.AvailableContacts.Add(scene.ContactUnit);
            if (scene.Areas.Length > 0) initial.Area = scene.Areas[0];
            initial.Hour += Math.Max(24, scene.DelayHours);
            check(Rules.Available(story, scene, initial), "q8g positive producer unavailable: " + scene.Id
                + "; missing=" + string.Join(",", scene.Requires.Where(k => !initial.Has(k)))
                + "; forbids=" + string.Join(",", scene.Forbids.Where(initial.Has)));
            check(Rules.ChoiceAvailable(scene.Nodes.Single(n => n.Id == node).Choices[answer], initial),
                "q8g selected producer answer is unavailable or unaffordable: " + scene.Id + "/" + node);
            var ends = Program.WalkVia(scene, initial, node, answer);
            check(ends.Count > 0, "q8g selected producer not traversed: " + scene.Id + "/" + node);
            var end = ends.First(w => w.Has(scene.Id));
            Refresh(end);
            return end;
        }
        string Text(string scene, Snapshot w) => string.Join(" ", SurfaceIds.Of(story, S(scene).Nodes[0]),
            string.Join(" ", Rules.VisibleParagraphs(S(scene).Nodes[0], w).Select(p => SurfaceIds.Of(story, p))));
        string Book(string id, Snapshot w)
        {
            var e = story.Books["trickster.ledger"].Entries.Single(x => x.Id == id);
            return Rules.BookEntryVisible(e, w) ? SurfaceIds.Of(story, e) + " " + string.Join(" ", e.Lines
                .Where(p => Rules.ParagraphVisible(p, w)).Select(p => SurfaceIds.Of(story, p))) : "";
        }
        void Finish(Snapshot w, bool closed, bool heroic)
        {
            w.Chapter = 6;
            w.Flags.Add("trickster.lastcall.taken");
            w.Flags.Add("trickster.lastcall.pillar.bottle");
            w.Flags.Add("ending.trickster");
            if (heroic) w.Flags.Add("sacrifice");
            if (closed) w.Flags.Add("ending.wound_closed");
            Refresh(w);
            check(w.Has("lastcall.active"), "q8g finish lacks earned Last Call state");
        }

        // Actual lease producer and all three collateral answers, crossed with
        // destruction, Wound closure and recorded Commander death (24 worlds).
        var lease = Play(S("arsinoe.trickster.cauldron.lease"), World(5, "arsinoe.capital", "council.cauldron_given", "fool_king.crowned"), "terms", 0);
        check(lease.Has("arsinoe.trickster.cost.lien"), "q8g lease did not produce lien");
        for (int pledge = 0; pledge < 3; pledge++)
        foreach (bool burst in new[] { false, true })
        foreach (bool closed in new[] { false, true })
        foreach (bool heroic in new[] { false, true })
        {
            var w = Play(S("arsinoe.trickster.cauldron.collection"), Program.Copy(lease), "pledge", pledge);
            w.Chapter = 6; w.Flags.Add("trickster.lastcall.open"); w.Flags.Add("arsinoe.committed");
            if (burst) w.Flags.Add("siphon.burst_shamira");
            Refresh(w);
            w = Play(S("arsinoe.lastcall.call"), w, "call", 0);
            Finish(w, closed, heroic);
            var text = Text("arsinoe.lastcall.page", w);
            check(SurfaceIds.Has(text, "[arsinoe.lastcall.page/page/paragraph/1]") == burst, "q8g incorrect cauldron condition");
            check(SurfaceIds.Has(text, "[arsinoe.lastcall.page/page/paragraph/6]") == (pledge == 1 && !closed), "q8g false Worldwound pledge/open callback");
            check(SurfaceIds.Has(text, "[arsinoe.lastcall.page/page/paragraph/7]") == (pledge == 1 && closed), "q8g missing closed pledged-Wound discharge");
            check(SurfaceIds.Has(text, "[arsinoe.lastcall.page/page/paragraph/2]") == (pledge == 0), "q8g still security not released");
            check(SurfaceIds.Has(text, "[arsinoe.lastcall.page/page/paragraph/3]") == (pledge == 2), "q8g wrong word pledge");
            check(SurfaceIds.Has(text, "[arsinoe.lastcall.page/page/paragraph/4]") == heroic, "q8g false recorded-death payment");
            var creditors = Text("trickster.lastcall.page.collectors", w);
            check(SurfaceIds.Has(creditors, "[trickster.lastcall.page.collectors/page/paragraph/7]"), "q8g Abadar creditor invents territory");
        }
        foreach (bool heroic in new[] { false, true })
        {
            var plain = World(6, "arsinoe.committed"); Finish(plain, heroic, heroic);
            check(Rules.Available(story, S("arsinoe.lastcall.page"), plain), "q8g ordinary no-lease coda blocked");
            var text = Text("arsinoe.lastcall.page", plain);
            check(!SurfaceIds.Has(text, "[arsinoe.lastcall.page/page/paragraph/0][arsinoe.lastcall.page/page/paragraph/1]") && !SurfaceIds.Has(text, "[arsinoe.lastcall.page/page/paragraph/3][arsinoe.lastcall.page/page/paragraph/6]") && !SurfaceIds.Has(text, "[arsinoe.lastcall.page/page/paragraph/4]"), "q8g no-lease financial history leaked");
            check(!plain.Has("arsinoe.lastcall.callable"), "q8g ordinary courtship creates lease debt");
        }
        var uncalledLease = Program.Copy(lease); Finish(uncalledLease, false, false);
        check(!Rules.JournalEntrySettled(story.Relationships["lastcall"].JournalEntries.Single(e => e.Id == "debt.abadar"), uncalledLease)
            && !SurfaceIds.Has(Book("debt.abadar", uncalledLease), "[book/trickster.ledger/debt.abadar/line/1]"), "q8g Last Call activity discharges an uncalled lease");

        // Offering-only is a valid friendship debt, without daily courtship.
        var friend = Play(S("eliandra.trickster.ch5.last_rite"), World(5, "eliandra.met_ch5", "eliandra.trickster.observed"), "after", 0);
        friend.Chapter = 6; friend.Flags.Add("trickster.lastcall.open"); Refresh(friend);
        check(!friend.Has("eliandra.committed") && friend.Has("eliandra.lastcall.callable"), "q8g offering-only friendship debt lost");
        var friendshipTrace = new List<string>();
        Program.Walk(S("eliandra.lastcall.call"), friend, (node, state) => friendshipTrace.Add(node));
        check(!friendshipTrace.Contains("daily") && !SurfaceIds.Has(Book("owed.eliandra", friend), "[book/trickster.ledger/owed.eliandra/line/2]"), "q8g friend receives daily courtship");
        var dailyStart = Program.Copy(friend); dailyStart.Chapter = 5;
        var daily = Play(S("eliandra.trickster.ch5.first_mile"), dailyStart, "ask", 0);
        daily.Chapter = 6; Refresh(daily);
        var dailyTrace = new List<string>();
        Program.Walk(S("eliandra.lastcall.call"), daily, (node, state) => dailyTrace.Add(node));
        check(dailyTrace.Contains("daily") && SurfaceIds.Has(Book("owed.eliandra", daily), "[book/trickster.ledger/owed.eliandra/line/2]"), "q8g earned daily courtship missing");

        // A constructed cairn and partnership do not put a stone in a pocket.
        var cairn = World(5, "wenduag.committed", "wenduag.in_party", "wenduag.q3_spared", "wenduag.trickster.cairn_built", "wenduag.trickster.court.cairn");
        cairn.Chapter = 6; cairn.Flags.Add("trickster.lastcall.open"); Refresh(cairn);
        var tokenFree = new List<string>();
        check(Rules.Available(story, S("wenduag.lastcall.call"), cairn), "q8g token-free partner call blocked");
        Program.Walk(S("wenduag.lastcall.call"), cairn, (node, state) => tokenFree.Add(node));
        check(!tokenFree.Contains("stone") && !SurfaceIds.Has(Book("owed.wenduag", cairn), "[book/trickster.ledger/owed.wenduag/line/2]"), "q8g built cairn grants stone");
        cairn.Chapter = 5;
        var pocket = Play(S("wenduag.trickster.court.morning"), Program.Copy(cairn), "end", 1);
        pocket.Chapter = 6; Refresh(pocket);
        var stoneTrace = new List<string>();
        Program.Walk(S("wenduag.lastcall.call"), pocket, (node, state) => stoneTrace.Add(node));
        check(stoneTrace.Contains("stone") && SurfaceIds.Has(Book("owed.wenduag", pocket), "[book/trickster.ledger/owed.wenduag/line/2]"), "q8g actually carried stone missing");
        var table = Play(S("wenduag.trickster.court.morning"), Program.Copy(cairn), "end", 0);
        check(!table.Has("wenduag.trickster.morning.pocket"), "q8g table exchange fabricated pocket receipt");
        var native = World(6, "wenduag.in_party", "wenduag.romance_finished.latched");
        Finish(native, false, true);
        var nativeText = Text("wenduag.lastcall.page", native);
        check(!SurfaceIds.Has(nativeText, "[wenduag.lastcall.page/page/paragraph/6]") && !SurfaceIds.Has(nativeText, "[wenduag.lastcall.page/page/paragraph/1]") && !SurfaceIds.Has(nativeText, "[wenduag.lastcall.page/page/paragraph/0]"),
            "q8g native partner invents a burial or stone history");
        Finish(pocket, false, true);
        check(SurfaceIds.Has(Text("wenduag.lastcall.page", pocket), "[wenduag.lastcall.page/page/paragraph/6]"), "q8g earned cairn history lost");

        // Dog-only and stolen personal soul share debt, never personal history.
        var dog = Play(S("kiana.trickster.awake.dog_collar"), World(5, "kiana.q2_done"), "bark", 0);
        var soul = Play(S("kiana.trickster.possessed.fake_gem"), World(5, "kiana.possessed"), "terms", 0);
        foreach (var source in new[] { dog, soul })
        {
            source.Chapter = 6; source.Flags.Add("trickster.lastcall.open"); source.Flags.Add("kiana.committed");
            source.Flags.Add("kiana.trickster.met"); Refresh(source);
            var refused = Play(S("kiana.lastcall.call"), Program.Copy(source), "letter", 3);
            check(!refused.Has(Freed) && !refused.Has(Pardon) && refused.Has("kiana.lastcall.resolved"), "q8g refused pardon releases guests");
            var accepted = Play(S("kiana.lastcall.call"), Program.Copy(source), "letter", 0);
            check(accepted.Has(Freed) && accepted.Has(Pardon), "q8g accepted release lacks enacted receipts");
            Finish(refused, false, false); Finish(accepted, false, false);
            var refusalText = Text("kiana.lastcall.page", refused);
            check(!SurfaceIds.Has(refusalText, "[kiana.lastcall.page/page/paragraph/0]"), "q8g refusal gets happy release");
            check(SurfaceIds.Has(refusalText, "[kiana.lastcall.page/page/paragraph/1]") == source.Has("kiana.soul_lost"), "q8g dog rescue invents Kiana soul rescue");
            check(SurfaceIds.Has(refusalText, "[kiana.lastcall.page/page/paragraph/3]") == source.Has("kiana.trickster.dog_saved"), "q8g dog-specific grievance missing");
            check(SurfaceIds.Has(Text("kiana.lastcall.page", accepted), "[kiana.lastcall.page/page/paragraph/0]"), "q8g enacted release lacks happy coda");
            check(!SurfaceIds.Has(Text("kiana.ending_promised", accepted), "[kiana.ending_promised/start/paragraph/0][kiana.ending_promised/start/paragraph/1]"), "q8g released guests remain unresolved in ending");
            check(SurfaceIds.Has(Text("kiana.ending_promised", refused), "[kiana.ending_promised/start/paragraph/0][kiana.ending_promised/start/paragraph/1]"), "q8g refusal erases unresolved pouch");
            var oldCalled = Program.Copy(refused); oldCalled.Flags.Add("kiana.lastcall.called"); Refresh(oldCalled);
            check(!oldCalled.Has(Recovered) && !SurfaceIds.Has(Text("kiana.lastcall.page", oldCalled), "[kiana.lastcall.page/page/paragraph/0]"), "q8g old called flag grants rescue");
        }
        // Already recovered guests settle only the old bill: no second rescue.
        var nativeRecovery = Program.Copy(dog);
        nativeRecovery.Flags.Add("seelah.souls_returned"); Refresh(nativeRecovery); // native quest observation
        var ransomRecovery = Play(S("kiana.trickster.awake.dog_collar"), World(5, "kiana.q2_done"), "start", 1);
        var buybackStart = Program.Copy(dog); buybackStart.Chapter = 5;
        var buybackRecovery = Play(S("kiana.trickster.pouch.second_offer"), buybackStart, "start", 0);
        check(ransomRecovery.Has("kiana.trickster.guests_ransomed") && buybackRecovery.Has("kiana.trickster.guests_bought_back"),
            "q8g independent recovery producers did not release the guests");
        foreach (var recovery in new[] { nativeRecovery, ransomRecovery, buybackRecovery })
        {
            var w = Program.Copy(recovery); w.Chapter = 6; w.Flags.Add("trickster.lastcall.open"); Refresh(w);
            var accepted = Play(S("kiana.lastcall.call"), w, "letter", 1);
            check(accepted.Has(Pardon) && !accepted.Has(Freed), "q8g independent rescue buys the same souls twice");
        }
        var dead = Program.Copy(dog); dead.Flags.Add("kiana.sunhammer_dead"); Refresh(dead);
        var deadEnds = Program.Walk(S("kiana.lastcall.call"), dead);
        check(deadEnds.All(w => w.Has("kiana.lastcall.resolved") && !w.Has(Pardon) && !w.Has(Freed)), "q8g dead jeweller offers pardon/release");

        // endings1: native ending observations crossed with actual Last Call
        // answers. Both bridge acceptances preserve death and concealed return.
        var prepared = World(6, "trickster.lastcall.open", "trickster.lastcall.pillar.bottle");
        foreach (bool heroic in new[] { false, true })
        foreach (int crossing in new[] { 0, 1, 2 })
        {
            if (!heroic && crossing != 0) continue;
            var state = Play(S("trickster.lastcall.last_joke"), Program.Copy(prepared), "wound", heroic ? 1 : 0);
            state.Flags.Add(heroic ? "ending.wound_closed" : "ending.trickster");
            if (heroic) state.Flags.Add("sacrifice");
            if (crossing != 0)
            {
                state.Flags.Add("iomedae.trickster.banner_carried");
                state.Flags.Add(crossing == 1 ? "iomedae.committed" : "iomedae.trickster.rescue_only");
            }
            Refresh(state);
            bool bridge = crossing != 0;
            check(state.Has("lastcall.bottled_held") == !bridge, "endings1: historical bottling implies current contents");
            check(state.Has("lastcall.public_return") == !bridge, "endings1: bridge return becomes public");
            check(state.Has("lastcall.recovered_corked") == (heroic && !bridge), "endings1: H2 recovery opens the flask or replaces the bridge");
            check(state.Has("lastcall.dead_on_record") == heroic, "endings1: a living return erases the death record");
            check(Rules.Available(story, S("trickster.lastcall.page.bottle"), state) == !bridge,
                "endings1: bottle page survives the empty-flask crossing");
            foreach (string rel in new[] { "anevia", "irabeth", "arueshalae", "devarra", "delamere", "mielarah", "nidalynn", "jannah", "nenio", "terendelev", "eliandra", "galfrey", "horzalah", "melazmera", "yaniel", "wenduag" })
            {
                var page = S(rel + ".lastcall.page").Nodes[0];
                bool IsRecovery(Paragraph pp) => pp.Requires.Contains("lastcall.recovered_corked")
                    || pp.Requires.Contains("lastcall.h2") && (pp.Requires.Contains("iomedae.trickster.buried_alive") || rel == "anevia" || rel == "wenduag");
                // Recipient life/presence is an independent prerequisite. Supply
                // it through the existing earned fixture, without changing the ending.
                var recipient = Program.Copy(state);
                foreach (string guard in page.Paragraphs.Where(IsRecovery).SelectMany(pp => pp.Requires)
                    .Where(k => k != "lastcall.recovered_corked" && k != "lastcall.h2" && k != "iomedae.trickster.buried_alive"))
                    HouseholdTests.Earn(story, recipient, guard);
                Refresh(recipient);
                var recovery = Rules.VisibleParagraphs(page, recipient).Where(IsRecovery).ToArray();
                check(recovery.Length == (heroic ? 1 : 0) && recovery.All(pp => !pp.Text.Contains("flask was opened")),
                    "endings1: wrong recovery/visibility for " + rel + "/" + crossing);
            }
        }
        var needle = World(6, "trickster.lastcall.open", "chadali.trickster.cost.needle_owed");
        var needleEnd = Play(S("chadali.lastcall.call"), needle, "call", 1);
        check(!needleEnd.Has("chadali.lastcall.luck_returned") && !needleEnd.Has("chadali.fortunes.loan_returned"),
            "endings1: needle-only call manufactures repayment");
        var luck = World(6, "trickster.lastcall.open", "chadali.trickster.cost.luck_owed");
        var luckEnd = Play(S("chadali.lastcall.call"), luck, "luck", 0);
        check(luckEnd.Has("chadali.fortunes.loan_returned") && !luckEnd.Has("chadali.lastcall.luck_due"),
            "endings1: real luck transfer lacks repayment receipt");
        foreach (var old in new[] {
            World(6, "trickster.lastcall.open", "chadali.trickster.cost.luck_owed", "chadali.fortunes.loan_returned"),
            World(6, "trickster.lastcall.open", "chadali.trickster.cost.luck_owed", "chadali.wagers.stake_luck", "chadali.wagers.stake_collected") })
            check(!old.Has("chadali.lastcall.account_due"), "endings1: returned/forfeited luck is called twice");
        foreach (string paid in new[] { "seelah.trickster.death_returned", "seelah.trickster.cost.robbed_back", "seelah.trickster.list_settled" })
            check(!World(6, "trickster.lastcall.open", "seelah.trickster.cost.keeps_it", paid).Has("seelah.lastcall.account_due"),
                "endings1: reclaimed list generates another promise");
        var listEnd = Play(S("seelah.lastcall.call"), World(6, "trickster.lastcall.open", "seelah.trickster.cost.keeps_it"), "list", 0);
        check(listEnd.Has("seelah.trickster.death_returned") && listEnd.Has("seelah.lastcall.list_returned"),
            "endings1: list dispatch does not resolve custody");
        foreach (int answer in new[] { 0, 1, 2 })
        {
            var k = Play(S("konomi.lastcall.call"), World(6, "trickster.lastcall.open", "konomi.trickster.cost.debt_owed", "konomi.trickster.favour_owed"), "terms", answer);
            check(k.Has("konomi.lastcall.terms_accepted") == (answer == 0), "endings1: counteroffer/refusal grants permanent political obligation");
            check(Rules.JournalEntrySettled(story.Relationships["lastcall"].JournalEntries.Single(e => e.Id == "owed.konomi"), k) == (answer == 0),
                "endings1: proposal alone discharges Konomi's account");
        }
        foreach (string paid in new[] { "konomi.trickster.debt_paid", "konomi.trickster.fee_paid" })
            check(!World(6, "trickster.lastcall.open", "konomi.trickster.cost.debt_owed", paid).Has("konomi.lastcall.account_due"),
                "endings1: prepaid/endorsed assistance reopens an unnamed debt");
        var dragonBill = World(6, "trickster.lastcall.open", "devarra.trickster.cost.egg_withheld", "devarra.trickster.refused", "devarra.closed");
        var unspoken = Play(S("trickster.lastcall.account.devarra"), dragonBill, "call", 0);
        check(unspoken.Has("devarra.lastcall.left_unspoken") && !unspoken.Has("devarra.lastcall.called"),
            "endings1: silent account summons a departed dragon");
        foreach (string branch in new[] { "cost.blood_sample", "cost.lab_funded", "cost.mutasafen_grudge" })
        {
            var hz = Play(S("hepzamirah.trickster.body.hounds"), World(5, "hepzamirah.trickster.returned", "hepzamirah.trickster." + branch), "joke", 0);
            check(hz.Has("hepzamirah.trickster.cost.vial_paid")
                && Rules.VisibleParagraphs(S("hepzamirah.trickster.epilogue.leavable").Nodes[0], hz).Any(pp => pp.Requires.SequenceEqual(new[] { "hepzamirah.trickster.cost.vial_paid" })),
                "endings1: blood sample consequence misses " + branch);
        }
        foreach (int courierAnswer in new[] { 1, 2 })
        {
            var refusedBlood = Play(S("hepzamirah.trickster.body.hounds"), World(5, "hepzamirah.trickster.returned", "hepzamirah.trickster.cost.blood_sample"), "joke", courierAnswer);
            check(!refusedBlood.Has("hepzamirah.trickster.cost.vial_paid")
                && !Rules.JournalEntrySettled(story.Relationships["lastcall"].JournalEntries.Single(e => e.Id == "debt.mutasafen"), refusedBlood),
                "endings1: wine or murdered courier manufactures blood payment");
        }
        foreach (string terminal in new[] { "refused_page", "inn" })
        {
            var refusal = S("nocticula.trickster.epilogue.commit").Nodes.Single(n => n.Id == terminal);
            var favour = refusal.Paragraphs.Single(pp => pp.Text.Contains("The chair was provided."));
            var paidFavour = World(6, "nocticula.trickster.cost.shade_paid");
            foreach (string guard in favour.Requires.Where(k => k != "nocticula.trickster.cost.shade_paid"))
                HouseholdTests.Earn(story, paidFavour, guard);
            Refresh(paidFavour);
            var unpaidFavour = Program.Copy(paidFavour);
            unpaidFavour.Flags.Remove("nocticula.trickster.cost.shade_paid"); Refresh(unpaidFavour);
            check(refusal.Choices.Count == 1 && refusal.Choices[0].Next == null && refusal.Choices[0].Set.Length == 0
                && Rules.ParagraphVisible(favour, paidFavour) && !Rules.ParagraphVisible(favour, unpaidFavour),
                "endings1: paid favour cancels romantic refusal or charges an unpaid branch");
        }
        var shadowBill = World(6, "trickster.lastcall.open", "noct.dead", "noct.fooled", "noct.closed", "nocticula.trickster.cost.shade_paid");
        var shadowAccount = Play(S("trickster.lastcall.account.nocticula"), shadowBill, "call", 0);
        check(shadowAccount.Has("nocticula.lastcall.called") && shadowAccount.Has("nocticula.lastcall.resolved")
            && !shadowAccount.Has("nocticula.lastcall.account_due") && !Rules.Available(story, S("nocticula.lastcall.call"), shadowBill),
            "endings1: paid protection needs a current romance or summons the absent queen");
        var ear = World(6, "trickster.lastcall.open", "horzalah.trickster.cost.ear");
        check(!ear.Has("horzalah.lastcall.account_due")
            && SurfaceIds.Has(Book("owed.horzalah", ear), "[book/trickster.ledger/owed.horzalah/line/3]")
            && !SurfaceIds.Has(Book("owed.horzalah", ear), "[book/trickster.ledger/owed.horzalah/line/2]"),
            "endings1: paid ear invents a Guild return or trophy location");
        var unpaid = World(6, "trickster.lastcall.taken", "ending.trickster", "chadali.trickster.cost.needle_owed", "chadali.fortunes.loan_returned");
        check(!Rules.JournalEntrySettled(story.Relationships["lastcall"].JournalEntries.Single(e => e.Id == "owed.chadali"), unpaid),
            "endings1: luck repayment discharges the separate needle oath");
        Console.WriteLine("PASS: eng8-q8g Last Call history and enacted debt inventory.");
    }
}
