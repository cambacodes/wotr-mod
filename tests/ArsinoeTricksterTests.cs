using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Arsinoe, Trickster (Writer/handoffs/trickster/arsinoe.md): the leased cauldron. Lease -> collection -> epilogue pages,
// plus the E14c collector paragraph on the registered kept endings and the two allocated reactions.
internal static class ArsinoeTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Contact = "a609ed9b2205d034bb3bb04d2a255681";
    private const string Lease = "arsinoe.trickster.cauldron.lease";
    private const string Collection = "arsinoe.trickster.cauldron.collection";

    private static Snapshot World(Story story, params string[] flags)
    {
        var state = new Snapshot { Chapter = 5, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.AvailableContacts.Add(Contact);
        Rules.Complete(story, state);
        return state;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        var lease = story.Scenes.Single(s => s.Id == Lease);
        var collection = story.Scenes.Single(s => s.Id == Collection);
        var epilogues = story.Scenes.Where(s => s.Id.StartsWith("arsinoe.trickster.epilogue.", StringComparison.Ordinal)).ToArray();
        check(epilogues.Length == 4 && epilogues.All(e => e.Owner == "Epilogue"), "Arsinoe Trickster epilogue pages missing.");
        check(new[] { lease, collection }.All(s => s.AnswerLists.SequenceEqual(new[] { "ecaf5cfe8087a4f45a2269974f4885c9" }) && s.ContactUnit == Contact),
            "Arsinoe Trickster beats leave her own vendor list.");

        // Trk_Arsinoe_InCapital / PathFailed: no cauldron, or the path lost, no lease.
        check(!Rules.Available(story, lease, World(story, "trickster", "arsinoe.capital")), "Lease offered without the Council's cauldron.");
        check(!Rules.Available(story, lease, World(story, "trickster.was", "trickster.failed", "arsinoe.capital", "council.cauldron_given")),
            "Lease offered after the Trickster path failed.");
        var ready = World(story, "trickster", "arsinoe.capital", "council.cauldron_given");
        check(Rules.Available(story, lease, ready), "Trk_Arsinoe_Cauldron: lease unavailable.");
        check(!Rules.Available(story, collection, ready), "Collection before the lease.");
        var notCapital = Program.Copy(ready); notCapital.Chapter = 4;
        check(!Rules.Available(story, lease, notCapital), "Physical lease outside chapter five.");

        // Native effects live on the joke only; the failed haggle adds its surcharge.
        var joke = lease.Nodes.Single(n => n.Id == "terms").Choices[0];
        check(joke.Mythic == "PlayerIsTrickster" && joke.Alignment?.Direction == "Lawful" && joke.Alignment.Value == 1
              && joke.Crusade?.Resource == "Finances" && joke.Crusade.Amount == -500, "Lease joke lost its native price.");
        var raised = lease.Nodes.Single(n => n.Id == "raised").Choices.Single();
        check(raised.Crusade?.Amount == -200 && raised.Set.Contains("arsinoe.trickster.cost.rent_raised"), "Failed haggle is free.");
        var haggle = lease.Nodes.Single(n => n.Id == "rent").Choices.Single(c => c.Check != null).Check!;
        check(haggle.Skill == "CheckDiplomacy" && haggle.DC == 25 && haggle.CommanderOnly, "Haggle uses the wrong check.");

        foreach (bool shamira in new[] { false, true })
        foreach (bool fought in new[] { false, true })
        {
            var start = Program.Copy(ready);
            if (shamira) start.Flags.Add("shamira.killed");
            if (fought) start.Flags.Add("council.fought");
            var pages = new HashSet<string>();
            var results = Program.Walk(lease, start, (page, partial) =>
            {
                pages.Add(page);
                // eng7-l09: the initial payment and failed-check liability are deliberately recorded before signing.
                var transactionFlags = new[] { "arsinoe.trickster.cost.rent_paid", "arsinoe.trickster.cost.rent_raised", "arsinoe.trickster.cost.rent_surcharge_paid" };
                check(partial.Flags.Except(transactionFlags).ToHashSet().SetEquals(start.Flags) || page == "leased" || page == "discount" || page == "grudge",
                    "Lease writes history before it is signed: " + page);
            });
            check(pages.Contains("shamira") == shamira, "Shamira's essence node ignores ShamiraKilled.");
            check(pages.Contains("grudge") == fought, "Grudge node ignores the Council fight.");
            var signed = results.Where(r => r.Has(Lease)).ToList();
            check(signed.Count > 0 && signed.All(r => r.Has("arsinoe.trickster.primed") && r.Has("arsinoe.trickster.cost.lien")),
                "Signed lease does not prime the collection.");
            check(results.Where(r => !r.Has(Lease)).All(r => r.Flags.SetEquals(start.Flags)), "Refusing the lease changes history.");
            check(results.Any(r => !r.Has(Lease)), "The lease cannot be refused or postponed.");
            foreach (var after in signed)
            {
                check(!Rules.Available(story, lease, after), "Lease replays.");
                var later = Program.Copy(after); later.Hour += collection.DelayHours;
                Rules.Complete(story, later);
                check(Rules.Available(story, collection, later), "Trk_Arsinoe_Cauldron: collection unreachable.");
                var early = Program.Copy(after); early.Hour += collection.DelayHours - 1;
                check(!Rules.Available(story, collection, early), "Collection ignores its delay.");
                // Ledger row 14: the lease does not close on the Council's fate; the collection survives losing the path.
                var lost = Program.Copy(later); lost.Flags.Remove("trickster"); lost.Flags.Add("trickster.was"); lost.Flags.Add("socot.gone");
                Rules.Complete(story, lost);
                check(Rules.Available(story, collection, lost), "Collection lost with the live Trickster path.");
            }
        }

        // Trk_Arsinoe_Coexistence (ledger row 14): every council.expired cause leaves the lease and its collection open.
        foreach (string expired in new[] { "socot.gone", "shyka.gone", "council.fought", "council.fought_nocta_allied" })
        {
            var world = World(story, "trickster", "arsinoe.capital", "council.cauldron_given", expired);
            check(Rules.Available(story, lease, world), "Lease closes on council.expired cause " + expired);
            foreach (var signed in Program.Walk(lease, world).Where(r => r.Has(Lease)))
            {
                var later = Program.Copy(signed); later.Hour += collection.DelayHours;
                check(Rules.Available(story, collection, later), "Collection closes on council.expired cause " + expired);
            }
        }

        foreach (bool lover in new[] { false, true })
        foreach (bool king in new[] { false, true })
        {
            var start = World(story, "trickster", "arsinoe.capital", "arsinoe.trickster.primed", "arsinoe.trickster.cost.lien", Lease);
            if (lover) start.Flags.UnionWith(new[] { "arsinoe.started", "arsinoe.campaign_lover", "arsinoe.committed" });
            if (king) { start.Flags.Add("fool_king.crowned"); Rules.Complete(story, start); }
            var pages = new HashSet<string>();
            var results = Program.Walk(collection, start, (page, _) => pages.Add(page));
            check(pages.Contains("threshold") == lover && pages.Contains("morning") == lover, "Intimate beat ignores the registered lover state.");
            check(pages.Contains("still") == king, "Fool King's still pledged without the King.");
            check(!pages.Contains("wedding") && !pages.Contains("rider"), "Other routes' costs read without their flags.");
            check(results.All(r => r.Has(Collection)), "Collection has a non-terminal exit.");
            check(results.Any(r => r.Has("arsinoe.trickster.stays_to_collect") && r.Has("arsinoe.started")), "Trk_Arsinoe_Flirt unreachable.");
            check(results.Any(r => r.Has("arsinoe.trickster.collection_closed") && !r.Has("arsinoe.trickster.stays_to_collect")),
                "Collection cannot be kept to business.");
            check(results.All(r => !r.Has("arsinoe.closed") && (!lover || r.Has("arsinoe.committed"))), "Collection closes or erases the romance.");
            check(results.Any(r => r.Has("arsinoe.trickster.cost.collateral_worldwound")), "Worldwound pledge unreachable.");
            foreach (var r in results) check(!Rules.Available(story, collection, r), "Collection replays.");
        }

        // Epilogue pages: exactly one cauldron page per finale, and the lien page splits on the Wound's closure.
        foreach (bool burst in new[] { false, true })
        foreach (bool wound in new[] { false, true })
        foreach (bool closed in new[] { false, true })
        {
            var end = World(story, "trickster.was", "arsinoe.trickster.cost.lien", "arsinoe.trickster.primed");
            end.Chapter = 6;
            if (burst) end.Flags.Add("siphon.burst_council");
            if (wound) end.Flags.Add("arsinoe.trickster.cost.collateral_worldwound");
            if (closed) end.Flags.Add("ending.wound_closed");
            Rules.Complete(story, end);
            var shown = epilogues.Where(e => Rules.Available(story, e, end)).Select(e => e.Id).ToList();
            check(shown.Count(id => id.EndsWith("bill_to_threshold") || id.EndsWith("pot_returned")) == 1, "Cauldron fate page missing or doubled.");
            check(shown.Contains("arsinoe.trickster.epilogue.bill_to_threshold") == burst, "Siphon burst ignored.");
            check(shown.Count(id => id.Contains("foreclosure")) == (wound ? 1 : 0), "Worldwound lien page wrong.");
        }

        // Every pledge is collected: the word and the still as paragraphs on both cauldron fate pages.
        foreach (string id in new[] { "arsinoe.trickster.epilogue.bill_to_threshold", "arsinoe.trickster.epilogue.pot_returned" })
        {
            var node = story.Scenes.Single(s => s.Id == id).Nodes[0];
            foreach (string pledge in new[] { "arsinoe.trickster.cost.collateral_word", "arsinoe.trickster.cost.collateral_still" })
            {
                var with = World(story, pledge); var without = World(story);
                check(Rules.VisibleParagraphs(node, with).Count(p => p.Requires.Contains(pledge)) == 1
                      && Rules.VisibleParagraphs(node, without).All(p => !p.Requires.Contains(pledge)),
                    "Pledge " + pledge + " is never collected on " + id);
            }
        }

        // The collector paragraph rides on the registered kept endings (E14c), never as a second page.
        foreach (string id in new[] { "arsinoe_ending_kept", "arsinoe_ending_open", "arsinoe_ending_promised" })
        {
            var para = story.Scenes.Single(s => s.Id == id).Nodes[0].Paragraphs;
            check(para != null && para.Any(p => p.Requires.SequenceEqual(new[] { "arsinoe.trickster.stays_to_collect" })),
                "Collector paragraph missing on " + id);
        }

        // Reactions: exactly the two allocated reactors, both reading the lien.
        var reactions = story.Scenes.Where(s => s.Relationship == "arsinoe" && s.Reaction).ToArray();
        check(reactions.Length == 2 && reactions.All(r => r.Requires.Contains("arsinoe.trickster.cost.lien")), "Arsinoe reactions changed.");

        // Sol INT (2026-09-30): Konomi hears of the lien in her office only; her Trickster return reopens a dismissal.
        var konomi = reactions.Single(r => r.Id == "arsinoe.trickster.cauldron_seen.react_konomi");
        var office = World(story, "trickster", "arsinoe.trickster.cost.lien", "konomi.in_office");
        check(Rules.Available(story, konomi, office), "Konomi's lien reaction is unreachable in her office.");
        check(!Rules.Available(story, konomi, World(story, "trickster", "arsinoe.trickster.cost.lien")), "Konomi reacts without being in office.");
        check(!Rules.Available(story, konomi, World(story, "trickster", "arsinoe.trickster.cost.lien", "konomi.in_office", "konomi.dismissed")),
            "A dismissed Konomi reacts.");
        check(Rules.Available(story, konomi, World(story, "trickster", "arsinoe.trickster.cost.lien", "konomi.in_office", "konomi.dismissed", "konomi.trickster.returned")),
            "A Konomi returned by her Trickster route never hears of the lien.");
        check(!Rules.Available(story, konomi, World(story, "trickster", "arsinoe.trickster.cost.lien", "konomi.in_office", "konomi.retained_dead")),
            "A dead Konomi reacts.");

        // Sol COX (2026-09-30), R2-6: the late commitment. A Trickster who flirted at the collection but never reached her
        // commitment scene gets the rent-day page; it offers a staged night, a deferred yes and a refusal.
        var lateCommit = story.Scenes.Single(s => s.Id == "arsinoe.trickster.late.commit");
        check(lateCommit.Owner == "Epilogue" && lateCommit.Relationship == "arsinoe", "Arsinoe late page is not her epilogue.");
        var flirted = World(story, "trickster.ever", "arsinoe.trickster.stays_to_collect", "arsinoe.started");
        flirted.Chapter = 6;
        check(flirted.Has("arsinoe.trickster.late_committed") && Rules.Available(story, lateCommit, flirted), "R2-6 late commitment unreachable.");
        foreach (string spoken in new[] { "arsinoe.committed", "arsinoe.future_spoken", "arsinoe.closed" })
        {
            var already = Program.Copy(flirted); already.Flags.Add(spoken);
            check(!Rules.Available(story, lateCommit, already), "Late page doubles an ordinary ending: " + spoken);
        }
        var business = World(story, "trickster.ever", "arsinoe.trickster.collection_closed");
        business.Chapter = 6;
        check(!Rules.Available(story, lateCommit, business), "A lease kept to business offers a late romance.");
        var latePages = new HashSet<string>();
        var lateResults = Program.Walk(lateCommit, flirted, (page, _) => latePages.Add(page));
        check(latePages.SetEquals(lateCommit.Nodes.Select(n => n.Id)), "Unreached late-commit page.");
        // R2-6: an epilogue writes no flags; the yes (night or table) and the refusal are narrative branches only.
        check(lateCommit.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0), "The late epilogue writes flags.");
        check(new[] { "night", "table", "business" }.All(id => lateCommit.Nodes.Single(n => n.Id == "offer").Choices.Any(c => c.Next == id)),
            "Late commitment lacks a night, a deferred yes or a refusal.");
        check(lateCommit.Nodes.Single(n => n.Id == "night").Choices.Single().Next == "morning", "Late night has no morning after.");

        // Sol r2 INT: the late page never visits a dead or ascended Commander; a Commander brought back is visited.
        foreach (var (extra, open, why) in new (string[], bool, string)[] {
            (new[] { "sacrifice" }, false, "genuine death"),
            (new[] { "sacrifice", "ending.wound_closed" }, false, "death at the closed Wound"),
            (new[] { "sacrifice", "ending.trickster" }, true, "native Trickster return"),
            (new[] { "sacrifice", "ending.wound_closed", "trickster.lastcall.taken", "trickster.lastcall.pillar.bottle" }, true, "Last Call return"),
            (new[] { "ascended" }, false, "ascension") })
        {
            var end = Program.Copy(flirted); end.Flags.UnionWith(extra); Rules.Complete(story, end);
            check(Rules.Available(story, lateCommit, end) == open, "Late page wrong after " + why);
        }
        var lateAscended = story.Scenes.Single(s => s.Id == "arsinoe.trickster.late.ascended");
        var risen = Program.Copy(flirted); risen.Flags.Add("ascended");
        check(Rules.Available(story, lateAscended, risen) && !Rules.Available(story, lateAscended, flirted), "Ascended late page wrong.");
        check(lateCommit.MinChapter == 6 && lateCommit.MaxChapter == 6 && lateAscended.MinChapter == 6, "Late pages outside the epilogue chapter.");
        // Sol r2 COX: an ordinary courtship begun on the roof, with no cauldron, also reaches the late page; friendship does not.
        // Sol r4 HOW: walk the opening through the roof and stop there (no later evenings are claimed).
        var cityScene = story.Scenes.Single(s => s.Id == "arsinoe_city_on_paper");
        var printerScene = story.Scenes.Single(s => s.Id == "arsinoe_printers_view");
        var roofScene = story.Scenes.Single(s => s.Id == "arsinoe_roofs");
        var entry = new Snapshot { Chapter = 5, Area = Drezen, Hour = 5000 };
        entry.Flags.UnionWith(new[] { "trickster", "arsinoe.capital" });
        entry.AvailableContacts.Add(Contact);
        Rules.Complete(story, entry);
        Snapshot? roofOnlyMaybe = null;
        foreach (var a in Program.Walk(cityScene, entry).Where(r => r.Has("arsinoe.picture_invitation")))
        {
            var b1 = Program.Copy(a); b1.Hour += printerScene.DelayHours;
            foreach (var b2 in Program.Walk(printerScene, b1).Where(r => r.Has("arsinoe.printer_met")))
            {
                var c1 = Program.Copy(b2); c1.Hour += roofScene.DelayHours;
                roofOnlyMaybe ??= Program.Walk(roofScene, c1).FirstOrDefault(r => r.Has("arsinoe.courting"));
            }
        }
        check(roofOnlyMaybe != null, "The roof courtship cannot be played from a Chapter 5 entry.");
        var roofOnly = Program.Copy(roofOnlyMaybe!);
        roofOnly.Chapter = 6; roofOnly.Flags.Add("trickster.ever");
        Rules.Complete(story, roofOnly);
        check(roofOnly.Has("arsinoe.trickster.late_committed") && Rules.Available(story, lateCommit, roofOnly), "Roof courtship has no late commitment.");
        var roofFriend = World(story, "trickster.ever", "arsinoe.roof_shared", "arsinoe.friendship");
        roofFriend.Chapter = 6;
        check(!Rules.Available(story, lateCommit, roofFriend), "Friendship is reopened as a late romance.");
        var roofOffer = lateCommit.Nodes.Single(n => n.Id == "offer");
        string OfferText(Snapshot st) => string.Join(" ", Rules.VisibleParagraphs(roofOffer, st).Select(p => p.Text));
        var roofText = OfferText(roofOnly);
        check(roofText.Contains("a roof, once") && !roofText.Contains("innkeeper") && !roofText.Contains("walk I made")
              && !roofText.Contains("Tovin's shop") && !roofText.Contains("line about late payments"),
            "Roof-only late offer recalls evenings that were never played.");
        check(OfferText(flirted).Contains("line about late payments") && !OfferText(flirted).Contains("a roof, once"),
            "Lease-flirt late offer borrows the roof history.");
        var booked = Program.Copy(roofOnly); booked.Flags.Add("arsinoe_first_impression");
        check(OfferText(booked).Contains("innkeeper") && !OfferText(booked).Contains("walk I made"), "Book callback wrong.");
        var tabled = Program.Copy(booked); tabled.Flags.UnionWith(new[] { "arsinoe_hours_of_her_own", "arsinoe.next_table" });
        check(OfferText(tabled).Contains("Tovin's shop") && !OfferText(tabled).Contains("walk I made"), "Table callback wrong.");
        var walked = Program.Copy(booked); walked.Flags.UnionWith(new[] { "arsinoe_hours_of_her_own", "arsinoe.next_walk" });
        check(OfferText(walked).Contains("walk I made") && !OfferText(walked).Contains("Tovin's shop"), "Walk callback wrong.");
        // A Chapter 5 fresh entry reaches the roof within the post-Coronation budget (168 h).
        int roofHours = new[] { "arsinoe_city_on_paper", "arsinoe_printers_view", "arsinoe_roofs" }.Sum(id => story.Scenes.Single(s => s.Id == id).DelayHours);
        check(roofHours <= 168, "Post-Coronation entry cannot reach the late-commit beat in 168 h: " + roofHours);

        // Sol r2 COX: the cauldron fate page agrees with Last Call (handed back at the rift, or the account closed at the table).
        var bill = story.Scenes.Single(s => s.Id == "arsinoe.trickster.epilogue.bill_to_threshold").Nodes[0];
        var potNode = story.Scenes.Single(s => s.Id == "arsinoe.trickster.epilogue.pot_returned").Nodes[0];
        foreach (bool active in new[] { false, true })
        foreach (bool called in new[] { false, true })
        {
            if (called && !active) continue;
            var st = World(story, "trickster.ever", "arsinoe.trickster.cost.lien", "siphon.burst_council");
            if (active) st.Flags.Add("lastcall.active");
            if (called) st.Flags.Add("arsinoe.lastcall.called");
            var shown = Rules.VisibleParagraphs(bill, st).Where(p => p.Requires.Length + p.Forbids.Length > 0 && !p.Requires.Any(r => r.Contains("collateral"))).ToArray();
            check(shown.Length == 1, "Burst cauldron page has no single fate variant (active=" + active + ", called=" + called + ")");
            check(shown.All(p => p.Text.Contains("unopened") == !active && p.Text.Contains("handed it") == called), "Burst page contradicts Last Call.");
            var whole = World(story, "trickster.ever", "arsinoe.trickster.cost.lien");
            if (active) whole.Flags.Add("lastcall.active");
            check(Rules.VisibleParagraphs(potNode, whole).Count(p => p.Text.Contains("still paying")) == (active ? 0 : 1), "Returned cauldron page contradicts Last Call.");
        }

        // Sol r4 BEL: no collateral or arrears paragraph has a dead Commander visit or pay; a Commander brought back does.
        foreach (string id in new[] { "arsinoe.trickster.epilogue.bill_to_threshold", "arsinoe.trickster.epilogue.pot_returned" })
        foreach (bool back in new[] { false, true })
        {
            var node = story.Scenes.Single(s => s.Id == id).Nodes[0];
            var st = World(story, "trickster.ever", "arsinoe.trickster.cost.lien", "arsinoe.trickster.cost.collateral_word", "sacrifice");
            if (back) st.Flags.Add("ending.trickster");
            Rules.Complete(story, st);
            var text = string.Join(" ", Rules.VisibleParagraphs(node, st).Select(p => p.Text));
            check(text.Contains("The Commander came") == back && text.Contains("never called in") == !back, "Pledged word ignores death on " + id);
            if (id.EndsWith("pot_returned"))
                check(text.Contains("still paying") == back && text.Contains("Nobody paid it") == !back, "Arrears ignore death.");
        }

        // Sol r2 INT: the Kiana wedding line (added to this scene by kiana_trickster.integrate) reads her route's robbery,
        // and is skipped once the guests are home (Q3 or her bought-back terms).
        foreach (string restitution in new[] { "", "seelah.souls_returned", "kiana.trickster.guests_bought_back" })
        foreach (bool recalled in new[] { false, true })
        {
            var st = World(story, "trickster", "arsinoe.capital", "arsinoe.trickster.primed", "arsinoe.trickster.cost.lien", Lease,
                "kiana.trickster.cost.guests_robbed", "kiana.soul_lost");
            if (restitution != "") st.Flags.Add(restitution);
            if (recalled) st.Flags.Add("konomi.trickster.cost.recalled");
            var seen = new HashSet<string>();
            var res = Program.Walk(collection, st, (page, _) => seen.Add(page));
            check(seen.Contains("wedding") == (restitution == ""), "Wedding line ignores restitution: " + restitution);
            check(seen.Contains("rider") == recalled && seen.Contains("pledge") && res.All(r => r.Has(Collection)), "Wedding routing broken.");
        }

        // Sol r5 COX/BEL: every combination of fate, Last Call, burst and Wound shows one settlement of the account across
        // all her Trickster epilogue pages: never "paid" beside "still owed", never a live foreclosure after a call-in.
        foreach (string life in new[] { "alive", "dead", "back" })
        foreach (string lc in new[] { "none", "active", "called" })
        foreach (bool burst in new[] { false, true })
        foreach (bool closedWound in new[] { false, true })
        {
            var st = World(story, "trickster.ever", "arsinoe.trickster.primed", "arsinoe.trickster.cost.lien",
                "arsinoe.trickster.cost.collateral_worldwound", "arsinoe.trickster.cost.collateral_word");
            st.Chapter = 6;
            if (life != "alive") st.Flags.Add("sacrifice");
            if (life == "back") st.Flags.Add("ending.trickster");
            if (lc != "none") st.Flags.Add("lastcall.active");
            if (lc == "called") st.Flags.Add("arsinoe.lastcall.called");
            if (burst) st.Flags.Add("siphon.burst_council");
            if (closedWound) st.Flags.Add("ending.wound_closed");
            Rules.Complete(story, st);
            var text = string.Join(" ", epilogues.Where(e => Rules.Available(story, e, st))
                .SelectMany(e => e.Nodes).SelectMany(n => new[] { n.Text }.Concat(Rules.VisibleParagraphs(n, st).Select(p => p.Text))));
            string what = life + "/" + lc + "/burst=" + burst + "/closed=" + closedWound;
            bool settled = text.Contains("paid by noon") || text.Contains("paid the arrears the next morning") || text.Contains("Released on payment");
            bool owed = text.Contains("still paying") || text.Contains("not yet foreclosed") || text.Contains("Nobody paid it") || text.Contains("came back unopened");
            check(!(settled && owed), "Arsinoe's account is both settled and owed: " + what);
            check(!text.Contains("Account satisfied"), "Wound closure claims the rent account satisfied: " + what);
            check(lc != "called" || !text.Contains("not yet foreclosed"), "A called-in lien still threatens foreclosure: " + what);
            check(lc == "none" || !owed, "Last Call leaves the account owed: " + what);
            bool alive = life != "dead" || lc != "none";
            check(!text.Contains("The Commander came.") || alive, "A dead Commander answers the called word: " + what);
        }

        // Sol COX/HOW: the courtship spine fits the shared chain ceiling (ledger: 504 h) at its minimum delays.
        string[] spine = { "arsinoe_printers_view", "arsinoe_roofs", "arsinoe_first_impression", "arsinoe_hours_of_her_own",
            "arsinoe_your_hours", "arsinoe_borrowed_court", "arsinoe_price_of_an_evening", "arsinoe_courtyard_company",
            "arsinoe_another_hour", "arsinoe_the_unprofitable_hour", "arsinoe_after_rain", "arsinoe_two_doors",
            "arsinoe_a_stone_in_hand", "arsinoe_the_first_cart", "arsinoe_what_she_asks", "arsinoe_where_she_stays", "arsinoe_the_window_opens" };
        int spineHours = spine.Sum(id => story.Scenes.Single(s => s.Id == id).DelayHours);
        check(spineHours <= 504, "Arsinoe's courtship spine exceeds the 504-hour chain ceiling: " + spineHours);
    }
}
