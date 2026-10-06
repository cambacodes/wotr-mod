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
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000,
            // eng-final / E-Q8-10: fund these positive histories; the walker enforces every debit.
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        // These positive predicate fixtures represent an already accepted route.
        // Coarse-key negatives are independent in PayoffDepartureRulesTests.
        foreach (var rel in story.Relationships)
            if (flags.Contains(rel.Value.CommittedFlag) && story.Derived.ContainsKey(rel.Key + ".payoff.ordinary"))
                HouseholdTests.Earn(story, state, rel.Key + ".payoff.ordinary");
        foreach (var context in flags.Where(story.Derived.ContainsKey))
            HouseholdTests.Earn(story, state, context);
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
        string Text(Scene s) => string.Join(" ", s.Nodes.Select(n => SurfaceIds.Of(story, n)));
        check(SurfaceIds.Has(Text(greeting), "[jerribeth.trickster.dead.setup_greeting/lease]") && SurfaceIds.Has(Text(greeting), "[jerribeth.trickster.dead.setup_greeting/lease]")
              && SurfaceIds.Has(Text(final), "[jerribeth.trickster.dead.setup_final/accepted]") && SurfaceIds.Has(Text(tenant), "[jerribeth.trickster.dead.tenant/tenant][jerribeth.trickster.dead.tenant/statue_done]"),
            "The lease law is not planted before the tenant pays it off.");
        check(!Rules.Available(story, greeting, World(story, 4, "trickster")) && !Rules.Available(story, greeting, World(story, 3)),
            "Greeting lease outside Chapter 3 or off the path.");

        // Trk_Jerribeth_Setups_AfterDeath: both primers Forbid the death; the late lease opens.
        var dead = World(story, 3, "trickster", "trickster.ever", "jerribeth.met", Dead);
        check(!Any(dead, greeting, final) && Rules.Available(story, backdated, dead) && !Rules.Available(story, tenant, dead),
            "Trk_Jerribeth_Setups_AfterDeath failed.");

        // Trk_Jerribeth_Dead_Primed: the tenant after 48 h, choice 0 (statue).
        var primed = World(story, 3, "trickster", "trickster.ever", "jerribeth.met", Dead, Primed, "jerribeth.xanthir_known");
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
            if (flags.Contains("jerribeth.killed_by_commander")) HouseholdTests.Earn(story, w, "jerribeth.killed_by_commander");
            Rules.Complete(story, w);
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
        check(!Any(failedPrimed, tenant, backdated),
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
              && invStart.Skip(3).Select(ch => ch.Next).SequenceEqual(new[] { "voice_tenant", "voice_toast", "voice_toast_levy" }),
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
            check(pages.Contains("arrival_note") && !pages.Contains("arrival") && !pages.Contains("threshold") && !pages.Contains("tenant_room"),
                "The living contract stages a bodily visit inside a letter (ledger R2-3).");
            var visitScene = S("jerribeth.trickster.visit");
            check(!visitScene.Remote && visitScene.InteractionHub == "jerribeth.presence" && story.Presences.ContainsKey("jerribeth.presence"),
                "The in-person collection is not a physical scene on her presence.");
            foreach (var signedOut in outs.Where(r => r.Has("jerribeth.committed")).Take(1))
            {
                var due = Later(story, signedOut, 12);
                due.AvailableContacts.Add("417ce3dcf3a9707488f2b9b2a790814b");   // her presence has spawned in the market
                check(signedOut.Has("jerribeth.trickster.visit_due") && Rules.Available(story, visitScene, due), "The signed contract never gets its visit.");
                var visitPages = new HashSet<string>();
                var visitOuts = Program.Walk(visitScene, due, (page, _) => visitPages.Add(page));
                check(visitPages.Contains("arrival") && visitPages.Contains("threshold") && visitPages.Contains("morning")
                      && visitPages.Contains("ask") && visitPages.Contains("threshold_free") && visitPages.Contains("morning_free")
                      && visitOuts.All(r => r.Has("jerribeth.trickster.visited")),
                    "The visit has no staged threshold, or keeping your hands has no distinct outcome.");
                var noSpawn = Program.Copy(due); noSpawn.Flags.Add("jerribeth.presence.failed"); noSpawn.Hour += 96;
                check(Rules.Available(story, S("jerribeth.trickster.visit_letter"), noSpawn)
                      && !Rules.Available(story, S("jerribeth.trickster.visit_letter"), Later(story, due, 24)),
                    "No delayed letter when her presence cannot spawn, or it plays beside the visit.");
            }
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
                                               "jerribeth.guise", "jerribeth.invitation", "jerribeth.price", "jerribeth.question_late" }),
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
        var tenantState = World(story, 3, "trickster", "trickster.ever", "jerribeth.met", Dead, Returned, "jerribeth.trickster.cost.tenant",
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
        var endLodger = World(story, 6, "trickster", "trickster.ever", "jerribeth.met", Dead, Returned, "jerribeth.committed",
                              "jerribeth.trickster.cost.tenant", "jerribeth.trickster.cost.lodger", "jerribeth.trickster.cost.forfeit");
        var together = S("jerribeth.ending_together");
        check(Rules.Available(story, together, endLodger), "G6: the returned tenant has no ending.");
        check(together.Nodes.Where(n => n.Id == "earlier" || n.Id == "room").All(n => n.Paragraphs.Take(12).Count(p => Rules.ParagraphVisible(p, endLodger)) == 2),
            "Tenant paragraphs missing on her ending.");
        var late2 = World(story, 6, "trickster", "trickster.ever", "jerribeth.met", "jerribeth.attracted", "jerribeth.commission", "jerribeth.lovers");
        check(Rules.Available(story, epCommit, late2) && !Rules.Available(story, S("jerribeth.ending_unfinished"), late2),
            "Trk_Jerribeth_EpilogueCommit failed.");
        var refused = World(story, 6, "trickster", "trickster.ever", "jerribeth.met", "jerribeth.commission", "jerribeth.lovers", "jerribeth.closed",
                            "jerribeth.trickster.no_forfeit");
        var apart = S("jerribeth.ending_apart");
        check(!Rules.Available(story, epCommit, refused) && Rules.Available(story, apart, refused)
              && apart.Nodes[0].Paragraphs.Take(14).Count(p => Rules.ParagraphVisible(p, refused)) == 1, "Trk_Jerribeth_EpilogueCommit_Refused failed.");
        var deadNoReturn = World(story, 6, "trickster", "trickster.ever", "jerribeth.met", Dead, "jerribeth.commission", "jerribeth.lovers");
        check(!Rules.Available(story, epCommit, deadNoReturn), "The late commit brings a dead Jerribeth to the door.");
        var canon = World(story, 6, "jerribeth.met", "jerribeth.attracted");
        check(Rules.Available(story, S("jerribeth.ending_unfinished"), canon), "Off the path, the unfinished ending is lost.");

        // Reactions: Camellia and Woljif only.
        var reactions = story.Scenes.Where(s => s.Relationship == "jerribeth" && s.Reaction).ToArray();
        check(reactions.Length == 7 && reactions.All(r => r.Owner == "Camellia" || r.Owner == "Woljif"), "Jerribeth reactions changed.");
        var hostWorld = World(story, 3, "trickster", "trickster.ever", "jerribeth.met", Dead, Returned, "jerribeth.trickster.cost.host");
        check(Rules.Available(story, S("jerribeth.trickster.reaction.camellia_host"), hostWorld)
              && !Rules.Available(story, S("jerribeth.trickster.reaction.camellia"), hostWorld), "Camellia's host line misrouted.");
        var levyWorld = toastOut.Single(r => r.Has(Toasted));
        check(Rules.Available(story, S("jerribeth.trickster.reaction.woljif_levy"), levyWorld)
              && !Rules.Available(story, S("jerribeth.trickster.reaction.woljif"), levyWorld), "Woljif's levy line misrouted.");

        // --- Sol quality pass (2026-09-30) ----------------------------------------------------------------------------
        const string Forfeit = "jerribeth.trickster.cost.forfeit", Offered = "jerribeth.trickster.forfeit_named";
        const string Saw = "jerribeth.camellia_spectacle_heard", Taken = "trickster.lastcall.taken";
        string Words(Scene s) => string.Join(" ", s.Nodes.Select(n => SurfaceIds.Of(story, n)).Concat(s.Nodes.SelectMany(n => n.Paragraphs).Select(p => SurfaceIds.Of(story, p))));
        int Visible(Scene s, Snapshot w, string needle) =>
            s.Nodes.SelectMany(n => Rules.VisibleParagraphs(n, w)).Count(p => SurfaceIds.Has(SurfaceIds.Of(story, p), needle));
        bool Shown(Choice ch, Snapshot w) => Rules.Match(ch.Requires, ch.Forbids, w);

        // CAN: Camellia recalls her Sanctum remark only when the player heard it (SeenCues JerribetnFinal/Cue_0039).
        check(story.SeenCues.TryGetValue(Saw, out var sawCues) && sawCues.SequenceEqual(new[] { "f52f61f9f2ada7045a3b7f2f89350b95" }),
            "Camellia's Sanctum remark is not bound as a seen cue.");
        foreach (bool heard in new[] { false, true })
        foreach (bool host in new[] { false, true })
        {
            var w = World(story, 3, "trickster", "trickster.ever", "jerribeth.met", Dead, Returned);
            w.Flags.Add("camellia.trickster.returned");
            if (heard) w.Flags.Add(Saw);
            if (host) w.Flags.Add("jerribeth.trickster.cost.host");
            var open = reactions.Where(r => r.Owner == "Camellia" && Rules.Available(story, r, w)).ToList();
            check(open.Count == 1 && SurfaceIds.Has(Words(open[0]), "[jerribeth.trickster.reaction.camellia_saw/start][jerribeth.trickster.reaction.camellia_host_saw/start]") == heard && SurfaceIds.Has(Words(open[0]), "[jerribeth.trickster.host.taken/start][jerribeth.future/tenant_host][jerribeth.ending_together/earlier/paragraph/2][jerribeth.ending_together/room/paragraph/2][jerribeth.ending_ascended/earlier/paragraph/2][jerribeth.ending_ascended/room/paragraph/2][jerribeth.ending_apart/start/paragraph/2][jerribeth.trickster.dead.tenant/host_done][jerribeth.trickster.epilogue.commit/offer/paragraph/1][jerribeth.trickster.epilogue.commit/night_host][jerribeth.trickster.epilogue.commit/collected/paragraph/5][jerribeth.lastcall.page/page/paragraph/2][jerribeth.trickster.reaction.camellia_host/start][jerribeth.trickster.reaction.camellia_host_saw/start]") == host,
                "Camellia's reaction claims a Sanctum memory the player never heard, or misses the one they did (heard " + heard + ", host " + host + ").");
            foreach (var absent in new[] { "camellia.dead", "camellia.killed", "camellia.kicked_out" })
            {
                w.Flags.Add(absent);
                check(reactions.Where(r => r.Owner == "Camellia").All(r => !Rules.Available(story, r, w)),
                    "A Camellia reaction plays while she is absent, despite the legacy return flag: " + absent);
                w.Flags.Remove(absent);
            }
            check(Rules.Available(story, open[0], w), "A Camellia reaction stays hidden after her current absence clears.");
        }
        foreach (var r in reactions.Where(x => x.Owner == "Camellia"))
            check(!r.ForbidOverrides.ContainsKey("camellia.dead"),
                "A named Camellia reaction overrides her current death: " + r.Id);

        // CAN/BEL (Sol r0, r1): the tenant letter is a Drezen letter (Chapters 3, 5) or its Nexus twin (Chapter 4), never both.
        // At the Nexus the Golarion vessels are ordered and the host only promised; he is taken on the first Drezen rest of
        // Chapter 5 (host.taken), and no line claims his body before then.
        const string Nexus = "7847c3e3537104f4694167af0b9fcd0e", Promised = "jerribeth.trickster.host_promised", Host = "jerribeth.trickster.cost.host";
        var hostTaken = S("jerribeth.trickster.host.taken");
        foreach (var node in new[] { "statue_done", "locust_done" })
        foreach (var (chapter, area) in new[] { (3, Drezen), (4, Nexus), (5, Drezen) })
        {
            var w = Later(story, World(story, chapter, "trickster", "trickster.ever", "jerribeth.met", Dead, Primed, "jerribeth.xanthir_known"), 48);
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
                check(!cancelled.Has(Forfeit) && Rules.Available(story, apart, end) && Visible(apart, end, "[jerribeth.ending_together/earlier/paragraph/10][jerribeth.ending_together/earlier/paragraph/11][jerribeth.ending_together/room/paragraph/10][jerribeth.ending_together/room/paragraph/11][jerribeth.ending_ascended/earlier/paragraph/10][jerribeth.ending_ascended/earlier/paragraph/11][jerribeth.ending_ascended/room/paragraph/10][jerribeth.ending_ascended/room/paragraph/11][jerribeth.ending_apart/start/paragraph/10][jerribeth.ending_apart/start/paragraph/11][jerribeth.ending_apart/start/paragraph/12][jerribeth.trickster.epilogue.commit/offer/paragraph/0][jerribeth.trickster.epilogue.commit/offer/paragraph/1][jerribeth.trickster.epilogue.commit/offer/paragraph/2][jerribeth.trickster.epilogue.commit/collected/paragraph/13][jerribeth.trickster.epilogue.commit/collected/paragraph/14][jerribeth.lastcall.page/page/paragraph/1]") == 0,
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
                ? Rules.VisibleParagraphs(s.Nodes.Single(n => n.Id == (s.Id == "jerribeth.lastcall.page" ? "page" : s.Id == "jerribeth.ending_apart" ? "start" : "earlier")), w).Count(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[jerribeth.future/her_terms/choice/0][jerribeth.future/her_terms/choice/3][jerribeth.future/her_terms_short/choice/0][jerribeth.future/her_terms_short/choice/3][jerribeth.future/grudge][jerribeth.future/grudge_short][jerribeth.future/arrival_terms][jerribeth.future/morning][jerribeth.future/tenant_morning][jerribeth.future/arrival_note][jerribeth.ending_together/earlier/paragraph/10][jerribeth.ending_together/earlier/paragraph/11][jerribeth.ending_together/room/paragraph/10][jerribeth.ending_together/room/paragraph/11][jerribeth.ending_ascended/earlier/paragraph/10][jerribeth.ending_ascended/earlier/paragraph/11][jerribeth.ending_ascended/room/paragraph/10][jerribeth.ending_ascended/room/paragraph/11][jerribeth.ending_apart/start/paragraph/10][jerribeth.ending_apart/start/paragraph/11][jerribeth.ending_apart/start/paragraph/12][jerribeth.trickster.dead.setup_final/lease][jerribeth.trickster.dead.backdated/signed][jerribeth.trickster.epilogue.commit/offer/paragraph/0][jerribeth.trickster.epilogue.commit/offer/paragraph/1][jerribeth.trickster.epilogue.commit/offer/paragraph/2][jerribeth.trickster.epilogue.commit/night_after][jerribeth.trickster.epilogue.commit/night_mind_after][jerribeth.trickster.epilogue.commit/collected/paragraph/13][jerribeth.trickster.epilogue.commit/collected/paragraph/14][jerribeth.trickster.epilogue.commit/torn][jerribeth.trickster.epilogue.commit/torn_mind][jerribeth.lastcall.page/page/paragraph/1][jerribeth.trickster.visit/arrival_terms][jerribeth.trickster.visit/morning][jerribeth.trickster.visit_letter/start][book/trickster.ledger/owed.jerribeth]")) : 0;
            int collections = OnPage(together) + OnPage(ascended) + OnPage(lcPage);
            check(Rules.Available(story, together, w) && collections == 1,
                "The single forfeit is collected " + collections + " times (Last Call " + lastCall + ", vessel '" + vessel + "').");
            if (!lastCall) continue;
            check(Rules.Available(story, lcPage, w), "The committed coda is missing on Last Call.");
            check((Visible(lcPage, w, "[jerribeth.ending_together/earlier/paragraph/0][jerribeth.ending_together/room/paragraph/0][jerribeth.ending_ascended/earlier/paragraph/0][jerribeth.ending_ascended/room/paragraph/0][jerribeth.ending_apart/start/paragraph/0][jerribeth.trickster.epilogue.commit/collected/paragraph/3][jerribeth.lastcall.page/page/paragraph/3]") == 1) == (vessel == "jerribeth.trickster.body.statue"),
                "The Last Call idol ignores the vessel she chose: '" + vessel + "'.");
            check((Visible(lcPage, w, "[jerribeth.lastcall.page/page/paragraph/0]") > 0) == (vessel != ""), "Last Call charges rent to a Jerribeth who is no tenant.");
        }
        // The call-in answers what she is: a tenant, a toasted stranger, or a living demon holding a forfeit. One line each.
        var callIn = S("jerribeth.lastcall.call");
        foreach (var deal in new[] { new[] { "jerribeth.trickster.cost.tenant", "jerribeth.trickster.cost.lodger" },
                                     new[] { "jerribeth.trickster.cost.tenant", "jerribeth.trickster.cost.host", Forfeit },
                                     new[] { "jerribeth.trickster.cost.toast", Forfeit }, new[] { Forfeit } })
        {
            var w = World(story, 6, deal.Concat(new[] { "trickster", "trickster.ever" }).ToArray());
            var lines = callIn.Nodes[0].Choices.Where(ch => Shown(ch, w)).ToList();
            bool tenantDeal = deal.Contains("jerribeth.trickster.cost.tenant");
            check(lines.Count == 1,
                "The Last Call call-in assumes every deal made her a skull tenant: " + string.Join(",", deal));
        }

        // BEL: the late commit is staged by what she is, has its own intimate threshold (cut at the start of the act) and a
        // morning, and keeps a nonsexual refusal. The tenant with no body never knocks, and the host never lends his body.
        foreach (var vessel in new[] { "", "jerribeth.trickster.cost.host", "jerribeth.trickster.cost.lodger", "jerribeth.trickster.body.statue", "jerribeth.trickster.body.locust" })
        {
            // eng7-l13: positive new late act uses current power, not history alone.
            var flags = new List<string> { "trickster", "trickster.ever", "jerribeth.met", "jerribeth.attracted", "jerribeth.commission", "jerribeth.lovers" };
            if (vessel != "") flags.AddRange(new[] { Dead, Returned, "jerribeth.trickster.cost.tenant", vessel });
            var w = World(story, 6, flags.ToArray());
            check(Rules.Available(story, epCommit, w), "The late commit is missing for vessel '" + vessel + "'.");
            var pages = new HashSet<string>();
            var outs = Program.Walk(epCommit, w, (page, _) =>
            {
                pages.Add(page);
                // Round 2 compiles partner choices into ending-local pages.
                // Preserve modality coverage without requiring persistent flags.
                if (page.StartsWith("late_local_", StringComparison.Ordinal)
                    && page.Length > 22 && page[^11] == '_')
                    pages.Add(page.Substring(11, page.Length - 22));
            });
            bool mind = vessel != "" && vessel != "jerribeth.trickster.cost.host";
            check(epCommit.Nodes[0].Paragraphs.Take(3).Count(p => Rules.ParagraphVisible(p, w)) == 1
                  && Rules.VisibleParagraphs(epCommit.Nodes.Single(n => n.Id == "collected"), w).Count(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[jerribeth.trickster.epilogue.commit/collected/paragraph/0][jerribeth.trickster.epilogue.commit/collected/paragraph/1][jerribeth.trickster.epilogue.commit/collected/paragraph/2]")) == 1,
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
                var next = Rules.MailbagArrivals(story, s).FirstOrDefault(x => x.Relationship == "jerribeth");
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
        check(!Rules.Available(story, visitor, ch5), "Woljif reports a visit that has not happened.");
        var atStall = Later(story, ch5, 12); atStall.AvailableContacts.Add("417ce3dcf3a9707488f2b9b2a790814b");
        check(Rules.Available(story, S("jerribeth.trickster.visit"), atStall), "The living contract's visit never plays.");
        ch5 = Program.Walk(S("jerribeth.trickster.visit"), atStall).First(r => r.Has("jerribeth.trickster.visited"));
        check(!ch5.Has(Returned) && !ch5.Has(Toasted) && Rules.Available(story, visitor, ch5)
              && reactions.Where(r => r != visitor).All(r => !Rules.Available(story, r, ch5)),
            "The living contract has no companion reaction, or a device reaction plays beside it.");
        check(SurfaceIds.Has(Words(visitor), "[jerribeth.trickster.reaction.woljif_visitor/start]") && SurfaceIds.Has(Words(visitor), "[jerribeth.trickster.reaction.woljif_visitor/start]"), "Woljif's line does not address the visitor or the pledged memory.");
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
            var firstHome = Later(story, home5, 48);
            check(!isDead || Rules.MailbagArrivals(story, firstHome).FirstOrDefault(x => x.Relationship == "jerribeth")?.Id == "jerribeth.trickster.host.taken",
                "The promised host is not taken on the first Drezen rest.");
            var (end5, ch5Tail) = Deliver(home5, 40);
            check(end5.Has("jerribeth.committed") && end5.Has("jerribeth.fate_terms") && ch5Tail.Count(x => !Device(x)) <= 8
                  && (!isDead || ch5Tail.Contains("jerribeth.trickster.host.taken") && end5.Has(Host) && ch5Tail.Count(Device) <= 2),
                "The delayed correspondence does not finish in Chapter 5 within its allowance: " + string.Join(",", ch5Tail));
        }

        // --- Sol round 2 -----------------------------------------------------------------------------------------------
        // CAN: the late commit dates itself by Threshold, never by a Wound that may have become the Crossroads.
        check(SurfaceIds.Has(Words(epCommit), "[jerribeth.trickster.epilogue.commit/offer]"), "The late commit claims the Wound closed.");

        // VOI: the kept hands are a challenge she prices (the scale is a loan), set up by the scale the Commander took.
        var freeMorning = SurfaceIds.Of(story, future.Nodes.Single(n => n.Id == "morning_free"));
        check(SurfaceIds.Has(freeMorning, "[jerribeth.future/morning_free]"),
            "The free-hands morning is an exceptional-lover line instead of a bargain over the scale.");

        // BEL: the tenant's payoff cites the single instalment taken when the lease was signed, never months of rent.
        foreach (var primer in new[] { greeting, final, backdated })
            check(SurfaceIds.Has(Words(primer), "[jerribeth.trickster.dead.setup_greeting/lease][jerribeth.trickster.dead.setup_final/accepted][jerribeth.trickster.dead.backdated/signed]"), "A lease is signed without its first instalment: " + primer.Id);
        check(SurfaceIds.Has(Words(tenant), "[jerribeth.trickster.dead.tenant/tenant]") && SurfaceIds.Has(Words(tenantNexus), "[jerribeth.trickster.dead.tenant_nexus/tenant]"), "The tenant's payoff cites rent that was never paid.");

        // BEL: each toast device keeps its own carrier through the invitation and the ending.
        const string Levy = "jerribeth.trickster.toast_levy", ToastHost = "jerribeth.trickster.cost.toast_host";
        const string Grudge = "jerribeth.trickster.cost.toast_grudge", Interest = "jerribeth.trickster.cost.toast_interest";
        foreach (bool levy in new[] { false, true })
        {
            var toastSource = levy ? toast : king;
            var toastStart = levy ? World(story, 5, "trickster") : World(story, 5, "trickster", "fool_king.crowned");
            var met = Program.Walk(toastSource, toastStart).Single(r => r.Has(Toasted));
            check(met.Has(Levy) == levy, "The toast device does not record its carrier.");
            var pagesSeen = new List<string>();
            var invOuts = Program.Walk(invitation, Later(story, met, 24), (page, _) => pagesSeen.Add(page));
            check(pagesSeen.Contains(levy ? "toast_price_levy" : "toast_price") && !pagesSeen.Contains(levy ? "toast_price" : "toast_price_levy"),
                "The toast carrier changes between the toast and the invitation (levy " + levy + ").");
            var given = invOuts.First(r => r.Has(ToastHost) && r.Has(invitation.Id));
            var end = World(story, 6, given.Flags.Concat(new[] { "jerribeth.committed" }).ToArray());
            var ending = together.Nodes.Single(n => n.Id == "earlier");
            var hostLines = Rules.VisibleParagraphs(ending, end).Where(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[jerribeth.ending_together/earlier/paragraph/6][jerribeth.ending_together/earlier/paragraph/7][jerribeth.ending_together/room/paragraph/6][jerribeth.ending_together/room/paragraph/7]")).ToList();
            check(hostLines.Count == 1,
                "The ending remembers the wrong toast carrier (levy " + levy + ").");
            // INT: the refused toast is charged to the future and collected, visibly, before any promise; refusing to pay ends it.
            check(invOuts.Any(r => r.Has(Grudge) && !r.Has(ToastHost) && !r.Has("jerribeth.trickster.cost.toast_memory")), "The refused toast records no grudge.");
        }
        foreach (string branch in new[] { "jerribeth.settlement_kept", "jerribeth.short_future_requested" })
        {
            var w = World(story, 5, "trickster", "jerribeth.trickster.met_by_toast", "jerribeth.commission", "jerribeth.lovers", branch, Grudge);
            var pagesSeen = new HashSet<string>();
            var outs = Program.Walk(future, w, (page, _) => pagesSeen.Add(page));
            check(pagesSeen.Contains(branch.EndsWith("settlement_kept") ? "grudge" : "grudge_short")
                  && pagesSeen.Contains(branch.EndsWith("settlement_kept") ? "interest" : "interest_short"), "The toast's interest is not demanded and collected on the page.");
            check(outs.Where(r => r.Has("jerribeth.committed")).All(r => r.Has(Interest)) && outs.Any(r => r.Has("jerribeth.committed")),
                "A promise is accepted before the toast's interest is paid.");
            var refusedPay = outs.Where(r => r.Has("jerribeth.closed") && !r.Has(Interest) && !r.Has("jerribeth.trickster.no_forfeit")).ToList();
            check(refusedPay.Count > 0, "Refusing to pay the interest has no exit.");
            var apartEnd = World(story, 6, refusedPay[0].Flags.ToArray());
            check(Rules.Available(story, apart, apartEnd) && Visible(apart, apartEnd, "[jerribeth.ending_apart/start/paragraph/13]") == 1, "The unpaid toast has no consequence.");
            var plain = Program.Copy(w); plain.Flags.Remove(Grudge);
            var plainPages = new HashSet<string>();
            Program.Walk(future, plain, (page, _) => plainPages.Add(page));
            check(!plainPages.Contains("grudge") && !plainPages.Contains("grudge_short"), "She charges interest on a toast that was paid.");
        }

        // COX (Sol r2): every fresh start stays within the letter allowances. Core letters: Ch3 <= 8, Ch4 <= 3 with the
        // device letters, Ch5 <= 8; device letters: Ch3 <= 2, Ch5 <= 2. A late (Chapter 5) start folds the ordinary evening
        // and the farewell into the promise, and the Xanthir talk rides inside price when the Commander knows of it.
        foreach (string kind in new[] { "met", "returned", "toasted" })
        foreach (int startCh in new[] { 3, 4, 5 })
        foreach (bool knows in new[] { false, true })
        {
            if (kind == "toasted" && startCh != 5) continue;
            var flags = new List<string> { "trickster" };
            if (kind != "toasted") flags.Add("jerribeth.met");
            if (kind == "returned") flags.AddRange(new[] { Dead, Primed });
            if (knows) flags.AddRange(new[] { "jerribeth.xanthir_known", "jerribeth.wintersun_known" });
            var s0 = World(story, startCh, flags.ToArray());
            if (startCh == 4) s0.Area = Nexus;
            var counts = new Dictionary<(int, bool), int>();
            var all = new List<string>();
            for (int chapter = startCh; chapter <= 5; chapter++)
            {
                s0.Chapter = chapter;
                s0.Area = chapter == 4 ? Nexus : Drezen;
                var (after, got) = Deliver(s0, 60);
                foreach (var id in got) counts[(chapter, Device(id))] = counts.TryGetValue((chapter, Device(id)), out var k) ? k + 1 : 1;
                all.AddRange(got);
                s0 = after;
            }
            int C(int ch, bool dev) => counts.TryGetValue((ch, dev), out var v) ? v : 0;
            string label = kind + " from Ch" + startCh + (knows ? " with knowledge" : "") + ": " + string.Join(",", all);
            check(C(3, false) <= 8 && C(5, false) <= 8 && C(4, false) + C(4, true) <= 3 && C(3, true) <= 2 && C(5, true) <= 2,
                "A fresh start breaks a letter allowance, " + label);
            check(s0.Has("jerribeth.committed") && s0.Has("jerribeth.fate_terms"), "A fresh start does not reach the promise, " + label);
            check(kind == "toasted" || s0.Has("jerribeth.farewell_kept"), "A fresh start never says farewell, " + label);
            check(!all.Contains("jerribeth.collection") && s0.Has("jerribeth.collection") == (knows && kind != "toasted"), "The Xanthir talk is a separate letter, or lost, " + label);
            bool isLate = startCh == 5 && kind != "toasted";
            check(s0.Has("jerribeth.late_start") == (startCh == 5 && kind == "met" || startCh == 5 && kind == "returned")
                  && (!isLate || !all.Contains("jerribeth.ordinary") && !all.Contains("jerribeth.farewell") && s0.Has("jerribeth.ordinary")),
                "The late start is not folded into the promise, " + label);
        }

        // --- Sol round 3 -----------------------------------------------------------------------------------------------
        // CAN: the locust vessel needs the pinning the Commander actually saw (JerribetnFinal/Cue_0001, xanthir_known). A
        // greeting-stage kill never saw it; a final-stage kill did.
        foreach (var device in new[] { tenant, tenantNexus })
        {
            var locust = device.Nodes.Single(n => n.Id == "house").Choices[1];
            var greetingKill = World(story, 3, "trickster", "trickster.ever", "jerribeth.met", Dead, Primed, "jerribeth.trickster.attack_bored");
            var finalKill = World(story, 3, "trickster", "trickster.ever", "jerribeth.met", Dead, Primed, "jerribeth.trickster.attack_final", "jerribeth.xanthir_known");
            check(greetingKill.Has("jerribeth.killed_by_commander") && !Shown(locust, greetingKill) && Shown(locust, finalKill)
                  && device.Nodes.Single(n => n.Id == "house").Choices.Count(ch => Shown(ch, greetingKill)) == 4,
                "The locust vessel assumes a pinning the Commander never saw: " + device.Id);
        }

        // BEL: the late commit opens on a lease only for a tenant; other histories open on the unfinished correspondence.
        foreach (var (label2, extra) in new[] { ("living", new string[0]), ("toasted", new[] { Toasted }),
                                                ("lodger", new[] { Dead, Returned, "jerribeth.trickster.cost.tenant", "jerribeth.trickster.cost.lodger" }),
                                                ("host", new[] { Dead, Returned, "jerribeth.trickster.cost.tenant", Host }) })
        {
            var w = World(story, 6, new[] { "trickster", "trickster.ever", "jerribeth.attracted", "jerribeth.commission", "jerribeth.lovers" }
                .Concat(label2 == "toasted" ? new string[0] : new[] { "jerribeth.met" }).Concat(extra).ToArray());
            check(Rules.Available(story, epCommit, w), "The late commit is missing for " + label2);
            var offer = epCommit.Nodes[0];
            string text = SurfaceIds.Of(story, offer) + " " + string.Join(" ", Rules.VisibleParagraphs(offer, w).Select(p => SurfaceIds.Of(story, p)));
            bool tenantHistory = label2 == "lodger" || label2 == "host";
            check(SurfaceIds.Has(text, "[jerribeth.trickster.epilogue.commit/offer/paragraph/1][jerribeth.trickster.epilogue.commit/offer/paragraph/2]") == tenantHistory && SurfaceIds.Has(text, "[jerribeth.trickster.epilogue.commit/offer/paragraph/0]") == !tenantHistory, "The late commit's opening claims the wrong history for " + label2 + ": " + text);
        }

        // COX + HOW (R2-6): the late history (commission reached, no campaign commitment) has its Last Call coda; a parted or
        // declined history has none, and the committed history does not read the late line.
        var lateLc = World(story, 6, "trickster", "trickster.ever", "jerribeth.met", "jerribeth.commission", "jerribeth.lovers", Taken, "ending.trickster");
        check(lateLc.Has("jerribeth.trickster.late_committed") && lateLc.Has("lastcall.active") && Rules.Available(story, epCommit, lateLc)
              && Rules.Available(story, lcPage, lateLc) && Visible(lcPage, lateLc, "[jerribeth.lastcall.page/page/paragraph/5]") == 1,
            "The late-commit history has no Last Call coda, or the coda claims a signed contract.");
        foreach (var guard in new[] { "jerribeth.trickster.parted", "jerribeth.trickster.declined" })
        {
            var guarded = Program.Copy(lateLc); guarded.Flags.Add(guard);
            check(!Rules.Available(story, lcPage, guarded), "Last Call plays for a history that ended: " + guard);
        }
        var committedLc = Program.Copy(lateLc); committedLc.Flags.Add("jerribeth.committed");
        check(Rules.Available(story, lcPage, committedLc) && Visible(lcPage, committedLc, "[jerribeth.lastcall.page/page/paragraph/5]") == 0, "The committed coda reads the late line.");
        check(story.Scenes.Where(s => s.Relationship == "jerribeth").SelectMany(s => s.Nodes).SelectMany(n => n.Choices)
                .Where(ch => ch.Set.Contains("jerribeth.closed")).All(ch => ch.Set.Contains("jerribeth.trickster.parted")),
            "An answer closes the relationship without recording parted.");
    }
}
