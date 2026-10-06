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
        string Text(string scene, Snapshot w) => string.Join(" ", S(scene).Nodes[0].Text,
            string.Join(" ", Rules.VisibleParagraphs(S(scene).Nodes[0], w).Select(p => p.Text)));
        string Book(string id, Snapshot w)
        {
            var e = story.Books["trickster.ledger"].Entries.Single(x => x.Id == id);
            return Rules.BookEntryVisible(e, w) ? e.Text + " " + string.Join(" ", e.Lines
                .Where(p => Rules.ParagraphVisible(p, w)).Select(p => p.Text)) : "";
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
            check(text.Contains("before it burst") == burst, "q8g incorrect cauldron condition");
            check(text.Contains("Slightly used") == (pledge == 1 && !closed), "q8g false Worldwound pledge/open callback");
            check(text.Contains("only scorched earth") == (pledge == 1 && closed), "q8g missing closed pledged-Wound discharge");
            check(text.Contains("released the lien") == (pledge == 0), "q8g still security not released");
            check(text.Contains("word had been the collateral") == (pledge == 2), "q8g wrong word pledge");
            check(text.Contains("from the deceased") == heroic, "q8g false recorded-death payment");
            var creditors = Text("trickster.lastcall.page.collectors", w);
            check(creditors.Contains("cauldron lease") && !creditors.Contains("lien attached itself"), "q8g Abadar creditor invents territory");
        }
        foreach (bool heroic in new[] { false, true })
        {
            var plain = World(6, "arsinoe.committed"); Finish(plain, heroic, heroic);
            check(Rules.Available(story, S("arsinoe.lastcall.page"), plain), "q8g ordinary no-lease coda blocked");
            var text = Text("arsinoe.lastcall.page", plain);
            check(!text.Contains("cauldron") && !text.Contains("collateral") && !text.Contains("payment"), "q8g no-lease financial history leaked");
            check(!plain.Has("arsinoe.lastcall.callable"), "q8g ordinary courtship creates lease debt");
        }
        var uncalledLease = Program.Copy(lease); Finish(uncalledLease, false, false);
        check(!Rules.JournalEntrySettled(story.Relationships["lastcall"].JournalEntries.Single(e => e.Id == "debt.abadar"), uncalledLease)
            && !Book("debt.abadar", uncalledLease).Contains("Settled"), "q8g Last Call activity discharges an uncalled lease");

        // Offering-only is a valid friendship debt, without daily courtship.
        var friend = Play(S("eliandra.trickster.ch5.last_rite"), World(5, "eliandra.met_ch5", "eliandra.trickster.observed"), "after", 0);
        friend.Chapter = 6; friend.Flags.Add("trickster.lastcall.open"); Refresh(friend);
        check(!friend.Has("eliandra.committed") && friend.Has("eliandra.lastcall.callable"), "q8g offering-only friendship debt lost");
        var friendshipTrace = new List<string>();
        Program.Walk(S("eliandra.lastcall.call"), friend, (node, state) => friendshipTrace.Add(node));
        check(!friendshipTrace.Contains("daily") && !Book("owed.eliandra", friend).Contains("every morning"), "q8g friend receives daily courtship");
        check(!Book("owed.eliandra", friend).Contains("no longer exists"), "q8g offering destroys cave");
        var dailyStart = Program.Copy(friend); dailyStart.Chapter = 5;
        var daily = Play(S("eliandra.trickster.ch5.first_mile"), dailyStart, "ask", 0);
        daily.Chapter = 6; Refresh(daily);
        var dailyTrace = new List<string>();
        Program.Walk(S("eliandra.lastcall.call"), daily, (node, state) => dailyTrace.Add(node));
        check(dailyTrace.Contains("daily") && Book("owed.eliandra", daily).Contains("every morning"), "q8g earned daily courtship missing");

        // A constructed cairn and partnership do not put a stone in a pocket.
        var cairn = World(5, "wenduag.committed", "wenduag.in_party", "wenduag.q3_spared", "wenduag.trickster.cairn_built", "wenduag.trickster.court.cairn");
        cairn.Chapter = 6; cairn.Flags.Add("trickster.lastcall.open"); Refresh(cairn);
        var tokenFree = new List<string>();
        check(Rules.Available(story, S("wenduag.lastcall.call"), cairn), "q8g token-free partner call blocked");
        Program.Walk(S("wenduag.lastcall.call"), cairn, (node, state) => tokenFree.Add(node));
        check(!tokenFree.Contains("stone") && !Book("owed.wenduag", cairn).Contains("pocket"), "q8g built cairn grants stone");
        cairn.Chapter = 5;
        var pocket = Play(S("wenduag.trickster.court.morning"), Program.Copy(cairn), "end", 1);
        pocket.Chapter = 6; Refresh(pocket);
        var stoneTrace = new List<string>();
        Program.Walk(S("wenduag.lastcall.call"), pocket, (node, state) => stoneTrace.Add(node));
        check(stoneTrace.Contains("stone") && Book("owed.wenduag", pocket).Contains("pocket"), "q8g actually carried stone missing");
        var table = Play(S("wenduag.trickster.court.morning"), Program.Copy(cairn), "end", 0);
        check(!table.Has("wenduag.trickster.morning.pocket"), "q8g table exchange fabricated pocket receipt");
        var native = World(6, "wenduag.in_party", "wenduag.romance_finished.latched");
        Finish(native, false, true);
        var nativeText = Text("wenduag.lastcall.page", native);
        check(!nativeText.Contains("own cairn") && !nativeText.Contains("sung for her") && !nativeText.Contains("flat grey stone"),
            "q8g native partner invents a burial or stone history");
        Finish(pocket, false, true);
        check(Text("wenduag.lastcall.page", pocket).Contains("own cairn"), "q8g earned cairn history lost");

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
            check(!refusalText.Contains("met every coach"), "q8g refusal gets happy release");
            check(refusalText.Contains("quicker to free her") == source.Has("kiana.soul_lost"), "q8g dog rescue invents Kiana soul rescue");
            check(refusalText.Contains("dog came home first") == source.Has("kiana.trickster.dog_saved"), "q8g dog-specific grievance missing");
            check(Text("kiana.lastcall.page", accepted).Contains("met every coach"), "q8g enacted release lacks happy coda");
            check(!Text("kiana.ending_promised", accepted).Contains("pouch never came back"), "q8g released guests remain unresolved in ending");
            check(Text("kiana.ending_promised", refused).Contains("pouch never came back"), "q8g refusal erases unresolved pouch");
            var oldCalled = Program.Copy(refused); oldCalled.Flags.Add("kiana.lastcall.called"); Refresh(oldCalled);
            check(!oldCalled.Has(Recovered) && !Text("kiana.lastcall.page", oldCalled).Contains("met every coach"), "q8g old called flag grants rescue");
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
        Console.WriteLine("PASS: eng8-q8g Last Call history and enacted debt inventory.");
    }
}
