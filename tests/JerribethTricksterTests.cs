using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Jerribeth, Trickster (Writer/handoffs/trickster/jerribeth.md): the tenant (F14) and the toast (F05).
// One test block per spec rules test (Trk_Jerribeth_*), plus the registered-route edits (invitation, refuge, future,
// price, evening, JER-08, G6, paragraphs) and the reactions.
internal static class JerribethTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Dead = "jerribeth.unavailable";
    private const string Primed = "jerribeth.trickster.primed";
    private const string Returned = "jerribeth.trickster.returned";
    private const string Toasted = "jerribeth.trickster.met_by_toast";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
        if (chapter > 1) state.Flags.Add("chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags) state.Times[flag] = state.Hour - 1000;   // the world was observed long ago
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours)
    {
        var later = Program.Copy(state); later.Hour += hours; Rules.Complete(story, later); return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var greeting = S("jerribeth.trickster.dead.setup_greeting");
        var final = S("jerribeth.trickster.dead.setup_final");
        var backdated = S("jerribeth.trickster.dead.backdated");
        var tenant = S("jerribeth.trickster.dead.tenant");
        var king = S("jerribeth.trickster.never_met.toast_king");
        var toast = S("jerribeth.trickster.never_met.toast");
        var invitation = S("jerribeth.invitation");
        var epCommit = S("jerribeth.trickster.epilogue.commit");
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));

        // Hooks and shape.
        check(greeting.AnswerLists.SequenceEqual(new[] { "190fda58a169c9340b626f1a503c696f" })
              && greeting.NativeReturnCue == "4f8372200576ead4e86c7c2606c580d0" && greeting.EntryMythic == "PlayerIsTrickster"
              && greeting.ContactUnit == null, "Greeting lease left the native deal list.");
        check(final.AnswerLists.SequenceEqual(new[] { "5cca8ccea46e72343a4544c44be9790c" }) && final.NativeReturnCue == null,
            "The Sanctum-final lease must stay a non-inline scene beside [Attack].");
        check(king.AnswerLists.SequenceEqual(new[] { "6dccfd39947ef4242a8afbe36b21a46c" })
              && king.NativeReturnCue == "7b050ba0745bf144e815632e39b34853" && king.Nodes[0].Speaker == "conversant",
            "The King's toast left his tavern hub.");
        check(backdated.Remote && tenant.Remote && toast.Remote && backdated.TricksterDevice && tenant.TricksterDevice
              && backdated.TricksterState == "dead" && tenant.TricksterState == "dead", "Device scenes mislabelled.");
        check(backdated.Chapters.SequenceEqual(new[] { 3, 5 }), "The late lease is offered in the Abyss.");
        var rel = story.Relationships["jerribeth"];
        check(rel.UnavailableOverrides.TryGetValue(Dead, out var over) && over == Returned && rel.TricksterAccess.Count == 2,
            "Jerribeth relationship patch missing.");
        check(story.PermanentEtudes.Contains(Dead), "JER-11: JerribethDead is not permanent.");
        check(story.SelectedAnswers.ContainsKey("jerribeth.trickster.attack_final") && story.Derived.ContainsKey("jerribeth.killed_by_commander"),
            "The [Attack] answers are not bound.");

        // Trk_Jerribeth_Alive: the registered route runs; no device, no toast.
        var alive = World(story, 3, "trickster", "trickster.ever", "jerribeth.met");
        check(Rules.Available(story, invitation, alive) && !Any(alive, tenant, backdated, toast, king), "Trk_Jerribeth_Alive failed.");

        // Trk_Jerribeth_Setup_Greeting: the joke primes; the other primer closes.
        var ch3 = World(story, 3, "trickster");
        check(Rules.Available(story, greeting, ch3) && Rules.Available(story, final, ch3), "Primers unavailable in the Sanctum.");
        var leased = Program.Walk(greeting, ch3);
        check(leased.Count == 1 && leased[0].Has(Primed) && !Rules.Available(story, final, leased[0]), "Trk_Jerribeth_Setup_Greeting failed.");
        var lore = World(story, 3, "trickster", "jerribeth.egg_lore_heard");
        var lorePages = new HashSet<string>();
        check(Program.Walk(greeting, lore, (page, _) => lorePages.Add(page)).Single().Has(Primed) && lorePages.Contains("lore"),
            "Nenio's lecture is not read at the lease.");
        var finals = Program.Walk(final, ch3);
        check(finals.Any(r => r.Has(Primed)) && finals.Any(r => !r.Has(Primed) && !r.Has(final.Id)), "Final lease cannot be taken or left.");
        check(final.Nodes[0].Choices[0].Mythic == "PlayerIsTrickster", "Final lease joke is not a [Trickster] answer.");
        check(!Rules.Available(story, greeting, World(story, 4, "trickster")) && !Rules.Available(story, greeting, World(story, 3)),
            "Greeting lease outside Chapter 3 or off the path.");

        // Trk_Jerribeth_Setups_AfterDeath: both primers Forbid the death; the late lease opens.
        var dead = World(story, 3, "trickster", "trickster.ever", "jerribeth.met", Dead);
        check(!Any(dead, greeting, final) && Rules.Available(story, backdated, dead) && !Rules.Available(story, tenant, dead),
            "Trk_Jerribeth_Setups_AfterDeath failed.");

        // Trk_Jerribeth_Dead_Primed: the tenant after 48 h, choice 0 (statue).
        var primed = World(story, 3, "trickster", "trickster.ever", "jerribeth.met", Dead, Primed);
        primed.Times[Primed] = primed.Hour - 47;
        check(!Rules.Available(story, tenant, primed), "Tenant ignores the 48 h delay.");
        primed = Later(story, primed, 1);
        check(Rules.Available(story, tenant, primed) && !Rules.Available(story, backdated, primed), "Trk_Jerribeth_Dead_Primed: wrong device.");
        var house = tenant.Nodes.Single(n => n.Id == "house").Choices;
        check(house.Count == 5 && house[0].Crusade?.Resource == "Favors" && house[0].Crusade!.Amount == -100
              && house[1].Crusade?.Resource == "Materials" && house[1].Crusade!.Amount == -100
              && house[2].Alignment?.Direction == "Evil" && house[2].Alignment!.Value == 2
              && house[3].Alignment?.Direction == "Chaotic" && house[3].Alignment!.Value == 1 && house[4].Abort,
            "The house choices lost their price or their order.");
        var homes = Program.Walk(tenant, primed);
        var statue = homes.Where(r => r.Has("jerribeth.trickster.body.statue")).ToList();
        check(statue.Count == 1 && statue[0].Has(Returned) && statue[0].Has("jerribeth.trickster.cost.tenant") && statue[0].Has("jerribeth.started"),
            "Trk_Jerribeth_Dead_Primed: the statue does not return her.");
        check(homes.Count(r => r.Has(Returned)) == 4 && homes.Any(r => !r.Has(tenant.Id)), "Four homes and a 'not tonight' expected.");
        foreach (var r in homes.Where(r => r.Has(Returned)))
        {
            check(!Any(r, tenant, backdated) && !Rules.Failed(rel, r), "A second return, or the journal still fails.");
            check(Rules.Available(story, invitation, r), "The returned Jerribeth cannot reach the invitation.");
        }

        // Tenant variants: each read shows once, in order, only when its flag is held.
        foreach (var flags in new[] { new[] { "jerribeth.trickster.cost.late" }, new[] { "jerribeth.killed_by_commander" },
                                      new[] { "jerribeth.betrayed_commander", "jerribeth.insulted" }, new[] { "trickster.failed" }, new string[0] })
        {
            var w = Program.Copy(primed); w.Flags.UnionWith(flags);
            var pages = new HashSet<string>();
            Program.Walk(tenant, w, (page, _) => pages.Add(page));
            check(pages.Contains("v_late") == flags.Contains("jerribeth.trickster.cost.late")
                  && pages.Contains("v_killed") == flags.Contains("jerribeth.killed_by_commander")
                  && pages.Contains("v_betrayed") == flags.Contains("jerribeth.betrayed_commander")
                  && pages.Contains("v_insulted") == flags.Contains("jerribeth.insulted")
                  && pages.Contains("v_failed") == flags.Contains("trickster.failed") && pages.Contains("house"),
                "Tenant variants misread: " + string.Join(",", flags));
        }

        // Trk_Jerribeth_Dead_Unprimed: the late lease, at a price.
        var signedPath = backdated.Nodes.Single(n => n.Id == "tenant_late").Choices.Single(ch => ch.Next == "signed");
        check(signedPath.Mythic == "PlayerIsTrickster" && signedPath.Alignment?.Direction == "Evil" && signedPath.Alignment!.Value == 1,
            "The late lease is free.");
        var late = Program.Walk(backdated, dead);
        var signed = late.Single(r => r.Has(Primed));
        check(signed.Has("jerribeth.trickster.cost.late"), "Trk_Jerribeth_Dead_Unprimed: no cost.late.");
        var lorePathPages = new HashSet<string>();
        var loreDead = Program.Copy(dead); loreDead.Flags.Add("jerribeth.egg_lore_heard");
        check(Program.Walk(backdated, loreDead, (page, _) => lorePathPages.Add(page)).Count == 2 && lorePathPages.Contains("lore"),
            "Late lease ignores Nenio's lecture.");

        // Trk_Jerribeth_Dead_LatePayoff: Chapter 4, choice 3 (lodger).
        var latePay = World(story, 4, "trickster", "trickster.ever", "jerribeth.met", Dead, Primed, "jerribeth.trickster.cost.late");
        latePay.Area = "7847c3e3537104f4694167af0b9fcd0e";   // the Nexus, where Chapter 4 letters are read
        check(Rules.Available(story, tenant, latePay) && !Rules.Available(story, backdated, latePay), "Trk_Jerribeth_Dead_LatePayoff: wrong device.");
        var lodger = Program.Walk(tenant, latePay).Single(r => r.Has("jerribeth.trickster.cost.lodger"));
        check(lodger.Has(Returned), "Trk_Jerribeth_Dead_LatePayoff: the lodger does not return her.");

        // Trk_Jerribeth_Dead_Declined: canon fate stands by choice.
        var declined = late.Single(r => r.Has("jerribeth.trickster.declined"));
        var afterDecline = Later(story, declined, 500);
        check(!Any(afterDecline, tenant, backdated) && !declined.Has(Primed), "Trk_Jerribeth_Dead_Declined failed.");
        var declinedPrimed = Program.Copy(primed); declinedPrimed.Flags.Add("jerribeth.trickster.declined");
        check(!Rules.Available(story, tenant, declinedPrimed), "Tenant survives the decline.");

        // Trk_Jerribeth_Dead_PathFailed_(Un)Primed.
        var failed = World(story, 4, "trickster.was", "trickster.failed", "jerribeth.met", Dead);
        check(!Any(failed, tenant, backdated), "Trk_Jerribeth_Dead_PathFailed_Unprimed: a device survives the lost path.");
        var failedPrimed = World(story, 4, "trickster.was", "trickster.failed", "jerribeth.met", Dead, Primed);
        check(Rules.Available(story, tenant, failedPrimed) && !Rules.Available(story, backdated, failedPrimed),
            "Trk_Jerribeth_Dead_PathFailed_Primed failed.");

        // Trk_Jerribeth_NeverMet / _King.
        var never = World(story, 5, "trickster", "trickster.ever");
        check(Rules.Available(story, toast, never) && !Any(never, king, tenant, invitation), "Trk_Jerribeth_NeverMet: wrong scene.");
        var toastOut = Program.Walk(toast, never);
        check(toastOut.Any(r => r.Has(Toasted) && r.Has("jerribeth.trickster.cost.toast") && r.Has("jerribeth.trickster.toast_levy"))
              && toastOut.Any(r => !r.Has(toast.Id)), "Trk_Jerribeth_NeverMet: the toast does not reach her.");
        check(Rules.Available(story, invitation, toastOut.Single(r => r.Has(Toasted))), "The toast does not open the invitation.");
        var crowned = World(story, 5, "trickster", "trickster.ever", "fool_king.crowned");
        check(Rules.Available(story, king, crowned) && !Rules.Available(story, toast, crowned), "Trk_Jerribeth_NeverMet_King: wrong scene.");
        var kingOut = Program.Walk(king, crowned);
        check(kingOut.Any(r => r.Has(Toasted) && r.Has("jerribeth.trickster.cost.toast") && !r.Has("jerribeth.trickster.toast_levy"))
              && kingOut.Any(r => !r.Has(king.Id)), "Trk_Jerribeth_NeverMet_King failed.");
        check(!Rules.Available(story, toast, World(story, 5, "trickster", "trickster.ever", "jerribeth.met"))
              && !Rules.Available(story, toast, World(story, 5, "trickster.was", "trickster.failed")), "Toast for a Commander who met her, or off the path.");

        // Trk_Jerribeth_ThirdDate (TT-05 slice): exactly one of {invitation, tenant, toast(s)} per state, after each branch.
        foreach (var branch in new[] { "", "jerribeth.betrays_vellexia", "jerribeth.patron_lost" })
        {
            var extra = branch == "" ? new string[0] : new[] { branch };
            var worlds = new[] {
                World(story, 5, extra.Concat(new[] { "trickster", "trickster.ever", "jerribeth.met" }).ToArray()),
                Later(story, World(story, 5, extra.Concat(new[] { "trickster", "trickster.ever", "jerribeth.met", Dead, Primed }).ToArray()), 48),
                World(story, 5, extra.Concat(new[] { "trickster", "trickster.ever" }).ToArray()) };
            foreach (var w in worlds)
                check(new[] { invitation, tenant, toast, king }.Count(s => Rules.Available(story, s, w)) == 1, "Trk_Jerribeth_ThirdDate: not exactly one scene.");
        }

        // Registered edit 1: the invitation's variants.
        var invStart = invitation.Nodes[0].Choices;
        check(invStart[0].Next == "voice" && invStart[0].Forbids.Contains(Returned) && invStart[0].Forbids.Contains(Toasted)
              && invStart.Skip(3).Select(ch => ch.Next).SequenceEqual(new[] { "voice_tenant", "voice_toast" }),
            "Invitation variants were not appended.");
        check(!invitation.Requires.Contains("jerribeth.met") && invitation.RequiresAny.Contains(Toasted), "Invitation gate not widened.");

        // Registered edit 3: her terms before any promise, on a Trickster run only; the blank page is her hard no.
        var future = S("jerribeth.future");
        foreach (bool trickster in new[] { false, true })
        foreach (string branch in new[] { "jerribeth.settlement_kept", "jerribeth.short_future_requested" })
        {
            var w = World(story, 5, "jerribeth.met", "jerribeth.commission", branch);
            if (trickster) { w.Flags.Add("trickster"); w.Flags.Add("trickster.ever"); }
            var pages = new HashSet<string>();
            var outs = Program.Walk(future, w, (page, _) => pages.Add(page));
            check(pages.Contains("her_terms") || pages.Contains("her_terms_short") ? trickster : !trickster, "Her terms shown off the path, or missing on it.");
            if (!trickster) continue;
            check(outs.Where(r => r.Has("jerribeth.committed")).All(r => r.Has("jerribeth.trickster.cost.forfeit")), "A Trickster promise without a forfeit.");
            check(outs.Any(r => r.Has("jerribeth.committed")), "No Trickster commit.");
            check(outs.Any(r => r.Has("jerribeth.closed") && r.Has("jerribeth.trickster.no_forfeit")), "Her blank-page no is missing.");
        }
        var fe = future.Nodes.Single(n => n.Id == "future_entry").Choices;
        check(fe[0].Next == "start" && fe[1].Next == "short_future" && fe[2].Next == "her_terms" && fe[3].Next == "her_terms_short",
            "future_entry choices reordered instead of appended.");

        // Registered edit 2: the refuge gates on her own evidence only.
        var refuge = S("jerribeth.refuge");
        check(!refuge.Requires.Contains("jerribeth.patron_lost"), "The refuge still waits on Vellexia's fate.");
        foreach (bool lost in new[] { false, true })
        {
            var w = World(story, 4, "jerribeth.met", "jerribeth.evening", "jerribeth.refuge_known");
            if (lost) w.Flags.Add("jerribeth.patron_lost");
            w.Area = "7847c3e3537104f4694167af0b9fcd0e";
            var pages = new HashSet<string>();
            Program.Walk(refuge, w, (page, _) => pages.Add(page));
            check((pages.Contains("left_need") || pages.Contains("left_anger")) == lost, "Refuge variant ignores whether she left the manor.");
        }

        // Registered edit 4: price and evening for the tenant.
        var tenantState = World(story, 3, "trickster.ever", "jerribeth.met", Dead, Returned, "jerribeth.trickster.cost.tenant",
                                "jerribeth.trickster.cost.host", "jerribeth.trickster.cost.late", "jerribeth.guise", "jerribeth.price");
        var pricePages = new HashSet<string>();
        var prices = Program.Walk(S("jerribeth.price"), tenantState, (page, _) => pricePages.Add(page));
        check(pricePages.Contains("trust_tenant") && !pricePages.Contains("refuse") && !pricePages.Contains("wintersun")
              && prices.Any(r => r.Has("jerribeth.terms")) && prices.Any(r => r.Has("jerribeth.closed")), "Price ignores the tenant.");
        var evPages = new HashSet<string>();
        Program.Walk(S("jerribeth.evening"), tenantState, (page, _) => evPages.Add(page));
        check(evPages.Contains("tenant_evening") && evPages.Contains("ev_host") && evPages.Contains("ev_late") && !evPages.Contains("ev_lodger"),
            "Evening ignores how she lives.");

        // Registered edit 5: JER-08.
        var ch3Letters = story.Scenes.Where(s => s.Relationship == "jerribeth" && s.Remote && !s.Id.StartsWith("jerribeth.trickster.", StringComparison.Ordinal)
                                                 && s.Chapters.Contains(3)).Select(s => s.Id).OrderBy(x => x).ToArray();
        check(ch3Letters.SequenceEqual(new[] { "jerribeth.collection", "jerribeth.commission", "jerribeth.evening", "jerribeth.guise",
                                               "jerribeth.invitation", "jerribeth.parting", "jerribeth.price", "jerribeth.question" }),
            "JER-08: the Chapter 3 letters are not the eight: " + string.Join(",", ch3Letters));

        // Epilogues: G6 overrides, the late commit, and the paragraphs.
        var endLodger = World(story, 6, "trickster.ever", "jerribeth.met", Dead, Returned, "jerribeth.committed",
                              "jerribeth.trickster.cost.tenant", "jerribeth.trickster.cost.lodger", "jerribeth.trickster.cost.forfeit");
        var together = S("jerribeth.ending_together");
        check(Rules.Available(story, together, endLodger), "G6: the returned tenant has no ending.");
        check(together.Nodes.Where(n => n.Paragraphs.Count > 0).All(n => Rules.VisibleParagraphs(n, endLodger).Length == 2),
            "Tenant paragraphs missing on her ending.");
        var late2 = World(story, 6, "trickster.ever", "jerribeth.met", "jerribeth.attracted", "jerribeth.commission", "jerribeth.lovers");
        check(Rules.Available(story, epCommit, late2) && !Rules.Available(story, S("jerribeth.ending_unfinished"), late2),
            "Trk_Jerribeth_EpilogueCommit failed.");
        var refused = World(story, 6, "trickster.ever", "jerribeth.met", "jerribeth.commission", "jerribeth.lovers", "jerribeth.closed",
                            "jerribeth.trickster.no_forfeit");
        var apart = S("jerribeth.ending_apart");
        check(!Rules.Available(story, epCommit, refused) && Rules.Available(story, apart, refused)
              && Rules.VisibleParagraphs(apart.Nodes[0], refused).Length == 1, "Trk_Jerribeth_EpilogueCommit_Refused failed.");
        var deadNoReturn = World(story, 6, "trickster.ever", "jerribeth.met", Dead, "jerribeth.commission", "jerribeth.lovers");
        check(!Rules.Available(story, epCommit, deadNoReturn), "The late commit brings a dead Jerribeth to the door.");
        var canon = World(story, 6, "jerribeth.met", "jerribeth.attracted");
        check(Rules.Available(story, S("jerribeth.ending_unfinished"), canon), "Off the path, the unfinished ending is lost.");

        // Reactions: Camellia and Woljif only.
        var reactions = story.Scenes.Where(s => s.Relationship == "jerribeth" && s.Reaction).ToArray();
        check(reactions.Length == 4 && reactions.All(r => r.Owner == "Camellia" || r.Owner == "Woljif"), "Jerribeth reactions changed.");
        var hostWorld = World(story, 3, "trickster.ever", "jerribeth.met", Dead, Returned, "jerribeth.trickster.cost.host");
        check(Rules.Available(story, S("jerribeth.trickster.reaction.camellia_host"), hostWorld)
              && !Rules.Available(story, S("jerribeth.trickster.reaction.camellia"), hostWorld), "Camellia's host line misrouted.");
        var levyWorld = toastOut.Single(r => r.Has(Toasted));
        check(Rules.Available(story, S("jerribeth.trickster.reaction.woljif_levy"), levyWorld)
              && !Rules.Available(story, S("jerribeth.trickster.reaction.woljif"), levyWorld), "Woljif's levy line misrouted.");
    }
}
