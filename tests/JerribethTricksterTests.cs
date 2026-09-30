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
              && king.NativeReturnCue == "7b050ba0745bf144e815632e39b34853" && king.Nodes[0].Speaker == king.Owner && king.Nodes.Skip(1).All(n => n.Speaker == "Narrator"),
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
        // BEL: the lease holds by a rule the route plants first (a thought the house keeps outlives its mother, as her
        // Wintersun ideas did), and the payoff cites that rule; the rent is hers to set and is paid in the Commander's memories.
        string Text(Scene s) => string.Join(" ", s.Nodes.Select(n => n.Text));
        check(Text(greeting).Contains("Wintersun") && Text(greeting).Contains("one of your memories a month")
              && Text(final).Contains("Ask Wintersun") && Text(tenant).Contains("Wintersun") && !Text(tenant).Contains("evicted by a sword"),
            "The lease law is not planted before the tenant pays it off.");
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
        var tenantNexus = S("jerribeth.trickster.dead.tenant_nexus");
        var latePay = World(story, 4, "trickster", "trickster.ever", "jerribeth.met", Dead, Primed, "jerribeth.trickster.cost.late");
        latePay.Area = "7847c3e3537104f4694167af0b9fcd0e";   // the Nexus, where Chapter 4 letters are read
        check(Rules.Available(story, tenantNexus, latePay) && !Rules.Available(story, tenant, latePay) && !Rules.Available(story, backdated, latePay),
            "Trk_Jerribeth_Dead_LatePayoff: wrong device.");
        var lodger = Program.Walk(tenantNexus, latePay).Single(r => r.Has("jerribeth.trickster.cost.lodger"));
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
        var failedPrimed = World(story, 5, "trickster.was", "trickster.failed", "jerribeth.met", Dead, Primed);
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
            // Directive 12: a Trickster contract is countersigned in person, and the cut lands at the start of the act.
            check(pages.Contains("arrival") && pages.Contains("threshold") && pages.Contains("morning") && !pages.Contains("tenant_room"),
                "The committed contract has no in-person threshold.");
            check(pages.Contains("ask") && pages.Contains("threshold_free") && pages.Contains("morning_free"),
                "Her restraint is not the Commander's choice, or keeping your hands has no distinct outcome.");
            check(outs.Where(r => r.Has("jerribeth.committed")).All(r => r.Has("jerribeth.future")), "The visit does not finish the promise.");
            var tenantW = Program.Copy(w); tenantW.Flags.UnionWith(new[] { Dead, Returned, "jerribeth.trickster.cost.host" });
            var tenantPages = new HashSet<string>();
            var tenantOuts = Program.Walk(future, tenantW, (page, _) => tenantPages.Add(page));
            check(tenantPages.Contains("tenant_room") && tenantPages.Contains("tenant_host") && tenantPages.Contains("tenant_body")
                  && !tenantPages.Contains("arrival") && tenantOuts.Any(r => r.Has("jerribeth.committed")),
                "The tenant's threshold is missing, or she knocks at a door she cannot use.");
            check(tenantPages.Contains("tenant_pinned") && tenantPages.Contains("tenant_free") && tenantPages.Contains("tenant_morning_free"),
                "The tenant pins without asking, or reaching for her has no distinct outcome.");
            // The toast branch pays a stranger's price before the courtship (host, memory, or a grudge), each reachable.
            var invite = S("jerribeth.invitation");
            var tw = World(story, 5, "trickster", "trickster.ever", "jerribeth.trickster.met_by_toast", "jerribeth.started");
            var tpages = new HashSet<string>();
            var touts = Program.Walk(invite, tw, (page, _) => tpages.Add(page));
            check(tpages.Contains("toast_price") && tpages.Contains("toast_given") && tpages.Contains("toast_paid") && tpages.Contains("toast_refused")
                  && touts.Any(r => r.Has("jerribeth.trickster.cost.toast_host")) && touts.Any(r => r.Has("jerribeth.trickster.cost.toast_memory")),
                "The toast branch skips the stranger's price, or one of its answers is unreachable.");
        }
        check(S("jerribeth.trickster.dead.tenant").Nodes.Concat(future.Nodes).All(n => !n.Text.Contains("thrust")),
            "The cut lands after the start of the act.");

        // JER-08 on a Trickster run: the purchaser/counteroffer campaign does not open; a toasted late entry ends at
        // the promise. Worst Chapter 5 branch (the toast): the seven rest letters of the core courtship (short_invitation is a
        // manual read), under the Chapter 5 cap of 8.
        check(!Rules.Available(story, S("jerribeth.offered_signature"),
                  World(story, 5, "trickster", "trickster.ever", "jerribeth.met", "jerribeth.commission", "jerribeth.terms", "jerribeth.lovers")),
            "The counteroffer campaign opens on a Trickster run.");
        check(Rules.Available(story, S("jerribeth.offered_signature"),
                  World(story, 5, "jerribeth.met", "jerribeth.commission", "jerribeth.terms", "jerribeth.lovers")),
            "The counteroffer campaign is lost off the path.");
        var lateLetters = story.Scenes.Where(s => s.Relationship == "jerribeth" && s.Remote && !s.Reaction && !s.ManualOnly
                                                  && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                                                  && !s.Id.StartsWith("jerribeth.trickster.", StringComparison.Ordinal)
                                                  && s.Chapters.Contains(5) && !s.Forbids.Contains(Toasted) && !s.Forbids.Contains("trickster.ever")
                                                  && !s.Requires.Any(r => r.Contains("counter") || r.Contains("purchaser") || r.Contains("settlement")
                                                                          || r.Contains("sale_") || r.Contains("unsold") || r.Contains("consequences_kept")
                                                                          || r == "jerribeth.offered_signature" || r == "jerribeth.fate_note_prepared"))
            .Select(s => s.Id).OrderBy(x => x).ToArray();
        check(lateLetters.SequenceEqual(new[] { "jerribeth.commission", "jerribeth.evening", "jerribeth.future",
                                               "jerribeth.guise", "jerribeth.invitation", "jerribeth.price", "jerribeth.question" }),
            "The toasted late entry has more than the core courtship: " + string.Join(",", lateLetters));
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
        check(reactions.Length == 7 && reactions.All(r => r.Owner == "Camellia" || r.Owner == "Woljif"), "Jerribeth reactions changed.");
        var hostWorld = World(story, 3, "trickster.ever", "jerribeth.met", Dead, Returned, "jerribeth.trickster.cost.host");
        check(Rules.Available(story, S("jerribeth.trickster.reaction.camellia_host"), hostWorld)
              && !Rules.Available(story, S("jerribeth.trickster.reaction.camellia"), hostWorld), "Camellia's host line misrouted.");
        var levyWorld = toastOut.Single(r => r.Has(Toasted));
        check(Rules.Available(story, S("jerribeth.trickster.reaction.woljif_levy"), levyWorld)
              && !Rules.Available(story, S("jerribeth.trickster.reaction.woljif"), levyWorld), "Woljif's levy line misrouted.");

        // --- Sol quality pass (2026-09-30) ----------------------------------------------------------------------------
        const string Forfeit = "jerribeth.trickster.cost.forfeit", Offered = "jerribeth.trickster.forfeit_named";
        const string Saw = "jerribeth.camellia_spectacle_heard", Taken = "trickster.lastcall.taken";
        string Words(Scene s) => string.Join(" ", s.Nodes.Select(n => n.Text).Concat(s.Nodes.SelectMany(n => n.Paragraphs).Select(p => p.Text)));
        int Visible(Scene s, Snapshot w, string needle) =>
            s.Nodes.SelectMany(n => Rules.VisibleParagraphs(n, w)).Count(p => p.Text.Contains(needle));
        bool Shown(Choice ch, Snapshot w) => Rules.Match(ch.Requires, ch.Forbids, w);

        // CAN: Camellia recalls her Sanctum remark only when the player heard it (SeenCues JerribetnFinal/Cue_0039).
        check(story.SeenCues.TryGetValue(Saw, out var sawCues) && sawCues.SequenceEqual(new[] { "f52f61f9f2ada7045a3b7f2f89350b95" }),
            "Camellia's Sanctum remark is not bound as a seen cue.");
        foreach (bool heard in new[] { false, true })
        foreach (bool host in new[] { false, true })
        {
            var w = World(story, 3, "trickster.ever", "jerribeth.met", Dead, Returned);
            if (heard) w.Flags.Add(Saw);
            if (host) w.Flags.Add("jerribeth.trickster.cost.host");
            var open = reactions.Where(r => r.Owner == "Camellia" && Rules.Available(story, r, w)).ToList();
            check(open.Count == 1 && Words(open[0]).Contains("repugnant spectacle") == heard && Words(open[0]).Contains("stockade") == host,
                "Camellia's reaction claims a Sanctum memory the player never heard, or misses the one they did (heard " + heard + ", host " + host + ").");
        }
        foreach (var r in reactions.Where(x => x.Owner == "Camellia" && x.Forbids.Contains("camellia.dead")))
            check(r.ForbidOverrides.TryGetValue("camellia.dead", out var lift) && lift == "camellia.trickster.returned",
                "A Camellia reaction does not lift her retained death on her return: " + r.Id);

        // CAN/BEL (Sol r0, r1): the tenant letter is a Drezen letter (Chapters 3, 5) or its Nexus twin (Chapter 4), never both.
        // At the Nexus the Golarion vessels are ordered and the host only promised; he is taken on the first Drezen rest of
        // Chapter 5 (host.taken), and no line claims his body before then.
        const string Nexus = "7847c3e3537104f4694167af0b9fcd0e", Promised = "jerribeth.trickster.host_promised", Host = "jerribeth.trickster.cost.host";
        var hostTaken = S("jerribeth.trickster.host.taken");
        foreach (var node in new[] { "statue_done", "locust_done" })
            check(tenantNexus.Nodes.Single(n => n.Id == node).Text.Contains("first hand going that way"),
                "A Golarion vessel is delivered at the Nexus: " + node);
        foreach (var (chapter, area) in new[] { (3, Drezen), (4, Nexus), (5, Drezen) })
        {
            var w = Later(story, World(story, chapter, "trickster", "trickster.ever", "jerribeth.met", Dead, Primed), 48);
            w.Area = area;
            var device = area == Nexus ? tenantNexus : tenant;
            check(Rules.Available(story, device, w) && !Rules.Available(story, area == Nexus ? tenant : tenantNexus, w),
                "Not exactly one tenant letter in chapter " + chapter);
            var outs = Program.Walk(device, w);
            check(new[] { "statue", "locust" }.All(x => outs.Any(r => r.Has("jerribeth.trickster.body." + x)))
                  && outs.Any(r => r.Has("jerribeth.trickster.cost.lodger")) && outs.Any(r => r.Has(area == Nexus ? Promised : Host))
                  && outs.All(r => !(area == Nexus && r.Has(Host))), "A house choice is unreachable, or the host is taken at the Nexus: " + chapter);
        }
        // Walk the promised host through Nexus rests: nothing claims his body; then the Drezen fulfillment takes him.
        var atNexus = Later(story, World(story, 4, "trickster", "trickster.ever", "jerribeth.met", Dead, Primed), 48);
        atNexus.Area = Nexus;
        var promised = Program.Walk(tenantNexus, atNexus).Single(r => r.Has(Promised));
        check(!Words(tenantNexus).Contains("Nobody asks the man's name"), "The Nexus letter narrates the taking.");
        var nexusRest = Later(story, promised, 48);
        check(!Rules.Available(story, hostTaken, nexusRest), "The host is taken at a Nexus rest.");
        var hostPages = new HashSet<string>();
        foreach (var id in new[] { "jerribeth.invitation", "jerribeth.question" })
        {
            var sc = S(id);
            check(Rules.Available(story, sc, nexusRest), "A Nexus core letter is not delivered to the promised tenant: " + id);
            nexusRest = Later(story, Program.Walk(sc, nexusRest, (page, _) => hostPages.Add(id + "/" + page)).First(r => r.Has(id) && !r.Has("jerribeth.closed")), 48);
        }
        check(!hostPages.Any(p => p.EndsWith("/ev_host") || p.EndsWith("/tenant_host")), "A Nexus letter claims the promised body.");
        var home = Program.Copy(nexusRest); home.Chapter = 5; home.Area = Drezen; Rules.Complete(story, home);
        check(Rules.Available(story, hostTaken, home) && Program.Walk(hostTaken, home).Single().Has(Host), "The promised host is never taken in Drezen.");

        // INT: naming the forfeit only offers it; the contract exists at the committing answer. Declining after naming
        // collects nothing on any ending.
        foreach (string branch in new[] { "jerribeth.settlement_kept", "jerribeth.short_future_requested" })
        {
            var w = World(story, 5, "trickster", "trickster.ever", "jerribeth.met", "jerribeth.commission", "jerribeth.lovers", branch);
            var outs = Program.Walk(future, w);
            check(outs.Any(r => r.Has(Offered) && r.Has("jerribeth.closed")), "The name-then-decline negotiation is unreachable: " + branch);
            check(outs.All(r => r.Has(Forfeit) == r.Has("jerribeth.committed")), "The forfeit is set without the contract, or the contract without it: " + branch);
            foreach (var cancelled in outs.Where(r => r.Has(Offered) && !r.Has("jerribeth.committed")))
            {
                var end = World(story, 6, cancelled.Flags.ToArray());
                check(!cancelled.Has(Forfeit) && Rules.Available(story, apart, end) && Visible(apart, end, "forfeit") == 0,
                    "ending_apart collects a forfeit from a negotiation that never became a contract.");
            }
        }

        // COX: exactly one forfeit collection per history. Last Call's coda owns it when it plays; otherwise the ending does.
        var lcPage = S("jerribeth.lastcall.page");
        var ascended = S("jerribeth.ending_ascended");
        foreach (bool lastCall in new[] { false, true })
        foreach (var vessel in new[] { "", "jerribeth.trickster.body.statue", "jerribeth.trickster.body.locust", "jerribeth.trickster.cost.host", "jerribeth.trickster.cost.lodger" })
        {
            var flags = new List<string> { "trickster.ever", "jerribeth.met", "jerribeth.committed", "jerribeth.lovers", Forfeit, "ending.trickster" };
            if (vessel != "") flags.AddRange(new[] { Dead, Returned, "jerribeth.trickster.cost.tenant", vessel });
            if (lastCall) flags.Add(Taken);
            var w = World(story, 6, flags.ToArray());
            check(w.Has("lastcall.active") == lastCall, "Last Call activity misread in the forfeit walk.");
            // One ending page per history: count its paragraphed (terminal) node once, plus the coda when it plays.
            int OnPage(Scene s) => Rules.Available(story, s, w)
                ? Rules.VisibleParagraphs(s.Nodes.First(n => n.Paragraphs.Count > 0), w).Count(p => p.Text.Contains("forfeit")) : 0;
            int collections = OnPage(together) + OnPage(ascended) + OnPage(lcPage);
            check(Rules.Available(story, together, w) && collections == 1,
                "The single forfeit is collected " + collections + " times (Last Call " + lastCall + ", vessel '" + vessel + "').");
            if (!lastCall) continue;
            check(Rules.Available(story, lcPage, w), "The committed coda is missing on Last Call.");
            check((Visible(lcPage, w, "gilt idol") == 1) == (vessel == "jerribeth.trickster.body.statue"),
                "The Last Call idol ignores the vessel she chose: '" + vessel + "'.");
            check((Visible(lcPage, w, "her rent") > 0) == (vessel != ""), "Last Call charges rent to a Jerribeth who is no tenant.");
        }
        // The call-in answers what she is: a tenant, a toasted stranger, or a living demon holding a forfeit. One line each.
        var callIn = S("jerribeth.lastcall.call");
        foreach (var deal in new[] { new[] { "jerribeth.trickster.cost.tenant", "jerribeth.trickster.cost.lodger" },
                                     new[] { "jerribeth.trickster.cost.tenant", "jerribeth.trickster.cost.host", Forfeit },
                                     new[] { "jerribeth.trickster.cost.toast", Forfeit }, new[] { Forfeit } })
        {
            var w = World(story, 6, deal.Concat(new[] { "trickster.ever" }).ToArray());
            var lines = callIn.Nodes[0].Choices.Where(ch => Shown(ch, w)).ToList();
            bool tenantDeal = deal.Contains("jerribeth.trickster.cost.tenant");
            check(lines.Count == 1 && lines[0].Text.Contains("tenant") == tenantDeal && lines[0].Text.Contains("toasted") == (!tenantDeal && deal.Contains("jerribeth.trickster.cost.toast")),
                "The Last Call call-in assumes every deal made her a skull tenant: " + string.Join(",", deal));
        }
        check(!Words(callIn).Contains("back of your skull") && !Words(lcPage).Contains("succubus"), "The call-in or coda misstates what she is.");

        // BEL: the late commit is staged by what she is, has its own intimate threshold (cut at the start of the act) and a
        // morning, and keeps a nonsexual refusal. The tenant with no body never knocks, and the host never lends his body.
        foreach (var vessel in new[] { "", "jerribeth.trickster.cost.host", "jerribeth.trickster.cost.lodger", "jerribeth.trickster.body.statue", "jerribeth.trickster.body.locust" })
        {
            var flags = new List<string> { "trickster.ever", "jerribeth.met", "jerribeth.attracted", "jerribeth.commission", "jerribeth.lovers" };
            if (vessel != "") flags.AddRange(new[] { Dead, Returned, "jerribeth.trickster.cost.tenant", vessel });
            var w = World(story, 6, flags.ToArray());
            check(Rules.Available(story, epCommit, w), "The late commit is missing for vessel '" + vessel + "'.");
            var pages = new HashSet<string>();
            var outs = Program.Walk(epCommit, w, (page, _) => pages.Add(page));
            bool mind = vessel != "" && vessel != "jerribeth.trickster.cost.host";
            check(epCommit.Nodes[0].Paragraphs.Count(p => Rules.ParagraphVisible(p, w)) == 1
                  && Rules.VisibleParagraphs(epCommit.Nodes.Single(n => n.Id == "collected"), w).Count(p => p.Text.Contains("muster")) == 1,
                "The late commit's arrival or muster is not exactly one variant for vessel '" + vessel + "'.");
            check(pages.Contains("collected") && (mind ? pages.Contains("torn_mind") && pages.Contains("signed_mind") && !pages.Contains("signed")
                                                        : pages.Contains("torn") && pages.Contains("signed") && !pages.Contains("signed_mind")),
                "The late commit's acceptance or refusal ignores what she is: '" + vessel + "'.");
            string night = vessel == "" ? "night" : "night_mind";
            string after = vessel == "" ? "night_after" : "night_mind_after";
            check(pages.Contains(night) && pages.Contains(after) && (vessel == "jerribeth.trickster.cost.host") == pages.Contains("night_host")
                  && (vessel == "") == pages.Contains("night"),
                "The accepted late commit has no staged threshold and morning for vessel '" + vessel + "'.");
            check(outs.Count >= 3, "The late commit lost its table-only or refusal branch: '" + vessel + "'.");
        }
        foreach (var id in new[] { "night", "night_mind" })
            check(epCommit.Nodes.Single(n => n.Id == id).Text.Contains("lowered herself onto the Commander")
                  && !epCommit.Nodes.Single(n => n.Id == id).Text.Contains("thrust"), "The late commit's cut misses the start of the act: " + id);

        // --- Sol round 1 -----------------------------------------------------------------------------------------------
        // Fresh histories: native observations are completed before every rest, authored prerequisites come only from
        // their producers, manual reads are omitted, and every delivered letter must open with a visible answer.
        var possessive = new[] { "ev_host", "tenant_host", "night_host" };
        (Snapshot State, List<string> Letters) Deliver(Snapshot from, int rests)
        {
            var s = Program.Copy(from);
            var got = new List<string>();
            for (int i = 0; i < rests; i++)
            {
                s.Hour += 48;
                Rules.Complete(story, s);
                var next = story.Scenes.FirstOrDefault(x => x.Relationship == "jerribeth" && x.Remote && !x.ManualOnly && !x.Reaction
                    && !x.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && Rules.Available(story, x, s));
                if (next == null) break;
                check(next.Nodes[0].Choices.Any(ch => Rules.Match(ch.Requires, ch.Forbids, s)), "A delivered Jerribeth letter opens with no answer: " + next.Id);
                got.Add(next.Id);
                var outs = Program.Walk(next, s, (page, at) => check(!possessive.Contains(page) || at.Has(Host),
                    "A line claims the stockade host's body before he is taken: " + next.Id + "/" + page));
                s = outs.Where(r => r.Has(next.Id) && !r.Has("jerribeth.closed"))
                    .OrderByDescending(r => r.Has("jerribeth.fate_terms")).ThenByDescending(r => r.Has(Promised)).First();
            }
            return (s, got);
        }
        bool Device(string id) => id.StartsWith("jerribeth.trickster.", StringComparison.Ordinal);

        // INT (Sol r1): the promise is delivered on a fresh Trickster history once the commission's own answer asks for it,
        // and the live-Trickster fate answer is earned on the shorter negotiation, with the named forfeit kept.
        var freshStart = World(story, 3, "trickster", "jerribeth.met");
        check(freshStart.Has("trickster.ever"), "A native Trickster run does not latch trickster.ever.");
        var (ch3End, ch3Letters2) = Deliver(freshStart, 40);
        check(ch3Letters2.Contains("jerribeth.commission") && ch3End.Has("jerribeth.short_future_requested") && !ch3End.Has("jerribeth.settlement_kept"),
            "On the path, the commission does not ask for the shorter promise: " + string.Join(",", ch3Letters2));
        var beforeAsk = Program.Copy(ch3End); beforeAsk.Flags.Remove("jerribeth.short_future_requested"); beforeAsk.Chapter = 5;
        check(!Rules.Available(story, future, Later(story, beforeAsk, 48)), "The promise is delivered before anything asked for it.");
        var ch5Start = Program.Copy(ch3End); ch5Start.Chapter = 5;
        var (ch5, ch5Letters) = Deliver(ch5Start, 40);
        check(ch5Letters.Contains("jerribeth.future") && ch5.Has("jerribeth.committed") && ch5.Has("jerribeth.fate_terms") && ch5.Has(Forfeit)
              && ch5Letters.Contains("jerribeth.farewell") && ch5Letters.Count(x => !Device(x)) <= 8,
            "A fresh Trickster history does not earn the fate answer, the contract or the farewell: " + string.Join(",", ch5Letters));

        // BEL (Sol r1 cap): the living, previously met Jerribeth's countersigned contract has a companion witness.
        var visitor = S("jerribeth.trickster.reaction.woljif_visitor");
        check(!ch5.Has(Returned) && !ch5.Has(Toasted) && Rules.Available(story, visitor, ch5)
              && reactions.Where(r => r != visitor).All(r => !Rules.Available(story, r, ch5)),
            "The living contract has no companion reaction, or a device reaction plays beside it.");
        check(Words(visitor).Contains("memory") && Words(visitor).Contains("knocked"), "Woljif's line does not address the visitor or the pledged memory.");
        foreach (var device in new[] { new[] { Dead, Returned, "jerribeth.trickster.cost.tenant" }, new[] { Toasted } })
        {
            var w = Program.Copy(ch5); w.Flags.UnionWith(device);
            check(!Rules.Available(story, visitor, w), "Woljif's visitor line plays beside a device reaction.");
        }

        // COX (Sol r1): a correspondence first opened at the Nexus sends at most three letters in Chapter 4, for the living
        // Jerribeth and for the tenant (whose Nexus letter promises the host); the rest are Drezen letters.
        foreach (bool isDead in new[] { false, true })
        {
            var nexus = isDead ? Later(story, World(story, 4, "trickster", "jerribeth.met", Dead, Primed), 48) : World(story, 4, "trickster", "jerribeth.met");
            nexus.Area = Nexus;
            var (after4, ch4Letters) = Deliver(nexus, 40);
            check(ch4Letters.Count <= 3 && ch4Letters.Count >= 2 && ch4Letters.Contains("jerribeth.invitation"),
                "Chapter 4 is silent or over its three letters: " + string.Join(",", ch4Letters));
            check(!isDead || ch4Letters.Contains("jerribeth.trickster.dead.tenant_nexus") && after4.Has(Promised) && !after4.Has(Host),
                "The Nexus tenant letter does not promise the host.");
            var home5 = Program.Copy(after4); home5.Chapter = 5; home5.Area = Drezen;
            var (end5, ch5Tail) = Deliver(home5, 40);
            check(end5.Has("jerribeth.committed") && end5.Has("jerribeth.fate_terms") && ch5Tail.Count(x => !Device(x)) <= 8
                  && (!isDead || ch5Tail.Contains("jerribeth.trickster.host.taken") && end5.Has(Host) && ch5Tail.Count(Device) <= 2),
                "The delayed correspondence does not finish in Chapter 5 within its allowance: " + string.Join(",", ch5Tail));
        }
    }
}
