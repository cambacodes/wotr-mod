using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class SoanaPartnerTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string K = "soana.partner.";
        const string Unit = "64805abb52739e44280a758f850b300c";
        const string Area = "0a5654e7dc18f074d9356009d55eb51b";
        const string Returned = "soana.trickster.returned";
        var loss = new[] { "soana.dead", "soana.killed_by_camellia", "soana.forest_dead" };
        void Refresh(Snapshot w)
        {
            w.Flags.ExceptWith(story.Derived.Keys);
            w.Flags.ExceptWith(story.Counts.Keys);
            Rules.Complete(story, w);
        }
        Scene S(string name, bool returned) => story.Scenes.Single(s => s.Id == K + name + (returned ? ".returned" : ""));
        Snapshot World(bool returned, string stance, int finances = 100, bool careful = false)
        {
            var w = new Snapshot { Chapter = 5, Hour = 5000, Area = Area,
                CrusadeResources = new Dictionary<string, int> { ["Finances"] = finances } };
            w.AvailableContacts.Add(Unit);
            w.Flags.UnionWith(new[] { "trickster", "trickster.ever", "soana.started", "soana.committed", stance });
            if (stance.EndsWith("exclusive", StringComparison.Ordinal)) w.Flags.Add(K + "exclusive_chosen");
            if (careful) w.Flags.Add(K + "bundle_hidden");
            if (returned) w.Flags.UnionWith(loss.Concat(new[] { Returned }));
            else w.Flags.Add("soana.after_quest");
            Refresh(w);
            foreach (var f in w.Flags) w.Times[f] = 4500;
            return w;
        }
        Snapshot Later(Snapshot w, int hours)
        {
            var next = Program.Copy(w); next.Hour += hours; Refresh(next); return next;
        }
        var allPages = new HashSet<string>();
        foreach (bool returned in new[] { false, true })
        foreach (string stance in new[] { "soana.partner_stance.share", "soana.partner_stance.secret", "soana.partner_stance.exclusive" })
        foreach (bool careful in stance.EndsWith("secret", StringComparison.Ordinal) ? new[] { false, true } : new[] { false })
        {
            var dispatch = S("dispatch", returned);
            var home = S("homecoming", returned);
            var exposed = S("returned_letter", returned);
            var initial = World(returned, stance, careful: careful);
            check(Rules.Available(story, dispatch, initial), "Corven dispatch has no earned living host.");
            check(!Rules.Available(story, S("dispatch", !returned), initial), "Corven dispatch uses the wrong native/returned host.");
            foreach (string blocked in new[] { "soana.closed", "inhuman", "trickster.failed", "legend", "swarm" })
            {
                var w = Program.Copy(initial); w.Flags.Add(blocked);
                // Main rebuilds derived current-path evidence from native readers.
                Refresh(w);
                check(!Rules.Available(story, dispatch, w), "Corven's new lead ignores " + blocked);
            }
            foreach (var missing in new[] { "trickster", "soana.started" })
            {
                var w = Program.Copy(initial); w.Flags.Remove(missing);
                Refresh(w);
                check(!Rules.Available(story, dispatch, w), "Corven's new lead is free without " + missing);
            }
            if (!returned)
                foreach (string flag in loss)
                {
                    var w = Program.Copy(initial); w.Flags.Add(flag); Refresh(w);
                    check(!Rules.Available(story, dispatch, w), "Dead Soana gets Corven's letter: " + flag);
                }
            var noStance = Program.Copy(initial); noStance.Flags.Remove(stance);
            check(Rules.Available(story, dispatch, noStance), "Family inquiry incorrectly requires a romantic arrangement.");
            if (stance.EndsWith("share", StringComparison.Ordinal))
            {
                var familyPaid = Program.Walk(dispatch, noStance, (id, _) => allPages.Add(dispatch.Id + "/" + id))
                    .First(w => w.Has(K + "pursued") && !w.Has("soana.round2.correspondence_only"));
                var familyReturns = Program.Walk(home, Later(familyPaid, 168), (id, _) => allPages.Add(home.Id + "/" + id));
                check(familyReturns.Any(w => w.Has("soana.trickster.friends"))
                    && familyReturns.Any(w => w.Has(K + "corven_together") && w.Has("soana.partner_stance.share")),
                    "Family inquiry loses its friendship or negotiated romantic answer.");
            }
            var absent = Program.Copy(initial); absent.AvailableContacts.Clear();
            check(!Rules.Available(story, dispatch, absent), "Corven's lead invents Soana's contact.");
            var outcomes = Program.Walk(dispatch, initial, (id, _) => allPages.Add(dispatch.Id + "/" + id));
            var reply = S("reply", returned);
            foreach (var letter in outcomes.Where(w => w.Has("soana.round2.correspondence_only")))
            {
                check(letter.CrusadeResources!["Finances"] == 100
                    && !Rules.Available(story, home, Later(letter, 168)),
                    "Correspondence charges for an escort or invents a physical arrival.");
                check(!Rules.Available(story, reply, Later(letter, 167))
                    && Rules.Available(story, reply, Later(letter, 168)),
                    "The family letter ignores its journey.");
                var replies = Program.Walk(reply, Later(letter, 168), (id, _) => allPages.Add(reply.Id + "/" + id));
                check(replies.All(w => stance.EndsWith("secret", StringComparison.Ordinal)
                    ? w.Has("soana.round2.family_reply") && !w.Has("soana.round2.reply_accepted")
                    : w.Has(K + "corven_known_alive")),
                    "The family reply loses its evidence or grants acceptance to the hidden affair.");
            }
            var escorts = outcomes.Where(w => w.Has(K + "pursued") && !w.Has("soana.round2.correspondence_only")).ToList();
            check(escorts.Count > 0 && escorts.All(w => w.CrusadeResources!["Finances"] == 25
                && !w.Has(K + "corven_known_alive")), "Every escorted family inquiry must pay before Corven answers.");
            var paid = escorts.First();
            check(paid.CrusadeResources!["Finances"] == 25 && !paid.Has(K + "corven_known_alive"),
                "Corven pursuit is unpaid or a signature becomes a living husband.");
            check(!Rules.Available(story, home, Later(paid, 167)) && Rules.Available(story, home, Later(paid, 168)),
                "Corven's paid journey ignores its week.");
            foreach (var unpaid in outcomes.Where(w => !w.Has(K + "pursued")))
                check(!Rules.Available(story, home, Later(unpaid, 1000)), "Corven walks home after a held or burned letter.");
            foreach (var w in Program.Walk(home, Later(paid, 168), (id, _) => allPages.Add(home.Id + "/" + id)))
            {
                check(w.Has(K + "corven_known_alive"), "Corven's homecoming leaves his current state unknown.");
                if (stance.EndsWith("share", StringComparison.Ordinal))
                    check(w.Has(K + "corven_together") && !w.Has(K + "corven_separated") && !w.Has(K + "affair_exposed"),
                        "Negotiated Corven terms become a secret affair.");
                else if (stance.EndsWith("exclusive", StringComparison.Ordinal))
                    check(w.Has(K + "corven_separated") && !w.Has(K + "affair_exposed") && !w.Has(K + "romance_ended"),
                        "Corven's answer to the separation becomes a discovered affair or an unearned breakup.");
                else if (w.Has(K + "quiet_homecoming"))
                    check(careful && !w.Has(K + "affair_exposed") && !w.Has(K + "romance_ended"),
                        "Packed-away bundle still exposes the affair.");
                else
                    check(w.Has(K + "corven_separated") && w.Has(K + "affair_exposed") && w.Has(K + "romance_ended")
                          && w.Has("soana.closed"), "Corven forgives the affair for free.");
            }
            var burned = outcomes.First(w => w.Has(K + "buried"));
            check(!Rules.Available(story, exposed, Later(burned, 71)) && Rules.Available(story, exposed, Later(burned, 72)),
                "The burned dispatch is discovered without its return journey.");
            foreach (var w in Program.Walk(exposed, Later(burned, 72), (id, _) => allPages.Add(exposed.Id + "/" + id)))
            {
                string state = stance.EndsWith("share", StringComparison.Ordinal) ? "corven_distant" : "corven_separated";
                check(w.Has(K + "corven_known_alive") && w.Has(K + state) && w.Has(K + "romance_ended") && w.Has("soana.closed"),
                    "The burned-letter disclosure loses Corven or leaves the romance free.");
                check(w.Has(K + "affair_exposed") == stance.EndsWith("secret", StringComparison.Ordinal),
                    "A secret confession does not reach Corven.");
                check(Rules.Available(story, story.Scenes.Single(s => s.Id == K + "epilogue.broken"), w),
                    "Corven's breakup has no ending.");
                var ending = story.Scenes.Single(s => s.Id == K + "epilogue.broken");
                foreach (var final in Program.Walk(ending, w, (id, _) => allPages.Add(ending.Id + "/" + id)))
                    check(final.Has(ending.Id), "Corven's breakup page has no terminal answer.");
            }
            foreach (var w in Program.Walk(dispatch, World(returned, stance, 74, careful)))
                check(!w.Has(K + "pursued") || w.Has("soana.round2.correspondence_only"), "Corven's escort is free when its debit is unaffordable.");
        }
        // r3: authentication-only inquiries have their own reply/proposal and
        // burned-letter outcomes, in both living and earned-return hosts.
        foreach (bool returned in new[] { false, true })
        {
            var bare = World(returned, "soana.partner_stance.share");
            bare.Flags.ExceptWith(new[] { "soana.partner_stance.share", "soana.committed" });
            Refresh(bare);
            var dispatch = S("dispatch", returned);
            var sent = Program.Walk(dispatch, bare, (id, _) => allPages.Add(dispatch.Id + "/" + id)).ToList();
            foreach (var letter in sent.Where(w => w.Has("soana.round2.correspondence_only")))
            {
                var reply = S("reply", returned);
                var answers = Program.Walk(reply, Later(letter, 168), (id, _) => allPages.Add(reply.Id + "/" + id));
                check(answers.Any(w => w.Has("soana.trickster.friends") && !w.Has("soana.round3.disclosed"))
                    && answers.Any(w => w.Has("soana.round3.disclosed") && w.Has("soana.round2.reply_accepted")),
                    "Authentication alone supplies lover terms, or cannot send a subsequent proposal.");
            }
            foreach (var letter in sent.Where(w => w.Has(K + "pursued") && !w.Has("soana.round2.correspondence_only")))
            {
                // Courtship chosen only after the question left: no disclosed bed.
                letter.Flags.Add("soana.partner_stance.share"); Refresh(letter);
                var home = S("homecoming", returned);
                Program.Walk(home, Later(letter, 168), (id, _) => allPages.Add(home.Id + "/" + id));
            }
            foreach (var letter in sent.Where(w => w.Has(K + "buried")))
            {
                var burned = S("returned_letter", returned);
                var answers = Program.Walk(burned, Later(letter, 72), (id, _) => allPages.Add(burned.Id + "/" + id));
                check(answers.All(w => w.Has(K + "corven_distant") && w.Has(K + "romance_ended")
                    && !w.Has(K + "affair_exposed")), "Burning a family inquiry invents a prior lover.");
            }
        }
        foreach (bool returned in new[] { false, true })
        {
            var late = story.Scenes.Single(s => s.Id == "soana.trickster.epilogue." + (returned ? "commit" : "luck_late"));
            var w = World(returned, "soana.partner_stance.share");
            w.Flags.ExceptWith(new[] { "soana.committed", "soana.partner_stance.share" });
            w.Flags.UnionWith(returned ? new[] { "soana.trickster.accounting_invited" }
                                      : new[] { "soana.trickster.luck_kept", "soana.trickster.cost.die_in_her_bowl", "soana.trickster.luck_tested" });
            Refresh(w);
            check(Rules.Available(story, late, w), "Stance choices changed the postwar invitation gate.");
            var reached = new HashSet<string>();
            var histories = new List<Snapshot> { w };
            var alternative = Program.Copy(w);
            if (returned)
            {
                // Mid-page old-save coverage, not a claim that the off-path book opens.
                alternative.Flags.Add("trickster.failed"); Refresh(alternative);
                check(!Rules.Available(story, late, alternative), "Off-path late book is newly available.");
            }
            else alternative.Flags.Add("soana.late_thorn_tested");
            histories.Add(alternative);
            var results = histories.SelectMany(input => Program.Walk(late, input, (id, _) => reached.Add(id))).ToList();
            check(results.Any(r => r.Has(K + "exclusive_chosen"))
                  && results.Any(r => r.Has("soana.partner_stance.exclusive") && r.Has("soana.closed")),
                "Postwar source lacks its earned yes or old-save refusal.");
            foreach (var final in results)
            {
                var stances = new[] { "share", "exclusive", "secret" }.Count(s => final.Has("soana.partner_stance." + s));
                check(stances <= 1 && final.Has(K + "agreed") == (stances == 1) && !final.Has("soana.committed"),
                    "A postwar invitation loses its stance or rewrites its existing commitment contract.");
                check(final.Has("soana.closed") == (final.Has("soana.partner_stance.exclusive") && !final.Has(K + "exclusive_chosen")),
                    "Postwar exclusive acceptance/refusal loses its earned outcome.");
            }
            foreach (var page in late.Nodes)
                check(reached.Contains(page.Id), "Unplayed postwar stance page: " + late.Id + "/" + page.Id);
        }
        // Main supplies ChapterFlag during the postwar book. The structural
        // partner audit also admits chapter zero on this old MinChapter=0 page.
        foreach (bool trickster in new[] { false, true })
        foreach (bool known in new[] { false, true })
        {
            if (known && !trickster) continue;
            var w = new Snapshot { Chapter = 6 };
            w.Flags.UnionWith(new[] { "chapter_later", "soana.committed", "soana.late_campaign_kept", "soana.partner_stance.share" });
            // Round-two current love reads the actual family answer and
            // renewed invitation; a historical commitment alone is insufficient.
            w.Flags.UnionWith(new[] { "soana.started", "soana.after_quest", "soana.progression_kept",
                "soana.late_thorn_tested", "soana.late_future_chosen" });
            if (trickster) w.Flags.UnionWith(new[] { "trickster", "trickster.ever" });
            if (known) w.Flags.UnionWith(new[] { K + "corven_known_alive", K + "corven_together" });
            Refresh(w);
            var ending = story.Scenes.Single(s => s.Id == "soana.ending_kept_life");
            check(Rules.Available(story, ending, w) == (!trickster || known),
                "Kept-life ignores the current-path family answer or changes ordinary eligibility.");
            var visible = Rules.VisibleParagraphs(ending.Nodes[0], w);
            check(visible.Any(p => known ? p.Requires.Contains(K + "corven_together")
                                        : p.Forbids.Contains(K + "corven_known_alive")),
                "Kept-life hides Corven's state in a runtime postwar history.");
        }
        foreach (var s in story.Scenes.Where(s => s.Id.StartsWith(K, StringComparison.Ordinal)))
            foreach (var page in s.Nodes.Where(n => !n.Id.Contains("_r3_", StringComparison.Ordinal)))
                check(allPages.Contains(s.Id + "/" + page.Id), "Unplayed Corven page: " + s.Id + "/" + page.Id);
        // Exercise the full runner's prerequisite-only fixture for these new
        // pages too, including a save with no other romance history supplied.
        var previouslyPlayed = story.Scenes.Where(s => !s.Id.StartsWith(K, StringComparison.Ordinal))
            .Select(s => s.Id).ToHashSet();
        Program.CheckDraftScenes(previouslyPlayed);
        Console.WriteLine("PASS: Soana partner stance, paid native/returned Corven journeys, disclosure and breakup.");
    }
}
