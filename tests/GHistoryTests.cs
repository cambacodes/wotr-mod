using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// J-G1: reviewed source neighborhoods, not sentence selectors. The slots below
// refer to COMMON (dead/prayer/inquiry), claim-only rites/writ/watch, and the
// appended chalk recollection. Paragraphs have no saved identity of their own.
// Wording in these slots still requires editorial review; this test proves history.
internal static class GHistoryTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string E = "elyanka.trickster.", C = "chadali.trickster.", S = "seelah.trickster.";
        Scene Scene(string id) => story.Scenes.Single(s => s.Id == id);
        Node Node(string id, string node) => Scene(id).Nodes.Single(n => n.Id == node);
        void Refresh(Snapshot w)
        {
            w.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
            Rules.Complete(story, w);
        }
        Snapshot World(params string[] flags)
        {
            var w = new Snapshot { Chapter = 5, Hour = 20000,
                CrusadeResources = new Dictionary<string, int> {
                    ["Finances"] = 1000, ["Favors"] = 200, ["Materials"] = 100 } };
            w.Flags.UnionWith(new[] { "trickster", "trickster.ever", "chapter_later" });
            w.Flags.UnionWith(flags);
            foreach (string f in w.Flags) w.Times[f] = 1;
            Refresh(w);
            return w;
        }
        Snapshot Play(string id, Snapshot w, string node, int answer, Func<Snapshot, bool>? select = null)
        {
            var sc = Scene(id);
            if (sc.ContactUnit != null) w.AvailableContacts.Add(sc.ContactUnit);
            if (sc.Areas.Length > 0) w.Area = sc.Areas[0];
            w.Hour += Math.Max(72, sc.DelayHours);
            Refresh(w);
            check(Rules.Available(story, sc, w), "jg1 producer unavailable: " + id
                + " missing=" + string.Join(",", sc.Requires.Where(f => !w.Has(f)))
                + " blocked=" + string.Join(",", sc.Forbids.Where(f => Rules.ForbidHolds(sc, f, w))));
            var ends = Program.WalkVia(sc, w, node, answer).Where(x => x.Has(id) && (select == null || select(x))).ToArray();
            check(ends.Length > 0, "jg1 selected producer not completed: " + id + "/" + node + "/" + answer);
            var end = ends.First();
            Refresh(end);
            return end;
        }
        bool Slot(string id, string node, int slot, Snapshot w) =>
            Rules.VisibleParagraphs(Node(id, node), w).Contains(Node(id, node).Paragraphs[slot]);

        // Independently reviewed history table: ending, unprayed transfer,
        // prayed transfer, burial, truth/misled/hers, chalk.
        var table = new[] {
            ("claim", 4, 5, 6, 16, 17, 18, 52),
            ("debt", 2, 3, 4, 14, 15, 16, 26),
            ("lock", 2, 3, 4, 14, 15, 16, 20),
            ("left_free", 2, 3, 4, 14, 15, 16, 21) };
        var receipts = new[] { "told_seelah", "misled", "hers" };
        foreach (bool prayed in new[] { false, true })
        for (int inquiry = -1; inquiry < 3; inquiry++)
        {
            if (!prayed && inquiry >= 0) continue; // The live inquiry follows the prayer reaction.
            // Native Iz dead and a previously earned bier are fixture inputs.
            // The transfer, optional prayer and inquiry outcomes are played.
            var w = World("elyanka.trickster.owned", "elyanka.trickster.bier_seen");
            if (prayed) { w.Flags.Add("seelah.in_party"); Refresh(w); }
            w = Play(E + "test.the_dead", w, "rows", prayed ? 0 : 1,
                x => x.Has(E + "gave_dead"));
            check(w.Has(E + "gave_dead"), "jg1 transfer missing");
            check(w.Has(E + "seelah_prayed") == prayed, "jg1 prayer fabricated or lost");
            if (inquiry >= 0)
            {
                w = Play(E + "react.seelah_rows", w, "start", 0);
                w = Play(E + "beat.inquiry", w, "her", inquiry);
                check(w.Has(E + "inquiry." + receipts[inquiry]), "jg1 inquiry receipt missing");
            }
            foreach (string loss in new[] { "", "seelah_dead", "seelah_gone" })
            {
                var past = Program.Copy(w); if (loss != "") past.Flags.Add(loss); Refresh(past);
                foreach (var row in table)
                {
                    string id = E + "epilogue." + row.Item1;
                    check(Slot(id, "page", row.Item2, past) == !prayed, "jg1 unprayed transfer: " + id);
                    check(Slot(id, "page", row.Item3, past) == prayed, "jg1 prayer count: " + id);
                    check(!Slot(id, "page", row.Item4, past), "jg1 transfer invents burial: " + id);
                    for (int i = 0; i < 3; i++)
                        check(Slot(id, "page", new[] { row.Item5, row.Item6, row.Item7 }[i], past) == (inquiry == i),
                            "jg1 inquiry direction: " + id + "/" + i);
                    check(Slot(id, "page", row.Item8, past) == (inquiry >= 0), "jg1 chalk requires performed inquiry: " + id);
                }
            }
        }
        // The truth proposal is not a spoken confession. Retain the old
        // timing/target contract while retiring its single wording assertion.
        var proposal = Node(E + "beat.inquiry", "truth").Choices[0];
        check(proposal.Set.Length == 0 && proposal.Next == "confess", "jg1 confession promised before spoken");
        var confession = Node(E + "beat.inquiry", "confess").Choices[0];
        check(confession.Next == "confession_answer", "jg1 confession reply target");
        check(Node(E + "beat.inquiry", "confession_answer").Choices[0].Set.Contains(E + "inquiry.told_seelah"),
            "jg1 spoken confession receipt missing");

        // Official writ and inquiry are independent. Omitted producers must
        // select the no-authority account; each actual writ suppresses it.
        for (int writ = -1; writ < 3; writ++)
        for (int inquiry = -1; inquiry < 3; inquiry++)
        {
            var w = World("elyanka.trickster.bier_seen", "elyanka.trickster.gave_dead",
                "elyanka.trickster.react.seelah_rows", "seelah.in_party", "trickster.secret.elyanka_rites");
            if (writ >= 0) w = Play(E + "beat.writ", w, "chaplain", writ);
            if (inquiry >= 0) w = Play(E + "beat.inquiry", w, "her", inquiry);
            string id = E + "epilogue.claim";
            check(Slot(id, "page", 42, w) == (writ < 0 && inquiry < 0), "jg1 false no-authority history");
            check(Slot(id, "page", 45, w) == (writ == 0 || writ == 2), "jg1 upheld/hers writ direction");
            check(Slot(id, "page", 46, w) == (writ == 1), "jg1 lying writ direction");
            check(Slot(id, "page", 51, w) == (inquiry >= 0), "jg1 watch requires inquiry");
        }

        // Custody continues through a forfeited wager, both priced returns,
        // observed renewed contact and the final coda. No injected coin_lost.
        var stake = Play("chadali.wagers.the_real_wager", World("chadali.started", C + "primed", "chadali.wagers.so_gloomy", "chadali.wagers.a_free_space"), "bet", 1);
        var released = Play(C + "council.second_cookie", Program.Copy(stake), "her_test", 0);
        check(released.Has("chadali.wagers.stake_released") && !released.Has("chadali.wagers.coin_lost"),
            "jg1 accepted wager falsely forfeited");
        released.Chapter = 6;
        released.Flags.UnionWith(new[] { "trickster.lastcall.taken", "trickster.lastcall.pillar.bottle", "ending.trickster" });
        Refresh(released);
        check(Rules.Available(story, Scene("chadali.lastcall.page"), released), "jg1 released wager coda unavailable");
        check(!Slot("chadali.lastcall.page", "page", 4, released)
            && !Slot(C + "epilogue.lucky_night", "page", 47, released), "jg1 released coin falsely collected");
        var lost = Play(C + "council.second_cookie", stake, "her_test", 1);
        check(lost.Has("chadali.wagers.coin_lost"), "jg1 wager did not derive coin loss");
        lost = Play(C + "after.orange_tree", lost, "start", 0);
        lost.Flags.Add("council.fought"); Refresh(lost);
        var offPath = Program.Copy(lost); offPath.Flags.Add("trickster.failed"); Refresh(offPath);
        check(!Rules.Available(story, Scene(C + "fought.lucky"), offPath), "jg1 return fires after leaving Trickster");
        var broke = Program.Copy(lost); broke.CrusadeResources!["Favors"] = 0;
        check(!Rules.ChoiceAvailable(Node(C + "fought.lucky", "refusal").Choices[0], broke),
            "jg1 public apology became free");
        for (int answer = 0; answer < 2; answer++)
        {
            var returned = Play(C + "fought.lucky", Program.Copy(lost), "refusal", answer);
            check(returned.Has(C + "returned") && returned.Has("chadali.wagers.coin_lost"), "jg1 return erased forfeiture");
            check(returned.Has(C + "cost.apologised") == (answer == 0)
                && returned.Has(C + "cost.needle_owed") == (answer == 1), "jg1 return price direction");
            var trace = new List<string>();
            Program.Walk(Scene(C + "fought.lucky"), lost, (n, _) => trace.Add(n));
            check(trace.Contains("coin_collected") && !trace.Contains("coin") && !trace.Contains("coin_home"),
                "jg1 forfeiture letter custody");
            returned.Chapter = 6;
            returned.Flags.UnionWith(new[] { "trickster.lastcall.taken", "trickster.lastcall.pillar.bottle", "ending.trickster" });
            Refresh(returned);
            check(Rules.Available(story, Scene("chadali.lastcall.page"), returned), "jg1 returned Chadali coda unavailable");
            check(Slot("chadali.lastcall.page", "page", 4, returned)
                && Slot(C + "epilogue.lucky_night", "page", 47, returned), "jg1 collected coin coda missing");
            check(!Slot("chadali.lastcall.page", "page", 5, returned), "jg1 forfeited coin falsely at home");
            var laterLoss = Program.Copy(returned); laterLoss.Flags.Add("chadali.returned_actor_lost"); Refresh(laterLoss);
            check(!Rules.Available(story, Scene("chadali.lastcall.page"), laterLoss), "jg1 later-lost Chadali appears");
            var absent = Program.Copy(lost); absent.Chapter = 6;
            absent.Flags.UnionWith(new[] { "trickster.lastcall.taken", "trickster.lastcall.pillar.bottle", "ending.trickster" }); Refresh(absent);
            check(!Rules.Available(story, Scene("chadali.lastcall.page"), absent), "jg1 unreturned Chadali appears");
        }

        // Direction is established by the answer she refused, not by the words
        // on the ending. Refusal must never become commitment or erase retry cost.
        foreach (string suffix in new[] { "commit", "commit_visit" })
        foreach (var refusal in new[] { ("no", "freedom_declined"), ("no_death", "list_declined"), ("no_stones", "stones_declined") })
        {
            var w = World(S + "returned", S + "stay_decided", "seelah.kissed");
            if (refusal.Item1 != "no") w.Flags.Add(S + "cost.holds_her_death");
            if (refusal.Item1 == "no_stones") w.Flags.Add(S + "death_returned");
            if (suffix.EndsWith("_visit")) w.Flags.Add("seelah.presence.failed");
            w = Play(S + "dismissed." + suffix, w, refusal.Item1, 0);
            check(w.Has(S + refusal.Item2) && w.Has(S + "declined") && !w.Has("seelah.committed"), "jg1 Seelah refusal direction");
            string retry = S + "dismissed.second_ask" + (suffix.EndsWith("_visit") ? "_visit" : "");
            w.Hour += 120; Refresh(w);
            check(Rules.Available(story, Scene(retry), w) == (refusal.Item2 != "stones_declined"),
                "jg1 unpaid coin refusal cannot retry for free");
            w.Chapter = 6; Refresh(w);
            check(Rules.Available(story, Scene(S + "epilogue.refused"), w), "jg1 refusal ending unavailable");
            check(Slot(S + "epilogue.refused", "end", 0, w) && !Slot(S + "epilogue.refused", "end", 1, w), "jg1 returned refusal callback");
            w.Flags.Add("seelah.committed"); Refresh(w);
            check(!Rules.Available(story, Scene(S + "epilogue.refused"), w), "jg1 committed Seelah gets refusal ending");
        }
    }
}
